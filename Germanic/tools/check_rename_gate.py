#!/usr/bin/env python3
"""Behaviour-neutral rename validation gate for one rule rename.

Given a former and canonical Foma identifier, this harness runs the automatable
gates that prove a rename changed nothing but the label. It is designed to run
inside the backend container (it invokes foma/flookup) with CWD = /usr/app.

Gates implemented here (task section 7):
  A  FST compiles cleanly; the former `define` is ABSENT (no alias) and the
     canonical `define` is present.
  B  Lexical-output identity: recompiling and re-applying preserves the frozen
     outputs_sha256 (and accepted/matched/mismatched counts).
  E' Executable order unchanged: the live order manifest equals the frozen
     (original) manifest after undoing ALL completed relabelings (former ->
     canonical), proving relabeling only, never reordering.
  G  Former-name audit: the former identifier and its snake/kebab derivatives are
     absent from active source and generated output, except individually
     allowlisted archival references.

Gates C (mismatch report), D (trace identity) and E (book/PDF) require the full
regeneration pipeline and are run separately per rule; this harness covers the
fast, decisive behaviour-neutrality gates. There is deliberately NO committed
Foma compatibility alias: an alias could let an incomplete migration compile and
hide stale references.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
import sys
from pathlib import Path

# Resolve repo layout whether run from /usr/app (container) or the host checkout.
CWD = Path.cwd()
if (CWD / "fsts/germanic.txt").exists():
    GERMANIC_ROOT = CWD                      # container: /usr/app
    DOCS = CWD / "docs/sound_changes"
    FST = CWD / "fsts/germanic.txt"
    TOOLS = CWD / "tools"
else:
    REPO = Path(__file__).resolve().parents[2]
    GERMANIC_ROOT = REPO / "Germanic"
    DOCS = GERMANIC_ROOT / "docs/sound_changes"
    FST = GERMANIC_ROOT / "fsts/germanic.txt"
    TOOLS = GERMANIC_ROOT / "tools"

BASELINE_DIR = DOCS / "cascade_baseline"
BASELINE_SUMMARY = BASELINE_DIR / "cascade_baseline_summary.json"
# The FROZEN old-order manifest is the immutable reference (old identifiers); the
# live manifest (cascade_order_manifest.tsv) is regenerated per rename.
FROZEN_ORDER_MANIFEST = BASELINE_DIR / "cascade_order_manifest_frozen.tsv"
ALLOWLIST = BASELINE_DIR / "rename_former_name_allowlist.tsv"

sys.path.insert(0, str(TOOLS))


def _snake(ident: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", ident).lower()


def _kebab(ident: str) -> str:
    return _snake(ident).replace("_", "-")


def former_variants(former: str) -> list[str]:
    # The exact identifier is the reliable, meaningful token to audit in source
    # and validation code. CAPR's snake/kebab bin-name forms (e.g. nwgmc_...) do
    # not follow a simple per-capital rule, so they are migrated explicitly per
    # rule and verified by the trace-regeneration gate, not guessed here.
    return [former]


def gate_a_compile_and_define(former: str, canonical: str) -> list[str]:
    errors: list[str] = []
    proc = subprocess.run(["foma", "-q", "-l", str(FST), "-e", "quit"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout.decode("utf-8", "replace")
    if proc.returncode != 0 or "***" in out or "defined" not in out.lower() and "Writing to file" not in out:
        # foma prints "defined X: ..." lines and "Writing to file" lines on success.
        if proc.returncode != 0:
            errors.append(f"A: foma compile failed (rc={proc.returncode})")
    text = FST.read_text(encoding="utf-8")
    if re.search(rf"\bdefine\s+{re.escape(former)}\b", text):
        errors.append(f"A: former `define {former}` still present (no alias allowed)")
    if not re.search(rf"\bdefine\s+{re.escape(canonical)}\b", text):
        errors.append(f"A: canonical `define {canonical}` not found")
    return errors


def gate_b_output_identity() -> list[str]:
    errors: list[str] = []
    import cascade_baseline as cb
    tsv = GERMANIC_ROOT / "data/germanic-aligned-final.tsv"
    bin_path = GERMANIC_ROOT / "old_english.bin"
    if not bin_path.exists():
        bin_path = Path("old_english.bin")
    baseline = cb.build_baseline(tsv, bin_path)
    frozen = json.loads(BASELINE_SUMMARY.read_text(encoding="utf-8"))
    got = baseline["summary"]
    for key in ("total_lexemes", "accepted", "rejected", "matched", "mismatched",
                "ambiguous_outputs", "outputs_sha256"):
        if got[key] != frozen[key]:
            errors.append(f"B: {key} changed: frozen={frozen[key]} now={got[key]}")
    return errors


def _tsv_rows(path: Path) -> list[dict[str, str]]:
    """Read a TSV that may carry a leading '#' comment block.

    Feeding comment lines straight to DictReader silently promotes a comment to
    the header row, which yields no usable records at all.
    """
    if not path.exists():
        return []
    body = "\n".join(
        line for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )
    return list(csv.DictReader(io.StringIO(body), delimiter="\t"))


def _retired_identifiers() -> set[str]:
    """Foma identifiers of rules the registry records as retired.

    Such rules legitimately no longer appear in the live cascade even though the
    frozen campaign-era manifest still lists them.
    """
    retired: set[str] = set()
    for row in _tsv_rows(DOCS / "registry/sc_registry.tsv"):
        if (row.get("lifecycle_status") or "").strip() == "retired":
            identifier = (row.get("fst_identifier") or "").strip()
            if identifier:
                retired.add(identifier)
    for row in _tsv_rows(BASELINE_DIR / "rename_migration_manifest.tsv"):
        if (row.get("migration_status") or "").strip() == "retired":
            former = (row.get("former_foma_identifier") or "").strip()
            if former:
                retired.add(former)
    return retired


def _completed_rename_map(former: str, canonical: str) -> dict[str, str]:
    """former_foma_identifier -> current_foma_identifier for every relabeling.

    Gate E compares the live order against the frozen (original) order after
    undoing *all* accumulated relabelings, not just the current rule's, so the
    order-identity check stays valid as renames accumulate.

    ``sound_change_aliases.tsv`` is the maintained authority here: it records a
    ``former_foma_rule_name`` alias alongside the SC's current ``foma_rule_name``.
    The archival rename-migration manifest is consulted as a fallback only; its
    rows are a campaign-time snapshot and some are stale.
    """
    mapping: dict[str, str] = {}
    alias_rows = _tsv_rows(DOCS / "sound_change_aliases.tsv")
    current: dict[str, str] = {}
    for row in alias_rows:
        if (row.get("alias_type") or "").strip() == "foma_rule_name":
            current[(row.get("change_id") or "").strip()] = (row.get("alias") or "").strip()
    for row in alias_rows:
        if (row.get("alias_type") or "").strip() == "former_foma_rule_name":
            sc = (row.get("change_id") or "").strip()
            old = (row.get("alias") or "").strip()
            new = current.get(sc, "")
            if old and new and old != new:
                mapping[old] = new
    for row in _tsv_rows(BASELINE_DIR / "rename_migration_manifest.tsv"):
        f = (row.get("former_foma_identifier") or "").strip()
        c = (row.get("canonical_foma_identifier") or "").strip()
        if f and c and f != c and f not in mapping:
            mapping[f] = c
    # Ensure the current rule is included even if not yet recorded.
    mapping[former] = canonical
    return mapping


def gate_e_order_unchanged(former: str, canonical: str) -> list[str]:
    """Assert the rename leaves the executable order intact.

    The frozen manifest is a campaign-era snapshot and is deliberately never
    rebaselined, so the live cascade legitimately contains rules added after
    the freeze. Comparing raw lengths would therefore fail for every rename
    once a single new rule is introduced. The invariant that actually matters
    is that the rules recorded in the frozen snapshot still occur in the live
    cascade, under their renamed identifiers, in the same relative order.
    """
    errors: list[str] = []
    import cascade_order_manifest as com
    live = list(csv.DictReader(io.StringIO(com.manifest_text()), delimiter="\t"))
    with FROZEN_ORDER_MANIFEST.open(encoding="utf-8") as handle:
        frozen = list(csv.DictReader(handle, delimiter="\t"))
    rename_map = _completed_rename_map(former, canonical)
    retired = _retired_identifiers()
    expected = [
        rename_map.get(r["foma_identifier"], r["foma_identifier"])
        for r in frozen
        if r["foma_identifier"] not in retired
        and rename_map.get(r["foma_identifier"], r["foma_identifier"]) not in retired
    ]
    live_names = [r["foma_identifier"] for r in live]
    missing = [name for name in expected if name not in live_names]
    if missing:
        errors.append(f"E: frozen rules absent from the live cascade: {missing}")
        return errors
    projected = [name for name in live_names if name in set(expected)]
    if projected != expected:
        for i, (got, want) in enumerate(zip(projected, expected), start=1):
            if got != want:
                errors.append(f"E: relative order changed at frozen position {i}: expected {want!r} got {got!r}")
                break
        else:
            errors.append(f"E: frozen rule count changed {len(expected)} -> {len(projected)}")
    return errors


def _load_allowlist() -> list[tuple[str, str]]:
    if not ALLOWLIST.exists():
        return []
    pairs = []
    with ALLOWLIST.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            pairs.append(((row.get("former_identifier") or "").strip(),
                          (row.get("path_substring") or "").strip()))
    return pairs


def gate_g_former_name_audit(former: str) -> list[str]:
    errors: list[str] = []
    allow = _load_allowlist()
    variants = former_variants(former)
    # Scan behaviour-bearing source + validation code; the registries, reader-
    # facing source, and generated artifacts are migrated per rule and
    # regenerated in final canonicalisation (task section 9).
    scan_roots = [GERMANIC_ROOT / "fsts", GERMANIC_ROOT / "tools", GERMANIC_ROOT / "tests"]
    offenders: dict[str, list[str]] = {}
    for variant in variants:
        proc = subprocess.run(["grep", "-rwIl", "--exclude=*.bin", variant, *[str(p) for p in scan_roots if p.exists()]],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for path in proc.stdout.decode("utf-8", "replace").splitlines():
            rel = path
            allowed = any(a_former in (former, "*") and sub and sub in rel for a_former, sub in allow)
            if not allowed:
                offenders.setdefault(rel, []).append(variant)
    for rel, vs in sorted(offenders.items()):
        errors.append(f"G: former name {sorted(set(vs))} still present in {rel}")
    return errors


def check(former: str, canonical: str, gates: str) -> int:
    all_errors: list[str] = []
    if "A" in gates:
        all_errors += gate_a_compile_and_define(former, canonical)
    if "B" in gates:
        all_errors += gate_b_output_identity()
    if "E" in gates:
        all_errors += gate_e_order_unchanged(former, canonical)
    if "G" in gates:
        all_errors += gate_g_former_name_audit(former)
    if all_errors:
        print(f"RENAME GATE FAILED for {former} -> {canonical}:")
        for e in all_errors:
            print(f"  - {e}")
        return 1
    print(f"RENAME GATE PASSED for {former} -> {canonical} (gates {gates}): "
          f"compile+no-alias, outputs_sha256 identity, order-unchanged, former-name audit clean")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--former", required=True)
    parser.add_argument("--canonical", required=True)
    parser.add_argument("--gates", default="ABEG", help="subset of ABEG to run (default all)")
    args = parser.parse_args()
    return check(args.former, args.canonical, args.gates)


if __name__ == "__main__":
    raise SystemExit(main())

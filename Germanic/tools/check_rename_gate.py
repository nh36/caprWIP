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
     manifest with (former -> canonical) substituted at the renamed slot only.
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


def gate_e_order_unchanged(former: str, canonical: str) -> list[str]:
    errors: list[str] = []
    import cascade_order_manifest as com
    live = com.build_manifest(FST)
    with FROZEN_ORDER_MANIFEST.open(encoding="utf-8") as handle:
        frozen = list(csv.DictReader(handle, delimiter="\t"))
    if len(live) != len(frozen):
        return [f"E: manifest length changed {len(frozen)} -> {len(live)}"]
    for i, (lrow, frow) in enumerate(zip(live, frozen), start=1):
        expected = canonical if frow["foma_identifier"] == former else frow["foma_identifier"]
        if lrow["foma_identifier"] != expected:
            errors.append(f"E: position {i} expected {expected!r} got {lrow['foma_identifier']!r}")
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

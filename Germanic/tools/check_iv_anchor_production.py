#!/usr/bin/env python3
"""Strict Stage 2 production parity check for IV anchors.

Canonical production Markdown now uses generated `.iv-anchor` block markers for
all non-explicit (heading/line) emissions. Legacy raw mode remains available
only as a parity fixture.

This checker verifies:
1. plan coverage and integrity;
2. raw-vs-anchor rendering trace equality (full emission records);
3. canonical Markdown anchor representation and ordering;
4. ordered command-sequence parity through real Pandoc/Lua runs;
5. narrowly scoped TeX normalization equality.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FILTER_LUA = REPO_ROOT / "Germanic/tools/index_verborum_filter.lua"
BOOK_EMISSIONS_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_book_emissions.tsv"
PRINT_MAIN_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
LANGUAGE_REGISTRY_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
VARIETY_REGISTRY_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_varieties.tsv"
EXPLICIT_PLAN_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_book_explicit_plan.tsv"
CANONICAL_MD = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"

EXPECTED_NON_EXPLICIT = 448
EXPECTED_TOTAL = 1865
EXPECTED_UNIQUE = 828

sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))
from build_capr_book_draft import build_book_markdown
from build_capr_book_draft import BookEmission


def _pandoc_available() -> bool:
    return subprocess.run(["pandoc", "--version"], capture_output=True).returncode == 0


def _extract_iv_commands(text: str) -> list[str]:
    cmds = []
    for m in re.finditer(r"\\index\[iv\]\{", text):
        pos = m.end()
        depth = 1
        end = pos
        while end < len(text) and depth > 0:
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
            end += 1
        cmds.append(r"\index[iv]{" + text[m.end():end - 1] + "}")
    return cmds


def _run_pandoc(md_text: str, tmp_dir: Path, label: str) -> str:
    env = dict(os.environ)
    env.update({
        "CAPR_IV_PRINT_MAIN_TSV": str(PRINT_MAIN_TSV),
        "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS_TSV),
        "CAPR_IV_EXPLICIT_PLAN_TSV": str(EXPLICIT_PLAN_TSV),
        "CAPR_IV_EXPLICIT_MODE": "legacy",
        "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(LANGUAGE_REGISTRY_TSV),
        "CAPR_IV_VARIETY_REGISTRY_TSV": str(VARIETY_REGISTRY_TSV),
    })
    src = tmp_dir / f"{label}.md"
    src.write_text(md_text, encoding="utf-8")
    proc = subprocess.run(
        ["pandoc", str(src), "--from", "markdown+raw_tex", "--to", "latex",
         "--lua-filter", str(FILTER_LUA)],
        capture_output=True, text=True, env=env, cwd=str(REPO_ROOT),
    )
    if proc.returncode != 0:
        print(f"pandoc failed ({label}):\n{proc.stderr[:600]}", file=sys.stderr)
        sys.exit(1)
    return proc.stdout


def _load_plan_ordered() -> list[tuple[str, str]]:
    """Return ordered (emission_id, emission_path) list from canonical plan."""
    import csv
    with BOOK_EMISSIONS_TSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    out: list[tuple[str, str]] = []
    for r in rows:
        path = (r.get("emission_path") or "").strip()
        eid = (r.get("emission_id") or "").strip()
        if path in ("heading_injection", "line_injection"):
            out.append((eid, path))
    return out


def _narrow_tex_normalize(tex: str) -> str:
    """Narrowly normalize TeX around standalone index-command blank lines.

    Allowed normalization:
    - strip trailing horizontal whitespace
    - collapse blank lines immediately before/after a line that is exactly an
      ``\index[iv]{...}`` command to a single canonical layout

    Not allowed:
    - broad blank-line collapsing elsewhere
    - prose/heading/citation/macro normalization
    """
    raw_lines = [ln.rstrip() for ln in tex.splitlines()]
    norm: list[str] = []
    i = 0
    n = len(raw_lines)
    cmd_re = re.compile(r"^\\index\[iv\]\{.*\}$")
    while i < n:
        line = raw_lines[i]
        if cmd_re.match(line):
            # remove trailing blank lines already in norm before command
            while norm and norm[-1] == "":
                norm.pop()
            norm.append(line)
            # skip immediate blank lines after command
            j = i + 1
            while j < n and raw_lines[j] == "":
                j += 1
            # keep exactly one separator blank line only if next line exists
            if j < n:
                norm.append("")
            i = j
            continue
        norm.append(line)
        i += 1
    return "\n".join(norm)


def _anchor_ids_in_order(anchor_md: str) -> list[str]:
    return re.findall(
        r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}',
        anchor_md,
    )


def _extract_nonexplicit_raw_commands(raw_md: str) -> list[str]:
    """Extract raw \index commands injected in Markdown (excluding \printindex)."""
    return [
        line.strip()
        for line in raw_md.splitlines()
        if line.strip().startswith(r"\index[iv]{")
    ]


def check(verbose: bool = False, canonical_md_override: str | None = None) -> bool:
    errors: list[str] = []

    # ── A. Canonical plan coverage ─────────────────────────────────────────────
    plan_ordered = _load_plan_ordered()
    plan_ids = [eid for eid, _ in plan_ordered]
    plan_set = set(plan_ids)
    blank_ids = [eid for eid in plan_ids if not eid]
    duplicate_ids = [eid for eid, cnt in Counter(plan_ids).items() if cnt > 1]
    if blank_ids:
        errors.append(f"A: plan has blank non-explicit emission_id rows ({len(blank_ids)})")
    if duplicate_ids:
        errors.append(f"A: plan has duplicate non-explicit emission_id rows ({len(duplicate_ids)})")
    if len(plan_ids) != EXPECTED_NON_EXPLICIT:
        errors.append(
            f"A: Expected {EXPECTED_NON_EXPLICIT} non-explicit emission IDs in plan, "
            f"got {len(plan_ids)}"
        )

    # ── B. Builder traces + markdown generation ────────────────────────────────
    anchor_trace: list[BookEmission] = []
    raw_trace: list[BookEmission] = []
    anchor_md = build_book_markdown(render_mode="anchor", emission_trace=anchor_trace)
    raw_md = build_book_markdown(render_mode="raw", emission_trace=raw_trace)
    if len(anchor_trace) != EXPECTED_NON_EXPLICIT:
        errors.append(f"B: anchor trace count {len(anchor_trace)} != {EXPECTED_NON_EXPLICIT}")
    if len(raw_trace) != EXPECTED_NON_EXPLICIT:
        errors.append(f"B: raw trace count {len(raw_trace)} != {EXPECTED_NON_EXPLICIT}")
    if [e.emission_id for e in anchor_trace] != [e.emission_id for e in raw_trace]:
        errors.append("B: anchor/raw trace emission_id sequence mismatch")
    if anchor_trace != raw_trace:
        errors.append("B: anchor/raw complete trace record sequence mismatch")
    if len({e.emission_id for e in anchor_trace}) != len(anchor_trace):
        errors.append("B: duplicate emission_id in anchor trace")
    if len({e.emission_id for e in raw_trace}) != len(raw_trace):
        errors.append("B: duplicate emission_id in raw trace")

    # ── C. Canonical production Markdown (anchor) ─────────────────────────────
    if canonical_md_override is not None:
        canonical_md = canonical_md_override
        if anchor_md != canonical_md:
            errors.append("C: canonical Markdown override is not byte-identical to generated anchor-mode Markdown")
    elif CANONICAL_MD.exists():
        canonical_md = CANONICAL_MD.read_text(encoding="utf-8")
        if anchor_md != canonical_md:
            errors.append("C: canonical Markdown is not byte-identical to generated anchor-mode Markdown")
    else:
        errors.append(f"C: canonical MD not found at {CANONICAL_MD}")

    block_ids = _anchor_ids_in_order(anchor_md)
    inline_ids = re.findall(
        r"\[\]\{[^}]*\.iv-anchor[^}]*emission_id=\"([^\"]+)\"[^}]*\}",
        anchor_md,
    )
    if len(block_ids) != EXPECTED_NON_EXPLICIT:
        errors.append(f"C: block anchor count {len(block_ids)} != {EXPECTED_NON_EXPLICIT}")
    if inline_ids:
        errors.append(f"C: found {len(inline_ids)} production inline anchors (expected 0)")
    raw_inj = sum(
        1 for line in anchor_md.splitlines()
        if r"\index[iv]{" in line and r"\printindex[iv]" not in line
    )
    if raw_inj:
        errors.append(f"C: canonical anchor Markdown has {raw_inj} raw non-explicit commands")
    actual_ids = block_ids
    missing = plan_set - set(actual_ids)
    extra = set(actual_ids) - plan_set
    dups = {eid: c for eid, c in Counter(actual_ids).items() if c > 1}
    if missing:
        errors.append(f"C: missing expected anchor IDs: {sorted(missing)[:3]} (count={len(missing)})")
    if extra:
        errors.append(f"C: unexpected anchor IDs: {sorted(extra)[:3]} (count={len(extra)})")
    if dups:
        errors.append(f"C: duplicate anchor IDs: {list(dups)[:3]} (count={len(dups)})")
    if actual_ids != [e.emission_id for e in anchor_trace]:
        errors.append("C: anchor ID sequence in Markdown != production rendering trace")
    # Ensure explicit_tag IDs are never anchored
    import csv
    with BOOK_EMISSIONS_TSV.open(encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f, delimiter="\t"))
    explicit_ids = {r["emission_id"] for r in all_rows if (r.get("emission_path") or "").strip() == "explicit_tag"}
    bad_explicit = explicit_ids.intersection(actual_ids)
    if bad_explicit:
        errors.append(f"C: explicit_tag emission IDs anchored unexpectedly: {sorted(list(bad_explicit))[:3]}")

    # ── D. Legacy raw Markdown invariants ──────────────────────────────────────
    raw_cmds_md = _extract_nonexplicit_raw_commands(raw_md)
    if len(raw_cmds_md) != EXPECTED_NON_EXPLICIT:
        errors.append(f"D: raw-mode Markdown has {len(raw_cmds_md)} non-explicit commands (expected {EXPECTED_NON_EXPLICIT})")
    if ".iv-anchor" in raw_md:
        errors.append("D: raw-mode Markdown contains .iv-anchor markers (expected 0)")

    # ── E/F. Pandoc runs and TeX parity ────────────────────────────────────────
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        raw_tex = _run_pandoc(raw_md, tmp_path, "raw")
        anchor_tex = _run_pandoc(anchor_md, tmp_path, "anchor")

    raw_cmds = _extract_iv_commands(raw_tex)
    anchor_cmds = _extract_iv_commands(anchor_tex)

    if len(raw_cmds) != EXPECTED_TOTAL:
        errors.append(f"E: raw TeX: {len(raw_cmds)} commands (expected {EXPECTED_TOTAL})")
    if len(anchor_cmds) != EXPECTED_TOTAL:
        errors.append(f"E: anchor TeX: {len(anchor_cmds)} commands (expected {EXPECTED_TOTAL})")

    raw_unique = len(set(raw_cmds))
    anchor_unique = len(set(anchor_cmds))
    if raw_unique != EXPECTED_UNIQUE:
        errors.append(f"E: raw TeX: {raw_unique} unique (expected {EXPECTED_UNIQUE})")
    if anchor_unique != EXPECTED_UNIQUE:
        errors.append(f"E: anchor TeX: {anchor_unique} unique (expected {EXPECTED_UNIQUE})")

    raw_ctr = Counter(raw_cmds)
    anchor_ctr = Counter(anchor_cmds)
    if raw_ctr != anchor_ctr:
        missing_c = {k: (raw_ctr[k], anchor_ctr.get(k, 0)) for k in raw_ctr if raw_ctr[k] > anchor_ctr.get(k, 0)}
        extra_c = {k: (raw_ctr.get(k, 0), anchor_ctr[k]) for k in anchor_ctr if anchor_ctr[k] > raw_ctr.get(k, 0)}
        errors.append(f"E: command Counter mismatch; missing={len(missing_c)} extra={len(extra_c)}")

    if not errors and raw_cmds != anchor_cmds:
        idx = next((i for i, (r, a) in enumerate(zip(raw_cmds, anchor_cmds)) if r != a), None)
        if idx is not None:
            errors.append(f"E: ordered command sequence mismatch at index {idx}; raw={raw_cmds[idx][:80]!r} anchor={anchor_cmds[idx][:80]!r}")

    # Narrow TeX comparison (only whitespace around standalone index commands)
    tex_identical = raw_tex == anchor_tex
    norm_equal = _narrow_tex_normalize(raw_tex) == _narrow_tex_normalize(anchor_tex)
    if not norm_equal:
        import difflib
        diff = list(difflib.unified_diff(raw_tex.splitlines(), anchor_tex.splitlines(),
                                         fromfile="raw_tex", tofile="anchor_tex",
                                         n=3, lineterm=""))
        focused = "\n".join(diff[:80])
        print("Focused TeX diff (first ~80 lines):", file=sys.stderr)
        print(focused, file=sys.stderr)
        errors.append("F: TeX outputs differ after narrow index-command whitespace normalization")

    if errors:
        print("ANCHOR PRODUCTION CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return False

    tex_note = "byte-identical" if tex_identical else "match after narrow index-command whitespace normalization"
    print(
        f"anchor production check passed:\n"
        f"  A: plan IDs={len(plan_ids)} non-explicit ✓\n"
        f"  B: raw/anchor traces equal ({len(anchor_trace)} records) ✓\n"
        f"  C: canonical anchor Markdown has {len(actual_ids)} block anchors, 0 inline, no raw non-explicit commands ✓\n"
        f"  D: legacy raw Markdown has {len(raw_cmds_md)} non-explicit raw commands, 0 anchors ✓\n"
        f"  E: raw/anchor commands: {len(raw_cmds)} total, {raw_unique} unique; Counter equal; ordered sequence equal ✓\n"
        f"  F: full TeX {tex_note}"
    )
    return True


def main() -> None:
    if not _pandoc_available():
        print("pandoc not found; skipping anchor production check.", file=sys.stderr)
        sys.exit(127)
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    sys.exit(0 if check(args.verbose) else 1)


if __name__ == "__main__":
    main()

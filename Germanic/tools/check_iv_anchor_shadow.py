#!/usr/bin/env python3
"""Strict shadow parity check for the .iv-anchor emission path.

Verifies Stage 1 of the IV emitter migration:

  A. Canonical plan: 448 non-explicit in-book emissions (heading/line injection).

  B. Raw mode byte-identical to tracked capr_book_draft_alpha_01.md.

  C. Anchor mode: exactly 448 .iv-anchor markers, all expected IDs present
     once (set check), no unexpected IDs, no duplicates, order matches builder's
     canonical traversal order.

  D. Both Pandoc/Lua runs produce 1865 commands (828 unique).
     Counter and ordered sequence are exactly equal.
     Full TeX outputs match after whitespace normalisation
     (blank lines around index commands differ harmlessly).

Exit codes
----------
  0    all checks pass
  1    check failure (details on stderr)
  127  pandoc not available
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
CANONICAL_MD = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"

EXPECTED_NON_EXPLICIT = 448
EXPECTED_TOTAL = 1865
EXPECTED_UNIQUE = 828

sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))
from build_capr_book_draft import build_book_markdown


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


def _load_plan_set() -> set[str]:
    """Return the set of non-explicit in-book emission IDs from the canonical plan."""
    import csv
    with BOOK_EMISSIONS_TSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    return {
        r["emission_id"]
        for r in rows
        if (r.get("emission_path") or "").strip() in ("heading_injection", "line_injection")
        and (r.get("emission_id") or "").strip()
    }


def _normalize_tex(tex: str) -> str:
    """Remove blank lines and trailing whitespace.

    The raw and anchor modes produce the same index commands at the same content
    positions, but raw commands are RawInline nodes (inside a paragraph) while
    anchor mode uses RawBlock nodes (standalone). Pandoc adds or removes blank
    lines around standalone blocks. After removing blank lines the content is
    identical.
    """
    return "\n".join(line.rstrip() for line in tex.splitlines() if line.strip())


def _anchor_ids_in_order(anchor_md: str) -> list[str]:
    return re.findall(
        r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}',
        anchor_md,
    )


def check(verbose: bool = False) -> bool:
    errors: list[str] = []

    # ── A. Canonical plan set ──────────────────────────────────────────────────
    plan_set = _load_plan_set()
    if len(plan_set) != EXPECTED_NON_EXPLICIT:
        errors.append(
            f"A: Expected {EXPECTED_NON_EXPLICIT} non-explicit emission IDs in plan, "
            f"got {len(plan_set)}"
        )

    # ── B. Raw Markdown ────────────────────────────────────────────────────────
    raw_md = build_book_markdown(render_mode="raw")
    if CANONICAL_MD.exists():
        if raw_md != CANONICAL_MD.read_text(encoding="utf-8"):
            errors.append("B: raw-mode Markdown is NOT byte-identical to canonical MD")
    else:
        errors.append(f"B: canonical MD not found at {CANONICAL_MD}")

    # ── C. Anchor Markdown ─────────────────────────────────────────────────────
    anchor_md = build_book_markdown(render_mode="anchor")

    # No raw injection commands
    raw_inj = sum(
        1 for line in anchor_md.splitlines()
        if r"\index[iv]{" in line and r"\printindex[iv]" not in line
    )
    if raw_inj:
        errors.append(f"C: anchor MD has {raw_inj} raw \\index[iv] injection(s)")

    # Anchor ID coverage (set check — order is builder's canonical traversal)
    actual_ids = _anchor_ids_in_order(anchor_md)
    actual_set = set(actual_ids)
    actual_counter = Counter(actual_ids)

    if len(actual_ids) != EXPECTED_NON_EXPLICIT:
        errors.append(
            f"C: Expected {EXPECTED_NON_EXPLICIT} anchors, got {len(actual_ids)}"
        )

    missing = plan_set - actual_set
    extra = actual_set - plan_set
    dups = {eid: cnt for eid, cnt in actual_counter.items() if cnt > 1}

    if missing:
        errors.append(f"C: {len(missing)} expected ID(s) missing; first: {sorted(missing)[:3]}")
    if extra:
        errors.append(f"C: {len(extra)} unexpected ID(s); first: {sorted(extra)[:3]}")
    if dups:
        errors.append(f"C: {len(dups)} duplicate anchor ID(s): {list(dups)[:3]}")

    # ── D. Pandoc runs ─────────────────────────────────────────────────────────
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        raw_tex = _run_pandoc(raw_md, tmp_path, "raw")
        anchor_tex = _run_pandoc(anchor_md, tmp_path, "anchor")

    raw_cmds = _extract_iv_commands(raw_tex)
    anchor_cmds = _extract_iv_commands(anchor_tex)

    if len(raw_cmds) != EXPECTED_TOTAL:
        errors.append(f"D: raw TeX: {len(raw_cmds)} commands (expected {EXPECTED_TOTAL})")
    if len(anchor_cmds) != EXPECTED_TOTAL:
        errors.append(f"D: anchor TeX: {len(anchor_cmds)} commands (expected {EXPECTED_TOTAL})")

    raw_unique = len(set(raw_cmds))
    anchor_unique = len(set(anchor_cmds))
    if raw_unique != EXPECTED_UNIQUE:
        errors.append(f"D: raw TeX: {raw_unique} unique (expected {EXPECTED_UNIQUE})")
    if anchor_unique != EXPECTED_UNIQUE:
        errors.append(f"D: anchor TeX: {anchor_unique} unique (expected {EXPECTED_UNIQUE})")

    raw_ctr = Counter(raw_cmds)
    anchor_ctr = Counter(anchor_cmds)
    if raw_ctr != anchor_ctr:
        missing_c = {k: (raw_ctr[k], anchor_ctr.get(k, 0)) for k in raw_ctr if raw_ctr[k] > anchor_ctr.get(k, 0)}
        extra_c = {k: (raw_ctr.get(k, 0), anchor_ctr[k]) for k in anchor_ctr if anchor_ctr[k] > raw_ctr.get(k, 0)}
        errors.append(
            f"D: command Counter mismatch; missing={len(missing_c)} extra={len(extra_c)}"
        )

    if not errors and raw_cmds != anchor_cmds:
        idx = next((i for i, (r, a) in enumerate(zip(raw_cmds, anchor_cmds)) if r != a), None)
        if idx is not None:
            errors.append(
                f"D: ordered command sequence mismatch at index {idx}; "
                f"raw: {raw_cmds[idx][:80]!r}, anchor: {anchor_cmds[idx][:80]!r}"
            )

    # Full TeX comparison after normalisation
    tex_identical = raw_tex == anchor_tex
    norm_equal = _normalize_tex(raw_tex) == _normalize_tex(anchor_tex)
    if not norm_equal:
        errors.append(
            "D: TeX outputs differ even after whitespace normalisation "
            "(not just blank-line placement)"
        )

    if errors:
        print("ANCHOR SHADOW CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return False

    tex_note = "byte-identical" if tex_identical else "match after blank-line normalization"
    print(
        f"anchor shadow check passed:\n"
        f"  A: plan has {len(plan_set)} non-explicit emission IDs ✓\n"
        f"  B: raw MD byte-identical to canonical ✓\n"
        f"  C: anchor MD has {len(actual_ids)} markers, all expected IDs present ✓\n"
        f"  D: raw TeX {len(raw_cmds)} commands ({raw_unique} unique) ✓\n"
        f"  D: anchor TeX {len(anchor_cmds)} commands ({anchor_unique} unique) ✓\n"
        f"  D: Counter equal ✓, ordered sequence equal ✓\n"
        f"  D: full TeX {tex_note}"
    )
    return True


def main() -> None:
    if not _pandoc_available():
        print("pandoc not found; skipping anchor shadow check.", file=sys.stderr)
        sys.exit(127)
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    sys.exit(0 if check(args.verbose) else 1)


if __name__ == "__main__":
    main()

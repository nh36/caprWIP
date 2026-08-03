#!/usr/bin/env python3
"""Shadow-mode anchor check.

Proves that the .iv-anchor path through the Lua filter produces
exactly the same set of \\index[iv]{...} commands as the production
Python-injection path.

Architecture being tested (shadow mode only — NOT yet active in production):
  heading/line injection sites → .iv-anchor Span markers
  .iv-anchor Span → Lua looks up emission_id in book_emissions.tsv
  Lua emits precomputed index_command verbatim

Production architecture (unchanged by this task):
  heading/line injection sites → raw \\index[iv]{...} in Markdown
  these pass through pandoc as-is, bypassing the Lua filter

Both paths must produce exactly the same command multiset.

Exit codes
----------
  0  — equivalence proved
  1  — differences found (details on stderr)
  127 — pandoc not available (skip)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SHADOW_BUILDER = REPO_ROOT / "Germanic/docs/assembly/build_capr_book_draft_shadow.py"
BOOK_EMISSIONS_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_book_emissions.tsv"
PRINT_MAIN_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
LANGUAGE_REGISTRY_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
VARIETY_REGISTRY_TSV = REPO_ROOT / "Germanic/docs/book/index_verborum_varieties.tsv"
FILTER_LUA = REPO_ROOT / "Germanic/tools/index_verborum_filter.lua"


def _extract_iv_bodies(text: str) -> list[str]:
    bodies = []
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
        bodies.append(text[m.end():end - 1])
    return bodies


def load_canonical_commands() -> Counter[str]:
    """Return the expected command multiset from the canonical emission plan."""
    import csv
    with BOOK_EMISSIONS_TSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    cmds: Counter[str] = Counter()
    for row in rows:
        cmd = (row.get("index_command") or "").strip()
        if cmd:
            cmds[cmd] += 1
    return cmds


def run_pandoc_anchor_check(shadow_md_path: Path) -> Counter[str]:
    """Run pandoc with the Lua filter on the shadow MD and collect \\index[iv] commands."""
    import os
    env = dict(os.environ)
    env["CAPR_IV_PRINT_MAIN_TSV"] = str(PRINT_MAIN_TSV)
    env["CAPR_IV_BOOK_EMISSIONS_TSV"] = str(BOOK_EMISSIONS_TSV)
    env["CAPR_IV_LANGUAGE_REGISTRY_TSV"] = str(LANGUAGE_REGISTRY_TSV)
    env["CAPR_IV_VARIETY_REGISTRY_TSV"] = str(VARIETY_REGISTRY_TSV)

    proc = subprocess.run(
        [
            "pandoc",
            str(shadow_md_path),
            "--from", "markdown+raw_tex",
            "--to", "latex",
            "--lua-filter", str(FILTER_LUA),
        ],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(REPO_ROOT),
    )
    if proc.returncode != 0:
        print("pandoc failed:", proc.stderr[:500], file=sys.stderr)
        sys.exit(1)

    bodies = _extract_iv_bodies(proc.stdout)
    return Counter(r"\index[iv]{" + b + "}" for b in bodies)


def check(shadow_md_path: Path | None = None) -> bool:
    """Return True if the shadow anchor path produces commands equal to the canonical plan."""
    # Step 1: build shadow MD if not already provided
    if shadow_md_path is None:
        shadow_md_path = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_shadow.md"
        proc = subprocess.run(
            [sys.executable, str(SHADOW_BUILDER)],
            capture_output=True, text=True, cwd=str(REPO_ROOT)
        )
        if proc.returncode != 0:
            print("Shadow builder failed:", proc.stderr[:500], file=sys.stderr)
            sys.exit(1)

    # Step 2: load canonical expected commands
    canonical = load_canonical_commands()

    # Step 3: run pandoc+lua on shadow MD
    actual = run_pandoc_anchor_check(shadow_md_path)

    # Step 4: compare
    errors: list[str] = []

    missing = {k: (canonical[k], actual.get(k, 0)) for k in canonical if canonical[k] > actual.get(k, 0)}
    extra = {k: (canonical.get(k, 0), actual[k]) for k in actual if actual[k] > canonical.get(k, 0)}

    if missing:
        errors.append(
            f"Missing commands: {len(missing)} command(s) expected more times than emitted:\n"
            + "\n".join(f"  expected={e} actual={a}: {k[:120]}" for k, (e, a) in sorted(missing.items())[:5])
        )
    if extra:
        errors.append(
            f"Extra commands: {len(extra)} command(s) emitted more times than expected:\n"
            + "\n".join(f"  expected={e} actual={a}: {k[:120]}" for k, (e, a) in sorted(extra.items())[:5])
        )

    if errors:
        print("ANCHOR SHADOW CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        print(f"\nCanonical commands: {sum(canonical.values())}", file=sys.stderr)
        print(f"Actual shadow commands: {sum(actual.values())}", file=sys.stderr)
        return False

    total = sum(canonical.values())
    print(
        f"anchor shadow check passed: {total} commands match canonical plan "
        f"({len(canonical)} unique commands)"
    )
    return True


def main() -> None:
    if not Path(subprocess.run(["which", "pandoc"], capture_output=True).stdout.decode().strip()).exists():
        print("pandoc not found; skipping anchor shadow check.", file=sys.stderr)
        sys.exit(127)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shadow-md", type=Path, default=None,
                        help="Path to pre-built shadow MD (default: rebuild from builder)")
    args = parser.parse_args()

    ok = check(args.shadow_md)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

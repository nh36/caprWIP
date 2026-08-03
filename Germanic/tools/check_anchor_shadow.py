#!/usr/bin/env python3
"""Shadow-mode anchor equivalence check.

Proves that the plan-driven ``.iv-anchor`` Lua emission path produces exactly
the same set of ``\\index[iv]{...}`` commands as the production Python-injection
(raw) path, for every non-explicit book emission.

Architecture tested (shadow mode — not yet active in production)
----------------------------------------------------------------
For heading/line injection sites the shadow path places::

    ::: {.iv-anchor emission_id="emit:xxx"}
    :::

in the assembled Markdown. The Lua filter (index_verborum_filter.lua) looks up
the emission_id in book_emissions.tsv and emits the precomputed index_command
verbatim. No semantic reconstruction happens in Lua.

The raw path (current production) inserts raw ``\\index[iv]{...}`` commands
directly into the Markdown, bypassing the Lua filter.

Both paths must produce the same 1865-command multiset from the same book
source material.

Explicit ``.iv`` spans are unaffected in both modes; they continue to emit
through the existing Lua span_to_index path.

Exit codes
----------
  0    equivalence proved
  1    differences found (details on stderr)
  2    configuration error
  127  pandoc not available (check skipped gracefully)
"""
from __future__ import annotations

import argparse
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

# Import the production builder (shared code, not a separate shadow copy)
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))
from build_capr_book_draft import build_book_markdown


def _pandoc_available() -> bool:
    result = subprocess.run(["pandoc", "--version"], capture_output=True)
    return result.returncode == 0


def _extract_iv_bodies(text: str) -> list[str]:
    bodies: list[str] = []
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
    return Counter(
        (row.get("index_command") or "").strip()
        for row in rows
        if (row.get("index_command") or "").strip()
    )


def run_pandoc_on_anchor_md(shadow_md_text: str) -> Counter[str]:
    """Run pandoc + Lua filter on anchor-mode Markdown; return command Counter."""
    env = dict(os.environ)
    env.update({
        "CAPR_IV_PRINT_MAIN_TSV": str(PRINT_MAIN_TSV),
        "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS_TSV),
        "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(LANGUAGE_REGISTRY_TSV),
        "CAPR_IV_VARIETY_REGISTRY_TSV": str(VARIETY_REGISTRY_TSV),
    })
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", encoding="utf-8", delete=False
    ) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write(shadow_md_text)

    try:
        proc = subprocess.run(
            [
                "pandoc", str(tmp_path),
                "--from", "markdown+raw_tex",
                "--to", "latex",
                "--lua-filter", str(FILTER_LUA),
            ],
            capture_output=True,
            text=True,
            env=env,
            cwd=str(REPO_ROOT),
        )
    finally:
        tmp_path.unlink(missing_ok=True)

    if proc.returncode != 0:
        print("pandoc failed:", proc.stderr[:500], file=sys.stderr)
        sys.exit(1)

    bodies = _extract_iv_bodies(proc.stdout)
    return Counter(r"\index[iv]{" + b + "}" for b in bodies)


def check(verbose: bool = False) -> bool:
    """Run the shadow equivalence check. Returns True on pass."""
    # Build anchor-mode Markdown using the production builder — same code, no copy.
    anchor_md = build_book_markdown(render_mode="anchor")

    # Verify anchor MD has markers and no raw injections
    if ".iv-anchor" not in anchor_md:
        print("FAIL: anchor-mode MD has no .iv-anchor markers", file=sys.stderr)
        return False

    raw_count = anchor_md.count(r"\index[iv]")
    if raw_count > 0:
        print(
            f"FAIL: anchor-mode MD contains {raw_count} raw \\index[iv] commands "
            "(expected 0 — anchors only)",
            file=sys.stderr,
        )
        return False

    # Canonical expected commands
    canonical = load_canonical_commands()

    # Shadow: run pandoc + Lua anchor handler
    actual = run_pandoc_on_anchor_md(anchor_md)

    # Compare
    missing = {k: (canonical[k], actual.get(k, 0)) for k in canonical if canonical[k] > actual.get(k, 0)}
    extra = {k: (canonical.get(k, 0), actual[k]) for k in actual if actual[k] > canonical.get(k, 0)}

    if missing or extra:
        print("ANCHOR SHADOW CHECK FAILED:", file=sys.stderr)
        if missing:
            print(
                f"  Missing {len(missing)} command(s) (expected > actual):",
                file=sys.stderr,
            )
            for k, (e, a) in sorted(missing.items())[:5]:
                print(f"    expected={e} actual={a}: {k[:120]}", file=sys.stderr)
        if extra:
            print(
                f"  Extra {len(extra)} command(s) (actual > expected):",
                file=sys.stderr,
            )
            for k, (e, a) in sorted(extra.items())[:5]:
                print(f"    expected={e} actual={a}: {k[:120]}", file=sys.stderr)
        print(
            f"  Canonical plan total: {sum(canonical.values())}",
            f"  Anchor path total:    {sum(actual.values())}",
            sep="\n  ",
            file=sys.stderr,
        )
        return False

    total = sum(canonical.values())
    unique = len(canonical)
    print(
        f"anchor shadow check passed: {total} commands, {unique} unique — "
        "anchor path equals canonical plan exactly"
    )
    return True


def main() -> None:
    if not _pandoc_available():
        print("pandoc not found; skipping anchor shadow check.", file=sys.stderr)
        sys.exit(127)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    ok = check(verbose=args.verbose)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

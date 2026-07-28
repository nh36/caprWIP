#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


CITEPROC_RE = re.compile(r"(\\citeproc\{[^{}]+\}\{)([^{}]*)(\})")
SECTS_RE = re.compile(r"\bsects\.?\s+([0-9][0-9A-Za-z.,\-– ]*)", re.IGNORECASE)
SECT_RE = re.compile(r"\bsect\.?\s+([0-9][0-9A-Za-z.,\-– ]*)", re.IGNORECASE)


def normalize_inner(text: str) -> tuple[str, int]:
    total = 0

    def repl_sects(match: re.Match[str]) -> str:
        nonlocal total
        total += 1
        return f"§§ {match.group(1)}"

    def repl_sect(match: re.Match[str]) -> str:
        nonlocal total
        total += 1
        return f"§ {match.group(1)}"

    text = SECTS_RE.sub(repl_sects, text)
    text = SECT_RE.sub(repl_sect, text)
    return text, total


def normalize_tex(content: str) -> tuple[str, int]:
    replacements = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal replacements
        prefix, inner, suffix = match.group(1), match.group(2), match.group(3)
        normalized, count = normalize_inner(inner)
        replacements += count
        return f"{prefix}{normalized}{suffix}"

    return CITEPROC_RE.sub(repl, content), replacements


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, required=True)
    args = parser.parse_args()

    tex_path = args.tex_path.expanduser().resolve()
    original = tex_path.read_text(encoding="utf-8")
    updated, replacements = normalize_tex(original)
    if updated != original:
        tex_path.write_text(updated, encoding="utf-8")
    print(f"Normalized citeproc section locators: {replacements} replacement(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

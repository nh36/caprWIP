#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
INTRO_PATH = SCRIPT_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
LEXICAL_PATH = SCRIPT_DIR / "lexical_volume_alpha_01.md"
OUTPUT_PATH = SCRIPT_DIR / "capr_book_draft_alpha_01.md"


def strip_title_block(text: str) -> str:
    lines = text.rstrip().splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).rstrip()


def strip_references(text: str) -> str:
    marker = "\n# References\n"
    return text.split(marker, 1)[0].rstrip() if marker in text else text.rstrip()


def transform_chronology(text: str) -> str:
    out: list[str] = []
    for line in strip_title_block(strip_references(text)).splitlines():
        if line == "## Introduction":
            out.append("## Scope and orientation")
        elif line == "## Numbering note":
            out.append("## Numbering note")
        elif line.startswith("# "):
            out.append("## " + line[2:])
        elif line.startswith("## "):
            out.append("### " + line[3:])
        else:
            out.append(line)
    return "\n".join(out).rstrip()


def transform_lexical(text: str) -> str:
    out: list[str] = []
    lines = strip_title_block(text).splitlines()
    if lines and lines[0].startswith("_Alpha 01"):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    for line in lines:
        if line.startswith("## Part "):
            out.append(re.sub(r"^## Part [IVX]+\.\s+", "## ", line))
        else:
            out.append(line)
    return "\n".join(out).rstrip()


def build_book_markdown() -> str:
    intro = INTRO_PATH.read_text(encoding="utf-8").rstrip()
    chronology = transform_chronology(CHRONOLOGY_PATH.read_text(encoding="utf-8"))
    lexical = transform_lexical(LEXICAL_PATH.read_text(encoding="utf-8"))
    parts = [
        r"\mainmatter",
        intro,
        r"\part{Sound changes, formalization, and relative chronology}",
        "# The ordered sound-change sequence",
        chronology,
        r"\part{Lexical derivations}",
        "# Word-by-word derivations",
        lexical,
        r"\backmatter",
        "# References",
        "",
        "::: {#refs}",
        ":::",
        "",
        r"\part*{Index verborum}",
        r"\addcontentsline{toc}{part}{Index verborum}",
        r"\printindex[oe]",
        r"\printindex[pgmc]",
        r"\printindex[pwgmc]",
        r"\printindex[nwgmc]",
        r"\printindex[preoe]",
        r"\printindex[on]",
        r"\printindex[ohg]",
        r"\printindex[ofris]",
        r"\printindex[goth]",
    ]
    return "\n\n".join(parts) + "\n"


def main() -> None:
    OUTPUT_PATH.write_text(build_book_markdown(), encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
INTRO_PATH = SCRIPT_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
LEXICAL_PATH = SCRIPT_DIR / "lexical_volume_alpha_01.md"
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
OUTPUT_PATH = SCRIPT_DIR / "capr_book_draft_alpha_01.md"
LANGUAGE_ORDER = ["oe", "pgmc", "pwgmc", "nwgmc", "preoe", "on", "ohg", "ofris", "goth"]


def latex_escape(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


def index_command(language: str, sort_key: str, display: str) -> str:
    return rf"\index[{language}]{{{latex_escape(sort_key)}@{latex_escape(display)}}}"


def load_production_rows() -> tuple[dict[str, list[str]], list[str]]:
    commands_by_ref: dict[str, list[str]] = defaultdict(list)
    counts = Counter()
    with FORMS_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            language = (row.get("language") or "").strip()
            if not language:
                continue
            counts[language] += 1
            if row.get("source_scope") == "explicit_tag":
                continue
            ref = (row.get("source_ref") or "").strip()
            if not ref:
                continue
            command = index_command(language, (row.get("sort_key") or "").strip(), (row.get("display") or "").strip())
            if command not in commands_by_ref[ref]:
                commands_by_ref[ref].append(command)
    nonempty = [language for language in LANGUAGE_ORDER if counts.get(language)]
    return commands_by_ref, nonempty


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
        elif line.startswith("# "):
            out.append("## " + line[2:])
        elif line.startswith("## "):
            out.append("### " + line[3:])
        else:
            out.append(line)
    return "\n".join(out).rstrip()


def transform_lexical(text: str, commands_by_ref: dict[str, list[str]]) -> str:
    out: list[str] = []
    lines = strip_title_block(text).splitlines()
    if lines and lines[0].startswith("_Alpha 01"):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    for line in lines:
        if line.startswith("## Part "):
            line = re.sub(r"^## Part [IVX]+\.\s+", "## ", line)
        out.append(line)
        if line.startswith("### "):
            ref = line[4:].strip()
            commands = commands_by_ref.get(ref, [])
            if commands:
                out.append("")
                out.extend(commands)
    return "\n".join(out).rstrip()


def build_book_markdown() -> str:
    commands_by_ref, nonempty_languages = load_production_rows()
    intro = INTRO_PATH.read_text(encoding="utf-8").rstrip()
    chronology = transform_chronology(CHRONOLOGY_PATH.read_text(encoding="utf-8"))
    lexical = transform_lexical(LEXICAL_PATH.read_text(encoding="utf-8"), commands_by_ref)
    index_parts = [rf"\printindex[{language}]" for language in nonempty_languages]
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
        *index_parts,
    ]
    return "\n\n".join(parts) + "\n"


def main() -> None:
    OUTPUT_PATH.write_text(build_book_markdown(), encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

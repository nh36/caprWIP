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
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
MANIFEST_PATH = SCRIPT_DIR / "manifest_all_by_class.tsv"
OUTPUT_PATH = SCRIPT_DIR / "capr_book_draft_alpha_01.md"
EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{\.iv(?P<attrs>[^}]*)\}")


def load_language_order() -> list[str]:
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        return [row["code"] for row in csv.DictReader(handle, delimiter="\t") if (row.get("active") or "").strip() == "1"]


LANGUAGE_ORDER = load_language_order()


def latex_escape(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


def index_command(language: str, sort_key: str, display: str) -> str:
    index_display = latex_escape(display)
    if language == "oe":
        index_display = rf"\emph{{{index_display}}}"
    return rf"\index[{language}]{{{latex_escape(sort_key)}@{index_display}}}"


def oe_target_display(counterpart: str, derivation_class: str) -> str:
    return f"*{counterpart}" if derivation_class == "reconstructed_oe" else counterpart


def heading_ref(lexical_item: str, counterpart: str, derivation_class: str = "") -> str:
    return f"{lexical_item} — OE {oe_target_display(counterpart, derivation_class)}"


def load_production_rows() -> tuple[dict[str, list[str]], dict[str, dict[int, list[str]]], list[str]]:
    commands_by_heading_ref: dict[str, list[str]] = defaultdict(list)
    commands_by_line_ref: dict[str, dict[int, list[str]]] = defaultdict(lambda: defaultdict(list))
    counts = Counter()
    model_entry_heading_map = {}
    line_injected_scopes = {"table_semantic_auto", "table_semantic_decision", "broad_prose_decision"}
    with MANIFEST_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            model_entry_heading_map[row["model_entry_path"]] = heading_ref(row["lexical_item"], row["counterpart"], row["derivation_class"])
    with PRINT_MAIN_PATH.open(encoding="utf-8") as handle:
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
            if ".md:" in ref:
                path_part, line_part = ref.rsplit(":", 1)
                if row.get("source_scope") in line_injected_scopes and line_part.isdigit():
                    line_no = int(line_part)
                    if command not in commands_by_line_ref[path_part][line_no]:
                        commands_by_line_ref[path_part][line_no].append(command)
                elif path_part in model_entry_heading_map:
                    heading = model_entry_heading_map[path_part]
                    if command not in commands_by_heading_ref[heading]:
                        commands_by_heading_ref[heading].append(command)
                elif line_part.isdigit():
                    line_no = int(line_part)
                    if command not in commands_by_line_ref[path_part][line_no]:
                        commands_by_line_ref[path_part][line_no].append(command)
            else:
                if command not in commands_by_heading_ref[ref]:
                    commands_by_heading_ref[ref].append(command)
    nonempty = [language for language in LANGUAGE_ORDER if counts.get(language)]
    return commands_by_heading_ref, commands_by_line_ref, nonempty


def annotate_explicit_tags_in_line(line: str, rel_path: str, line_no: int) -> str:
    source_ref = f'{rel_path}:{line_no}'

    def repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if re.search(r'(^|\s)source_ref=', attrs):
            return match.group(0)
        attrs_body = attrs.strip()
        if attrs_body:
            merged_attrs = f" {attrs_body} source_ref=\"{source_ref}\""
        else:
            merged_attrs = f" source_ref=\"{source_ref}\""
        return f"[{match.group('content')}]{{.iv{merged_attrs}}}"

    return EXPLICIT_TAG_RE.sub(repl, line)


def annotate_explicit_tags_with_source_ref(path: Path, text: str) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    return "\n".join(
        annotate_explicit_tags_in_line(line, rel, line_no)
        for line_no, line in enumerate(text.splitlines(), start=1)
    )


def inject_line_commands(path: Path, line_commands: dict[str, dict[int, list[str]]]) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    commands = line_commands.get(rel, {})
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    for idx, line in enumerate(lines, start=1):
        out.append(annotate_explicit_tags_in_line(line, rel, idx))
        if idx in commands:
            out.extend(commands[idx])
    return "\n".join(out).rstrip()


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
            if " — OE _" in ref and ref.endswith("_"):
                lexical_item, target = ref.split(" — OE ", 1)
                # perform the replacement before interpolating into the f-string to avoid backslashes inside f-string expressions
                cleaned_target = target[1:-1].replace('\\*', '*')
                ref = f"{lexical_item} — OE {cleaned_target}"
            commands = commands_by_ref.get(ref, [])
            if commands:
                out.append("")
                out.extend(commands)
    return "\n".join(out).rstrip()


def build_book_markdown() -> str:
    commands_by_ref, line_commands, nonempty_languages = load_production_rows()
    intro = inject_line_commands(INTRO_PATH, line_commands)
    chronology = transform_chronology(inject_line_commands(CHRONOLOGY_PATH, line_commands))
    lexical = transform_lexical(
        annotate_explicit_tags_with_source_ref(LEXICAL_PATH, LEXICAL_PATH.read_text(encoding="utf-8")),
        commands_by_ref,
    )
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

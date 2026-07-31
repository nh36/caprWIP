#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_EXCLUDED_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_excluded.tsv"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
INDEX_HEADER_PATH = REPO_ROOT / "Germanic/docs/assembly/book_draft_pdf_header.tex"
DEFAULT_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"
PROSE_RULE_WORDS = {"form", "output", "expected", "stage", "rule"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def latex_escape(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


def _check_build_lang_order() -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        for order, row in enumerate(csv.DictReader(handle, delimiter="\t"), start=1):
            code = (row.get("code") or "").strip()
            title = (row.get("title") or "").strip()
            active = (row.get("active") or "").strip()
            if code and active == "1":
                result[code] = (f"{order:02d}{code}", title)
    return result


_CHECK_LANG_ORDER: dict[str, tuple[str, str]] | None = None


def check_get_lang_order() -> dict[str, tuple[str, str]]:
    global _CHECK_LANG_ORDER
    if _CHECK_LANG_ORDER is None:
        _CHECK_LANG_ORDER = _check_build_lang_order()
    return _CHECK_LANG_ORDER


def index_command(row: dict[str, str]) -> str:
    language = row.get("language", "")
    sort_key = row.get("sort_key", "")
    display = row.get("display", "")
    index_display = latex_escape(display)
    if language == "oe":
        index_display = rf"\emph{{{index_display}}}"
    lang_order = check_get_lang_order()
    lang_prefix, lang_title = lang_order.get(language, (f"99{language}", language))
    lang_title_escaped = lang_title.replace("@", r"\@").replace("!", r"\!")
    lang_header = rf"\textbf{{{lang_title_escaped}}}"
    return rf"\index[iv]{{{lang_prefix}@{lang_header}!{latex_escape(sort_key)}@{index_display}}}"


def explicit_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (
        row.get("language", ""),
        row.get("sort_key", ""),
        row.get("display", ""),
        row.get("form_role", "") or "evidence_form",
    )


def require_row(rows: list[dict[str, str]], predicate, label: str) -> dict[str, str]:
    for row in rows:
        if predicate(row):
            return row
    raise AssertionError(f"Missing regression row for {label}")


def decode_latex_index_value(value: str) -> str:
    return value.replace(r"\@", "@").replace(r"\!", "!").replace(r"\|", "|")


def parse_tex_index_commands(tex_text: str) -> list[tuple[str, str, str]]:
    """Parse \\index[iv]{LANGPREFIX@TITLE!sort@display} into (lang_prefix, sort, display) tuples."""
    commands: list[tuple[str, str, str]] = []
    # Match both legacy per-language and new unified format
    for match in re.finditer(r"\\index\[(?P<lang>[^\]]+)\]\{(?P<body>[^}]*)\}", tex_text):
        lang = match.group("lang")
        body = match.group("body")
        if lang == "iv" and "!" in body:
            # Unified two-level: LANGPREFIX@TITLE!sort@display
            # Split on first un-escaped !
            parts = re.split(r"(?<!\\)!", body, maxsplit=1)
            if len(parts) == 2:
                lang_part, form_part = parts
                if "@" in form_part:
                    sort_key, display = form_part.split("@", 1)
                else:
                    sort_key, display = form_part, form_part
                commands.append((lang, decode_latex_index_value(sort_key), decode_latex_index_value(display)))
        else:
            # Legacy or non-iv format
            if "@" in body:
                sort_key, display = body.split("@", 1)
            else:
                sort_key, display = body, body
            commands.append((lang, decode_latex_index_value(sort_key), decode_latex_index_value(display)))
    return commands


def normalized_index_token(value: str) -> str:
    return value.casefold().lstrip("*").strip("`.,;:!?()[]{}\"' ")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, default=DEFAULT_TEX_PATH)
    args = parser.parse_args()

    tex_path = args.tex_path.expanduser().resolve()
    tex_text = tex_path.read_text(encoding="utf-8")
    header_text = INDEX_HEADER_PATH.read_text(encoding="utf-8")
    form_rows = load_rows(FORMS_PATH)
    main_rows = load_rows(PRINT_MAIN_PATH)
    excluded_rows = load_rows(PRINT_EXCLUDED_PATH)
    main_commands = {index_command(row) for row in main_rows}
    tex_commands = parse_tex_index_commands(tex_text)

    main_explicit_keys = {
        explicit_key(row)
        for row in main_rows
        if row.get("source_scope") == "explicit_tag"
    }

    # With unified index, all commands go through \index[iv]{...}; no per-language \index[lang] should appear
    assert r"\index[preoe]{" not in tex_text, "Direct preoe index command must not appear; use unified iv index."
    assert r"\indexsetup{level=\section*,noclearpage}" in header_text, "Expected indexsetup with level=\\section* for index layout."
    assert r"\indexsetup{level=\chapter*" not in header_text

    for row in excluded_rows:
        if row.get("form_role") != "regular_output":
            continue
        if explicit_key(row) in main_explicit_keys:
            continue
        command = index_command(row)
        if command in main_commands:
            continue
        assert command not in tex_text, f"Excluded explicit regular_output leaked into TeX: {command}"

    reader_failure_rows = [row for row in form_rows if (row.get("source_scope") or "").startswith("reader_failure_")]
    for row in reader_failure_rows:
        command = index_command(row)
        if command in main_commands:
            continue
        assert command not in tex_text, f"Reader-facing failure row leaked into TeX: {command}"

    for form in ("fogol", "woll", "wylf", "*bakan"):
        for row in excluded_rows:
            if row.get("form") != form:
                continue
            if row.get("source_scope") == "explicit_tag" and explicit_key(row) in main_explicit_keys:
                continue
            command = index_command(row)
            if command in main_commands:
                continue
            assert command not in tex_text, f"Excluded form leaked into TeX index commands: {command}"

    for language, sort_key, display in tex_commands:
        token_sort = normalized_index_token(sort_key)
        token_display = normalized_index_token(display)
        assert token_sort not in {"monch", "jugend"}, f"Unexpected prose index entry leaked into TeX: {sort_key}@{display}"
        assert token_display not in {"mönch", "jugend"}, f"Unexpected prose index entry leaked into TeX: {sort_key}@{display}"
        assert token_sort not in PROSE_RULE_WORDS and token_display not in PROSE_RULE_WORDS, (
            f"Prose/rule-label token leaked into TeX index commands: {sort_key}@{display}"
        )

    included_explicit_rows = [row for row in main_rows if row.get("source_scope") == "explicit_tag"]
    assert included_explicit_rows, "Expected at least one printable explicit-tag row."
    assert any(index_command(row) in tex_text for row in included_explicit_rows), "No printable explicit-tag command found in TeX."

    assert r"\printindex[iv]" in tex_text, "Missing unified \\printindex[iv] command in TeX."

    for language in ("greek", "skt", "lat"):
        language_rows = [row for row in included_explicit_rows if row.get("language") == language]
        if language_rows:
            assert any(index_command(row) in tex_text for row in language_rows), f"Missing explicit {language} index commands in TeX."

    assert "Modern English linguistic forms" not in tex_text
    assert r"\makeindex[name=iv,title={},columns=3]" in tex_text, "Missing unified \\makeindex[name=iv] declaration in TeX."
    assert r"\chapter*{Old English}" not in tex_text
    assert r"\chapter*{Proto-Germanic}" not in tex_text

    ordinary_oe_target = require_row(
        main_rows,
        lambda row: row.get("language") == "oe"
        and row.get("form_role") == "target_form"
        and row.get("source_scope") == "lexical_heading"
        and not row.get("display", "").startswith("*"),
        "ordinary OE target",
    )
    source_backed_pgmc = require_row(
        main_rows,
        lambda row: row.get("language") == "pgmc"
        and row.get("form_role") == "source_protoform"
        and row.get("source_scope") == "lexical_protoform",
        "source-backed PGmc protoform",
    )
    reconstructed_oe_target = require_row(
        main_rows,
        lambda row: row.get("language") == "oe"
        and row.get("form_role") == "target_form"
        and row.get("source_scope") == "lexical_heading"
        and row.get("display", "").startswith("*"),
        "reconstructed OE target",
    )
    for label, row in (
        ("ordinary OE target", ordinary_oe_target),
        ("source-backed PGmc protoform", source_backed_pgmc),
        ("reconstructed OE target", reconstructed_oe_target),
    ):
        command = index_command(row)
        assert command in tex_text, f"Missing expected TeX index command for {label}: {command}"

    print("book draft tex index policy checks passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_EXCLUDED_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_excluded.tsv"
DEFAULT_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def latex_escape(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


def index_command(row: dict[str, str]) -> str:
    language = row.get("language", "")
    sort_key = row.get("sort_key", "")
    display = row.get("display", "")
    return rf"\index[{language}]{{{latex_escape(sort_key)}@{latex_escape(display)}}}"


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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, default=DEFAULT_TEX_PATH)
    args = parser.parse_args()

    tex_path = args.tex_path.expanduser().resolve()
    tex_text = tex_path.read_text(encoding="utf-8")
    main_rows = load_rows(PRINT_MAIN_PATH)
    excluded_rows = load_rows(PRINT_EXCLUDED_PATH)
    main_commands = {index_command(row) for row in main_rows}

    main_explicit_keys = {
        explicit_key(row)
        for row in main_rows
        if row.get("source_scope") == "explicit_tag"
    }

    assert r"\index[preoe]{" not in tex_text, "Generated TeX must not emit preoe index commands."

    for row in excluded_rows:
        if row.get("source_scope") != "explicit_tag" or row.get("form_role") != "regular_output":
            continue
        if explicit_key(row) in main_explicit_keys:
            continue
        command = index_command(row)
        if command in main_commands:
            continue
        assert command not in tex_text, f"Excluded explicit regular_output leaked into TeX: {command}"

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

    included_explicit_rows = [row for row in main_rows if row.get("source_scope") == "explicit_tag"]
    assert included_explicit_rows, "Expected at least one printable explicit-tag row."
    assert any(index_command(row) in tex_text for row in included_explicit_rows), "No printable explicit-tag command found in TeX."

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

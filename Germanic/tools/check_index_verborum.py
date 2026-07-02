#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

from build_index_verborum import (
    INTRO_PATH,
    OVERRIDES_PATH,
    build_audit_rows,
    build_production_rows,
    explicit_tag_occurrences,
    load_overrides,
    transliterate_sort_key,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"


def assert_sort_keys() -> None:
    assert transliterate_sort_key("þanc") == "thanc"
    assert transliterate_sort_key("bæþ") == "baeth"
    assert transliterate_sort_key("bǣr") == "baer"
    assert transliterate_sort_key("ġiefan") == "giefan"
    assert transliterate_sort_key("sċuldrum") == "sculdrum"


def assert_explicit_tags() -> None:
    tags = explicit_tag_occurrences()
    refs = {(row["display"], row["language"], row["source_ref"]) for row in tags}
    assert ("sċuldrum", "oe", f"{INTRO_PATH.relative_to(REPO_ROOT).as_posix()}:61") in refs
    assert ("*skúldramiz", "pgmc", f"{INTRO_PATH.relative_to(REPO_ROOT).as_posix()}:97") in refs


def assert_production_rows() -> None:
    rows = build_production_rows()
    keys = {(row.display, row.language, row.source_scope, row.source_ref) for row in rows}
    assert ("bacan", "oe", "lexical_heading", "bake — OE bacan") in keys
    assert ("*θánkijaną", "pgmc", "lexical_protoform", "think — OE þenċan") in keys
    assert ("sċuldrum", "oe", "explicit_tag", f"{INTRO_PATH.relative_to(REPO_ROOT).as_posix()}:61") in keys


def assert_written_table_schema() -> None:
    with FORMS_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == ["language", "form", "display", "sort_key", "source_scope", "source_ref", "origin", "status"]
        first_rows = list(reader)[:10]
    assert all(row["language"] for row in first_rows)
    assert all(row["status"] in {"auto", "override"} for row in first_rows)


def assert_ignore_override_behavior() -> None:
    add_overrides, ignore_overrides = load_overrides()
    assert add_overrides == []
    assert ignore_overrides == []
    rows = build_production_rows()
    audit = build_audit_rows(rows)
    needs_review = {entry["form"] for entry in audit.get("needs_review", [])}
    assert "sċuldrum" not in needs_review


def main() -> None:
    assert_sort_keys()
    assert_explicit_tags()
    assert_production_rows()
    assert_written_table_schema()
    assert_ignore_override_behavior()
    print("index verborum checks passed")


if __name__ == "__main__":
    main()

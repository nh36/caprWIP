#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

from build_index_verborum import (
    INTRO_PATH,
    CandidateOccurrence,
    add_production,
    build_audit_rows,
    build_production_rows,
    compare_against_baseline,
    explicit_tag_occurrences,
    load_unresolved_baseline,
    transliterate_sort_key,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
BASELINE_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_unresolved_baseline.tsv"


def assert_sort_keys() -> None:
    assert transliterate_sort_key("þanc") == "thanc"
    assert transliterate_sort_key("bæþ") == "baeth"
    assert transliterate_sort_key("bǣr") == "baer"
    assert transliterate_sort_key("ġiefan") == "giefan"
    assert transliterate_sort_key("sċuldrum") == "sculdrum"


def assert_explicit_tags() -> None:
    tags = explicit_tag_occurrences()
    rel = INTRO_PATH.relative_to(REPO_ROOT).as_posix() + ":"
    assert any(row["display"] == "sċuldrum" and row["language"] == "oe" and row["source_ref"].startswith(rel) for row in tags)
    assert any(row["display"] == "*skúldramiz" and row["language"] == "pgmc" and row["source_ref"].startswith(rel) for row in tags)


def assert_production_rows() -> None:
    rows = build_production_rows()
    keys = {(row.display, row.language, row.source_scope, row.source_ref) for row in rows}
    assert ("bacan", "oe", "lexical_heading", "bake — OE bacan") in keys
    assert ("*θánkijaną", "pgmc", "lexical_protoform", "think — OE þenċan") in keys
    rel = INTRO_PATH.relative_to(REPO_ROOT).as_posix() + ":"
    assert any(row.display == "sċuldrum" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith(rel) for row in rows)


def assert_written_table_schema() -> None:
    with FORMS_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == ["language", "form", "display", "sort_key", "source_scope", "source_ref", "origin", "status"]
        first_rows = list(reader)[:10]
    assert all(row["language"] for row in first_rows)
    assert all(row["status"] in {"auto", "override"} for row in first_rows)


def assert_overrides_load() -> None:
    with (REPO_ROOT / "Germanic/docs/book/index_verborum_overrides.tsv").open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
    assert any(row["action"] == "add" for row in rows)
    assert any(row["action"] == "ignore" for row in rows)


def assert_add_override_behavior() -> None:
    store: dict[tuple[str, str, str, str, str], object] = {}
    add_production(
        store,
        language="on",
        form="báðir",
        display="báðir",
        sort_key=transliterate_sort_key("báðir"),
        source_scope="override_add_test",
        source_ref="synthetic:on:1",
        origin="override",
        status="override",
    )
    assert any(getattr(row, "display", "") == "báðir" and getattr(row, "language", "") == "on" for row in store.values())


def assert_ignore_override_behavior() -> None:
    rows = build_production_rows()
    synthetic = CandidateOccurrence(
        form="attestation",
        source_ref="synthetic:model:1",
        source_path="synthetic/model.md",
        line_no=1,
        heading="### Old English evidence",
        line_text="attestation",
    )
    ignore_overrides = [{"action": "ignore", "form": "attestation", "source_ref": "synthetic:model:1"}]
    audit = build_audit_rows(rows, candidates=[synthetic], ignore_overrides=ignore_overrides)
    assert audit.get("needs_review", []) == []
    assert audit.get("ignored_by_override", []) and audit["ignored_by_override"][0]["form"] == "attestation"


def assert_baseline_strictness() -> None:
    rows = build_production_rows()
    audit = build_audit_rows(rows)
    needs_review = audit.get("needs_review", [])
    baseline = load_unresolved_baseline(BASELINE_PATH)
    new_entries, _ = compare_against_baseline(needs_review, baseline)
    assert new_entries == []

    synthetic_entries = list(needs_review) + [
        {
            "form": "synthetic-form",
            "source_ref": "synthetic.md:1",
            "category": "likely_pgmc",
            "sort_key": "syntheticform",
        }
    ]
    new_entries, _ = compare_against_baseline(synthetic_entries, baseline)
    assert any(entry["form"] == "synthetic-form" for entry in new_entries)


def main() -> None:
    assert_sort_keys()
    assert_explicit_tags()
    assert_production_rows()
    assert_written_table_schema()
    assert_overrides_load()
    assert_add_override_behavior()
    assert_ignore_override_behavior()
    assert_baseline_strictness()
    print("index verborum checks passed")


if __name__ == "__main__":
    main()

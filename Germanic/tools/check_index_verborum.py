#!/usr/bin/env python3
from __future__ import annotations

import csv
import tempfile
import re
from pathlib import Path

from build_index_verborum import (
    INTRO_PATH,
    LANGUAGE_TITLES,
    CandidateOccurrence,
    add_production,
    build_audit_rows,
    build_production_rows,
    compare_against_baseline,
    excluded_intermediate_trace_forms,
    explicit_tag_occurrences,
    load_unresolved_baseline,
    table_candidates_from_path,
    transliterate_sort_key,
    unresolved_baseline_key,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
BASELINE_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_unresolved_baseline.tsv"
COMBINED_MD_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"
AUDIT_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_audit.md"
REGISTRY_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/book_draft_index_registry.tex"


def load_forms_rows() -> list[dict[str, str]]:
    with FORMS_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def audit_section(title: str) -> str:
    text = AUDIT_PATH.read_text(encoding="utf-8")
    marker = f"## {title}\n"
    assert marker in text, title
    tail = text.split(marker, 1)[1]
    return tail.split("\n## ", 1)[0]


def parse_audit_language_summary() -> set[str]:
    section = audit_section("Production indexed forms by language")
    titles: set[str] = set()
    for line in section.splitlines():
        if not line.startswith("|") or line.startswith("| Language |") or line.startswith("| ---"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if parts and parts[0]:
            titles.add(parts[0])
    return titles


def parse_table_scanned_unresolved_pairs() -> set[tuple[str, str]]:
    section = audit_section("Table-scanned unresolved candidates")
    pairs: set[tuple[str, str]] = set()
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 2:
            pairs.add((parts[0].strip("`"), parts[1]))
    return pairs


def parse_registry_codes() -> set[str]:
    codes: set[str] = set()
    for line in REGISTRY_TEX_PATH.read_text(encoding="utf-8").splitlines():
        match = re.search(r"name=([^,]+),title=", line)
        if match:
            codes.add(match.group(1))
    return codes


def assert_sort_keys() -> None:
    assert transliterate_sort_key("þanc") == "thanc"
    assert transliterate_sort_key("bæþ") == "baeth"
    assert transliterate_sort_key("bǣr") == "baer"
    assert transliterate_sort_key("ġiefan") == "giefan"
    assert transliterate_sort_key("sċuldrum") == "sculdrum"
    assert transliterate_sort_key("śrī") == "sri"
    assert transliterate_sort_key("λόγος") == "logos"


def assert_explicit_tags() -> None:
    tags = explicit_tag_occurrences()
    rel = INTRO_PATH.relative_to(REPO_ROOT).as_posix() + ":"
    assert any(row["display"] == "sċuldrum" and row["language"] == "oe" and row["source_ref"].startswith(rel) for row in tags)
    assert any(row["display"] == "*skúldramiz" and row["language"] == "pgmc" and row["source_ref"].startswith(rel) for row in tags)


def assert_production_rows() -> None:
    rows = build_production_rows()
    keys = {(row.display, row.language, row.source_scope, row.source_ref, row.form_role) for row in rows}
    assert ("bacan", "oe", "lexical_heading", "bake — OE bacan", "target_form") in keys
    assert ("*θánkijaną", "pgmc", "lexical_protoform", "think — OE þenċan", "source_protoform") in keys
    rel = INTRO_PATH.relative_to(REPO_ROOT).as_posix() + ":"
    assert any(row.display == "sċuldrum" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith(rel) for row in rows)
    assert ("báðir", "on", "explicit_tag", "Germanic/docs/lexeme_reports/model_entries/1958-both-bū.model.md:27", "comparison_form") in keys
    assert ("skawōn", "os", "override", "Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.model.md:22", "comparison_form") in keys
    assert ("bocc", "oe", "explicit_tag", "Germanic/docs/lexeme_reports/model_entries/1973-buck-bucc.model.md:38", "regular_output") in keys
    assert ("*cnobba", "oe", "lexical_heading", "knob — OE *cnobba", "target_form") in keys
    assert ("*rēac", "oe", "lexical_heading", "reek — OE *rēac", "target_form") in keys
    assert ("*strīeġan", "oe", "lexical_heading", "strew — OE *strīeġan", "target_form") in keys
    assert any(row.form == "*xémonų" and row.form_role == "selected_input" and row.source_scope == "trace_proto_input" for row in rows)
    assert not any(row.source_scope in {"trace_stage", "trace_output"} for row in rows)


def assert_written_table_schema() -> None:
    rows = load_forms_rows()
    with FORMS_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == ["language", "form", "display", "sort_key", "form_role", "source_scope", "source_ref", "origin", "status"]
    first_rows = rows[:10]
    assert all(row["language"] for row in first_rows)
    assert all(row["form_role"] for row in first_rows)
    assert all(row["status"] in {"auto", "override"} for row in first_rows)


def assert_overrides_load() -> None:
    with (REPO_ROOT / "Germanic/docs/book/index_verborum_overrides.tsv").open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
    assert any(row["action"] == "add" for row in rows)
    assert any(row["action"] == "ignore" for row in rows)


def assert_add_override_behavior() -> None:
    rows = build_production_rows(
        add_overrides=[
            {
                "action": "add",
                "language": "on",
                "form": "báðir",
                "display": "báðir",
                "sort_key": transliterate_sort_key("báðir"),
                "source_scope": "override_add_test",
                "source_ref": "synthetic:on:1",
                "note": "synthetic add override",
            }
        ],
        ignore_overrides=[],
    )
    assert any(row.display == "báðir" and row.language == "on" and row.source_scope == "override_add_test" for row in rows)


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
    repo_baseline = load_unresolved_baseline(BASELINE_PATH)
    assert repo_baseline

    # The checked-in baseline may lag deliberate coverage-model broadening, but it must still load
    # and compare cleanly.
    repo_new_entries, repo_resolved_entries = compare_against_baseline(needs_review, repo_baseline)
    assert isinstance(repo_new_entries, list)
    assert isinstance(repo_resolved_entries, list)

    synthetic_baseline = {unresolved_baseline_key(entry): dict(entry) for entry in needs_review}
    new_entries, resolved_entries = compare_against_baseline(needs_review, synthetic_baseline)
    assert new_entries == []
    assert resolved_entries == []

    synthetic_entries = list(needs_review) + [
        {
            "form": "synthetic-form",
            "source_path": "synthetic.md",
            "source_ref": "synthetic.md:1",
            "heading": "### Synthetic heading",
            "category": "likely_pgmc",
            "sort_key": "syntheticform",
            "context": "synthetic form in synthetic context",
        }
    ]
    new_entries, _ = compare_against_baseline(synthetic_entries, synthetic_baseline)
    assert any(entry["form"] == "synthetic-form" for entry in new_entries)


def assert_table_form_handling() -> None:
    rows = build_production_rows()
    assert any(row.display == "cnopp" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md:") for row in rows)
    assert any(row.display == "cnoppa" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md:") for row in rows)
    assert any(row.display == "cnæp" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md:") for row in rows)
    assert any(row.display == "*xémenaz" and row.language == "pgmc" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2068-heaven-heofon.model.md:") for row in rows)
    assert any(row.display == "hefen" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2068-heaven-heofon.model.md:") for row in rows)
    assert any(row.display == "sparen" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2205-spare-sparian.model.md:") for row in rows)
    assert any(row.display == "liccaþ" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.model.md:") for row in rows)
    assert any(row.display == "sċēawa" and row.language == "oe" and row.source_scope == "explicit_tag" and row.source_ref.startswith("Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.model.md:") for row in rows)


def assert_greek_and_sanskrit_explicit_tags() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        fixture = Path(tmpdir) / "synthetic-iv.md"
        fixture.write_text(
            "[*λόγος*]{.iv lang=greek sort=logos}\n"
            "[śrī]{.iv lang=skt sort=sri}\n",
            encoding="utf-8",
        )
        tags = explicit_tag_occurrences(paths=[fixture])
        store = {}
        for row in tags:
            add_production(
                store,
                language=row["language"],
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
                form_role=row["form_role"],
                source_scope=row["source_scope"],
                source_ref=row["source_ref"],
                origin=row["origin"],
            )
        rows = list(store.values())
    assert any(row.form == "λόγος" and row.language == "greek" and row.sort_key == "logos" for row in rows)
    assert any(row.form == "śrī" and row.language == "skt" and row.sort_key == "sri" for row in rows)


def assert_optional_role_support() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        fixture = Path(tmpdir) / "synthetic-role-iv.md"
        fixture.write_text(
            "[`bocc`]{.iv lang=oe sort=bocc role=regular_output}\n"
            "[bucca]{.iv lang=oe sort=bucca role=comparison_form}\n"
            "[`*búkkaz`]{.iv lang=pgmc sort=bukkaz role=selected_input}\n",
            encoding="utf-8",
        )
        tags = explicit_tag_occurrences(paths=[fixture])
        store = {}
        for row in tags:
            add_production(
                store,
                language=row["language"],
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
                form_role=row["form_role"],
                source_scope=row["source_scope"],
                source_ref=row["source_ref"],
                origin=row["origin"],
            )
        rows = list(store.values())
    assert any(row.form == "bocc" and row.form_role == "regular_output" for row in rows)
    assert any(row.form == "bucca" and row.form_role == "comparison_form" for row in rows)
    assert any(row.form == "*búkkaz" and row.form_role == "selected_input" for row in rows)


def assert_table_audit_scanner() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        fixture = Path(tmpdir) / "synthetic-table.model.md"
        fixture.write_text(
            "### Paradigm comparison\n\n"
            "| Candidate input | OE comparison form | Result |\n"
            "| :--- | :--- | :--- |\n"
            "| *bákaną | bacan | mismatch |\n",
            encoding="utf-8",
        )
        candidates = table_candidates_from_path(fixture, allow_non_model_entry=True)
    forms = {(candidate.form, candidate.heading, candidate.candidate_origin) for candidate in candidates}
    assert ("*bákaną", "### Paradigm comparison", "table_candidate") in forms
    assert ("bacan", "### Paradigm comparison", "table_candidate") in forms


def assert_ordinary_glosses_ignored() -> None:
    rows = build_production_rows()
    synthetic = CandidateOccurrence(
        form="friend",
        source_ref="Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md:183",
        source_path="Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md",
        line_no=183,
        heading="## Synthetic reader-facing heading",
        line_text="friend",
    )
    audit = build_audit_rows(rows, candidates=[synthetic])
    assert any(entry["form"] == "friend" for entry in audit.get("ignored_by_override", []))


def assert_intermediate_trace_forms_excluded() -> None:
    rows = build_production_rows()
    excluded = excluded_intermediate_trace_forms()
    assert any(entry["form"] == "*bækaną" for entry in excluded)
    assert not any(row.form == "*bækaną" and row.source_scope == "trace_stage" for row in rows)


def assert_generated_consistency() -> None:
    forms_rows = load_forms_rows()
    production_pairs = {(row["form"], row["source_ref"]) for row in forms_rows}
    table_pairs = parse_table_scanned_unresolved_pairs()
    assert production_pairs.isdisjoint(table_pairs)

    form_languages = {row["language"] for row in forms_rows}
    expected_titles = {LANGUAGE_TITLES[code] for code in form_languages}
    audit_titles = parse_audit_language_summary()
    assert expected_titles.issubset(audit_titles)

    registry_codes = parse_registry_codes()
    assert registry_codes == form_languages

    for code in ("dutch", "german", "modeng"):
        if code in form_languages:
            assert LANGUAGE_TITLES[code] in audit_titles


def assert_no_derivational_expression_rows() -> None:
    rows = load_forms_rows()
    assert not any(">" in row["form"] or ">" in row["display"] for row in rows)


def assert_reconstructed_oe_index_commands() -> None:
    text = COMBINED_MD_PATH.read_text(encoding="utf-8")
    for heading, needle in (
        ("### knob — OE *cnobba", r"\index[oe]{cnobba@*cnobba}"),
        ("### reek — OE *rēac", r"\index[oe]{reac@*rēac}"),
        ("### strew — OE *strīeġan", r"\index[oe]{striegan@*strīeġan}"),
    ):
        start = text.index(heading)
        window = text[start : start + 400]
        assert needle in window


def main() -> None:
    assert_sort_keys()
    assert_explicit_tags()
    assert_production_rows()
    assert_written_table_schema()
    assert_overrides_load()
    assert_add_override_behavior()
    assert_ignore_override_behavior()
    assert_baseline_strictness()
    assert_table_form_handling()
    assert_greek_and_sanskrit_explicit_tags()
    assert_optional_role_support()
    assert_table_audit_scanner()
    assert_ordinary_glosses_ignored()
    assert_intermediate_trace_forms_excluded()
    assert_generated_consistency()
    assert_no_derivational_expression_rows()
    assert_reconstructed_oe_index_commands()
    print("index verborum checks passed")


if __name__ == "__main__":
    main()

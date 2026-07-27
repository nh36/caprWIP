#!/usr/bin/env python3
from __future__ import annotations

import csv
import tempfile
import re
from pathlib import Path

from build_index_verborum import (
    ALLOWED_FORM_ROLES,
    INTRO_PATH,
    LANGUAGE_TITLES,
    TABLE_STOPWORDS,
    CandidateOccurrence,
    add_production,
    broad_prose_notation_reason,
    build_audit_rows,
    build_production_rows,
    compare_against_baseline,
    excluded_intermediate_trace_forms,
    explicit_tag_occurrences,
    infer_broad_prose_language,
    infer_broad_prose_suggestion,
    load_broad_prose_decisions,
    load_print_decisions,
    load_table_decisions,
    load_unresolved_baseline,
    split_print_main_rows,
    table_candidates_from_path,
    transliterate_sort_key,
    unresolved_baseline_key,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_EXCLUDED_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_excluded.tsv"
PRINT_UNIQUE_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_unique.tsv"
PRINT_ANOMALIES_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_anomalies.tsv"
PREOE_REVIEW_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_preoe_review.tsv"
PRINT_DECISIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_decisions.tsv"
READER_FACING_EXAMPLE_PATH = REPO_ROOT / "Germanic/docs/book/reader_facing_example_forms.tsv"
BASELINE_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_unresolved_baseline.tsv"
COMBINED_MD_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"
BUILDER_PATH = REPO_ROOT / "Germanic/docs/assembly/build_capr_book_draft.py"
BOOK_DRAFT_DOCKER_BUILD_PATH = REPO_ROOT / "Germanic/docs/assembly/build_capr_book_draft_docker.sh"
AUDIT_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_audit.md"
PRINT_AUDIT_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_audit.md"
REGISTRY_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/book_draft_index_registry.tex"
FILTER_LUA_PATH = REPO_ROOT / "Germanic/tools/index_verborum_filter.lua"
PDF_HEADER_PATH = REPO_ROOT / "Germanic/docs/assembly/book_draft_pdf_header.tex"
SUGGESTIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_table_suggestions.tsv"
BROAD_SUGGESTIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_broad_prose_suggestions.tsv"
DECISIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_table_decisions.tsv"
BROAD_DECISIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_broad_prose_decisions.tsv"


def load_forms_rows() -> list[dict[str, str]]:
    with FORMS_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_print_main_rows() -> list[dict[str, str]]:
    with PRINT_MAIN_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_print_excluded_rows() -> list[dict[str, str]]:
    with PRINT_EXCLUDED_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_print_unique_rows() -> list[dict[str, str]]:
    with PRINT_UNIQUE_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_print_anomaly_rows() -> list[dict[str, str]]:
    with PRINT_ANOMALIES_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_preoe_review_rows() -> list[dict[str, str]]:
    with PREOE_REVIEW_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_reader_facing_example_rows() -> list[dict[str, str]]:
    with READER_FACING_EXAMPLE_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_suggestion_rows() -> list[dict[str, str]]:
    with SUGGESTIONS_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_broad_suggestion_rows() -> list[dict[str, str]]:
    with BROAD_SUGGESTIONS_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def audit_section(title: str) -> str:
    text = AUDIT_PATH.read_text(encoding="utf-8")
    marker = f"## {title}\n"
    assert marker in text, title
    tail = text.split(marker, 1)[1]
    return tail.split("\n## ", 1)[0]


def parse_audit_language_summary() -> set[str]:
    section_title = "Internal production forms by language"
    if f"## {section_title}\n" not in AUDIT_PATH.read_text(encoding="utf-8"):
        section_title = "Production indexed forms by language"
    section = audit_section(section_title)
    titles: set[str] = set()
    for line in section.splitlines():
        if not line.startswith("|") or line.startswith("| Language |") or line.startswith("| ---"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if parts and parts[0]:
            titles.add(parts[0])
    return titles


def parse_printed_audit_language_summary() -> set[str]:
    section = audit_section("Printed main-index forms by language")
    titles: set[str] = set()
    for line in section.splitlines():
        if not line.startswith("|") or line.startswith("| Language |") or line.startswith("| ---"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if parts and parts[0]:
            titles.add(parts[0])
    return titles


def parse_audit_summary_lines() -> set[str]:
    lines = set()
    started = False
    for line in AUDIT_PATH.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            if started:
                break
            continue
        if line.startswith("- "):
            started = True
            lines.add(line)
    return lines


def parse_audit_table_semantic_notation_pairs() -> set[tuple[str, str]]:
    section = audit_section("Table semantic notation / compound expressions")
    pairs: set[tuple[str, str]] = set()
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 2:
            pairs.add((parts[0].strip("`"), parts[1]))
    return pairs


def parse_audit_table_semantic_ignored_pairs() -> set[tuple[str, str]]:
    section = audit_section("Table semantic ignored")
    pairs: set[tuple[str, str]] = set()
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 2:
            pairs.add((parts[0].strip("`"), parts[1]))
    return pairs


def parse_audit_bucket_pairs(title: str) -> set[tuple[str, str]]:
    section = audit_section(title)
    pairs: set[tuple[str, str]] = set()
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 2:
            pairs.add((parts[0].strip("`"), parts[1]))
    return pairs


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


def parse_table_scanned_unresolved_forms() -> set[str]:
    return {form for form, _ in parse_table_scanned_unresolved_pairs()}


def parse_registry_codes() -> set[str]:
    codes: set[str] = set()
    for line in REGISTRY_TEX_PATH.read_text(encoding="utf-8").splitlines():
        match = re.search(r"name=([^,]+),title=", line)
        if match:
            codes.add(match.group(1))
    return codes


def parse_registry_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    for line in REGISTRY_TEX_PATH.read_text(encoding="utf-8").splitlines():
        match = re.search(r"name=([^,]+),title=\{([^}]*)\}", line)
        if match:
            titles[match.group(1)] = match.group(2)
    return titles


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


def assert_table_decisions_load() -> None:
    assert DECISIONS_PATH.exists()
    rows = load_table_decisions()
    assert rows
    assert any(row["action"] == "accept" for row in rows)
    assert any(row["action"] == "defer" for row in rows)
    assert any(row["action"] == "ignore" for row in rows)


def assert_broad_decisions_load() -> None:
    assert BROAD_DECISIONS_PATH.exists()
    rows = load_broad_prose_decisions()
    assert rows
    assert any(row["action"] == "accept" for row in rows)
    assert any(row["action"] == "defer" for row in rows)
    assert any(row["action"] == "ignore" for row in rows)


def assert_broad_suggestions_load() -> None:
    assert BROAD_SUGGESTIONS_PATH.exists()
    rows = load_broad_suggestion_rows()
    assert rows
    assert any(row["form"] == "giefan" and row["suggested_language"] == "oe" for row in rows)
    assert not any(row["source_ref"] == "Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model.md:29" and row["form"] == "duru" for row in rows)
    assert not any(row["source_ref"] == "Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md:53" and row["form"] in {"Jugend", "Mönch"} for row in rows)
    for form, source_ref in {
        ("*flēoganą", "Germanic/docs/lexeme_reports/model_entries/2022-fly-flēogan.model.md:33"),
        ("*gánga", "Germanic/docs/lexeme_reports/model_entries/2038-gang-gang.model.md:33"),
        ("*búrdi", "Germanic/docs/lexeme_reports/model_entries/1951-birth-byrd.model.md:33"),
    }:
        assert not any(
            row["form"] == form
            and row["source_ref"] == source_ref
            and row["suggested_language"] == "pgmc"
            and row["suggested_role"] == "source_protoform"
            for row in rows
        )


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
    assert isinstance(repo_baseline, dict)
    assert repo_baseline == {}
    assert len(BASELINE_PATH.read_text(encoding="utf-8").splitlines()) == 1

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
            "| *bákaną | bacan | mismatch |\n"
            "| attested | Ritual | note |\n",
            encoding="utf-8",
        )
        candidates = table_candidates_from_path(fixture, allow_non_model_entry=True)
    forms = {(candidate.form, candidate.heading, candidate.candidate_origin) for candidate in candidates}
    assert ("*bákaną", "### Paradigm comparison", "table_candidate") in forms
    assert ("bacan", "### Paradigm comparison", "table_candidate") in forms
    assert ("attested", "### Paradigm comparison", "table_candidate") not in forms
    assert ("Ritual", "### Paradigm comparison", "table_candidate") not in forms


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


def assert_already_indexed_nearby_bucket() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        fixture = Path(tmpdir) / "synthetic-nearby.md"
        fixture.write_text(
            "### Old English evidence\n"
            "[cniht]{.iv lang=oe sort=cniht role=target_form}\n"
            "cniht\n",
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
        synthetic = CandidateOccurrence(
            form="cniht",
            source_ref=f"{fixture.as_posix()}:3",
            source_path=fixture.as_posix(),
            line_no=3,
            heading="### Old English evidence",
            line_text="cniht",
            candidate_origin="broad_prose_candidate",
        )
        audit = build_audit_rows(list(store.values()), candidates=[synthetic], ignore_overrides=[])
    assert any(entry["form"] == "cniht" for entry in audit.get("already_indexed_nearby", []))


def assert_intermediate_trace_forms_excluded() -> None:
    rows = build_production_rows()
    excluded = excluded_intermediate_trace_forms()
    assert any(entry["form"] == "*bækaną" for entry in excluded)
    assert not any(row.form == "*bækaną" and row.source_scope == "trace_stage" for row in rows)


def assert_generated_consistency() -> None:
    forms_rows = load_forms_rows()
    print_rows = load_print_main_rows()
    production_pairs = {(row["form"], row["source_ref"]) for row in forms_rows}
    table_pairs = parse_table_scanned_unresolved_pairs()
    assert production_pairs.isdisjoint(table_pairs)

    form_languages = {row["language"] for row in forms_rows}
    expected_titles = {LANGUAGE_TITLES[code] for code in form_languages}
    audit_titles = parse_audit_language_summary()
    assert expected_titles.issubset(audit_titles)
    print_languages = {row["language"] for row in print_rows}
    printed_titles = parse_printed_audit_language_summary()
    expected_printed_titles = {LANGUAGE_TITLES[code] for code in print_languages}
    assert expected_printed_titles.issubset(printed_titles)
    assert LANGUAGE_TITLES["preoe"] not in printed_titles

    registry_codes = parse_registry_codes()
    assert registry_codes == print_languages

    for code in ("dutch", "german", "modeng"):
        if code in form_languages:
            assert LANGUAGE_TITLES[code] in audit_titles
    summary_lines = parse_audit_summary_lines()
    assert "- True remaining unresolved: 0" in summary_lines
    assert "- Table-scanned unresolved candidates: 0" in summary_lines
    assert any(line.startswith("- True remaining unresolved: ") for line in summary_lines)
    assert any(line.startswith("- Table-scanned unresolved candidates: ") for line in summary_lines)
    assert any(line.startswith("- Already indexed in same entry: ") for line in summary_lines)
    assert any(line.startswith("- Broad-prose notation / compound expressions: ") for line in summary_lines)
    assert any(line.startswith("- Broad-prose evidence suggestions: ") for line in summary_lines)
    assert any(line.startswith("- Curated broad-prose deferred: ") for line in summary_lines)
    assert any(line.startswith("- Curated broad-prose ignored: ") for line in summary_lines)
    assert any(line.startswith("- Reader-facing examples quarantined (separate example index policy): ") for line in summary_lines)
    assert any(line.startswith("- Printed main-index occurrences: ") for line in summary_lines)
    assert any(line.startswith("- Printed main-index unique forms: ") for line in summary_lines)
    assert any(line.startswith("- Print-excluded occurrences: ") for line in summary_lines)
    assert any(line.startswith("- Print-excluded unique forms: ") for line in summary_lines)
    assert any(line.startswith("- Print exclusions (preoe_model_internal_default_exclusion): ") for line in summary_lines)
    assert any(line.startswith("- Print exclusions (regular_output_default_exclusion): ") for line in summary_lines)
    assert any(line.startswith("- Print exclusions (reader_facing_pedagogical_example): ") for line in summary_lines)
    assert any(line.startswith("- Print exclusions (deferred_by_print_decision): ") for line in summary_lines)
    assert any(line.startswith("- Print exclusions (excluded_by_print_decision): ") for line in summary_lines)
    assert any(line.startswith("- Internal-only rows (preoe_model_internal_default_exclusion): ") for line in summary_lines)
    assert any(line.startswith("- Internal-only rows (regular_output_default_exclusion): ") for line in summary_lines)
    assert any(line.startswith("- Internal-only rows (reader_facing_pedagogical_example): ") for line in summary_lines)
    assert any(line.startswith("- Internal-only rows (deferred_by_print_decision): ") for line in summary_lines)
    assert any(line.startswith("- Internal-only rows (excluded_by_print_decision): ") for line in summary_lines)
    assert any(line.startswith("- Pre-OE review rows: ") for line in summary_lines)
    assert any(line.startswith("- Reader-facing example candidate rows: ") for line in summary_lines)
    assert any(line.startswith("- Reader-facing rows include_in_example_index=yes: ") for line in summary_lines)
    assert any(line.startswith("- Reader-facing rows include_in_example_index=no: ") for line in summary_lines)
    assert any(line.startswith("- Ordinary prose/gloss ignored: ") for line in summary_lines)
    assert any(line.startswith("- Orthographic/normalization variants: ") for line in summary_lines)
    assert any(line.startswith("- Table semantic deferred decisions: ") for line in summary_lines)
    assert any(line.startswith("- Already indexed nearby: ") for line in summary_lines)


def assert_no_derivational_expression_rows() -> None:
    rows = load_forms_rows()
    assert not any(">" in row["form"] or ">" in row["display"] for row in rows)


def assert_table_semantic_rows() -> None:
    forms_rows = load_forms_rows()
    suggestion_rows = load_suggestion_rows()
    table_auto_rows = [row for row in forms_rows if row["source_scope"] == "table_semantic_auto"]
    table_decision_rows = [row for row in forms_rows if row["source_scope"] == "table_semantic_decision"]
    table_rows = table_auto_rows + table_decision_rows
    assert table_auto_rows
    assert table_decision_rows
    for row in table_rows:
        assert row["form_role"] in ALLOWED_FORM_ROLES
        assert row["language"]
        assert row["form_role"]
        assert row["form"].casefold() not in TABLE_STOPWORDS
        assert row["display"].casefold() not in TABLE_STOPWORDS
        assert ">" not in row["form"]
        assert ">" not in row["display"]
        if row["form"].startswith("*") and row["language"] == "oe":
            assert row["form_role"] == "target_form"
    scope_map: dict[tuple[str, str, str, str], set[str]] = {}
    for row in forms_rows:
        key = (row["language"], row["form"], row["form_role"], row["source_ref"])
        scope_map.setdefault(key, set()).add(row["source_scope"])
    assert all(not ({"explicit_tag", "table_semantic_auto"} <= scopes) for scopes in scope_map.values())
    assert all(not ({"explicit_tag", "table_semantic_decision"} <= scopes) for scopes in scope_map.values())
    production_keys = {(row["language"], row["form"], row["form_role"], row["source_ref"]) for row in forms_rows}
    for row in suggestion_rows:
        key = (row["suggested_language"], row["form"], row["suggested_role"], row["source_ref"])
        assert key not in production_keys
    assert not any(row["form"] == "*nēþlō" and row["language"] == "oe" for row in table_rows)
    assert not any(row["form"] == "*nḗdlō" for row in table_rows)
    assert not any(row["form"] == "*lákaną" and row["suggested_language"] == "oe" for row in suggestion_rows)
    assert any(
        row["form"] == "*kráftaz"
        and row["language"] == "pgmc"
        and row["form_role"] == "selected_input"
        and row["source_ref"] == "Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model.md:50"
        for row in table_auto_rows
    )
    assert not any(
        row["form"] == "*kráftaz"
        and row["language"] == "preoe"
        and row["source_ref"] == "Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model.md:50"
        for row in table_rows
    )
    unresolved_pairs = parse_table_scanned_unresolved_pairs()
    assert unresolved_pairs == set()
    unresolved_forms = parse_table_scanned_unresolved_forms()
    for label in {"OE", "ON", "OHG", "OS", "OFri", "Goth", "PGmc", "PWGmc", "NWGmc", "pre-OE"}:
        assert label not in unresolved_forms
    notation_pairs = parse_audit_table_semantic_notation_pairs()
    assert any(form == "*fōr ~ *fun-" for form, _ in notation_pairs)
    assert any(form == "*watar-~*watan-" for form, _ in notation_pairs)
    ignored_pairs = parse_audit_table_semantic_ignored_pairs()
    for form in {"*kōz", "*kūi", "*kūiz", "*nasō", "*núsō"}:
        assert not any(pair_form == form for pair_form, _ in ignored_pairs)
    assert ("stefn", "Germanic/docs/lexeme_reports/model_entries/2216-stem-stefn.model.md:62") in ignored_pairs

    def auto_or_suggest(form: str, role: str) -> bool:
        return (
            any(row["form"] == form and row["form_role"] == role for row in table_rows)
            or any(row["form"] == form and row["suggested_role"] == role for row in suggestion_rows)
        )

    assert auto_or_suggest("*kráftaz", "selected_input")
    assert auto_or_suggest("*lúnganjō", "selected_input")
    assert auto_or_suggest("*xláxjaną", "selected_input")
    for key in {
        ("oe", "creft", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model.md:48"),
        ("oe", "craft", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model.md:49"),
        ("oe", "leornian", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2095-learn-liornian.model.md:63"),
        ("oe", "næfla", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2133-navel-nafola.model.md:60"),
        ("oe", "rast", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2152-rest-ræste.model.md:59"),
        ("oe", "hlæhhan", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2092-laugh-hliehhan.model.md:58"),
        ("oe", "hlehhan", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2092-laugh-hliehhan.model.md:58"),
        ("oe", "nasu", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2143-nose-nosu.model.md:59"),
    }:
        assert key in production_keys
    for key in {
        ("oe", "cū", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:65"),
        ("oe", "cā", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:67"),
        ("pgmc", "*kōz", "source_protoform", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:64"),
        ("pgmc", "*kūi", "selected_input", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:66"),
        ("pgmc", "*kūiz", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:67"),
        ("pgmc", "*nasō", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2143-nose-nosu.model.md:59"),
        ("pgmc", "*núsō", "selected_input", "Germanic/docs/lexeme_reports/model_entries/2143-nose-nosu.model.md:60"),
        ("preoe", "*nḗdlō", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/2136-needle-nǣdl.model.md:59"),
    }:
        assert key in {
            (row["suggested_language"], row["form"], row["suggested_role"], row["source_ref"])
            for row in suggestion_rows
        }


def assert_broad_prose_buckets() -> None:
    broad_rows = load_broad_suggestion_rows()
    assert not any(row["form"] == "target" for row in broad_rows)
    assert not any(row["form"].startswith("*") and row["suggested_language"] == "german" for row in broad_rows)

    same_entry_pairs = parse_audit_bucket_pairs("Already indexed in same entry")
    assert ("bōc", "Germanic/docs/lexeme_reports/model_entries/1942-beech-bōc.model.md:25") in same_entry_pairs
    assert ("cræft", "Germanic/docs/lexeme_reports/model_entries/1981-craft-cræft.model.md:31") in same_entry_pairs
    assert ("cȳ", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:34") in same_entry_pairs
    assert ("slǣpan", "Germanic/docs/lexeme_reports/model_entries/2196-sleep-slǣpan.model.md:25") in same_entry_pairs

    notation_pairs = parse_audit_bucket_pairs("Broad-prose notation / compound expressions")
    assert ("*bōk(j)ō-", "Germanic/docs/lexeme_reports/model_entries/1942-beech-bōc.model.md:21") in notation_pairs
    assert ("*budman- ~ *buttman-", "Germanic/docs/lexeme_reports/model_entries/1959-bottom-botm.model.md:22") in notation_pairs
    assert ("*kō- ~ *ku-", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:22") in notation_pairs
    assert ("cū(e), cȳ, cūs", "Germanic/docs/lexeme_reports/model_entries/1980-cow-cȳ.model.md:33") in notation_pairs

    reader_pairs = parse_audit_bucket_pairs("Reader-facing examples quarantined (separate example index policy)")
    reader_source = "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md:"
    for form in {"*bacan", "*fúrxtīnaz", "ġeoc"}:
        assert any(item_form == form and source_ref.startswith(reader_source) for item_form, source_ref in reader_pairs)

    prose_pairs = parse_audit_bucket_pairs("Ordinary prose/gloss ignored")
    intro_source = "Germanic/docs/assembly/capr_book_intro_alpha_01.md:"
    assert any(item_form == "OEIUmlaut" and source_ref.startswith(intro_source) for item_form, source_ref in prose_pairs)
    assert ("sea", "Germanic/docs/lexeme_reports/model_entries/2169-sea-sǣ.model.md:33") in prose_pairs

    variant_pairs = parse_audit_bucket_pairs("Orthographic/normalization variant of indexed form")
    assert ("Boraþ", "Germanic/docs/lexeme_reports/model_entries/2312-bore-(3sg)-boraþ.model.md:29") in variant_pairs
    assert ("Caelf", "Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.model.md:25") in variant_pairs
    assert ("Cealf", "Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.model.md:21") in variant_pairs


def assert_broad_prose_decisions_and_inference() -> None:
    forms_rows = load_forms_rows()
    production_keys = {(row["language"], row["form"], row["form_role"], row["source_ref"]) for row in forms_rows}
    decision_rows = [row for row in forms_rows if row["source_scope"] == "broad_prose_decision"]
    assert decision_rows
    assert not any(row["form"] == "Mönch" for row in forms_rows)
    for key in {
        ("oe", "boc", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1942-beech-bōc.model.md:21"),
        ("oe", "boc", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1942-beech-bōc.model.md:25"),
        ("oe", "duru", "comparison_form", "Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model.md:29"),
        ("pgmc", "*kwedu-2", "source_protoform", "Germanic/docs/lexeme_reports/model_entries/1983-cud-cwedu.model.md:21"),
        ("pgmc", "*dēdiz", "source_protoform", "Germanic/docs/lexeme_reports/model_entries/1987-deed-dǣd.model.md:21"),
    }:
        assert key in production_keys

    scope_map: dict[tuple[str, str, str, str], set[str]] = {}
    for row in forms_rows:
        key = (row["language"], row["form"], row["form_role"], row["source_ref"])
        scope_map.setdefault(key, set()).add(row["source_scope"])
    assert all(not ({"explicit_tag", "broad_prose_decision"} <= scopes) for scopes in scope_map.values())
    broad_rows = load_broad_suggestion_rows()
    for row in broad_rows:
        key = (row["suggested_language"], row["form"], row["suggested_role"], row["source_ref"])
        assert key not in production_keys

    raw_audit = build_audit_rows(build_production_rows())
    raw_suggestions = raw_audit.get("broad_prose_suggestion", [])
    assert any(
        row["form"] == "duru"
        and row["source_ref"] == "Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model.md:29"
        and row["suggested_language"] == "oe"
        and row["suggested_role"] == "comparison_form"
        for row in raw_suggestions
    )
    assert not any(
        row["form"].startswith("*") and row["suggested_language"] == "german"
        for row in raw_suggestions
    )
    synthetic = CandidateOccurrence(
        form="duru",
        source_ref="Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model.md:29",
        source_path="Germanic/docs/lexeme_reports/model_entries/1992-door-dor.model.md",
        line_no=29,
        heading="### Development to Old English",
        line_text="From `*dúrą`, Northwest Germanic u-lowering gives `*dórą`, and heavy-syllable nasal apocope then yields `dor`. The regular development treated in this entry is therefore `*dúrą > dor`; the feminine `duru` belongs to the separate line identified by Kroonen and Ringe-Taylor [@Kroonen2013; @RingeTaylor2014].",
    )
    assert infer_broad_prose_language(synthetic) == "oe"

    chain_line = "From `*fáraną`, Anglo-Frisian brightening first gives `*færaną`, then later yields `faran`."
    source_candidate = CandidateOccurrence(
        form="*fáraną",
        source_ref="synthetic/dev-chain:1",
        source_path="synthetic/dev-chain.model.md",
        line_no=1,
        heading="### Development to Old English",
        line_text=chain_line,
        candidate_origin="broad_prose_candidate",
    )
    intermediate_candidate = CandidateOccurrence(
        form="*færaną",
        source_ref="synthetic/dev-chain:1",
        source_path="synthetic/dev-chain.model.md",
        line_no=1,
        heading="### Development to Old English",
        line_text=chain_line,
        candidate_origin="broad_prose_candidate",
    )
    source_suggestion = infer_broad_prose_suggestion(source_candidate)
    assert source_suggestion is not None and source_suggestion["suggested_role"] == "source_protoform"
    assert infer_broad_prose_suggestion(intermediate_candidate) is None
    assert broad_prose_notation_reason(intermediate_candidate) == "intermediate or model-stage form in development chain"

    curated_ignored_pairs = parse_audit_bucket_pairs("Curated broad-prose ignored")
    assert ("Mönch", "Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md:53") in curated_ignored_pairs
    assert ("Jugend", "Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md:53") in curated_ignored_pairs
    unresolved_false_positive_pairs = parse_audit_bucket_pairs("Likely ordinary-language false positives")
    assert ("Mönch", "Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md:53") not in unresolved_false_positive_pairs
    assert ("Jugend", "Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md:53") not in unresolved_false_positive_pairs


def assert_print_layer_outputs() -> None:
    assert PRINT_MAIN_PATH.exists()
    assert PRINT_EXCLUDED_PATH.exists()
    assert PRINT_UNIQUE_PATH.exists()
    assert PRINT_ANOMALIES_PATH.exists()
    assert PREOE_REVIEW_PATH.exists()
    assert PRINT_DECISIONS_PATH.exists()
    assert READER_FACING_EXAMPLE_PATH.exists()
    assert PRINT_AUDIT_PATH.exists()

    with PRINT_MAIN_PATH.open(encoding="utf-8") as handle:
        main_reader = csv.DictReader(handle, delimiter="\t")
        main_rows = list(main_reader)
        assert main_reader.fieldnames == ["language", "form", "display", "sort_key", "form_role", "source_scope", "source_ref", "origin", "status"]

    with PRINT_EXCLUDED_PATH.open(encoding="utf-8") as handle:
        excluded_reader = csv.DictReader(handle, delimiter="\t")
        excluded_rows = list(excluded_reader)
        assert excluded_reader.fieldnames == [
            "language",
            "form",
            "display",
            "sort_key",
            "form_role",
            "source_scope",
            "source_ref",
            "origin",
            "status",
            "exclusion_reason",
            "decision_action",
            "decision_note",
        ]

    with PRINT_UNIQUE_PATH.open(encoding="utf-8") as handle:
        unique_reader = csv.DictReader(handle, delimiter="\t")
        unique_rows = list(unique_reader)
        assert unique_reader.fieldnames == [
            "language",
            "display",
            "sort_key",
            "occurrence_count",
            "roles",
            "source_scopes",
            "sample_sources",
        ]
        assert unique_rows

    with PRINT_ANOMALIES_PATH.open(encoding="utf-8") as handle:
        anomaly_reader = csv.DictReader(handle, delimiter="\t")
        anomaly_rows = list(anomaly_reader)
        assert anomaly_reader.fieldnames == [
            "language",
            "form",
            "display",
            "sort_key",
            "form_role",
            "source_scope",
            "source_ref",
            "anomaly_flags",
            "hard_error",
            "note",
        ]

    with PREOE_REVIEW_PATH.open(encoding="utf-8") as handle:
        preoe_reader = csv.DictReader(handle, delimiter="\t")
        preoe_rows = list(preoe_reader)
        assert preoe_reader.fieldnames == [
            "form",
            "source_ref",
            "source_scope",
            "form_role",
            "reason_for_current_inclusion",
            "proposed_print_status",
            "note",
        ]

    with READER_FACING_EXAMPLE_PATH.open(encoding="utf-8") as handle:
        reader_examples = csv.DictReader(handle, delimiter="\t")
        example_rows = list(reader_examples)
        assert reader_examples.fieldnames == [
            "source_ref",
            "nearest_heading",
            "form",
            "inferred_language",
            "example_role",
            "main_index_overlap",
            "include_in_example_index",
            "reason",
            "context",
        ]

    forms_rows = load_forms_rows()
    main_keys = {(row["language"], row["form"], row["form_role"], row["source_ref"]) for row in main_rows}
    decisions = load_print_decisions()
    builder_text = BUILDER_PATH.read_text(encoding="utf-8")
    docker_build_text = BOOK_DRAFT_DOCKER_BUILD_PATH.read_text(encoding="utf-8")
    filter_text = FILTER_LUA_PATH.read_text(encoding="utf-8")
    header_text = PDF_HEADER_PATH.read_text(encoding="utf-8")
    registry_titles = parse_registry_titles()
    assert "index_verborum_print_main.tsv" in builder_text
    assert "index_verborum_forms.tsv" not in builder_text
    assert "check_book_draft_tex_indexes.py" in docker_build_text
    assert "check_sound_change_heading_wrapping.py" in docker_build_text
    assert "check_bibliography_sanity.py" in docker_build_text
    assert "check_print_index_ready.py" in docker_build_text
    assert "index_verborum_print_main.tsv" in filter_text
    assert r"\indexsetup{level=\section*,noclearpage}" in header_text
    assert "toclevel" not in header_text
    assert "Old English forms" not in REGISTRY_TEX_PATH.read_text(encoding="utf-8")
    assert "Proto-Germanic forms" not in REGISTRY_TEX_PATH.read_text(encoding="utf-8")
    assert "Modern English linguistic forms" not in REGISTRY_TEX_PATH.read_text(encoding="utf-8")
    if "modeng" in registry_titles:
        assert registry_titles["modeng"] == "Modern English"

    assert not any(row["language"] == "preoe" for row in main_rows)
    assert preoe_rows
    preoe_excluded_rows = [row for row in excluded_rows if row["language"] == "preoe"]
    assert preoe_excluded_rows
    assert all(
        row["exclusion_reason"] in {
            "preoe_model_internal_default_exclusion",
            "excluded_by_print_decision",
            "reader_facing_pedagogical_example",
        }
        for row in preoe_excluded_rows
    )
    assert not any(code == "preoe" for code in parse_registry_codes())
    assert not any(row["source_scope"].startswith("reader_failure_") for row in main_rows)
    assert not any(row["form"] in {"Mönch", "Jugend"} for row in forms_rows)
    assert not any(row["form"] in {"Mönch", "Jugend"} for row in main_rows)

    include_regular_keys = {
        (row.get("language", ""), row.get("form", ""), row.get("form_role", ""), row.get("source_ref", ""))
        for row in decisions
        if row.get("action") == "include_main" and row.get("form_role") == "regular_output"
    }
    for row in main_rows:
        if row["form_role"] == "regular_output":
            key = (row["language"], row["form"], row["form_role"], row["source_ref"])
            assert key in include_regular_keys
    if not include_regular_keys:
        assert not any(row["form_role"] == "regular_output" for row in main_rows)
        assert all("regular_output" not in (row.get("roles") or "") for row in unique_rows)

    for form in {"fogol", "woll", "wylf"}:
        if not any(decision.get("action") == "include_main" and decision.get("form") == form for decision in decisions):
            assert not any(row["form"] == form for row in main_rows)
            assert any(
                row["form"] == form
                and row["form_role"] == "regular_output"
                and row["exclusion_reason"] == "regular_output_default_exclusion"
                for row in excluded_rows
            )

    assert ("pgmc", "*θánkijaną", "source_protoform", "think — OE þenċan") in main_keys
    for language in ("pgmc", "pwgmc", "nwgmc"):
        source_like_rows = [
            row for row in forms_rows
            if row["language"] == language
            and row["form_role"] in {"source_protoform", "selected_input"}
            and not row["source_scope"].startswith("reader_failure_")
        ]
        if source_like_rows:
            assert any(
                (row["language"], row["form"], row["form_role"], row["source_ref"]) in main_keys
                for row in source_like_rows
            )

    assert any(
        row["language"] == "oe"
        and row["source_scope"] == "lexical_heading"
        and row["display"].startswith("*")
        and row["form_role"] == "target_form"
        for row in main_rows
    )
    assert example_rows
    assert any(row["include_in_example_index"] == "yes" for row in example_rows)
    assert any(row["example_role"] == "notation_or_segment" for row in example_rows)
    assert not any(row["form"] == "form" and row["include_in_example_index"] == "yes" for row in example_rows)
    assert not any(row["form"] == "*ō" and row["inferred_language"] == "on" for row in example_rows)
    assert not any(row["form"] == "sleaan | slēaan" and row["inferred_language"] == "on" for row in example_rows)

    with tempfile.TemporaryDirectory() as tmpdir:
        fixture = Path(tmpdir) / "synthetic-print-explicit.md"
        fixture.write_text(
            "[*λόγος*]{.iv lang=greek sort=logos}\n"
            "[śrī]{.iv lang=skt sort=sri}\n"
            "[rōsa]{.iv lang=lat sort=rosa}\n",
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
        synthetic_main, _ = split_print_main_rows(list(store.values()), decisions=[])
        synthetic_keys = {(row.language, row.form) for row in synthetic_main}
    assert ("greek", "λόγος") in synthetic_keys
    assert ("skt", "śrī") in synthetic_keys
    assert ("lat", "rōsa") in synthetic_keys

    print_audit_text = PRINT_AUDIT_PATH.read_text(encoding="utf-8")
    assert "# Index verborum print audit" in print_audit_text
    assert "## Print exclusions by reason" in print_audit_text
    assert "## Printed main-index forms by language" in print_audit_text
    assert "## Printed main-index forms by role" in print_audit_text
    assert "## Internal-only rows by reason" in print_audit_text
    assert "## Print-unique entry audit" in print_audit_text
    assert "## Reader-facing include=yes summary buckets" in print_audit_text
    assert "### Included rows by inferred language" in print_audit_text
    assert "### Included rows by main-index overlap" in print_audit_text
    assert not any(row["hard_error"] == "yes" for row in anomaly_rows)


def assert_reader_failure_pair_roles() -> None:
    rows = load_reader_facing_example_rows()
    expected_roles = {
        "*bárdaz": "example_input",
        "*bearda": "yielded_output",
        "*beard": "expected_output",
        "*kámbaz": "example_input",
        "*camba": "yielded_output",
        "*camb": "expected_output",
        "*kráftaz": "example_input",
        "*craft": "yielded_output",
        "*cræft": "expected_output",
        "*dágaz": "example_input",
        "*dag": "yielded_output",
        "*dæġ": "expected_output",
    }
    row_by_key = {(row["source_ref"], row["form"]): row for row in rows}
    source_refs = {row["source_ref"] for row in rows if row["form"] == "*bárdaz"}
    source_ref = next(
        (
            ref
            for ref in source_refs
            if all((ref, form) in row_by_key for form in expected_roles)
        ),
        None,
    )
    assert source_ref is not None, "Missing reader-facing failure-pair example group"
    for form, expected_role in expected_roles.items():
        row = row_by_key[(source_ref, form)]
        assert row["example_role"] == expected_role, f"Expected {form} to be {expected_role}, got {row['example_role']}"
        assert row["include_in_example_index"] == "yes"


def assert_reconstructed_oe_index_commands() -> None:
    text = COMBINED_MD_PATH.read_text(encoding="utf-8")
    for heading, needle in (
        ("### knob — OE _\\*cnobba_", r"\index[oe]{cnobba@\emph{*cnobba}}"),
        ("### reek — OE _\\*rēac_", r"\index[oe]{reac@\emph{*rēac}}"),
        ("### strew — OE _\\*strīeġan_", r"\index[oe]{striegan@\emph{*strīeġan}}"),
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
    assert_table_decisions_load()
    assert_broad_decisions_load()
    assert_broad_suggestions_load()
    assert_add_override_behavior()
    assert_ignore_override_behavior()
    assert_baseline_strictness()
    assert_table_form_handling()
    assert_greek_and_sanskrit_explicit_tags()
    assert_optional_role_support()
    assert_table_audit_scanner()
    assert_ordinary_glosses_ignored()
    assert_already_indexed_nearby_bucket()
    assert_intermediate_trace_forms_excluded()
    assert_generated_consistency()
    assert_table_semantic_rows()
    assert_broad_prose_buckets()
    assert_broad_prose_decisions_and_inference()
    assert_print_layer_outputs()
    assert_reader_failure_pair_roles()
    assert_no_derivational_expression_rows()
    assert_reconstructed_oe_index_commands()
    print("index verborum checks passed")


if __name__ == "__main__":
    main()

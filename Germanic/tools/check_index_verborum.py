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
    build_audit_rows,
    build_production_rows,
    compare_against_baseline,
    excluded_intermediate_trace_forms,
    explicit_tag_occurrences,
    load_table_decisions,
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
SUGGESTIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_table_suggestions.tsv"
BROAD_SUGGESTIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_broad_prose_suggestions.tsv"
DECISIONS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_table_decisions.tsv"


def load_forms_rows() -> list[dict[str, str]]:
    with FORMS_PATH.open(encoding="utf-8") as handle:
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
    section = audit_section("Production indexed forms by language")
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


def assert_broad_suggestions_load() -> None:
    assert BROAD_SUGGESTIONS_PATH.exists()
    rows = load_broad_suggestion_rows()
    assert rows
    assert any(row["form"] == "boc" and row["suggested_language"] == "oe" for row in rows)
    assert any(row["form"] == "bodan" and row["suggested_language"] == "oe" for row in rows)
    assert any(row["form"] == "brōc" and row["suggested_language"] == "oe" for row in rows)
    assert any(row["form"] == "calfur" and row["suggested_language"] == "oe" for row in rows)
    assert any(row["form"] == "cūm" and row["suggested_language"] == "oe" for row in rows)


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
    summary_lines = parse_audit_summary_lines()
    assert any(line.startswith("- True remaining unresolved: ") for line in summary_lines)
    assert any(line.startswith("- Table-scanned unresolved candidates: ") for line in summary_lines)
    assert any(line.startswith("- Already indexed in same entry: ") for line in summary_lines)
    assert any(line.startswith("- Broad-prose notation / compound expressions: ") for line in summary_lines)
    assert any(line.startswith("- Broad-prose evidence suggestions: ") for line in summary_lines)
    assert any(line.startswith("- Reader-facing examples needing policy: ") for line in summary_lines)
    assert any(line.startswith("- Ordinary prose/gloss ignored: ") for line in summary_lines)
    assert any(line.startswith("- Orthographic/normalization variants: ") for line in summary_lines)
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

    reader_pairs = parse_audit_bucket_pairs("Reader-facing examples needing policy")
    assert ("*bacan", "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md:1155") in reader_pairs
    assert ("*fúrxtīnaz", "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md:2224") in reader_pairs
    assert ("ġeoc", "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md:378") in reader_pairs

    prose_pairs = parse_audit_bucket_pairs("Ordinary prose/gloss ignored")
    assert ("shoulder", "Germanic/docs/assembly/capr_book_intro_alpha_01.md:97") in prose_pairs
    assert ("sea", "Germanic/docs/lexeme_reports/model_entries/2169-sea-sǣ.model.md:33") in prose_pairs

    variant_pairs = parse_audit_bucket_pairs("Orthographic/normalization variant of indexed form")
    assert ("Boraþ", "Germanic/docs/lexeme_reports/model_entries/2312-bore-(3sg)-boraþ.model.md:29") in variant_pairs
    assert ("Caelf", "Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.model.md:25") in variant_pairs
    assert ("Cealf", "Germanic/docs/lexeme_reports/model_entries/1975-calf-ċealf.model.md:21") in variant_pairs


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
    assert_table_decisions_load()
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
    assert_no_derivational_expression_rows()
    assert_reconstructed_oe_index_commands()
    print("index verborum checks passed")


if __name__ == "__main__":
    main()

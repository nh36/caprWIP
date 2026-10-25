"""Individual reader ownership, executable parity and isolated reorder regressions."""
import collections
import csv
from dataclasses import replace
from pathlib import Path
import re
import sys
from unittest.mock import patch

import pytest

GERMANIC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(GERMANIC / "tools"))
import build_reader_book as book
import executable_facts
import generate_registry_views as registry
import oe_pipeline


def rows(text):
    return list(csv.DictReader(
        (line for line in text.splitlines() if line and not line.startswith("#")),
        delimiter="\t"))


def identity_sequence(text):
    headings = re.findall(r"^#{2,3}\s+(?:\\CAPRRuleHeading\{)?(SC\d{3})\.", text, re.M)
    return [sc for i, sc in enumerate(headings) if i == 0 or headings[i - 1] != sc]


def canonical_sequence(reg, stages):
    eligible = {r["fst_identifier"]: r["sc_id"] for r in reg
                if r["lifecycle_status"] == "active"
                and r["include_in_volume"] == r["is_reader_facing"] == "yes"}
    return [eligible[s.foma_identifier] for s in stages if s.foma_identifier in eligible]


def test_complete_order_parity_in_manifest_reader_and_combined_manuscripts():
    reg = registry.read_tsv(registry.SC_REGISTRY)
    expected = canonical_sequence(reg, oe_pipeline.named_stages())
    manifest = registry.read_tsv(registry.READER_MANIFEST)
    assert [r["sc_id"] for r in manifest] == expected
    rendered = book.render()[book.OUT_MD]
    assert identity_sequence(rendered) == expected
    assert book.OUT_MD.read_text() == rendered
    combined = (GERMANIC / "docs/assembly/capr_book_draft_alpha_01.md").read_text()
    assert identity_sequence(combined) == expected
    for row in manifest:
        anchor = "{#rule-" + row["fst_identifier"] + "}"
        assert rendered.count(anchor) == combined.count(anchor) == 1


def test_each_source_has_only_its_registered_identity_and_one_primary_heading():
    reg = registry.read_tsv(registry.SC_REGISTRY)
    generated = rows(registry.build_reader_manifest(reg, registry.read_reader_sources()))
    assert len({r["reader_file"] for r in generated}) == len(generated)
    assert {r["sc_id"] for r in generated} == set(canonical_sequence(reg, oe_pipeline.stages()))
    assert {p.name for p in book.READER_ROOT.glob("[0-9]*.md")} == {
        r["reader_file"] for r in generated}


def test_all_foma_blocks_citations_and_semantic_tags_reach_both_books():
    manifest = registry.read_tsv(registry.READER_MANIFEST)
    chapters = registry.read_reader_sources()
    sources = [(book.READER_ROOT / r["reader_file"]).read_text() for r in manifest]
    sources += [(book.READER_ROOT / c["intro_file"]).read_text() for c in chapters]
    reader = book.render()[book.OUT_MD]
    combined = (GERMANIC / "docs/assembly/capr_book_draft_alpha_01.md").read_text()
    combined = re.sub(r' (?:source_ref|occ_id)="[^"]+"', "", combined)
    for pattern in (r"```foma\n([\s\S]*?)```", r"@([A-Za-z][A-Za-z0-9_-]*)",
                    r"\{[^}\n]*\.(?:iv|lex|recon|pred)\b[^}\n]*\}"):
        expected = collections.Counter(x for text in sources for x in re.findall(pattern, text))
        actual = collections.Counter(re.findall(pattern, reader))
        assert actual == expected
        assert not expected - collections.Counter(re.findall(pattern, combined))


def test_rule_links_in_both_entries_and_shared_context_reach_unique_destinations():
    paths = [book.READER_ROOT / r["reader_file"]
             for r in registry.read_tsv(registry.READER_MANIFEST)]
    paths += [book.READER_ROOT / c["intro_file"] for c in registry.read_reader_sources()]
    texts = [p.read_text() for p in paths]
    anchors = collections.Counter(a for text in texts for a in re.findall(r"\{#(rule-[^}]+)\}", text))
    for text in texts:
        for target in re.findall(r"\]\(#(rule-[^)]+)\)", text):
            assert anchors[target] == 1, target


def test_source_boundaries_do_not_insert_page_breaks():
    rendered = book.render()[book.OUT_MD]
    source_breaks = sum((book.READER_ROOT / r["reader_file"]).read_text().count(r"\newpage")
                        for r in registry.read_tsv(registry.READER_MANIFEST))
    intro_breaks = sum((book.READER_ROOT / c["intro_file"]).read_text().count(r"\newpage")
                       for c in registry.read_reader_sources())
    assert rendered.count(r"\newpage") == len(registry.read_reader_sources()) + 1 + source_breaks + intro_breaks


def test_individual_sources_are_nested_below_real_chapters_without_changing_code():
    rendered = book.render()[book.OUT_MD]
    top_level = re.findall(r"^# (.+)$", rendered, re.M)
    assert top_level == ["The ordered sound-change sequence"] + [
        f"Chapter {c['chapter_id']}. {c['title']}" for c in registry.read_reader_sources()
    ] + ["References"]
    assert not re.search(r"^## (?:\\CAPRRuleHeading\{)?SC\d{3}\.", rendered, re.M)
    source = "# Entry\n\n## Rule\n\n```foma\n# Code comment\n```\n"
    assert book.nest_entry_headings(source) == "## Entry\n\n### Rule\n\n```foma\n# Code comment\n```"


def test_isolated_sc035_movement_crosses_a_chapter_without_source_or_membership_edits():
    reg = registry.read_tsv(registry.SC_REGISTRY)
    chapters = registry.read_reader_sources()
    original = rows(registry.build_reader_manifest(reg, chapters))
    stages = oe_pipeline.stages()
    moving = next(s for s in stages if s.foma_identifier == "OEPrefixAReduction")
    stages.remove(moving)
    destination = next(i for i, s in enumerate(stages) if s.foma_identifier == "EAFFinalZDeletion")
    stages.insert(destination, moving)
    stages = [replace(s, exec_index=i) for i, s in enumerate(stages, 1)]
    moved = rows(registry.build_reader_manifest(reg, chapters, stages=stages))
    assert [r["sc_id"] for r in moved] == canonical_sequence(reg, stages)
    old_row = next(r for r in original if r["sc_id"] == "SC035")
    new_row = next(r for r in moved if r["sc_id"] == "SC035")
    assert old_row["reader_file"] == new_row["reader_file"]
    assert (old_row["chapter_id"], new_row["chapter_id"]) == ("4", "2")
    chapter_map = {c["chapter_id"]: c for c in chapters}
    with patch.object(book, "load_manifest", return_value=(moved, chapter_map)):
        assert identity_sequence(book.render()[book.OUT_MD]) == canonical_sequence(reg, stages)


@pytest.fixture
def example(tmp_path):
    reg = []
    stages = []
    chapters = []
    for i in (1, 2):
        sc, identifier, filename = f"SC00{i}", f"Example{i}", f"00{i}-example.md"
        reg.append(dict(sc_id=sc, fst_identifier=identifier, lifecycle_status="active",
                        include_in_volume="yes", is_reader_facing="yes",
                        source_reader_facing_file=filename))
        stages.append(oe_pipeline.Stage(i, identifier, "Example", "named", cascade_position=i))
        (tmp_path / filename).write_text(
            f"# Example {i}\n\n## {sc}. Example (`{identifier}`) {{#rule-{identifier}}}\n\n"
            f"```foma\ndefine {identifier} [a -> b];\n```\n")
        (tmp_path / f"intro{i}.md").write_text(f"# Chapter {i}\n\nContext.\n")
        chapters.append(dict(chapter_id=str(i), title=f"Chapter {i}",
                             intro_file=f"intro{i}.md", starts_at_sc=sc))
    return reg, chapters, stages, tmp_path


@pytest.mark.parametrize("fault", [
    "missing-stage", "duplicate-stage", "duplicate-position", "duplicate-identity",
    "shared-source", "missing-source", "missing-heading", "duplicate-primary",
    "foreign-section", "malformed-component", "orphan-source", "named-orphan-source",
    "missing-definition", "duplicate-definition", "foreign-definition",
    "duplicate-anchor", "missing-boundary",
    "crossed-boundaries", "duplicate-boundary", "noninitial-boundary", "missing-intro",
    "entry-in-intro", "duplicate-chapter", "duplicate-intro",
])
def test_configuration_ambiguities_fail_closed_with_diagnostics(example, fault, capsys):
    reg, chapters, stages, root = example
    path = root / reg[0]["source_reader_facing_file"]
    if fault == "missing-stage":
        stages.pop()
    elif fault == "duplicate-stage":
        stages.append(stages[0])
    elif fault == "duplicate-position":
        stages[1] = replace(stages[1], exec_index=1)
    elif fault == "duplicate-identity":
        reg.append(dict(reg[0]))
    elif fault == "shared-source":
        reg[1]["source_reader_facing_file"] = reg[0]["source_reader_facing_file"]
    elif fault == "missing-source":
        path.unlink()
    elif fault == "missing-heading":
        path.write_text("# Example\n\nNo primary heading.\n")
    elif fault == "duplicate-primary":
        path.write_text(path.read_text() + path.read_text().split("\n\n")[1])
    elif fault == "foreign-section":
        path.write_text(path.read_text() + (root / reg[1]["source_reader_facing_file"]).read_text())
    elif fault == "malformed-component":
        path.write_text(path.read_text() + "\n## SC001. Missing component identifier/anchor\n")
    elif fault == "missing-definition":
        path.write_text(re.sub(r"```foma[\s\S]*?```", "", path.read_text()))
    elif fault == "duplicate-definition":
        path.write_text(path.read_text() + "\n```foma\ndefine Example1 [a -> b];\n```\n")
    elif fault == "foreign-definition":
        path.write_text(path.read_text() + "\n```foma\ndefine Example2 [a -> b];\n```\n")
    elif fault == "orphan-source":
        (root / "003-orphan.md").write_text("# Orphan\n")
    elif fault == "named-orphan-source":
        (root / "orphan-source.md").write_text(path.read_text())
    elif fault == "duplicate-anchor":
        path.write_text(path.read_text() + "\n### Component {#rule-Example1}\n")
    elif fault == "missing-boundary":
        chapters[1]["starts_at_sc"] = "SC999"
    elif fault == "crossed-boundaries":
        chapters[0]["starts_at_sc"], chapters[1]["starts_at_sc"] = "SC002", "SC001"
    elif fault == "duplicate-boundary":
        chapters[1]["starts_at_sc"] = "SC001"
    elif fault == "noninitial-boundary":
        chapters = [dict(chapters[1], chapter_id="1")]
    elif fault == "missing-intro":
        (root / chapters[0]["intro_file"]).unlink()
    elif fault == "entry-in-intro":
        (root / chapters[0]["intro_file"]).write_text(path.read_text())
    elif fault == "duplicate-chapter":
        chapters[1]["chapter_id"] = "1"
    elif fault == "duplicate-intro":
        chapters[1]["intro_file"] = chapters[0]["intro_file"]
    with pytest.raises(SystemExit):
        registry.build_reader_manifest(reg, chapters, stages=stages, reader_root=root)
    assert "READER CONFIG ERROR:" in capsys.readouterr().err


def test_builder_refuses_a_stale_or_manually_reordered_manifest(tmp_path):
    stale = tmp_path / "reader_manifest.tsv"
    stale.write_text("reader_order\n1\n")
    with patch.object(book, "READER_MANIFEST", stale), pytest.raises(ValueError, match="--refresh"):
        book.load_manifest()


def test_printed_definition_must_match_the_canonical_executable_body(example, capsys):
    reg, chapters, stages, root = example
    canonical = executable_facts.define_facts()
    canonical.update(executable_facts.parse_defines("define Example1 [a -> c];"))
    with patch.object(executable_facts, "define_facts", return_value=canonical):
        with pytest.raises(SystemExit):
            registry.build_reader_manifest(reg, chapters, stages=stages, reader_root=root)
    assert "differs from germanic.txt" in capsys.readouterr().err

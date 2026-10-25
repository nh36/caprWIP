"""Focused guards for the established publication and semantic-filter owners."""
from pathlib import Path
import re
import subprocess
import sys
import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / "Germanic/docs/sound_changes/reader_facing"))
import build_reader_book as book
import generate_registry_views as registry
from reader_facing_check_utils import display_source_path
import check_reader_facing_chronology_evidence as cues


def pandoc(text, filter_path):
    return subprocess.run(
        ["pandoc", "--from=markdown+raw_tex", "--to=latex", "--lua-filter", str(filter_path)],
        input=text, text=True, capture_output=True)


@pytest.mark.parametrize("source,expected", [
    ("[dejæ]{.pred}", r"\Pred{dejæ}"),
    ("[*wudowe*]{.pred}", r"\Pred{wudowe}"),
    ("[a&b]{.pred}", r"\Pred{a\&b}"),
])
def test_predicted_filter_preserves_and_escapes_form_content(source, expected):
    proc = pandoc(source, ROOT / "Germanic/tools/predicted_form_filter.lua")
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == expected


@pytest.mark.parametrize("source", [r"[\emph{*dejæ}]{.pred}", "[]{.pred}"])
def test_predicted_filter_fails_instead_of_emitting_an_empty_form(source):
    proc = pandoc(source, ROOT / "Germanic/tools/predicted_form_filter.lua")
    assert proc.returncode != 0
    assert ".pred" in proc.stderr


def test_short_code_boxes_are_kept_together_without_unbreakable_long_rules():
    filter_path = book.READER_ROOT / "reader_facing_foma.lua"
    short = pandoc("```foma\ndefine A [a -> b];\n```", filter_path)
    long = pandoc("```foma\n" + "\n".join(["a -> b"] * 9) + "\n```", filter_path)
    wide = pandoc("```foma\n" + "x" * 81 + "\n```", filter_path)
    for proc in (short, long, wide):
        assert proc.returncode == 0, proc.stderr
    assert r"\begin{minipage}{\linewidth}" in short.stdout
    assert r"\begin{minipage}" not in long.stdout + wide.stdout


def test_wrapped_heading_does_not_turn_a_markdown_escape_into_tex_math():
    text = "## SC103. " + "A long heading " * 6 + r"before \*x (`Example`) {#rule-Example}"
    rendered = book.wrap_long_rule_headings(text)
    assert r"\CAPRRuleHeading" in rendered
    assert r"\*x" not in rendered
    assert "*x" in rendered


def test_coverage_classifies_current_population_not_historical_report_gaps():
    report = book.render()[book.OUT_COVERAGE]
    assert "Published identities: 97. Missing or erroneous omissions: 0." in report
    assert "| SC021 | retired |" in report
    assert "| SC058 | retired |" in report
    assert "published technical support" in report
    assert "Secondary historical change-report comparison" in report
    assert "expected gaps" not in report.lower()


def test_genuine_coverage_omission_fails():
    manifest = registry.read_tsv(registry.READER_MANIFEST)
    files = [r["reader_file"] for r in manifest]
    mapping = {r["reader_file"]: [r["sc_id"]] for r in manifest}
    with pytest.raises(ValueError, match="coverage differs"):
        book.render_coverage_report(files, mapping, [r["sc_id"] for r in manifest][1:])


def test_report_paths_are_portable_and_textual_cues_are_not_scientific_verdicts():
    assert display_source_path(book.READER_MANIFEST) == (
        "Germanic/docs/sound_changes/registry/reader_manifest.tsv")
    result = cues.check_section("example.md", "SC001. Component", "A supported technical step.")
    report = cues.render_report([result])
    assert result.warnings
    assert "not a scientific evidence gate" in report
    assert "Sections with warnings" not in report


def test_current_youth_description_keeps_glide_spelling_after_phonology():
    path = ROOT / "Germanic/docs/lexeme_reports/model_entries/2308-youth-ġeoguþ.model.md"
    text = path.read_text()
    assert "late West Saxon spelling, not early palatal fronting" in text
    assert not re.search(r"\[jé[uo]g", text)


def test_sc024_alternative_account_is_preserved_without_a_duplicate_passage():
    text = (book.READER_ROOT / "024-long-e-lowering.md").read_text()
    for sentence in ("Campbell is deliberately noncommittal",
                     "Ringe and Taylor answer with the lengthened place-adverbs",
                     "The present model adopts the two-step reconstruction"):
        assert text.count(sentence) == 1

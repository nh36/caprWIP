"""The authorised weak-neuter witness, exact population transition and publication."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
GERMANIC = ROOT / "Germanic"
BASELINE = GERMANIC / "docs/sound_changes/cascade_baseline"
AUDIT = GERMANIC / "docs/sound_changes/audits/sc040-experiments"


def rows(path):
    return list(csv.DictReader(path.read_text().splitlines(), delimiter="\t"))


def test_selected_attested_cell_is_separate_from_its_comparative_citation():
    row = next(r for r in rows(GERMANIC / "data/germanic-aligned-final.tsv")
               if r["ID"] == "2336")
    assert (row["PROTO"], row["PROTOFORM"], row["COUNTERPART"], row["DERIVATION_CLASS"]) == (
        "*érθa-kùnðaz", "*érθa-kùnðǭ", "eorþcunde", "attested_variant")
    assert "Genesis A 1627" in row["NOTE"]
    assert "weak neuter accusative singular" in row["NOTE"]
    stage = next(r for r in rows(GERMANIC / "data/entry_stage_metadata.tsv")
                 if r["row_id"] == "2336")
    assert (stage["proto_stage"], stage["protoform_stage"], stage["decision_type"]) == (
        "pgmc", "pgmc", "same_stage_pgmc_paradigm_cell")


def test_every_pre_admission_source_row_and_stage_entry_is_unchanged():
    proof = json.loads((AUDIT / "population-transition.json").read_text())
    for relative, declaration in proof["source_conservation"].items():
        previous = subprocess.check_output(
            ["git", "show", proof["scientific_commit"] + ":" + relative], cwd=ROOT)
        current = subprocess.check_output(
            ["git", "show", "ee73f189d2c4af2fab6170f7af066d96611ce749:" + relative],
            cwd=ROOT)
        assert hashlib.sha256(previous).hexdigest() == declaration["previous_sha256"]
        assert current.startswith(previous)
        assert len(current.splitlines()) == len(previous.splitlines()) + 1
        assert current.splitlines()[-1].startswith(b"2336\t")


def test_authorised_writer_transition_preserves_every_original_record_and_archive():
    previous_path = BASELINE / "cascade_baseline_outputs_pre_sc040_earthly.tsv"
    previous = {r["row_id"]: r for r in rows(previous_path)}
    current = {r["row_id"]: r for r in rows(
        BASELINE / "cascade_baseline_outputs_pre_sc114_nonhigh_cells.tsv")}
    proof = json.loads((AUDIT / "population-transition.json").read_text())
    assert len(previous) == 390 and len(current) == 391
    assert set(current) - set(previous) == {"2336"}
    assert all(current[key] == record for key, record in previous.items())
    assert current["2336"]["outputs"] == "eorþcunde"
    assert current["2336"]["accepted"] == current["2336"]["match"] == "1"
    assert current["2336"]["output_count"] == "1"
    summary = json.loads(
        (BASELINE / "cascade_baseline_summary_pre_sc114_nonhigh_cells.json").read_text())
    assert summary == proof["new_summary"]
    assert (summary["accepted"], summary["matched"], summary["mismatched"],
            summary["ambiguous_outputs"]) == (391, 383, 8, 0)
    assert summary["legacy_subset_count"] == 380
    assert summary["legacy_subset_sha256"] == proof["previous_summary"]["legacy_subset_sha256"]
    assert hashlib.sha256(previous_path.read_bytes()).hexdigest() == (
        proof["previous_outputs_archive_sha256"])
    for name, sha in proof["protected_archives_and_approvals_sha256"].items():
        data = (BASELINE / name).read_bytes()
        if name == "approved_input_migrations.tsv":
            previous_ledger = subprocess.check_output(
                ["git", "show", "ee73f189d2c4af2fab6170f7af066d96611ce749:"
                 + str((BASELINE / name).relative_to(ROOT))], cwd=ROOT)
            assert data.startswith(previous_ledger)
            assert [row["row_id"] for row in rows(BASELINE / name)][-6:] == [
                "2011", "2201", "2282", "2053", "2335", "2208"]
            assert len(data.splitlines()) == len(previous_ledger.splitlines()) + 6
            data = previous_ledger
        assert hashlib.sha256(data).hexdigest() == sha, name
    assert {key for key, record in current.items() if record["match"] == "0"} == {
        key for key, record in previous.items() if record["match"] == "0"}


def test_actual_source_ledger_and_editorial_selection_are_paired():
    model = GERMANIC / "docs/lexeme_reports/model_entries/2336-earthly-eorþcunde.model.md"
    ledger = model.with_name("2336-earthly-eorþcunde.source_ledger.md")
    assert ledger.is_file()
    assert r"\emph{*weo.rul.des}" in model.read_text()
    case = next(r for r in rows(GERMANIC / "docs/lexeme_reports/pgmc_integration/editorial_cases.tsv")
                if r["row_id"] == "2336")
    assert case["requires_extended_discussion"] == "1"
    assert case["publication_source"] == "model_entries/2336-earthly-eorþcunde.model.md"


def test_new_article_is_assembled_in_its_alphabetical_class_position():
    manifest = rows(GERMANIC / "docs/assembly/manifest_attested_variant.tsv")
    entry = next(r for r in manifest if r["row_id"] == "2336")
    assert entry["lexical_item"] == "earthly"
    headwords = [r["lexical_item"].casefold() for r in manifest]
    assert headwords == sorted(headwords)
    for relative in (
            "docs/debug_snapshots/oe_derivation_class_trace_report.txt",
            "docs/assembly/lexical_volume_alpha_01.md",
            "docs/assembly/capr_book_draft_alpha_01.md"):
        assert "eorþcunde" in (GERMANIC / relative).read_text(), relative

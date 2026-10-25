"""Scientific alternatives to the accepted compressed weak-prefix proxy."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
SC = ROOT / "Germanic/docs/sound_changes"
BASE = "5533f7653f87d3962a92935a280190882c16b61b"
RECORD = SC / "audits/sc035-model-comparison/evidence.json"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from capr_runtime import run_in_runner
import adjudicate
from historical_sc035 import historical_runtime


def record():
    return json.loads(RECORD.read_text())


def checkpoint(model, row, stage):
    return next(item for item in record()["models"][model]["focal_traces"][row]
                if item["stage"] == stage)


def test_original_closure_and_experiments_remain_historical_records():
    for relative in (
        "audits/sc035-adjudication.md",
        "audits/sc035-prefix-reduction/evidence.json",
        "audits/sc035-prefix-reduction/experiment.py",
        "order_tests/chronology_cards/SC035-oe-prefix-a-reduction-early.md",
    ):
        path = SC / relative
        original = subprocess.check_output(
            ["git", "show", f"{BASE}:{path.relative_to(ROOT)}"], cwd=ROOT)
        assert path.read_bytes() == original


def test_comparison_receipt_identifies_actual_accepted_source_and_both_populations():
    data = record()
    source = subprocess.check_output(
        ["git", "show", f"{BASE}:Germanic/fsts/germanic.txt"], cwd=ROOT)
    assert data["accepted_base_commit"] == BASE
    assert data["source_sha256"] == hashlib.sha256(source).hexdigest()
    assert (data["selected_rows"], data["legacy380_identity_rows"],
            data["stages_compared"]) == (389, 380, 108)
    assert data["canonical_artifacts_unchanged"]
    assert set(data["models"]) == {"A", "B", "C"}


def test_all_intermediate_changes_and_final_invariance_are_explicit():
    data = record()
    for model, result in data["models"].items():
        assert result["final_differences"] == []
        differences = result["all_intermediate_differences"]
        if model == "A":
            assert differences == []
        else:
            assert len(differences) == 63
            assert {row["row_id"] for stage in differences
                    for row in stage["rows"]} == {"1944"}
            assert all(row["legacy380_identity"] for stage in differences
                       for row in stage["rows"])
            for row in ("1943", "1950", "2037", "2041", "2049", "2179"):
                assert result["focal_traces"][row] == data["models"]["A"]["focal_traces"][row]


def test_staged_fronting_and_raising_are_not_conflated():
    fronting = "EAFBrighteningUnstressed"
    palatal = "OEWsPalatalDiphthongization"
    merger = "OEUnstressedAEMerger"
    assert checkpoint("A", "1944", fronting)["after"][0].startswith("*g*ĕ*l")
    for model in ("B", "C"):
        assert checkpoint(model, "1944", fronting)["after"][0].startswith("*ᵖ*g*æ*l")
        stage = checkpoint(model, "1944", palatal)
        assert stage["before"] == stage["after"]
        assert checkpoint(model, "1944", merger)["after"][0].startswith("*ᵖ*ʝ*e*l")
    assert checkpoint("B", "1944", palatal)["before"][0].startswith("*ᵖ*ʝ*æ*l")
    assert checkpoint("C", "1944", palatal)["before"][0].startswith("*ᵖ*ʝ*i*l")


def test_missing_acute_is_not_a_general_stress_classifier():
    assert checkpoint("A", "2049", "EAFBrightening")["after"] == ["*g*æ*s*t*i"]
    for model in ("A", "B", "C"):
        assert checkpoint(model, "2049", "OEWsPalatalDiphthongization")["after"] == [
            "*ʝ*ea*s*t*i"]
        assert checkpoint(model, "2041", "OEWsPalatalDiphthongization")["after"] == [
            "*ʝ*íe*β*ą*n"]
        assert checkpoint(model, "2179", "OEWsPalatalDiphthongization")["after"] == [
            "*ʃ*ēa*p"]
        gall = checkpoint(model, "2037", "OEWsPalatalDiphthongization")
        assert gall["before"] == gall["after"] == ["*ʝ*ea*l*l*ô"]


def test_cluster_coverage_advantage_is_not_hidden_by_selected_output_equality():
    models = record()["models"]
    assert models["A"]["full_input_climb"] == [["ġiestīgan"]]
    assert models["A"]["staged_control_finals"]["climb"] == ["ġiestīgan"]
    assert models["A"]["staged_control_finals"]["climb-stress-erased"] == ["ġiestegan"]
    for model in ("B", "C"):
        assert models[model]["full_input_climb"] == [["ġestīgan"]]
        assert models[model]["staged_control_finals"]["climb"] == ["ġestīgan"]
        assert models[model]["staged_control_finals"]["climb-stress-erased"] == ["ġestīgan"]
        assert models[model]["early_gi_merger"] == ["*ᵖ*ʝ*e*s*t*ḯ*g*a"]
    assert models["A"]["early_gi_merger"] == ["*ʝ*i*s*t*ḯ*g*a"]
    assert "artificial" in record()["controls"]["ni-template"]["status"]


def test_current_decision_links_followup_without_claiming_a_unique_history():
    row = adjudicate.load_registry_row("SC035")
    assert row["adjudication_memo"].endswith("sc035-literature-adjudication.md")
    assert row["verdict"] == "RETAIN"
    assert adjudicate.check_memo("SC035", row=row) == []


@pytest.mark.runtime
def test_fresh_foma_comparison_reproduces_every_recorded_intermediate():
    with historical_runtime(BASE) as execute:
        executed = execute(
            "python3 docs/sound_changes/audits/sc035-model-comparison/experiment.py")
    current = json.loads(executed.stdout)
    historical = record()
    assert current["source_sha256"] == historical["source_sha256"]
    for key in ("accepted_base_commit", "selected_rows", "legacy380_identity_rows",
                "stages_compared", "controls", "models", "canonical_artifacts_unchanged"):
        assert current[key] == historical[key], key

"""Checks of the failed SC040 adoption assay, not production certification."""
import gzip
import hashlib
import json
from pathlib import Path
import tarfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/sc040-experiments"


@pytest.fixture(scope="module")
def report():
    return json.loads(gzip.decompress(
        (EVIDENCE / "diagnosed-results.json.gz").read_bytes()))


def test_failed_adoption_is_not_published_as_success(report):
    assert report["assay_status"] == "failed"
    formal = report["formal_diagnosis"]
    for name in ("MFoot", "MFootOne", "MLate", "MLateOne"):
        assert formal[name]["stdout"].strip() == "0 (1 = TRUE, 0 = FALSE)"
    for name in ("MSyll", "MAccent", "MPlainLower", "MDecode", "RFoot", "RLate"):
        assert formal[name]["stdout"].strip() == "1 (1 = TRUE, 0 = FALSE)"
    manifest = json.loads((EVIDENCE / "evidence-manifest.json").read_text())
    assert len(manifest["attempts"]) == 3
    with tarfile.open(EVIDENCE / "evidence.tar.gz") as archive:
        for attempt in manifest["attempts"]:
            completion = json.load(archive.extractfile(
                attempt + "/completion.json"))
            assert completion["outcome"] == "failed"
            receipt_names = [name for name in manifest["members"]
                            if name.startswith(attempt + "/results/SC040-full-assay-")
                            and name.endswith(".receipt.json")]
            assert len(receipt_names) == 1
            receipt = json.load(archive.extractfile(receipt_names[0]))
            assert receipt["returncode"] != 0 and not receipt["ok"]


def test_evidence_archive_preserves_original_inputs_and_receipt_logs():
    manifest = json.loads((EVIDENCE / "evidence-manifest.json").read_text())
    assert hashlib.sha256((EVIDENCE / "evidence.tar.gz").read_bytes()).hexdigest() == (
        manifest["archive_sha256"])
    with tarfile.open(EVIDENCE / "evidence.tar.gz") as archive:
        files = {m.name: m for m in archive.getmembers() if m.isfile()}
        assert set(files) == set(manifest["members"])
        for name, sha in manifest["members"].items():
            assert hashlib.sha256(archive.extractfile(files[name]).read()).hexdigest() == sha
        for attempt in manifest["attempts"]:
            snapshot = json.load(archive.extractfile(attempt + "/receipt.json"))
            for entry in snapshot["inputs"].values():
                name = attempt + "/snapshot/" + entry["snapshot_name"]
                assert manifest["members"][name] == entry["sha256"]
        for name in files:
            if not name.endswith(".receipt.json"):
                continue
            receipt = json.load(archive.extractfile(name))
            for stream in ("stdout", "stderr"):
                log_name = str(Path(name).parent / Path(receipt[stream + "_log"]).name)
                assert manifest["members"][log_name] == receipt[stream + "_sha256"]


def test_every_existing_population_stage_is_conserved(report):
    assert len(report["plan"]["rows"]) == 390
    assert report["population_checks"]["immutable380_count"] == 380
    expected = ["1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"]
    for model in report["models"].values():
        assert model["counts"]["matched"] == 382
        assert model["counts"]["mismatch_ids"] == expected
        assert not model["selected_final_delta_ids"]
        assert not model["immutable_final_delta_indices"]
        for stage in model["aligned_intermediate_deltas"]:
            assert not stage["rows"] and not stage["immutable_indices"]
        for trace in model["traces"]:
            assert all(len(value) <= 1 for value in trace["after"])
        assert model["order"].count("OEStripSecondaryStress") == 1
    assert report["canonical_before"] == report["canonical_after"]
    lowering = next(s for s in report["models"]["identity"]["traces"]
                    if s["stage"] == "OEMedUnstressedULowering")
    fired = {row["row_id"] for row, before, after in zip(
        report["plan"]["rows"], lowering["before"], lowering["after"])
        if before != after}
    assert fired == {"2060", "2063", "2068", "2126", "2133", "2142",
                     "2174", "2201", "2242", "2302"}


def test_complete_cells_succeed_only_in_the_unapproved_proposal(report):
    weak = "earthly-weak-neuter-unaugmented-nasal"
    genitive = "earthly-genitive-grave"
    original = report["models"]["identity"]["candidates"]
    assert original[weak]["parser_accepted"]
    assert original[weak]["final"] == ["eorþconde"]
    assert original[genitive]["final"] == ["eorþcondes"]
    for name in ("production-proposal", "single-onset-proposal"):
        cells = report["models"][name]["candidates"]
        assert cells[weak]["parser_accepted"]
        assert cells[weak]["final"] == ["eorþcunde"]
        assert cells[genitive]["final"] == ["eorþcundes"]
        for stage in ("OEMedialSyncope", "OELAdjacentSyncope",
                      "OEPreconsonantalDegemination"):
            step = next(s for s in cells[weak]["steps"] if s["stage"] == stage)
            assert step["before"] == step["after"]


def test_general_component_controls_and_annotation_removal(report):
    inputs = report["plan"]["components"]
    result = report["component_results"]
    for head in ("MFoot", "MFootOne"):
        for name in ("late-earthly", "late-godcund-accusative",
                     "late-godcund-feminine-genitive", "initial-kn-heavy-medial",
                     "initial-hw-heavy-medial", "initial-vowel-heavy-medial",
                     "pretonic-heavy-medial", "pretonic-heavy-prefix"):
            assert result[head][name] == [inputs[name].replace("*u", "*ù")]
        for name in ("initial-LH-negative", "open-medial-negative",
                     "final-heavy-negative", "cyning-LH", "late-being"):
            assert result[head][name] == [inputs[name]]
        assert result[head]["initial-LL-heavy-medial"] == [
            inputs["initial-LL-heavy-medial"].replace("*i", "*ì")]
        assert result[head]["nonhigh-heavy-medial"] == [
            inputs["nonhigh-heavy-medial"].replace("*a", "*à")]
    assert result["MLate"]["headed-u-following-u"] == [inputs["headed-u-following-u"]]
    for model_name in ("production-proposal", "single-onset-proposal"):
        model = report["models"][model_name]
        internal = model["internal_operations"][-1]
        stage = next(s for s in model["traces"] if s["stage"] == internal["stage"])
        assert internal["operations"][0]["before"] == stage["before"]
        assert internal["operations"][-1]["after"] == stage["after"]
        for operation in internal["operations"]:
            assert all(len(value) <= 1 for value in operation["after"])
        assert all(not any(mark in value for mark in "ᵇàèìòù")
                   for values in internal["operations"][-1]["after"] for value in values)

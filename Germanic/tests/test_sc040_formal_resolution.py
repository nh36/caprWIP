"""Reduced formal-composition regression and source-pinned scientific evidence."""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import tarfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/sc040-experiments"


@pytest.fixture(scope="module")
def formal():
    return json.loads((EVIDENCE / "formal-results.json").read_text())


@pytest.fixture(scope="module")
def report():
    return json.loads(gzip.decompress((EVIDENCE / "corrected-results.json.gz").read_bytes()))


def test_reduced_delayed_identity_explains_the_formal_false_negative(formal):
    delayed = formal["components"]["MinDelay"]
    aligned = formal["components"]["MinAligned"]
    assert not delayed["functional"]
    assert aligned["functional"]
    assert delayed["ab_replay"].strip() == aligned["ab_replay"].strip() == "ab\tab"
    assert delayed["square"]["independent_identity"]["identity"]
    assert aligned["square"]["independent_identity"]["identity"]


def test_restricted_composition_is_identity_checked_without_a_lexical_filter(formal):
    components = formal["components"]
    for name in ("MSyll", "MAccent", "MUnsyll", "DiagSA", "DiagCore"):
        assert components[name]["functional"]
    assert not components["DiagSent"]["functional"]
    assert components["DiagSent"]["square"]["independent_identity"]["identity"]
    assert components["DiagSent"]["square"]["independent_identity"]["reachable_states"] > 100
    for name in ("QFoot", "QFootOne", "QLate", "QLateOne"):
        assert components[name]["functional"]
    for name in ("QFoot", "QLate", "QLateOne"):
        assert components[name]["square"]["independent_identity"]["identity"]


def test_independent_identity_check_rejects_a_genuinely_distinct_output_pair():
    spec = importlib.util.spec_from_file_location("sc040_formal", EVIDENCE / "formal_resolution.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.identity_debt("0\t1\ta\t@0@\n1\t2\t@0@\ta\n2\n")["identity"]
    with pytest.raises(AssertionError, match="distinct symbols"):
        module.identity_debt("0\t1\ta\tb\n1\n")


def test_resolution_archive_preserves_source_snapshots_and_actual_signed_logs():
    manifest = json.loads((EVIDENCE / "resolution-evidence.json").read_text())
    assert hashlib.sha256((EVIDENCE / "resolution-evidence.tar.gz").read_bytes()).hexdigest() == (
        manifest["archive_sha256"])
    with tarfile.open(EVIDENCE / "resolution-evidence.tar.gz") as archive:
        files = {member.name: member for member in archive.getmembers() if member.isfile()}
        assert set(files) == set(manifest["members"])
        for name, sha in manifest["members"].items():
            assert hashlib.sha256(archive.extractfile(files[name]).read()).hexdigest() == sha
        for snapshot in ("sc040-formal-composition-01", "sc040-formal-composition-02",
                         "sc040-corrected-adoption-01", "sc040-corrected-adoption-02"):
            receipt = json.load(archive.extractfile(snapshot + "/receipt.json"))
            for entry in receipt["inputs"].values():
                assert manifest["members"][snapshot + "/snapshot/" + entry["snapshot_name"]] == (
                    entry["sha256"])
        for name in files:
            if not name.endswith(".receipt.json"):
                continue
            receipt = json.load(archive.extractfile(name))
            for stream in ("stdout", "stderr"):
                log_name = str(Path(name).parent / Path(receipt[stream + "_log"]).name)
                assert manifest["members"][log_name] == receipt[stream + "_sha256"]


def test_corrected_component_and_wrapper_pass_the_unchanged_formal_gate(report):
    assert report["assay_status"] == "passed"
    for name in ("QSyll", "QFoot", "QFootOne", "QULower", "QDecode", "QLate", "QLateOne"):
        assert "1 (1 = TRUE, 0 = FALSE)" in report["formal"][name]["stdout"]
    assert report["canonical_before"] == report["canonical_after"]


def test_all_original_populations_and_physical_stages_are_conserved(report):
    assert len(report["plan"]["rows"]) == 390
    assert report["population_checks"]["immutable380_count"] == 380
    for model in report["models"].values():
        assert model["counts"]["matched"] == 382
        assert model["counts"]["mismatch_ids"] == [
            "1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"]
        assert not model["selected_final_delta_ids"]
        assert not model["immutable_final_delta_indices"]
        for step in model["aligned_intermediate_deltas"]:
            assert not step["rows"] and not step["immutable_indices"]


def test_complete_cells_have_real_protection_and_cleanup_subtraces(report):
    candidates = report["plan"]["candidates"]
    for model_name in ("production-proposal", "single-onset-proposal"):
        model = report["models"][model_name]
        operations = model["internal_operations"][-1]["operations"]
        for name, expected in (
                ("earthly-weak-neuter-unaugmented-nasal", "eorþcunde"),
                ("earthly-genitive-grave", "eorþcundes")):
            cell = model["candidates"][name]
            assert cell["parser_accepted"] and cell["final"] == [expected]
            index = 390 + 380 + list(candidates).index(name)
            assert "*ù" in operations[0]["after"][index][0]
            assert operations[1]["after"][index] == operations[0]["after"][index]
            assert "*ù" not in operations[2]["after"][index][0]


def test_initial_foot_medial_weight_and_pretonic_controls_are_general(report):
    inputs = report["plan"]["components"]
    components = report["component_results"]
    for head in ("QFoot", "QFootOne"):
        for name in ("late-earthly", "initial-kn-heavy-medial",
                     "initial-hw-heavy-medial", "initial-vowel-heavy-medial",
                     "pretonic-heavy-medial", "pretonic-heavy-prefix",
                     "late-godcund-accusative", "late-godcund-feminine-genitive"):
            assert components[head][name] == [inputs[name].replace("*u", "*ù")]
        for name in ("initial-LH-negative", "open-medial-negative",
                     "final-heavy-negative", "cyning-LH", "late-being"):
            assert components[head][name] == [inputs[name]]
        assert components[head]["initial-LL-heavy-medial"] == [
            inputs["initial-LL-heavy-medial"].replace("*i", "*ì")]
        assert components[head]["late-riding"] == [inputs["late-riding"].replace("*e", "*è", 1)]
    assert components["QLate"]["headed-u-following-u"] == [inputs["headed-u-following-u"]]

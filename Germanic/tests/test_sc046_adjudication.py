"""Source-bound SC046 trials and inexpensive current-production controls."""
import hashlib
import json
from pathlib import Path
import shlex
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from capr_runtime import run_in_runner

EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/sc046-restoration-evidence"


def trials():
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    for name, digest in manifest["members"].items():
        assert hashlib.sha256((EVIDENCE / name).read_bytes()).hexdigest() == digest
    provenance = json.loads((EVIDENCE / "provenance.json").read_text())
    observed = {}
    for label in ("initial", "followup"):
        record = provenance[label]
        receipt = record["completion"]["command_receipts"][0]
        payload = (EVIDENCE / (label + "-observed.json")).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == receipt["stdout_sha256"]
        assert hashlib.sha256(record["stderr"].encode()).hexdigest() == receipt["stderr_sha256"]
        assert receipt["ok"] and not receipt["source_changed"]
        assert receipt["source_identity_sha256"] == receipt["source_identity_after"]["identity_sha256"]
        assert record["completion"]["outcome"] == "passed"
        assert record["snapshot"]["inputs"]["source"]["sha256"] == manifest["source_sha256"]
        assert hashlib.sha256((EVIDENCE / (label + "-worker.py")).read_bytes()).hexdigest() == (
            record["snapshot"]["inputs"]["worker"]["sha256"])
        observed[label] = json.loads(payload)
    failed = provenance["bootstrap_failure"]
    assert failed["completion"]["outcome"] == "failed"
    assert "IndexError: 5" in failed["stderr"]
    return observed


def test_authenticated_full_corpus_trials_do_not_turn_score_into_adoption():
    observed = trials()["initial"]
    assert len(observed["rows"]) == 394
    assert sum(row["target"] in row["baseline"] for row in observed["rows"]) == 386
    expected = {
        "stress": {"2148": (["reġnboga"], ["reġneafoga"])},
        "no_geminate": {"2090": (["lappa"], ["læppa"]), "2240": (["tappa"], ["tæppa"])},
    }
    for name, deltas in expected.items():
        comparison = observed["corpus"][name]
        assert len(comparison["rows"]) == 394
        assert comparison["rejected"] == comparison["ambiguous"] == 0
        assert {row["row_id"]: (row["baseline"], row["outputs"])
                for row in comparison["rows"] if row["changed"]} == deltas
    for label in ("current", "stress", "no_geminate"):
        query = observed["queries"][label + ":local"]
        values = dict(zip(query["inputs"], query["outputs"]))
        for before, after in (("*k*r*æ*b*b*ô", "*k*r*a*b*b*ô"),
                              ("*r*æ*k*k*ô", "*r*a*k*k*ô")):
            assert values[before] == [before if label == "no_geminate" else after]


def test_fixed_apocope_and_compound_interventions_have_distinct_observed_effects():
    observed = trials()
    initial = observed["initial"]["queries"]
    followup = observed["followup"]["queries"]
    assert initial["48_then_46:local"]["outputs"] == [
        ["*b*a*k*a*n"], ["*w*a*d*a*n"]]
    assert initial["48_then_46:final"]["outputs"] == [["bacen"], ["waden"]]
    assert followup["47:local"]["outputs"] == [["*b*æ*k*a*n"], ["*w*æ*d*a*n"]]
    assert followup["47_46_48:local"]["outputs"] == [["*b*a*k*ą*n"], ["*w*a*d*ą*n"]]
    assert followup["47_48_46:local"]["outputs"] == [["*b*æ*k*ą*n"], ["*w*æ*d*ą*n"]]
    assert followup["47_48_46:final"]["outputs"] == [["bæcan"], ["wædan"]]
    assert followup["stress:before_back_mutation"]["outputs"] == [
        ["*r*é*ʝ*n*æ*b*o*g*ô"], ["*éo*r*θ*æ*k*ù*n*d*ǣ"]]
    assert followup["stress:back_mutation"]["outputs"] == [
        ["*r*é*ʝ*n*ea*b*o*g*ô"], ["*éo*r*θ*æ*k*ù*n*d*ǣ"]]
    assert initial["stress:syncope"]["outputs"] == [
        ["*r*é*ʝ*n*ea*b*o*g*ô"], ["*éo*r*θ*k*ù*n*d*ǣ"]]
    assert initial["stress:final"]["outputs"] == [["reġneafoga"], ["eorþcunde"]]


@pytest.mark.runtime
def test_current_production_restoration_positives_and_scoped_residue(record_testsuite_property):
    script = """
import json, sys
sys.path.insert(0, "docs/sound_changes/audits/sc046-restoration-evidence")
import experiment
import oe_pipeline
from capr_runtime import layout
from sound_change_order_sensitivity import batch_apply_down
actual = experiment.production()
runtime = layout()
rows = {row["row_id"]: row for row in oe_pipeline.load_rows(runtime.corpus_tsv)}
inputs = [rows[key]["fst_input"] for key in actual]
for name in ("PNWGmcULowering", "OEBackMutation", "OENonHighSyn", "PGmcBAllophony"):
    path = runtime.bin_dir / oe_pipeline.stage_for(name).snapshot_bin
    for key, values in zip(actual, batch_apply_down(path, inputs)):
        actual[key][name] = values
print(json.dumps(actual))
"""
    result = run_in_runner(
        "python3 -c " + shlex.quote(script),
        text=True, capture_output=True, check=True, timeout=180)
    actual = json.loads(result.stdout)
    expected = {
        "1934": ("*b*æ*k*a*n*ą", "*b*a*k*a*n*ą", "bacan"),
        "1938": ("*b*æ*s*t*ą", "*b*æ*s*t*ą", "bæst"),
        "1981": ("*k*r*æ*f*t", "*k*r*æ*f*t", "cræft"),
        "1985": ("*d*æ*g", "*d*æ*g", "dæġ"),
        "2016": ("*f*l*æ*s*k*ō*n", "*f*l*a*s*k*ō*n", "flascan"),
        "2090": ("*l*æ*p*p*ô", "*l*a*p*p*ô", "lappa"),
        "2141": ("*m*æ*r*ǣ", "*m*æ*r*ǣ", "mære"),
        "2148": ("*r*é*g*n*æ*b*o*g*ô", "*r*é*g*n*æ*b*o*g*ô", "reġnboga"),
        "2240": ("*t*æ*p*p*ô", "*t*a*p*p*ô", "tappa"),
        "2266": ("*w*æ*d*a*n*ą", "*w*a*d*a*n*ą", "wadan"),
        "2336": ("*éo*r*θ*æ*k*ù*n*d*ǣ", "*éo*r*θ*æ*k*ù*n*d*ǣ", "eorþcunde"),
    }
    assert actual.keys() == expected.keys()
    for key, (before, after, final) in expected.items():
        assert actual[key]["OEVelarFricativePalatalization"] == [before]
        assert actual[key]["OEARestoration"] == [after]
        assert actual[key]["final"] == [final]
    assert actual["2148"]["PNWGmcULowering"] == ["*r*é*g*n*a*b*ò*g*ô"]
    for key, before, after in (
            ("2148", "*r*é*ʝ*n*æ*b*o*g*ô", "*r*é*ʝ*n*b*o*g*ô"),
            ("2336", "*éo*r*θ*æ*k*ù*n*d*ǣ", "*éo*r*θ*k*ù*n*d*ǣ")):
        assert actual[key]["OEBackMutation"] == [before]
        assert actual[key]["OENonHighSyn"] == [after]
        if key == "2148":
            assert actual[key]["PGmcBAllophony"] == [after]
    record_testsuite_property("sc046_production_only", json.dumps(actual, ensure_ascii=False))

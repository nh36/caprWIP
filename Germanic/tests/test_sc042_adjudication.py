"""SC042's source-bound oral-final fragment and separated fronting dependencies."""

import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Germanic/docs/sound_changes/audits/sc042-experiments"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines
from oe_trace_parse import parse_entries


def evidence():
    return json.loads((AUDIT / "evidence.json").read_text())


def test_complete_live_census_is_rest_and_protected_quantities_remain_unchanged():
    controls = {
        "water": "*w*á*t*a*r", "four": "*f*ēo*w*a*r", "gift": "*g*í*f*t*i",
        "tongue": "*t*ú*n*g*ǭ", "heart": "*x*é*r*t*ǭ", "earth": "*é*r*θ*ǭ",
        "name": "*n*á*m*ô", "who": "*x*w*ā", "horn": "*x*ó*r*n*ą",
        "bake": "*b*á*k*a*n*ą",
    }
    firings, checked = {}, set()
    entries = parse_entries((ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt").read_text())
    for entry in entries.values():
        i = next(i for i, stage in enumerate(entry.stages)
                 if stage.label == "PWGmcSurvivingBimoricOUnrounding")
        before, after = entry.stages[i - 1].forms, entry.stages[i].forms
        if before != after:
            firings[entry.concept] = (entry.proto, before, after, entry.outputs)
        if entry.concept in controls:
            assert before == after == (controls[entry.concept],)
            checked.add(entry.concept)
    assert checked == set(controls)
    assert firings == {"rest": ("*rástōz", ("*r*á*s*t*ō",), ("*r*á*s*t*ā",), "ræste")}


def test_immutable_assays_authenticate_logs_and_preserve_the_sc042_definition():
    manifest = json.loads((AUDIT / "manifest.json").read_text())
    assert hashlib.sha256((AUDIT / "experiments.zip").read_bytes()).hexdigest() == manifest["archive_sha256"]
    assert hashlib.sha256((AUDIT / "evidence.json").read_bytes()).hexdigest() == manifest["evidence_sha256"]
    with zipfile.ZipFile(AUDIT / "experiments.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        source = archive.read("sc042-baseline-20261111/snapshot/germanic_fst.txt").decode()
        for name in ("canonical-evidence-receipt.json", "counterfactual-execution-receipt.json"):
            receipt = json.loads(archive.read("execution/" + name))
            assert receipt["ok"] and not receipt["source_changed"]
            for field in ("stdout_log", "stderr_log"):
                content = archive.read("execution/" + Path(receipt[field]).name)
                assert hashlib.sha256(content).hexdigest() == receipt[field.replace("_log", "_sha256")]
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    assayed = parse_defines(source)
    rule = "PWGmcSurvivingBimoricOUnrounding"
    assert current[rule].body == assayed[rule].body


def test_executed_component_controls_distinguish_quantity_nasality_finality_and_proxy_scope():
    checks = {row["id"]: row for row in evidence()["variants"]["before-z"]["component_checks"]}
    for name in ("light-final-oral", "heavy-final-oral"):
        row = checks[name]
        assert row["outputs"] == [row["input"][:-2] + "*ā"] == [row["expected"]]
    for name in ("monosyllabic-long-o", "nasal-long-o", "short-o", "trimoric-marker",
                 "protected-by-z", "protected-by-r-proxy-limit", "no-intervening-consonant"):
        row = checks[name]
        assert row["outputs"] == [row["input"]]
    assert checks["final-fronting-feeder"]["outputs"] == ["*r*æ*s*t*ǣ"]
    assert checks["final-fronting-unfed"]["outputs"] == ["*r*æ*s*t*ō"]
    assert checks["who-final-fronting-negative"]["outputs"] == ["*x*w*ā"]


def test_displacements_require_exposure_and_final_support_not_stressed_fronting():
    variants = evidence()["variants"]
    for variant in variants.values():
        assert variant["no_output"] == variant["multiple_output"] == 0
    assert variants["after-stressed-fronting"]["changed_rows"] == []
    successful = variants["after-stressed-fronting"]["rest"]["intermediates"]
    assert successful["root_after"] == successful["moved_before"] == ["*r*æ*s*t*ō"]
    assert successful["moved_after"] == ["*r*æ*s*t*ā"]
    assert successful["final_after"] == successful["restoration_after"] == ["*r*æ*s*t*ǣ"]
    for name in ("before-z", "after-final-fronting"):
        variant = variants[name]
        assert [row["concept"] for row in variant["changed_rows"]] == ["rest"]
        row = variant["changed_rows"][0]
        assert row["outputs"] == ["rasta"]
        assert row["baseline_match"] and not row["variant_match"]
        assert row["intermediates"]["final_before"] == row["intermediates"]["final_after"] == ["*r*æ*s*t*ō"]
    early = variants["before-z"]["changed_rows"][0]["intermediates"]
    assert early["moved_before"] == early["moved_after"] == ["*r*á*s*t*ō*z"]
    assert early["z_after"] == ["*r*á*s*t*ō"]
    assert early["restoration_before"] == ["*r*æ*s*t*ō"]
    assert early["restoration_after"] == ["*r*a*s*t*ō"]
    late = variants["after-final-fronting"]["changed_rows"][0]["intermediates"]
    assert late["moved_before"] == ["*r*æ*s*t*ō"]
    assert late["moved_after"] == late["restoration_before"] == ["*r*æ*s*t*ā"]
    assert late["restoration_after"] == ["*r*a*s*t*ā"]

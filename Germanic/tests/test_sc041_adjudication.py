"""SC041's oral-a domain, authenticated assays and restoration bleeding."""

import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Germanic/docs/sound_changes/audits/sc041-experiments"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines
from oe_trace_parse import parse_entries


def evidence():
    return json.loads((AUDIT / "evidence.json").read_text())


def test_current_trace_deletes_only_exposed_short_oral_a_and_preserves_controls():
    entries = parse_entries((ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt").read_text())
    firings = set()
    controls = {"bake", "horn", "rest", "who", "ban", "earth", "earthly"}
    checked_controls = set()
    for entry in entries.values():
        index = next(i for i, stage in enumerate(entry.stages)
                     if stage.label == "PWGmcFinalBareALoss")
        before, after = entry.stages[index - 1].forms, entry.stages[index].forms
        if before != after:
            firings.add(entry.concept)
            assert entry.proto.endswith("az")
            assert len(before) == len(after) == 1
            assert before[0].endswith("*a")
            assert after[0] == before[0][:-2]
        if entry.concept in controls:
            assert before == after
            checked_controls.add(entry.concept)
    assert {"beard", "comb", "craft", "day", "fright", "hedge", "hammer", "rust", "dart"} <= firings
    assert checked_controls == controls


def test_assay_archive_authenticates_inputs_logs_and_the_current_deletion_rule():
    manifest = json.loads((AUDIT / "manifest.json").read_text())
    assert hashlib.sha256((AUDIT / "experiments.zip").read_bytes()).hexdigest() == manifest["archive_sha256"]
    assert hashlib.sha256((AUDIT / "evidence.json").read_bytes()).hexdigest() == manifest["evidence_sha256"]
    with zipfile.ZipFile(AUDIT / "experiments.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        source = archive.read("sc041-baseline-20261111/snapshot/germanic_fst.txt")
        for name in ("canonical-evidence-receipt.json", "counterfactual-execution-receipt.json"):
            receipt = json.loads(archive.read("execution/" + name))
            assert receipt["ok"] and not receipt["source_changed"]
            for field in ("stdout_log", "stderr_log"):
                content = archive.read("execution/" + Path(receipt[field]).name)
                assert hashlib.sha256(content).hexdigest() == receipt[field.replace("_log", "_sha256")]
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    assayed = parse_defines(source.decode())
    assert current["PWGmcFinalBareALoss"].body == assayed["PWGmcFinalBareALoss"].body


def test_executed_component_controls_distinguish_weight_nasality_quantity_and_protection():
    checks = {row["id"]: row for row in evidence()["variants"]["before-z"]["component_checks"]}
    for name in ("short-oral-a", "heavy-short-oral-a"):
        row = checks[name]
        assert row["outputs"] == [row["expected"]]
        assert row["outputs"] == [row["input"][:-2]]
    for name in ("nasal-a", "long-a", "stressed-a", "protected-by-s", "high-i", "high-u"):
        row = checks[name]
        assert row["outputs"] == [row["input"]]
    assert checks["restoration-trigger-present"]["outputs"] == ["*d*a*g*a"]
    assert checks["restoration-trigger-absent"]["outputs"] == ["*d*æ*g"]


def test_paired_displacements_separate_restoration_bleeding_from_missed_n_loss():
    report = evidence()
    before = {row["concept"]: row for row in report["variants"]["before-restoration"]["changed_rows"]}
    after = {row["concept"]: row for row in report["variants"]["after-restoration"]["changed_rows"]}
    restoration = {"craft", "dale", "day", "hazel", "mast", "staff", "whale"}
    assert set(before) == {"fright"}
    assert set(after) == restoration | {"fright"}
    assert before["fright"]["outputs"] == after["fright"]["outputs"] == ["fyrhten"]
    assert {row["concept"] for row in report["local_restoration_difference"]} == restoration
    day = next(row for row in report["local_restoration_difference"] if row["concept"] == "day")
    assert day["before_variant_intermediates"]["restoration_before"] == ["*d*æ*g"]
    assert day["before_variant_intermediates"]["restoration_after"] == ["*d*æ*g"]
    assert day["after_variant_intermediates"]["restoration_before"] == ["*d*æ*g*a"]
    assert day["after_variant_intermediates"]["restoration_after"] == ["*d*a*g*a"]
    early = next(row for row in report["variants"]["before-z"]["changed_rows"] if row["concept"] == "beard")
    assert early["intermediates"]["moved_before"] == early["intermediates"]["moved_after"] == ["*b*á*r*d*a*z"]
    assert early["intermediates"]["z_after"] == ["*b*á*r*d*a"]

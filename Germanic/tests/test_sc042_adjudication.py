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


VERIFICATION = AUDIT.parent / "sc042-verification-experiments"


def verification():
    return json.loads((VERIFICATION / "evidence.json").read_text())


def test_verification_preserves_genuine_failure_and_authenticates_the_local_repair():
    manifest = json.loads((VERIFICATION / "manifest.json").read_text())
    assert hashlib.sha256((VERIFICATION / "experiments.zip").read_bytes()).hexdigest() == manifest["archive_sha256"]
    assert hashlib.sha256((VERIFICATION / "evidence.json").read_bytes()).hexdigest() == manifest["evidence_sha256"]
    with zipfile.ZipFile(VERIFICATION / "experiments.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        receipts = {
            "initial": json.loads(archive.read("execution/initial.receipt.json")),
            "followup": json.loads(archive.read("execution/followup.receipt.json")),
        }
        assert not receipts["initial"]["ok"] and receipts["initial"]["returncode"] == 1
        assert receipts["followup"]["ok"] and receipts["followup"]["returncode"] == 0
        for label, receipt in receipts.items():
            assert not receipt["source_changed"]
            for stream in ("stdout", "stderr"):
                assert hashlib.sha256(archive.read(f"execution/{label}.{stream}.log")).hexdigest() == receipt[f"{stream}_sha256"]
        recipes = json.loads(archive.read("followup/snapshot/recipes.json"))
        repair = next(r for r in recipes["recipes"] if r["id"] == "trimoric-z")
        prototype = parse_defines(repair["definitions"])["AF20"].body
        original = parse_defines(archive.read("initial/snapshot/current_fst.txt").decode())
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    normalize = lambda body: " ".join(body.split())
    expected = original["EAFFinalZDeletion"].body.replace(
        "EnglishStarVocalic ?* _ .#.", "[EnglishStarVocalic | {*ô}] ?* _ .#.")
    assert normalize(current["EAFFinalZDeletion"].body) == normalize(expected)
    assert normalize(prototype) == "[ " + normalize(expected) + " ]"
    assert current["PWGmcSurvivingBimoricOUnrounding"].body == original["PWGmcSurvivingBimoricOUnrounding"].body


def test_trimoric_positive_and_bimoric_nasal_protected_negatives_are_independent():
    result = verification()
    initial = {c["id"]: c for c in result["initial"]["controls"]}
    repaired = {c["id"]: c for c in result["followup"]["variants"]["trimoric-z"]["controls"]}
    assert set(initial) == set(repaired)
    assert [name for name, c in initial.items() if not c["passed"]] == ["z-protected-trimoric"]
    assert initial["z-protected-trimoric"]["outputs"] == ["*r*á*t*a*z"]
    assert all(c["passed"] and c["outputs"] == [c["expected"]] for c in repaired.values())
    for name, expected in {
        "z-protected-trimoric": "*r*á*t*a",
        "light-surviving-final": "*r*á*t*ā",
        "heavy-surviving-final": "*r*á*s*t*ā",
        "inherited-oral-final": "*r*á*t*u",
        "bimoric-before-r": "*w*á*t*a*r",
        "trimoric-before-r-negative": "*r*á*t*ô*r",
        "nonfinal-r-negative": "*r*á*t*ō*r*u",
        "already-nasal-final": "*r*á*t*e",
        "trimoric-final": "*n*á*m*a",
        "stressed-monosyllable": "*d*ū",
        "other-final-consonant": "*r*á*t*ō*s",
        "medial-long-o": "*r*á*t*ō*d*u*n",
    }.items():
        assert repaired[name]["outputs"] == [expected]
    assert result["diagnosis"]["parser"][0] == ["*g*é*b*ô*z"]
    assert result["diagnosis"]["full_outputs"][0] == []
    contrast = result["followup"]["variants"]["trimoric-z"]["source_positives"]
    assert contrast["raw"] == ["gébôz", "gébōz", "námô"]
    assert contrast["outputs"] == [["ġiefa"], ["ġiefe"], ["nama"]]


def test_targeted_orderings_preserve_every_output_but_do_not_establish_a_hiatus_history():
    result = verification()["followup"]
    for variant in result["variants"].values():
        assert variant["changed"] == variant["no_output"] == variant["multiple_output"] == 0
        assert len(variant["rows"]) == result["accepted"]
        for row in variant["rows"]:
            assert row["outputs"] == row["baseline_outputs"] and len(row["outputs"]) == 1
    for name in ("after-z", "after-hiatus"):
        rest = next(r for r in result["variants"][name]["rows"] if r["concept"] == "rest")
        assert rest["intermediates"]["moved_before"] == ["*r*á*s*t*ō"]
        assert rest["intermediates"]["moved_after"] == ["*r*á*s*t*ā"]
        assert rest["intermediates"]["final_after"] == ["*r*æ*s*t*ǣ"]
    hiatus = result["hiatus_diagnostic"]
    assert hiatus["early"]["outputs"] == ["*t*ā*w*ō"]
    assert hiatus["post-hiatus"]["outputs"] == ["*t*ā*w*ǣ"]
    assert all("not an attested" in row["status"] for row in hiatus.values())



NASAL = AUDIT.parent / "sc042-nasal-interaction-experiments"


def test_nasal_interaction_failure_is_authentic_and_not_hidden_by_matching_endings():
    manifest = json.loads((NASAL / "manifest.json").read_text())
    data = json.loads((NASAL / "evidence.json").read_text())
    assert hashlib.sha256((NASAL / "experiments.zip").read_bytes()).hexdigest() == manifest["archive_sha256"]
    assert hashlib.sha256((NASAL / "evidence.json").read_bytes()).hexdigest() == manifest["evidence_sha256"]
    with zipfile.ZipFile(NASAL / "experiments.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        for label in ("canonical", "prototype"):
            completion = json.loads(archive.read(label + "/completion.json"))
            receipt = completion["command_receipts"][0]
            assert not receipt["source_changed"]
            assert receipt["ok"] == (label == "prototype")
            for stream in ("stdout", "stderr"):
                name = label + "/results/" + Path(receipt[stream + "_log"]).name
                assert hashlib.sha256(archive.read(name)).hexdigest() == receipt[stream + "_sha256"]
    observed = data["canonical"]
    assert observed["raw_inputs"][:4] == ["rátōz", "rátǭ", "gébōz", "gébǭ"]
    assert observed["final_outputs"][:4] == [["ræte"], ["rate"], ["ġiefe"], ["ġiefe"]]
    checkpoints = {row["stage"]: row["outputs"] for row in observed["checkpoints"]}
    assert checkpoints["EnglishProtoInput"][:2] == [["*r*á*t*ō*z"], ["*r*á*t*ǭ"]]
    assert checkpoints["EAFBrighteningLongFinal"][:2] == [["*r*æ*t*ǣ"], ["*r*æ*t*ǭ"]]
    assert checkpoints["OEARestoration"][:2] == [["*r*æ*t*ǣ"], ["*r*a*t*ǭ"]]
    assert checkpoints["OEUnstressedAEMerger"][:2] == [["*r*æ*t*e"], ["*r*a*t*e"]]


def test_unadopted_nasal_merger_quantifies_all_protected_output_conflicts():
    data = json.loads((NASAL / "evidence.json").read_text())
    proposal = data["proposal"]
    assert proposal["accepted"] == len(proposal["rows"]) == 394
    assert proposal["no_output"] == proposal["multiple_output"] == 0
    changed = {row["concept"]: (row["baseline_outputs"], row["outputs"])
               for row in proposal["rows"] if row["changed"]}
    assert changed == {
        "flask": (["flasce"], ["flæsċe"]),
        "nightmare": (["mare"], ["mære"]),
        "toe": (["tā"], ["tāhe"]),
        "tongue": (["tunge"], ["tunġe"]),
    }
    assert proposal["changed"] == 4 and proposal["matches"] == 382
    for row in proposal["rows"]:
        assert row["changed"] == (row["outputs"] != row["baseline_outputs"])
        assert len(row["outputs"]) == 1
    assert proposal["phonological_controls"]["outputs"] == [
        ["ræte"], ["ræte"], ["ġiefe"], ["ġiefe"], ["ġiefa"], ["nama"]]
    normalize = lambda body: " ".join(body.split())
    with zipfile.ZipFile(NASAL / "experiments.zip") as archive:
        original = parse_defines(archive.read("prototype/snapshot/current_source.txt").decode())
    prototype = parse_defines(proposal["recipe"]["definitions"])
    expected = original["PWGmcSurvivingBimoricOUnrounding"].body.replace(
        "{*ō} -> {*ā}", "[{*ō} | {*ǭ}] -> {*ā}")
    assert normalize(prototype["AF42N"].body) == "[ " + normalize(expected) + " ]"
    assert normalize(prototype["AF20"].body) == "[ " + normalize(original["EAFFinalZDeletion"].body) + " ]"

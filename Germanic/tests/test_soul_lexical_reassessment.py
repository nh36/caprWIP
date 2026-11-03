"""Verify research evidence without adopting its proposed lexical transitions."""
import gzip
import hashlib
import json
from pathlib import Path
import re
import tarfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/soul-lexical-reassessment"


@pytest.fixture(scope="module")
def report():
    return json.loads(gzip.decompress((EVIDENCE / "results.json.gz").read_bytes()))


@pytest.fixture(scope="module")
def followup():
    return json.loads(gzip.decompress((EVIDENCE / "control-results.json.gz").read_bytes()))


def starred(text):
    return "".join("*" + token for token in re.findall(
        r"ēa|ēo|īe|īo|ea|eo|ie|io|ai|au|eu|iu|.", text))


def test_complete_independently_selected_cells_and_unsuccessful_alternatives(report):
    for model in ("C-nonhigh", "G-light-nonhigh", "K-stress-aware"):
        candidates = report["models"][model]["candidates"]
        for key, source, target in (
            ("find-nom-pl", "*fúnðanai", "fundne"),
            ("west-nasal-base", "*wéstą", "west"),
            ("hammer-nom", "*xámaraz", "hamer"),
            ("soul-acc", "*sáiwalǭ", "sāwle"),
        ):
            assert candidates[key]["input"] == source
            assert candidates[key]["final"] == [target]
        assert candidates["west-literal-base"]["final"] == ["westan"]
        assert candidates["west-direction-long"]["final"] == ["westne"]
        assert candidates["west-direction-short"]["final"] == []
        assert candidates["find-nom"]["final"] == ["fundan"]
        assert candidates["find-in-nom"]["final"] == ["fynden"]
    k = report["models"]["K-stress-aware"]["candidates"]
    assert k["find-complete-acc"]["final"] == ["fundenne"]
    assert k["hammer-gen"]["final"] == ["hamres"]
    assert report["models"]["C-nonhigh"]["candidates"]["hammer-gen"]["final"] == ["hameres"]
    assert report["models"]["A-coverage"]["candidates"]["find-nom-pl"]["final"] == ["fundene"]


def test_light_root_extension_and_stress_aware_locality_are_independent(report):
    for name in ("hook-light-gen", "glad-light-gen"):
        source, target = report["controls"][name]
        assert report["component"]["SNonHighSyn"][name] == [starred(source)]
        assert report["component"]["RPosttonic"][name] == [starred(target)]
    for model, expected in (("C-nonhigh", "fæġenes"),
                            ("G-light-nonhigh", "fæġnes"),
                            ("K-stress-aware", "fæġnes")):
        assert report["models"][model]["candidates"]["glad-gen-en"]["final"] == [expected]
    for name in ("marked-prefix-heavy", "longer-posttonic-domain"):
        source, target = report["controls"][name]
        assert report["component"]["TNonHigh"][name] == [starred(source)]
        assert report["component"]["RPosttonic"][name] == [starred(target)]
    source, _ = report["controls"]["marked-primary-root"]
    assert report["component"]["RPosttonic"]["marked-primary-root"] == [starred(source)]
    assert report["component"]["RLocal"]["marked-primary-root"] != [starred(source)]
    assert report["models"]["G-light-nonhigh"]["candidates"]["find-prefixed-nom-pl"]["final"] == [
        "ġefundene"]
    assert report["models"]["K-stress-aware"]["candidates"]["find-prefixed-nom-pl"]["final"] == [
        "ġefundne"]


def test_nonhigh_negatives_do_not_conceal_unchanged_high_vowel_gaps(report, followup):
    assert report["component"]["RPosttonic"]["lord-high-closed"] == []
    assert followup["prior_invalid_control"] == []
    for name, (source, target) in followup["controls"].items():
        if source == target:
            assert followup["component"]["RPosttonic"][name] == [starred(source)], name
    k = report["models"]["K-stress-aware"]["candidates"]
    for name, target in (("summer-nom", "sumer"), ("water-nom", "wæter"),
                         ("over-base", "ofer"), ("over-i", "ofer")):
        assert k[name]["final"] == [target]
    for name, actual in (("idle-fem", "īdel"), ("blessed-fem", "ēadiġ"),
                         ("head-neut-pl", "hēafod"), ("head-gen", "hēafodes"),
                         ("many-gen", "manġes")):
        assert k[name]["final"] == [actual]
        assert k[name]["final"] != [k[name]["expected"]]
    assert k["glad-gen-an"]["final"] == ["fagnes"]
    assert report["models"]["J-open-medial"]["candidates"]["idle-fem"]["final"] == ["īdl"]


def test_frozen_k_comparator_replay_and_correct_stage_symbols(followup):
    assert followup["definitions_equal_to_assay03"]
    assert followup["production_unchanged"]
    assert followup["reused_report_sha256"] == hashlib.sha256(
        (EVIDENCE / "results.json.gz").read_bytes()).hexdigest()
    assert followup["component"]["RPosttonic"]["lord-high-closed"] == [starred("drixtin")]
    assert followup["component"]["RPosttonic"]["beg-cluster-limit"] == [starred("bedekian")]
    for name, expected in (("kettle", "ċietel"), ("angel", "enġl"),
                           ("health", "hǣlþ"), ("theft", "þīefþ"), ("warmth", "wiermeþ")):
        assert followup["probes"][name]["production"] == [expected]
        assert followup["probes"][name]["K"] == [expected]


def test_all_sparse_intermediates_reconstruct_candidates_and_composed_outputs(report):
    offset = len(report["rows"]) + len(report["immutable380"])
    baseline = report["models"]["A-production"]["final"]
    for model in report["models"].values():
        states = [[value] for value in report["input_order"]]
        assert len(model["order"]) == len(model["transitions"])
        for position, (name, stage) in enumerate(zip(model["order"], model["transitions"])):
            assert name == stage["stage"]
            for index, candidate in enumerate(report["candidates"], offset):
                trace = model["candidate_traces"][candidate["id"]][position]
                assert trace["stage"] == name
                assert trace["before"] == states[index]
            changed = set()
            for change in stage["changes"]:
                index = change["index"]
                assert index not in changed
                changed.add(index)
                assert states[index] == change["before"]
                assert change["before"] != change["after"]
                states[index] = change["after"]
            for index, candidate in enumerate(report["candidates"], offset):
                assert model["candidate_traces"][candidate["id"]][position]["after"] == states[index]
        assert states == model["final"]
        assert model["composed_crosscheck"]
        assert not model["finite_ambiguity"]
        assert model["matched"] == sum(
            row["counterpart"] in values for row, values in zip(report["rows"], states))
        assert {d["row_id"] for d in model["deltas"]} == {
            row["row_id"] for i, row in enumerate(report["rows"]) if states[i] != baseline[i]}
        assert {d["concept"] for d in model["immutable380_deltas"]} == {
            row["concept"] for i, row in enumerate(report["immutable380"], len(report["rows"]))
            if states[i] != baseline[i]}
    k = report["models"]["K-stress-aware"]
    assert {d["concept"] for d in k["deltas"]} == {"find", "hammer", "soul", "west"}
    assert {d["concept"] for d in k["immutable380_deltas"]} == {"find", "hammer", "soul", "west"}


def test_protected_histories_and_unchanged_high_vowel_stages(report):
    protected = {"world", "earthly", "rainbow", "nettle", "spindle", "filth",
                 "thistle", "flask", "nightmare", "toe", "tongue"}
    indices = [i for i, row in enumerate(report["rows"]) if row["concept"] in protected]
    for model in report["models"].values():
        states = [[value] for value in report["input_order"]]
        for stage in model["transitions"]:
            for change in stage["changes"]:
                if change["index"] in indices:
                    assert stage["stage"] != "RPosttonic"
                states[change["index"]] = change["after"]
        for i in indices:
            assert states[i] == report["models"]["A-production"]["final"][i]
    for name in ("A-production", "A-coverage"):
        assert not report["models"][name]["deltas"]
        assert not report["models"][name]["immutable380_deltas"]
    assert report["production_unchanged"]
    assert report["protected_before"] == report["protected_after"]
    for relative in ("fsts/germanic.txt", "data/germanic-aligned-final.tsv"):
        assert hashlib.sha256((ROOT / "Germanic" / relative).read_bytes()).hexdigest() == (
            report["protected_before"]["/usr/app/" + relative])


def test_parser_and_native_formal_limits_are_not_relabelled_global_success(report):
    assert not report["parser_evidence"]["repaired_ambiguities"]
    for name, result in report["formal"].items():
        assert result["stdout"].startswith("0 " if name.startswith("RWhole") else "1 ")
    decision = json.loads((EVIDENCE / "decision.json").read_text())
    assert decision["verdict"] == "DEFER"
    assert not decision["intended_source_modifications"]


def test_evidence_archive_preserves_failed_receipts_and_all_frozen_inputs():
    manifest = json.loads((EVIDENCE / "evidence-manifest.json").read_text())
    assert hashlib.sha256((EVIDENCE / "evidence.tar.gz").read_bytes()).hexdigest() == (
        manifest["archive_sha256"])
    with tarfile.open(EVIDENCE / "evidence.tar.gz") as archive:
        members = {member.name: archive.extractfile(member).read()
                   for member in archive.getmembers() if member.isfile()}
    assert set(members) == set(manifest["members"])
    for name, data in members.items():
        assert hashlib.sha256(data).hexdigest() == manifest["members"][name]
    candidate_hashes = []
    attempts = list(zip(manifest["attempts"], (False, False, True)))
    attempts += [(name, True) for name in manifest["followups"]]
    for attempt, outcome in attempts:
        frozen = json.loads(members[attempt + "/receipt.json"])
        for entry in frozen["inputs"].values():
            path = attempt + "/snapshot/" + entry["snapshot_name"]
            assert hashlib.sha256(members[path]).hexdigest() == entry["sha256"]
            if entry["original_path"].endswith("/candidates.json"):
                candidate_hashes.append(entry["sha256"])
        commands = [json.loads(data) for name, data in members.items()
                    if name.startswith(attempt + "/results/") and name.endswith(".receipt.json")]
        assert len(commands) == 1
        command = commands[0]
        assert command["ok"] is outcome
        assert not command["source_changed"]
        for field in ("stdout", "stderr"):
            path = attempt + "/results/" + Path(command[field + "_log"]).name
            assert hashlib.sha256(members[path]).hexdigest() == command[field + "_sha256"]
    assert len(set(candidate_hashes)) == 1

"""Source-bound research comparisons do not authorize a selected-cell migration."""
import gzip
import hashlib
import json
from pathlib import Path
import re
import tarfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/soul-syncope-resolution"


@pytest.fixture(scope="module")
def report():
    return json.loads(gzip.decompress((EVIDENCE / "results.json.gz").read_bytes()))


@pytest.fixture(scope="module")
def followup():
    return json.loads(gzip.decompress((EVIDENCE / "control-results.json.gz").read_bytes()))


def starred(text):
    return "".join("*" + token for token in re.findall(
        r"ēa|ēo|īe|īo|ea|eo|ie|io|ai|au|eu|iu|.", text))


def output(report, model, concept):
    index = next(i for i, row in enumerate(report["rows"]) if row["concept"] == concept)
    return report["models"][model]["final"][index]


def test_nonhigh_only_is_sufficient_for_accusative_not_for_all_selected_histories(report):
    for name in ("C-nonhigh", "D-nonhigh-fulk-apo", "E-high-retained",
                 "F-old-broad-A", "G-light-nonhigh"):
        model = report["models"][name]
        assert model["candidates"]["soul-acc"]["final"] == ["sāwle"]
        assert "OEInterStressRaising" not in model["order"]
        assert "OELHWeakRaising" in model["order"]
        for control, expected in (("good-acc", "gōdne"), ("blind-acc", "blindne")):
            assert model["candidates"][control]["final"] == [expected]
        assert model["candidates"]["find-complete-acc"]["final"] == ["fundenene"]
    c = report["models"]["C-nonhigh"]
    assert "OEHighVowelApocope" in c["order"]
    assert {"OEMedialSyncope", "OELAdjacentSyncope"} <= set(c["order"])
    assert {row["concept"] for row in c["deltas"]} == {"find", "soul", "west"}
    assert output(report, "C-nonhigh", "find") == ["fundne"]
    assert output(report, "C-nonhigh", "west") == ["westne"]


def test_factorial_separates_apocope_and_each_legacy_syncope_operation(report):
    c, d, e = (report["models"][name] for name in
               ("C-nonhigh", "D-nonhigh-fulk-apo", "E-high-retained"))
    assert c["final"][:771] == report["models"]["E-high-old-apo"]["final"][:771]
    assert d["final"][:771] == e["final"][:771]
    for name in ("D-nonhigh-fulk-apo", "E-high-retained"):
        assert output(report, name, "nettle") == ["netle"]
        assert output(report, name, "spindle") == ["spinlu"]
        assert output(report, name, "filth") == ["fȳlþu"]
    assert output(report, "E-no65", "filth") == ["fȳleþu"]
    assert output(report, "E-no65", "nettle") == ["netle"]
    assert output(report, "E-no66", "filth") == ["fȳlþu"]
    assert output(report, "E-no66", "spindle") == ["spinnelu"]
    assert output(report, "E-no66", "nettle") == ["netele"]
    old_thistle = next(s for s in c["traces"]["2250"]
                       if s["stage"] == "OELAdjacentSyncope")
    new_thistle = next(s for s in e["traces"]["2250"]
                       if s["stage"] == "OELAdjacentSyncope")
    assert old_thistle["before"] != old_thistle["after"]
    assert new_thistle["before"] == new_thistle["after"]


def test_independent_light_root_controls_expose_a_real_scope_gap(report, followup):
    for control in ("hook-light-gen", "glad-light-gen"):
        raw, expected = report["controls"][control]
        assert report["component"]["SNonHighSyn"][control] == [starred(raw)]
        assert report["component"]["TNonHigh"][control] == [starred(expected)]
    assert output(report, "G-light-nonhigh", "hammer") == ["hamres"]
    assert report["component"]["SFulkSyn"]["lord-high-closed"] == []
    for values in followup["component"].values():
        assert values["lord-high-closed"] == [starred("drixtin")]
        assert values["beg-cluster-limit"] == [starred("bedekian")]
    assert followup["definitions_equal_to_factorial"]
    assert followup["reused_report_sha256"] == hashlib.sha256(
        (EVIDENCE / "results.json.gz").read_bytes()).hexdigest()
    for probe in followup["probes"].values():
        assert probe["production"] == probe["C"]
    assert followup["probes"]["kettle"]["C"] == ["ċietel"]
    assert followup["probes"]["angel"]["C"] == ["enġl"]
    assert followup["probes"]["health"]["C"] == ["hǣlþ"]
    assert followup["probes"]["theft"]["C"] == ["þīefþ"]
    assert followup["probes"]["warmth"]["C"] == ["wiermeþ"]


def test_sparse_evidence_reconstructs_every_intermediate_and_final_state(report):
    indices = {row["row_id"]: i for i, row in enumerate(report["rows"])}
    for model in report["models"].values():
        states = [[value] for value in report["input_order"]]
        assert len(model["order"]) == len(model["transitions"])
        for position, (name, stage) in enumerate(zip(model["order"], model["transitions"])):
            assert name == stage["stage"]
            for row_id, trace in model["traces"].items():
                assert trace[position]["before"] == states[indices[row_id]]
            changed = set()
            for change in stage["changes"]:
                index = change["index"]
                assert index not in changed
                changed.add(index)
                assert states[index] == change["before"]
                assert change["before"] != change["after"]
                states[index] = change["after"]
            for row_id, trace in model["traces"].items():
                assert trace[position]["after"] == states[indices[row_id]]
        assert states == model["final"]
        assert model["composed_crosscheck"]
        assert not model["finite_ambiguity"]


def test_population_and_established_sc040_histories_are_not_refrozen(report):
    baseline = report["models"]["A-production"]
    assert report["production_unchanged"]
    assert report["protected_before"] == report["protected_after"]
    for model in report["models"].values():
        assert not ({"2148", "2302", "2336"} & {r["row_id"] for r in model["deltas"]})
        for row_id in ("2148", "2302", "2336"):
            previous = next(s for s in baseline["traces"][row_id]
                            if s["stage"] == "OEMedUnstressedULowering")
            current = next(s for s in model["traces"][row_id]
                           if s["stage"] == "OEMedUnstressedULowering")
            assert current == previous
    for name in ("A-production", "A-coverage"):
        assert not report["models"][name]["deltas"]
        assert not report["models"][name]["immutable380_deltas"]
    previous = json.loads(gzip.decompress(
        (EVIDENCE.parent / "soul-fulk-oblique/results.json.gz").read_bytes()))
    assert report["models"]["C-nonhigh"]["final"][:391] == previous["models"]["C-nonhigh"]["final"]
    assert report["models"]["F-old-broad-A"]["final"][:391] == previous["models"]["A-fulk"]["final"]
    for relative, key in (("fsts/germanic.txt", "/usr/app/fsts/germanic.txt"),
                          ("data/germanic-aligned-final.tsv", "/usr/app/data/germanic-aligned-final.tsv")):
        assert hashlib.sha256((ROOT / "Germanic" / relative).read_bytes()).hexdigest() == (
            report["protected_before"][key])


def test_native_formal_limits_and_authentic_archived_inputs_are_preserved(report):
    for name in ("SNonHighSyn", "SFulkSyn", "SFulkApo", "TNonHigh"):
        assert report["formal"][name]["stdout"].startswith("1 ")
    assert report["formal"]["TWhole0"]["stdout"].startswith("0 ")
    decision = json.loads((EVIDENCE / "decision.json").read_text())
    assert decision["verdict"] == "DEFER"
    assert not decision["intended_source_modifications"]
    manifest = json.loads((EVIDENCE / "evidence-manifest.json").read_text())
    assert hashlib.sha256((EVIDENCE / "evidence.tar.gz").read_bytes()).hexdigest() == (
        manifest["archive_sha256"])
    with tarfile.open(EVIDENCE / "evidence.tar.gz") as archive:
        members = {member.name: member for member in archive.getmembers() if member.isfile()}
        assert set(members) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.extractfile(members[name]).read()).hexdigest() == digest
        for attempt in manifest["attempts"]:
            receipt = json.load(archive.extractfile(attempt + "/receipt.json"))
            for entry in receipt["inputs"].values():
                assert manifest["members"][attempt + "/snapshot/" + entry["snapshot_name"]] == (
                    entry["sha256"])

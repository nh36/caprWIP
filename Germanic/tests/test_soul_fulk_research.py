"""Research evidence is not permission to adopt a general syncope cascade."""
import gzip
import hashlib
import json
from pathlib import Path
import re
import tarfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/soul-fulk-oblique"


@pytest.fixture(scope="module")
def report():
    return json.loads(gzip.decompress((EVIDENCE / "results.json.gz").read_bytes()))


def starred(text):
    return "".join("*" + token for token in re.findall(
        r"ēa|ēo|īe|īo|ea|eo|ie|io|ai|au|eu|iu|.", text))


def test_inherited_accusative_and_unrounded_ending_converge_without_proxy(report):
    for model in ("A-fulk", "A-unrounded-ending", "C-nonhigh"):
        candidate = report["models"][model]["candidates"]["soul-acc"]
        assert candidate["input"] == "*sáiwalǭ"
        assert candidate["final"] == ["sāwle"]
        assert "OEInterStressRaising" not in report["models"][model]["order"]
        syncope = next(s for s in candidate["steps"]
                       if s["stage"] in ("SFulkSyn", "SNonHighSyn"))
        assert syncope["before"] != syncope["after"]
        assert "*a*l" in syncope["before"][0] or "*æ*l" in syncope["before"][0]
        assert "*w*l" in syncope["after"][0]
    original = report["models"]["input-coverage"]["candidates"]["soul-acc"]
    assert original["final"] == ["sāwele"]
    unrounded = report["models"]["A-unrounded-ending"]["candidates"]["soul-acc"]
    step = next(s for s in unrounded["steps"] if s["stage"] == "SAccUnround")
    assert step["before"][0].endswith("*ǭ")
    assert step["after"][0].endswith("*ā")


def test_heavy_following_syncope_has_independent_positive_and_negative_controls(report):
    for name, (_, expected) in report["controls"].items():
        assert report["component"]["SFulkSyn"][name] == [starred(expected)], name
    for name in ("soul-light", "idle-light", "head-light", "cattle-shortened-light"):
        before = starred(report["controls"][name][0])
        assert report["component"]["SFulkApo"][name] == [before]
    assert report["component"]["SFulkApo"]["light-initial"] == [starred("werud")]


def test_retention_and_quantity_cannot_be_hidden_by_correct_accusative(report):
    staged = report["staged"]["A-fulk"]
    assert staged["soul-long-nasal"]["final"] == ["sāwle"]
    assert staged["soul-prematurely-shortened"]["final"] == ["sāwele"]
    assert staged["idle-light"]["final"] == ["īdelu"]
    assert staged["head-closed"]["final"] == ["hēafdes"]
    assert staged["head-light"]["final"] == ["hēafodu"]
    assert report["models"]["A-fulk"]["candidates"]["soul-nom"]["final"] == ["sāwelu"]
    assert report["models"]["A-fulk"]["candidates"]["blessed-fem"]["final"] == ["ēadegu"]
    assert report["models"]["A-fulk"]["candidates"]["soul-dat-fulk"]["final"] == ["sāwelai"]
    assert report["models"]["A-fulk"]["candidates"]["soul-gen-fulk"]["final"] == ["sāwla"]


def test_general_epenthesis_is_not_an_accepted_rescue(report):
    assert report["epenthesis"]["soul"] == [starred("sāwol")]
    assert report["epenthesis"]["oblique"] == [starred("sāwle")]
    assert report["epenthesis"]["dental-negative"] == [starred("setl")]
    for name, expected in (("bird", "fugol"), ("star", "tungol"), ("banner", "cumbol")):
        assert report["epenthesis"][name] == [starred(expected)]
    changes = {r["concept"]: r for r in report["models"]["B-general-l-epenthesis"]["deltas"]}
    assert changes["fell"]["new"] == ["felel"]
    assert changes["hall"]["new"] == ["healel"]
    assert report["models"]["B-no-new-epenthesis"]["candidates"]["soul-nom"]["final"] == ["sāwl"]


def test_selected_and_immutable_populations_are_not_silently_refrozen(report):
    assert report["production_unchanged"]
    assert report["protected_before"] == report["protected_after"]
    assert len(report["rows"]) == 391
    for name in ("identity", "input-coverage"):
        assert report["models"][name]["matched"] == 383
        assert not report["models"][name]["deltas"]
        assert not report["models"][name]["immutable380_deltas"]
    assert report["models"]["A-fulk"]["matched"] == 377
    for model in report["models"].values():
        assert model["composed_crosscheck"]
        assert not ({"2148", "2302", "2336"} & {r["row_id"] for r in model["deltas"]})
    assert {r["concept"] for r in report["models"]["A-fulk"]["deltas"]} == {
        "find", "nettle", "soul", "spindle", "west", "filth"}


def test_failed_attempts_and_immutable_inputs_remain_verifiable():
    manifest = json.loads((EVIDENCE / "evidence-manifest.json").read_text())
    assert hashlib.sha256((EVIDENCE / "evidence.tar.gz").read_bytes()).hexdigest() == (
        manifest["archive_sha256"])
    with tarfile.open(EVIDENCE / "evidence.tar.gz") as archive:
        files = {member.name: member for member in archive.getmembers() if member.isfile()}
        assert set(files) == set(manifest["members"])
        for name, expected in manifest["members"].items():
            assert hashlib.sha256(archive.extractfile(files[name]).read()).hexdigest() == expected
        failed = json.load(archive.extractfile("soul-fulk-01/completion.json"))
        assert failed["outcome"] == "failed"
        for attempt in manifest["attempts"]:
            snapshot = json.load(archive.extractfile(attempt + "/receipt.json"))
            for entry in snapshot["inputs"].values():
                assert manifest["members"][attempt + "/snapshot/" + entry["snapshot_name"]] == (
                    entry["sha256"])

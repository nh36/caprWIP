"""Authenticate the corrected-control trials without rerunning their sweeps."""
import functools
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/sc047-sc048-followup-evidence"


@functools.lru_cache(maxsize=1)
def observations():
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    payload = (EVIDENCE / "experiments.zip").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == manifest["archive_sha256"]
    result = {}
    with zipfile.ZipFile(EVIDENCE / "experiments.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        for label, snapshot in manifest["snapshots"].items():
            prefix = snapshot + "/"
            raw = archive.read(prefix + "results/observed.json")
            completion = json.loads(archive.read(prefix + "completion.json"))
            receipt, = completion["command_receipts"]
            assert completion["outcome"] == "passed" and receipt["ok"]
            assert hashlib.sha256(raw).hexdigest() == receipt["stdout_sha256"]
            result[label] = json.loads(raw)
            assert result[label]["source_sha256"] == manifest["source_sha256"]
            assert result[label]["corpus_sha256"] == manifest["corpus_sha256"]
    return result


def deltas(run, label):
    return {row["row_id"]: row["outputs"] for row in run["corpus"][label]["rows"]
            if row["baseline"] != row["outputs"]}


def test_full_output_projection_matches_the_executed_relations():
    data = json.loads((EVIDENCE / "evidence.json").read_text())
    for phase, observed in observations().items():
        expected = {}
        for label, result in observed["corpus"].items():
            assert len(result["rows"]) == 394
            expected[label] = {key: value for key, value in result.items() if key != "rows"}
            expected[label]["deltas"] = [
                row for row in result["rows"] if row["baseline"] != row["outputs"]]
            assert result["changed"] == len(expected[label]["deltas"])
        assert data["runs"][phase] == expected
        assert data["cost"][phase] == observed["cost"]
        assert deltas(observed, "identity") == {}
        assert observed["corpus"]["identity"]["matches"] == 386
    for label in ["loss_after_rhotacism", "loss_after_SC041",
                  "early_coda_i_onset_restore", "early_direct_coda"]:
        assert deltas(observations()["staged"], label) == {}


def test_prior_lowering_recovers_every_firing_but_not_the_other_dependencies():
    observed = observations()["controlled"]
    populations = {}
    for label in observed["corpus"]:
        before = observed["queries"][label + ":census:PNWGmcULowering:before"]["outputs"]
        after = observed["queries"][label + ":census:PNWGmcULowering:after"]["outputs"]
        populations[label] = {
            row["row_id"] for row, left, right in zip(observed["rows"], before, after)
            if left != right}
    original = populations["identity"]
    assert len(original) == 40
    assert populations["lower_only_pre_gemination"] == original
    assert populations["lower_then_loss_pre_gemination"] == original
    assert populations["loss_only_pre_gemination"] < original
    assert len(original - populations["loss_only_pre_gemination"]) == 13
    assert "2307" in original - populations["loss_only_pre_gemination"]
    assert "2307" not in deltas(observed, "loss_only_pre_gemination")
    assert deltas(observed, "lower_only_pre_gemination") == {}
    assert len(deltas(observed, "loss_only_pre_gemination")) == 14
    assert deltas(observed, "lower_then_loss_pre_gemination") == {
        "1988": ["dēo"], "1992": ["dōr"], "2224": ["stræw"]}
    staged = observations()["staged"]
    assert deltas(staged, "loss_after_ordinary_z") == {
        "1988": ["dēo"], "1992": ["dōr"]}
    assert deltas(staged, "before_SC023_negative")["1991"] == []


def test_source_staged_nuclearization_preserves_quantity_and_exposes_limits():
    observed = observations()["resolution"]
    query = observed["queries"]
    prefix = "pre_gemination_nuclearization:glides:"
    assert query[prefix + "FNU"]["outputs"] == [
        ["*s*á*r*u"], ["*r*ī*k*ī"], ["*s*á*g*j*a*s"]]
    assert query[prefix + "PWGmcJGemination"]["outputs"][2] == ["*s*á*g*g*j*a*s"]
    assert query[prefix + "OEARestoration"]["outputs"][0] == ["*s*a*r*u"]
    assert query[prefix + "OEHighVowelApocope"]["outputs"][1] == ["*r*ī*ʧ*ī"]
    assert query[prefix + "OldEnglishSurface"]["outputs"][:2] == [
        ["saru"], ["rīċe"]]
    assert deltas(observed, "pre_gemination_nuclearization") == {
        "1988": ["dēo"], "1992": ["dōr"], "2061": ["hēa"],
        "2138": ["nete"], "2224": ["stræw"], "2332": ["hii"]}
    staged = observations()["staged"]["queries"]
    assert staged["oral_loss_nuclearization"]["outputs"] == [["*g*é*l*u"]]
    assert query["ordinary_oral_glide_full"]["outputs"] == [["ġielu"]]


def test_coda_consumer_source_cells_and_carrier_are_not_conflated():
    query = observations()["staged"]["queries"]
    assert query["early_coda:staged:OESecondaryNasalization"]["outputs"][0] == [
        "*b*í*n*d*ą*n*d*ī"]
    assert query["local:nasal_i_first_step"]["outputs"][0] == ["*b*í*n*d*æ*n*d*ī"]
    assert query["early_coda:staged:OldEnglishSurface"]["outputs"][0] == ["bindande"]
    for label in ["identity", "early_coda_i_onset_restore", "early_direct_coda"]:
        assert query[label + ":staged:OldEnglishSurface"]["outputs"][:2] == [
            ["bindende"], ["bindan"]]
        assert query[label + ":guma:OldEnglishSurface"]["outputs"][:5] == [
            ["gumn"], ["guman"], ["guman"], ["gymen"], ["gymen"]]
    resolved = observations()["resolution"]["queries"]
    for label in ["early_coda_i_onset_restore", "early_direct_coda"]:
        assert resolved[label + ":onset:OldEnglishSurface"]["outputs"][:2] == [
            ["gumne"], ["gumne"]]
    assert resolved["early_coda_i_onset_restore:onset:OldEnglishSurface"]["outputs"][2] == [
        "gumena"]
    assert resolved["early_direct_coda:onset:OldEnglishSurface"]["outputs"][2] == [
        "gumana"]

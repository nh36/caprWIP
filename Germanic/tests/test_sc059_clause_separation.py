"""Authenticate SC059's composed-clause correction without rewriting older trials."""
import functools
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines

EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/sc059-clause-evidence"
OLD_EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/sc047-sc048-evidence"


@functools.lru_cache(maxsize=1)
def separated_sources():
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    source = subprocess.check_output(
        ["git", "show", manifest["base_commit"] + ":Germanic/fsts/germanic.txt"], cwd=ROOT)
    assert hashlib.sha256(source).hexdigest() == manifest["source_sha256"]
    archived = OLD_EVIDENCE / "unadopted-strict-ws.patch"
    assert hashlib.sha256(archived.read_bytes()).hexdigest() == manifest["archived_patch_sha256"]
    with tempfile.TemporaryDirectory() as temporary:
        target = Path(temporary) / "Germanic/fsts/germanic.txt"
        target.parent.mkdir(parents=True)
        target.write_bytes(source)
        subprocess.run(["git", "apply", str(archived)], cwd=temporary,
                       check=True, capture_output=True)
        candidate = target.read_bytes()
    assert hashlib.sha256(candidate).hexdigest() == manifest["candidate_sha256"]
    before, after = parse_defines(source.decode()), parse_defines(candidate.decode())
    assert before.keys() == after.keys()
    assert {name for name in before if before[name].body != after[name].body} == {
        "OEBackMutation"}
    return before, after


def before_sc059_separation(current):
    """Peel only the authenticated correction before checking historical layers."""
    before, after = separated_sources()
    assert current["OEBackMutation"].body == after["OEBackMutation"].body
    result = dict(current)
    result["OEBackMutation"] = before["OEBackMutation"]
    return result


@functools.lru_cache(maxsize=1)
def observations():
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    payload = (EVIDENCE / "experiment.zip").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == manifest["archive_sha256"]
    with zipfile.ZipFile(EVIDENCE / "experiment.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        prefix = manifest["snapshot"] + "/"
        raw = archive.read(prefix + "results/observed.json")
        completion = json.loads(archive.read(prefix + "completion.json"))
        assert completion["outcome"] == "passed"
        receipt, = completion["command_receipts"]
        assert receipt["ok"] and hashlib.sha256(raw).hexdigest() == receipt["stdout_sha256"]
        plan = json.loads(archive.read(prefix + "snapshot/plan.json"))
    observed = json.loads(raw)
    assert observed["source_sha256"] == manifest["source_sha256"]
    assert observed["corpus_sha256"] == manifest["corpus_sha256"]
    _, after = separated_sources()
    executed = parse_defines(plan["definitions"]["FS59"])["FS59"].body
    assert "".join(after["OEBackMutation"].body.split()) == "".join(executed.split())
    return observed


def test_archived_candidate_is_the_live_clause_separation():
    _, after = separated_sources()
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    assert current["OEBackMutation"].body == after["OEBackMutation"].body
    query = observations()["queries"]["separate:local"]
    assert query["outputs"] == [
        ["*s*t*eo*l*u*n"], ["*s*t*e*l*a*n"],
        ["*s*t*éo*l*u*n"], ["*s*t*é*l*a*n"],
        ["*g*e*b*eo*b*u"], ["*g*e*b*è*b*a"],
        ["*g*e*b*e*b*u"], ["*ea*l*u"], ["*ea*l*a"],
        ["*g*e*b*ea*b*a"], ["*g*e*b*æ*b*u"], ["*s*t*æ*ð*u*l"]]
    assert observations()["queries"]["separate:ealu_staged"]["outputs"] == [["ealu"]]


def test_every_selected_output_and_corrected_displacement_are_accounted_for():
    observed = observations()
    for label in ["identity", "separate", "separate_late_nasal"]:
        summary = observed["corpus"][label]
        assert len(summary["rows"]) == 394 and summary["matches"] == 386
        assert summary["changed"] == summary["rejected"] == summary["ambiguous"] == 0
        assert all(row["baseline"] == row["outputs"] for row in summary["rows"])
    old = observed["corpus"]["old_late_nasal"]
    assert {row["concept"]: row["outputs"] for row in old["rows"]
            if row["baseline"] != row["outputs"]} == {
                "steal": ["steolan"], "weave": ["weofan"]}
    assert observed["queries"]["separate:raw_controls"]["outputs"] == [
        ["reġnboga"], ["boga"], ["eorþcunde"], ["reġnbecan"],
        ["reġnheofon"], ["reġnhbon"]]
    later = observed["corpus"]["separate_late_back"]
    assert later["matches"] == 382 and later["changed"] == 4
    assert later["rejected"] == later["ambiguous"] == 0
    assert {row["concept"]: row["outputs"] for row in later["rows"]
            if row["baseline"] != row["outputs"]} == {
                "heaven": ["hefon"], "milk": ["meloc"],
                "seven": ["sefon"], "world": ["werold"]}

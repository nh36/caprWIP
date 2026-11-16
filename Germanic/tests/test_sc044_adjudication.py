"""Source-bound paired controls for the SC044 adjudication."""
import csv
import functools
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Germanic/docs/sound_changes/audits/sc044-breaking-evidence"
BASE = "54b15a2d3a764d5ac92c9ce0c1ecaf398aed878f"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines


@functools.lru_cache(maxsize=1)
def source_pair():
    archive_path = AUDIT / "experiments.zip"
    assert hashlib.sha256(archive_path.read_bytes()).hexdigest() == (
        AUDIT / "archive.sha256").read_text().split()[0]
    report = json.loads((AUDIT / "observed.json").read_text())
    with zipfile.ZipFile(archive_path) as archive:
        name = report["secondary_snapshot_id"] + "/snapshot/candidate.txt"
        adopted = archive.read(name)
    control = subprocess.check_output(
        ["git", "show", BASE + ":Germanic/fsts/germanic.txt"], cwd=ROOT)
    report = json.loads((AUDIT / "observed.json").read_text())
    assert hashlib.sha256(adopted).hexdigest() == report["adopted"]["source_sha256"]
    return parse_defines(control.decode()), parse_defines(adopted.decode())


def before_sc044_adoption(current):
    """Verify the exact new promotion, then preserve all older historical guards."""
    control, adopted = source_pair()
    retired = {"EnglishBreakingXContextNonWeakA", "EnglishBreakingXContextWeakTail"}
    assert current.keys() == adopted.keys() - retired
    for name in current:
        assert "".join(current[name].body.split()) == "".join(adopted[name].body.split()), name
    return control


@pytest.fixture(scope="module")
def observed():
    before_sc044_adoption(parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text()))
    return json.loads((AUDIT / "observed.json").read_text())


@pytest.mark.parametrize(("identifier", "expected"), [
    ("seal-lx", "*s*éo*l*x"),
    ("languish-selk", "*s*éo*l*k*a*n"),
    ("milk-melk", "*m*é*l*k*a*n"),
    ("unwitnessed-elg", "*b*é*l*g*a*n"),
    ("yellow-lw", "*g*éo*l*w*æ"),
    ("self-ws", "*s*é*l*f"),
    ("southern-half", "*x*ea*l*f"),
    ("palatal-sellan", "*s*æ*l*l*j*a*n"),
    ("filhith-short-i", "*f*ío*l*x*i*θ"),
    ("fulwiht-weak", "*f*u*l*w*i*x*t"),
    ("explicit-secondary-i", "*x*á*m*w*io*x*t"),
    ("weak-ae", "*x*á*m*æ*r*d"),
    ("weak-e", "*x*á*m*e*r*d"),
    ("weak-selk", "*x*á*m*s*e*l*k"),
    ("knee-short", "*k*n*éo*w*ē"),
    ("w-before-i", "*k*n*é*w*i"),
    ("erian-rj", "*æ*r*j*a*n"),
    ("near-long", "*n*ēa*x"),
    ("light-weight-long", "*l*īo*x*t"),
    ("long-not-weak", "*x*á*m*ī*x*t"),
    ("secondary-ae", "*s*æ*l*io*w*ea*r*d"),
    ("secondary-e", "*x*á*m*eo*r*d"),
    ("secondary-rj", "*x*á*m*æ*r*j*a"),
])
def test_vowel_specific_positive_and_negative_controls(observed, identifier, expected):
    assert observed["adopted"]["components"]["component:OEBreaking"][identifier] == [expected]


def test_short_quantity_and_the_removed_overlapping_fallback(observed):
    old = observed["experiments"]["control"]["components"]["component:OEBreaking"]
    new = observed["adopted"]["components"]["component:OEBreaking"]
    assert old["x-a-bare"] == ["*s*l*ea*x", "*s*l*ēa*x"]
    assert new["x-a-bare"] == ["*s*l*a*x"]
    assert new["x-æ-*a*n*ą"] == ["*s*l*ea*x*a*n*ą"]
    normal = {r["id"]: r["outputs"] for r in observed["adopted"]["raw"]}
    assert {key: normal[key] for key in ("slay", "hell", "sell", "milk",
                                        "flask-nompl", "flask-datsg", "maere")} == {
        "slay": ["slēan"], "hell": ["hell"], "sell": ["sellan"], "milk": ["melcan"],
        "flask-nompl": ["flascan"], "flask-datsg": ["flascan"], "maere": ["mære"]}


def test_mutation_created_e_really_distinguishes_the_finite_orders(observed):
    components = observed["pre_secondary_carry"]["components"]
    early, late = (components["component:" + name] for name in ("AFConventional", "AFLate"))
    assert early["farmjan"] == ["*f*e*r*m*j*a*n"]
    assert late["farmjan"] == ["*f*eo*r*m*j*a*n"]
    assert early["germantlab"] == late["germantlab"] == ["*g*eo*r*m*a*n*t*l*æ*β"]
    assert early["tar-consonantal-w"] == ["*t*eo*r*w*u"]
    assert late["tar-consonantal-w"] == ["*t*e*r*w*u"]
    assert early["tar-vocalized-w"] == late["tar-vocalized-w"] == ["*t*e*r*u"]


def test_subordinate_root_survives_without_weak_linker_breaking(observed):
    raw = {row["id"]: row for row in observed["adopted"]["raw"]}
    for i in range(3):
        row = raw["compound-" + str(i)]
        assert row["outputs"] == ["seleweard"]
        assert "*ǽ" in row["trace"]["EAFBrightening"][0]
        assert "*ǽ" not in row["trace"]["OEBreaking"][0]


def test_complete_selected_records_are_conserved(observed):
    with (AUDIT / "corpus-comparison.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == len({row["row_id"] for row in rows}) == 394
    assert all(row["identical_record"] == "1" for row in rows)
    assert observed["adopted"]["corpus_delta"] == []
    assert observed["adopted"]["summary"] == observed["summary"]


@pytest.mark.runtime
def test_west_saxon_vowel_order_with_live_remainder(isolated_definitions, record_testsuite_property):
    import importlib.util
    spec = importlib.util.spec_from_file_location("sc044_west_saxon", AUDIT / "west_saxon.py")
    experiment = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(experiment)
    result = experiment.capture(isolated_definitions, ROOT)
    assert result["endpoints"] == [["bielġ"], ["hliehhan"]]
    assert result["live"]["EAFBrightening"] == [
        ["*b*æ*l*g*i"], ["*x*l*æ*x*x*j*a*n*ą"]]
    queries = result["queries"]
    assert queries["breaking"]["outputs"] == [
        ["*b*ea*l*g*i"], ["*x*l*ea*x*x*j*a*n*ą"]]
    assert queries["breaking_then_mutation"]["outputs"] == [
        ["*b*ie*l*g*i"], ["*x*l*ie*x*x*j*a*n*ą"]]
    assert queries["mutation"]["outputs"] == [
        ["*b*e*l*g*i"], ["*x*l*e*x*x*j*a*n*ą"]]
    assert queries["mutation_then_breaking"]["outputs"] == [
        ["*b*e*l*g*i"], ["*x*l*eo*x*x*j*a*n*ą"]]
    assert result["live"]["OEVelarFricativePalatalization"][1] == [
        "*x*l*ea*x*ç*j*a*n*ą"]
    assert queries["mutation_early:palatalization"]["outputs"][1] == [
        "*x*l*eo*x*ç*j*a*n*ą"]
    assert queries["breaking_late:palatalization"]["outputs"][1] == [
        "*x*l*æ*ç*ç*j*a*n*ą"]
    assert queries["mutation_early:second_operation"]["outputs"] == [
        ["*b*e*l*g*i"], ["*x*l*eo*x*x*j*a*n*ą"]]
    assert queries["breaking_late:second_operation"]["outputs"] == [
        ["*b*e*l*ʝ*i"], ["*x*l*e*ç*ç*j*ą*n"]]
    for variant, laugh in (("mutation_early", "*x*l*eo*x*ç*j*ą*n"),
                           ("breaking_late", "*x*l*e*ç*ç*j*ą*n")):
        for checkpoint in ("before_late_palatal", "late_palatal"):
            assert queries[variant + ":" + checkpoint]["outputs"] == [
                ["*b*e*l*ʝ*i"], [laugh]]
    assert queries["mutation_early:final"]["outputs"] == [["belġ"], ["hleohhan"]]
    assert queries["breaking_late:final"]["outputs"] == [["belġ"], ["hlehhan"]]
    assert result["cost"]["networks"] == 14
    assert result["cost"]["compiler_calls"] == 1
    assert result["cost"]["definition_preparation_calls"] == 0
    assert result["cost"]["image_loaded"] == bool(isolated_definitions)
    record_testsuite_property("sc044_west_saxon", json.dumps(result, ensure_ascii=False))

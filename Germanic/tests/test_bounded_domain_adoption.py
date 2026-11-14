"""Source-bound SC001 domain repair and SC092 late spelling projection."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from capr_runtime import check_build_manifest, layout, run_in_runner
from executable_facts import parse_defines
import oe_pipeline
from test_sc037_adjudication import (
    INTERVENTION_CHANGED, LEXICAL_GRAMMAR_CHANGED, assert_intervention_scope,
)

AUDIT = ROOT / "Germanic/docs/sound_changes/audits/bounded-domain-adoption"
BASE = "7e6023eda8a52df8916181aa98bbd935f331d069"


def frozen(name):
    with zipfile.ZipFile(AUDIT / "evidence.zip") as archive:
        return archive.read(name).decode()


def test_only_the_six_optional_groups_and_surviving_gamma_clause_are_reformulated():
    old = parse_defines(subprocess.check_output(
        ["git", "show", f"{BASE}:Germanic/fsts/germanic.txt"], cwd=ROOT, text=True))
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    for name in ("pgrmStrongPlainHeavy", "pgrmSimpleWord"):
        assert current[name].body == old[name].body.replace("(", "[").replace(")", "]")
    compact = lambda body: re.sub(r"\s+", "", body)
    assert compact(current["OldEnglishOrthography"].body) == (
        "[{*ɣ}->g," + compact(old["OldEnglishOrthography"].body)[1:])


def test_certificates_are_bound_to_the_archived_parser_closure_and_orthography():
    assert_intervention_scope()
    source = frozen("snapshot/candidate.txt")
    expected = parse_defines(source)
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    pending = ["EnglishProtoInput", "OldEnglishOrthography",
               "EnglishStarAlphabet", "EnglishPalatalConsonant"]
    visited = set()
    while pending:
        name = pending.pop()
        if name in visited:
            continue
        visited.add(name)
        # The shared guard pins the later native -anz extension exactly.
        if name not in INTERVENTION_CHANGED | LEXICAL_GRAMMAR_CHANGED:
            assert current[name].body == expected[name].body
        pending.extend(set(re.findall(r"\b[A-Za-z][A-Za-z0-9_]*\b", expected[name].body))
                       & expected.keys() - visited)
    compiler = json.loads(frozen("outputs/compiler.json"))
    assert compiler["candidate_sha256"] == hashlib.sha256(source.encode()).hexdigest()
    spec = importlib.util.spec_from_file_location(
        "bounded_parser_proof", AUDIT.parent / "parser-formal-resolution/functionality.py")
    proof = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(proof)
    for name in ("parser", "gamma-map"):
        proof.verify(frozen(f"outputs/{name}.att"), json.loads(frozen(f"proofs/{name}.proof.json")))
    assert json.loads(frozen("proofs/factorization-difference.proof.json"))["empty"]


def lookup(bin_name, words):
    result = run_in_runner(
        "flookup -i " + shlex.quote(bin_name), input="\n".join(words) + "\n",
        capture_output=True, text=True, check=True, timeout=120)
    found = {word: set() for word in words}
    for line in result.stdout.splitlines():
        if "\t" in line:
            word, value = line.split("\t", 1)
            if value != "+?":
                found[word].add(value)
    return {word: sorted(values) for word, values in found.items()}


@pytest.mark.runtime
def test_actual_canonical_parser_rejects_empty_roots_and_conserves_selected_analyses():
    assert check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], layout()) == []
    records = json.loads(frozen("outputs/selected391.json"))
    gate = oe_pipeline.stage_for("EnglishProtoInput").snapshot_bin
    expected = {row["fst_input"]: row["analysis"] for row in records}
    actual = lookup(gate, list(expected) + ["", "p", "s", "-"])
    assert {word: actual[word] for word in expected} == expected
    assert all(actual[word] == [] for word in ("", "p", "s", "-"))


@pytest.mark.runtime
def test_actual_surviving_gamma_projection_and_unchanged_selected_finals():
    records = json.loads(frozen("outputs/selected391.json"))
    expected = {row["fst_input"]: row["outputs"] for row in records}
    controls = json.loads(frozen("outputs/controls.json"))["full"]
    assert_intervention_scope()
    assert controls["é-ìwi"] == ["iī", "īi"]
    # This synthetic stress control changes under the separately pinned
    # marker/breaking intervention, not the unchanged gamma projection.
    current_controls = {**controls, "é-ìwi": ["eī"]}
    assert expected["spénnilō"] == ["spinl"]
    assert expected["fūliθō"] == ["fȳlþ"]
    # The unchanged historical inputs are counterfactuals after consolidation.
    assert expected["féxu"] == ["feoh"]
    assert expected["fláskōn"] == ["flasce"]
    assert expected["márōn"] == ["mare"]
    expected.update({
        "spénnilō": ["spinnelu"], "fūliθō": ["fȳleþu"], "féxu": ["feou"],
        "fláskōn": ["flæsċe"], "márōn": ["mære"],
    })
    actual = lookup("old_english.bin", list(dict.fromkeys([*expected, *controls])))
    assert {word: actual[word] for word in expected} == expected
    assert all(actual[word] == outputs for word, outputs in current_controls.items())

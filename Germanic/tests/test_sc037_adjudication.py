"""Source-bound light/heavy contrasts for compound linking-vowel syncope."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Germanic/docs/sound_changes/audits/sc037-experiments"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines
INTERVENTION_ADDED = {"EnglishIUmlautThroughU", "OEHighLinkSyncope"}
INTERVENTION_CHANGED = {
    "EnglishBreakingWContext", "EnglishProtoToOE", "OEBreakingI",
    "OECompoundLinkingSyncope", "OEIUmlautFronting", "OEStripSecondaryStress",
    "PGmcStarVowel", "pgrmCodaComplex", "pgrmCompoundFirst", "pgrmLinkingVowel",
}
CONSOLIDATION_ADDED = {
    "OEHighStressDecode", "OEMedLongShort", "HvS", "HvL", "HvV", "HvH", "HvI", "HvP",
}
CONSOLIDATION_CHANGED = {
    "EnglishProtoToOE", "OECompoundLinkingSyncope", "OEHighLinkSyncope",
    "OEMedialSyncope", "OELAdjacentSyncope", "OENonHighSyn", "OEHighVowelApocope",
    "OEWLossBeforeI",
}
LEXICAL_GRAMMAR_CHANGED = {"PGCellEnd"}


def assert_intervention_scope():
    accepted = subprocess.check_output(
        ["git", "show", "0129a313dbad7de55965e72ba8a0fefa69115636:Germanic/fsts/germanic.txt"],
        cwd=ROOT)
    assert hashlib.sha256(accepted).hexdigest() == (
        "49516473bdd7d078708680716f8da578a1503e391f6b5ed3f64643fb44fe1711")
    old = parse_defines(subprocess.check_output(
        ["git", "show", "439067680b0bcc4d80676b8ee882becafe67148f:Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True))
    tested = parse_defines(accepted.decode())
    assert tested.keys() - old.keys() == INTERVENTION_ADDED
    assert not old.keys() - tested.keys()
    assert {name for name in old if old[name].definition_raw != tested[name].definition_raw} == (
        INTERVENTION_CHANGED)
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    for name in (INTERVENTION_ADDED | INTERVENTION_CHANGED) - CONSOLIDATION_CHANGED:
        assert current[name].definition_raw == tested[name].definition_raw
    consolidated_base = parse_defines(subprocess.check_output(
        ["git", "show", "b58e7af59d5675fb2c01a2f5acc2b8b15148d2b6:Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True))
    assert current.keys() - consolidated_base.keys() == CONSOLIDATION_ADDED
    assert not consolidated_base.keys() - current.keys()
    assert {name for name in consolidated_base
            if "".join(current[name].body.split()) !=
               "".join(consolidated_base[name].body.split())} == (
                   CONSOLIDATION_CHANGED | LEXICAL_GRAMMAR_CHANGED)
    corrected = parse_defines(subprocess.check_output(
        ["git", "show", "3e2fe1b6d8ac606e854534798bb6688805c3875e:Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True))
    for name in CONSOLIDATION_ADDED | CONSOLIDATION_CHANGED:
        assert current[name].body == corrected[name].body
    lexical = parse_defines(subprocess.check_output(
        ["git", "show", "e16ac243382280b0c7ffc50335d6cc1f28051b3e:Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True))
    assert "".join(lexical["PGCellEnd"].body.split()) == (
        "".join(corrected["PGCellEnd"].body.split()).replace(
            "a:{*a}s:{*s}|", "a:{*a}s:{*s}|a:{*a}n:{*n}z:{*z}|"))
    assert current["PGCellEnd"].body == lexical["PGCellEnd"].body


def test_intervention_changes_are_exactly_source_bound():
    assert_intervention_scope()


def evidence():
    return json.loads((AUDIT / "evidence.json").read_text())


def test_archived_restriction_and_preconsolidation_a_kernel_are_immutable():
    report = evidence()
    manifest = json.loads((AUDIT / "manifest.json").read_text())
    assert hashlib.sha256((AUDIT / "experiments.zip").read_bytes()).hexdigest() == manifest["archive"]
    with zipfile.ZipFile(AUDIT / "experiments.zip") as archive:
        name = next(name for name in archive.namelist()
                    if name.endswith("sc037-compound-conditioning-04/snapshot/candidate.txt"))
        candidate = archive.read(name)
    assert hashlib.sha256(candidate).hexdigest() == report["candidate_sha256"]
    old = subprocess.check_output(
        ["git", "show", manifest["base_commit"] + ":Germanic/fsts/germanic.txt"], cwd=ROOT)
    assert hashlib.sha256(old).hexdigest() == report["source_sha256"]
    before, tested = parse_defines(old.decode()), parse_defines(candidate.decode())
    assert before.keys() == tested.keys()
    assert {name for name in before if before[name].body != tested[name].body} == {
        "OECompoundLinkingSyncope"}
    current = parse_defines(subprocess.check_output(
        ["git", "show", "b58e7af59d5675fb2c01a2f5acc2b8b15148d2b6:Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True))
    archived_a = tested["OECompoundLinkingSyncope"].body.split("] .o. [", 1)[0] + "])"
    assert "".join(current["OECompoundLinkingSyncope"].body.split()) == (
        "".join(archived_a.split()))


def test_light_high_linkers_survive_while_heavy_high_linkers_and_short_a_syncopate():
    controls = {row["id"]: row for row in evidence()["controls"]}
    for name in ("light-i", "light-u"):
        row = controls[name]
        assert row["actual"] == [row["input"]]
        assert row["previous"] != row["actual"]
    for name in ("short-a", "heavy-i", "heavy-u", "long-i"):
        row = controls[name]
        assert row["actual"] == [row["expected"]] == row["previous"]
        assert row["actual"] != [row["input"]]
    row = controls["no-secondary"]
    assert row["actual"] == [row["input"]] == row["previous"]


def test_selected_derivations_and_native_component_functionality_are_preserved():
    report = evidence()
    assert (report["selected_count"], report["selected_rule_changes"],
            report["selected_final_changes"]) == (391, 0, 0)
    assert [(row["row_id"], row["concept"]) for row in report["firings"]] == [
        ("2148", "rainbow"), ("2336", "earthly")]
    assert all(row["before"] != row["after"] for row in report["firings"])
    assert all(result["stdout"].strip() == "1 (1 = TRUE, 0 = FALSE)"
               and not result["stderr"] for result in report["functionality"].values())
    assert hashlib.sha256((AUDIT / "evidence.json").read_bytes()).hexdigest() == (
        json.loads((AUDIT / "manifest.json").read_text())["evidence"])

"""SC036's historical distinctions and observed executable behavior."""
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
ASSAY = ROOT / "Germanic/docs/sound_changes/audits/sc036-experiments"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudicate
import oe_pipeline
from check_bibliography_sanity import parse_entries


def receipt():
    return json.loads((ASSAY / "evidence.json").read_text())


def git_bytes(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def test_receipt_identifies_its_actual_source_and_overlapping_populations():
    evidence = receipt()
    source = git_bytes(evidence["base_commit"], "Germanic/fsts/germanic.txt")
    assert hashlib.sha256(source).hexdigest() == evidence["source_sha256"]
    assert evidence["selected_rows"] == 389
    assert evidence["legacy380_identities"] == 380
    assert evidence["canonical_composed_incremental_agree"]
    assert evidence["protected_files_unchanged"] >= 160
    firings = evidence["models"]["existing"]["firings"]
    assert [(r["row_id"], r["concept"]) for r in firings] == [
        ("2201", "soul"), ("2302", "world")]
    assert all(row["legacy380_identity"] for row in firings)


def test_only_sc036_and_its_explicit_branches_changed():
    source = (ROOT / "Germanic/fsts/germanic.txt").read_text()
    base = git_bytes(receipt()["base_commit"], "Germanic/fsts/germanic.txt").decode()

    def definitions(text):
        return {name: re.sub(r"\s+", "", body) for name, body in
                oe_pipeline._define_bodies(oe_pipeline._strip_comments(text)).items()}

    current, old = definitions(source), definitions(base)
    # The input-gate extension (audits/lexical-witnesses-2335-2336,
    # commit 7d79e179) is adjudicated separately and pinned exactly by
    # test_lexical_witness_input_gate.py; relative to SC036's base it
    # adds pgrmInputTailVowel and rewires the two gate defines below.
    gate_added = {"pgrmInputTailVowel"}
    gate_changed = {"pgrmSimpleWord", "pgrmCompoundSecond"}
    assert current.keys() - old.keys() == (
        {"OELHWeakRaising", "OESoulProxy"} | gate_added)
    assert old.keys() <= current.keys()
    assert {name for name in old if old[name] != current[name]} == (
        {"OEInterStressRaising", "EnglishProtoToOE"} | gate_changed)
    assert current["OEInterStressRaising"] == (
        "[OELHWeakRaising.o.OESoulProxy]")


def test_single_comma_shares_context_including_the_grave_mapping():
    evidence = receipt()
    assert evidence["formal_equivalence_to_original"] == {
        "OEInterStressRaising": True, "AFR": True, "AFRV": False}
    original = evidence["component_results"]["OEInterStressRaising"]
    assert original == evidence["component_results"]["AFR"]
    for name in (
        "grave-without-u", "grave-before-front-vowel", "grave-word-initial",
        "primary-a", "no-left-nucleus", "no-right-consonant", "long-target",
        "j-immediately-before-u", "j-earlier-in-right-cluster",
        "following-i", "following-o", "atomic-diphthong-left",
        "retained-secondary-no-u",
    ):
        assert original[name] == evidence["probe_inputs"][name]
    assert original["soul-live"] == "*s*ā*w*u*l*u"
    assert original["world-live"] == "*w*é*r*u*l*d*u"
    assert original["j-in-left-cluster"] == "*w*é*j*u*l*d*u"
    assert (evidence["component_results"]["AFB"]["grave-without-u"] ==
            "*w*é*r*u*l*d*a")


def test_independent_clause_and_displacement_failures_are_not_adopted_outputs():
    models = receipt()["models"]
    assert models["existing"]["final_differences"] == []
    assert models["restricted-unified"]["final_differences"] == []
    assert models["restricted-vocalic"]["final_differences"] == []
    assert models["after-SC037"]["final_differences"] == []
    assert models["after-SC038"]["final_differences"] == []
    assert [(r["concept"], r["candidate"]) for r in
            models["A-only"]["final_differences"]] == [("world", "wereald")]
    assert [(r["concept"], r["candidate"]) for r in
            models["B-only"]["final_differences"]] == [("soul", "sāwel")]
    assert [(r["concept"], r["candidate"]) for r in
            models["after-SC040"]["final_differences"]] == [
                ("soul", "sāwel"), ("world", "wereald")]
    assert models["vocalic-before-SC004"]["final_differences"] == []
    assert [(r["concept"], r["candidate"]) for r in
            models["vocalic-before-SC019"]["final_differences"]] == [
                ("soul", "sāwel")]
    assert models["vocalic-SC019-before-early-SC036"]["final_differences"] == []


def test_secondary_marker_bleeding_is_not_historical_chronology():
    evidence = receipt()
    interaction = evidence["interactions"][
        "OEInterStressRaising:OECompoundLinkingSyncope"]["linking-before-grave-a"]
    assert interaction["forward"] == "*w*é*r*a*t*u*l*d*u"
    assert interaction["reverse"] == "*w*é*r*t*u*l*d*u"
    assert evidence["interactions"]["OEInterStressRaising:OEStripSecondaryStress"] == {}
    edges = adjudicate.read_tsv(
        ROOT / "Germanic/docs/sound_changes/registry/chronology_edges.tsv")
    current = {row["target_change_id"]: row for row in edges
               if row["source_change_id"] == "SC036"}
    assert set(current) == {"SC004", "SC019", "SC040", "SC038", "SC107", "SC059"}
    assert all(row["evidence_basis"] == "technical" for row in current.values())
    assert all(row["relation_type"] == "technical_computational"
               for row in current.values())


def test_current_authority_and_source_access_qualifications():
    row = adjudicate.load_registry_row("SC036")
    assert row["verdict"] == "REFORMULATE/REORDER"
    assert row["confidence"] == "C"
    assert (row["hist_stage"], row["hist_scope"]) == ("oe", "english_specific")
    assert adjudicate.check_memo("SC036", row=row) == []
    with (ASSAY / "source-evidence.tsv").open() as handle:
        claims = list(csv.DictReader(handle, delimiter="\t"))
    assert len({r["claim_id"] for r in claims}) == len(claims)
    assert all(None not in r and all(r.values()) for r in claims)
    by_id = {r["claim_id"]: r for r in claims}
    assert by_id["RT330"]["verification"] == "original_page_checked"
    assert by_id["BU366"]["verification"] == "retained_text_only"
    entries = {entry.key for entry in parse_entries((ROOT / "docs/refs.bib").read_text())}
    assert {r["source"] for r in claims if r["claim_id"] != "FORMAL"} <= entries


def test_staged_receipt_remains_historical_not_a_current_production_replay():
    staged = json.loads((ASSAY / "staged-evidence.json").read_text())
    rejected = staged["staged_alternatives"]["world-unshifted-i-stem-comparison"]
    assert rejected["status"] == "rejected"
    assert rejected["rejection"]["stage"] == "OEMedUnstressedILowering"
    assert staged["staged_alternatives"]["world-without-grave"]["final"] == "weorold"
    # Current production is verified separately by the inherited-migration assay.
    for name in ("evidence.json", "staged-evidence.json"):
        path = (ASSAY / name).relative_to(ROOT)
        assert (ROOT / path).read_bytes() == git_bytes(
            "5665e3038dab311a4803e64b0f517b03b4806b4d", path)

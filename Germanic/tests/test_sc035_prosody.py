"""Regular raising, positive prosody, foot-initial PD and source provenance."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
SC = ROOT / "Germanic/docs/sound_changes"
ASSAY = SC / "audits/sc035-prosody"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import oe_pipeline
import adjudicate
from capr_runtime import run_in_runner
from check_bibliography_sanity import parse_entries
from historical_sc035 import historical_runtime


def receipt():
    return json.loads((ASSAY / "evidence.json").read_text())


def test_frozen_comparison_preserves_both_populations_and_explicit_stage_changes():
    data = receipt()
    assert (data["selected_rows"], data["legacy380_identity_rows"],
            data["stages_compared"]) == (389, 380, 108)
    source = subprocess.check_output(
        ["git", "show", data["accepted_base_commit"] + ":Germanic/fsts/germanic.txt"], cwd=ROOT)
    assert hashlib.sha256(source).hexdigest() == data["source_sha256"]
    assert data["canonical_artifacts_unchanged"]
    for model, result in data["models"].items():
        assert result["final_differences"] == []
        changed = {row["row_id"] for stage in result["all_intermediate_differences"]
                   for row in stage["rows"]}
        assert changed == (set() if model == "A" else {"1943", "1944"})
        assert all(row["legacy380_identity"] for stage in result["all_intermediate_differences"]
                   for row in stage["rows"])


def test_source_backed_foot_and_cluster_controls_distinguish_the_models():
    models = receipt()["models"]
    assert models["A"]["full_input_climb"] == [["ġiestīgan"]]
    assert models["A"]["staged_control_finals"]["prefixed-shaft"] == ["ġeasċeft"]
    for name in ("B", "C"):
        model = models[name]
        assert model["full_input_climb"] == [["ġestīgan"]]
        assert model["staged_control_finals"]["prefixed-shaft"] == ["ġesċeaft"]
        assert model["staged_control_finals"]["shaft"] == ["sċeaft"]
        assert model["staged_control_finals"]["climb-stress-erased"] == ["ġiestegan"]
        assert model["positive_stress_annotation"]["outputs"][-3:] == [
            ["*g*a*t*ā"], ["*ᶠ*b*a*t*á"], ["*ᶠ*ʝ*æ*t*á"]]


def test_raising_and_later_lowering_are_separate_from_ae_merger():
    models = receipt()["models"]
    def after(model, stage):
        return next(item["after"] for item in models[model]["focal_traces"]["1944"]
                    if item["stage"] == stage)
    assert after("B", "OEVelarPalatalization")[0].startswith("*ᶠ*ʝ*æ*l")
    assert after("C", "OEVelarPalatalization")[0].startswith("*ᶠ*ʝ*i*l")
    assert after("C", "OEUnstressedAEMerger")[0].startswith("*ᶠ*ʝ*i*l")
    assert after("C", "OEPrefixIReduction")[0].startswith("*ʝ*e*l")


def test_context_lifting_preserves_the_other_segmental_rule_kernels():
    old = subprocess.check_output(
        ["git", "show", receipt()["accepted_base_commit"] + ":Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True)
    previous = oe_pipeline._define_bodies(oe_pipeline._strip_comments(old))
    current = oe_pipeline._define_bodies(oe_pipeline._strip_comments(
        (ROOT / "Germanic/fsts/germanic.txt").read_text()))
    changed = set()
    for stage in oe_pipeline.named_stages():
        name = stage.foma_identifier
        if name not in previous:
            assert name == "OEStressFootContext"
            continue
        body = current[name]
        if body.startswith(("Ctx(", "FootCtx(")) and not previous[name].startswith(("Ctx(", "FootCtx(")):
            body = body[body.index("(") + 1:-1]
        if re.sub(r"\s+", "", body) != re.sub(r"\s+", "", previous[name]):
            changed.add(name)
    # The separate rainbow test pins the exact subordinate-root extension;
    # the SC066 reformulation is pinned by test_sc066_sc068_adjudication.py.
    assert changed == {"OEPrefixAReduction", "OEUnstressedAEMerger",
                       "OEPrefixIReduction", "OEInterStressRaising",
                       "PNWGmcULowering", "OELAdjacentSyncope"}
    assert current["OEWsPalatalDiphthongization"].startswith("FootCtx(")


def test_reader_prints_adopted_definitions_and_all_material_scholarship():
    source = oe_pipeline._define_bodies(oe_pipeline._strip_comments(
        (ROOT / "Germanic/fsts/germanic.txt").read_text()))
    for identifier, filename in (
        ("OEPrefixAReduction", "035-pretonic-front-vowel-raising.md"),
        ("OEWsPalatalDiphthongization", "056-west-saxon-palatal-diphthongization.md"),
        ("OEUnstressedAEMerger", "073-unstressed-ae-merger.md"),
        ("OEPrefixIReduction", "076-prefix-i-reduction.md"),
    ):
        reader = (SC / "reader_facing" / filename).read_text()
        body = oe_pipeline._define_bodies(oe_pipeline._strip_comments(reader))[identifier]
        assert re.sub(r"\s+", "", body) == re.sub(r"\s+", "", source[identifier])
    reader = (SC / "reader_facing/035-pretonic-front-vowel-raising.md").read_text()
    for key in ("HoggGrammar1992", "MinkovaZhou2022", "RieggerBogelWalkden2024", "Berg2014"):
        assert "@" + key + "," in reader
    for sc in ("SC035", "SC056", "SC073", "SC076"):
        assert adjudicate.check_memo(sc) == []


def test_context_checkpoint_is_registered_without_inventing_a_historical_law():
    from generate_registry_views import read_tsv
    row = next(row for row in read_tsv(SC / "registry/sc_registry.tsv")
               if row["fst_identifier"] == "OEStressFootContext")
    assert row["sc_id"] == "SC113"
    assert row["entry_type"] == "support_stage"
    for field in ("hist_stage", "hist_scope", "confidence", "verdict"):
        assert row[field] == ""
    assert row["include_in_volume"] == row["is_reader_facing"] == "no"


def test_verified_bibliographic_metadata_and_traceable_acquisition():
    entries = parse_entries((ROOT / "docs/refs.bib").read_text())
    expected = {
        "MinkovaZhou2022": ("Zhou, Z. L.", "533--558", "10.1017/S1360674322000144"),
        "RieggerBogelWalkden2024": ('B{\\\"o}gel, Tina', "2065--2069", "10.21437/Interspeech.2024-289"),
        "Berg2014": ("Berg, Joakim P.", "2014", "10852/39907"),
    }
    index = (ROOT / "Germanic/docs/REFERENCES.md").read_text()
    acquisitions = (ROOT / "docs/references/README_resources.md").read_text()
    for key, facts in expected.items():
        matches = [entry for entry in entries if entry.key == key]
        assert len(matches) == 1
        for fact in facts:
            assert fact in matches[0].body
        assert key in index and key in acquisitions
    holdings = {
        "minkova_zhou_2022_functional_stress_shifts": (
            26, "4f93aa967f531772a57629690c10e317f6dc155a95c0edf8c3a7f5cedfcd6b34"),
        "riegger_bogel_walkden_2024_prosody_ge": (
            5, "ce258d6cb4f5012b92bd98a42786f884717dfdf5030c1dc6299b7eca2ad62107"),
        "berg_2014_old_english_unstressed_vowels": (
            104, "9c5d105f8e3373ad2205e7edc3fa10de62e6e54a956e151bd08380880a8a0d77"),
    }
    for stem, (sheets, digest) in holdings.items():
        holding = ROOT / "docs/references" / stem
        assert hashlib.sha256(holding.with_suffix(".pdf").read_bytes()).hexdigest() == digest
        text = holding.with_suffix(".txt").read_text()
        assert digest in text
        assert len(re.findall(r"=== PDF sheet \d+ ===", text)) == sheets
    assert "HoggGrammar1992" in acquisitions and "§5.48" in acquisitions


@pytest.mark.runtime
@pytest.mark.historical_replay
def test_fresh_commit_pinned_comparison_reproduces_the_entire_receipt():
    expected = receipt()
    with historical_runtime(expected["accepted_base_commit"]) as execute:
        result = execute("python3 docs/sound_changes/audits/sc035-prosody/experiment.py")
    assert json.loads(result.stdout) == expected


@pytest.mark.runtime
def test_fresh_adopted_cascade_and_phonological_components():
    result = run_in_runner(
        "python3 docs/sound_changes/audits/sc035-prosody/verify.py",
        text=True, capture_output=True, check=True, timeout=1800)
    data = json.loads(result.stdout)
    # 390 selected rows after the SC065 filth admission (row 2335).
    assert data["selected_rows"] == 390
    assert data["canonical_and_isolated_agree"] and data["composed_and_incremental_agree"]
    assert data["full_input_climb"] == [["ġestīgan"]]
    assert data["staged_control_finals"] == receipt()["models"]["C"]["staged_control_finals"]
    controls = data["controls"]
    assert controls["raising"]["outputs"] == [
        ["*ᶠ*ʝ*i*t*á"], ["*ᶠ*b*æ*t*á"], ["*ᶠ*ʝ*e*t*á"],
        ["*ʝ*æ*t"], ["*ᶠ*ʝ*i*ʃ*æ*f*t"]]
    assert controls["diphthongization"]["outputs"] == [
        ["*ᶠ*ʝ*æ*ʃ*ea*f*t"], ["*ʃ*ea*f*t"], ["*ʝ*ea*s*t*i"],
        ["*ʝ*íe*β*a*n"], ["*ʃ*īe*p"], ["*ʝ*ea*l*l*a"]]
    assert controls["ae_merger"]["outputs"] == [
        ["*ᶠ*b*e*t*á"], ["*b*æ*t"], ["*ᶠ*ʝ*i*s*t*ḯ*g*a"]]
    assert controls["i_lowering"]["outputs"] == [
        ["*ʝ*e*s*t*ḯ*g*a"], ["*b*e*g*í*n*n*a*n"], ["*n*e*t*á"],
        ["*b*í*n*d*a*n"], ["*n*i"]]

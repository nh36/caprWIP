"""World's source-critical conclusions and complete-cascade diagnostics."""
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
ASSAY = ROOT / "Germanic/docs/sound_changes/audits/world-2302-experiments"
BASE = "6b2baf5f88af8a3c7702628bb3376c53c466e2a6"
FOLLOWUP_BASE = "61a0d67ef02a8da681ab21fba741b0ad63ea0a95"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudicate
from capr_runtime import run_in_runner
from check_bibliography_sanity import parse_entries


def receipt():
    return json.loads((ASSAY / "evidence.json").read_text())


def base_bytes(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)


def read_tsv(text):
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def test_scientific_sources_and_archives_are_preserved():
    paths = [
        "Germanic/fsts/germanic.txt",
        "Germanic/fsts/old_english_sandbox.txt",
        "Germanic/docs/sound_changes/registry/sc_registry.tsv",
        "Germanic/docs/sound_changes/registry/chronology_edges.tsv",
        "Germanic/data/entry_context_metadata.tsv",
    ]
    for directory in (
        "Germanic/docs/sound_changes/cascade_baseline",
        "Germanic/docs/sound_changes/audits/sc036-experiments",
    ):
        paths.extend(subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", BASE, directory],
            cwd=ROOT, text=True).splitlines())
    for path in paths:
        if path.endswith("/oe_equivalence_report.json"):
            continue
        assert (ROOT / path).read_bytes() == base_bytes(path), path
    equivalent = json.loads((ROOT /
        "Germanic/docs/sound_changes/cascade_baseline/oe_equivalence_report.json").read_text())
    assert equivalent["status"] == "equivalent"
    assert equivalent["rows_compared"] == 389


def test_only_editorial_row_fields_changed():
    for path, allowed in (
        ("Germanic/data/germanic-aligned-final.tsv", {"NOTE"}),
        ("Germanic/data/entry_stage_metadata.tsv", {"evidence"}),
    ):
        old = read_tsv(base_bytes(path).decode())
        new = read_tsv((ROOT / path).read_text())
        assert len(old) == len(new)
        differences = []
        for before, after in zip(old, new):
            changed = {key for key in before if before[key] != after[key]}
            if changed:
                assert changed == allowed
                assert before.get("ID", before.get("row_id")) == "2302"
                differences.append(changed)
        assert len(differences) == 1


def test_full_start_candidates_do_not_reuse_staged_rejection():
    evidence = receipt()
    assert evidence["base_commit"] == BASE
    assert evidence["selected_rows"] == 389
    assert evidence["legacy380_identities"] == 380
    assert evidence["protected_files_unchanged"] >= 169
    assert evidence["identity_composed_incremental_snapshots_agree"]
    assert evidence["source_sha256"] == hashlib.sha256(
        base_bytes("Germanic/fsts/germanic.txt")).hexdigest()
    identity = evidence["models"]["identity"]
    assert [(r["row_id"], r["concept"]) for r in identity["firings"]] == [
        ("2201", "soul"), ("2302", "world")]
    candidates = identity["full_cascade_candidates"]
    assert len({r["input"] for r in candidates}) == 12
    for row in candidates:
        assert row["status"] == "accepted"
        assert row["trace"][0]["stage"] == "EnglishProtoInput"
        if row["input"].endswith("ldiz"):
            assert row["final"] == "wereald"
            assert "PWGmcEarlyIApocope" in {t["stage"] for t in row["trace"]}
            assert "OEInterStressRaising" not in {t["stage"] for t in row["trace"]}
        elif "ra-à" in row["input"]:
            assert row["final"] == "weorauld"
            assert "OECompoundLinkingSyncope" not in {t["stage"] for t in row["trace"]}
        else:
            assert row["final"] == "weorold"
            assert ("PNWGmcFinalLongORaising" in {t["stage"] for t in row["trace"]}) == (
                row["input"].endswith("ō"))


def test_positive_negative_and_hiatus_contexts():
    evidence = receipt()
    inputs = evidence["component_inputs"]
    raising = evidence["component_results"]["OEInterStressRaising"]
    assert raising["ordinary-positive"] == "*w*é*r*u*l*d*u"
    for name in ("right-j", "following-i", "primary-before-l",
                 "plain-before-l-without-u", "grave-before-l-without-u"):
        assert raising[name] == inputs[name]
    syncope = evidence["component_results"]["OECompoundLinkingSyncope"]
    assert syncope["literal-vowel-hiatus"] == inputs["literal-vowel-hiatus"]
    assert syncope["consonantal-linking-control"] == "*w*é*r*t*à*l*d*u"
    wide = evidence["component_results"]["WWide"]
    assert wide["plain-before-l-without-u"] == "*w*é*r*o*l*d*a"
    assert wide["primary-before-l"] == inputs["primary-before-l"]


def test_model_deltas_and_marker_dependency_are_not_adopted():
    models = receipt()["models"]
    for name in ("identity", "strip-after-SC037-before-raising",
                 "factored-rounding-then-raising"):
        assert models[name]["final_differences"] == []
    for name in ("strip-after-input", "strip-before-SC036"):
        assert [(r["row_id"], r["existing"], r["candidate"]) for r in
                models[name]["final_differences"]] == [
                    ("2148", "reġnboga", "reġnofuga")]
    for name in ("rounding-only-same-context", "wide-before-l-diagnostic"):
        assert [(r["row_id"], r["candidate"]) for r in
                models[name]["final_differences"]] == [
                    ("2201", "sāwal"), ("2302", "weorald")]
    assert all(r["legacy380_identity"] for m in models.values()
               for r in m["final_differences"])
    row = adjudicate.load_registry_row("SC036")
    assert (row["verdict"], row["confidence"]) == ("REFORMULATE", "C")


def test_paradigm_rejections_are_explicit_input_coverage_gaps():
    comparisons = receipt()["models"]["identity"]["paradigm_comparisons"]
    assert len(comparisons) == 6
    for name in ("i-stem-long-i-dative-comparison",
                 "i-stem-genitive-comparison",
                 "o-stem-genitive-trimoric-comparison"):
        row = comparisons[name]
        assert row["status"] == "rejected"
        assert row["final"] is None
        assert row["rejection"]["stage"] == "EnglishProtoInput"
    assert comparisons["i-stem-short-i-comparison"]["final"] == "wereald"
    for name in ("o-stem-accusative-comparison",
                 "o-stem-genitive-bimoric-comparison"):
        assert comparisons[name]["final"] == "werealde"


def test_source_evidence_keys_mappings_and_verification_limits():
    claims = read_tsv((ASSAY / "source-evidence.tsv").read_text())
    assert len({r["claim_id"] for r in claims}) == len(claims)
    assert all(None not in r and all(r.values()) for r in claims)
    by_id = {r["claim_id"]: r for r in claims}
    assert by_id["CA244"]["verification"] == "original_page_checked"
    assert by_id["GO2023"]["verification"] == "full_text_read_reflow_images_checked"
    entries = {e.key for e in parse_entries((ROOT / "docs/refs.bib").read_text())}
    assert {r["source"] for r in claims if r["source"] != "CAPR"} <= entries
    intake = ROOT / "docs/references/world_2026-10-26"
    holdings = read_tsv((intake / "holdings.tsv").read_text())
    assert {r["citation_key"] for r in holdings} == {
        "Fulk2010", "Fulk2022", "Britton1996", "Hogg1996",
        "Minkova1996", "Goering2023", "Cermak2005", "Sauer1992"}
    maps = read_tsv((intake / "page_map.tsv").read_text())
    assert {r["printed_page_or_range"] for r in maps
            if r["citation_key"] == "Fulk2010"} == {str(p) for p in range(126, 145)}
    assert {r["printed_page_or_range"] for r in maps
            if r["citation_key"] == "Hogg1996"} == {str(p) for p in range(3, 13)}
    for key, sheet, printed in (
        ("Cermak2005", "1", "unnumbered (blank)"),
        ("Cermak2005", "6", "39"),
        ("Cermak2005", "12", "45"),
        ("Sauer1992", "5", "V"),
        ("Sauer1992", "28", "XXVIII"),
        ("Sauer1992", "29", "1"),
        ("Sauer1992", "118", "90"),
        ("Sauer1992", "384", "356"),
    ):
        assert [r["printed_page_or_range"] for r in maps
                if r["citation_key"] == key and r["pdf_sheet"] == sheet] == [printed]


def reassessment():
    return json.loads((ASSAY / "reassessment.json").read_text())


def inherited_candidate(model):
    return next(row for row in model["full_cascade_candidates"]
                if row["input"] == "*wír-àldiz")


def test_followup_preserves_production_and_prior_receipts():
    paths = [
        "Germanic/data/germanic-aligned-final.tsv",
        "Germanic/data/entry_stage_metadata.tsv",
        "Germanic/data/entry_context_metadata.tsv",
        "Germanic/docs/sound_changes/audits/world-2302-closeout.md",
        "Germanic/docs/sound_changes/audits/world-2302-experiments/evidence.json",
    ]
    for path in paths:
        old = subprocess.check_output(
            ["git", "show", f"{FOLLOWUP_BASE}:{path}"], cwd=ROOT)
        assert (ROOT / path).read_bytes() == old, path
    evidence = reassessment()
    assert evidence["base_commit"] == FOLLOWUP_BASE
    assert evidence["selected_rows"] == 389
    assert evidence["legacy380_identities"] == 380
    assert evidence["protected_files_unchanged"] >= 172
    assert evidence["identity_incremental_all_snapshots_agree"]
    assert evidence["prior_receipt_sha256"] == hashlib.sha256(
        (ASSAY / "evidence.json").read_bytes()).hexdigest()
    assert evidence["corpus_sha256"] == hashlib.sha256(
        (ROOT / paths[0]).read_bytes()).hexdigest()
    assert set(evidence["families"]) == set("ABCDEF")
    assert len(evidence["component_inputs"]) == 23
    for model in evidence["models"].values():
        assert len(model["full_cascade_candidates"]) == 18
        assert len(model["paradigm_comparisons"]) == 6
        for raw in ("*wír-aldį", "*wír-àldį"):
            candidate = next(r for r in model["full_cascade_candidates"]
                             if r["input"] == raw)
            assert candidate["status"] == "rejected"
            assert candidate["rejection"]["stage"] == "EnglishProtoInput"
    reader_path = "Germanic/docs/sound_changes/reader_facing/036-inter-stress-raising.md"
    reader = (ROOT / reader_path).read_text()
    before = subprocess.check_output(
        ["git", "show", f"{FOLLOWUP_BASE}:{reader_path}"], cwd=ROOT, text=True)
    assert reader.split("### The distinct history of soul", 1)[1] == (
        before.split("### The distinct history of soul", 1)[1])


def test_inherited_success_is_not_evidence_for_necessary_analogy():
    models = reassessment()["models"]
    identity = inherited_candidate(models["identity"])
    assert identity["status"] == "accepted"
    assert identity["final"] == "wereald"
    for name in ("C-early-high", "C-postfront-high", "C-supplement-high",
                 "D-rounded-then-high", "D-high-u-only-back"):
        row = inherited_candidate(models[name])
        assert row["final"] == "weorold"
        stages = {step["stage"]: step for step in row["trace"]}
        assert stages["PWGmcEarlyIApocope"]["post"] == "*w*í*r*à*l*d*z"
        assert "OEInterStressRaising" not in stages
        assert "OEBreaking" not in stages
        back = "WBackU" if name == "D-high-u-only-back" else "OEBackMutation"
        assert stages[back]["post"] == "*w*éo*r*u*l*d"
    trace = inherited_candidate(models["C-postfront-high"])["trace"]
    stages = {row["stage"]: row for row in trace}
    assert stages["EAFBrighteningUnstressed"]["post"] == "*w*é*r*æ*l*d"
    assert stages["WToU"]["pre"] == "*w*é*r*æ*l*d"
    assert stages["WToU"]["post"] == "*w*é*r*u*l*d"
    assert inherited_candidate(models["C-after-breaking"])["final"] == "wereald"
    assert models["C-supplement-high"]["final_differences"] == []


def test_rounded_failure_is_later_lowering_not_an_impossible_o_stage():
    models = reassessment()["models"]
    rounded = inherited_candidate(models["D-rounded-only"])
    assert rounded["final"] == "weorald"
    steps = {row["stage"]: row for row in rounded["trace"]}
    assert steps["WToO"]["post"] == "*w*é*r*o*l*d"
    assert steps["OEBackMutation"]["post"] == "*w*éo*r*o*l*d"
    assert steps["OEFinalUnstressedOLowering"]["post"] == "*w*éo*r*a*l*d"
    assert inherited_candidate(models["D-no-final-lowering"])["final"] == "weorold"
    assert inherited_candidate(models["D-rounded-u-only-back"])["final"] == "werald"
    assert inherited_candidate(models["D-high-before-u-only"])["final"] == "weorald"
    assert inherited_candidate(models["D-existing-raising-earlier"])["final"] == "weorald"


def test_back_mutation_shared_contexts_are_measured_not_silently_corrected():
    evidence = reassessment()
    controls = evidence["component_results"]
    inputs = evidence["component_inputs"]
    for probe, expected in (
        ("back-mutation-with-o", "*w*éo*r*o*l*d"),
        ("back-mutation-plain-e-o", "*w*eo*r*o*l*d"),
        ("back-mutation-with-a", "*w*éo*r*a*l*d"),
    ):
        assert controls["OEBackMutation"][probe] == expected
        assert controls["WBackU"][probe] == inputs[probe]
    for component in ("OEBackMutation", "WBackU"):
        assert controls[component]["back-mutation-with-u"] == "*w*éo*r*u*l*d"
        assert controls[component]["back-mutation-fronted-a-o"] == "*w*ea*r*o*l*d"
        probe = "back-mutation-dental-control"
        assert controls[component][probe] == inputs[probe]
    assert evidence["models"]["back-u-only-control"]["final_differences"] == []


def test_broader_candidate_has_controls_but_no_proven_prosodic_domain():
    evidence = reassessment()
    controls = evidence["component_results"]
    inputs = evidence["component_inputs"]
    for probe in ("right-j", "primary-before-l", "strong-accent-before-l",
                  "primary-fronted-before-l", "weak-l-without-cluster",
                  "toward-shaped-weak"):
        assert controls["WToU"][probe] == inputs[probe]
    assert controls["WToU"]["weak-noncompound-shaped"] == "*s*é*t*u*l*d"
    for probe in ("twofold-shaped-weak", "twofold-shaped-grave"):
        assert controls["WToU"][probe] == "*t*w*í*f*u*l*d"
    assert controls["OEInterStressRaising"]["fronted-world-final"] == (
        inputs["fronted-world-final"])
    assert controls["WToU"]["fronted-world-final"] == "*w*é*r*u*l*d"
    assert controls["OECompoundLinkingSyncope"]["literal-vowel-hiatus"] == (
        inputs["literal-vowel-hiatus"])


@pytest.mark.parametrize("name,expected", [
    ("identity", []),
    ("C-early-high", [("2201", "sāwel")]),
    ("C-postfront-high", [("2201", "sāwel")]),
    ("C-supplement-high", []),
    ("C-after-breaking", [("2201", "sāwel"), ("2302", "wereald")]),
    ("D-rounded-only", [("2201", "sāwel"), ("2302", "weorald")]),
    ("D-rounded-then-high", [("2201", "sāwel")]),
    ("D-high-before-u-only", [("2201", "sāwel")]),
    ("D-existing-raising-earlier", [("2201", "sāwel"), ("2327", "wundode")]),
    ("D-no-final-lowering", [
        ("2127", "mōnoþ"), ("2201", "sāwel"), ("2310", "macoþ"),
        ("2312", "boroþ"), ("2314", "leornoþ"), ("2316", "liccoþ"),
        ("2318", "sċēawoþ")]),
    ("back-u-only-control", []),
    ("D-rounded-u-only-back", [("2201", "sāwel"), ("2302", "werald")]),
    ("D-high-u-only-back", [("2201", "sāwel")]),
    ("F-global-strip-control", [("2148", "reġnofuga")]),
])
def test_every_reassessment_selected_final_delta_is_explicit(name, expected):
    models = reassessment()["models"]
    differences = models[name]["final_differences"]
    assert [(row["row_id"], row["candidate"]) for row in differences] == expected
    assert all(row["legacy380_identity"] == (row["row_id"] != "2327")
               for row in differences)
    assert all(stage["stage"] in models[name]["order"]
               for stage in models[name]["intermediate_differences"])


@pytest.mark.runtime
def test_fresh_world_assay_repeats_candidates_controls_and_all_deltas(tmp_path):
    result = run_in_runner(
        "python3 docs/sound_changes/audits/world-2302-experiments/experiment.py",
        text=True, capture_output=True, check=True, timeout=1800)
    current = json.loads(result.stdout)
    (tmp_path / "world-current-evidence.json").write_text(result.stdout)
    observed = receipt()
    assert current["component_results"] == observed["component_results"]
    for name, model in observed["models"].items():
        fresh = current["models"][name]
        for field in ("final_differences", "full_cascade_candidates",
                      "paradigm_comparisons", "focal_traces"):
            assert fresh[field] == model[field]


@pytest.mark.runtime
def test_fresh_reassessment_repeats_candidates_controls_and_all_deltas(tmp_path):
    result = run_in_runner(
        "python3 docs/sound_changes/audits/world-2302-experiments/experiment.py"
        " --reassessment",
        text=True, capture_output=True, check=True, timeout=1800)
    current = json.loads(result.stdout)
    (tmp_path / "world-reassessment-current.json").write_text(result.stdout)
    observed = reassessment()
    for field in ("source_sha256", "corpus_sha256", "prior_receipt_sha256",
                  "selected_rows", "legacy380_identities", "component_inputs",
                  "component_results", "coordinates", "families", "models"):
        assert current[field] == observed[field], field
    assert current["protected_files_unchanged"] >= 172
    assert current["identity_incremental_all_snapshots_agree"]

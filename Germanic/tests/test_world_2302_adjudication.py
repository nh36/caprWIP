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
        "Minkova1996", "Goering2023"}
    maps = read_tsv((intake / "page_map.tsv").read_text())
    assert {r["printed_page_or_range"] for r in maps
            if r["citation_key"] == "Fulk2010"} == {str(p) for p in range(126, 145)}
    assert {r["printed_page_or_range"] for r in maps
            if r["citation_key"] == "Hogg1996"} == {str(p) for p in range(3, 13)}


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

"""The adopted rainbow history changes its route, not its selected endpoint."""
import gzip
import csv
import importlib.util
import json
from pathlib import Path
import shlex
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
ASSAY = ROOT / "Germanic/docs/sound_changes/audits/rainbow-2148-adoption"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from capr_runtime import run_in_runner
from executable_facts import parse_defines
from historical_sc035 import historical_runtime

# The adoption commit: replaying its frozen capture must pin both the adopted
# FST and the 389-row corpus of that moment (later admissions are separate).
ADOPTION = "2c5b139c54490a32482ef48ff4107b928460865a"


def read(name):
    with gzip.open(ASSAY / f"{name}.json.gz", "rt") as handle:
        return json.load(handle)


def test_only_the_authorized_clause_changes_and_no_order_or_scientific_field():
    before, after = read("before"), read("after")
    base = subprocess.check_output(
        ["git", "show", before["base_commit"] + ":Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True)
    assert {name: value.body for name, value in parse_defines(base).items()} == (
        before["definitions"])
    spec = importlib.util.spec_from_file_location("rainbow_capture", ASSAY / "capture.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    compared = dict(after)
    module.compare(before, compared)
    assert compared == after
    old = "".join(before["definitions"]["PNWGmcULowering"].split())
    new = "".join(after["definitions"]["PNWGmcULowering"].split())
    clause = ("Ctx([{*ù}->{*ò}||_[EnglishStarConsonantNoJ-EnglishStarNasal]"
              "EnglishStarConsonantNoJ*EnglishStarNonHighVowel])")
    assert new == "[" + old + ".o." + clause + "]"
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    assert current["PNWGmcULowering"].body == after["definitions"]["PNWGmcULowering"]


def test_firing_transfer_and_every_rainbow_stage():
    before, after = read("before"), read("after")
    assert len(after["rows"]) == 389
    assert len(after["immutable380_rows"]) == 380
    assert len(after["transitions"]) == 109
    assert len(after["mismatch_ids"]) == 8
    for report in (before, after):
        assert all(len(value) == 1 for value in report["selected_final"])
        assert sum(value == [row["counterpart"]] for row, value in
                   zip(report["rows"], report["selected_final"])) == 381
    index = next(i for i, row in enumerate(after["rows"])
                 if row["row_id"] == "2148")
    changed = {}
    previous = [after["selected_inputs"][index]]
    for step in after["transitions"]:
        value = step["selected_states"][index]
        assert len(value) == 1
        if value != previous:
            changed[step["stage"]] = value[0]
        previous = value
    assert changed == {
        "EnglishProtoInput": "*r*é*g*n*a*b*ù*g*ô",
        "PNWGmcULowering": "*r*é*g*n*a*b*ò*g*ô",
        "OECompoundLinkingSyncope": "*r*é*g*n*b*ò*g*ô",
        "OEStripSecondaryStress": "*r*é*g*n*b*o*g*ô",
        "OEVelarPalatalization": "*r*é*ʝ*n*b*o*g*ô",
        "OEUnstressedLongVowelShortening": "*r*é*ʝ*n*b*o*g*a",
        "OEPalatalFricativeMerger": "*r*é*j*n*b*o*g*a",
        "OldEnglishOrthography": "*r*éġ*n*b*o*g*a",
        "OldEnglishRemoveStars": "reġnboga",
    }
    for stage, counts in [("PNWGmcULowering", (39, 40)),
                          ("OEMedUnstressedULowering", (11, 10))]:
        old, new = [next(s for s in r["transitions"] if s["stage"] == stage)
                    for r in (before, after)]
        assert (len(old["changes"]), len(new["changes"])) == counts
        delta = {r["row_id"] for r in old["changes"]} ^ {
            r["row_id"] for r in new["changes"]}
        assert delta == {"2148"}
    for row_id in ("1963", "2060", "2063", "2201", "2302"):
        i = next(i for i, row in enumerate(after["rows"]) if row["row_id"] == row_id)
        assert [s["selected_states"][i] for s in before["transitions"]] == [
            s["selected_states"][i] for s in after["transitions"]]


def test_component_controls_keep_real_restrictions_and_expose_domain_choice():
    receipt = read("controls")
    values = receipt["outputs"]["PNWGmcULowering"]
    assert values["subordinate-root"] == ["*r*é*g*n*a*b*ò*g*ô"]
    assert values["independent-bow"] == ["*b*ó*g*ô"]
    for name in ("high-trigger", "nasal-first", "intervening-j",
                 "plain-weak-medial"):
        assert values[name] == [receipt["inputs"][name]]
    assert values["later-nasal-literal-guard"] == ["*s*á*t*ò*g*n*a"]
    assert values["grave-without-primary-synthetic"] == ["*b*ò*g*ô"]
    assert receipt["outputs"]["RCompound"]["grave-without-primary-synthetic"] == (
        ["*b*ù*g*ô"])
    assert receipt["linked"] == [["*r*é*g*n*b*ò*g*ô"]]
    assert receipt["stripped"] == [["*r*é*g*n*b*o*g*ô"]]
    assert receipt["forward_functional"]
    assert receipt["selected_general_compound_equivalent"]
    assert sorted(receipt["parser"]["known-biu-ambiguity"]) == ["*b*i*u", "*b*iu"]
    assert receipt["parser"]["rainbow"] == ["*r*é*g*n*a*b*ù*g*ô"]
    assert receipt["parser"]["invalid-ending"] == []


def test_rainbow_is_published_once_in_both_presentations_without_reclassification():
    assembly = ROOT / "Germanic/docs/assembly"
    with (assembly / "manifest_all_by_class.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    # 169 = 168 at rainbow adoption + the published filth article (row 2335).
    assert len(rows) == 169
    regular = [row for row in rows if row["derivation_class"] == "regular"]
    assert len(regular) == 91
    rainbow = [row for row in regular if row["row_id"] == "2148"]
    assert len(rainbow) == 1
    assert (rainbow[0]["proto"], rainbow[0]["protoform"],
            rainbow[0]["counterpart"]) == (
        "*régna-bùgô", "*régna-bùgô", "reġnboga")
    words = [row["lexical_item"] for row in regular]
    assert words == sorted(words)
    for path in (assembly / "lexical_volume_alpha_01.md",
                 assembly / "capr_book_draft_alpha_01.md",
                 ROOT / "Germanic/docs/debug_snapshots/"
                 "oe_derivation_class_trace_report.with_lexeme_reports.publish.md"):
        assert path.read_text().count("The compound means 'rain-bow'.") == 1, path
    path = "Germanic/docs/book/index_semantic_fingerprint_allowlist.tsv"
    previous = list(csv.DictReader(subprocess.check_output(
        ["git", "show", read("before")["base_commit"] + ":" + path],
        cwd=ROOT, text=True).splitlines(), delimiter="\t"))
    current = list(csv.DictReader((ROOT / path).read_text().splitlines(), delimiter="\t"))
    assert all(row in current for row in previous)
    added = [row for row in current if row not in previous]
    # The SC065 adjudication and the filth publication closeout (row 2335)
    # pin their own rows: 3 under the volume heading ref, 8 under the model
    # path, 2 explicit section-20 cognate tags (os/ohg).
    filth_refs = {
        "filth — OE fȳlþ",
        "Germanic/docs/lexeme_reports/model_entries/2335-filth-fȳlþ.model.md",
    }
    filth = [row for row in added if row["source_ref"] in filth_refs
             or (row["source_ref"].endswith("reader_facing_local_section_20.md")
                 and (row["language"], row["form"]) in {("os", "fulitha"),
                                                        ("ohg", "fülida")})]
    assert len(filth) == 13
    added = [row for row in added if row not in filth]
    assert len(added) == 8
    assert {(r["language"], r["form"], r["form_role"], r["source_scope"])
            for r in added} == {
        ("oe", "reġnboga", "target_form", "lexical_heading"),
        ("pgmc", "*régna-bùgô", "source_protoform", "lexical_protoform"),
        ("oe", "reġnboga", "target_form", "explicit_tag"),
        ("oe", "boga", "comparison_form", "explicit_tag"),
        ("oe", "Buga", "comparison_form", "explicit_tag"),
        ("oe", "Boga", "comparison_form", "explicit_tag"),
        ("oe", "rénboga", "evidence_form", "explicit_tag"),
        ("oe", "rénbogan", "evidence_form", "explicit_tag"),
    }
    model = "Germanic/docs/lexeme_reports/model_entries/2148-rainbow-reġnboga.model.md"
    assert all(r["action"] == "add" and not r["variety"] and
               r["source_ref"] == (
                   model if r["source_scope"] == "explicit_tag"
                   else "rainbow — OE reġnboga") for r in added)


@pytest.mark.runtime
def test_fresh_container_capture_and_private_controls_match_committed_receipts():
    script = """
import gzip, json, sys
from pathlib import Path
sys.path.insert(0, '/usr/app/docs/sound_changes/audits/rainbow-2148-adoption')
import capture
p = Path('/usr/app/docs/sound_changes/audits/rainbow-2148-adoption')
before, after, controls = [json.load(gzip.open(p / (n+'.json.gz'), 'rt'))
                           for n in ('before', 'after', 'controls')]
fresh = capture.capture()
capture.compare(before, fresh)
assert fresh == after
assert capture.controls(before) == controls
print('109 stages; selected389 and immutable380; private controls executed')
"""
    with historical_runtime(ADOPTION) as execute:
        result = execute("python3 -c " + shlex.quote(script), timeout=600)
    assert result.returncode == 0, result.stdout + "\n" + result.stderr
    assert "private controls executed" in result.stdout

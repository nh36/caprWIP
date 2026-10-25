"""SC035 historical/domain distinctions and real isolated Foma comparisons."""
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

import pytest


ROOT = Path(__file__).resolve().parents[2]
SC = ROOT / "Germanic/docs/sound_changes"
EVIDENCE = SC / "audits/sc035-prefix-reduction/evidence.json"
BASE = "60b91080d2adadf431c92f7388ab1dd6199a4c7a"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudicate
import oe_pipeline
from capr_runtime import run_in_runner
from historical_sc035 import historical_runtime


def table(path):
    return list(csv.DictReader(
        (line for line in path.read_text().splitlines() if not line.startswith("#")),
        delimiter="\t"))


class PrefixReductionTests(unittest.TestCase):
    def test_adjudicated_history_and_confidence_are_distinct_from_proxy_date(self):
        row = adjudicate.load_registry_row("SC035")
        self.assertEqual((row["adjudication_status"], row["verdict"]),
                         ("adjudicated", "RETAIN"))
        self.assertEqual((row["hist_stage"], row["historical_stage_label"],
                          row["hist_scope"], row["confidence"]),
                         ("preoe", "Pre-Old English",
                          "english_specific", "B"))
        self.assertEqual(row["chronology_profile"], "source_partial_chain")
        self.assertEqual(adjudicate.check_memo("SC035", row=row), [])

    def test_literal_proxy_and_reader_definition_agree(self):
        accepted = "5533f7653f87d3962a92935a280190882c16b61b"
        def historical_text(relative):
            return subprocess.check_output(
                ["git", "show", f"{accepted}:{relative}"], cwd=ROOT, text=True)
        source = historical_text("Germanic/fsts/germanic.txt")
        reader = historical_text(
            "Germanic/docs/sound_changes/reader_facing/035-037-prefix-and-compound-adjustments.md")
        expected = "[ {*a} -> {*ĕ} || .#. {*g} _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic ]"
        for text in (source, reader):
            body = oe_pipeline._define_bodies(
                oe_pipeline._strip_comments(text))["OEPrefixAReduction"]
            self.assertEqual(re.sub(r"\s+", " ", body).strip(), expected)
        self.assertIn("SC107 EAFBrighteningUnstressed", reader)
        self.assertNotIn("witness dates prefix reduction before brightening", reader)
        self.assertNotIn("p. 147, §354", reader)

    def test_only_technical_and_runner_limited_relations_are_claimed(self):
        original = subprocess.check_output(
            ["git", "show", "5533f765:Germanic/docs/sound_changes/registry/chronology_edges.tsv"],
            cwd=ROOT, text=True)
        edges = [r for r in csv.DictReader(
            (line for line in original.splitlines() if not line.startswith("#")), delimiter="\t")
                 if "SC035" in (r["source_change_id"], r["target_change_id"])]
        self.assertEqual({
            (r["source_change_id"], r["target_change_id"],
             r["relation_type"], r["evidence_basis"]) for r in edges
        }, {
            ("SC035", "SC107", "technical_computational", "technical"),
            ("SC035", "PWGmcChanges", "runner_limited_boundary", "boundary_observation"),
        })
        technical = next(r for r in edges if r["target_change_id"] == "SC107")
        self.assertEqual(technical["witness_role"], "displacement_witness")
        self.assertEqual(ROOT / technical["machine_evidence"], EVIDENCE)

    def test_historical_card_is_preserved_not_reinterpreted_in_place(self):
        relative = (
            "Germanic/docs/sound_changes/order_tests/chronology_cards/"
            "SC035-oe-prefix-a-reduction-early.md")
        old = subprocess.check_output(["git", "show", f"{BASE}:{relative}"], cwd=ROOT)
        self.assertEqual((ROOT / relative).read_bytes(), old)

    def test_recorded_assay_identifies_both_populations_and_complete_census(self):
        record = json.loads(EVIDENCE.read_text())
        original_source = subprocess.check_output(
            ["git", "show", f"{BASE}:Germanic/fsts/germanic.txt"], cwd=ROOT)
        self.assertEqual(record["source_sha256"],
                         hashlib.sha256(original_source).hexdigest())
        self.assertEqual((record["selected_rows"], record["legacy380_identity_rows"]),
                         (389, 380))
        self.assertTrue(record["canonical_artifacts_unchanged"])
        self.assertEqual(len(record["live_census"]), 1)
        witness = record["live_census"][0]
        self.assertEqual((witness["row_id"], witness["proto"],
                          witness["fst_input"], witness["legacy380_identity"]),
                         ("1944", "*galáubijaną", "galáubijaną", True))
        self.assertEqual(witness["before"], ["*g*a*l*ēa*b*i*j*a*n*ą"])
        self.assertEqual(witness["after"], ["*g*ĕ*l*ēa*b*i*j*a*n*ą"])
        self.assertEqual(witness["final"], ["ġelīefan"])
        self.assertEqual({row["row_id"] for row in record["live_negative_controls"]},
                         {"2037", "2049", "2044"})
        for control in record["live_negative_controls"]:
            self.assertEqual(control["before"], control["after"])

    def test_recorded_positive_and_negative_component_controls(self):
        record = json.loads(EVIDENCE.read_text())
        inputs, outputs = record["component_inputs"], record["component_outputs"]
        for name, form in inputs.items():
            with self.subTest(name=name):
                expected = form.replace("*a", "*ĕ", 1) if name in {
                    "believe-prefix", "unsegmented-gaCV-structural-control"
                } else form
                self.assertEqual(outputs[name], [expected])
        self.assertEqual(outputs["climb-prefix-cluster"], ["*g*a*s*t*ī*g*a*n"])

    def test_counterfactual_dependency_is_unstressed_not_ordinary_sc043(self):
        variants = json.loads(EVIDENCE.read_text())["variants"]
        self.assertEqual(variants["identity"]["changed"], [])
        for name in ("skip", "after-sc107", "after-sc043", "after-breaking"):
            variant = variants[name]
            self.assertEqual(variant["changed"], [{
                "row_id": "1944", "concept": "believe", "input": "galáubijaną",
                "baseline": ["ġelīefan"], "variant": ["ġealīefan"],
            }])
            trace = variant["believe"]
            self.assertEqual(trace["EAFBrighteningUnstressed-before"],
                             ["*g*a*l*ēa*b*i*j*a*n*ą"])
            self.assertEqual(trace["EAFBrighteningUnstressed-after"],
                             ["*g*æ*l*ēa*b*i*j*a*n*ą"])
            self.assertEqual(trace["EAFBrightening-before"],
                             trace["EAFBrightening-after"])
            self.assertEqual(trace["OEWsPalatalDiphthongization-after"],
                             ["*ʝ*ea*l*ēa*β*j*ą*n"])
        live = variants["identity"]["believe"]
        self.assertEqual(live["OEWsPalatalDiphthongization-before"],
                         live["OEWsPalatalDiphthongization-after"])
        self.assertEqual(live["final"], ["ġelīefan"])

    @pytest.mark.runtime
    def test_fresh_container_assay_reproduces_census_controls_and_counterfactuals(self):
        with historical_runtime(BASE) as execute:
            executed = execute(
                "python3 docs/sound_changes/audits/sc035-prefix-reduction/experiment.py")
        current = json.loads(executed.stdout)
        historical = json.loads(EVIDENCE.read_text())
        self.assertEqual(
            current["source_sha256"],
            historical["source_sha256"])
        for key in ("selected_rows", "legacy380_identity_rows", "live_census",
                    "live_negative_controls", "component_inputs", "component_outputs",
                    "variants", "canonical_artifacts_unchanged"):
            with self.subTest(field=key):
                self.assertEqual(current[key], historical[key])


if __name__ == "__main__":
    unittest.main()

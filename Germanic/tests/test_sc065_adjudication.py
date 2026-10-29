#!/usr/bin/env python3
"""Focused regression for the SC065 medial-syncope adjudication (2026).

Adjudication memo: Germanic/docs/sound_changes/audits/sc065-adjudication.md
Counterfactual receipt: audits/sc065-experiments/counterfactual_receipt.json

Protected invariants:

  * The executable rule `OEMedialSyncope` keeps its adjudicated narrow
    shape: three clauses deleting `{*i}` after a heavy syllable before a
    dental obstruent only. Both restrictions are load-bearing at this
    cascade site (receipt: u-extension corrupts hēafod; any-consonant
    corrupts hierfest and sċilling).
  * The complete live firing population over ALL selected rows is exactly
    {filth} (row 2335, *fūliþō → fȳlþ). The census deliberately does not
    pre-filter candidate rows (an *r* or a syncope site may arise during
    the cascade), unlike earlier narrower tests.
  * Negative controls (head, harvest, shilling, soul) pass the production
    SC065 stage untouched.
  * Chronology: SC055 OEIUmlaut < SC065 is independently demonstrated by
    the filth displacement witness (early syncope bleeds umlaut: +fūlþ).

Run: cd Germanic/tests && python3 -m unittest test_sc065_adjudication
"""
from __future__ import annotations

import csv
import json
import re
import shlex
import sys
import unittest
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
SC_DIR = GERMANIC / "docs" / "sound_changes"
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
RECEIPT = SC_DIR / "audits" / "sc065-experiments" / "counterfactual_receipt.json"

sys.path.insert(0, str(GERMANIC / "tools"))
from capr_runtime import run_in_runner  # noqa: E402


# The adjudicated firing population (sc065-adjudication.md).
EXPECTED_FIRING_CONCEPTS = {"filth"}

# These selected targets must survive the production SC065 stage; each one
# falsified a tested broadening in the counterfactual receipt.
NEGATIVE_CONTROL_CONCEPTS = {
    "head",      # medial *u before dental: the *i-only restriction
    "harvest",   # *i before s: the pre-dental restriction
    "shilling",  # *i before velar: the pre-dental restriction
    "soul",      # medial *a: outside the high-vowel domain entirely
}

DENTALS = r"\[\{\*θ\}\|\{\*ð\}\|\{\*d\}\|\{\*t\}\]"


class SC065AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        with BASELINE.open(encoding="utf-8") as handle:
            cls.baseline = {row["row_id"]: row
                            for row in csv.DictReader(handle, delimiter="\t")}
        cls.by_concept = {row["concept"]: row for row in cls.baseline.values()}
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.positions = {row["foma_identifier"]: int(row["position"])
                             for row in csv.DictReader(handle, delimiter="\t")}

    @classmethod
    def live_stages(cls):
        if not hasattr(cls, "_live_stages"):
            script = """
import json, sys
sys.path.insert(0, "tools")
from capr_runtime import layout
from oe_pipeline import load_rows, evaluation_input
from sc_evidence import STAGES, find_stage, validate_bin
from sound_change_order_sensitivity import batch_apply_down
rt = layout()
index, _, filename = find_stage("OEMedialSyncope")
paths = [rt.bin_dir / STAGES[index - 1][1], rt.bin_dir / filename]
for path in paths:
    validate_bin(path, None)
rows = load_rows(rt.corpus_tsv)
forms = [evaluation_input(r) for r in rows]
before, after = [batch_apply_down(path, forms) for path in paths]
print(json.dumps({r["row_id"]: {"concept": r["concept"],
    "fst_input": form, "before": pre, "after": post}
    for r, form, pre, post in zip(rows, forms, before, after)}))
"""
            result = run_in_runner(
                f"python3 -c {shlex.quote(script)}", capture_output=True,
                text=True, timeout=180)
            if result.returncode:
                raise AssertionError(
                    "SC065 runtime census must execute in the provisioned "
                    f"backend container, not skip:\n{result.stdout}\n{result.stderr}")
            cls._live_stages = json.loads(result.stdout)
        return cls._live_stages

    # ------------------------------------------------------------------
    # Executable rule stability
    # ------------------------------------------------------------------

    def test_rule_definition_keeps_adjudicated_narrow_shape(self):
        match = re.search(
            r"define\s+OEMedialSyncope\s+FootCtx\(\[(.*?)\]\);",
            self.uncommented, re.DOTALL)
        self.assertIsNotNone(match, "OEMedialSyncope define missing")
        body = match.group(1)
        clauses = [c.strip() for c in body.split(",\n") if c.strip()]
        self.assertEqual(len(clauses), 3,
                         "OEMedialSyncope must keep its 3 heavy-syllable "
                         "clauses (RETAIN verdict)")
        expected = [
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*EnglishStarLongVowel\s+"
            r"OEAnyConsonant\+\s*_\s*" + DENTALS + "$",
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*EnglishStarLongDiphthong\s+"
            r"OEAnyConsonant\+\s*_\s*" + DENTALS + "$",
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*EnglishStarShortVowel\s+"
            r"OEAnyConsonant\s+OEAnyConsonant\+\s*_\s*" + DENTALS + "$",
        ]
        for clause, pattern in zip(clauses, expected):
            self.assertRegex(
                clause, pattern,
                "every clause must keep the heavy left flank, the *i-only "
                "target and the dental enumeration; the counterfactual "
                "receipt rejects each tested broadening")
        self.assertNotIn("{*u}", body,
                         "no *u target: the u-extension broadening was "
                         "rejected (corrupts hēafod)")
        self.assertIn("OEMedialSyncope", self.positions,
                      "rule must stay a live numbered cascade stage")

    # ------------------------------------------------------------------
    # Live firing population and negative controls (stage bins)
    # ------------------------------------------------------------------

    @pytest.mark.runtime
    def test_firing_population_over_all_rows_is_exactly_filth(self):
        fired = {}
        live = self.live_stages()
        self.assertEqual(set(live), set(self.baseline))
        # Deliberately census EVERY selected row: candidate environments can
        # arise mid-cascade, so no protoform pre-filter is applied.
        for row_id, row in sorted(self.baseline.items()):
            actual = live[row_id]
            concept = row["concept"]
            self.assertEqual(actual["concept"], concept)
            self.assertEqual(actual["fst_input"], row["fst_input"])
            before, after = actual["before"], actual["after"]
            self.assertTrue(before and after, f"{concept}: missing stage output")
            if before != after:
                fired[row_id] = (concept, before, after)
        self.assertEqual({value[0] for value in fired.values()},
                         EXPECTED_FIRING_CONCEPTS,
                         f"SC065 firing census changed: {sorted(fired)}")
        self.assertEqual(len(fired), len(EXPECTED_FIRING_CONCEPTS))
        concept, before, after = fired[self.by_concept["filth"]["row_id"]]
        self.assertEqual(before, ["*f*ȳ*l*i*θ"])
        self.assertEqual(after, ["*f*ȳ*l*θ"])

    @pytest.mark.runtime
    def test_negative_controls_pass_the_stage_untouched(self):
        for concept in sorted(NEGATIVE_CONTROL_CONCEPTS):
            actual = self.live_stages()[self.by_concept[concept]["row_id"]]
            with self.subTest(concept=concept):
                before, after = actual["before"], actual["after"]
                self.assertEqual(
                    before, after,
                    f"{concept}: SC065 must preserve the selected target")

    # ------------------------------------------------------------------
    # Witness admission and baseline
    # ------------------------------------------------------------------

    def test_filth_witness_row_is_admitted_and_accepted(self):
        row = self.by_concept.get("filth")
        self.assertIsNotNone(row, "filth (row 2335) missing from baseline")
        self.assertEqual(row["row_id"], "2335")
        self.assertEqual(row["proto"], "*fūliþō")
        self.assertEqual(row["counterpart"], "fȳlþ")
        self.assertEqual(row["accepted"], "1")
        self.assertEqual(row["match"], "1")
        self.assertEqual(row["outputs"], "fȳlþ")

    def test_expansion_preserves_original_population(self):
        directory = BASELINE.parent
        previous = {
            row["row_id"]: row
            for row in csv.DictReader(
                (directory / "cascade_baseline_outputs_pre_sc065_expansion.tsv")
                .open(encoding="utf-8"), delimiter="\t")
        }
        current = self.baseline
        receipt = {
            row["field"]: row["value"]
            for row in csv.DictReader(
                (directory / "corpus_expansion_sc065.tsv").open(encoding="utf-8"),
                delimiter="\t")
        }
        self.assertEqual(len(previous), 389)
        self.assertEqual(len(current), 390)
        self.assertEqual(set(current) - set(previous), {"2335"})
        self.assertEqual(
            [(row_id, previous[row_id]["outputs"], current[row_id]["outputs"])
             for row_id in previous
             if previous[row_id]["outputs"] != current[row_id]["outputs"]],
            [],
        )
        summary = json.loads(
            (directory / "cascade_baseline_summary.json").read_text(encoding="utf-8"))
        archived = json.loads(
            (directory / "cascade_baseline_summary_pre_sc065_expansion.json")
            .read_text(encoding="utf-8"))
        self.assertEqual(receipt["adjudication"], "SC065")
        self.assertEqual(receipt["added_row_ids"], "2335")
        self.assertEqual(
            (receipt["previous_selected_count"], receipt["new_selected_count"]),
            ("389", "390"))
        self.assertEqual(receipt["previous_outputs_sha256"], archived["outputs_sha256"])
        self.assertEqual(receipt["new_outputs_sha256"], summary["outputs_sha256"])
        self.assertEqual(receipt["original_row_output_deltas"], "0")
        self.assertEqual(archived["legacy_subset_sha256"], summary["legacy_subset_sha256"])

    # ------------------------------------------------------------------
    # Chronology
    # ------------------------------------------------------------------

    def test_sc065_after_i_umlaut_edge_is_preserved(self):
        lines = [line for line
                 in EDGES.read_text(encoding="utf-8").splitlines()
                 if not line.startswith("#")]
        rows = [row for row in csv.DictReader(lines, delimiter="\t")
                if row["source_change_id"] == "SC065"
                and row["target_change_id"] == "SC055"]
        self.assertEqual(len(rows), 1, "SC065 -> SC055 edge missing")
        edge = rows[0]
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertEqual(edge["witness_role"], "displacement_witness")
        self.assertIn("filth", edge["representative_lexemes"])
        self.assertIn("fūlþ", edge["representative_forms"])

    # ------------------------------------------------------------------
    # Counterfactual receipt pins
    # ------------------------------------------------------------------

    def test_receipt_pins_the_load_bearing_restrictions(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        self.assertTrue(receipt["control_matches_canonical"])
        self.assertEqual(receipt["selected_rows"], 390)
        variants = receipt["variants"]

        def changed(name):
            return {c["row_id"]: c for c in variants[name]["changes"]}

        self.assertEqual(variants["production_control"].get("changes", []), [])
        retired = changed("retired")
        self.assertEqual(set(retired), {"2335"})
        self.assertEqual(retired["2335"]["variant_outputs"], ["fȳleþ"])
        u_ext = changed("u_extension")
        self.assertEqual(set(u_ext), {"2063"})
        self.assertEqual(u_ext["2063"]["variant_outputs"], ["hēafd"])
        any_c = changed("any_consonant")
        self.assertEqual(set(any_c), {"2057", "2181"})
        insitu = changed("open_syllable_insitu")
        self.assertEqual(set(insitu), {"2335"})
        pre_apo = changed("open_syllable_pre_apocope")
        self.assertEqual(set(pre_apo), {"2201"})
        self.assertEqual(pre_apo["2201"]["variant_outputs"], ["sāwl"])
        early = changed("early_pre_umlaut")
        self.assertEqual(set(early), {"2335"})
        self.assertEqual(early["2335"]["variant_outputs"], ["fūlþ"])

    def test_receipt_witness_probes_support_the_chronology(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        probes = {p["id"]: p for p in
                  receipt["variants"]["early_pre_umlaut"]["witness_probes"]}
        # Early syncope bleeds i-umlaut in the *-iþō abstracts.
        self.assertEqual(probes["filth"]["outputs"], ["fūlþ"])
        self.assertEqual(probes["health"]["outputs"], ["hālþ"])
        self.assertEqual(probes["theft"]["outputs"], ["þēofþ"])
        production = {p["id"]: p for p in
                      receipt["variants"]["production_control"]["witness_probes"]}
        self.assertEqual(production["filth"]["outputs"], ["fȳlþ"])
        self.assertEqual(production["health"]["outputs"], ["hǣlþ"])


if __name__ == "__main__":
    unittest.main()

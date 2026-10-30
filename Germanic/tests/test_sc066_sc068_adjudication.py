#!/usr/bin/env python3
"""Focused regression for the SC066/SC068 joint adjudication (2026-10-30).

Adjudication memos:
  Germanic/docs/sound_changes/audits/sc066-adjudication.md  (REFORMULATE)
  Germanic/docs/sound_changes/audits/sc068-adjudication.md  (RETAIN)
Counterfactual receipt:
  audits/sc066-068-experiments/counterfactual_receipt.json

Protected invariants:

  * `OELAdjacentSyncope` keeps its adjudicated weight/open-syllable shape:
    heavy clauses (long V / long diphthong + C+, short nucleus + CC+) and
    the light clause requiring a following vowel. The old single
    environment `V C+ _ *l` was rejected (it syncopates a cetel-type
    nominative, receipt kettle probe).
  * `{*ie}` (WS palatal diphthongization of short *e) is classed as a
    SHORT diphthong; classing it long made the kettle probe wrongly heavy
    (receipt `weight_open_split` vs `weight_open_split_ie_short`).
  * `OEPreconsonantalDegemination` keeps its RETAIN shape
    (TT .o. NN composition).
  * Live firings: SC066 fires on exactly {nettle, spindle, thistle};
    SC068 on exactly {bottom, spindle}. Milk (meoloc) is a negative
    control at the SC066 stage (Barrack 390 would corrupt it).
  * Chronology: SC066 < SC068 is reciprocal and independently
    demonstrated by spindle; SC066 > SC055 by nettle/spindle.

Run: cd Germanic/tests && python3 -m unittest test_sc066_sc068_adjudication
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
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
RECEIPT = (SC_DIR / "audits" / "sc066-068-experiments"
           / "counterfactual_receipt.json")

sys.path.insert(0, str(GERMANIC / "tools"))
from capr_runtime import run_in_runner  # noqa: E402

SC066_EXPECTED_FIRING_CONCEPTS = {"nettle", "spindle", "thistle"}
SC068_EXPECTED_FIRING_CONCEPTS = {"bottom", "spindle"}
# meoloc must survive the SC066 stage untouched: the rule deletes {*i}
# only, and Barrack's 390 post-liquid deletion was rejected because it
# corrupts this row (receipt: barrack_390_postliquid).
SC066_NEGATIVE_CONTROL_CONCEPTS = {"milk"}


def _live_stages(rule_identifier: str) -> dict:
    script = f"""
import json, sys
sys.path.insert(0, "tools")
from capr_runtime import layout
from oe_pipeline import load_rows, evaluation_input
from sc_evidence import STAGES, find_stage, validate_bin
from sound_change_order_sensitivity import batch_apply_down
rt = layout()
index, _, filename = find_stage({rule_identifier!r})
paths = [rt.bin_dir / STAGES[index - 1][1], rt.bin_dir / filename]
for path in paths:
    validate_bin(path, None)
rows = load_rows(rt.corpus_tsv)
forms = [evaluation_input(r) for r in rows]
before, after = [batch_apply_down(path, forms) for path in paths]
print(json.dumps({{r["row_id"]: {{"concept": r["concept"],
    "before": pre, "after": post}}
    for r, pre, post in zip(rows, before, after)}}))
"""
    result = run_in_runner(
        f"python3 -c {shlex.quote(script)}", capture_output=True,
        text=True, timeout=180)
    if result.returncode:
        raise AssertionError(
            f"{rule_identifier} runtime census must execute in the "
            "provisioned backend container, not skip:\n"
            f"{result.stdout}\n{result.stderr}")
    return json.loads(result.stdout)


class SC066SC068AdjudicationTests(unittest.TestCase):
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

    # ------------------------------------------------------------------
    # Executable rule stability
    # ------------------------------------------------------------------

    def test_sc066_keeps_the_weight_open_syllable_shape(self):
        match = re.search(
            r"define\s+OELAdjacentSyncope\s+Ctx\(\[(.*?)\]\);",
            self.uncommented, re.DOTALL)
        self.assertIsNotNone(match, "OELAdjacentSyncope define missing")
        body = match.group(1)
        clauses = [c.strip() for c in body.split(",\n") if c.strip()]
        self.assertEqual(len(clauses), 4,
                         "OELAdjacentSyncope must keep its adjudicated "
                         "4-clause weight/open-syllable shape "
                         "(REFORMULATE verdict)")
        light = r"\[EnglishStarShortVowel\|EnglishStarShortDiphthong\]"
        expected = [
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*EnglishStarLongVowel\s+"
            r"OEAnyConsonant\+\s*_\s*\{\*l\}$",
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*EnglishStarLongDiphthong\s+"
            r"OEAnyConsonant\+\s*_\s*\{\*l\}$",
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*" + light +
            r"\s+OEAnyConsonant\s+OEAnyConsonant\+\s*_\s*\{\*l\}$",
            r"^\{\*i\}\s*->\s*0\s*\|\|\s*" + light +
            r"\s+OEAnyConsonant\s+_\s*\{\*l\}\s+EnglishStarVocalic$",
        ]
        for clause, pattern in zip(clauses, expected):
            self.assertRegex(
                clause, pattern,
                "the heavy clauses and the light open-syllable clause are "
                "all load-bearing: the receipt rejects the old broad "
                "environment (kettle probe) and the wholesale "
                "open-syllable restriction (corrupts spindle)")
        self.assertNotIn("{*e}", body,
                         "the rule deletes {*i} only; the old comment's "
                         "*e claim was false")
        self.assertIn("OELAdjacentSyncope", self.positions)

    def test_ie_diphthong_is_classed_short(self):
        short = re.search(
            r"define\s+EnglishStarShortDiphthong\s+\[(.*?)\];",
            self.text, re.DOTALL).group(1)
        long_ = re.search(
            r"define\s+EnglishStarLongDiphthong\s+\[(.*?)\];",
            self.text, re.DOTALL).group(1)
        short = re.sub(r"(?m)^\s*#.*$", "", short)
        long_ = re.sub(r"(?m)^\s*#.*$", "", long_)
        self.assertIn("{*ie}", short,
                      "{*ie} (WS palatal diphthongization of short *e) "
                      "must stay a SHORT diphthong: classing it long made "
                      "a ċietel-type probe wrongly heavy for SC066")
        self.assertNotIn("{*ie}", long_.replace("{*īe}", ""),
                         "{*ie} must not reappear in the long class "
                         "(the long product of *ē is {*īe})")
        self.assertIn("{*īe}", long_)

    def test_sc068_keeps_the_retain_shape(self):
        self.assertIn(
            "define OEPreconsonantalDegemination "
            "Ctx(OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN);",
            self.uncommented,
            "SC068 RETAIN verdict: TT/NN are segmental cases of one "
            "change; no SPLIT or broadening was licensed")
        self.assertIn("OEPreconsonantalDegemination", self.positions)

    # ------------------------------------------------------------------
    # Live firing populations (stage bins)
    # ------------------------------------------------------------------

    @pytest.mark.runtime
    def test_sc066_firing_population(self):
        live = _live_stages("OELAdjacentSyncope")
        self.assertEqual(set(live), set(self.baseline))
        fired = {live[row_id]["concept"]
                 for row_id in live
                 if live[row_id]["before"] != live[row_id]["after"]}
        self.assertEqual(fired, SC066_EXPECTED_FIRING_CONCEPTS,
                         "SC066 firing census changed")
        nettle = live[self.by_concept["nettle"]["row_id"]]
        self.assertEqual(nettle["before"], ["*n*e*t*i*l*ǭ"])
        self.assertEqual(nettle["after"], ["*n*e*t*l*ǭ"])
        for concept in sorted(SC066_NEGATIVE_CONTROL_CONCEPTS):
            actual = live[self.by_concept[concept]["row_id"]]
            self.assertEqual(actual["before"], actual["after"],
                             f"{concept}: SC066 must not touch this row")

    @pytest.mark.runtime
    def test_sc068_firing_population(self):
        live = _live_stages("OEPreconsonantalDegemination")
        fired = {live[row_id]["concept"]
                 for row_id in live
                 if live[row_id]["before"] != live[row_id]["after"]}
        self.assertEqual(fired, SC068_EXPECTED_FIRING_CONCEPTS,
                         "SC068 firing census changed")
        spindle = live[self.by_concept["spindle"]["row_id"]]
        self.assertEqual(spindle["before"], ["*s*p*i*n*n*l"])
        self.assertEqual(spindle["after"], ["*s*p*i*n*l"])

    # ------------------------------------------------------------------
    # Registry and chronology
    # ------------------------------------------------------------------

    def test_registry_verdicts(self):
        lines = [line for line
                 in REGISTRY.read_text(encoding="utf-8").splitlines()
                 if not line.startswith("#")]
        rows = {row["sc_id"]: row
                for row in csv.DictReader(lines, delimiter="\t")}
        self.assertEqual(rows["SC066"]["adjudication_status"], "adjudicated")
        self.assertEqual(rows["SC066"]["verdict"], "REFORMULATE")
        self.assertEqual(rows["SC068"]["adjudication_status"], "adjudicated")
        self.assertEqual(rows["SC068"]["verdict"], "RETAIN")

    def test_spindle_orders_sc066_before_sc068(self):
        lines = [line for line
                 in EDGES.read_text(encoding="utf-8").splitlines()
                 if not line.startswith("#")]
        rows = {(row["source_change_id"], row["target_change_id"]): row
                for row in csv.DictReader(lines, delimiter="\t")}
        edge = rows[("SC068", "SC066")]
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertEqual(edge["witness_role"], "displacement_witness")
        self.assertIn("spindle", edge["representative_lexemes"])
        earlier = rows[("SC066", "SC055")]
        self.assertEqual(earlier["evidence_basis"],
                         "independently_demonstrated")

    # ------------------------------------------------------------------
    # Counterfactual receipt pins
    # ------------------------------------------------------------------

    def test_receipt_pins_the_load_bearing_conditions(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        self.assertTrue(receipt["control_matches_canonical"])
        self.assertEqual(receipt["selected_rows"], 390)
        variants = receipt["variants"]

        def changed(name):
            return {c["row_id"]: c
                    for c in variants[name].get("changes", [])}

        self.assertEqual(variants["production_control"].get("changes", []),
                         [])
        # Retirements corrupt exactly the live firings.
        self.assertEqual(set(changed("sc066_retired")),
                         {"2139", "2208", "2250"})
        self.assertEqual(set(changed("sc068_retired")), {"1959", "2208"})
        self.assertEqual(changed("sc068_retired")["2208"]["variant_outputs"],
                         ["spinnl"])
        # The adopted reformulation is extensionally identity on the corpus.
        self.assertEqual(
            variants["weight_open_split_ie_short"].get("changes", []), [])
        # A wholesale open-syllable restriction corrupts spindle.
        self.assertEqual(set(changed("open_syllable_only")), {"2208"})
        # Barrack's 390 post-liquid deletion corrupts meoloc and only it.
        b390 = changed("barrack_390_postliquid")
        self.assertEqual(set(b390), {"2126"})
        self.assertEqual(b390["2126"]["variant_outputs"], ["meolc"])
        # The reciprocal order witness.
        order = changed("sc068_before_sc066")
        self.assertEqual(set(order), {"2208"})
        self.assertEqual(order["2208"]["variant_outputs"], ["spinnl"])

    def test_receipt_witness_probes(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        variants = receipt["variants"]

        def probes(name):
            return {p["id"]: p for p in variants[name]["witness_probes"]}

        adopted = probes("weight_open_split_ie_short")
        self.assertEqual(adopted["kettle"]["outputs"], ["ċietel"])
        self.assertTrue(adopted["kettle"]["assertion_holds"],
                        "the cetel-type nominative must retain its vowel")
        self.assertFalse(adopted["angel"]["assertion_holds"],
                         "engel-type latent residue is documented, not "
                         "silently repaired")
        # The old environment syncopates the kettle probe...
        self.assertFalse(
            probes("production_control")["kettle"]["assertion_holds"])
        # ...and the weight split alone is defeated by the {*ie}
        # long-class error (diagnostic for the reclassification).
        self.assertFalse(
            probes("weight_open_split")["kettle"]["assertion_holds"])


if __name__ == "__main__":
    unittest.main()

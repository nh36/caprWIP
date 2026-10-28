#!/usr/bin/env python3
"""Focused regression for the SC087 r-metathesis adjudication (2026).

Adjudication memo: Germanic/docs/sound_changes/audits/sc087-adjudication.md
Counterfactual receipts: audits/sc087-experiments/receipt.json

Protected invariants:

  * The executable rule `OERMetathesis` keeps its adjudicated narrow shape:
    `{*r} V -> V {*r}` for short vowels only, with the protective left
    consonant context and the `{*s} {*t}` cluster requirement. Barrack
    (1975: 115-18) rules 459.1/459.3 describe a broader prevocalic s/n
    metathesis and a regressive pre-xt metathesis. The tested variants
    do not preserve the selected targets; this rejects their unqualified
    adoption, not every possible historical account of the byforms.
  * The complete live firing population is exactly {burst, frost}; both
    firings respect the formal rV -> Vr / C _ st domain.
  * The in-corpus negative controls (brand, drench, string, grass, run,
    fright) pass the production metathesis stage untouched.
  * Chronology: SC087 after SC044 (breaking) remains the independently
    demonstrated displacement edge (burst witness: early metathesis would
    produce +beorstan).

Run: cd Germanic/tests && python3 -m unittest test_sc087_adjudication
"""
from __future__ import annotations

import csv
import importlib.util
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

sys.path.insert(0, str(GERMANIC / "tools"))
from capr_runtime import run_in_runner  # noqa: E402


# The adjudicated firing population (sc087-adjudication.md).
EXPECTED_FIRING_CONCEPTS = {"burst", "frost"}

# These selected targets must survive the production stage. Some broader
# variants yield an attested but unselected byform, not an unattested word.
NEGATIVE_CONTROL_CONCEPTS = {
    "brand", "drench", "string",  # rVn under Barrack 459.1 s/n matrix
    "grass",                      # rVs with fronted ae vowel
    "run",                        # word-initial rVn (no left consonant)
    "fright",                     # Vrxt under Barrack 459.3 regressive rule
}


class SC087AdjudicationTests(unittest.TestCase):
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
index, _, filename = find_stage("OERMetathesis")
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
                    "SC087 runtime census must execute in the provisioned "
                    f"backend container, not skip:\n{result.stdout}\n{result.stderr}")
            cls._live_stages = json.loads(result.stdout)
        return cls._live_stages

    # ------------------------------------------------------------------
    # Executable rule stability
    # ------------------------------------------------------------------

    def test_rule_definition_keeps_adjudicated_narrow_shape(self):
        match = re.search(r"define\s+OERMetathesis\s*\[(.*?)\];",
                          self.uncommented, re.DOTALL)
        self.assertIsNotNone(match, "OERMetathesis define missing")
        body = match.group(1)
        clauses = [c.strip() for c in body.split(",") if c.strip()]
        self.assertEqual(len(clauses), 8,
                         "OERMetathesis must keep its 8 short-vowel clauses")
        for clause in clauses:
            self.assertRegex(
                clause,
                r"^\{\*r\}\s*\{\*[euioaéóá]\}\s*->\s*\{\*[euioaéóá]\}\s*\{\*r\}"
                r"\s*\|\|\s*EnglishStarConsonant\s*_\s*\{\*s\}\s*\{\*t\}$",
                "every clause must keep the left consonant context and the "
                "st cluster requirement (RETAIN verdict; Barrack broadening "
                "rejected by counterfactual receipts)")
        self.assertNotIn("{*n}", body,
                         "no nasal context: the Barrack 459.1 s/n broadening "
                         "was rejected (corrupts brandes/drenc/streng)")
        self.assertIn("OERMetathesis", self.positions,
                      "rule must stay a live numbered cascade stage")
        self.assertNotIn("OERRegressiveMetathesis", self.uncommented,
                         "the Barrack 459.3 regressive variant is "
                         "experiment-only (corrupts fyrhte)")

    # ------------------------------------------------------------------
    # Live firing population and negative controls (stage bins)
    # ------------------------------------------------------------------

    @pytest.mark.runtime
    def test_firing_population_is_exactly_burst_and_frost(self):
        fired = {}
        live = self.live_stages()
        self.assertEqual(set(live), set(self.baseline))
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
                         f"SC087 firing census changed: {sorted(fired)}")
        self.assertEqual(len(fired), len(EXPECTED_FIRING_CONCEPTS))
        for row_id, (concept, before, after) in fired.items():
            with self.subTest(row_id=row_id, concept=concept):
                self.assertEqual(len(before), 1)
                self.assertEqual(len(after), 1)
                self.assertRegex(
                    before[0].replace("*", ""),
                    r"r[euioaéóá]st",
                    f"{concept}: input not in the rV-st domain")
                self.assertRegex(
                    after[0].replace("*", ""),
                    r"[euioaéóá]rst",
                    f"{concept}: output not metathesized to Vr-st")

    @pytest.mark.runtime
    def test_negative_controls_pass_the_stage_untouched(self):
        for concept in sorted(NEGATIVE_CONTROL_CONCEPTS):
            actual = self.live_stages()[self.by_concept[concept]["row_id"]]
            with self.subTest(concept=concept):
                before, after = actual["before"], actual["after"]
                self.assertEqual(
                    before, after,
                    f"{concept}: SC087 must preserve the selected target")

    # ------------------------------------------------------------------
    # Chronology
    # ------------------------------------------------------------------

    def test_sc087_after_breaking_edge_is_preserved(self):
        lines = [line for line
                 in EDGES.read_text(encoding="utf-8").splitlines()
                 if not line.startswith("#")]
        rows = [row for row in csv.DictReader(lines, delimiter="\t")
                if row["source_change_id"] == "SC087"
                and row["target_change_id"] == "SC044"]
        self.assertEqual(len(rows), 1, "SC087 -> SC044 edge missing")
        edge = rows[0]
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertEqual(edge["witness_role"], "displacement_witness")
        self.assertIn("burst", edge["representative_lexemes"])


class ControlledComparisonTests(unittest.TestCase):
    def test_factorial_variants_isolate_the_two_dimensions(self):
        path = SC_DIR / "audits/sc087-experiments/experiment.py"
        spec = importlib.util.spec_from_file_location("sc087_experiment", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sources = module.variant_sources(FST, controlled=True)
        blocks = {name: module.METATHESIS_BLOCK.search(text).group(0)
                  for name, text in sources.items()}
        self.assertEqual(
            blocks["A"].replace("{*s} {*t}", "{*s}"), blocks["B"])
        self.assertEqual(
            blocks["C"].replace("{*s} {*t}", "{*s}"), blocks["D"])
        self.assertEqual(
            module.extended_vowel_block(blocks["A"], "{*s} {*t}"), blocks["C"])
        for name, source in sources.items():
            self.assertEqual(
                source.replace(blocks[name], "RULE"),
                sources["A"].replace(blocks["A"], "RULE"))

    def test_controlled_receipt_discriminates_grass_without_a_corpus_change(self):
        receipt = json.loads(
            (SC_DIR / "audits/sc087-experiments/controlled_receipt.json").read_text())
        self.assertTrue(receipt["control_matches_canonical"])
        comparisons = receipt["comparisons"]
        self.assertEqual(comparisons["A_vs_B"]["changes"], [])
        self.assertEqual(comparisons["A_vs_C"]["changes"], [])
        changes = comparisons["C_vs_D"]["changes"]
        self.assertEqual([r["row_id"] for r in changes], ["2045"])
        grass = changes[0]
        self.assertEqual(grass["pre_sc087"], ["*g*r*æ*s"])
        self.assertEqual(grass["selected_target"], "græs")
        self.assertEqual(grass["left_outputs"], ["græs"])
        self.assertEqual(grass["right_outputs"], ["gærs"])
        self.assertEqual(grass["assessment"], "attested_alternative_not_selected")
        self.assertTrue(grass["left_matches_selected"])
        self.assertFalse(grass["right_matches_selected"])

    def test_cress_receipt_separates_local_predictions_from_admission(self):
        receipt = json.loads(
            (SC_DIR / "audits/sc087-experiments/cress_receipt.json").read_text())
        self.assertFalse(receipt["admitted"])
        self.assertEqual(len(receipt["inherited_probes"]), 2)
        for probe in receipt["inherited_probes"]:
            self.assertEqual(probe["first_rejecting_stage"], "EnglishProtoInput")
        components = receipt["local_components"]
        for name in ("A", "C"):
            for probe in components[name]["probes"]:
                self.assertEqual(probe["post_sc087"], [probe["pre_sc087"]])
        self.assertEqual(components["B"]["probes"][0]["post_sc087"],
                         ["*k*e*r*s*s*e"])
        self.assertEqual(components["B"]["probes"][1]["post_sc087"],
                         ["*k*r*æ*s*s*e"])
        self.assertEqual(components["D"]["probes"][1]["post_sc087"],
                         ["*k*æ*r*s*s*e"])


if __name__ == "__main__":
    unittest.main()

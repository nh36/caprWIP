#!/usr/bin/env python3
"""Focused regression for the SC087 r-metathesis adjudication (2026).

Adjudication memo: Germanic/docs/sound_changes/audits/sc087-adjudication.md
Counterfactual receipts: audits/sc087-experiments/receipt.json

Protected invariants:

  * The executable rule `OERMetathesis` keeps its adjudicated narrow shape:
    `{*r} V -> V {*r}` for short vowels only, with the protective left
    consonant context and the `{*s} {*t}` cluster requirement. Barrack
    (1975: 115-18) rules 459.1/459.3 describe a broader prevocalic s/n
    metathesis and a regressive pre-xt metathesis; both were tested as
    counterfactual variants and rejected (RETAIN verdict): the broad law
    corrupts attested brandes/drenc/streng/graes while deriving nothing
    new, and the regressive law corrupts attested fyrhte.
  * The complete live firing population is exactly {burst, frost}; both
    firings respect the formal rV -> Vr / C _ st domain.
  * The in-corpus negative controls (brand, drench, string, grass, run,
    fright) pass the metathesis stage untouched: OE selects their
    unmetathesized doublet variants, so any broadened rule must fail here.
  * Chronology: SC087 after SC044 (breaking) remains the independently
    demonstrated displacement edge (burst witness: early metathesis would
    produce +beorstan).

Run: cd Germanic/tests && python3 -m unittest test_sc087_adjudication
"""
from __future__ import annotations

import csv
import re
import shutil
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
BIN_DIR = REPO_ROOT / "backend"

import sys

sys.path.insert(0, str(GERMANIC / "tools"))
from oe_pipeline import run_stage  # noqa: E402

RUNTIME_BUILT = ((BIN_DIR / "old_english_sandbox_after_oe_r_metathesis.bin").is_file()
                 and shutil.which("flookup") is not None)
_runtime_available = unittest.skipUnless(
    RUNTIME_BUILT,
    "live runtime probe: needs local sandbox bins (adjudicate --evidence) "
    "and flookup on PATH")


def requires_runtime(test):
    return pytest.mark.runtime(_runtime_available(test))


# The adjudicated firing population (sc087-adjudication.md).
EXPECTED_FIRING_CONCEPTS = {"burst", "frost"}

# In-corpus negative controls: attested OE selects the unmetathesized
# variant, so the narrow law must leave these untouched. The counterfactual
# broadened variants (receipt.json) each corrupt a subset of these.
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
            cls.baseline = {row["concept"]: row
                            for row in csv.DictReader(handle, delimiter="\t")}
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.positions = {row["foma_identifier"]: int(row["position"])
                             for row in csv.DictReader(handle, delimiter="\t")}

    def stage(self, name, form):
        return run_stage(BIN_DIR, f"old_english_sandbox_after_{name}.bin", form)

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

    @requires_runtime
    def test_firing_population_is_exactly_burst_and_frost(self):
        fired = {}
        candidates = {concept: row for concept, row in self.baseline.items()
                      if "r" in row["proto"]}
        for concept, row in sorted(candidates.items()):
            before = self.stage("oe_contraction", row["fst_input"])
            after = self.stage("oe_r_metathesis", row["fst_input"])
            if before != after:
                fired[concept] = (before, after)
        self.assertEqual(set(fired), EXPECTED_FIRING_CONCEPTS,
                         f"SC087 firing census changed: {sorted(fired)}")
        for concept, (before, after) in fired.items():
            with self.subTest(concept=concept):
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

    @requires_runtime
    def test_negative_controls_pass_the_stage_untouched(self):
        for concept in sorted(NEGATIVE_CONTROL_CONCEPTS):
            row = self.baseline[concept]
            with self.subTest(concept=concept):
                before = self.stage("oe_contraction", row["fst_input"])
                after = self.stage("oe_r_metathesis", row["fst_input"])
                self.assertEqual(
                    before, after,
                    f"{concept}: attested OE selects the unmetathesized "
                    "variant; SC087 must not touch it")

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


if __name__ == "__main__":
    unittest.main()

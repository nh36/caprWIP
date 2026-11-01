"""Portable checks of the executed, current-baseline lexical research."""
import gzip
import hashlib
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


class EarthlyEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(gzip.decompress((HERE / "results.json.gz").read_bytes()))

    def cell(self, model, name):
        return self.report["models"][model]["candidates"][name]

    def test_fresh_identity_matches_every_frozen_selected_output(self):
        report = self.report
        self.assertEqual(len(report["plan"]["rows"]), 390)
        self.assertEqual(report["models"]["identity"]["counts"]["matched"], 382)
        self.assertEqual(
            report["snapshot"]["inputs"]["source"]["sha256"],
            hashlib.sha256((HERE.parents[4] / "Germanic/fsts/germanic.txt").read_bytes()).hexdigest())
        summary = json.loads((HERE.parents[4] / (
            "Germanic/docs/sound_changes/cascade_baseline/cascade_baseline_summary.json")).read_text())
        self.assertEqual(report["population_checks"]["selected390_evaluator_sha256"],
                         summary["outputs_sha256"])
        self.assertEqual(report["population_checks"]["active380_sha256"],
                         summary["legacy_subset_sha256"])

    def test_every_model_preserves_both_populations_at_every_aligned_stage(self):
        for name, model in self.report["models"].items():
            with self.subTest(model=name):
                self.assertFalse(model["selected_final_delta_ids"])
                self.assertFalse(model["immutable_final_delta_indices"])
                for delta in model["aligned_intermediate_deltas"]:
                    self.assertFalse(delta["rows"])
                    self.assertFalse(delta["immutable_indices"])
                self.assertEqual(len(model["traces"]), len(model["order"]))
                for trace in model["traces"]:
                    self.assertEqual(len(trace["after"]),
                                     390 + 380 + len(self.report["plan"]["candidates"]))
                    self.assertTrue(all(len(value) <= 1 for value in trace["after"]))
                for internal in model["internal_operations"]:
                    stage = next(t for t in model["traces"] if t["stage"] == internal["stage"])
                    self.assertEqual(internal["operations"][0]["before"], stage["before"])
                    self.assertEqual(internal["operations"][-1]["after"], stage["after"])
                    self.assertTrue(all(len(value) <= 1 for operation in internal["operations"]
                                        for value in operation["after"]))

    def test_general_prominence_derives_complete_genitive_not_the_plain_compound(self):
        for model in ("earlier-prominence", "single-onset-sensitivity",
                      "final-overheavy-sensitivity", "r-syncope-slice", "combined-sensitivity"):
            for name in ("earthly-genitive-grave", "earthly-genitive-final-a",
                         "earthly-genitive-neuter-es"):
                self.assertEqual(self.cell(model, name)["final"], ["eorþcundes"])
            self.assertEqual(self.cell(model, "earthly-genitive-plain")["final"],
                             ["eorþocundes"])
        self.assertEqual(self.cell("identity", "earthly-genitive-grave")["final"],
                         ["eorþcondes"])
        self.assertEqual(self.cell("parser-only", "earthly-genitive-grave")["final"],
                         ["eorþcondes"])

    def test_current_syncopes_do_not_solve_the_feminine_ending(self):
        cell = self.cell("earlier-prominence", "earthly-feminine-genitive")
        self.assertEqual(cell["final"], ["eorþcundere"])
        for stage in ("OEMedialSyncope", "OELAdjacentSyncope", "OEPreconsonantalDegemination"):
            step = next(s for s in cell["steps"] if s["stage"] == stage)
            self.assertEqual(step["before"], step["after"])
        for model in ("r-syncope-slice", "combined-sensitivity"):
            self.assertEqual(self.cell(model, "earthly-feminine-genitive")["final"],
                             ["eorþcundre"])
            self.assertEqual(self.cell(model, "godcund-feminine-genitive")["final"],
                             ["godcundre"])
        self.assertEqual(
            self.cell("earlier-prominence", "earthly-feminine-genitive-iz")["final"],
            ["eorþcyndere"])

    def test_ending_success_is_not_conflated_with_grammatical_identification(self):
        self.assertEqual(
            self.cell("earlier-prominence", "earthly-weak-neuter-ending-on-diagnostic")["final"],
            ["eorþcunde"])
        self.assertEqual(
            self.cell("earlier-prominence", "earthly-feminine-accusative")["final"],
            ["eorþcunde"])
        self.assertEqual(
            self.cell("earlier-prominence", "earthly-accusative-masculine")["final"],
            ["eorþcundene"])

    def test_bimoric_nasal_ending_diagnostic_is_not_a_plain_long_vowel(self):
        self.assertFalse(self.cell(
            "identity", "earthly-unsupported-trimoric-nasal-trial")["parser_accepted"])
        for model in ("earlier-prominence", "single-onset-sensitivity",
                      "final-overheavy-sensitivity", "r-syncope-slice",
                      "combined-sensitivity"):
            self.assertEqual(
                self.cell(model, "earthly-weak-neuter-unaugmented-nasal")["final"],
                ["eorþcunde"])
            self.assertEqual(
                self.cell(model, "godcund-weak-neuter-unaugmented-nasal")["final"],
                ["godcunde"])
        self.assertEqual(
            self.cell("identity", "earthly-weak-neuter-unaugmented-nasal")["final"],
            ["eorþconde"])
        self.assertEqual(
            self.cell("earlier-prominence", "earthly-weak-neuter-ending-o-diagnostic")["final"],
            ["eorþcond"])
        self.assertEqual(
            self.cell("earlier-prominence", "earthly-strong-masculine-accusative-nasal")["final"],
            ["eorþcundene"])

    def test_dative_has_a_real_diphthong_but_still_fails_its_complete_ending(self):
        for name, expected in (("earthly-strong-dative-plural", "eorþcundem"),
                               ("godcund-strong-dative-plural", "godcundem")):
            self.assertFalse(self.cell("identity", name)["parser_accepted"])
            cell = self.cell("earlier-prominence", name)
            self.assertTrue(cell["parser_accepted"])
            self.assertIn("*ai", cell["steps"][0]["after"][0])
            monophthongization = next(s for s in cell["steps"]
                                     if s["stage"] == "PNWGmcUnstressedAiMonophthongization")
            self.assertNotEqual(monophthongization["before"], monophthongization["after"])
            self.assertEqual(cell["final"], [expected])

    def test_foot_controls_and_the_final_overheavy_qualification(self):
        data = self.report["plan"]["components"]
        foot = self.report["component_results"]["RFoot"]
        for name in ("late-godcund-accusative", "late-godcund-feminine-genitive",
                     "late-earthly", "late-eorpthcundre"):
            self.assertEqual(foot[name], [data[name].replace("*u", "*ù")])
        for name in ("late-world-inflected", "late-cyning-inflected",
                     "late-godcund-uninflected"):
            self.assertEqual(foot[name], [data[name]])
        final = self.report["component_results"]["RLastFoot"]
        self.assertEqual(final["late-godcund-uninflected"],
                         [data["late-godcund-uninflected"].replace("*u", "*ù")])
        self.assertEqual(final["late-final-overheavy-LH-synthetic"],
                         [data["late-final-overheavy-LH-synthetic"]])

    def test_general_syncope_slice_has_actual_phonological_negatives(self):
        data = self.report["plan"]["components"]
        result = self.report["component_results"]["RRSlice"]
        self.assertEqual(result["syncope-headed-heavy-r"],
                         [data["syncope-headed-heavy-r"].replace("*e*r", "*r")])
        for name in ("syncope-light-r-negative", "syncope-no-following-vowel-negative",
                     "syncope-long-vowel-negative"):
            self.assertEqual(result[name], [data[name]])

    def test_functional_relations_and_independent_composed_crosschecks(self):
        for result in self.report["formal"].values():
            self.assertIn("1 (1 = TRUE, 0 = FALSE)", result["stdout"])
        for name in ("identity", "earlier-prominence", "final-overheavy-sensitivity",
                     "combined-sensitivity"):
            self.assertTrue(self.report["models"][name]["composed_crosscheck"])
        for model in self.report["models"].values():
            self.assertEqual(model["order"].count("OEStripSecondaryStress"), 1)

    def test_runtime_and_all_preexisting_tracked_sources_were_unchanged(self):
        self.assertEqual(self.report["canonical_before"], self.report["canonical_after"])
        protection = json.loads((HERE / "protection.json").read_text())
        self.assertEqual(protection["before"], protection["after"])
        self.assertEqual(protection["runtime_before"], protection["runtime_after"])
        self.assertIn("old_english.bin", protection["runtime_before"])
        self.assertIn("oe_build_manifest.json", protection["runtime_before"])


if __name__ == "__main__":
    unittest.main()

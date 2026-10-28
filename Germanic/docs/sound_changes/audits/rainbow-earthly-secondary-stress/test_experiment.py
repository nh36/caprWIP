"""Portable assertions over the actual isolated Foma research receipt."""
from __future__ import annotations

import gzip
import hashlib
import json
import unittest
from pathlib import Path


class ResearchReceipt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with gzip.open(Path(__file__).with_name("results.json.gz"), "rt") as handle:
            cls.report = json.load(handle)

    def candidate(self, model, name):
        return next(row for row in self.report["models"][model]["candidates"]
                    if row["name"] == name)

    def step(self, model, candidate, stage):
        return next(row for row in self.candidate(model, candidate)["steps"]
                    if row["stage"] == stage)

    def test_identity_matches_live_outputs_and_every_snapshot(self):
        report = self.report
        self.assertTrue(report["identity_equal"])
        baseline = {row["row_id"]: row for row in report["baseline"]["records"]}
        identity = report["models"]["identity"]
        for row, output in zip(report["rows"], identity["final"]):
            with self.subTest(row=row["row_id"]):
                self.assertEqual("|".join(output), baseline[row["row_id"]]["outputs"])
        self.assertEqual(identity["population_checks"]["evaluator_sha256"],
                         report["baseline"]["summary"]["outputs_sha256"])
        self.assertEqual(identity["population_checks"]["active380_sha256"],
                         report["baseline"]["summary"]["legacy_subset_sha256"])
        self.assertFalse(identity["population_checks"]["immutable380_delta_ids"])

    def test_sources_runtime_bins_and_receipts_remained_identical(self):
        self.assertTrue(self.report["production_unchanged"])
        self.assertEqual(self.report["protected_before"], self.report["protected_after"])
        self.assertIn("old_english.bin", self.report["protected_before"])
        self.assertIn("oe_build_manifest.json", self.report["protected_before"])
        self.assertTrue(any("migration.json" in name
                            for name in self.report["protected_before"]))

    def test_full_traces_include_nonfirings_and_rejections(self):
        for name, result in self.report["models"].items():
            with self.subTest(model=name):
                self.assertEqual(result["order"].count("OEStripSecondaryStress"), 1)
                self.assertEqual(len(result["transitions"]), len(result["order"]))
                for step in result["transitions"]:
                    self.assertTrue(all(len(outputs) <= 1 for outputs in step["corpus_states"]))
                    self.assertEqual(len(step["immutable380_states"]), 380)
                    self.assertTrue(all(len(outputs) <= 1
                                        for outputs in step["immutable380_states"]))
                self.assertEqual(
                    result["transitions"][-1]["immutable380_states"],
                    result["population_checks"]["immutable380_outputs"])
                for candidate in result["candidates"]:
                    self.assertEqual(len(candidate["steps"]), len(result["order"]))
                    self.assertEqual(candidate["steps"][-1]["after"], candidate["final"])
                    self.assertTrue(any(not step["changed"] for step in candidate["steps"]))
                    self.assertTrue(all(len(step["after"]) <= 1 for step in candidate["steps"]))

    def test_composed_foma_relations_agree_with_component_cascades(self):
        for model in (
            "identity", "A-secondary", "A-compound", "B2-foot-annotations",
            "B3-conditioned-lowering", "joint",
        ):
            with self.subTest(model=model):
                self.assertTrue(self.report["models"][model]["composed_crosscheck"])

    def test_early_lowering_preserves_accent_and_respects_nasal_j_high_vowel(self):
        results = self.report["components"]["RSyllEarly"]
        original = self.report["component_inputs"]
        for name in ("early-kund-grave", "early-high-vowel-synthetic",
                     "early-j-block-synthetic", "early-unstressed-synthetic"):
            with self.subTest(control=name):
                self.assertEqual(results[name], [original[name]])
        self.assertEqual(results["early-bow-grave"],
                         [original["early-bow-grave"].replace("*ù", "*ò")])
        self.assertEqual(self.report["components"]["RCompEarly"]["early-bow-grave"],
                         results["early-bow-grave"])
        self.assertNotEqual(
            self.report["components"]["RBroadEarly"]["early-unstressed-synthetic"],
            [original["early-unstressed-synthetic"]])

    def test_late_dental_nasal_is_not_the_labial_nasal_exception(self):
        late = self.report["components"]["OEMedUnstressedULowering"]
        inputs = self.report["component_inputs"]
        self.assertEqual(late["late-dental-nasal"],
                         [inputs["late-dental-nasal"].replace("*u", "*o")])
        self.assertEqual(late["late-labial-nasal"], [inputs["late-labial-nasal"]])

    def test_light_initial_world_does_not_acquire_a_secondary_foot(self):
        foot = self.report["components"]["RFoot"]
        inputs = self.report["component_inputs"]
        for name in (
            "late-world", "late-world-inflected", "late-world-back-mutated",
            "late-world-back-mutated-inflected", "late-earthly-uninflected",
        ):
            with self.subTest(control=name):
                self.assertEqual(foot[name], [inputs[name]])
        for name in ("late-earthly", "late-earthly-accusative", "late-godcund",
                     "late-earthly-pretonic-synthetic"):
            with self.subTest(control=name):
                self.assertEqual(foot[name], [inputs[name].replace("*u", "*ù")])

    def test_syllabification_and_footing_are_functions_not_optional_annotations(self):
        for rule in ("RSyll", "RFoot"):
            for name, outputs in self.report["components"][rule].items():
                with self.subTest(rule=rule, control=name):
                    self.assertEqual(len(outputs), 1)

    def test_formal_forward_functionality_not_inverse_uniqueness(self):
        with gzip.open(Path(__file__).with_name("functionality.json.gz"), "rt") as handle:
            formal = json.load(handle)
        self.assertEqual(formal["source_sha256"], self.report["source_sha256"])
        experimental = self.report["definitions"].split("\ndefine RWhole0 ", 1)[0]
        self.assertEqual(formal["experimental_definitions_sha256"],
                         hashlib.sha256(experimental.encode()).hexdigest())
        self.assertTrue(formal["sound_operations_functional"])
        self.assertEqual(formal["protected_before"], formal["protected_after"])
        for name, result in formal["checks"].items():
            with self.subTest(component=name):
                if name in ("EnglishProtoInput", "RInput"):
                    self.assertFalse(result["functional"])
                    self.assertFalse(result["ambiguous_domain_empty"])
                    self.assertEqual(result["biu_witness"], ["*b*i*u", "*b*iu"])
                else:
                    self.assertTrue(result["ambiguous_domain_empty"])
        for name in ("REarly", "REarlyComp", "RFoot", "RLate", "RLateOne"):
            self.assertTrue(formal["checks"][name]["functional"])

    def test_rainbow_lowering_is_early_and_not_reversed_or_supplied_late(self):
        early = self.step("joint", "rainbow", "REarly")
        self.assertEqual(early["after"], [early["before"][0].replace("*ù", "*ò")])
        for stage in ("OEMedUnstressedORaising", "RLate"):
            step = self.step("joint", "rainbow", stage)
            self.assertFalse(step["changed"])
            self.assertIn("*o", step["before"][0])
        self.assertTrue(self.step(
            "B3-conditioned-lowering", "rainbow", "RLate")["changed"])
        self.assertEqual(self.candidate("joint", "rainbow")["final"], ["reġnboga"])

    def test_complete_genitive_not_merely_the_stem_and_honest_ending_failures(self):
        for name in ("earthly-genitive-grave", "earthly-genitive-final-a",
                     "earthly-genitive-neuter-es"):
            self.assertEqual(self.candidate("joint", name)["final"], ["eorþcundes"])
        self.assertEqual(self.candidate("identity", "earthly-genitive-grave")["final"],
                         ["eorþcondes"])
        self.assertEqual(self.candidate("G-parser-only", "earthly-genitive-final-a")["final"],
                         ["eorþcondes"])
        self.assertEqual(self.candidate("joint", "earthly-genitive-plain")["final"],
                         ["eorþocundes"])
        self.assertEqual(self.candidate("joint", "earthly-accusative-masculine")["final"],
                         ["eorþcundene"])
        self.assertEqual(self.candidate("joint", "earthly-feminine-genitive")["final"],
                         ["eorþcundere"])

    def test_serious_models_preserve_selected_and_both_protected_populations(self):
        reference = self.report["models"]["identity"]
        for name, result in self.report["models"].items():
            if name.startswith("strip-") or name == "A-overbroad-diagnostic":
                continue
            with self.subTest(model=name):
                self.assertEqual(result["counts"], reference["counts"])
                self.assertEqual(result["final"], reference["final"])
                self.assertFalse(result["final_deltas"])
                self.assertEqual(result["population_checks"],
                                 reference["population_checks"])
                for word, output in (("world", "weorold"), ("soul", "sāwol")):
                    self.assertEqual(self.candidate(name, word)["final"], [output])

    def test_overbroad_and_ordering_controls_expose_specific_failures(self):
        deltas = self.report["models"]["A-overbroad-diagnostic"]["final_deltas"]
        self.assertEqual({row["row_id"]: (row["old"], row["new"]) for row in deltas},
                         {"2060": (["hafoc"], ["hafac"]),
                          "2063": (["hēafod"], ["hēafad"])})
        models = self.report["models"]
        self.assertEqual(
            {row["row_id"] for row in models["strip-after-late-early-0"]["final_deltas"]},
            {"2148", "2302"})
        self.assertEqual(
            {row["row_id"] for row in models["strip-after-late-early-1"]["final_deltas"]},
            {"2302"})

    def test_weight_and_inflection_controls_do_not_reduce_to_heavy_medial_stress(self):
        inputs = self.report["component_inputs"]
        foot = self.report["components"]["RFoot"]
        self.assertEqual(foot["late-aetheling-inflected"],
                         [inputs["late-aetheling-inflected"].replace("*i", "*ì")])
        self.assertEqual(foot["late-cyning-inflected"], [inputs["late-cyning-inflected"]])
        self.assertEqual(foot["late-sinfull-uninflected"], [inputs["late-sinfull-uninflected"]])
        self.assertEqual(foot["late-sinfull-inflected"],
                         [inputs["late-sinfull-inflected"].replace("*u", "*ù")])

    def test_weak_lh_positive_and_negative_controls(self):
        weak = self.report["components"]["OELHWeakRaising"]
        inputs = self.report["component_inputs"]
        for name in ("weak-LH-world", "weak-LH-twofold"):
            self.assertEqual(weak[name], [inputs[name].replace("*a", "*u")])
        for name in (
            "weak-LH-grave", "weak-LH-primary", "weak-LH-heavy-first",
            "weak-LH-no-cluster", "weak-LH-initial-weak", "weak-LH-onefold",
        ):
            with self.subTest(control=name):
                self.assertEqual(weak[name], [inputs[name]])


if __name__ == "__main__":
    unittest.main()

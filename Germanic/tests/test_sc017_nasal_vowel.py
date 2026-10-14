"""Production admission and complete-derivation receipt for nasal bimoric o."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))

from executable_facts import parse_defines
from verify_sc017_nasal_vowel import CLASSES, consumer_audit


class NasalBimoricTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (ROOT / "Germanic/fsts/germanic.txt").read_text()
        cls.definitions = parse_defines(cls.source)
        cls.receipt = json.loads((
            ROOT / "Germanic/docs/sound_changes/audits/sc017-nasal-vowel-adoption-receipt.json"
        ).read_text())

    def test_all_general_classes_recognize_the_single_codepoint(self):
        for name in CLASSES:
            with self.subTest(name=name):
                self.assertIn("{*ǭ}", self.definitions[name].body)
                self.assertNotIn("o\u0328\u0304", self.definitions[name].body)

    def test_complete_selected_derivations_are_unchanged(self):
        report = self.receipt
        self.assertEqual(report["selected_rows"], 387)
        self.assertEqual(report["checkpoint_count"], 107)
        self.assertEqual(report["identical_row_checkpoints"], 41409)
        for key in ("changed_derivation_ids", "changed_final_ids", "rejected_ids", "ambiguous_ids"):
            self.assertEqual(report[key], [])
        self.assertEqual(report["mismatch_ids"],
                         ["1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"])
        self.assertTrue(report["canonical_artifacts_unchanged"])

    def test_raw_wool_cells_and_context_prefix_are_not_conflated(self):
        self.assertEqual(self.receipt["wool_raw_cells"], {
            "wúllō": ["woll"], "wúllǭ": ["wolle"],
            "wullō": ["woll"], "wullǭ": ["wolle"],
        })
        self.assertEqual(self.receipt["you_context_input"], "ᵘízwiz")
        self.assertEqual(self.receipt["you_output"], ["ēow"])
        checks = self.receipt["component_checks"]
        self.assertGreaterEqual(len(checks), 50)
        for prefix in ("", "*ᵘ", "*ᶜ"):
            self.assertIn({
                "component": "PNWGmcILowering", "input": prefix + "*n*í*s*ǭ",
                "outputs": [prefix + "*n*é*s*ǭ"],
            }, checks)
            self.assertIn({
                "component": "PNWGmcULowering", "input": prefix + "*w*ú*l*l*ų",
                "outputs": [prefix + "*w*ú*l*l*ų"],
            }, checks)
        self.assertIn({"component": "EnglishProtoInput", "input": "wúllôz", "outputs": []},
                      checks)

    def test_consumer_audit_is_complete_and_not_a_second_cascade(self):
        adopted_source = subprocess.check_output(
            ["git", "show",
             "dcafc62590c9b4cb71328207aab70d153dc6f88e:Germanic/fsts/germanic.txt"],
            cwd=ROOT,
            text=True,
        )
        self.assertEqual(self.receipt["class_consumers"], consumer_audit(adopted_source))
        self.assertIn("PNWGmcILowering", self.receipt["class_consumers"]["EnglishStarNonHighVowel"])
        self.assertIn("EAFFinalZDeletion", self.receipt["class_consumers"]["PGmcStarVowel"])
        self.assertIn("OEHighVowelApocope", self.receipt["class_consumers"]["EnglishStarLongVowel"])

    def test_current_consumers_preserve_lowering_and_distinct_vowel_domains(self):
        consumers = consumer_audit(self.source)
        for name in ("PNWGmcILowering", "PNWGmcULowering"):
            self.assertIn(name, consumers["EnglishStarNonHighVowel"])
        self.assertIn("EAFFinalZDeletion", consumers["PGmcStarVowel"])
        self.assertIn("OEHighVowelApocope", consumers["EnglishStarLongVowel"])
        self.assertNotIn("{*ǭ}", self.definitions["PNWGmcFinalLongORaising"].body)
        self.assertNotIn("{*ô}", self.definitions["PGmcStarVowel"].body)


if __name__ == "__main__":
    unittest.main()

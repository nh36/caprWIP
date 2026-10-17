"""Focused SC112 adoption and corpus-expansion checks."""

import csv
import io
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GERMANIC = ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
CORPUS = GERMANIC / "data" / "germanic-aligned-final.tsv"
BASELINE = GERMANIC / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs.tsv"
PREVIOUS = GERMANIC / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs_pre_sc112_expansion.tsv"
LEGACY = GERMANIC / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs_legacy380.tsv"


def rows(path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


class Sc112Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.current = {r["row_id"]: r for r in rows(BASELINE)}
        cls.previous = {r["row_id"]: r for r in rows(PREVIOUS)}
        cls.corpus = {r["ID"]: r for r in rows(CORPUS)}

    def test_general_rule_precedes_rhotacism(self):
        self.assertLess(
            self.text.index("PNWGmcMonosyllabicFinalRLengthening"),
            self.text.index("define EAFRhotacism"),
        )
        body = re.search(
            r"define PNWGmcMonosyllabicFinalRLengthening \[(.*?)\n\];",
            self.text,
            re.S,
        ).group(1)
        self.assertIn("EnglishStarConsonant* _ {*r} .#.", body)
        self.assertNotIn("concept", body)

    def test_new_rows_and_targets(self):
        self.assertEqual(
            {
                row_id: (self.corpus[row_id]["PROTOFORM"], self.corpus[row_id]["COUNTERPART"])
                for row_id in ("2333", "2334")
            },
            {"2333": ("*θár", "þǣr"), "2334": ("*xwár", "hwǣr")},
        )
        self.assertEqual(self.current["2333"]["outputs"], "þǣr")
        self.assertEqual(self.current["2334"]["outputs"], "hwǣr")

    def test_expansion_preserves_original_population(self):
        self.assertEqual(len(self.previous), 387)
        self.assertEqual(len(self.current), 389)
        self.assertEqual(set(self.previous), set(self.current) - {"2333", "2334"})
        self.assertEqual(
            [(row_id, self.previous[row_id]["outputs"], self.current[row_id]["outputs"])
             for row_id in self.previous
             if self.previous[row_id]["outputs"] != self.current[row_id]["outputs"]],
            [],
        )
        self.assertEqual(len(rows(LEGACY)), 380)

    def test_exact_counts_and_known_mismatch_membership(self):
        self.assertEqual(sum(r["match"] == "1" for r in self.current.values()), 381)
        self.assertEqual(sum(r["match"] == "0" for r in self.current.values()), 8)
        self.assertEqual(
            {r["row_id"] for r in self.current.values() if r["match"] == "0"},
            {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"},
        )


if __name__ == "__main__":
    unittest.main()

"""Focused SC112 adoption and corpus-expansion checks."""

import csv
import io
import re
import sys
import unittest
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GERMANIC = ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
CORPUS = GERMANIC / "data" / "germanic-aligned-final.tsv"
BASELINE = GERMANIC / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs.tsv"
PREVIOUS = GERMANIC / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs_pre_sc112_expansion.tsv"
LEGACY = GERMANIC / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs_legacy380.tsv"
sys.path.insert(0, str(GERMANIC / "tools"))
import pytest
import oe_pipeline
from capr_runtime import check_build_manifest, layout, run_in_runner


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

    def test_live_sc015_definition_remains_the_adopted_rule(self):
        body = re.search(
            r"define PNWGmcILowering .*?\[(.*?)\n\]\);", self.text, re.S
        ).group(1)
        normalized = re.sub(r"\s+", "", body)
        expected = re.sub(r"\s+", "", """
    {*i} -> {*e} ||
        .#. EnglishStarConsonant* _
        [{*z} [EnglishStarConsonant | .#.]
         | {*s} {*t}
         | {*r}],
    {*í} -> {*é} ||
        .#. EnglishStarConsonant* _
        [{*z} [EnglishStarConsonant | .#.]
         | {*s} {*t}
         | {*r}]
""")
        self.assertEqual(normalized, expected)

    def test_executable_manifest_order_and_inventory_census(self):
        manifest = rows(
            GERMANIC / "docs/sound_changes/cascade_baseline/cascade_order_manifest.tsv"
        )
        positions = {row["foma_identifier"]: int(row["position"]) for row in manifest}
        self.assertEqual(
            positions["PNWGmcMonosyllabicFinalRLengthening"] + 1,
            positions["EAFRhotacism"],
        )
        census_lines = [
            line for line in (
                GERMANIC / "docs/sound_changes/cascade_baseline/rule_coverage_census.tsv"
            ).read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("#")
        ]
        census = next(
            row for row in csv.DictReader(census_lines, delimiter="\t")
            if row["sc_id"] == "SC112"
        )
        self.assertEqual(census["foma_identifier"], "PNWGmcMonosyllabicFinalRLengthening")
        self.assertEqual(census["corpus_firing_count"], "2")
        self.assertEqual(census["lexical_witnesses"], "there, where")

    @pytest.mark.runtime
    def test_production_transducer_executes_current_population_and_controls(self):
        self.assertEqual(check_build_manifest(
            oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], layout()
        ), [])
        inputs = [row["fst_input"] for row in self.current.values()]
        result = run_in_runner(
            "flookup -i old_english.bin",
            input="\n".join(inputs) + "\n",
            text=True,
            capture_output=True,
            check=True,
            timeout=120,
        )
        outputs = {}
        for line in result.stdout.splitlines():
            if not line.strip():
                continue
            source, output = line.split("\t", 1)
            outputs.setdefault(source, []).append(output)
        self.assertEqual(len(outputs), 389)
        self.assertTrue(
            all(len(set(values)) == 1 and values[0] != "+?" for values in outputs.values())
        )
        self.assertEqual(outputs["θár"], ["þǣr"])
        self.assertEqual(outputs["xwár"], ["hwǣr"])
        self.assertEqual(
            {row_id: outputs[row["fst_input"]][0] for row_id, row in self.current.items()},
            {row_id: row["outputs"] for row_id, row in self.current.items()},
        )
        controls = run_in_runner(
            "flookup -i old_english.bin",
            input="θárą\nbázą\ndúrą\n",
            text=True,
            capture_output=True,
            check=True,
            timeout=30,
        )
        control_outputs = {
            source: output
            for line in controls.stdout.splitlines()
            if line.strip()
            for source, output in [line.split("\t", 1)]
        }
        self.assertEqual(control_outputs, {"θárą": "þær", "bázą": "bær", "dúrą": "dor"})

    def test_original_population_preserves_approved_identity_context_and_outputs(self):
        fields = ("concept", "proto", "proto_norm", "fst_input", "word_stress",
                  "phonological_finality", "counterpart", "outputs")
        for row_id, previous in self.previous.items():
            with self.subTest(row_id=row_id):
                if row_id == "2302":
                    previous = dict(previous, proto="*wír-àldiz",
                                    proto_norm="wír-àldiz", fst_input="wír-àldiz")
                self.assertEqual(
                    tuple(self.current[row_id][field] for field in fields),
                    tuple(previous[field] for field in fields),
                )

    def test_experimental_early_condition_matches_production_relevant_semantics(self):
        path = (
            GERMANIC / "docs/sound_changes/audits/"
            "sc015-r-adverb-lengthening-investigation/followup_experiment.py"
        )
        spec = importlib.util.spec_from_file_location("sc112_experiment", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        experimental = module.lengthening_expression()
        for source, target in (("á", "ā"), ("é", "ē"), ("í", "ī"),
                               ("ó", "ō"), ("ú", "ū")):
            self.assertIn(f"{{*{source}}} -> {{*{target}}}", experimental)
        self.assertIn("EnglishStarConsonant* _ {*r} .#.", experimental)
        self.assertIn("EnglishStarConsonant* _ {*r} .#.", self.text)
        self.assertNotIn("{*æ} -> {*ǣ}", experimental)

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

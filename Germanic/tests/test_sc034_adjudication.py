"""SC034's complete population and protected current-model diagnostics."""

from __future__ import annotations

import hashlib
import csv
import json
import subprocess
import sys
import unittest
from pathlib import Path

from test_sc032_adjudication import trace_records

ROOT = Path(__file__).resolve().parents[2]
GERMANIC = ROOT / "Germanic"
sys.path.insert(0, str(GERMANIC / "tools"))

from anglo_frisian_experiments import load_recipes  # noqa: E402
from generate_registry_views import read_tsv  # noqa: E402
from oe_full_trace_report import trace_provenance_problems  # noqa: E402

SC = GERMANIC / "docs/sound_changes"
RESEARCH_COMMIT = "812cc437ea467296a056c04618fa792df2e2c139"
EXPECTED = {
    "2186": ("*s*k*á*w*ō*j*a*n*ą", "*s*k*ḗa*w*ō*j*a*n*ą"),
    "2317": ("*s*k*á*w*ô", "*s*k*ḗa*w*ô"),
    "2318": ("*s*k*á*w*ō*θ", "*s*k*ḗa*w*ō*θ"),
}


class SC034AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = trace_records()

    def test_fresh_complete_trace_and_all_three_actual_applications(self):
        trace = (GERMANIC / "docs/debug_snapshots/oe_full_trace_report.txt").read_text(
            encoding="utf-8"
        )
        self.assertEqual(trace_provenance_problems(trace), [])
        self.assertEqual(len(self.records), 390)
        self.assertEqual({"2333", "2334"} <= set(self.records), True)
        for identifier in ("2333", "2334"):
            forms = self.records[identifier][2]
            self.assertEqual(forms["OEDiphthongLeveling"], forms["OEAwLongDiphthong"])
        actual = {}
        for identifier, (_, _, forms) in self.records.items():
            before = forms["OEDiphthongLeveling"]
            after = forms["OEAwLongDiphthong"]
            if before != after:
                actual[identifier] = before, after
        self.assertEqual(actual, EXPECTED)

    def test_dew_and_hew_have_already_completed_the_inherited_geminate_path(self):
        for identifier, reanalysis, realization in (
            ("1989", "*d*áu*w*ō", "*d*ēa*w*u"),
            ("2074", "*x*áu*w*a*n*ą", "*x*ēa*w*a*n*ą"),
        ):
            with self.subTest(row=identifier):
                forms = self.records[identifier][2]
                self.assertEqual(forms["OEWWSimplification"], reanalysis)
                self.assertEqual(forms["OEDiphthongLeveling"], realization)
                self.assertEqual(forms["OEAwLongDiphthong"], realization)

    def test_straws_regular_branch_retains_attested_target_as_mismatch(self):
        forms = self.records["2224"][2]
        self.assertEqual(forms["PWGmcEndinglessAw"], "*s*t*r*áu")
        self.assertEqual(forms["OEAuBrightening"], "*s*t*r*áeu")
        self.assertEqual(forms["OEDiphthongLeveling"], "*s*t*r*ēa")
        self.assertEqual(forms["OEAwLongDiphthong"], "*s*t*r*ēa")
        self.assertEqual(forms["OEHeavySyllableNasalApocope"], "*s*t*r*ēa")
        with (SC / "cascade_baseline/cascade_baseline_outputs.tsv").open() as handle:
            row = next(row for row in csv.DictReader(handle, delimiter="\t")
                       if row["row_id"] == "2224")
        self.assertEqual((row["proto"], row["counterpart"], row["outputs"], row["match"]),
                         ("*stráwą", "strēaw", "strēa", "0"))

    def test_historical_recipes_preserve_source_pins_and_real_identity_relations(self):
        data = load_recipes(
            SC / "literature_dossiers/anglo_frisian/oe_sc034_controls.json"
        )
        released = load_recipes(
            SC / "literature_dossiers/anglo_frisian/oe_post_hue_controls.json"
        )
        for field in ("baseline_fst_sha256", "baseline_corpus_sha256"):
            self.assertEqual(data[field], released[field])
        for field, path in (
            ("baseline_context_sha256", GERMANIC / "data/entry_context_metadata.tsv"),
            ("baseline_context_helper_sha256", ROOT / "backend/oe_input_context.py"),
        ):
            with self.subTest(field=field):
                content = subprocess.check_output(
                    ["git", "show", f"{RESEARCH_COMMIT}:{path.relative_to(ROOT).as_posix()}"],
                    cwd=ROOT,
                )
                self.assertEqual(data[field], hashlib.sha256(content).hexdigest())
        recipes = {recipe["id"]: recipe for recipe in data["recipes"]}
        self.assertEqual(set(recipes), {
            "identity", "sc034-skip", "sc034-after-nasal-apocope",
            "sc047-before-sc034", "sc034-straw-regular-spans",
            "sc034-straw-regular-nominative",
        })
        for identifier in ("sc034-skip", "sc034-after-nasal-apocope"):
            self.assertIn("define AF034Skip [?*];", recipes[identifier]["definitions"])
            self.assertEqual(recipes[identifier]["replace"],
                             {"OEAwLongDiphthong": "AF034Skip"})
            self.assertNotIn("input_overrides", recipes[identifier])
        self.assertEqual(recipes["sc034-after-nasal-apocope"]["insert_after"],
                         "OEHeavySyllableNasalApocope")
        self.assertEqual(recipes["sc047-before-sc034"]["replace"],
                         {"OEHeavySyllableNasalApocope": "AF047Skip"})
        self.assertIn("define AF047Skip [?*];",
                      recipes["sc047-before-sc034"]["definitions"])

    def test_straw_tail_diagnostics_distinguish_regular_and_levelled_states(self):
        data = load_recipes(
            SC / "literature_dossiers/anglo_frisian/oe_sc034_controls.json"
        )
        recipe = next(
            item for item in data["recipes"]
            if item["id"] == "sc034-straw-regular-spans"
        )
        self.assertEqual(recipe["replace"], {})
        self.assertNotIn("input_overrides", recipe)
        checks = recipe["staged_checks"]
        self.assertEqual(
            [(item["input"], item["expected"]) for item in checks],
            [("*s*t*r*ḗa", "strēa"), ("*s*t*r*ḗa*w", "strēaw")],
        )
        for item in checks:
            self.assertEqual(item["stage"], "OEAwLongDiphthong")
            self.assertEqual(item["side"], "after")
        self.assertIn("not PGmc", checks[1]["evidence"])

    def test_registry_and_technical_boundary_do_not_invent_historical_order(self):
        rows = {row["sc_id"]: row for row in read_tsv(SC / "registry/sc_registry.tsv")}
        for identifier in ("SC034", "SC111"):
            self.assertEqual(rows[identifier]["entry_type"], "support_stage")
            for field in ("hist_stage", "hist_scope", "confidence"):
                self.assertEqual(rows[identifier][field], "")
        self.assertEqual(rows["SC034"]["verdict"], "REFORMULATE/DEFER")
        self.assertEqual((rows["SC111"]["include_in_volume"], rows["SC111"]["is_reader_facing"]),
                         ("yes", "yes"))
        self.assertEqual(rows["SC111"]["source_reader_facing_file"],
                         "111-endingless-aw-fragment.md")
        edge = next(row for row in read_tsv(SC / "registry/chronology_edges.tsv")
                    if (row["source_change_id"], row["target_change_id"])
                    == ("SC047", "SC034"))
        self.assertEqual((edge["relation_type"], edge["evidence_basis"]),
                         ("technical_computational", "technical"))

    def test_historical_post_sc034_assay_preserves_all_finals_and_eight_mismatches(self):
        directory = SC / "literature_dossiers/anglo_frisian"
        data = load_recipes(directory / "oe_post_sc034_controls.json")
        recipe = next(row for row in data["recipes"] if row["id"] == "post-sc034-controls")
        report = json.loads((directory / "oe_post_sc034_result.json").read_text())
        self.assertEqual(report["recipe"], recipe)
        self.assertEqual(report["selected_rows"], 387)
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        for field in ("changed_ids", "input_changed_ids", "missing_output_ids",
                      "ambiguous_output_ids"):
            self.assertEqual(report[field], [])
        self.assertEqual(report["variant_mismatch_ids"],
                         ["1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"])
        self.assertEqual(len(report["checked_component_fixtures"]), 5)
        self.assertEqual(len(report["checked_staged_fixtures"]), 9)
        for field, path in (
            ("baseline_fst_sha256", GERMANIC / "fsts/germanic.txt"),
            ("baseline_corpus_sha256", GERMANIC / "data/germanic-aligned-final.tsv"),
            ("baseline_context_sha256", GERMANIC / "data/entry_context_metadata.tsv"),
            ("baseline_context_helper_sha256", ROOT / "backend/oe_input_context.py"),
        ):
            revision = "757e36e0" if field == "baseline_corpus_sha256" else RESEARCH_COMMIT
            content = subprocess.check_output(
                ["git", "show", f"{revision}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT)
            self.assertEqual(data[field], hashlib.sha256(content).hexdigest())
            captured = [checksum for name, checksum in report["canonical_protected_hashes"].items()
                        if name.endswith("/" + path.name)]
            self.assertEqual(captured, [data[field]])
        with (SC / "cascade_baseline/cascade_baseline_outputs_pre_sc017_rust_input.tsv").open() as handle:
            expected = {row["row_id"]: row["outputs"].split("|")
                        for row in csv.DictReader(handle, delimiter="\t")}
        self.assertEqual({row["id"]: row["variant_outputs"] for row in report["rows"]}, expected)


if __name__ == "__main__":
    unittest.main()

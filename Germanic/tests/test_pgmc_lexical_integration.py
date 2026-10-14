from __future__ import annotations

import copy
import csv
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / "Germanic/docs/sound_changes/reader_facing"))

import pgmc_lexical_integration as integration
import check_reader_facing_citations as citations


class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.crosswalk, cls.inventory, cls.stats = integration.build()
        cls.rows = {r["row_id"]: r for r in cls.crosswalk}
        cls.editorial = {r["row_id"]: r for r in cls.inventory}
        cls.cases = integration.table(ROOT / integration.DIRECTORY / "editorial_cases.tsv")

    def test_population_counts_and_unique_ids(self):
        self.assertEqual(len(self.rows), 393)
        self.assertEqual(len(self.editorial), 393)
        for key, value in {"legacy": 380, "selected": 387, "audit": 393,
                           "assembled": 164, "production_pilots": 11,
                           "format_tests": 1, "reviewed_rows": 13, "scoped_cases": 16}.items():
            with self.subTest(key=key):
                self.assertEqual(self.stats[key], value)
        required = {row["row_id"] for row in self.crosswalk if row["old_policy_requires_report"]}
        legacy_required = {identifier for identifier in required
                           if self.rows[identifier]["legacy380"]}
        self.assertIn("2224", legacy_required)
        self.assertEqual(len(required - {"2224"}), 157)
        self.assertEqual(len(legacy_required - {"2224"}), 150)
        self.assertEqual(self.stats["required"], len(required))
        self.assertEqual(self.stats["legacy_current_required"], len(legacy_required))

    def test_added_witnesses_and_research_only(self):
        self.assertEqual(self.stats["added_selected"],
                         ["2322", "2326", "2327", "2328", "2329", "2330", "2332"])
        self.assertEqual(self.stats["research_only"],
                         ["1935", "1947", "1948", "1994", "2156", "2218"])
        for row_id in self.stats["research_only"]:
            self.assertEqual(self.rows[row_id]["target"], "-")
            self.assertEqual(self.rows[row_id]["old_policy_requires_report"], 0)
        for row_id in map(str, range(2309, 2319)):
            self.assertEqual(self.rows[row_id]["legacy380"], 1)

    def test_real_assembly_differences(self):
        self.assertEqual(self.stats["required_not_assembled"],
                         ["2055", "2120", "2327", "2328", "2329"])
        self.assertEqual(self.stats["assembled_not_required"],
                         ["1933", "1955", "1989", "2018", "2029", "2044", "2074",
                          "2113", "2185", "2200", "2283"])
        self.assertIn("/2055-", self.rows["2055"]["stable_id_material_paths"])
        self.assertNotIn("/2055-", self.rows["2054"]["stable_id_material_paths"])

    def test_selected_forms_cells_and_context(self):
        expected = {
            "1933": ("*nḗdrōn", "*nḗdrōn", "nǣdre", "regular", "nǣdre"),
            "2013": ("*fūri", "*fūri", "fȳre", "known_unmodelled", "fȳr"),
            "2085": ("*knéwą", "*knéwai", "cneowe", "late_analogy", "cneowe"),
            "2162": ("*rústaz", "*rústaz", "rust", "unexplained_unmodelled", "rost"),
            "2224": ("*stráwą", "*stráwą", "strēaw", "late_analogy", "strēa"),
            "2283": ("*wéθruz", "*wéθruz", "weþer", "regular", "weþer"),
            "2326": ("*ízwiz", "*ízwiz", "ēow", "regular", "ēow"),
            "2330": ("*θánxtē", "*θánxtē", "þōhte", "regular", "þōhte"),
            "2332": ("*xíwją", "*xíwją", "hīew", "regular", "hīew"),
        }
        for row_id, values in expected.items():
            with self.subTest(row_id=row_id):
                row = self.rows[row_id]
                self.assertEqual(tuple(row[k] for k in (
                    "proto", "protoform", "target", "derivation_class", "documented_outputs")), values)
                self.assertEqual(row["proto_stage"], "pgmc")
                self.assertTrue(row["input_stage"])
                self.assertEqual(row["input_variety"], "")
        self.assertNotEqual(self.rows["2326"]["word_stress"], "unknown")
        self.assertNotEqual(self.rows["2326"]["phonological_finality"], "unknown")

    def test_archived_research_links_remain_discoverable_by_stable_id(self):
        for row in self.crosswalk:
            for name in row["stable_id_material_paths"].split(";"):
                if name:
                    self.assertTrue((ROOT / name).is_file(), name)
        adder = self.rows["1933"]["stable_id_material_paths"]
        self.assertIn("/archive/dev_notes_slices/1933-", adder)
        self.assertIn(".source_ledger.md", adder)
        packets = sorted((ROOT / "Germanic/docs/lexeme_reports/archive/packets").glob("[0-9]*.md"))
        self.assertTrue(packets)
        for path in packets:
            row = self.rows[path.name.split("-")[0]]
            self.assertIn(str(path.relative_to(ROOT)), row["stable_id_material_paths"])

    def test_inventory_is_not_a_controversy_census(self):
        self.assertEqual(self.stats["routes"], {
            "candidate_comparison_review": 1, "focused_comparison_review": 91,
            "ordinary_evidence_review": 293, "unit_comparability_review": 8})
        unreviewed = [r for r in self.inventory if r["editorial_review"] == "not_editorially_reviewed"]
        self.assertEqual(len(unreviewed), 380)
        self.assertTrue(all(not r["reviewed_categories"] for r in unreviewed))
        self.assertEqual(self.editorial["2085"]["reviewed_categories"],
                         "non_substantive_difference;qualified_alternative")
        self.assertEqual(self.editorial["1937"]["reviewed_categories"],
                         "no_special_discussion;non_substantive_difference")
        self.assertEqual(self.editorial["2162"]["reviewed_categories"], "qualified_alternative")
        self.assertTrue(all(r["audit_alignment"] == "bounded_limit" for r in self.crosswalk))

    def test_screen_ignores_alignment_types_and_output(self):
        ordinary = {"scope": "core_triage", "comparability": "undetermined",
                    "alignment_status": "bounded_limit", "type_tags": "quantity;vocalism",
                    "outputs": "wrong"}
        self.assertEqual(integration.screen([ordinary]), "ordinary_evidence_review")
        ordinary.update(type_tags="", outputs="right", alignment_status="unreviewed")
        self.assertEqual(integration.screen([ordinary]), "ordinary_evidence_review")
        ordinary["comparability"] = "different_units"
        self.assertEqual(integration.screen([ordinary]), "unit_comparability_review")
        ordinary["comparability"] = "substantive_difference"
        self.assertEqual(integration.screen([ordinary]), "candidate_comparison_review")
        ordinary["scope"] = "focused"
        self.assertEqual(integration.screen([ordinary]), "focused_comparison_review")

    def test_duplicate_and_empty_ids_fail_closed(self):
        for records in ([{"id": "1"}, {"id": "1"}], [{"id": ""}]):
            with self.assertRaisesRegex(ValueError, "empty or duplicate"):
                integration.unique(records, "id", "fixture")

    def check_case_fixture(self, changes, corpus=None, forms=None):
        case = copy.deepcopy(next(c for c in self.cases if c["case_id"] == "adder-feminine-vocalism"))
        case["example_path"] = ""
        case["requires_extended_discussion"] = "0"
        case["publication_source"] = ""
        case.update(changes)
        evidence_id = case["evidence_ids"].split(";")[0]
        case["evidence_ids"] = evidence_id
        corpus = corpus if corpus is not None else {case["row_id"]: {}}
        forms = forms if forms is not None else {
            evidence_id: {"row_ids": case["row_id"], "printed_pages": "286", "source_key": "Orel2003"}}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / integration.DIRECTORY
            directory.mkdir(parents=True)
            (directory / "editorial_cases.tsv").write_text(
                integration.tsv([case], integration.CASE_FIELDS), encoding="utf-8")
            return integration.load_cases(root, corpus, forms)

    def test_wrong_row_missing_page_and_missing_premise_refused(self):
        case = next(c for c in self.cases if c["case_id"] == "adder-feminine-vocalism")
        evidence_id = case["evidence_ids"].split(";")[0]
        with self.assertRaisesRegex(ValueError, "wrong-row"):
            self.check_case_fixture({}, forms={evidence_id: {
                "row_ids": "2085", "printed_pages": "286", "source_key": "Orel2003"}})
        with self.assertRaisesRegex(ValueError, "missing source/page"):
            self.check_case_fixture({}, forms={evidence_id: {
                "row_ids": "1933", "printed_pages": "", "source_key": "Orel2003"}})
        with self.assertRaisesRegex(ValueError, "missing premise"):
            self.check_case_fixture({"missing_premise": ""})
        with self.assertRaisesRegex(ValueError, "uncited"):
            self.check_case_fixture({"evidence_ids": ""})

    def test_provisional_paths_cannot_escape(self):
        with self.assertRaisesRegex(ValueError, "unsafe"):
            self.check_case_fixture({"example_path": "../production.md"})

    def test_publication_requires_explicit_scoped_and_safe_decision(self):
        with self.assertRaisesRegex(ValueError, "explicit editorial decision"):
            self.check_case_fixture({"requires_extended_discussion": ""})
        with self.assertRaisesRegex(ValueError, "unsafe or wrong-row"):
            self.check_case_fixture({"requires_extended_discussion": "1",
                                     "publication_source": "../other.md"})
        with self.assertRaisesRegex(ValueError, "non-substantive"):
            self.check_case_fixture({"requires_extended_discussion": "1",
                                     "category": "no_special_discussion"})
        with self.assertRaisesRegex(ValueError, "unselected case"):
            self.check_case_fixture({"publication_source": "model_entries/1933-adder.model.md"})

    def test_six_examples_not_promoted_to_manifest(self):
        examples = sorted((ROOT / integration.DIRECTORY / "examples").glob("*.md"))
        self.assertEqual({p.name.split("-")[0] for p in examples},
                         {"1933", "2013", "2085", "2326", "2330", "2332"})
        for name in ("Germanic/docs/lexeme_reports/report_manifest.tsv",
                     "Germanic/docs/assembly/manifest_all_by_class.tsv"):
            self.assertNotIn("pgmc_integration", (ROOT / name).read_text())

    def test_every_prose_citation_has_key_and_checked_printed_pages(self):
        allowed = {
            "Orel2003": {42, 171, 172, 286},
            "Kroonen2013": {60, 151, 224, 275, 276, 381, 386},
            "Fulk2018": {55, 57, 58, 59, 71, 72, 126, 132, 147, 153, 154,
                         187, 188, 299, 300, 301},
            "Ringe2017": {147, 151, 152, 153, 233, 234, 235, 281, 309},
            "RingeTaylor2014": {41, 42, 55, 57, 58, 71, 72, 73, 74, 75,
                               97, 98, 99, 119, 141, 142, 143, 171, 172, 173,
                               174, 175, 187, 188, 225, 250, 387},
            "HoggGrammar2011": {21, 22, 86}, "Campbell1959": {46, 232, 233, 283},
            "Luick1914": {139}, "Toller1921": {276},
        }
        keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", (ROOT / "docs/refs.bib").read_text()))
        count = 0
        for path in sorted((ROOT / integration.DIRECTORY / "examples").glob("*.md")):
            self.assertEqual(citations.scan_file(path, set()), [], path.name)
            for block in citations.CITATION_BLOCK_RE.finditer(path.read_text()):
                for item in citations.split_citations(block.group(1)):
                    key = citations.KEY_RE.search(item if item.startswith("@") else "@" + item).group(1)
                    self.assertIn(key, keys)
                    self.assertIn(key, allowed)
                    locator = re.search(r"\bpp?\.\s*(.+)", item).group(1)
                    for token in locator.split(","):
                        endpoints = [int(n) for n in re.findall(r"\d+", token)]
                        self.assertTrue(endpoints)
                        pages = set(range(endpoints[0], endpoints[-1] + 1))
                        self.assertLessEqual(pages, allowed[key], (path.name, item))
                    count += 1
        self.assertGreaterEqual(count, 30)

    def test_rejected_and_component_attributions_remain_explicit(self):
        directory = ROOT / integration.DIRECTORY / "examples"
        fire = (directory / "2013-fire.md").read_text()
        self.assertIn("he rejects", fire)
        self.assertIn("[@Toller1921, p. 276]", fire)
        self.assertNotIn("@BosworthToller1898", fire)
        thought = (directory / "2330-thought.md").read_text()
        self.assertIn("counterfactual buy", thought)
        self.assertIn("not the noun", thought)
        self.assertIn("CAPR's paradigm construction", (directory / "2085-knee.md").read_text())
        self.assertIn("not a verbatim", (directory / "2085-knee.md").read_text())

    def test_deterministic_projection(self):
        first = integration.render()
        self.assertEqual(first, integration.render())
        self.assertEqual({p.name for p in first}, set(integration.OUTPUT_NAMES))
        rows = list(csv.DictReader(first[ROOT / integration.DIRECTORY / "population_crosswalk.tsv"]
                                   .splitlines(), delimiter="\t"))
        self.assertEqual(len(rows), 393)
        self.assertEqual(len({r["row_id"] for r in rows}), 393)

    def test_graph_integration_follows_lexical_assembly(self):
        import artifact_graph
        nodes = artifact_graph.nodes()
        names = [n.name for n in nodes]
        self.assertLess(names.index("lexical_sources"), names.index("pgmc_lexical_integration"))
        self.assertLess(names.index("pgmc_lexical_integration"), names.index("book_draft"))


if __name__ == "__main__":
    unittest.main()

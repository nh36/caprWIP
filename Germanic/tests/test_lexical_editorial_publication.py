from __future__ import annotations

import copy
import csv
from collections import Counter
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / "Germanic/docs/assembly"))

import oe_derivation_report_with_lexeme_reports as assembly
import oe_lexeme_report_coverage as coverage
import pgmc_lexical_integration as editorial
from build_full_lexical_volume import parse_model_entry
from validate_oe_lexeme_report_assembly import parse_entries

BASE = "b74e3ce3f60f05c8843555eb409b35020386dcf0"
REPORTS = ROOT / "Germanic/docs/lexeme_reports"
SNAPSHOTS = ROOT / "Germanic/docs/debug_snapshots"
PRINCIPAL = {"1933", "2013", "2085", "2326", "2330", "2332"}


def committed(path: Path) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BASE}:{path.relative_to(ROOT)}"], cwd=ROOT, text=True)


class EditorialPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = coverage.load_oe_rows(ROOT / "Germanic/data/germanic-aligned-final.tsv")
        entries = coverage.load_manifest(REPORTS / "report_manifest.tsv")
        diagnostics, _ = coverage.apply_manifest(
            cls.rows, entries, REPORTS, coverage.load_report_files(REPORTS))
        assert not diagnostics, diagnostics
        cls.old_required = {r.row_id for r in cls.rows if r.requires_report}
        coverage.apply_editorial_selection(cls.rows, REPORTS)
        cls.by_id = {r.row_id: r for r in cls.rows}
        cls.report_map = assembly.add_editorial_reports(
            assembly.build_production_report_map(entries, REPORTS), cls.rows, REPORTS)
        cls.compact = (SNAPSHOTS / "oe_derivation_class_trace_report.compact.md").read_text()
        cls.index = assembly.build_row_index(cls.rows)

    def test_scoped_philology_is_independent_of_derivation_status(self):
        self.assertIn("2224", self.old_required)
        self.assertEqual(len(self.old_required - {"2224"}), 157)
        straw = self.by_id["2224"]
        self.assertEqual(straw.derivation_class, "late_analogy")
        self.assertEqual(straw.editorial_case_ids, ["straw-endingless-and-levelling"])
        self.assertTrue(straw.has_publication_report)
        self.assertFalse(straw.has_production_manifest_report)
        self.assertEqual({r.row_id for r in self.rows if r.editorial_case_ids},
                         PRINCIPAL | {"1934", "1941", "2162", "2224", "2283"})
        beaver = self.by_id["1941"]
        self.assertEqual(beaver.derivation_class, "regular")
        self.assertFalse(beaver.note)
        self.assertTrue(beaver.requires_report)
        self.assertIn("philological=beaver-formation-direction", beaver.requirement_basis)
        self.assertFalse(beaver.has_production_manifest_report)
        self.assertTrue(beaver.has_publication_report)

    def test_publication_graph_node_is_fresh_and_has_one_output_owner(self):
        import artifact_graph

        nodes = [n for n in artifact_graph.nodes() if n.name == "lexeme_publication"]
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].kind, "projection")
        expected = {REPORTS / "coverage_audit.md"} | {
            SNAPSHOTS / ("oe_derivation_class_trace_report.with_lexeme_reports" + suffix)
            for suffix in (".md", ".audit.md", ".publish.md", ".publish.missing_reports.md")
        }
        self.assertEqual(set(nodes[0].outputs()), expected)
        self.assertEqual(nodes[0].verify(), [])
        owners = artifact_graph.declared_outputs()
        for path in expected:
            self.assertEqual([name for name, outputs in owners.items() if path in outputs],
                             ["lexeme_publication"])

    def test_qualified_cases_have_explicit_selected_decisions(self):
        cases = editorial.table(ROOT / editorial.DIRECTORY / "editorial_cases.tsv")
        selected = {c["case_id"] for c in cases if c["requires_extended_discussion"] == "1"}
        self.assertIn("bake-present-formation", selected)
        self.assertIn("knee-ending", selected)
        self.assertNotIn("knee-selected-cell", selected)
        self.assertTrue(all(c["missing_premise"] for c in cases
                            if c["category"] == "qualified_alternative"))

    def test_two_ordinary_controls_do_not_gain_reports(self):
        for row_id in ("1937", "1950"):
            self.assertFalse(self.by_id[row_id].editorial_case_ids)
            self.assertNotIn(row_id, self.report_map)
        selected = assembly.assemble_report(self.compact, self.index, self.report_map, mode="publish")
        entries = parse_entries(selected, self.index)
        for row_id in ("1937", "1950"):
            self.assertNotIn("### Lexeme report", entries[row_id])

    def test_audit_tags_routes_and_outputs_do_not_select_publication(self):
        row = copy.deepcopy(self.by_id["1941"])
        row.editorial_case_ids = []
        row.editorial_report_path = ""
        self.assertFalse(row.requires_report)
        for category in ("bounded_limit", "substantive_difference", "regular"):
            self.assertEqual(editorial.screen([{
                "scope": "core_triage", "comparability": "undetermined",
                "alignment_status": category, "type_tags": category, "outputs": "befer",
            }]), "ordinary_evidence_review")
        self.assertFalse(row.requires_report)

    def test_complete_derivations_are_preserved_byte_for_byte(self):
        before = parse_entries(self.compact, self.index)
        for mode in ("audit", "publish"):
            after = parse_entries(assembly.assemble_report(
                self.compact, self.index, self.report_map, mode=mode), self.index)
            self.assertEqual(set(after), set(before))
            self.assertEqual(len(after), 387)
            for row_id, lines in before.items():
                original = assembly.trim_blank_edges(
                    [line for line in lines if not line.startswith("NOTE:")])
                self.assertEqual(after[row_id][:len(original)], original, (mode, row_id))

    def test_short_source_does_not_require_a_new_model_or_expand_book(self):
        self.assertFalse(list((REPORTS / "model_entries").glob("1941-*.model.md")))
        source = self.by_id["1941"].editorial_report_path
        self.assertEqual(source, "research_memos/1941-beaver-befer.md")
        self.assertIn("opposed derivational directions", "\n".join(self.report_map["1941"]))
        manifest = ROOT / "Germanic/docs/assembly/manifest_all_by_class.tsv"
        current = list(csv.DictReader(manifest.read_text().splitlines(), delimiter="\t"))
        old = list(csv.DictReader(committed(manifest).splitlines(), delimiter="\t"))
        self.assertEqual(len(current), 164)
        added = [r for r in current if r["row_id"] in {"2185", "2200", "2224", "2283"}]
        self.assertEqual({r["row_id"] for r in added}, {"2185", "2200", "2224", "2283"})
        unchanged = [r for r in current if r["row_id"] not in {"2185", "2200", "2224", "2283"}]
        for now, before in zip(unchanged, old, strict=True):
            if before["row_id"] == "2162":
                self.assertEqual((before["proto"], before["protoform"]), ("*rústō", "*rústō"))
                before = dict(before, proto="*rústaz", protoform="*rústaz")
            preceding = [r for r in added
                         if int(r["global_order"]) < int(now["global_order"])]
            self.assertEqual(int(now["global_order"]), int(before["global_order"]) + len(preceding))
            self.assertEqual(int(now["class_order"]), int(before["class_order"])
                             + sum(r["derivation_class"] == now["derivation_class"]
                                   for r in preceding))
            self.assertEqual({k: v for k, v in now.items() if k not in {"global_order", "class_order"}},
                             {k: v for k, v in before.items() if k not in {"global_order", "class_order"}})
        self.assertEqual(sum(r["derivation_class"] == "late_analogy" for r in current), 29)

    def test_superior_knee_and_hue_sections_are_retained(self):
        for row_id in ("2085", "2332"):
            path = REPORTS / self.by_id[row_id].editorial_report_path
            old = committed(path)
            now = path.read_text()
            for paragraph in old.split("\n\n"):
                self.assertIn(paragraph, now, row_id)
            self.assertGreater(len(now.split()), len(old.split()))

    def test_mature_model_sources_keep_live_selected_identity(self):
        for path in (REPORTS / "model_entries").glob("*.model.md"):
            row = self.by_id[path.name.split("-")[0]]
            metadata = parse_model_entry(path)["metadata"]
            for key, value in {"PROTO": row.proto, "PROTOFORM": row.protoform,
                               "COUNTERPART": row.counterpart,
                               "DERIVATION_CLASS": row.derivation_class}.items():
                self.assertEqual(metadata[key], value, path.name)

    def test_source_and_live_identity_mismatches_fail_closed(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r.row_id == "1941").protoform = "*wrong"
        with self.assertRaisesRegex(ValueError, "identity mismatch"):
            assembly.add_editorial_reports({}, rows, REPORTS)

    def test_format_test_is_not_promoted_by_model_certification(self):
        self.assertTrue(self.by_id["1933"].has_format_test_manifest_report)
        self.assertFalse(self.by_id["1933"].has_production_manifest_report)
        self.assertNotIn((REPORTS / "pilot/adder.md").read_text(),
                         "\n".join(self.report_map["1933"]))

    def test_errata_and_distinct_fire_uncertainties_survive(self):
        fire = "\n".join(self.report_map["2013"])
        self.assertIn("@Toller1921, 276", fire)
        self.assertNotIn("@BosworthToller1898", fire)
        self.assertIn("neither passage", fire.lower())
        self.assertIn("interpreted by CAPR", fire)
        adder = "\n".join(self.report_map["1933"])
        self.assertIn("@Fulk2018, 132", adder)
        self.assertIn("not proof", adder)

    def test_source_metadata_and_sc_internal_references_are_retained(self):
        for row_id in PRINCIPAL:
            row = self.by_id[row_id]
            path = REPORTS / row.editorial_report_path
            model = parse_model_entry(path)
            self.assertEqual(model["metadata"]["PROTO"], row.proto)
            self.assertEqual(model["metadata"]["PROTOFORM"], row.protoform)
            old_refs = __import__("re").findall(r"\]\(#rule-[^)]+\)", committed(path))
            for reference in old_refs:
                self.assertIn(reference, path.read_text())
            self.assertNotIn("**", path.read_text())

    def test_you_variety_audit_receipt_tracks_the_unchanged_source_evidence(self):
        path = REPORTS / self.by_id["2326"].editorial_report_path
        rows = editorial.table(ROOT / "Germanic/docs/book/index_verborum_variety_annotation_audit.tsv")
        receipt = next(r for r in rows if "2326-you-" in r["source_ref"])
        line = path.read_text().splitlines()[int(receipt["source_ref"].rsplit(":", 1)[1]) - 1]
        self.assertIn("early West Saxon and Northumbrian", line)
        self.assertIn("īow", line)
        self.assertEqual(receipt["decision"], "not_variety_evidence")

    def test_current_principal_sc_links_resolve_in_assembled_book(self):
        import re

        book = (ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md").read_text()
        for row_id in PRINCIPAL:
            source = (REPORTS / self.by_id[row_id].editorial_report_path).read_text()
            for target in re.findall(r"\]\(#(rule-[^)]+)\)", source):
                self.assertRegex(book, r"\{#" + re.escape(target) + r"(?:\s|\})")

    def test_new_citation_objects_keep_keys_and_printed_page_locators(self):
        import re

        bibliography = (ROOT / "docs/refs.bib").read_text()
        keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", bibliography))
        count = 0
        for row in self.rows:
            if not row.editorial_report_path:
                continue
            path = REPORTS / row.editorial_report_path
            old = "" if row.row_id in {"1941", "2224", "2283"} else committed(path)
            pattern = r"\[[^\]\n]*@[^\]\n]*(?:\n[^\]]*)?\]"
            added = Counter(re.findall(pattern, path.read_text())) - Counter(re.findall(pattern, old))
            for block in added:
                for citation in block[1:-1].split(";"):
                    match = re.search(r"@(\w+)", citation)
                    self.assertIsNotNone(match, block)
                    self.assertIn(match[1], keys)
                    self.assertRegex(citation, r",\s*pp?\.\s*\d+")
                    count += 1
        self.assertGreaterEqual(count, 20)


if __name__ == "__main__":
    unittest.main()

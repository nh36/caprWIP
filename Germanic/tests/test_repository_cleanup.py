"""Permanent archive integrity and recurring lexical acceptance contracts."""

import csv
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / "Germanic/docs/assembly"))

import artifact_graph
import build_class_manifests
import check_repository_cleanup as cleanup
import oe_lexeme_report_coverage as coverage
from check_bibliography_sanity import parse_entries


class CleanupTests(unittest.TestCase):
    def test_archived_records_preserve_original_bytes(self):
        old = cleanup.baseline_blobs()
        pairs = cleanup.archive_pairs()
        self.assertGreaterEqual(len(pairs), 913)
        for source, target in pairs:
            with self.subTest(source=str(source)):
                self.assertEqual(cleanup.blob_id(ROOT / target), old[str(source)])

    def test_all_old_paired_paperwork_is_archived_not_required(self):
        old = cleanup.baseline_blobs()
        for suffix in (".reviewer_checklist.md", ".model_implementation_report.md"):
            sources = [Path(p) for p in old if p.endswith(suffix)]
            self.assertEqual(len(sources), 151)
            for source in sources:
                self.assertFalse((ROOT / source).exists())
                target = cleanup.LEXICAL / "archive" / source.relative_to(cleanup.LEXICAL)
                self.assertEqual(cleanup.blob_id(ROOT / target), old[str(source)])

    def test_drafting_discovery_keeps_history_but_excludes_process_archives(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            names = ("model_entries/1933-adder.model.md",
                     "archive/packets/1933-adder.md",
                     "archive/dev_notes_slices/1933-adder.md",
                     "archive/model_entries/1933-adder.reviewer_checklist.md",
                     "archive/production_backlog.md")
            for name in names:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("historical material\n")
            self.assertEqual(
                {str(p.relative_to(root)) for p in coverage.load_report_files(root)},
                set(names[:3]))

    def test_models_have_live_identity_and_bibliography_keys(self):
        keys = {e.key for e in parse_entries((ROOT / "docs/refs.bib").read_text())}
        with (ROOT / "Germanic/data/germanic-aligned-final.tsv").open() as handle:
            rows = {r["ID"]: r for r in csv.DictReader(handle, delimiter="\t")
                    if r["DOCULECT"] == "Old_English"}
        for path in sorted(build_class_manifests.MODEL_DIR.glob("*.model.md")):
            with self.subTest(model=path.name):
                model = build_class_manifests.parse_model_entry(path)
                self.assertFalse(model["missing_metadata"])
                self.assertIn(model["class_bucket"], build_class_manifests.CLASS_CONFIG)
                row = rows[str(model["row_id"])]
                for field in build_class_manifests.REQUIRED_METADATA:
                    self.assertEqual(model["metadata"][field], row[field])
                cited = set(re.findall(r"@([A-Za-z][A-Za-z0-9]*)", path.read_text()))
                self.assertTrue(cited, "model must cite its scholarly sources")
                self.assertFalse(cited - keys, f"unknown bibliography keys: {cited - keys}")

    def test_graph_inventory_uses_existing_output_declarations(self):
        node = artifact_graph.Node(
            "fixture", "projection", "source fixture",
            lambda: self.fail("inventory must not verify"),
            lambda: self.fail("inventory must not build"),
            lambda: [ROOT / "fixture.md"])
        with patch.object(artifact_graph, "nodes", return_value=(node,)):
            self.assertEqual(artifact_graph.inventory(), [{
                "name": "fixture", "kind": "projection", "authority": "source fixture",
                "outputs": ["fixture.md"]}])


if __name__ == "__main__":
    unittest.main()

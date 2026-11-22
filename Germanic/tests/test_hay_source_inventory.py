import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "docs/references/inventory_hay_sources.py"


def load_script():
    spec = importlib.util.spec_from_file_location("inventory_hay_sources", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def write_priority(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, delimiter="\t", fieldnames=fields,
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class HaySourceInventoryTests(unittest.TestCase):
    def test_germanic2_is_not_classified_as_germanic(self):
        module = load_script()
        germanic = Path("/tmp/repo/Downloads/Germanic")
        germanic2 = Path("/tmp/repo/Downloads/Germanic 2")
        candidate = germanic2 / "article.pdf"
        self.assertEqual(
            module.scope_for(candidate, germanic, germanic2),
            "Germanic2",
        )

    def test_refresh_preserves_curated_dispositions(self):
        module = load_script()
        with tempfile.TemporaryDirectory() as dirname:
            existing = Path(dirname) / "inventory.tsv"
            fields = list(module.PRIORITY_FIELDS)
            write_priority(existing, [{
                "source_path": "Downloads/Germanic 2/article.pdf",
                "sha256": "a" * 64,
                "classification": "new scholarly source",
                "priority": "1",
                "ingestion_status": "preserved",
                "extraction_status": "native_complete",
                "missing_material": "none",
                "image_verification_status": "representative_pages",
                "consulted": "no",
                "bibliography_key": "Example2026",
                "next_action": "keep this disposition",
            }], fields)
            raw = [{
                "source_path": "Downloads/Germanic 2/article.pdf",
                "sha256": "a" * 64,
                "classification": "",
                "priority": "to_classify",
                "ingestion_status": "unclassified",
                "extraction_status": "",
                "missing_material": "",
                "image_verification_status": "",
                "consulted": "no",
                "bibliography_key": "",
                "next_action": "",
            }]
            merged = module.merge_inventory(raw, existing)
            row = merged[0]
            self.assertEqual(row["classification"], "new scholarly source")
            self.assertEqual(row["priority"], "1")
            self.assertEqual(row["next_action"], "keep this disposition")

    def test_missing_directory_is_reported_not_fatal_for_inventory(self):
        module = load_script()
        with tempfile.TemporaryDirectory() as dirname:
            repo = Path(dirname)
            germanic = repo / "Downloads/Germanic"
            germanic2 = repo / "Downloads/Germanic 2"
            rows, counts = module.collect_priority(
                germanic, germanic2, repo, {}
            )
            self.assertEqual(rows, [])
            self.assertEqual(counts["missing"], 2)

    def test_checksum_index_is_built_once(self):
        module = load_script()
        with tempfile.TemporaryDirectory() as dirname:
            repo = Path(dirname)
            pdf = repo / "docs/references/example.pdf"
            pdf.parent.mkdir(parents=True)
            pdf.write_bytes(b"sample")
            index = module.canonical_index(repo)
            digest = module.sha256(pdf)
            self.assertEqual(index[digest], ["docs/references/example.pdf"])

    def test_unresolved_priority_is_visible_in_verification(self):
        module = load_script()
        with tempfile.TemporaryDirectory() as dirname:
            root = Path(dirname)
            priority = root / "priority.tsv"
            today = root / "today.tsv"
            write_priority(priority, [{
                "source_path": "Downloads/Germanic 2/x.pdf",
                "original_filename": "x.pdf",
                "sha256": "b" * 64,
                "size": "1",
                "type": "pdf",
                "title": "",
                "author": "",
                "pages": "",
                "native_sample_status": "unavailable",
                "canonical_matches": "",
                "status": "new_external_original_candidate",
                "scope": "Germanic2",
                "priority": "to_classify",
                "consulted": "no",
                "classification": "",
                "ingestion_status": "unclassified",
                "extraction_status": "",
                "missing_material": "",
                "image_verification_status": "",
                "bibliography_key": "",
                "next_action": "",
            }], list(module.PRIORITY_FIELDS))
            write_priority(today, [], list(module.TODAY_FIELDS))
            json_path = root / "inventory.json"
            json_path.write_text(json.dumps({"priority": [], "today": []}))
            errors = module.verify_outputs(priority, today, json_path)
            self.assertTrue(any("unclassified" in error for error in errors))

    def test_run_is_idempotent_for_raw_tsv_and_json(self):
        module = load_script()
        with tempfile.TemporaryDirectory() as dirname:
            root = Path(dirname)
            source = root / "Downloads"
            germanic = source / "Germanic"
            germanic2 = source / "Germanic 2"
            germanic.mkdir(parents=True)
            germanic2.mkdir(parents=True)
            (germanic2 / "a.pdf").write_bytes(b"%PDF fixture")
            repo = root / "repo"
            (repo / "docs/references").mkdir(parents=True)
            index = module.canonical_index(repo)
            first, counts = module.collect_priority(germanic, germanic2, repo, index)
            second, counts2 = module.collect_priority(germanic, germanic2, repo, index)
            self.assertEqual(first, second)
            self.assertEqual(counts, counts2)


if __name__ == "__main__":
    unittest.main()

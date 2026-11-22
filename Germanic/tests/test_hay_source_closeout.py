import csv
import re
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
REF = REPO / "docs/references"


def tsv_rows(path):
    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


class HaySourceCloseoutTests(unittest.TestCase):
    def test_all_priority_candidates_are_resolved(self):
        rows = tsv_rows(REF / "hay-germanic-downloads-comprehensive-2026-11-22.tsv")
        self.assertEqual(len(rows), 113)
        unresolved = [
            row for row in rows
            if (
                row["status"] in ("new_external_original_candidate", "to_classify")
                and not row["classification"]
            )
            or row["priority"] in ("", "to_classify")
        ]
        self.assertEqual(unresolved, [])
        counts = {}
        for row in rows:
            counts[row["scope"]] = counts.get(row["scope"], 0) + 1
        self.assertEqual(counts.get("Germanic", 0), 0)
        self.assertEqual(counts.get("Germanic2"), 113)

    def test_work_ids_are_not_duplicated_in_priority_inventory(self):
        rows = tsv_rows(REF / "hay-article-source-inventory-2026-11-22.tsv")
        keys = [row["key"] for row in rows]
        duplicate_keys = sorted({key for key in keys if keys.count(key) > 1})
        self.assertEqual(set(duplicate_keys), set())
        stiles = [row for row in rows if row["key"] == "Stiles1995"]
        self.assertEqual(len(stiles), 1)

    def test_ill_status_is_explicit_and_goering_bennett_acquired(self):
        rows = tsv_rows(REF / "hay-article-source-inventory-2026-11-22.tsv")
        by_key = {row["key"]: row for row in rows}
        self.assertIn("ILL requested", by_key["Ritt2000"]["status"])
        self.assertIn("ILL requested", by_key["Dal1934"]["status"])
        self.assertEqual(by_key["Goering2025"]["status"], "held_and_extracted")
        self.assertEqual(by_key["Bennett1968"]["status"], "held_and_extracted")

    def test_stiles_and_bennett_maps_have_no_duplicate_printed_pages(self):
        stiles = tsv_rows(REF / "hay-stiles-1995-page-map-2026-11-22.tsv")
        pages = [int(row["printed_page"]) for row in stiles]
        self.assertEqual(pages, list(range(177, 221)))
        bennett = tsv_rows(REF / "hay-sehrt-bennett-page-map-2026-11-22.tsv")
        bpages = [int(row["printed_page"]) for row in bennett]
        self.assertEqual(bpages, list(range(53, 61)))

    def test_goetz_missing_page_does_not_overlap_present_pages(self):
        rows = tsv_rows(REF / "hay-goetz-page-level-2026-11-22.tsv")
        present = {
            int(row["printed_page"]) for row in rows
            if row["status"] == "complete"
        }
        missing = {
            int(row["printed_page"]) for row in rows
            if row["status"] == "missing"
        }
        self.assertEqual(present & missing, set())
        self.assertIn(121, missing)

    def test_goetz_declares_the_available_contiguous_tranches(self):
        rows = tsv_rows(REF / "hay-goetz-page-level-2026-11-22.tsv")
        present = {
            int(row["printed_page"]) for row in rows
            if row["status"] == "complete"
        }
        self.assertTrue(set(range(51, 69)).issubset(present))
        self.assertTrue(set(range(69, 88)).issubset(present))
        self.assertTrue(set(range(88, 108)).issubset(present))
        self.assertTrue(set(range(108, 121)).issubset(present))
        self.assertTrue(set(range(122, 127)).issubset(present))

    def test_bibliography_keys_are_unique_and_hay_keys_resolve(self):
        text = (REPO / "docs/refs.bib").read_text(encoding="utf-8")
        keys = re.findall(r"@\w+\{([^,\n]+)", text)
        duplicate_keys = sorted({key for key in keys if keys.count(key) > 1})
        self.assertEqual(duplicate_keys, [])
        for key in ("Jones1989", "Minkova2014", "Mokrowiecki2015",
                    "Goering2025", "Bennett1968", "Stiles1995",
                    "Stiles1995Revised2018", "Wright1914", "Rask1865",
                    "Goetz1971"):
            self.assertRegex(text, r"@\w+\{" + re.escape(key) + r"[,\n]")

    def test_handoff_points_to_exact_pr_commit_and_worktree(self):
        baseline = (REPO / "Germanic/articles/hay/SC047_BASELINE.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("113101ac5f169b589e1a9647cdf24d32cdd4d919", baseline)
        self.assertIn(".capr-work/worktrees/sc047-model-adoption", baseline)
        self.assertIn("8048652604b1925ea815265a66bffa12a55017cc", baseline)

    def test_private_original_checkout_is_optional(self):
        # This test documents the repository-level contract: no private original
        # is required for metadata-only validation.
        self.assertTrue((REPO / "docs/references/hay-article-source-report-2026-11-22.md").is_file())


if __name__ == "__main__":
    unittest.main()

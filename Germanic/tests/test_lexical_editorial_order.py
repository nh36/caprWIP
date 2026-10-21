"""Lexical entries are an editorial projection: derivation class, then alphabetical headword.

Row IDs, filenames and corpus order identify entries; they never decide where an
entry is published. Departures from the alphabetical default are explicit rows in
Germanic/docs/assembly/lexical_editorial_order.tsv.
"""

import csv
import random
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSEMBLY = ROOT / "Germanic/docs/assembly"
MODELS = ROOT / "Germanic/docs/lexeme_reports/model_entries"
sys.path.insert(0, str(ASSEMBLY))

import build_class_manifests as manifests

ENTRY_HEADING = re.compile(r"^#{2,3} (?P<headword>.+?) — OE ", re.M)


def tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def models() -> list[dict[str, object]]:
    return [manifests.parse_model_entry(path) for path in sorted(MODELS.glob("*.model.md"))]


def write_exceptions(directory: str, *rows: tuple[str, str, str]) -> Path:
    path = Path(directory) / "exceptions.tsv"
    path.write_text("row_id\tsort_as\treason\n" + "".join("\t".join(row) + "\n" for row in rows),
                    encoding="utf-8")
    return path


class EditorialOrderSourceTests(unittest.TestCase):
    def test_exceptions_are_well_formed_and_reference_real_entries(self):
        exceptions = manifests.load_editorial_order()
        row_ids = {str(model["row_id"]) for model in models()}
        self.assertLessEqual(set(exceptions), row_ids)
        for row_id, row in exceptions.items():
            self.assertTrue(row["reason"], row_id)

    def test_malformed_exception_tables_fail_closed(self):
        cases = {
            "duplicate": (("1933", "adder", "r"), ("1933", "adder", "r")),
            "numeric row ID": (("adder", "adder", "r"),),
            "plain a-z": (("1933", "Adder!", "r"),),
            "editorial reason": (("1933", "adder", ""),),
        }
        for pattern, rows in cases.items():
            with self.subTest(pattern), tempfile.TemporaryDirectory() as directory:
                with self.assertRaisesRegex(ValueError, pattern):
                    manifests.load_editorial_order(write_exceptions(directory, *rows))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "exceptions.tsv"
            path.write_text("row_id\tsort_key\treason\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "columns must be"):
                manifests.load_editorial_order(path)

    def test_reference_to_an_unknown_entry_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown row_id: 9999"):
            manifests.order_models(models(), {"9999": {"row_id": "9999", "sort_as": "zzz", "reason": "x"}})

    def test_headword_outside_plain_collation_requires_an_explicit_exception(self):
        entry = dict(models()[0], lexical_item="Ætheling")
        with self.assertRaisesRegex(ValueError, "sort_as exception"):
            manifests.order_models([entry], {})
        key = str(entry["row_id"])
        ordered = manifests.order_models([entry], {key: {"row_id": key, "sort_as": "atheling", "reason": "x"}})
        self.assertEqual(ordered, [entry])

    def test_indistinguishable_entries_must_be_separated_editorially(self):
        first, second = models()[:2]
        first = dict(first, metadata=dict(first["metadata"], COUNTERPART="aaa"))
        second = dict(second, lexical_item=first["lexical_item"], class_rank=first["class_rank"],
                      metadata=dict(second["metadata"], COUNTERPART="zzz"))
        # Differing Old English forms must not break the tie: only an editorial exception may.
        with self.assertRaisesRegex(ValueError, "tie in editorial order"):
            manifests.order_models([first, second], {})
        key = str(second["row_id"])
        ordered = manifests.order_models(
            [first, second], {key: {"row_id": key, "sort_as": f"{first['lexical_item']} (2)", "reason": "x"}})
        self.assertEqual([m["path"] for m in ordered], [first["path"], second["path"]])


class EditorialOrderPolicyTests(unittest.TestCase):
    def test_order_is_independent_of_identifiers_filenames_and_input_order(self):
        reference = [m["path"].name for m in manifests.order_models(models(), manifests.load_editorial_order())]
        for seed in range(5):
            shuffled = models()
            random.Random(seed).shuffle(shuffled)
            self.assertEqual(
                [m["path"].name for m in manifests.order_models(shuffled, manifests.load_editorial_order())],
                reference,
            )
        # Reassigning every row ID (and so every filename-derived identity) moves nothing.
        renumbered = [dict(m, row_id=900000 + i) for i, m in enumerate(models())]
        self.assertEqual([m["path"].name for m in manifests.order_models(renumbered, {})],
                         [m["path"].name for m in manifests.order_models(models(), {})])

    def test_exception_moves_only_the_named_entry_and_changes_no_scientific_data(self):
        baseline = manifests.order_models(models(), {})
        regular = [m for m in baseline if m["class_bucket"] == "regular"]
        moved, target = regular[0], regular[-1]
        exceptions = {str(moved["row_id"]): {
            "row_id": str(moved["row_id"]), "sort_as": str(target["lexical_item"]) + " (zz)", "reason": "test"}}
        reordered = manifests.order_models(models(), exceptions)
        self.assertNotEqual([m["path"] for m in reordered], [m["path"] for m in baseline])
        self.assertEqual(sorted(str(m["path"]) for m in reordered), sorted(str(m["path"]) for m in baseline))
        self.assertEqual([m["class_bucket"] for m in reordered], [m["class_bucket"] for m in baseline])
        regular_after = [m for m in reordered if m["class_bucket"] == "regular"]
        self.assertEqual(regular_after[-1]["path"], moved["path"])
        self.assertEqual([m["path"] for m in regular_after[:-1]], [m["path"] for m in regular[1:]])


class GeneratedManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = tsv(ASSEMBLY / "manifest_all_by_class.tsv")
        cls.exceptions = manifests.load_editorial_order()

    def test_manifest_contains_each_model_entry_exactly_once(self):
        expected = {str(int(path.name.split("-")[0])): path for path in MODELS.glob("*.model.md")}
        self.assertEqual(len(expected), len(list(MODELS.glob("*.model.md"))))
        ids = [r["row_id"] for r in self.rows]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(expected))
        for row in self.rows:
            self.assertEqual(ROOT / row["model_entry_path"], expected[row["row_id"]])

    def test_positions_are_contiguous_and_classes_are_in_catalogue_order(self):
        self.assertEqual([int(r["global_order"]) for r in self.rows], list(range(1, len(self.rows) + 1)))
        rank = {bucket: config[2] for bucket, config in manifests.CLASS_CONFIG.items()}
        self.assertEqual([rank[r["class_bucket"]] for r in self.rows],
                         sorted(rank[r["class_bucket"]] for r in self.rows))
        for bucket in rank:
            members = [r for r in self.rows if r["class_bucket"] == bucket]
            self.assertEqual([int(r["class_order"]) for r in members], list(range(1, len(members) + 1)))
            per_class = tsv(manifests.CLASS_MANIFESTS[bucket])
            self.assertEqual(per_class, members)

    def test_manifest_is_the_approved_editorial_sequence(self):
        # Independent restatement of the policy: headword, then qualifier, within class.
        def key(row):
            headword = self.exceptions.get(row["row_id"], {}).get("sort_as", row["lexical_item"])
            base, _, qualifier = headword.partition(" (")
            return (base, qualifier.rstrip(")"))

        for bucket in manifests.CLASS_CONFIG:
            members = [r for r in self.rows if r["class_bucket"] == bucket]
            self.assertEqual([r["row_id"] for r in members],
                             [r["row_id"] for r in sorted(members, key=key)], bucket)

    def test_sc112_witnesses_sit_at_their_alphabetical_positions(self):
        regular = [r["lexical_item"] for r in self.rows if r["class_bucket"] == "regular"]
        self.assertEqual(len(regular), 88)
        self.assertEqual(regular, sorted(regular))
        self.assertLess(regular.index("there"), regular.index("where"))
        self.assertNotEqual((regular.index("there") + 1, regular.index("where") + 1), (87, 88))

    def test_generated_summary_states_the_policy_and_exception_count(self):
        summary = (ASSEMBLY / "manifest_summary.md").read_text(encoding="utf-8")
        self.assertIn("alphabetically by Modern English headword", summary)
        self.assertIn(f"**{len(self.exceptions)}**", summary)


class DownstreamPropagationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = tsv(ASSEMBLY / "manifest_all_by_class.tsv")

    def headwords(self, name: str) -> list[str]:
        text = (ASSEMBLY / name).read_text(encoding="utf-8")
        return [match.group("headword") for match in ENTRY_HEADING.finditer(text)]

    def test_lexical_volume_follows_the_manifest(self):
        self.assertEqual(self.headwords("lexical_volume_alpha_01.md"),
                         [r["lexical_item"] for r in self.rows])

    def test_combined_book_follows_the_manifest(self):
        self.assertEqual(self.headwords("capr_book_draft_alpha_01.md"),
                         [r["lexical_item"] for r in self.rows])


if __name__ == "__main__":
    unittest.main()

"""Exact, authorized straw output-only migration with an attested target."""

import copy
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import cascade_baseline as baseline

BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"


class StrawOutputAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.approval = json.loads((BASE / "approved_sc034_output_migration.json").read_text())
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc034.tsv",
            BASE / "cascade_baseline_summary_pre_sc034.json",
        )
        self.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs.tsv", BASE / "cascade_baseline_summary.json",
        )

    def test_exact_output_match_delta_preserves_all_other_fields_and_386_rows(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        old = {row["row_id"]: row for row in self.previous["records"]}
        new = {row["row_id"]: row for row in self.current["records"]}
        self.assertEqual([identifier for identifier in old if old[identifier] != new[identifier]],
                         ["2224"])
        self.assertEqual({field for field in old["2224"]
                          if old["2224"][field] != new["2224"][field]}, {"outputs", "match"})
        self.assertEqual((new["2224"]["proto"], new["2224"]["counterpart"],
                          new["2224"]["outputs"], new["2224"]["match"]),
                         ("*stráwą", "strēaw", "strēa", "0"))
        self.assertEqual(
            {row["row_id"] for row in new.values() if row["match"] == "0"},
            {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"},
        )
        self.assertEqual(
            [self.current["summary"][field] for field in
             ("total_lexemes", "accepted", "matched", "mismatched", "ambiguous_outputs")],
            [387, 387, 379, 8, 0],
        )

    def test_rejects_unapproved_record_or_summary_drift(self):
        for identifier, field, value in (
            ("2224", "match", "1"), ("2224", "counterpart", "strēa"),
            ("2224", "proto", "*stráu"), ("2224", "word_stress", "unstressed"),
            ("2085", "outputs", "changed"), ("2085", "match", "0"),
        ):
            candidate = copy.deepcopy(self.current)
            next(row for row in candidate["records"] if row["row_id"] == identifier)[field] = value
            with self.subTest(identifier=identifier, field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, self.approval)
        for field in ("matched", "mismatched", "accepted", "total_lexemes"):
            candidate = copy.deepcopy(self.current)
            candidate["summary"][field] += 1
            with self.subTest(summary=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, self.approval)

    def test_match_approval_fails_closed_for_missing_unequal_or_inconsistent_fields(self):
        for kind in ("missing_before", "missing_after", "wrong_before", "wrong_after",
                     "invalid_flag", "no_op"):
            approval = copy.deepcopy(self.approval)
            candidate = copy.deepcopy(self.current)
            change = approval["changes"][0]
            if kind == "missing_before":
                del change["before"]["match"]
            elif kind == "missing_after":
                del change["after"]["match"]
            elif kind == "wrong_before":
                change["before"]["match"] = "0"
            elif kind == "wrong_after":
                change["after"]["match"] = "1"
            elif kind == "invalid_flag":
                change["after"]["match"] = "invalid"
                next(row for row in candidate["records"]
                     if row["row_id"] == "2224")["match"] = "invalid"
            else:
                change["after"] = dict(change["before"])
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, approval)

    def test_legacy_migration_rejects_noop_and_false_match_flags(self):
        with (BASE / "approved_input_migrations.tsv").open() as handle:
            migrations = list(csv.DictReader(handle, delimiter="\t"))
        with (BASE / "cascade_baseline_outputs_legacy380.tsv").open() as handle:
            legacy = list(csv.DictReader(handle, delimiter="\t"))
        for kind in ("no_op", "wrong_old", "wrong_new", "false_match"):
            approved = copy.deepcopy(migrations)
            records = copy.deepcopy(self.current["records"])
            migration = next(row for row in approved if row["row_id"] == "2224")
            if kind == "no_op":
                migration["new_outputs"] = migration["old_outputs"]
            elif kind == "wrong_old":
                migration["old_outputs"] = "wrong"
            elif kind == "wrong_new":
                migration["new_outputs"] = "wrong"
            else:
                next(row for row in records if row["row_id"] == "2224")["match"] = "1"
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.legacy_subset(records, legacy, approved)

    def test_adoption_preserves_previous_and_legacy_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source, destination in (
                ("cascade_baseline_outputs_pre_sc034.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc034.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
                ("approved_input_migrations.tsv", "approved_input_migrations.tsv"),
            ):
                (target / destination).write_bytes((BASE / source).read_bytes())
            old = (target / "cascade_baseline_outputs.tsv").read_bytes()
            legacy = (target / "cascade_baseline_outputs_legacy380.tsv").read_bytes()
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual((target / "cascade_baseline_outputs_pre_sc034.tsv").read_bytes(), old)
            self.assertEqual((target / "cascade_baseline_outputs_legacy380.tsv").read_bytes(), legacy)
            before = {path.name: path.read_bytes() for path in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual({path.name: path.read_bytes() for path in target.iterdir()}, before)


if __name__ == "__main__":
    unittest.main()

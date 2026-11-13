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


class CellAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.approval = json.loads((BASE / "approved_cell_migration.json").read_text())
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc033.tsv",
            BASE / "cascade_baseline_summary_pre_sc033.json",
        )
        self.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc033_hue.tsv",
            BASE / "cascade_baseline_summary_pre_sc033_hue.json",
        )

    def test_exact_knee_cell_transition(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        old = {row["row_id"]: row for row in self.previous["records"]}
        new = {row["row_id"]: row for row in self.current["records"]}
        self.assertEqual([identifier for identifier in old if old[identifier] != new[identifier]],
                         ["2085"])
        self.assertEqual(new["2085"]["proto"], "*knéwai")
        self.assertEqual(new["2085"]["counterpart"], "cneowe")
        self.assertEqual(new["2085"]["outputs"], "cneowe")
        self.assertEqual(self.current["summary"]["total_lexemes"], 387)
        self.assertEqual(self.current["summary"]["matched"], 380)
        self.assertEqual(self.current["summary"]["mismatched"], 7)
        self.assertEqual(self.current["summary"]["ambiguous_outputs"], 0)

    def test_rejects_undeclared_record_identity_and_summary_drift(self):
        for field, value in (
            ("proto", "*knéwą"), ("counterpart", "cnēow"), ("outputs", "cneow"),
            ("fst_input", "knéwą"), ("word_stress", "unstressed"),
            ("output_count", "2"), ("match", "0"), ("concept", "changed"),
        ):
            changed = copy.deepcopy(self.current)
            next(row for row in changed["records"] if row["row_id"] == "2085")[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, changed, self.approval)
        for kind in ("duplicate", "missing", "other_output", "fingerprint", "count"):
            changed = copy.deepcopy(self.current)
            if kind == "duplicate":
                changed["records"].append(copy.deepcopy(changed["records"][0]))
            elif kind == "missing":
                changed["records"].pop()
            elif kind == "other_output":
                changed["records"][0]["outputs"] = "changed"
            elif kind == "fingerprint":
                changed["summary"]["outputs_sha256"] = "0" * 64
            else:
                changed["summary"]["matched"] += 1
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, changed, self.approval)

    def test_rejects_incomplete_malformed_and_inconsistent_approval(self):
        for kind in ("missing_hash", "bad_hash", "adjudication", "memo", "duplicate",
                     "unknown", "before", "after", "multiplicity", "context"):
            approval = copy.deepcopy(self.approval)
            changed = copy.deepcopy(self.current)
            if kind == "missing_hash":
                approval["previous_summary"].pop("outputs_sha256")
            elif kind == "bad_hash":
                approval["legacy_archive_sha256"] = "bad"
            elif kind == "adjudication":
                approval["adjudication"] = "../unsafe"
            elif kind == "memo":
                approval["adjudication_memo"] = "wrong.md"
            elif kind == "duplicate":
                approval["changes"].append(copy.deepcopy(approval["changes"][0]))
            elif kind == "unknown":
                approval["changes"][0]["row_id"] = "missing"
            elif kind == "before":
                approval["changes"][0]["before"]["outputs"] = "wrong"
            elif kind == "after":
                approval["changes"][0]["after"]["outputs"] = "wrong"
            else:
                field, value = ("outputs", "cneowe|other") if kind == "multiplicity" else (
                    "fst_input", "ᵘknéwai")
                approval["changes"][0]["after"][field] = value
                next(row for row in changed["records"] if row["row_id"] == "2085")[field] = value
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, changed, approval)

    def test_adoption_preserves_archive_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source, destination in (
                ("cascade_baseline_outputs_pre_sc033.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc033.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
                ("approved_input_migrations.tsv", "approved_input_migrations.tsv"),
            ):
                (target / destination).write_bytes((BASE / source).read_bytes())
            old = (target / "cascade_baseline_outputs.tsv").read_bytes()
            with (BASE / "approved_input_migrations.tsv").open() as handle:
                reader = csv.DictReader(handle, delimiter="\t")
                fields = reader.fieldnames
                migrations = [row for row in reader if row["row_id"] in {"2040", "2085"}]
            with (target / "approved_input_migrations.tsv").open("w") as handle:
                writer = csv.DictWriter(handle, fields, delimiter="\t")
                writer.writeheader()
                writer.writerows(migrations)
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual((target / "cascade_baseline_outputs_pre_sc033.tsv").read_bytes(), old)
            before = {path.name: path.read_bytes() for path in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual({path.name: path.read_bytes() for path in target.iterdir()}, before)
            (target / "cascade_baseline_summary_pre_sc033.json").unlink()
            with self.assertRaisesRegex(ValueError, "incomplete"):
                baseline.adopt_cell_baseline(self.current, target, self.approval)


class LexicalExpansionTests(unittest.TestCase):
    def setUp(self):
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs.tsv", BASE / "cascade_baseline_summary.json")
        self.addition = dict(self.previous["records"][0],
                             row_id="900000", concept="admission-fixture")
        self.candidate = copy.deepcopy(self.previous)
        self.candidate["records"].append(self.addition)
        self.candidate["records"].sort(
            key=lambda row: (row["fst_input"], row["counterpart"], row["concept"]))
        self.update_summary()
        self.approval = {
            "adjudication": "SC063",
            "adjudication_memo": "Germanic/docs/sound_changes/audits/sc063-adjudication.md",
            "transition_id": "expansion_test",
            "previous_summary": {key: self.previous["summary"][key] for key in (
                "outputs_sha256", "lexical_outputs_sha256", "legacy_subset_sha256")},
            "legacy_archive_sha256": baseline.projection_sha256(
                baseline.read_baseline(
                    BASE / "cascade_baseline_outputs_legacy380.tsv",
                    BASE / "cascade_baseline_summary.json")["records"], "proto_norm"),
            "additions": [self.addition],
        }

    def update_summary(self):
        records = self.candidate["records"]
        self.candidate["summary"].update(
            total_lexemes=len(records),
            accepted=sum(row["accepted"] == "1" for row in records),
            rejected=sum(row["accepted"] == "0" for row in records),
            matched=sum(row["match"] == "1" for row in records),
            mismatched=sum(row["match"] == "0" for row in records),
            ambiguous_outputs=sum(int(row["output_count"]) > 1 for row in records),
            outputs_sha256=baseline.projection_sha256(records, "fst_input"),
            lexical_outputs_sha256=baseline.projection_sha256(records, "proto_norm"))

    def test_exact_admission_preserves_every_previous_record(self):
        baseline.validate_expansion_transition(self.previous, self.candidate, self.approval)
        self.assertEqual(self.candidate["summary"]["total_lexemes"],
                         self.previous["summary"]["total_lexemes"] + 1)
        self.assertEqual(self.candidate["summary"]["legacy_subset_sha256"],
                         self.previous["summary"]["legacy_subset_sha256"])

    def test_transparently_approved_mismatch_is_not_hidden_by_a_score_gate(self):
        self.addition.update(counterpart="different-attested-target", match="0")
        self.update_summary()
        baseline.validate_expansion_transition(self.previous, self.candidate, self.approval)
        self.assertEqual(self.candidate["summary"]["mismatched"],
                         self.previous["summary"]["mismatched"] + 1)

    def test_undeclared_record_identity_context_and_summary_drift_fail_closed(self):
        for case in ("old_record", "missing_old", "duplicate", "unapproved", "summary", "hash",
                     "context", "normalization", "multiplicity", "match", "concept"):
            candidate = copy.deepcopy(self.candidate)
            approval = copy.deepcopy(self.approval)
            new = next(row for row in candidate["records"] if row["row_id"] == "900000")
            if case == "old_record":
                next(row for row in candidate["records"]
                     if row["row_id"] == self.previous["records"][0]["row_id"])["outputs"] = "changed"
            elif case == "missing_old":
                candidate["records"] = [row for row in candidate["records"]
                                        if row["row_id"] != self.previous["records"][0]["row_id"]]
            elif case == "duplicate":
                candidate["records"].append(dict(new))
            elif case == "unapproved":
                candidate["records"].append(dict(new, row_id="900001", concept="extra"))
            elif case == "summary":
                candidate["summary"]["matched"] += 1
            elif case == "hash":
                approval["previous_summary"]["outputs_sha256"] = "0" * 64
            else:
                field, value = {
                    "context": ("fst_input", "ᵘ" + new["proto_norm"]),
                    "normalization": ("proto_norm", "different"),
                    "multiplicity": ("outputs", new["outputs"] + "|other"),
                    "match": ("match", "0"),
                    "concept": ("concept", self.previous["records"][0]["concept"]),
                }[case]
                new[field] = value
                approval["additions"][0][field] = value
            with self.subTest(case=case), self.assertRaises(ValueError):
                baseline.validate_expansion_transition(self.previous, candidate, approval)

    def test_adopter_and_journal_planner_preserve_archives_and_prior_approvals(self):
        import adjudication_run
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for name in ("cascade_baseline_outputs.tsv", "cascade_baseline_summary.json",
                         "cascade_baseline_outputs_legacy380.tsv", "approved_input_migrations.tsv"):
                (directory / name).write_bytes((BASE / name).read_bytes())
            originals = {path.name: path.read_bytes() for path in directory.iterdir()}
            transition = dict(approval_filename="approved_fixture_expansion.json",
                              approval=self.approval, candidate=self.candidate)
            planned = adjudication_run._expansion_transition_files(transition, directory)
            baseline.adopt_expansion_baseline(self.candidate, directory, self.approval)
            for path, data in planned.items():
                if not path.name.startswith("approved_"):
                    self.assertEqual(path.read_bytes(), data)
            for name in ("cascade_baseline_outputs_legacy380.tsv", "approved_input_migrations.tsv"):
                self.assertEqual((directory / name).read_bytes(), originals[name])
            self.assertEqual(
                (directory / "cascade_baseline_outputs_pre_sc063_expansion_test.tsv").read_bytes(),
                originals["cascade_baseline_outputs.tsv"])
            before = {path.name: path.read_bytes() for path in directory.iterdir()}
            baseline.adopt_expansion_baseline(self.candidate, directory, self.approval)
            self.assertEqual({path.name: path.read_bytes() for path in directory.iterdir()}, before)


if __name__ == "__main__":
    unittest.main()

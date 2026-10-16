"""Source-supported wether u-stem: exact input migration, unchanged laws/finals."""
from __future__ import annotations

import copy
import csv
import gzip
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import artifact_graph
import cascade_baseline as baseline

BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
AUDITS = ROOT / "Germanic/docs/sound_changes/audits"
REPORTS = ROOT / "Germanic/docs/lexeme_reports"
BEFORE = "695609f33ebd039c46a1c53bad173699b7b7fcef"
WETHER_RELEASE = "23c146eddd2d9f7527a05363b6768e352eddeb54"
MISMATCHES = {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"}


def table(path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader((line for line in handle if not line.startswith("#")),
                                   delimiter="\t"))


def committed(path):
    return subprocess.check_output(
        ["git", "show", f"{BEFORE}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT)


def released(path):
    return subprocess.check_output(
        ["git", "show", f"{WETHER_RELEASE}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT)


def released_table(path):
    return list(csv.DictReader(
        (line for line in released(path).decode().splitlines() if not line.startswith("#")),
        delimiter="\t"))


class WetherInputAdoptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc015_wether_input.tsv",
            BASE / "cascade_baseline_summary_pre_sc015_wether_input.json")
        cls.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc015.tsv",
            BASE / "cascade_baseline_summary_pre_sc015.json")
        cls.approval = json.loads((BASE / "approved_wether_input_migration.json").read_text())
        cls.receipt = json.loads(gzip.decompress(
            (AUDITS / "wether-input-trials.json.gz").read_bytes()))

    def test_exact_shared_etymology_fields_and_no_other_corpus_change(self):
        path = ROOT / "Germanic/data/germanic-aligned-final.tsv"
        old = list(csv.DictReader(committed(path).decode().splitlines(), delimiter="\t"))
        new = released_table(path)
        changes = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
        self.assertEqual({b["ID"] for a, b in changes}, {"1119", "1120", "1121", "2283"})
        for before, after in changes:
            self.assertEqual(after["COGIDS"], "307")
            self.assertEqual({key for key in before if before[key] != after[key]},
                             {"PROTO", "PROTOFORM"})
            self.assertEqual((before["PROTO"], before["PROTOFORM"]), ("*wíθrą", "*wíθrą"))
            self.assertEqual((after["PROTO"], after["PROTOFORM"]), ("*wéθruz", "*wéθruz"))
        wether = next(row for row in new if row["ID"] == "2283")
        self.assertEqual((wether["COUNTERPART"], wether["DERIVATION_CLASS"]), ("weþer", "regular"))
        weather = next(row for row in new if row["ID"] == "2280")
        self.assertEqual((weather["PROTO"], weather["COUNTERPART"]), ("*wédrą", "weder"))
        self.assertEqual(next(row for row in table(path) if row["ID"] == "2283"), wether)

    def test_preserved_pre_sc015_state_is_the_complete_wether_release(self):
        for stem, suffix in (("outputs", "tsv"), ("summary", "json")):
            self.assertEqual(
                (BASE / f"cascade_baseline_{stem}_pre_sc015.{suffix}").read_bytes(),
                released(BASE / f"cascade_baseline_{stem}.{suffix}"))

    def test_named_migration_preserves_all_final_outputs_and_mismatches(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        old = {r["row_id"]: r for r in self.previous["records"]}
        new = {r["row_id"]: r for r in self.current["records"]}
        self.assertEqual([key for key in old if old[key] != new[key]], ["2283"])
        self.assertEqual({key for key in old["2283"] if old["2283"][key] != new["2283"][key]},
                         {"proto", "proto_norm", "fst_input"})
        self.assertEqual({key: r["outputs"] for key, r in old.items()},
                         {key: r["outputs"] for key, r in new.items()})
        self.assertEqual({key for key, row in new.items() if row["match"] == "0"}, MISMATCHES)
        self.assertEqual([self.current["summary"][key] for key in (
            "total_lexemes", "accepted", "matched", "mismatched", "rejected", "ambiguous_outputs")],
            [387, 387, 379, 8, 0, 0])
        self.assertEqual((new["2283"]["counterpart"], new["2283"]["outputs"]), ("weþer", "weþer"))

    def test_both_source_alternatives_have_protected_complete_corpus_trials(self):
        probes = self.receipt["snapshot_probes"]
        self.assertGreaterEqual(len(probes), 100)
        for name, form in (("wether-u-stem", "*wéθruz"), ("wether-a-stem", "*wéθraz")):
            result = self.receipt["results"][name]
            with self.subTest(name=name):
                self.assertTrue(result["identity_equal"])
                self.assertTrue(result["canonical_artifacts_unchanged"])
                self.assertEqual(result["selected_rows"], 387)
                self.assertEqual(result["input_changed_ids"], ["2283"])
                for field in ("changed_ids", "missing_output_ids", "ambiguous_output_ids"):
                    self.assertEqual(result[field], [])
                self.assertEqual(set(result["baseline_mismatch_ids"]), MISMATCHES)
                self.assertEqual(set(result["variant_mismatch_ids"]), MISMATCHES)
                for row in result["rows"]:
                    self.assertEqual(set(row["intermediates"]), {p["id"] for p in probes})
                    if row["id"] != "2283":
                        self.assertTrue(all(pair["baseline"] == pair["variant"]
                                            for pair in row["intermediates"].values()), row["id"])
                    else:
                        self.assertEqual(row["variant_proto"], form)
                        self.assertEqual(row["variant_outputs"], ["weþer"])
        for field, path in (
            ("baseline_fst_sha256", ROOT / "Germanic/fsts/germanic.txt"),
            ("baseline_corpus_sha256", ROOT / "Germanic/data/germanic-aligned-final.tsv"),
        ):
            self.assertEqual(self.receipt["recipes"][field], hashlib.sha256(committed(path)).hexdigest())

    def test_laws_registry_contexts_and_historical_investigation_are_unchanged(self):
        paths = [ROOT / "Germanic/fsts/germanic.txt"]
        paths.extend(ROOT / "Germanic/data" / name for name in (
            "entry_stage_metadata.tsv", "entry_context_metadata.tsv"))
        paths.extend(ROOT / "Germanic/docs/sound_changes/registry" / name for name in (
            "sc_registry.tsv", "chronology_edges.tsv", "sc_inventory_notes.tsv"))
        paths.extend(path for path in (AUDITS / "sc015-hill-investigation").rglob("*")
                     if path.is_file())
        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(released(path), committed(path))
        registry = released_table(ROOT / "Germanic/docs/sound_changes/registry/sc_registry.tsv")
        sc015 = next(row for row in registry if row["sc_id"] == "SC015")
        self.assertEqual(sc015["adjudication_status"], "unadjudicated")
        self.assertEqual(sc015["verdict"], "")
        memo = released(AUDITS / "sc015-adjudication.md").decode()
        self.assertNotRegex(memo, r"(?m)^Registry-verdict:")
        self.assertEqual(len(re.findall(r"(?m)^## ", memo)), 9)
        self.assertEqual((AUDITS / "sc015-wether-input-adjudication.md").read_bytes(),
                         released(AUDITS / "sc015-adjudication.md"))

    def test_ending_history_and_only_authorized_application_changes(self):
        census_path = BASE / "rule_coverage_census.tsv"
        old = list(csv.DictReader(
            (line for line in committed(census_path).decode().splitlines()
             if not line.startswith("#")), delimiter="\t"))
        old = {row["sc_id"]: row for row in old}
        current = released_table(census_path)
        deltas = {row["sc_id"]: int(row["corpus_firing_count"])
                  - int(old[row["sc_id"]]["corpus_firing_count"])
                  for row in current
                  if row["corpus_firing_count"] != old[row["sc_id"]]["corpus_firing_count"]}
        self.assertEqual(deltas, {"SC015": -1, "SC020": 1, "SC047": -1, "SC063": 1})
        lowering = next(row for row in current if row["sc_id"] == "SC015")
        self.assertEqual(lowering["lexical_witnesses"], "meed, nest, world")
        selected = next(row for row in self.receipt["results"]["wether-u-stem"]["rows"]
                        if row["id"] == "2283")
        checkpoints = {probe["stage"]: probe["id"] for probe in self.receipt["snapshot_probes"]}
        trace = (ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt").read_text()
        trace = trace.split("--- wether ---", 1)[1].split("\n--- ", 1)[0]
        for stage, output, changes in (
            ("PNWGmcILowering", "*w*é*θ*r*u*z", False),
            ("EAFFinalZDeletion", "*w*é*θ*r*u", True),
            ("PWGmcFinalBareALoss", "*w*é*θ*r*u", False),
            ("OEHeavySyllableNasalApocope", "*w*é*θ*r*u", False),
            ("OEHighVowelApocope", "*w*é*θ*r", True),
            ("OEEpentheticVowel", "*w*é*θ*e*r", True),
            ("OldEnglishOrthography", "*w*éþ*e*r", True),
        ):
            with self.subTest(stage=stage):
                self.assertEqual(selected["intermediates"][checkpoints[stage]]["variant"], [output])
                label = stage if changes else stage + " [no-change]"
                self.assertIn(f"\n{label}: {output}\n", trace)
        self.assertIn("\nOldEnglishRemoveStars: weþer\n", trace)

    def test_actual_full_trace_preserves_every_other_lexical_entry(self):
        path = ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"
        before = re.split(r"(?m)^--- (.+) ---$", committed(path).decode())
        after = re.split(r"(?m)^--- (.+) ---$", released(path).decode())
        self.assertEqual(before[1:775:2], after[1:775:2])
        self.assertEqual(len(after[1:775:2]), 387)
        changed = [after[index] for index in range(1, 775, 2)
                   if before[index + 1] != after[index + 1]]
        self.assertEqual(changed, ["wether"])

    def test_legacy380_requires_the_exact_wether_mapping(self):
        legacy = table(BASE / "cascade_baseline_outputs_legacy380.tsv")
        migrations = released_table(BASE / "approved_input_migrations.tsv")
        self.assertEqual(len(baseline.legacy_subset(self.current["records"], legacy, migrations)), 380)
        for kind in ("missing", "wrong_old", "wrong_new", "wrong_output"):
            approved = copy.deepcopy(migrations)
            wether = next(row for row in approved if row["row_id"] == "2283")
            if kind == "missing":
                approved.remove(wether)
            else:
                wether[{"wrong_old": "old_proto", "wrong_new": "new_proto",
                        "wrong_output": "new_outputs"}[kind]] = "corrupt"
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.legacy_subset(self.current["records"], legacy, approved)

    def test_unauthorized_output_or_other_row_changes_fail(self):
        for identifier, field, value in (
            ("2283", "outputs", "wīþer"), ("2283", "counterpart", "weder"),
            ("2283", "word_stress", "unstressed"), ("2283", "output_count", "2"),
            ("2283", "proto", "*wéθraz"), ("2280", "proto", "*weather"),
        ):
            candidate = copy.deepcopy(self.current)
            next(r for r in candidate["records"] if r["row_id"] == identifier)[field] = value
            with self.subTest(identifier=identifier, field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, self.approval)

    def test_named_adopter_archives_prior_state_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source, destination in (
                ("cascade_baseline_outputs_pre_sc015_wether_input.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc015_wether_input.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
                ("approved_input_migrations.tsv", "approved_input_migrations.tsv"),
            ):
                data = (released(BASE / source) if source == "approved_input_migrations.tsv"
                        else (BASE / source).read_bytes())
                (target / destination).write_bytes(data)
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            for name, suffix in (("outputs", "tsv"), ("summary", "json")):
                path = BASE / f"cascade_baseline_{name}_pre_sc015_wether_input.{suffix}"
                self.assertEqual((target / path.name).read_bytes(), committed(
                    BASE / f"cascade_baseline_{name}.{suffix}"))
                self.assertIn(path, artifact_graph.ARCHIVE_PATHS)
            before = {p.name: p.read_bytes() for p in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual(before, {p.name: p.read_bytes() for p in target.iterdir()})

    def test_book_note_is_historical_page_cited_and_explicitly_selected(self):
        path = REPORTS / "model_entries/2283-wether-weþer.model.md"
        text = path.read_text()
        prose = text.split("### Comparative reconstruction and development", 1)[1]
        self.assertGreaterEqual(len(prose.split()), 300)
        self.assertLessEqual(len(prose.split()), 550)
        for required in ("PROTO: *wéθruz", "PROTOFORM: *wéθruz", "DERIVATION_CLASS: regular",
                         "CAPR therefore adopts", r"\emph{*weþraz}", "genitive *weþeres*",
                         "[vatsá-]{.lex lang=skt}"):
            self.assertIn(required, text)
        for excluded in ("*wíθrą", "Wiktionary", "SC015", "regression", "previous input", "**"):
            self.assertNotIn(excluded, prose)
        for citation in re.findall(r"\[(@[^\]]+)\]", prose):
            for part in citation.split(";"):
                self.assertRegex(part, r"@\w+,\s*pp?\.\s*[0-9]")
        cases = table(REPORTS / "pgmc_integration/editorial_cases.tsv")
        selected = [r for r in cases if r["row_id"] == "2283"]
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["publication_source"],
                         "model_entries/2283-wether-weþer.model.md")
        self.assertEqual(selected[0]["requires_extended_discussion"], "1")

    def test_exact_publication_fingerprint_deltas_remain_guarded(self):
        import check_reader_facing_semantics as semantics

        expected = {
            ("add", "oe", "weþer", "target_form", "lexical_heading", "wether — OE weþer"),
            ("add", "pgmc", "*wéθruz", "selected_input", "trace_proto_input", "wether — OE weþer"),
            ("add", "pgmc", "*wéθruz", "source_protoform", "lexical_protoform", "wether — OE weþer"),
            ("remove", "pgmc", "*wíθrą", "selected_input", "trace_proto_input", "wether — OE weþer"),
        }
        path = ROOT / "Germanic/docs/book/index_semantic_fingerprint_allowlist.tsv"
        before = list(csv.DictReader(committed(path).decode().splitlines(), delimiter="\t"))
        added = [row for row in released_table(path) if row not in before]
        self.assertEqual({tuple(row[key] for key in (
            "action", "language", "form", "form_role", "source_scope", "source_ref"))
            for row in added}, expected)
        semantics.run_index_fingerprint_checks()
        additions, removals, errors = semantics._load_allowlist()
        for action, language, form, role, scope, source in expected:
            key = (language, "", form, role, scope, source)
            with self.subTest(action=action, form=form, role=role):
                reduced_additions = additions - {key} if action == "add" else additions
                reduced_removals = removals - {key} if action == "remove" else removals
                with patch.object(semantics, "_load_allowlist", return_value=(
                        reduced_additions, reduced_removals, errors)):
                    with self.assertRaisesRegex(AssertionError, "fingerprint drift"):
                        semantics.run_index_fingerprint_checks()


if __name__ == "__main__":
    unittest.main()

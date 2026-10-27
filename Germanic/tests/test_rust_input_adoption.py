"""Authorized masculine rust input: unchanged endpoints and recoverable history."""
import copy
import csv
import json
import shlex
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import artifact_graph
import cascade_baseline as baseline
import oe_known_problems_report as known
import oe_pipeline
from capr_runtime import run_in_runner, check_build_manifest

BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
RUST_ADOPTION_COMMIT = "586ec5f370e58d9038142d330121acf58b085a18"


def read_tsv(path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader((line for line in handle if not line.startswith("#")),
                                   delimiter="\t"))


class RustInputAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc017_rust_input.tsv",
            BASE / "cascade_baseline_summary_pre_sc017_rust_input.json")
        self.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc015_wether_input.tsv",
            BASE / "cascade_baseline_summary_pre_sc015_wether_input.json")
        self.approval = json.loads((BASE / "approved_rust_input_migration.json").read_text())

    def test_exact_input_only_transition_and_unchanged_387_outputs(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        old = {r["row_id"]: r for r in self.previous["records"]}
        new = {r["row_id"]: r for r in self.current["records"]}
        self.assertEqual([key for key in old if old[key] != new[key]], ["2162"])
        self.assertEqual({key for key in old["2162"] if old["2162"][key] != new["2162"][key]},
                         {"proto", "proto_norm", "fst_input"})
        self.assertEqual({key: row["outputs"] for key, row in old.items()},
                         {key: row["outputs"] for key, row in new.items()})
        self.assertEqual(new["2162"]["proto"], "*rústaz")
        self.assertEqual((new["2162"]["counterpart"], new["2162"]["outputs"]), ("rust", "rost"))
        self.assertEqual({key for key, row in new.items() if row["match"] == "0"},
                         {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"})
        self.assertEqual([self.current["summary"][key] for key in
                          ("total_lexemes", "accepted", "matched", "mismatched",
                           "rejected", "ambiguous_outputs")], [387, 387, 379, 8, 0, 0])

    def test_original380_rust_identity_requires_exact_migration(self):
        legacy = read_tsv(BASE / "cascade_baseline_outputs_legacy380.tsv")
        migrations = [row for row in read_tsv(BASE / "approved_input_migrations.tsv")
                      if row["row_id"] not in {"2283", "2095", "2313", "2314", "2302"}]
        original = next(row for row in legacy
                        if (row["concept"], row["counterpart"]) == ("rust", "rust"))
        self.assertEqual(original["proto"], "*rústō")
        self.assertEqual(original["outputs"], "rost")
        resolved = baseline.legacy_subset(self.current["records"], legacy, migrations)
        self.assertEqual(len(resolved), 380)
        for kind in ("missing", "wrong_old", "wrong_new", "wrong_output"):
            approved = copy.deepcopy(migrations)
            rust = next(row for row in approved if row["row_id"] == "2162")
            if kind == "missing":
                approved.remove(rust)
            else:
                rust[{"wrong_old": "old_proto", "wrong_new": "new_proto",
                      "wrong_output": "new_outputs"}[kind]] = "corrupt"
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.legacy_subset(self.current["records"], legacy, approved)

    def test_unauthorized_other_row_or_rust_endpoint_change_fails(self):
        for identifier, field, value in (
            ("2162", "outputs", "rust"), ("2162", "counterpart", "rost"),
            ("2162", "word_stress", "unstressed"), ("2162", "output_count", "2"),
            ("2162", "match", "1"), ("2035", "proto", "*other"),
        ):
            candidate = copy.deepcopy(self.current)
            next(row for row in candidate["records"] if row["row_id"] == identifier)[field] = value
            with self.subTest(identifier=identifier, field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, self.approval)

    def test_adopter_preserves_post_sc034_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source, destination in (
                ("cascade_baseline_outputs_pre_sc017_rust_input.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc017_rust_input.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
                ("approved_input_migrations.tsv", "approved_input_migrations.tsv"),
            ):
                (target / destination).write_bytes((BASE / source).read_bytes())
            migrations_path = target / "approved_input_migrations.tsv"
            migrations = [row for row in read_tsv(migrations_path)
                          if row["row_id"] not in {"2283", "2095", "2313", "2314", "2302"}]
            with migrations_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(migrations[0]), delimiter="\t")
                writer.writeheader()
                writer.writerows(migrations)
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            for name in ("outputs", "summary"):
                archived = BASE / f"cascade_baseline_{name}_pre_sc017_rust_input.{'tsv' if name == 'outputs' else 'json'}"
                self.assertEqual((target / archived.name).read_bytes(), archived.read_bytes())
                self.assertIn(archived, artifact_graph.ARCHIVE_PATHS)
                committed = subprocess.check_output(
                    ["git", "show", f"757e36e0:{archived.relative_to(ROOT).as_posix().replace('_pre_sc017_rust_input', '')}"],
                    cwd=ROOT)
                self.assertEqual(archived.read_bytes(), committed)
            before = {path.name: path.read_bytes() for path in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual(before, {path.name: path.read_bytes() for path in target.iterdir()})

    def test_rust_adoption_corpus_delta_was_only_authorized_fields_and_oe_row(self):
        path = ROOT / "Germanic/data/germanic-aligned-final.tsv"
        old_text = subprocess.check_output(
            ["git", "show", f"757e36e0:{path.relative_to(ROOT)}"], cwd=ROOT, text=True)
        old = list(csv.DictReader(old_text.splitlines(), delimiter="\t"))
        adopted_text = subprocess.check_output(
            ["git", "show", f"{RUST_ADOPTION_COMMIT}:{path.relative_to(ROOT).as_posix()}"],
            cwd=ROOT, text=True)
        new = list(csv.DictReader(adopted_text.splitlines(), delimiter="\t"))
        changes = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
        self.assertEqual(len(changes), 1)
        before, after = changes[0]
        self.assertEqual((after["ID"], after["DOCULECT"]), ("2162", "Old_English"))
        self.assertEqual({key for key in before if before[key] != after[key]},
                         {"PROTO", "PROTOFORM", "NOTE"})
        sidecar = read_tsv(ROOT / "Germanic/data/entry_stage_metadata.tsv")
        self.assertFalse(any(row["row_id"] == "2162" for row in sidecar))

    def test_reader_model_ledger_and_census_agree(self):
        model = (ROOT / "Germanic/docs/lexeme_reports/model_entries/2162-rust-rust.model.md").read_text()
        for value in ("PROTO: *rústaz", "PROTOFORM: *rústaz", "COUNTERPART: rust",
                      "DERIVATION_CLASS: unexplained_unmodelled", "*rústaz > rost"):
            self.assertIn(value, model)
        self.assertIn("not an attested Proto-Germanic citation form", model)
        self.assertIn("[@Toller1921, p. 691]", model)
        self.assertNotIn("BosworthToller1898", model)
        self.assertNotIn("*-st-*", model)
        self.assertEqual(model.count("_-st-_"), 2)
        findings = (ROOT / "Germanic/docs/analysis/notable_findings.md").read_text()
        lowering = findings.split("## 2.", 1)[1].split("## 3.", 1)[0]
        self.assertIn("Rust is the nonlabial counterexample", lowering)
        self.assertIn("not CAPR's adopted explanation", lowering)
        self.assertNotIn("the pattern is gradient/probabilistic", lowering)
        census = read_tsv(BASE / "rule_coverage_census.tsv")
        for identifier, count in (("SC017", "39"), ("SC019", "28"), ("SC020", "114")):
            row = next(row for row in census if row["sc_id"] == identifier)
            self.assertEqual(row["corpus_firing_count"], count)
        ledger = known.load_ledger(ROOT / "Germanic/data/oe_known_problems.tsv")
        rust = ledger["*rústaz"]
        self.assertEqual((rust["status"], rust["added"], rust["category"]),
                         ("wontfix", "2026-04-25", "u_lowering_lexical_retention"))
        report = known.render_report(known.baseline_mismatches(self.current["records"]), ledger)
        self.assertIn("Total mismatches:         8", report)
        self.assertIn("*stráwą", report)
        self.assertNotIn("orst", rust["reason"].replace("forst", ""))
        self.assertEqual(
            (ROOT / "Germanic/docs/debug_snapshots/oe_known_problems_report.txt").read_text(), report)

    def test_rust_adoption_changed_only_its_intermediate_trace_and_paths_converged(self):
        import re

        path = ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"
        old = subprocess.check_output(
            ["git", "show", f"757e36e0:{path.relative_to(ROOT)}"], cwd=ROOT, text=True)
        new = subprocess.check_output(
            ["git", "show", f"{RUST_ADOPTION_COMMIT}:{path.relative_to(ROOT).as_posix()}"],
            cwd=ROOT, text=True)
        adopted_baseline = subprocess.check_output(
            ["git", "show",
             f"{RUST_ADOPTION_COMMIT}:Germanic/docs/sound_changes/cascade_baseline/"
             "cascade_baseline_outputs.tsv"],
            cwd=ROOT, text=True)
        adopted_records = list(csv.DictReader(adopted_baseline.splitlines(), delimiter="\t"))

        def blocks(text, records):
            identifiers = {(row["concept"], row["proto"]): row["row_id"] for row in records}
            parts = re.split(r"(?m)^--- (.+) ---\n", text)[1:]
            result = {}
            for heading, body in zip(parts[::2], parts[1::2], strict=True):
                proto = re.search(r"(?m)^PROTO: (.+)$", body)
                if proto is None:
                    continue
                identifier = identifiers[heading, proto[1]]
                self.assertNotIn(identifier, result)
                result[identifier] = body.split("\n=== BUCKET:", 1)[0].strip()
            return result

        before = blocks(old, self.previous["records"])
        after = blocks(new, adopted_records)
        self.assertEqual(len(before), 387)
        self.assertEqual(before.keys(), after.keys())
        self.assertEqual([key for key in before if before[key] != after[key]], ["2162"])
        for line in (
            "PNWGmcULowering: *r*ó*s*t*a*z",
            "PNWGmcFinalLongORaising [no-change]: *r*ó*s*t*a*z",
            "EAFFinalZDeletion: *r*ó*s*t*a",
            "PWGmcFinalBareALoss: *r*ó*s*t",
            "OEHighVowelApocope [no-change]: *r*ó*s*t",
        ):
            self.assertIn(line, after["2162"])
        self.assertIn("PNWGmcFinalLongORaising: *r*ó*s*t*u", before["2162"])
        self.assertIn("OEHighVowelApocope: *r*ó*s*t", before["2162"])

    def test_index_preserves_source_alternative_without_promoting_diagnostics(self):
        rows = read_tsv(ROOT / "Germanic/docs/book/index_verborum_print_main.tsv")
        rust = [row for row in rows if "2162-rust-rust.model.md" in row["source_ref"]]
        for form in ("rústaz", "rústō"):
            tagged = [row for row in rust
                      if row["form"] == form and row["source_scope"] == "explicit_tag"]
            self.assertEqual(len(tagged), 1)
            self.assertEqual((tagged[0]["language"], tagged[0]["display"]),
                             ("pgmc", "*" + form))
        self.assertTrue(any(row["language"] == "ohg" and row["form"] == "rost"
                            for row in rust))
        self.assertFalse(any(row["form"].lstrip("*") in
                             {"róstaz", "rústas", "rústai", "rústi", "rústu"}
                             for row in rust))


@pytest.mark.runtime
def test_fresh_production_and_isolated_rust_diagnostics():
    assert not check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    code = """import sys,json,tempfile
from pathlib import Path
sys.path.insert(0,'tools')
import anglo_frisian_experiments as e
from oe_full_trace_report import apply_down,normalize_proto
from capr_runtime import layout
recipe={'id':'identity','definitions':'','insert_rule':'','insert_after':'','replace':{},'sources':[]}
forms=['*rústaz','*rústō','*rústas','*rústai','*rústi','*rústu','*frústą']
rt=layout()
with tempfile.TemporaryDirectory() as directory:
 bins=e.compile_isolated(rt.germanic_fst,recipe,[],Path(directory))
 result={form:{'production':apply_down(rt.bin_dir/'old_english.bin',normalize_proto(form)),
               'isolated':apply_down(bins['final'],normalize_proto(form))} for form in forms}
print(json.dumps(result,ensure_ascii=False))
"""
    result = run_in_runner("python3 -c " + shlex.quote(code), capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    expected = dict(zip(("*rústaz", "*rústō", "*rústas", "*rústai", "*rústi", "*rústu", "*frústą"),
                        ("rost", "rost", "rostes", "roste", "ryst", "rust", "forst"), strict=True))
    assert json.loads(result.stdout) == {
        form: {"production": [output], "isolated": [output]} for form, output in expected.items()}

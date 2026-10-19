"""Authorized consonant-conditioned lowering and independent learn selections."""
from __future__ import annotations

import copy
import csv
import gzip
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import cascade_baseline as baseline
import artifact_graph
from executable_facts import parse_defines

SC = ROOT / "Germanic/docs/sound_changes"
BASE = SC / "cascade_baseline"
ADOPTION = SC / "audits/sc015-adoption"
FST = ROOT / "Germanic/fsts/germanic.txt"
HISTORICAL_AFTER_COMMIT = "3f3deb56f81a76324eefcc68401887f03a15a674"
HISTORICAL_FST = subprocess.check_output(
    ["git", "show", f"{HISTORICAL_AFTER_COMMIT}:Germanic/fsts/germanic.txt"],
    cwd=ROOT, text=True)
HISTORICAL_CORPUS = ROOT / "Germanic/data/germanic-aligned-final.tsv"
TARGETS = {"2095": "leornian", "2313": "leorna", "2314": "leornaþ"}
MISMATCHES = {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"}
RULE = """Ctx([
    {*i} -> {*e} ||
        .#. EnglishStarConsonant* _
        [{*z} [EnglishStarConsonant | .#.]
         | {*s} {*t}
         | {*r}],
    {*í} -> {*é} ||
        .#. EnglishStarConsonant* _
        [{*z} [EnglishStarConsonant | .#.]
         | {*s} {*t}
         | {*r}]
])"""


def compact(text):
    return re.sub(r"\s+", "", text)


def table(path):
    return list(csv.DictReader(
        (line for line in path.read_text().splitlines() if not line.startswith("#")),
        delimiter="\t"))


class SC015AdoptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = json.loads(gzip.decompress((ADOPTION / "before.json.gz").read_bytes()))
        cls.after = json.loads(gzip.decompress((ADOPTION / "after.json.gz").read_bytes()))
        cls.probes = json.loads((ADOPTION / "probes.json").read_text())
        cls.approval = json.loads((BASE / "approved_sc015_targets_migration.json").read_text())
        cls.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc015.tsv",
            BASE / "cascade_baseline_summary_pre_sc015.json")
        cls.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc112_expansion.tsv",
            BASE / "cascade_baseline_summary_pre_sc112_expansion.json")

    def test_exact_candidate_and_only_authorized_definition_change(self):
        source = HISTORICAL_FST
        old_source = subprocess.check_output([
            "git", "show", "23c146ed:Germanic/fsts/germanic.txt"], cwd=ROOT, text=True)
        old, new = parse_defines(old_source), parse_defines(source)
        self.assertEqual(compact(new["PNWGmcILowering"].body), compact(RULE))
        self.assertEqual(set(old) - set(new),
                         {"EnglishStarNonVelar", "EnglishStarNonVelarConsonant"})
        self.assertEqual(set(new) - set(old), set())
        changed = {name for name in new if old[name].body != new[name].body}
        self.assertEqual(changed, {"PNWGmcILowering"})
        for name in new.keys() - changed:
            self.assertEqual(old[name].body, new[name].body, name)
        self.assertNotIn("EnglishStarNonVelar", source)
        reader = (SC / "reader_facing/014-015-opening-vowel-prelude.md").read_text()
        block = next(block for block in re.findall(r"```foma\n(.*?)```", reader, re.S)
                     if "define PNWGmcILowering " in block)
        self.assertEqual(compact(parse_defines(block)["PNWGmcILowering"].body), compact(RULE))

    def test_complete_census_and_exact_intermediate_changes(self):
        a, b = self.before["rows"], self.after["rows"]
        self.assertEqual(len(a), 387)
        self.assertEqual(a.keys(), b.keys())
        stage = "PNWGmcILowering"
        names = list(next(iter(b.values()))["checkpoints"])
        previous = names[names.index(stage) - 1]
        firing = {i for i, r in b.items() if r["checkpoints"][previous] != r["checkpoints"][stage]}
        self.assertEqual(firing, {"2095", "2124", "2137", "2250", "2302", "2313", "2314"})
        self.assertEqual(len(names), 107)
        deltas = {i for i in a if a[i]["checkpoints"] != b[i]["checkpoints"]}
        self.assertEqual(deltas, {*TARGETS, "2250"})
        self.assertEqual({i for i in a if a[i]["outputs"] != b[i]["outputs"]}, set(TARGETS))
        self.assertEqual(self.after["matched_three_states"], [379, 376, 379])
        self.assertEqual(b["2250"]["outputs"], a["2250"]["outputs"])
        self.assertEqual(b["2283"]["checkpoints"], a["2283"]["checkpoints"])
        for identifier, target in TARGETS.items():
            self.assertEqual(b[identifier]["outputs"], [target])
        self.assertTrue(all(len(row["outputs"]) == 1 for row in b.values()))

    def test_component_controls_and_counterevidence_are_not_confused(self):
        probes = {r["id"]: r for r in self.probes["components"]}
        self.assertEqual(len(probes), 22)
        for name in ("nistan", "mizdon", "wiraz", "iz", "hiz", "hir", "velar_onset",
                     "acute", "high_following", "list"):
            self.assertNotEqual(probes[name]["input"], probes[name]["outputs"][0], name)
        for name in ("fish", "wisko", "bitanaz", "bithanaz", "nidana", "lid",
                     "long", "later_nucleus", "intervocalic_z", "nistijan_mutation", "listiz_mutation"):
            self.assertEqual(probes[name]["outputs"], [probes[name]["input"]], name)
        self.assertEqual(probes["twine"]["role"], "counterevidence")
        self.assertIn("NOT a correct reflex", probes["twine"]["basis"])
        self.assertEqual(self.probes["fst_sha256"],
                         hashlib.sha256(HISTORICAL_FST.encode()).hexdigest())
        historical_corpus = subprocess.check_output(
            ["git", "show", f"{HISTORICAL_AFTER_COMMIT}:Germanic/data/germanic-aligned-final.tsv"],
            cwd=ROOT)
        self.assertEqual(self.probes["corpus_sha256"],
                         hashlib.sha256(historical_corpus).hexdigest())
        self.assertEqual({r["row_id"]: r["outputs"] for r in self.probes["learn_paradigm"]},
                         {key: [value] for key, value in TARGETS.items()})

    def test_rich_migration_is_reproducible_and_preserves_all_other_fields(self):
        spec = importlib.util.spec_from_file_location("sc015_migration", ADOPTION / "migration.py")
        migration = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(migration)
        self.assertEqual(json.loads((ADOPTION / "migration.json").read_text()), migration.build())
        self.assertEqual({r["row_id"] for r in self.current["records"] if r["match"] == "0"},
                         MISMATCHES)
        self.assertEqual(self.current["summary"]["matched"], 379)
        self.assertEqual(self.current["summary"]["mismatched"], 8)

    def test_strict_migration_rejects_undeclared_or_wrong_changes(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        for identifier, field, value in (
            ("2095", "proto", "*leznōjaną"), ("2095", "outputs", "liornian"),
            ("2313", "counterpart", "leornian"), ("2314", "word_stress", "unstressed"),
            ("2250", "outputs", "þestel"), ("2283", "proto", "*wíθrą"),
        ):
            candidate = copy.deepcopy(self.current)
            next(r for r in candidate["records"] if r["row_id"] == identifier)[field] = value
            with self.subTest(identifier=identifier, field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, self.approval)
        for changed in ("missing", "duplicate", "wrong_input"):
            approval = copy.deepcopy(self.approval)
            if changed == "missing":
                approval["changes"].pop()
            elif changed == "duplicate":
                approval["changes"].append(approval["changes"][0])
            else:
                approval["changes"][0]["after"]["proto"] = "*leznōjaną"
            with self.subTest(approval=changed), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, self.current, approval)

    def test_adopter_is_idempotent_and_refuses_conflicting_archive(self):
        for path in (BASE / "cascade_baseline_outputs_pre_sc015.tsv",
                     BASE / "cascade_baseline_summary_pre_sc015.json"):
            self.assertIn(path, artifact_graph.ARCHIVE_PATHS)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for path in BASE.iterdir():
                if path.is_file() and path.suffix in {".tsv", ".json"}:
                    shutil.copyfile(path, target / path.name)
            shutil.copyfile(
                BASE / "cascade_baseline_outputs_pre_sc112_expansion.tsv",
                target / "cascade_baseline_outputs.tsv",
            )
            shutil.copyfile(
                BASE / "cascade_baseline_summary_pre_sc112_expansion.json",
                target / "cascade_baseline_summary.json",
            )
            initial = {p.name: p.read_bytes() for p in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual(initial, {p.name: p.read_bytes() for p in target.iterdir()})
            (target / "cascade_baseline_summary_pre_sc015.json").unlink()
            with self.assertRaisesRegex(ValueError, "incomplete pre-cell baseline archive"):
                baseline.adopt_cell_baseline(self.current, target, self.approval)

    def test_metadata_and_chronology_keep_the_scientific_axes_separate(self):
        registry = next(row for row in table(SC / "registry/sc_registry.tsv") if row["sc_id"] == "SC015")
        self.assertEqual(registry["verdict"], "REFORMULATE")
        self.assertEqual(registry["adjudication_status"], "adjudicated")
        self.assertEqual(registry["hist_stage"], "pnwgmc")
        self.assertEqual(registry["hist_scope"], "pan_pnwgmc")
        self.assertEqual(registry["confidence"], "B")
        edges = [r for r in table(SC / "registry/chronology_edges.tsv")
                 if r["source_change_id"] == "SC015"]
        self.assertFalse(any(r["target_change_id"] == "SC036" for r in edges))
        self.assertTrue(any(r["target_change_id"] == "PWGmcChanges" for r in edges))
        memo = (SC / "audits/sc015-adjudication.md").read_text()
        self.assertIn("Registry-verdict: SC015=REFORMULATE", memo)
        reader = (SC / "reader_facing/014-015-opening-vowel-prelude.md").read_text()
        prose = reader.split("### A disputed Germanic correspondence", 1)[1]
        prose = re.sub(r"```[\s\S]*?```|\[@[^\]]+\]", "", prose)
        self.assertGreaterEqual(len(prose.split()), 2500)
        self.assertLessEqual(len(prose.split()), 3500)
        whitelist = table(SC / "reader_facing/reader_facing_citation_whitelist.tsv")
        exceptions = [row for row in whitelist if row["key"] == "deVaan2016"]
        self.assertEqual(len(exceptions), 1)
        self.assertEqual(exceptions[0]["file_name"], "014-015-opening-vowel-prelude.md")
        self.assertEqual(exceptions[0]["whole_work_general"], "no")
        self.assertIn("unpaginated", exceptions[0]["reason"])
        self.assertIn("paragraphs “Verwante vormen” and “Zowel”", reader)
        self.assertIn(r"\emph{*hir} > \emph{*her} > \emph{*hēr}.", reader)
        self.assertNotIn(r"\longrightarrow", reader)

    def test_publication_delta_is_scoped_to_authorized_lexical_accounts(self):
        import check_reader_facing_semantics as semantics

        path = ROOT / "Germanic/docs/book/index_semantic_fingerprint_allowlist.tsv"
        old = list(csv.DictReader(subprocess.check_output([
            "git", "show", "23c146ed:" + str(path.relative_to(ROOT))],
            cwd=ROOT, text=True).splitlines(), delimiter="\t"))
        fields = ("action", "language", "form", "form_role", "source_scope", "source_ref")
        old_keys = {tuple(row[field] for field in fields) for row in old}
        post_sc015 = list(csv.DictReader(subprocess.check_output([
            "git", "show", "c92cbd9d541785986998ab2ab99a416f87da4f68:"
            + str(path.relative_to(ROOT))],
            cwd=ROOT, text=True).splitlines(), delimiter="\t"))
        added = [row for row in post_sc015
                 if tuple(row[field] for field in fields) not in old_keys]
        sc015 = added
        self.assertEqual(len(sc015), 52)
        self.assertEqual(sum(row["action"] == "add" for row in sc015), 18)
        self.assertEqual(sum(row["action"] == "remove" for row in sc015), 34)
        self.assertEqual(sum(row.get("variety") == "north" for row in sc015), 4)
        for row in sc015:
            self.assertTrue(any(token in row["source_ref"] for token in (
                "2095-learn-", "2313-learn-", "2314-learn-", "2137-nest-",
                "learn — OE ", "learn (3sg) — OE ", "learn (iptv.2sg) — OE ",
                "nest — OE nest")), row)
        audit = table(ROOT / "Germanic/docs/book/index_verborum_variety_annotation_audit.tsv")
        withdrawn = [row for row in audit
                     if any(f"/{identifier}-learn-" in row["source_ref"]
                            for identifier in ("2313", "2314"))]
        self.assertEqual(len(withdrawn), 4)
        self.assertTrue(all(row["decision"] == "not_variety_evidence"
                            and not row["proposed_variety"] for row in withdrawn))
        semantics.run_index_fingerprint_checks()


if __name__ == "__main__":
    unittest.main()

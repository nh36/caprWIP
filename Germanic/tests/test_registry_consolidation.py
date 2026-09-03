"""Structural invariants for the consolidated control plane.

These tests enforce the SOURCE / GENERATED / ARCHIVE contract:
- the canonical registries are internally coherent;
- generated views reproduce byte-identically from canonical sources;
- retired SCs cannot re-enter live executable machinery;
- adjudication memos agree with the registry verdicts;
- archived material is not an input to current-state generation;
- current navigation docs do not present archived files as authoritative.
"""

import importlib.util
import json
import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
REGISTRY_DIR = SC_DIR / "registry"
ARCHIVE_DIRS = (
    REPO_ROOT / "Germanic/docs/archive",
    SC_DIR / "archive",
)
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
BASELINE_SUMMARY = SC_DIR / "cascade_baseline/cascade_baseline_summary.json"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


views = _load("generate_registry_views")
adjudicate = _load("adjudicate")


class RegistryCoherenceTests(unittest.TestCase):
    def setUp(self):
        self.reg = views.read_tsv(views.SC_REGISTRY)
        self.edges = views.read_tsv(views.EDGE_REGISTRY)
        self.by_id = {r["sc_id"]: r for r in self.reg}

    def test_every_sc_appears_exactly_once(self):
        ids = [r["sc_id"] for r in self.reg]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(re.fullmatch(r"SC\d{3}[a-z]?", i) for i in ids), ids)

    def test_validator_reports_no_errors(self):
        self.assertEqual(views.validate_registry(self.reg, self.edges), [])

    def test_edge_endpoints_exist_in_registry(self):
        # Boundary/technical edges may target non-SC sentinels: the
        # PWGmcChanges umbrella FST block and the RUNNER_LIMIT marker.
        sentinels = {"PWGmcChanges", "RUNNER_LIMIT"}
        for e in self.edges:
            self.assertIn(e["source_change_id"], self.by_id)
            tgt = e["target_change_id"]
            if tgt in sentinels:
                self.assertIn(
                    e["relation_type"],
                    {"runner_limited_boundary", "technical_computational"},
                    e,
                )
            else:
                self.assertIn(tgt, self.by_id)

    def test_verdict_tokens_are_in_controlled_vocabulary(self):
        for r in self.reg:
            for tok in filter(None, r["verdict"].split("/")):
                self.assertIn(tok, views.VERDICT_VOCABULARY, r["sc_id"])

    def test_adjudicated_rows_point_to_existing_memo(self):
        for r in self.reg:
            if r["adjudication_status"] == "adjudicated":
                memo = r["adjudication_memo"]
                self.assertTrue(memo, r["sc_id"])
                self.assertTrue((REPO_ROOT / memo).exists(), memo)


class GeneratedViewTests(unittest.TestCase):
    def test_generated_views_reproduce_exactly(self):
        for path, text in views.build_all().items():
            self.assertTrue(path.exists(), path)
            self.assertEqual(
                path.read_text(encoding="utf-8"),
                text,
                f"{path} is dirty: regenerate with "
                "python3 Germanic/tools/generate_registry_views.py",
            )

    def test_generated_files_carry_do_not_edit_banner(self):
        for path in views.build_all():
            head = path.read_text(encoding="utf-8")[:400]
            self.assertIn("GENERATED", head, path)
            self.assertIn("DO NOT EDIT", head, path)


class RetiredExecutableTests(unittest.TestCase):
    def test_retired_fst_identifiers_are_not_live(self):
        reg = views.read_tsv(views.SC_REGISTRY)
        fst_text = FST.read_text(encoding="utf-8")
        live_lines = [
            l for l in fst_text.splitlines() if not l.lstrip().startswith("#")
        ]
        manifest_text = ORDER_MANIFEST.read_text(encoding="utf-8")
        for r in reg:
            if r["lifecycle_status"] != "retired":
                continue
            self.assertEqual(r["cascade_position"], "", r["sc_id"])
            self.assertEqual(r["staging_row"], "no", r["sc_id"])
            ident = r["fst_identifier"]
            if not ident:
                continue
            for line in live_lines:
                self.assertNotRegex(
                    line,
                    rf"\bdefine\s+{re.escape(ident)}\b",
                    f"retired {r['sc_id']} identifier {ident} still defined",
                )
            self.assertNotIn(
                ident,
                manifest_text,
                f"retired {r['sc_id']} identifier {ident} in live order manifest",
            )


class MemoAgreementTests(unittest.TestCase):
    def test_memo_registry_verdict_lines_agree_with_registry(self):
        reg = views.read_tsv(views.SC_REGISTRY)
        for r in reg:
            if r["adjudication_status"] != "adjudicated":
                continue
            rc = adjudicate.check(r["sc_id"])
            self.assertEqual(rc, 0, f"adjudicate --check failed for {r['sc_id']}")


class ArchiveIsolationTests(unittest.TestCase):
    def test_no_generator_input_lives_in_an_archive(self):
        for path in views.DECLARED_INPUTS:
            for arch in ARCHIVE_DIRS:
                self.assertNotIn(str(arch), str(path))

    def test_navigation_docs_do_not_cite_archives_as_authoritative(self):
        docs = [
            REPO_ROOT / "Germanic/docs/README.md",
            REPO_ROOT / "Germanic/docs/CURRENT_STATE.md",
            SC_DIR / "README.md",
        ]
        for doc in docs:
            text = doc.read_text(encoding="utf-8")
            for stale in ("DEV_NOTES.md", "CANONICAL_STATE.md", "WORKFLOW.md"):
                for line in text.splitlines():
                    if stale in line:
                        self.assertRegex(
                            line.lower(),
                            r"archive|frozen|historical|tombstone|superseded",
                            f"{doc} cites {stale} without marking it archival: {line}",
                        )

    def test_tombstones_point_to_archive(self):
        for name in ("CANONICAL_STATE.md", "DEV_NOTES.md", "WORKFLOW.md"):
            tomb = REPO_ROOT / "Germanic/docs" / name
            self.assertTrue(tomb.exists(), name)
            text = tomb.read_text(encoding="utf-8")
            self.assertIn("archive/", text, name)
            self.assertLess(len(text), 2000, f"{name} tombstone is not small")


class FingerprintGuardTests(unittest.TestCase):
    def test_frozen_fingerprints_unchanged(self):
        data = json.loads(BASELINE_SUMMARY.read_text(encoding="utf-8"))
        self.assertEqual(
            data["outputs_sha256"],
            "7bed2ba862d91f82a0b7553e1a98fc78d9137483d39d94af0050af5aa18bdd33",
        )
        self.assertEqual(
            data["legacy_subset_sha256"],
            "a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc",
        )


if __name__ == "__main__":
    unittest.main()

"""Control-system regression tests: immutable experiment snapshots.

Milestone 2 (``Germanic/tools/experiment_snapshot.py``): an adjudication
experiment is pinned to a hashed, read-only copy of its inputs; later
production edits cannot change it; interrupted runs leave no
valid-looking completion receipt; a failed experiment cannot be recorded
as passed. These tests never compile the Germanic cascade and never touch
Docker (container staging is exercised with mocked subprocesses).
"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest import mock
import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
sys.path.insert(0, str(TOOLS))

import adjudication_control as ac  # noqa: E402
import experiment_snapshot as es  # noqa: E402


class SnapshotImmutabilityTests(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmpdir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.work_root = self.tmpdir / "experiments"
        self.fst = self.tmpdir / "germanic.txt"
        self.fst.write_text("define A a -> b;\n", encoding="utf-8")

    def _create(self, experiment_id="exp-001", **kwargs):
        return es.create_snapshot(
            experiment_id, "synthetic control-system test",
            {"germanic_fst": self.fst}, work_root=self.work_root, **kwargs)

    def test_duplicate_experiment_id_refused(self):
        """Concurrent or repeated experiments cannot silently share (and so
        corrupt) each other's recorded evidence."""
        self._create("exp-dup")
        with self.assertRaisesRegex(RuntimeError, "already exists"):
            self._create("exp-dup")

    def test_concurrent_experiments_have_disjoint_directories(self):
        first = self._create("exp-a")
        second = self._create("exp-b")
        self.assertNotEqual(first.root, second.root)
        self.assertFalse(set(first.root.parts) >= set(second.root.parts))
        # Completing one leaves the other's staging/results untouched.
        receipt = {"label": "probe", "ok": True, "returncode": 0}
        first.complete("passed", "done", command_receipts=[receipt])
        self.assertFalse(second.is_complete())

    def test_production_edit_does_not_reach_running_experiment(self):
        """Acceptance test: modify the production FST after the snapshot;
        the experiment's source is unchanged and its receipt identifies the
        original content."""
        snap = self._create()
        original_sha = snap.receipt()["inputs"]["germanic_fst"]["sha256"]
        pinned = snap.input_path("germanic_fst")
        before = pinned.read_text(encoding="utf-8")
        # Concurrent "production edit" in the ordinary working tree.
        self.fst.write_text("define A a -> c;  ! edited mid-experiment\n",
                            encoding="utf-8")
        self.assertEqual(pinned.read_text(encoding="utf-8"), before)
        self.assertEqual(snap.input_path("germanic_fst").read_text(
            encoding="utf-8"), before)
        self.assertEqual(snap.receipt()["inputs"]["germanic_fst"]["sha256"],
                         original_sha)

    def test_snapshot_records_source_identity_and_variants(self):
        snap = self._create(
            experiment_id="exp-ident",
            variants={"v1": "define X b -> c;"},
            probes=[{"input": "*ab", "expected": "ac"}],
            negative_controls=["*ad must not change"])
        receipt = snap.receipt()
        self.assertTrue(receipt["source_identity"]["head_commit"])
        self.assertTrue(receipt["source_identity"]["identity_sha256"])
        self.assertIn("v1", receipt["variant_sha256"])
        self.assertEqual(len(receipt["variant_sha256"]["v1"]), 64)
        self.assertFalse(receipt["environment"]["recorded"])

    def test_snapshot_files_are_read_only(self):
        snap = self._create(experiment_id="exp-ro")
        pinned = snap.input_path("germanic_fst")
        with self.assertRaises(PermissionError):
            pinned.open("w")

    def test_corrupted_snapshot_fails_closed(self):
        snap = self._create(experiment_id="exp-corrupt")
        pinned = snap.snapshot_dir / "germanic_fst.txt"
        pinned.chmod(0o644)
        pinned.write_text("tampered\n", encoding="utf-8")
        with self.assertRaises(RuntimeError) as ctx:
            snap.input_path("germanic_fst")
        self.assertIn("must not proceed", str(ctx.exception))

    def test_unsafe_identifiers_and_paths_rejected(self):
        for identifier in ("..", "../escape", "x;rm", "x y", "/tmp/x"):
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValueError):
                    self._create(experiment_id=identifier)
        snap = self._create()
        with self.assertRaises(ValueError):
            snap.stage_in_container(service="backend; false")

    @pytest.mark.runtime
    def test_existing_compiler_uses_pinned_source_after_production_edit(self):
        self.fst.write_text("define Tiny a -> b;\n")
        recipe = self.tmpdir / "recipe.json"
        recipe.write_text(json.dumps({
            "insert_rule": "", "definitions": "", "component_checks": [{"component": "Tiny"}]}))
        snap = es.create_snapshot(
            "pin-" + uuid.uuid4().hex, "compiled immutability control",
            {"germanic_fst": self.fst, "recipe": recipe}, work_root=self.work_root)
        self.fst.write_text("define Tiny a -> c;\n")
        result = snap.compile_isolated("germanic_fst", "recipe", components_only=True)
        try:
            lookup = subprocess.run(
                ["docker", "compose", "exec", "-T", "backend", "flookup", "-i",
                 result["bins"]["component:Tiny"]], input="a\n", text=True,
                capture_output=True, check=True, cwd=REPO_ROOT)
            self.assertIn("a\tb", lookup.stdout)
            self.assertNotIn("a\tc", lookup.stdout)
        finally:
            subprocess.run(
                ["docker", "compose", "exec", "-T", "backend", "chmod", "-R", "u+w",
                 result["container_source"]], check=True, cwd=REPO_ROOT)
            subprocess.run(
                ["docker", "compose", "exec", "-T", "backend", "rm", "-rf",
                 result["container_source"], result["container_output"]],
                check=True, cwd=REPO_ROOT)


class CompletionReceiptTests(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmpdir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        fst = self.tmpdir / "germanic.txt"
        fst.write_text("define A a -> b;\n", encoding="utf-8")
        self.snap = es.create_snapshot(
            "exp-complete", "completion tests", {"germanic_fst": fst},
            work_root=self.tmpdir / "experiments")
        self.log_dir = self.tmpdir / "logs"

    def _ok_receipt(self):
        return ac.run_logged([sys.executable, "-c", "print('ran')"],
                             label="probe", log_dir=self.log_dir)

    def _failed_receipt(self):
        return ac.run_logged([sys.executable, "-c", "raise SystemExit(3)"],
                             label="failing-probe", log_dir=self.log_dir)

    def test_interrupted_run_leaves_no_completion(self):
        (self.snap.staging_dir / "partial.json").write_text("{}")
        # Process dies here: no complete() call.
        self.assertFalse(self.snap.is_complete())
        self.assertFalse(self.snap.results_dir.exists())

    def test_failed_command_cannot_be_recorded_as_passed(self):
        with self.assertRaises(RuntimeError) as ctx:
            self.snap.complete("passed", "pretend success",
                              command_receipts=[self._failed_receipt()])
        self.assertIn("failures", str(ctx.exception))
        self.assertFalse(self.snap.is_complete())

    def test_passed_requires_an_execution_receipt(self):
        with self.assertRaises(RuntimeError) as ctx:
            self.snap.complete("passed", "no evidence")
        self.assertIn("command receipt", str(ctx.exception))

    def test_successful_completion_promotes_atomically(self):
        (self.snap.staging_dir / "report.json").write_text(
            json.dumps({"result": 1}))
        payload = self.snap.complete(
            "passed", "synthetic pass",
            command_receipts=[self._ok_receipt()])
        self.assertFalse(self.snap.staging_dir.exists())
        self.assertTrue((self.snap.results_dir / "report.json").is_file())
        self.assertIn("report.json", payload["result_hashes"])
        self.assertEqual(payload["source_identity_sha256"],
                         self.snap.receipt()["source_identity"]
                         ["identity_sha256"])
        # A second completion must be refused, not silently rewritten.
        with self.assertRaises(RuntimeError):
            self.snap.complete("passed", "again",
                               command_receipts=[self._ok_receipt()])

    def test_failed_outcome_is_recordable_honestly(self):
        payload = self.snap.complete(
            "failed", "negative control fired",
            command_receipts=[self._failed_receipt()])
        self.assertEqual(payload["outcome"], "failed")
        self.assertTrue(self.snap.is_complete())

    def test_unknown_outcome_rejected(self):
        with self.assertRaises(ValueError):
            self.snap.complete("sort-of-passed", "nope")


class ContainerStagingTests(unittest.TestCase):
    """Container staging verified with mocked subprocesses (no Docker)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmpdir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        fst = self.tmpdir / "germanic.txt"
        fst.write_text("define A a -> b;\n", encoding="utf-8")
        self.snap = es.create_snapshot(
            "exp-container", "container staging", {"germanic_fst": fst},
            work_root=self.tmpdir / "experiments")
        self.sha = self.snap.receipt()["inputs"]["germanic_fst"]["sha256"]

    def _completed(self, rc=0, stdout=""):
        return subprocess.CompletedProcess([], rc, stdout=stdout, stderr="")

    def test_verified_staging_succeeds(self):
        listing = f"{self.sha}  germanic_fst.txt\n"
        with mock.patch.object(es.subprocess, "run", side_effect=[
                self._completed(), self._completed(),
                self._completed(stdout=listing)]):
            path = self.snap.stage_in_container()
        self.assertTrue(path.startswith("/tmp/capr-exp-exp-container-"))

    def test_hash_mismatch_inside_container_fails_closed(self):
        listing = "deadbeef  germanic_fst.txt\n"
        with mock.patch.object(es.subprocess, "run", side_effect=[
                self._completed(), self._completed(),
                self._completed(stdout=listing)]):
            with self.assertRaises(RuntimeError) as ctx:
                self.snap.stage_in_container()
        self.assertIn("recorded hashes", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()

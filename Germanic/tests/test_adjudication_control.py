"""Control-system regression tests: preflight gate and reliable execution.

Milestone 1 of the adjudication workflow control system
(``Germanic/tools/adjudication_control.py``):

* a malformed finalisation request is rejected cheaply, BEFORE any Docker
  or Foma work starts, with an actionable diagnostic (including the exact
  indented ``Registry-verdict:`` defect);
* an investigation preflight does not demand a completed verdict;
* frozen ARCHIVE modifications and unapproved protected-baseline changes
  block every operation;
* ``run_logged`` records the true exit code and full logs, so filtered
  output can never conceal a failure;
* the runtime lock prevents concurrent mutation of shared runtime
  artifacts and ignores stale (dead-pid) locks.

These tests run without compiling the Germanic cascade: the runner probe
is disabled or monkeypatched throughout.
"""

import json
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
sys.path.insert(0, str(TOOLS))

import adjudicate  # noqa: E402
import adjudication_control as ac  # noqa: E402

VALID_MEMO = """# SC900 synthetic adjudication

## Identity
- **SC id:** SC900

## Question
x

## Current state (before any edits)
x

## Diagnosis
x

## Literature
x

## Historical analysis
x

## Verdict
x

Registry-verdict: SC900=RETAIN

## Propagation (only after verdict)
x

## Residue
x
"""

REGISTRY_HEADER = (
    "sc_id\tlifecycle_status\tentry_type\tpipeline_stage\tcanonical_change_id"
    "\tduplicate_group\tstaging_row\tfst_identifier\tdisplay_name"
    "\tinventory_display_name\tstage_label\thistorical_stage_label\thist_stage"
    "\thist_scope\tconfidence\tsource_reader_facing_file\tinclude_in_volume"
    "\tis_reader_facing\tadjudication_status\tverdict\tadjudication_memo"
    "\tchronology_profile\tchronology_card\tchronology_has_reciprocal_boundary"
    "\tchronology_summary\taction_status\tcapr_evidence\tchronology_problem"
    "\tstaging_notes"
)


def synthetic_registry(tmpdir: Path, *, verdict="RETAIN",
                       status="adjudicated", memo_text=VALID_MEMO,
                       fst_identifier="") -> Path:
    """One-row synthetic registry whose memo lives in *tmpdir*.

    *tmpdir* must be inside the repository (the gitignored
    ``.capr-work/test-fixtures/``) so registry pointers stay repo-relative,
    exactly like production rows.
    """
    memo = tmpdir / "sc900-adjudication.md"
    memo.write_text(memo_text, encoding="utf-8")
    registry = tmpdir / "sc_registry.tsv"
    row = {h: "" for h in REGISTRY_HEADER.split("\t")}
    row.update(sc_id="SC900", lifecycle_status="active",
               entry_type="historical_change", adjudication_status=status,
               verdict=verdict,
               adjudication_memo=str(memo.relative_to(REPO_ROOT)),
               fst_identifier=fst_identifier)
    registry.write_text(
        REGISTRY_HEADER + "\n"
        + "\t".join(row[h] for h in REGISTRY_HEADER.split("\t")) + "\n",
        encoding="utf-8")
    return registry


class PreflightGateTests(unittest.TestCase):
    """Cheap preflight rejection before any expensive work."""

    def setUp(self):
        import shutil
        import tempfile
        fixtures = REPO_ROOT / ".capr-work" / "test-fixtures"
        fixtures.mkdir(parents=True, exist_ok=True)
        self.tmpdir = Path(tempfile.mkdtemp(dir=fixtures))
        self.addCleanup(shutil.rmtree, self.tmpdir, True)
        # No preflight test may touch Docker or mutate the worktree model.
        patcher = mock.patch.object(
            ac, "worktree_changes", return_value=[])
        patcher.start()
        self.addCleanup(patcher.stop)

    def _patch_registry(self, registry: Path):
        patcher = mock.patch.object(adjudicate, "SC_REGISTRY", registry)
        patcher.start()
        self.addCleanup(patcher.stop)

    def _forbid_runner(self):
        def explode(*a, **k):  # pragma: no cover - failure path
            raise AssertionError(
                "expensive runner invoked during a preflight that must "
                "block first")
        import capr_runtime
        patcher = mock.patch.object(capr_runtime, "run_in_runner", explode)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_unknown_sc_blocks(self):
        report = ac.preflight("SC999", "investigate", probe_runner=False)
        self.assertEqual(report.status, "BLOCKED")
        self.assertIn("not found", report.checks[0]["detail"])

    def test_valid_finalize_passes_without_runner(self):
        self._patch_registry(synthetic_registry(self.tmpdir))
        report = ac.preflight("SC900", "finalize", probe_runner=False)
        blocked = [c for c in report.checks if c["status"] == "BLOCKED"]
        self.assertEqual(blocked, [], blocked)
        self.assertEqual(report.status, "PASS")
        self.assertTrue(report.source["head_commit"])
        self.assertTrue(report.source["identity_sha256"])

    def test_indented_registry_verdict_blocks_before_docker(self):
        """Acceptance test: an incorrectly indented Registry-verdict line
        blocks finalisation before Docker/Foma, naming the exact defect."""
        memo = VALID_MEMO.replace("Registry-verdict: SC900=RETAIN",
                                  "    Registry-verdict: SC900=RETAIN")
        self._patch_registry(synthetic_registry(self.tmpdir, memo_text=memo))
        self._forbid_runner()
        report = ac.preflight("SC900", "finalize")
        self.assertEqual(report.status, "BLOCKED")
        verdict_check = [c for c in report.checks
                         if c["name"] == "memo_verdict"][0]
        self.assertEqual(verdict_check["status"], "BLOCKED")
        self.assertIn("indented", verdict_check["detail"])
        self.assertIn("column 0", verdict_check["detail"])

    def test_finalize_cli_blocks_before_refresh(self):
        """adjudicate.finalize() must not reach the artifact graph when the
        preflight is blocked."""
        memo = VALID_MEMO.replace("Registry-verdict: SC900=RETAIN",
                                  "    Registry-verdict: SC900=RETAIN")
        self._patch_registry(synthetic_registry(self.tmpdir, memo_text=memo))
        self._forbid_runner()
        import artifact_graph
        with mock.patch.object(
                artifact_graph, "refresh",
                side_effect=AssertionError("refresh ran despite blocked "
                                           "preflight")):
            rc = adjudicate.finalize("SC900")
        self.assertEqual(rc, 1)

    def test_bad_verdict_token_blocks(self):
        self._patch_registry(
            synthetic_registry(self.tmpdir, verdict="RETAIN/FROBNICATE"))
        report = ac.preflight("SC900", "finalize", probe_runner=False)
        self.assertEqual(report.status, "BLOCKED")
        detail = [c for c in report.checks
                  if c["name"] == "verdict_vocabulary"][0]["detail"]
        self.assertIn("FROBNICATE", detail)

    def test_missing_memo_section_blocks_finalize(self):
        memo = VALID_MEMO.replace("## Residue\nx\n", "")
        self._patch_registry(synthetic_registry(self.tmpdir, memo_text=memo))
        report = ac.preflight("SC900", "finalize", probe_runner=False)
        sections = [c for c in report.checks if c["name"] == "memo_sections"][0]
        self.assertEqual(sections["status"], "BLOCKED")
        self.assertIn("Residue", sections["detail"])

    def test_investigation_does_not_require_verdict(self):
        self._patch_registry(
            synthetic_registry(self.tmpdir, verdict="", status="pending"))
        report = ac.preflight("SC900", "investigate", probe_runner=False)
        self.assertEqual(report.status, "PASS")
        verdict_check = [c for c in report.checks
                         if c["name"] == "verdict_vocabulary"][0]
        self.assertEqual(verdict_check["status"], "NOT_APPLICABLE")

    def test_evidence_requires_live_fst_identifier(self):
        self._patch_registry(
            synthetic_registry(self.tmpdir, fst_identifier="NoSuchRuleXyz"))
        report = ac.preflight("SC900", "evidence", probe_runner=False)
        ident = [c for c in report.checks if c["name"] == "fst_identifier"][0]
        self.assertEqual(ident["status"], "BLOCKED")
        self.assertIn("NoSuchRuleXyz", ident["detail"])

    def test_modified_archive_blocks(self):
        import artifact_graph
        archive_rel = str(
            artifact_graph.ARCHIVE_PATHS[0].relative_to(ac.REPO_ROOT))
        self._patch_registry(synthetic_registry(self.tmpdir))
        with mock.patch.object(ac, "worktree_changes",
                               return_value=[archive_rel]):
            report = ac.preflight("SC900", "investigate", probe_runner=False)
        frozen = [c for c in report.checks if c["name"] == "archive_frozen"][0]
        self.assertEqual(frozen["status"], "BLOCKED")
        self.assertIn(archive_rel, frozen["detail"])

    def test_unapproved_baseline_change_blocks(self):
        baseline_rel = str(
            adjudicate.BASELINE_SUMMARY.relative_to(ac.REPO_ROOT))
        self._patch_registry(synthetic_registry(self.tmpdir))
        with mock.patch.object(ac, "worktree_changes",
                               return_value=[baseline_rel]):
            report = ac.preflight("SC900", "investigate", probe_runner=False)
        protected = [c for c in report.checks
                     if c["name"] == "protected_baselines"][0]
        self.assertEqual(protected["status"], "BLOCKED")

    def test_runtime_conflict_blocks_finalize(self):
        self._patch_registry(synthetic_registry(self.tmpdir))
        holder = {"pid": os.getpid() + 0, "operation": "evidence SC001"}
        # A live foreign holder: fake a different live pid via the holder API.
        with mock.patch.object(ac, "runtime_lock_holder",
                               return_value={"pid": 99999999,
                                             "operation": "evidence SC001"}):
            report = ac.preflight("SC900", "finalize", probe_runner=False)
        conflict = [c for c in report.checks
                    if c["name"] == "runtime_conflict"][0]
        self.assertEqual(conflict["status"], "BLOCKED")
        del holder

    def test_report_json_shape(self):
        self._patch_registry(synthetic_registry(self.tmpdir))
        report = ac.preflight("SC900", "finalize", probe_runner=False)
        payload = report.to_json()
        self.assertEqual(payload["sc_id"], "SC900")
        self.assertEqual(payload["operation"], "finalize")
        self.assertIn(payload["status"], {"PASS", "BLOCKED"})
        self.assertTrue(all({"name", "status", "detail"} <= set(c)
                            for c in payload["checks"]))
        json.dumps(payload)  # serialisable


class RunLoggedTests(unittest.TestCase):
    """True exit codes and full logs; no shell-pipeline masking."""

    def setUp(self):
        import tempfile
        self._tmp = tempfile.TemporaryDirectory()
        self.log_dir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_success_receipt(self):
        receipt = ac.run_logged([sys.executable, "-c", "print('fine')"],
                                label="ok", log_dir=self.log_dir)
        self.assertTrue(receipt["ok"])
        self.assertEqual(receipt["returncode"], 0)
        self.assertIn("fine", Path(receipt["stdout_log"]).read_text())
        saved = json.loads(Path(receipt["receipt_path"]).read_text())
        self.assertEqual(saved["returncode"], 0)

    def test_failure_cannot_be_concealed_by_output(self):
        """A validator that prints success-looking text but exits nonzero is
        recorded as failed, with the full log preserved (acceptance test for
        filtered-output masking)."""
        receipt = ac.run_logged(
            [sys.executable, "-c",
             "print('ALL CHECKS PASSED'); raise SystemExit(7)"],
            label="masked-failure", log_dir=self.log_dir)
        self.assertFalse(receipt["ok"])
        self.assertEqual(receipt["returncode"], 7)
        self.assertIn("ALL CHECKS PASSED",
                      Path(receipt["stdout_log"]).read_text())

    def test_shell_strings_rejected(self):
        with self.assertRaises(TypeError):
            ac.run_logged("true | tail -1", label="bad",
                          log_dir=self.log_dir)

    def test_stderr_captured_separately(self):
        receipt = ac.run_logged(
            [sys.executable, "-c",
             "import sys; sys.stderr.write('boom\\n'); raise SystemExit(2)"],
            label="stderr", log_dir=self.log_dir)
        self.assertEqual(receipt["returncode"], 2)
        self.assertIn("boom", Path(receipt["stderr_log"]).read_text())


class RuntimeLockTests(unittest.TestCase):

    def setUp(self):
        import tempfile
        self._tmp = tempfile.TemporaryDirectory()
        tmpdir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.lock_path = tmpdir / "runtime-runner.lock"
        patcher = mock.patch.object(ac, "RUNTIME_LOCK", self.lock_path)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_lock_acquired_and_released(self):
        with ac.runtime_lock("evidence SC900"):
            record = json.loads(self.lock_path.read_text())
            self.assertEqual(record["pid"], os.getpid())
            self.assertEqual(record["operation"], "evidence SC900")
        self.assertFalse(self.lock_path.exists())

    def test_live_foreign_holder_blocks(self):
        with mock.patch.object(
                ac, "runtime_lock_holder",
                return_value={"pid": 4242, "operation": "finalize SC001",
                              "acquired_at": "t"}):
            with self.assertRaises(RuntimeError) as ctx:
                ac.runtime_lock("evidence SC900").__enter__()
        self.assertIn("4242", str(ctx.exception))

    def test_stale_dead_pid_lock_ignored(self):
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        # A pid that cannot be alive: beyond pid_max on supported platforms.
        self.lock_path.write_text(json.dumps(
            {"pid": 2 ** 22 + 12345, "operation": "ghost"}))
        with mock.patch.object(ac, "_pid_alive", return_value=False):
            self.assertIsNone(ac.runtime_lock_holder())
            with ac.runtime_lock("evidence SC900"):
                record = json.loads(self.lock_path.read_text())
                self.assertEqual(record["pid"], os.getpid())

    def test_corrupt_lock_treated_as_absent(self):
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        self.lock_path.write_text("{not json")
        self.assertIsNone(ac.runtime_lock_holder())


if __name__ == "__main__":
    unittest.main()

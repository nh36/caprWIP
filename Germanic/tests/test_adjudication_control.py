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
import subprocess
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

    def test_accepted_sc112_legacy_memo_passes(self):
        report = ac.preflight("SC112", "finalize", probe_runner=False)
        self.assertFalse(report.blocked, report.render())

    def test_new_or_edited_memo_still_requires_template(self):
        self._patch_registry(synthetic_registry(self.tmpdir, memo_text=VALID_MEMO.replace("## Diagnosis\n", "")))
        report = ac.preflight("SC900", "finalize", probe_runner=False)
        self.assertTrue(any(c["name"] == "memo_sections" and c["status"] == "BLOCKED"
                            for c in report.checks))

    def test_approval_filename_does_not_authorise_baseline_edit(self):
        self._patch_registry(synthetic_registry(self.tmpdir))
        rel = str(adjudicate.BASELINE_SUMMARY.relative_to(REPO_ROOT))
        with mock.patch.object(ac, "worktree_changes", return_value=[
                rel, str(Path(rel).with_name("approved_bogus_migration.json"))]):
            report = ac.preflight("SC900", "finalize", probe_runner=False)
        self.assertTrue(any(c["name"] == "protected_baselines" and c["status"] == "BLOCKED"
                            for c in report.checks))
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

    def test_repeated_labels_preserve_unique_logs_and_receipts(self):
        first = ac.run_logged([sys.executable, "-c", "print('first')"],
                              label="repeat", log_dir=self.log_dir)
        second = ac.run_logged([sys.executable, "-c", "print('second')"],
                               label="repeat", log_dir=self.log_dir)
        self.assertNotEqual(first["receipt_path"], second["receipt_path"])
        self.assertIn("first", Path(first["stdout_log"]).read_text())
        ac.verify_receipt(first)
        ac.verify_receipt(second)

    def test_source_changes_during_execution_are_detected(self):
        identities = [{"identity_sha256": "a" * 64}, {"identity_sha256": "b" * 64}]
        with mock.patch.object(ac, "source_identity", side_effect=identities):
            receipt = ac.run_logged([sys.executable, "-c", "pass"],
                                    label="changes", log_dir=self.log_dir)
        self.assertTrue(receipt["source_changed"])
        self.assertTrue(receipt["ok"])  # execution succeeded; validation is not certified
        with self.assertRaisesRegex(ValueError, "source identity changed"):
            ac.verify_receipt(receipt)

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

    def test_cli_evidence_dispatch_reaches_preflight(self):
        """Regression: a local variable in main()'s --run parsing must not
        shadow the module-level evidence() dispatch (UnboundLocalError)."""
        completed = subprocess.run(
            [sys.executable, str(TOOLS / "adjudicate.py"), "SC999",
             "--evidence"], capture_output=True, text=True, timeout=120)
        combined = completed.stdout + completed.stderr
        self.assertNotIn("UnboundLocalError", combined)
        self.assertEqual(completed.returncode, 1)
        self.assertIn("SC999", combined)

    def test_stderr_captured_separately(self):
        receipt = ac.run_logged(
            [sys.executable, "-c",
             "import sys; sys.stderr.write('boom\\n'); raise SystemExit(2)"],
            label="stderr", log_dir=self.log_dir)
        self.assertEqual(receipt["returncode"], 2)
        self.assertIn("boom", Path(receipt["stderr_log"]).read_text())

    def test_downstream_filter_cannot_mask_validator_failure(self):
        """Acceptance (brief section 7): a validator fails while its output
        is filtered through another command. Because each step runs under
        run_logged with its own receipt, the controller still holds the
        validator's original exit code and full log; the filter's success
        cannot overwrite them."""
        validator = ac.run_logged(
            [sys.executable, "-c",
             "print('line1'); print('FAIL: witness lost'); "
             "raise SystemExit(5)"],
            label="validator", log_dir=self.log_dir)
        # The "| tail -1"-style filtering happens on the captured log,
        # as a separate receipted step that succeeds.
        filter_step = ac.run_logged(
            [sys.executable, "-c",
             "import sys; print(open(sys.argv[1]).read().splitlines()[-1])",
             validator["stdout_log"]],
            label="filter", log_dir=self.log_dir)
        self.assertTrue(filter_step["ok"])
        self.assertFalse(validator["ok"])
        self.assertEqual(validator["returncode"], 5)
        full_log = Path(validator["stdout_log"]).read_text()
        self.assertIn("line1", full_log)
        self.assertIn("FAIL: witness lost", full_log)


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
        self.assertIsNone(ac.runtime_lock_holder())

    def test_live_foreign_holder_blocks(self):
        with ac.runtime_lock("finalize SC001"):
            with self.assertRaises(RuntimeError) as ctx:
                ac.runtime_lock("evidence SC900").__enter__()
        self.assertIn("finalize SC001", str(ctx.exception))

    def test_simultaneous_cross_process_acquisition(self):
        code = (
            "import sys,time; from pathlib import Path; "
            "sys.path.insert(0,sys.argv[1]); import adjudication_control as ac; "
            "ac.RUNTIME_LOCK=Path(sys.argv[2]); sys.stdin.readline();\n"
            "try:\n"
            " with ac.runtime_lock('child'):\n"
            "  print('ACQUIRED',flush=True); time.sleep(1)\n"
            "except RuntimeError:\n"
            " print('BLOCKED',flush=True); sys.exit(3)\n")
        children = [subprocess.Popen(
            [sys.executable, "-c", code, str(TOOLS), str(self.lock_path)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for _ in range(2)]
        try:
            for child in children:
                child.stdin.write("go\n")
                child.stdin.flush()
            outputs = [child.communicate(timeout=10) for child in children]
            self.assertEqual(sorted(child.returncode for child in children), [0, 3])
            self.assertEqual(sorted(out.strip() for out, _ in outputs), ["ACQUIRED", "BLOCKED"])
        finally:
            for child in children:
                if child.poll() is None:
                    child.terminate()
                    child.wait()

    def test_standalone_refresh_uses_runtime_lock_without_nesting(self):
        with ac.runtime_lock("other"):
            with mock.patch.object(adjudicate, "_refresh_unlocked") as refresh:
                self.assertEqual(adjudicate.refresh(), 1)
                refresh.assert_not_called()

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


class GraphOwnershipTests(unittest.TestCase):
    def test_index_overrides_are_source_inputs_not_generated_outputs(self):
        import artifact_graph
        path = artifact_graph.BOOK_DIR / "index_verborum_overrides.tsv"
        outputs = {p.resolve() for node in artifact_graph.nodes(mode="portable")
                   for p in node.outputs()}
        self.assertNotIn(path.resolve(), outputs)
        self.assertIn((artifact_graph.BOOK_DIR / "index_verborum_forms.tsv").resolve(), outputs)
        self.assertEqual(artifact_graph.propagation_path_kind(
            path, generated=outputs), "SOURCE")

    def test_lexeme_output_ownership_does_not_require_refreshed_citation_reports(self):
        import artifact_graph
        import oe_derivation_report_with_lexeme_reports
        publication = next(node for node in artifact_graph.nodes(mode="portable")
                           if node.name == "lexeme_publication")
        with mock.patch.object(oe_derivation_report_with_lexeme_reports, "render",
                               side_effect=ValueError("stale lexical reports")):
            self.assertEqual(len(publication.outputs()), 5)
            with self.assertRaisesRegex(ValueError, "stale lexical reports"):
                publication.build()

    def test_reader_output_ownership_does_not_require_a_fresh_manifest(self):
        import artifact_graph
        import build_reader_book
        reader = next(node for node in artifact_graph.nodes(mode="portable")
                      if node.name == "reader_book")
        with mock.patch.object(build_reader_book, "load_manifest",
                               side_effect=ValueError("Reader manifest is stale")):
            self.assertEqual(set(reader.outputs()), {
                build_reader_book.OUT_MD, build_reader_book.OUT_COVERAGE})
            with self.assertRaisesRegex(ValueError, "manifest is stale"):
                reader.build()


if __name__ == "__main__":
    unittest.main()

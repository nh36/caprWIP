"""Tests for the durable adjudication workflow journal (adjudication_run).

All tests are synthetic: dependency domains are redirected to temp files,
source identity is stubbed, and no Docker, Foma or real registry access
occurs.  They demonstrate the Milestone 3 guarantees:

* an interrupted run resumes without rerunning validated evidence when
  inputs are unchanged, and invalidates it when the FST changed;
* invalidation is selective (memo edits never invalidate Foma evidence);
* the scientific gate: failing required negative controls or
  unacknowledged counterexamples cannot be recorded as resolved;
* VALIDATE requires honest receipts against the current source identity.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import adjudication_run as ar  # noqa: E402
import adjudication_control as ac  # noqa: E402

SC = "SC901"

DECISION = {
    "historical_phenomenon": "test phenomenon",
    "conditioning": "test conditioning",
    "executable_implementation": "defTest",
    "selected_input_assumptions": "none",
    "firing_census": {"fires": 3},
    "positive_witnesses": ["w1"],
    "negative_controls": [{"description": "no overgeneration",
                           "required": True, "passed": True}],
    "counterfactual_results": ["cf1"],
    "literature_support": [{"ref": "X 1990: 12", "verified": True}],
    "historical_vs_modelling": "historical",
    "unresolved": [],
    "verdict": "RETAIN",
    "intended_source_modifications": "none",
}


class RunHarness(unittest.TestCase):
    """Shared synthetic environment for workflow tests."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="capr-run-test-"))
        self.runs = self.tmp / "runs"
        self.files = {}
        for domain in ("executable_model", "corpus", "registry", "memo"):
            path = self.tmp / f"{domain}.txt"
            path.write_text(f"{domain} v1\n", encoding="utf-8")
            self.files[domain] = path
        patches = [
            mock.patch.object(ar, "_domain_files",
                              lambda domain, sc: [self.files[domain]]),
            mock.patch.object(ac, "source_identity",
                              lambda: {"identity_sha256": "f" * 64,
                                       "head": "deadbeef", "dirty": []}),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def start(self):
        return ar.start(SC, runs_dir=self.runs)

    def load(self):
        return ar.load(SC, runs_dir=self.runs)

    def advance_to(self, run, last_stage, decision=None, receipts=None):
        for stage in ar.STAGES:
            evidence = None
            if stage == "DECIDE":
                evidence = decision or DECISION
            if stage == "VALIDATE":
                evidence = {"receipts": receipts or [{"label": "pytest",
                                                      "ok": True}]}
            run.complete_stage(stage, evidence=evidence)
            if stage == last_stage:
                return


class JournalLifecycleTests(RunHarness):

    def test_start_and_status(self):
        run = self.start()
        report = run.report()
        self.assertIn("INSPECT", report)
        self.assertIn("next permitted operation", report)
        self.assertEqual(run.frontier(), "INSPECT")
        self.assertTrue((run.root / "state.json").is_file())
        self.assertTrue(any(e["kind"] == "run_started"
                            for e in run.events()))

    def test_prerequisites_enforced_in_order(self):
        run = self.start()
        with self.assertRaisesRegex(ar.WorkflowError, "prerequisite INSPECT"):
            run.complete_stage("PREFLIGHT")

    def test_double_completion_rejected(self):
        run = self.start()
        run.complete_stage("INSPECT")
        with self.assertRaisesRegex(ar.WorkflowError, "already complete"):
            run.complete_stage("INSPECT")

    def test_second_start_blocked_while_active(self):
        self.start().complete_stage("INSPECT")
        with self.assertRaisesRegex(ar.WorkflowError, "active run"):
            self.start()

    def test_completed_run_is_archived_on_restart(self):
        run = self.start()
        self.advance_to(run, "COMPLETE")
        self.start()
        archived = list((self.runs / "archive").iterdir())
        self.assertEqual(len(archived), 1)
        self.assertEqual(self.load().frontier(), "INSPECT")

    def test_load_missing_run_is_actionable(self):
        with self.assertRaisesRegex(ar.WorkflowError, "--run start"):
            self.load()


class ResumeAndInvalidationTests(RunHarness):
    """Acceptance test for Milestone 3 (brief section 5)."""

    def test_resume_with_identical_inputs_keeps_evidence(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        # Simulate interruption: reload from disk in a fresh object.
        resumed = self.load()
        self.assertEqual(resumed.refresh_validity(), [])
        self.assertEqual(resumed.frontier(), "PROPAGATE")
        state = resumed.state()
        self.assertEqual(state["stages"]["INVESTIGATE"]["status"], "complete")

    def test_fst_change_invalidates_evidence_and_decision(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        self.files["executable_model"].write_text("edited\n", encoding="utf-8")
        resumed = self.load()
        invalidated = resumed.refresh_validity()
        self.assertEqual(sorted(invalidated), ["DECIDE", "INVESTIGATE"])
        state = resumed.state()
        self.assertEqual(state["stages"]["PREFLIGHT"]["status"], "complete")
        self.assertIn("executable_model",
                      state["stages"]["INVESTIGATE"]["invalidated_because"])

    def test_memo_edit_invalidates_only_preflight(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        self.files["memo"].write_text("reworded memo\n", encoding="utf-8")
        self.assertEqual(self.load().refresh_validity(), ["PREFLIGHT"])
        state = self.load().state()
        self.assertEqual(state["stages"]["INVESTIGATE"]["status"], "complete")
        self.assertEqual(state["stages"]["DECIDE"]["status"], "complete")

    def test_propagated_edit_does_not_retroinvalidate_decision(self):
        run = self.start()
        self.advance_to(run, "PROPAGATE")
        # Propagation deliberately changes the executable model.
        self.files["executable_model"].write_text("propagated\n",
                                                  encoding="utf-8")
        self.assertEqual(self.load().refresh_validity(), [])

    def test_validate_always_checked_against_current_tree(self):
        run = self.start()
        self.advance_to(run, "VALIDATE")
        self.files["executable_model"].write_text("late edit\n",
                                                  encoding="utf-8")
        self.assertEqual(self.load().refresh_validity(), ["VALIDATE"])

    def test_invalidated_stage_reported_as_blocker(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        self.files["executable_model"].write_text("edited\n", encoding="utf-8")
        report = self.load().report()
        self.assertIn("invalidated", report)
        self.assertIn("blockers", report)


class ScientificGateTests(RunHarness):

    def _ready(self):
        run = self.start()
        self.advance_to(run, "SNAPSHOT")
        run.complete_stage("INVESTIGATE")
        return run

    def test_decision_record_fields_required(self):
        run = self._ready()
        partial = {"verdict": "RETAIN"}
        with self.assertRaisesRegex(ar.WorkflowError, "missing"):
            run.complete_stage("DECIDE", evidence=partial)

    def test_controlled_verdict_vocabulary(self):
        run = self._ready()
        bad = dict(DECISION, verdict="MAYBE")
        with self.assertRaisesRegex(ar.WorkflowError, "controlled"):
            run.complete_stage("DECIDE", evidence=bad)

    def test_failing_required_negative_control_blocks_resolution(self):
        run = self._ready()
        bad = dict(DECISION, negative_controls=[
            {"description": "must not fire on strong verbs",
             "required": True, "passed": False}])
        with self.assertRaisesRegex(ar.WorkflowError, "negative control"):
            run.complete_stage("DECIDE", evidence=bad)

    def test_defer_is_legitimate_despite_failing_control(self):
        run = self._ready()
        deferred = dict(DECISION, verdict="DEFER", negative_controls=[
            {"description": "open counterexample", "required": True,
             "passed": False}])
        record = run.complete_stage("DECIDE", evidence=deferred)
        self.assertEqual(record["evidence"]["verdict"], "DEFER")

    def test_unacknowledged_counterexample_blocks_resolution(self):
        run = self._ready()
        bad = dict(DECISION, unresolved=["weorc fails SC-x"])
        with self.assertRaisesRegex(ar.WorkflowError, "counterexample"):
            run.complete_stage("DECIDE", evidence=bad)

    def test_acknowledged_counterexample_permits_resolution(self):
        run = self._ready()
        fine = dict(DECISION, unresolved=[
            {"item": "weorc", "acknowledged_in": "Residue"}])
        run.complete_stage("DECIDE", evidence=fine)
        self.assertEqual(run.frontier(), "PROPAGATE")


class ValidationReceiptTests(RunHarness):

    def _at_validate(self):
        run = self.start()
        self.advance_to(run, "PROPAGATE")
        return run

    def test_validate_requires_receipts(self):
        run = self._at_validate()
        with self.assertRaisesRegex(ar.WorkflowError, "receipts"):
            run.complete_stage("VALIDATE", evidence={})

    def test_failing_receipt_cannot_be_recorded_as_passed(self):
        run = self._at_validate()
        with self.assertRaisesRegex(ar.WorkflowError, "failures"):
            run.complete_stage("VALIDATE", evidence={"receipts": [
                {"label": "pytest-strict", "ok": False}]})

    def test_stale_source_identity_rejected(self):
        run = self._at_validate()
        with self.assertRaisesRegex(ar.WorkflowError, "modified source"):
            run.complete_stage("VALIDATE", evidence={"receipts": [
                {"label": "pytest-strict", "ok": True,
                 "source_identity_sha256": "0" * 64}]})

    def test_matching_receipts_complete_validate(self):
        run = self._at_validate()
        run.complete_stage("VALIDATE", evidence={"receipts": [
            {"label": "pytest-strict", "ok": True,
             "source_identity_sha256": "f" * 64}]})
        self.assertEqual(run.frontier(), "COMPLETE")


class JournalMetadataTests(RunHarness):

    def test_scientific_reference_state_recorded(self):
        run = self.start()
        ar.set_scientific_reference(run, "0080a190",
                                    "last scientifically accepted baseline")
        state = run.state()
        self.assertEqual(state["scientific_reference_state"]["commit"],
                         "0080a190")
        self.assertTrue(any(e["kind"] == "scientific_reference_set"
                            for e in run.events()))

    def test_comparison_recording_and_vocabulary(self):
        run = self.start()
        ar.record_comparison(run, kind="incremental_regression",
                             compared={"base": "HEAD~1", "target": "HEAD"})
        events = [e for e in run.events()
                  if e["kind"] == "comparison_performed"]
        self.assertEqual(events[0]["compared"]["target"], "HEAD")
        with self.assertRaises(ar.WorkflowError):
            ar.record_comparison(run, kind="vibes", compared={})

    def test_incremental_regression_result_recorded_verbatim(self):
        """An editorial commit's comparison is journaled with the exact
        resolved states, basis and zero Foma invocations."""
        run = self.start()
        result = {"states": {"current": "a" * 12, "reference": "b" * 12,
                             "basis": "HEAD vs first parent (HEAD^1)"},
                  "identical": True, "foma_invocations": 0,
                  "limitations": []}
        ar.record_incremental_regression(run, result)
        event = [e for e in run.events()
                 if e["kind"] == "comparison_performed"][0]
        self.assertEqual(event["comparison"], "incremental_regression")
        self.assertIn("first parent", event["compared"]["basis"])
        self.assertEqual(event["receipt"]["foma_invocations"], 0)

    def test_incremental_regression_requires_resolved_states(self):
        run = self.start()
        with self.assertRaisesRegex(ar.WorkflowError, "run_comparison"):
            ar.record_incremental_regression(run, {"identical": True})

    def test_validation_level_separates_executed_from_reused(self):
        run = self.start()
        ar.record_validation_level(
            run, "B",
            receipts=[{"label": "artifact-graph-verify", "ok": True,
                       "returncode": 0}],
            reused_evidence=[{"check": "runtime-trace",
                              "basis": "fresh provenance recorded in "
                                       "oe_full_trace_report PROVENANCE"}])
        event = [e for e in run.events()
                 if e["kind"] == "validation_level"][0]
        self.assertEqual(event["level"], "B")
        self.assertEqual([r["label"] for r in event["executed"]],
                         ["artifact-graph-verify"])
        self.assertEqual([r["check"] for r in event["reused"]],
                         ["runtime-trace"])

    def test_reused_evidence_requires_a_basis(self):
        run = self.start()
        with self.assertRaisesRegex(ar.WorkflowError, "basis"):
            ar.record_validation_level(
                run, "C", receipts=[],
                reused_evidence=[{"check": "mystery pass"}])

    def test_validation_level_vocabulary(self):
        run = self.start()
        with self.assertRaisesRegex(ar.WorkflowError, "level"):
            ar.record_validation_level(run, "D", receipts=[])

    def test_events_are_append_only_history(self):
        run = self.start()
        run.complete_stage("INSPECT")
        kinds = [e["kind"] for e in run.events()]
        self.assertEqual(kinds, ["run_started", "stage_complete"])


class DomainDerivationTests(unittest.TestCase):
    """The domains derive from the existing v2 provenance contract."""

    def test_executable_model_matches_v2_contract(self):
        import oe_trace_parse
        files = {p.name for p in ar._domain_files("executable_model", SC)}
        expected = {Path(rel).name
                    for label, rel in oe_trace_parse.SOURCE_PATHS.items()
                    if label not in ("germanic-aligned-final.tsv",
                                     "entry_context_metadata.tsv")}
        self.assertEqual(files, expected)

    def test_corpus_domain_is_data_only(self):
        names = {p.name for p in ar._domain_files("corpus", SC)}
        self.assertEqual(names, {"germanic-aligned-final.tsv",
                                 "entry_context_metadata.tsv"})

    def test_unknown_domain_rejected(self):
        with self.assertRaises(ValueError):
            ar._domain_files("prose", SC)


if __name__ == "__main__":
    unittest.main()

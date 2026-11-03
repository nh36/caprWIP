"""Tests for the durable adjudication workflow journal (adjudication_run).

Tests use disposable SOURCE fixtures, with no production science edits or
Docker/Foma work. One integration test runs the real preflight, finalisation,
Git identity, locking and receipt paths, mocking only expensive graph work.
They demonstrate the Milestone 3 guarantees:

* an interrupted run resumes without rerunning validated evidence when
  inputs are unchanged, and invalidates it when the FST changed;
* invalidation is selective (memo edits never invalidate Foma evidence);
* the scientific gate: failing required negative controls or
  unacknowledged counterexamples cannot be recorded as resolved;
* VALIDATE requires honest receipts against the current source identity.
"""
import json
import hashlib
import copy
import csv
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock
from types import SimpleNamespace

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import artifact_graph as ag  # noqa: E402
import adjudication_run as ar  # noqa: E402
import adjudication_control as ac  # noqa: E402

REAL_SOURCE_IDENTITY = ac.source_identity
REAL_PREFLIGHT = ac.preflight

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
    "intended_source_modifications": {},
}


class RunHarness(unittest.TestCase):
    """Shared synthetic environment for workflow tests."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="capr-run-test-")).resolve()
        self.addCleanup(shutil.rmtree, self.tmp)
        self.runs = self.tmp / "runs"
        self.files = {}
        for domain, relative in {
                "executable_model": "Germanic/fsts/germanic.txt",
                "corpus": "Germanic/data/germanic-aligned-final.tsv",
                "registry": "Germanic/docs/sound_changes/registry/sc_registry.tsv",
                "memo": "Germanic/docs/sound_changes/audits/sc901.md"}.items():
            path = self.tmp / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"{domain} v1\n", encoding="utf-8")
            self.files[domain] = path
        self.sc_dir = self.tmp / "Germanic/docs/sound_changes"
        shutil.copyfile(ag.SC_DIR / "registry/CONTROL_PLANE.md",
                        self.sc_dir / "registry/CONTROL_PLANE.md")
        self.entrypoint = self.tmp / "Germanic/tools/adjudicate.py"
        self.entrypoint.parent.mkdir()
        shutil.copyfile(TOOLS / "adjudicate.py", self.entrypoint)
        self.tests_dir = self.tmp / "Germanic/tests"
        self.tests_dir.mkdir()
        self.focused_test = self.tests_dir / "test_fixture.py"
        self.focused_test.write_text("def test_fixture():\n    assert True\n")
        patches = [
            mock.patch("artifact_graph.nodes", return_value=()),
            mock.patch.object(ag, "REPO_ROOT", self.tmp),
            mock.patch.object(ag, "SC_DIR", self.sc_dir),
            mock.patch.object(ag, "BASELINE_DIR", self.sc_dir / "cascade_baseline"),
            mock.patch.object(ar, "REPO_ROOT", self.tmp),
            mock.patch.object(ar, "_domain_files",
                              lambda domain, sc: [self.files[domain]]),
            mock.patch.object(ac, "source_identity", self.source_identity),
            mock.patch.object(ac, "preflight", side_effect=self.preflight),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def source_identity(self):
        changes = {p.relative_to(self.tmp).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted((self.tmp / "Germanic").rglob("*")) if p.is_file()}
        return {"identity_sha256": hashlib.sha256(json.dumps(changes, sort_keys=True).encode()).hexdigest(),
                "head_commit": "deadbeef", "worktree_changes": changes}

    def preflight(self, sc_id, operation, **kwargs):
        return ac.PreflightReport(sc_id, operation, source=ac.source_identity())

    def start(self):
        return ar.start(SC, runs_dir=self.runs)

    def load(self):
        return ar.load(SC, runs_dir=self.runs)

    def advance_to(self, run, last_stage, decision=None, receipts=None):
        for stage in ar.STAGES:
            evidence = None
            if stage == "DECIDE":
                evidence = decision or DECISION
            if stage == "SNAPSHOT":
                evidence = {"no_executable_experiment": "synthetic journal-only test"}
            if stage == "PROPAGATE":
                run.begin_propagation({})
                evidence = {"receipts": [self.receipt(
                    [sys.executable, str(self.entrypoint), SC, "--finalize"])]}
            if stage == "VALIDATE":
                evidence = {"receipts": receipts or self.validation_receipts()}
            run.complete_stage(stage, evidence=evidence)
            if stage == last_stage:
                return

    def receipt(self, argv=None, level=None, lane=None, rc=0, cwd=None, output=None):
        def execute(argv, **kwargs):
            text = output or ("CONTROL PLANE CLEAN\n" if "--refresh" in argv
                      else "STATUS OK (scientific/publication axes consistent)\n" if "--status" in argv
                      else "Reader-facing semantic regression suite passed.\n"
                      if str(self.entrypoint.with_name("check_reader_facing_semantics.py")) in argv
                      else "2 passed, 5 skipped\n")
            kwargs["stdout"].write(text.encode())
            for arg in argv:
                if arg.startswith("--junitxml="):
                    Path(arg.split("=", 1)[1]).write_text(
                        '<testsuites><testsuite tests="7" failures="0" errors="0" skipped="5"/></testsuites>')
            return subprocess.CompletedProcess(argv, rc)
        with mock.patch.object(ac.subprocess, "run", side_effect=execute):
            return ac.run_logged(argv or [sys.executable, "-c", "pass"],
                                 label="test", log_dir=self.tmp / "logs", cwd=cwd or self.tmp,
                                 level=level, lane=lane)

    def validation_receipts(self):
        return [self.receipt([sys.executable, "-m", "pytest", "-q", str(self.focused_test)], "A"),
                self.receipt([sys.executable, str(self.entrypoint), "--refresh"], "B"),
                self.receipt([sys.executable, str(self.entrypoint), "--status"], "B"),
                self.receipt([sys.executable, "-m", "pytest", "-q",
                              "--ignore=test_evidence_interface.py"], "C", "serial"),
                self.receipt([sys.executable, "-m", "pytest", "-q",
                              "test_evidence_interface.py"], "C", "exclusive")]


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

    def test_snapshot_stage_requires_real_verified_inputs(self):
        run = self.start()
        self.advance_to(run, "PREFLIGHT")
        with self.assertRaisesRegex(ar.WorkflowError, "real verified snapshot"):
            run.complete_stage("SNAPSHOT", evidence={})
        import experiment_snapshot
        snapshot = experiment_snapshot.create_snapshot(
            "real-inputs", "synthetic snapshot gate",
            {"fst": self.files["executable_model"]}, work_root=self.tmp / "experiments")
        run.complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})

    def test_experiment_exception_requires_reason_and_cannot_cover_experiments(self):
        run = self.start()
        self.advance_to(run, "PREFLIGHT")
        with self.assertRaisesRegex(ar.WorkflowError, "documented reason"):
            run.complete_stage("SNAPSHOT", evidence={"no_executable_experiment": True})
        run.complete_stage("SNAPSHOT", evidence={"no_executable_experiment": "editorial adjudication"})
        with self.assertRaisesRegex(ar.WorkflowError, "no-experiment exception"):
            run.complete_stage("INVESTIGATE", evidence={"experiments": [{"ok": True}]})


class ControlledCellPropagationTests(RunHarness):
    def setUp(self):
        super().setUp()
        import cascade_baseline as baseline
        self.baseline = baseline
        self.directory = ag.BASELINE_DIR
        self.directory.mkdir()
        old = dict(row_id="1", concept="fixture", proto="*a", proto_norm="a",
                   fst_input="a", word_stress="stressed", phonological_finality="final",
                   counterpart="x", accepted="1", output_count="1", match="1", outputs="x")
        new = dict(old, proto="*ba", proto_norm="ba", fst_input="ba", counterpart="y", outputs="y")

        def candidate(row):
            lexical = baseline.projection_sha256([row], "proto_norm")
            return dict(records=[row], summary=dict(
                total_lexemes=1, accepted=1, rejected=0, matched=1, mismatched=0,
                ambiguous_outputs=0, legacy_subset_count=1, legacy_subset_sha256=lexical,
                lexical_outputs_sha256=lexical,
                outputs_sha256=baseline.projection_sha256([row], "fst_input")))

        previous, after = candidate(old), candidate(new)
        baseline.write_outputs(previous, self.directory)
        shutil.copyfile(self.directory / "cascade_baseline_outputs.tsv",
                        self.directory / "cascade_baseline_outputs_legacy380.tsv")
        fields = ("proto", "proto_norm", "fst_input", "counterpart", "outputs", "match")
        approval = dict(
            adjudication="SC902",
            adjudication_memo="Germanic/docs/sound_changes/audits/sc902-adjudication.md",
            previous_summary={k: previous["summary"][k] for k in (
                "outputs_sha256", "lexical_outputs_sha256", "legacy_subset_sha256")},
            legacy_archive_sha256=previous["summary"]["legacy_subset_sha256"],
            transition_id="fixture_cells",
            changes=[dict(row_id="1", before={k: old[k] for k in fields},
                          after={k: new[k] for k in fields})])
        migration = dict(
            row_id="1", concept="fixture", counterpart="x", new_counterpart="y",
            old_proto="*a", new_proto="*ba", old_outputs="x", new_outputs="y",
            adjudication_memo=approval["adjudication_memo"])
        self.ledger = self.directory / "approved_input_migrations.tsv"
        with self.ledger.open("w", newline="") as handle:
            csv.DictWriter(handle, list(migration), delimiter="\t", lineterminator="\n").writeheader()
        self.transition = dict(
            approval_filename="approved_fixture_cells_migration.json",
            approval=approval, candidate=after, migrations=[migration])

    def decision(self, **changes):
        return dict(DECISION, coordinated_adjudications=[SC, "SC902"],
                    cell_transition=self.transition, **changes)

    def test_reloaded_plan_and_fresh_candidate_have_identical_protected_bytes(self):
        reloaded = json.loads(json.dumps(self.transition, sort_keys=True))
        planned = ar._cell_transition_files(reloaded, self.directory)
        for path, data in planned.items():
            if path.name.startswith("approved_"):
                path.write_bytes(data)
        self.baseline.adopt_cell_baseline(
            self.transition["candidate"], self.directory, self.transition["approval"]
        )
        for path, data in planned.items():
            self.assertEqual(path.read_bytes(), data, path.name)

    def test_exact_protected_effects_require_the_existing_adopter_and_each_owner(self):
        original = (self.directory / "cascade_baseline_outputs.tsv").read_bytes()
        run = self.start()
        self.advance_to(run, "DECIDE", decision=self.decision())
        run.begin_propagation({})
        planned = ar._cell_transition_files(self.transition, self.directory)
        for path, data in planned.items():
            if path.name.startswith("approved_"):
                path.write_bytes(data)
        self.baseline.adopt_cell_baseline(
            self.transition["candidate"], self.directory, self.transition["approval"])
        self.assertEqual(
            (self.directory / "cascade_baseline_outputs_pre_sc902_fixture_cells.tsv").read_bytes(),
            original)
        self.assertEqual(
            (self.directory / "cascade_baseline_outputs_legacy380.tsv").read_bytes(), original)
        finalize = [self.receipt([sys.executable, str(self.entrypoint), sc, "--finalize"])
                    for sc in [SC, "SC902"]]
        with self.assertRaisesRegex(ar.WorkflowError, "adopt-cell-baseline"):
            run.complete_stage("PROPAGATE", evidence={"receipts": finalize})
        adopt = self.receipt([sys.executable, str(self.entrypoint), "SC902",
                              "--adopt-cell-baseline", "--approval",
                              self.transition["approval_filename"]])
        with self.assertRaisesRegex(ar.WorkflowError, "each SC-specific"):
            run.complete_stage("PROPAGATE", evidence={"receipts": [adopt, finalize[0]]})
        run.complete_stage("PROPAGATE", evidence={"receipts": [adopt, *finalize]})
        self.assertEqual(run.frontier(), "VALIDATE")

    def test_undeclared_drift_prior_approval_replacement_and_defer_fail_closed(self):
        for case in ("drift", "extra_migration", "old_approval", "unowned", "defer"):
            with self.subTest(case=case):
                transition = copy.deepcopy(self.transition)
                decision = self.decision()
                decision["cell_transition"] = transition
                if case == "drift":
                    transition["candidate"]["records"][0]["outputs"] = "undeclared"
                elif case == "extra_migration":
                    transition["migrations"].append(dict(transition["migrations"][0]))
                elif case == "old_approval":
                    (self.directory / transition["approval_filename"]).write_text("{}")
                elif case == "unowned":
                    decision["coordinated_adjudications"] = [SC]
                else:
                    decision["verdict"] = "DEFER"
                run = ar.start(SC, runs_dir=self.tmp / ("runs-" + case))
                with self.assertRaises(ar.WorkflowError):
                    self.advance_to(run, "DECIDE", decision=decision)
                (self.directory / transition["approval_filename"]).unlink(missing_ok=True)

    def test_earlier_migration_rows_cannot_be_dropped(self):
        with self.ledger.open("a", newline="") as handle:
            old = dict(self.transition["migrations"][0], row_id="older")
            csv.DictWriter(handle, list(old), delimiter="\t", lineterminator="\n").writerow(old)
        with self.assertRaisesRegex(ValueError, "preserve every earlier approval"):
            ar._cell_transition_files(self.transition, self.directory)

    def test_previous_approval_remains_frozen_during_an_otherwise_valid_transition(self):
        old_approval = self.directory / "approved_older_migration.json"
        old_approval.write_text("frozen receipt\n")
        run = self.start()
        self.advance_to(run, "DECIDE", decision=self.decision())
        run.begin_propagation({})
        old_approval.write_text("rewritten\n")
        self.assertFalse(run._sanctioned_changes(run.state()))
        with self.assertRaisesRegex(ar.WorkflowError, "unexpected edits"):
            run.complete_stage("PROPAGATE")

    def test_new_owned_outputs_follow_declared_source_changes_not_filename_guessing(self):
        run = self.start()
        path = self.files["corpus"]
        replacement = b"corpus v2\n"
        modifications = {str(path.relative_to(self.tmp)): hashlib.sha256(replacement).hexdigest()}
        self.advance_to(run, "DECIDE", decision=self.decision(
            intended_source_modifications=modifications))
        run.begin_propagation(modifications)
        path.write_bytes(replacement)
        generated = self.sc_dir / "new-owned-report.tsv"
        generated.write_text("owned output\n")
        with mock.patch.object(ag, "nodes", return_value=(
                SimpleNamespace(outputs=lambda: [generated]),)):
            self.assertTrue(run._sanctioned_changes(run.state()))
            (self.sc_dir / "similar-but-unowned-report.tsv").write_text("not owned\n")
            self.assertFalse(run._sanctioned_changes(run.state()))

    def test_declared_sidecars_and_shared_bibliography_do_not_admit_other_docs(self):
        for relative in (
                "docs/refs.bib", "Germanic/data/entry_stage_metadata.tsv",
                "Germanic/docs/lexeme_reports/model_entries/1-fixture.source_ledger.md"):
            self.assertEqual(ag.propagation_path_kind(
                self.tmp / relative, generated=set()), "SOURCE")
        self.assertEqual(ag.propagation_path_kind(
            self.tmp / "docs/unowned.md", generated=set()), "UNKNOWN")


class ResumeAndInvalidationTests(RunHarness):
    """Acceptance test for Milestone 3 (brief section 5)."""

    def test_graph_owned_regeneration_in_shared_executable_domain_is_sanctioned(self):
        generated = self.tmp / "Germanic/fsts/old_english_sandbox.txt"
        generated.write_text("generated v1\n")
        domain_files = lambda domain, sc: (
            [self.files[domain], generated]
            if domain == "executable_model" else [self.files[domain]]
        )
        with mock.patch.object(ar, "_domain_files", side_effect=domain_files), \
                mock.patch.object(ag, "nodes", return_value=(
                    SimpleNamespace(outputs=lambda: [generated]),)):
            run = self.start()
            self.advance_to(run, "DECIDE")
            run.begin_propagation({})
            generated.write_text("generated v2\n")
            self.assertTrue(run._sanctioned_changes(run.state()))
            self.assertEqual(run.refresh_validity(), [])
            self.files["corpus"].write_text("unapproved corpus change\n")
            self.assertFalse(run._sanctioned_changes(run.state()))

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
        target = self.files["executable_model"]
        target.write_text("define Tiny a -> b;\n")
        modifications = {str(target): hashlib.sha256(b"define Tiny a -> c;\n").hexdigest()}
        self.advance_to(run, "DECIDE", decision=dict(DECISION, intended_source_modifications=modifications))
        run.begin_propagation(modifications)
        target.write_text("define Tiny a -> c;\n", encoding="utf-8")
        self.assertEqual(self.load().refresh_validity(), [])
        run.complete_stage("PROPAGATE", evidence={"receipts": [
            self.receipt([sys.executable, str(self.entrypoint), SC, "--finalize"])]})
        self.assertEqual(self.load().refresh_validity(), [])

    def test_unexpected_edit_during_propagation_invalidates_evidence(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        run.begin_propagation({})
        self.files["executable_model"].write_text("unexpected\n")
        self.assertEqual(self.load().refresh_validity(), ["INVESTIGATE", "DECIDE"])
        with self.assertRaises(ar.WorkflowError):
            run.complete_stage("PROPAGATE")

    def test_defer_blocks_executable_propagation(self):
        run = self.start()
        modifications = {str(self.files["executable_model"]): "0" * 64}
        self.advance_to(run, "DECIDE", decision=dict(
            DECISION, verdict="DEFER", intended_source_modifications=modifications))
        with self.assertRaisesRegex(ar.WorkflowError, "DEFER"):
            run.begin_propagation(modifications)

    def test_defer_without_executable_edits_can_complete_propagation(self):
        run = self.start()
        self.advance_to(run, "PROPAGATE", decision=dict(DECISION, verdict="DEFER"))
        self.assertEqual(run.frontier(), "VALIDATE")

    def test_propagation_checks_must_succeed_and_match_target_hashes(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        run.begin_propagation({})
        with self.assertRaisesRegex(ar.WorkflowError, "receipt"):
            run.complete_stage("PROPAGATE", evidence={"receipts": [self.receipt(rc=1)]})
        self.assertEqual(run.frontier(), "PROPAGATE")

    def test_noop_and_unrelated_entry_points_cannot_attest_finalisation(self):
        unrelated = self.tmp / "other/adjudicate.py"
        unrelated.parent.mkdir()
        unrelated.write_text("pass\n")
        (self.tmp / "-m").symlink_to(self.entrypoint)
        (self.tmp / f"{SC}.py").write_text("pass\n")
        run = self.start()
        self.advance_to(run, "DECIDE")
        run.begin_propagation({})
        for argv in (
                [sys.executable, "-c", "pass", SC, "--finalize"],
                [sys.executable, "-c", "pass", str(self.entrypoint), SC, "--finalize"],
                [sys.executable, "-m", "unrelated", SC, "--finalize"],
                [sys.executable, str(unrelated), SC, "--finalize"],
                [sys.executable, str(self.entrypoint), "SC902", "--finalize"]):
            with self.subTest(argv=argv):
                receipt = self.receipt(argv)
                with mock.patch.object(ac, "preflight") as preflight:
                    with self.assertRaisesRegex(ar.WorkflowError, "SC-specific --finalize"):
                        run.complete_stage("PROPAGATE", evidence={"receipts": [receipt]})
                    preflight.assert_not_called()
        self.assertEqual(run.frontier(), "PROPAGATE")
        module_receipt = ac.run_logged(
            [sys.executable, "-m", SC, "--finalize"], label="unrelated-module",
            log_dir=self.tmp / "logs", cwd=self.tmp)
        self.assertEqual(module_receipt["returncode"], 0)
        with self.assertRaisesRegex(ar.WorkflowError, "SC-specific --finalize"):
            run.complete_stage("PROPAGATE", evidence={"receipts": [module_receipt]})

    def test_recorded_executable_uses_the_execution_path_not_the_controllers_path(self):
        fake_python = self.tmp / "bin/python3"
        fake_python.parent.mkdir()
        fake_python.write_text("#!/bin/sh\nprintf '2 passed\\nCONTROL PLANE CLEAN\\nSTATUS OK\\n'\n")
        fake_python.chmod(0o755)
        env = dict(os.environ, PATH=str(fake_python.parent))
        run = self.start()
        self.advance_to(run, "DECIDE")
        run.begin_propagation({})
        receipt = ac.run_logged(
            ["python3", str(self.entrypoint), SC, "--finalize"], label="masquerade",
            log_dir=self.tmp / "logs", cwd=self.tmp, env=env)
        self.assertEqual(receipt["returncode"], 0)
        self.assertEqual(receipt["executable_path"], str(fake_python))
        with self.assertRaisesRegex(ar.WorkflowError, "SC-specific --finalize"):
            run.complete_stage("PROPAGATE", evidence={"receipts": [receipt]})
        run.complete_stage("PROPAGATE", evidence={"receipts": [self.receipt(
            [sys.executable, str(self.entrypoint), SC, "--finalize"])]})
        for level, args, index in (
                ("A", ["-m", "pytest", str(self.focused_test)], 0),
                ("B", [str(self.entrypoint), "--refresh"], 1)):
            with self.subTest(level=level):
                receipts = self.validation_receipts()
                receipts[index] = ac.run_logged(
                    ["python3", *args], label=level, log_dir=self.tmp / "logs",
                    cwd=self.tmp, env=env, level=level)
                with self.assertRaisesRegex(ar.WorkflowError, f"Level {level} requires"):
                    run.complete_stage("VALIDATE", evidence={"receipts": receipts})

    def test_finalisation_accepts_resolved_aliases_and_python_options(self):
        alias = self.entrypoint.with_name("finalisation-alias.py")
        alias.symlink_to(self.entrypoint.name)
        run = self.start()
        self.advance_to(run, "DECIDE")
        run.begin_propagation({})
        receipt = self.receipt(
            [sys.executable, "-B", "./finalisation-alias.py", SC, "--finalize"],
            cwd=self.entrypoint.parent)
        run.complete_stage("PROPAGATE", evidence={"receipts": [receipt]})
        self.assertEqual(run.frontier(), "VALIDATE")

    def test_finalization_may_regenerate_authorised_graph_outputs(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        generated = ar.REPO_ROOT / ".capr-work/synthetic-generated.txt"
        with mock.patch("artifact_graph.nodes", return_value=(
                SimpleNamespace(outputs=lambda: [generated]),)):
            run.begin_propagation({})
        before = self.source_identity()
        after = dict(before, identity_sha256="a" * 64,
                     worktree_changes={**before["worktree_changes"],
                                       str(generated.relative_to(ar.REPO_ROOT)): "b" * 64})
        with mock.patch.object(ac, "source_identity", side_effect=[before, after]):
            receipt = self.receipt(
                [sys.executable, str(self.entrypoint), SC, "--finalize"])
        with mock.patch.object(ac, "source_identity", return_value=after):
            run.complete_stage("PROPAGATE", evidence={"receipts": [receipt]})
        self.assertEqual(run.frontier(), "VALIDATE")

    def test_validate_always_checked_against_current_tree(self):
        run = self.start()
        self.advance_to(run, "VALIDATE")
        self.files["executable_model"].write_text("late edit\n",
                                                  encoding="utf-8")
        self.assertEqual(self.load().refresh_validity(), ["INVESTIGATE", "DECIDE", "VALIDATE"])

    def test_invalidated_stage_reported_as_blocker(self):
        run = self.start()
        self.advance_to(run, "DECIDE")
        self.files["executable_model"].write_text("edited\n", encoding="utf-8")
        report = self.load().report()
        self.assertIn("invalidated", report)
        self.assertIn("blockers", report)


class ScholarlyPropagationTests(RunHarness):

    def prepare_edits(self, run, *, verdict="RETAIN"):
        reader = self.sc_dir / "reader_facing/0901-test.md"
        reader.parent.mkdir(exist_ok=True)
        reader.write_text("Existing reader discussion.\n")
        new_dossier = self.sc_dir / "book_dossiers/new-adjudication.md"
        new_dossier.parent.mkdir(exist_ok=True)
        self.edits = {**{p: f"{domain} propagated\n" for domain, p in self.files.items()
                         if domain != "corpus"},
                      reader: "Integrated reader discussion.\n",
                      new_dossier: "New source-backed dossier.\n"}
        if verdict == "DEFER":
            del self.edits[self.files["executable_model"]]
        modifications = {str(p.relative_to(self.tmp)): hashlib.sha256(text.encode()).hexdigest()
                         for p, text in self.edits.items()}
        self.advance_to(run, "DECIDE", decision=dict(
            DECISION, verdict=verdict, intended_source_modifications=modifications))
        run.begin_propagation(modifications)
        return reader, new_dossier

    def apply_edits(self):
        for path, text in self.edits.items():
            path.write_text(text)

    def finish_propagation(self, run):
        run.complete_stage("PROPAGATE", evidence={"receipts": [self.receipt(
            [sys.executable, str(self.entrypoint), SC, "--finalize"])]})

    def test_authorised_scholarly_sequence_preserves_investigation_and_validates(self):
        run = self.start()
        _, new_dossier = self.prepare_edits(run)
        before = run.state()["stages"]["PREFLIGHT"]
        self.assertEqual(run.state()["propagation"]["before"][str(new_dossier)], "absent")
        self.apply_edits()
        self.assertEqual(run.refresh_validity(), [])
        self.finish_propagation(run)
        state = run.state()
        self.assertEqual(state["stages"]["PREFLIGHT"], before)
        fresh = state["propagation"]["finalization_preflight"]
        self.assertEqual(fresh["operation"], "finalize")
        self.assertEqual(fresh["status"], ac.PASS)
        self.assertNotEqual(fresh["source_identity"]["identity_sha256"],
                            before["source_identity"]["identity_sha256"])
        run.complete_stage("VALIDATE", evidence={"receipts": self.validation_receipts()})
        self.assertEqual(run.refresh_validity(), [])
        self.assertEqual(run.frontier(), "COMPLETE")

    def test_unexpected_registry_model_and_document_edits_block_completion(self):
        for kind in ("registry", "executable_model", "document"):
            with self.subTest(kind=kind):
                run = self.start()
                self.prepare_edits(run)
                self.apply_edits()
                if kind == "document":
                    unexpected = self.sc_dir / "reader_facing/0902-unrelated.md"
                else:
                    unexpected = self.files[kind]
                unexpected.write_text("Not part of the authorised decision.\n")
                with self.assertRaises(ar.WorkflowError):
                    self.finish_propagation(run)
                self.assertNotEqual(run.state()["stages"].get("PROPAGATE", {}).get("status"),
                                    "complete")
                shutil.rmtree(self.runs)
                if kind == "document":
                    unexpected.unlink()

    def test_missing_or_wrong_new_document_hash_blocks_completion(self):
        for create in (False, True):
            with self.subTest(create=create):
                run = self.start()
                _, new_dossier = self.prepare_edits(run)
                self.apply_edits()
                if create:
                    new_dossier.write_text("Unapproved contents.\n")
                else:
                    new_dossier.unlink()
                with self.assertRaisesRegex(ar.WorkflowError, "target hashes"):
                    self.finish_propagation(run)
                shutil.rmtree(self.runs)

    def test_fresh_finalisation_preflight_is_required(self):
        run = self.start()
        self.prepare_edits(run)
        self.apply_edits()
        blocked = self.preflight(SC, "finalize")
        blocked.add("memo_verdict", ac.BLOCKED, "memo does not agree with registry")
        with mock.patch.object(ac, "preflight", return_value=blocked):
            with self.assertRaisesRegex(ar.WorkflowError, "finalisation preflight blocked"):
                self.finish_propagation(run)
        self.assertEqual(run.frontier(), "PROPAGATE")

    def test_defer_can_propagate_documentation_but_not_executable_changes(self):
        run = self.start()
        old_fst = self.files["executable_model"].read_bytes()
        self.prepare_edits(run, verdict="DEFER")
        self.apply_edits()
        self.finish_propagation(run)
        self.assertEqual(self.files["executable_model"].read_bytes(), old_fst)
        self.assertEqual(run.frontier(), "VALIDATE")

    def test_unapproved_document_change_invalidates_completed_validation(self):
        run = self.start()
        reader, _ = self.prepare_edits(run)
        self.apply_edits()
        self.finish_propagation(run)
        run.complete_stage("VALIDATE", evidence={"receipts": self.validation_receipts()})
        reader.write_text("Later unapproved reader change.\n")
        self.assertIn("VALIDATE", run.refresh_validity())
        run.refresh_validity()
        self.assertEqual(run.state()["stages"]["PREFLIGHT"]["status"], "complete")
        with self.assertRaises(ar.WorkflowError):
            run.complete_stage("COMPLETE")

    def test_unrelated_document_change_invalidates_completed_validation(self):
        run = self.start()
        self.advance_to(run, "VALIDATE")
        unrelated = self.sc_dir / "literature_dossiers/unrelated.md"
        unrelated.parent.mkdir()
        unrelated.write_text("Later unrelated scholarly source.\n")
        self.assertEqual(run.refresh_validity(), ["VALIDATE"])

    def test_generated_archived_protected_unknown_and_escaping_paths_rejected(self):
        paths = [self.sc_dir / "registry/sc_inventory_annotations.tsv",
                 self.sc_dir / "reader_facing/archive/0901-retired.md",
                 self.sc_dir / "cascade_baseline/cascade_baseline_summary.json",
                 self.tmp / "Germanic/docs/unknown-source.md",
                 self.tmp / "../outside-source.md"]
        generated = SimpleNamespace(outputs=lambda: [paths[0]])
        for path in paths:
            with self.subTest(path=path):
                run = self.start()
                modifications = {str(path): "a" * 64}
                self.advance_to(run, "DECIDE", decision=dict(
                    DECISION, intended_source_modifications=modifications))
                with mock.patch.object(ag, "nodes", return_value=[generated]):
                    with self.assertRaisesRegex(ar.WorkflowError, "authorised SOURCE"):
                        run.begin_propagation(modifications)
                shutil.rmtree(self.runs)

    def test_existing_source_map_covers_new_literature_and_model_documents(self):
        for relative in ("literature_dossiers/new.md", "literature_dossiers/topic/new.md",
                         "../lexeme_reports/model_entries/new.model.md"):
            with self.subTest(path=relative):
                self.assertEqual(ag.propagation_path_kind(
                    self.sc_dir / relative, generated=set()), "SOURCE")


class PropagationIntegrationTests(RunHarness):

    def test_real_finalisation_receipt_for_registry_memo_reader_and_new_dossier(self):
        import adjudicate as ad
        from test_adjudication_control import REGISTRY_HEADER, VALID_MEMO

        reader = self.sc_dir / "reader_facing/0901-test.md"
        dossier = self.sc_dir / "book_dossiers/sc901.md"
        reader.parent.mkdir()
        dossier.parent.mkdir()
        reader.write_text("Existing scholarly discussion.\n")
        self.files["executable_model"].write_text("define Tiny a -> b;\n")
        self.files["memo"].write_text("Pre-decision investigation notes.\n")
        row = dict.fromkeys(REGISTRY_HEADER.split("\t"), "")
        row.update(sc_id=SC, lifecycle_status="active", entry_type="historical_change",
                   fst_identifier="Tiny", adjudication_status="pending",
                   adjudication_memo=str(self.files["memo"].relative_to(self.tmp)),
                   source_reader_facing_file=str(reader.relative_to(self.tmp)))

        def registry_text(row):
            return REGISTRY_HEADER + "\n" + "\t".join(row[h] for h in row) + "\n"

        self.files["registry"].write_text(registry_text(row))
        tests = self.tests_dir
        (tests / "conftest.py").write_text(
            "def pytest_addoption(parser):\n"
            "    parser.addoption('--validation-mode', default='full')\n")
        (tests / "test_serial.py").write_text(
            "import pytest\n"
            "def test_fixture():\n    assert True\n"
            "@pytest.mark.parametrize('case', range(5))\n"
            "@pytest.mark.skip(reason='synthetic historical-replay exception')\n"
            "def test_historical_replay(case):\n    assert False\n")
        (tests / "test_evidence_interface.py").write_text(
            "def test_exclusive_fixture():\n    assert True\n")
        self.focused_test.write_text(
            "from pathlib import Path\n"
            "def test_propagated_source():\n"
            "    root = Path(__file__).resolve().parents[2]\n"
            "    assert (root / 'Germanic/fsts/germanic.txt').read_text() == 'define Tiny a -> c;\\n'\n"
            "    assert 'Registry-verdict: SC901=RETAIN' in "
            "(root / 'Germanic/docs/sound_changes/audits/sc901.md').read_text()\n"
            "    assert (root / 'Germanic/docs/sound_changes/book_dossiers/sc901.md').is_file()\n")
        (self.sc_dir / "registry/adjudication_programme.json").write_text(
            json.dumps({"start_sc": SC}))
        baseline = self.sc_dir / "cascade_baseline/cascade_baseline_summary.json"
        baseline.parent.mkdir()
        baseline.write_text(json.dumps({"total_lexemes": 1}))
        shutil.copyfile(ac.TEMPLATE, self.sc_dir / "audits/ADJUDICATION_TEMPLATE.md")
        (self.tmp / ".gitignore").write_text(
            ".capr-work/\nruns/\nlogs/\n.pytest_cache/\n__pycache__/\n")
        for args in (["init", "-q"], ["add", "."],
                     ["-c", "user.name=CAPR fixture", "-c", "user.email=fixture@example.invalid",
                      "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false",
                      "commit", "-qm", "Synthetic investigation fixture\n\n"
                      "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"]):
            subprocess.run(["git", *args], cwd=self.tmp, check=True, capture_output=True)

        patches = [
            mock.patch.object(ac, "source_identity", REAL_SOURCE_IDENTITY),
            mock.patch.object(ac, "preflight", REAL_PREFLIGHT),
            mock.patch.object(ac, "REPO_ROOT", self.tmp),
            mock.patch.object(ac, "WORK_DIR", self.tmp / ".capr-work"),
            mock.patch.object(ac, "RUNTIME_LOCK", self.tmp / ".capr-work/locks/runtime-runner.lock"),
            mock.patch.object(ag, "ARCHIVE_PATHS", ()),
            mock.patch.object(ad, "REPO_ROOT", self.tmp),
            mock.patch.object(ad, "SC_REGISTRY", self.files["registry"]),
            mock.patch.object(ad, "BASELINE_SUMMARY",
                              self.sc_dir / "cascade_baseline/cascade_baseline_summary.json"),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

        run = self.start()
        run.complete_stage("INSPECT")
        investigation = ac.preflight(SC, "investigate", probe_runner=False)
        self.assertFalse(investigation.blocked, investigation.render())
        run.complete_stage("PREFLIGHT", evidence=investigation.to_json())
        run.complete_stage("SNAPSHOT", evidence={
            "no_executable_experiment": "integration fixture; no counterfactual compilation"})
        run.complete_stage("INVESTIGATE", evidence={"fixture": "pre-change evidence"})
        row.update(adjudication_status="adjudicated", verdict="RETAIN",
                   capr_evidence=str(dossier.relative_to(self.tmp)))
        edits = {self.files["executable_model"]: "define Tiny a -> c;\n",
                 self.files["registry"]: registry_text(row),
                 self.files["memo"]: VALID_MEMO.replace("SC900", SC),
                 reader: "Existing scholarly discussion, integrated with the verdict.\n",
                 dossier: "New scholarly SOURCE dossier.\n"}
        modifications = {str(p.relative_to(self.tmp)): hashlib.sha256(text.encode()).hexdigest()
                         for p, text in edits.items()}
        run.complete_stage("DECIDE", evidence=dict(
            DECISION, intended_source_modifications=modifications))
        run.begin_propagation(modifications)
        old_preflight = run.state()["stages"]["PREFLIGHT"]
        for path, text in edits.items():
            path.write_text(text)
        self.assertEqual(run.refresh_validity(), [])

        # Python startup substitutions exist only in this disposable fixture;
        # receipts still invoke the unmodified repository entry point directly.
        substitutions = self.tmp / ".capr-work/substitutions"
        substitutions.mkdir(parents=True)
        (substitutions / "sitecustomize.py").write_text(f"""
from pathlib import Path
from subprocess import CompletedProcess
import adjudication_control as ac, artifact_graph as ag, generate_registry_views as views
import capr_runtime, pgmc_lexical_integration as pli
root = Path({str(self.tmp)!r})
ac.REPO_ROOT = ag.REPO_ROOT = root
ac.WORK_DIR = root / '.capr-work'
ac.RUNTIME_LOCK = ac.WORK_DIR / 'locks/runtime-runner.lock'
ac.TEMPLATE = root / 'Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md'
views.SC_REGISTRY = root / 'Germanic/docs/sound_changes/registry/sc_registry.tsv'
ag.ARCHIVE_PATHS = ()
ag._refresh_unlocked = lambda **kwargs: []
ag.verify_all = lambda **kwargs: []
capr_runtime.run_in_runner = lambda *args, **kwargs: CompletedProcess(args, 0, stdout='', stderr='')
pli.build = lambda: ([], [], {{
    'selected': 1, 'assembled': 1, 'required': 1, 'philological_selected': 0,
    'publication_selected_models': [], 'publication_missing_ledgers': [],
    'required_not_assembled': []
}})
""")
        env = dict(os.environ, PYTHONPATH=str(substitutions) + os.pathsep + str(TOOLS))
        receipt = ac.run_logged(
            [sys.executable, str(self.entrypoint), SC, "--finalize"],
            label="actual-finalization", log_dir=self.tmp / ".capr-work/logs", cwd=self.tmp, env=env)
        self.assertEqual(receipt["returncode"], 0, Path(receipt["stdout_log"]).read_text())
        ac.verify_receipt(receipt, allow_source_change=True)
        run.complete_stage("PROPAGATE", evidence={"receipts": [receipt]})
        state = run.state()
        self.assertEqual(state["stages"]["PREFLIGHT"], old_preflight)
        fresh = state["propagation"]["finalization_preflight"]
        self.assertEqual(fresh["source_identity"]["identity_sha256"],
                         receipt["source_identity_after"]["identity_sha256"])
        self.assertTrue(all(check["status"] != ac.BLOCKED for check in fresh["checks"]))

        receipts = [ac.run_logged(
            [sys.executable, "-m", "pytest", "-q", str(self.focused_test)], label="focused",
            log_dir=self.tmp / ".capr-work/logs", cwd=tests, level="A")]
        for operation in ("--refresh", "--status"):
            receipts.append(ac.run_logged(
                [sys.executable, str(self.entrypoint), operation], label=operation,
                log_dir=self.tmp / ".capr-work/logs", cwd=self.tmp, env=env, level="B"))
        for lane, args in (("serial", ["--ignore=test_evidence_interface.py"]),
                           ("exclusive", ["test_evidence_interface.py"])):
            receipts.append(ac.run_logged(
                [sys.executable, "-m", "pytest", "-q", *args], label=lane,
                log_dir=self.tmp / ".capr-work/logs", cwd=tests, level="C", lane=lane))
        run.complete_stage("VALIDATE", evidence={"receipts": receipts})
        self.assertEqual(run.refresh_validity(), [])
        self.assertEqual(run.frontier(), "COMPLETE")


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
        with self.assertRaisesRegex(ar.WorkflowError, "receipt"):
            run.complete_stage("VALIDATE", evidence={"receipts": [
                self.receipt(rc=7)]})

    def test_stale_source_identity_rejected(self):
        run = self._at_validate()
        with mock.patch.object(ac, "source_identity", return_value={"identity_sha256": "0" * 64}):
            stale = self.receipt()
        with self.assertRaisesRegex(ar.WorkflowError, "stale source"):
            run.complete_stage("VALIDATE", evidence={"receipts": [
                stale]})

    def test_matching_receipts_complete_validate(self):
        run = self._at_validate()
        run.complete_stage("VALIDATE", evidence={"receipts": self.validation_receipts()})
        self.assertEqual(run.frontier(), "COMPLETE")

    def test_noop_receipts_cannot_attest_level_a_or_b(self):
        run = self._at_validate()
        for level, index in (("A", 0), ("B", 1)):
            with self.subTest(level=level):
                receipts = self.validation_receipts()
                receipts[index] = self.receipt([sys.executable, "-c", "pass"], level=level)
                with self.assertRaisesRegex(ar.WorkflowError, f"Level {level} requires"):
                    run.complete_stage("VALIDATE", evidence={"receipts": receipts})

    def test_level_b_requires_both_prescribed_checks_and_the_real_entry_point(self):
        run = self._at_validate()
        receipts = self.validation_receipts()
        for missing in (1, 2):
            with self.subTest(missing=missing):
                with self.assertRaisesRegex(ar.WorkflowError, "both --refresh and --status"):
                    run.complete_stage("VALIDATE", evidence={
                        "receipts": receipts[:missing] + receipts[missing + 1:]})
        receipts[1] = self.receipt(
            [sys.executable, "-c", "pass", "--refresh"], level="B")
        with self.assertRaisesRegex(ar.WorkflowError, "Level B requires"):
            run.complete_stage("VALIDATE", evidence={"receipts": receipts})

    def test_level_a_requires_executed_focused_tests(self):
        run = self._at_validate()
        for args, output in (
                (["--collect-only", str(self.focused_test)], None),
                ([str(self.focused_test)], "7 skipped\n"),
                ([], None)):
            with self.subTest(args=args, output=output):
                receipts = self.validation_receipts()
                receipts[0] = self.receipt(
                    [sys.executable, "-m", "pytest", "-q", *args], level="A", output=output)
                with self.assertRaisesRegex(ar.WorkflowError, "Level A requires"):
                    run.complete_stage("VALIDATE", evidence={"receipts": receipts})

    def test_protocol_command_variants_and_semantic_regressions_are_supported(self):
        semantics = self.entrypoint.with_name("check_reader_facing_semantics.py")
        shutil.copyfile(TOOLS / semantics.name, semantics)
        run = self._at_validate()
        receipts = self.validation_receipts()
        receipts[0] = self.receipt(
            [sys.executable, "-B", "-m", "pytest", "-q",
             str(self.focused_test) + "::test_fixture", "-k", "fixture"], level="A")
        receipts[1] = self.receipt(
            [sys.executable, "-u", "./adjudicate.py", "--refresh", "--mode", "full"],
            cwd=self.entrypoint.parent, level="B")
        receipts.append(self.receipt(
            [sys.executable, "-m", "pytest", "-q", "-k", "fixture"],
            cwd=self.tests_dir, level="A"))
        receipts.append(self.receipt([sys.executable, str(semantics)], level="A"))
        run.complete_stage("VALIDATE", evidence={"receipts": receipts})
        self.assertEqual(run.frontier(), "COMPLETE")

    def test_missing_identity_is_not_a_match(self):
        with self.assertRaisesRegex(ar.WorkflowError, "incomplete execution receipt"):
            self._at_validate().complete_stage("VALIDATE", evidence={"receipts": [{"ok": True}]})

    def test_incomplete_strict_validation_is_blocked(self):
        with self.assertRaisesRegex(ar.WorkflowError, "incomplete strict"):
            self._at_validate().complete_stage("VALIDATE", evidence={
                "receipts": self.validation_receipts()[:-1]})

    def test_tampered_receipt_is_blocked(self):
        receipt = self.receipt()
        receipt["argv"] = ["fabricated"]
        with self.assertRaisesRegex(ar.WorkflowError, "persisted record"):
            self._at_validate().complete_stage("VALIDATE", evidence={"receipts": [receipt]})


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


class BudgetAndFailureControlTests(RunHarness):

    def test_operation_recorded_with_count_and_elapsed(self):
        run = self.start()
        ar.record_operation(run, "foma_compilation", identity="k1",
                            elapsed_seconds=12.5, ok=True, label="variant-A")
        summary = ar.operations_summary(run)
        self.assertEqual(summary["foma_compilation"]["count"], 1)
        self.assertAlmostEqual(
            summary["foma_compilation"]["elapsed_seconds"], 12.5)
        self.assertIn("operations:", run.report())

    def test_unknown_operation_kind_rejected(self):
        run = self.start()
        with self.assertRaisesRegex(ar.WorkflowError, "unknown operation"):
            ar.record_operation(run, "vibes")

    def test_budget_exhaustion_blocks_without_override(self):
        run = self.start()
        ar.set_budget(run, "experiment_variant", 2, "small test budget")
        ar.record_operation(run, "experiment_variant", label="v1")
        ar.record_operation(run, "experiment_variant", label="v2")
        with self.assertRaisesRegex(ar.WorkflowError, "budget exhausted"):
            ar.record_operation(run, "experiment_variant", label="v3")

    def test_override_permits_and_journals_the_excess(self):
        run = self.start()
        ar.set_budget(run, "full_suite", 1, "test")
        ar.record_operation(run, "full_suite", label="first")
        ar.record_operation(run, "full_suite", label="second",
                            override_reason="repair changed certified state")
        overrides = [e for e in run.events()
                     if e["kind"] == "budget_override"]
        self.assertEqual(overrides[0]["reason"],
                         "repair changed certified state")

    def test_budget_change_is_journaled_with_reason(self):
        run = self.start()
        ar.set_budget(run, "foma_compilation", 100, "large counterfactual set")
        self.assertEqual(run.state()["budgets"]["foma_compilation"], 100)
        events = [e for e in run.events() if e["kind"] == "budget_set"]
        self.assertEqual(events[0]["reason"], "large counterfactual set")
        with self.assertRaises(ar.WorkflowError):
            ar.set_budget(run, "cache_hit", 5, "not budgetable")

    def test_redundant_repeat_on_unchanged_inputs_is_flagged(self):
        run = self.start()
        ar.record_operation(run, "cascade_evaluation", identity="inputs-x",
                            ok=True)
        record = ar.record_operation(run, "cascade_evaluation",
                                     identity="inputs-x")
        self.assertTrue(record["redundant"])
        warnings = [e for e in run.events()
                    if e["kind"] == "redundant_operation_warning"]
        self.assertEqual(warnings[0]["identity"], "inputs-x")

    def test_failed_prior_operation_is_not_redundant_basis(self):
        run = self.start()
        ar.record_operation(run, "cascade_evaluation", identity="inputs-x",
                            ok=False)
        record = ar.record_operation(run, "cascade_evaluation",
                                     identity="inputs-x")
        self.assertFalse(record["redundant"])

    def test_cache_events_are_visible_but_unbudgeted(self):
        run = self.start()
        for _ in range(100):
            ar.record_operation(run, "cache_hit", identity=None)
        self.assertEqual(ar.operations_summary(run)["cache_hit"]["count"],
                         100)

    def test_repair_loop_stops_after_two_attempts(self):
        run = self.start()
        self.assertEqual(ar.record_repair_attempt(run, "pytest::test_x"), 1)
        self.assertEqual(ar.record_repair_attempt(run, "pytest::test_x"), 2)
        with self.assertRaisesRegex(ar.WorkflowError, "stop the automatic"):
            ar.record_repair_attempt(run, "pytest::test_x")
        # A different underlying failure has its own counter.
        self.assertEqual(ar.record_repair_attempt(run, "pytest::test_y"), 1)


if __name__ == "__main__":
    unittest.main()

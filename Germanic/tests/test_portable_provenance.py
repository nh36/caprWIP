"""Capability separation must fail closed on available-source regressions."""
import json
import io
import os
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
import pgmc_reconstruction_survey as survey


@pytest.mark.parametrize("mode", ["full", "portable"])
def test_available_hash_changes_are_not_hidden(tmp_path, mode):
    path = tmp_path / survey.DIRECTORY / "survey_provenance.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"inputs": {"tracked.txt": "old", "original.pdf": "historic"},
                               "population": 393}))
    expected = {"inputs": {"tracked.txt": "new"}, "population": 393}
    if mode == "portable":
        expected.update(unavailable_holdings=["original.pdf"],
                        validation_mode="portable",
                        image_verification="historical records only; not repeated")
    else:
        expected["inputs"]["original.pdf"] = "changed"
    with patch.object(survey, "render", return_value={path: json.dumps(expected)}):
        problems = survey.provenance_problems(tmp_path, mode=mode)
    assert any("tracked.txt" in problem for problem in problems)
    assert any("original.pdf" in problem for problem in problems) == (mode == "full")


def test_portable_missing_original_does_not_manufacture_hash(tmp_path):
    path = tmp_path / survey.DIRECTORY / "survey_provenance.json"
    path.parent.mkdir(parents=True)
    recorded = {"inputs": {"tracked.txt": "actual", "original.pdf": "historic"},
                "population": 393}
    path.write_text(json.dumps(recorded))
    expected = {"inputs": {"tracked.txt": "actual"}, "population": 393,
                "unavailable_holdings": ["original.pdf"], "validation_mode": "portable",
                "image_verification": "historical records only; not repeated"}
    with patch.object(survey, "render", return_value={path: json.dumps(expected)}):
        assert survey.provenance_problems(tmp_path, mode="portable") == []
    assert json.loads(path.read_text()) == recorded


def test_portable_does_not_execute_runtime_nodes():
    import artifact_graph
    runtime = artifact_graph.Node("fixture", "runtime", "fixture",
                                  lambda: pytest.fail("runtime verifier executed"),
                                  lambda: [], lambda: [])
    with patch.object(artifact_graph, "nodes", return_value=(runtime,)):
        assert artifact_graph.verify_all(mode="portable") == []
        with pytest.raises(pytest.fail.Exception, match="runtime verifier executed"):
            artifact_graph.verify_all()


def test_portable_refresh_updates_tracked_hashes_but_preserves_historical_originals(tmp_path):
    import artifact_graph
    path = tmp_path / survey.DIRECTORY / "survey_provenance.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"inputs": {"tracked.txt": "old", "original.pdf": "historic"},
                               "population": 393}))
    expected = {"inputs": {"tracked.txt": "new"}, "population": 393,
                "unavailable_holdings": ["original.pdf", "new-original.pdf"],
                "validation_mode": "portable",
                "image_verification": "historical records only; not repeated"}
    with patch.object(artifact_graph, "REPO_ROOT", tmp_path), \
            patch.object(artifact_graph, "_render_pgmc_reconstruction_survey",
                         side_effect=lambda mode: {path: json.dumps(expected)}):
        artifact_graph._survey_node("portable").build()
    recorded = json.loads(path.read_text())
    assert recorded["inputs"] == {"tracked.txt": "new"}
    assert recorded["historical_unavailable_inputs"] == {
        "original.pdf": "historic", "new-original.pdf": None}
    assert recorded["validation_mode"] == "portable"
    with patch.object(survey, "render", return_value={path: json.dumps(expected)}):
        assert survey.provenance_problems(tmp_path, mode="portable") == []
    full = {"inputs": {"tracked.txt": "new", "original.pdf": "changed",
                       "new-original.pdf": "real"}, "population": 393}
    with patch.object(survey, "render", return_value={path: json.dumps(full)}):
        failures = survey.provenance_problems(tmp_path)
    assert any("original.pdf" in failure for failure in failures)
    assert any("new-original.pdf" in failure for failure in failures)


def test_variety_locator_rebase_requires_unique_unchanged_source_anchor(tmp_path):
    from check_index_verborum import resolve_variety_audit_ref
    path = tmp_path / "entry.model.md"
    tag = "[word]{.iv lang=oe variety=lws sort=word role=comparison_form}"
    path.write_text("intro\n" + tag + "\n" + tag + "\n")
    audit = {"source_ref": "entry.model.md:99", "sort_key": "word",
             "proposed_variety": "lws", "evidence_text": tag}
    row = {"source_ref": "entry.model.md:2", "language": "oe",
           "sort_key": "word", "variety": "lws"}
    assert resolve_variety_audit_ref(audit, [row], tmp_path) == "entry.model.md:2"
    with pytest.raises(ValueError, match="unambiguous"):
        resolve_variety_audit_ref(
            audit, [row, dict(row, source_ref="entry.model.md:3")], tmp_path)
    path.write_text("intro\n" + tag.replace("variety=lws", "variety=angl") + "\n")
    with pytest.raises(ValueError, match="unambiguous"):
        resolve_variety_audit_ref(audit, [row], tmp_path)
    prefixed = tag.replace("sort=word", "sort=wordplus")
    path.write_text("intro\n" + prefixed + "\n")
    with pytest.raises(ValueError, match="unambiguous"):
        resolve_variety_audit_ref(dict(audit, evidence_text=prefixed), [row], tmp_path)


def test_reporter_stops_once_at_preflight_and_does_not_reuse_old_results(tmp_path):
    import run_portable_checks as runner
    output = tmp_path / "results"
    output.mkdir()
    (output / "tests.xml").write_text("<testsuites><testcase name='stale-result'/></testsuites>")
    with patch.object(runner, "ROOT", tmp_path), patch.object(runner, "OUTPUT", output), \
            patch.object(runner, "run_check", return_value=23) as execute, \
            patch.dict(runner.os.environ, {"GITHUB_STEP_SUMMARY": ""}):
        assert runner.main() == 23
    assert execute.call_count == 1
    summary = (output / "summary.md").read_text()
    assert "Portable: FAIL" in summary
    assert "Preflight failed once" in summary
    assert "NOT RUN" in summary
    assert "stale-result" not in summary


def test_reporter_streams_before_child_exit_and_preserves_bytes_and_status(tmp_path):
    import run_portable_checks as runner
    log = tmp_path / "child.log"
    acknowledged = tmp_path / "acknowledged"

    class LiveOutput(io.StringIO):
        def write(self, text):
            if "first " in text:
                assert log.read_bytes() == b"first \xc4"
                acknowledged.touch()
            return super().write(text)

    script = (
        "import pathlib,sys,time\n"
        "sys.stdout.buffer.write(b'first \\xc4'); sys.stdout.buffer.flush()\n"
        "for _ in range(500):\n"
        f" if pathlib.Path({str(acknowledged)!r}).exists(): break\n"
        " time.sleep(.01)\n"
        "else: sys.exit(93)\n"
        "sys.stdout.buffer.write(b'\\x81\\n'); sys.stdout.buffer.flush()\n"
        "sys.stderr.write('second\\n'); sys.exit(7)\n"
    )
    output = LiveOutput()
    with patch.object(runner.sys, "stdout", output):
        assert runner.run_check([sys.executable, "-c", script], log, dict(os.environ)) == 7
    assert log.read_bytes() == b"first \xc4\x81\nsecond\n"
    assert output.getvalue() == "first \u0101\nsecond\n"


@pytest.mark.parametrize("code,xml,expected", [
    (17, None, 17),
    (0, None, 1),
    (0, "<broken>", 1),
    (0, '<testsuites><testsuite tests="1" failures="1"><testcase name="bad">'
        '<failure message="deliberate"/></testcase></testsuite></testsuites>', 1),
])
def test_reporter_keeps_fatal_pytest_diagnostics_without_usable_junit(tmp_path, code, xml, expected):
    import run_portable_checks as runner
    output = tmp_path / "results"

    def execute(argv, log, env):
        log.write_text("complete original diagnostics\n")
        if argv[1:3] == ["-m", "pytest"]:
            if xml is not None:
                (output / "tests.xml").write_text(xml)
            return code
        return 0

    with patch.object(runner, "ROOT", tmp_path), patch.object(runner, "OUTPUT", output), \
            patch.object(runner, "run_check", side_effect=execute), \
            patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}):
        assert runner.main() == expected
    summary = (output / "summary.md").read_text()
    assert "Portable: FAIL" in summary
    assert "Preflight failed once" not in summary
    assert (output / "regressions.log").read_text() == "complete original diagnostics\n"
    phases = json.loads((output / "timings.json").read_text())["phases"]
    assert len(phases) == 5
    assert phases[2]["returncode"] == code
    assert all(phase["elapsed_seconds"] >= 0 for phase in phases)


@pytest.mark.parametrize("workers", [1, 2, 4])
def test_reporter_workers_do_not_change_portable_selection(tmp_path, workers, capsys):
    import run_portable_checks as runner
    output = tmp_path / "results"
    commands = []

    def execute(argv, log, env):
        log.write_text("original output\n")
        assert env["PYTHONUNBUFFERED"] == "1"
        if argv[1:3] == ["-m", "pytest"]:
            commands.append(argv)
            (output / "tests.xml").write_text(
                '<testsuites><testsuite tests="1"><testcase name="passing" '
                'time="0.1"/></testsuite></testsuites>')
        return 0

    with patch.object(runner, "ROOT", tmp_path), patch.object(runner, "OUTPUT", output), \
            patch.object(runner, "run_check", side_effect=execute), \
            patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}):
        assert runner.main(["--workers", str(workers)]) == 0
    command, = commands
    assert "--validation-mode=portable" in command
    assert "--durations=40" in command
    assert "Germanic/tests" in command
    if workers == 1:
        assert "-n" not in command
    else:
        assert command[command.index("-n") + 1] == str(workers)
        assert command[command.index("--dist") + 1] == "loadfile"
    assert not any(arg.startswith(("-k", "--deselect", "--ignore")) for arg in command)
    live = capsys.readouterr().out
    assert "START regressions" in live
    assert "END regressions: PASS" in live
    assert "Slowest test cases" in live


def test_reporter_missing_executable_retains_failure_diagnostic(tmp_path):
    import run_portable_checks as runner
    log = tmp_path / "missing.log"
    assert runner.run_check([str(tmp_path / "missing")], log, dict(os.environ)) == 127
    assert "Cannot start" in log.read_text()


def test_direct_memo_check_is_independent_but_strict_propagation_keeps_runtime_gate(tmp_path):
    import adjudicate
    memo = tmp_path / "memo.md"
    memo.write_text("Registry-verdict: SC023=RETAIN\n")
    row = dict(adjudicate.load_registry_row("SC023"),
               adjudication_memo="memo.md", verdict="RETAIN",
               adjudication_status="adjudicated", lifecycle_status="active")
    with patch.object(adjudicate, "REPO_ROOT", tmp_path), \
            patch.object(adjudicate, "load_registry_row", return_value=row), \
            patch.object(adjudicate.artifact_graph, "verify_all",
                         return_value=["runtime bin manifest missing"]) as runtime:
        assert adjudicate.check_memo("SC023") == []
        runtime.assert_not_called()
        assert adjudicate.check("SC023") == 1
        runtime.assert_called_once_with()
        memo.write_text("Registry-verdict: SC023=RETIRE\n")
        assert any("!= registry verdict" in error
                   for error in adjudicate.check_memo("SC023"))


def test_integration_output_inventory_does_not_validate_or_build():
    import artifact_graph
    import pgmc_lexical_integration as integration
    with patch.object(integration, "render",
                      side_effect=AssertionError("output introspection must not render")):
        output = artifact_graph.declared_outputs()["pgmc_lexical_integration"]
    assert output == sorted(survey.ROOT / integration.DIRECTORY / name
                            for name in integration.OUTPUT_NAMES)


@pytest.mark.parametrize("mode", ["full", "portable"])
def test_cli_capability_selection_does_not_turn_failures_into_success(mode):
    import artifact_graph
    import adjudicate
    with patch.object(artifact_graph.sys, "argv", ["artifact_graph.py", "--check", "--mode", mode]), \
            patch.object(artifact_graph, "verify_all", return_value=["genuine fixture failure"]) as verify:
        assert artifact_graph.main() == 1
        verify.assert_called_once_with(mode=mode)
    with patch.object(adjudicate.sys, "argv", ["adjudicate.py", "--refresh", "--mode", mode]), \
            patch.object(adjudicate, "refresh", return_value=1) as refresh:
        assert adjudicate.main() == 1
        refresh.assert_called_once_with(mode=mode)


@pytest.mark.runtime
def test_full_runtime_node_freshness(request):
    import artifact_graph
    if request.config.getoption("--validation-mode") == "portable":
        pytest.skip("runtime-dependent: full graph runtime_bins/full_trace/lexical_sources/"
                    "interaction_matrix requires a provisioned Foma runner, bins and build manifests; "
                    "portable capability explicitly does not run this gate")
    problems = [f"{node.name}: {problem}"
                for node in artifact_graph.nodes()
                if node.kind == "runtime"
                for problem in node.verify()]
    assert not problems, "\n".join(problems)


def test_full_pytest_runtime_gate_fails_instead_of_skipping_missing_manifest():
    import artifact_graph
    from types import SimpleNamespace
    node = artifact_graph.Node("runtime_fixture", "runtime", "fixture",
                               lambda: ["build manifest missing"], lambda: [], lambda: [])
    request = SimpleNamespace(config=SimpleNamespace(getoption=lambda _: "full"))
    with patch.object(artifact_graph, "nodes", return_value=(node,)):
        with pytest.raises(AssertionError, match="build manifest missing"):
            test_full_runtime_node_freshness(request)

@pytest.mark.parametrize("mode,expected_skips", [("portable", 1), ("full", 0)])
def test_runtime_capability_selection_covers_live_evidence(mode, expected_skips):
    from conftest import pytest_collection_modifyitems
    from types import SimpleNamespace
    from test_evidence_interface import EvidenceIntegrationTests
    from test_final_z_firing_populations import Sc097SyntheticControlTests

    assert any(mark.name == "runtime" for mark in EvidenceIntegrationTests.pytestmark)
    assert any(mark.name == "runtime" for mark in Sc097SyntheticControlTests.pytestmark)
    skipped = []
    runtime = SimpleNamespace(get_closest_marker=lambda name: object(),
                              add_marker=skipped.append)
    portable = SimpleNamespace(get_closest_marker=lambda name: None,
                               add_marker=lambda mark: pytest.fail("portable test skipped"))
    pytest_collection_modifyitems(
        SimpleNamespace(getoption=lambda name: mode), [runtime, portable])
    assert len(skipped) == expected_skips

@pytest.mark.parametrize("module_name", [
    "test_sc021_adjudication", "test_sc023_adjudication", "test_sc024_adjudication",
    "test_sc025_sc104_adjudication", "test_sc026_sc027_adjudication",
])
def test_live_probe_decorators_declare_runtime_capability(module_name):
    module = __import__(module_name)

    def test_probe():
        pass

    marked = module.requires_runtime(test_probe)
    assert any(mark.name == "runtime" for mark in marked.pytestmark)
    assert not getattr(marked, "__unittest_skip__", False)


def test_live_stage_batch_uses_runner_and_fails_loudly_when_unavailable():
    import conftest
    from types import SimpleNamespace
    from subprocess import CalledProcessError
    with patch.object(conftest, "run_in_runner", return_value=SimpleNamespace(
            stdout='[["a", "b"], ["+?"]]')) as runner:
        assert conftest.runtime_stage_batch("stage.bin", ["a", "rejected"]) == [
            ["a", "b"], ["+?"]]
        command = runner.call_args.args[0]
        assert "batch_apply_down" in command and "stage.bin" in command
        assert runner.call_args.kwargs["check"] is True
    with patch.object(conftest, "run_in_runner", side_effect=CalledProcessError(1, "docker")):
        with pytest.raises(CalledProcessError):
            conftest.runtime_stage_batch("stage.bin", ["a"])


def test_unknown_adjudication_still_fails_before_runtime_validation():
    import adjudicate
    with patch.object(adjudicate, "load_registry_row", return_value=None) as registry, \
            patch.object(adjudicate.artifact_graph, "verify_all",
                         side_effect=AssertionError("unknown SC must not reach runtime")) as runtime:
        assert adjudicate.check("SC999") == 1
        registry.assert_called_once_with("SC999")
        runtime.assert_not_called()

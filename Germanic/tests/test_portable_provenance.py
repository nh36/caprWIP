"""Capability separation must fail closed on available-source regressions."""
import json
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
    import subprocess
    output = tmp_path / "results"
    output.mkdir()
    (output / "tests.xml").write_text("<testsuites><testcase name='stale-result'/></testsuites>")
    with patch.object(runner, "ROOT", tmp_path), patch.object(runner, "OUTPUT", output), \
            patch.object(runner.subprocess, "run",
                         return_value=subprocess.CompletedProcess([], 1)) as execute, \
            patch.dict(runner.os.environ, {"GITHUB_STEP_SUMMARY": ""}):
        assert runner.main() == 1
    assert execute.call_count == 1
    summary = (output / "summary.md").read_text()
    assert "Portable: FAIL" in summary
    assert "Preflight failed once" in summary
    assert "NOT RUN" in summary
    assert "stale-result" not in summary


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

    assert any(mark.name == "runtime" for mark in EvidenceIntegrationTests.pytestmark)
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


def test_unknown_adjudication_still_fails_before_runtime_validation():
    import adjudicate
    with patch.object(adjudicate, "load_registry_row", return_value=None) as registry, \
            patch.object(adjudicate.artifact_graph, "verify_all",
                         side_effect=AssertionError("unknown SC must not reach runtime")) as runtime:
        assert adjudicate.check("SC999") == 1
        registry.assert_called_once_with("SC999")
        runtime.assert_not_called()

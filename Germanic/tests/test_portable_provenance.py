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

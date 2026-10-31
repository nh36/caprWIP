"""Tests for incremental regression and the historical-replay lane.

Incremental regression compares consecutive canonical full-trace reports
retrieved from Git; these tests validate its actual behaviour (state
resolution, provenance validation, complete stage-by-stage comparison,
Level C integration) with small controlled reports and disposable Git
repositories. No Foma, containers or authoritative scientific data are
involved: everything here runs in the portable lane.
"""
import ast
import re
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic" / "tools"))

import compile_cache  # noqa: E402
import incremental_regression as incremental  # noqa: E402
import oe_trace_parse  # noqa: E402


# --- synthetic canonical reports ---------------------------------------------

def _sha(payload: bytes) -> str:
    return sha256(payload).hexdigest()


def default_sources() -> dict:
    return {label: f"content of {label}\n".encode()
            for label in oe_trace_parse.SOURCE_PATHS}


def provenance_block(sources: dict) -> list:
    lines = ["=== PROVENANCE ==="]
    for label in oe_trace_parse.SOURCE_PATHS:
        lines.append(f"{label} sha256: {_sha(sources[label])}")
    lines.append(f"old_english.bin sha256 (informational): {'0' * 64}")
    lines.append("bins_provenance: canonical (test build)")
    lines.append("build_manifest_built_at: test")
    lines.append("build_manifest_runner: test")
    lines.append("build_manifest_foma_version: test-foma")
    lines.append("build_manifest_expected_bins: 4")
    for label in sorted(set(oe_trace_parse.SOURCE_PATHS)
                        - oe_trace_parse.MANIFEST_EXEMPT):
        lines.append(f"manifest:{label} sha256: {_sha(sources[label])}")
    lines.append("")
    return lines


def make_report(entries, stage_labels, sources=None, fidelity=None,
                include_fidelity=True) -> str:
    """A minimal but format-faithful canonical full-trace report.

    ``entries``: list of (concept, proto, expected, outputs,
    {label: forms-string}); ``fidelity``: {(concept, proto, expected):
    [fidelity lines]} for the RAW STAGE FIDELITY section.
    """
    sources = sources or default_sources()
    lines = provenance_block(sources)
    lines.append(f"=== BUCKET: exact_match ({len(entries)}) ===")
    lines.append("")
    fired = {label: [] for label in stage_labels}
    for concept, proto, expected, outputs, stages in entries:
        lines.extend([f"--- {concept} ---", f"PROTO: {proto}",
                      "INPUT_CONTEXT: SC098; stress=stressed; finality=final",
                      f"EXPECTED: {expected}", f"OUTPUTS: {outputs}", ""])
        previous = None
        for label in stage_labels:
            forms = stages[label]
            tag = ""
            if previous is not None and forms == previous:
                tag = " [no-change]"
            elif previous is not None:
                fired[label].append(f"{concept} :: {proto}")
            lines.append(f"{label}{tag}: {forms}")
            previous = forms
        lines.append("")
    lines.append("")
    if include_fidelity:
        lines.extend(["=== RAW STAGE FIDELITY ===", "",
                      "entries with raw-stage distinctions: "
                      f"{len(fidelity or {})}", ""])
        for key, fidelity_lines in (fidelity or {}).items():
            lines.append("--- {} | {} | {} ---".format(*key))
            lines.extend(fidelity_lines)
            lines.append("")
    lines.extend(["=== STAGE FIRING SUMMARY ===", ""])
    for label in stage_labels:
        lines.append(f"{label}: {len(fired[label])}")
        if fired[label]:
            lines.append(", ".join(fired[label]))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _state(text: str) -> dict:
    return {"state": "test", "text": text, "problems": [], "limitations": []}


BASE_STAGES = ["StageA", "StageB", "StageC", "StageD"]


def base_entry(concept="stone", proto="*stainaz", expected="stān",
               outputs="stān", **stage_forms):
    stages = {"StageA": "*s*t*a*i*n*a*z", "StageB": "*s*t*ā*n*a*z",
              "StageC": "*s*t*ā*n", "StageD": "stān"}
    stages.update(stage_forms)
    return (concept, proto, expected, outputs, stages)


# --- complete stage-by-stage comparison --------------------------------------

def test_intermediate_change_with_identical_final_output_is_reported():
    reference = make_report([base_entry()], BASE_STAGES)
    current = make_report([base_entry(StageB="*s*t*ē*n*a*z")], BASE_STAGES)
    report = incremental.compare(_state(current), _state(reference))
    key = "stone | *stainaz | stān"
    change = report["entry_changes"][key]
    assert change["first_divergence"] == "StageB"
    assert change["intermediate_only"] and not change["final_changed"]
    assert report["intermediate_only_changes"] == [key]
    assert report["final_output_changes"] == []


def test_divergence_followed_by_convergence_is_identified():
    current = make_report([base_entry(StageB="*s*t*ē*n*a*z")], BASE_STAGES)
    reference = make_report([base_entry()], BASE_STAGES)
    change = incremental.compare(_state(current), _state(reference))[
        "entry_changes"]["stone | *stainaz | stān"]
    assert change["divergent_stages"] == ["StageB"]
    assert change["reconverged"]
    assert change["at_first_divergence"] == {
        "reference": ["*s*t*ā*n*a*z"], "current": ["*s*t*ē*n*a*z"]}


def test_changed_forms_with_identical_firing_populations_are_detected():
    # StageB fires for the entry in both versions (so the firing summary is
    # unchanged), but produces a different form.
    current = make_report(
        [base_entry(StageB="*s*t*ē*n*a*z", StageC="*s*t*ē*n",
                    StageD="stēn", outputs="stēn")], BASE_STAGES)
    reference = make_report([base_entry()], BASE_STAGES)
    report = incremental.compare(_state(current), _state(reference))
    assert report["firing_population_changes"] == {}
    change = report["entry_changes"]["stone | *stainaz | stān"]
    assert change["first_divergence"] == "StageB"
    assert change["final_changed"]
    assert change["final"] == {"reference": "stān", "current": "stēn"}


def test_first_stage_changes_and_stage_structure_changes_are_reported():
    current = make_report(
        [base_entry(StageA="*s*t*a*i*n*a*s")], BASE_STAGES)
    reference = make_report([base_entry()], BASE_STAGES)
    report = incremental.compare(_state(current), _state(reference))
    assert report["entry_changes"]["stone | *stainaz | stān"][
        "first_divergence"] == "StageA"

    entry = base_entry()
    reordered = ["StageA", "StageC", "StageB", "StageD"]
    report = incremental.compare(
        _state(make_report([entry], reordered)),
        _state(make_report([entry], BASE_STAGES)))
    assert report["stage_order_changed"]
    assert not report["stages_added"] and not report["stages_removed"]

    replaced = ["StageA", "StageB", "StageE", "StageD"]
    stages = dict(entry[4], StageE=entry[4]["StageC"])
    report = incremental.compare(
        _state(make_report([(*entry[:4], stages)], replaced)),
        _state(make_report([entry], BASE_STAGES)))
    assert report["stages_added"] == ["StageE"]
    assert report["stages_removed"] == ["StageC"]
    assert report["stage_order_changed"]


def test_corpus_changes_are_distinguished_from_phonological_changes():
    yoke = base_entry(concept="yoke", proto="*jukan", expected="ġeoc",
                      outputs="ġeoc")
    current = make_report([base_entry(), yoke], BASE_STAGES)
    reference = make_report(
        [base_entry(concept="youth", proto="*juwunþiz", expected="ġeoguð",
                    outputs="ġeoguð"), base_entry()], BASE_STAGES)
    report = incremental.compare(_state(current), _state(reference))
    assert report["entries_added"] == ["yoke | *jukan | ġeoc"]
    assert report["entries_removed"] == ["youth | *juwunþiz | ġeoguð"]
    assert report["entry_changes"] == {}  # the shared entry is unchanged

    changed_context = make_report([base_entry()], BASE_STAGES).replace(
        "stress=stressed", "stress=unstressed")
    report = incremental.compare(
        _state(changed_context), _state(make_report([base_entry()],
                                                     BASE_STAGES)))
    change = report["entry_changes"]["stone | *stainaz | stān"]
    assert change["context_changed"] and not change["final_changed"]
    assert report["context_changes"] == ["stone | *stainaz | stān"]


def test_rejection_states_are_preserved_and_compared():
    # In the displayed trace a rejected stage shows the previous form tagged
    # [no-change], exactly like a genuine no-change stage. Only the RAW
    # STAGE FIDELITY section distinguishes them.
    key = ("stone", "*stainaz", "stān")
    entry = base_entry(StageB="*s*t*a*i*n*a*z")  # displayed: no change at B
    current = make_report([entry], BASE_STAGES)
    reference = make_report([entry], BASE_STAGES,
                            fidelity={key: ["StageB: rejected"]})
    report = incremental.compare(_state(current), _state(reference))
    change = report["entry_changes"]["stone | *stainaz | stān"]
    assert change["first_divergence"] == "StageB"
    assert change["at_first_divergence"]["reference"] == ["rejected"]


def test_ambiguous_multiple_outputs_are_preserved():
    current = make_report(
        [base_entry(StageC="*s*t*ā*n, *s*t*ǣ*n")], BASE_STAGES)
    reference = make_report([base_entry()], BASE_STAGES)
    change = incremental.compare(_state(current), _state(reference))[
        "entry_changes"]["stone | *stainaz | stān"]
    assert change["at_first_divergence"]["current"] == [
        "*s*t*ā*n", "*s*t*ǣ*n"]


def test_context_marker_differences_are_detected_through_raw_fidelity():
    # display_form strips context annotation marks, so the displayed stage
    # lines coincide; the raw forms recorded in the fidelity section differ.
    key = ("stone", "*stainaz", "stān")
    current = make_report([base_entry()], BASE_STAGES,
                          fidelity={key: ["StageB: raw = *ᵘ*s*t*ā*n*a*z"]})
    reference = make_report([base_entry()], BASE_STAGES)
    report = incremental.compare(_state(current), _state(reference))
    change = report["entry_changes"]["stone | *stainaz | stān"]
    assert change["first_divergence"] == "StageB"
    assert change["at_first_divergence"]["current"] == ["*ᵘ*s*t*ā*n*a*z"]


def test_older_reports_without_fidelity_compare_display_level_explicitly():
    key = ("stone", "*stainaz", "stān")
    entry = base_entry(StageB="*s*t*a*i*n*a*z")
    current = make_report([entry], BASE_STAGES,
                          fidelity={key: ["StageB: rejected"]})
    old_format = make_report([entry], BASE_STAGES, include_fidelity=False)
    report = incremental.compare(_state(current), _state(old_format))
    # Without the predecessor's fidelity data the rejection cannot be
    # compared; the comparison is display-level and says so.
    assert report["display_level_comparison"]
    assert report["entry_changes"] == {}
    assert oe_trace_parse.parse_fidelity(old_format) is None


# --- provenance validation and Git retrieval ---------------------------------

def _run(repo, *arguments):
    subprocess.run(arguments, cwd=repo, check=True, capture_output=True)


def _write_state(repo: Path, sources: dict, report: str) -> None:
    for label, path in oe_trace_parse.SOURCE_PATHS.items():
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(sources[label])
    trace = repo / incremental.TRACE_PATH
    trace.parent.mkdir(parents=True, exist_ok=True)
    trace.write_text(report, encoding="utf-8")


@pytest.fixture()
def repo(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    _run(repo, "git", "init", "-q")
    _run(repo, "git", "config", "user.email", "test@example.invalid")
    _run(repo, "git", "config", "user.name", "Test")
    return repo


def _commit(repo, message):
    _run(repo, "git", "add", "-A")
    _run(repo, "git", "commit", "-q", "-m", message)


def test_consecutive_commits_compare_via_git_with_zero_foma(repo):
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    _commit(repo, "state one")
    sources2 = dict(sources)
    sources2["germanic.txt"] = b"changed grammar\n"
    _write_state(repo, sources2, make_report(
        [base_entry(StageB="*s*t*ē*n*a*z")], BASE_STAGES, sources=sources2))
    _commit(repo, "state two")
    result = incremental.run_comparison(root=repo)
    assert result["foma_invocations"] == 0
    assert result["states"]["basis"] == "HEAD vs first parent (HEAD^1)"
    assert result["dependencies"]["consequence"] == (
        "requires transducer recompilation")
    change = result["comparison"]["entry_changes"]["stone | *stainaz | stān"]
    assert change["intermediate_only"]


def test_no_change_commit_pair_terminates_on_the_fast_path(repo):
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    _commit(repo, "state one")
    (repo / "unrelated.md").write_text("docs only\n")
    _commit(repo, "docs change")
    result = incremental.run_comparison(root=repo)
    assert result["identical"]
    assert result["comparison"] is None
    assert result["dependencies"]["consequence"] == (
        "no effect on the executable model")


def test_stale_report_evidence_is_rejected_not_silently_substituted(repo):
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    _commit(repo, "consistent state")
    # The grammar changes but the committed report is not regenerated: the
    # current state's report no longer matches its own sources.
    (repo / "Germanic/fsts/germanic.txt").write_bytes(b"edited grammar\n")
    _commit(repo, "inconsistent state")
    with pytest.raises(incremental.StateError, match="STALE w.r.t"):
        incremental.run_comparison(root=repo)


def test_missing_and_invalid_predecessor_reports_are_explicit_failures(repo):
    sources = default_sources()
    # Predecessor commit has no report at all.
    for label, path in oe_trace_parse.SOURCE_PATHS.items():
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(sources[label])
    _commit(repo, "no report yet")
    sources2 = dict(sources)
    sources2["germanic.txt"] = b"new grammar\n"
    _write_state(repo, sources2, make_report([base_entry()], BASE_STAGES,
                                             sources=sources2))
    _commit(repo, "report added")
    with pytest.raises(incremental.StateError,
                       match="predecessor state.*no full-trace report"):
        incremental.run_comparison(root=repo)


def test_report_without_firing_summary_is_incomplete_evidence(repo):
    sources = default_sources()
    truncated = make_report([base_entry()], BASE_STAGES).split(
        "=== STAGE FIRING SUMMARY ===")[0]
    _write_state(repo, sources, truncated)
    _commit(repo, "incomplete report")
    (repo / "unrelated.md").write_text("second commit\n")
    _commit(repo, "second")
    with pytest.raises(incremental.StateError, match="STAGE FIRING SUMMARY"):
        incremental.run_comparison(root=repo)


def test_evaluation_code_changes_are_never_computationally_irrelevant(repo):
    # oe_pipeline.py changes while germanic.txt and the report stay
    # identical: the comparison must classify the executable consequence
    # instead of calling the states identical.
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    (repo / "Germanic/tools/oe_pipeline.py").write_text("STAGES = 1\n")
    _commit(repo, "state one")
    (repo / "Germanic/tools/oe_pipeline.py").write_text("STAGES = 2\n")
    _commit(repo, "evaluation code change")
    result = incremental.run_comparison(root=repo)
    assert not result["identical"]
    assert result["dependencies"]["recompile_changed"] == [
        "Germanic/tools/oe_pipeline.py"]
    assert result["dependencies"]["consequence"] == (
        "requires transducer recompilation")


def test_staged_state_is_compared_and_unstaged_work_is_excluded(repo):
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    _commit(repo, "committed state")
    # Stage a consistent proposed state...
    staged_sources = dict(sources)
    staged_sources["germanic.txt"] = b"staged grammar\n"
    _write_state(repo, staged_sources, make_report(
        [base_entry(StageB="*s*t*ē*n*a*z")], BASE_STAGES,
        sources=staged_sources))
    _run(repo, "git", "add", "-A")
    # ...then dirty the working tree differently without staging.
    (repo / "Germanic/fsts/germanic.txt").write_bytes(b"unstaged edit\n")
    result = incremental.run_comparison(root=repo)
    assert result["states"]["current"] == incremental.STAGED
    assert "unstaged work is NOT part" in result["states"]["basis"]
    change = result["comparison"]["entry_changes"]["stone | *stainaz | stān"]
    assert change["first_divergence"] == "StageB"


def test_explicit_worktree_mode_compares_the_working_tree(repo):
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    _commit(repo, "committed state")
    worktree_sources = dict(sources)
    worktree_sources["germanic.txt"] = b"worktree grammar\n"
    _write_state(repo, worktree_sources, make_report(
        [base_entry(StageC="*s*t*ǣ*n")], BASE_STAGES,
        sources=worktree_sources))
    result = incremental.run_comparison(root=repo, worktree=True)
    assert result["states"]["current"] == incremental.WORKTREE
    assert "working tree vs HEAD" in result["states"]["basis"]
    assert "stone | *stainaz | stān" in result["comparison"]["entry_changes"]


def test_stale_worktree_report_fails_closed_without_refresh(repo):
    sources = default_sources()
    _write_state(repo, sources, make_report([base_entry()], BASE_STAGES))
    _commit(repo, "committed state")
    (repo / "Germanic/fsts/germanic.txt").write_bytes(b"worktree edit\n")
    with pytest.raises(incremental.StateError, match="STALE w.r.t"):
        incremental.run_comparison(root=repo, worktree=True,
                                   allow_refresh=False)


def test_comparison_never_invokes_foma_containers_or_historical_replay():
    source = (ROOT / "Germanic/tools/incremental_regression.py").read_text()
    for forbidden in ("flookup", "docker", "historical_runtime",
                      "compile_cache"):
        assert forbidden not in source, forbidden
    # The only subprocess use is Git retrieval of stored states (so Foma is
    # unreachable from this module).
    for match in re.finditer(r"subprocess\.\w+\(\[\"?(\w+)", source):
        assert match.group(1) == "git", match.group(0)


# --- Level C integration -----------------------------------------------------

def test_level_c_runs_the_consecutive_version_comparison_automatically():
    """The automatic Level C comparison of the real repository.

    A green run of the ordinary suite establishes that the incremental
    comparison completed on the actual consecutive states: missing reports,
    invalid provenance or unidentified source states fail this test rather
    than becoming silent skips. Zero Foma invocations are required; the
    Git-stored canonical reports are reused as-is.
    """
    result = incremental.run_comparison()
    assert result["foma_invocations"] == 0
    assert result["identical"] or result["comparison"]["entries_examined"] > 0
    summary = incremental.summarize(result)
    assert "INCREMENTAL REGRESSION" in summary
    incremental.write_diagnostics(result, summary)
    assert (incremental.RESULTS_DIR / incremental.REPORT_NAME).is_file()
    assert (incremental.RESULTS_DIR / incremental.SUMMARY_NAME).is_file()


def test_diagnostics_use_stable_untracked_filenames():
    tracked = subprocess.run(
        ["git", "ls-files", ".ci-results"], cwd=ROOT,
        capture_output=True, text=True, check=True).stdout.strip()
    assert tracked == "", "comparison diagnostics must never be tracked"
    gitignore = (ROOT / ".gitignore").read_text()
    assert ".ci-results/" in gitignore
    # Stable names, replaced on each run; never timestamped accumulation.
    assert incremental.SUMMARY_NAME == "incremental_regression.txt"
    assert incremental.REPORT_NAME == "incremental_regression.json"


# --- build cache (historical replay only) ------------------------------------

@pytest.fixture()
def isolated_cache(monkeypatch, tmp_path):
    monkeypatch.setattr(compile_cache, "CACHE_DIR", tmp_path / "cache")
    return tmp_path / "cache"


def _key(**overrides):
    arguments = dict(image="image-1", source=b"define A a -> b;",
                     corpus=b"ID\tDOCULECT\n", extra={"backend/oe_input_context.py": b"x"})
    arguments.update(overrides)
    return compile_cache.compile_cache_key(**arguments)


def test_identical_inputs_reuse_the_same_cache_entry(isolated_cache):
    key = _key()
    assert key == _key()
    compile_cache.store_build(key, b"tar-bytes", "test")
    assert compile_cache.cached_build(_key()) == b"tar-bytes"


def test_grammar_changes_invalidate_the_cached_build(isolated_cache):
    compile_cache.store_build(_key(), b"tar-bytes", "test")
    assert compile_cache.cached_build(_key(source=b"define A a -> c;")) is None


def test_corrupted_cache_entries_are_rejected_not_trusted(isolated_cache):
    key = _key()
    compile_cache.store_build(key, b"tar-bytes", "test")
    (compile_cache.CACHE_DIR / f"{key}.tar").write_bytes(b"tampered")
    assert compile_cache.cached_build(key) is None


def test_the_evaluation_cache_is_gone_git_is_the_store_of_record():
    # Incremental regression consumes Git-stored canonical reports; the
    # removed evaluation cache must not quietly return.
    assert not hasattr(compile_cache, "cached_evaluation")
    assert not hasattr(compile_cache, "store_evaluation")
    assert "eval.json" not in (
        ROOT / "Germanic/tools/compile_cache.py").read_text()


# --- replay gating ----------------------------------------------------------

HISTORICAL_REPLAY_TESTS = {
    "test_sc035_prosody.py":
        {"test_fresh_commit_pinned_comparison_reproduces_the_entire_receipt"},
    "test_sc035_model_comparison.py":
        {"test_fresh_foma_comparison_reproduces_every_recorded_intermediate"},
    "test_sc035_prefix_reduction.py":
        {"test_fresh_container_assay_reproduces_census_controls_and_counterfactuals"},
    "test_rainbow_2148_adoption.py":
        {"test_fresh_container_capture_and_private_controls_match_committed_receipts"},
    "test_chronology_consistency.py":
        {"test_original_displacement_is_contingent_on_the_retired_early_glide"},
}


def _marked_functions(path, marker):
    tree = ast.parse(path.read_text())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                text = ast.unparse(decorator)
                if f"pytest.mark.{marker}" in text:
                    names.add(node.name)
    return names


def test_every_historical_compilation_test_is_in_the_explicit_replay_lane():
    tests = Path(__file__).resolve().parent
    for filename, expected in HISTORICAL_REPLAY_TESTS.items():
        marked = _marked_functions(tests / filename, "historical_replay")
        assert expected <= marked, (filename, expected - marked)
        # Replay tests stay in the serial Foma lane when executed.
        runtime = _marked_functions(tests / filename, "runtime")
        assert expected <= runtime, (filename, expected - runtime)


def test_no_unmarked_test_module_reconstructs_historical_models():
    """Ordinary validation must not invoke historical compilation.

    Every consumer of historical_runtime() and every git-show of a
    historical germanic.txt that feeds a compiler must be a marked
    historical_replay test (or the mocked lifecycle test, which prohibits
    real subprocess execution).
    """
    tests = Path(__file__).resolve().parent
    allowed = set(HISTORICAL_REPLAY_TESTS) | {
        "historical_sc035.py",              # the shared replay helper itself
        "test_historical_runtime_lifecycle.py",  # fully mocked, no Foma
        Path(__file__).name,                # mentions the helper in prose only
    }
    consumers = set()
    for path in tests.glob("test_*.py"):
        text = path.read_text()
        if "historical_runtime(" in text:
            consumers.add(path.name)
    assert consumers <= allowed, consumers - allowed
    # And the consumers that do compile are all marked.
    for name in consumers - {"test_historical_runtime_lifecycle.py",
                             Path(__file__).name}:
        assert _marked_functions(tests / name, "historical_replay"), name


def test_conftest_gates_the_replay_marker_behind_an_explicit_flag():
    conftest = (Path(__file__).resolve().parent / "conftest.py").read_text()
    assert "--historical-replay" in conftest
    assert 'get_closest_marker("historical_replay")' in conftest
    gate = re.search(r'if not config\.getoption\("--historical-replay"\)', conftest)
    assert gate, "default skip of historical_replay tests must remain"


def test_current_model_chronology_controls_stay_in_ordinary_validation():
    text = (Path(__file__).resolve().parent
            / "test_chronology_consistency.py").read_text()
    marked = _marked_functions(
        Path(__file__).resolve().parent / "test_chronology_consistency.py",
        "historical_replay")
    assert "test_current_lowering_displacement_and_written_surface_controls" \
        not in marked
    assert "chronology_replay_current" in text


def test_historical_receipts_remain_protected_without_replay():
    """The immutable receipts stay asserted in the ordinary suite."""
    receipts = [
        ROOT / "Germanic/docs/sound_changes/audits/sc035-prosody/evidence.json",
        ROOT / "Germanic/docs/sound_changes/audits/sc035-model-comparison",
        ROOT / "Germanic/docs/sound_changes/audits/sc035-prefix-reduction",
    ]
    for path in receipts:
        assert path.exists(), path


class _FakeItem:
    def __init__(self, markers):
        self._markers = set(markers)
        self.added = []

    def get_closest_marker(self, name):
        return object() if name in self._markers else None

    def add_marker(self, marker):
        self.added.append(marker)


class _FakeConfig:
    def __init__(self, replay):
        self._options = {"--validation-mode": "full",
                         "--historical-replay": replay}

    def getoption(self, name):
        return self._options[name]


def _live_conftest():
    """The real conftest module as loaded by this very pytest session."""
    path = str(Path(__file__).resolve().parent / "conftest.py")
    for module in list(sys.modules.values()):
        if getattr(module, "__file__", None) == path:
            return module
    raise AssertionError("session conftest module not found")


def test_replay_tests_are_skipped_by_default_and_run_with_the_flag():
    conftest = _live_conftest()
    for replay, expect_skip in ((False, True), (True, False)):
        gated = _FakeItem({"historical_replay", "runtime"})
        ordinary = _FakeItem({"runtime"})
        conftest.pytest_collection_modifyitems(
            _FakeConfig(replay), [gated, ordinary])
        assert bool(gated.added) is expect_skip, replay
        assert not ordinary.added  # ordinary runtime tests are never gated
        if expect_skip:
            reason = gated.added[0].kwargs.get("reason", "")
            assert "historical replay" in reason
            assert "--historical-replay" in reason

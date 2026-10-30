"""Tests for the incremental-regression mechanism and historical-replay lane.

These validate the mechanism itself (state resolution, cache identity,
replay gating) without compiling any Foma model: they are fast,
mock-based checks in the portable lane.
"""
import ast
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic" / "tools"))

import compile_cache  # noqa: E402
import incremental_regression as incremental  # noqa: E402


# --- state resolution -------------------------------------------------------

def _patch_git(monkeypatch, head, parents_line):
    def fake_git(*arguments):
        if arguments[0] == "rev-parse":
            return head + "\n"
        if arguments[0] == "rev-list":
            return parents_line + "\n"
        raise AssertionError(arguments)
    monkeypatch.setattr(incremental, "_git", fake_git)


def test_clean_tree_compares_head_against_its_first_parent(monkeypatch):
    _patch_git(monkeypatch, "c" * 40, f"{'c' * 40} {'p' * 40}")
    files = {path: b"same" for path in incremental.INPUT_PATHS}
    monkeypatch.setattr(incremental, "state_files", lambda label: dict(files))
    states = incremental.resolve_states()
    assert states == {"current": "c" * 40, "reference": "p" * 40,
                      "basis": "HEAD vs first parent (HEAD^1)"}


def test_uncommitted_working_tree_compares_against_head(monkeypatch):
    _patch_git(monkeypatch, "c" * 40, f"{'c' * 40} {'p' * 40}")
    head_files = {path: b"same" for path in incremental.INPUT_PATHS}
    dirty = dict(head_files)
    dirty["Germanic/fsts/germanic.txt"] = b"edited grammar"
    monkeypatch.setattr(
        incremental, "state_files",
        lambda label: dict(dirty) if label == "worktree" else dict(head_files))
    states = incremental.resolve_states()
    assert states["current"] == "worktree"
    assert states["reference"] == "c" * 40
    assert "uncommitted" in states["basis"]


def test_merge_commit_uses_first_parent_and_says_so(monkeypatch):
    _patch_git(monkeypatch, "m" * 40, f"{'m' * 40} {'a' * 40} {'b' * 40}")
    files = {path: b"same" for path in incremental.INPUT_PATHS}
    monkeypatch.setattr(incremental, "state_files", lambda label: dict(files))
    states = incremental.resolve_states()
    assert states["reference"] == "a" * 40
    assert "merge" in states["basis"] and "FIRST parent" in states["basis"]


def test_parentless_head_is_an_explicit_error(monkeypatch):
    _patch_git(monkeypatch, "r" * 40, "r" * 40)
    files = {path: b"same" for path in incremental.INPUT_PATHS}
    monkeypatch.setattr(incremental, "state_files", lambda label: dict(files))
    with pytest.raises(incremental.StateError, match="no immediate predecessor"):
        incremental.resolve_states()


def test_non_executable_edits_do_not_make_the_tree_count_as_dirty(monkeypatch):
    # resolve_states compares only the executable INPUT_PATHS, so an edit to
    # documentation or an unrelated test cannot change the comparison basis.
    assert "Germanic/fsts/germanic.txt" in incremental.INPUT_PATHS
    assert "Germanic/data/germanic-aligned-final.tsv" in incremental.INPUT_PATHS
    assert "Germanic/data/entry_context_metadata.tsv" in incremental.INPUT_PATHS
    assert "backend/oe_input_context.py" in incremental.INPUT_PATHS
    assert len(incremental.INPUT_PATHS) == 4


# --- cache identity ---------------------------------------------------------

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


def test_corpus_changes_invalidate_the_cached_build(isolated_cache):
    compile_cache.store_build(_key(), b"tar-bytes", "test")
    changed = _key(corpus=b"ID\tDOCULECT\n2000\tOld_English\n")
    assert compile_cache.cached_build(changed) is None


def test_context_dependency_changes_invalidate_the_cached_build(isolated_cache):
    compile_cache.store_build(_key(), b"tar-bytes", "test")
    assert compile_cache.cached_build(
        _key(extra={"backend/oe_input_context.py": b"y"})) is None


def test_image_and_tool_changes_invalidate_the_key(isolated_cache, monkeypatch, tmp_path):
    base = _key()
    assert _key(image="image-2") != base
    # The key digests the live build-tool sources, never a bare commit id.
    fake_root = tmp_path / "repo"
    tools = fake_root / "Germanic/tools"
    tools.mkdir(parents=True)
    for tool in compile_cache.BUILD_TOOLS:
        tools.joinpath(tool).write_bytes(
            (compile_cache.ROOT / "Germanic/tools" / tool).read_bytes())
    monkeypatch.setattr(compile_cache, "ROOT", fake_root)
    assert _key() == base  # identical tool bytes: same key
    with tools.joinpath(compile_cache.BUILD_TOOLS[0]).open("ab") as handle:
        handle.write(b"\n# changed build tool\n")
    assert _key() != base


def test_corrupted_cache_entries_are_rejected_not_trusted(isolated_cache):
    key = _key()
    compile_cache.store_build(key, b"tar-bytes", "test")
    (compile_cache.CACHE_DIR / f"{key}.tar").write_bytes(b"tampered")
    assert compile_cache.cached_build(key) is None


def test_cached_evaluation_round_trips_and_is_keyed_by_content(isolated_cache):
    key = _key()
    record = {"finals": {"2001": ["stān"]}, "stage_order": ["A"]}
    compile_cache.store_evaluation(key, record)
    assert compile_cache.cached_evaluation(key) == {**record, "cache_key": key}
    assert compile_cache.cached_evaluation(_key(source=b"other")) is None


def test_identical_states_short_circuit_without_execution():
    record = {"stage_order": ["A", "B"], "corpus": {"1": "x"},
              "concepts": {"1": "stone"}, "finals": {"1": ["y"]},
              "snapshots": {"a.bin": {"1": ["x"]}, "b.bin": {"1": ["y"]}},
              "cache_key": "k1"}
    report = incremental.compare(record, dict(record))
    assert report["identical_executable_inputs"]
    assert not report["finals_changed"]


def test_comparison_reports_every_protected_change_dimension():
    reference = {"stage_order": ["A", "B", "C"],
                 "corpus": {"1": "in1", "2": "in2"},
                 "concepts": {"1": "stone", "2": "yoke"},
                 "finals": {"1": ["out1"], "2": ["out2"]},
                 "snapshots": {"a.bin": {"1": ["s1"], "2": ["in2"]},
                               "b.bin": {"1": ["s1"], "2": ["out2"]},
                               "c.bin": {"1": ["out1"], "2": ["out2"]}},
                 "cache_key": "ref"}
    current = {"stage_order": ["A", "C", "D"],
               "corpus": {"1": "in1", "3": "in3"},
               "concepts": {"1": "stone", "3": "youth"},
               "finals": {"1": ["changed"], "3": ["out3"]},
               "snapshots": {"a.bin": {"1": ["s1"], "3": ["in3"]},
                             "c.bin": {"1": ["changed"], "3": ["out3"]},
                             "d.bin": {"1": ["changed"], "3": ["out3"]}},
               "cache_key": "cur"}
    report = incremental.compare(current, reference)
    assert not report["identical_executable_inputs"]
    assert report["stage_order_changed"]
    assert report["stages_added"] == ["D"] and report["stages_removed"] == ["B"]
    assert report["rows_added"] == ["3"] and report["rows_removed"] == ["2"]
    assert report["finals_changed"]["1"]["reference"] == ["out1"]
    assert report["finals_changed"]["1"]["current"] == ["changed"]
    assert report["finals_changed"]["1"]["first_divergence"] == "c.bin"
    assert report["firing_population_changes"]["C"] == {
        "gained": ["3"], "lost": []}


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

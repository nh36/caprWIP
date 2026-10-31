"""Explicit test capabilities; ordinary local invocations remain strict."""
from functools import partial
import json
from pathlib import Path
import shlex
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import pgmc_reconstruction_survey as survey
import pgmc_lexical_integration as integration
from capr_runtime import run_in_runner


def runtime_stage_batch(bin_name, forms):
    """Read one stage for all probes in the provisioned backend, never host Foma."""
    script = f"""
import json, sys
from pathlib import Path
sys.path.insert(0, "tools")
from sc_evidence import validate_bin
from sound_change_order_sensitivity import batch_apply_down
path = Path({bin_name!r})
validate_bin(path, None)
print(json.dumps([outputs or ["+?"] for outputs in
                 batch_apply_down(path, {forms!r})]))
"""
    result = run_in_runner(
        f"python3 -c {shlex.quote(script)}",
        text=True, capture_output=True, check=True, timeout=180)
    return json.loads(result.stdout)


def pytest_addoption(parser):
    parser.addoption("--validation-mode", choices=("full", "portable"), default="full")
    parser.addoption(
        "--historical-replay", action="store_true", default=False,
        help=("execute historical-replay tests: reconstruct commit-pinned "
              "historical Foma models and re-derive their immutable receipts "
              "by live execution (see docs/HISTORICAL_REPLAY.md)"))


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "runtime: strict provisioned-runtime validation, explicitly not run in portable mode")
    config.addinivalue_line(
        "markers", "historical_replay: live reconstruction of a commit-pinned "
        "historical model; explicit reproducibility lane, not ordinary "
        "validation (run with --historical-replay)")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--validation-mode") == "portable":
        skip = pytest.mark.skip(reason=(
            "runtime-dependent: not executed in portable mode; "
            "use --validation-mode=full with the provisioned Foma runtime"))
        for item in items:
            if item.get_closest_marker("runtime") is not None:
                item.add_marker(skip)
    if not config.getoption("--historical-replay"):
        replay_skip = pytest.mark.skip(reason=(
            "historical replay: explicit lane; ordinary validation checks the "
            "immutable receipts without recompiling historical models. "
            "Run with --historical-replay (docs/HISTORICAL_REPLAY.md)."))
        for item in items:
            if item.get_closest_marker("historical_replay") is not None:
                item.add_marker(replay_skip)


def pytest_runtest_setup(item):
    # Concurrency guard: runtime-marked tests share the single authoritative
    # Foma binary directory and backend container (capr_runtime.layout()), so
    # they must never execute inside a pytest-xdist worker. Rejected loudly
    # rather than risking two competing compilations against shared bins.
    if (item.get_closest_marker("runtime") is not None
            and hasattr(item.config, "workerinput")):
        pytest.fail(
            "runtime-marked tests require exclusive serial access to the shared "
            "Foma runtime; run them without -n (see docs/CI_VALIDATION.md: "
            "parallel lane uses -m 'not runtime').", pytrace=False)


def pytest_sessionstart(session):
    mode = session.config.getoption("--validation-mode")
    try:
        survey.load(mode=mode)
    except (survey.SurveyError, OSError) as exc:
        pytest.exit(
            f"{mode.upper()} holding/evidence preflight failed: {exc}\n"
            "Provision declared local holdings for full validation, or explicitly "
            "select --validation-mode=portable (no original-image certification).",
            returncode=1)


@pytest.fixture(scope="session", autouse=True)
def selected_validation_capability(request):
    mode = request.config.getoption("--validation-mode")
    # Only the test invocation selects these defaults. Explicit API modes still
    # override them; production APIs always default to full.
    with pytest.MonkeyPatch.context() as monkeypatch:
        for module, names in ((survey, ("load", "render")),
                              (integration, ("build", "render"))):
            for name in names:
                monkeypatch.setattr(module, name, partial(getattr(module, name), mode=mode))
        yield


@pytest.fixture(autouse=True)
def selected_graph_capability(request, monkeypatch):
    mode = request.config.getoption("--validation-mode")
    if request.module is not None and hasattr(request.module, "VALIDATION_MODE"):
        monkeypatch.setattr(request.module, "VALIDATION_MODE", mode)

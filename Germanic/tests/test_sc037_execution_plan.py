"""Selection changes execution extent, never the independent phonological oracle."""

from dataclasses import replace
import json
from pathlib import Path
import subprocess
import sys

import pytest

import sc037_intervention_controls as controls
from oe_trace_parse import EntryTrace, StageLine


def test_dart_plan_has_no_unrelated_models_probes_or_components():
    plan = controls.execution_plan("dart")
    assert set(plan) == {"current"}
    assert plan["current"] == {
        "forms": [], "selected": False, "staged": [], "components": [],
        "tails": ["AF66Good", "AF66Closed"],
    }


def test_full_plan_retains_consumers_and_omits_unused_roots():
    plan = controls.execution_plan("full")
    assert len(plan) == 13
    assert sum(bool(value["forms"]) for value in plan.values()) == 8
    assert plan["current"]["selected"]
    assert len(plan["current"]["tails"]) == 15
    assert all(not value["components"] and not value["tails"]
               for name, value in plan.items() if name != "current")
    assert plan["no-high"]["staged"] == ["furthest", "companion"]
    assert plan["no-n-loss"]["staged"] == ["early-fright", "early-pillow"]


def test_unknown_request_fails_before_any_compilation(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["worker", "--request", "unknown"])
    def forbidden(*args):
        pytest.fail("unknown request reached evaluation")
    monkeypatch.setattr(controls, "run_controls", forbidden)
    with pytest.raises(ValueError, match="unknown SC037 request"):
        controls.main()


def checkpoint_fixture():
    row = {"concept": "dart", "proto": "*input", "counterpart": "target"}
    key = tuple(row.values())
    entry = EntryTrace("dart", "*input", None, "target", "target", (
        StageLine("Previous", True, ("*a",)),
        StageLine("OELAdjacentSyncope", True, ("*a",)),
    ), "")
    return row, key, entry


def test_before_uses_sparse_raw_fidelity_and_never_guesses_a_missing_stage():
    row, key, entry = checkpoint_fixture()
    assert controls.before({key: entry}, {}, row, "OELAdjacentSyncope") == "*a"
    fidelity = {key: {"Previous": {"raw": ("*ᶠ*a",), "rejected": False}}}
    assert controls.before({key: entry}, fidelity, row, "OELAdjacentSyncope") == "*ᶠ*a"
    for stages in (entry.stages[:1], entry.stages[1:], entry.stages + entry.stages[1:]):
        with pytest.raises(ValueError, match="required checkpoint"):
            controls.before({key: replace(entry, stages=stages)}, {}, row, "OELAdjacentSyncope")
    with pytest.raises(ValueError, match="fidelity section"):
        controls.before({key: entry}, None, row, "OELAdjacentSyncope")


@pytest.mark.parametrize("record", [
    {"raw": None, "rejected": True},
    {"raw": ("*a", "*b"), "rejected": False},
    {"raw": ("+?",), "rejected": False},
])
def test_before_rejects_rejected_or_ambiguous_checkpoint(record):
    row, key, entry = checkpoint_fixture()
    with pytest.raises(ValueError, match="raw checkpoint"):
        controls.before({key: entry}, {key: {"Previous": record}}, row, "OELAdjacentSyncope")


def test_definition_filter_keeps_transitive_helpers_but_not_unrelated_tails():
    text = "define Helper a;\ndefine Good Helper;\ndefine Bad b;\n"
    selected = controls.selected_definitions(text, ["Good"])
    assert set(controls.parse_defines(selected)) == {"Helper", "Good"}


def test_subprocess_profile_counts_actual_calls_without_changing_results(monkeypatch, capsys):
    def assay(request, profile):
        profile["phase"] = "measurement-control"
        result = subprocess.run([sys.executable, "-c", "print('live')"],
                                check=True, capture_output=True, text=True)
        assert result.stdout == "live\n"
        return {"current": {"live": True}}
    monkeypatch.setattr(controls, "run_controls", assay)
    monkeypatch.setattr(sys, "argv", ["worker", "--request", "dart"])
    controls.main()
    report = json.loads(capsys.readouterr().out)
    profile = report["_execution"]
    assert report["current"] == {"live": True}
    assert profile["subprocess_counts"] == {Path(sys.executable).name: 1}
    assert len(profile["subprocesses"]) == 1
    assert profile["subprocesses"][0]["phase"] == "measurement-control"
    assert profile["subprocesses"][0]["returncode"] == 0
    assert profile["seconds"] >= profile["subprocesses"][0]["seconds"] > 0


def test_profile_preserves_original_subprocess_failure(monkeypatch, capsys):
    def assay(request, profile):
        profile["phase"] = "failure-control"
        subprocess.run([sys.executable, "-c", "raise SystemExit(7)"], check=True)
    monkeypatch.setattr(controls, "run_controls", assay)
    monkeypatch.setattr(sys, "argv", ["worker", "--request", "dart"])
    with pytest.raises(subprocess.CalledProcessError) as failure:
        controls.main()
    assert failure.value.returncode == 7
    assert not capsys.readouterr().out

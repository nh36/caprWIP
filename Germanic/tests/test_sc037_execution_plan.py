"""Selection changes execution extent, never the independent phonological oracle."""

from dataclasses import replace
import ast
import inspect
import json
from pathlib import Path
import subprocess
import sys

import pytest

import sc037_intervention_controls as controls
from oe_trace_parse import EntryTrace, StageLine


def test_dart_plan_has_no_unrelated_models_probes_or_components():
    plan = controls.execution_plan("dart")
    assert plan["variants"] == ["current"]
    assert {p["id"] for p in plan["probes"]} == {
        "metadata-dart", "endpoint-dart", "stage-dart", "dart-stage-foil",
        "dart-AF66Good", "dart-AF66Closed"}


def test_full_plan_retains_consumers_and_omits_unused_roots():
    plan = controls.execution_plan("full")
    assert len(plan["variants"]) == 13
    routine = controls.execution_plan("routine")
    assert set(plan["variants"]) - set(routine["variants"]) == {
        "old-early", "bad-breaking", "early-b"}
    assert all(p["kind"] != "population" for p in plan["probes"])
    assert {p["label"] for p in plan["probes"] if p["kind"] == "tail"} == set(
        controls.CLOSEOUT_RULES)


def test_selected_assertions_take_exact_union_and_do_not_needlessly_prepare_definitions():
    owners = ["test_sc037_intervention.py::" + name for name, group in
              controls.ASSERTION_GROUPS.items() if group in {"dart", "nettle"}]
    plan = controls.execution_plan(owners)
    expected = {p["id"] for group in ("dart", "nettle")
                for p in controls.execution_plan(group)["probes"]}
    assert {p["id"] for p in plan["probes"]} == expected
    assert plan["variants"] == ["current"]
    assert plan["assertion_owners"] == sorted(owners)
    assert not controls.execution_plan("nettle")["compilation_required"]
    assert not controls.execution_plan("fee")["compilation_required"]
    assert controls.execution_plan("pillow")["compilation_required"]
    for selection in ([], ["unknown_test"]):
        with pytest.raises(ValueError, match="selection|unmapped"):
            controls.execution_plan(selection)


def test_every_collected_test_has_an_explicit_dependency_map():
    tree = ast.parse(Path(controls.__file__).with_name("test_sc037_intervention.py").read_text())
    names = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)
             and node.name.startswith("test_")}
    assert names == set(controls.ASSERTION_GROUPS)


def test_missing_required_result_or_probe_fails_explicitly():
    plan = controls.execution_plan("nettle")
    report = {"_execution": {"evaluated": [p["id"] for p in plan["probes"]]}}
    with pytest.raises(ValueError, match="missing required SC037 result"):
        controls.validate_results("nettle", report)
    for probe in plan["probes"]:
        controls.put_result(report, probe["path"], {})
    controls.validate_results("nettle", report)
    report["_execution"]["evaluated"].pop()
    with pytest.raises(ValueError, match="evaluated SC037 probes"):
        controls.validate_results("nettle", report)


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


@pytest.mark.runtime
def test_bounded_probe_preserves_branches_rejection_duplicates_and_epsilon_input():
    from capr_runtime import run_in_runner
    script = """
import sys,tempfile
from pathlib import Path
sys.path.insert(0,"tools")
from anglo_frisian_experiments import _compile_foma,foma_domain
from oe_pipeline import apply_down
from sound_change_order_sensitivity import batch_apply_down
""" + inspect.getsource(controls.bounded_expression) + """
with tempfile.TemporaryDirectory(prefix="capr_sc037_relational_") as temporary:
    root=Path(temporary)
    forms=["a","q","d","a","","e"]
    expression,inputs=bounded_expression(["Base"],forms)
    script=root/"test.foma"
    script.write_text(
        "define Base [a:b|a:c|d:d|e:0|0:w];\\n"
        "define EpsilonReference [z:0] .o. Base;\\n"
        "define Bounded ["+expression+"];\\n"
        "clear stack\\nregex Base;\\nsave stack base.bin\\n"
        "clear stack\\nregex EpsilonReference;\\nsave stack epsilon.bin\\n"
        "clear stack\\nregex Bounded;\\nsave stack bounded.bin\\nquit\\n")
    _compile_foma(script,root)
    outputs=batch_apply_down(root/"bounded.bin",inputs)
    reference=[apply_down(root/"base.bin",form) if form else
               apply_down(root/"epsilon.bin","z") for form in forms]
    assert [set(o) for o in outputs]==[set(o) for o in reference]
    assert set(outputs[0])=={"b","c"}
    assert outputs[1]==[] and outputs[2]==["d"]
    assert outputs[3]==outputs[0] and outputs[4]==["w"] and outputs[5]==[]
print("bounded relational parity")
"""
    proc = run_in_runner(
        't=$(mktemp) && cat > "$t" && python3 "$t"; rc=$?; rm -f "$t"; exit $rc',
        input=script, text=True, capture_output=True, check=True, timeout=60)
    assert "bounded relational parity" in proc.stdout

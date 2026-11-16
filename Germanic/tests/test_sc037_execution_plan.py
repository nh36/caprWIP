"""Selection changes execution extent, never the independent phonological oracle."""

from dataclasses import replace
import ast
import inspect
import json
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

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


@pytest.fixture
def worker_environment(monkeypatch, tmp_path):
    import anglo_frisian_experiments as compiler
    import capr_runtime

    germanic = Path(controls.__file__).resolve().parents[1]
    runtime = SimpleNamespace(
        germanic_fst=germanic / "fsts/germanic.txt",
        corpus_tsv=germanic / "data/germanic-aligned-final.tsv",
        data_dir=germanic / "data", bin_dir=tmp_path)
    monkeypatch.setattr(capr_runtime, "layout", lambda: runtime)
    monkeypatch.setattr(capr_runtime, "check_build_manifest", lambda names: [])
    monkeypatch.setenv("CAPR_FOMA_DEFINITION_IMAGE", "")
    calls = []

    def forbidden(*args, **kwargs):
        pytest.fail("unexpected private definition preparation")

    def raw(argv, **kwargs):
        assert argv[0] == "flookup"
        form = kwargs["input"].decode().rstrip("\n")
        return subprocess.CompletedProcess(argv, 0, stdout=(form + "\t*stage\n\n").encode())

    def compile_script(script, directory):
        text = script.read_text()
        calls.append(text)
        import re
        for name in re.findall(r"(?m)^save stack (\S+)", text):
            (directory / name).write_bytes(b"test-network")

    monkeypatch.setattr(controls, "prepare_definition_image", forbidden)
    monkeypatch.setattr(controls.subprocess, "run", raw)
    monkeypatch.setattr(controls, "batch_apply_down",
                        lambda binary, forms: [["result"] for _ in forms])
    monkeypatch.setattr(compiler, "_compile_foma", compile_script)
    monkeypatch.setattr(compiler, "definition_image_source",
                        lambda text, directory: "load defined /test/session.bin\nclear stack\n")
    return calls


def test_production_only_worker_never_prepares_or_compiles_definitions(worker_environment):
    owners = [name for name, group in controls.ASSERTION_GROUPS.items()
              if group in {"nettle", "fee"}]
    profile = {}
    report = controls.run_controls(owners, profile, definition_mode="session")
    controls.validate_results(owners, {**report, "_execution": profile})
    assert worker_environment == []
    assert profile["definition_image_origin"] == "none"
    assert profile["definition_preparation_seconds"] == 0
    assert profile["networks"] == {"production": 1, "bounded": 0}


@pytest.mark.parametrize("selection,variants,exports", [
    ("routine", 10, 54), ("full", 13, 57),
    (["test_selected_dart_protects_closed_final_pre_l_nonapplication",
      "test_selected_nettle_has_live_open_medial_deletion"], 1, 3),
])
def test_worker_sends_only_bounded_selected_compositions_through_shared_definitions(
        worker_environment, monkeypatch, tmp_path, selection, variants, exports):
    image = tmp_path / "session.bin"
    image.with_suffix(".json").write_text('{"test": "session"}')
    monkeypatch.setenv("CAPR_FOMA_DEFINITION_IMAGE", str(image))
    profile = {}
    report = controls.run_controls(selection, profile, definition_mode="session")
    controls.validate_results(selection, {**report, "_execution": profile})
    assert len(worker_environment) == len(profile["models"]) == variants
    assert sum(len(model["queries"]) for model in profile["models"]) == exports
    assert profile["networks"] == {"production": 1, "bounded": exports}
    for model, script in zip(profile["models"], worker_environment):
        assert model["image_loaded"] and not model["fallback"]
        assert script.startswith("load defined ")
        assert "AFContextRoot" not in script and "old_english_variant.bin" not in script
        for index, query in enumerate(model["queries"]):
            domain = controls.foma_domain(query["inputs"])
            expression = " .o. ".join(query["members"])
            assert f"define AFSelected{index} [{domain} .o. {expression}];" in script


@pytest.mark.parametrize("mode,ambient", [
    ("full-source", False), ("full-source", True), ("auto", False),
])
def test_full_source_intent_and_standalone_preparation(
        worker_environment, monkeypatch, tmp_path, mode, ambient):
    image = tmp_path / "session.bin"
    image.with_suffix(".json").write_text('{"test": "session"}')
    if ambient:
        monkeypatch.setenv("CAPR_FOMA_DEFINITION_IMAGE", str(image))
    prepared = []
    def prepare(*args):
        prepared.append(True)
        return image
    monkeypatch.setattr(controls, "prepare_definition_image", prepare)
    profile = {}
    controls.run_controls("dart", profile, definition_mode=mode)
    assert prepared == ([True] if mode == "auto" else [])
    assert len(worker_environment) == 1
    assert worker_environment[0].startswith("load defined ") == (mode == "auto")
    assert profile["definition_image_origin"] == ("worker" if mode == "auto" else "full-source")
    if mode == "full-source":
        assert profile["definition_image_receipt"] is None
        assert not profile["models"][0]["image_supplied"]


def test_missing_session_image_fails_instead_of_preparing_a_private_one(worker_environment):
    with pytest.raises(ValueError, match="requires the selected session"):
        controls.run_controls("dart", {}, definition_mode="session")
    assert worker_environment == []


@pytest.mark.parametrize("group,fresh,uses_fixture", [
    ("nettle", False, False), ("dart", True, False), ("dart", False, True),
])
def test_pytest_fixture_passes_definition_intent_without_accidental_preparation(
        monkeypatch, tmp_path, group, fresh, uses_fixture):
    import test_sc037_intervention as owner
    name = next(name for name, value in controls.ASSERTION_GROUPS.items() if value == group)
    requested, commands = [], []
    def fixture(name):
        requested.append(name)
        return "export CAPR_FOMA_DEFINITION_IMAGE=/session.bin; "
    def run(command, **kwargs):
        commands.append(command)
        return SimpleNamespace(stdout=json.dumps({"_execution": {
            "request": [], "networks": {}, "subprocess_counts": {}, "seconds": 0}}))
    monkeypatch.setattr(owner, "ROOT", tmp_path)
    monkeypatch.setattr(owner, "run_in_runner", run)
    monkeypatch.setattr(owner, "validate_results", lambda *args: None)
    request = SimpleNamespace(
        module=owner, session=SimpleNamespace(items=[
            SimpleNamespace(module=owner, nodeid="test_sc037_intervention.py::" + name)]),
        getfixturevalue=fixture,
        config=SimpleNamespace(
            getoption=lambda option: fresh,
            pluginmanager=SimpleNamespace(getplugin=lambda name: None)))
    owner.current.__wrapped__(request, lambda *args: None)
    assert requested == (["isolated_definitions"] if uses_fixture else [])
    assert ("--definitions full-source" if fresh else "--definitions session") in commands[0]


def test_subprocess_profile_counts_actual_calls_without_changing_results(monkeypatch, capsys):
    def assay(request, profile, *, definition_mode):
        assert definition_mode == "auto"
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
    def assay(request, profile, *, definition_mode):
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


@pytest.mark.runtime
def test_sc037_worker_shared_and_explicit_full_source_execute_the_same_small_live_case():
    from capr_runtime import run_in_runner
    worker = Path(controls.__file__).read_text().split('if __name__ == "__main__":')[0]
    script = worker + """
from types import SimpleNamespace
import capr_runtime
with tempfile.TemporaryDirectory(prefix="capr_sc037_definition_intent_") as temporary:
    root = Path(temporary)
    source = root / "source.txt"
    source.write_text("define Base [a:b | a:c | e:0];\\n")
    image = prepare_definition_image(source, root)
    assert image is not None
    os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
    runtime = SimpleNamespace(germanic_fst=source, data_dir=Path("/usr/app/data"),
                              bin_dir=root, corpus_tsv=root/"unused.tsv")
    probe = {"id":"small", "kind":"component", "variant":"current",
             "members":["Base"], "inputs":["a","q","a","e"], "path":["current","small"]}
    def forbidden(*args):
        raise AssertionError("worker unexpectedly prepared an image")
    reports = []
    with patch.object(capr_runtime, "layout", return_value=runtime), \\
         patch.object(capr_runtime, "check_build_manifest", return_value=[]), \\
         patch.dict(globals(), {
             "corpus_rows":lambda path: [],
             "execution_plan":lambda request: {"probes":[probe]},
             "model_definitions":lambda path: ("",""),
             "variant_edits":lambda: ({"current":{}},{"current":("","")}),
             "complete_variant_order":lambda recipe: ["Base"],
             "prepare_definition_image":forbidden}):
        for mode in ("session","full-source"):
            profile = {}
            report = run_controls("small", profile, definition_mode=mode)
            assert profile["models"][0]["image_loaded"] == (mode == "session")
            assert profile["definition_preparation_seconds"] == 0
            reports.append(report["current"]["small"])
    assert reports[0] == reports[1]
    assert set(reports[0][0]) == set(reports[0][2]) == {"b","c"}
    assert reports[0][1] == reports[0][3] == []
print("SC037 shared/full-source live parity")
"""
    proc = run_in_runner(
        't=$(mktemp) && cat > "$t" && python3 "$t"; rc=$?; rm -f "$t"; exit $rc',
        input=script, text=True, capture_output=True, check=True, timeout=60)
    assert "SC037 shared/full-source live parity" in proc.stdout

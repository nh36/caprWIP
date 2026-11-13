"""Fresh current-cascade controls for the source-supported Model B subset."""

import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from adjudication_control import runtime_lock
from capr_runtime import run_in_runner

pytestmark = pytest.mark.runtime

CONTROLS = [
    ("oral", "PWGmcSurvivingBimoricOUnrounding", "*r*á*t*ō", "*r*á*t*ā"),
    ("nasal", "PWGmcSurvivingBimoricOUnrounding", "*r*á*t*ǭ", "*r*á*t*ā"),
    ("trimoric", "PWGmcSurvivingBimoricOUnrounding", "*r*á*t*ô", "*r*á*t*ô"),
    ("stressed-root", "PWGmcSurvivingBimoricOUnrounding", "*θ*ǭ", "*θ*ǭ"),
    ("nasal-root-and-ending", "PWGmcSurvivingBimoricOUnrounding", "*r*ǭ*t*ǭ", "*r*ǭ*t*ā"),
    ("low-nasal-root", "PWGmcSurvivingBimoricOUnrounding", "*θ*ã*x*ǭ", "*θ*ã*x*ā"),
    ("protected-ending", "PWGmcSurvivingBimoricOUnrounding", "*r*á*t*ō*n", "*r*á*t*ō*n"),
    ("short-nasal", "PWGmcSurvivingBimoricOUnrounding", "*r*á*t*ą", "*r*á*t*ą"),
    ("secondary-front-stop", "OEVelarPalatalization", "*t*u*n*g*ǣ", "*t*u*n*g*ǣ"),
    ("original-high-stop", "OEVelarPalatalization", "*l*a*n*g*ī", "*l*a*n*ʤ*ī"),
    ("singleton-fricative", "OEVelarPalatalization", "*b*e*g*e", "*b*e*ʝ*e"),
    ("initial-fricative", "OEVelarPalatalization", "*g*æ", "*ʝ*æ"),
    ("velar-back-back", "OEHLoss", "*w*l*ō*x*u*m", "*w*l*ō*u*m"),
    ("palatal-loss", "OEHLoss", "*θ*ō*ç*æ", "*θ*ō*æ"),
    ("geminate-velar", "OEHLoss", "*a*x*x*a", "*a*x*x*a"),
    ("geminate-palatal", "OEHLoss", "*a*ç*ç*a", "*a*ç*ç*a"),
    ("pretonic", "OEHLoss", "*ᶠ*b*i*x*í*n*d*a*n", "*ᶠ*b*i*x*í*n*d*a*n"),
]

SCRIPT = r'''
import json, tempfile, sys
from pathlib import Path
sys.path.insert(0, "/usr/app/tools")
from anglo_frisian_experiments import compile_isolated
from capr_runtime import layout, check_build_manifest
from oe_pipeline import stages
from sound_change_order_sensitivity import batch_apply_down
controls = __CONTROLS__
rt = layout()
problems = check_build_manifest(["old_english.bin", *(stage.snapshot_bin for stage in stages())])
assert not problems, problems
recipe = {
    "id": "final-nasal-controls", "replace": {}, "insert_rule": "",
    "insert_after": "", "definitions": "",
    "component_checks": [{"component": c[1]} for c in controls],
}
with tempfile.TemporaryDirectory(prefix="capr_final_nasal_") as temporary:
    bins = compile_isolated(rt.germanic_fst, recipe, [], Path(temporary), components_only=True)
    observed = {
        name: batch_apply_down(bins["component:" + component], [value])[0]
        for name, component, value, expected in controls
    }
    raw = ["márōn", "fláskōn", "táixōn", "túngōn", "rástōz",
           "námô", "gébōz", "gébǭ", "gébôz"]
    finals = batch_apply_down(rt.bin_dir / "old_english.bin", raw)
print(json.dumps({"controls": observed, "raw": raw, "finals": finals}, ensure_ascii=False))
'''


@pytest.fixture(scope="module")
def observed(isolated_definitions):
    with runtime_lock("Final nasal candidate source-backed controls"):
        result = run_in_runner(
            isolated_definitions
            + 't=$(mktemp) && cat > "$t" && python3 "$t"; rc=$?; rm -f "$t"; exit $rc',
            input=SCRIPT.replace("__CONTROLS__", repr(CONTROLS)),
            text=True, capture_output=True, timeout=1800)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


@pytest.mark.parametrize("name,component,value,expected", CONTROLS, ids=[c[0] for c in CONTROLS])
def test_source_supported_positive_and_negative_controls(observed, name, component, value, expected):
    assert observed["controls"][name] == [expected]


def test_complete_inputs_preserve_quantity_and_resolve_only_the_intended_nominative(observed):
    assert observed["finals"] == [
        ["mære"], ["flæsċe"], ["tā"], ["tunge"], ["ræste"],
        ["nama"], ["ġiefe"], ["ġiefe"], ["ġiefa"],
    ]

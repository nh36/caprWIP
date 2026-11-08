"""Historical controls distinguish fixes from meaningful wrong implementations."""

import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from capr_runtime import run_in_runner

pytestmark = pytest.mark.runtime


@pytest.fixture(scope="module")
def current():
    worker = Path(__file__).with_name("sc037_intervention_controls.py")
    result = run_in_runner(
        "CAPR_AF_DEFINITION_ISOLATED=1 python3 -",
        input=worker.read_text(), text=True, capture_output=True,
        check=True, timeout=3600)
    return json.loads(result.stdout)


def test_canonical_compound_hypotheses_discriminate_three_wrong_accounts(current):
    for form in ("sáli-wàrðaz", "sáli-wàrðuz", "sáli-wàrðą"):
        assert current["current"]["canonical"][form] == ["seleweard"]
        assert current["old-early"]["canonical"][form] == ["sealweard"]
        assert current["bad-breaking"]["canonical"][form] == ["seleoweard"]
        # Replacing unified HVD also removes final deletion in the u-stem foil.
        wrong = "selweardu" if form == "sáli-wàrðuz" else "selweard"
        assert current["no-weight"]["canonical"][form] == [wrong]


def test_independent_preoe_stages_test_weight_mutation_and_loss(current):
    assert current["current"]["furthest"] == [["ȳtmest"]]
    assert current["no-high"]["furthest"] == [["ȳtemest"]]
    assert current["opaque-umlaut"]["furthest"] == [["ūtmest"]]
    assert current["current"]["companion"] == [["gædeling"]]
    assert current["no-weight"]["companion"] == [["gædling"]]
    assert current["no-high"]["companion"] == [["gædeling"]]


def test_selected_weight_negative_and_previous_breaking_umlaut_histories(current):
    values = current["current"]["canonical"]
    assert values["wíduwōn"] == ["wuduwe"]
    assert current["no-weight"]["canonical"]["wíduwōn"] == ["wudwe"]
    assert values["knéwai"] == ["cneowe"]
    assert values["fūliθǭ"] == ["fȳlþe"]
    assert values["spénnilǭ"] == ["spinle"]
    selected = current["current"]["selected"]
    assert len(selected) == 391
    assert all(len(row["outputs"]) == 1 for row in selected)
    assert {row["concept"] for row in selected
            if row["outputs"] != [row["counterpart"]]} == {
                "buck", "fire", "fowl", "rust", "straw", "tap", "wolf", "wool"}


def test_weak_breaking_root_breaking_and_high_front_blockers(current):
    assert current["current"]["breaking"] == [
        ["*f*u*l*w*i*x*t"], ["*n*a*w*i*x*t"],
        ["*s*io*w"], ["*s*ío*w"], ["*b*io*r*x*t"],
        ["*w*i*w*i"], ["*w*i*w*ī"],
        ["*s*æ*l*io*w*ea*r*d"], ["*ᶠ*b*i*s*io*w"],
    ]


def test_closed_medial_syllables_and_secondary_high_stress_are_preserved(current):
    values = current["current"]
    assert values["high"] == [
        ["*s*e*l*i*w*ea*r*d"], ["*x*a*n*d*s*ea*x"],
        ["*ȳ*t*m*i*s*t"], ["*b*o*n*d*i*n*s*t*a"],
        ["*ʃ*y*l*d*ç*ǣ*t*j*ā"], ["*l*a*n*d*w*i*n*a"],
    ]
    assert values["stressed"] == ["*l*á*n*d*x*y*m*i", "*l*á*n*d*w*i*n*a"]
    assert values["umlaut"] == [
        ["*ȳ*t*y*m*i"], ["*g*æ*d*y*l*i*n*g"],
        ["*ū*t*e*m*i"], ["*ū*t*ỳ*m*i"],
    ]
    assert values["atomic_iu"] == [["*s*íu*w*à*r*d*a*z"]]


def test_selected_accusatives_discriminate_mutation_and_degemination_order(current):
    assert current["early-high"]["canonical"]["fūliθǭ"] == ["fūlþe"]
    assert current["early-high"]["canonical"]["spénnilǭ"] == ["spenle"]
    assert current["late-high"]["canonical"]["spénnilǭ"] == ["spinnle"]
    assert current["no-high"]["canonical"]["fūliθǭ"] == ["fȳleþe"]
    assert current["no-high"]["canonical"]["spénnilǭ"] == ["spinnele"]
    assert current["current"]["heads"] == [["hēafodu"]]


def test_early_n_loss_preserves_later_livestock_and_inherited_fright(current):
    assert current["current"]["blockers"]["late-livestock"] == [["nēten"]]
    assert current["late-n-loss"]["blockers"]["late-livestock"] == [["nēte"]]
    assert current["current"]["blockers"]["early-fright"] == [["fyrhte"]]
    assert current["no-n-loss"]["blockers"]["early-fright"] == [["fyrhten"]]
    assert current["current"]["n_loss"] == [
        ["*f*ú*r*x*t*ī"], ["*p*ú*l*w*ī"], ["*s*t*r*á*n*g*ī"],
        ["*t*ú*n*g*a*n"], ["*s*t*ī"], ["*s*t*ḯ*n"],
    ]


def test_pillow_requires_general_noninitial_w_loss_not_a_lexical_exemption(current):
    assert current["current"]["blockers"]["early-pillow"] == [["pyle"]]
    assert current["old-w-loss"]["blockers"]["early-pillow"] == [["pylwe"]]
    assert current["no-n-loss"]["blockers"]["early-pillow"] == [["pylen"]]
    assert current["current"]["w_loss"] == [
        ["*w*ī"], ["*s*w*ī"], ["*a*i"], ["*p*y*l*ī"],
        ["*p*y*l*w*í"], ["*g*ea*r*i*d*e"],
    ]


def test_fee_transponent_is_not_a_new_post_h_deletion(current):
    assert current["current"]["fee"] == [["feoh"], ["feou"], ["feoh"]]
    fee = next(row for row in current["current"]["selected"] if row["id"] == "2006")
    assert fee["reconstruction"] == "*féxu"
    assert fee["proto"] == "*féx"
    assert fee["outputs"] == ["feoh"]


def test_weak_unrounding_light_retention_and_positional_labials(current):
    assert current["current"]["canonical"]["régna-bùgô"] == ["reġnboga"]
    assert current["early-b"]["canonical"]["régna-bùgô"] == ["reġnfoga"]
    assert current["no-unrounding"]["companion"] == [["gædyling"]]
    assert current["current"]["weak"] == [
        ["*y*n"], ["*g*æ*d*i*l*i*n*g"], ["*l*a*n*d*x*ỳ*m*i"]]
    assert current["current"]["light"] == [
        ["*n*e*t*l*ǭ"], ["*g*æ*d*i*l*i*n*g"], ["*k*e*t*i*l"],
        ["*a*θ*i*l*a"], ["*a*f*i*l*a"]]
    assert current["current"]["labial"] == [
        ["*b*a"], ["*a*β*a"], ["*l*a*m*b"], ["*x*a*b*b*a"],
        ["*r*e*g*n*b*o*g*ô"], ["*r*e*g*n*β*o*g*ô"]]

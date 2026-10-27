"""Input coverage must not be confused with a successful inherited derivation."""

import gzip
import json
import shlex
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import oe_pipeline
from capr_runtime import check_build_manifest, layout, run_in_runner
from executable_facts import parse_defines

AUDIT = ROOT / "Germanic/docs/sound_changes/audits/lexical-witnesses-2335-2336"
BASE = "0dd533e3f15c85f20a976a3781a9b4d79bf6f928"


def receipt(name):
    return json.loads(gzip.decompress((AUDIT / name).read_bytes()))


def candidates(data):
    return {row["name"]: row for row in data["candidates"]}


def lookup(bin_name, forms):
    result = run_in_runner(
        f"flookup -i {shlex.quote(bin_name)}",
        input="\n".join(dict.fromkeys(forms)) + "\n", text=True, capture_output=True,
        check=True, timeout=120,
    )
    outputs = {form: [] for form in forms}
    for line in result.stdout.splitlines():
        if line.strip():
            form, output = line.split("\t", 1)
            if output != "+?" and output not in outputs[form]:
                outputs[form].append(output)
    return outputs


def test_extension_changes_only_input_grammar_not_sound_laws():
    old = parse_defines(subprocess.check_output(
        ["git", "show", f"{BASE}:Germanic/fsts/germanic.txt"], cwd=ROOT, text=True,
    ))
    current = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
    assert current.keys() - old.keys() == {"pgrmInputTailVowel"}
    assert not old.keys() - current.keys()
    assert {name for name in old
            if old[name].definition_raw != current[name].definition_raw} == {
                "pgrmSimpleWord", "pgrmCompoundSecond",
            }
    for name in ("pgrmSimpleWord", "pgrmCompoundSecond"):
        assert current[name].definition_raw.replace(
            "pgrmInputTailVowel", "pgrmWeakTailVowel") == old[name].definition_raw
    expected = (
        "define pgrmInputTailVowel [ pgrmWeakTailVowel | "
        "{ai}:{*ai} z:{*z} ō:{*ō} z:{*z} | i:{*i} z:{*z} ō:{*ō} z:{*z} ];"
    )
    assert current["pgrmInputTailVowel"].definition_raw == expected


def test_gate_receipt_conserves_every_preexisting_record_and_order():
    before = receipt("pre_gate.json.gz")
    extended = receipt("gate_experiment.json.gz")
    assert before["source_sha256"] == extended["source_sha256"]
    assert before["existing_population"] == extended["existing_population"]
    assert before["order"] == extended["order"]
    assert before["order"] == [
        stage.foma_identifier if stage.kind == "named" else stage.inline_text
        for stage in oe_pipeline.stages()
    ]
    assert extended["production_equivalent"]
    old, new = candidates(before), candidates(extended)
    assert old.keys() == new.keys()
    changed = {name for name in old
               if old[name]["final_outputs"] != new[name]["final_outputs"]}
    assert changed == {
        "earthly-genitive-feminine-compound", "earthly-genitive-feminine-grave",
    }


def test_admission_exposes_mismatches_without_protecting_suffix_u():
    data = candidates(receipt("gate_experiment.json.gz"))
    assert data["which-compound-notation"]["final_outputs"] == ["hwileċ"]
    plain = data["earthly-genitive-feminine-compound"]
    grave = data["earthly-genitive-feminine-grave"]
    assert plain["parser_accepted"] and grave["parser_accepted"]
    assert plain["final_outputs"] == ["eorþocundere"]
    assert grave["final_outputs"] == ["eorþcondere"]
    changed = {
        row["name"]: [step["stage"] for step in row["steps"] if step["changed"]]
        for row in (plain, grave)
    }
    assert "OECompoundLinkingSyncope" not in changed[plain["name"]]
    assert "OECompoundLinkingSyncope" in changed[grave["name"]]
    assert changed[grave["name"]].index("OEStripSecondaryStress") < (
        changed[grave["name"]].index("OEMedUnstressedULowering"))
    assert data["world-selected-control"]["final_outputs"] == ["weorold"]
    assert data["rainbow-selected-control"]["final_outputs"] == ["reġnboga"]
    for row in (plain, grave):
        assert row["rejection"] is None
        assert len(row["steps"]) == len(receipt("gate_experiment.json.gz")["order"])


@pytest.mark.runtime
def test_production_gate_is_generic_and_preserves_every_old_output():
    assert check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], layout(),
    ) == []
    gate = oe_pipeline.stage_for("EnglishProtoInput").snapshot_bin
    forms = [
        "érθa-kunðaizōz", "érθa-kùnðaizōz",
        "fúllaizōz", "fúllizōz",
        "érθa-kùnðaizōzz", "érθa-kùnðaizō", "xláiba-warðaz",
    ]
    outputs = lookup(gate, forms)
    assert outputs[forms[0]] == ["*é*r*θ*a*k*u*n*ð*ai*z*ō*z"]
    assert outputs[forms[1]] == ["*é*r*θ*a*k*ù*n*ð*ai*z*ō*z"]
    assert outputs[forms[2]] == ["*f*ú*l*l*ai*z*ō*z"]
    assert outputs[forms[3]] == ["*f*ú*l*l*i*z*ō*z"]
    assert all(outputs[form] == [] for form in forms[4:])
    records = receipt("pre_gate.json.gz")["existing_population"]["records"]
    old_inputs = [row["fst_input"] for row in records]
    current = lookup("old_english.bin", old_inputs + forms[:2] + ["xwí-līkaz"])
    for row in records:
        assert current[row["fst_input"]] == row["outputs"].split("|")
    assert current[forms[0]] == ["eorþocundere"]
    assert current[forms[1]] == ["eorþcondere"]
    assert current["xwí-līkaz"] == ["hwileċ"]

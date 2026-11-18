"""Low-vowel loss, final-n exposure and source-backed weak-cell admission."""
import functools
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Germanic/docs/sound_changes/audits/sc047-sc048-evidence"
BASE = "3f2bbd90307e0b4157e8c544da55b1de8f759a93"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines
from oe_trace_parse import parse_entries


@functools.lru_cache(maxsize=1)
def baseline_definitions():
    return parse_defines(subprocess.check_output(
        ["git", "show", BASE + ":Germanic/fsts/germanic.txt"], cwd=ROOT, text=True))


def before_sc047_adoption(current):
    """Authenticate the input-only layer before applying older exact guards."""
    previous = baseline_definitions()
    extra = """a:{*a} n:{*n} ų:{*ų} |
        a:{*a} m:{*m} a:{*a} z:{*z} |
        a:{*a} m:{*m} m:{*m} a:{*a} z:{*z} |
        o:{*o} n:{*n} m:{*m} i:{*i} z:{*z}"""
    expected = previous["PGWeakTails"].body.rstrip()[:-1] + "|" + extra + "]"
    assert current.keys() == previous.keys()
    for name in previous:
        body = expected if name == "PGWeakTails" else previous[name].body
        assert "".join(current[name].body.split()) == "".join(body.split()), name
    return previous


def report():
    return json.loads((AUDIT / "evidence.json").read_text())


def test_current_census_deletes_short_nasal_a_without_a_weight_or_class_filter():
    entries = parse_entries(
        (ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt").read_text())
    nasal, secondary = set(), set()
    for entry in entries.values():
        for label, population in [
            ("OEHeavySyllableNasalApocope", nasal),
            ("OESecondaryNasalization", secondary),
        ]:
            i = next(i for i, stage in enumerate(entry.stages) if stage.label == label)
            before, after = entry.stages[i - 1].forms, entry.stages[i].forms
            if before == after:
                continue
            population.add(entry.concept)
            assert len(before) == len(after) == 1
            if label == "OEHeavySyllableNasalApocope":
                assert entry.proto.endswith("ą")
                assert before[0].endswith("*ą")
                assert after == (before[0][:-2],)
            else:
                assert entry.proto.endswith("aną")
                assert before[0].endswith("*a*n")
                assert after == (before[0][:-4] + "*ą*n",)
    expected = report()["census"]
    assert nasal == {r["concept"] for r in expected["SC047"]}
    assert secondary == {r["concept"] for r in expected["SC048"]}
    assert {"thatch", "horn", "bake", "bind", "net", "hue"} <= nasal
    assert {"bake", "bind", "sow", "betray"} <= secondary
    assert not {"flask", "straw", "rainbow", "earthly"} & nasal
    assert not {"thatch", "horn", "bast", "do", "flask"} & secondary


def test_archived_matrix_authenticates_execution_and_distinct_mechanisms():
    manifest = json.loads((AUDIT / "manifest.json").read_text())
    assert hashlib.sha256((AUDIT / "experiments.zip").read_bytes()).hexdigest() == (
        manifest["archive_sha256"])
    with zipfile.ZipFile(AUDIT / "experiments.zip") as archive:
        assert set(archive.namelist()) == set(manifest["members"])
        for name, digest in manifest["members"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
    data = report()
    initial = data["runs"]["initial"]
    assert initial["early_loss"]["changed"] == 0
    assert initial["47-46-48"]["changed"] == 0
    assert initial["47-48-46"]["changed"] == 7
    assert initial["48-47-46"]["changed"] == 89
    assert initial["before_SC023_negative"]["rejected"] == 1
    assert [r["concept"] for r in initial["before_SC023_negative"]["deltas"]
            if not r["outputs"]] == ["do"]
    followup = data["runs"]["followup"]
    assert followup["early_coda_i_onset_restore"]["changed"] == 0
    assert followup["direct_strict_WS"]["changed"] == 0
    assert initial["nasal_after_back_WS"]["changed"] == 2
    assert followup["nasal_after_back_strict_WS"]["changed"] == 0
    assert data["runs"]["admission"]["after_rhotacism"]["changed"] == 0
    assert {r["lexical_item"] for r in data["historical_reversal"]} == (
        {r["concept"] for r in data["census"]["SC048"]} - {"sow", "betray"})


def test_only_the_source_backed_productive_input_tails_change():
    before_sc047_adoption(
        parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text()))


@pytest.mark.runtime
def test_live_gate_accepts_unselected_source_cells_without_repairing_their_histories():
    from capr_runtime import check_build_manifest, layout, run_in_runner
    import oe_pipeline
    assert check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], layout()) == []
    forms = ["gúmanų", "gúmamaz", "gúmammaz", "gúmonmiz", "gúmonų", "gúmaniz"]
    gate = oe_pipeline.stage_for("EnglishProtoInput").snapshot_bin
    result = run_in_runner(
        "flookup -i " + gate, input="\n".join(forms) + "\n",
        text=True, capture_output=True, check=True, timeout=120)
    observed = {form: [] for form in forms}
    for line in result.stdout.splitlines():
        if line.strip():
            form, output = line.split("\t", 1)
            if output != "+?" and output not in observed[form]:
                observed[form].append(output)
    for form in forms:
        assert observed[form] == ["*" + "*".join(form)]
    # Admission is not evidence that the whole paradigm is implemented.
    candidate = report()["admitted_source_cells"]
    assert candidate["guma_acc_RTaylor"] == ["gumn"]
    assert candidate["guma_acc_Fulk_PGmc"] == ["guman"]

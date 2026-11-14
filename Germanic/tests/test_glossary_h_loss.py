"""External glossary witnesses, not accepted corpus rows or endpoint targets.

Sweet1885 p.36, Epinal3: thohae (argillus); p.41, Corpus207: thoae (argilla).
RingeTaylor2014 p.314, sec.6.9.3 reads thohae/thoae as thōhæ/thōæ > þō.
Sweet1885 p.104, Epinal1066 and the aligned Erfurt parallel: uulohum
(villis); p.107, Corpus2122: uuloum. Normalized wlōhum > wlōum is dat.pl.;
RingeTaylor's *wlōm is reconstructed, not the attested test target.

Written h does not identify [x] versus [ç]. The corrected candidate supplies
an early front ending and ç; the corrected lexical base had x before the
late front ending e. The feature assertion below does not equate cascade e
with diplomatic ae or establish the historical chronology of the ae/e merger.
"""

import json
from pathlib import Path
import re
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from adjudication_control import runtime_lock
from capr_runtime import run_in_runner

pytestmark = pytest.mark.runtime

SCRIPT = r'''
import hashlib, json, tempfile
from pathlib import Path
import sys
sys.path.insert(0, "/usr/app/tools")
import oe_pipeline as pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from cascade_baseline import build_baseline, read_baseline
from sound_change_order_sensitivity import batch_apply_down

rt = layout()
stages = pipeline.named_stages()
by_name = {s.foma_identifier: s for s in stages}
assert len(by_name) == len(stages), "ambiguous executable checkpoint"
expected_bins = ["old_english.bin", *(s.snapshot_bin for s in stages)]
problems = check_build_manifest(expected_bins)
assert not problems, problems

def named(identifier):
    stage = pipeline.stage_for(identifier)
    assert by_name[identifier] == stage
    return stage

def predecessor(identifier):
    stage = pipeline.previous_stage(named(identifier).foma_identifier)
    assert stage is not None, "missing preceding checkpoint: " + identifier
    return stage.foma_identifier

def one(outputs):
    assert len(outputs) == 1 and outputs[0] != "+?", (
        "rejected or ambiguous stage output", outputs)
    return outputs

clay_input = "*θ*á*n*x*ō*n"
entry = named("PGmcNasalLossBeforeX").foma_identifier
clay_stops = {
    "nasal_loss": entry,
    "palatalization": named("OEVelarFricativePalatalization").foma_identifier,
    "before_h_loss": predecessor("OEHLoss"),
    "before_contraction": predecessor("OEContraction"),
    "after_contraction": named("OEContraction").foma_identifier,
    "surface": named("OldEnglishSurface").foma_identifier,
}
extra = """
define AFCRev [OEContraction .o. OEHLoss];
define AFFrontH [
    {*x} -> 0 || EnglishStarFrontVowel _ EnglishStarVocalic,
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarFrontVowel
];
"""
components = ["OEHLoss", "OEContraction", "AFFrontH", "AFCRev"]
for identifier in components:
    if not identifier.startswith("AF"):
        named(identifier)
recipe = {
    "id": "glossary-h-loss", "replace": {}, "insert_rule": None,
    "insert_after": None, "definitions": extra,
    "component_checks": [{"component": s} for s in components],
}
stage_slice = [
    s for s in pipeline.stages()
    if named(entry).exec_index <= s.exec_index
    <= named("OldEnglishSurface").exec_index]
slice_components = [
    s.inline_text if s.kind == "inline" else s.foma_identifier
    for s in stage_slice]
protected = [rt.germanic_fst, rt.corpus_tsv, rt.build_manifest,
             *(rt.bin_dir / name for name in expected_bins)]
baseline_dir = rt.docs_dir / "sound_changes/cascade_baseline"
protected.extend(p for p in baseline_dir.iterdir() if p.is_file())
before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
with tempfile.TemporaryDirectory(prefix="capr_clay_fringe_") as temporary:
    bins = compile_isolated(
        rt.germanic_fst, recipe, [], Path(temporary), components_only=True,
        diagnostic_stages=slice_components)
    def apply(component, value):
        return one(batch_apply_down(bins["component:" + component], [value])[0])
    clay, clay_trace, states = {}, [], [clay_input]
    pretonic, pretonic_trace = {}, []
    pretonic_states = ["*ᶠ*b*i*x*í*n*d*a*n"]
    unmarked_states = None
    prefix_stage = named("OEPrefixIReduction")
    h_loss_stage = named("OEHLoss")
    for number, stage in enumerate(stage_slice):
        states = one(batch_apply_down(bins["diagnostic:" + str(number)], states)[0])
        clay_trace.append({"stage": slice_components[number], "outputs": states})
        for key, stop in clay_stops.items():
            if stage.foma_identifier == stop:
                clay[key] = states
        if stage.exec_index >= prefix_stage.exec_index:
            pretonic_states = one(batch_apply_down(
                bins["diagnostic:" + str(number)], pretonic_states)[0])
            if stage == prefix_stage:
                pretonic["after_prefix_reduction"] = pretonic_states
                unmarked_states = [pretonic_states[0].replace("*ᶠ", "")]
            elif stage.exec_index < h_loss_stage.exec_index:
                unmarked_states = one(batch_apply_down(
                    bins["diagnostic:" + str(number)], unmarked_states)[0])
                assert [pretonic_states[0].replace("*ᶠ", "")] == unmarked_states, (
                    "retained stress marker changed an intervening stage", stage)
            if stage.foma_identifier == predecessor("OEHLoss"):
                pretonic["before_h_loss"] = pretonic_states
            if stage == h_loss_stage:
                pretonic["after_h_loss"] = pretonic_states
            if stage.foma_identifier == "OldEnglishSurface":
                pretonic["surface"] = pretonic_states
            pretonic_trace.append({
                "stage": slice_components[number], "outputs": pretonic_states})
    assert set(clay) == set(clay_stops), "missing clay checkpoint"
    before_h = clay["before_h_loss"][0]
    reversed_clay = {
        "before_contraction": [before_h],
        "after_contraction": apply("OEContraction", before_h),
        "after_loss": apply("AFCRev", before_h),
    }
    states = reversed_clay["after_loss"]
    for number, stage in enumerate(stage_slice):
        if stage.exec_index > named("OEContraction").exec_index:
            states = one(batch_apply_down(
                bins["diagnostic:" + str(number)], states)[0])
    reversed_clay["surface"] = states
    fringe_input = "*w*l*ō*x*u*m"
    front_control = "*t*ā*x*e"
    fringe = {
        "input": fringe_input,
        "after_h_loss": apply("OEHLoss", fringe_input),
        "front_only": apply("AFFrontH", fringe_input),
        "front_only_positive_input": front_control,
        "front_only_positive": apply("AFFrontH", front_control),
    }

    toe = [r for r in pipeline.load_rows(rt.corpus_tsv) if r["concept"] == "toe"]
    assert len(toe) == 1
    toe = toe[0]
    toe_trace = {
        key: one(pipeline.run_stage(
            rt.bin_dir, named(stop).snapshot_bin, pipeline.evaluation_input(toe)))
        for key, stop in clay_stops.items()}
    raw_clay = pipeline.run_stage(
        rt.bin_dir, named("EnglishProtoInput").snapshot_bin,
        pipeline.normalize_proto("θánxōn"))
    current = build_baseline(rt.corpus_tsv, rt.bin_dir / "old_english.bin")
    frozen = read_baseline(baseline_dir / "cascade_baseline_outputs.tsv",
                           baseline_dir / "cascade_baseline_summary.json")
    previous = {r["row_id"]: r for r in frozen["records"]}
    corpus_delta = [
        {"row_id": r["row_id"], "concept": r["concept"],
         "before": previous[r["row_id"]]["outputs"], "after": r["outputs"]}
        for r in current["records"] if r["outputs"] != previous[r["row_id"]]["outputs"]]
    assert current == frozen, (
        "accepted corpus no longer matches protected baseline", corpus_delta)
    assert not {r["concept"] for r in current["records"]} & {"clay", "fringe"}
after = {str(p): hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in protected}
assert before == after, "stage assays mutated canonical runtime or baselines"
print(json.dumps({
    "source_sha256": before[str(rt.germanic_fst)], "checkpoints": clay_stops,
    "clay_entry": {"before": entry, "input": clay_input},
    "clay": clay, "clay_trace": clay_trace,
    "pretonic": pretonic, "pretonic_trace": pretonic_trace,
    "reversed_clay": reversed_clay, "fringe": fringe,
    "toe": toe_trace, "raw_clay_tokenizer": raw_clay,
    "baseline": current["summary"], "corpus_delta": corpus_delta,
    "protected_artifacts_unchanged": before == after,
}, ensure_ascii=False))
'''


@pytest.fixture(scope="module")
def observed(isolated_definitions):
    with runtime_lock("External clay/fringe named-stage witnesses"):
        result = run_in_runner(
            isolated_definitions
            + 't=$(mktemp) && cat > "$t" && python3 "$t"; rc=$?; rm -f "$t"; exit $rc',
            input=SCRIPT, text=True, capture_output=True, timeout=1800)
    assert result.returncode == 0, result.stderr
    value = json.loads(result.stdout)
    print("\nGlossary stage observations: " + json.dumps(value, ensure_ascii=False))
    return value


def assert_hiatus(outputs):
    assert len(outputs) == 1 and re.fullmatch(r"\*θ\*ō\*[æeǣēiī]", outputs[0]), (
        "clay must have adjacent vowels and no fricative before contraction", outputs)


def assert_clay_surface(outputs):
    assert outputs == ["þō"], ("clay must contract to þō", outputs)


def assert_clay_contraction(outputs):
    assert outputs == ["*θ*ō"], ("clay must contract to starred θō", outputs)


def assert_fringe_hiatus(outputs):
    assert outputs == ["*w*l*ō*u*m"], (
        "fringe must lose x between back vowels and retain both u and m", outputs)


def test_clay_has_a_front_ending_with_h_then_hiatus_then_contraction(observed):
    clay = observed["clay"]
    assert re.fullmatch(r"\*θ\*ō\*[xç]\*[æeǣēiī]", clay["before_h_loss"][0])
    assert_hiatus(clay["before_contraction"])
    assert_clay_contraction(clay["after_contraction"])
    assert_clay_surface(clay["surface"])


def test_ordinary_toe_uses_existing_cumulative_snapshots(observed):
    toe = observed["toe"]
    assert toe["before_h_loss"] == ["*t*ā*ç*e"]
    assert toe["before_contraction"] == ["*t*ā*e"]
    assert toe["after_contraction"] == ["*t*ā"]
    assert toe["surface"] == ["tā"]


def test_pretonic_h_survives_prefix_reduction_and_h_loss_without_marker_leak(observed):
    pretonic = observed["pretonic"]
    assert pretonic["after_prefix_reduction"] == ["*ᶠ*b*e*x*í*n*d*a*n"]
    assert "*ᶠ" in pretonic["before_h_loss"][0]
    assert "*x" in pretonic["after_h_loss"][0]
    assert "*ᶠ" not in pretonic["after_h_loss"][0]
    assert pretonic["surface"] == ["behindan"]
    assert "ᶠ" not in pretonic["surface"][0]


def test_fringe_loses_h_between_back_vowels_without_losing_um(observed):
    assert_fringe_hiatus(observed["fringe"]["after_h_loss"])


def test_reversed_clay_order_fails_the_same_hiatus_and_surface_assertions(observed):
    trial = observed["reversed_clay"]
    assert trial["after_contraction"] == observed["clay"]["before_h_loss"]
    assert trial["after_loss"] == observed["clay"]["before_contraction"]
    with pytest.raises(AssertionError, match="adjacent vowels and no fricative"):
        assert_hiatus(trial["before_contraction"])
    with pytest.raises(AssertionError, match="contract to starred"):
        assert_clay_contraction(trial["after_contraction"])
    with pytest.raises(AssertionError, match="contract to þō"):
        assert_clay_surface(trial["surface"])


def test_front_only_loss_fails_fringe_but_deletes_before_fixed_front_e(observed):
    fringe = observed["fringe"]
    assert fringe["front_only"] == [fringe["input"]]
    assert fringe["front_only_positive"] == ["*t*ā*e"]
    with pytest.raises(AssertionError, match="lose x between back vowels"):
        assert_fringe_hiatus(fringe["front_only"])

#!/usr/bin/env python3
"""Complete-cascade world candidates and private representation diagnostics."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from cascade_baseline import legacy_subset
from sound_change_order_sensitivity import batch_apply_down


BASE = "6b2baf5f88af8a3c7702628bb3376c53c466e2a6"
RAISE = "OEInterStressRaising"
STRIP = "OEStripSecondaryStress"
SYNCOPE = "OECompoundLinkingSyncope"
DEFINITIONS = """
define WNoop ?*;
define WRound Ctx([
    [{*a}|{*à}] -> {*o} || PGmcStarVowel EnglishStarConsonant* _
        [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define WFurther Ctx([
    {*o} -> {*u} || PGmcStarVowel EnglishStarConsonant* _
        [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define WWide Ctx([
    [{*a}|{*à}] -> {*o} || PGmcStarVowel EnglishStarConsonant* _ {*l}
]);
"""
CANDIDATES = [
    f"*w{vowel}{ending}"
    for vowel in ("í", "é")
    for ending in ("r-àldu", "r-aldu", "r-àldō", "r-aldō",
                   "ra-àldō", "r-àldiz")
]
PARADIGM_CANDIDATES = {
    "i-stem-short-i-comparison": "*wír-aldi",
    "i-stem-long-i-dative-comparison": "*wír-aldī",
    "i-stem-genitive-comparison": "*wír-aldaiz",
    "o-stem-accusative-comparison": "*wír-aldǭ",
    "o-stem-genitive-trimoric-comparison": "*wír-aldôz",
    "o-stem-genitive-bimoric-comparison": "*wír-aldōz",
}
PROBES = {
    "literal-vowel-hiatus": "*w*é*r*a*à*l*d*u",
    "consonantal-linking-control": "*w*é*r*a*t*à*l*d*u",
    "plain-before-l-without-u": "*w*é*r*a*l*d*a",
    "grave-before-l-without-u": "*w*é*r*à*l*d*a",
    "primary-before-l": "*w*é*r*á*l*d*u",
    "right-j": "*w*é*r*a*j*l*d*u",
    "ordinary-positive": "*w*é*r*a*l*d*u",
    "following-i": "*w*é*r*a*l*d*i",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_apply(path, forms, label):
    outputs = batch_apply_down(path, forms)
    if len(outputs) != len(forms) or any(len(values) != 1 for values in outputs):
        raise RuntimeError(f"{label}: production rejection/ambiguity: {outputs}")
    return [values[0] for values in outputs]


def candidate_trace(bins, sequence, raw):
    state = oe_pipeline.evaluation_input(
        {"proto_norm": oe_pipeline.normalize_proto(raw)})
    trace = []
    for index, identifier in enumerate(sequence, 1):
        outputs = batch_apply_down(bins["component:" + identifier], [state])[0]
        if not outputs:
            return dict(input=raw, status="rejected", final=None, trace=trace,
                        rejection=dict(step=index, stage=identifier,
                                       input=state, outputs=outputs))
        if len(outputs) != 1:
            raise RuntimeError(f"candidate ambiguity: {identifier}: {raw}: {outputs}")
        new = outputs[0]
        if new != state:
            trace.append(dict(step=index, stage=identifier, pre=state, post=new))
        state = new
    return dict(input=raw, status="accepted", final=state,
                trace=trace, rejection=None)


def run():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("Run inside the backend after canonical SC036 --evidence")
    stages = oe_pipeline.stages()
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    order = [stage.inline_text if stage.kind == "inline" else stage.foma_identifier
             for stage in stages]
    baseline_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
    protected = [
        runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
        runtime.build_manifest,
        *(runtime.bin_dir / name for name in
          oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]),
        *(path for path in baseline_dir.iterdir() if path.is_file()),
    ]
    before = {str(path): digest(path) for path in protected}
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]

    def table(filename):
        with (baseline_dir / filename).open() as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    legacy = {row["row_id"] for row in legacy_subset(
        table("cascade_baseline_outputs.tsv"),
        table("cascade_baseline_outputs_legacy380.tsv"),
        table("approved_input_migrations.tsv"))}
    early_strip = [item for item in order if item != STRIP]
    early_strip.insert(1, STRIP)
    pre_raise_strip = [item for item in order if item != STRIP]
    pre_raise_strip.insert(pre_raise_strip.index(RAISE), STRIP)
    post_syncope_strip = [item for item in order if item not in {STRIP, RAISE}]
    anchor = post_syncope_strip.index(SYNCOPE) + 1
    post_syncope_strip[anchor:anchor] = [STRIP, RAISE]
    models = {
        "identity": order,
        "strip-after-input": early_strip,
        "strip-before-SC036": pre_raise_strip,
        "strip-after-SC037-before-raising": post_syncope_strip,
        "rounding-only-same-context": [
            "WRound" if item == RAISE else item for item in order],
        "factored-rounding-then-raising": [
            part for item in order
            for part in (["WRound", "WFurther"] if item == RAISE else [item])],
        "wide-before-l-diagnostic": [
            "WWide" if item == RAISE else item for item in order],
    }
    canonical = strict_apply(runtime.bin_dir / "old_english.bin", forms, "production")
    recipe = dict(definitions=DEFINITIONS, insert_after="", insert_rule="", replace={},
                  component_checks=[dict(component=item) for item in
                                    dict.fromkeys(order + [
                                        "WNoop", "WRound", "WFurther", "WWide"])])
    results = {}
    baseline_states = []
    with tempfile.TemporaryDirectory(prefix="capr_world2302_") as temporary:
        bins = compile_isolated(runtime.germanic_fst, recipe, [], Path(temporary))
        if strict_apply(bins["final"], forms, "isolated identity") != canonical:
            raise RuntimeError("Isolated full composition differs from production")
        for name, sequence in models.items():
            print("evaluating " + name, file=sys.stderr, flush=True)
            states = list(forms)
            focal = {row["row_id"]: [] for row in rows
                     if row["row_id"] in {"2302", "2148", "2252"}}
            intermediate = []
            firings = []
            for index, identifier in enumerate(sequence):
                previous = states
                states = strict_apply(bins["component:" + identifier], states,
                                      name + ":" + identifier)
                if name == "identity":
                    baseline_states.append(states)
                    stage = stages[index]
                    if stage.kind == "named" and states != strict_apply(
                            runtime.bin_dir / stage.snapshot_bin, forms, identifier):
                        raise RuntimeError("Canonical snapshot differs at " + identifier)
                    if identifier == RAISE:
                        firings = [
                            dict(row_id=row["row_id"], concept=row["concept"],
                                 input=forms[i], pre=previous[i], post=states[i],
                                 target=row["counterpart"],
                                 legacy380_identity=row["row_id"] in legacy)
                            for i, row in enumerate(rows) if previous[i] != states[i]]
                if len(sequence) == len(order) and name != "identity":
                    changes = [
                        dict(row_id=row["row_id"], concept=row["concept"],
                             existing=old, candidate=new)
                        for row, old, new in zip(rows, baseline_states[index], states)
                        if old != new]
                    if changes:
                        intermediate.append(dict(step=index + 1, stage=identifier,
                                                 rows=changes))
                for i, row in enumerate(rows):
                    if row["row_id"] in focal and previous[i] != states[i]:
                        focal[row["row_id"]].append(dict(
                            step=index + 1, stage=identifier,
                            pre=previous[i], post=states[i]))
            if name == "identity" and states != canonical:
                raise RuntimeError("Incremental identity differs from production")
            results[name] = dict(
                order=sequence, focal_traces=focal, firings=firings,
                intermediate_differences=intermediate,
                final_differences=[
                    dict(row_id=row["row_id"], concept=row["concept"], input=forms[i],
                         existing=old, candidate=new, target=row["counterpart"],
                         legacy380_identity=row["row_id"] in legacy)
                    for i, (row, old, new) in enumerate(zip(rows, canonical, states))
                    if old != new],
                full_cascade_candidates=[
                    candidate_trace(bins, sequence, raw) for raw in CANDIDATES],
                paradigm_comparisons={
                    label: candidate_trace(bins, sequence, raw)
                    for label, raw in PARADIGM_CANDIDATES.items()})
        components = {
            identifier: dict(zip(PROBES, strict_apply(
                bins["component:" + identifier], list(PROBES.values()), identifier)))
            for identifier in [RAISE, SYNCOPE, STRIP, "WRound", "WFurther", "WWide"]}
    if before != {str(path): digest(path) for path in protected}:
        raise RuntimeError("Private experiment altered protected files")
    return dict(
        base_commit=BASE, source_sha256=digest(runtime.germanic_fst),
        corpus_sha256=digest(runtime.corpus_tsv),
        build_manifest=json.loads(runtime.build_manifest.read_text()),
        selected_rows=len(rows), legacy380_identities=len(legacy),
        protected_files_unchanged=len(before),
        identity_composed_incremental_snapshots_agree=True,
        coordinates=[dict(identifier=stage.foma_identifier,
                          exec_index=stage.exec_index,
                          cascade_position=stage.cascade_position)
                     for stage in stages if stage.foma_identifier in {
                         RAISE, STRIP, SYNCOPE, "PNWGmcILowering",
                         "PNWGmcFinalLongORaising", "OEMedUnstressedULowering"}],
        component_inputs=PROBES, component_results=components, models=results)


REASSESSMENT_BASE = "61a0d67ef02a8da681ab21fba741b0ad63ea0a95"
REASSESSMENT_DEFINITIONS = """
define WLow [{*a}|{*à}|{*æ}];
define WLC [{*l} EnglishStarConsonant];
define WToU Ctx([
    WLow -> {*u} || PGmcStarVowel EnglishStarConsonant* _ WLC
]);
define WToO Ctx([
    WLow -> {*o} || PGmcStarVowel EnglishStarConsonant* _ WLC
]);
define WOToU Ctx([
    {*o} -> {*u} || PGmcStarVowel EnglishStarConsonant* _ WLC
]);
define WOUOnly Ctx([
    {*o} -> {*u} || PGmcStarVowel EnglishStarConsonant* _
        [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define WBackU Ctx([
    [{*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}]
    .o.
    [{*æ} -> {*ea} ||
        _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger]
    .o.
    [{*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}]
]);
"""
REASSESSMENT_PROBES = {
    **PROBES,
    "fronted-world-final": "*w*é*r*æ*l*d",
    "fronted-world-before-u": "*w*é*r*æ*l*d*u",
    "weak-l-without-cluster": "*w*é*r*æ*l*u",
    "primary-fronted-before-l": "*w*æ*l*d",
    "strong-accent-before-l": "*w*é*r*á*l*d",
    "weak-noncompound-shaped": "*s*é*t*æ*l*d",
    "twofold-shaped-weak": "*t*w*í*f*æ*l*d",
    "twofold-shaped-grave": "*t*w*í*f*à*l*d",
    "toward-shaped-weak": "*t*ō*w*æ*r*d",
    "back-mutation-with-o": "*w*é*r*o*l*d",
    "back-mutation-plain-e-o": "*w*e*r*o*l*d",
    "back-mutation-with-a": "*w*é*r*a*l*d",
    "back-mutation-with-u": "*w*é*r*u*l*d",
    "back-mutation-fronted-a-o": "*w*æ*r*o*l*d",
    "back-mutation-dental-control": "*w*é*t*o*l*d",
}


def reassessment_orders(order):
    def after(sequence, anchor, extra):
        result = list(sequence)
        result[result.index(anchor) + 1:result.index(anchor) + 1] = [extra]
        return result

    no_raise = ["WNoop" if item == RAISE else item for item in order]
    front = "EAFBrighteningUnstressed"
    back = "OEBackMutation"
    rounded = after(no_raise, front, "WToO")
    models = {
        "identity": list(order),
        "C-early-high": ["WToU" if item == RAISE else item for item in order],
        "C-postfront-high": after(no_raise, front, "WToU"),
        "C-supplement-high": after(order, front, "WToU"),
        "C-after-breaking": after(no_raise, "OEBreaking", "WToU"),
        "D-rounded-only": rounded,
        "D-rounded-then-high": after(rounded, "OEJClusterCoalescence", "WOToU"),
        "D-high-before-u-only": after(rounded, "OEJClusterCoalescence", "WOUOnly"),
    }
    early_oraising = [item for item in rounded if item != "OEMedUnstressedORaising"]
    models["D-existing-raising-earlier"] = after(
        early_oraising, "OEJClusterCoalescence", "OEMedUnstressedORaising")
    models["D-no-final-lowering"] = [
        "WNoop" if item == "OEFinalUnstressedOLowering" else item
        for item in rounded]
    for name, sequence in (
        ("back-u-only-control", order),
        ("D-rounded-u-only-back", rounded),
        ("D-high-u-only-back", models["D-rounded-then-high"]),
    ):
        models[name] = ["WBackU" if item == back else item for item in sequence]
    early_strip = [item for item in order if item != STRIP]
    models["F-global-strip-control"] = after(early_strip, "EnglishProtoInput", STRIP)
    return models


def run_reassessment():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("Run the isolated reassessment inside the backend")
    stages = oe_pipeline.stages()
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    order = [stage.inline_text if stage.kind == "inline" else stage.foma_identifier
             for stage in stages]
    models = reassessment_orders(order)
    directory = runtime.docs_dir / "sound_changes/cascade_baseline"
    protected = [
        runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
        runtime.build_manifest,
        runtime.data_dir / "entry_stage_metadata.tsv",
        runtime.data_dir / "entry_context_metadata.tsv",
        Path(__file__).with_name("evidence.json"),
        *(runtime.bin_dir / name for name in
          oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]),
        *(path for path in directory.iterdir() if path.is_file()),
    ]
    before = {str(path): digest(path) for path in protected}
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    canonical = strict_apply(runtime.bin_dir / "old_english.bin", forms, "production")

    def table(filename):
        with (directory / filename).open() as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    legacy = {row["row_id"] for row in legacy_subset(
        table("cascade_baseline_outputs.tsv"),
        table("cascade_baseline_outputs_legacy380.tsv"),
        table("approved_input_migrations.tsv"))}
    candidates = list(dict.fromkeys([
        *CANDIDATES, "*wír-aldiz", "*wér-aldiz",
        "*wír-aldi", "*wír-àldi", "*wír-aldį", "*wír-àldį",
    ]))
    components = list(dict.fromkeys([
        *(item for sequence in models.values() for item in sequence),
        "WOToU", "WOUOnly", "WToO", "WToU", "WBackU",
    ]))
    definitions = DEFINITIONS + REASSESSMENT_DEFINITIONS
    recipe = dict(
        definitions=definitions, insert_after="", insert_rule="", replace={},
        component_checks=[dict(component=item) for item in components])
    results, baseline_states = {}, {}

    def differences(old, new):
        return [
            dict(row_id=row["row_id"], concept=row["concept"],
                 existing=a, candidate=b, target=row["counterpart"],
                 legacy380_identity=row["row_id"] in legacy)
            for row, a, b in zip(rows, old, new) if a != b]

    with tempfile.TemporaryDirectory(prefix="capr_world2_") as temporary:
        bins = compile_isolated(
            runtime.germanic_fst, recipe, [], Path(temporary), components_only=True)
        for name, sequence in models.items():
            print("reassessment " + name, file=sys.stderr, flush=True)
            states = list(forms)
            changes, firings = [], []
            focal = {identifier: [] for identifier in ("2302", "2201", "2148")}
            for step, identifier in enumerate(sequence, 1):
                previous = states
                states = strict_apply(bins["component:" + identifier], states,
                                      name + ":" + identifier)
                if name == "identity":
                    baseline_states[identifier] = states
                    stage = stages[step - 1]
                    if stage.kind == "named" and states != strict_apply(
                            runtime.bin_dir / stage.snapshot_bin, forms, identifier):
                        raise RuntimeError("Canonical snapshot differs: " + identifier)
                    if identifier == RAISE:
                        firings = differences(previous, states)
                elif identifier in baseline_states:
                    deltas = differences(baseline_states[identifier], states)
                    if deltas:
                        changes.append(dict(step=step, stage=identifier, rows=deltas))
                for row, a, b in zip(rows, previous, states):
                    if row["row_id"] in focal and a != b:
                        focal[row["row_id"]].append(dict(
                            step=step, stage=identifier, pre=a, post=b))
            if name == "identity" and states != canonical:
                raise RuntimeError("Incremental identity differs from production")
            results[name] = dict(
                order=sequence, firings=firings, focal_traces=focal,
                intermediate_differences=changes,
                final_differences=differences(canonical, states),
                full_cascade_candidates=[
                    candidate_trace(bins, sequence, raw) for raw in candidates],
                paradigm_comparisons={
                    label: candidate_trace(bins, sequence, raw)
                    for label, raw in PARADIGM_CANDIDATES.items()})
        controls = {
            identifier: dict(zip(REASSESSMENT_PROBES, strict_apply(
                bins["component:" + identifier], list(REASSESSMENT_PROBES.values()),
                identifier)))
            for identifier in (
                RAISE, SYNCOPE, STRIP, "WToU", "WToO", "WOToU", "WOUOnly",
                "OEBackMutation", "WBackU", "OEMedUnstressedORaising",
                "OEFinalUnstressedOLowering")}
    if before != {str(path): digest(path) for path in protected}:
        raise RuntimeError("Reassessment altered protected sources, bins or receipts")
    return dict(
        base_commit=REASSESSMENT_BASE, source_sha256=digest(runtime.germanic_fst),
        corpus_sha256=digest(runtime.corpus_tsv),
        prior_receipt_sha256=digest(Path(__file__).with_name("evidence.json")),
        selected_rows=len(rows), legacy380_identities=len(legacy),
        protected_files_unchanged=len(before),
        identity_incremental_all_snapshots_agree=True,
        build_manifest=json.loads(runtime.build_manifest.read_text()),
        definitions=definitions, component_inputs=REASSESSMENT_PROBES,
        component_results=controls,
        coordinates=[dict(identifier=stage.foma_identifier,
                          exec_index=stage.exec_index,
                          cascade_position=stage.cascade_position)
                     for stage in stages],
        families={
            "A": dict(model="identity", input="*wír-àldu"),
            "B": dict(model="identity", inputs=["*wír-àldiz", "*wír-aldi"]),
            "C": dict(models=[name for name in models if name.startswith("C-")],
                      inputs=["*wír-àldiz", "*wír-aldi"]),
            "D": dict(models=[name for name in models if name.startswith("D-")],
                      inputs=["*wír-àldiz", "*wír-aldi", "*wír-àldō"]),
            "E": dict(models=[name for name in models if not name.startswith("F-")],
                      inputs=["*wír-àldō", "*wír-aldō"]),
            "F": dict(models=["identity", "F-global-strip-control"],
                      inputs=["*wír-àldu", "*wír-aldu"]),
        }, models=results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reassessment", action="store_true")
    args = parser.parse_args()
    print(json.dumps(run_reassessment() if args.reassessment else run(),
                     ensure_ascii=False, indent=2))

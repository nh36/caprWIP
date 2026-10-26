#!/usr/bin/env python3
"""Isolated SC036 clause, displacement and representation experiments."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from cascade_baseline import legacy_subset
from sound_change_order_sensitivity import batch_apply_down


RULE = "OEInterStressRaising"
EARLY = "EAFAiMonophthongization"
FINAL = "PNWGmcFinalLongORaising"
LATE = "OEMedUnstressedULowering"
SYNCOPE = "OECompoundLinkingSyncope"
STRIP = "OEStripSecondaryStress"
DEFINITIONS = """
define AFOriginal Ctx([
    {*a} -> {*u} || PGmcStarVowel EnglishStarConsonant* _
    [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
]);
define AFA Ctx([
    {*a} -> {*u} || PGmcStarVowel EnglishStarConsonant* _
    [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define AFB Ctx([{*à} -> {*u}]);
define AFAV Ctx([
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant* _
    [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define AFR Ctx([
    [{*a}|{*à}] -> {*u} || PGmcStarVowel EnglishStarConsonant* _
    [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define AFRV Ctx([
    [{*a}|{*à}] -> {*u} || EnglishStarVocalic EnglishStarConsonant* _
    [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}]
]);
define AFNoop ?*;
"""

# Starred strings are component-level representations, not new corpus data.
PROBES = {
    "soul-live": "*s*ā*w*a*l*u",
    "world-live": "*w*é*r*à*l*d*u",
    "plain-a-world": "*w*é*r*a*l*d*u",
    "grave-without-u": "*w*é*r*à*l*d*a",
    "grave-before-front-vowel": "*w*é*r*à*l*d*i",
    "grave-word-initial": "*à*l*d*u",
    "primary-a": "*w*é*r*á*l*d*u",
    "no-left-nucleus": "*w*a*l*d*u",
    "no-right-consonant": "*w*é*r*a*u",
    "long-target": "*w*é*r*ā*l*d*u",
    "long-following-u": "*w*é*r*a*l*d*ū",
    "j-immediately-before-u": "*l*ú*ŋ*g*a*n*j*u",
    "j-earlier-in-right-cluster": "*w*é*r*a*j*l*d*u",
    "j-in-left-cluster": "*w*é*j*a*l*d*u",
    "following-i": "*w*é*r*a*l*d*i",
    "following-o": "*w*é*r*a*l*d*o",
    "atomic-diphthong-left": "*s*ái*w*a*l*u",
    "linking-before-grave-a": "*w*é*r*a*t*à*l*d*u",
    "linking-before-grave-i": "*w*é*r*a*t*ì*l*d*u",
    "retained-secondary-no-u": "*á*n*f*à*l*d*a",
    "two-graves": "*w*é*r*à*t*à*l*d*u",
}

STAGED_ALTERNATIVES = {
    "world-after-root-lowering": "*w*é*r*à*l*d*u",
    "world-without-grave": "*w*é*r*a*l*d*u",
    "world-already-rounded": "*w*é*r*u*l*d*u",
    "world-unshifted-i-stem-comparison": "*w*é*r*a*l*d*i*z",
    "soul-after-nonhigh-syncope": "*s*ā*w*l*u",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def apply(path, forms, label):
    outputs = batch_apply_down(path, forms)
    failures = [(form, out) for form, out in zip(forms, outputs)
                if len(out) != 1 or out == ["+?"]]
    if len(outputs) != len(forms) or failures:
        raise RuntimeError(f"{label}: rejected/ambiguous outputs: {failures[:8]}")
    return [out[0] for out in outputs]


def displaced(order, rule, anchor, after=False):
    result = [stage for stage in order if stage != rule]
    result.insert(result.index(anchor) + int(after), rule)
    return result


def run():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("run inside the backend container after SC036 --evidence")
    stages = oe_pipeline.stages()
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    order = [s.inline_text if s.kind == "inline" else s.foma_identifier for s in stages]
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
        table("approved_input_migrations.tsv"),
    )}
    models = {
        "existing": order,
        "A-only": ["AFA" if item == RULE else item for item in order],
        "B-only": ["AFB" if item == RULE else item for item in order],
        "restricted-unified": ["AFR" if item == RULE else item for item in order],
        "restricted-vocalic": ["AFRV" if item == RULE else item for item in order],
        "skip": ["AFNoop" if item == RULE else item for item in order],
        "before-SC004": displaced(order, RULE, EARLY),
        "before-SC019": displaced(order, RULE, FINAL),
        "SC019-before-early-SC036": displaced(
            displaced(order, RULE, FINAL), FINAL, RULE),
        "SC004-before-early-SC036": displaced(
            displaced(order, RULE, FINAL), EARLY, RULE),
        "SC004-and-SC019-before-early-SC036": displaced(
            displaced(displaced(order, RULE, FINAL), EARLY, RULE), FINAL, RULE),
        "vocalic-before-SC004": [
            "AFRV" if item == RULE else item
            for item in displaced(order, RULE, EARLY)],
        "vocalic-before-SC019": [
            "AFRV" if item == RULE else item
            for item in displaced(order, RULE, FINAL)],
        "vocalic-SC019-before-early-SC036": [
            "AFRV" if item == RULE else item for item in displaced(
                displaced(order, RULE, FINAL), FINAL, RULE)],
        "after-SC040": displaced(order, RULE, LATE, after=True),
        "after-SC037": displaced(order, RULE, SYNCOPE, after=True),
        "after-SC038": displaced(order, RULE, STRIP, after=True),
    }
    extra = ["AFA", "AFB", "AFAV", "AFR", "AFRV", "AFOriginal", "AFNoop"]
    recipe = {
        "definitions": DEFINITIONS, "insert_after": "", "insert_rule": "",
        "replace": {}, "component_checks": [
            {"component": identifier} for identifier in order + extra],
    }
    canonical = apply(runtime.bin_dir / "old_english.bin", forms, "production")
    focal = {row["row_id"] for row in rows if row["concept"] in {"soul", "world", "lung"}}
    results = {}
    baseline_states = []
    with tempfile.TemporaryDirectory(prefix="capr_sc036_") as temporary:
        bins = compile_isolated(runtime.germanic_fst, recipe, [], Path(temporary))
        isolated = apply(bins["final"], forms, "isolated composition")
        if isolated != canonical:
            raise RuntimeError("isolated identity differs from production")
        equivalence = {}
        for candidate in (RULE, "AFR", "AFRV"):
            script = Path(temporary) / "equivalence.foma"
            script.write_text(
                f"load stack {bins['component:AFOriginal']}\n"
                f"load stack {bins['component:' + candidate]}\n"
                "test equivalent\nquit\n", encoding="utf-8")
            result = subprocess.run(
                ["foma", "-q", "-f", str(script)], capture_output=True,
                text=True, check=True, timeout=120)
            matches = re.findall(
                r"(?m)^\s*([01])\s*\(1 = TRUE, 0 = FALSE\)", result.stdout)
            if len(matches) != 1:
                raise RuntimeError("missing formal equivalence result: " + result.stdout)
            equivalence[candidate] = matches[0] == "1"
        if not equivalence[RULE] or not equivalence["AFR"] or equivalence["AFRV"]:
            raise RuntimeError("unexpected incumbent/shared-context equivalence")
        for model, sequence in models.items():
            print(f"evaluating {model}", file=sys.stderr, flush=True)
            states = list(forms)
            trace = {row_id: [] for row_id in focal}
            differences = []
            firings = []
            for index, identifier in enumerate(sequence):
                previous = states
                states = apply(bins["component:" + identifier], states,
                               f"{model}:{identifier}")
                if model == "existing":
                    baseline_states.append(states)
                    stage = stages[index]
                    if stage.kind == "named":
                        expected = apply(runtime.bin_dir / stage.snapshot_bin, forms,
                                         "canonical:" + identifier)
                        if states != expected:
                            raise RuntimeError("snapshot mismatch at " + identifier)
                    if identifier == RULE:
                        firings = [
                            {"row_id": row["row_id"], "concept": row["concept"],
                             "input": forms[i], "pre": previous[i], "post": states[i],
                             "target": row["counterpart"],
                             "legacy380_identity": row["row_id"] in legacy}
                            for i, row in enumerate(rows) if previous[i] != states[i]
                        ]
                elif sequence == order or model in {
                    "A-only", "B-only", "restricted-unified", "restricted-vocalic", "skip"
                }:
                    changed = [
                        {"row_id": row["row_id"], "concept": row["concept"],
                         "existing": old, "candidate": new}
                        for row, old, new in zip(rows, baseline_states[index], states)
                        if old != new]
                    if changed:
                        differences.append({"stage": identifier, "rows": changed})
                for i, row in enumerate(rows):
                    if row["row_id"] in focal and previous[i] != states[i]:
                        trace[row["row_id"]].append({
                            "stage": identifier, "pre": previous[i], "post": states[i]})
            if model == "existing" and states != canonical:
                raise RuntimeError("incremental identity differs from composition")
            results[model] = {
                "order": sequence, "focal_traces": trace,
                "intermediate_differences": differences,
                "final_differences": [
                    {"row_id": row["row_id"], "concept": row["concept"],
                     "input": forms[i], "target": row["counterpart"],
                     "existing": old, "candidate": new,
                     "legacy380_identity": row["row_id"] in legacy}
                    for i, (row, old, new) in enumerate(zip(rows, canonical, states))
                    if old != new],
            }
            if model == "existing":
                results[model]["firings"] = firings
        component_results = {}
        for identifier in [RULE, *extra[:-1], EARLY, FINAL, LATE, SYNCOPE, STRIP]:
            component_results[identifier] = dict(zip(
                PROBES, apply(bins["component:" + identifier],
                              list(PROBES.values()), identifier + ":probes")))
        staged_orders = {}
        for sequence in [
            [EARLY, FINAL, RULE], [EARLY, RULE, FINAL],
            [FINAL, RULE, EARLY], [FINAL, EARLY, RULE],
        ]:
            states = ["*s*ái*w*a*l*ō"]
            trace = []
            for identifier in sequence:
                states = apply(bins["component:" + identifier], states, identifier)
                trace.append({"stage": identifier, "post": states[0]})
            staged_orders[" / ".join(sequence)] = trace
        alternative_states = list(STAGED_ALTERNATIVES.values())
        alternative_traces = {name: [] for name in STAGED_ALTERNATIVES}
        alternative_rejections = {}
        for identifier in order[order.index(RULE):]:
            active = [(i, name, form) for i, (name, form) in enumerate(
                zip(STAGED_ALTERNATIVES, alternative_states))
                if name not in alternative_rejections]
            outputs = batch_apply_down(
                bins["component:" + identifier], [form for _, _, form in active])
            if len(outputs) != len(active):
                raise RuntimeError("alternative output count mismatch at " + identifier)
            for (i, name, old), values in zip(active, outputs):
                if not values or values == ["+?"]:
                    alternative_rejections[name] = {
                        "stage": identifier, "input": old, "outputs": values}
                    alternative_states[i] = None
                    continue
                if len(values) != 1:
                    raise RuntimeError(
                        f"alternative:{identifier}: ambiguous {old}: {values}")
                new = values[0]
                alternative_states[i] = new
                if old != new:
                    alternative_traces[name].append(
                        {"stage": identifier, "pre": old, "post": new})
        interactions = {}
        for first, second in [(RULE, SYNCOPE), (RULE, STRIP), (RULE, LATE),
                              ("AFRV", SYNCOPE), ("AFRV", STRIP)]:
            inputs = list(PROBES.values())
            forward = apply(bins["component:" + second], apply(
                bins["component:" + first], inputs, first), second)
            reverse = apply(bins["component:" + first], apply(
                bins["component:" + second], inputs, second), first)
            interactions[first + ":" + second] = {
                name: {"input": form, "forward": fwd, "reverse": rev}
                for name, form, fwd, rev in zip(PROBES, inputs, forward, reverse)
                if fwd != rev}
    after = {str(path): digest(path) for path in protected}
    if before != after:
        raise RuntimeError("experiment altered protected production/evidence files")
    return {
        "base_commit": "a36dbcfc2ec8fc4f28bf366a643473227cebb510",
        "source_sha256": digest(runtime.germanic_fst),
        "corpus_sha256": digest(runtime.corpus_tsv),
        "build_manifest": json.loads(runtime.build_manifest.read_text()),
        "selected_rows": len(rows), "legacy380_identities": len(legacy),
        "coordinates": [
            {"identifier": s.foma_identifier, "exec_index": s.exec_index,
             "cascade_position": s.cascade_position}
            for s in stages if s.foma_identifier in {RULE, EARLY, FINAL, LATE, SYNCOPE, STRIP}],
        "canonical_composed_incremental_agree": True,
        "protected_files_unchanged": len(before),
        "models": results, "probe_inputs": PROBES,
        "component_results": component_results, "interactions": interactions,
        "formal_equivalence_to_original": equivalence,
        "controlled_three_component_orders": staged_orders,
        "grave_annotated_selected_inputs": [
            {"row_id": row["row_id"], "concept": row["concept"], "input": form}
            for row, form in zip(rows, forms) if any(c in form for c in "àèìòù")],
        "staged_alternatives": {
            name: {"input": form, "final": final, "trace": alternative_traces[name],
                   "status": "rejected" if name in alternative_rejections else "accepted",
                   "rejection": alternative_rejections.get(name)}
            for name, form, final in zip(
                STAGED_ALTERNATIVES, STAGED_ALTERNATIVES.values(), alternative_states)},
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

#!/usr/bin/env python3
"""Bounded SC035 model comparison using the existing isolated Foma compiler."""
from __future__ import annotations

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


BASE = "5533f7653f87d3962a92935a280190882c16b61b"
FLAG = "*ᵖ"
PREFIX = "OEPrefixAReduction"
FOCAL = {"begin", "believe", "bind", "gall", "guest", "give", "sheep"}
ROOT_DOMAIN = {
    "OEBreaking", "OEARestoration", "OEIUmlaut", "OEMedialSyncope",
    "OEUnstressedFrontingEarly", "OEUnstressedLongVowelShortening",
    "OEMedUnstressedILowering1", "OEMedUnstressedULowering",
}
CONTROLS = {
    "climb": {
        "input": "*g*a*s*t*ḯ*g*a*n",
        "status": "source-backed staged reconstruction; Ringe-Taylor p.335; CAPR root-stress notation",
        "comparison": "early Northumbrian gistīga; late gestīga; WS gestīgan",
    },
    "climb-stress-erased": {
        "input": "*g*a*s*t*ī*g*a*n",
        "status": "representation control: source-backed segmental shape without CAPR root accent",
        "comparison": "tests the effect of omitting the independently available stressed-long-i tier",
    },
    "accented-ga": {
        "input": "*g*á*t*w*a",
        "status": "source-backed staged stress contrast; Ringe-Taylor pp.216,335",
        "comparison": "stressed prefix in ġeatwa; not a new selected input",
    },
    "boundary-free-gaCV": {
        "input": "*g*a*t*á",
        "status": "artificial structural control; no attestation claimed",
        "comparison": "no boundary encoded; tests root stress after weak vowel",
    },
    "weak-before-lC": {
        "input": "*g*a*l*t*á",
        "status": "artificial structural control; no attestation claimed",
        "comparison": "tests protection from breaking before a consonant cluster",
    },
    "ni-template": {
        "input": "*n*i*t*á",
        "status": "artificial CV template, not an attested ni-prefixed word",
        "comparison": "late restricted i-prefix component; independent ni > ne evidence",
    },
}


def orders():
    return [
        stage.inline_text if stage.kind == "inline" else stage.foma_identifier
        for stage in oe_pipeline.stages()
    ]


def recipe(model):
    if model == "A":
        return {
            "definitions": "", "insert_after": "", "insert_rule": "", "replace": {},
            "component_checks": [
                {"component": "OEWsPalatalDiphthongization"},
                {"component": "OEUnstressedAEMerger"},
            ],
        }
    definitions = [
        "define AFNoop ?*;",
        # Same context-lifting pattern as canonical Ctx(T), but the flag
        # identifies a weak first syllable, not a weak sentence-level word.
        "define AFW(T) [ [{*ᵖ}|0] [EnglishStarAlphabet* .o. T] ];",
        "define AFR(T) [ "
        "{*ᵖ} OEAnyConsonant* EnglishStarVocalic [EnglishStarAlphabet* .o. T] "
        "| [EnglishStarAlphabet* .o. T] ];",
        "define AFMark [ {*g} -> {*ᵖ} {*g} || .#. _ {*a} "
        "OEAnyConsonant+ EnglishStarVocalic ];",
        "define AFMerge [ "
        "[{*æ} -> {*e} || .#. {*ᵖ} OEAnyConsonant* _] .o. "
        "[{*i} -> {*e} || .#. {*ᵖ} OEAnyConsonant* _] .o. "
        "AFR(OEUnstressedAEMerger) ];",
        "define AFDrop AFW(OEPrefixIReduction) .o. [{*ᵖ} -> 0];",
    ]
    original = orders()
    start, stop = original.index(PREFIX), original.index("OEPrefixIReduction")
    replacements = {PREFIX: "AFMark", "OEPrefixIReduction": "AFDrop"}
    for index in range(start + 1, stop):
        stage = original[index]
        name = f"AFW{index:03d}"
        body = f"AFR({stage})" if stage in ROOT_DOMAIN else f"AFW({stage})"
        if stage == "OEUnstressedAEMerger":
            body = "AFMerge"
        elif stage == "OEWsPalatalDiphthongization" and model == "B":
            body = "[ {*ᵖ} EnglishStarAlphabet* | OEWsPalatalDiphthongization ]"
        elif stage == "OEVelarPalatalization" and model == "C":
            body += (
                " .o. [{*æ} -> {*i} || .#. {*ᵖ} {*ʝ} _ "
                "[OEAnyConsonant | .#.]]"
            )
        definitions.append(f"define {name} {body};")
        replacements[stage] = name
    return {
        "definitions": "\n".join(definitions),
        "insert_after": PREFIX, "insert_rule": "AFNoop",
        "replace": replacements, "component_checks": [{"component": "AFMerge"}],
    }


def checked_apply(path, forms, label):
    outputs = batch_apply_down(path, forms)
    if len(outputs) != len(forms) or any(
        len(output) != 1 or output == ["+?"] for output in outputs
    ):
        failures = [(form, output) for form, output in zip(forms, outputs)
                    if len(output) != 1 or output == ["+?"]]
        raise RuntimeError(
            f"{label}: missing, rejected or ambiguous output: {failures[:8]}")
    return outputs


def run():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("run in the backend container, after SC035 --evidence")
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    baseline_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
    protected = [
        runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
        runtime.build_manifest, runtime.data_dir / "entry_context_metadata.tsv",
        *(runtime.bin_dir / name for name in
          oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]),
        *(path for path in baseline_dir.iterdir() if path.is_file()),
        Path(__file__).parent.parent / "sc035-adjudication.md",
        Path(__file__).parent.parent / "sc035-prefix-reduction/evidence.json",
    ]

    def hashes():
        return {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in protected}

    protected_before = hashes()
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]

    def table(name):
        with (baseline_dir / name).open() as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    legacy = {row["row_id"] for row in legacy_subset(
        table("cascade_baseline_outputs.tsv"),
        table("cascade_baseline_outputs_legacy380.tsv"),
        table("approved_input_migrations.tsv"),
    )}
    production = checked_apply(runtime.bin_dir / "old_english.bin", forms, "production")
    stages = oe_pipeline.stages()
    original_order = orders()
    entry = original_order.index(PREFIX)
    baseline_states = []
    results = {}
    for model in ("A", "B", "C"):
        candidate = recipe(model)
        diagnostics = [candidate["replace"].get(stage, stage) for stage in original_order]
        with tempfile.TemporaryDirectory(prefix="capr_sc035_models_") as temporary:
            bins = compile_isolated(
                runtime.germanic_fst, candidate, [], Path(temporary),
                diagnostic_stages=diagnostics)
            final = batch_apply_down(bins["final"], forms)
            states = [[form] for form in forms]
            control_states = {name: [control["input"]] for name, control in CONTROLS.items()}
            trace = {row["row_id"]: [] for row in rows if row["concept"] in FOCAL}
            control_traces = {name: [] for name in CONTROLS}
            changes = []
            for index, stage in enumerate(stages):
                identifier = original_order[index]
                component = bins[f"diagnostic:{index}"]
                before = states
                states = checked_apply(
                    component, [output[0] for output in states], f"{model}:{identifier}")
                if model == "A":
                    baseline_states.append(states)
                    canonical = checked_apply(
                        runtime.bin_dir / stage.snapshot_bin, forms,
                        f"A:canonical:{identifier}")
                    if states != canonical:
                        raise RuntimeError(f"identity disagrees at {identifier}")
                else:
                    different = [
                        {"row_id": row["row_id"], "concept": row["concept"],
                         "legacy380_identity": row["row_id"] in legacy,
                         "A": old, model: new,
                         "segmental_difference": old !=
                         [form.replace(FLAG, "") for form in new]}
                        for row, old, new in zip(rows, baseline_states[index], states)
                        if old != new
                    ]
                    if different:
                        changes.append({"stage": identifier, "rows": different})
                for position, row in enumerate(rows):
                    if row["row_id"] in trace:
                        trace[row["row_id"]].append({
                            "stage": identifier, "before": before[position],
                            "after": states[position],
                        })
                if index >= entry:
                    for name, old in control_states.items():
                        new = checked_apply(
                            component, old, f"{model}:control:{name}:{identifier}")[0]
                        if old != new or identifier in {
                            PREFIX, "EAFBrighteningUnstressed", "EAFBrightening",
                            "OEBreaking", "OEVelarPalatalization",
                            "OEWsPalatalDiphthongization", "OEIUmlaut",
                            "OEUnstressedLongVowelShortening",
                            "OEUnstressedAEMerger", "OEPrefixIReduction",
                        }:
                            control_traces[name].append({
                                "stage": identifier, "before": old, "after": new})
                        control_states[name] = new
            if states != final:
                raise RuntimeError(f"{model}: incremental and composed cascades disagree")
            if model == "A" and final != production:
                raise RuntimeError("isolated identity disagrees with accepted production")
            results[model] = {
                "recipe": candidate, "all_intermediate_differences": changes,
                "final_differences": [
                    {"row_id": row["row_id"], "concept": row["concept"],
                     "input": forms[index], "legacy380_identity": row["row_id"] in legacy,
                     "A": old, model: new}
                    for index, (row, old, new) in enumerate(zip(rows, production, final))
                    if old != new
                ],
                "focal_traces": trace, "staged_control_traces": control_traces,
                "staged_control_finals": control_states,
                "full_input_climb": checked_apply(
                    bins["final"], ["gastḯganą"], f"{model}:source-backed full climb"),
                "early_gi_merger": checked_apply(
                    bins["component:OEUnstressedAEMerger" if model == "A"
                         else "component:AFMerge"],
                    [("" if model == "A" else FLAG) + "*ʝ*i*s*t*ḯ*g*a"],
                    f"{model}:attested early weak-gi merger")[0],
            }
            if model == "A":
                pd = bins["component:OEWsPalatalDiphthongization"]
                samples = ["*ʝ*æ*l*l*a", "*ʝ*æ*s*t*i", "*ʝ*é*β*a*n", "*ʃ*ḗ*p"]
                results[model]["palatal_component"] = {
                    "inputs": samples, "outputs": checked_apply(pd, samples, "PD controls")}
    if hashes() != protected_before:
        raise RuntimeError("model comparison modified protected artifacts")
    return {
        "accepted_base_commit": BASE,
        "source_sha256": hashlib.sha256(runtime.germanic_fst.read_bytes()).hexdigest(),
        "selected_rows": len(rows), "legacy380_identity_rows": len(legacy),
        "stages_compared": len(stages), "controls": CONTROLS,
        "models": results, "canonical_artifacts_unchanged": True,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

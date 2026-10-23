#!/usr/bin/env python3
"""Compare positively stress-anchored SC035 models in isolated Foma builds."""
from __future__ import annotations

import hashlib
import csv
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from cascade_baseline import legacy_subset


BASE = "310665a3f62ba850a946edaa27676d73d8022f6c"
SOURCE_SHA256 = "91373171ba23d32464e78944ccf379932dd5d8c00df1ce7fb40dcaa39f22b209"
FLAG = "*ᶠ"
historical_path = Path(__file__).parent.parent / "sc035-model-comparison/experiment.py"
spec = importlib.util.spec_from_file_location("sc035_historical_comparison", historical_path)
historical = importlib.util.module_from_spec(spec)
spec.loader.exec_module(historical)
CONTROLS = {
    **historical.CONTROLS,
    "shaft": {
        "input": "*s*k*á*f*t",
        "status": "source-backed root-stressed stem comparison; Hogg Grammar 5.48 n.1",
        "comparison": "sceaft; no unattested full citation cell or ending supplied",
    },
    "prefixed-shaft": {
        "input": "*g*a*s*k*á*f*t",
        "status": "source-backed weak-plus-stressed stem comparison; Hogg Grammar 5.48 n.1",
        "comparison": "gesceaft; diphthongization in the headed root, not the weak syllable",
    },
    "nongrammatical-weak-front": {
        "input": "*g*e*t*á",
        "status": "artificial phonological generality control, not an attested word",
        "comparison": "no morpheme identity supplied; raising is restricted to fronted ae",
    },
    "nongrammatical-weak-back": {
        "input": "*b*a*t*á",
        "status": "artificial phonological generality control, not an attested word",
        "comparison": "ordinary fronting without the preceding palatal-fricative trigger",
    },
}


def recipe(model, order):
    if model == "A":
        return historical.recipe("A")
    if model not in {"B", "C"}:
        raise ValueError(f"unknown model {model}")
    definitions = [
        "define AFNoop ?*;",
        "define AFSkip ?*;",
        "define AFSeg [EnglishStarAlphabet|{*áeu}];",
        "define AFWeak [{*a}|{*e}|{*i}|{*o}|{*u}|{*æ}];",
        "define AFStress [PGmcStarAcuteVowel|{*ái}|{*áu}|{*éu}|{*íu}];",
        "define AFInput [OEAnyConsonant* AFWeak OEAnyConsonant+ "
        "AFStress EnglishStarAlphabet*];",
        # Disjoint branches insert exactly one flag, without epsilon rewriting.
        "define AFMark [[0:{*ᶠ} AFInput] | [EnglishStarAlphabet* - AFInput]];",
        "define AFW(T) [[{*ᶠ}|0] [AFSeg* .o. T]];",
        "define AFR(T) [{*ᶠ} OEAnyConsonant* EnglishStarVocalic "
        "[AFSeg* .o. T] | [AFSeg* .o. T]];",
        "define AFRaise [{*æ} -> {*i} || .#. {*ᶠ} "
        "OEAnyConsonant* {*ʝ} _];",
        "define AFPD AFR(OEWsPalatalDiphthongization);",
        "define AFMerge [[{*æ} -> {*e} || .#. {*ᶠ} "
        "OEAnyConsonant* _] .o. AFR(OEUnstressedAEMerger)];",
        "define AFDrop [[{*i} -> {*e} || .#. {*ᶠ} "
        "OEAnyConsonant* _] .o. [{*ᶠ} -> 0]];",
        "define AFEntry [EAFLongAFronting .o. AFMark];",
    ]
    start, stop = order.index("EAFLongAFronting"), order.index("OEPrefixIReduction")
    replacements = {
        "EAFLongAFronting": "AFEntry",
        "OEPrefixAReduction": "AFSkip",
        "OEPrefixIReduction": "AFDrop",
    }
    for index in range(start + 1, stop):
        stage = order[index]
        if stage == "OEPrefixAReduction":
            continue
        name = f"AFW{index:03d}"
        body = f"AFR({stage})" if stage in historical.ROOT_DOMAIN else f"AFW({stage})"
        if stage == "OEWsPalatalDiphthongization":
            body = "AFPD"
        elif stage == "OEUnstressedAEMerger":
            body = "AFMerge"
        elif stage == "OEVelarPalatalization" and model == "C":
            body += " .o. AFRaise"
        definitions.append(f"define {name} [{body}];")
        replacements[stage] = name
    return {
        "definitions": "\n".join(definitions),
        "insert_after": "EAFLongAFronting", "insert_rule": "AFNoop",
        "replace": replacements,
        "component_checks": [{"component": name} for name in
                             ("AFMark", "AFRaise", "AFPD", "AFMerge", "AFDrop")],
    }


def run():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("run inside the backend container after SC035 --evidence")
    source_hash = hashlib.sha256(runtime.germanic_fst.read_bytes()).hexdigest()
    if source_hash != SOURCE_SHA256:
        raise RuntimeError("comparison requires the accepted source at " + BASE)
    bin_names = oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]
    errors = check_build_manifest(bin_names, runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    baseline_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
    protected = [
        runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
        runtime.build_manifest, runtime.data_dir / "entry_context_metadata.tsv",
        *(runtime.bin_dir / name for name in bin_names),
        *(path for path in baseline_dir.iterdir() if path.is_file()),
        historical_path, historical_path.with_name("evidence.json"),
        historical_path.parent.parent / "sc035-prefix-reduction/evidence.json",
    ]

    def hashes():
        return {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in protected}

    before_hashes = hashes()
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    def table(name):
        with (baseline_dir / name).open() as handle:
            return list(csv.DictReader(handle, delimiter="\t"))
    legacy = {row["row_id"] for row in legacy_subset(
        table("cascade_baseline_outputs.tsv"),
        table("cascade_baseline_outputs_legacy380.tsv"),
        table("approved_input_migrations.tsv"),
    )}
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    stages = oe_pipeline.stages()
    order = historical.orders()
    entry = order.index("EAFLongAFronting")
    production = historical.checked_apply(runtime.bin_dir / "old_english.bin", forms, "production")
    baseline_states, results = [], {}
    for model in ("A", "B", "C"):
        candidate = recipe(model, order)
        diagnostics = [candidate["replace"].get(stage, stage) for stage in order]
        with tempfile.TemporaryDirectory(prefix="capr_sc035_prosody_") as temporary:
            bins = compile_isolated(runtime.germanic_fst, candidate, [], Path(temporary),
                                    diagnostic_stages=diagnostics)
            final = historical.checked_apply(bins["final"], forms, model + ":composed")
            states = [[form] for form in forms]
            trace = {row["row_id"]: [] for row in rows if row["concept"] in historical.FOCAL}
            controls = {name: [control["input"]] for name, control in CONTROLS.items()}
            control_traces = {name: [] for name in CONTROLS}
            changes = []
            for index, stage in enumerate(stages):
                identifier = order[index]
                component = bins[f"diagnostic:{index}"]
                previous = states
                states = historical.checked_apply(
                    component, [output[0] for output in states], model + ":" + identifier)
                if model == "A":
                    baseline_states.append(states)
                    canonical = historical.checked_apply(
                        runtime.bin_dir / stage.snapshot_bin, forms, "canonical:" + identifier)
                    if states != canonical:
                        raise RuntimeError("identity disagrees at " + identifier)
                else:
                    different = [
                        {"row_id": row["row_id"], "concept": row["concept"],
                         "legacy380_identity": row["row_id"] in legacy,
                         "A": old, model: new,
                         "segmental_difference": old != [form.replace(FLAG, "") for form in new]}
                        for row, old, new in zip(rows, baseline_states[index], states)
                        if old != new
                    ]
                    if different:
                        changes.append({"stage": identifier, "rows": different})
                for position, row in enumerate(rows):
                    if row["row_id"] in trace:
                        trace[row["row_id"]].append({
                            "stage": identifier, "before": previous[position],
                            "after": states[position],
                        })
                if index >= entry:
                    for name, old in controls.items():
                        new = historical.checked_apply(
                            component, old, model + ":" + name + ":" + identifier)[0]
                        control_traces[name].append({
                            "stage": identifier, "before": old, "after": new})
                        controls[name] = new
            if states != final:
                raise RuntimeError(model + ": incremental and composed cascades disagree")
            if model == "A" and final != production:
                raise RuntimeError("identity disagrees with accepted production")
            results[model] = {
                "recipe": candidate, "all_intermediate_differences": changes,
                "final_differences": [
                    {"row_id": row["row_id"], "concept": row["concept"],
                     "legacy380_identity": row["row_id"] in legacy,
                     "input": forms[position], "A": old, model: new}
                    for position, (row, old, new) in enumerate(zip(rows, production, final))
                    if old != new
                ],
                "focal_traces": trace, "staged_control_traces": control_traces,
                "staged_control_finals": controls,
                "full_input_climb": historical.checked_apply(
                    bins["final"], ["gastḯganą"], model + ":full climb"),
            }
            if model != "A":
                samples = [
                    "*ʝ*i*s*t*ḯ*g*a", "*b*i*g*í*n*n*a*n",
                    "*ʝ*i*d*y*r*s*t*i*ʝ", "*ʝ*i*b*ēa*t*æ*n",
                ]
                results[model]["early_i_merger"] = historical.checked_apply(
                    bins["component:AFDrop"], [FLAG + form for form in samples], "early i merger")
                samples = [
                    "*g*a*l*áu*b*i*j*a*n", "*b*i*g*í*n*n*a*n", "*g*a*s*t*ḯ*g*a*n",
                    "*g*á*t*w*a", "*g*a*t*ā", "*b*a*t*á", "*ʝ*æ*t*á",
                ]
                results[model]["positive_stress_annotation"] = {
                    "inputs": samples,
                    "outputs": historical.checked_apply(bins["component:AFMark"], samples, "stress annotation"),
                }
    if hashes() != before_hashes:
        raise RuntimeError("comparison modified protected artifacts")
    return {
        "accepted_base_commit": BASE, "source_sha256": source_hash,
        "selected_rows": len(rows),
        "legacy380_identity_rows": len(legacy),
        "legacy_identity_method": "fresh legacy_subset census with approved input migrations",
        "stages_compared": len(stages), "controls": CONTROLS,
        "models": results, "canonical_artifacts_unchanged": True,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

#!/usr/bin/env python3
"""Fresh complete-cascade and component verification of the adopted model."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from experiment import historical, CONTROLS


def run():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("run in the backend container after supported finalization")
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    stages = oe_pipeline.stages()
    order = [s.inline_text if s.kind == "inline" else s.foma_identifier for s in stages]
    components = {
        "annotation": ("OEStressFootContext", [
            "*g*a*l*áu*b*i*j*a*n", "*g*a*s*t*ḯ*g*a*n",
            "*b*a*t*á", "*g*á*t*w*a", "*g*a*t*ī",
        ]),
        "raising": ("OEPrefixAReduction", [
            "*ᶠ*ʝ*æ*t*á", "*ᶠ*b*æ*t*á", "*ᶠ*ʝ*e*t*á",
            "*ʝ*æ*t", "*ᶠ*ʝ*æ*ʃ*æ*f*t",
        ]),
        "diphthongization": ("OEWsPalatalDiphthongization", [
            "*ᶠ*ʝ*æ*ʃ*æ*f*t", "*ʃ*æ*f*t", "*ʝ*æ*s*t*i",
            "*ʝ*é*β*a*n", "*ʃ*ḗ*p", "*ʝ*ea*l*l*a",
        ]),
        "ae_merger": ("OEUnstressedAEMerger", [
            "*ᶠ*b*æ*t*á", "*b*æ*t", "*ᶠ*ʝ*i*s*t*ḯ*g*a",
        ]),
        "i_lowering": ("OEPrefixIReduction", [
            "*ᶠ*ʝ*i*s*t*ḯ*g*a", "*ᶠ*b*i*g*í*n*n*a*n",
            "*ᶠ*n*i*t*á", "*b*í*n*d*a*n", "*n*i",
        ]),
    }
    recipe = {
        "definitions": "", "insert_after": "", "insert_rule": "", "replace": {},
        "component_checks": [{"component": identifier}
                             for identifier, _ in components.values()],
    }
    focal = {row["row_id"]: [] for row in rows if row["concept"] in historical.FOCAL}
    with tempfile.TemporaryDirectory(prefix="capr_sc035_adopted_") as temporary:
        bins = compile_isolated(runtime.germanic_fst, recipe, [], Path(temporary),
                                diagnostic_stages=order)
        final = historical.checked_apply(bins["final"], forms, "composed production")
        canonical = historical.checked_apply(
            runtime.bin_dir / "old_english.bin", forms, "canonical production")
        if final != canonical:
            raise RuntimeError("isolated adopted cascade differs from canonical production")
        states = [[form] for form in forms]
        controls = {name: [control["input"]] for name, control in CONTROLS.items()}
        entry = order.index("OEStressFootContext")
        for index, stage in enumerate(stages):
            before = states
            states = historical.checked_apply(
                bins[f"diagnostic:{index}"], [output[0] for output in states], order[index])
            if stage.kind == "named":
                expected = historical.checked_apply(
                    runtime.bin_dir / stage.snapshot_bin, forms, order[index] + ":snapshot")
                if states != expected:
                    raise RuntimeError("adopted incremental trace differs at " + order[index])
            for position, row in enumerate(rows):
                if row["row_id"] in focal:
                    focal[row["row_id"]].append({
                        "stage": order[index], "before": before[position],
                        "after": states[position],
                    })
            if index >= entry:
                for name, previous in controls.items():
                    controls[name] = historical.checked_apply(
                        bins[f"diagnostic:{index}"], previous, order[index] + ":" + name)[0]
        if states != final:
            raise RuntimeError("adopted incremental and composed cascades differ")
        checks = {
            name: {"inputs": inputs, "outputs": historical.checked_apply(
                bins["component:" + identifier], inputs, name)}
            for name, (identifier, inputs) in components.items()
        }
        climb = historical.checked_apply(bins["final"], ["gastḯganą"], "full climb")
    return {
        "source_sha256": hashlib.sha256(runtime.germanic_fst.read_bytes()).hexdigest(),
        "selected_rows": len(rows), "stages_compared": len(stages),
        "composed_and_incremental_agree": True,
        "canonical_and_isolated_agree": True,
        "full_input_climb": climb, "controls": checks,
        "staged_control_finals": controls, "focal_traces": focal,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

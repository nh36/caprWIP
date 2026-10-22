#!/usr/bin/env python3
"""SC035 component/domain and full-corpus displacement assay, container only.

Run after SC035 --evidence:
docker compose exec -T backend python3 \
  docs/sound_changes/audits/sc035-prefix-reduction/experiment.py

Uses the existing isolated experiment compiler; never writes canonical bins,
sources, baselines or receipts. JSON on stdout is a current execution, not a
replacement for the historical chronology card.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from cascade_baseline import legacy_subset
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from sound_change_order_sensitivity import batch_apply_down


RULE = "OEPrefixAReduction"
CHECKPOINTS = (
    RULE, "EAFBrighteningUnstressed", "EAFBrightening", "OEBreaking",
    "OEWsPalatalDiphthongization",
)
COMPONENT_INPUTS = {
    "believe-prefix": "*g*a*l*ēa*b*i*j*a*n*ą",
    "gall-stressed-root": "*g*á*l*l*ā",
    "guest-stressed-cluster": "*g*á*s*t*i",
    # Ringe–Taylor p.335: a real prefix with a cluster; staged diagnostic,
    # not an admitted full-cascade reconstruction or an attested intermediate.
    "climb-prefix-cluster": "*g*a*s*t*ī*g*a*n",
    "stressed-ga-structural-control": "*g*á*l*ēa*b*i*j*a*n*ą",
    "grave-ga-structural-control": "*g*à*l*ēa*b*i*j*a*n*ą",
    "noninitial-ga-structural-control": "*a*g*a*l*á",
    "prevocalic-ga-structural-control": "*g*a*á",
    "unsegmented-gaCV-structural-control": "*g*a*t*á",
}


def recipe(after: str | None) -> dict:
    if after is None:
        return {"definitions": "", "insert_after": "", "insert_rule": "", "replace": {},
                "component_checks": [{"component": RULE}]}
    return {
        "definitions": (
            "define AFNoA [ ?* ];\n"
            f"define AFPreA [ {'?*' if after == 'skip' else RULE} ];"
        ),
        "insert_after": RULE if after == "skip" else after,
        "insert_rule": "AFPreA",
        "replace": {RULE: "AFNoA"},
        "component_checks": [],
    }


def run() -> dict:
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("SC035 assay must run in the backend container")
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("run SC035 --evidence first: " + "; ".join(errors))
    baseline_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
    protected = [
        runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
        runtime.build_manifest, runtime.data_dir / "entry_context_metadata.tsv",
        runtime.bin_dir / "old_english.bin",
        *(runtime.bin_dir / name for name in oe_pipeline.expected_snapshot_bins()),
        *baseline_dir.glob("cascade_baseline_*"),
    ]
    hashes = lambda: {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in protected if p.is_file()}
    before_hashes = hashes()
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    baseline = batch_apply_down(runtime.bin_dir / "old_english.bin", forms)
    if any(len(output) != 1 or output == ["+?"] for output in baseline):
        raise RuntimeError("missing or ambiguous live production output")
    def table(name):
        with (baseline_dir / name).open() as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    legacy = {row["row_id"] for row in legacy_subset(
        table("cascade_baseline_outputs.tsv"),
        table("cascade_baseline_outputs_legacy380.tsv"),
        table("approved_input_migrations.tsv"),
    )}

    previous = oe_pipeline.previous_stage(RULE)
    pre = batch_apply_down(runtime.bin_dir / previous.snapshot_bin, forms)
    post = batch_apply_down(
        runtime.bin_dir / oe_pipeline.stage_for(RULE).snapshot_bin, forms)
    census = [
        {**row, "before": a, "after": b, "final": final,
         "legacy380_identity": row["row_id"] in legacy}
        for row, a, b, final in zip(rows, pre, post, baseline) if a != b
    ]
    controls = []
    for concept in ("gall", "guest", "goose"):
        index = next(i for i, row in enumerate(rows) if row["concept"] == concept)
        controls.append({**rows[index], "before": pre[index], "after": post[index],
                         "final": baseline[index]})

    probes = [{"id": f"{stage}-{side}", "stage": stage, "side": side}
              for stage in CHECKPOINTS for side in ("before", "after")]
    witness_index = next(i for i, row in enumerate(rows) if row["row_id"] == "1944")
    variants = {}
    component_outputs = {}
    for name, after in (
        ("identity", None), ("skip", "skip"),
        ("after-sc107", "EAFBrighteningUnstressed"),
        ("after-sc043", "EAFBrightening"),
        ("after-breaking", "OEBreaking"),
    ):
        with tempfile.TemporaryDirectory(prefix="capr_sc035_") as temporary:
            bins = compile_isolated(
                runtime.germanic_fst, recipe(after), probes, Path(temporary))
            outputs = batch_apply_down(bins["final"], forms)
            if name == "identity" and outputs != baseline:
                raise RuntimeError("isolated identity disagrees with production")
            if any(len(output) != 1 or output == ["+?"] for output in outputs):
                raise RuntimeError(f"{name}: missing or ambiguous output")
            variants[name] = {
                "changed": [
                    {"row_id": row["row_id"], "concept": row["concept"],
                     "input": oe_pipeline.evaluation_input(row),
                     "baseline": old, "variant": new}
                    for row, old, new in zip(rows, baseline, outputs) if old != new
                ],
                "believe": {
                    key: batch_apply_down(path, [forms[witness_index]])[0]
                    for key, path in bins.items() if not key.startswith("component:")
                },
            }
            if name == "identity":
                component_outputs = dict(zip(
                    COMPONENT_INPUTS,
                    batch_apply_down(bins[f"component:{RULE}"],
                                     list(COMPONENT_INPUTS.values())),
                ))
    if hashes() != before_hashes:
        raise RuntimeError("isolated experiment changed protected canonical artifacts")
    return {
        "base_commit": "60b91080d2adadf431c92f7388ab1dd6199a4c7a",
        "source_sha256": hashlib.sha256(runtime.germanic_fst.read_bytes()).hexdigest(),
        "selected_rows": len(rows),
        "legacy380_identity_rows": sum(row["row_id"] in legacy for row in rows),
        "live_census": census, "live_negative_controls": controls,
        "component_inputs": COMPONENT_INPUTS, "component_outputs": component_outputs,
        "variants": variants, "canonical_artifacts_unchanged": True,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

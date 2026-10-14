"""Protected full-cascade assays with independently checked stage replay."""
import copy
import csv
import json
from pathlib import Path
import sys
import tempfile
import time

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import check_build_manifest, layout

ROOT = Path("/research")
runtime = layout()
data = assay.load_recipes(ROOT / "recipes-context-v2.json")
stage_map = json.loads((ROOT / "stage_map.json").read_text())
probes = [probe for probe in data["probes"] if probe["stage"] in {
    "PNWGmcULowering", "PNWGmcStressedMonosyllableORaising",
    "PNWGmcFinalLongORaising", "OEHighVowelApocope",
}]

if not runtime.is_container:
    raise RuntimeError("Container execution required")
for field, path in (
    ("baseline_fst_sha256", runtime.germanic_fst),
    ("baseline_corpus_sha256", runtime.corpus_tsv),
    ("baseline_context_sha256", runtime.data_dir / assay.METADATA_FILENAME),
    ("baseline_context_helper_sha256", runtime.bin_dir / "oe_input_context.py"),
):
    if data[field] != assay.digest(path):
        raise RuntimeError(f"Stale scientific pin: {field}")
errors = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
if errors:
    raise RuntimeError(f"Stale copied baseline: {errors}")

baseline_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
protected = [
    runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
    runtime.data_dir / assay.METADATA_FILENAME, runtime.bin_dir / "oe_input_context.py",
    runtime.build_manifest, runtime.bin_dir / "old_english.bin",
    *(runtime.bin_dir / name for name in oe_pipeline.expected_snapshot_bins()),
    *sorted(baseline_dir.glob("cascade_baseline_outputs*.tsv")),
    *sorted(baseline_dir.glob("cascade_baseline_summary*.json")),
    *sorted(baseline_dir.glob("approved_*_migration.json")),
    baseline_dir / "approved_input_migrations.tsv",
    *(runtime.docs_dir / "sound_changes/registry" / name for name in (
        "sc_registry.tsv", "chronology_edges.tsv", "sc_inventory_notes.tsv")),
]
before = {str(path): assay.digest(path) for path in protected}
rows = assay.corpus_rows(runtime.corpus_tsv)
forms = [oe_pipeline.evaluation_input(row) for row in rows]
canonical = assay.batch_apply_down(runtime.bin_dir / "old_english.bin", forms)
if len(rows) != 387 or any(len(output) != 1 for output in canonical):
    raise RuntimeError("Baseline population/determinism failed")

# Each cell is PGmc; acute root stress is CAPR encoding, not a new source quote.
families = [
    ("wool", "wúll", "Ringe2017 pp.242-243", "2300", "wull", "wulle"),
    ("love", "lúb", "RingeTaylor2014 p.32; Orel2003 p.249", "", "lufu", "lufe"),
    ("shoal", "skúl", "Fulk2018 p.56; ending Fulk2018 p.155", "", "scolu", ""),
    ("nose", "nús", "Campbell1959 p.43; Kroonen2013 p.383", "2143", "nosu", ""),
    ("shovel", "skúfl", "Orel2003 p.347; ending Fulk2018 p.155", "2185", "sċofl", ""),
    ("sorrow", "súrg", "RingeTaylor2014 p.299; Kroonen2013 p.493", "2200", "sorg", "sorge"),
    ("palm", "fúlm", "Orel2003 p.118; ending Fulk2018 p.155", "", "folm", ""),
]
cells = [
    {"id": f"{name}-{case}", "lexeme": name, "case": case, "stage": "pgmc",
     "source": source, "corpus_id": identifier, "attested_target": target,
     "raw_input": stem + ending,
     "tokenized_input": "".join("*" + char for char in stem + ending),
     "quotation_status": (
         "whole wool cell from Ringe, with CAPR acute stress" if name == "wool"
         else "source stem plus independently supported inflectional cell, CAPR assembly"),
     }
    for name, stem, source, identifier, nominative, accusative in families
    for case, ending, target in (("nom-sg", "ō", nominative), ("acc-sg", "ǭ", accusative))
]
cells += [
    {"id": f"wool-{label}", "lexeme": "wool", "case": label, "stage": "pgmc",
     "source": "RingeTaylor2014 pp.59,299 vs Fulk2018 pp.85,155",
     "corpus_id": "", "attested_target": "wulle", "raw_input": "wúll" + ending,
     "tokenized_input": "".join("*" + char for char in "wúll" + ending),
     "quotation_status": "CAPR assembly of competing generic genitive endings; not an attributed full wool quotation"}
    for label, ending in (("rt-gen-sg-bimoric", "ōz"), ("fulk-gen-sg-trimoric", "ôz"))
]
predictions = json.loads((ROOT / "predictions.json").read_text())
baseline_states = None
baseline_results = None

def replay(bins, order, inputs, start=0):
    outputs = [[form] for form in inputs]
    states = {}
    for position in range(start, len(order)):
        if any(len(output) != 1 for output in outputs):
            failures = [(inputs[index], output) for index, output in enumerate(outputs)
                        if len(output) != 1]
            raise RuntimeError(f"Non-deterministic stage before {order[position]}: {failures}")
        outputs = assay.batch_apply_down(
            bins[f"diagnostic:{position}"], [output[0] for output in outputs])
        states[order[position]] = outputs
    return states, outputs

for recipe in data["recipes"]:
    name = recipe["id"]
    destination = ROOT / f"{name}-replay.json"
    if destination.exists():
        if name != "identity":
            raise RuntimeError(f"Receipt already exists: {destination}")
        prior = json.loads(destination.read_text())
        if prior["recipe"] != recipe or not prior["canonical_artifacts_unchanged"]:
            raise RuntimeError("Saved identity provenance disagrees")
        baseline_states = {
            item["expression"]: [row["intermediates"][item["probe"]]["baseline"]
                                 for row in prior["rows"]]
            for item in stage_map
        }
        baseline_results = [row["baseline_outputs"] for row in prior["rows"]]
        print("REUSE VERIFIED IDENTITY", flush=True)
        continue
    print(f"START REPLAY {name}", flush=True)
    started = time.monotonic()
    order = assay.complete_variant_order(recipe)
    with tempfile.TemporaryDirectory(prefix="capr_wull_replay_") as temporary:
        bins = assay.compile_isolated(
            runtime.germanic_fst, recipe, probes, Path(temporary),
            diagnostic_stages=order)
        full = assay.batch_apply_down(bins["final"], forms)
        states, replayed = replay(bins, order, forms)
        if replayed != full:
            raise RuntimeError(f"Stage replay disagrees with complete compiled cascade: {name}")
        prefix = assay.intermediate_outputs(bins, forms)
        for probe in probes:
            expression = recipe["replace"].get(probe["stage"], probe["stage"])
            if prefix[probe["id"]] != states[expression]:
                raise RuntimeError(f"Independent prefix checkpoint failed: {name}/{probe['id']}")
        if name == "identity":
            if full != canonical:
                raise RuntimeError("Independent complete identity differs from copied canonical bin")
            baseline_states, baseline_results = copy.deepcopy(states), copy.deepcopy(full)
        if baseline_states is None:
            raise RuntimeError("Identity must precede counterfactuals")
        cell_states, cell_finals = replay(
            bins, order, [cell["tokenized_input"] for cell in cells],
            order.index("EnglishProtoInput") + 1)
        wool_nom_index = next(i for i, cell in enumerate(cells) if cell["id"] == "wool-nom-sg")
        wool_acc_index = next(i for i, cell in enumerate(cells) if cell["id"] == "wool-acc-sg")
        if name in predictions:
            sc017 = recipe["replace"].get("PNWGmcULowering", "PNWGmcULowering")
            for key, index in (("wool_nom_after_sc017", wool_nom_index),
                               ("wool_acc_after_sc017", wool_acc_index)):
                if cell_states[sc017][index] != [predictions[name][key]]:
                    raise RuntimeError(f"Declared historical prediction failed: {name}/{key}")
            if "wool_nom_after_revaluation" in predictions[name]:
                if cell_states["AFReval"][wool_nom_index] != [
                    predictions[name]["wool_nom_after_revaluation"]]:
                    raise RuntimeError("D's distinct intermediate prediction failed")
        report_rows = []
        for i, row in enumerate(rows):
            intermediates = {
                item["probe"]: {
                    "baseline": baseline_states[item["expression"]][i],
                    "variant": states[recipe["replace"].get(item["expression"], item["expression"])][i],
                } for item in stage_map
            }
            report_rows.append({
                **row, "baseline_outputs": baseline_results[i], "variant_outputs": full[i],
                "changed": baseline_results[i] != full[i],
                "intermediates": intermediates,
                "changed_intermediate_probes": [
                    probe for probe, pair in intermediates.items()
                    if pair["baseline"] != pair["variant"]],
                "inserted_states": {
                    recipe["insert_rule"]: states[recipe["insert_rule"]][i]
                } if recipe["insert_rule"] else {},
            })
        report = {
            "recipe": recipe, "selected_rows": len(rows),
            "identity_equal": True, "full_wrapper_equals_stage_replay": True,
            "independent_prefix_probe_ids": list(prefix),
            "baseline_mismatch_ids": [row["id"] for i, row in enumerate(rows)
                                      if baseline_results[i] != [row["counterpart"]]],
            "variant_mismatch_ids": [row["id"] for i, row in enumerate(rows)
                                     if full[i] != [row["counterpart"]]],
            "changed_ids": [row["id"] for row in report_rows if row["changed"]],
            "changed_intermediate_ids": [row["id"] for row in report_rows
                                        if row["changed_intermediate_probes"]],
            "missing_output_ids": [row["id"] for i, row in enumerate(rows) if not full[i]],
            "ambiguous_output_ids": [row["id"] for i, row in enumerate(rows) if len(full[i]) > 1],
            "input_changed_ids": [], "checkpoint_count": len(stage_map),
            "canonical_protected_hashes": before,
            "canonical_artifacts_unchanged": before == {
                str(path): assay.digest(path) for path in protected},
            "elapsed_seconds": time.monotonic() - started,
            "rows": report_rows,
            "paradigms": [
                {**cell, "outputs": cell_finals[i],
                 "intermediates": {expression: outputs[i]
                                   for expression, outputs in cell_states.items()}}
                for i, cell in enumerate(cells)],
        }
        if not report["canonical_artifacts_unchanged"]:
            raise RuntimeError("Protected private artifact mutated")
        if name in predictions and report["changed_ids"] != predictions[name]["expected_changed_final_ids"]:
            raise RuntimeError(f"Declared changed-row prediction failed: {name}")
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({key: report[key] for key in (
            "selected_rows", "changed_ids", "changed_intermediate_ids",
            "variant_mismatch_ids", "missing_output_ids",
            "ambiguous_output_ids", "elapsed_seconds")}), flush=True)

"""Derive research annexes from completed private receipts, never production."""
import csv
import dataclasses
import json
from pathlib import Path
import sys

sys.path.insert(0, "/usr/app/tools")
import oe_pipeline
from capr_runtime import layout

root = Path("/research")
runtime = layout()
names = ["identity", "a-order-only", "b-conditioning-only", "c-combined", "d-live-allophony"]
reports = {name: json.loads((root / f"{name}-replay.json").read_text()) for name in names}
equivalence = json.loads((root / "independent-equivalence.json").read_text())
if not equivalence["all_original_107_prefixes_equal_stage_replay"]:
    raise RuntimeError("Independent baseline prefix verification failed")
registry_path = runtime.docs_dir / "sound_changes/registry/sc_registry.tsv"
with registry_path.open() as handle:
    registry = {row["fst_identifier"]: row for row in csv.DictReader(
        (line for line in handle if line.strip() and not line.startswith("#")),
        delimiter="\t")}

def write_table(name, fields, rows):
    destination = root / name
    if destination.exists():
        raise RuntimeError(f"Annex already exists: {destination}")
    with destination.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

def packed(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))

stages = list(oe_pipeline.stages())
write_table("composition_and_historical_metadata.tsv",
            ["exec_index", "cascade_position", "identifier", "kind", "origin_block",
             "sc_id", "hist_stage", "hist_scope", "confidence", "adjudication_status", "verdict"],
            [{"exec_index": stage.exec_index, "cascade_position": stage.cascade_position,
              "identifier": stage.foma_identifier or stage.inline_text,
              "kind": stage.kind, "origin_block": stage.origin_block,
              **{key: registry.get(stage.foma_identifier, {}).get(key, "")
                 for key in ("sc_id", "hist_stage", "hist_scope", "confidence",
                             "adjudication_status", "verdict")}}
             for stage in stages])

write_table("all_387_rows_all_variants.tsv",
            ["variant", "id", "concept", "selected_input", "evaluation_input", "target",
             "baseline_outputs", "variant_outputs", "changed_final", "changed_intermediate",
             "mismatch", "rejected", "ambiguous"],
            [{"variant": name, "id": row["id"], "concept": row["concept"],
              "selected_input": row["proto"], "evaluation_input": row["fst_input"],
              "target": row["counterpart"], "baseline_outputs": packed(row["baseline_outputs"]),
              "variant_outputs": packed(row["variant_outputs"]),
              "changed_final": int(row["changed"]),
              "changed_intermediate": int(bool(row["changed_intermediate_probes"])),
              "mismatch": int(row["variant_outputs"] != [row["counterpart"]]),
              "rejected": int(not row["variant_outputs"]),
              "ambiguous": int(len(row["variant_outputs"]) > 1)}
             for name, report in reports.items() for row in report["rows"]])

write_table("all_changed_intermediates.tsv",
            ["variant", "id", "concept", "probe", "baseline", "variant_state"],
            [{"variant": name, "id": row["id"], "concept": row["concept"], "probe": probe,
              "baseline": packed(pair["baseline"]), "variant_state": packed(pair["variant"])}
             for name, report in reports.items() for row in report["rows"]
             for probe, pair in row["intermediates"].items()
             if pair["baseline"] != pair["variant"]])

write_table("all_paradigm_cells.tsv",
            ["variant", "id", "lexeme", "case", "stage", "source", "quotation_status",
             "corpus_id", "raw_input", "tokenized_input", "attested_target",
             "outputs", "rejected", "ambiguous"],
            [{"variant": name, **{key: cell[key] for key in (
                "id", "lexeme", "case", "stage", "source", "quotation_status",
                "corpus_id", "raw_input", "tokenized_input", "attested_target")},
              "outputs": packed(cell["outputs"]), "rejected": int(not cell["outputs"]),
              "ambiguous": int(len(cell["outputs"]) > 1)}
             for name, report in reports.items() for cell in report["paradigms"]])

maps = json.loads((root / "stage_map.json").read_text())
baseline = reports["identity"]["rows"]
census = []
for identifier in ("PNWGmcULowering", "PNWGmcStressedMonosyllableORaising",
                   "PNWGmcFinalLongORaising"):
    index = next(i for i, stage in enumerate(maps) if stage["expression"] == identifier)
    before, after = maps[index - 1]["probe"], maps[index]["probe"]
    for row in baseline:
        if row["intermediates"][before]["baseline"] != row["intermediates"][after]["baseline"]:
            census.append({
                "rule": identifier, "id": row["id"], "concept": row["concept"],
                "selected_input": row["proto"],
                "before": packed(row["intermediates"][before]["baseline"]),
                "after": packed(row["intermediates"][after]["baseline"]),
                "witness_role": (
                    "live application; selected lexical history is an unresolved exception"
                    if identifier == "PNWGmcULowering" and row["id"] in
                    {"1973", "2030", "2162", "2298", "2300"}
                    else "live application; root lowering or quantity change in stated executable domain"),
            })
write_table("complete_sc017_sc018_sc019_firing_census.tsv",
            ["rule", "id", "concept", "selected_input", "before", "after", "witness_role"],
            census)
write_table("paradigm_all_intermediate_states.tsv",
            ["variant", "cell", "expression", "outputs"],
            [{"variant": name, "cell": cell["id"], "expression": stage,
              "outputs": packed(outputs)}
             for name, report in reports.items() for cell in report["paradigms"]
             for stage, outputs in cell["intermediates"].items()])
summary = {
    name: {key: report[key] for key in (
        "selected_rows", "changed_ids", "changed_intermediate_ids",
        "variant_mismatch_ids", "missing_output_ids", "ambiguous_output_ids",
        "elapsed_seconds", "canonical_artifacts_unchanged")}
    for name, report in reports.items()
}
(root / "measured-summary.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
print("Built six exact-ID TSV annexes and measured summary")

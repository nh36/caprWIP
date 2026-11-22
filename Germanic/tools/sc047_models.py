#!/usr/bin/env python3
"""Build and audit the two active Old English cascades inside CAPR's backend."""

import argparse
import csv
import gzip
import hashlib
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import anglo_frisian_experiments as compiler
from capr_runtime import layout
from oe_pipeline import CITATION_CONTEXT, METADATA_FILENAME, load_rows, parse_stages
from sound_change_order_sensitivity import batch_apply_down

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = DOCS / "sound_changes/literature_dossiers/sc047_paired_chronologies"
FROZEN = BASE / "comparative_followup/parallel/observations.json.gz"
PLAN = BASE / "labial_review/plan.json"
CELLS = DOCS / "models/sc047/cells.tsv"
MODELS = {"A": "early", "B2": "split_geminate_only"}
VERSION = "sc047-active-v2"
FROZEN_SHA = "f2962dde3a9f0e1771c6de1bab6cbd2b18f0f844bbddfcb6807b7dab81e43060"
PLAN_SHA = "71b0bf5b33e9ee8196964245b6f0050ea3a200a71f7ba10065f3379f9ca155d5"
PROPOSAL = "399c50ad1dd339df4d235dda53334b39fb5fec14"
RAISE = "PNWGmcFinalLongORaising"
LOWER = "PNWGmcULowering"
LENGTHEN = "PNWGmcMonosyllabicFinalRLengthening"
Z_LOSS = "EAFFinalZDeletion"
ORAL = "PWGmcFinalBareALoss"
NASAL = "OEHeavySyllableNasalApocope"
GEM = "PWGmcJGemination"
W_LOSS = "OEWLossBeforeI"
INPUT = "EnglishProtoInput"
ACTIVE_INPUT = "SC047ProtoInput"
DAT_MONO = "SC047FinalOi"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def capture_inputs(runtime=None):
    runtime = runtime or layout()
    return {
        "frozen_sha256": FROZEN,
        "plan_sha256": PLAN,
        "cells_sha256": CELLS,
        "fst_sha256": runtime.germanic_fst,
        "corpus_sha256": runtime.corpus_tsv,
        "context_metadata_sha256": runtime.data_dir / METADATA_FILENAME,
        "runner_sha256": Path(__file__).resolve(),
        "pipeline_sha256": runtime.tools_dir / "oe_pipeline.py",
        "compiler_sha256": runtime.tools_dir / "anglo_frisian_experiments.py",
        "executable_facts_sha256": runtime.tools_dir / "executable_facts.py",
        "stage_lookup_sha256": runtime.tools_dir / "sound_change_order_sensitivity.py",
        "input_context_sha256": runtime.bin_dir / "oe_input_context.py",
    }


def verify_capture_inputs(capture):
    for field, path in capture_inputs().items():
        if capture.get(field) != sha(path):
            raise ValueError(f"Active model capture is stale for {path.name}")


def model_orders(canonical, plan):
    orders = {}
    for model, archived in MODELS.items():
        order = list(canonical)
        for op in plan["configurations"][archived]:
            if "replace" in op:
                order[order.index(op["replace"])] = op["with"]
            else:
                stage = op.get("move") or op["insert"]
                if "move" in op:
                    order.remove(stage)
                order.insert(order.index(op["after"]) + 1, stage)
        # Restore SC019 before SC020 without sacrificing the lowering and door controls.
        order.remove(RAISE)
        order.insert(order.index(LENGTHEN) + 1, RAISE)
        order[order.index(INPUT)] = ACTIVE_INPUT
        order.insert(order.index("PNWGmcUnstressedAiMonophthongization") + 1, DAT_MONO)
        if model == "A":
            order[order.index("FNU")] = "FNG"
        order[order.index("OEAwLongDiphthong")] = "SC047NarrowAw"
        order.insert(order.index(W_LOSS) + 1, "SC047FinalIi")
        orders[model] = order
    return orders


def read_cells():
    with CELLS.open(encoding="utf-8") as source:
        cells = list(csv.DictReader(source, delimiter="\t"))
    keys = {(row["lexeme"], row["cell"]) for row in cells}
    if len(keys) != len(cells):
        raise ValueError("Duplicate paradigm cell")
    if any(row["selected_in"] not in ("", "A", "B2", "AB2") for row in cells):
        raise ValueError("Unknown model in cell register")
    return cells


def selections(rows, cells, model):
    by_id = {row["row_id"]: row for row in rows}
    result = {row_id: {} for row_id in by_id}
    for cell in cells:
        if cell["selected_in"] not in (model, "AB2"):
            continue
        row_id = cell["row_id"]
        if (row_id not in by_id or result[row_id] or cell["lexeme"] != by_id[row_id]["concept"]
                or not cell["target"] or not cell["evidence"]
                or not cell["input"]):
            raise ValueError(f"Incomplete, duplicate or misidentified selection: {cell}")
        row = by_id[row_id]
        if CITATION_CONTEXT.encode(row["proto_norm"]) != row["fst_input"]:
            raise ValueError(f"Selection needs an explicit non-citation context: {cell}")
        result[row_id] = {
            "selected_cell": cell["cell"],
            "selected_input": CITATION_CONTEXT.encode(cell["input"]),
            "selected_target": cell["target"],
        }
    return result


def apply_stage(bin_path, previous):
    domain = sorted({value for outputs in previous.values() for value in outputs})
    mapped = dict(zip(domain, batch_apply_down(bin_path, domain))) if domain else {}
    return {key: sorted({out for value in outputs for out in mapped[value]})
            for key, outputs in previous.items()}


def trace(order, paths, inputs):
    previous = {key: [value] for key, value in inputs.items()}
    changes = {key: [] for key in inputs}
    for stage in order:
        current = apply_stage(paths[f"component:{stage}"], previous)
        for key, output in current.items():
            if output != previous[key]:
                changes[key].append([stage, output])
        previous = current
    return previous, changes


def model_sources(source):
    if sha(PLAN) != PLAN_SHA:
        raise ValueError("SC047 configuration does not match the reviewed plan")
    canonical = [stage.foma_identifier for stage in parse_stages(source)]
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    orders = model_orders(canonical, plan)
    definitions = [plan["definitions"][name] for name in ("FW", "FNU", "FON", "FNG")]
    definitions.extend((
        """define SC047NarrowAw Ctx([
            {*a} {*w} -> {*ēa} {*w} || _ [[EnglishStarVocalic - [{*i}|{*ī}]] | {*ô}],
            {*á} {*w} -> {*ḗa} {*w} || _ [[EnglishStarVocalic - [{*i}|{*ī}]] | {*ô}]
        ]);""",
        "define SC047FinalIi Ctx([{*í} {*i} -> {*ḯ} || _ .#.]);",
        """define SC047ExtraCell [pgrmPrefix | 0] PGCellRoot PGCellStem*
            ō:{*ō} [i:{*i} | m:{*m} i:{*i} z:{*z}];
        define SC047ProtoInput [EnglishProtoInput |
            _unambpart([[SC047ExtraCell.u - EnglishProtoInput.u] .o. SC047ExtraCell])];""",
        "define SC047FinalOi Ctx([{*ō} {*i} -> {*ē} || _ .#.]);",
    ))
    return canonical, orders, "\n".join(definitions)


def composition(model, order):
    return f"define CAPR{model} " + "\n    .o. ".join(order) + ";\n"


def editor_source(model):
    source = layout().germanic_fst
    text = source.read_text(encoding="utf-8")
    _, orders, definitions = model_sources(source)
    export = "regex OldEnglish;\nsave stack old_english.bin"
    if text.count(export) != 1:
        raise ValueError("Expected exactly one Old English export")
    return text.replace(export, definitions + "\n" + composition(model, orders[model])
                        + f"regex CAPR{model};\nsave stack old_english.bin") + "\nquit\n"


def run(models, forms=(), *, active=False, binaries=None):
    source = layout().germanic_fst
    inputs = capture_inputs()
    hashes = {label: sha(path) for label, path in inputs.items()}
    if hashes["frozen_sha256"] != FROZEN_SHA or hashes["plan_sha256"] != PLAN_SHA:
        raise ValueError("SC047 historical input digest does not match the pinned archive")
    with gzip.open(FROZEN, "rt", encoding="utf-8") as stream:
        frozen = json.load(stream)
    if hashes["fst_sha256"] != frozen["inputs_sha256"]["germanic.txt"]:
        raise ValueError("A changed canonical FST needs a new reviewed model base")
    expected = {row["row_id"]: row for row in frozen["corpus"]}
    fields = ("row_id", "concept", "proto", "proto_norm", "fst_input", "word_stress",
              "phonological_finality", "counterpart")
    rows = [{key: row[key] for key in fields} for row in frozen["corpus"]]
    live_rows = load_rows(layout().corpus_tsv) if active else []
    if len({row["row_id"] for row in live_rows}) != len(live_rows):
        raise ValueError("Duplicate active lexical identity")

    canonical, orders, definitions = model_sources(source)
    cells = read_cells()
    components = set(canonical).union(*(orders[model] for model in models))
    exports = ("\n".join(composition(model, orders[model]) +
                         f"clear stack\nregex CAPR{model};\nsave stack old_english_{model}.bin"
                         for model in models) if binaries is not None else "")
    queries = {f"query:{i}": form for i, form in enumerate(forms)}
    results = {}
    with tempfile.TemporaryDirectory(prefix="capr-sc047-active-") as tmp:
        work = Path(tmp)
        image = compiler.prepare_definition_image(source, work)
        if image is None:
            raise RuntimeError("Unable to prepare the common definition image")
        with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
            paths = compiler.compile_isolated(source, {
                "definitions": definitions + "\n" + exports, "replace": {},
                "insert_rule": None, "insert_after": None,
                "component_checks": [{"component": stage} for stage in sorted(components)],
            }, [], work, components_only=True)
        diag = {f"row:{row['row_id']}": row["fst_input"] for row in rows}
        live = {f"active:{row['row_id']}": row["fst_input"] for row in live_rows}
        canonical_outputs, canonical_traces = trace(canonical, paths, diag)
        for row in rows:
            if canonical_outputs[f"row:{row['row_id']}"] != expected[row["row_id"]]["identity"]:
                raise RuntimeError(f"Stage evaluation disagrees with canonical composition: {row['row_id']}")
        for model in models:
            overrides = selections(rows, cells, model)
            probes = {f"cell:{cell['lexeme']}:{cell['cell']}": CITATION_CONTEXT.encode(cell["input"])
                      for cell in cells}
            selected = {f"selected:{row_id}": override["selected_input"]
                        for row_id, override in overrides.items() if override}
            endpoints, traces = trace(orders[model], paths, diag | probes | selected | queries | live)
            if binaries is not None:
                path = work / f"old_english_{model}.bin"
                inputs_to_verify = diag | probes | selected | queries | live
                composed = batch_apply_down(path, list(inputs_to_verify.values()))
                for key, output in zip(inputs_to_verify, composed):
                    if sorted(set(output)) != endpoints[key]:
                        raise RuntimeError(f"Model {model} composed output disagrees with trace: {key}")
            corpus = []
            for row in rows:
                row_id = row["row_id"]
                diag_key = f"row:{row_id}"
                selected_key = f"selected:{row_id}" if overrides[row_id] else diag_key
                corpus.append({
                    **row,
                    "diagnostic_outputs": endpoints[diag_key],
                    "canonical_outputs": canonical_outputs[diag_key],
                    "canonical_trace": canonical_traces[diag_key],
                    "selected_cell": None,
                    "selection_status": ("unresolved comparison" if model == "A" and row_id == "2061"
                                         else "explicit cell" if overrides[row_id] else "retained"),
                    "selected_input": row["fst_input"],
                    "selected_target": row["counterpart"],
                    **overrides[row_id],
                    "selected_outputs": endpoints[selected_key],
                    "diagnostic_trace": traces[diag_key],
                    "selected_trace": traces[selected_key] if selected_key != diag_key else None,
                })
            results[model] = {
                "order": orders[model], "corpus": corpus,
                "paradigms": [{**cell, "outputs": endpoints[key], "trace": traces[key]}
                              for cell, key in zip(cells, probes)],
                "queries": [{"input": form, "outputs": endpoints[key], "trace": traces[key]}
                            for key, form in queries.items()],
            }
            if active:
                results[model]["active_corpus"] = [
                    {**row, "outputs": endpoints[f"active:{row['row_id']}"],
                     "trace": traces[f"active:{row['row_id']}"]}
                    for row in live_rows
                ]
        if any(sha(path) != hashes[label] for label, path in inputs.items()):
            raise RuntimeError("An input changed while evaluating the SC047 model")
        if binaries is not None:
            binaries.mkdir(parents=True, exist_ok=True)
            files = [f"old_english_{model}.bin" for model in models]
            files.extend(("english.bin", "german.bin", "dutch.bin", "old_english.bin"))
            for name in files:
                path = work / name
                with tempfile.NamedTemporaryFile(dir=binaries, delete=False) as tmp_bin:
                    tmp_bin.write(path.read_bytes())
                    temp_path = Path(tmp_bin.name)
                os.replace(temp_path, binaries / name)
    return {"version": VERSION, "lexical_proposal": PROPOSAL, **hashes, "models": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=(*MODELS, "both"), default="both")
    parser.add_argument("--active", action="store_true",
                        help="also evaluate the shared active lexical corpus, without changing the benchmark")
    parser.add_argument("--form", action="append", default=[],
                        help="also trace a CAPR-encoded input (omit the reconstruction asterisk)")
    parser.add_argument("--build-bins", type=Path,
                        help="compile each selected model, verify against stage traces, and write bins here")
    args = parser.parse_args()
    if args.build_bins is not None and not args.active:
        parser.error("--build-bins requires --active to verify the live corpus")
    if any(not form or any(c in form for c in "\r\n\t") for form in args.form):
        parser.error("--form must be nonempty and contain no tabs or line breaks")
    models = tuple(MODELS) if args.model == "both" else (args.model,)
    print(json.dumps(run(models, args.form, active=args.active, binaries=args.build_bins),
                     ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()

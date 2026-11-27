#!/usr/bin/env python3
"""Batch trace research inputs against a private copy of the frozen cascade."""

import csv
import gzip
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unicodedata
from unittest.mock import patch

BASE = "113101ac5f169b589e1a9647cdf24d32cdd4d919"
ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "Germanic/tools"))

import sc047_models as frozen


def read_json(path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def evaluate(order, paths, inputs, anchors):
    states = {key: [form] for key, form in inputs.items()}
    records = {key: {"input": form, "changes": [], "anchors": {}}
               for key, form in inputs.items()}
    for stage in order:
        after = frozen.apply_stage(paths[f"component:{stage}"], states)
        for key, result in after.items():
            record = records[key]
            if states[key] != result:
                record["changes"].append([stage, result])
            if stage in anchors:
                record["anchors"][stage] = [states[key], result]
        states = after
    for key, result in states.items():
        records[key]["output"] = result
    return records


def compile_stages(source, definitions, orders, directory):
    compiler = frozen.compiler
    image = compiler.prepare_definition_image(source, directory)
    if image is None:
        raise RuntimeError("Missing common definition image")
    recipe = {"definitions": definitions, "replace": {}, "insert_rule": None,
              "insert_after": None, "component_checks": [
                  {"component": stage} for stage in sorted(set().union(*orders.values()))
              ]}
    with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
        return compiler.compile_isolated(source, recipe, [], directory, components_only=True)


def main():
    source = ROOT / "Germanic/fsts/germanic.txt"
    archive = read_json(frozen.FROZEN)
    capture = read_json(frozen.DOCS / "models/sc047/captures/sc047-adoption-v1.json.gz")
    if (frozen.sha(frozen.FROZEN) != frozen.FROZEN_SHA
            or frozen.sha(source) != archive["inputs_sha256"]["germanic.txt"]
            or frozen.sha(source) != capture["fst_sha256"]
            or frozen.sha(frozen.CELLS) != capture["cells_sha256"]):
        raise RuntimeError("Frozen sources do not match the capture")
    inventory = HERE / "historical.tsv"
    with inventory.open(encoding="utf-8") as stream:
        inputs = {r["id"]: unicodedata.normalize("NFC", r["submit"])
                  for r in csv.DictReader(stream, delimiter="\t") if r["submit"]}
    canonical, orders, definitions = frozen.model_sources(source)
    orders = {"canonical": canonical, **orders}
    anchors = {"OEWLossBeforeI", "SC047FinalIi", "OEHighVowelApocope",
               "OEMedUnstressedILowering1", "OEMedUnstressedILowering",
               "OEUnstressedEIContraction", "OEHLoss", "OEContraction",
               "OldEnglishOrthography", "OldEnglishSurface"}
    reference = {f'row:{r["row_id"]}': r for r in archive["corpus"]}
    corpus = {key: row["fst_input"] for key, row in reference.items()}
    results = {}
    with tempfile.TemporaryDirectory(prefix="hay-build-") as tmp:
        paths = compile_stages(source, definitions, orders, Path(tmp))
        for model, order in orders.items():
            expected = ({key: row["identity"] for key, row in reference.items()}
                        if model == "canonical" else
                        {f'row:{row["row_id"]}': row["diagnostic_outputs"]
                         for row in capture["models"][model]["corpus"]})
            selected = {key: corpus[key] for key in expected}
            actual = evaluate(order, paths, inputs | selected, anchors | {order[0]})
            if any(actual[key]["output"] != output for key, output in expected.items()):
                raise RuntimeError(f"{model} does not reproduce the frozen corpus")
            results[model] = {"reference_rows_reproduced": len(expected),
                              "traces": {key: actual[key] for key in inputs}}
    data = {"base": BASE, "source_sha256": frozen.sha(source),
            "inventory_sha256": frozen.sha(inventory),
            "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
            "orders": orders, "models": results}
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

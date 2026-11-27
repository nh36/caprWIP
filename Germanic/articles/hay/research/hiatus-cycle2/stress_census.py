#!/usr/bin/env python3
"""Census exact frozen and foot-guard contraction on archived and active panels."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch

sys.path.insert(0, str(Path(sys.argv[1]) / "Germanic/articles/hay/research/hiatus"))
import run

from reproduce_stress import DELETION, verify
from stress_repairs import FOOT_DEFINITION


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    capture_path = run.frozen.DOCS / "models/sc047/captures/sc047-adoption-v1.json.gz"
    capture = run.read_json(capture_path)
    archive = run.read_json(run.frozen.FROZEN)
    verify(run.frozen.sha(run.frozen.FROZEN), run.frozen.FROZEN_SHA, "archived corpus identity")
    verify(run.frozen.sha(source), capture["fst_sha256"], "frozen source identity")
    verify(run.frozen.sha(run.frozen.CELLS), capture["cells_sha256"], "frozen cell identity")
    reference_file = run.HERE / "joint-corpus.json"
    reference = json.loads(reference_file.read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-stress-census-") as directory:
        recipe = {"definitions": FOOT_DEFINITION, "replace": {}, "insert_rule": None,
                  "insert_after": None, "component_checks": [{"component": "StFoot"}]}
        with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(args.stage_cache / "defined.bin")}):
            if not run.frozen.compiler.definition_image_source(
                    source.read_text(encoding="utf-8"), Path(directory)).startswith("load defined "):
                raise RuntimeError("Census requires the verified frozen definition image")
            repair = run.frozen.compiler.compile_isolated(
                source, recipe, [], Path(directory), components_only=True)["component:StFoot"]
        for model, order in orders.items():
            archived = archive["corpus"] if model == "canonical" else capture["models"][model]["corpus"]
            active = capture["models"]["A" if model == "canonical" else model]["active_corpus"]
            rows = {f"{panel}:{row['row_id']}": row for panel, items in
                    (("archived", archived), ("active", active)) for row in items}
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            verify(len(rows), 790, f"{model}/panel size")
            original = run.evaluate(order, paths, inputs, {DELETION})
            previous = reference["models"][model]["baseline"]
            verify({key: (row["input"], row["output"]) for key, row in original.items()},
                   {key: (row["fst_input"], row["output"]) for key, row in previous.items()},
                   f"{model}/all frozen endpoints")
            candidate_outputs = run.frozen.apply_stage(
                repair, {key: row["anchors"][DELETION][0] for key, row in original.items()})
            firings = {}
            changes = {}
            compare = {}
            for key, row in original.items():
                entering, frozen_out = row["anchors"][DELETION]
                repaired_out = candidate_outputs[key]
                if entering != frozen_out or entering != repaired_out:
                    firings[key] = {"concept": rows[key]["concept"], "input": row["input"],
                                    "before": entering, "S0": frozen_out, "S1": repaired_out}
                if frozen_out != repaired_out:
                    compare[key] = row["input"]
            if compare:
                traces = run.evaluate(order, paths | {f"component:{DELETION}": repair},
                                      compare, {DELETION})
                changes = {key: {"baseline": original[key], "repaired": trace}
                           for key, trace in traces.items()}
            models[model] = {"panel_sizes": {"archived": len(archived), "active": len(active)},
                             "firings": firings, "changed_derivations": changes}
    print(json.dumps({"base": run.BASE, "source_sha256": run.frozen.sha(source),
                      "prior_receipt_sha256": run.frozen.sha(reference_file),
                      "runner_sha256": run.frozen.sha(Path(__file__)),
                      "repair": FOOT_DEFINITION, "models": models},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()

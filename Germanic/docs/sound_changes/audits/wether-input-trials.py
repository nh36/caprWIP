#!/usr/bin/env python3
"""Reproduce the pre-adoption wether input-only comparisons in the backend."""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import anglo_frisian_experiments as experiments
import oe_pipeline
from capr_runtime import layout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("refusing to overwrite an experimental receipt")
    identity = {
        "id": "identity", "description": "Unchanged canonical cascade",
        "definitions": "", "insert_after": "", "insert_rule": "", "replace": {},
        "sources": [],
        "assumptions": "Selected masculine nominative singular; PGmc input.",
        "limitations": "Output convergence does not select the reconstruction.",
    }
    data = {
        "schema_version": 1,
        "baseline_fst_sha256": "6c33b3c723150b61de4a41c89e228f32eeceb8280114b573e182eb8baf6ff51f",
        "baseline_corpus_sha256": "165f859329efee0fc3bda0fbc9d4030de340ec9e5ad5341a738dfbf8e494699b",
        "recipes": [identity],
        "probes": [
            {"id": f"after_{number:03d}", "stage": stage.foma_identifier, "side": "after"}
            for number, stage in enumerate(oe_pipeline.stages())
            if stage.foma_identifier == "PNWGmcILowering"
        ],
    }
    for name, form in (("wether-u-stem", "*wéθruz"), ("wether-a-stem", "*wéθraz")):
        data["recipes"].append({
            **identity, "id": name, "description": f"Input-only comparison: {form}",
            "sources": [{"key": "Kroonen2013", "pages": "584"},
                        {"key": "Orel2003", "pages": "459-460"}],
            "input_overrides": [{"row_id": "2283", "baseline_input": "*wíθrą",
                                 "variant_input": form, "input_stage": "pgmc"}],
        })
    with tempfile.TemporaryDirectory(prefix="capr_wether_recipe_") as temporary:
        path = Path(temporary) / "recipes.json"
        path.write_text(json.dumps(data, ensure_ascii=False))
        recipes = experiments.load_recipes(path)
        results = {}
        runtime = layout()
        rows = experiments.corpus_rows(runtime.corpus_tsv)
        forms = [oe_pipeline.evaluation_input(row) for row in rows]
        probes = [
            {"id": f"after_{number:03d}", "stage": stage.foma_identifier,
             "side": "after", "bin": stage.snapshot_bin}
            for number, stage in enumerate(oe_pipeline.stages())
            if stage.kind != "inline"
        ]
        for name in ("wether-u-stem", "wether-a-stem"):
            result = experiments.run(recipes, name)
            recipe = next(item for item in recipes["recipes"] if item["id"] == name)
            variant = experiments.apply_input_overrides(rows, recipe)
            variant_forms = [oe_pipeline.evaluation_input(row) for row in variant]
            # Input-only trials can reuse the provenance-checked canonical
            # prefixes instead of recompiling all 106 identical prefixes.
            for probe in probes:
                path = runtime.bin_dir / probe["bin"]
                old = experiments.batch_apply_down(path, forms)
                new = experiments.batch_apply_down(path, variant_forms)
                for row, before, after in zip(result["rows"], old, new):
                    row["intermediates"][probe["id"]] = {"baseline": before, "variant": after}
            changed = [path for path, expected in result["canonical_protected_hashes"].items()
                       if experiments.digest(Path(path)) != expected]
            if changed:
                raise RuntimeError("canonical artifacts changed during checkpoint comparison: "
                                   + "; ".join(changed))
            results[name] = result
            print(f"{name}: complete wrapper and {len(probes)} canonical checkpoints checked",
                  flush=True)
    receipt = {"recipes": data, "snapshot_probes": probes, "results": results}
    args.output.write_bytes(gzip.compress(
        (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode(), mtime=0))
    for name, result in results.items():
        print(name, {key: value for key, value in result.items()
                     if key not in {"rows", "recipe", "canonical_protected_hashes"}})


if __name__ == "__main__":
    main()

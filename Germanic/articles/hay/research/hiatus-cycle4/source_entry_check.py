"""Replay source-quantity corrections to the archived local stage entries."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from quantity_check import ComponentBuild, DELETION, common, digest, run, trial, verify
from integrated import Components


ENTRIES = {
    "OEWLossBeforeI": {
        "pillow-short": "*p*y*l*w*i",
        "pillow-long": "*p*y*l*w*ī",
        "pillow-long-after-loss": "*p*y*l*ī",
        "prepare-ws-lowered": "*ʝ*i*e*r*w*i*d*e",
        "prepare-ws-long-tail": "*ʝ*ie*r*w*i*d*ǣ",
        "prepare-merc-long-tail": "*ʝ*e*r*w*i*d*ǣ",
        "betray-lowered": "*l*ē*w*i*d*e",
        "betray-long-tail": "*l*ē*w*i*d*ǣ",
        "strew-lowered": "*s*t*r*e*w*i*d*e",
        "strew-e-long-tail": "*s*t*r*e*w*i*d*ǣ",
        "strew-long-tail": "*s*t*r*æ*w*i*d*ǣ",
    },
    "OEHLoss": {
        "higher-short-tail": "*x*ē*ç*i*r*a",
        "higher-long-tail": "*x*ē*ç*i*r*ā",
    },
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    baseline = json.loads((run.HERE / "baseline.json").read_text())
    verify(digest(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    results = {}
    with tempfile.TemporaryDirectory(prefix="hay4-source-entries-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Components, runtime)
        paths = frozen | build.verify()
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        for model, order in orders.items():
            placements = common(order)
            results[model] = {
                "frozen": trial(order, frozen, ENTRIES, ()),
                "cycle3-common": trial(order, paths, ENTRIES, placements),
                "placements": placements,
            }
        print(json.dumps({
            "base": run.BASE, "orders": orders, "inputs": ENTRIES,
            "source_sha256": digest(source), "runner_sha256": digest(Path(__file__)),
            "frozen_component_hashes": {key: digest(value) for key, value in frozen.items()},
            "historical_pdf": {"sheets": [273, 274, 275, 332],
                               "sha256": "278f94f6076a31278ecca75d8d0429f0822728e5efe0ec3011186a694cf8d6f2"},
            "components": build.receipt(), "definitions": Components.definitions(), "models": results,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

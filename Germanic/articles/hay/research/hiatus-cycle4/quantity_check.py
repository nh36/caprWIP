"""Re-evaluate the exact long inputs behind the three R8 h-loss claims."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from component_check import SNAPSHOT, run, verify
from components import ComponentBuild, digest


sys.path.insert(0, str(SNAPSHOT / "Germanic/articles/hay/research/hiatus-cycle3"))

from integrated import common
from later_h import Components
from matched import trial
from reproduce_stress import DELETION
from sources import AFTER_H, H


ENTRIES = {
    H: {
        "cover-original": "*w*r*i*ç*i*θ",
        "cover-long": "*w*r*ī*ç*i*θ",
        "cover-long-full-ending": "*w*r*ī*ç*i*θ*i",
        "receive-original": "*f*æ*ç*i*θ",
        "receive-rounded": "*f*œ̄*ç*i*θ",
        "receive-rounded-full-ending": "*f*œ̄*ç*i*θ*i",
        "receive-unrounded-proxy": "*f*ē*ç*i*θ",
        "rug-front-original": "*r*y*ç*e",
        "rug-front-ringe-taylor": "*r*ȳ*ç*ǣ",
        "rug-front-lowered-probe": "*r*ȳ*ç*e",
        "rug-back-original": "*r*y*x*a*n",
        "rug-back-long": "*r*ȳ*x*a*n",
    },
    AFTER_H: {"receive-rounded-after-loss": "*f*œ̄*i*θ"},
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
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay4-quantity-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Components, runtime)
        paths = frozen | build.verify()
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        for model, order in orders.items():
            placements = tuple(sorted(common(order) + ((AFTER_H, "HbFront"), (AFTER_H, "HbIden")),
                                      key=lambda pair: order.index(pair[0])))
            m = models[model] = {
                "frozen": trial(order, frozen, ENTRIES, ()),
                "cycle3-common": trial(order, paths, ENTRIES, placements),
                "placements": placements,
            }
            trace = m["cycle3-common"]
            verify(trace["cover-long"]["anchors"]["AbsHigh"],
                   [["*w*r*ī*i*θ"], ["*w*r*ī*θ"]], f"{model} long-vowel absorption")
            verify(trace["cover-original"]["anchors"]["OEContraction"],
                   [["*w*r*i*i*θ"], ["*w*r*ī*θ"]], f"{model} misassigned short coalescence")
            verify(trace["receive-unrounded-proxy"]["anchors"]["AbsHigh"],
                   [["*f*ē*i*θ"], ["*f*ē*θ"]], f"{model} supported long-token proxy")
        print(json.dumps({
            "base": run.BASE, "orders": orders, "inputs": ENTRIES,
            "source_sha256": digest(source), "runner_sha256": digest(Path(__file__)),
            "frozen_component_hashes": {key: digest(value) for key, value in frozen.items()},
            "historical_pdf": {"sheets": [332], "printed_pages": [317],
                               "sha256": "278f94f6076a31278ecca75d8d0429f0822728e5efe0ec3011186a694cf8d6f2"},
            "components": build.receipt(), "definitions": Components.definitions(), "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

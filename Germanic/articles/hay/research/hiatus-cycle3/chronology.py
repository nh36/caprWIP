#!/usr/bin/env python3
"""Vary only bounded front-hiatus placements, preserving all other T5m operations."""

import argparse
import json
from pathlib import Path
import tempfile

from integrated import Components, MECHANISMS, apply, common
from matched import trial
from representation import components as representation_components
from reproduce_stress import DELETION, run, verify


HVD = "OEHighVowelApocope"
LOWERING = "OEMedUnstressedILowering1"
AFTER_REDUCTION = "OEJLossAfterHeavy"
HL = "OEHLoss"
MERGER = "OEPalatalFricativeMerger"

LOCAL = {
    "OEWLossBeforeI": {
        "flock-short": "*e*w*i*d*i",       # Ringe–Taylor p. 259
        "flock-long": "*e*w*i*d*ī",        # ending sensitivity, not a reconstruction
        "flock-lowered": "*e*w*i*d*e",     # ending sensitivity, not a reconstruction
        "flock-no-tail": "*e*w*i*d",       # shorter consonant-final alternative
        "flock-gen": "*e*w*i*d*æ*s",      # protected projection, not an attested w-less cell
        "flock-dat-pl": "*e*w*i*d*u*m",   # protected projection, not an attested w-less cell
        "couch-acc": "*s*t*r*e*w*i*n*ǭ",  # cycle 2 analysis
        "strew-singular": "*s*t*r*e*w*i*d*e",
        "call-prefixed": "*ᶠ*ʝ*e*k*e*w*i*θ",
        "hay-edge": "*ç*e*w*i",
    },
    HL: {
        "strike-i": "*s*l*e*ç*i*θ",
        "strike-e": "*s*l*e*ç*e*θ",
        "strike-accented": "*s*l*é*ç*i*θ",
    },
    MERGER: {
        "inherited-j": "*t*e*j*n",
        "secondary-fricative": "*t*e*ʝ*n",
        "atomic": "*t*ei*n",
        "key": "*k*ǣ*j",
    },
}


def timing(order):
    after = lambda stage: order[order.index(stage) + 1]
    return {
        "after-w": after("OEWLossBeforeI"), "before-hvd": HVD, "after-hvd": after(HVD),
        "before-weak-i": LOWERING, "after-weak-i": AFTER_REDUCTION,
        "before-h": HL, "after-h": after(HL),
        "before-merger": MERGER, "after-merger": after(MERGER),
    }


def variants(order):
    sites = timing(order)
    yield "common", ()
    for mechanism, components in MECHANISMS.items():
        for label, site in sites.items():
            yield f"{label}:{mechanism}", tuple((site, step) for step in components)
    for mechanism in "JN":
        first, second = MECHANISMS[mechanism]
        for a, b in (("after-w", "after-hvd"), ("after-w", "after-h"),
                     ("before-h", "after-h"), ("before-h", "after-merger")):
            if order.index(sites[a]) >= order.index(sites[b]):
                raise RuntimeError(f"Bad serial window order: {a}, {b}")
            yield f"{a}+{b}:{mechanism}", ((sites[a], first), (sites[b], second))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    base = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, base["orders"], "frozen orders")
    verify(run.frozen.sha(source), base["source_sha256"], "frozen source")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay3-chronology-") as work:
        work = Path(work)
        paths = frozen | run.compile_candidates(source, args.stage_cache, work, Components)
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        private = representation_components(source)
        private_paths = frozen | run.compile_candidates(source, args.stage_cache, work, private)
        weight = {}
        for label, ending in (("Sh", "*i"), ("Lt", "")):
            stage = f"{label}OEHighVowelApocope"
            weight[label] = apply(private_paths, ("RpNu", stage, "RpMo"),
                                  {"direct": "*e*i*d*i", "acute": "*é*i*d*i"})
            verify(weight[label]["RpMo"], {"direct": ["*ē*d" + ending],
                                           "acute": ["*ḗ*d" + ending]},
                   f"independent flock nucleus weight {label}")
        for model, order in orders.items():
            records = {}
            for name, changes in variants(order):
                placements = tuple(sorted(common(order) + changes, key=lambda p: order.index(p[0])))
                records[name] = {"placements": placements,
                                 "traces": trial(order, paths, LOCAL, placements)}
            for mechanism in MECHANISMS:
                for timing_label, output in (("before-hvd", "ēd"), ("after-hvd", "ēde")):
                    check = records[f"{timing_label}:{mechanism}"]["traces"]["flock-short"]
                    verify(check["output"], [output], f"{model}/{timing_label}:{mechanism}")
            for mechanism in "JN":
                check = records[f"after-w+after-hvd:{mechanism}"]["traces"]["flock-short"]
                verify(check["output"], ["ēd"], f"{model} early weight suffices/{mechanism}")
            for name in ("flock-long", "flock-lowered"):
                for mechanism in MECHANISMS:
                    check = records[f"before-hvd:{mechanism}"]["traces"][name]
                    verify(check["output"], ["ēde"], f"{model} {name} sensitivity")
            for record in records.values():
                verify(record["traces"]["key"]["output"], ["cǣġ"], f"{model} key preservation")
            models[model] = {"sites": timing(order), "arms": records}
    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": Components.definitions(),
        "local_inputs": LOCAL, "weight_controls": weight,
        "weight_definitions": private.definitions(), "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

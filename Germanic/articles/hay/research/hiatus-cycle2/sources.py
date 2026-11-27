#!/usr/bin/env python3
"""Separate early back-vowel incorporation from later h-loss hiatus."""

import argparse
import json
from pathlib import Path
import tempfile

from matched import apply, rule, trial
from quantity import Components as Quantity
from reproduce_stress import DELETION, run, verify


BACK = "OEAuBrightening"
CLUSTER = "EAFBrighteningUnstressed"
H = "OEHLoss"
AFTER_H = "OEContraction"


class Components:
    extra = {
        "BkWL": "[{*w} -> 0 || EnglishStarShortVowel _ {*u} .#.]",
        "BkNu": ("[{*a} {*u} -> {*au} || _ .#.] .o. "
                 "[{*á} {*u} -> {*áu} || _ .#.] .o. "
                 "[{*e} {*u} -> {*eu} || _ .#.] .o. "
                 "[{*é} {*u} -> {*éu} || _ .#.]"),
        "BkAu": "[{*aeu} -> {*ēa} || _ .#.]",
        "BkCoda": "[{*u} -> {*w} || EnglishStarShortVowel _ .#.]",
        "BkLate": ("[{*a} {*u} -> {*ēa} || _ .#.] .o. "
                   "[{*e} {*u} -> {*ēo} || _ .#.]"),
        "HwRed": "[{*w} -> 0 || {*x} _ EnglishStarVocalic]",
        "HLFront": rule(("e", "i"), ("ē",), ""),
        "HLBack": ("[[{*e}|{*æ}] {*a} -> {*ēa}] .o. "
                   "[[{*é}|{*ǽ}] {*a} -> {*ḗa}]"),
        "HLBroken": ("[[{*eo}|{*ēo}|{*éo}|{*ḗo}] [{*a}|{*æ}] -> {*ēo}] .o. "
                     "[[{*ea}|{*ēa}|{*éa}|{*ḗa}] [{*a}|{*æ}|{*u}] -> {*ēa}]"),
    }
    RULES = (*Quantity.RULES, *extra)

    @classmethod
    def definitions(cls):
        return Quantity.definitions() + "".join(f"define {name} {body};\n"
                                                 for name, body in cls.extra.items())


FULL = {
    "claw": "kláwu", "knee-pl": "knéwō", "tree-pl": "tréwō",
    "claw-oblique": "kláwa", "tree-sg": "tréwą", "knee-sg": "knéwą",
    "see-inf": "séxwaną", "strike-inf": "sláxaną", "draw-inf": "téuxaną",
    "shoe-pl": "skōxōz",
}

LOCAL = {
    BACK: {
        "claw-hiatus": "*k*l*a*u", "tree-hiatus": "*t*r*e*u", "knee-hiatus": "*k*n*e*u",
        "claw-early-nucleus": "*k*l*au", "tree-early-nucleus": "*t*r*eu",
        "knee-early-nucleus": "*k*n*eu", "threat": "*θ*r*a*w*u",
        "few-neut-pl": "*f*a*w*u", "claw-protected": "*k*l*a*w*a",
        "tree-protected": "*t*r*e*w*a*s", "new-ii": "*n*i*w*i",
    },
    H: {
        "river-short": "*e*ç*i", "river-long": "*ḗ*ç*i", "river-nom": "*ea*x*u",
        "river-contracted": "*ēa", "strike-i": "*s*l*e*ç*i*θ",
        "strike-lowered": "*s*l*e*ç*e*θ",
        "see-ws": "*s*eo*x*a*n", "see-angl": "*s*e*x*a*n",
        "draw-ws": "*t*ēo*x*a*n", "draw-subj": "*t*ēo*x*æ",
        "high-angl": "*x*ē*ç*i*r*a", "high-ws": "*x*ēa*x*u*m",
        "shoe-ws": "*ʃ*ēo*x*a*s", "shoe-unbroken": "*ʃ*ō*x*a*s",
        "gain-offglide": "*t*ei*d", "identical-i": "*s*i*ç*i*d",
        "thrive-ws": "*θ*eo*x*a*n", "strike-ws": "*s*l*ea*x*a*n",
    },
}


ARMS = {
    "H0": (),
    "back-diphthong": ((BACK, "BkWL"), (BACK, "BkNu"), ("OEEwLongDiphthong", "BkAu")),
    "back-coda": ((BACK, "BkWL"), (BACK, "BkCoda")),
    "back-late": ((BACK, "BkWL"), ("OEContraction", "BkLate")),
    "cluster": ((CLUSTER, "HwRed"),),
    "cluster-and-contraction": ((CLUSTER, "HwRed"), (AFTER_H, "HLBroken")),
    "h-direct-DN": ((AFTER_H, "DcDN"),),
    "h-glide-DN": ((AFTER_H, "GlDN"), (AFTER_H, "GaDN")),
    "h-nuclear-DN": ((AFTER_H, "NuDN"), (AFTER_H, "NaDN")),
    "h-direct-broad": ((AFTER_H, "HLFront"),),
    "h-absorb": ((AFTER_H, "AbsHigh"),),
    "h-back": ((AFTER_H, "HLBack"),),
    "h-broken": ((AFTER_H, "HLBroken"),),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    base = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, base["orders"], "ordered components")
    verify(run.frozen.sha(source), base["source_sha256"], "frozen source")
    frozen_paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-source-") as directory:
        private = run.compile_candidates(source, args.stage_cache, Path(directory), Components)
        paths = frozen_paths | private | {f"component:{DELETION}": private["component:StFoot"]}
        for model, order in orders.items():
            batches = {order[0]: FULL, **LOCAL}
            models[model] = {arm: {"placements": where, "traces": trial(order, paths, batches, where)}
                             for arm, where in ARMS.items()}
        stages = apply(paths, ("BkWL", "BkNu"), LOCAL[BACK])
        verify(stages["BkWL"]["claw-protected"], [LOCAL[BACK]["claw-protected"]], "retained w")
        verify(stages["BkWL"]["few-neut-pl"], ["*f*a*u"], "independent short back hiatus")
        verify(stages["BkNu"]["threat"], ["*θ*r*au"], "independent incorporated nucleus")
        verify(stages["BkNu"]["tree-hiatus"], ["*t*r*eu"], "e.u differs from a.u")
        verify(models["A"]["H0"]["traces"]["see-inf"]["output"], ["seohwan"], "frozen cluster")
        verify(models["A"]["cluster-and-contraction"]["traces"]["see-inf"]["output"],
               ["sēon"], "separate cluster and contraction requirements")
        verify([models["A"]["back-diphthong"]["traces"][key]["output"]
                for key in ("claw", "knee-pl", "tree-pl", "threat", "few-neut-pl")],
               [["clēa"], ["cnēo"], ["trēo"], ["þrēa"], ["fēa"]],
               "back source and held-out examples")
        for arm in ("h-direct-DN", "h-glide-DN", "h-nuclear-DN"):
            verify(models["A"][arm]["traces"]["strike-i"]["output"], ["slēþ"], arm)
        verify(models["A"]["H0"]["traces"]["strike-lowered"]["output"], ["slēþ"], "identical hiatus")

    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": Components.definitions(),
        "full_inputs": FULL, "local_inputs": LOCAL, "back_components": stages, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

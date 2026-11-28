#!/usr/bin/env python3
"""Separate early incorporation, nuclear realization, and retained labials."""

import argparse
import json
from pathlib import Path
import tempfile

from integrated import Components as Prior, common
from matched import trial
from reproduce_stress import DELETION, run, verify
from sources import BACK


REALIZE = "OEDiphthongLeveling"
PROXY = "OEAwLongDiphthong"
LATE = "OEJLossAfterHeavy"
AFTER_BRIGHTENING = "OEEwLongDiphthong"
ENTRIES = {
    BACK: {
        "three": "*θ*r*i*u", "three-acute": "*θ*r*í*u",
        "front-vowel-hiatus": "*θ*r*i*o",
        "inherited-iu": "*l*iu*d",
        "atomic-iu": "*t*iu", "atomic-iu-acute": "*t*íu",
        "atomic-eu": "*t*eu", "atomic-eu-acute": "*t*éu",
        "atomic-au": "*t*au", "atomic-au-acute": "*t*áu",
        "claw-direct": "*k*l*a*w*u", "claw-acc": "*k*l*a*w*e",
        "claw-acc-early": "*k*l*a*w*a", "claw-gen": "*k*l*a*w*æ",
        "claw-dat-pl": "*k*l*a*w*u*m",
        "claw-dat-pl-levelled": "*k*l*au*m",
        "knee-direct-pl": "*k*n*e*w*u", "tree-direct-pl": "*t*r*e*w*u",
        "knee-gen-sg": "*k*n*e*w*e*s", "tree-gen-sg": "*t*r*e*w*e*s",
        "knee-dat-pl": "*k*n*e*w*u*m", "tree-dat-pl": "*t*r*e*w*u*m",
        "knee-acc-pl-north": "*k*n*e*w*a", "claw-long": "*k*l*ā*w*u",
    },
    AFTER_BRIGHTENING: {
        "transient-aeu": "*t*aeu", "transient-aeu-acute": "*t*áeu",
        "transient-aeu-closed": "*t*aeu*m",
    },
    LATE: {
        "claw-remodelled": "*k*l*a*w*u",
        "claw-remodelled-pl": "*k*l*a*w*a",
        "knee-remodelled": "*k*n*ēo*w*u",
        "tree-remodelled": "*t*r*ēo*w*u",
    },
}
VARIANTS = {
    "common": (),
    "incorporation-only": ((BACK, "BkIu"),),
    "realization-only": ((REALIZE, "BkIo"),),
    "incorporation-and-realization": ((BACK, "BkIu"), (REALIZE, "BkIo")),
    "transient-bridge": ((AFTER_BRIGHTENING, "BkAe"),),
    "closed-um": ((BACK, "BkWm"), (BACK, "BkNm"), (AFTER_BRIGHTENING, "BkAe")),
}


class Components:
    definitions_by_name = {
        "BkIu": ("[{*i} {*u} -> {*iu} || _ .#.] .o. "
                 "[{*í} {*u} -> {*íu} || _ .#.]"),
        "BkIo": "[[{*iu}|{*íu}] -> {*īo}]",
        "BkAe": "[{*aeu} -> {*ēa}, {*áeu} -> {*ḗa}]",
        "BkWm": "[{*w} -> 0 || EnglishStarShortVowel _ {*u} {*m} .#.]",
        "BkNm": ("[{*a} {*u} -> {*au} || _ {*m} .#.] .o. "
                 "[{*á} {*u} -> {*áu} || _ {*m} .#.] .o. "
                 "[{*e} {*u} -> {*eu} || _ {*m} .#.] .o. "
                 "[{*é} {*u} -> {*éu} || _ {*m} .#.]"),
        "BkRt": ("[{*æ} -> {*a}, {*ǽ} -> {*á} || _ {*w} EnglishStarVocalic]"),
        "BkId": "?*",
    }
    RULES = (*Prior.RULES, *definitions_by_name)

    @classmethod
    def definitions(cls):
        return Prior.definitions() + "".join(
            f"define {key} {body};\n" for key, body in cls.definitions_by_name.items())


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
    with tempfile.TemporaryDirectory(prefix="hay3-back-vowels-") as work:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(work), Components)
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        for model, order in orders.items():
            records = {}
            for name, additions in VARIANTS.items():
                sites = tuple(sorted(common(order) + additions, key=lambda p: order.index(p[0])))
                records[name] = trial(order, paths, ENTRIES, sites)
            no_proxy = paths | {f"component:{PROXY}": paths["component:BkId"]}
            records["no-aw-proxy"] = trial(order, no_proxy, ENTRIES, common(order))
            sites = tuple(sorted(common(order) + (("OEBreaking", "BkRt"),),
                                 key=lambda p: order.index(p[0])))
            records["no-aw-proxy+retraction"] = trial(order, no_proxy, ENTRIES, sites)
            verify(records["common"]["three"]["output"], ["þreo"], f"{model} frozen mismatch")
            verify(records["incorporation-and-realization"]["three"]["output"], ["þrīo"],
                   f"{model} source-oriented realization")
            if model == "canonical":
                verify(records["no-aw-proxy"]["claw-acc"]["output"], ["clæwe"],
                       "canonical oblique without long-aw proxy")
                verify(records["no-aw-proxy+retraction"]["claw-acc"]["output"], ["clawe"],
                       "canonical oblique with ordinary pre-w retraction")
            verify(records["transient-bridge"]["transient-aeu-closed"]["output"], ["tēam"],
                   f"{model} closed transient bridges before alphabet filter")
            verify(records["closed-um"]["claw-dat-pl"]["output"], ["clēam"],
                   f"{model} closed-u contraction in the dative plural")
            for key, target in (("claw-direct", "clēa"), ("knee-direct-pl", "cnēo"),
                                ("tree-direct-pl", "trēo")):
                for name, record in records.items():
                    verify(record[key]["output"], [target], f"{model}/{name} {key}")
            models[model] = records
    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": Components.definitions(),
        "entries": ENTRIES, "placements": VARIANTS, "bypassed_stage": PROXY, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

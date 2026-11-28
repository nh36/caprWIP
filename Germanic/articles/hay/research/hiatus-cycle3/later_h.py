#!/usr/bin/env python3
"""Replay regional and grammatical h-loss inputs without changing production rules."""

import argparse
import json
from pathlib import Path
import tempfile

from integrated import Components as Prior, MECHANISMS, common
from matched import trial
from reproduce_stress import DELETION, run, verify
from sources import AFTER_H, CLUSTER, H


LOCAL = {
    CLUSTER: {"see-full": "séxwaną", "draw-full": "téuxaną"},
    H: {
        "see-ws": "*s*eo*x*a*n", "see-anglian": "*s*e*x*a*n",
        "see-ws-subj": "*s*eo*x*æ", "see-anglian-subj": "*s*e*ç*e",
        "draw-inf": "*t*ēo*x*a*n", "draw-subj": "*t*ēo*x*æ",
        "strike-ws-inf": "*s*l*ea*x*a*n", "strike-anglian-inf": "*s*l*æ*x*a*n",
        "strike-raised": "*s*l*e*ç*i*θ", "strike-lowered": "*s*l*e*ç*e*θ",
        "wealth-dative": "*f*eo*x*e", "wealth-acute": "*f*éo*x*e",
        "wealth-final-h": "*f*eo*x", "wealth-smoothed": "*f*e*ç*e",
        "wealth-shared-front": "*s*ēo*x*e",
        "river-direct": "*ea*x*u", "river-oblique-short": "*e*ç*i",
        "river-oblique-long": "*ḗ*ç*i", "river-oblique-ie": "*īe*ç*i",
        "river-oblique-remodelled": "*ēa", "river-dat-pl": "*ea*x*u*m",
        "fringe": "*w*l*ō*x*u*m", "clay": "*θ*ō*x*e",
        "high-weak": "*x*ēa*x*a*n",
        "postconsonantal": "*f*eo*r*x*e", "postconsonantal-positive": "*f*eo*r*e",
        "identical-short-i": "*s*i*ç*i*d", "identical-short-e": "*t*e*ç*e*d",
        "identical-acute-i": "*s*í*ç*i*d", "identical-short-back": "*t*a*x*a*n",
    },
}


class Components:
    extra = {
        "HbFront": ("[[{*eo}|{*ēo}] {*e} -> {*ēo}] .o. "
                    "[[{*éo}|{*ḗo}] {*e} -> {*ḗo}]"),
        "HbPost": "[[{*x}|{*ç}] -> 0 || {*r} _ EnglishStarVocalic]",
        "HbIden": "[{*é} {*e} -> {*ḗ}, {*í} {*i} -> {*ḯ}]",
        "HbOU": "[{*ō} {*u} -> {*ō}]",
    }
    RULES = (*Prior.RULES, *extra)

    @classmethod
    def definitions(cls):
        return Prior.definitions() + "".join(f"define {key} {body};\n"
                                             for key, body in cls.extra.items())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    base = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(run.frozen.sha(source), base["source_sha256"], "frozen source")
    verify(orders, base["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay3-later-h-") as work:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(work), Components)
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        for model, order in orders.items():
            entries = {start: batch for start, batch in LOCAL.items() if start != CLUSTER}
            entries[order[0]] = LOCAL[CLUSTER] | {
                "whale": "xwálaz", "while": "xwīlō", "whine": "xwīnaną",
                "who": "xwáz", "where": "xwār",
            }
            variants = {
                "common": common(order),
                "without-hw-reduction": tuple(pair for pair in common(order) if pair[1] != "HwMed"),
                "broken-front": common(order) + ((AFTER_H, "HbFront"),),
                "no-post-lengthening": common(order) + ((H, "HbPost"),),
                "marked-identicals": common(order) + ((AFTER_H, "HbIden"),),
                "unattested-fringe": common(order) + ((AFTER_H, "HbOU"),),
            }
            for kind, rules in MECHANISMS.items():
                repeat = tuple((AFTER_H, rule) for rule in rules)
                edge = {"D": "DcEd", "J": "GlEd", "N": "NuEd"}[kind]
                variants[kind] = common(order) + repeat
                variants[f"{kind}-edge"] = common(order) + repeat + ((AFTER_H, edge),)
            records = {}
            for name, changes in variants.items():
                sites = tuple(sorted(changes, key=lambda pair: order.index(pair[0])))
                records[name] = {"placements": sites, "traces": trial(order, paths, entries, sites)}
            def out(arm, key):
                return records[arm]["traces"][key]["output"]

            verify(out("broken-front", "wealth-dative"), ["fēo"], f"{model} front broken positive")
            verify(out("broken-front", "wealth-final-h"), out("common", "wealth-final-h"),
                   f"{model} protective final h")
            verify(out("no-post-lengthening", "postconsonantal"), ["feore"],
                   f"{model} short root after postconsonantal loss")
            for key in ("whale", "while", "whine", "who", "where"):
                check = out("common", key)
                if not check or not all(text.startswith("hw") for text in check):
                    raise RuntimeError(f"{model}/{key} must exercise initial hw: {check!r}")
                verify(check, out("without-hw-reduction", key), f"{model}/{key} preserved")
            for arm in "DJN":
                verify(out(arm, "strike-raised"), ["slēþ"], f"{model}/{arm} short post-h hiatus")
            models[model] = records
    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": Components.definitions(),
        "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

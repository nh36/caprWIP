"""Replay distinct SC086 proposals without a common contraction overlay."""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import trial
from audit import audit_delta, corpus_run


SITE = "OEContraction"
ENTRIES = {
    "OEHLoss": {
        "flee-subj": "*f*l*ēo*x*æ", "flee-pl": "*f*l*ēo*x*a*θ",
        "pupil-direct": "*s*eo*x*æ", "pupil-acc": "*s*eo*x*a*n",
        "wealth": "*f*eo*x*e", "wealth-acute": "*f*éo*x*e",
        "wealth-final": "*f*eo*x", "wealth-postconsonantal": "*f*eo*r*x*e",
        "see-ws": "*s*eo*x*æ", "see-anglian": "*s*e*ç*æ",
        "clay-source": "*θ*ō*x*æ", "clay-lowered-proxy": "*θ*ō*x*e",
        "cover-long": "*w*r*ī*ç*i*θ*i", "cover-short-sensitivity": "*w*r*i*ç*i*θ*i",
        "receive-rounded": "*f*œ̄*ç*i*θ*i", "receive-unrounded-proxy": "*f*ē*ç*i*θ*i",
        "rug-front": "*r*ȳ*ç*ǣ", "rug-back": "*r*ȳ*x*a*n", "toe": "*t*ā*x*æ",
        "hostile": "*f*ā*x*æ", "trough": "*θ*r*ū*x*u*m", "fringe": "*w*l*ō*x*u*m",
        "catch-inf": "*f*ō*x*a*n", "catch-imperative": "*f*ō*x",
        "catch-ptc": "*f*ō*x*e*n*d*e", "strike-unlike": "*s*l*e*ç*i*θ",
        "draw-acute": "*t*éo*x*a*n", "high-weak": "*x*ēa*x*a*n",
        "identical-short-e": "*t*e*ç*e*d", "identical-acute-e": "*t*é*ç*e*d",
        "identical-short-i": "*s*i*ç*i*d", "identical-acute-i": "*s*í*ç*i*d",
        "river-long-control": "*ē*ç*i",
    },
    "OEWLossBeforeI": {"betray-exact-tail": "*l*ē*w*i*d*ǣ", "betray-lowered": "*l*ē*w*i*d*e",
                      "strew-retained": "*s*t*r*æ*w*i*d*ǣ"},
    SITE: {"unsupported-rounded-after-loss": "*f*œ̄*i*θ", "long-inherited-j": "*k*ǣ*j",
           "acute-broken-front": "*s*éo*æ", "short-unlike": "*t*e*i*d"},
}


class SC086:
    rules = {
        "CtBrAe": ("[[{*eo}|{*ēo}] {*æ} -> {*ēo}] .o. "
                   "[[{*éo}|{*ḗo}] {*æ} -> {*ḗo}]"),
        "CtBrE": ("[[{*eo}|{*ēo}] {*e} -> {*ēo}] .o. "
                  "[[{*éo}|{*ḗo}] {*e} -> {*ḗo}]"),
        "CtBrA": ("[[{*éo}|{*ḗo}] {*a} -> {*ḗo}] .o. "
                  "[[{*éa}|{*ḗa}] {*a} -> {*ḗa}]"),
        "CtHigh": "[{*i} -> 0 || [EnglishStarLongVowel | EnglishStarLongDiphthong] _]",
        "CtId": "[{*é} {*e} -> {*ḗ}, {*í} {*i} -> {*ḯ}]",
    }
    RULES = tuple(rules)

    @classmethod
    def definitions(cls):
        return "".join(f"define {name} {body};\n" for name, body in cls.rules.items())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    baseline = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(digest(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="capr-sc086-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, SC086, runtime)
        candidate = paths | build.verify()
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in rows),
                   Counter(archived=394, active=396), f"{model} panel populations")
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            control = corpus_run(order, paths, inputs, ())
            verify({key: row["output"] for key, row in control.items()},
                   {key: row["output"] for key, row in rows.items()}, f"{model} archived endpoints")
            frozen = trial(order, paths, ENTRIES, ())
            verify(frozen["betray-exact-tail"]["output"], ["lēde"], f"{model} existing exact path")
            verify(frozen["receive-rounded"]["output"], [], f"{model} admission gap")
            arms = {}
            for name in SC086.RULES:
                placements = ((SITE, name),)
                wide = corpus_run(order, candidate, inputs, placements)
                local = trial(order, candidate, ENTRIES, placements)
                for key in ("wealth-final", "wealth-postconsonantal", "catch-imperative",
                            "fringe", "long-inherited-j", "short-unlike", "strew-retained"):
                    verify(local[key]["output"], frozen[key]["output"], f"{model} {name} retains {key}")
                arms[name] = {"wide": audit_delta(wide, control), "local": local}
            for arm, expected in {
                "CtBrAe": {"flee-subj": "flēo", "pupil-direct": "sēo", "see-ws": "sēo"},
                "CtBrE": {"wealth": "fēo", "wealth-acute": "fēo"},
                "CtId": {"identical-acute-e": "tēd", "identical-acute-i": "sīd"},
            }.items():
                for key, value in expected.items():
                    verify(arms[arm]["local"][key]["output"], [value], f"{model} {arm} {key}")
            models[model] = {"frozen_local": frozen, "arms": arms}
        incumbent = re.search(r"^define OEContraction \[.*?^];",
                              source.read_text(encoding="utf-8"), re.S | re.M).group()
        print(json.dumps({
            "base": run.BASE, "orders": orders, "source_sha256": digest(source),
            "archive_sha256": digest(archive_path), "runner_sha256": digest(Path(__file__)),
            "incumbent": incumbent, "definitions": SC086.definitions(), "component": build.receipt(),
            "frozen_exports": {key: digest(path) for key, path in paths.items()}, "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

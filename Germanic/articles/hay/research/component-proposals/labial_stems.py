"""Replay distinct labial-loss, nuclear and protected-stem hypotheses."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import trial
from sources import Components as Previous


SITE = "OEAuBrightening"
ENTRIES = {
    SITE: {
        "claw-short-direct": "*k*l*a*w*u",
        "claw-long-direct": "*k*l*ā*w*u",
        "claw-long-after-loss": "*k*l*ā*u",
        "claw-atomic-au": "*k*l*au",
        "claw-short-oblique": "*k*l*a*w*a",
        "claw-long-oblique": "*k*l*ā*w*ā",
        "knee-pl": "*k*n*e*w*u",
        "knee-sg-vocalized": "*k*n*e*u",
        "knee-protected": "*k*n*e*w*a",
        "tree-pl": "*t*r*e*w*u",
        "tree-sg-vocalized": "*t*r*e*u",
        "tree-protected": "*t*r*e*w*u*m",
        "threat-direct": "*θ*r*a*w*u",
        "threat-protected": "*θ*r*a*w*ā",
        "few-direct": "*f*a*w*u",
        "few-dative-sensitivity": "*f*a*w*u*m",
        "straw-vocalized": "*s*t*r*a*u",
        "servant-vocalized": "*θ*e*u",
        "servant-protected": "*θ*e*w*e",
        "negative-long-retention": "*s*ā*w*a",
        "negative-front-tail": "*n*i*w*i",
        "negative-closed-tail": "*s*ā*w*u*m",
    },
    "OldEnglishOrthography": {"claw-rebuilt-surface": "*k*l*a*w*u"},
}
SHORT = ((SITE, "BkWL"), (SITE, "BkNu"), ("OEEwLongDiphthong", "BkAu"))
ARMS = {
    "frozen": (),
    "short": SHORT,
    "short-plus-long-loss": ((SITE, "LongWL"), *SHORT),
    "short-plus-long-loss-and-merge": ((SITE, "LongWL"), (SITE, "LongAu"), *SHORT),
}


class Labial:
    rules = {key: Previous.extra[key] for key in ("BkWL", "BkNu", "BkAu")}
    rules.update({
        "LongWL": "[{*w} -> 0 || [{*ā}|{*à}] _ {*u} .#.]",
        "LongAu": ("[{*ā} {*u} -> {*au} || _ .#.] .o. "
                   "[{*à} {*u} -> {*áu} || _ .#.]"),
    })
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
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(digest(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="capr-labial-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Labial, runtime)
        paths = frozen | build.verify()
        for model, order in orders.items():
            arms = {name: trial(order, paths, ENTRIES, placements)
                    for name, placements in ARMS.items()}
            for name in ARMS:
                for key in ("claw-long-oblique", "negative-long-retention",
                            "negative-front-tail", "negative-closed-tail"):
                    verify(arms[name][key]["changes"], arms["frozen"][key]["changes"],
                           f"{model} {name} protected {key}")
            verify(arms["short"]["claw-short-direct"]["output"], ["clēa"], model)
            verify(arms["short-plus-long-loss"]["claw-long-direct"]["anchors"]
                   ["LongWL"], [["*k*l*ā*w*u"], ["*k*l*ā*u"]], model)
            verify(arms["short-plus-long-loss-and-merge"]["claw-long-direct"]["output"],
                   ["clēa"], model)
            models[model] = arms
        print(json.dumps({
            "base": run.BASE, "orders": orders, "inputs": ENTRIES, "placements": ARMS,
            "source_sha256": digest(source), "runner_sha256": digest(Path(__file__)),
            "frozen_exports": {key: digest(value) for key, value in frozen.items()},
            "definitions": Labial.definitions(), "build": build.receipt(), "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

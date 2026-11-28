"""Separate incorporation, early realization, and a late merger projection."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import trial


SITE = "OEDiphthongLeveling"
LATE = "OldEnglishOrthography"
ENTRIES = {
    SITE: {
        "three-edge": "*θ*r*i*u",
        "three-edge-acute": "*θ*r*í*u",
        "three-nuclear": "*θ*r*iu",
        "friend": "*f*r*iu*n*d",
        "devil": "*d*iu*b*u*l",
        "she": "*x*iu",
        "your": "*iu*w*a*r",
        "deep": "*d*eu*p",
        "thief": "*θ*eu*b",
        "tree-after-w-loss": "*t*r*eu",
        "three-unrelated-io-hiatus": "*θ*r*i*o",
        "recipient-i-u-nonfinal": "*f*r*i*u*n*d",
        "preexisting-io": "*l*īo*d",
        "preexisting-eo": "*l*ēo*d",
    }
}
ARMS = {
    "frozen": (),
    "incorporation-only": ((SITE, "IuEdge"),),
    "realization-only": ((SITE, "IuHigh"),),
    "incorporation-and-realization": ((SITE, "IuEdge"), (SITE, "IuHigh")),
    "early-then-late-merger": ((SITE, "IuEdge"), (SITE, "IuHigh"), (LATE, "IoLate")),
}


class Nuclei:
    rules = {
        "IuEdge": ("[{*i} {*u} -> {*iu} || _ .#.] .o. "
                   "[{*í} {*u} -> {*íu} || _ .#.]"),
        "IuHigh": "[[{*iu}|{*íu}] -> {*īo}]",
        "IoLate": "[{*īo} -> {*ēo}]",
    }
    RULES = tuple(rules)

    @classmethod
    def definitions(cls):
        return "".join(f"define {key} {body};\n" for key, body in cls.rules.items())


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
    with tempfile.TemporaryDirectory(prefix="capr-early-nuclei-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Nuclei, runtime)
        paths = frozen | build.verify()
        for model, order in orders.items():
            arms = {name: trial(order, paths, ENTRIES, placements)
                    for name, placements in ARMS.items()}
            for name in arms:
                for key in ("deep", "thief", "tree-after-w-loss",
                            "three-unrelated-io-hiatus", "recipient-i-u-nonfinal",
                            "preexisting-eo"):
                    verify(arms[name][key]["changes"], arms["frozen"][key]["changes"],
                           f"{model} {name} control {key}")
            high = arms["incorporation-and-realization"]
            late = arms["early-then-late-merger"]
            for key, before, after in (
                ("three-edge", "þrīo", "þrēo"), ("friend", "frīond", "frēond"),
                ("preexisting-io", "līod", "lēod"),
            ):
                verify(high[key]["output"], [before], f"{model} early {key}")
                verify(late[key]["output"], [after], f"{model} late {key}")
            models[model] = arms
        print(json.dumps({
            "base": run.BASE, "orders": orders, "inputs": ENTRIES, "placements": ARMS,
            "source_sha256": digest(source), "runner_sha256": digest(Path(__file__)),
            "frozen_exports": {key: digest(value) for key, value in frozen.items()},
            "definitions": Nuclei.definitions(), "build": build.receipt(), "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

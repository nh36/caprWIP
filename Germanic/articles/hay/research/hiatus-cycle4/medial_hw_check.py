"""Replay source-distinct labiovelar families without scoring validation data."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import apply, trial
from sources import CLUSTER


class Hw:
    RULES = ("HwMed", "HwRed")

    @staticmethod
    def definitions():
        return (
            "define HwMed [{*w} -> 0 || EnglishStarVocalic {*x} _ EnglishStarVocalic];\n"
            "define HwRed [{*w} -> 0 || {*x} _ EnglishStarVocalic];"
        )


FULL = {"see-inf": "séxwaną", "lend-inf": "līxwaną",
        "filter-inf": "sīxwaną", "white": "xwītaz", "turn-inf": "xwérβaną"}
LOCAL = {"see-PWGmc": "*s*é*x*w*a*n", "lend-PWGmc": "*l*ī*x*w*a*n",
         "filter-PWGmc": "*s*ī*x*w*a*n", "sieve-PWGmc": "*s*i*x*x*w*ā",
         "filtered-voiced": "*s*i*w*æ*n", "horse-preOE": "*e*x*w",
         "white-PWGmc": "*x*w*ī*t", "turn-PWGmc": "*x*w*e*r*b*a*n"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    baseline = json.loads((run.HERE / "baseline.json").read_text())
    verify(digest(source), baseline["source_sha256"], "frozen source")
    orders = {"canonical": canonical, **alternatives}
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    with tempfile.TemporaryDirectory(prefix="hay4-hw-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Hw, runtime)
        paths = frozen | build.verify()
        narrow = apply(paths, ("HwMed",), LOCAL)["HwMed"]
        verify(narrow, {key: [form.replace("*x*w", "*x") if key in
                              {"see-PWGmc", "lend-PWGmc", "filter-PWGmc"} else form]
                        for key, form in LOCAL.items()}, "medial singleton-only scope")
        broad = apply(paths, ("HwRed",), LOCAL)["HwRed"]
        for key in ("sieve-PWGmc", "white-PWGmc"):
            verify(broad[key], [LOCAL[key].replace("*x*w", "*x")],
                   f"broad reduction touches {key} outside the singleton domain")
        models = {}
        for model, order in orders.items():
            cases = {order[0]: FULL, CLUSTER: LOCAL}
            control = trial(order, paths, cases, ())
            test = trial(order, paths, cases, ((CLUSTER, "HwMed"),))
            for key in ("white", "turn-PWGmc"):
                before, after = test[key]["anchors"]["HwMed"]
                if not before:
                    raise RuntimeError(f"{model} initial negative {key} did not reach HwMed")
                verify(after, before, f"{model} initial negative {key}")
            for key, output in (("see-inf", "seoan"), ("lend-inf", "līoan"),
                                ("filter-inf", "sīoan")):
                before, after = test[key]["anchors"]["HwMed"]
                verify(after, [before[0].replace("*x*w", "*x")], f"{model} live reduction {key}")
                before, after = test[key]["anchors"]["OEHLoss"]
                verify(after, [before[0].replace("*x", "")], f"{model} fed h-loss {key}")
                verify(test[key]["output"], [output], f"{model} residual realization gap")
            models[model] = {"frozen": control, "narrow": test}
        print(json.dumps({"base": run.BASE, "orders": orders, "source_sha256": digest(source),
                          "runner_sha256": digest(Path(__file__)), "components": build.receipt(),
                          "definitions": Hw.definitions(), "local": {"narrow": narrow, "broad": broad},
                          "models": models}, ensure_ascii=False))


if __name__ == "__main__":
    main()

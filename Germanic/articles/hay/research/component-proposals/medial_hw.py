"""Isolate singleton and geminate medial delabialization."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import trial
from audit import audit_delta, corpus_run


SITE = "EAFBrighteningUnstressed"
FULL = {"see-inf": "séxwaną", "lend-inf": "līxwaną", "filter-inf": "sīxwaną",
        "white-full": "xwītaz", "turn-full": "xwérβaną"}
LOCAL = {"see": "*s*é*x*w*a*n", "lend": "*l*ī*x*w*a*n", "filter": "*s*ī*x*w*a*n",
         "sieve": "*s*i*x*x*w*ā", "arrange": "*t*i*x*x*ō*n", "drain": "*s*i*x*t*r*ō",
         "filtered-voiced": "*s*i*w*æ*n", "horse-edge-proxy": "*e*x*w",
         "horse-direct": "*e*x*u", "white": "*x*w*ī*t", "turn": "*x*w*e*r*b*a*n"}


class Hw:
    RULES = ("HwMed", "HwGem")

    @staticmethod
    def definitions():
        return (
            "define HwMed [{*w} -> 0 || EnglishStarVocalic {*x} _ EnglishStarVocalic];\n"
            "define HwGem [{*w} -> 0 || EnglishStarVocalic {*x} {*x} _ EnglishStarVocalic];\n"
        )


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
    with tempfile.TemporaryDirectory(prefix="capr-medial-hw-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Hw, runtime)
        candidate = paths | build.verify()
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in rows),
                   Counter(archived=394, active=396), f"{model} panel populations")
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            control = corpus_run(order, paths, inputs, ())
            verify({key: row["output"] for key, row in control.items()},
                   {key: row["output"] for key, row in rows.items()}, f"{model} archived endpoints")
            entries = {order[0]: FULL, SITE: LOCAL}
            arms = {"frozen": {"local": trial(order, paths, entries, ())}}
            for name, enabled in (("singleton", ("HwMed",)), ("geminate", ("HwGem",)),
                                  ("both", Hw.RULES)):
                placements = tuple((SITE, rule) for rule in enabled)
                wide = corpus_run(order, candidate, inputs, placements)
                local = trial(order, candidate, entries, placements)
                for component in enabled:
                    hits = {key for key, row in local.items()
                            if row["anchors"][component][0] != row["anchors"][component][1]}
                    expected = {"sieve"} if component == "HwGem" else {
                        "see", "lend", "filter", "see-inf", "lend-inf", "filter-inf"}
                    verify(hits, expected, f"{model} {component} local firing domain")
                if "HwGem" in enabled:
                    entering, leaving = local["sieve"]["anchors"]["OEHLoss"]
                    verify(leaving, entering, f"{model} geminate survives h-loss")
                    verify(local["sieve"]["anchors"]["HwGem"][1], ["*s*i*x*x*ā"],
                           f"{model} delabialization is not shortening")
                arms[name] = {"wide": audit_delta(wide, control), "local": local}
            models[model] = arms
        print(json.dumps({
            "base": run.BASE, "orders": orders, "source_sha256": digest(source),
            "archive_sha256": digest(archive_path), "runner_sha256": digest(Path(__file__)),
            "definitions": Hw.definitions(), "component": build.receipt(), "site": SITE,
            "frozen_exports": {key: digest(path) for key, path in paths.items()}, "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

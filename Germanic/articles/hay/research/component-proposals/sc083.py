"""Compile only the SC083 foot guard, then replay each frozen order."""

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
from reproduce_stress import DELETION
from stress_repairs import FOOT_DEFINITION


class SC083:
    RULES = ("StFoot",)

    @staticmethod
    def definitions():
        return FOOT_DEFINITION


def outputs(rows):
    return {key: value["output"] for key, value in rows.items()}


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
    verify(digest(source), baseline["source_sha256"], "frozen source")
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, baseline["orders"], "frozen orders")
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    cycle2 = args.snapshot / "Germanic/articles/hay/research/hiatus-cycle2"
    prior = json.loads((cycle2 / "stress-census.json").read_text(encoding="utf-8"))
    historical = {row["id"]: row["input"] for row in run.dsv(cycle2 / "stress-panel.tsv")
                  if row["entry"] == "full"}
    panel_file = Path(__file__).with_name("sc083-panel.tsv")
    panel = run.dsv(panel_file)
    verify(len({row["id"] for row in panel}), len(panel), "regression IDs")
    models = {}
    with tempfile.TemporaryDirectory(prefix="capr-sc083-proposal-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, SC083, runtime)
        guarded = paths | {f"component:{DELETION}": build.verify()["component:StFoot"]}
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in rows),
                   Counter(archived=394, active=396), f"{model} panel populations")
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            before = run.evaluate(order, paths, inputs, {DELETION})
            after = run.evaluate(order, guarded, inputs, {DELETION})
            verify(outputs(before), outputs(rows), f"{model} archived endpoints")
            firings = {
                key: {"input": row["input"], "before": entering, "S0": original, "S1": updated}
                for key, row in before.items()
                for entering, original in [row["anchors"][DELETION]]
                for candidate_in, updated in [after[key]["anchors"][DELETION]]
                if entering != original or candidate_in != updated
            }
            verify(firings, {key: {k: v for k, v in row.items() if k != "concept"}
                             for key, row in prior["models"][model]["firings"].items()},
                   f"{model} inherited firing census")
            wide_delta = {key: {"incumbent": row, "candidate": after[key]}
                          for key, row in before.items() if row != after[key]}
            entries = {order[0]: dict(historical), DELETION: {}}
            for row in panel:
                entries[order[0] if row["entry"] == "full" else DELETION][row["id"]] = row["input"]
            control = trial(order, paths, entries, ())
            candidate = trial(order, guarded, entries, ())
            for key, result in {
                "first-foot-head": "*ᶠ*ʝ*e*k*e*i*d",
                "love-local": "*l*u*b*i*a*n",
                "liccian-local": "*l*i*k*k*i*a*n",
                "stressed-prefix": "*ʝ*é*k*i*d",
                "multiple-weak": "*ᶠ*ʝ*e*k*é*t*i*d*i*n",
                "secondary-marked": "*w*í*r*l*è*i*d",
                "secondary-decoded": "*w*í*r*l*i*d",
                "two-pretonics-decoded": "*ʝ*e*k*a*t*i*d",
                "simplex-head": "*k*e*i*d",
            }.items():
                verify(candidate[key]["anchors"][DELETION][1], [result], f"{model} {key}")
            for key in ("believe", "world", "call-simplex"):
                verify(candidate[key], control[key], f"{model} {key} unchanged")
            for key, suffix in (("call-present", "þ"), ("call-participle", "d")):
                verify(candidate[key]["output"], [f"ġecei{suffix}"] if model != "canonical"
                       else control[key]["output"], f"{model} {key}")
            models[model] = {"panel_size": len(rows), "firings": firings, "wide_delta": wide_delta,
                             "regression": {"incumbent": control, "candidate": candidate}}
        incumbent = re.search(rf"^define {DELETION} \[.*?^];",
                              source.read_text(), re.M | re.S).group()
        print(json.dumps({
            "base": run.BASE, "orders": orders, "source_sha256": digest(source),
            "archive_sha256": digest(archive_path), "runner_sha256": digest(Path(__file__)),
            "prior_sha256": digest(cycle2 / "stress-census.json"), "panel_sha256": digest(panel_file),
            "historical_panel_sha256": digest(cycle2 / "stress-panel.tsv"),
            "incumbent": incumbent, "candidate": SC083.definitions(),
            "component": build.receipt(), "frozen_exports": {key: digest(path) for key, path in paths.items()},
            "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

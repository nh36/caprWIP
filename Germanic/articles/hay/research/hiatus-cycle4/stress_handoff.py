"""Test a bounded foot-marker handoff across frozen h-loss."""

import argparse
import gzip
import json
from pathlib import Path
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import trial
from reproduce_stress import DELETION
from stress_repairs import FOOT_DEFINITION, valid


HL = "OEHLoss"
CONTRACTION = "OEContraction"
WORLD_STAGE = "OEMedUnstressedULowering"


class Stress:
    RULES = ("StFoot", "StKeepH", "StStrip", "StLateCon", "StLateGl", "StLateNu",
             "StPrint", "StBadLift")

    @staticmethod
    def definitions():
        return "\n".join((
            FOOT_DEFINITION,
            run.candidates.PREFIX,
            "define StKeepH FootCtx([[{*x}|{*ç}] -> 0 || EnglishStarVocalic _ EnglishStarVocalic]);",
            "define StStrip [{*ᶠ} -> 0];",
            "define StLateCon " + run.candidates.rewrite("ei", "ē") + ";",
            "define StLateGl " + run.candidates.rewrite("ei", "ej") + ";",
            "define StLateNu [{*e} {*i} -> {*ei} || HiHeadContext _] .o. [{*é} {*i} -> {*ei}];",
            "define StPrint [{*ei} -> {*e} {*i}];",
            f"define StBadLift [{WORLD_STAGE} / [{{*⌃}}|{{*⌄}}]];",
        ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    baseline = json.loads((run.HERE / "baseline.json").read_text())
    verify(digest(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    cycle2 = args.snapshot / "Germanic/articles/hay/research/hiatus-cycle2"
    census = json.loads((cycle2 / "stress-census.json").read_text())
    with gzip.open(cycle2 / "stress-repairs.json.gz", "rt") as old:
        repairs = json.load(old)
    panel = {r["id"]: r["input"] for r in run.dsv(cycle2 / "stress-panel.tsv")
             if r["entry"] == "full"}
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay4-stress-handoff-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Stress, runtime)
        paths = frozen | build.verify()
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        kept = paths | {f"component:{HL}": paths["component:StKeepH"]}
        for model, order in orders.items():
            earlier = repairs["models"][model]["S2"]["world"]
            state = next(forms for stage, forms in earlier["changes"] if stage == "OEBackMutation")
            broken = run.frozen.apply_stage(paths["component:StBadLift"], {"world": state})["world"]
            verify(broken, earlier["issues"][0][2], f"{model} exact S2 world drift")
            verify([form for form in broken if valid(form, ["*⌃", "*⌄"])], [],
                   f"{model} S2 world has no valid alignment")
            weak = census["models"][model]["firings"]
            entries = {order[0]: panel | {key: r["input"] for key, r in weak.items()},
                       HL: {"palatal-loss": "*s*l*e*ç*i*θ",
                            "late-root": "*ᶠ*ʝ*e*k*e*i*d",
                            "late-weak": "*ᶠ*ʝ*e*k*a*t*e*i*d"}}
            control = trial(order, paths, entries, ())
            retained = trial(order, kept, entries, ((CONTRACTION, "StStrip"),))
            verify({key: row["output"] for key, row in retained.items()},
                   {key: row["output"] for key, row in control.items()}, f"{model} no-op handoff")
            verify(retained["world"]["output"], ["weorold"], f"{model} compound control")
            verify(retained["palatal-loss"]["anchors"][HL][1], ["*s*l*e*i*θ"],
                   f"{model} live deletion")
            for key, row in weak.items():
                verify(retained[key]["anchors"][DELETION], [row["before"], row["S1"]],
                       f"{model} archived weak reduction {key}")
            late = {}
            for mode, output in (("Con", "*ē"), ("Gl", "*e*j"), ("Nu", "*ei")):
                steps = ((CONTRACTION, f"StLate{mode}"), (CONTRACTION, "StStrip"))
                if mode == "Nu":
                    steps += (("OldEnglishOrthography", "StPrint"),)
                late[mode] = trial(order, kept, entries, steps)
                late_state = late[mode]["late-root"]["anchors"][f"StLate{mode}"]
                verify(late_state, [["*ᶠ*ʝ*e*k*e*i*d"], [f"*ᶠ*ʝ*e*k{output}*d"]],
                       f"{model} strictly late plain root under {mode}")
                if mode == "Nu":
                    verify(late[mode]["late-root"]["anchors"]["StPrint"],
                           [["*j*e*k*ei*d"], ["*j*e*k*e*i*d"]],
                           f"{model} explicit nucleus serialization")
                before, after = late[mode]["late-weak"]["anchors"][f"StLate{mode}"]
                verify(after, before, f"{model} weak material under {mode}")
            if model in ("A", "B2"):
                for key, ending in (("call-present", "þ"), ("call-participle", "d")):
                    verify(late["Con"][key]["output"], [f"ġecē{ending}"], f"{model} strictly late {key}")
            models[model] = {"S1": control, "retained": retained, "late": late,
                             "world_s2": {"input": state, "invalid": broken}}
        print(json.dumps({
            "base": run.BASE, "orders": orders, "source_sha256": digest(source),
            "runner_sha256": digest(Path(__file__)),
            "source_receipts": {name: digest(cycle2 / name) for name in
                                ("stress-census.json", "stress-repairs.json.gz", "stress-panel.tsv")},
            "frozen_component_hashes": {key: digest(value) for key, value in frozen.items()},
            "components": build.receipt(), "definitions": Stress.definitions(), "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()

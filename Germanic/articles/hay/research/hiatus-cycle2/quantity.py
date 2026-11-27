#!/usr/bin/env python3
"""Compare quantity and final-palatal placement in the isolated substrate."""

import argparse
import json
from pathlib import Path
import tempfile

from matched import Components as Matched, apply, trial
from panel import batches_for, inventory
from reproduce_stress import DELETION, run, verify


class Components:
    extra = {name: run.candidates.RULES[name]
             for name in ("HiPreLength", "HiLongGlide", "HiPostLength")}
    extra["AbsHigh"] = "[{*i} -> 0 || [EnglishStarLongVowel | EnglishStarLongDiphthong] _]"
    RULES = (*Matched.RULES, *extra)

    @classmethod
    def definitions(cls):
        return Matched.definitions() + "".join(f"define {name} {rule};\n"
                                               for name, rule in cls.extra.items())


def placements(order):
    early = order[order.index("OEWLossBeforeI") + 1]
    late = "OEJLossAfterHeavy"
    return {
        "H0": (),
        "short-edge": ((early, "GlEd"),),
        "prior-length-early-glide": ((early, "HiPreLength"), (early, "HiLongGlide")),
        "prior-length-late-glide": ((early, "HiPreLength"), (late, "HiLongGlide")),
        "post-length": ((early, "GlEd"), (late, "HiPostLength")),
        "loss-with-length": ((early, "GlDN"), (late, "GaDN")),
        "contraction": ((early, "DcEd"),),
        "absorption-early": ((early, "AbsHigh"),),
        "absorption-late": ((late, "AbsHigh"),),
        "Dahl-before-glide": ((early, "DaFinalJ"), (early, "GlEd")),
        "Dahl-after-glide": ((early, "GlEd"), (late, "DaFinalJ")),
        "Dahl-after-length": (
            (early, "GlEd"), (late, "HiPostLength"),
            ("OEPalatalFricativeMerger", "DaFinalJ")),
        "Dahl-after-merger": (("OECjCleanup", "DaFinalJ"),),
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
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    inherited, extension = inventory()
    frozen_paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    palatals = run.dsv(run.HERE / "palatal.tsv")
    compounds = {row["id"]: row["form"] for row in run.dsv(run.HERE / "compound.tsv")}
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-quantity-") as directory:
        private = run.compile_candidates(source, args.stage_cache, Path(directory), Components)
        paths = frozen_paths | private | {f"component:{DELETION}": private["component:StFoot"]}
        probes = {row["id"]: row["form"] for row in palatals if row["start"] != "full"}
        edge = {rule: apply(paths, [rule], probes | compounds)[rule] for rule in
                ("DaFinalJ", "DaMemberLoss", "AbsHigh", "HiPreLength", "HiPostLength",
                 "OEJLossAfterHeavy")}
        for key in ("long-edge", "short-diph-edge", "long-diph-edge", "key-long"):
            verify(edge["DaFinalJ"][key], [probes[key][:-2]], f"literal Dahl scope/{key}")
        for key in ("short-edge", "key-protected", "long-syllabic"):
            verify(edge["DaFinalJ"][key], [probes[key]], f"literal Dahl negative/{key}")
        verify(edge["AbsHigh"]["long-syllabic"], ["*t*ḗ"], "absorption, not coda loss")
        for model, order in orders.items():
            batches = batches_for(order, inherited, extension, archive["models"][model]["baseline"])
            for row in palatals:
                # Full rows are in the T1 panel or resolved explicitly here; @ aliases
                # point to the unchanged inherited submission.
                form, start = row["form"], row["start"]
                if form.startswith("@"):
                    form = batches[order[0]][form[1:]]
                batches.setdefault(order[0] if start == "full" else start, {})[
                    "palatal:" + row["id"]] = form
            models[model] = {arm: {"placements": where, "traces": trial(order, paths, batches, where)}
                             for arm, where in placements(order).items()}

    print(json.dumps({
        "base": run.BASE, "source_sha256": run.frozen.sha(source), "orders": orders,
        "runner_sha256": run.frozen.sha(Path(__file__)), "definition_text": Components.definitions(),
        "parcels_sha256": run.frozen.sha(run.HERE / "palatal.tsv"),
        "inputs": probes | compounds, "isolated": edge, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

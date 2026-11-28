#!/usr/bin/env python3
"""Probe late stress, token structure and weight without lifting the frozen corpus."""

import argparse
import json
from pathlib import Path
import re
import sys
import tempfile


SNAPSHOT = Path(sys.argv[1])
sys.path.insert(0, str(SNAPSHOT / "Germanic/articles/hay/research/hiatus-cycle2"))

from matched import apply
from medial import Components as Prior
from reproduce_stress import run, verify


PROBES = {
    "hiatus": "*t*e*i*d*i", "accented": "*t*é*i*d*i",
    "old-nuclear": "*t*ei*d*i", "accented-nuclear": "*t*éi*d*i",
    "approximant": "*t*e*j*d*i", "fricative": "*t*e*ʝ*d*i",
    "prefixed": "*ᶠ*ʝ*e*k*e*i*θ", "prefixed-acute": "*ᶠ*ʝ*e*k*é*i*θ",
    "posttonic": "*t*á*k*e*i*θ",
    "short-control": "*t*e*d*i", "long-control": "*t*ē*d*i",
    "plain-final": "*t*e*i", "acute-final": "*t*é*i",
}


def components(source):
    source_text = source.read_text(encoding="utf-8")
    hvd = source_text[source_text.index("define HvS "):source_text.index("# SC117")]

    def weight(label, target):
        body = re.sub(r"\b(?:Hv[SLVHIP]|OEHighVowelApocope)\b",
                      lambda m: label + m[0], hvd)
        name = f"EnglishStar{target}Diphthong"
        return (body.replace(name, f"[{name}|{{*ėi}}|{{*éi}}]")
                .replace("FootCtx(", "RpFoot("))

    class Components:
        RULES = (*Prior.RULES, "RpNu", "RpMo", "RpRead",
                 "LtOEHighVowelApocope", "ShOEHighVowelApocope")

        @staticmethod
        def definitions():
            return (Prior.definitions() +
                    "define RpNu [{*é} {*i} -> {*éi}] .o. "
                    "[{*e} {*i} -> {*ėi} || HiHeadContext _];\n"
                    "define RpMo [{*éi} -> {*ḗ} || _ [{*d}|{*θ}|{*ð}|{*n}]] .o. "
                    "[{*ėi} -> {*ē} || _ [{*d}|{*θ}|{*ð}|{*n}]];\n"
                    "define RpRead [{*éi} -> e i, {*ėi} -> e i];\n" +
                    "define RpSeg [ContextSegments|{*ėi}|{*éi}];\n"
                    "define RpFoot(T) [[{*ᵘ}|{*ᶜ}|0] "
                    "[[{*ᶠ} OEAnyConsonant* EnglishStarVocalic|0] "
                    "[RpSeg* .o. T]]];\n" +
                    weight("Lt", "Long") + weight("Sh", "Short"))

    return Components


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canon, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canon, **alternatives}
    baseline = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    verify(run.frozen.sha(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    private = components(source)
    orth = ("OEPalatalFricativeMerger", "OldEnglishOrthography",
            "OldEnglishRemoveStars", "OldEnglishSurface")
    with tempfile.TemporaryDirectory(prefix="hay3-representation-") as work:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(work), private)
        sequences = {
            "cycle2": ("NuDN", "NaDN"),
            "pre-h": ("RpNu",), "post-h": ("OEHLoss", "RpNu"),
            "private-nuclear": ("RpNu", "RpMo"),
            "frozen-weight": ("RpNu", "OEHighVowelApocope"),
            "private-short": ("RpNu", "ShOEHighVowelApocope"),
            "private-long": ("RpNu", "LtOEHighVowelApocope"),
            "unincorporated-weight": ("OEHighVowelApocope",),
            "frozen-print": orth,
            "nuclear-print": ("RpNu", "RpRead", *orth),
        }
        receipts = {key: apply(paths, steps, PROBES) for key, steps in sequences.items()}
    verify(receipts["cycle2"]["NuDN"]["accented"], ["*t*ei*d*i"], "cycle 2 consumes acute")
    verify(receipts["private-nuclear"]["RpNu"]["accented"], ["*t*éi*d*i"], "acute nuclear token")
    verify(receipts["private-nuclear"]["RpMo"]["accented"], ["*t*ḗ*d*i"], "acute retained")
    verify(receipts["private-nuclear"]["RpMo"]["old-nuclear"], [PROBES["old-nuclear"]],
           "inherited token kept separate")
    verify(receipts["pre-h"]["RpNu"]["prefixed"], ["*ᶠ*ʝ*e*k*ėi*θ"], "pre-h foot path")
    verify(receipts["post-h"]["RpNu"]["prefixed"], ["*ʝ*e*k*e*i*θ"], "loss of foot path")
    verify(receipts["post-h"]["RpNu"]["prefixed-acute"], ["*ʝ*e*k*éi*θ"], "acute path independent")
    verify(receipts["post-h"]["RpNu"]["posttonic"], [PROBES["posttonic"]], "posttonic negative")
    for label, ending in (("short", "*i"), ("long", "")):
        stage = {"short": "Sh", "long": "Lt"}[label] + "OEHighVowelApocope"
        for key, token in (("hiatus", "*ėi"), ("accented", "*éi")):
            verify(receipts[f"private-{label}"][stage][key], ["*t" + token + "*d" + ending],
                   f"{label} nuclear weight/{key}")
    verify(receipts["nuclear-print"]["OldEnglishSurface"]["acute-final"], ["tei"],
           "explicit serialization")
    print(json.dumps({
        "base": run.BASE, "source_sha256": run.frozen.sha(source),
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": private.definitions(),
        "probes": PROBES, "receipts": receipts,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

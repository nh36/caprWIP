"""Co-admit light and heavy front nuclei in a stage-local research alphabet."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from matched import apply


LIGHT = ("ėi", "éi")
HEAVY = ("ēi", "ḗi")
PRIVATE = LIGHT + HEAVY


def symbols(items):
    return "|".join(f"{{*{item}}}" for item in items)


def family(source):
    text = source.read_text(encoding="utf-8")

    def definition(name):
        return re.search(rf"^define {name}\b.*?;", text, flags=re.M | re.S)[0]

    aliases = {"HvS": "NxS", "HvL": "NxL", "HvV": "NxV", "HvH": "NxH",
               "HvI": "NxI", "HvP": "NxP", "OEHighVowelApocope": "NxHvd",
               "OESecondaryFrontDecode": "NxDecode", "OENonHighSyn": "NxSyn",
               "OELAdjacentSyncope": "NxLSyn", "OEPalatalFricativeMerger": "NxPal"}
    names = tuple(aliases)
    aliases |= {"FootCtx": "NxFoot", "Ctx": "NxCtx", "EnglishStarVocalic": "NxVocalic",
                "EnglishStarShortDiphthong": "NxShort", "EnglishStarLongDiphthong": "NxLong"}
    pattern = re.compile(r"\b(" + "|".join(aliases) + r")\b")

    class Nucleus:
        RULES = ("NxHvd", "NxSyn", "NxLSyn", "NxPal", "NxLight", "NxHeavy",
                 "NxMono", "NxPrint", "NxGate")

        @staticmethod
        def definitions():
            return "\n".join((
                run.candidates.PREFIX,
                f"define NxShort [EnglishStarShortDiphthong|{symbols(LIGHT)}];",
                f"define NxLong [EnglishStarLongDiphthong|{symbols(HEAVY)}];",
                f"define NxVocalic [EnglishStarVocalic|{symbols(PRIVATE)}];",
                f"define NxSeg [ContextSegments|{symbols(PRIVATE)}];",
                "define NxSentence(T) [[{*ᵘ}|{*ᶜ}|0] [[NxSeg|{*ᶠ}]* .o. T]];",
                "define NxFoot(T) NxSentence([{*ᶠ} OEAnyConsonant* NxVocalic "
                "[NxSeg* .o. T] | [NxSeg* .o. T]]);",
                "define NxCtx(T) NxSentence([[{*ᶠ}|0] [NxSeg* .o. T]]);",
                "define NxGate [[{*ᵘ}|{*ᶜ}|0] [{*ᶠ}|0] NxSeg+];",
                *(pattern.sub(lambda m: aliases[m[0]], definition(name))
                  for name in names),
                "define NxLight [{*é} {*i} -> {*éi}] .o. "
                "[{*e} {*i} -> {*ėi} || HiHeadContext _];",
                "define NxHeavy [{*é} {*i} -> {*ḗi}] .o. "
                "[{*e} {*i} -> {*ēi} || HiHeadContext _];",
                "define NxMono [{*éi} -> {*ḗ} || _ [{*d}|{*θ}|{*ð}|{*n}]] .o. "
                "[{*ėi} -> {*ē} || _ [{*d}|{*θ}|{*ð}|{*n}]] .o. "
                "[{*ḗi} -> {*ḗ} || _ [{*d}|{*θ}|{*ð}|{*n}]] .o. "
                "[{*ēi} -> {*ē} || _ [{*d}|{*θ}|{*ð}|{*n}]];",
                "define NxPrint [{*ėi} -> {*ei}, {*éi} -> {*ei}, "
                "{*ēi} -> {*ei}, {*ḗi} -> {*ei}];",
            ))

    return Nucleus


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
    probes = {"hiatus": "*t*e*i*d*i", "long-v": "*t*ē*j*d*i",
              "inherited": "*t*ei*d*i", "j": "*t*e*j*d*i", "fricative": "*t*e*ʝ*d*i",
              **{item: f"*t*{item}*d*i" for item in PRIVATE}}
    with tempfile.TemporaryDirectory(prefix="hay4-nucleus-") as directory:
        recipe = family(source)
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, recipe, runtime)
        paths = frozen | build.verify()
        assays = {
            "admission": apply(paths, ("NxGate", "NxHvd"), probes | {"unknown": "*t*λ*d*i"}),
            "frozen-weight": apply(paths, ("OEHighVowelApocope",), probes),
            "nuclear-entry": {
                name: apply(paths, (name, "NxGate", "NxHvd", "NxMono"), {
                    "plain": "*t*e*i*d*i", "acute": "*t*é*i*d*i",
                    "foot": "*ᶠ*ʝ*e*k*e*i*d*i", "weak": "*t*á*k*e*i*d*i",
                }) for name in ("NxLight", "NxHeavy")
            },
            "compound-link": apply(paths, ("NxSyn", "OECompoundLinkingSyncope"),
                                   {item: f"*w*{item}*r*a*l*i*d" for item in PRIVATE}),
            "light-syncope": apply(paths, ("NxLSyn",),
                                   {item: f"*n*{item}*t*i*l*ǭ" for item in PRIVATE}),
            "palatals": apply(paths, ("NxPal",), {"j": probes["j"], "fricative": probes["fricative"]}),
            "print": apply(paths, ("NxPrint", "OldEnglishOrthography", "OldEnglishRemoveStars",
                                   "OldEnglishSurface"), {item: f"*t*{item}*d" for item in PRIVATE}),
            "proto-gate": apply(paths, ("EnglishProtoInput",),
                                {"valid": "tédiz", **{item: f"t{item}diz" for item in PRIVATE}}),
        }
        verify(assays["admission"]["NxGate"]["unknown"], [], "unlicensed symbol")
        verify(assays["admission"]["NxHvd"], {
            key: ([form.removesuffix("*i")] if key in {*HEAVY, "inherited", "long-v", "j", "fricative"}
                  else [form]) for key, form in probes.items()
        } | {"unknown": []}, "HVD and stage admission")
        verify({item: assays["frozen-weight"]["OEHighVowelApocope"][item] for item in PRIVATE},
               dict.fromkeys(PRIVATE, []), "frozen rejection is not deletion")
        verify(assays["palatals"]["NxPal"], dict.fromkeys(("j", "fricative"), [probes["j"]]),
               "palatal merger deliberately neutralizes the earlier distinction")
        verify(assays["compound-link"]["NxSyn"], {
            item: [f"*w*{item}*r*l*i*d"] for item in PRIVATE
        }, "compound-vowel syncope")
        verify(assays["light-syncope"]["NxLSyn"], {
            item: [f"*n*{item}*t{'*i' if item in HEAVY else ''}*l*ǭ"] for item in PRIVATE
        }, "l-adjacent syncope sensitive to quantity, not accent")
        verify(assays["print"]["OldEnglishSurface"],
               dict.fromkeys(PRIVATE, ["teid"]), "late serialization collapses research distinctions")
        verify({item: assays["proto-gate"]["EnglishProtoInput"][item] for item in PRIVATE},
               {"ėi": [], "éi": [], "ēi": ["*t*ē*i*d*i*z"], "ḗi": ["*t*ḗ*i*d*i*z"]},
               "proto admission cannot construct a private nucleus")
        for label, (plain, acute) in zip(("NxLight", "NxHeavy"), (LIGHT, HEAVY)):
            traces = assays["nuclear-entry"][label]
            verify(traces[label], {"plain": [f"*t*{plain}*d*i"], "acute": [f"*t*{acute}*d*i"],
                                   "foot": [f"*ᶠ*ʝ*e*k*{plain}*d*i"], "weak": ["*t*á*k*e*i*d*i"]},
                   f"{label} keeps stress and weak material distinct")
            verify(traces["NxMono"]["acute"], ["*t*ḗ*d" + ("*i" if label == "NxLight" else "")],
                   f"{label} accented monophthongization")
        print(json.dumps({"base": run.BASE, "orders": orders, "source_sha256": digest(source),
                          "runner_sha256": digest(Path(__file__)), "components": build.receipt(),
                          "definitions": recipe.definitions(), "assays": assays}, ensure_ascii=False))


if __name__ == "__main__":
    main()

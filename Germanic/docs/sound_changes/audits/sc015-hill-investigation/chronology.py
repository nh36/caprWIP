#!/usr/bin/env python3
"""Component-only supplement to the protected SC015 research receipt."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
from capr_runtime import layout


def stars(form):
    return "".join("*" + char for char in form.replace("h", "x").replace("þ", "θ"))


def main():
    rt = layout()
    if not rt.is_container:
        raise RuntimeError("Run inside the backend container")
    primary = json.loads(Path(sys.argv[1]).read_text())
    if assay.digest(rt.germanic_fst) != primary["fst_sha256"]:
        raise RuntimeError("Source no longer matches the primary experiment")
    definitions = primary["definitions"] + """
define AFRLength [Ctx([
  {*i} -> {*ī} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*í} -> {*ī} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*e} -> {*ē} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*é} -> {*ḗ} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*a} -> {*ā} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*á} -> {*ā} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*u} -> {*ū} || .#. EnglishStarConsonant* _ {*r} .#.,
  {*ú} -> {*ū} || .#. EnglishStarConsonant* _ {*r} .#.
])];
"""
    components = [
        "AFRLength", "AFHill", "AFTauto", "PNWGmcILowering",
        "EnglishStarNonHighVowel",
    ]
    recipe = {
        "id": "sc015-r-lengthening-supplement",
        "definitions": definitions, "replace": {}, "insert_rule": "",
        "component_checks": [{"component": c} for c in components],
    }
    result = {
        "fst_sha256": primary["fst_sha256"],
        "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "recipe": recipe,
        "citation": "Hill2017:148-149,156-158;Kroonen2013:270",
        "normalization": "Source h -> CAPR x; source thorn -> CAPR theta.",
        "limit": "Component experiment, not an adopted law or a complete native history. "
        "Close source e is represented by CAPR e. The u mapping is a schematic "
        "short-vowel completeness control, not an additional lexical witness.",
    }
    with tempfile.TemporaryDirectory(prefix="capr_sc015_r_") as directory:
        bins = assay.compile_isolated(
            rt.germanic_fst, recipe, [], Path(directory), components_only=True,
        )

        def apply(component, forms):
            return assay.batch_apply_down(bins["component:" + component], forms)

        result["r_order"] = {}
        for form in ("hir", "xír", "hīr", "hwar", "þar"):
            encoded = stars(form)
            lowered = apply("AFHill", [encoded])[0]
            lengthened = apply("AFRLength", [encoded])[0]
            if len(lowered) != 1 or len(lengthened) != 1:
                raise RuntimeError(f"Non-deterministic component: {form}")
            result["r_order"][form] = {
                "input": encoded,
                "lower_first": lowered,
                "lower_then_lengthen": apply("AFRLength", lowered)[0],
                "lengthen_first": lengthened,
                "lengthen_then_lower": apply("AFHill", lengthened)[0],
            }
        if result["r_order"]["hir"]["lower_then_lengthen"] != [stars("hēr")]:
            raise RuntimeError("Lowering-before-lengthening does not produce her with long e")
        if result["r_order"]["hir"]["lengthen_then_lower"] != [stars("hīr")]:
            raise RuntimeError("Lengthening-before-lowering fails to preserve long i")
        vowel_symbols = ("a", "ā", "ą", "e", "ē", "ḗ", "o", "ō", "ǭ",
                         "ɔ̆", "ô", "à", "è", "ò", "i", "u", "ī", "ū")
        forms = {f"nir-{v}": stars("nir") + "*" + v for v in vowel_symbols}
        forms.update({
            "irha-inherited-counterexample": stars("irha"),
            "iz-between-vowels": stars("wizana"),
            "nasal-z-control": stars("ninza"),
        })
        result["domain_inputs"] = forms
        result["domain_outputs"] = {
            c: dict(zip(forms, apply(c, list(forms.values()))))
            for c in ("AFHill", "AFTauto", "PNWGmcILowering")
        }
        vowels = ["*" + v for v in vowel_symbols]
        result["nonhigh_acceptance"] = dict(zip(
            vowels, apply("EnglishStarNonHighVowel", vowels),
        ))
    if assay.digest(rt.germanic_fst) != primary["fst_sha256"]:
        raise RuntimeError("Canonical source changed during component experiment")
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    Path(sys.argv[2]).write_text(text)
    print("SC015 r-order and extended-domain supplement complete")


if __name__ == "__main__":
    main()

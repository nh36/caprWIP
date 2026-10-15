#!/usr/bin/env python3
"""Component-only chronology supplement for the SC015 a-ablaut investigation.

Pairwise ordering tests between candidate lowering components and the
neighbouring canonical stages (monosyllabic r-lengthening proxy, SC036
OEInterStressRaising, MonosyllabicFinalZLoss, EAFRhotacism, OEIUmlaut).
Research receipt only: nothing here is an adopted law or a complete native
history.  Must run inside the backend container against the unchanged source.
"""
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


CANONICAL = [
    "PNWGmcILowering", "OEInterStressRaising", "MonosyllabicFinalZLoss",
    "EAFFinalZDeletion", "EAFRhotacism", "OEIUmlaut",
]
CANDIDATES = ["AFHillB", "AFHillR", "AFHillZ", "AFHillSt", "AFTradA"]


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
    components = CANONICAL + CANDIDATES + ["AFRLength"]
    recipe = {
        "id": "sc015-a-ablaut-chronology", "definitions": definitions,
        "replace": {}, "insert_rule": "",
        "component_checks": [{"component": c} for c in components],
    }
    result = {
        "fst_sha256": primary["fst_sha256"],
        "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "recipe": recipe,
        "normalization": "Source h -> CAPR x; source thorn -> CAPR theta; CAPR close short e for Hill's lowered vowel.",
        "limit": "Pairwise component ordering only. AFRLength is a schematic monosyllabic "
        "r-lengthening proxy (Hill 2017), not an adopted law. Inputs are controlled "
        "segment strings or the live CAPR PROTOFORMs named below.",
    }
    with tempfile.TemporaryDirectory(prefix="capr_sc015_chron_") as directory:
        bins = assay.compile_isolated(
            rt.germanic_fst, recipe, [], Path(directory), components_only=True,
        )

        def apply(component, forms):
            outs = assay.batch_apply_down(bins["component:" + component], forms)
            for form, out in zip(forms, outs):
                if len(out) != 1:
                    raise RuntimeError(f"Non-deterministic {component} on {form}: {out}")
            return [out[0] for out in outs]

        def order(first, second, encoded):
            a = apply(first, [encoded])[0]
            b = apply(second, [encoded])[0]
            return {
                "input": encoded,
                f"{first}_then_{second}": apply(second, [a])[0],
                f"{second}_then_{first}": apply(first, [b])[0],
            }

        # 1. Monosyllabic r-lengthening versus lowering (Hill 2017: 148-149, 156-158).
        result["r_lengthening"] = {
            cand: {f: order(cand, "AFRLength", stars(f)) for f in ("hir", "xír", "hwar")}
            for cand in ("PNWGmcILowering", "AFHillB", "AFHillR")
        }
        for cand in ("AFHillB", "AFHillR"):
            r = result["r_lengthening"][cand]["hir"]
            if r[f"{cand}_then_AFRLength"] != stars("hēr") or r[f"AFRLength_then_{cand}"] != stars("hīr"):
                raise RuntimeError(f"{cand}: r-lengthening order test failed: {r}")

        # 2. SC036 OEInterStressRaising versus lowering: the live `world` PROTOFORM.
        world = {"wír-àldu": "*w*í*r*à*l*d*u", "wér-àldu": "*w*é*r*à*l*d*u"}
        result["sc036_world"] = {
            cand: {k: order(cand, "OEInterStressRaising", v) for k, v in world.items()}
            for cand in ("PNWGmcILowering", "AFHillB", "AFHillR", "AFTradA")
        }
        inc = result["sc036_world"]["PNWGmcILowering"]["wír-àldu"]
        if inc["PNWGmcILowering_then_OEInterStressRaising"] == inc["OEInterStressRaising_then_PNWGmcILowering"]:
            raise RuntimeError("Expected the incumbent to be order-sensitive against SC036")
        hill = result["sc036_world"]["AFHillB"]["wír-àldu"]
        if hill["AFHillB_then_OEInterStressRaising"] != hill["OEInterStressRaising_then_AFHillB"]:
            raise RuntimeError("Expected Hill-style r-conditioning to be order-insensitive against SC036")

        # 3. z-component versus monosyllabic z-loss / general final-z deletion.
        z_forms = {"iz": stars("iz"), "hiz": stars("hiz"), "wiraz": stars("wiraz"), "mizdai": "*m*í*z*d*ē"}
        result["z_loss"] = {
            loss: {cand: {k: order(cand, loss, v) for k, v in z_forms.items()}
                   for cand in ("PNWGmcILowering", "AFHillB", "AFHillZ")}
            for loss in ("MonosyllabicFinalZLoss", "EAFFinalZDeletion")
        }

        # 4. Rhotacism versus lowering: does late r-conditioning recover z-cases?
        result["rhotacism"] = {
            cand: {k: order(cand, "EAFRhotacism", v)
                   for k, v in {"mizdai": "*m*í*z*d*ē", "liznojana": "*l*í*z*n*ō*j*a*n*ą", "iz": stars("iz")}.items()}
            for cand in ("PNWGmcILowering", "AFHillB", "AFHillR", "AFHillZ")
        }

        # 5. i-mutation recovery for apparent exceptions (nest-derivative, list, learn).
        result["umlaut_recovery"] = {
            cand: {k: order(cand, "OEIUmlaut", v)
                   for k, v in {"nistijana": stars("nistijana"), "listiz": stars("listiz"),
                                "liznijana": stars("liznijana")}.items()}
            for cand in ("PNWGmcILowering", "AFHillB", "AFHillSt", "AFHillZ")
        }

    if assay.digest(rt.germanic_fst) != primary["fst_sha256"]:
        raise RuntimeError("Canonical source changed during component experiment")
    Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("SC015 a-ablaut chronology supplement complete")


if __name__ == "__main__":
    main()

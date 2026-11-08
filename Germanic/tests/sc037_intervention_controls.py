"""Fresh production controls for the source-backed SC037 intervention."""

import json
import os
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, "/usr/app/tools")
from anglo_frisian_experiments import (
    compile_isolated, corpus_rows, prepare_definition_image,
)
from executable_facts import parse_defines
from sound_change_order_sensitivity import batch_apply_down

source = Path("/usr/app/fsts/germanic.txt")
definitions = parse_defines(source.read_text())
extra = """
define AFPass ?*;
define AFOld037 Ctx([
    {*a} -> 0 || PGmcStarAcuteVowel OEAnyConsonant+ _ OEAnyConsonant+ PGmcStarGraveVowel
] .o. [
    [{*i}|{*u}] -> 0 || PGmcStarAcuteVowel OEAnyConsonant+ _ OEAnyConsonant+ PGmcStarGraveVowel
]);
define AFNoWeight FootCtx([
    [{*i}|{*u}|{*y}] -> 0
        || .#. OEAnyConsonant* EnglishStarVocalic OEAnyConsonant+
            _ OEAnyConsonant EnglishStarVocalic
]);
define AFNoHigh ?*;
define AFEarlyHigh """ + definitions["OEHighVowelApocope"].body + """;
define AFLateHigh """ + definitions["OEHighVowelApocope"].body + """;
define AFLateN NWGmcInStemNLoss;
define AFOldW Ctx([{*w} -> 0 || EnglishStarVocalic _ {*i} .#.]);
define AFEarlyB """ + definitions["PGmcBAllophony"].body + """;
define AFHighHandling [OEHighVowelApocope .o. OEMedialSyncope .o. OEHighLinkSyncope .o. OEHighStressDecode];
define AFBadI """ + definitions["OEBreakingI"].body.replace(
    ".#. OEAnyConsonant* _", "_") + """;
define AFBadBr FootCtx(OEBreakingA .o. OEBreakingE .o. AFBadI);
define AFOpaqueFront """ + definitions["OEIUmlautFronting"].body.replace(
    "EnglishIUmlautThroughU", "EnglishIUmlautIntervening") + """;
define AFOpaqueUm FootCtx(AFOpaqueFront .o. OEIUmlautRaising .o. OEIUmlautDiphthong);
"""
forms = ["sáli-wàrðaz", "sáli-wàrðuz", "sáli-wàrðą", "wíduwōn",
         "knéwai", "fūliθǭ", "spénnilǭ", "régna-bùgô"]
staged = [
    {"id": "furthest", "stage": "OEIUmlaut", "side": "before",
     "input": "*ū*t*u*m*i*s*t", "expected": "ȳtmest",
     "evidence": "Ringe-Taylor p267; Hogg 5.76/6.10; pre-OE, not PGmc"},
    {"id": "companion", "stage": "OEIUmlaut", "side": "before",
     "input": "*g*á*d*u*l*i*n*g", "expected": "gædeling",
     "evidence": "Hogg 5.76/6.10; pre-OE, not PGmc"},
    {"id": "heads", "stage": "OENonHighSyn", "side": "before",
     "input": "*x*ēa*β*u*d*u", "expected": "hēafodu",
     "evidence": "Fulk2010 pp129-134; Goering2016 pp186-188; quantitative HLL retention"},
    {"id": "late-livestock", "stage": "OEWeightMarkers", "side": "before",
     "input": "*n*ē*t*ī*n", "expected": "nēten",
     "evidence": "Goering2016 pp186-188 / 2023 pp67-68; late state, not inherited input"},
    {"id": "early-fright", "stage": "PWGmcFinalBareALoss", "side": "after",
     "input": "*f*ú*r*x*t*ī*n", "expected": "fyrhte",
     "evidence": "RingeTaylor2014 pp87-88,380-381; inherited oblique"},
    {"id": "early-pillow", "stage": "PWGmcFinalBareALoss", "side": "after",
     "input": "*p*ú*l*w*ī*n", "expected": "pyle",
     "evidence": "Campbell473; RingeTaylor2014 p260; independent loan control"},
]
components = ["EnglishProtoInput", "OEBreaking", "OEIUmlaut",
              "OEHighVowelApocope", "OEMedialSyncope", "OEHighLinkSyncope", "OEHighStressDecode",
              "AFHighHandling", "OELAdjacentSyncope", "PGmcBAllophony",
              "OEStripSecondaryStress", "NWGmcInStemNLoss", "OEWLossBeforeI"]
break_inputs = ["*f*u*l*w*i*x*t", "*n*a*w*i*x*t", "*s*i*w", "*s*í*w",
                "*b*i*r*x*t", "*w*i*w*i", "*w*i*w*ī",
                "*s*æ*l*ì*w*æ*r*d", "*ᶠ*b*i*s*i*w"]
high_inputs = ["*s*e*l*i*w*ea*r*d", "*x*a*n*d*u*s*ea*x",
               "*ȳ*t*y*m*i*s*t", "*b*o*n*d*i*n*s*t*a",
               "*ʃ*y*l*d*i*ç*ǣ*t*j*ā", "*l*a*n*d*w*ì*n*a"]
umlaut_inputs = ["*ū*t*u*m*i", "*g*a*d*u*l*i*n*g",
                 "*ū*t*a*m*i", "*ū*t*ù*m*i"]
report = {}
with tempfile.TemporaryDirectory(prefix="capr-sc037-controls-") as temporary:
    root = Path(temporary)
    image = prepare_definition_image(source, root)
    if image:
        os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
    for name, replacements in (
        ("current", {}),
        ("old-early", {"OECompoundLinkingSyncope": "AFOld037"}),
        ("bad-breaking", {"OEBreaking": "AFBadBr"}),
        ("no-weight", {"OEHighVowelApocope": "AFNoWeight"}),
        ("no-high", {"OEHighVowelApocope": "AFNoHigh"}),
        ("early-high", {"OEHighVowelApocope": "AFNoHigh"}),
        ("late-high", {"OEHighVowelApocope": "AFNoHigh"}),
        ("no-n-loss", {"NWGmcInStemNLoss": "AFNoHigh"}),
        ("late-n-loss", {"NWGmcInStemNLoss": "AFNoHigh"}),
        ("old-w-loss", {"OEWLossBeforeI": "AFOldW"}),
        ("early-b", {"PGmcBAllophony": "AFNoHigh"}),
        ("no-unrounding", {"OEHighLinkSyncope": "AFNoHigh"}),
        ("opaque-umlaut", {"OEIUmlaut": "AFOpaqueUm"}),
    ):
        directory = root / name
        directory.mkdir()
        recipe = {"definitions": extra, "replace": replacements,
                  "id": name, "insert_rule": "AFPass", "insert_after": "EnglishProtoInput",
                  "staged_checks": staged,
                  "component_checks": [{"component": member} for member in components]}
        if name == "early-high":
            recipe.update(insert_rule="AFEarlyHigh",
                          insert_after="OEWsPalatalDiphthongization")
        elif name == "late-high":
            recipe.update(insert_rule="AFLateHigh",
                          insert_after="OEPreconsonantalDegemination")
        elif name == "late-n-loss":
            recipe.update(insert_rule="AFLateN", insert_after="OEHighVowelApocope")
        elif name == "early-b":
            recipe.update(insert_rule="AFEarlyB", insert_after="OESecondaryNasalization")
        bins = compile_isolated(source, recipe, [], directory)
        value = {
            "canonical": dict(zip(forms, batch_apply_down(bins["final"], forms))),
            "furthest": batch_apply_down(bins["staged:furthest"], [staged[0]["input"]]),
            "companion": batch_apply_down(bins["staged:companion"], [staged[1]["input"]]),
            "heads": batch_apply_down(bins["staged:heads"], [staged[2]["input"]]),
            "blockers": {
                item["id"]: batch_apply_down(bins["staged:" + item["id"]], [item["input"]])
                for item in staged[3:]
            },
        }
        if name == "current":
            value["breaking"] = batch_apply_down(bins["component:OEBreaking"], break_inputs)
            value["high"] = batch_apply_down(bins["component:AFHighHandling"], high_inputs)
            value["umlaut"] = batch_apply_down(bins["component:OEIUmlaut"], umlaut_inputs)
            value["atomic_iu"] = batch_apply_down(
                bins["component:EnglishProtoInput"], ["síu-wàrdaz"])
            stressed = ["*l*á*n*d*x*ù*m*i", "*l*á*n*d*w*ì*n*a"]
            for member in ("OEStripSecondaryStress", "OEBreaking", "OEIUmlaut",
                           "OEHighVowelApocope", "OEMedialSyncope", "OEHighLinkSyncope", "OEHighStressDecode"):
                stressed = [outputs[0] for outputs in batch_apply_down(
                    bins["component:" + member], stressed)]
            value["stressed"] = stressed
            rows = corpus_rows(Path("/usr/app/data/germanic-aligned-final.tsv"))
            outputs = batch_apply_down(bins["final"], [row["fst_input"] for row in rows])
            value["selected"] = [{**row, "outputs": output}
                                 for row, output in zip(rows, outputs)]
            value["fee"] = batch_apply_down(bins["final"], ["féx", "féxu", "féxą"])
            value["n_loss"] = batch_apply_down(
                bins["component:NWGmcInStemNLoss"],
                ["*f*ú*r*x*t*ī*n", "*p*ú*l*w*ī*n", "*s*t*r*á*n*g*ī*n",
                 "*t*ú*n*g*a*n", "*s*t*ī*n", "*s*t*ḯ*n"])
            value["w_loss"] = batch_apply_down(
                bins["component:OEWLossBeforeI"],
                ["*w*ī", "*s*w*ī", "*a*w*i", "*p*y*l*w*ī",
                 "*p*y*l*w*í", "*g*ea*r*w*i*d*e"])
            value["weak"] = batch_apply_down(
                bins["component:OEHighLinkSyncope"],
                ["*y*n", "*g*æ*d*y*l*i*n*g", "*l*a*n*d*x*ỳ*m*i"])
            value["light"] = batch_apply_down(
                bins["component:OELAdjacentSyncope"],
                ["*n*e*t*i*l*ǭ", "*g*æ*d*i*l*i*n*g", "*k*e*t*i*l",
                 "*a*θ*i*l*a", "*a*f*i*l*a"])
            value["labial"] = batch_apply_down(
                bins["component:PGmcBAllophony"],
                ["*b*a", "*a*b*a", "*l*a*m*b", "*x*a*b*b*a",
                 "*r*e*g*n*b*o*g*ô", "*r*e*g*n*β*o*g*ô"])
        report[name] = value
print(json.dumps(report, ensure_ascii=False))

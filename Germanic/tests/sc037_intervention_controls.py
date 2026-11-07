"""Fresh production controls for the source-backed SC037 intervention."""

import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, "/usr/app/tools")
from anglo_frisian_experiments import compile_isolated, corpus_rows
from executable_facts import parse_defines
from sound_change_order_sensitivity import batch_apply_down

source = Path("/usr/app/fsts/germanic.txt")
definitions = parse_defines(source.read_text())
quality = definitions["OEHighLinkSyncope"].body.split("]) .o.", 1)[1]
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
]) .o. """ + quality + """;
define AFNoHigh """ + quality + """;
define AFBadI """ + definitions["OEBreakingI"].body.replace(
    ".#. OEAnyConsonant* _", "_") + """;
define AFBadBr FootCtx(OEBreakingA .o. OEBreakingE .o. AFBadI);
define AFOpaqueFront """ + definitions["OEIUmlautFronting"].body.replace(
    "EnglishIUmlautThroughU", "EnglishIUmlautIntervening") + """;
define AFOpaqueUm FootCtx(AFOpaqueFront .o. OEIUmlautRaising .o. OEIUmlautDiphthong);
"""
forms = ["sáli-wàrðaz", "sáli-wàrðuz", "sáli-wàrðą", "wíduwōn",
         "knéwai", "fūliθō"]
staged = [
    {"id": "furthest", "stage": "OEIUmlaut", "side": "before",
     "input": "*ū*t*u*m*i*s*t", "expected": "ȳtmest",
     "evidence": "Ringe-Taylor p267; Hogg 5.76/6.10; pre-OE, not PGmc"},
    {"id": "companion", "stage": "OEIUmlaut", "side": "before",
     "input": "*g*á*d*u*l*i*n*g", "expected": "gædeling",
     "evidence": "Hogg 5.76/6.10; pre-OE, not PGmc"},
]
components = ["EnglishProtoInput", "OEBreaking", "OEIUmlaut",
              "OEHighLinkSyncope", "OEStripSecondaryStress"]
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
    for name, replacements in (
        ("current", {}),
        ("old-early", {"OECompoundLinkingSyncope": "AFOld037"}),
        ("bad-breaking", {"OEBreaking": "AFBadBr"}),
        ("no-weight", {"OEHighLinkSyncope": "AFNoWeight"}),
        ("no-high", {"OEHighLinkSyncope": "AFNoHigh"}),
        ("opaque-umlaut", {"OEIUmlaut": "AFOpaqueUm"}),
    ):
        directory = root / name
        directory.mkdir()
        recipe = {"definitions": extra, "replace": replacements,
                  "id": name, "insert_rule": "AFPass", "insert_after": "EnglishProtoInput",
                  "staged_checks": staged,
                  "component_checks": [{"component": member} for member in components]}
        bins = compile_isolated(source, recipe, [], directory)
        value = {
            "canonical": dict(zip(forms, batch_apply_down(bins["final"], forms))),
            "furthest": batch_apply_down(bins["staged:furthest"], [staged[0]["input"]]),
            "companion": batch_apply_down(bins["staged:companion"], [staged[1]["input"]]),
        }
        if name == "current":
            value["breaking"] = batch_apply_down(bins["component:OEBreaking"], break_inputs)
            value["high"] = batch_apply_down(bins["component:OEHighLinkSyncope"], high_inputs)
            value["umlaut"] = batch_apply_down(bins["component:OEIUmlaut"], umlaut_inputs)
            value["atomic_iu"] = batch_apply_down(
                bins["component:EnglishProtoInput"], ["síu-wàrdaz"])
            stressed = ["*l*á*n*d*x*ù*m*i", "*l*á*n*d*w*ì*n*a"]
            for member in ("OEStripSecondaryStress", "OEBreaking", "OEIUmlaut",
                           "OEHighLinkSyncope"):
                stressed = [outputs[0] for outputs in batch_apply_down(
                    bins["component:" + member], stressed)]
            value["stressed"] = stressed
            rows = corpus_rows(Path("/usr/app/data/germanic-aligned-final.tsv"))
            outputs = batch_apply_down(bins["final"], [row["fst_input"] for row in rows])
            value["selected"] = [{**row, "outputs": output}
                                 for row, output in zip(rows, outputs)]
        report[name] = value
print(json.dumps(report, ensure_ascii=False))

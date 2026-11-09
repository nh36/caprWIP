"""Fresh production controls for the source-backed SC037 intervention."""

import json
import hashlib
import os
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, "/usr/app/tools")
from anglo_frisian_experiments import (
    compile_isolated, complete_variant_order, corpus_rows, prepare_definition_image,
)
from executable_facts import parse_defines
from oe_trace_parse import parse_entries, parse_fidelity, parse_provenance, structural_problems
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
rows = corpus_rows(Path("/usr/app/data/germanic-aligned-final.tsv"))
by_concept = {row["concept"]: row for row in rows}
little = by_concept["little"]
forms.append(little["fst_input"])
coverage_finish = {concept: by_concept[concept] for concept in ("livestock", "dart")}
forms.extend(row["fst_input"] for row in coverage_finish.values())
trace_text = Path("/usr/app/docs/debug_snapshots/oe_full_trace_report.txt").read_text()
assert not structural_problems(trace_text)
provenance = parse_provenance(trace_text)
assert provenance.canonical and provenance.version == 2
assert provenance.recorded["germanic.txt"] == hashlib.sha256(source.read_bytes()).hexdigest()
assert provenance.recorded["germanic-aligned-final.tsv"] == hashlib.sha256(
    Path("/usr/app/data/germanic-aligned-final.tsv").read_bytes()).hexdigest()
entries, fidelity = parse_entries(trace_text), parse_fidelity(trace_text)


def before(concept, stage):
    row = by_concept[concept]
    key = (row["concept"], row["proto"], row["counterpart"])
    entry = entries[key]
    index = next(i for i, item in enumerate(entry.stages) if item.label == stage)
    previous = entry.stages[index - 1]
    raw = fidelity.get(key, {}).get(previous.label, {})
    assert not raw.get("rejected")
    values = raw.get("raw") or previous.forms
    assert len(values) == 1
    return values[0]


closeout = """
define AFHvHeavy [OEHighVowelApocope .o. FootCtx([
    [{*i}|{*u}|{*y}|{*ų}] -> 0 ||
    .#. OEAnyConsonant* HvH _ OEAnyConsonant EnglishStarVocalic
])];
define AFHvHap [OEHighVowelApocope .o. FootCtx([
    [{*i}|{*u}|{*y}|{*ų}] -> 0 ||
    .#. OEAnyConsonant* HvH EnglishStarVocalic OEAnyConsonant+ _ .#.
])];
define AFLClosed Ctx([
    {*i} -> 0 || [EnglishStarShortVowel|EnglishStarShortDiphthong]
    [OEAnyConsonant - [{*d}|{*θ}|{*f}]] _ {*l}
]);
define AFLHeavy Ctx([
    {*i} -> 0 || EnglishStarVocalic
    [OEAnyConsonant - [{*d}|{*θ}|{*f}]] _ {*l} EnglishStarVocalic
]);
define AFShFinal [OEMedLongShort .o. FootCtx([
    {*ī} -> {*i} || EnglishStarVocalic OEAnyConsonant+ _ .#.
])];
define AFWPost Ctx([{*w} -> 0 || EnglishStarVocalic _ [{*i}|{*ī}]]);
define AFWShort Ctx([
    {*w} -> 0 || EnglishStarVocalic EnglishStarConsonant* _ {*i}
]);
define AFWAll Ctx([
    {*w} -> 0 || EnglishStarVocalic EnglishStarConsonant* _ EnglishStarVocalic
]);
define AFNAll Ctx([
    {*n} -> 0 || [EnglishStarShortVowel|EnglishStarLongVowel] _ .#.
]);
"""
order = complete_variant_order({"replace": {}, "insert_rule": None, "insert_after": None})
closeout_rules = {
    "AF63Good": ("OEHighVowelApocope", "OEHighVowelApocope"),
    "AF63Heavy": ("OEHighVowelApocope", "AFHvHeavy"),
    "AF63Hap": ("OEHighVowelApocope", "AFHvHap"),
    "AF66Good": ("OELAdjacentSyncope", "OELAdjacentSyncope"),
    "AF66Closed": ("OELAdjacentSyncope", "AFLClosed"),
    "AF66Heavy": ("OELAdjacentSyncope", "AFLHeavy"),
    "AF117Good": ("OEMedLongShort", "OEMedLongShort"),
    "AF117Final": ("OEMedLongShort", "AFShFinal"),
    "AF117Omitted": ("OEMedLongShort", "AFPass"),
    "AF54Good": ("OEWLossBeforeI", "OEWLossBeforeI"),
    "AF54Post": ("OEWLossBeforeI", "AFWPost"),
    "AF54Short": ("OEWLossBeforeI", "AFWShort"),
    "AF54All": ("OEWLossBeforeI", "AFWAll"),
    "AF64Good": ("NWGmcInStemNLoss", "NWGmcInStemNLoss"),
    "AF64All": ("NWGmcInStemNLoss", "AFNAll"),
}
for label, (stage, replacement) in closeout_rules.items():
    tail = [replacement, *order[order.index(stage) + 1:]]
    closeout += "define " + label + " [" + " .o. ".join(tail) + "];\n"
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
        recipe = {"definitions": extra + (closeout if name == "current" else ""), "replace": replacements,
                  "id": name, "insert_rule": "AFPass", "insert_after": "EnglishProtoInput",
                  "staged_checks": staged,
                  "component_checks": [{"component": member} for member in [
                      *components, *(closeout_rules if name == "current" else [])]]}
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
            value["lexical_closeout"] = {
                "little": {"row_id": little["id"], "input": little["fst_input"],
                           "target": little["counterpart"]},
                "coverage_finish": {
                    concept: {"row_id": row["id"], "input": row["fst_input"],
                              "target": row["counterpart"]}
                    for concept, row in coverage_finish.items()},
                "livestock_hll": {label: batch_apply_down(bins["component:" + label], [
                    before("livestock", "OEHighVowelApocope")])
                    for label in ("AF63Good", "AF63Heavy", "AF63Hap")},
                "livestock_shortening": {
                    label: batch_apply_down(bins["component:" + label], [
                        before("livestock", "OEMedLongShort"),
                        before("little", "OEMedLongShort")])
                    for label in ("AF117Good", "AF117Omitted")},
                "closed_dart": {label: batch_apply_down(bins["component:" + label], [
                    before("dart", "OELAdjacentSyncope")])
                    for label in ("AF66Good", "AF66Closed")},
                "hll": {label: batch_apply_down(bins["component:" + label], [
                    before("little", "OEHighVowelApocope")])
                    for label in ("AF63Good", "AF63Heavy", "AF63Hap")},
                "light_root": {label: batch_apply_down(bins["component:" + label], [
                    before("nettle", "OELAdjacentSyncope"),
                    before("little", "OELAdjacentSyncope")])
                    for label in ("AF66Good", "AF66Heavy")},
                "closed_kettle": {label: batch_apply_down(bins["component:" + label], [
                    "*ʧ*ie*t*i*l"])
                    for label in ("AF66Good", "AF66Closed")},
                "closed_kettle_scope": "Early WS post-apocope historical stage, not a selected/primary-certified complete kettle cell.",
                "shortening": {label: batch_apply_down(bins["component:" + label], [
                    before("fright", "OEMedLongShort")])
                    for label in ("AF117Good", "AF117Final")},
                "w_scope": {label: batch_apply_down(bins["component:" + label], [
                    before("sea", "OEWLossBeforeI"),
                    before("dew", "OEWLossBeforeI"), "*p*y*l*w*ī"])
                    for label in ("AF54Good", "AF54Post", "AF54Short", "AF54All")},
                "n_scope": {label: batch_apply_down(bins["component:" + label], [
                    before("fright", "NWGmcInStemNLoss"),
                    before("heaven", "NWGmcInStemNLoss")])
                    for label in ("AF64Good", "AF64All")},
                "pgmc_accusative_gate": batch_apply_down(
                    bins["component:EnglishProtoInput"],
                    [little["reconstruction"].strip("*")[:-2] + "anz"]),
            }
        report[name] = value
print(json.dumps(report, ensure_ascii=False))

"""Fresh, assertion-directed controls for the source-backed SC037 intervention."""

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from unittest.mock import patch

sys.path.insert(0, "/usr/app/tools")
from anglo_frisian_experiments import (
    compile_isolated, complete_variant_order, corpus_rows, prepare_definition_image,
)
import entry_stages
from executable_facts import parse_defines
from oe_trace_parse import (
    SOURCE_PATHS, parse_entries, parse_fidelity, provenance_problems, structural_problems,
)
from sound_change_order_sensitivity import batch_apply_down


COMPOUNDS = ("sáli-wàrðaz", "sáli-wàrðuz", "sáli-wàrðą")
FORMS = (*COMPOUNDS, "wíduwōn", "knéwai", "fūliθǭ", "spénnilǭ", "régna-bùgô")
STAGED = [
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
COMPONENTS = [
    "EnglishProtoInput", "OEBreaking", "OEIUmlaut", "OEHighVowelApocope",
    "OEMedialSyncope", "OEHighLinkSyncope", "OEHighStressDecode",
    "AFHighHandling", "OELAdjacentSyncope", "PGmcBAllophony",
    "OEStripSecondaryStress", "NWGmcInStemNLoss", "OEWLossBeforeI",
]
CLOSEOUT_RULES = {
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


def execution_plan(request):
    if request == "dart":
        return {"current": {"forms": [], "selected": False, "staged": [],
                            "components": [], "tails": ["AF66Good", "AF66Closed"]}}
    if request != "full":
        raise ValueError(f"unknown SC037 request: {request}")
    dependencies = {
        "current": (list(FORMS), [item["id"] for item in STAGED]),
        "old-early": (list(COMPOUNDS), []),
        "bad-breaking": (list(COMPOUNDS), []),
        "no-weight": ([*COMPOUNDS, "wíduwōn"], ["companion"]),
        "no-high": (["fūliθǭ", "spénnilǭ"], ["furthest", "companion"]),
        "early-high": (["fūliθǭ", "spénnilǭ"], []),
        "late-high": (["spénnilǭ"], []),
        "no-n-loss": ([], ["early-fright", "early-pillow"]),
        "late-n-loss": ([], ["late-livestock"]),
        "old-w-loss": ([], ["early-pillow"]),
        "early-b": (["régna-bùgô"], []),
        "no-unrounding": ([], ["companion"]),
        "opaque-umlaut": ([], ["furthest"]),
    }
    return {name: {
        "forms": forms, "selected": name == "current", "staged": staged,
        "components": COMPONENTS[:] if name == "current" else [],
        "tails": list(CLOSEOUT_RULES) if name == "current" else [],
    } for name, (forms, staged) in dependencies.items()}


def before(entries, fidelity, row, stage):
    if fidelity is None:
        raise ValueError("required raw fidelity section is missing")
    key = (row["concept"], row["proto"], row["counterpart"])
    entry = entries[key]
    matches = [i for i, item in enumerate(entry.stages) if item.label == stage]
    if len(matches) != 1 or matches[0] == 0:
        raise ValueError(f"{row['concept']}: missing/ambiguous required checkpoint {stage}")
    previous = entry.stages[matches[0] - 1]
    raw = fidelity.get(key, {}).get(previous.label, {})
    # The canonical sparse fidelity section records only raw/display differences.
    values = raw.get("raw") or previous.forms
    if raw.get("rejected") or len(values) != 1 or values[0] == "+?":
        raise ValueError(f"{row['concept']}: required raw checkpoint is missing/rejected/ambiguous")
    return values[0]


def selected_definitions(text, requested):
    definitions = parse_defines(text)
    needed = set(requested) & definitions.keys()
    while True:
        expanded = needed | {
            token for name in needed
            for token in re.findall(r"\b[A-Za-z][A-Za-z0-9_]*\b", definitions[name].body)
            if token in definitions}
        if expanded == needed:
            break
        needed = expanded
    return "\n".join(f"define {name} {definition.body};"
                     for name, definition in definitions.items() if name in needed)


def run_controls(request, profile):
    plan = execution_plan(request)
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
    closeout_helpers = """
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
    rows = corpus_rows(source.parent.parent / "data/germanic-aligned-final.tsv")
    by_concept = {row["concept"]: row for row in rows}
    little = by_concept["little"]
    coverage_finish = {concept: by_concept[concept] for concept in
                       (("dart",) if request == "dart" else ("livestock", "dart"))}
    plan["current"]["forms"].extend(
        ([coverage_finish["dart"]["fst_input"]] if request == "dart" else
         [little["fst_input"], *(row["fst_input"] for row in coverage_finish.values())]))
    trace_text = Path("/usr/app/docs/debug_snapshots/oe_full_trace_report.txt").read_text()
    problems = structural_problems(trace_text)
    # The container mounts Germanic at /usr/app and the backend at the same root.
    hashes = {label: hashlib.sha256(
        (source.parent.parent / relative.removeprefix("Germanic/").removeprefix("backend/")).read_bytes()
    ).hexdigest() for label, relative in SOURCE_PATHS.items()}
    problems.extend(provenance_problems(trace_text, hashes, require_version=2))
    if problems:
        raise ValueError("unusable canonical trace: " + "; ".join(problems))
    entries, fidelity = parse_entries(trace_text), parse_fidelity(trace_text)
    profile["checkpoints"] = []

    def checkpoint(concept, stage):
        value = before(entries, fidelity, by_concept[concept], stage)
        profile["checkpoints"].append({"concept": concept, "stage": stage, "input": value})
        return value

    with patch.object(entry_stages, "STAGE_METADATA_PATH",
                      source.parent.parent / "data/entry_stage_metadata.tsv"):
        sidecar = entry_stages.load_stage_metadata()
    profile["entry_stages"] = {}
    for row in (rows if request == "full" else [coverage_finish["dart"]]):
        proto, selected, variety, notes = entry_stages.resolve_stages(
            row["id"], row["reconstruction"], row["proto"], sidecar)
        if notes:
            raise ValueError(f"{row['id']}: unresolved selected input stage: {notes}")
        profile["entry_stages"][row["id"]] = {
            "proto": proto, "selected": selected, "variety": variety,
            "input": row["fst_input"], "context": row["input_context"]}
    order = complete_variant_order({"replace": {}, "insert_rule": None, "insert_after": None})
    closeout = closeout_helpers
    for label in plan["current"]["tails"]:
        stage, replacement = CLOSEOUT_RULES[label]
        tail = [replacement, *order[order.index(stage) + 1:]]
        closeout += "define " + label + " [" + " .o. ".join(tail) + "];\n"
    replacements = {
        "current": {}, "old-early": {"OECompoundLinkingSyncope": "AFOld037"},
        "bad-breaking": {"OEBreaking": "AFBadBr"},
        "no-weight": {"OEHighVowelApocope": "AFNoWeight"},
        "no-high": {"OEHighVowelApocope": "AFNoHigh"},
        "early-high": {"OEHighVowelApocope": "AFNoHigh"},
        "late-high": {"OEHighVowelApocope": "AFNoHigh"},
        "no-n-loss": {"NWGmcInStemNLoss": "AFNoHigh"},
        "late-n-loss": {"NWGmcInStemNLoss": "AFNoHigh"},
        "old-w-loss": {"OEWLossBeforeI": "AFOldW"},
        "early-b": {"PGmcBAllophony": "AFNoHigh"},
        "no-unrounding": {"OEHighLinkSyncope": "AFNoHigh"},
        "opaque-umlaut": {"OEIUmlaut": "AFOpaqueUm"},
    }
    insertions = {
        "early-high": ("AFEarlyHigh", "OEWsPalatalDiphthongization"),
        "late-high": ("AFLateHigh", "OEPreconsonantalDegemination"),
        "late-n-loss": ("AFLateN", "OEHighVowelApocope"),
        "early-b": ("AFEarlyB", "OESecondaryNasalization"),
    }
    report = {}
    profile.update(plan=plan, models=[], lookups=[], networks=Counter())
    with tempfile.TemporaryDirectory(prefix="capr-sc037-controls-") as temporary:
        root = Path(temporary)
        profile["phase"] = "definitions"
        started = time.perf_counter()
        image = prepare_definition_image(source, root)
        profile["definition_preparation_seconds"] = time.perf_counter() - started
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        for name, requested in plan.items():
            directory = root / name
            directory.mkdir()
            insert_rule, insert_after = insertions.get(name, ("AFPass", "EnglishProtoInput"))
            recipe = {
                "replace": replacements[name], "id": name, "insert_rule": insert_rule,
                "insert_after": insert_after,
                "staged_checks": [item for item in STAGED if item["id"] in requested["staged"]],
                "component_checks": [{"component": member}
                                     for member in [*requested["components"], *requested["tails"]]],
            }
            wanted = [insert_rule, *replacements[name].values(),
                      *requested["components"], *requested["tails"]]
            recipe["definitions"] = selected_definitions(
                extra + (closeout if name == "current" else ""), wanted)
            profile["phase"] = name
            started = time.perf_counter()
            bins = compile_isolated(source, recipe, [], directory,
                                    include_final=bool(requested["forms"]))
            inventory = {
                "roots": int("final" in bins),
                "staged": len({path for key, path in bins.items() if key.startswith("staged:")}),
                "components": len(requested["components"]), "tails": len(requested["tails"]),
            }
            profile["networks"].update(inventory)
            profile["models"].append({
                "variant": name, "recipe": recipe, "networks": inventory,
                "seconds": time.perf_counter() - started,
                "exports": {key: path.name for key, path in bins.items()}})

            def apply(binary, forms):
                outputs = batch_apply_down(binary, forms)
                profile["lookups"].append({
                    "variant": name, "bin": binary.name, "inputs": list(forms), "outputs": outputs})
                return outputs

            value = {}
            if requested["forms"]:
                value["canonical"] = dict(zip(
                    requested["forms"], apply(bins["final"], requested["forms"])))
            for item in recipe["staged_checks"]:
                outputs = apply(bins["staged:" + item["id"]], [item["input"]])
                if item["id"] in {"furthest", "companion", "heads"}:
                    value[item["id"]] = outputs
                else:
                    value.setdefault("blockers", {})[item["id"]] = outputs
            if name != "current":
                report[name] = value
                continue
            close = {
                "coverage_finish": {
                    concept: {"row_id": row["id"], "input": row["fst_input"],
                              "target": row["counterpart"]}
                    for concept, row in coverage_finish.items()},
                "closed_dart": {
                    label: apply(bins["component:" + label], [
                        checkpoint("dart", "OELAdjacentSyncope")])
                    for label in ("AF66Good", "AF66Closed")},
            }
            value["lexical_closeout"] = close
            if request == "dart":
                report[name] = value
                continue
            value["breaking"] = apply(bins["component:OEBreaking"], [
                "*f*u*l*w*i*x*t", "*n*a*w*i*x*t", "*s*i*w", "*s*í*w",
                "*b*i*r*x*t", "*w*i*w*i", "*w*i*w*ī",
                "*s*æ*l*ì*w*æ*r*d", "*ᶠ*b*i*s*i*w"])
            value["high"] = apply(bins["component:AFHighHandling"], [
                "*s*e*l*i*w*ea*r*d", "*x*a*n*d*u*s*ea*x",
                "*ȳ*t*y*m*i*s*t", "*b*o*n*d*i*n*s*t*a",
                "*ʃ*y*l*d*i*ç*ǣ*t*j*ā", "*l*a*n*d*w*ì*n*a"])
            value["umlaut"] = apply(bins["component:OEIUmlaut"], [
                "*ū*t*u*m*i", "*g*a*d*u*l*i*n*g", "*ū*t*a*m*i", "*ū*t*ù*m*i"])
            value["atomic_iu"] = apply(bins["component:EnglishProtoInput"], ["síu-wàrdaz"])
            stressed = ["*l*á*n*d*x*ù*m*i", "*l*á*n*d*w*ì*n*a"]
            for member in ("OEStripSecondaryStress", "OEBreaking", "OEIUmlaut",
                           "OEHighVowelApocope", "OEMedialSyncope",
                           "OEHighLinkSyncope", "OEHighStressDecode"):
                stressed = [outputs[0] for outputs in apply(bins["component:" + member], stressed)]
            value["stressed"] = stressed
            outputs = apply(bins["final"], [row["fst_input"] for row in rows])
            value["selected"] = [{**row, "outputs": output} for row, output in zip(rows, outputs)]
            value["fee"] = apply(bins["final"], ["féx", "féxu", "féxą"])
            for key, component, inputs in (
                ("n_loss", "NWGmcInStemNLoss", [
                    "*f*ú*r*x*t*ī*n", "*p*ú*l*w*ī*n", "*s*t*r*á*n*g*ī*n",
                    "*t*ú*n*g*a*n", "*s*t*ī*n", "*s*t*ḯ*n"]),
                ("w_loss", "OEWLossBeforeI", [
                    "*w*ī", "*s*w*ī", "*a*w*i", "*p*y*l*w*ī",
                    "*p*y*l*w*í", "*g*ea*r*w*i*d*e"]),
                ("weak", "OEHighLinkSyncope", [
                    "*y*n", "*g*æ*d*y*l*i*n*g", "*l*a*n*d*x*ỳ*m*i"]),
                ("light", "OELAdjacentSyncope", [
                    "*n*e*t*i*l*ǭ", "*g*æ*d*i*l*i*n*g", "*k*e*t*i*l",
                    "*a*θ*i*l*a", "*a*f*i*l*a"]),
                ("labial", "PGmcBAllophony", [
                    "*b*a", "*a*b*a", "*l*a*m*b", "*x*a*b*b*a",
                    "*r*e*g*n*b*o*g*ô", "*r*e*g*n*β*o*g*ô"]),
            ):
                value[key] = apply(bins["component:" + component], inputs)
            close["little"] = {"row_id": little["id"], "input": little["fst_input"],
                               "target": little["counterpart"]}
            for key, labels, inputs in (
                ("livestock_hll", ("AF63Good", "AF63Heavy", "AF63Hap"),
                 [checkpoint("livestock", "OEHighVowelApocope")]),
                ("livestock_shortening", ("AF117Good", "AF117Omitted"),
                 [checkpoint("livestock", "OEMedLongShort"), checkpoint("little", "OEMedLongShort")]),
                ("hll", ("AF63Good", "AF63Heavy", "AF63Hap"),
                 [checkpoint("little", "OEHighVowelApocope")]),
                ("light_root", ("AF66Good", "AF66Heavy"),
                 [checkpoint("nettle", "OELAdjacentSyncope"), checkpoint("little", "OELAdjacentSyncope")]),
                ("closed_kettle", ("AF66Good", "AF66Closed"), ["*ʧ*ie*t*i*l"]),
                ("shortening", ("AF117Good", "AF117Final"),
                 [checkpoint("fright", "OEMedLongShort")]),
                ("w_scope", ("AF54Good", "AF54Post", "AF54Short", "AF54All"),
                 [checkpoint("sea", "OEWLossBeforeI"), checkpoint("dew", "OEWLossBeforeI"), "*p*y*l*w*ī"]),
                ("n_scope", ("AF64Good", "AF64All"),
                 [checkpoint("fright", "NWGmcInStemNLoss"), checkpoint("heaven", "NWGmcInStemNLoss")]),
            ):
                close[key] = {label: apply(bins["component:" + label], inputs) for label in labels}
            close["closed_kettle_scope"] = (
                "Early WS post-apocope historical stage, not a selected/primary-certified complete kettle cell.")
            close["pgmc_accusative_gate"] = apply(
                bins["component:EnglishProtoInput"], [little["reconstruction"].strip("*")[:-2] + "anz"])
            report[name] = value
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", default="full")
    args = parser.parse_args()
    execution_plan(args.request)
    profile = {"request": args.request, "subprocesses": []}
    original_run = subprocess.run

    def measured(argv, *args, **kwargs):
        started = time.perf_counter()
        result = original_run(argv, *args, **kwargs)
        profile["subprocesses"].append({
            "command": Path(argv[0]).name, "phase": profile["phase"],
            "seconds": time.perf_counter() - started, "returncode": result.returncode})
        return result

    started = time.perf_counter()
    with patch.object(subprocess, "run", side_effect=measured):
        report = run_controls(args.request, profile)
    profile["seconds"] = time.perf_counter() - started
    profile["subprocess_counts"] = dict(Counter(item["command"] for item in profile["subprocesses"]))
    report["_execution"] = profile
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

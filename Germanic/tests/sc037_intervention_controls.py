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
    compile_isolated, complete_variant_order, corpus_rows, foma_domain, prepare_definition_image,
)
import entry_stages
from executable_facts import parse_defines
from flookup_records import parse_records
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


def reference_plan(request):
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


def model_definitions(source):
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
    return extra, closeout_helpers


def variant_edits():
    return {
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
    }, {
        "early-high": ("AFEarlyHigh", "OEWsPalatalDiphthongization"),
        "late-high": ("AFLateHigh", "OEPreconsonantalDegemination"),
        "late-n-loss": ("AFLateN", "OEHighVowelApocope"),
        "early-b": ("AFEarlyB", "OESecondaryNasalization"),
    }


def reference_controls(request, profile):
    plan = reference_plan(request)
    source = Path("/usr/app/fsts/germanic.txt")
    extra, closeout_helpers = model_definitions(source)
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
    replacements, insertions = variant_edits()
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
                "*s*æ*l*ì*w*ǽ*r*d", "*ᶠ*b*i*s*i*w"])
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


ASSERTION_GROUPS = {
    "test_canonical_compound_hypotheses_discriminate_three_wrong_accounts": "compound-full",
    "test_current_compounds_retain_outputs_and_weight_contrast": "compound",
    "test_independent_preoe_stages_test_weight_mutation_and_loss": "independent",
    "test_selected_weight_negative_and_previous_breaking_umlaut_histories": "selected",
    "test_weak_breaking_root_breaking_and_high_front_blockers": "breaking",
    "test_closed_medial_syllables_and_secondary_high_stress_are_preserved": "high",
    "test_selected_accusatives_discriminate_mutation_and_degemination_order": "order",
    "test_early_n_loss_preserves_later_livestock_and_inherited_fright": "n-loss",
    "test_pillow_requires_general_noninitial_w_loss_not_a_lexical_exemption": "pillow",
    "test_fee_transponent_is_not_a_new_post_h_deletion": "fee",
    "test_weak_unrounding_light_retention_and_positional_labials": "labial",
    "test_early_labial_realization_changes_rainbow": "early-b",
    "test_selected_little_protects_both_hll_vowels_against_wrong_deletions": "little",
    "test_inherited_livestock_plural_protects_shortening_dependency_and_hll": "livestock",
    "test_selected_dart_protects_closed_final_pre_l_nonapplication": "dart",
    "test_selected_nettle_has_live_open_medial_deletion": "nettle",
    "test_light_root_and_open_medial_conditions_have_distinct_controls": "light-root",
    "test_canonical_fright_and_heaven_discriminate_quantity_and_n_scope": "n-scope",
    "test_canonical_sea_dew_and_staged_pillow_discriminate_w_scope": "w-scope",
    "test_genuine_unselected_strong_plural_is_not_excluded_by_proto_gate": "gate",
}
EXTENDED_GROUPS = {"compound-full", "early-b"}
EXTENDED_TRIGGERS = {
    "old-early": "compound syncope, breaking or compound input hypotheses",
    "bad-breaking": "compound syncope, breaking or compound input hypotheses",
    "early-b": "placement of labial realization",
}


def probe_catalog():
    probes = []

    def add(identifier, groups, path, kind, inputs=(), variant="current", **extra):
        probes.append(dict(id=identifier, groups=groups.split(), path=[variant, *path.split("/")],
                           variant=variant, kind=kind, inputs=list(inputs), **extra))

    def raw(identifier, groups, forms, variant="current"):
        add(identifier, groups, "canonical", "raw", forms, variant, format="canonical")

    def component(identifier, groups, path, member, inputs):
        add(identifier, groups, path, "component", inputs, members=[member])

    def tail(identifier, groups, path, label, inputs):
        add(identifier, groups, "lexical_closeout/" + path + "/" + label,
            "tail", inputs, label=label)

    def checkpoint(concept, stage):
        return {"before": [concept, stage]}

    for variant in ("current", "old-early", "bad-breaking", "no-weight"):
        groups = "compound compound-full" if variant in {"current", "no-weight"} else "compound-full"
        raw("compound-" + variant, groups, COMPOUNDS, variant)
    raw("selected-current", "selected", FORMS[3:7])
    raw("selected-no-weight", "selected", ["wíduwōn"], "no-weight")
    for identifier in ("2141", "2016", "2006"):
        add("entry-" + identifier, "fee" if identifier == "2006" else "selected",
            "entries/" + identifier, "entry", row_id=identifier)
    for item in STAGED:
        groups = {"furthest": "independent", "companion": "independent labial",
                  "heads": "order", "late-livestock": "n-loss",
                  "early-fright": "n-loss", "early-pillow": "pillow"}[item["id"]]
        variants = {
            "furthest": ("current", "no-high", "opaque-umlaut"),
            "companion": ("current", "no-weight", "no-high", "no-unrounding"),
            "heads": ("current",), "late-livestock": ("current", "late-n-loss"),
            "early-fright": ("current", "no-n-loss"),
            "early-pillow": ("current", "old-w-loss", "no-n-loss"),
        }[item["id"]]
        for variant in variants:
            wanted = groups
            if item["id"] == "companion":
                wanted = "labial" if variant == "no-unrounding" else "independent"
            path = item["id"] if item["id"] in {"furthest", "companion", "heads"} else "blockers/" + item["id"]
            add("staged-" + item["id"] + "-" + variant, wanted, path, "staged",
                [item["input"]], variant, stage=item["stage"], side=item["side"],
                evidence=item["evidence"])
    for variant, forms in (
        ("early-high", ["fūliθǭ", "spénnilǭ"]), ("late-high", ["spénnilǭ"]),
        ("no-high", ["fūliθǭ", "spénnilǭ"]),
    ):
        raw("order-" + variant, "order", forms, variant)
    raw("rainbow", "labial early-b", ["régna-bùgô"])
    raw("rainbow-early-b", "early-b", ["régna-bùgô"], "early-b")
    add("fee", "fee", "fee", "raw", ["féx", "féxu", "féxą"])
    component("breaking", "breaking", "breaking", "OEBreaking", [
        "*f*u*l*w*i*x*t", "*n*a*w*i*x*t", "*s*i*w", "*s*í*w", "*b*i*r*x*t",
        "*w*i*w*i", "*w*i*w*ī", "*s*æ*l*ì*w*ǽ*r*d", "*ᶠ*b*i*s*i*w"])
    component("high", "high", "high", "AFHighHandling", [
        "*s*e*l*i*w*ea*r*d", "*x*a*n*d*u*s*ea*x", "*ȳ*t*y*m*i*s*t",
        "*b*o*n*d*i*n*s*t*a", "*ʃ*y*l*d*i*ç*ǣ*t*j*ā", "*l*a*n*d*w*ì*n*a"])
    component("umlaut", "high", "umlaut", "OEIUmlaut", [
        "*ū*t*u*m*i", "*g*a*d*u*l*i*n*g", "*ū*t*a*m*i", "*ū*t*ù*m*i"])
    component("atomic-iu", "high", "atomic_iu", "EnglishProtoInput", ["síu-wàrdaz"])
    add("stressed", "high", "stressed", "component",
        ["*l*á*n*d*x*ù*m*i", "*l*á*n*d*w*ì*n*a"],
        members=["OEStripSecondaryStress", "OEBreaking", "OEIUmlaut", "OEHighVowelApocope",
                 "OEMedialSyncope", "OEHighLinkSyncope", "OEHighStressDecode"], format="single")
    for identifier, groups, member, inputs in (
        ("n_loss", "n-loss", "NWGmcInStemNLoss", [
            "*f*ú*r*x*t*ī*n", "*p*ú*l*w*ī*n", "*s*t*r*á*n*g*ī*n",
            "*t*ú*n*g*a*n", "*s*t*ī*n", "*s*t*ḯ*n"]),
        ("w_loss", "pillow", "OEWLossBeforeI", [
            "*w*ī", "*s*w*ī", "*a*w*i", "*p*y*l*w*ī", "*p*y*l*w*í", "*g*ea*r*w*i*d*e"]),
        ("weak", "labial", "OEHighLinkSyncope", [
            "*y*n", "*g*æ*d*y*l*i*n*g", "*l*a*n*d*x*ỳ*m*i"]),
        ("light", "labial", "OELAdjacentSyncope", [
            "*n*e*t*i*l*ǭ", "*g*æ*d*i*l*i*n*g", "*k*e*t*i*l", "*a*θ*i*l*a", "*a*f*i*l*a"]),
        ("labial", "labial", "PGmcBAllophony", [
            "*b*a", "*a*b*a", "*l*a*m*b", "*x*a*b*b*a", "*r*e*g*n*b*o*g*ô", "*r*e*g*n*β*o*g*ô"]),
    ):
        component(identifier, groups, identifier, member, inputs)
    for concept, groups in (("little", "little livestock"), ("livestock", "livestock"),
                            ("dart", "dart")):
        path = "little" if concept == "little" else "coverage_finish/" + concept
        add("metadata-" + concept, groups, "lexical_closeout/" + path, "metadata", concept=concept)
        raw("endpoint-" + concept, groups, [{"row": concept}])
    for concept in ("dart", "nettle"):
        add("stage-" + concept, concept, "stages/" + concept, "stage",
            concept=concept, stage="OELAdjacentSyncope")
    raw("endpoint-nettle", "nettle", [{"row": "nettle"}])
    component("dart-stage-foil", "dart", "stages/dart/foil_after", "AFLClosed",
              [checkpoint("dart", "OELAdjacentSyncope")])
    for label in ("AF66Good", "AF66Closed"):
        tail("dart-" + label, "dart", "closed_dart", label,
             [checkpoint("dart", "OELAdjacentSyncope")])
    for name, groups, labels, inputs in (
        ("hll", "little", ("AF63Good", "AF63Heavy", "AF63Hap"),
         [checkpoint("little", "OEHighVowelApocope")]),
        ("livestock_hll", "livestock", ("AF63Good", "AF63Heavy", "AF63Hap"),
         [checkpoint("livestock", "OEHighVowelApocope")]),
        ("livestock_shortening", "livestock", ("AF117Good", "AF117Omitted"),
         [checkpoint("livestock", "OEMedLongShort"), checkpoint("little", "OEMedLongShort")]),
        ("light_root", "light-root", ("AF66Good", "AF66Heavy"),
         [checkpoint("nettle", "OELAdjacentSyncope"), checkpoint("little", "OELAdjacentSyncope")]),
        ("closed_kettle", "light-root", ("AF66Good", "AF66Closed"), ["*ʧ*ie*t*i*l"]),
        ("shortening", "n-scope", ("AF117Good", "AF117Final"),
         [checkpoint("fright", "OEMedLongShort")]),
        ("n_scope", "n-scope", ("AF64Good", "AF64All"),
         [checkpoint("fright", "NWGmcInStemNLoss"), checkpoint("heaven", "NWGmcInStemNLoss")]),
        ("w_scope", "w-scope", ("AF54Good", "AF54Post", "AF54Short", "AF54All"),
         [checkpoint("sea", "OEWLossBeforeI"), checkpoint("dew", "OEWLossBeforeI"), "*p*y*l*w*ī"]),
    ):
        for label in labels:
            tail(name + "-" + label, groups, name, label, inputs)
    component("gate", "gate", "lexical_closeout/pgmc_accusative_gate", "EnglishProtoInput",
              [{"accusative": "little"}])
    return probes


def execution_plan(request):
    groups = set(ASSERTION_GROUPS.values())
    if isinstance(request, str):
        if request == "routine":
            groups -= EXTENDED_GROUPS
        elif request != "full":
            if request not in groups:
                raise ValueError(f"unknown SC037 request: {request}")
            groups = {request}
        owners = sorted(name for name, group in ASSERTION_GROUPS.items() if group in groups)
    else:
        owners = sorted(request)
        if not owners:
            raise ValueError("empty SC037 assertion selection")
        unknown = [name for name in owners if name.split("::")[-1] not in ASSERTION_GROUPS]
        if unknown:
            raise ValueError("unmapped SC037 assertions: " + ", ".join(unknown))
        groups = {ASSERTION_GROUPS[name.split("::")[-1]] for name in owners}
    probes = [probe for probe in probe_catalog() if groups.intersection(probe["groups"])]
    compiled = [p for p in probes if p["kind"] not in {"metadata", "entry", "stage"}
                and not (p["kind"] == "raw" and p["variant"] == "current")]
    return {"assertion_owners": owners, "groups": sorted(groups), "probes": probes,
            "compilation_required": bool(compiled),
            "variants": sorted({p["variant"] for p in compiled})}


def result_at(report, path):
    try:
        for key in path:
            report = report[key]
    except (KeyError, TypeError) as exc:
        raise ValueError("missing required SC037 result: " + "/".join(path)) from exc
    return report


def validate_results(request, report):
    plan = execution_plan(request)
    try:
        evaluated = report["_execution"]["evaluated"]
    except (KeyError, TypeError) as exc:
        raise ValueError("missing evaluated SC037 probes") from exc
    if set(evaluated) != {p["id"] for p in plan["probes"]}:
        raise ValueError("missing/unexpected evaluated SC037 probes")
    for probe in plan["probes"]:
        result_at(report, probe["path"])


def put_result(report, path, value):
    for key in path[:-1]:
        report = report.setdefault(key, {})
    if path[-1] in report and isinstance(value, dict):
        report[path[-1]].update(value)
    else:
        report[path[-1]] = value


def bounded_expression(members, forms):
    expression = " .o. ".join(members)
    if "" not in forms:
        return foma_domain(forms) + " .o. " + expression, forms
    # flookup's blank input is a separator, not an epsilon query.
    labels = ["capr" + str(i) for i in range(len(forms))]
    adapter = " | ".join(
        "[" + foma_domain([label]) + " : " + (foma_domain([form]) if form else "0") + "]"
        for label, form in zip(labels, forms))
    return "[" + adapter + "] .o. " + expression, labels


def run_controls(request, profile, *, definition_mode="auto"):
    from capr_runtime import check_build_manifest, layout
    import oe_pipeline

    if definition_mode not in {"auto", "session", "full-source"}:
        raise ValueError("unknown SC037 definition mode: " + definition_mode)
    plan = execution_plan(request)
    rt = layout()
    profile["phase"] = "canonical manifest"
    problems = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    if problems:
        raise ValueError("unusable canonical SC037 bins: " + "; ".join(problems))
    rows = corpus_rows(rt.corpus_tsv)
    by_concept, by_id = ({r["concept"]: r for r in rows}, {r["id"]: r for r in rows})
    stages = oe_pipeline.stages()
    cache, report = {}, {}
    profile.update(plan=plan, evaluated=[], models=[], lookups=[], checkpoints=[],
                   definition_preparation_seconds=0, definition_image_origin="none",
                   definition_mode=definition_mode)

    def apply(binary, forms, probe):
        outputs = batch_apply_down(binary, forms)
        if len(outputs) != len(forms):
            raise ValueError("missing required SC037 lookup results: " + probe)
        profile["lookups"].append({
            "probe": probe, "bin": binary.name, "inputs": forms, "outputs": outputs})
        return outputs

    def stage_record(concept, identifier):
        key = (concept, identifier)
        if key not in cache:
            matches = [i for i, stage in enumerate(stages) if stage.foma_identifier == identifier]
            if len(matches) != 1 or matches[0] == 0 or stages[matches[0] - 1].kind != "named":
                raise ValueError("missing/ambiguous required live SC037 checkpoint: " + identifier)
            index = matches[0]
            form = by_concept[concept]["fst_input"]
            before_stage, after_stage = stages[index - 1], stages[index]
            # Preserve epsilon intermediates rather than treating them as rejection.
            def raw_stage(stage):
                proc = subprocess.run(["flookup", "-i", str(rt.bin_dir / stage.snapshot_bin)],
                                      input=(form + "\n").encode(), capture_output=True, check=True)
                try:
                    outputs = parse_records(proc.stdout.decode(), form)
                except ValueError as exc:
                    raise ValueError("invalid live SC037 checkpoint result: " + str(exc)) from exc
                profile["lookups"].append({
                    "probe": concept + ":" + identifier, "bin": stage.snapshot_bin,
                    "inputs": [form], "outputs": [outputs]})
                return outputs
            cache[key] = {"input": form, "stage": identifier,
                          "before": raw_stage(before_stage), "after": raw_stage(after_stage)}
            profile["checkpoints"].append({"concept": concept, **cache[key]})
        return cache[key]

    def inputs_for(probe):
        groups = []
        for item in probe["inputs"]:
            if isinstance(item, str):
                groups.append([item])
            elif "before" in item:
                groups.append(stage_record(*item["before"])["before"])
            elif "row" in item:
                groups.append([by_concept[item["row"]]["fst_input"]])
            else:
                row = by_concept[item["accusative"]]
                groups.append([row["reconstruction"].strip("*")[:-2] + "anz"])
        return groups

    pending = {}
    profile["phase"] = "production and stage lookups"
    for probe in plan["probes"]:
        kind = probe["kind"]
        if kind == "metadata":
            row = by_concept[probe["concept"]]
            value = {"row_id": row["id"], "input": row["fst_input"], "target": row["counterpart"]}
        elif kind == "stage":
            value = dict(stage_record(probe["concept"], probe["stage"]))
        elif kind == "entry":
            row = by_id[probe["row_id"]]
            value = {**row, "outputs": apply(
                rt.bin_dir / "old_english.bin", [row["fst_input"]], probe["id"])[0]}
        elif kind == "raw" and probe["variant"] == "current":
            forms = [group[0] for group in inputs_for(probe)]
            outputs = apply(rt.bin_dir / "old_english.bin", forms, probe["id"])
            value = dict(zip(forms, outputs)) if probe.get("format") == "canonical" else outputs
        else:
            pending.setdefault(probe["variant"], []).append((probe, inputs_for(probe)))
            continue
        put_result(report, probe["path"], value)
        profile["evaluated"].append(probe["id"])

    with patch.object(entry_stages, "STAGE_METADATA_PATH", rt.data_dir / "entry_stage_metadata.tsv"):
        sidecar = entry_stages.load_stage_metadata()
    profile["entry_stages"] = {}
    used = {item["row"] for p in plan["probes"] for item in p["inputs"]
            if isinstance(item, dict) and "row" in item}
    for concept in used:
        row = by_concept[concept]
        proto, selected, variety, notes = entry_stages.resolve_stages(
            row["id"], row["reconstruction"], row["proto"], sidecar)
        if notes:
            raise ValueError("unresolved SC037 selected input stage: " + str(notes))
        profile["entry_stages"][row["id"]] = {
            "proto": proto, "selected": selected, "variety": variety,
            "input": row["fst_input"], "context": row["input_context"]}
    if not pending:
        profile["networks"] = {"production": 1, "bounded": 0}
        return report
    extra, helpers = model_definitions(rt.germanic_fst)
    replacements, insertions = variant_edits()
    canonical_order = complete_variant_order({"replace": {}, "insert_rule": None, "insert_after": None})
    with tempfile.TemporaryDirectory(prefix="capr_sc037_selected_") as temporary:
        root = Path(temporary)
        if definition_mode == "full-source":
            profile["definition_image_origin"] = "full-source"
        elif os.environ.get("CAPR_FOMA_DEFINITION_IMAGE"):
            profile["definition_image_origin"] = "session"
        elif definition_mode == "session":
            raise ValueError("SC037 requires the selected session definition image")
        else:
            profile["phase"] = "definitions"
            started = time.perf_counter()
            image = prepare_definition_image(rt.germanic_fst, root)
            profile["definition_preparation_seconds"] = time.perf_counter() - started
            if image:
                os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
            profile["definition_image_origin"] = "worker"
        selected_image = (os.environ.get("CAPR_FOMA_DEFINITION_IMAGE")
                          if definition_mode != "full-source" else None)
        profile["definition_image_receipt"] = (
            json.loads(Path(selected_image).with_suffix(".json").read_text())
            if selected_image else None)
        profile["isolated_wrapper_flag"] = os.environ.get("CAPR_AF_DEFINITION_ISOLATED")
        for name, probes in pending.items():
            directory = root / name
            directory.mkdir()
            insert_rule, insert_after = insertions.get(name, ("AFPass", "EnglishProtoInput"))
            recipe = {"id": name, "replace": replacements[name], "insert_rule": insert_rule,
                      "insert_after": insert_after, "component_checks": []}
            order = complete_variant_order(recipe)
            expressions, requested, work = [], [], []
            for number, (probe, input_groups) in enumerate(probes):
                if probe["kind"] == "raw":
                    members = order
                elif probe["kind"] == "staged":
                    anchor = replacements[name].get(probe["stage"], probe["stage"])
                    if order.count(anchor) != 1:
                        raise ValueError("missing/ambiguous staged SC037 entry: " + anchor)
                    start = order.index(anchor) + (probe["side"] == "after")
                    members = order[start:]
                elif probe["kind"] == "tail":
                    anchor, replacement = CLOSEOUT_RULES[probe["label"]]
                    members = [replacement, *canonical_order[canonical_order.index(anchor) + 1:]]
                else:
                    members = probe["members"]
                forms = list(dict.fromkeys(form for group in input_groups for form in group))
                expression, lookup_inputs = bounded_expression(members, forms)
                identifier = "AFSelected" + str(number)
                expressions.append(f"define {identifier} [{expression}];")
                requested.extend(members)
                recipe["component_checks"].append({"component": identifier})
                work.append((probe, input_groups, forms, lookup_inputs, identifier, members))
            recipe["definitions"] = selected_definitions(extra + helpers, requested) + "\n" + "\n".join(expressions)
            profile["phase"] = name + " compilation"
            started = time.perf_counter()
            bins = compile_isolated(
                rt.germanic_fst, recipe, [], directory, components_only=True,
                use_definition_image=definition_mode != "full-source")
            script = (directory / "experiment.foma").read_text()
            loaded = script.startswith("load defined ")
            profile["models"].append({
                "variant": name, "seconds": time.perf_counter() - started,
                "image_supplied": bool(selected_image),
                "image_loaded": loaded, "fallback": not loaded,
                "recipe": {**recipe, "definitions": selected_definitions(extra + helpers, requested)},
                "queries": [{"id": p["id"], "members": members, "inputs": forms,
                             "lookup_inputs": actual, "input_groups": groups}
                            for p, groups, forms, actual, _, members in work]})
            profile["phase"] = name + " lookups"
            for probe, groups, forms, actual, identifier, members in work:
                outputs = apply(bins["component:" + identifier], actual, probe["id"])
                by_form = dict(zip(forms, outputs))
                values = [list(dict.fromkeys(out for form in group for out in by_form[form]))
                          for group in groups]
                if probe.get("format") == "canonical":
                    value = {form: by_form[form] for form in forms}
                elif probe.get("format") == "single":
                    if any(len(result) != 1 for result in values):
                        raise ValueError("ambiguous/rejected required singleton SC037 probe")
                    value = [result[0] for result in values]
                else:
                    value = values
                put_result(report, probe["path"], value)
                profile["evaluated"].append(probe["id"])
    profile["networks"] = {"production": 1, "bounded": len([
        p for probes in pending.values() for p in probes])}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", default="full")
    parser.add_argument("--tests", help="JSON array of actually selected pytest node IDs")
    parser.add_argument("--reference", action="store_true", help="run the preserved PR13/14 compiler")
    parser.add_argument("--definitions", choices=("auto", "session", "full-source"), default="auto",
                        help="standalone auto preparation, required session image, or no image")
    args = parser.parse_args()
    if args.reference and args.definitions != "auto":
        parser.error("--definitions applies only to the current worker")
    request = json.loads(args.tests) if args.tests else args.request
    (reference_plan if args.reference else execution_plan)(request)
    profile = {"request": request, "subprocesses": []}
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
        report = (reference_controls(request, profile) if args.reference else
                  run_controls(request, profile, definition_mode=args.definitions))
    profile["seconds"] = time.perf_counter() - started
    profile["subprocess_counts"] = dict(Counter(item["command"] for item in profile["subprocesses"]))
    report["_execution"] = profile
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

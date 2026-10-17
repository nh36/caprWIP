#!/usr/bin/env python3
"""Build research hypotheses, never compile them or select lexical witnesses.

After historical verification:
  python3 build_recipes.py --witnesses WITNESSES.tsv --probes probes.json \
      --already-long-probe LEAD_SUPPLIED_ID --output recipes.json

probes.json is either the driver's probe list or an object containing "probes"
and optionally "already_long_probe_ids". All forms, attestations and historical
metadata must be supplied by the lead. --recipe ID can select bounded batches;
without it all21 candidate/representation/duration controls are emitted.
Deferred merger defaults to before MonosyllabicFinalZLoss, before its explicit
e/é compensatory-lengthening clauses. --deferred-merge-before OEBreaking is
an explicitly labelled representation-stress control, not a safe equivalent.

Hill2017 pp.137–149,153–158 is the hypothesis under examination, not evidence
that every conditioning clause, date or input below has been independently
established. No new phoneme, lexical reconstruction or chronology edge is adopted.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import experiment as driver

BASE_COMMIT = "c92cbd9d541785986998ab2ab99a416f87da4f68"
EXPECTED_SOURCES = {
    "germanic_fst": "da04db7a21664bf9a606e331c5dd484a023d00e00a5ecf7c19ea3e8e310789e9",
    "corpus_tsv": "514cfe096b636ea6790361787a154a70e6dafb7d8bf3e4936fced51f3b1b2a6f",
}
LOWER = "PNWGmcILowering"
EARLY = "PNWGmcLongELowering"
FRONT = "EAFLongAFronting"
BREAKING = "OEBreaking"
ZLOSS = "MonosyllabicFinalZLoss"
HYPOTHESIS = (
    "Hill2017 pp.137–149,153–158: proposed lowering and monosyllabic "
    "lengthening hypotheses only; inherited-r restriction, precise executable "
    "domain and dating remain assumptions to assess against the supplied witnesses."
)
REPRESENTATIONS = {
    "existing": {
        "short": ("e", "é"), "long": "ē",
        "description": "Existing short e/é; newly lengthened e uses ē, never early ē₁-tier ḗ.",
    },
    "explicit": {
        "short": ("ẹ", "ḙ"), "long": "ệ",
        "description": (
            "Explicit lowered close-mid short ẹ, acute-tier surrogate ḙ, "
            "long surrogate ệ; all labels are single Unicode scalars. "
            "Neither the spelling ḙ/ệ nor its diacritics assert a phoneme or "
            "a phonetic value beyond the declared technical serialization."
        ),
    },
    "origin": {
        "short": ("ị", "ỉ"), "long": "ē",
        "description": (
            "Transient lowered-origin short labels ị/plain and ỉ/acute, not "
            "new reconstructed phonemes; lengthening enters existing ē directly."
        ),
    },
}


def insert(rule, target, side="before"):
    return {"action": "insert", "rule": rule, "target": target, "side": side}


def replace(target, rule):
    return {"action": "replace", "target": target, "rule": rule}


def lowering_component(body, component):
    if component == "unified":
        return body
    environment = re.compile(
        r"\[\{\*z\}\s+\[EnglishStarConsonant\s+\|\s+\.\#\.\]"
        r"\s+\|\s+\{\*s\}\s+\{\*t\}\s+\|\s+\{\*r\}\]"
    )
    replacement = "{*r}" if component == "r" else "[{*z} [EnglishStarConsonant | .#.] | {*s} {*t}]"
    result, count = environment.subn(lambda _match: replacement, body)
    driver.require(count == 2, "canonical SC015 environment changed; cannot derive split components")
    return result


def represented_lowering(body, representation):
    plain, acute = REPRESENTATIONS[representation]["short"]
    for old, new in (("{*i} -> {*e}", "{*i} -> {*" + plain + "}"),
                     ("{*í} -> {*é}", "{*í} -> {*" + acute + "}")):
        driver.require(body.count(old) == 1, "source-derived lowering clause changed")
        body = body.replace(old, new, 1)
    return body


def lengthening(representation, collision=False):
    short = REPRESENTATIONS[representation]["short"]
    long = REPRESENTATIONS[representation]["long"]
    mappings = [("a", "ā"), ("á", "ā"), ("e", long), ("é", "ḗ" if collision else long),
                ("i", "ī"), ("í", "ḯ"), ("o", "ō"), ("ó", "ō"),
                ("u", "ū"), ("ú", "ū"), ("y", "ȳ"), ("æ", "ǣ")]
    if representation != "existing":
        mappings.extend((symbol, long) for symbol in short)
    rules = ",\n    ".join(
        "{*" + source + "} -> {*" + target + "}" for source, target in mappings)
    # Context-bearing weak words are identity paths, not lengthening inputs.
    return (
        "[ [?* [{*ᵘ}|{*ᶜ}] ?*] | "
        "[ [EnglishStarAlphabet - [{*ᵘ}|{*ᶜ}]]* .o. [\n    "
        + rules + "\n    || .#. EnglishStarConsonant* _ {*r} .#.\n] ] ]"
    )


def merger(representation):
    plain, acute = REPRESENTATIONS[representation]["short"]
    rules = ["{*" + plain + "} -> {*e}", "{*" + acute + "} -> {*é}"]
    if representation == "explicit":
        rules.append("{*ệ} -> {*ē}")
    return "[ " + ", ".join(rules) + " ]"


def class_extensions(text, bodies, representation):
    if representation == "existing":
        return [], [], {}
    plain, acute = REPRESENTATIONS[representation]["short"]
    long = ["ệ"] if representation == "explicit" else []
    short = [plain, acute]
    memberships = {
        "PGmcStarVowel": short + long,
        "PGmcStarFrontVowel": short + long,
        "PGmcStarAcuteVowel": [acute],
        "PGmcStarStressedVowel": [acute] + long,
        "EnglishStarShortVowel": short,
        "EnglishStarNonHighVowel": short + long,
    }
    if long:
        memberships["EnglishStarLongVowel"] = long
    changes, consumers_by_class = [], {}
    for name, symbols in memberships.items():
        anchor = "define " + name + " ["
        driver.require(name in bodies and text.count(anchor) == 1,
                       f"expected unique source class declaration: {name}")
        consumers = sorted(other for other, body in bodies.items()
                           if other != name and re.search(r"\b" + re.escape(name) + r"\b", body))
        consumers_by_class[name] = consumers
        changes.append({
            "old": anchor,
            "new": anchor + "\n    " + " | ".join("{*" + s + "}" for s in symbols) + " |",
            "reason": (
                f"Research-only {representation} membership in {name}; preserve "
                "plain/acute distinction, front-vowel and quantity behavior. "
                "The nonhigh extension deliberately exposes the same lowered "
                "vowel to PNWGmcULowering's following-vowel test. "
                "Long ệ shares ē's default-root-stress class, not its acute class."
            ),
            "consumers": [name] + consumers,
        })
    symbols = []
    roles = {
        plain: "plain-tier short lowered vowel" if representation == "explicit"
        else "plain-tier transient lowered-origin short vowel",
        acute: "acute-tier short lowered vowel" if representation == "explicit"
        else "acute-tier transient lowered-origin short vowel",
        "ệ": "single-scalar long close-mid technical label; merges to existing ē",
    }
    for symbol in short + long:
        classes = [name for name, members in memberships.items() if symbol in members]
        symbols.append({"symbol": symbol, "role": roles[symbol], "consumers": classes,
                        "class_memberships": classes})
    return changes, symbols, consumers_by_class


def make_recipe(text, bodies, architecture, placement, representation="existing",
                duration=None, reverse=False, collision=False):
    identifier = architecture.lower() + "-" + placement + "-" + representation
    if duration:
        identifier += "-" + duration
    if reverse:
        identifier += "-reverse"
    if collision:
        identifier += "-collision"
    changes, symbols, consumers = class_extensions(text, bodies, representation)
    definitions = {"XRLen": lengthening(representation, collision)}
    edits = []
    current_lower = LOWER
    if architecture == "C":
        definitions["XRLowerR"] = represented_lowering(
            lowering_component(bodies[LOWER], "r"), representation)
        definitions["XRLowerZS"] = represented_lowering(
            lowering_component(bodies[LOWER], "zst"), representation)
        edits.extend((replace(LOWER, "XRLowerZS"), insert("XRLowerR", EARLY)))
        current_lower = "XRLowerZS"
        edits.append(insert("XRLen", "XRLowerR", "after"))
    else:
        if representation != "existing":
            definitions["XRLower"] = represented_lowering(bodies[LOWER], representation)
            edits.append(replace(LOWER, "XRLower"))
            current_lower = "XRLower"
        if architecture == "B":
            edits.append({"action": "move", "rule": current_lower, "target": EARLY, "side": "before"})
            edits.append(insert("XRLen", current_lower, "before" if reverse else "after"))
        elif placement == "before-sc024":
            edits.append(insert("XRLen", EARLY))
        elif placement == "after-sc015":
            edits.append(insert("XRLen", current_lower, "after"))
        elif placement == "before-fronting":
            edits.append(insert("XRLen", FRONT))
        else:
            raise ValueError(f"unsupported placement: {placement}")
    if representation != "existing":
        definitions["XRMerge"] = merger(representation)
        if duration == "immediate":
            edits.append(insert("XRMerge", "XRLen", "after"))
            if architecture == "C":
                definitions["XRLateMerge"] = merger(representation)
                edits.append(insert("XRLateMerge", current_lower, "after"))
        elif duration in {"before-z-loss", "before-breaking"}:
            edits.append(insert("XRMerge", ZLOSS if duration == "before-z-loss" else BREAKING))
        else:
            raise ValueError("explicit/origin representation requires an explicit duration")
        for item in symbols:
            atom = "{*" + item["symbol"] + "}"
            item["consumers"] += [name for name, body in definitions.items() if atom in body]
    assumptions = [
        "Hypothesis, not adoption: consonant-only onset plus a single short nucleus "
        "and inherited final r at this stage; word-boundary .#. on both sides.",
        "Plain short first nuclei count as stressed citation roots; acute and plain "
        "serializations remain distinct. The rule is not a three-lexeme rewrite.",
        "The formal quality domain is oral a/e/i/o/u/y/æ and their available "
        "acute tiers, with existing long counterparts; o/u/y/æ are generality "
        "controls, not a claim that Hill independently attests each case. "
        "Reduced ĕ, secondary-stress grave vowels and nasal vowels are excluded.",
        "Weak context markers are identity paths while present. After "
        "PWGmcUnstressedWordFinalIApocope consumes weak-final marking, late "
        "placements cannot independently recover that lost word-stress metadata; "
        "interpret late stress-sensitive controls accordingly.",
        "Inherited-r identity is an ordering assumption: after EAFRhotacism a bare "
        "r could not distinguish its origin; these proposed anchors precede it.",
        "The explicit representation labels only lowered products, not every "
        "inherited short e; phonemic interpretation requires independent evidence.",
    ]
    if placement == "before-fronting":
        assumptions.append(
            "This later anchor follows rhotacism and several early losses. "
            "Consequently inherited-r identity is NOT enforced by the bare-r rule; "
            "rhotacized-r and newly monosyllabic controls test its overgeneration.")
        assumptions[4] = (
            "Late bare r is origin-insensitive: do not interpret a successful "
            "final output as evidence that its r was inherited.")
    if duration == "immediate":
        assumptions.append(
            "Short and explicit long labels merge immediately after lengthening; "
            "C separately merges newly produced late z/st lowering. Distinct-short "
            "duration is a declared implementation/chronology assumption.")
    elif duration == "before-z-loss":
        assumptions.append(
            "Short/long labels persist until immediately before MonosyllabicFinalZLoss, "
            "then merge before its explicit e/é compensatory-lengthening clauses, "
            "rhotacism, diphthong leveling, breaking and umlaut. Compare the "
            "immediate merger to test the distinct-short duration assumption.")
    elif duration == "before-breaking":
        assumptions.append(
            "Short/long labels persist until immediately before OEBreaking; "
            "all class memberships are extended for that interval. Explicit "
            "e/é breaking and later umlaut then see the merged native symbols. "
            "Compare immediate-merger recipe to expose duration effects.")
        assumptions.append(
            "Deliberate representation-stress control: MonosyllabicFinalZLoss "
            "is NOT extended for surrogate short labels. Final-z probes can "
            "therefore lose compensatory lengthening. Such a difference is a "
            "known representation effect, not evidence for historical chronology.")
    if collision:
        assumptions.append(
            "Deliberately naive collision control: acute é lengthens to ḗ before "
            "SC024; plain e lengthens to ē. This is not a proposed valid representation.")
    if architecture == "D":
        assumptions.append(
            "Comparator interpretation requires the lead's separately sourced "
            "already-long here probe, not selection of that input from fit. "
            "Later r-lengthening is a competing conditional account, not an approved law.")
    recipe = {
        "id": identifier, "architecture": architecture,
        "representation": REPRESENTATIONS[representation]["description"],
        "evidence": HYPOTHESIS, "assumptions": "\n".join(assumptions),
        "definitions": definitions, "source_replacements": changes, "symbols": symbols,
        "edits": edits, "representation_audit": {
            "implementation": representation, "short_merger_timing": duration or "not applicable",
            "direct_class_consumers": consumers,
            "input_stage": (
                "No pgrm input classes/mappings are extended: technical symbols "
                "are introduced after EnglishProtoInput only. Full-entry probes "
                "must use native input inventory; explicit technical inputs require "
                "declared stage-entry probes and are not native corpus reconstructions."
            ),
        },
    }
    if representation != "existing":
        order = driver.edited_order(driver.source_order(driver.layout().germanic_fst), recipe)
        starts = [order.index(name) for name in ("XRLower", "XRLowerR", "XRLowerZS") if name in order]
        end = order.index("XRMerge")
        recipe["representation_audit"]["crossed_native_literal_events"] = [
            {"event": event, "literals": [symbol for symbol in ("e", "é", "ē", "ḗ")
                                         if "{*" + symbol + "}" in bodies[event]]}
            for event in order[min(starts):end] if event in bodies and
            any("{*" + symbol + "}" in bodies[event] for symbol in ("e", "é", "ē", "ḗ"))
        ]
        recipe["representation_audit"]["literal_audit_limit"] = (
            "These exact native leaf expressions mention e-tier literals while "
            "technical labels may be present. Class extensions do not extend "
            "their literal rewrite clauses; applicability must be checked in "
            "the traces. This list is not a historical interaction claim."
        )
    return recipe


def hill_lengthen_then_lower_long_i(text, bodies):
    recipe = make_recipe(text, bodies, "A", "before-sc024")
    recipe["id"] = "hill-lengthen-then-lower-long-i"
    recipe["evidence"] = (
        "Hill2017 p.148 explicitly gives *hir > *hīr > *hẹ̄r as the "
        "alternative order; the rule and its domain here are an isolated "
        "formalization for testing, not an adopted sound change."
    )
    recipe["definitions"]["XRLongILower"] = (
        "[ {*ī} -> {*ē}, {*ḯ} -> {*ē} "
        "|| .#. EnglishStarConsonant* _ {*r} .#. ]"
    )
    recipe["edits"].append(insert("XRLongILower", "XRLen", "after"))
    recipe["assumptions"] += (
        "\nHill-order sensitivity: first lengthen short i to existing long ī/ḯ, "
        "then apply a separately stated long-ī lowering to long ē before final r. "
        "This operation is not SC015's adopted short-i lowering. It applies to "
        "all long ī/ḯ in the stated environment, not only newly lengthened "
        "adverb vowels; inspect all selected-row and negative-control effects. "
        "The output uses CAPR ē, distinct from inherited ē₁ serialization ḗ."
    )
    driver.validate({
        "schema_version": 1,
        "base_commit": BASE_COMMIT,
        "witness_sha256": "0" * 64,
        "pins": {key: driver.digest(path)
                 for key, path in driver.pin_paths(driver.layout()).items()},
        "recipes": [recipe],
        "probes": [],
    }, driver.layout().germanic_fst)
    return recipe


def build_spec(witness_sha256, probes, already_long_probe_ids=(), requested=(),
               deferred_merge_before=ZLOSS):
    runtime = driver.layout()
    pins = {key: driver.digest(path) for key, path in driver.pin_paths(runtime).items()}
    for key, expected in EXPECTED_SOURCES.items():
        driver.require(pins[key] == expected, f"pinned research source changed: {key}")
    text = runtime.germanic_fst.read_text(encoding="utf-8")
    bodies = driver.oe_pipeline._define_bodies(driver.oe_pipeline._strip_comments(text))
    recipes = [
        make_recipe(text, bodies, "A", placement)
        for placement in ("before-sc024", "after-sc015", "before-fronting")
    ]
    recipes.extend((
        make_recipe(text, bodies, "B", "before-sc024"),
        make_recipe(text, bodies, "C", "before-sc024"),
        make_recipe(text, bodies, "B", "before-sc024", reverse=True),
        make_recipe(text, bodies, "D", "before-fronting"),
        make_recipe(text, bodies, "B", "before-sc024", collision=True),
    ))
    recipes.append(hill_lengthen_then_lower_long_i(text, bodies))
    for architecture, placement in (("A", "after-sc015"), ("B", "before-sc024"), ("C", "before-sc024")):
        for representation in ("explicit", "origin"):
            driver.require(deferred_merge_before in {ZLOSS, BREAKING}, "unknown deferred merger anchor")
            delayed = "before-z-loss" if deferred_merge_before == ZLOSS else "before-breaking"
            for duration in ("immediate", delayed):
                recipes.append(make_recipe(text, bodies, architecture, placement, representation, duration))
    probe_ids = {probe["id"] for probe in probes}
    driver.require(set(already_long_probe_ids) <= probe_ids, "unknown already-long probe ID")
    for recipe in recipes:
        if recipe["architecture"] == "D":
            recipe["comparator_probe_ids"] = list(already_long_probe_ids)
            recipe["comparator_limitation"] = (
                "All probes are evaluated under every recipe; comparator IDs "
                "identify the lead's independently sourced alternative inputs, "
                "not a recipe-specific corpus input override."
            )
    if requested:
        driver.require(set(requested) <= {r["id"] for r in recipes}, "unknown requested recipe ID")
        recipes = [recipe for recipe in recipes if recipe["id"] in requested]
    specification = {
        "schema_version": 1, "base_commit": BASE_COMMIT,
        "witness_sha256": witness_sha256, "pins": pins, "recipes": recipes, "probes": probes,
    }
    driver.validate(specification, runtime.germanic_fst)
    return specification


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--witnesses", type=Path, required=True)
    parser.add_argument("--probes", type=Path, required=True)
    parser.add_argument("--already-long-probe", action="append", default=[])
    parser.add_argument("--recipe", action="append", default=[], help="emit only this ID; repeat for a batch")
    parser.add_argument("--deferred-merge-before", choices=(ZLOSS, BREAKING), default=ZLOSS)
    parser.add_argument("--output", type=Path, required=True, help="new recipes JSON path; never overwritten")
    args = parser.parse_args()
    driver.require(args.witnesses.is_file() and args.witnesses.stat().st_size > 0,
                   "source-verified witness table must already exist")
    data = json.loads(args.probes.read_text(encoding="utf-8"))
    probes = data["probes"] if isinstance(data, dict) else data
    long_ids = args.already_long_probe + (data.get("already_long_probe_ids", []) if isinstance(data, dict) else [])
    driver.require(isinstance(probes, list) and probes, "lead-supplied sourced probes required")
    if not args.recipe or "d-before-fronting-existing" in args.recipe:
        driver.require(long_ids, "nominate at least one independently sourced already-long comparator probe")
    result = build_spec(driver.digest(args.witnesses), probes, long_ids, args.recipe,
                        args.deferred_merge_before)
    driver.require(not args.output.exists() and args.output.parent.is_dir(), "output must be a new file")
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({"status": "validated_recipes_written_no_foma", "recipes": len(result["recipes"]),
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()

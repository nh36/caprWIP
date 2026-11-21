"""Build the opt-in comparative assay from the frozen labial review plan."""

import json
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().parents[1] / "labial_review" / "plan.json"
    previous = json.loads(source.read_text())
    old = previous["configurations"]
    gem = "PWGmcJGemination"
    oral = "PWGmcFinalBareALoss"
    nasal = "OEHeavySyllableNasalApocope"
    z = "EAFFinalZDeletion"
    final = "OldEnglishSurface"
    wloss = "OEWLossBeforeI"
    aw = "OEAwLongDiphthong"
    earlier = "OEIntervocalicJVocalization"
    late = "OEContraction"
    block = (
        "OEAwwjResolution", "OEAuBrightening", "OEEwLongDiphthong",
        "OEJWWSimplification", "OEJGlideIO", "OEDiphthongLeveling",
    )

    def move(rule, after):
        return {"move": rule, "after": after}

    def insert(rule, after):
        return {"insert": rule, "after": after}

    # Keep a distinct oral-after-gemination arm. This tests Boutkan's
    # Northern ordering, not his whole WGmc final-vowel or OHG analysis.
    north = old["split"] + [
        move(z, gem), move(oral, z), move("FON", oral),
        move(nasal, "FON"), move("FNU", nasal),
    ]
    placed = [move(rule, after) for after, rule in zip((gem, *block), block)]
    narrow = {"replace": aw, "with": "FWA"}
    arms = {
        "identity": [],
        "A": old["early"],
        "B": old["split"],
        "C_northern_order": north,
        "A_contraction": old["early"] + [insert("FII", wloss)],
        "A_late_contraction": old["early"] + [insert("FII", late)],
        "A_singleton_aw": old["early"] + [narrow],
        "live_singleton_aw": [narrow],
        "B_geminate_only": old["split_geminate_only"],
        "B_consumers_before_loss": old["split"] + placed,
        "C_consumers_before_loss": north + placed,
    }
    # The snapshot compiler reads definitions in insertion order.
    definitions = {
        name: previous["definitions"][name] for name in ("FW", "FNU", "FON", "FNG")
    }
    definitions["FII"] = "define FII [{*í} {*i} -> {*ḯ}];"
    definitions["FWA"] = """define FWA Ctx([
        {*a} {*w} -> {*ēa} {*w} || _ [[EnglishStarVocalic - [{*i}|{*ī}]] | {*ô}],
        {*á} {*w} -> {*ḗa} {*w} || _ [[EnglishStarVocalic - [{*i}|{*ī}]] | {*ô}]
    ]);"""
    probes = dict(zip(previous["probe_ids"],
                      previous["queries"][f"identity:cell:{final}"]["inputs"],
                      strict=True))
    probes.update({
        "bedd.dat.sg": "bádjai",
        "mene.neuter.proposal": "mánją",
        "mene.gen.sg.proposal": "mánjas",
        "mete.i_stem": "mátiz",
        "mete.gen.pl.analogical_ending_probe": "mátją",
        "glee.direct": "glíwją",
        "glee.protected": "glíwjas",
        "new.oral_direct": "níwjaz",
        "new.protected": "níwjas",
        "sea.direct": "sáiwiz",
        "show.inf": "skáwōjaną",
    })
    stages = [
        z, oral, nasal, "FON", "FNU", "FNG", gem, "PWGmcSyllabicJ",
        "EAFRhotacism", *block, aw, "EAFBrightening", "OEBreaking",
        "OEIUmlaut", wloss, "FII", earlier, "OEHighVowelApocope", late, final,
    ]
    queries = {}
    for arm, ops in arms.items():
        for stage in stages:
            if stage in definitions and not any(op.get("insert") == stage for op in ops):
                continue
            stop = "FWA" if stage == aw and narrow in ops else stage
            queries[f"{arm}:cell:{stage}"] = {
                "configuration": arm, "through": stop, "inputs": list(probes.values()),
            }
    queries["wloss.local"] = {
        "members": [wloss, "FII"],
        "inputs": [
            "*ç*í*w*i", "*g*l*í*w*i", "*n*í*w*i",
            "*p*í*w*i", "*p*í*w*í", "*p*i*w*i", "*p*ḯ*w*i",
            "*p*í*w*ī", "*p*é*w*i", "*p*í*w*j*a", "*p*í*i*t*i",
        ],
    }
    queries["contraction.local"] = {
        "members": ["FII"],
        "inputs": ["*p*í*i", "*p*í*í", "*p*i*i", "*p*í*ī", "*p*ḯ*i", "*p*í*i*n"],
    }
    queries["existing.contraction.local"] = {
        **queries["contraction.local"], "members": [late],
    }
    for arm in ("A", "A_singleton_aw"):
        for stage in (aw, "EAFBrightening", "OEIUmlaut", wloss, final):
            queries[f"{arm}:aw_local:{stage}"] = {
                "configuration": arm,
                "after": "OEDiphthongLeveling",
                "through": "FWA" if arm == "A_singleton_aw" and stage == aw else stage,
                "inputs": [
                    "*x*á*w*i", "*á*w*i*d*i", "*s*t*r*á*w*i*d*ē",
                    "*g*a*k*á*w*i*d*ē", "*s*k*á*w*ō*j*a*n*ą"
                ],
            }
    plan = {
        "purpose": "Compare early, split and Northern gemination-first apocope, with independent labial sensitivities.",
        "start_after": previous["start_after"],
        "configurations": arms,
        "definitions": definitions,
        "aliases": {
            name: {op["replace"]: op["with"] for op in ops if "replace" in op}
            for name, ops in arms.items()
        },
        "trace_concepts": [
            "net", "bed", "hay", "hue", "strew", "deer", "door", "there", "where",
            "hedge", "rest", "show", "sea",
        ],
        "complete_traces": list(arms),
        "census_stages": [
            "PNWGmcULowering", "PNWGmcMonosyllabicFinalRLengthening",
            "PWGmcEndinglessAw", aw, wloss,
        ],
        "probe_ids": list(probes),
        "queries": queries,
        "predictions": {
            "A": "Early oral and nasal apocope bleed direct-cell gemination; obliques remain eligible.",
            "B": "Early oral but post-gemination nasal loss; nasal direct cells geminate.",
            "C_northern_order": "Both endings survive gemination; oral secg joins nasal secg, without a proposed donor.",
            "FII": "Stressed short i plus unstressed short i yields stressed long i. Test immediately after w-loss versus a late control.",
            "FWA": "Exclude unstressed high front vowels from the tentative singleton-aw proxy; do not change the inherited or geminate-derived au route.",
            "placement": "Run the existing labial block before either newly exposed terminal ww+j faces vocalization. Test whether later conditioning survives without exception.",
        },
        "negative_controls": [
            "All 394 original selections, exact runtime identity, no corpus or registry edits.",
            "SC017, SC112 and SC111 censuses; no unlabelled final-z change.",
            "Nonhomorganic vowels, two stressed vowels, and existing long vowels do not undergo FII.",
        ],
    }
    if sys.argv[2:] == ["--placement-trace"]:
        traced_arms = (
            "B", "C_northern_order", "B_consumers_before_loss", "C_consumers_before_loss",
        )
        placement_arms = ("identity", *traced_arms)
        plan.update(
            purpose="Localize the two unrelated terminal differences in early labial placement",
            configurations={arm: arms[arm] for arm in placement_arms},
            aliases={arm: plan["aliases"][arm] for arm in placement_arms},
            trace_concepts=["believe", "straw"],
            complete_traces=list(traced_arms),
            census_stages=["PWGmcEndinglessAw"],
            queries={},
        )
    elif sys.argv[2:] == ["--source-integration"]:
        probes.update({
            "cynn.direct": "kúnją",
            "cynn.gen.sg": "kúnjas",
            "cynn.dat.sg": "kúnjai",
        })
        control_arms = ("identity", "A", "B", "C_northern_order",
                        "A_contraction", "A_late_contraction", "A_singleton_aw")
        combined = [narrow, insert("FII", wloss)]
        matched = {arm + "_matched": arms[arm] + combined
                   for arm in ("A", "B", "C_northern_order")}
        matched["A_presyncope_contraction"] = arms["A"] + [
            insert("FII", "OEWeakTailNasalLoss"),
        ]
        matched["B_matched_geminate_only"] = arms["B_geminate_only"] + combined
        matched["C_matched_geminate_only"] = [
            {**op, "insert": "FNG"} if op.get("insert") == "FNU" else
            {**op, "move": "FNG"} if op.get("move") == "FNU" else op
            for op in north
        ] + combined
        integrated = {arm: arms[arm] for arm in control_arms} | matched
        aliases = {
            arm: {op["replace"]: op["with"] for op in ops if "replace" in op}
            for arm, ops in integrated.items()
        }
        for arm, ops in integrated.items():
            for stage in stages:
                if stage in definitions and not any(op.get("insert") == stage for op in ops):
                    continue
                queries[f"{arm}:cell:{stage}"] = {
                    "configuration": arm, "through": aliases[arm].get(stage, stage),
                    "inputs": list(probes.values()),
                }
        queries = {
            name: query for name, query in queries.items()
            if query.get("configuration", "identity") in integrated
        }
        queries["erdmann.gemination.local"] = {
            "members": [gem],
            "inputs": ["*d*á*n*i*j*ō", "*d*á*n*j*ō",
                       "*w*í*n*i*j*ō", "*w*í*n*j*ō"],
        }
        plan.update(
            purpose="Recompare low-vowel orders with identical narrow labial and hiatus treatments",
            configurations=integrated,
            aliases=aliases,
            trace_concepts=plan["trace_concepts"] + [
                "believe", "straw", "dill", "show (iptv.2sg)", "show (3sg)",
            ],
            complete_traces=list(integrated),
            census_stages=plan["census_stages"] + [gem, oral, nasal],
            probe_ids=list(probes),
            queries=queries,
        )
    elif sys.argv[2:] == ["--morphology"]:
        probes = {
            f"{word}.{cell}": stem + ending
            for word, stem in (("fenn", "fánj"), ("wedd", "wádj"), ("webb", "wábj"))
            for cell, ending in (("direct", "ą"), ("gen", "as"), ("dat", "ai"))
        }
        selected = {arm: arms[arm] for arm in ("identity", "A", "B", "C_northern_order")}
        queries = {
            f"{arm}:cell:{stage}": {
                "configuration": arm, "through": stage, "inputs": list(probes.values()),
            }
            for arm in selected
            for stage in (oral, nasal, gem, "FNU", "OEHighVowelApocope",
                          "OEFinalGeminateSimplification", final)
            if stage != "FNU" or arm != "identity"
        }
        # A broad compensatory-lengthening countermodel, not a proposed sound law.
        definitions["FWL"] = """define FWL Ctx([
            {*í} {*w} -> {*ḯ} || _ [{*i}|{*ī}],
            {*é} {*w} -> {*ḗ} || _ [{*i}|{*ī}],
            {*ý} {*w} -> {*ȳ} || _ [{*i}|{*ī}]
        ]) .o. OEWLossBeforeI;"""
        hiatus = [
            "*ç*í*w*i", "*g*l*í*w*i", "*n*í*w*i",
            "*p*í*w*ī", "*p*í*w*í", "*p*í*i", "*p*í*w*j*i",
            "*p*y*l*w*ī", "*g*e*r*w*i*þ*i", "*s*t*r*é*w*i*d*ē",
            "*s*ǣ*w*i",
        ]
        for label, members in (
            ("loss", [wloss]), ("fusion", [wloss, "FII"]),
            ("lengthening", ["FWL"]),
            ("lengthening_hvd", ["FWL", "OEHighVowelApocope"]),
            ("fusion_hvd", [wloss, "FII", "OEHighVowelApocope"]),
        ):
            queries[f"hiatus:{label}"] = {"members": members, "inputs": hiatus}
        plan.update(
            purpose="Screen additional inherited light ja-stems and distinguish hiatus mechanisms",
            configurations=selected,
            aliases={arm: plan["aliases"][arm] for arm in selected},
            definitions={name: value for name, value in definitions.items() if name != "FWA"},
            census_stages=[], complete_traces=[], trace_concepts=[], trace_stages=[],
            probe_ids=list(probes), queries=queries,
            predictions={
                "light ja-stems": "With early loss direct cells strand j; protected cells still geminate.",
                "hiatus": "Fusion consumes i; broad compensation retains it and also lengthens short e before lost w.",
            },
            negative_controls=[
                "Exact identity and reference-arm corpus equality.",
                "Long, stressed or glide-separated second vowels do not feed FII.",
                "Attested Mercian streide preserves both vowel qualities; a long first vowel is not licensed by that spelling alone.",
            ],
        )
    elif len(sys.argv) != 2:
        raise SystemExit("use make_plan.py OUTPUT [--placement-trace|--source-integration|--morphology]")
    Path(sys.argv[1]).write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()

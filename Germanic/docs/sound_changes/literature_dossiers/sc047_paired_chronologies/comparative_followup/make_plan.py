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
        placement_arms = (
            "B", "C_northern_order", "B_consumers_before_loss", "C_consumers_before_loss",
        )
        plan.update(
            purpose="Localize the two unrelated terminal differences in early labial placement",
            configurations={arm: arms[arm] for arm in placement_arms},
            aliases={arm: plan["aliases"][arm] for arm in placement_arms},
            trace_concepts=["believe", "straw"],
            complete_traces=list(placement_arms),
            census_stages=["PWGmcEndinglessAw"],
            queries={},
        )
    Path(sys.argv[1]).write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()

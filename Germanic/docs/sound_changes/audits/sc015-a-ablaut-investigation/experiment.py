#!/usr/bin/env python3
"""SC015 a-ablaut investigation: source-pinned private experiments comparing
three candidate families (A traditional vowel-conditioned, B Hill unified
consonantal, C decomposed r / z(C|#) / st components in all orderings and
alternative positions). Run in backend container; writes incremental JSON
to sys.argv[1]. Nothing here modifies production artifacts."""
import csv
import hashlib
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import check_build_manifest, layout

FST_HASH = "6c33b3c723150b61de4a41c89e228f32eeceb8280114b573e182eb8baf6ff51f"
CORPUS_HASH = "1fd8ec257581a54603b59835a46ca764ee2ba0f438c9b497b874a58ee2fe8f73"


def starred(form):
    return "".join("*" + char for char in form.removeprefix("*").replace("h", "x") if char != "-")


def lowering(name, onset, right):
    return (
        f"define {name} [ Ctx([ "
        f"{{*i}} -> {{*e}} || .#. {onset}* _ {right}, "
        f"{{*í}} -> {{*é}} || .#. {onset}* _ {right} "
        "]) ];"
    )


TRAD = lowering(
    "AFTrad", "EnglishStarConsonant",
    "EnglishStarCoronal+ EnglishStarNonHighVowel",
)
HILL = lowering(
    "AFHill", "EnglishStarConsonant", "[{*z} | {*s} {*t} | {*r}]",
)
TAUTO = lowering(
    "AFTauto", "EnglishStarConsonant",
    "[{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}]",
)
BROAD = lowering(
    "AFBroad", "EnglishStarConsonant",
    "[EnglishStarConsonant - EnglishStarNasal - {*j}]+ EnglishStarNonHighVowel",
)
# Family A: traditional vowel-conditioned lowering with only the j and
# nasal+consonant blockers; no preceding-velar prohibition, no coronal limit.
TRADA = lowering(
    "AFTradA", "EnglishStarConsonant",
    "[EnglishStarConsonant - EnglishStarNasal - {*j}]* EnglishStarNonHighVowel",
)
# Family B: Hill's unified consonantal conditioning (tautosyllabic z, st, r),
# with the immediate-z reading kept as a labelled sensitivity test.
HILLB = lowering(
    "AFHillB", "EnglishStarConsonant",
    "[{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}]",
)
HILLBZ = lowering(
    "AFHillBz", "EnglishStarConsonant", "[{*z} | {*s} {*t} | {*r}]",
)
# Family C: Hill's conditioning decomposed into three independent components.
HILLR = lowering("AFHillR", "EnglishStarConsonant", "{*r}")
HILLZ = lowering(
    "AFHillZ", "EnglishStarConsonant", "{*z} [EnglishStarConsonant | .#.]",
)
HILLST = lowering("AFHillSt", "EnglishStarConsonant", "{*s} {*t}")
C_ORDERS = {
    "RZS": ("AFHillR", "AFHillZ", "AFHillSt"),
    "RSZ": ("AFHillR", "AFHillSt", "AFHillZ"),
    "ZRS": ("AFHillZ", "AFHillR", "AFHillSt"),
    "ZSR": ("AFHillZ", "AFHillSt", "AFHillR"),
    "SRZ": ("AFHillSt", "AFHillR", "AFHillZ"),
    "SZR": ("AFHillSt", "AFHillZ", "AFHillR"),
}
C_COMPOSITIONS = tuple(
    f"define AFC{key} [{' .o. '.join(parts)}];" for key, parts in C_ORDERS.items()
)
DEFINITIONS = "\n".join((
    TRAD, HILL, TAUTO, BROAD,
    TRADA, HILLB, HILLBZ, HILLR, HILLZ, HILLST, *C_COMPOSITIONS,
    "define AFSkip [?*];",
    "define AFNoop [?*];",
    "define AFLate [PNWGmcILowering];",
    "define AFLength [Ctx(["
    "{*e} -> {*ē} || .#. EnglishStarConsonant* _ {*r} .#.,"
    "{*é} -> {*ḗ} || .#. EnglishStarConsonant* _ {*r} .#."
    "])];",
))

PROBES = [
    {"id": "dental_before", "stage": "PWGmcDentalHardening", "side": "before"},
    {"id": "dental_after", "stage": "PWGmcDentalHardening", "side": "after"},
    {"id": "lower_before", "stage": "PNWGmcILowering", "side": "before"},
    {"id": "lower_after", "stage": "PNWGmcILowering", "side": "after"},
    {"id": "u_lower_after", "stage": "PNWGmcULowering", "side": "after"},
    {"id": "final_z_after", "stage": "MonosyllabicFinalZLoss", "side": "after"},
    {"id": "rhotacism_after", "stage": "EAFRhotacism", "side": "after"},
    {"id": "interstress_after", "stage": "OEInterStressRaising", "side": "after"},
    {"id": "wi_raising_after", "stage": "OEWICombinativeUUmlaut", "side": "after"},
    {"id": "umlaut_before", "stage": "OEIUmlaut", "side": "before"},
    {"id": "umlaut_after", "stage": "OEIUmlaut", "side": "after"},
    {"id": "backmutation_after", "stage": "OEBackMutation", "side": "after"},
]
COMPONENTS = [
    "PNWGmcILowering", "AFTrad", "AFHill", "AFTauto", "AFBroad",
    "EnglishProtoInput", "PWGmcDentalHardening", "OEIUmlaut",
    "EnglishStarCoronal", "EnglishStarNonHighVowel", "AFLength",
    "AFTradA", "AFHillB", "AFHillBz", "AFHillR", "AFHillZ", "AFHillSt",
    *(f"AFC{key}" for key in C_ORDERS),
]

LEXICAL = [
    ("iz", "iz", "PGmc monosyllabic pronoun; comparative probe, no OE target", "Hill2017:137-138,153"),
    ("hiz", "hiz", "PGmc monosyllabic demonstrative", "Hill2017:137-138,153"),
    ("hir", "hir", "early PGmc reconstruction under Hill's hypothesis, not a late PGmc citation", "Hill2017:156-158"),
    ("wiraz", "wiraz", "early PGmc i-reconstruction; late PGmc e is a serious alternative", "Hill2017:156;RingeTaylor2014:34"),
    ("nistan", "nistan", "Hill's PGmc neuter *-an; component form, not silently equated with CAPR nasal spelling", "Hill2017:153"),
    ("mizdon", "mizdōn", "Hill's PGmc nominative, different from selected dat.sg. *mizdai", "Hill2017:153"),
    ("fiskaz", "fiskaz", "PGmc masculine a-stem nominative", "Hill2017:154"),
    ("wisko", "wiskō", "PGmc feminine nominative; OE evidence is compound -wisc", "Hill2017:154-155"),
    ("bitanaz", "bitanaz", "PNWGmc masculine participial reconstruction, not an infinitive or selected neuter cell", "Hill2017:151-152"),
    ("bidanaz", "biðanaz", "PNWGmc Verner participial reconstruction; test *ð and its PWGmc *d separately", "Hill2017:151-152"),
    ("nidana", "nidana", "schematic WGmc adverb based on OHG nidana; not a quoted PGmc whole-word reconstruction", "Hill2017:152;Lloyd1966:741"),
    ("nestijan", "nestijan", "user-requested stem-shaped probe, not a complete PGmc citation", "Hill2017:153"),
    ("nestijana", "nestijana", "PNWGmc derivative antecedent, e for author's close *ẹ", "Hill2017:153"),
    ("nistijana", "nistijana", "private earlier-i contrast of the same derivative, not an additional author quotation", "Hill2017:153"),
    ("listiz", "listiz", "earlier i-stem counterpart of Hill's PNWGmc *lẹstiz", "Hill2017:153"),
    ("lestiz", "lestiz", "PNWGmc lowered i-stem; CAPR *e represents source *ẹ", "Hill2017:153"),
    ("liznijana", "liznijana", "private earlier-i counterpart of source *lẹznijana; weak-class levelling not encoded", "Hill2017:153,n25"),
    ("lez nijana".replace(" ", ""), "leznijana", "PNWGmc source derivative; e for *ẹ", "Hill2017:153,n25"),
    ("lid", "xlidą", "current selected PGmc input without acute; *ą retained", "live2100;Lloyd1966:738"),
    ("diskaz", "diskaz", "Latin loan with retained i before sk; PGmc-stage control, not a native witness", "RingeTaylor2014:135"),
    ("hina", "hina", "PGmc demonstrative with i before single nasal; negative control for nasal blocking", "Orel2003:171;Kroonen2013:224"),
    ("irha", "irxa", "PGmc *irxa- 'he-goat' with i before r; comparative probe", "Kroonen2013:271;Orel2003:204"),
    ("bedinn", "biðinaz", "ON beðinn participle antecedent entered at PGmc shape; comparative-only, no OE target", "Hill2017:151-152"),
    ("liznon", "liznōn", "weak class-III stem-shaped probe for the learn family", "Scheungraber2010:74-75;TarsiLaker2026:40-47"),
    ("wether_current", "wéθruz", "current selected input (adopted 2026); root e, not a SC015 witness", "live2283;Kroonen2013:584;Orel2003:459-460"),
    ("wether_old", "wíθrą", "superseded former selected input, retained as historical comparison only", "Kroonen2013:584;Orel2003:459-460"),
    ("wether_e_control", "wéθrą", "root-only e control with neuter-shaped ending, NOT a recommended lexical reconstruction", "Kroonen2013:584;Orel2003:459-460"),
    ("world_current", "wíràldu", "current selected early-analogy input without serialized hyphen", "live2302"),
    ("world_e_control", "wéràldu", "root-only private e control at unchanged selected input stage; not a full source quotation", "RingeTaylor2014:326"),
]


def assert_single(outputs, expected, label):
    if outputs != [expected]:
        raise RuntimeError(f"{label}: {outputs!r} != {[expected]!r}")


def main():
    rt = layout()
    if not rt.is_container:
        raise RuntimeError("Foma experiments require backend container")
    if assay.digest(rt.germanic_fst) != FST_HASH or assay.digest(rt.corpus_tsv) != CORPUS_HASH:
        raise RuntimeError("Research baseline changed; do not repin this experiment")
    errors = check_build_manifest(["old_english.bin", *oe_pipeline.expected_snapshot_bins()], rt)
    if errors:
        raise RuntimeError("; ".join(errors))
    protected = [
        rt.germanic_fst, rt.corpus_tsv, rt.sandbox_fst, rt.build_manifest,
        rt.bin_dir / "old_english.bin",
        *(rt.bin_dir / name for name in oe_pipeline.expected_snapshot_bins()),
        rt.data_dir / "entry_stage_metadata.tsv",
        rt.data_dir / "entry_context_metadata.tsv",
    ]
    for directory in ("registry", "cascade_baseline", "audits/sc017-sc019-wull-investigation"):
        protected.extend(p for p in (rt.docs_dir / "sound_changes" / directory).rglob("*") if p.is_file())
    missing = [str(p) for p in protected if not p.exists()]
    if missing:
        raise RuntimeError(f"Missing protections: {missing}")
    before = {str(p): assay.digest(p) for p in protected}
    rows = assay.corpus_rows(rt.corpus_tsv)
    if len(rows) != 387:
        raise RuntimeError("Selected population changed")
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    canonical = assay.batch_apply_down(rt.bin_dir / "old_english.bin", forms)
    mismatches = [r["id"] for r, out in zip(rows, canonical) if out != [r["counterpart"]]]
    if set(mismatches) != {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"}:
        raise RuntimeError(f"Unexpected live mismatches: {mismatches}")
    component_forms = {name: starred(form) for name, form, _, _ in LEXICAL}
    # These are controlled segment strings, not new etymological witnesses.
    for onset in ("", "x", "k", "xl", "b"):
        for coda in ("r", "st", "d", "θr", "sk", "b", "nt", "n", "sj", "z", "zd"):
            for vowel in ("a", "i", "u"):
                component_forms[f"synthetic-{onset or 'zero'}-i-{coda}-{vowel}"] = starred(onset + "i" + coda + vowel)
    component_forms["synthetic-unstressed-second-syllable"] = starred("baristaz")
    component_forms["synthetic-long-i"] = starred("hīr")
    component_forms["synthetic-acute"] = starred("xíraz")
    component_forms["synthetic-proclitic-marker"] = "*ᵘ" + starred("hiz")
    native_probes = [
        ("iz", "iz"), ("hiz", "xiz"), ("hir", "xir"), ("wiraz", "wiraz"),
        ("nest_capr", "nístą"), ("mizdon", "mízdōn"), ("fiskaz", "fískaz"),
        ("wisko", "wískō"), ("bitanaz", "bítanaz"), ("bidanaz", "bíðanaz"),
        ("nest_derivative", "nístjaną"), ("listiz", "lístiz"),
        ("wether_capr", "wéθruz"), ("diskaz", "dískaz"), ("hina", "xína"),
    ]
    identities = []
    variants = [
        ("incumbent", {}, "", ""),
        # Family A: traditional vowel-conditioned lowering
        ("A-trad", {"PNWGmcILowering": "AFTradA"}, "", ""),
        ("A-trad-coronal-noguard", {"PNWGmcILowering": "AFTrad"}, "", ""),
        # Family B: Hill's unified consonantal conditioning
        ("B-hill-tauto", {"PNWGmcILowering": "AFHillB"}, "", ""),
        ("B-hill-immediate-z", {"PNWGmcILowering": "AFHillBz"}, "", ""),
        # Family C: decomposed r / z / st components at the incumbent position
        *[(f"C-{key}", {"PNWGmcILowering": f"AFC{key}"}, "", "") for key in C_ORDERS],
        # Family C repositioning
        ("C-early", {"PNWGmcILowering": "AFSkip"}, "EAFLThVoicing", "AFCRZS"),
        ("C-late-z-before-zloss", {"PNWGmcILowering": "AFSkip"}, "PWGmcUnstressedWordFinalIApocope", "AFCRZS"),
        # Controls retained from the prior driver
        ("skip", {"PNWGmcILowering": "AFSkip"}, "", ""),
        ("late-current", {"PNWGmcILowering": "AFSkip"}, "OEInterStressRaising", "AFLate"),
        ("late-hill", {"PNWGmcILowering": "AFSkip"}, "OEInterStressRaising", "AFHill"),
    ]
    result = {
        "fst_sha256": FST_HASH, "corpus_sha256": CORPUS_HASH,
        "definitions": DEFINITIONS, "probes": PROBES,
        "normalization": "Hill h -> CAPR x; source close short e -> CAPR e. Full input grammar normalization and component segmentation are separate.",
        "selected_rows": len(rows), "baseline_mismatch_ids": mismatches,
        "derived_order": assay.complete_variant_order({"insert_rule": "", "replace": {}}),
        "lexical_probe_sources": [
            {"id": n, "form": f, "stage_and_limits": s, "citation": c}
            for n, f, s, c in LEXICAL
        ],
        "component_inputs": component_forms, "variants": [],
    }
    with tempfile.TemporaryDirectory(prefix="capr_sc015_") as temporary:
        temporary = Path(temporary)
        baseline_intermediate = None
        for name, replacements, anchor, inserted in variants:
            print(f"Compiling {name}", file=sys.stderr, flush=True)
            directory = temporary / name
            directory.mkdir()
            recipe = {
                "id": name, "definitions": DEFINITIONS, "replace": replacements,
                "insert_after": anchor or ("PNWGmcILowering" if replacements else ""),
                "insert_rule": inserted or ("AFNoop" if replacements else ""),
                "component_checks": [{"component": c} for c in COMPONENTS],
            }
            bins = assay.compile_isolated(rt.germanic_fst, recipe, PROBES, directory)
            outputs = assay.batch_apply_down(bins["final"], forms)
            if any(len(out) != 1 for out in outputs):
                raise RuntimeError(f"{name}: corpus missing or ambiguous")
            intermediate = assay.intermediate_outputs(bins, forms)
            if baseline_intermediate is None:
                if outputs != canonical:
                    raise RuntimeError("Full derived wrapper disagrees with production")
                baseline_intermediate = intermediate
                result["components"] = {
                    c: dict(zip(component_forms, assay.batch_apply_down(
                        bins[f"component:{c}"], list(component_forms.values()))))
                    for c in COMPONENTS if c != "EnglishProtoInput"
                }
                result["class_members"] = {
                    c: {
                        s: out for s, out in zip(
                            list("bdfgjklmnprstwxzðŋɣθβ"),
                            assay.batch_apply_down(bins[f"component:{c}"], [
                                "*" + s for s in "bdfgjklmnprstwxzðŋɣθβ"
                            ]),
                        ) if out
                    } for c in ["EnglishStarCoronal"]
                }
                result["baseline_all_rows"] = [
                    {**r, "outputs": o, "checkpoints": {k: v[i] for k, v in intermediate.items()}}
                    for i, (r, o) in enumerate(zip(rows, outputs))
                ]
                result["live_firing_ids"] = [
                    r["id"] for i, r in enumerate(rows)
                    if intermediate["lower_before"][i] != intermediate["lower_after"][i]
                ]
                Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=2))
                result["lengthening_order"] = {}
                for lower in ("PNWGmcILowering", "AFHill"):
                    first = assay.batch_apply_down(bins[f"component:{lower}"], [starred("hir")])[0]
                    if len(first) != 1:
                        raise RuntimeError(f"Lengthening control failed: {lower}: {first}")
                    low_then_long = assay.batch_apply_down(bins["component:AFLength"], first)[0]
                    long_first = assay.batch_apply_down(bins["component:AFLength"], [starred("hir")])[0]
                    long_then_low = assay.batch_apply_down(bins[f"component:{lower}"], long_first)[0]
                    result["lengthening_order"][lower] = {
                        "lower_then_e_lengthening": low_then_long,
                        "e_lengthening_then_lower": long_then_low,
                        "limit": "Demonstrates necessary ordering only for e-specific lengthening proxy; not a new lengthening law.",
                    }
                assert_single(result["components"]["AFHill"]["bitanaz"], starred("bitanaz"), "Hill bitanaz")
                assert_single(result["components"]["AFHill"]["bidanaz"], starred("biðanaz"), "Hill bidanaz")
                assert_single(result["components"]["AFHill"]["hir"], starred("her"), "Hill hir")
                assert_single(result["components"]["PNWGmcILowering"]["hir"], starred("hir"), "Current hir")
                for component in ("PNWGmcILowering", "AFTrad", "AFHill", "AFTauto"):
                    for fixture in ("fiskaz", "wisko", "lid"):
                        assert_single(result["components"][component][fixture],
                                      component_forms[fixture] if component != "AFTrad" or fixture != "lid"
                                      else starred("xledą"), f"{component} {fixture}")
                # Hill's unified consonantal condition (B) must leave the s-cluster and velar
                # negatives untouched; traditional A without the velar guard lowers lid.
                for fixture in ("fiskaz", "wisko", "diskaz", "hina", "lid"):
                    assert_single(result["components"]["AFHillB"][fixture], component_forms[fixture], f"AFHillB {fixture}")
                    assert_single(result["components"]["AFCRZS"][fixture], component_forms[fixture], f"AFCRZS {fixture}")
                assert_single(result["components"]["AFTradA"]["lid"], starred("xledą"), "AFTradA lid")
                for fixture, expected in (("nistan", "nestan"), ("mizdon", "mezdōn"), ("wiraz", "weraz"), ("hir", "her")):
                    assert_single(result["components"]["AFHillB"][fixture], starred(expected), f"AFHillB {fixture}")
                for source, lowered, mutated in (
                    ("nistijana", "nestijana", "nistijana"),
                    ("listiz", "lestiz", "listiz"),
                    ("liznijana", "leznijana", "liznijana"),
                ):
                    lowered_out = assay.batch_apply_down(bins["component:AFHill"], [starred(source)])[0]
                    assert_single(lowered_out, starred(lowered), f"lower {source}")
                    actual = assay.batch_apply_down(bins["component:OEIUmlaut"], lowered_out)[0]
                    assert_single(actual, starred(mutated), f"mutate {source}")
                    identities.append({"input": starred(source), "lowered": lowered_out, "umlauted": actual})
            changed = []
            for i, row in enumerate(rows):
                diffs = {
                    k: {"baseline": baseline_intermediate[k][i], "variant": v[i]}
                    for k, v in intermediate.items()
                    if v[i] != baseline_intermediate[k][i]
                }
                if diffs or outputs[i] != canonical[i]:
                    changed.append({
                        **row, "baseline_outputs": canonical[i], "variant_outputs": outputs[i],
                        "final_changed": outputs[i] != canonical[i], "checkpoints": diffs,
                    })
            alternative_inputs = ["wér-àldu", "wír-àldu", "wéθrą", "wéθruz", "wéθraz"]
            alternative_final = assay.batch_apply_down(bins["final"], alternative_inputs)
            native_outputs = assay.batch_apply_down(bins["final"], [f for _, f in native_probes])
            result["variants"].append({
                "id": name, "recipe": recipe,
                "mismatch_ids": [r["id"] for r, o in zip(rows, outputs) if o != [r["counterpart"]]],
                "changed_final_ids": [r["id"] for r, o, b in zip(rows, outputs, canonical) if o != b],
                "changed_rows": changed,
                "alternative_inputs": dict(zip(alternative_inputs, alternative_final)),
                "supplementary_full_prefix_outputs": {
                    n: {"input": f, "outputs": o,
                        "status": "rejected_by_current_full_grammar" if not o else "diagnostic_only_not_admitted"}
                    for (n, f), o in zip(native_probes, native_outputs)
                },
            })
            Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=2))
            print(f"Finished {name}: final changes {result['variants'][-1]['changed_final_ids']}", file=sys.stderr, flush=True)
    result["mutation_recovery"] = identities
    after = {p: assay.digest(Path(p)) for p in before}
    if after != before:
        raise RuntimeError("Canonical artifacts changed during isolated research")
    result["canonical_protection"] = {"count": len(before), "unchanged": True, "hashes": before}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

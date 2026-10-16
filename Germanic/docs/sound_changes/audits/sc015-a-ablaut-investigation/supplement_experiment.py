#!/usr/bin/env python3
"""SC015 counterevidence supplement: extends experiment.py with (i) a
corrected traditional candidate whose nasal blocker is nasal+consonant
rather than any nasal, (ii) the *twizna- 'twine' family and the numeral
adverbs *twiz / *þriz flagged by E. Hill (private correspondence,
15 Oct 2026), and (iii) component-level chronology tests of z-lowering
against rhotacism and preconsonantal z-loss. Reuses the isolated build
machinery of the main driver; nothing here touches production artifacts.
Run in backend container: python3 supplement_experiment.py OUT.json"""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, "/usr/app/tools")
import experiment as base  # noqa: E402
import anglo_frisian_experiments as assay  # noqa: E402
import oe_pipeline  # noqa: E402
from capr_runtime import check_build_manifest, layout  # noqa: E402

starred, lowering = base.starred, base.lowering

# Corrected traditional candidate: j blocks; a nasal blocks only when
# followed by a consonant (covered nasal). A single prevocalic nasal is
# transparent. No coronal limit, no preceding-velar prohibition.
TRADNC = lowering(
    "AFTradNC", "EnglishStarConsonant",
    "[EnglishStarConsonant - EnglishStarNasal - {*j}]* (EnglishStarNasal) EnglishStarNonHighVowel",
)
# Light-syllable sensitivity: at most one intervening consonant (short
# root syllable), same blockers. A sensitivity test only, used because
# some formulations are stated for single consonants.
TRADNCL = lowering(
    "AFTradNCL", "EnglishStarConsonant",
    "[EnglishStarConsonant - {*j}] EnglishStarNonHighVowel",
)
# Schematic proxies for chronology tests only; neither is a proposed law.
ZN_LOSS = (
    "define AFZnLoss [Ctx(["
    "{*i} {*z} -> {*ī} || _ {*n}, {*í} {*z} -> {*ḯ} || _ {*n},"
    "{*e} {*z} -> {*ē} || _ {*n}, {*é} {*z} -> {*ḗ} || _ {*n},"
    "{*i} {*z} -> {*ī} || _ {*d}, {*í} {*z} -> {*ḯ} || _ {*d},"
    "{*e} {*z} -> {*ē} || _ {*d}, {*é} {*z} -> {*ḗ} || _ {*d}"
    "])];"
)
# Diagnostic restriction, not an established syllabification law: exclude
# z+sonorant while retaining zd and final z. Historical licensing is unresolved.
SONORANT = "[{*m} | {*n} | {*l} | {*r} | {*w} | {*j}]"
HILLZO = lowering(
    "AFHillZo", "EnglishStarConsonant",
    f"{{*z}} [[EnglishStarConsonant - {SONORANT}] | .#.]",
)
HILLBO = lowering(
    "AFHillBo", "EnglishStarConsonant",
    f"[{{*z}} [[EnglishStarConsonant - {SONORANT}] | .#.] | {{*s}} {{*t}} | {{*r}}]",
)
HILLRZO = "define AFHillRZo [AFHillR .o. AFHillZo];"
DEFINITIONS = "\n".join((base.DEFINITIONS, TRADNC, TRADNCL, ZN_LOSS, HILLZO, HILLBO, HILLRZO))
COMPONENTS = [
    *base.COMPONENTS, "AFTradNC", "AFTradNCL", "AFZnLoss", "AFHillZo", "AFHillBo", "AFHillRZo",
    "EAFRhotacism", "MonosyllabicFinalZLoss", "EAFFinalZDeletion", "EnglishStarNasal",
]

# Supplementary comparative inputs. Status: 'reconstruction' = quoted PGmc
# reconstruction from a cited source; 'schematic' = stem/segment string
# built for a controlled test; 'control' = altered vowel for contrast.
LEXICAL = [
    ("twizna", "twízną", "schematic", "Neuter-shaped completion of source stem *twizna-, not an attributed nominative; compare masculine *twiznaz below. Kroonen has no *twizna- lemma.", "KlugeSeebold2011:1021;Orel2003:414;deVaan2016"),
    ("twiznaz", "twíznaz", "reconstruction", "same noun as masculine a-stem nominative", "Orel2003"),
    ("twezna_control", "twézną", "control", "early-lowered counterpart of *twizna-; tests whether e survives to OE", "Hill2017:153"),
    ("twizno", "twíznō", "schematic", "feminine shape of a *-zn- derivative, testing stem alone", "deVaan2016"),
    ("twiz", "twíz", "schematic", "schematic monosyllabic adverb *twiz as a FINAL-z test; the inherited sibilant may be *s (ON tvisvar) — see supplement §3", "Noreen1923;Orel2003"),
    ("thriz", "θríz", "schematic", "schematic monosyllabic adverb *þriz, same caveat", "Noreen1923;Orel2003"),
    ("twizo", "twízō", "schematic", "polysyllabic adverb shape *twizō behind OHG zwiro if r < *z; not a quoted reconstruction", "LloydLuhrSpringer1998:col.784"),
    ("twizor", "twízōr", "schematic", "extended adverb shape behind OHG zwiror; not a quoted reconstruction", "LloydLuhrSpringer1998:col.784"),
    ("thrizor", "θrízōr", "schematic", "extended adverb shape behind OHG driror; not a quoted reconstruction", "LloydLuhrSpringer1998:col.784"),
    ("twiswo", "twíswō", "schematic", "voiceless-sibilant alternative *twis-wō (ON tvisvar); outside any z-environment", "Noreen1923"),
    ("mizdo", "mízdō", "reconstruction", "PGmc *mizdō nominative; OE mēd/meord", "Kroonen2013;Hill2017:153"),
    ("mizdai", "mízdai", "reconstruction", "selected dat.sg. input of live row 2124", "live2124"),
    ("liznona", "líznōną", "schematic", "CAPR infinitive completion of *liznōn-; class-II/III prehistory disputed, not a quoted full paradigm cell", "Kroonen2013:340;RingeTaylor2014:38,84"),
    ("leznona_control", "léznōną", "control", "early-lowered counterpart", "Hill2017:153"),
    ("hina", "xína", "schematic", "Single-prevocalic-nasal probe corresponding to Lloyd's hina adverbial negative; not a verified PGmc nominative", "Lloyd1966:740-741"),
    ("hine", "xínǭ", "schematic", "acc.sg.m. shape with single nasal before non-high vowel", "Orel2003"),
    ("nimana", "nímaną", "control", "i-vocalism control for *nemaną 'take'; single nasal + a", "Kroonen2013"),
    ("sinaz_synthetic", "sínaz", "schematic", "synthetic i + single nasal + a", "synthetic"),
    ("bindana", "bíndaną", "reconstruction", "nasal + consonant blocker control (live 1950)", "live1950"),
    ("windaz_synthetic", "wíndaz", "schematic", "synthetic nasal+consonant", "synthetic"),
    ("rinnana", "rínnaną", "reconstruction", "geminate nasal control (live 2161)", "live2161"),
    ("wiraz", "wíraz", "reconstruction", "lowering before inherited r (comparator)", "Hill2017:156"),
    ("nista", "nístą", "reconstruction", "selected input of live row 2137", "live2137"),
    ("iz", "iz", "reconstruction", "PGmc pronoun; final-z comparator", "Hill2017:153"),
    ("hiz", "xiz", "reconstruction", "PGmc demonstrative; final-z comparator", "Hill2017:153"),
]
PROBES = [
    *base.PROBES,
    {"id": "finalzdel_after", "stage": "EAFFinalZDeletion", "side": "after"},
]
NATIVE_PROBES = [(n, f) for n, f, *_ in LEXICAL]
# OE comparanda for the full-cascade probes (attested target where one exists).
OE_TARGETS = {
    "twizna": "twīn", "twiznaz": "twīn", "twezna_control": "twīn", "mizdo": "mēd",
    "mizdai": "meorde", "liznona": "liornian/leornian", "hina": "hine", "nimana": "niman",
    "bindana": "bindan", "rinnana": "rinnan", "nista": "nest", "iz": "hē (ē)", "hiz": "hē",
}


def main():
    rt = layout()
    if not rt.is_container:
        raise RuntimeError("Foma experiments require backend container")
    if assay.digest(rt.germanic_fst) != base.FST_HASH or assay.digest(rt.corpus_tsv) != base.CORPUS_HASH:
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
    before = {str(p): assay.digest(p) for p in protected}
    rows = assay.corpus_rows(rt.corpus_tsv)
    if len(rows) != 387:
        raise RuntimeError("Selected population changed")
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    canonical = assay.batch_apply_down(rt.bin_dir / "old_english.bin", forms)
    mismatches = [r["id"] for r, out in zip(rows, canonical) if out != [r["counterpart"]]]
    if set(mismatches) != {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"}:
        raise RuntimeError(f"Unexpected live mismatches: {mismatches}")
    component_forms = {name: starred(form) for name, form, *_ in LEXICAL}
    variants = [
        ("incumbent", {}, "", ""),
        ("A-trad", {"PNWGmcILowering": "AFTradA"}, "", ""),
        ("A-trad-nasal-cluster", {"PNWGmcILowering": "AFTradNC"}, "", ""),
        ("A-trad-nasal-cluster-light", {"PNWGmcILowering": "AFTradNCL"}, "", ""),
        ("B-hill-tauto", {"PNWGmcILowering": "AFHillB"}, "", ""),
        ("C-RZS", {"PNWGmcILowering": "AFCRZS"}, "", ""),
        ("B-hill-z-obstruent", {"PNWGmcILowering": "AFHillBo"}, "", ""),
        ("C-r-z-obstruent-no-st", {"PNWGmcILowering": "AFHillRZo"}, "", ""),
        ("skip", {"PNWGmcILowering": "AFSkip"}, "", ""),
    ]
    result = {
        "fst_sha256": base.FST_HASH, "corpus_sha256": base.CORPUS_HASH,
        "provenance_note": "Counterexamples zwirn, zwiro/zwiror, driror and the beðinn correction communicated by Eugen Hill to Nathan Hill, private e-mail, 15 October 2026 (paraphrased; not reproduced).",
        "definitions": DEFINITIONS, "probes": PROBES,
        "selected_rows": len(rows), "baseline_mismatch_ids": mismatches,
        "lexical_probe_sources": [
            {"id": n, "form": f, "status": st, "note": note, "citation": c} for n, f, st, note, c in LEXICAL
        ],
        "oe_targets": OE_TARGETS,
        "component_inputs": component_forms, "variants": [], "chronology": {},
    }
    with tempfile.TemporaryDirectory(prefix="capr_sc015c_") as temporary:
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
                comp = {
                    c: dict(zip(component_forms, assay.batch_apply_down(
                        bins[f"component:{c}"], list(component_forms.values()))))
                    for c in COMPONENTS if c != "EnglishProtoInput"
                }
                result["components"] = comp
                result["live_firing_ids"] = [
                    r["id"] for i, r in enumerate(rows)
                    if intermediate["lower_before"][i] != intermediate["lower_after"][i]
                ]
                # Nasal blocker: corrected A must lower before a single nasal but not
                # before nasal+consonant; the earlier A blocks both.
                base.assert_single(comp["AFTradNC"]["hina"], starred("xéna"), "TradNC hina")
                base.assert_single(comp["AFTradNC"]["nimana"], starred("némaną"), "TradNC nimana")
                base.assert_single(comp["AFTradNC"]["bindana"], starred("bíndaną"), "TradNC bindana")
                base.assert_single(comp["AFTradNC"]["rinnana"], starred("rínnaną"), "TradNC rinnana")
                base.assert_single(comp["AFTradA"]["hina"], starred("xína"), "TradA hina")
                # Hill B lowers *twizna- and *twiz exactly as it lowers *mizdō and *iz.
                for fixture, expected in (("twizna", "twézną"), ("twiz", "twéz"), ("thriz", "θréz"),
                                          ("mizdo", "mézdō"), ("iz", "ez"), ("liznona", "léznōną"),
                                          ("twiswo", "twíswō"), ("twizo", "twízō")):
                    base.assert_single(comp["AFHillB"][fixture], starred(expected), f"HillB {fixture}")
                # Incumbent: coronal cluster before non-high vowel lowers mizdo and twizo, but
                # NOT -zn- (nasal excluded from EnglishStarCoronal): twizna/liznona unchanged.
                for fixture, expected in (("twizna", "twízną"), ("mizdo", "mézdō"), ("liznona", "líznōną"),
                                          ("twiz", "twíz"), ("twizo", "twézō")):
                    base.assert_single(comp["PNWGmcILowering"][fixture], starred(expected), f"incumbent {fixture}")
                for fixture, expected in (("twizna", "twízną"), ("liznona", "líznōną"), ("mizdo", "mézdō"),
                                          ("iz", "ez"), ("twiz", "twéz"), ("nista", "néstą"), ("wiraz", "wéraz")):
                    base.assert_single(comp["AFHillBo"][fixture], starred(expected), f"HillBo {fixture}")
                base.assert_single(comp["AFHillRZo"]["nista"], starred("nístą"), "RZo nista")
                chron = {}
                def run(seq, start):
                    cur = [start]
                    trace = [start]
                    for comp_name in seq:
                        cur = [o for outs in assay.batch_apply_down(bins[f"component:{comp_name}"], cur) for o in outs]
                        trace.append(list(cur))
                    return trace
                for label, start in (("twizna", starred("twízną")), ("mizdo", starred("mízdō")),
                                     ("liznona", starred("líznōną")), ("iz", starred("iz")),
                                     ("twiz", starred("twíz"))):
                    chron[label] = {
                        "lower_z_then_zn_loss": run(["AFHillZ", "AFZnLoss"], start),
                        "lower_zo_then_zn_loss": run(["AFHillZo", "AFZnLoss"], start),
                        "lower_zo_then_rhotacism": run(["AFHillZo", "EAFRhotacism"], start),
                        "zn_loss_then_lower_z": run(["AFZnLoss", "AFHillZ"], start),
                        "lower_z_then_rhotacism": run(["AFHillZ", "EAFRhotacism"], start),
                        "rhotacism_then_lower_z": run(["EAFRhotacism", "AFHillZ"], start),
                        "rhotacism_then_lower_r": run(["EAFRhotacism", "AFHillR"], start),
                        "lower_z_then_final_z_loss": run(["AFHillZ", "MonosyllabicFinalZLoss"], start),
                        "final_z_loss_then_lower_z": run(["MonosyllabicFinalZLoss", "AFHillZ"], start),
                        "incumbent_then_rhotacism": run(["PNWGmcILowering", "EAFRhotacism"], start),
                        "incumbent_then_zn_loss": run(["PNWGmcILowering", "AFZnLoss"], start),
                        "tradNC_then_zn_loss": run(["AFTradNC", "AFZnLoss"], start),
                    }
                result["chronology"] = chron
                Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=2))
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
            native_outputs = assay.batch_apply_down(bins["final"], [f for _, f in NATIVE_PROBES])
            native_trace = assay.intermediate_outputs(bins, [f for _, f in NATIVE_PROBES])
            result["variants"].append({
                "id": name, "recipe": recipe,
                "exact": sum(1 for r, o in zip(rows, outputs) if o == [r["counterpart"]]),
                "mismatch_ids": [r["id"] for r, o in zip(rows, outputs) if o != [r["counterpart"]]],
                "changed_final_ids": [r["id"] for r, o, b in zip(rows, outputs, canonical) if o != b],
                "changed_rows": changed,
                "supplementary_full_cascade": {
                    n: {"input": f, "outputs": o, "oe_comparandum": OE_TARGETS.get(n),
                        "checkpoints": {k: v[i] for k, v in native_trace.items()},
                        "status": "rejected_by_current_full_grammar" if not o else "diagnostic_only_not_admitted"}
                    for i, ((n, f), o) in enumerate(zip(NATIVE_PROBES, native_outputs))
                },
            })
            Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=2))
            print(f"Finished {name}: exact {result['variants'][-1]['exact']} changed {result['variants'][-1]['changed_final_ids']}", file=sys.stderr, flush=True)
    after = {p: assay.digest(Path(p)) for p in before}
    if after != before:
        raise RuntimeError("Canonical artifacts changed during isolated research")
    result["canonical_protection"] = {"count": len(before), "unchanged": True}
    Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({k: result[k] for k in ("live_firing_ids", "canonical_protection")}))


if __name__ == "__main__":
    main()

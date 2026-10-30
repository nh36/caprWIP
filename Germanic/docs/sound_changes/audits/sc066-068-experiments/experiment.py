#!/usr/bin/env python3
"""SC066 (OELAdjacentSyncope) × SC068 (OEPreconsonantalDegemination)
counterfactual experiments (backend container).

The joint investigation asks (a) whether SC066's single environment
`V C+ _ *l` states more than the handbooks license — it fires correctly on
the three selected rows (nettle, spindle, thistle) but would also syncopate
a kettle-type input (*katilaz → ×cetl), which every consulted source keeps
disyllabic (R/T p. 272 "apparently not of cytel, cetel"; Luick §336 and
Brunner §159c restrict the light-syllable deletion to open medial
syllables; Campbell §§388, 589 likewise); (b) whether the reciprocal
SC066 < SC068 ordering (spindle) reproduces; and (c) whether Barrack's
390 post-liquid syncope (p. 96: *meluk > meolc) is admissible — CAPR's
selected milk row keeps meoloc, so it must not be.

Variants compiled through the identical truncation path:

  production_control    -- unmodified cascade; must match canonical
                           old_english.bin on every selected row.
  sc066_retired         -- SC066 replaced by identity; expected: corrupts
                           nettle, spindle, thistle (the live firings).
  weight_open_split     -- proposed reformulation. Heavy-syllable clauses
                           (long V / long diphthong + C+, or short
                           V/short diphthong + CC+) keep the inherited
                           heavy-syllable law; the light-syllable clause
                           (short V/short diphthong + single C)
                           additionally requires a following vowel (open
                           syllable), per Luick §336 / Brunner §159c.
                           Short diphthongs pattern light. NOTE: the
                           kettle probe reaches the rule as *ċietil with
                           UNMARKED {*ie} (WS palatal diphthongization of
                           short *e), which germanic.txt classes as a
                           LONG diphthong "pending probe" — so this
                           variant alone still syncopates the probe.
                           Expected: zero corpus delta; kettle probe
                           still VIOLATED (diagnostic for the next
                           variant).
  weight_open_split_ie_short
                        -- the adopted reformulation: weight_open_split
                           plus reclassification of {*ie} as a short
                           diphthong (the long product of *ē is {*īe},
                           already classed long; handbooks treat ie < *e
                           as short, e.g. Campbell §185). This resolves
                           the class definition's own "pending probe"
                           note. Expected: zero corpus delta; kettle
                           probe retains its medial vowel.
  open_syllable_only    -- all three current clauses require a following
                           vowel. Expected: corrupts spindle (post-apocope
                           site sees *spinnil with final *l), showing why
                           the handbook open-syllable condition cannot be
                           imposed wholesale at this cascade site.
  barrack_390_postliquid-- Barrack's rule 390 (V L V2 C → V L 0 C, his
                           meolc derivation) composed as its own rule
                           directly after SC066. Expected: corrupts the
                           selected meoloc row.
  sc068_before_sc066    -- composition order permuted. Expected: spindle
                           surfaces as spinnl (degemination runs before
                           syncope has created the cluster).
  sc068_retired         -- SC068 replaced by identity; expected: corrupts
                           bottom and spindle (the live firings).

Witness probes (source-backed reconstruction families, NOT admitted corpus
selections): *kátilaz 'kettle' (Orel 2003:211 *katilaz, Lat. catillus
loan; OE cetel/ċietel attested disyllabic, R/T p. 272) and *ángilaz
'angel' (Lat. angelus loan; OE engel, gen. engles) — the latter documents
a latent heavy-closed-syllable overgeneration shared by the current and
reformulated rules (out-of-corpus; recorded, not repaired here).

Usage (from the repository root on the host):
  docker compose exec -T backend python3 \
    /usr/app/docs/sound_changes/audits/sc066-068-experiments/experiment.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
from capr_runtime import layout  # noqa: E402
from oe_pipeline import (evaluation_input, load_rows,
                         normalize_proto)  # noqa: E402
from sound_change_order_sensitivity import batch_apply_down  # noqa: E402

EXPERIMENT_DIR = Path(__file__).resolve().parent
TRUNCATION_MARK = "save stack old_english.bin"
SC066_BLOCK = re.compile(r"define OELAdjacentSyncope Ctx\(\[.*?\]\);",
                         re.DOTALL)
SC068_LINE = ("define OEPreconsonantalDegemination "
              "Ctx(OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN);")
SC066_COMPOSE = "    .o. OELAdjacentSyncope\n"
SC068_COMPOSE = "    .o. OEPreconsonantalDegemination\n"
PRE_SC066_BIN = "old_english_sandbox_after_oe_medial_syncope.bin"
PRE_SC068_BIN = "old_english_sandbox_after_oe_dental_assimilation.bin"

WEIGHT_OPEN_SPLIT = """define OELAdjacentSyncope Ctx([
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ {*l},
    {*i} -> 0 || [EnglishStarShortVowel|EnglishStarShortDiphthong] OEAnyConsonant OEAnyConsonant+ _ {*l},
    {*i} -> 0 || [EnglishStarShortVowel|EnglishStarShortDiphthong] OEAnyConsonant _ {*l} EnglishStarVocalic
]);"""

OPEN_SYLLABLE_ONLY = """define OELAdjacentSyncope Ctx([
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l} EnglishStarVocalic,
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l} EnglishStarVocalic,
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l} EnglishStarVocalic
]);"""

# The {*ie} produced by WS palatal diphthongization of SHORT *e is
# historically a short diphthong (the long product of *ē is {*īe}, already
# classed long). germanic.txt kept {*ie} in EnglishStarLongDiphthong
# "pending probe"; the kettle probe is that probe. The adopted variant
# pairs the weight/open split with the corrected classification.
IE_LONG_MEMBER = "    {*ḗo} |\n    {*ie}"
IE_LONG_REMOVED = "    {*ḗo}"
IE_SHORT_ANCHOR = "    {*éa} | {*éo} | {*ío} | {*íe}"
IE_SHORT_ADDED = "    {*éa} | {*éo} | {*ío} | {*íe} | {*ie}"


def reclassify_ie_short(text: str) -> str:
    if IE_LONG_MEMBER not in text or IE_SHORT_ANCHOR not in text:
        raise RuntimeError("{*ie} diphthong-class anchors not found")
    return (text.replace(IE_SHORT_ANCHOR, IE_SHORT_ADDED)
                .replace(IE_LONG_MEMBER, IE_LONG_REMOVED))


# Composed as a SEPARATE rule after SC066: foma merges the context sets of
# comma-separated parallel clauses, so adding the *u clause inside the same
# bracketed rule would leak the i-clauses' contexts onto *u and vice versa
# (empirically verified: it corrupted nafola, sāwol, weorold and sċilling).
BARRACK_390_DEFINE = ("\ndefine Barrack390PostLiquid "
                      "Ctx([{*u} -> 0 || {*l} _ OEAnyConsonant]);")
BARRACK_390_COMPOSE = "    .o. Barrack390PostLiquid\n"

WITNESS_PROBES = [
    {"id": "kettle", "input": "*kátilaz", "attested": "cetel (disyllabic)",
     "assert": "no_tl_cluster",
     "basis": "Orel 2003:211 *katilaz (Lat. catillus loan; OE cytel); "
              "R/T 2014 p. 272 ('apparently not of cytel, cetel'); "
              "Luick §336 / Brunner §159c: deletion only in open medial "
              "syllables — nom. sg. *katilaz has *i in a closed final "
              "syllable after apocope and is outside every published "
              "formulation of the change"},
    {"id": "angel", "input": "*ángilaz", "attested": "engel (disyllabic)",
     "assert": "no_gl_cluster",
     "basis": "Lat. angelus loan; OE engel, gen. engles (Campbell §574). "
              "Latent heavy-closed overgeneration probe: the selected-cell "
              "architecture sees post-apocope strings, so neither the "
              "current rule nor the reformulation can distinguish *spinnil "
              "(historically trisyllabic *spinnilō, syncopated while open) "
              "from a nominative that was never trisyllabic. Recorded as a "
              "latent out-of-corpus limitation, equal in all variants."},
]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def variant_sources(source: Path) -> dict[str, str]:
    text = source.read_text(encoding="utf-8")
    cut = text.find(TRUNCATION_MARK)
    if cut < 0:
        raise RuntimeError(f"missing truncation mark: {TRUNCATION_MARK}")
    text = text[: cut + len(TRUNCATION_MARK)] + "\nquit\n"
    match = SC066_BLOCK.search(text)
    if not match:
        raise RuntimeError("OELAdjacentSyncope define not found")
    blk = match.group(0)
    if text.count(SC068_LINE) != 1:
        raise RuntimeError("OEPreconsonantalDegemination define not unique")
    for anchor in (SC066_COMPOSE, SC068_COMPOSE):
        if text.count(anchor) != 1:
            raise RuntimeError(f"composition anchor not unique: {anchor!r}")
    variants = {
        "production_control": text,
        "sc066_retired": text.replace(
            blk, "define OELAdjacentSyncope ?*;"),
        "weight_open_split": text.replace(blk, WEIGHT_OPEN_SPLIT),
        "weight_open_split_ie_short": reclassify_ie_short(
            text.replace(blk, WEIGHT_OPEN_SPLIT)),
        "open_syllable_only": text.replace(blk, OPEN_SYLLABLE_ONLY),
        "barrack_390_postliquid": text
        .replace(blk, blk + BARRACK_390_DEFINE)
        .replace(SC066_COMPOSE, SC066_COMPOSE + BARRACK_390_COMPOSE),
        "sc068_before_sc066": text
        .replace(SC068_COMPOSE, "")
        .replace(SC066_COMPOSE, SC068_COMPOSE + SC066_COMPOSE),
        "sc068_retired": text.replace(
            SC068_LINE, "define OEPreconsonantalDegemination ?*;"),
    }
    for name, variant in variants.items():
        if name != "production_control" and variant == text:
            raise RuntimeError(f"variant {name} is identical to control")
    return variants


def compile_variant(name: str, text: str, workdir: Path) -> Path:
    directory = workdir / name
    directory.mkdir()
    script = directory / "variant.foma"
    script.write_text(text, encoding="utf-8")
    result = subprocess.run(["foma", "-q", "-f", script.name], cwd=directory,
                            capture_output=True, text=True, timeout=1800)
    log = result.stdout + "\n" + result.stderr
    if result.returncode or re.search(r"(?im)^\*\*\*|syntax error|not defined",
                                      log):
        raise RuntimeError(f"{name}: compilation failed:\n{log[-4000:]}")
    bin_path = directory / "old_english.bin"
    if not bin_path.is_file() or bin_path.stat().st_size == 0:
        raise RuntimeError(f"{name}: old_english.bin missing or empty")
    return bin_path


def classify(row: dict, old: list[str], new: list[str]) -> str:
    target = [row["counterpart"]]
    if old == target and new != target:
        return "corrupts_previously_correct_prediction"
    if old != target and new == target:
        return "repairs_previous_mismatch"
    if old != target and new != target:
        return "alters_existing_mismatch"
    return "unexpected"


def probe_ok(probe: dict, outputs: list[str]) -> bool:
    if not outputs:
        return False
    if probe["assert"] == "no_tl_cluster":
        return not any("tl" in o for o in outputs)
    if probe["assert"] == "no_gl_cluster":
        return not any("gl" in o or "ġl" in o for o in outputs)
    raise RuntimeError(f"unknown assertion {probe['assert']!r}")


def main() -> int:
    rt = layout()
    if not rt.is_container:
        print("run this Foma experiment inside the backend container",
              file=sys.stderr)
        return 2
    source = rt.fsts_dir / "germanic.txt"
    rows = load_rows(rt.corpus_tsv)
    forms = [evaluation_input(r) for r in rows]
    before_066 = batch_apply_down(rt.bin_dir / PRE_SC066_BIN, forms)
    before_068 = batch_apply_down(rt.bin_dir / PRE_SC068_BIN, forms)
    canonical = batch_apply_down(rt.bin_dir / "old_english.bin", forms)
    probe_forms = [evaluation_input({"proto_norm": normalize_proto(p["input"])})
                   for p in WITNESS_PROBES]
    sources = variant_sources(source)
    report = {
        "experiment": "sc066-068-counterfactuals",
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "germanic.txt_sha256": sha256_of(source),
        "corpus_sha256": sha256_of(rt.corpus_tsv),
        "selected_rows": len(rows),
        "selected_inputs_sha256": hashlib.sha256(
            json.dumps(rows, ensure_ascii=False, sort_keys=True)
            .encode()).hexdigest(),
        "pre_sc066_bin": PRE_SC066_BIN,
        "pre_sc068_bin": PRE_SC068_BIN,
        "variants": {},
    }
    outputs = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in sources.items():
            print(f"Compiling variant {name}", flush=True)
            bin_path = compile_variant(name, text, Path(tmp))
            outputs[name] = batch_apply_down(bin_path, forms)
            block = SC066_BLOCK.search(text)
            report["variants"][name] = {
                "sc066_definition": (block.group(0) if block
                                     else "define OELAdjacentSyncope ?*;"),
                "source_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "composition_order": (
                    "SC068 before SC066" if name == "sc068_before_sc066"
                    else "canonical (SC066 < SC067 < SC068)"),
                "witness_probes": [
                    {**p, "fst_input": form, "outputs": out,
                     "assertion_holds": probe_ok(p, out)}
                    for p, form, out in zip(WITNESS_PROBES, probe_forms,
                                            batch_apply_down(bin_path,
                                                             probe_forms))
                ],
            }
    if outputs["production_control"] != canonical:
        raise RuntimeError("production control differs from canonical bin")
    report["control_matches_canonical"] = True
    for name in sources:
        if name == "production_control":
            continue
        changed = []
        for row, pre66, pre68, old, new in zip(
                rows, before_066, before_068,
                outputs["production_control"], outputs[name]):
            if old == new:
                continue
            changed.append({
                "row_id": row["row_id"], "proto": row["proto"],
                "fst_input": evaluation_input(row),
                "pre_sc066": pre66, "pre_sc068": pre68,
                "selected_target": row["counterpart"],
                "control_outputs": old, "variant_outputs": new,
                "control_matches_selected": old == [row["counterpart"]],
                "variant_matches_selected": new == [row["counterpart"]],
                "assessment": classify(row, old, new),
            })
        report["variants"][name]["rows_changed"] = len(changed)
        report["variants"][name]["changes"] = changed
    receipt = EXPERIMENT_DIR / "counterfactual_receipt.json"
    receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    print(f"receipt written: {receipt}")
    for name, data in report["variants"].items():
        print(f"\n{name}: rows_changed={data.get('rows_changed', 0)}")
        for p in data["witness_probes"]:
            print(f"  {p['id']}: {p['outputs']} "
                  f"{'OK' if p['assertion_holds'] else 'VIOLATED'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

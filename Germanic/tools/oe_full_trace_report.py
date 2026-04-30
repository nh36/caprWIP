#!/usr/bin/env python3
"""Full OE bucket report with stage-by-stage traces for every lexeme."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

# Strip braces, stars, whitespace, slashes, parens — but KEEP hyphens for compound markers
PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")

PROTO_VOWELS = set("aeiouyāēīōūǣȳ")
PROTO_TRIGGERS = set("ijī")
PROTO_DIPHTHONGS = ("ai", "au", "eu", "iu")

FRONT_VOWELS = set("æǣeiīyȳ")
BACK_VOWELS = set("aāoōuū")
LONG_VOWELS = set("āēīōūǣȳ")
HIGH_FRONT_VOWELS = set("iīyȳ")
OE_DIPHTHONGS = ("īe", "ie", "ēo", "eo", "ēa", "ea")
PALATAL_MARKERS = ("ċ", "ġ", "sc", "cg")
BREAKING_DIPHTHONGS = ("ēa", "ēo", "īe", "ea", "eo", "ie")

# STAGES mirrors Germanic/fsts/old_english_sandbox.txt exactly: one entry per
# `save stack old_english_sandbox_after_<slug>.bin` line, in cascade order.
# Each stage is one rule from OldEnglishReflexes — no bundles, no Modern
# English contamination. If the sandbox changes, regenerate this list.
#
# STAGE_HEADERS marks chronological section breakpoints for the trace report.
# These are typographical (markdown) headers — they do NOT change the cascade
# order or rule application. The five sections track historical phases:
#   1. Proto-Germanic consonant inheritance
#   2. Proto-West Germanic developments (PWGmcChanges bundle, individuated)
#   3. Northwest Germanic developments (PNWGmc-era vowel/nasal changes)
#   4. Old English (Anglo-Frisian + AF→OE rules)
#   5. Orthography & surface
#
# Some PGmc/PWGmc rules (PGmcBAllophony, PWGmcFinalBareALoss,
# NWGmcInStemNLoss, etc.) appear in the OE section because the cascade
# applies them late for chronological-interaction reasons — they are kept in
# their cascade position rather than re-grouped by historical phase.
STAGES: List[Tuple[str, str]] = [
    ("ProtoInput", "old_english_sandbox_after_proto_input.bin"),
    ("GmSimplification", "old_english_sandbox_after_gm_simplification.bin"),
    ("Rhotacism", "old_english_sandbox_after_rhotacism.bin"),
    ("PWGmcAiMonophthongization", "old_english_sandbox_after_pwgmc_ai_monophthongization.bin"),
    ("NWGmcAToUBeforeM", "old_english_sandbox_after_nwgmc_a_to_u_before_m.bin"),
    ("PWGmcEarlyIApocope", "old_english_sandbox_after_pwgmc_early_i_apocope.bin"),
    ("PWGmcFinalOrLowering", "old_english_sandbox_after_pwgmc_final_or_lowering.bin"),
    ("PWGmcCoronalWAssimilation", "old_english_sandbox_after_pwgmc_coronal_w_assimilation.bin"),
    ("PWGmcIjContraction", "old_english_sandbox_after_pwgmc_ij_contraction.bin"),
    ("PWGmcJGemination", "old_english_sandbox_after_pwgmc_j_gemination.bin"),
    ("PWGmcSyllabicJ", "old_english_sandbox_after_pwgmc_syllabic_j.bin"),
    ("PWGmcLThVoicing", "old_english_sandbox_after_pwgmc_l_th_voicing.bin"),
    ("PWGmcDentalHardening", "old_english_sandbox_after_pwgmc_dental_hardening.bin"),
    ("NWGmcUnstressedAiMonophthongization", "old_english_sandbox_after_nwgmc_unstressed_ai_monophthongization.bin"),
    ("NWGmcILowering", "old_english_sandbox_after_nwgmc_i_lowering.bin"),
    ("OEWsPalatalGlide", "old_english_sandbox_after_oe_ws_palatal_glide.bin"),
    ("NWGmcULowering", "old_english_sandbox_after_nwgmc_u_lowering.bin"),
    ("NWGmcStressedMonosyllableORaising", "old_english_sandbox_after_nwgmc_stressed_monosyllable_o_raising.bin"),
    ("NWGmcFinalLongORaising", "old_english_sandbox_after_nwgmc_final_long_o_raising.bin"),
    ("PGmcFinalZDeletion", "old_english_sandbox_after_pgmc_final_z_deletion.bin"),
    ("NWGmcUnstressedORaising", "old_english_sandbox_after_nwgmc_unstressed_o_raising.bin"),
    ("NWGmcMnDissimilation", "old_english_sandbox_after_nwgmc_mn_dissimilation.bin"),
    ("NWGmcNStemNLoss", "old_english_sandbox_after_nwgmc_n_stem_n_loss.bin"),
    ("NWGmcLongELowering", "old_english_sandbox_after_nwgmc_long_e_lowering.bin"),
    ("NWGmcLongENasalRounding", "old_english_sandbox_after_nwgmc_long_e_nasal_rounding.bin"),
    ("NWGmcNasalSpirantLengthening", "old_english_sandbox_after_nwgmc_nasal_spirant_lengthening.bin"),
    ("NWGmcNasalSpirantLoss", "old_english_sandbox_after_nwgmc_nasal_spirant_loss.bin"),
    ("NWGmcPreconsonantalXLoss", "old_english_sandbox_after_nwgmc_preconsonantal_x_loss.bin"),
    ("OEAwjGlideFormation", "old_english_sandbox_after_oe_awj_glide_formation.bin"),
    ("OEAuFronting", "old_english_sandbox_after_oe_au_fronting.bin"),
    ("OEWWSimplification", "old_english_sandbox_after_oe_ww_simplification.bin"),
    ("OEDiphthongLeveling", "old_english_sandbox_after_oe_diphthong_leveling.bin"),
    ("OEEwLongDiphthong", "old_english_sandbox_after_oe_ew_long_diphthong.bin"),
    ("OEAwLongDiphthong", "old_english_sandbox_after_oe_aw_long_diphthong.bin"),
    ("OEPrefixAReductionEarly", "old_english_sandbox_after_oe_prefix_a_reduction_early.bin"),
    ("OEInterStressRaising", "old_english_sandbox_after_oe_inter_stress_raising.bin"),
    ("OECompoundLinkingSyncope", "old_english_sandbox_after_oe_compound_linking_syncope.bin"),
    ("OEStripSecondaryStress", "old_english_sandbox_after_oe_strip_secondary_stress.bin"),
    ("OEWICombinativeUUmlaut", "old_english_sandbox_after_oe_wi_combinative_u_umlaut.bin"),
    ("OEMedUnstressedULowering", "old_english_sandbox_after_oe_med_unstressed_u_lowering.bin"),
    ("PWGmcFinalBareALoss", "old_english_sandbox_after_pwgmc_final_bare_a_loss.bin"),
    ("PWGmcSurvivingBimoricOUnrounding", "old_english_sandbox_after_pwgmc_surviving_bimoric_o_unrounding.bin"),
    ("AngloFrisianBrightening", "old_english_sandbox_after_anglo_frisian_brightening.bin"),
    ("OEBreaking", "old_english_sandbox_after_oe_breaking.bin"),
    ("OEVelarFricativePalatalization", "old_english_sandbox_after_oe_velar_fricative_palatalization.bin"),
    ("OEARestoration", "old_english_sandbox_after_oe_a_restoration.bin"),
    ("OEHeavySyllableNasalApocope", "old_english_sandbox_after_oe_heavy_syllable_nasal_apocope.bin"),
    ("OESecondaryNasalization", "old_english_sandbox_after_oe_secondary_nasalization.bin"),
    ("PGmcBAllophony", "old_english_sandbox_after_pgmc_b_allophony.bin"),
    ("SieversLawSyncope", "old_english_sandbox_after_sievers_law_syncope.bin"),
    ("OESkPalatalization", "old_english_sandbox_after_oe_sk_palatalization.bin"),
    ("OEVelarPalatalization", "old_english_sandbox_after_oe_velar_palatalization.bin"),
    ("OEPostVelarWLoss", "old_english_sandbox_after_oe_post_velar_w_loss.bin"),
    ("OEWLossBeforeI", "old_english_sandbox_after_oe_w_loss_before_i.bin"),
    ("OEIUmlaut", "old_english_sandbox_after_oe_i_umlaut.bin"),
    ("OEWsPalatalDiphthongization", "old_english_sandbox_after_oe_ws_palatal_diphthongization.bin"),
    ("OEJClusterCoalescence", "old_english_sandbox_after_oe_j_cluster_coalescence.bin"),
    ("OENasalDissimilation", "old_english_sandbox_after_oe_nasal_dissimilation.bin"),
    ("OEBackMutation", "old_english_sandbox_after_oe_back_mutation.bin"),
    ("OEWsPalatalUmlaut", "old_english_sandbox_after_oe_ws_palatal_umlaut.bin"),
    ("OEWeakTailNasalLoss", "old_english_sandbox_after_oe_weak_tail_nasal_loss.bin"),
    ("OEWeightMarkers", "old_english_sandbox_after_oe_weight_markers.bin"),
    ("OEHighVowelApocope", "old_english_sandbox_after_oe_high_vowel_apocope.bin"),
    ("NWGmcInStemNLoss", "old_english_sandbox_after_nwgmc_in_stem_n_loss.bin"),
    ("OEMedialSyncope", "old_english_sandbox_after_oe_medial_syncope.bin"),
    ("OELAdjacentSyncope", "old_english_sandbox_after_oe_l_adjacent_syncope.bin"),
    ("OEDentalAssimilation", "old_english_sandbox_after_oe_dental_assimilation.bin"),
    ("OEPreconsonantalDegemination", "old_english_sandbox_after_oe_preconsonantal_degemination.bin"),
    ("OEEarlyOShortening", "old_english_sandbox_after_oe_early_o_shortening.bin"),
    ("OEUnstressedFrontingEarly", "old_english_sandbox_after_oe_unstressed_fronting_early.bin"),
    ("OELateOShortening", "old_english_sandbox_after_oe_late_o_shortening.bin"),
    ("OEUnstressedLongVowelShortening", "old_english_sandbox_after_oe_unstressed_long_vowel_shortening.bin"),
    ("OEUnstressedAEMerger", "old_english_sandbox_after_oe_unstressed_ae_merger.bin"),
    ("OEMedUnstressedILowering1", "old_english_sandbox_after_oe_med_unstressed_i_lowering_1.bin"),
    ("OEMedUnstressedILowering", "old_english_sandbox_after_oe_med_unstressed_i_lowering.bin"),
    ("OEPrefixIReduction", "old_english_sandbox_after_oe_prefix_i_reduction.bin"),
    ("OEPrefixAReductionLate", "old_english_sandbox_after_oe_prefix_a_reduction_late.bin"),
    ("OEWeakTailReduction", "old_english_sandbox_after_oe_weak_tail_reduction.bin"),
    ("OEJLossAfterHeavy", "old_english_sandbox_after_oe_j_loss_after_heavy.bin"),
    ("OEFinalGeminateSimplification", "old_english_sandbox_after_oe_final_geminate_simplification.bin"),
    ("OEJStrengtheningAfterFrontDiphthong", "old_english_sandbox_after_oe_j_strengthening_after_front_diphthong.bin"),
    ("OEIntervocalicJVocalization", "old_english_sandbox_after_oe_intervocalic_j_vocalization.bin"),
    ("OEUnstressedEIContraction", "old_english_sandbox_after_oe_unstressed_ei_contraction.bin"),
    ("OEWeightCleanup", "old_english_sandbox_after_oe_weight_cleanup.bin"),
    ("OEHLoss", "old_english_sandbox_after_oe_h_loss.bin"),
    ("OEContraction", "old_english_sandbox_after_oe_contraction.bin"),
    ("OERMetathesis", "old_english_sandbox_after_oe_r_metathesis.bin"),
    ("OEEpentheticVowel", "old_english_sandbox_after_oe_epenthetic_vowel.bin"),
    ("OELateUnstressedAgSuffix", "old_english_sandbox_after_oe_late_unstressed_ag_suffix.bin"),
    ("OECjCleanup", "old_english_sandbox_after_oe_cj_cleanup.bin"),
    ("OEXsMerge", "old_english_sandbox_after_oe_xs_merge.bin"),
    ("OldEnglishOrthography", "old_english_sandbox_after_old_english_orthography.bin"),
    ("OEGlideUToEo", "old_english_sandbox_after_oe_glide_u_to_eo.bin"),
    ("OldEnglishRemoveStars", "old_english_sandbox_after_old_english_remove_stars.bin"),
    ("OldEnglishSurface", "old_english_sandbox_after_old_english_surface.bin"),
]

# Markdown section headers injected before the named stage in the trace
# output. Section dividers only — they do not alter the cascade.
STAGE_HEADERS: Dict[str, str] = {
    "ProtoInput": "## Section 1: Proto-Germanic consonant inheritance",
    "PWGmcAiMonophthongization": "## Section 2: Proto-West Germanic developments",
    "NWGmcUnstressedAiMonophthongization": "## Section 3: Northwest Germanic developments",
    "OEAwjGlideFormation": "## Section 4: Old English",
    "OldEnglishOrthography": "## Section 5: Orthography & surface",
}


def normalize_proto(raw: str) -> str:
    normalized = PROTO_STRIP_RE.sub("", raw or "")
    # Proto inventory uses θ; normalize þ to avoid false no_output buckets.
    return normalized.replace("þ", "θ")


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            proto = (row.get("PROTOFORM") or "").strip()
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not proto or not counterpart or counterpart == "-":
                continue
            norm = normalize_proto(proto)
            if not norm:
                continue
            rows.append(
                {
                    "concept": row.get("CONCEPT", ""),
                    "proto": proto,
                    "proto_norm": norm,
                    "counterpart": counterpart,
                }
            )
    return rows


def apply_down(bin_path: Path, form: str) -> List[str]:
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=(form + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split("\t", 1)
        out = parts[1] if len(parts) == 2 else ""
        if out and out != "+?":
            outputs.append(out)
    seen = set()
    deduped: List[str] = []
    for item in outputs:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def run_stage(bin_dir: Path, bin_name: str, form: str) -> List[str]:
    stage_path = (bin_dir / bin_name).resolve()
    proc = subprocess.run(
        ["flookup", "-i", str(stage_path)],
        input=(form + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split("\t", 1)
        out = parts[1] if len(parts) == 2 else raw
        outputs.append(out or "+?")
    if not outputs:
        outputs.append("+?")
    seen = set()
    deduped: List[str] = []
    for item in outputs:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def has_front(s: str) -> bool:
    return any(ch in s for ch in FRONT_VOWELS) or any(d in s for d in ("ie", "īe", "eo", "ēo", "ea", "ēa"))


def has_back(s: str) -> bool:
    return any(ch in s for ch in BACK_VOWELS)


def has_long(s: str) -> bool:
    return any(ch in s for ch in LONG_VOWELS) or any(d in s for d in ("ēa", "ēo", "īe"))


def has_high_front(s: str) -> bool:
    return any(ch in s for ch in HIGH_FRONT_VOWELS) or any(d in s for d in ("ie", "īe"))


def oe_first_vowel_unit(s: str) -> str:
    for i in range(len(s)):
        for diph in OE_DIPHTHONGS:
            if s.startswith(diph, i):
                return diph
        ch = s[i]
        if ch in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS):
            return ch
    return ""


def oe_first_is_front(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in FRONT_VOWELS or unit in {"ie", "īe", "eo", "ēo", "ea", "ēa"}


def oe_first_is_back(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in BACK_VOWELS


def oe_first_is_high_front(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in HIGH_FRONT_VOWELS or unit in {"ie", "īe"}


def vowel_sequence(s: str) -> List[str]:
    """Return vowel/diphthong units in order for quick mismatch heuristics."""
    seq: List[str] = []
    i = 0
    while i < len(s):
        pair = s[i : i + 2]
        if pair in BREAKING_DIPHTHONGS:
            seq.append(pair)
            i += 2
            continue
        if s[i] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS):
            seq.append(s[i])
        i += 1
    return seq


def consonant_sequence(s: str) -> str:
    """Strip vowels/diphthongs to compare consonant order (keeps gemination)."""
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    return "".join(ch for ch in s if ch not in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS))


def has_palatal_variant_mismatch(out: str, expected: str) -> bool:
    """Detect sc/cg vs ċ/ġ representation mismatches."""
    exp_fine = ("ċ" in expected) or ("ġ" in expected)
    exp_sc = ("sc" in expected) or ("cg" in expected)
    out_fine = ("ċ" in out) or ("ġ" in out)
    out_sc = ("sc" in out) or ("cg" in out)
    return (exp_fine and out_sc and not out_fine) or (exp_sc and out_fine and not out_sc)


def has_consonant_gemination(s: str) -> bool:
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i] not in vowels:
            return True
    return False


def has_breaking_diph(s: str) -> bool:
    return any(d in s for d in BREAKING_DIPHTHONGS)


def consonant_skeleton(s: str) -> str:
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    for ch in LONG_VOWELS | FRONT_VOWELS | BACK_VOWELS:
        s = s.replace(ch, "")
    return s


def has_palatal_marker(s: str) -> bool:
    return any(marker in s for marker in PALATAL_MARKERS)


def trigger_in_next_syllable(proto_norm: str) -> bool:
    first_vowel_idx = None
    for idx, ch in enumerate(proto_norm):
        if ch in PROTO_VOWELS:
            first_vowel_idx = idx
            break
    if first_vowel_idx is None:
        return False
    for ch in proto_norm[first_vowel_idx + 1 :]:
        if ch in PROTO_TRIGGERS:
            return True
        if ch in PROTO_VOWELS:
            return False
    return False


def proto_first_vowel_unit(proto_norm: str) -> str:
    for i in range(len(proto_norm)):
        for diph in PROTO_DIPHTHONGS:
            if proto_norm.startswith(diph, i):
                return diph
        ch = proto_norm[i]
        if ch in PROTO_VOWELS:
            return ch
    return ""


def is_a_fronting_context(proto_norm: str) -> bool:
    return proto_first_vowel_unit(proto_norm) in {"a", "ā"}


def ends_with_vowel(s: str) -> bool:
    return bool(s) and s[-1] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS)


def proto_mismatch_suspect(proto_norm: str, out: str, expected: str) -> bool:
    if trigger_in_next_syllable(proto_norm):
        return False
    if not oe_first_is_high_front(expected):
        return False
    if oe_first_is_high_front(out):
        return False
    if not oe_first_is_back(out):
        return False
    first = proto_first_vowel_unit(proto_norm)
    if first in {"e", "ē", "i", "ī", "æ", "ǣ", "y", "ȳ", "eu", "iu"}:
        return True
    return False


def base_bucket(proto_norm: str, out: str, expected: str) -> str:
    if proto_mismatch_suspect(proto_norm, out, expected):
        return "proto_mismatch_suspect"
    if has_breaking_diph(expected) and not has_breaking_diph(out):
        return "breaking_missing"
    if has_long(expected) and not has_long(out):
        expected_cons = consonant_skeleton(expected)
        out_cons = consonant_skeleton(out)
        if expected_cons and expected_cons != out_cons and expected_cons in out_cons:
            return "other"
        return "long_vowel_missing"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        if trigger_in_next_syllable(proto_norm):
            return "i_umlaut_missing_true"
        if is_a_fronting_context(proto_norm):
            return "fronting_missing_no_trigger"
        return "other"
    if has_palatal_marker(expected) and not has_palatal_marker(out):
        return "palatalization_missing"
    return "other"


def other_subtype(out: str, expected: str) -> str:
    if expected.endswith("n") and not out.endswith("n"):
        return "final_n_missing"
    if ends_with_vowel(expected) and not ends_with_vowel(out):
        return "final_vowel_missing"
    if ends_with_vowel(out) and not ends_with_vowel(expected):
        return "final_vowel_extra"
    if has_breaking_diph(out) and not has_breaking_diph(expected):
        return "breaking_extra_other"
    if has_palatal_marker(out) and not has_palatal_marker(expected):
        return "palatal_extra_other"
    if has_palatal_variant_mismatch(out, expected):
        return "palatal_marker_variant"
    if has_long(out) and not has_long(expected):
        return "length_extra_other"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        return "front_expected_back_out"
    if oe_first_is_back(expected) and oe_first_is_front(out):
        return "back_expected_front_out"
    out_cons = consonant_sequence(out)
    expected_cons = consonant_sequence(expected)
    if out_cons == expected_cons:
        out_vowels = vowel_sequence(out)
        expected_vowels = vowel_sequence(expected)
        if len(expected_vowels) > len(out_vowels):
            return "epenthetic_vowel_missing"
        if len(expected_vowels) == len(out_vowels) and expected_vowels != out_vowels:
            return "vowel_quality_other"
    if has_consonant_gemination(out) and not has_consonant_gemination(expected):
        return "gemination_extra"
    if out_cons != expected_cons:
        return "consonant_mismatch_other"
    return "uncategorized"


def bucket_entry(proto_norm: str, out: str, expected: str) -> str:
    bucket = base_bucket(proto_norm, out, expected)
    if bucket == "other":
        return other_subtype(out, expected)
    return bucket


def trace_lexeme(proto_norm: str, bin_dir: Path) -> List[Tuple[str, List[str]]]:
    trace: List[Tuple[str, List[str]]] = []
    last_outputs: List[str] | None = None
    for label, bin_name in STAGES:
        outputs = run_stage(bin_dir, bin_name, proto_norm)
        usable = [out for out in outputs if out != "+?"]
        if not usable:
            # Stage rejected the input: keep showing the previous stage's form
            # and flag as no-change so the trace still reads continuously.
            outputs = last_outputs if last_outputs is not None else [proto_norm]
            label = f"{label} [no-change]"
        else:
            outputs = usable
            if last_outputs is not None and outputs == last_outputs:
                label = f"{label} [no-change]"
        last_outputs = outputs
        trace.append((label, outputs))
    return trace


def write_report(
    rows: Iterable[Dict[str, str]],
    bin_path: Path,
    bin_dir: Path,
    output_path: Path,
    trace_all: bool = False,
) -> None:
    buckets: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    stage_fires: Dict[str, List[str]] = defaultdict(list)
    fronted_rows: List[str] = []; unfronted_rows: List[str] = []; fronting_correct: List[str] = []; fronting_unfronting_correct: List[str] = []; fronting_unfronting_incorrect: List[str] = []
    for row in rows:
        afb = run_stage(bin_dir, "old_english_sandbox_after_anglo_frisian_brightening.bin", row["proto_norm"]); ar = run_stage(bin_dir, "old_english_sandbox_after_oe_a_restoration.bin", row["proto_norm"])
        afb_out = next((o for o in afb if o != "+?"), ""); ar_out = next((o for o in ar if o != "+?"), "")
        fronted = is_a_fronting_context(row["proto_norm"]) and oe_first_is_front(afb_out); unfronted = fronted and oe_first_is_back(ar_out)
        outputs = apply_down(bin_path, row["proto_norm"])
        expected = row["counterpart"]
        if fronted:
            summary = f"{row['concept']} | {row['proto']} | exp {expected} | afb {afb_out or '+?'} | ar {ar_out or '+?'}"
            fronted_rows.append(summary)
            if unfronted:
                unfronted_rows.append(summary)
                if oe_first_is_back(expected):
                    fronting_unfronting_correct.append(summary)
                elif oe_first_is_front(expected):
                    fronting_unfronting_incorrect.append(summary)
            elif oe_first_is_front(expected):
                fronting_correct.append(summary)
        if not outputs:
            bucket = "no_output"
        elif expected in outputs:
            bucket = "exact_match"
        elif len(outputs) > 1:
            bucket = "multiple_outputs"
        else:
            bucket = bucket_entry(row["proto_norm"], outputs[0], expected)
        row_copy = dict(row)
        row_copy["outputs"] = ", ".join(outputs) if outputs else "+?"
        buckets[bucket].append(row_copy)

    order = [
        "exact_match",
        "multiple_outputs",
        "no_output",
        "i_umlaut_missing_true",
        "proto_mismatch_suspect",
        "fronting_missing_no_trigger",
        "breaking_missing",
        "long_vowel_missing",
        "palatalization_missing",
        "final_vowel_extra",
        "length_extra_other",
        "front_expected_back_out",
        "final_vowel_missing",
        "breaking_extra_other",
        "final_n_missing",
        "palatal_extra_other",
        "back_expected_front_out",
        "palatal_marker_variant",
        "epenthetic_vowel_missing",
        "vowel_quality_other",
        "gemination_extra",
        "consonant_mismatch_other",
        "uncategorized",
    ]

    lines: List[str] = []
    for bucket in order:
        items = buckets.get(bucket, [])
        if not items:
            continue
        lines.append(f"=== BUCKET: {bucket} ({len(items)}) ===")
        lines.append("")
        for row in items:
            lines.append(f"--- {row['concept']} ---")
            lines.append(f"PROTO: {row['proto']}")
            lines.append(f"EXPECTED: {row['counterpart']}")
            lines.append(f"OUTPUTS: {row['outputs']}")
            lines.append("")
            prev_outputs: List[str] | None = None
            lexeme_label = f"{row['concept']} :: {row['proto']}"
            for label, outputs in trace_lexeme(row["proto_norm"], bin_dir):
                base_label = label.split(" [", 1)[0]
                header = STAGE_HEADERS.get(base_label)
                if header is not None:
                    lines.append("")
                    lines.append(header)
                    lines.append("")
                if prev_outputs is not None and outputs != prev_outputs:
                    stage_fires[base_label].append(lexeme_label)
                prev_outputs = outputs
                pretty = ", ".join(outputs)
                lines.append(f"{label}: {pretty}")
            lines.append("")
        lines.append("")

    lines.append("=== A-FRONTING AUDIT ==="); lines.append("")
    for title, items in [("fronted", fronted_rows), ("unfronted_by_ar", unfronted_rows), ("fronting_correct", fronting_correct), ("fronting_plus_unfronting_correct", fronting_unfronting_correct), ("fronting_plus_unfronting_incorrect", fronting_unfronting_incorrect)]:
        if items:
            lines.append(f"--- {title} ({len(items)}) ---"); lines.extend(items); lines.append("")

    lines.append("=== STAGE FIRING SUMMARY ===")
    lines.append("")
    for label, _bin in STAGES:
        fired = stage_fires.get(label, [])
        lines.append(f"{label}: {len(fired)}")
        if fired:
            lines.append(", ".join(fired))
        lines.append("")

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    # Default paths: relative to this file's location in Germanic/tools/
    tools_dir = Path(__file__).resolve().parent
    germanic_dir = tools_dir.parent  # Germanic/
    repo_root = germanic_dir.parent  # capr-v3-working/
    parser.add_argument(
        "--tsv",
        default=str(germanic_dir / "data" / "germanic-aligned-final.tsv"),
        help="Aligned TSV with Old English rows (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(repo_root / "backend" / "old_english.bin"),
        help="Generator FST for apply-down (default: %(default)s)",
    )
    parser.add_argument(
        "--bin-dir",
        default=str(repo_root / "backend"),
        help="Directory containing old_english_sandbox_after_*.bin (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=str(germanic_dir / "docs" / "debug_snapshots" / "oe_full_trace_report.txt"),
        help="Report output path (default: %(default)s)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Trace all entries including exact_match (default: mismatches only)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    bin_dir = Path(args.bin_dir).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path)
    write_report(rows, bin_path, bin_dir, output_path, trace_all=args.all)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

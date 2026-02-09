#!/usr/bin/env python3
"""Unified OE mismatch report with mechanistic sub-buckets.

Each bucket targets ONE hypothesis / ONE mechanism so that future debugging
is safe and focused.  See inline comments for the rationale behind each split.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

PROTO_STRIP_RE = re.compile(r"[{}*\s\-/()]")

# Treat these as vowels in the proto stream when looking for an i/j trigger.
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
# Characters that are definitely consonants in OE orthography.
OE_CONSONANTS = set("bcdfgġhklmnprstwxþðċ")


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
            proto = (row.get("PROTO") or "").strip()
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
    # Deduplicate while preserving order.
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


def has_breaking_diph(s: str) -> bool:
    return any(d in s for d in BREAKING_DIPHTHONGS)


def consonant_skeleton(s: str) -> str:
    """Strip vowels/diphthongs to compare consonant material."""
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    for ch in LONG_VOWELS | FRONT_VOWELS | BACK_VOWELS:
        s = s.replace(ch, "")
    return s


def has_palatal_marker(s: str) -> bool:
    return any(marker in s for marker in PALATAL_MARKERS)


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


def has_final_devoicing_issue(out: str, expected: str) -> bool:
    """Detect voiced stop in output that should be devoiced in expected.
    
    Handles both word-final (d#→t#) and pre-consonantal (dm→tm) contexts.
    """
    if not out or not expected:
        return False
    out_cons = consonant_sequence(out)
    exp_cons = consonant_sequence(expected)
    if not out_cons or not exp_cons or len(out_cons) != len(exp_cons):
        return False
    # Check for d→t, g→c/k, b→p in final or pre-consonantal position
    # Compare last few consonants
    pairs = [("d", "t"), ("g", "c"), ("g", "k"), ("b", "p")]
    for i in range(min(3, len(out_cons))):  # Check last 3 consonants
        idx = -(i+1)
        for voiced, voiceless in pairs:
            if out_cons[idx] == voiced and exp_cons[idx] == voiceless:
                # Rest of consonants should match
                if out_cons[:idx] == exp_cons[:idx] and (idx == -1 or out_cons[idx+1:] == exp_cons[idx+1:]):
                    return True
    return False


def has_intervocalic_voicing_issue(out: str, expected: str) -> bool:
    """Detect intervocalic b/d/g that should be f/þ/ġ (fricatives)."""
    if not out or not expected:
        return False
    # Check for patterns like VbV→VfV, VdV→VþV (medial stops should be fricatives)
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    # Simple heuristic: look for b in out where expected has f/v, same for d/þ, g/ġ
    for i in range(1, len(out) - 1):
        if out[i] in "bdg":
            if (i > 0 and out[i-1] in vowels) and (i < len(out)-1 and out[i+1] in vowels):
                # Intervocalic position
                if out[i] == "b" and ("f" in expected or "v" in expected):
                    return True
                if out[i] == "d" and "þ" in expected:
                    return True
                if out[i] == "g" and "ġ" in expected:
                    return True
    return False


def trigger_in_next_syllable(proto_norm: str) -> bool:
    """Heuristic: an i/ī/j appears before any other vowel after the first vowel."""
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
    first = proto_first_vowel_unit(proto_norm)
    return first in {"a", "ā"}


def ends_with_vowel(s: str) -> bool:
    if not s:
        return False
    return s[-1] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS)


def proto_mismatch_suspect(proto_norm: str, out: str, expected: str) -> bool:
    """Heuristic: expected shows high-front raising but proto lacks trigger and starts front."""
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
        return _breaking_subtype(out, expected)
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
            # Check if the mismatch also involves a form-class difference
            # (e.g., verb infinitive in proto but noun expected, or vice versa)
            out_cons = consonant_sequence(out)
            exp_cons = consonant_sequence(expected)
            if out_cons != exp_cons:
                return "fronting_missing__also_wrong_form"
            return "fronting_missing__afb"
        return "other"
    if has_palatal_marker(expected) and not has_palatal_marker(out):
        return "palatalization_missing"
    return "other"


def _find_first_cons_mismatch(out: str, expected: str) -> str:
    """Find the first consonant pair that differs between out and expected.

    Returns a string like 'þ_vs_d' or '' if consonants are identical / not alignable.
    """
    out_c = consonant_sequence(out)
    exp_c = consonant_sequence(expected)
    if out_c == exp_c:
        return ""
    for i in range(min(len(out_c), len(exp_c))):
        if out_c[i] != exp_c[i]:
            return f"{out_c[i]}_vs_{exp_c[i]}"
    if len(out_c) != len(exp_c):
        return "length_diff"
    return ""


def _cons_mismatch_position(out: str, expected: str) -> str:
    """Classify the position of the first consonant mismatch."""
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    out_c = consonant_sequence(out)
    exp_c = consonant_sequence(expected)
    mismatch_idx = -1
    for i in range(min(len(out_c), len(exp_c))):
        if out_c[i] != exp_c[i]:
            mismatch_idx = i
            break
    if mismatch_idx < 0:
        return ""
    # Find the mismatched consonant in the original string and check context
    mismatched_char = out_c[mismatch_idx]
    cons_count = 0
    for i, ch in enumerate(out):
        if ch in OE_CONSONANTS:
            if cons_count == mismatch_idx:
                # Check context
                before = out[i - 1] if i > 0 else ""
                after = out[i + 1] if i < len(out) - 1 else ""
                if i == len(out) - 1 or (after not in vowels and before not in vowels):
                    return "word_final"
                if before in vowels and after in vowels:
                    return "intervocalic"
                return "cluster"
            cons_count += 1
    return ""


def _breaking_subtype(out: str, expected: str) -> str:
    """Classify breaking mismatch by expected diphthong and produced monophthong."""
    for diph in BREAKING_DIPHTHONGS:
        if diph in expected and diph not in out:
            mono = oe_first_vowel_unit(out) if not has_breaking_diph(out) else ""
            if diph in ("ea", "ēa"):
                if mono in ("a", "ā", "æ", "ǣ"):
                    return "breaking_missing__expected_ea_got_a"
                return "breaking_missing__expected_ea"
            if diph in ("eo", "ēo"):
                if mono in ("e", "ē"):
                    return "breaking_missing__expected_eo_got_e"
                return "breaking_missing__expected_eo"
            if diph in ("ie", "īe"):
                if mono in ("i", "ī"):
                    return "breaking_missing__expected_ie_got_i"
                return "breaking_missing__expected_ie"
    return "breaking_missing"


def _breaking_extra_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify cases where output has a breaking diphthong but expected doesn't."""
    out_cons = consonant_sequence(out)
    exp_cons = consonant_sequence(expected)

    # If consonant skeletons differ substantially, this is likely a wrong-form/lexeme
    # issue rather than a genuine extra-breaking phonology problem.
    if out_cons != exp_cons and len(out_cons) != len(exp_cons):
        return "breaking_extra__wrong_form"

    # Identify which diphthong is extra in the output
    for diph in BREAKING_DIPHTHONGS:
        if diph in out and diph not in expected:
            exp_vowel = oe_first_vowel_unit(expected)
            if diph in ("ea", "ēa"):
                if exp_vowel in ("a", "ā", "æ", "ǣ"):
                    return "breaking_extra__ea_for_a"
                return "breaking_extra__ea_other"
            if diph in ("eo", "ēo"):
                if exp_vowel in ("e", "ē"):
                    return "breaking_extra__eo_for_e"
                if exp_vowel in ("i", "ī", "u", "ū"):
                    return "breaking_extra__eo_for_high"
                return "breaking_extra__eo_other"
            if diph in ("ie", "īe"):
                if exp_vowel in ("i", "ī"):
                    return "breaking_extra__ie_for_i"
                if exp_vowel in ("ē",):
                    return "breaking_extra__ie_for_e"
                return "breaking_extra__ie_other"
    return "breaking_extra__other"


def _palatal_extra_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify palatal-extra mismatch by the mechanism that caused it."""
    # Check if this is purely an orthographic normalization difference:
    # expected has plain c/g where output has ċ/ġ, but underlying phonology identical.
    out_depal = out.replace("ċ", "c").replace("ġ", "g")
    exp_depal = expected.replace("ċ", "c").replace("ġ", "g")
    if out_depal == exp_depal:
        return "palatal_extra__orth_normalization"

    # Check if palatalization was triggered by a *j in the proto-form
    has_j = "j" in proto_norm
    if has_j:
        # Check if the palatal marker is adjacent to the j-related vowel
        return "palatal_extra__j_triggered"

    # Check if velar was palatalized before a front vowel
    # Pattern: we produced ċ/ġ, expected has c/g — velar before front vowel in our output
    for i, ch in enumerate(out):
        if ch in ("ċ", "ġ") and i < len(out) - 1:
            next_ch = out[i + 1]
            if next_ch in FRONT_VOWELS:
                # Check if expected has the non-palatal version in roughly the same position
                plain = "c" if ch == "ċ" else "g"
                if plain in expected:
                    return "palatal_extra__velar_before_front"
    # Broader check: is there any front vowel adjacent to a palatal in the output?
    for i, ch in enumerate(out):
        if ch in ("ċ", "ġ"):
            before = out[i - 1] if i > 0 else ""
            after = out[i + 1] if i < len(out) - 1 else ""
            if before in FRONT_VOWELS or after in FRONT_VOWELS:
                return "palatal_extra__velar_before_front"

    return "palatal_extra__other"


def _back_front_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify back_expected_front_out by AFB / a-restoration / morphology."""
    # Check if the mismatch is primarily in suffix/tail material
    # Heuristic: if the first 2+ characters match, it's probably a tail/suffix issue
    common_prefix = 0
    for i in range(min(len(out), len(expected))):
        if out[i] == expected[i]:
            common_prefix += 1
        else:
            break
    if common_prefix >= 2 and common_prefix >= len(expected) - 2:
        return "back_expected_front_out__morph_or_data_tail"

    # Is this an AFB-like context? (proto *a before nasal/liquid + consonant)
    if is_a_fronting_context(proto_norm):
        return "back_expected_front_out__AFB_like"

    # Check for a-restoration-like patterns: expected has back vowel (a/o) where
    # we produce a front vowel — suggests a-restoration should undo fronting
    first_exp = oe_first_vowel_unit(expected)
    first_out = oe_first_vowel_unit(out)
    if first_exp in ("a", "ā") and first_out in ("æ", "ǣ", "e", "ē"):
        return "back_expected_front_out__a_restoration_like"

    return "back_expected_front_out__other"


# Known u-lowering exception roots (Luick §78, R/T §2.3.1).
# Output has o where expected has u (or vice versa) near labials/velars.
_U_LOWERING_ROOTS = {"wulf", "wolf", "full", "foll", "bucc", "bocc", "fugol", "fogol",
                     "wull", "woll", "rust", "rost", "lufu", "lofu"}


def _vowel_quality_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Split vowel_quality_other into mechanistic sub-buckets."""
    out_vowels = vowel_sequence(out)
    exp_vowels = vowel_sequence(expected)

    # 1. u/o alternation (u-lowering exceptions)
    for i in range(min(len(out_vowels), len(exp_vowels))):
        if (out_vowels[i] == "o" and exp_vowels[i] == "u") or \
           (out_vowels[i] == "u" and exp_vowels[i] == "o"):
            # Check if this is a known u-lowering exception context
            if any(root in out or root in expected for root in _U_LOWERING_ROOTS):
                return "vowel_quality__u_lowering_exception"
            return "vowel_quality__u_o_alternation"

    # 2. æ/e quality (AFB-related or fronting quality)
    for i in range(min(len(out_vowels), len(exp_vowels))):
        if {out_vowels[i], exp_vowels[i]} == {"æ", "e"} or \
           {out_vowels[i], exp_vowels[i]} == {"ǣ", "ē"}:
            return "vowel_quality__ae_e_alternation"

    # 3. Stressed vowel: first vowel differs, rest are the same
    if len(out_vowels) == len(exp_vowels) and len(out_vowels) >= 1:
        if out_vowels[0] != exp_vowels[0] and out_vowels[1:] == exp_vowels[1:]:
            return "vowel_quality__stressed_vowel"

    # 4. Unstressed vowel: first vowel matches, later vowel(s) differ
    if len(out_vowels) == len(exp_vowels) and len(out_vowels) >= 2:
        if out_vowels[0] == exp_vowels[0] and out_vowels[1:] != exp_vowels[1:]:
            return "vowel_quality__unstressed_vowel"

    return "vowel_quality__other"


def _final_vowel_missing_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify final_vowel_missing by mechanism."""
    out_cons = consonant_sequence(out)
    exp_cons = consonant_sequence(expected)

    # Check for weak-noun-like patterns: output ends in -o/-a/-on/-an
    # but expected ends in -e/-a (weak noun nominative).
    if expected[-1:] in ("e", "a") and out_cons == exp_cons:
        return "final_vowel_missing__weak_noun_like"

    # Apocope candidate: expected has final vowel, output doesn't, and the
    # consonant skeletons match (pure final-vowel difference).
    if exp_cons == out_cons:
        return "final_vowel_missing__apocope_candidate"

    # Proto form suspect: different consonant structures.
    if len(out_cons) != len(exp_cons):
        # Detect verb-infinitive producing an inflected form where expected is a noun:
        # proto ends in -ăną (strong verb inf) or -ōjăną/-ēją (weak verb inf)
        # and expected is a much shorter noun/adjective.
        is_verb_proto = proto_norm.endswith("ană") or proto_norm.endswith("anăn") or \
                        "ōjăną" in proto_norm or "ējăną" in proto_norm or \
                        proto_norm.endswith("ēną") or proto_norm.endswith("ōną")
        if is_verb_proto and len(expected) <= len(out) - 2:
            return "final_vowel_missing__verb_vs_noun"

        # Detect weak-noun oblique (proto ends in -ōn/-ăn) where expected is
        # a different form (nominative or stem).
        is_weak_noun = proto_norm.endswith("ōn") or proto_norm.endswith("ăn") or \
                       proto_norm.endswith("ōną") or proto_norm.endswith("ōn")
        if is_weak_noun and expected[-1:] in ("e", "a"):
            return "final_vowel_missing__weak_noun_form"

        return "final_vowel_missing__morph_form_mismatch"

    return "final_vowel_missing__other"


def _inflectional_suffix_extra_subtype(out: str, expected: str, proto_norm: str = "") -> str:
    """Subdivide inflectional_suffix_extra by the kind of suffix."""
    # Detect verb-infinitive vs noun/adj mismatch: proto has verbal *-ăną
    # (ă=U+0103, n, ą=U+0105) but expected is a bare stem.
    if out.endswith("an") and proto_norm.endswith("\u0103n\u0105"):
        exp_cons = consonant_sequence(expected)
        out_stem = out[:-2]
        if consonant_sequence(out_stem) == exp_cons or exp_cons in consonant_sequence(out_stem):
            return "infl_suffix_extra__verb_vs_noun"

    # Detect noun n-stem suffix: proto ends in ăn (ă=U+0103, n) but NOT verb inf.
    # TSV has n-stem oblique, expected is nominative/bare.
    if out.endswith("an") and proto_norm.endswith("\u0103n") and not proto_norm.endswith("\u0103n\u0105"):
        exp_cons = consonant_sequence(expected)
        out_stem = out[:-2]
        if consonant_sequence(out_stem) == exp_cons or exp_cons in consonant_sequence(out_stem):
            return "infl_suffix_extra__nstem_vs_bare"

    for suffix in ("on", "an", "en", "ian"):
        if out.endswith(suffix):
            exp_cons = consonant_sequence(expected)
            out_stem = out[: -len(suffix)]
            if consonant_sequence(out_stem) == exp_cons or exp_cons in consonant_sequence(out_stem):
                return f"infl_suffix_extra__{suffix}"
    for suffix in ("as", "es", "os"):
        if out.endswith(suffix):
            return f"infl_suffix_extra__{suffix}"
    return "infl_suffix_extra__other"


def _final_n_missing_subtype(out: str, expected: str) -> str:
    """Subdivide final_n_missing by context."""
    # Check if expected ends with -an (infinitive/weak noun)
    if expected.endswith("an"):
        return "final_n_missing__expected_an"
    if expected.endswith("on"):
        return "final_n_missing__expected_on"
    if expected.endswith("en"):
        return "final_n_missing__expected_en"
    # Bare -n
    return "final_n_missing__bare_n"


def other_subtype(out: str, expected: str, proto_norm: str = "") -> str:
    if expected.endswith("n") and not out.endswith("n"):
        return _final_n_missing_subtype(out, expected)
    if ends_with_vowel(expected) and not ends_with_vowel(out):
        return _final_vowel_missing_subtype(out, expected, proto_norm)
    if ends_with_vowel(out) and not ends_with_vowel(expected):
        return "final_vowel_extra"
    if has_breaking_diph(out) and not has_breaking_diph(expected):
        return _breaking_extra_subtype(out, expected, proto_norm)
    if has_palatal_marker(out) and not has_palatal_marker(expected):
        return _palatal_extra_subtype(out, expected, proto_norm)
    if has_palatal_variant_mismatch(out, expected):
        return "palatal_marker_variant"
    if has_long(out) and not has_long(expected):
        return "length_extra_other"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        return "front_expected_back_out"
    if oe_first_is_back(expected) and oe_first_is_front(out):
        return _back_front_subtype(out, expected, proto_norm)
    out_cons = consonant_sequence(out)
    expected_cons = consonant_sequence(expected)
    if out_cons == expected_cons:
        out_vowels = vowel_sequence(out)
        expected_vowels = vowel_sequence(expected)
        if len(expected_vowels) > len(out_vowels):
            return "epenthetic_vowel_missing"
        if len(expected_vowels) == len(out_vowels) and expected_vowels != out_vowels:
            return _vowel_quality_subtype(out, expected, proto_norm)
    if has_consonant_gemination(out) and not has_consonant_gemination(expected):
        return "gemination_extra"
    # Check specific consonant phenomena before falling back to catch-all
    if out_cons != expected_cons:
        exp_cons_only = consonant_sequence(expected)
        # 0. Inflectional suffix present in output but not expected
        if len(out) > len(expected) + 1:
            for suffix in ("an", "en", "on", "um", "as", "es", "os", "ian"):
                if out.endswith(suffix):
                    out_stem = out[: -len(suffix)]
                    if consonant_sequence(out_stem) == exp_cons_only:
                        return _inflectional_suffix_extra_subtype(out, expected, proto_norm)
                    if exp_cons_only and len(out_cons) > len(exp_cons_only):
                        if out_cons.endswith(exp_cons_only[-1:]) and exp_cons_only in out_cons:
                            return _inflectional_suffix_extra_subtype(out, expected, proto_norm)
        # 1. Final devoicing
        if has_final_devoicing_issue(out, expected):
            return "final_devoicing_missing"
        # 2. Intervocalic voicing
        if has_intervocalic_voicing_issue(out, expected):
            return "intervocalic_voicing_missing"
        # 3. Prefix morphology
        if len(expected) >= len(out) + 2:
            if exp_cons_only and out_cons in exp_cons_only[1:]:
                return "prefix_morphology_issue"
        # 4. Consonant-pair sub-buckets
        pair = _find_first_cons_mismatch(out, expected)
        pos = _cons_mismatch_position(out, expected)
        if pair and pos:
            return f"cons_mismatch__{pair}__{pos}"
        if pair:
            return f"cons_mismatch__{pair}"
        return "consonant_mismatch_other"
    # Check for r-metathesis (VrC ↔ rVC)
    if _is_metathesis(out, expected):
        return "r_metathesis"
    # Check for suffix form mismatch (-eian vs -ian, etc.)
    if out.endswith("eian") and expected.endswith("ian"):
        return "suffix_form__eian_vs_ian"
    if out.endswith("eon") and expected.endswith("on") and len(out) == len(expected) + 1:
        return "suffix_form__eon_vs_on"
    # Syncopation: output has extra medial vowel compared to expected
    if len(out) > len(expected) and consonant_sequence(out) == consonant_sequence(expected):
        return "syncopation_missing"
    return "uncategorized"


def _is_metathesis(out: str, expected: str) -> bool:
    """Detect if the difference is likely r-metathesis (VrC ↔ rVC)."""
    # Check for common OE r-metathesis patterns
    out_s = sorted(out)
    exp_s = sorted(expected)
    if out_s != exp_s:
        return False
    # Same characters but different order → likely metathesis
    if "r" in out and "r" in expected:
        return True
    return False


def build_report(
    rows: Iterable[Dict[str, str]], bin_path: Path
) -> Tuple[Dict[str, List[Tuple[str, str, str]]], Dict[str, List[Tuple[str, str, str]]]]:
    buckets: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    other_subs: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    for row in rows:
        outputs = apply_down(bin_path, row["proto_norm"])
        expected = row["counterpart"]
        if not outputs:
            buckets["no_output"].append((row["proto"], "+?", expected))
            continue
        if expected in outputs:
            continue
        out = outputs[0]
        bucket = base_bucket(row["proto_norm"], out, expected)
        buckets[bucket].append((row["proto"], out, expected))
        if bucket == "other":
            other_subs[other_subtype(out, expected, row["proto_norm"])].append((row["proto"], out, expected))
    return buckets, other_subs


def write_report(
    buckets: Dict[str, List[Tuple[str, str, str]]],
    other_subs: Dict[str, List[Tuple[str, str, str]]],
    output_path: Path,
    max_examples: int,
) -> None:
    # Core buckets (from base_bucket) — include breaking sub-buckets
    core_keys = [
        "i_umlaut_missing_true",
        "proto_mismatch_suspect",
        "fronting_missing__afb",
        "fronting_missing__also_wrong_form",
        "long_vowel_missing",
        "no_output",
        "palatalization_missing",
    ]
    # Add any breaking_missing sub-bucket keys that actually exist
    breaking_keys = sorted(k for k in buckets if k.startswith("breaking_missing"))
    core_keys = core_keys[:4] + breaking_keys + core_keys[4:]

    # Other-bucket sub-categories — fixed order for stable ones, then dynamic
    fixed_other_keys = [
        "final_vowel_extra",
        "length_extra_other",
        "front_expected_back_out",
        "palatal_marker_variant",
        "epenthetic_vowel_missing",
        "syncopation_missing",
        "gemination_extra",
        "final_devoicing_missing",
        "intervocalic_voicing_missing",
        "prefix_morphology_issue",
        "r_metathesis",
    ]
    # Collect all dynamic sub-bucket keys not in the fixed list
    dynamic_keys = sorted(k for k in other_subs if k not in fixed_other_keys)
    # Group dynamic keys by prefix for readability
    breaking_extra_keys = [k for k in dynamic_keys if k.startswith("breaking_extra__")]
    palatal_keys = [k for k in dynamic_keys if k.startswith("palatal_extra__")]
    back_front_keys = [k for k in dynamic_keys if k.startswith("back_expected_front_out__")]
    vowel_quality_keys = [k for k in dynamic_keys if k.startswith("vowel_quality__")]
    final_vowel_keys = [k for k in dynamic_keys if k.startswith("final_vowel_missing__")]
    final_n_keys = [k for k in dynamic_keys if k.startswith("final_n_missing__")]
    infl_suffix_keys = [k for k in dynamic_keys if k.startswith("infl_suffix_extra__")]
    cons_mismatch_keys = [k for k in dynamic_keys if k.startswith("cons_mismatch__")]
    suffix_form_keys = [k for k in dynamic_keys if k.startswith("suffix_form__")]
    other_dynamic = [
        k for k in dynamic_keys
        if not any(k.startswith(p) for p in (
            "breaking_extra__", "palatal_extra__", "back_expected_front_out__",
            "vowel_quality__", "final_vowel_missing__", "final_n_missing__",
            "infl_suffix_extra__", "cons_mismatch__", "suffix_form__",
        ))
        and k not in ("consonant_mismatch_other", "uncategorized")
    ]

    other_order = (
        fixed_other_keys
        + ["--- breaking_extra sub-buckets ---"] + breaking_extra_keys
        + ["--- palatal_extra sub-buckets ---"] + palatal_keys
        + ["--- back_expected_front_out sub-buckets ---"] + back_front_keys
        + ["--- vowel_quality sub-buckets ---"] + vowel_quality_keys
        + ["--- final_vowel_missing sub-buckets ---"] + final_vowel_keys
        + ["--- final_n_missing sub-buckets ---"] + final_n_keys
        + ["--- inflectional_suffix_extra sub-buckets ---"] + infl_suffix_keys
        + ["--- consonant_mismatch sub-buckets ---"] + cons_mismatch_keys
        + ["--- suffix_form sub-buckets ---"] + suffix_form_keys
        + other_dynamic
        + ["consonant_mismatch_other", "uncategorized"]
    )

    mismatch_total = sum(len(v) for v in buckets.values())
    lines: List[str] = []
    lines.append(f"Total mismatches: {mismatch_total}")
    lines.append("")

    # Summary counts
    lines.append("=== CORE BUCKETS ===")
    for key in core_keys:
        count = len(buckets.get(key, []))
        if count > 0:
            lines.append(f"  {key}: {count}")
    lines.append("")
    lines.append("=== OTHER SUB-BUCKETS ===")
    for key in other_order:
        if key.startswith("---"):
            lines.append(key)
            continue
        count = len(other_subs.get(key, []))
        if count > 0:
            lines.append(f"  {key}: {count}")
    lines.append("")

    # Detailed examples
    lines.append("=== DETAILED EXAMPLES ===")
    lines.append("")
    for key in core_keys:
        items = buckets.get(key, [])
        if not items:
            continue
        lines.append(f"{key} ({len(items)}):")
        for proto, out, expected in items[:max_examples]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
        lines.append("")

    for key in other_order:
        if key.startswith("---"):
            continue
        items = other_subs.get(key, [])
        if not items:
            continue
        lines.append(f"{key} ({len(items)}):")
        for proto, out, expected in items[:max_examples]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
        lines.append("")

    lines.append("=== A-FRONTING AUDIT ===")
    lines.append("--- fronting_missing__afb ---")
    for proto, out, expected in buckets.get("fronting_missing__afb", []):
        lines.append(f"{proto} -> {out} (expected {expected})")
    lines.append("")
    lines.append("--- fronting_missing__also_wrong_form ---")
    for proto, out, expected in buckets.get("fronting_missing__also_wrong_form", []):
        lines.append(f"{proto} -> {out} (expected {expected})")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--tsv",
        default=str(default_root / "data" / "germanic-aligned-final.tsv"),
        help="Aligned TSV with Old English rows (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(default_root / "old_english.bin"),
        help="Generator FST for apply-down (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=str(Path("docs/debug_snapshots/oe_mismatch_report.txt")),
        help="Report output path (default: %(default)s)",
    )
    parser.add_argument(
        "--examples",
        type=int,
        default=5,
        help="Max examples per bucket (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path)
    buckets, other_subs = build_report(rows, bin_path)
    write_report(buckets, other_subs, output_path, args.examples)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

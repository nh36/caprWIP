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

PROTO_STRIP_RE = re.compile(r"[{}*\s\-/()]")

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

STAGES: List[Tuple[str, str]] = [
    ("ProtoInput", "old_english_sandbox_after_proto_input.bin"),
    ("InitialKn", "old_english_sandbox_after_initial_kn.bin"),
    ("Palatalisation", "old_english_sandbox_after_palatalisation.bin"),
    ("ConsonantRules", "old_english_sandbox_after_consonant_rules.bin"),
    ("WestGermanic", "old_english_sandbox_after_west_germanic.bin"),
    ("NWGmcULowering", "old_english_sandbox_after_nwgmc_u_lowering.bin"),
    ("NWGmcFinalLongORaising", "old_english_sandbox_after_nwgmc_final_long_o_raising.bin"),
    ("AuFronting", "old_english_sandbox_after_au_fronting.bin"),
    ("WWSimplification", "old_english_sandbox_after_ww_simplification.bin"),
    ("DiphthongLeveling", "old_english_sandbox_after_diphthong_leveling.bin"),
    ("EwLongDiphthong", "old_english_sandbox_after_ew_long_diphthong.bin"),
    ("AngloFrisianBrightening", "old_english_sandbox_after_anglo_frisian_brightening.bin"),
    ("BreakingLengthening", "old_english_sandbox_after_breaking_lengthening.bin"),
    ("VelarFricPal", "old_english_sandbox_after_velar_fricative_palatalization.bin"),
    ("ARestoration", "old_english_sandbox_after_a_restoration.bin"),
    ("FinalWeakSchwaApocope", "old_english_sandbox_after_final_weak_schwa_apocope.bin"),
    ("JGemination", "old_english_sandbox_after_j_gemination.bin"),
    ("SkPalatalization", "old_english_sandbox_after_sk_palatalization.bin"),
    ("VelarPalatalization", "old_english_sandbox_after_velar_palatalization.bin"),
    ("IUmlaut", "old_english_sandbox_after_i_umlaut.bin"),
    ("JClusterCoalescence", "old_english_sandbox_after_j_cluster_coalescence.bin"),
    ("BackMutation", "old_english_sandbox_after_back_mutation.bin"),
    ("NasalSpirantLengthening", "old_english_sandbox_after_nasal_spirant_lengthening.bin"),
    ("NasalSpirantLoss", "old_english_sandbox_after_nasal_spirant_loss.bin"),
    ("WeakTailNasalLoss", "old_english_sandbox_after_weak_tail_nasal_loss.bin"),
    ("WeightMarkers", "old_english_sandbox_after_weight_markers.bin"),
    ("HighVowelApocope", "old_english_sandbox_after_high_vowel_apocope.bin"),
    ("HeavySyllableNasalApocope", "old_english_sandbox_after_heavy_syllable_nasal_apocope.bin"),
    ("WeakTailReduction", "old_english_sandbox_after_weak_tail_reduction.bin"),
    ("JLossAfterHeavy", "old_english_sandbox_after_j_loss_after_heavy.bin"),
    ("WeightCleanup", "old_english_sandbox_after_weight_cleanup_full.bin"),
    ("HLoss", "old_english_sandbox_after_h_loss.bin"),
    ("Contraction", "old_english_sandbox_after_contraction.bin"),
    ("ProtoToOEWeakTail", "old_english_sandbox_after_proto_to_oe_weak_tail.bin"),
    ("ProtoToOEWeightMarkers", "old_english_sandbox_after_proto_to_oe_weight_markers.bin"),
    ("ProtoToOEApocope", "old_english_sandbox_after_proto_to_oe_apocope.bin"),
    ("ProtoToOEWeightCleanup", "old_english_sandbox_after_proto_to_oe_weight_cleanup.bin"),
    ("ProtoToOE", "old_english_sandbox_after_proto_to_oe.bin"),
    ("WGlide", "old_english_sandbox_after_w_glide.bin"),
    ("GhMarker", "old_english_sandbox_after_gh_marker.bin"),
    ("GlideDeletion", "old_english_sandbox_after_glide_deletion.bin"),
    ("Epenthesis", "old_english_sandbox_after_epenthesis.bin"),
    ("Orthography", "old_english_sandbox_after_orthography.bin"),
    ("Surface", "old_english_sandbox_after_surface.bin"),
]


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
    last_outputs = [proto_norm]
    carrying = False
    for label, bin_name in STAGES:
        outputs = run_stage(bin_dir, bin_name, proto_norm)
        usable = [out for out in outputs if out != "+?"]
        carried = False
        if not usable:
            outputs = last_outputs
            carried = True
        else:
            outputs = usable
        last_outputs = outputs
        if carried:
            label = f"{label} [carry]"
            carrying = True
        elif carrying:
            label = f"{label} [resume]"
            carrying = False
        trace.append((label, outputs))
    return trace


def write_report(
    rows: Iterable[Dict[str, str]],
    bin_path: Path,
    bin_dir: Path,
    output_path: Path,
) -> None:
    buckets: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    stage_fires: Dict[str, List[str]] = defaultdict(list)
    fronted_rows: List[str] = []; unfronted_rows: List[str] = []; fronting_correct: List[str] = []; fronting_unfronting_correct: List[str] = []; fronting_unfronting_incorrect: List[str] = []
    for row in rows:
        afb = run_stage(bin_dir, "old_english_sandbox_after_anglo_frisian_brightening.bin", row["proto_norm"]); ar = run_stage(bin_dir, "old_english_sandbox_after_a_restoration.bin", row["proto_norm"])
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
        "--bin-dir",
        default=str(default_root),
        help="Directory containing old_english_sandbox_after_*.bin (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=str(Path("docs/debug_snapshots/oe_full_trace_report.txt")),
        help="Report output path (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    bin_dir = Path(args.bin_dir).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path)
    write_report(rows, bin_path, bin_dir, output_path)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

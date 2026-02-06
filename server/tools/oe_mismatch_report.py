#!/usr/bin/env python3
"""Unified OE mismatch report with detailed subcategories (no separate 'other' report)."""

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
            other_subs[other_subtype(out, expected)].append((row["proto"], out, expected))
    return buckets, other_subs


def write_report(
    buckets: Dict[str, List[Tuple[str, str, str]]],
    other_subs: Dict[str, List[Tuple[str, str, str]]],
    output_path: Path,
    max_examples: int,
) -> None:
    core_order = [
        "i_umlaut_missing_true",
        "proto_mismatch_suspect",
        "fronting_missing_no_trigger",
        "breaking_missing",
        "no_output",
        "long_vowel_missing",
        "palatalization_missing",
    ]
    other_order = [
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
    order = core_order + other_order
    mismatch_total = sum(len(v) for v in buckets.values())
    lines: List[str] = []
    lines.append(f"Total mismatches: {mismatch_total}")
    lines.append("")
    for key in core_order:
        lines.append(f"{key}: {len(buckets.get(key, []))}")
    for key in other_order:
        lines.append(f"{key}: {len(other_subs.get(key, []))}")
    lines.append("")
    lines.append("Examples:")
    for key in core_order:
        lines.append(f"{key}:")
        for proto, out, expected in buckets.get(key, [])[:max_examples]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
    for key in other_order:
        lines.append(f"{key}:")
        for proto, out, expected in other_subs.get(key, [])[:max_examples]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
    lines.append("")
    lines.append("=== A-FRONTING AUDIT ===")
    lines.append("--- fronting_missing_no_trigger ---")
    for proto, out, expected in buckets.get("fronting_missing_no_trigger", []):
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

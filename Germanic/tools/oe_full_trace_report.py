#!/usr/bin/env python3
"""Full OE bucket report with stage-by-stage traces for every lexeme."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import layout, sha256_of  # noqa: E402

# Corpus/flookup helpers live in the shared model module; re-exported here
# for the existing consumers of this module's API.
from oe_pipeline import (  # noqa: E402,F401
    PROTO_STRIP_RE,
    apply_down,
    load_rows,
    normalize_proto,
    run_stage,
)

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

# The ordered stage sequence is DERIVED from the shared executable model
# (oe_pipeline.py; authority: the production OldEnglish composition in
# germanic.txt). One (stage label, snapshot bin) pair per named executable
# stage, labels = canonical Foma identifiers. No hand-maintained copy.
STAGES: List[Tuple[str, str]] = [
    (s.foma_identifier, s.snapshot_bin) for s in oe_pipeline.named_stages()
]

# Markdown section headers injected before the named stage in the trace
# output. Presentation metadata only — they do NOT determine rule order.
# Some PGmc/PWGmc rules appear in later sections because the cascade
# applies them late for chronological-interaction reasons.
STAGE_HEADERS: Dict[str, str] = {
    "EnglishProtoInput": "## Section 1: Proto-Germanic consonant inheritance",
    "PNWGmcUnstressedAiMonophthongization": "## Section 2: Northwest and West Germanic developments",
    "EAFAiMonophthongization": "## Section 3: Early Anglo-Frisian (North Sea Germanic)",
    "OEAwjGlideFormation": "## Section 4: Old English",
    "OldEnglishOrthography": "## Section 5: Orthography & surface",
}


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


def provenance_lines(tsv_path: Path, bin_path: Path, fsts_dir: Path) -> List[str]:
    """Provenance block recording the canonical live inputs of this report.

    Source files (germanic.txt, old_english_sandbox.txt, the TSV) are the
    freshness contract enforced by test_final_z_firing_populations.py: if the
    committed report's hashes do not match the live sources, the report is
    stale. The compiled .bin hash is informational only — foma compilation is
    byte-non-deterministic, so it is NOT part of the freshness contract.
    """
    lines = ["=== PROVENANCE ==="]
    for label, path in [
        ("germanic.txt", fsts_dir / "germanic.txt"),
        ("old_english_sandbox.txt", fsts_dir / "old_english_sandbox.txt"),
        ("germanic-aligned-final.tsv", tsv_path),
    ]:
        lines.append(f"{label} sha256: {sha256_of(path)}")
    lines.append(f"old_english.bin sha256 (informational): {sha256_of(bin_path)}")
    lines.append("")
    return lines


def write_report(
    rows: Iterable[Dict[str, str]],
    bin_path: Path,
    bin_dir: Path,
    output_path: Path,
    trace_all: bool = False,
    provenance: List[str] | None = None,
) -> None:
    buckets: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    stage_fires: Dict[str, List[str]] = defaultdict(list)
    fronted_rows: List[str] = []; unfronted_rows: List[str] = []; fronting_correct: List[str] = []; fronting_unfronting_correct: List[str] = []; fronting_unfronting_incorrect: List[str] = []
    for row in rows:
        afb = run_stage(bin_dir, "old_english_sandbox_after_eaf_brightening.bin", row["proto_norm"]); ar = run_stage(bin_dir, "old_english_sandbox_after_oe_a_restoration.bin", row["proto_norm"])
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
    if provenance:
        lines.extend(provenance)
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


def default_paths() -> Dict[str, Path]:
    """Resolve canonical default paths via the shared runtime layout.

    The authoritative runtime bin directory is the foma working directory:
    <repo>/backend on the host, /usr/app inside the container.  Never
    Germanic/fsts/, which may hold stale duplicates.
    """
    rt = layout()
    return {
        "tsv": rt.corpus_tsv,
        "bin": rt.bin_dir / "old_english.bin",
        "bin_dir": rt.bin_dir,
        "fsts_dir": rt.fsts_dir,
        "output": rt.docs_dir / "debug_snapshots" / "oe_full_trace_report.txt",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    defaults = default_paths()
    germanic_dir = Path(__file__).resolve().parent.parent
    parser.add_argument(
        "--tsv",
        default=str(defaults["tsv"]),
        help="Aligned TSV with Old English rows (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(defaults["bin"]),
        help="Generator FST for apply-down (default: %(default)s)",
    )
    parser.add_argument(
        "--bin-dir",
        default=str(defaults["bin_dir"]),
        help="Directory containing old_english_sandbox_after_*.bin (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=str(defaults["output"]),
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
    fsts_dir = germanic_dir / "fsts"
    provenance = provenance_lines(tsv_path, bin_path, fsts_dir)
    write_report(rows, bin_path, bin_dir, output_path, trace_all=args.all,
                 provenance=provenance)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

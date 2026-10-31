#!/usr/bin/env python3
"""Shared parser for the canonical OE full-trace report format.

One authoritative reader for ``Germanic/docs/debug_snapshots/
oe_full_trace_report.txt``: the provenance header, the per-lexeme stage
traces, the RAW STAGE FIDELITY section and the STAGE FIRING SUMMARY.
Used by the derivation-class projection (oe_derivation_class_trace_report)
and by incremental regression (incremental_regression), so the committed
report has exactly one parsing authority and never needs re-evaluation to
be read.

This module is stdlib-only and never touches Foma, the runtime layout or
the working tree: callers supply the report text and, for provenance
validation, the source hashes belonging to the report's own version
(live files for the current state, Git blobs for a predecessor).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Mapping, Optional, Tuple

PROVENANCE_MARKER = "=== PROVENANCE ==="
FIDELITY_MARKER = "=== RAW STAGE FIDELITY ==="
FIRING_MARKER = "=== STAGE FIRING SUMMARY ==="

# Repository-relative paths of the sources hashed in the provenance block,
# keyed by their provenance labels. These are the files a report must be
# validated against -- for a historical report, at its own Git state.
SOURCE_PATHS: Dict[str, str] = {
    "germanic.txt": "Germanic/fsts/germanic.txt",
    "old_english_sandbox.txt": "Germanic/fsts/old_english_sandbox.txt",
    "germanic-aligned-final.tsv": "Germanic/data/germanic-aligned-final.tsv",
    "entry_context_metadata.tsv": "Germanic/data/entry_context_metadata.tsv",
    "oe_input_context.py": "backend/oe_input_context.py",
    "oe_full_trace_report.py": "Germanic/tools/oe_full_trace_report.py",
}
# Labels whose hash is also recorded in the build manifest (compilation
# inputs); the rest participate in evaluation/report generation only.
MANIFEST_EXEMPT = {
    "entry_context_metadata.tsv", "oe_input_context.py",
    "oe_full_trace_report.py",
}

_PROVENANCE_HASH_RE = re.compile(
    r"^(\S+) sha256(?: \(informational\))?: ([0-9a-f]{64})$")

# Identical to the historical oe_derivation_class_trace_report regex: one
# match per lexeme block, INPUT_CONTEXT optional in older reports.
ENTRY_RE = re.compile(
    r"^--- (.*?) ---\nPROTO: ([^\n]*)\n(?:INPUT_CONTEXT: ([^\n]*)\n)?"
    r"EXPECTED: ([^\n]*)\nOUTPUTS: ([^\n]*)\n(.*?)(?=^--- |^=== |\Z)",
    re.M | re.S)

STAGE_LINE_RE = re.compile(
    r"^([A-Za-z][A-Za-z0-9]*)((?: \[[^\]]+\])*): (.*)$")

Key = Tuple[str, str, str]  # (concept, proto, expected)


@dataclass(frozen=True)
class Provenance:
    present: bool
    canonical: bool
    recorded: Mapping[str, str]  # label -> sha256 (incl. manifest:* labels)
    meta: Mapping[str, str]      # build_manifest_* fields


@dataclass(frozen=True)
class StageLine:
    label: str                 # canonical Foma identifier
    no_change: bool
    forms: Tuple[str, ...]     # displayed forms, in order


@dataclass(frozen=True)
class EntryTrace:
    concept: str
    proto: str
    input_context: Optional[str]  # None in pre-context report formats
    expected: str
    outputs: str                  # raw OUTPUTS field ('+?' == no output)
    stages: Tuple[StageLine, ...]
    body: str                     # verbatim stage-trace body


def parse_provenance(text: str) -> Provenance:
    if PROVENANCE_MARKER not in text:
        return Provenance(False, False, {}, {})
    recorded: Dict[str, str] = {}
    meta: Dict[str, str] = {}
    canonical = False
    for line in text.split(PROVENANCE_MARKER, 1)[1].splitlines():
        line = line.strip()
        if not line:
            if recorded:
                break
            continue
        if line.startswith("bins_provenance: canonical"):
            canonical = True
        if ": " in line and line.startswith("build_manifest_"):
            key, value = line.split(": ", 1)
            meta[key] = value.strip()
        m = _PROVENANCE_HASH_RE.match(line)
        if m:
            recorded[m.group(1)] = m.group(2)
    return Provenance(True, canonical, recorded, meta)


def provenance_problems(
    text: str,
    source_hashes: Mapping[str, Optional[str]],
    *,
    expected_bins: Optional[str] = None,
    foma_version: Optional[str] = None,
) -> List[str]:
    """Freshness/provenance problems of a trace report (empty == usable).

    ``source_hashes`` maps each provenance label of SOURCE_PATHS to the
    sha256 of that source *in the report's own version* (None == the file
    does not exist in that state). ``expected_bins``/``foma_version``, when
    given, additionally enforce the build-identity contract (used for the
    current state only; a predecessor is validated against itself).
    """
    prov = parse_provenance(text)
    if not prov.present:
        return ["trace report has no PROVENANCE block; regenerate with "
                "tools/oe_full_trace_report.py --all"]
    problems: List[str] = []
    if not prov.canonical:
        problems.append("trace report bins provenance is not canonical "
                        "(missing or NONCANONICAL DEBUG); regenerate from "
                        "validated canonical bins")
    recorded = prov.recorded
    for label in SOURCE_PATHS:
        if label not in recorded:
            problems.append(f"trace PROVENANCE lacks a hash for {label}")
        elif source_hashes.get(label) is None:
            problems.append(f"source state lacks a file for {label}; the "
                            "trace report cannot be validated against it")
        elif recorded[label] != source_hashes[label]:
            problems.append(f"trace report is STALE w.r.t. {label}")
        if label in MANIFEST_EXEMPT:
            continue
        manifest_label = f"manifest:{label}"
        if manifest_label not in recorded:
            problems.append(f"trace PROVENANCE lacks {manifest_label} "
                            "(pre-build-identity report); regenerate")
        elif recorded.get(label) and recorded[manifest_label] != recorded[label]:
            problems.append(f"trace report's build manifest disagrees with "
                            f"its own source hash for {label}")
    if expected_bins is not None and (
            prov.meta.get("build_manifest_expected_bins") != expected_bins):
        problems.append(
            "trace report's expected-bin count "
            f"({prov.meta.get('build_manifest_expected_bins', 'missing')}) "
            f"does not match the current executable model contract "
            f"({expected_bins}); regenerate from a current canonical build")
    if foma_version is not None and (
            prov.meta.get("build_manifest_foma_version") != foma_version):
        problems.append(
            "trace report's recorded Foma version "
            f"({prov.meta.get('build_manifest_foma_version', 'missing')}) "
            f"differs from the current build manifest ({foma_version}); "
            "regenerate under the current build configuration")
    return problems


def _parse_stage_lines(body: str) -> Tuple[StageLine, ...]:
    stages: List[StageLine] = []
    for line in body.splitlines():
        m = STAGE_LINE_RE.match(line)
        if not m:
            continue  # markdown section headers / blanks: presentation only
        label, annotations, forms = m.groups()
        stages.append(StageLine(
            label=label,
            no_change="[no-change]" in annotations,
            forms=tuple(forms.split(", ")) if forms else (),
        ))
    return tuple(stages)


def parse_entries(text: str) -> Dict[Key, EntryTrace]:
    """All lexeme blocks of a full-trace report, keyed by stable identity.

    The identity (concept, PROTO, EXPECTED) is the historical row identity
    used by every consumer of the committed report; duplicate identities
    are a hard error exactly as in the derivation-class projection.
    """
    entries: Dict[Key, EntryTrace] = {}
    for match in ENTRY_RE.finditer(text):
        concept, proto, context, expected, outputs, body = match.groups()
        key: Key = (concept, proto, expected)
        if key in entries:
            raise ValueError(f"duplicate full-trace identity: {key}")
        entries[key] = EntryTrace(
            concept=concept, proto=proto, input_context=context,
            expected=expected, outputs=outputs,
            stages=_parse_stage_lines(body), body=body)
    return entries


def parse_firing_summary(
    text: str,
) -> Optional[Dict[str, Tuple[int, List[Tuple[str, str]]]]]:
    """Ordered STAGE FIRING SUMMARY: label -> (count, [(lexeme, proto)]).

    Returns None when the report has no firing summary (which the census
    and firing-population consumers treat as a regeneration error).
    """
    idx = text.find(FIRING_MARKER)
    if idx < 0:
        return None
    summary: Dict[str, Tuple[int, List[Tuple[str, str]]]] = {}
    current: Optional[str] = None
    for line in text[idx + len(FIRING_MARKER):].splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*): (\d+)$", line)
        if m:
            current = m.group(1)
            summary[current] = (int(m.group(2)), [])
            continue
        if current and " :: " in line:
            count, pairs = summary[current]
            for chunk in line.split(", "):
                lexeme, _, proto = chunk.partition(" :: ")
                pairs.append((lexeme.strip(), proto.strip()))
            summary[current] = (count, pairs)
            current = None
    return summary


def parse_fidelity(
    text: str,
) -> Optional[Dict[Key, Dict[str, Dict[str, object]]]]:
    """RAW STAGE FIDELITY section: raw-stage distinctions per entry.

    Returns None when the section is absent (older report formats; the
    caller must state that limitation explicitly rather than guessing).
    Otherwise maps (concept, proto, expected) -> stage label ->
    {"rejected": bool, "raw": tuple of raw forms or None}.
    """
    idx = text.find(FIDELITY_MARKER)
    if idx < 0:
        return None
    fidelity: Dict[Key, Dict[str, Dict[str, object]]] = {}
    current: Optional[Dict[str, Dict[str, object]]] = None
    for line in text[idx + len(FIDELITY_MARKER):].splitlines():
        line = line.rstrip()
        if line.startswith("=== "):
            break
        header = re.match(r"^--- (.*?) \| (.*?) \| (.*?) ---$", line)
        if header:
            key: Key = header.groups()  # type: ignore[assignment]
            if key in fidelity:
                raise ValueError(f"duplicate fidelity identity: {key}")
            current = fidelity.setdefault(key, {})
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*): (rejected|raw = .*)$", line)
        if m and current is not None:
            label, value = m.groups()
            record = current.setdefault(label,
                                        {"rejected": False, "raw": None})
            if value == "rejected":
                record["rejected"] = True
            else:
                record["raw"] = tuple(value[len("raw = "):].split(", "))
    return fidelity

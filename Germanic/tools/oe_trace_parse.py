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
# Version 1 (original contract): compilation inputs, corpus/context data,
# the input-context helper and the generator itself.
V1_SOURCE_PATHS: Dict[str, str] = {
    "germanic.txt": "Germanic/fsts/germanic.txt",
    "old_english_sandbox.txt": "Germanic/fsts/old_english_sandbox.txt",
    "germanic-aligned-final.tsv": "Germanic/data/germanic-aligned-final.tsv",
    "entry_context_metadata.tsv": "Germanic/data/entry_context_metadata.tsv",
    "oe_input_context.py": "backend/oe_input_context.py",
    "oe_full_trace_report.py": "Germanic/tools/oe_full_trace_report.py",
}
# Version 2 extends the contract to the evaluation helpers that genuinely
# participate in producing the trace without being compilation inputs:
# oe_pipeline (stage set/order and bin mapping), batch_apply_down (the
# Foma lookup used for every stage) and capr_runtime (layout + manifest
# validation under which the report is generated). Changes to these can
# alter derivations without changing any v1-hashed file.
V2_SOURCE_PATHS: Dict[str, str] = {
    "oe_pipeline.py": "Germanic/tools/oe_pipeline.py",
    "sound_change_order_sensitivity.py":
        "Germanic/tools/sound_change_order_sensitivity.py",
    "capr_runtime.py": "Germanic/tools/capr_runtime.py",
}
SOURCE_PATHS: Dict[str, str] = {**V1_SOURCE_PATHS, **V2_SOURCE_PATHS}
PROVENANCE_VERSION = 2
# Labels whose hash is also recorded in the build manifest (compilation
# inputs); the rest participate in evaluation/report generation only.
MANIFEST_EXEMPT = {
    "entry_context_metadata.tsv", "oe_input_context.py",
    "oe_full_trace_report.py", *V2_SOURCE_PATHS,
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
    version: int = 1             # declared contract version (1 if undeclared)


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
    version = 1
    for line in text.split(PROVENANCE_MARKER, 1)[1].splitlines():
        line = line.strip()
        if not line:
            if recorded:
                break
            continue
        if line.startswith("trace_provenance_version: "):
            declared = line.split(": ", 1)[1].strip()
            version = int(declared) if declared.isdigit() else 1
        if line.startswith("bins_provenance: canonical"):
            canonical = True
        if ": " in line and line.startswith("build_manifest_"):
            key, value = line.split(": ", 1)
            meta[key] = value.strip()
        m = _PROVENANCE_HASH_RE.match(line)
        if m:
            recorded[m.group(1)] = m.group(2)
    return Provenance(True, canonical, recorded, meta, version)


def required_labels(version: int) -> List[str]:
    """Provenance labels a report of *version* must record."""
    labels = list(V1_SOURCE_PATHS)
    if version >= 2:
        labels.extend(V2_SOURCE_PATHS)
    return labels


def provenance_problems(
    text: str,
    source_hashes: Mapping[str, Optional[str]],
    *,
    expected_bins: Optional[str] = None,
    foma_version: Optional[str] = None,
    require_version: Optional[int] = None,
) -> List[str]:
    """Freshness/provenance problems of a trace report (empty == usable).

    ``source_hashes`` maps each provenance label of SOURCE_PATHS to the
    sha256 of that source *in the report's own version* (None == the file
    does not exist in that state). ``expected_bins``/``foma_version``, when
    given, additionally enforce the build-identity contract (used for the
    current state only; a predecessor is validated against itself).

    Each report is checked against its own declared contract version: a
    report declaring ``trace_provenance_version: 2`` must record every v2
    label (missing required provenance is never silently accepted), while
    a legacy report without the declaration is validated against the v1
    label set only -- the caller states that limitation explicitly.
    ``require_version`` additionally rejects any report declaring an older
    contract (the ordinary freshness check for the current canonical
    report, which must always satisfy the current contract).
    """
    prov = parse_provenance(text)
    if not prov.present:
        return ["trace report has no PROVENANCE block; regenerate with "
                "tools/oe_full_trace_report.py --all"]
    problems: List[str] = []
    if require_version is not None and prov.version < require_version:
        problems.append(
            f"trace provenance contract v{prov.version} predates the "
            f"required v{require_version}: evaluation-helper provenance "
            f"({', '.join(V2_SOURCE_PATHS)}) is not recorded; regenerate "
            "with tools/oe_full_trace_report.py --all")
    if not prov.canonical:
        problems.append("trace report bins provenance is not canonical "
                        "(missing or NONCANONICAL DEBUG); regenerate from "
                        "validated canonical bins")
    recorded = prov.recorded
    for label in required_labels(prov.version):
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
            if label in current:
                raise ValueError(
                    "duplicate fidelity record for entry "
                    f"{' | '.join(key)} stage {label}")
            record = current.setdefault(label,
                                        {"rejected": False, "raw": None})
            if value == "rejected":
                record["rejected"] = True
            else:
                record["raw"] = tuple(value[len("raw = "):].split(", "))
    return fidelity


_FIRING_LABEL_RE = re.compile(r"^([A-Za-z][A-Za-z0-9]*): \d+$")


def structural_problems(text: str) -> List[str]:
    """Structural-completeness problems of a full-trace report.

    Checks every parsed lexical entry against the stage sequence the report
    itself declares in its STAGE FIRING SUMMARY: complete membership, the
    declared order, no duplicates, no unexpected stages, and recorded
    outputs for every stage; the firing summary must declare each stage
    exactly once, and fidelity annotations must refer to existing entries
    and stages without duplicate records. Operates purely on the report
    text -- no Foma, no assumption that two compared reports share stages.
    Older formats (no RAW STAGE FIDELITY section, no INPUT_CONTEXT) remain
    valid.
    """
    firing = parse_firing_summary(text)
    if firing is None:
        return ["report has no STAGE FIRING SUMMARY (the report's own "
                "stage-sequence declaration); regenerate with "
                "tools/oe_full_trace_report.py --all"]
    problems: List[str] = []
    declared = list(firing)
    firing_section = text[text.find(FIRING_MARKER) + len(FIRING_MARKER):]
    seen_labels: List[str] = []
    for line in firing_section.splitlines():
        m = _FIRING_LABEL_RE.match(line.strip())
        if m:
            seen_labels.append(m.group(1))
    for label in sorted({l for l in seen_labels if seen_labels.count(l) > 1}):
        problems.append(f"firing summary declares stage {label} more than "
                        "once; the stage sequence is incoherent")
    if not declared:
        problems.append("firing summary declares no stages")
    try:
        entries = parse_entries(text)
    except ValueError as exc:
        return problems + [str(exc)]
    if not entries:
        problems.append("report contains no lexical entries")
    expected_set = set(declared)
    for key, entry in entries.items():
        ident = " | ".join(key)
        labels = [stage.label for stage in entry.stages]
        if labels != declared:
            label_set = set(labels)
            missing = [l for l in declared if l not in label_set]
            unexpected = sorted(label_set - expected_set)
            duplicated = sorted({l for l in labels if labels.count(l) > 1})
            if missing:
                problems.append(f"entry {ident}: missing stage(s) "
                                + ", ".join(missing))
            if unexpected:
                problems.append(f"entry {ident}: unexpected stage(s) "
                                + ", ".join(unexpected))
            if duplicated:
                problems.append(f"entry {ident}: duplicated stage(s) "
                                + ", ".join(duplicated))
            if not (missing or unexpected or duplicated):
                problems.append(f"entry {ident}: stages are out of the "
                                "order declared by the firing summary")
        for stage in entry.stages:
            if not stage.forms:
                problems.append(f"entry {ident}: stage {stage.label} has "
                                "no recorded outputs")
    try:
        fidelity = parse_fidelity(text)
    except ValueError as exc:
        problems.append(str(exc))
        fidelity = None
    for key, stages in (fidelity or {}).items():
        ident = " | ".join(key)
        if key not in entries:
            problems.append(f"fidelity annotation refers to a nonexistent "
                            f"entry {ident}")
            continue
        for label in stages:
            if label not in expected_set:
                problems.append(f"fidelity annotation for entry {ident} "
                                f"refers to an unknown stage {label}")
    return problems

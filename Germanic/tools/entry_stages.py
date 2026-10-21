#!/usr/bin/env python3
"""Stage resolution for corpus entries: the one authoritative implementation.

This is scientific code, not presentation code. The reconstruction survey and
the lexical assembler both consume it, and both record its hash in their
provenance. It must not import or contain any ordering, layout or other
editorial logic: changing where something is published must never change a
scientific dependency.
"""
from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
# Historical-stage sidecar for reconstructed selected inputs, keyed by row_id.
# Lives with the corpus data (upstream of assembly) because it encodes scholarly
# historical judgments, not assembly output.
#
# CAPR project convention (author decision): PROTO is the Proto-Germanic
# lexeme-level reconstruction, so proto_stage is always pgmc. When PROTOFORM ==
# PROTO the selected input IS that PGmc reconstruction, so protoform_stage = pgmc
# automatically. The sidecar therefore records ONLY the exceptional rows where
# PROTOFORM != PROTO, whose stage is a separate historical question. A PROTOFORM
# != PROTO row with no sidecar entry fails closed (it is never silently pgmc).
STAGE_METADATA_PATH = REPO_ROOT / "Germanic/data/entry_stage_metadata.tsv"


def load_stage_metadata() -> dict[str, dict[str, str]]:
    """row_id -> {protoform_stage, protoform_variety} for the PROTOFORM != PROTO exception rows."""
    with STAGE_METADATA_PATH.open(encoding="utf-8") as handle:
        return {
            row["row_id"].strip(): {
                "protoform_stage": (row.get("protoform_stage") or "").strip(),
                "protoform_variety": (row.get("protoform_variety") or "").strip(),
            }
            for row in csv.DictReader(handle, delimiter="\t")
        }


def resolve_stages(row_id: str, proto: str, protoform: str, sidecar: dict[str, dict[str, str]]) -> tuple[str, str, str, list[str]]:
    """Resolve (proto_stage, protoform_stage, protoform_variety) under the CAPR convention.

    proto_stage is always pgmc (PROTO is the PGmc lexeme reconstruction). When
    PROTOFORM == PROTO, protoform_stage is pgmc by convention. When they differ,
    protoform_stage must come from an explicit sidecar decision; a missing entry
    is reported (fail closed), never defaulted to pgmc. protoform_variety is a
    separate orthogonal axis (e.g. 'transponent') and is blank unless the sidecar
    declares one; equality rows never carry a variety.
    """
    notes: list[str] = []
    proto_stage = "pgmc"
    if (proto or "").strip() and (proto or "").strip() == (protoform or "").strip():
        return proto_stage, "pgmc", "", notes
    entry = sidecar.get(str(row_id))
    if entry and entry.get("protoform_stage"):
        return proto_stage, entry["protoform_stage"], entry.get("protoform_variety", ""), notes
    notes.append("PROTOFORM != PROTO but no explicit stage decision (unresolved)")
    return proto_stage, "", "", notes

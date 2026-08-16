#!/usr/bin/env python3
"""Extract a machine-readable manifest of the actual executable cascade order.

The Old English derivation is driven by the ``EnglishProtoToOE`` composition in
``Germanic/fsts/germanic.txt``.  That composition begins with the historically
mixed ``EarlyEnglishLineChanges`` block and then composes a long sequence of individual
rules with ``.o.``.  This tool flattens that composition into a single ordered
list of Foma identifiers, expanding the ``EarlyEnglishLineChanges`` block inline so the
manifest reflects the true rule-application order.

The manifest is *descriptive*: it records what the cascade currently does.  It
does not encode any historical stage judgement — stage/scope metadata lives in
the authoritative rule registry
(``Germanic/docs/sound_changes/sound_change_historical_staging_map.tsv``).

Output (deterministic TSV, sorted by executable position):

    position    foma_identifier    origin_block

``origin_block`` is ``EarlyEnglishLineChanges`` for rules expanded out of that block, or
``EnglishProtoToOE`` for rules composed directly in the master pipeline.

This script is pure text parsing; it needs neither foma nor flookup and runs on
the host.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
DEFAULT_OUT = REPO_ROOT / "Germanic/docs/sound_changes/cascade_baseline/cascade_order_manifest.tsv"

# A Foma identifier is an alphanumeric/underscore token that starts with a
# letter.  Composition members appear as ``.o. Identifier`` or as the first
# token inside the block body.
_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def _strip_comments(text: str) -> str:
    """Remove Foma ``#`` line comments while preserving line structure."""
    out_lines = []
    for line in text.splitlines():
        hash_pos = line.find("#")
        if hash_pos != -1:
            line = line[:hash_pos]
        out_lines.append(line)
    return "\n".join(out_lines)


def _extract_block_body(text: str, define_name: str, open_char: str, close_char: str) -> str:
    """Return the raw body between the matching delimiters of a define block."""
    marker = f"define {define_name} "
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"could not find 'define {define_name}' in FST source")
    open_pos = text.find(open_char, start)
    if open_pos < 0:
        raise ValueError(f"could not find opening '{open_char}' for {define_name}")
    depth = 0
    for i in range(open_pos, len(text)):
        ch = text[i]
        if ch == open_char:
            depth += 1
        elif ch == close_char:
            depth -= 1
            if depth == 0:
                return text[open_pos + 1 : i]
    raise ValueError(f"unterminated block for {define_name}")


def _composition_members(body: str) -> list[str]:
    """Flatten a ``.o.``-separated composition body into member identifiers.

    The first member has no leading ``.o.``; subsequent members follow ``.o.``.
    Only bare identifiers are treated as named-rule members; inline regex
    fragments (containing ``->``, ``{``, ``[`` etc.) are skipped because they are
    anonymous and cannot be reordered as named stages.
    """
    # Normalise whitespace, then split on the ``.o.`` composition operator.
    segments = re.split(r"\.o\.", body)
    members: list[str] = []
    for seg in segments:
        token = seg.strip()
        if not token:
            continue
        # A named member is a single bare identifier.  Take the first
        # whitespace-delimited token and verify it is a clean identifier and
        # that nothing else (an inline regex) follows.
        first = token.split()[0] if token.split() else ""
        if _IDENT_RE.match(token) or (_IDENT_RE.match(first) and token == first):
            members.append(first)
        else:
            # Anonymous inline fragment (e.g. a bare `[...]` rewrite) — record a
            # placeholder so positions still reflect the true composition length.
            members.append(f"<inline:{len(members)}>")
    return members


def build_manifest(fst_path: Path) -> list[dict[str, str]]:
    text = _strip_comments(fst_path.read_text(encoding="utf-8"))

    pwgmc_body = _extract_block_body(text, "EarlyEnglishLineChanges", "[", "]")
    pwgmc_members = _composition_members(pwgmc_body)

    pipeline_body = _extract_block_body(text, "EnglishProtoToOE", "(", ")")
    pipeline_members = _composition_members(pipeline_body)

    # SC096 RootNounNomZLoss is composed at the head of EnglishProtoToOE,
    # before EarlyEnglishLineChanges (it must precede PWGmcIjContraction).
    # Emit any such head rules in order, then expand EarlyEnglishLineChanges.
    if "EarlyEnglishLineChanges" not in pipeline_members:
        raise ValueError(
            "expected EnglishProtoToOE to contain EarlyEnglishLineChanges; "
            f"got {pipeline_members[:3]!r}"
        )
    block_index = pipeline_members.index("EarlyEnglishLineChanges")

    rows: list[dict[str, str]] = []
    position = 0
    for ident in pipeline_members[:block_index]:
        position += 1
        rows.append({"position": str(position), "foma_identifier": ident, "origin_block": "EnglishProtoToOE"})
    # Expand EarlyEnglishLineChanges in place of its reference in the pipeline.
    for ident in pwgmc_members:
        position += 1
        rows.append({"position": str(position), "foma_identifier": ident, "origin_block": "EarlyEnglishLineChanges"})
    for ident in pipeline_members[block_index + 1:]:
        position += 1
        rows.append({"position": str(position), "foma_identifier": ident, "origin_block": "EnglishProtoToOE"})
    return rows


def write_manifest(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["position\tfoma_identifier\torigin_block"]
    for row in rows:
        lines.append(f"{row['position']}\t{row['foma_identifier']}\t{row['origin_block']}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fst", type=Path, default=DEFAULT_FST, help="Path to germanic.txt")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output manifest TSV path")
    parser.add_argument("--check", action="store_true", help="Print manifest to stdout without writing")
    args = parser.parse_args()

    rows = build_manifest(args.fst)
    named = [r for r in rows if not r["foma_identifier"].startswith("<inline:")]
    inline = [r for r in rows if r["foma_identifier"].startswith("<inline:")]
    if args.check:
        for r in rows:
            print(f"{r['position']}\t{r['foma_identifier']}\t{r['origin_block']}")
    else:
        write_manifest(rows, args.out)
        print(f"wrote {args.out} ({len(rows)} positions: {len(named)} named, {len(inline)} inline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

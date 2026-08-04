#!/usr/bin/env python3
"""Phase 1: inventory the CAPR research archive for the audited historical rules.

Adjudication-first: before judging any rule we must know which research files
exist for it. This tool maps each audited SC to every relevant archive file so
the adjudication reads sources rather than trusting the staging map (which is an
index of prior decisions, not independently authoritative).

For each audited SC it records the current registry metadata and the archive
files that reference it, categorised by archive layer. Ranged files (e.g.
``026-027-nasal-spirant-corridor.md``, ``049-050-...``) are attached to every SC
in their range.

Output: a TSV inventory plus a short coverage summary. Pure host-side file
discovery; it makes no historical judgement.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
DEFAULT_OUT = SC_DIR / "cascade_baseline/historical_audit_evidence_inventory.tsv"

# The rules the task requires auditing (plus any the archive later reveals).
DEFAULT_TARGETS = [f"SC{n:03d}" for n in range(3, 29)] + ["SC041", "SC042", "SC049", "SC050", "SC064"]

# Archive layers to scan, in read priority order.
ARCHIVE_LAYERS = {
    "reader_facing": SC_DIR / "reader_facing",
    "change_report_full": SC_DIR / "change_reports/full",
    "change_report_review": SC_DIR / "change_reports",
    "literature_dossier": SC_DIR / "literature_dossiers",
    "book_dossier": SC_DIR / "book_dossiers",
    "chronology_card": SC_DIR / "order_tests/chronology_cards",
}

# Leading run of one or more zero-padded 3-digit numbers, e.g. "026-027-..." or "049-050-...".
_LEADING_NUMS_RE = re.compile(r"^(\d{3})(?:-(\d{3}))*")


def _sc_numbers_in_filename(name: str) -> set[int]:
    """Return the SC numbers a filename's leading numeric range covers."""
    m = re.match(r"^((?:\d{3})(?:-\d{3})*)", name)
    if not m:
        return set()
    parts = [int(p) for p in m.group(1).split("-")]
    # A hyphenated pair like 026-027 denotes an inclusive range; 049-050 likewise.
    if len(parts) == 2 and parts[1] > parts[0] and parts[1] - parts[0] <= 12:
        return set(range(parts[0], parts[1] + 1))
    return set(parts)


def _read_tsv_skip_comments(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


def discover_files(targets: list[str]) -> dict[str, dict[str, list[str]]]:
    """Return {sc_id: {layer: [relative_paths]}} for files referencing each SC."""
    want = {int(sc[2:]) for sc in targets}
    result: dict[str, dict[str, list[str]]] = {sc: {layer: [] for layer in ARCHIVE_LAYERS} for sc in targets}
    for layer, directory in ARCHIVE_LAYERS.items():
        if not directory.exists():
            continue
        for path in sorted(directory.iterdir()):
            if not path.is_file() or not path.name.endswith(".md"):
                continue
            nums = _sc_numbers_in_filename(path.name)
            for n in nums & want:
                sc = f"SC{n:03d}"
                result[sc][layer].append(path.relative_to(REPO_ROOT).as_posix())
    return result


def build_inventory(targets: list[str]) -> list[dict[str, str]]:
    staging = {r["sc_id"]: r for r in _read_tsv_skip_comments(STAGING_MAP)}
    with INVENTORY.open(encoding="utf-8") as handle:
        inv = {r["change_id"]: r for r in csv.DictReader(handle, delimiter="\t")}
    files = discover_files(targets)

    rows: list[dict[str, str]] = []
    for sc in targets:
        s = staging.get(sc, {})
        i = inv.get(sc, {})
        layer_files = files.get(sc, {})
        rows.append({
            "sc_id": sc,
            "fst_identifier": s.get("fst_identifier", ""),
            "implemented_transformation": (i.get("foma_definition_raw", "") or "").strip(),
            "current_reader_name": s.get("display_name", ""),
            "current_book_chapter": s.get("v1_chapter", ""),
            "current_hist_stage": s.get("hist_stage", ""),
            "current_hist_scope": s.get("hist_scope", ""),
            "current_confidence": s.get("confidence", ""),
            "staging_chronology_problem": s.get("chronology_problem", ""),
            "reader_facing_file": "; ".join(layer_files.get("reader_facing", [])),
            "change_report_full": "; ".join(layer_files.get("change_report_full", [])),
            "change_report_review": "; ".join(layer_files.get("change_report_review", [])),
            "literature_dossier": "; ".join(layer_files.get("literature_dossier", [])),
            "book_dossier": "; ".join(layer_files.get("book_dossier", [])),
            "chronology_card": "; ".join(layer_files.get("chronology_card", [])),
        })
    return rows


FIELDS = [
    "sc_id", "fst_identifier", "implemented_transformation",
    "current_reader_name", "current_book_chapter",
    "current_hist_stage", "current_hist_scope", "current_confidence",
    "staging_chronology_problem",
    "reader_facing_file", "change_report_full", "change_report_review",
    "literature_dossier", "book_dossier", "chronology_card",
]


def write_inventory(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--targets", nargs="*", default=DEFAULT_TARGETS)
    parser.add_argument("--print-coverage", action="store_true")
    args = parser.parse_args()

    rows = build_inventory(args.targets)
    write_inventory(rows, args.out)
    print(f"wrote {args.out} ({len(rows)} audited rules)")
    if args.print_coverage:
        for r in rows:
            layers = [layer for layer in ("reader_facing_file", "change_report_full",
                                          "literature_dossier", "book_dossier", "chronology_card")
                      if r[layer]]
            print(f"  {r['sc_id']}: {r['fst_identifier']:<30} evidence layers: {', '.join(layers) or 'NONE'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

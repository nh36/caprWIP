#!/usr/bin/env python3
"""Read-only preservation/accounting for the c06c896d architectural cleanup.

This is a migration audit, not a new scientific baseline or artifact graph.
Run --check during this cleanup; later authorized scientific/prose changes need
not preserve this release's current SOURCE bytes. Historical archive bytes do.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = "c06c896da21f50df756d91c9f5729511b910b8c9"
LEXICAL = Path("Germanic/docs/lexeme_reports")
ASSEMBLY = Path("Germanic/docs/assembly")


@lru_cache
def baseline_blobs() -> dict[str, str]:
    result = subprocess.check_output(
        ["git", "ls-tree", "-rz", BASE], cwd=ROOT)
    return {
        path.decode(): metadata.decode().split()[2]
        for record in result.split(b"\0") if record
        for metadata, path in [record.split(b"\t", 1)]
    }


def blob_id(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def archive_pairs() -> list[tuple[Path, Path]]:
    """Derive old/new paths from the mirrored archive, not an editable register."""
    pairs = []
    old = baseline_blobs()
    for root in (LEXICAL, ASSEMBLY):
        for target in sorted((ROOT / root / "archive").rglob("*")):
            if not target.is_file():
                continue
            source = root / target.relative_to(ROOT / root / "archive")
            if str(source) in old:
                pairs.append((source, target.relative_to(ROOT)))
    return pairs


def protected(path: str) -> bool:
    p = Path(path)
    return (
        path.startswith("Germanic/data/")
        or path.startswith("Germanic/fsts/") and p.suffix == ".txt"
        or "/sound_changes/cascade_baseline/" in path
        or "/sound_changes/audits/" in path
        or "/sound_changes/book_dossiers/" in path
        or "/sound_changes/literature_dossiers/" in path
        or path.startswith("Germanic/docs/archive/")
        or path.endswith((".model.md", ".source_ledger.md"))
        or path.startswith(str(LEXICAL / "research_memos") + "/")
        and p.name.split("-", 1)[0].isdigit()
        or "/assembly/book_prose/" in path
        or path == str(LEXICAL / "pgmc_integration/editorial_cases.tsv")
        or path == str(LEXICAL / "report_manifest.tsv")
        or path.startswith(str(LEXICAL / "pgmc_reconstructions") + "/")
        and (p.suffix == ".tsv" or "reading_accountability" in p.parts
             or p.name == "commentary.md")
        or "/sound_changes/registry/" in path and p.name in {
            "sc_registry.tsv", "chronology_edges.tsv", "sc_inventory_notes.tsv",
            "reader_chapters.tsv", "reader_files.tsv", "adjudication_programme.json",
            "archival_orders.tsv",
        }
    )


def accounting(paths: list[str]) -> dict:
    docs = [p for p in paths if p.startswith(str(LEXICAL) + "/")]
    active = [p for p in docs if "/archive/" not in p]
    return {
        "tracked_files": len(paths),
        "lexical_files": len(docs),
        "active_lexical_files": len(active),
        "active_lexical_markdown": sum(p.endswith(".md") for p in active),
        "active_by_directory": dict(sorted(Counter(
            str(Path(p).relative_to(LEXICAL).parent) for p in active).items())),
    }


def audit() -> dict:
    old = baseline_blobs()
    pairs = archive_pairs()
    errors = []
    for source, target in pairs:
        if blob_id(ROOT / target) != old[str(source)]:
            errors.append(f"historical content changed: {source} -> {target}")
    checked = [p for p in old if protected(p)]
    for path in checked:
        current = ROOT / path
        if not current.is_file() or blob_id(current) != old[path]:
            errors.append(f"protected cleanup SOURCE changed: {path}")
    listed = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached"],
        cwd=ROOT).decode().split("\0")
    current = sorted({p for p in listed if p and (ROOT / p).is_file()})
    return {
        "baseline": BASE, "before": accounting(list(old)),
        "after": accounting(current), "protected_files_checked": len(checked),
        "archives": [{"old": str(a), "new": str(b), "git_blob": old[str(a)]}
                     for a, b in pairs],
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if historical or protected cleanup bytes differ")
    args = parser.parse_args()
    result = audit()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return int(args.check and bool(result["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Iterable

DOCUMENT_SUFFIXES = {".pdf", ".djvu", ".epub", ".doc", ".docx"}
CURATED_FIELDS = (
    "work_key", "edition_key", "status", "classification", "priority",
    "ingestion_status", "extraction_status", "missing_material",
    "image_verification_status", "consulted", "bibliography_key",
    "next_action",
)
PRIORITY_FIELDS = (
    "source_path", "original_filename", "sha256", "size", "type",
    "title", "author", "pages", "native_sample_status",
    "canonical_matches", "status", "scope", "priority", "consulted",
    "classification", "ingestion_status", "extraction_status",
    "missing_material", "image_verification_status", "bibliography_key",
    "next_action",
)
TODAY_FIELDS = (
    "source_path", "original_filename", "sha256", "size", "type",
    "title", "author", "pages", "native_sample_status",
    "canonical_matches", "status", "mtime", "mtime_is_download_date",
    "classification", "priority", "ingestion_status", "next_action",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdfinfo(path: Path) -> tuple[str, str, str]:
    try:
        completed = subprocess.run(
            ["pdfinfo", str(path)], check=False, capture_output=True,
            text=True, timeout=20,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "", "", ""
    fields = {}
    for line in completed.stdout.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields.get("Title", ""), fields.get("Author", ""), fields.get("Pages", "")


def native_sample_status(path: Path) -> str:
    if path.suffix.lower() != ".pdf":
        return "not_applicable"
    try:
        completed = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "3", "-layout", str(path), "-"],
            check=False, capture_output=True, text=True, timeout=30,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "unavailable"
    text = completed.stdout
    if len(text.strip()) < 100:
        return "no_usable_text_in_first_three_pages"
    if sum(text.count(marker) for marker in ("\ufffd", "\x00")) > 20:
        return "defective_in_first_three_pages"
    return "native_text_present_in_first_three_pages"


def canonical_index(repo: Path) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    reference_dir = repo / "docs/references"
    if not reference_dir.is_dir():
        return index
    for path in reference_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".pdf", ".epub", ".djvu"}:
            continue
        try:
            digest = sha256(path)
            public = str(path.relative_to(repo))
        except (OSError, ValueError):
            continue
        index.setdefault(digest, []).append(public)
    for matches in index.values():
        matches.sort()
    return index


def public_path(path: Path, repo: Path) -> str:
    try:
        return str(path.resolve().relative_to(repo.resolve()))
    except (ValueError, OSError):
        return str(path)


def relative_downloads_path(path: Path, downloads: Path) -> str:
    try:
        relative = path.resolve().relative_to(downloads.resolve())
        return str(Path("Downloads") / relative)
    except (ValueError, OSError):
        return str(path)


def scope_for(path: Path, germanic: Path, germanic2: Path) -> str:
    resolved = path.resolve()
    try:
        resolved.relative_to(germanic2.resolve())
        return "Germanic2"
    except ValueError:
        pass
    try:
        resolved.relative_to(germanic.resolve())
        return "Germanic"
    except ValueError:
        return "Other"


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def merge_curated(raw: dict[str, str], existing: dict[str, str]) -> dict[str, str]:
    merged = dict(raw)
    identities = (raw.get("sha256"), raw.get("source_path"), raw.get("original_filename"))
    if existing:
        for field in CURATED_FIELDS:
            if field in existing and existing[field]:
                merged[field] = existing[field]
    return merged


def existing_priority_index(path: Path) -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for row in read_tsv(path):
        sha = row.get("sha256", "")
        if sha:
            index[sha] = row
        elif row.get("source_path"):
            index["path:" + row["source_path"]] = row
    return index


def find_existing(index: dict[str, dict[str, str]], row: dict[str, str]):
    return index.get(row.get("sha256", "")) or (
        index.get("path:" + row["source_path"]) if row.get("source_path") else None
    )


def collect_priority(
    germanic: Path,
    germanic2: Path,
    repo: Path,
    index: dict[str, list[str]],
) -> tuple[list[dict[str, str]], dict[str, int]]:
    roots = []
    counts = {"Germanic": 0, "Germanic2": 0, "missing": 0}
    for name, root in (("Germanic", germanic), ("Germanic2", germanic2)):
        if not root.is_dir():
            counts["missing"] += 1
            continue
        roots.append((name, root))
    rows = []
    seen: set[str] = set()
    for name, root in roots:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in DOCUMENT_SUFFIXES:
                continue
            resolved = str(path.resolve())
            if resolved in seen:
                continue
            seen.add(resolved)
            try:
                digest = sha256(path)
                size = path.stat().st_size
            except OSError:
                continue
            title, author, pages = pdfinfo(path) if path.suffix.lower() == ".pdf" else ("", "", "")
            matches = index.get(digest, [])
            scope = scope_for(path, germanic, germanic2)
            counts[scope] = counts.get(scope, 0) + 1
            rows.append({
                "source_path": relative_downloads_path(path, germanic.parent),
                "original_filename": path.name,
                "sha256": digest,
                "size": str(size),
                "type": path.suffix.lower().lstrip("."),
                "title": title,
                "author": author,
                "pages": pages,
                "native_sample_status": native_sample_status(path),
                "canonical_matches": "|".join(matches),
                "status": "exact_canonical_duplicate" if matches else "new_external_original_candidate",
                "scope": scope,
                "priority": "",
                "consulted": "no",
                "classification": "",
                "ingestion_status": "preserved" if matches else "unclassified",
                "extraction_status": "",
                "missing_material": "",
                "image_verification_status": "",
                "bibliography_key": "",
                "next_action": "",
            })
    rows.sort(key=lambda row: (row["scope"], row["source_path"]))
    return rows, counts


def collect_today(downloads: Path, today: dt.date, repo: Path, index: dict[str, list[str]]) -> list[dict[str, str]]:
    if not downloads.is_dir():
        return []
    start = dt.datetime.combine(today, dt.time.min)
    end = start + dt.timedelta(days=1)
    rows = []
    for path in sorted(downloads.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in DOCUMENT_SUFFIXES:
            continue
        try:
            modified = dt.datetime.fromtimestamp(path.stat().st_mtime)
            digest = sha256(path)
            size = path.stat().st_size
        except OSError:
            continue
        if not start <= modified < end:
            continue
        title, author, pages = pdfinfo(path) if path.suffix.lower() == ".pdf" else ("", "", "")
        matches = index.get(digest, [])
        rows.append({
            "source_path": relative_downloads_path(path, downloads),
            "original_filename": path.name,
            "sha256": digest,
            "size": str(size),
            "type": path.suffix.lower().lstrip("."),
            "title": title,
            "author": author,
            "pages": pages,
            "native_sample_status": native_sample_status(path),
            "canonical_matches": "|".join(matches),
            "status": "exact_canonical_duplicate" if matches else "new_external_original_candidate",
            "mtime": modified.isoformat(timespec="seconds"),
            "mtime_is_download_date": "unknown",
            "classification": "",
            "priority": "",
            "ingestion_status": "preserved" if matches else "unclassified",
            "next_action": "",
        })
    rows.sort(key=lambda row: row["source_path"])
    return rows


def write_tsv(path: Path, rows: list[dict[str, str]], fields: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, delimiter="\t", fieldnames=list(fields), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def merge_inventory(
    raw_priority: list[dict[str, str]],
    existing_priority_path: Path,
) -> list[dict[str, str]]:
    existing = existing_priority_index(existing_priority_path)
    return [merge_curated(row, find_existing(existing, row) or {}) for row in raw_priority]


def verify_outputs(priority_path: Path, today_path: Path, json_path: Path) -> list[str]:
    errors = []
    priority = read_tsv(priority_path)
    today = read_tsv(today_path)
    unresolved = [row for row in priority if row.get("priority") in ("", "to_classify")]
    if unresolved:
        errors.append(f"{len(unresolved)} priority rows are unclassified")
    if not json_path.is_file():
        errors.append("JSON snapshot is missing")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh the hay source inventory without erasing curated dispositions")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--downloads", type=Path)
    parser.add_argument("--germanic", type=Path)
    parser.add_argument("--germanic2", type=Path)
    parser.add_argument("--today-date", default="2026-11-22")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--priority-output", type=Path)
    parser.add_argument("--today-output", type=Path)
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    downloads = (args.downloads or (repo.parent.parent / "Downloads")).resolve()
    germanic = (args.germanic or (downloads / "Germanic")).resolve()
    germanic2 = (args.germanic2 or (downloads / "Germanic 2")).resolve()
    out = repo / "docs/references"
    priority_output = args.priority_output or (out / "hay-germanic-downloads-comprehensive-2026-11-22.tsv")
    today_output = args.today_output or (out / "hay-todays-downloads-2026-11-22.tsv")
    json_output = args.json_output or (out / "hay-source-inventory-2026-11-22.json")
    index = canonical_index(repo)
    raw_priority, counts = collect_priority(germanic, germanic2, repo, index)
    priority = merge_inventory(raw_priority, priority_output)
    today = collect_today(downloads, dt.date.fromisoformat(args.today_date), repo, index)

    existing_today = {row["sha256"]: row for row in read_tsv(today_output) if row.get("sha256")}
    for row in today:
        if row["sha256"] in existing_today:
            for field in ("classification", "priority", "ingestion_status", "next_action"):
                if existing_today[row["sha256"]].get(field):
                    row[field] = existing_today[row["sha256"]][field]

    if not args.verify:
        write_tsv(priority_output, priority, PRIORITY_FIELDS)
        write_tsv(today_output, today, TODAY_FIELDS)
        json_output.write_text(
            json.dumps({"priority": priority, "today": today}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    errors = verify_outputs(priority_output if args.verify else priority_output, today_output, json_output)
    print(json.dumps({"counts": counts, "priority_count": len(priority), "today_count": len(today), "missing_directories": counts["missing"], "errors": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

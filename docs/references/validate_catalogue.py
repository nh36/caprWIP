#!/usr/bin/env python3
"""Validate reference-catalogue identities, project links, and local paths."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "docs/references/catalogue.tsv"
PROJECTS = ROOT / "docs/references/projects"


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def split_paths(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def split_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(";")] if value else []


def exists(path: str) -> bool:
    target = ROOT / path
    return target.is_file() or target.is_dir()


def is_ignored(path: str) -> bool:
    return subprocess.run(
        ["git", "check-ignore", "-q", path], cwd=ROOT, check=False
    ).returncode == 0


def is_tracked(path: str) -> bool:
    return subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", path],
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    catalogue = rows(CATALOGUE)
    if not catalogue:
        print("ERROR: catalogue is empty", file=sys.stderr)
        return 1

    required = {
        "source_id",
        "bib_key",
        "title",
        "author_or_editor",
        "year",
        "original_file_path",
        "searchable_text_path",
        "edition_or_version",
        "original_sha256",
        "availability_status",
        "rights_access_restrictions",
        "page_map_links",
        "availability_scope",
    }
    missing_columns = required - set(catalogue[0])
    if missing_columns:
        errors.append(f"catalogue lacks columns: {', '.join(sorted(missing_columns))}")

    source_ids: set[str] = set()
    bib_keys: set[str] = set()
    for row in catalogue:
        source_id = row["source_id"]
        if not source_id:
            errors.append("catalogue row has an empty source_id")
        elif source_id in source_ids:
            errors.append(f"duplicate source_id: {source_id}")
        source_ids.add(source_id)

        bib_key = row["bib_key"]
        if bib_key:
            if bib_key in bib_keys:
                errors.append(f"duplicate bib_key: {bib_key}")
            bib_keys.add(bib_key)
            if source_id != f"ref:{bib_key}":
                errors.append(f"{source_id} does not match bib_key {bib_key}")

        paths = []
        for column in (
            "original_file_path",
            "searchable_text_path",
            "metadata_manifest",
        ):
            paths.extend((column, path) for path in split_paths(row.get(column, "")))
        for page_map in split_paths(row.get("page_map_links", "")):
            paths.append(("page_map_links", page_map.split("#", 1)[0]))
        for column, path in paths:
            if not exists(path):
                warnings.append(f"{source_id}: {column} unavailable here: {path}")
            if "/docs/references/local/" in f"/{path}":
                if not is_ignored(path):
                    errors.append(f"private reference path is not Git-ignored: {path}")
                if is_tracked(path):
                    errors.append(f"private reference path is tracked by Git: {path}")

        for path_column, hash_column, label in (
            ("original_file_path", "original_sha256", "original"),
            ("searchable_text_path", "search_text_sha256", "search text"),
        ):
            file_paths = split_paths(row.get(path_column, ""))
            hashes = split_values(row.get(hash_column, ""))
            if hashes and len(hashes) != len(file_paths):
                errors.append(
                    f"{source_id}: {label} path/hash counts differ "
                    f"({len(file_paths)} paths, {len(hashes)} hashes)"
                )
                continue
            for index, file_path in enumerate(file_paths):
                target = ROOT / file_path
                if not target.is_file():
                    continue
                if index >= len(hashes) or not hashes[index]:
                    errors.append(f"{source_id}: missing {label} SHA-256 for {file_path}")
                    continue
                actual_hash = hashlib.sha256(target.read_bytes()).hexdigest()
                if len(hashes[index]) != 64 or hashes[index] != actual_hash:
                    errors.append(f"{source_id}: incorrect {label} SHA-256 for {file_path}")

    project_rows = 0
    for manifest in sorted(PROJECTS.glob("*.tsv")):
        for row in rows(manifest):
            project_rows += 1
            if row["source_id"] not in source_ids:
                errors.append(
                    f"{manifest.relative_to(ROOT)} references unknown "
                    f"source_id {row['source_id']}"
                )
            if not row.get("project_id"):
                errors.append(f"{manifest.relative_to(ROOT)} has an empty project_id")

    for row in catalogue:
        for related_id in split_paths(row.get("related_source_ids", "")):
            if related_id not in source_ids:
                errors.append(
                    f"{row['source_id']} references unknown related source {related_id}"
                )
        for value in row.values():
            if value and ("/Users/" in value or str(Path.home()) in value):
                errors.append(f"absolute machine path in catalogue: {row['source_id']}")

    print(
        f"Catalogue: {len(catalogue)} records, {len(bib_keys)} bibliography keys; "
        f"project manifests: {project_rows} rows."
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Catalogue identifiers, manifests, paths, and privacy boundaries passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

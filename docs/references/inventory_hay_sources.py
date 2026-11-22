#!/usr/bin/env python3
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path("/Users/nathanhill")
REPO = ROOT / "Code/capr"
OUT = REPO / "docs/references"
PRIORITY_ROOTS = [
    ROOT / "Downloads/Germanic",
    ROOT / "Downloads/Germanic 2",
]
TODAY_ROOT = ROOT / "Downloads"
DOCUMENT_SUFFIXES = {".pdf", ".djvu", ".epub", ".doc", ".docx"}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdfinfo(path):
    try:
        output = subprocess.run(
            ["pdfinfo", str(path)],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        ).stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "", "", ""
    fields = {}
    for line in output.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields.get("Title", ""), fields.get("Author", ""), fields.get("Pages", "")


def text_status(path):
    if path.suffix.lower() != ".pdf":
        return "n/a"
    try:
        output = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "3", "-layout", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        text = output.stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "unknown"
    if len(text.strip()) < 100:
        return "no_usable_text_in_sample"
    bad = sum(text.count(marker) for marker in ("\ufffd", "^"))
    if bad > 20:
        return "native_text_defective"
    return "native_text_present"


def canonical_matches(digest):
    matches = []
    for path in (OUT).rglob("*"):
        if path.is_file() and path.suffix.lower() == ".pdf":
            try:
                if sha256(path) == digest:
                    matches.append(str(path.relative_to(REPO)))
            except OSError:
                pass
    return matches


def collect_priority():
    rows = []
    seen = set()
    for root in PRIORITY_ROOTS:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in DOCUMENT_SUFFIXES:
                continue
            resolved = str(path.resolve())
            if resolved in seen:
                continue
            seen.add(resolved)
            digest = sha256(path)
            title, author, pages = pdfinfo(path) if path.suffix.lower() == ".pdf" else ("", "", "")
            matches = canonical_matches(digest)
            status = "exact_canonical_duplicate" if matches else "new_external_original_candidate"
            if str(path).startswith(str(REPO)):
                public_path = str(path.relative_to(REPO))
            elif str(path).startswith(str(ROOT / "Downloads")):
                public_path = str(path.relative_to(ROOT))
            else:
                public_path = path.name
            rows.append({
                "source_path": public_path,
                "original_filename": path.name,
                "sha256": digest,
                "size": path.stat().st_size,
                "type": path.suffix.lower().lstrip("."),
                "title": title,
                "author": author,
                "pages": pages,
                "text_status": text_status(path),
                "canonical_matches": "|".join(matches),
                "status": status,
                "scope": "Germanic" if str(path).startswith(str(PRIORITY_ROOTS[0])) else "Germanic2",
                "priority": "to_classify",
                "consulted": "no",
            })
    return rows


def collect_today():
    rows = []
    start = datetime.datetime(2026, 11, 22)
    end = start + datetime.timedelta(days=1)
    for path in sorted(TODAY_ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in DOCUMENT_SUFFIXES:
            continue
        try:
            modified = datetime.datetime.fromtimestamp(path.stat().st_mtime)
        except OSError:
            continue
        if not start <= modified < end:
            continue
        digest = sha256(path)
        title, author, pages = pdfinfo(path) if path.suffix.lower() == ".pdf" else ("", "", "")
        matches = canonical_matches(digest)
        if str(path).startswith(str(REPO)):
            public_path = str(path.relative_to(REPO))
        elif str(path).startswith(str(ROOT / "Downloads")):
            public_path = str(path.relative_to(ROOT))
        else:
            public_path = path.name
        rows.append({
            "source_path": public_path,
            "original_filename": path.name,
            "sha256": digest,
            "size": path.stat().st_size,
            "type": path.suffix.lower().lstrip("."),
            "title": title,
            "author": author,
            "pages": pages,
            "text_status": text_status(path),
            "canonical_matches": "|".join(matches),
            "status": "exact_canonical_duplicate" if matches else "new_external_original_candidate",
            "mtime": modified.isoformat(timespec="seconds"),
            "mtime_is_download_date": "unknown",
        })
    return rows


def write_tsv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write("\t".join(fields) + "\n")
        for row in rows:
            stream.write("\t".join(str(row.get(field, "")).replace("\t", " ").replace("\n", " ") for field in fields) + "\n")


if __name__ == "__main__":
    priority = collect_priority()
    today = collect_today()
    fields = ["source_path", "original_filename", "sha256", "size", "type", "title", "author", "pages", "text_status", "canonical_matches", "status", "scope", "priority", "consulted"]
    write_tsv(OUT / "hay-germanic-downloads-comprehensive-2026-11-22.tsv", priority, fields)
    today_fields = ["source_path", "original_filename", "sha256", "size", "type", "title", "author", "pages", "text_status", "canonical_matches", "status", "mtime", "mtime_is_download_date"]
    write_tsv(OUT / "hay-todays-downloads-2026-11-22.tsv", today, today_fields)
    (OUT / "hay-source-inventory-2026-11-22.json").write_text(
        json.dumps({"priority": priority, "today": today}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({"priority_count": len(priority), "today_count": len(today)}, indent=2))

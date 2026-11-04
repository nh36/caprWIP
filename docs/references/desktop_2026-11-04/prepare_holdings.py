#!/usr/bin/env python3
"""Preserve supplied originals and prepare local-only searchable source holdings."""
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile


ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
LOCAL = ROOT / "docs/references/local/desktop-2026-11-04"
SOURCES = (
    ("Seiler2019", "Seiler 2019 - The spelling of the Erfurt glossary.pdf",
     "seiler_2019_erfurt_glossary", 16),
    ("BremmerJohnstonVries1998", "Approaches_to_Old_Frisian_Philology.pdf",
     "approaches_old_frisian_philology_1998", 344),
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy_exact(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if sha(source) != sha(target):
            raise ValueError(f"Refusing to overwrite different bytes: {target}")
    else:
        shutil.copy2(source, target)
    assert sha(source) == sha(target)


def extract(pdf):
    result = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                            capture_output=True, check=True)
    if result.stderr:
        raise ValueError(result.stderr.decode())
    return result.stdout


def preserve():
    LOCAL.mkdir(parents=True, exist_ok=True)
    records = []
    for key, name, stem, extent in SOURCES:
        origin = Path.home() / "Desktop" / name
        target = ROOT / "docs/references" / (stem + ".pdf")
        copy_exact(origin, target)
        native = extract(target)
        assert native.count(b"\f") == extent
        (LOCAL / (key + ".native.txt")).write_bytes(native)
        info = subprocess.check_output(["pdfinfo", str(target)], text=True)
        records.append(dict(citation_key=key, origin="$HOME/Desktop/" + name,
                            path=str(target.relative_to(ROOT)), sha256=sha(target),
                            sheets=extent, pdfinfo=info,
                            native_text_characters=len(native.decode().replace("\f", "").strip())))
    (RECORD / "originals.json").write_text(json.dumps(records, indent=2) + "\n")


def ocr():
    original = ROOT / "docs/references/approaches_old_frisian_philology_1998.pdf"
    output = LOCAL / "approaches_1998.ocr.pdf"
    if output.exists():
        raise ValueError("Keep existing OCR attempt; do not overwrite it")
    environment = dict(os.environ, OMP_THREAD_LIMIT="1")
    subprocess.run([
        "ocrmypdf", "--jobs", "2", "--language", "eng+deu",
        "--output-type", "pdf", "--optimize", "0", "--deskew",
        "--rotate-pages", "--sidecar", str(LOCAL / "Approaches1998.ocr-sidecar.txt"),
        str(original), str(output)], check=True, env=environment)
    (LOCAL / "Approaches1998.ocr-native.txt").write_bytes(extract(output))


def table(path, rows):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t",
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(stream.getvalue())


def finalize(main):
    previous_path = RECORD / "preservation.json"
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else None
    if previous:
        copy_exact(previous_path, RECORD / "preflight-preservation.json")
    originals = json.loads((RECORD / "originals.json").read_text())
    prepared = [
        ("Seiler2019", SOURCES[0][2], "Seiler2019.native.txt", 1, 16, 525,
         "complete chapter, printed525-540", "supplied ABBYY text; uncorrected glyphs"),
        ("BremmerJohnstonVries1998", SOURCES[1][2], "Approaches1998.ocr-native.txt",
         1, 344, None,
         "all344 supplied sheets; duplicatexi/18, missing21, ends at printed329",
         "local OCRmyPDF/Tesseract eng+deu; uncorrected OCR"),
        ("Fulk1998", SOURCES[1][2], "Approaches1998.ocr-native.txt", 155, 170, 139,
         "complete chapter, printed139-154",
         "local OCRmyPDF/Tesseract eng+deu; uncorrected OCR"),
    ]
    holdings, maps = [], []
    for key, stem, native, first, last, printed_start, coverage, method in prepared:
        pages = (LOCAL / native).read_text().split("\f")
        if not pages[-1].strip():
            pages.pop()
        assert len(pages) == (16 if key == "Seiler2019" else 344)
        pdf = ROOT / "docs/references" / (stem + ".pdf")
        chunks = [f"Source: {key}\nPDF SHA256: {sha(pdf)}\n"
                  "Local-only searchable navigation; source images are authoritative.\n"
                  f"Coverage: {coverage}\nMethod: {method}\n"]
        for sheet in range(first, last + 1):
            if printed_start is not None:
                label = str(printed_start + sheet - first)
            elif sheet in (35, 36, 37):
                label = str(sheet - 17)
            elif sheet >= 318:
                label = str(sheet - 15)
            elif sheet >= 17:
                label = str(sheet - 16)
            else:
                label = "frontmatter"
            maps.append(dict(citation_key=key, pdf_sheet=sheet, printed_page=label,
                             basis="sequential complete article pagination" if key == "Seiler2019"
                             else ("selected boundaries and folio headers checked" if key == "Fulk1998"
                                   else "folio offsets; image-checked overrides35-37; blank302 omitted")))
            chunks.append(f"=== PDF sheet {sheet:03}; printed page {label} ===\n"
                          + pages[sheet - 1].rstrip() + "\n")
        text = LOCAL / (key + (".v2.txt" if key == "BremmerJohnstonVries1998" else ".txt"))
        text.write_text("\n\f\n".join(chunks))
        holdings.append(dict(
            citation_key=key, pdf_path=str(pdf.relative_to(ROOT)), pdf_sha256=sha(pdf),
            pdf_sheets=len(pages), first_sheet=first, last_sheet=last,
            text_path=str(text.relative_to(ROOT)), text_sha256=sha(text),
            access="local_only", extraction=method, coverage=coverage))
    table(RECORD / "holdings.tsv", holdings)
    table(RECORD / "page_map.tsv", maps)
    assets = [ROOT / record["path"] for record in originals]
    assets += [path for path in LOCAL.iterdir() if path.is_file()]
    for path in assets:
        copy_exact(path, main / path.relative_to(ROOT))
    bundle = main / "docs/references/local/backups/desktop-2026-11-04-checked.tar.gz"
    if bundle.exists():
        raise ValueError("Keep existing restoration bundle; do not overwrite it")
    with tarfile.open(bundle, "w:gz") as archive:
        for path in assets:
            archive.add(path, arcname=str(path.relative_to(ROOT)))
    with tarfile.open(bundle) as archive:
        for path in assets:
            member = archive.extractfile(str(path.relative_to(ROOT)))
            assert hashlib.sha256(member.read()).hexdigest() == sha(path)
    receipt = dict(
        originals=originals,
        derivatives=[dict(path=str(path.relative_to(ROOT)), sha256=sha(path),
                          bytes=path.stat().st_size) for path in assets if path.parent == LOCAL],
        restoration=dict(path=str(bundle.relative_to(main)), sha256=sha(bundle),
                         members=len(assets), role="same-disk restoration, not independent backup"),
        provisional_receipt="preflight-preservation.json" if previous else None,
        tools={name: subprocess.check_output(argv, text=True, stderr=subprocess.STDOUT).strip()
               for name, argv in (("ocrmypdf", ["ocrmypdf", "--version"]),
                                  ("tesseract", ["tesseract", "--version"]))})
    (RECORD / "preservation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"PASS: {len(assets)} exact local assets and restoration members; "
          "three searchable holdings with page maps")


def check(main):
    receipt = json.loads((RECORD / "preservation.json").read_text())
    for record in receipt["originals"] + receipt["derivatives"]:
        for root in (ROOT, main):
            path = root / record["path"]
            if not path.is_file() or path.is_symlink() or sha(path) != record["sha256"]:
                raise ValueError(f"Absent or changed project holding: {path}")
    rows = list(csv.DictReader((RECORD / "holdings.tsv").open(), delimiter="\t"))
    maps = list(csv.DictReader((RECORD / "page_map.tsv").open(), delimiter="\t"))
    for row in rows:
        assert sha(ROOT / row["pdf_path"]) == row["pdf_sha256"]
        assert sha(ROOT / row["text_path"]) == row["text_sha256"]
        count = int(row["last_sheet"]) - int(row["first_sheet"]) + 1
        selected = [r for r in maps if r["citation_key"] == row["citation_key"]]
        assert [int(r["pdf_sheet"]) for r in selected] == list(
            range(int(row["first_sheet"]), int(row["last_sheet"]) + 1))
        assert (ROOT / row["text_path"]).read_text().count("=== PDF sheet ") == count
    labels = {(r["citation_key"], int(r["pdf_sheet"])): r["printed_page"] for r in maps}
    for sheet, folio in {34: 18, 35: 18, 36: 19, 37: 20, 38: 22,
                         155: 139, 170: 154, 317: 301, 318: 303, 344: 329}.items():
        assert labels["BremmerJohnstonVries1998", sheet] == str(folio)
    for sheet in range(155, 171):
        assert labels["Fulk1998", sheet] == str(sheet - 16)
    for sheet in range(1, 17):
        assert labels["Seiler2019", sheet] == str(sheet + 524)
    for native, count in (("Seiler2019.native.txt", 16),
                          ("Approaches1998.ocr-native.txt", 344)):
        pages = (LOCAL / native).read_text().split("\f")
        assert len(pages) == count + 1 and not pages[-1].strip()
        assert all(page.strip() for page in pages[:-1])
    restoration = receipt["restoration"]
    bundle = main / restoration["path"]
    assert sha(bundle) == restoration["sha256"]
    with tarfile.open(bundle) as archive:
        for record in receipt["originals"] + receipt["derivatives"]:
            member = archive.extractfile(record["path"])
            assert hashlib.sha256(member.read()).hexdigest() == record["sha256"]
    print("PASS: original/derivative hashes, both project roots, full sheet coverage, "
          "chapter maps and checked restoration members; Desktop not required")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("preserve", "ocr", "finalize", "check"))
    parser.add_argument("--main", type=Path)
    args = parser.parse_args()
    if args.stage == "preserve":
        preserve()
    elif args.stage == "ocr":
        ocr()
    else:
        if args.main is None:
            parser.error(f"{args.stage} requires --main")
        if args.stage == "check":
            check(args.main.resolve())
        else:
            finalize(args.main.resolve())

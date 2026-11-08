#!/usr/bin/env python3
"""Prepare/check the private article extracts and their public acquisition metadata."""
import argparse
import csv
import hashlib
import io
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
LOCAL = ROOT / "docs/references/local/prosody-2026-11-08"
ARTICLES = (
    ("Goering2016", "goering_2016_early_old_english_foot_structure",
     "357f123fb2c680647b3786dc185e76a3892631eb6706cbeda4f2a9afe2607b94",
     27, 171, "new_original", "goering2016.pdf"),
    ("Russom2001", "russom_2001_subordinate_stress",
     "d939e461d0f921459a52061195f7ed9b94f2addd29e0ac6c1c59e30163e6d189",
     26, 39, "already_held_identical_original",
     "Russom 2001 Metrical evidence for subordinate stress in Old English.pdf"),
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def extract(path, count):
    result = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, check=True)
    if result.stderr:
        raise ValueError(result.stderr.decode())
    chunks = result.stdout.decode().split("\f")
    if chunks[-1].strip() or len(chunks) != count + 1:
        raise ValueError(f"Unexpected PDF sheet coverage: {path}")
    if any(not chunk.strip() for chunk in chunks[:-1]):
        raise ValueError(f"Empty extracted sheet: {path}")
    return result.stdout, chunks[:-1]


def table(records):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(records[0]),
                            delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(records)
    return stream.getvalue().encode()


def prepared():
    holdings, page_map = [], []
    for key, stem, pdf_sha, count, first, status, supplied_name in ARTICLES:
        pdf = ROOT / "docs/references" / (stem + ".pdf")
        if digest(pdf.read_bytes()) != pdf_sha:
            raise ValueError(f"Original checksum mismatch: {pdf}")
        native, native_pages = extract(pdf, count)
        yield LOCAL / (key + ".native.txt"), native
        if key == "Goering2016":
            ocr_pdf = LOCAL / (key + ".ocr.pdf")
            ocr, pages = extract(ocr_pdf, count)
            yield LOCAL / (key + ".ocr-layout.txt"), ocr
            method = "OCRmyPDF 17.1.0 force-ocr; Tesseract 5.5.2 eng; pdftotext 26.02.0 -layout"
            ocr_path, ocr_sha = str(ocr_pdf.relative_to(ROOT)), digest(ocr_pdf.read_bytes())
            caution = "native accent control codes; OCR quantity/phonetic/table errors; PDF authoritative"
        else:
            if native.decode().count("\uf6d9") != 1 or native.decode().count("\uf8e7") != 24:
                raise ValueError("Unexpected Russom native glyph mapping")
            pages = [page.replace("\uf6d9", "\u00a9").replace("\uf8e7", "\u2014")
                     for page in native_pages]
            method = "pdftotext 26.02.0 -layout; verified copyright/author-repeat glyph substitutions"
            ocr_path, ocr_sha = "", ""
            caution = "line wraps and visual metrical alignment require PDF; raw native retained"
        intro = (
            f"Source: {key}\nOriginal PDF SHA256: {pdf_sha}\n"
            f"Method: {method}\n"
            f"Local-only complete search aid, not a diplomatic transcription. {caution}.\n\n"
        )
        chunks = []
        for sheet, (native_page, page) in enumerate(zip(native_pages, pages, strict=True), 1):
            printed = first + sheet - 1
            if str(printed) not in native_page:
                raise ValueError(f"Missing printed folio anchor: {key} sheet {sheet}")
            chunks.append(
                f"=== PDF sheet {sheet:03}; printed page {printed} ===\n{page.rstrip()}\n\f")
            controls = sorted({
                f"U+{ord(c):04X}" for c in native_page
                if (ord(c) < 32 and c not in "\n\r\t") or 0xE000 <= ord(c) <= 0xF8FF
            })
            page_map.append(dict(
                citation_key=key, pdf_sheet=sheet, printed_page=printed,
                mapping_basis="continuous publisher pagination; every sheet rendered and inspected",
                native_characters=len(native_page), search_characters=len(page),
                native_glyph_warnings=",".join(controls),
                inspection="page image, running folio, body/examples, notes and reference boundaries"))
        text = (intro + "\n".join(chunks)).encode()
        text_path = LOCAL / (key + ".txt")
        yield text_path, text
        holdings.append(dict(
            citation_key=key, pdf_path=str(pdf.relative_to(ROOT)), pdf_sha256=pdf_sha,
            pdf_sheets=count, first_sheet=1, last_sheet=count,
            printed_first=first, printed_last=first + count - 1,
            original_status=status, supplied_filename=supplied_name,
            text_path=str(text_path.relative_to(ROOT)), text_sha256=digest(text),
            native_text_path=str((LOCAL / (key + ".native.txt")).relative_to(ROOT)),
            native_text_sha256=digest(native),
            ocr_pdf_path=ocr_path, ocr_pdf_sha256=ocr_sha,
            access="local_only_copyright_restricted",
            extraction=method,
            coverage=f"complete article; all {count} sheets including notes/examples/references",
            limitations=caution))
    yield RECORD / "holdings.tsv", table(holdings)
    yield RECORD / "page_map.tsv", table(page_map)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, data in prepared():
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                raise ValueError(f"Absent or stale extraction/record: {path}")
        elif path.exists() and path.read_bytes() != data:
            raise ValueError(f"Refusing to overwrite an existing version: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print("PASS: two originals, complete 27/26-sheet search aids, hashes and 53 printed-page mappings")


if __name__ == "__main__":
    main()

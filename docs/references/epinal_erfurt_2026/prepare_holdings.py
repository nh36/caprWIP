#!/usr/bin/env python3
"""Create and verify private text aids for the revised Epinal-Erfurt PDFs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
LOCAL = ROOT / "docs/references/local/herren-erfurt-2026"
LANGUAGES = "eng+deu+lat+grc"
JOBS = "2"
SOURCES = (
    ("A", "herren_et_al_epinal_erfurt_revised_a.pdf",
     "583e3ad01f10373da249d74456f62bda4ae13911330ca355feea99ced1a811f3", 60),
    ("B", "herren_et_al_epinal_erfurt_revised_b.pdf",
     "be821d1c564f4ca356d696e8b8c66169525859cc60ff48593a2c5ac75f0765df", 17),
    ("C", "herren_et_al_epinal_erfurt_revised_c.pdf",
     "dc098032cb80d07806b4cf64d20fef019a51602c259d4d864c6487554b17952f", 47),
    ("P", "herren_et_al_epinal_erfurt_revised_p.pdf",
     "d12fc1178a2661ea2d8824b0e24b160f7667bf793b923e2d4e0e56a8277e6faf", 53),
    ("Introduction", "herren_et_al_epinal_erfurt_revised_introduction.pdf",
     "2c1baf45d25faac33e98de3eb4ecf97b131a574c90313729c70c8614efd0bdf4", 1),
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def text_version(command: list[str]) -> str:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return (result.stdout or result.stderr).splitlines()[0].strip()


def extract(path: Path, expected_pages: int) -> tuple[bytes, list[str]]:
    result = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        capture_output=True,
        check=True,
    )
    text = result.stdout.decode("utf-8", "replace")
    pages = text.split("\f")
    if pages[-1].strip() or len(pages) != expected_pages + 1:
        raise ValueError(f"Unexpected PDF page coverage: {path}")
    body = pages[:-1]
    if any(not page.strip() for page in body):
        raise ValueError(f"Empty extracted page: {path}")
    return result.stdout, body


def table(records: list[dict[str, str]]) -> bytes:
    stream = io.StringIO()
    writer = csv.DictWriter(
        stream,
        fieldnames=list(records[0]),
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(records)
    return stream.getvalue().encode()


def marked_text_for_record(
    part: str, filename: str, sha: str, kind: str,
    page_texts: list[str], method: str,
) -> bytes:
    chunks = [
        f"=== PDF sheet {number:03} ===\n{page.rstrip()}\n\f"
        for number, page in enumerate(page_texts, 1)
    ]
    header = (
        f"Source: HerrenEtAl2026 part {part}\n"
        f"Original PDF: docs/references/{filename}\n"
        f"Original PDF SHA256: {sha}\n"
        f"Extraction: {kind}; {method}\n"
        "Local-only search aid, not a diplomatic transcription. "
        "Consult the original PDF for exact forms, diacritics, tables, "
        "and layout.\n\n"
    )
    return (header + "\n".join(chunks)).encode()


def outputs(check_only: bool) -> list[tuple[Path, bytes]]:
    holdings: list[dict[str, str]] = []
    page_map: list[dict[str, str]] = []
    result: list[tuple[Path, bytes]] = []
    ocrmypdf_version = text_version(["ocrmypdf", "--version"])
    tesseract_version = text_version(["tesseract", "--version"])
    pdftotext_version = text_version(["pdftotext", "-v"])
    method = (
        f"OCRmyPDF {ocrmypdf_version} --force-ocr; "
        f"{tesseract_version} {LANGUAGES}; "
        f"{pdftotext_version} -layout"
    )

    for part, filename, expected_sha, page_count in SOURCES:
        original = ROOT / "docs/references" / filename
        if digest(original.read_bytes()) != expected_sha:
            raise ValueError(f"Original checksum mismatch: {original}")
        _, native_pages = extract(original, page_count)
        slug = part.lower()
        ocr_pdf = LOCAL / f"part-{slug}.ocr.pdf"
        if not ocr_pdf.is_file():
            if check_only:
                raise ValueError(f"Missing OCR PDF: {ocr_pdf}")
            subprocess.run(
                [
                    "ocrmypdf",
                    "--force-ocr",
                    "--jobs", JOBS,
                    "--language", LANGUAGES,
                    "--output-type", "pdf",
                    "--optimize", "0",
                    str(original),
                    str(ocr_pdf),
                ],
                check=True,
            )
        ocr_bytes, ocr_pages = extract(ocr_pdf, page_count)
        native_path = LOCAL / f"part-{slug}.native.txt"
        ocr_text_path = LOCAL / f"part-{slug}.ocr.txt"
        native_data = marked_text_for_record(
            part, filename, expected_sha,
            "native PDF text layer", native_pages, method,
        )
        ocr_data = marked_text_for_record(
            part, filename, expected_sha,
            "Tesseract OCR text layer", ocr_pages, method,
        )
        result.extend(((native_path, native_data), (ocr_text_path, ocr_data)))

        for sheet, (native_page, ocr_page) in enumerate(
            zip(native_pages, ocr_pages, strict=True), 1
        ):
            page_map.append(
                {
                    "part": part,
                    "pdf_sheet": str(sheet),
                    "native_characters": str(len(native_page)),
                    "tesseract_characters": str(len(ocr_page)),
                    "native_sha256": digest(native_page.encode()),
                    "tesseract_sha256": digest(ocr_page.encode()),
                    "printed_folio": "not independently mapped",
                    "note": "PDF image is authoritative",
                }
            )

        holdings.append(
            {
                "part": part,
                "original_path": str(original.relative_to(ROOT)),
                "original_sha256": expected_sha,
                "pdf_pages": str(page_count),
                "native_text_path": str(native_path.relative_to(ROOT)),
                "native_text_sha256": digest(native_data),
                "ocr_pdf_path": str(ocr_pdf.relative_to(ROOT)),
                "ocr_pdf_sha256": digest(ocr_bytes),
                "ocr_text_path": str(ocr_text_path.relative_to(ROOT)),
                "ocr_text_sha256": digest(ocr_data),
                "method": method,
                "coverage": f"complete; all {page_count} PDF sheets",
                "access": "private local holding; no redistribution permission",
            }
        )

    result.extend(
        (
            (RECORD / "holdings.tsv", table(holdings)),
            (RECORD / "page_map.tsv", table(page_map)),
        )
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        LOCAL.mkdir(parents=True, exist_ok=True)
    for path, data in outputs(check_only=args.check):
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                raise ValueError(f"Absent or stale extraction/record: {path}")
        elif path.exists() and path.read_bytes() != data:
            raise ValueError(f"Refusing to overwrite an existing version: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print("PASS: five originals, all 178 sheets, native/OCR texts and checksums")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

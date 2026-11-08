# Goering2016 and Russom2001: reference acquisition, 8 November 2026

This is library acquisition and technical verification, not a historical
adjudication. No FST, lexical selection or book text is changed.

## Identity and existing holdings

| Key | Original under `docs/references/` | Extent | Disposition |
|---|---|---|---|
| `Goering2016` | `goering_2016_early_old_english_foot_structure.pdf` | 27 PDF sheets, printed171--197 | Newly incorporated, byte-preserved from supplied `goering2016.pdf`; no exact original already in this reference library |
| `Russom2001` | `russom_2001_subordinate_stress.pdf` | 26 PDF sheets, printed39--64 | Already held; supplied download is byte-identical, so no replacement or second original |

Goering is Nelson Goering, “Early Old English Foot Structure,” *Transactions
of the Philological Society* 114(2), 2016, pp.171--197,
DOI10.1111/1467-968X.12079. The publisher title page and Crossref metadata
agree on author, article, journal, volume, issue, year and pages.
The already-held `Goering2023` chapter is a distinct publication; its
bibliographic entry, original and extraction are unchanged.

Russom is Geoffrey Russom, “Metrical Evidence for Subordinate Stress in Old
English,” *Journal of Germanic Linguistics* 13(1), 2001, pp.39--64,
DOI10.1017/S147054270100318X. Title-page metadata and every publisher DOI
footer verify the existing `Russom2001` entry, retained without duplication.
The direct Crossref lookup returned404 and its title search did not resolve
this article; no alternate DOI was inferred or substituted.

No complete article text was previously located in the established reference
library for either key. Both complete search aids are new. This does not
claim that no temporary excerpts exist elsewhere.

## Coverage and text quality

All53 PDF sheets were rendered and inspected. Both originals contain the
complete articles, footnotes, examples and closing references, with no
missing folios, added cover sheet or clipped page found. Goering's notes run
through37 and references finish on197; Russom's notes run through34 and
references finish on64. This verifies access and supplied coverage, not
scholarly acceptance of the arguments.

Printed pagination is not PDF sheet numbering:

- Goering: printed page = PDF sheet +170.
- Russom: printed page = PDF sheet +38.

`page_map.tsv` records every sheet, its printed folio, extraction character
counts and native glyph warnings. Complete marked search files are
`docs/references/local/prosody-2026-11-08/Goering2016.txt` and `Russom2001.txt`.
Every page, including notes and references, is present and nonempty.

Goering's native layer is not safe for quantity/diacritic transcription:
Poppler emits328 U+0001,110 U+0003,4 U+0004 and2 U+0005 controls, while
pypdf exposes unresolved font glyph names. The unmodified complete native
extract is retained separately. A separate OCR-derived PDF was produced
locally using the established OCRmyPDF17.1.0/Tesseract5.5.2 workflow,
`--force-ocr --jobs 2 --language eng --output-type pdf`. Its layout extraction
supplies the marked search aid. The original PDF was never overwritten.

OCR still loses or confuses macrons, breves, accents, phonetic letters,
asterisks, arrows and table/metrical alignment. Detailed original-image
checks included the paradigm on178 and the four-column comparison and
notes on187, alongside all-sheet inspection. Neither OCR nor the defective
native layer is a diplomatic transcription. The original PDF is readable;
quantity-bearing forms and metrical notation must be verified there during
the subsequent research. No unreadable original passage or omitted page
was identified.

Russom's native prose, examples and footnotes are usable without OCR.
After visual verification, the search aid substitutes © for the single
U+F6D9 copyright glyph and em dashes for24 U+F8E7 author-repeat strokes in
the references on63--64. The untouched native extraction is retained.
Line wrapping and spatial metrical alignment still require the original.

## Preservation, permissions and normal access

`holdings.tsv` registers original, marked-text, raw-native and separate
Goering OCR-PDF paths/hashes, method, extent, rights and limitations.
It follows the existing intake-manifest schema and is automatically
discovered by `holdings_audit_2026-11-04/audit.py`; the dated older inventory
remains a historical observation rather than being hand-edited.

Original PDFs are ignored by `docs/references/*.pdf`; complete native/OCR
texts, OCR PDF and inspection images are ignored under
`docs/references/local/`. No redistribution permission was verified.
Only bibliography, metadata, this acquisition record and its preparation
script are public. No restricted text was sent to an external OCR service.
Crossref requests contained only public bibliographic identifiers.

Access and checks use project-local files, never Downloads:

```sh
python3 docs/references/prosody_2026-11-08/prepare_holdings.py --check
rg -n '=== PDF sheet|foot|stress' docs/references/local/prosody-2026-11-08/Goering2016.txt
pdftotext -f 8 -l 8 -layout docs/references/goering_2016_early_old_english_foot_structure.pdf -
```

The final command addresses printed178, not printed8. For exact glyphs,
open the original PDF at sheet8. `README_resources.md` is the normal library
entry point. Same-machine holdings are not claimed as off-machine backup.

# Source intake: Old English verse, glosses and DOE, 23 November 2026

## Holdings, scope and reproducibility

All eight user-supplied originals were identified by content in `~/Downloads`,
copied rather than moved, and matched to the copies by SHA-256. The six
publications are **general CAPR library holdings**, not article attachments.
Their full bibliographic records are in `article_refs.bib`, and the general
library registers original and text paths, PDF and text SHA-256 hashes, page
counts, pagination, methods and caveats in
`docs/references/scholarly_2026-11-23/holdings.tsv`. The shared
`docs/refs.bib` was not changed: it is a publication and survey-provenance
input, and this intake does not authorize changing the book or scientific
projections. DOI metadata were checked against DOI records and publisher
catalogues; Toswell's thesis has no DOI identified.

All six originals and whole-publication text files are under the ignored
`docs/references/local/scholarly-2026-11-23/`. `pdftotext -layout` was applied
to **every sheet**, including front matter, references and appendices;
form feeds delimit PDF pages, starting with sheet 1. Sparse-sheet contact
sheets were visually checked: blank leaves, covers, section dividers, and
the Tamoto plate are not missing article chapters. Figure contents cannot be
searched as prose. The extracts are navigation aids, not diplomatic
transcriptions; images are decisive for signs, accents, tables and exact
wording. These local copies are not an independent backup.

For the mixed born-digital Tamoto and Minkova files, pages containing
private-use glyphs or non-whitespace controls were selectively rasterized at
180 dpi and OCRed with Tesseract English, two workers; the native extraction
was retained for all pages. The additional page-numbered files are
`tamoto2013.glyph-ocr.txt` (99 pages, SHA-256
`b70d3e1628990c2b2c354a09dd37914a86f2c427f0a973699db7bf7afa7d7afb`)
and `minkova2003.glyph-ocr.txt` (93 pages, SHA-256
`f2e96c5b5382822b63cf9a48ca2576172a13147458928f2033e6418d155849b3`).
These supplement rather than replace complete native extracts. Checking
Tamoto PDF 160 shows the OCR corrupts `hóeg`, despite the legible printed
original; it does not resolve the accent or special-character defects.
Kuhn's independently OCRed complete text has SHA-256
`47005030e21d0b2d9e6488767b08c72cb27b79f25e08466aecfc754d69907e98`;
its examples likewise need image verification.

| Publication and general use | Private PDF / complete text (basename under the directory above) | PDF sheets; printed mapping | Extraction and image checks |
|---|---|---|---|
| R. D. Fulk, *A History of Old English Meter* (University of Pennsylvania Press, 1992), DOI `10.9783/9781512802221`. Verse, prosody, syncope, contraction and chronology. | `fulk1992.pdf` / `fulk1992.txt` | 492; body printed p. = PDF p. − 24; printed 1–466 | Existing OCR text layer, extracted in full. PDF 434/printed 410 checked against image. OCR errors and historical characters remain. |
| Kenichi Tamoto, ed., *The Macregol Gospels or The Rushworth Gospels: Edition of the Latin Text with the Old English Interlinear Gloss Transcribed from Oxford Bodleian Library, MS Auctarium D. 2. 19* (John Benjamins, 2013), DOI `10.1075/z.180`. Interlinear glosses, palaeography and textual transmission. | `tamoto2013.pdf` / `tamoto2013.txt` | 480; edition p. = PDF p. − 141; introduction xcix–c at PDF 100–101 | Born-digital extraction. PDF 160/printed 19 and PDF 188/printed 47 checked visually. Private-use glyphs, including abbreviations, and control characters impair searching; check the image. Selective OCR is a secondary aid, not a diplomatic transcription. |
| Julia Fernández Cuesta and Sara M. Pons-Sanz, eds., *The Old English Gloss to the Lindisfarne Gospels: Language, Author and Context* (De Gruyter, Anglia Book Series 51, 2016), DOI `10.1515/9783110449105`. Glossing practice, morphology, textual and manuscript history. | `fernandez-cuesta-pons-sanz2016.pdf` / `fernandez-cuesta-pons-sanz2016.txt` | 445; body p. = PDF p. − 13; printed 1–432 | Native layer; PDF 390/printed 377 visually checked. A few private-use glyphs and special signs require images. |
| M. Jane Toswell, *Studies in the Paris Psalter, Metrical Version* (D.Phil. thesis, University of Oxford, 1990). Psalter manuscript, translation, gloss traditions and verse. | `toswell1990.pdf` / `toswell1990.txt` | 439; body p. = PDF p. − 10; printed 1–429 | Supplied OCRed scan; full extraction. PDF 260/printed 250 visually checked. OCR, character and layout errors persist. This is a thesis, not a commercially published book. |
| Donka Minkova, *Alliteration and Sound Change in Early English* (Cambridge University Press, Cambridge Studies in Linguistics 101, 2003), DOI `10.1017/CBO9780511486968`. Verse as evidence, Old and Middle English alliteration, onsets and phonology. | `minkova2003.pdf` / `minkova2003.txt` | 422; body p. = PDF p. − 22; printed 1–400 | Native layer; PDF 160/printed 138 visually checked. Some controls and private-use characters corrupt search results; selective OCR is a secondary aid. Inspect image for phonetic notation. |
| Sherman M. Kuhn, “E and Æ in Farman's Mercian Glosses,” *PMLA* 60.3 (1945), 631–669, DOI `10.2307/459169`. Rushworth dialect spelling and historical vowel development. | `kuhn1945.pdf` / `kuhn1945.txt`; additional full `kuhn1945.ocr.txt` and `kuhn1945.ocr.pdf` | 40; printed p. = PDF p. + 629 for sheets 2–40; sheet 1 cover | PDF 3/printed 632 visually checked. Native glyph mapping is defective. Full forced Tesseract English OCR provides an independent search aid but also misreads æ, macrons and examples; neither is authoritative. |

Two private source exports are separately preserved in
`docs/references/local/hay-article/`:

| Original handoff | SHA-256 | Scope |
|---|---|---|
| `CAPR_hay_DOE_corpus_handoff_2026-11-23.md` | `816d55f0b2e408fcb3543f8701792d5f8a1a7d2d06ef8899e0ddec9d80cd6174` | Seven exact-form searches; full supplied `heg`, `hig`, `hyg` blocks, selected `hege` and `heges` excerpts plus group indices, complete displayed `hieg` and `heig` passages. |
| `CAPR_hay_DOE_supplement_2026-11-23.md` | `ce548873d99d576fbac045461dce6dc40da0fe11dd2b2705bf38221057469657` | Nine further searches, including full supplied `hige` block and two `hoeg` passages. |

These are complete copies of the *supplied handoffs*, not necessarily complete
raw DOE exports. In particular `hig` reports 2,373 citations but the supplied
file contains only 678 excerpt lines. Interface settings and folding cannot be
reconstructed. The `heg` report says 57 citations; 56 citation lines are
visible in the supplied block. The crosswalk indexes the visible `heg` lines
and the 27 mechanically flagged `hig` lines, with preliminary context-based
lexical screening and explicit pronoun, boundary and mixed-use controls.
These are not separately verified manuscript attestations; its search ledger
links back to the remaining private material.
Neither export nor any full publication belongs in Git.

## Consulted passages and limits

- **Tamoto**, pp. xcix–c/PDF 100–101: discusses Farman's accented glosses and
  reports Waring's contrast with the other hand; the cited Mark examples and
  lack of examples in Farman's John portion complicate generalizations.
  At Mt 6:30 p. 19/PDF 160, and Mt 14:19 p. 47/PDF 188, the *printed
  edition images* show `hóeg`; DOE has `hoeg`. No manuscript facsimile was
  checked and neither editorial accent nor vowel length is settled.
- **Fulk**, Appendix A pp. 410–414/PDF 434–438: metrical faults make secure
  classification and precise counts problematic. He argues an Anglian,
  probably Mercian, original was subsequently Saxonized. This is his textual
  hypothesis, not a settled dialect assignment for the present tokens.
- **McColl Millar**, pp. 153–168/PDF 166–181: noun-phrase morphology and
  changes in inflection; authorial claims, not a classification of `hege`.
  **Pons-Sanz**, pp. 301–328/PDF 314–341: multiple glosses, especially in
  Mark; ordering is not entirely consistent. **Lendinara**, p. 348/PDF 361:
  Mt 6:30 and Aldred's `heofone` for Latin *clibanum*, with the `gers ł heg`
  double gloss in context. **Kotake**, pp. 377–396/PDF 390–409, especially
  p. 394/PDF 407: questions a simple direct-copy account of Owun's source
  and proposes a more complex relationship; the conclusion is tentative and
  does not deny all textual connections.
- **Toswell**, ch. 1 p. 21/PDF 31 onward: Paris manuscript and text history;
  ch. 5 p. 260/PDF 270 onward: relations to glossed Psalters; ch. 6
  p. 299/PDF 309 onward: poetic and metrical traits, including differences
  from classical verse. Her appendix begins metrical analysis of Psalms
  118–122 at p. 419/PDF 429; that appendix is not a scan of the present verses.
- **Minkova**, §2.6 p. 68/PDF 90: explicitly warns of circularity between
  reconstructed phonology and verse analysis, and argues for independent
  controls. Ch. 3 pp. 71–134/PDF 93–156 and ch. 4 pp. 135–191/PDF 157–213
  examine alliteration, velars and syllable onsets. It is not a comprehensive
  study of vowel quantity.
- **Kuhn**, pp. 631–632/PDF 2–3 frames Farman's inconsistent `e` and `æ`;
  p. 634/PDF 5 discusses an acute and short vowels **in Lindisfarne**. Do not
  transfer that observation uncritically to Farman or use it as an established
  calibration of the Rushworth accents.

The [crosswalk](DOE_CROSSWALK_2026-11-23.tsv) identifies attested spellings,
edition witnesses, tentative morphology and existing concordance links. The
[cycle 3 handoff](CYCLE3_RESEARCH_HANDOFF.md) sets the remaining work. Ritt
2000 and Dal 1934 are still awaiting ILL: reports by others are not firsthand
consultation of either original.

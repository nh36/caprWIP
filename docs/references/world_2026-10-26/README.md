# World/prosody source intake, 26 October 2026

Acquisition metadata, not scientific adoption. Initial research revision:
`6b2baf5f88af8a3c7702628bb3376c53c466e2a6`, branch `update`.
`docs/refs.bib` owns bibliography; the two normal reference indexes link here.
The complete Downloads inventory is local-only:
`docs/references/local/world-2026-10-26/downloads-inventory.json`.
It records original absolute locations, creation/modification timestamps,
sizes, checksums, duplicate checks and dispositions for all 14 files found
on the initial recursive scan with creation or modification date26 October.
Unrelated project and private office material remains in place, not publicly
catalogued or ingested into CAPR; OS metadata is not a scholarly source.
Files downloaded after the scan are not silently certified by this receipt.

## Complete holdings

| Key | Supplied filename | Canonical local PDF stem | Extent and page map |
| --- | --- | --- | --- |
| Fulk2010 | `fulk2010.pdf` | `fulk_2010_high_vowel_deletion` | all19 sheets; printed126--144 |
| Fulk2022 | `10.1515_9781802700251-007.pdf` | `fulk_2022_metre_editorial_concern` | all8 sheets; printed11--18 |
| Goering2023 | `417751951.pdf` | `goering_2023_heafudu_problem` | all28 reflow sheets, including endnotes; original print52--86 anchors |
| Britton1996 | supplied complete *English Historical Linguistics 1994* volume | `britton_1996_english_historical_linguistics` | all412 sheets; frontmatter separated from numbered body |
| Hogg1996 | within Britton1996 | same volume, not a duplicate acquisition | sheets12--21; printed3--12 |
| Minkova1996 | within Britton1996 | same volume, not a duplicate acquisition | sheets22--47; printed13--38 |
| Cermak2005 | `Notes on Obscured Compounds in Old English_Čermák.pdf` | `cermak_2005_obscured_compounds` | all12 sheets; sheet1 blank, sheets2--12 printed35--45 |
| Sauer1992 | supplied complete *Nominalkomposita im Frühmittelenglischen* | `sauer_1992_nominalkomposita` | all768 sheets; unnumbered sheets1--4, Roman V--XXVIII on5--28, body page = sheet minus28 |

Original filenames, including the long Britton filename, are preserved in
the private inventory. The supplied `fulk2010.pdf` is the complete19-page
article requested as `fulk2010(1).pdf`; the exact latter name was not found
in today's Downloads scan. Neither the original nor existing holdings were
overwritten. All four hashes are new against the pre-intake root PDF library.
`holdings.tsv` records exact SHA256, PDF extent, article selection, complete
text path and hash. The initial intake registered six bibliographic identities, not six
independent PDFs. The bounded follow-up below adds two identities and
two PDFs. Minkova's supplied printed title has singular
“Reconstruction”; the bibliography follows that title.

The full existing Fulk2018 PDF is438 sheets, SHA256
`d54ef92bda6db690f69f7dc4631bfdec10e4b4681c7adb73f4ccc0232b73ddcf`.
Its full `fulk_comparative_grammar_early_germanic.vision.txt` remains the
searchable holding, not a collection of selected snippets. Existing
Downloads copies with that hash are duplicates, not new evidence.

## Preparation and verification

From the repository root, after provision of the six named local PDFs:

```sh
python3 docs/references/world_2026-10-26/prepare_holdings.py
python3 docs/references/world_2026-10-26/prepare_holdings.py --check
```

This uses the established local `pdftotext -layout` method and explicit
sheet/page markers, preserving every supplied sheet. Full native extractions,
including the entire Britton volume, are retained under the existing
Git-ignored local-holding directory. Article-level Hogg and Minkova extracts
are independently searchable and do not require rereading or re-extracting
the volume. The checker re-extracts and verifies complete text hashes,
sheet counts and exact page-map rows. No external OCR service is used.

The Goering PDF is a publisher export of reflowed content: individual sheets
span portions of multiple original pages. Its in-text `p.` anchors, not
a global offset or PDF sheet numbers, determine print-page navigation;
endnotes follow the main text. Tables and foot diagrams require image
inspection. It is not represented as an original printed-page facsimile.
The supplied source carries a CC BY4.0 notice, but this intake conservatively
keeps the supplied complete PDF/text local in accordance with project policy.

Fulk2010's embedded text frequently displaces quantity/stress signs and
contains control characters. It is usable for navigation, not diplomatic
quotation of accented forms. Fulk2022's text is substantially cleaner.
The Britton scan's text layer has ordinary OCR errors in thorn, eth, vowel
quantity and phonetic symbols; page images remain authoritative.
No claim of fully corrected diplomatic transcripts follows from extraction.
An additional complete19-sheet local Tesseract extraction of Fulk2010
(`Fulk2010.tesseract.txt`, with source/output hashes and engine provenance
in `Fulk2010.tesseract.json`) supplies navigation where the embedded text
is damaged. It is uncorrected OCR, not a replacement scholarly text.
Image-check and critical-reading results are separate from these technical
holding checks and are recorded with the world research evidence.

All five requested articles/chapters have now been read in full, including
notes and references where supplied. The full Britton volume is ingested,
not claimed critically read beyond Hogg and Minkova. Original images checked
include Hogg pp.3,12, Minkova pp.13,38 and Fulk2010 p.142. Minkova's
references end on p.37; p.38 is blank. Goering export sheets21--22
were visually checked, including the Cahuilla foot diagrams, print80--82
anchors, actual versus explicitly hypothetical verse examples, and the
argument against medial secondary stress in early Old English *weruld*.
This is visual verification of the supplied reflow, not original-print
facsimile certification. Other detailed source checks belong to the
world adjudication's claim ledger, not to a blanket OCR-quality assertion.

Fulk2022 is retained in full for the later separately authorized soul review.
Its pp.15--17 argue against the handbook syncope-first account and propose
retention plus later analogy. This is an accurately attributed source lead,
not an adjudication or an alteration of the closed SC036 account.

## Bounded follow-up: Čermák and Sauer

The follow-up starts at research baseline
`61a0d67ef02a8da681ab21fba741b0ad63ea0a95`. Only the two newly supplied
Downloads holdings were added; the original 14-file scan was not repeated
or retrospectively extended. Originals remain untouched; the PDF copies
are byte-identical, with hashes in `holdings.tsv`. Exact supplied filenames
and local locations are retained in the private follow-up acquisition
record, `docs/references/local/world-2026-10-26/follow-up-acquisition.json`.
The Čermák filename uses decomposed diacritics; this is a filename detail,
not a difference in the scholarly identity. Sauer's printed title and
copyright identify the 1992 Niemeyer edition, Buchreihe der Anglia30,
print ISBN3-484-42130-4; the electronic filename's ISBN is not substituted.

Čermák2005 has been read completely, printed35--45, including the table,
references and endnotes. Original-page images36 and39 were checked.
Table1's *world* versus *woruld, worold* is category B (medial-vowel loss),
not category A (second-member weakening). The suffix *-eld* suggestion
retains its question mark. The methodology on35--36 uses Bosworth--Toller
and checks variant spellings against the DOE Corpus; the *world* row gives
no word-specific primary-text locator or newly collated manuscript reading.
Its typology is not independent evidence for prehistoric low-vowel raising.

Sauer1992 has been read selectively: §2.3,68--73; §2.4.2.8,85--86;
the inflectional/compound discussion87--92, especially *wor(u)ld* on90;
§§4.5--4.5.6,345--356, with the continuation357--358 distinguishing
later developments. This does not claim reading the whole monograph.
Original-page images68,90,354 and356 were checked. Page90 confirms
OE feminine *woruld*, genitive *worulde*, and later ME genitive-*s*
variation, with *Poema Morale* manuscript variants. These are later
morphological data, not evidence dating an early ō-stem shift or SC036.
The stress discussion distinguishes lexical from verse prominence;
the obscuration survey distinguishes multiple processes rather than
establishing a single compound sound law. Printed p.352's
*worleriche/worlepinge* concerns loss at a later compound junction,
not prehistoric raising of the medial vowel of *world* itself.

Both complete native extractions are searchable locally. Their diacritics,
accent diagrams and tabular alignment are not certified diplomatic text.
Sauer's embedded fonts produce repeated `Invalid Font Weight` diagnostics;
the preparation command reports their distinct messages and count while
checking all sheets and hashes. Images, not malformed text-layer symbols,
control critical readings. Registration and reading do not prejudge the
new historical/model comparison.

## Rights and availability

All newly supplied PDFs are byte-identical local copies under the existing
ignored `docs/references/*.pdf` convention; complete extracted texts and
the Downloads provenance inventory are also ignored. Public files contain
metadata, hashes, mapping and original scientific synthesis only.
No copyrighted complete transcript, scan or page image is committed,
uploaded to a third-party OCR system or made available by a public clone.

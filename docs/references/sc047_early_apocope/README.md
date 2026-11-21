# SC047 follow-up: private original-source intake

Bibliographic identity belongs to `docs/refs.bib`. This record registers
acquisition, not completion of the SC047 research or adoption of a sound law.
The historical adjudications retain their original consultation limits:
newly acquiring an original does not retroactively certify an earlier citation.
For the later [Dahl, Hogg and Adamczyk intake and reading record](nominal-levelling.md),
see the separate nominal-levelling bibliography.

| Key | Original and supplied coverage | Search aid |
| :--- | :--- | :--- |
| `HoggFulk2011` | *A Grammar of Old English*, Volume 2: *Morphology*, 2011; 406 PDF sheets, including title/imprint, front matter and final subject index | Complete native-layout extraction; some custom-font vowel symbols are corrupt |
| `Boutkan1995` | *The Germanic 'Auslautgesetze'*, Rodopi, 1995, Leiden Studies in Indo-European 4; 242 two-page spreads, ending at printed 476 | Complete independent OCR, with left and right faces kept in reading order |
| `BallStiles1983` | Original *Anglia* 101 article, printed 5--28, 24 sheets | Complete native-layout extraction, including notes and references |
| `Stiles2013` | Original *NOWELE* 66(1) article, printed 5--38, 34 sheets | Complete native-layout extraction, including notes and references |
| `Versloot2019` | Original *NOWELE* 72(1) article, printed 78--98, 21 sheets | Complete native-layout extraction, including both appendices |
| `Hollifield1980` | Both parts of *The Phonological Development of Final Syllables in Germanic*, *Die Sprache* 26 (1980), 19--53 and 145--178 | Private per-sheet OCR, including title sheets and the volume cover; use the original images for notation |

Installed originals are byte-identical to the valid supplied files.
`holdings.tsv` records their original filenames, exact SHA256 identities,
canonical paths and extraction hashes. No file in Downloads was moved,
renamed or deleted, and no existing holding was replaced.

The original Hogg/Fulk download was a 114-byte download-limit message,
not a PDF; only the valid `-1.pdf` replacement was installed. An empty
extra Boutkan download was also excluded, not treated as a second original.
The valid morphology title and imprint identify Volume 2, not the
previously held Volume 1 *Phonology*. The held Boutkan title/series pages,
not the supplied filename's added subtitle or volume zero, own its identity.
The two licensed Hollifield originals have their own [part-level receipt and
page map](hollifield1980.tsv), linked to the single bibliographic identity.

## Extraction, pagination and reading limits

Complete texts and intermediate OCR remain private under
`docs/references/local/sc047-early-apocope/`. `pdftotext -layout` supplies
the untouched native extracts. For Boutkan, all 484 page faces are rendered
independently at 450 dpi in grayscale and OCRed with installed Tesseract,
languages `eng+deu`, `--psm 3`, at most two single-threaded workers.
The original image-only PDF is never altered. Blank faces and unpaginated
front matter remain represented rather than silently dropped.

`page_map.tsv` maps PDF sheets and, for Boutkan, left/right regions.
Article mappings use their continuous printed pagination. Morphology body
page = PDF sheet minus 14; the separate Roman/unpaginated front matter must
not be assigned that offset. Boutkan's numbered sequence starts on the
right of sheet 4: left = twice the sheet minus 8, right = twice the sheet
minus 7, through printed 476 on the left of sheet 242. These are navigation
maps inferred from inspected anchors, not a claim that every folio or every
page image has been checked.

Acquisition checks cover identity, boundary coverage, extraction coverage
and selected original-image pagination anchors. No full scholarly reading,
new diplomatic transcription, verified reconstruction or historical verdict
is claimed. In particular, morphology's native text can turn vowel symbols
into ordinary Latin letters; OCR can likewise lose quantity, nasalization,
stress and phonetic distinctions. Search locates the passage; original
images establish its notation.

## Rights and preservation

Original PDFs, complete extracts, intermediate OCR and restoration bundles
are ignored local holdings. No redistribution permission is asserted.
Only bibliographic and acquisition metadata belong in public Git.
The private restoration bundle is
`docs/references/local/backups/sc047-early-apocope-intake.tar.gz`;
its members and hashes are checked against the installed holdings.
This same-volume copy is not independent disaster recovery.

No lexical row, rule, production order, reader claim, historical experiment
or certified scientific baseline is changed by this intake.

# Desktop source intake, 4 November 2026

The supplied Seiler2019 chapter and *Approaches to Old Frisian Philology*
scan are now project-local holdings. Fulk1998 is complete within the latter.
This closes two acquisition gaps, not a historical adjudication. The earlier
four-cell scientific state and full-cascade diagnosis are unchanged.

## Holdings, extent and identity

| Key | Preserved original | Coverage and searchable holding |
|---|---|---|
| `Seiler2019` | `docs/references/seiler_2019_erfurt_glossary.pdf` | All 16 sheets, printed525-540; `docs/references/local/desktop-2026-11-04/Seiler2019.txt` |
| `Fulk1998` | `docs/references/approaches_old_frisian_philology_1998.pdf` | Complete chapter, sheets155-170, printed139-154; `docs/references/local/desktop-2026-11-04/Fulk1998.txt` |
| `BremmerJohnstonVries1998` | Same assembled volume, not another original | All 344 supplied sheets OCRed; `docs/references/local/desktop-2026-11-04/BremmerJohnstonVries1998.v2.txt`; incomplete edition |

`originals.json` records exact Desktop filenames, original SHA256s, PDF metadata
and native-text status. `holdings.tsv` records original/text hashes, method,
rights and exact selected ranges. `page_map.tsv` maps every supplied sheet
and both complete selected chapters. Original files are copied byte-for-byte,
not replaced by OCR output. All original and derivative assets are retained
in both the durable main project and this worktree; access no longer depends
on Desktop. Copyrighted PDFs and complete texts remain ignored/local-only.

The Seiler PDF identifies Annina Seiler and the correct title, ends at printed
p.540, and includes its appendix and references. The containing Winter volume
is ISBN9783825369361, confirmed by its publisher catalogue.
The supplied volume's title/copyright sheets identify the three editors,
Rodopi1998, ISSN0165-7305 and ISBN90-420-0651-X. Its contents identifies Fulk
at p.139; the next contribution begins at p.155. Opening, closing and adjacent
chapter images confirm the complete16-page selection. Fulk's closing section
and its footnotes are present.

## Complete processing is not complete-edition or diplomatic certification

The assembled volume has no embedded text: native extraction yields only
344 form feeds. All344 sheets were processed locally with OCRmyPDF17.1.0,
Tesseract5.5.2, `eng+deu`, two workers, deskew and orientation detection.
A separate OCR-derived PDF, raw sidecar and embedded-layer extraction are kept.
All344 supplied sheets have nonempty OCR output. No copyrighted source was
sent to an external OCR service.

Seiler's supplied ABBYY layer was extracted completely rather than silently
replaced or normalised. Image checks reveal misrecognition of thorn/wynn-shaped
and phonetic letters. The local book OCR likewise misreads phonetic letters,
occasionally separates letters within words, and handles the sideways map
poorly. These texts are complete supplied-sheet navigation aids, not
glyph-corrected diplomatic editions. Load-bearing forms, tables and glyphs
must be checked against the preserved source images.

Checks included title/copyright/contents, both chapter boundaries, all Fulk
folio anchors, representative Seiler glyph/table sheets and its final
references, the book's pagination discontinuity and its actual final sheet.
The supplied volume is not complete:

| Defect | Evidence and consequence |
|---|---|
| Preface xi duplicated | Sheets10 and11 are separate scans of the same printed page; retained, not counted as independent content |
| Printed18 duplicated,21 absent | Sheets34/35 both18; sheet36 is19,37 is20,38 is22; explicit map overrides preserve correct labels |
| Blank302 omitted | Sheet317 is301 and318 begins303 |
| Tail missing | Final sheet344 is printed329, mid-contribution; contents lists Contributors at341, so at least330-341 remain absent |

None of these defects intersects Fulk's complete pp.139-154.
The first provisional sequential-map output is retained in the original
restoration bundle and `preflight-preservation.json`; its volume text is
not the current citation/navigation authority. The checked `.v2.txt` and
current manifest correct the three displaced early folio labels. No source
scan was reordered, deduplicated, overwritten or silently completed.

## Neutral navigation and reading limits

Seiler: pp.525-526 introduce the supplied source; pp.527-528 discuss glossary
relationships; pp.529-531 provide spelling/method sections; pp.532-533 and
534-536 are the two graphemic analyses; p.536 contains the conclusion;
pp.537-538 the appendix; pp.539-540 references.
These are author-section locators, not new CAPR historical conclusions.

Fulk: pp.139-142 introduce the question and competing chronological lists;
pp.143-153 contain the argument; p.154 has the closing section and footnotes.
This receipt certifies identity, supplied coverage and technical usability.
It does not claim a new complete scholarly adjudication of every premise.
Existing syntheses and source ledgers retain their original direct/indirect
evidence boundaries until an explicit research reassessment.

### Later direct scholarly review

The post-acquisition reassessment based at `7a3fb4df` directly reviewed
both complete chapters and their significant page images. Its findings are
recorded separately in the
[Fulk source card](../../../Germanic/docs/sound_changes/literature_dossiers/anglo_frisian/source_cards/14-fulk-1998-chronology.md)
and [Seiler source card](../../../Germanic/docs/sound_changes/audits/seiler2019-direct-source-card.md).
The [reader proposal](../../../Germanic/docs/sound_changes/audits/post-acquisition-reader-proposal.md)
distinguishes access corrections, evidence qualifications and unadopted
historical alternatives. The technical ingestion receipt above remains
unchanged in meaning; neither acquisition nor this reading authorizes
an executable or publication change.

## Reproduction, preservation and verification

`prepare_holdings.py preserve`, `ocr`, and `finalize --main MAIN_PROJECT`
performed ingestion. Native and OCR outputs remain separate.
The checked finalisation preserves the provisional receipt rather than
overwriting its restoration bundle.

```sh
python3 docs/references/desktop_2026-11-04/prepare_holdings.py check \
  --main /Users/nathanhill/Code/capr
```

Verification uses project files and recorded hashes, not the Desktop originals.
It checks both roots, complete sheet/marker coverage, selected ranges and every
restoration member. `preservation.json` identifies the checked local restoration
bundle and the original provisional receipt. These are same-disk restoration
copies, not independent off-machine backup.

Bibliographical identities are registered in `docs/refs.bib`. Earlier
unavailable-source receipts are preserved but explicitly superseded for access.
The November holdings inventory is refreshed through its existing generator.
The [remaining acquisition list](remaining-acquisitions.md) gives the three
still-requested works and identifier verification, plus the separate volume-tail
and p.21 completion gap.

The owner-managed portable refresh also records current bibliography provenance.
Its initial run exposed 37 pre-existing survey PDFs absent only from this isolated
worktree; these were copied from the durable project after matching every
previously certified input hash. This restores worktree-local access, not 37
new acquisitions. Portable provenance is explicitly labelled as such; no new
strict scientific or runtime certification is claimed.

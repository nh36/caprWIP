# Bibliography audit 02 report

## Summary

- Inspected **all 60 records** in `docs/refs.bib`: 28 `@book`, 23 `@article`, 2 `@incollection`, 3 `@misc`, 3 `@unpublished`, and 1 `@phdthesis`.
- Changed **49 BibTeX records** in `docs/refs.bib`.
- Performed the audit-02 publisher/address cleanup and removed the audit-01 `City: Publisher` workaround from the bibliography source.
- Regenerated the compact-alpha outputs through the established compact build route. The assembled Markdown was regenerated but did not change; the rendered TeX/PDF bibliography did.
- **No prose files were edited.**

## Publisher/address cleanup

Audit 01 had embedded publication places directly inside `publisher` strings for cited books so the current Pandoc/citeproc path would print them in the compact-alpha bibliography, for example `publisher = {{Oxford: Clarendon Press}}`.

Audit 02 restored clean BibTeX structure throughout the affected book layer, keeping **`address`** as the canonical place field and returning entries to the form `publisher = {Clarendon Press}` plus `address = {Oxford}`. This was applied across the previously hacked cited-book set and rechecked on the full `@book` inventory.

The current Pandoc/citeproc route still suppresses book publication places from clean `address`/`location` data. The regenerated compact-alpha bibliography therefore no longer prints cities, but the underlying bibliography data are now clean again. No `City: Publisher` fallback remains in `docs/refs.bib`.

## Newly completed records

### Kaluza1906

- **Fields added:** `year`, `volumes`, `publisher`.
- **Result:** `Historische Grammatik der englischen Sprache`, 2 vols., E. Felber, Berlin, 1906.
- **Source used:** Local OCR file plus the task brief's supplied verification target.
- **Remaining uncertainty:** None for the fields now carried.

### Erdmann1972

- **Fields added:** `author`, `journal`, `volume`, `number`, `pages`, `month`, `url`.
- **Result:** `Language` 48(2): 407-415, stable JSTOR URL.
- **Source used:** Local JSTOR text file `docs/references/erdmann_1972_suffixal_j_germanic.txt`.
- **Remaining uncertainty:** None.

### Pierce2006

- **Fields added:** `journal`, `volume`, `number`, `pages`.
- **Result:** `Journal of Germanic Linguistics` 18(4): 275-319.
- **Source used:** Local text file header `docs/references/pierce_2006_syllable_sievers_gothic.txt`.
- **Remaining uncertainty:** None.

## Rechecked priority records

- **Bammesberger1997:** Remains a clean `@article` and still renders with `Anglia` 115(2): 223-230 plus DOI. No further structural change was needed.
- **Lloyd1966:** Remains a clean `@article` and still renders with `Language` 42(4): 738-745 plus DOI/URL. No further change was needed after the address cleanup.
- **GermanicSlavicBaltic2025:** Kept as an honest unpublished-manuscript style record with date, place, unfinished-status note, and public URL. No publisher/container is implied.
- **Kroonen2011:** Remains correctly typed as `@book`; audit 02 only removed the embedded-place publisher hack and restored clean `publisher = {Rodopi}` plus `address = {Amsterdam and New York}`.

## Remaining unresolved records

No record-level gaps remain in the audited article/incollection tail from audit 01. A mechanical scan after the patch found:

- **0 incomplete `@article` records**
- **0 incomplete `@incollection` records**

The remaining issue is output-layer rather than source-layer: the current Pandoc/citeproc path suppresses publication-place display for books even when `address` is present and verified.

Two legacy citekeys were intentionally retained for citation stability even though their corrected metadata no longer matches the key year exactly:

- `HowellSalmons1988` now carries the verified 1997 article metadata.
- `Stiles2017` now honestly represents the revised 2017 typescript rather than the earlier published article alone.

## Output inspection

- **Cited books:** The regenerated compact-alpha bibliography is structurally clean, but publication places no longer display because the renderer suppresses `address`.
- **Bammesberger:** Adequate in the regenerated PDF bibliography; journal, volume, issue, pages, and DOI all render.
- **Lloyd:** Adequate in the regenerated PDF bibliography; journal, volume, issue, pages, and DOI all render.
- **Viredaz:** Adequate in the regenerated PDF bibliography; author, title, manuscript status, date/place, and URL render honestly.
- **Kaluza:** The record is complete in `refs.bib`, but it is **not cited in the current compact-alpha volume**, so it does not appear in that PDF bibliography. A separate citeproc spot-check confirms it now renders as `Kaluza, Max. 1906. Historische Grammatik der englischen Sprache. 2 vols. E. Felber.`
- **Erdmann:** The record is complete in `refs.bib`, but it is **not cited in the current compact-alpha volume**, so it does not appear in that PDF bibliography. A separate citeproc spot-check confirms `Language` 48(2): 407-415.
- **Pierce 2006:** The record is complete in `refs.bib`, but it is **not cited in the current compact-alpha volume**, so it does not appear in that PDF bibliography. A separate citeproc spot-check confirms `Journal of Germanic Linguistics` 18(4): 275-319.
- **References heading/page break:** Still correct; the references section begins on a fresh page with a visible heading.

## Recommendation

**A. Bibliography is now adequate for continued visual/prose review.**

The remaining blocker is not missing record metadata in the audited tail, but the current citeproc rendering behavior for book publication places. If visible city-of-publication output is required for publication review, that now needs a renderer-side solution rather than more source cleanup in `refs.bib`.

## Scope confirmation

- No TSV, FST, compact trace, model-entry prose, or citation-locator report files were edited.
- No generated TeX or PDF was hand-edited.
- Changes were limited to `docs/refs.bib`, regenerated compact-alpha outputs, `bibliography_audit_inventory.tsv`, and this report.
- No bibliography metadata/config file was changed, because no clean renderer-side fix for place display was identified in this pass.

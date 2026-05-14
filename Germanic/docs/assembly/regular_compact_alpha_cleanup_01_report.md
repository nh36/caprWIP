# Regular compact alpha cleanup 01 report

## Summary

- All 11 listed issues were addressed.
- 10 were fully repaired in the upstream source layer; 1 remains partial only in the sense that the Bammesberger bibliography record still lacks a safely verified journal/volume field.
- Bibliography records were updated for Viredaz, Adamczyk, and Bammesberger.
- `lexical_volume_regular_compact_alpha_01.md`, `.tex`, and `.pdf` were regenerated.
- Original model entries **were** edited where the artifact clearly originated in non-regular source prose.

## Issue-by-issue fixes

1. **`\*weljōn/\*weljOn`**
   - **Source location:** `2293-will-willa` regular prose in both the model entry and compact regular book-prose layer.
   - **Upstream file edited:** `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.model.md`; `Germanic/docs/assembly/book_prose/regular_all_01/2293-will-willa.book.md`
   - **Correction made:** normalized the reader-facing form to `*weljōn`.
   - **Verification result:** no `weljOn` remains in the regenerated compact alpha Markdown or TeX. Evidence for the normalization came from local reference files: Orel OCR gives `*weljōn`, while the Kluge OCR uses capital vowels in comparable long-vowel forms such as `*augOn`, so `*weljOn` was treated as OCR-level notation rather than a distinct intended form.

2. **Bold `normalized`**
   - **Source location:** `2242-ten-tēon.model.md`
   - **Upstream file edited:** `Germanic/docs/lexeme_reports/model_entries/2242-ten-tēon.model.md`
   - **Correction made:** removed bold from “normalized spelling”.
   - **Verification result:** the regenerated output reads “a normalized spelling” in plain roman type; `**normalized**` no longer appears.

3. **Italicize `folgian` in `PNWGmc *fulgija- ~ *fulgai- > OE fylgan ~ folgian`**
   - **Source location:** mixed inline-code rendering in `2027-follow-fylġan.model.md`
   - **Upstream file edited:** `Germanic/docs/assembly/build_full_lexical_volume.py`
   - **Correction made:** changed the inline linguistic tokenizer to look at the nearest non-whitespace context token, so lowercase forms after separators such as `~`, `/`, and `>` are still recognized as forms.
   - **Verification result:** the regenerated Markdown now has `PNWGmc _*fulgija-_ ~ _*fulgai-_ > OE _fylgan_ ~ _folgian_`.

4. **`palatal _ made explicit` in `ġealla`**
   - **Source location:** `2037-gall-ġealla.model.md`
   - **Upstream file edited:** `Germanic/docs/lexeme_reports/model_entries/2037-gall-ġealla.model.md`
   - **Correction made:** rewrote the sentence as “palatal ġ made explicit.”
   - **Verification result:** no stray underscore or broken `<ġ>` markup remains at that location.

5. **Italicize first `nosu` in `citing nosu < *nusō`**
   - **Source location:** mixed inline-code rendering in `2143-nose-nosu.model.md`
   - **Upstream file edited:** `Germanic/docs/assembly/build_full_lexical_volume.py`
   - **Correction made:** added `<` to `INLINE_SEPARATOR_CHARS`, so `nosu < *nusō` is tokenized as two forms around a roman separator.
   - **Verification result:** the regenerated Markdown now reads `citing _nosu_ < _*nusō_`.

6. **Italicize second `nosu` in `*núsō > *nósō > *nósu > nosu`**
   - **Source location:** mixed inline-code rendering in `2143-nose-nosu.model.md`
   - **Upstream file edited:** `Germanic/docs/assembly/build_full_lexical_volume.py`
   - **Correction made:** same tokenizer/separator fix as in item 5.
   - **Verification result:** the regenerated Markdown now reads `_*núsō_ > _*nósō_ > _*nósu_ > _nosu_`.

7. **Bold `genitive singular`**
   - **Source location:** `2235-swan-swanes.model.md`
   - **Upstream file edited:** `Germanic/docs/lexeme_reports/model_entries/2235-swan-swanes.model.md`
   - **Correction made:** removed bold from “genitive singular” in both the reconstruction and OE-evidence prose.
   - **Verification result:** `**genitive singular**` no longer appears in the regenerated compact alpha.

8. **`gs. swanes` formatting**
   - **Source location:** `2235-swan-swanes.model.md`
   - **Upstream file edited:** `Germanic/docs/lexeme_reports/model_entries/2235-swan-swanes.model.md`
   - **Correction made:** rewrote the Bright gloss sentence so the grammatical statement stays in roman prose while the forms remain italicized, and marked the full phrase `_swanes feðre_` explicitly.
   - **Verification result:** the regenerated output reads `form _swanes_ ... genitive singular _swanes_ and cites the phrase _swanes feðre_`; there is no italicized `_gs._` artifact.

9. **Viredaz bibliography problem**
   - **Source location:** `docs/refs.bib`, key `GermanicSlavicBaltic2025`
   - **Upstream file edited:** `docs/refs.bib`
   - **Correction made:** added `author = {Viredaz, Rémy}` and replaced the placeholder title with the locally verified paper title `Germanic, Slavic and Baltic "thousand" once more`; also expanded the note to `Working paper, Geneva, 20 October 2025.`
   - **Verification result:** the citation now renders as `Viredaz 2025` in the rebuilt TeX, and the bibliography entry begins `Viredaz, Rémy. 2025.`

10. **`palatal _.` in `wīþiġ`**
    - **Source location:** `2296-withy-wīþiġ.model.md`
    - **Upstream file edited:** `Germanic/docs/lexeme_reports/model_entries/2296-withy-wīþiġ.model.md`
    - **Correction made:** rewrote the sentence as “palatal ġ marked explicitly.”
    - **Verification result:** no broken underscore/HTML-style artifact remains at that location.

11. **Thin bibliography entries for Adamczyk and Bammesberger**
    - **Source location:** `docs/refs.bib`
    - **Upstream file edited:** `docs/refs.bib`
    - **Correction made:**  
      - `Adamczyk2001`: added journal title, volume, page range, ISSN, and stable URL from the Adam Mickiewicz University repository page.  
      - `Bammesberger1997`: corrected the title to the locally verified article title `Die Vorform von altenglisch hærfest` and added the page range `223--230` from the local scan.
    - **Verification result:** Adamczyk now renders as a normal journal article in the bibliography; Bammesberger now renders with corrected title and pages, but the journal/volume could not be verified safely from local or lookup evidence and were left unset.

## Bibliography repair

- **Viredaz:** added author, corrected the working-paper title from the local PDF first page, and expanded the note to include `Geneva, 20 October 2025`.
- **Adamczyk:** added `Studia Anglica Posnaniensia: An International Review of English Studies`, vol. 36 (2001), pp. 61-72, ISSN 0081-6272, and the stable handle URL `http://hdl.handle.net/10593/18335`.
- **Bammesberger:** replaced the incorrect English title with the locally verified German title `Die Vorform von altenglisch hærfest` and added pages `223--230`, confirmed from the local PDF page sequence.
- **Unverified:** Bammesberger’s journal title and volume/issue remain unverified; they were not invented.

## Artifact scan

- Fixed the additional `<ġ>`-markup artifact in `2027-follow-fylġan.model.md` by replacing the raw angle-bracket grapheme reference with plain `ġ`.
- The second rebuild confirmed that the remaining local false positives from a raw string scan were legitimate linguistic italics such as `palatal _g_`, `palatal _weġ_`, or `_\*-gj-\*_`, not stray markup corruption.
- No remaining `weljOn`, `**normalized**`, `**genitive singular**`, `palatal _`, or authorless Viredaz citation was found in the regenerated compact alpha Markdown or TeX.

## Output inspection

- The regenerated compact alpha no longer contains `*weljOn`.
- `normalized` is plain roman in the `tēon` entry.
- `folgian` is italicized in the rebuilt `PNWGmc ... > OE ...` line.
- The `ġealla` and `wīþiġ` sentences no longer contain `palatal _` artifacts.
- Both targeted `nosu` occurrences are italicized.
- The bold `genitive singular` wording is gone.
- The `swanes` location now keeps grammatical prose in roman while italicizing the OE forms and the full phrase `_swanes feðre_`.
- The Viredaz citation now renders by author.
- Adamczyk is materially fuller in the bibliography; Bammesberger is corrected and fuller, though still lacking safely verified journal/volume data.
- The regenerated PDF remains 110 pages.

## Scope confirmation

- No TSV, FST, compact trace, citation-locator report, or unrelated pilot/generated files were edited.
- Changes were limited to the compact-regular book-prose layer where needed, the non-regular source model entries where the artifact clearly originated there, `build_full_lexical_volume.py`, `docs/refs.bib`, the regenerated compact-alpha outputs, and this report.
- No hand edits were made directly to generated TeX or PDF files.

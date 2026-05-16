# Citation locator source-preparation triage 01 report

## Summary

- broad citations before: **209**
- broad citations after: **187**
- `page_markers_unreliable` before: **17**
- `page_markers_unreliable` after: **7**
- `source_preparation_needed` before: **15**
- `source_preparation_needed` after: **2**
- rows inspected: **32**
- locators added: **17**
- citation spans removed after direct witness review: **5**
- rows reclassified by status:
  - `general_background`: **1**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass treated the remaining `page_markers_unreliable` and
`source_preparation_needed` queue as a source-quality problem, not a prose-style
problem. The main gain came from going back to the actual local PDFs: several
sources that had looked unsafe in OCR-only form turned out to preserve printed
page headers well enough for exact recovery.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the
claim-isolation-06 baseline:

1. **22** rows were removed from the remaining-broad manifest after locator
   repair or citation removal.
2. **1** row was reclassified in place from `source_preparation_needed` to
   `general_background`.
3. **9** rows remain in the source-quality buckets after direct inspection.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `general_background` | 60 |
| `claim_not_isolated` | 56 |
| `headword_not_found` | 39 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `page_markers_unreliable` | 7 |
| `source_preparation_needed` | 2 |

The localized rows also appear in the regenerated
`lexical_volume_regular_compact_alpha_01.md`, so the manifest and the current
reader-facing Markdown remain synchronized.

## Primary-source verification

Every new locator added in this pass has a matching row in
`citation_locator_primary_source_evidence.tsv`.

New evidence rows were added for:

- `CLMM01-0051`, `CLMM01-0053` — `BosworthToller1898, 495`
- `CLMM01-0213` — `Kroonen2011, 167`
- `CLMM01-0237`, `CLMM01-0238` — `Kroonen2013, 423`
- `CLMM01-0241` — `Orel2003, 328`
- `CLMM01-0244` — `Orel2003, 362`
- `CLMM01-0258` — `Kroonen2013, 262`
- `CLMM01-0266` — `Seebold1970, 280`
- `CLMM01-0286` — `Seebold1970, 89`
- `CLMM01-0299` — `Orel2003, 120`
- `CLMM01-0361` — `BosworthToller1898, 85`
- `CLMM01-0362` — `BosworthToller1898, 699`
- `CLMM01-0366` — `Sweet1953, 29`
- `CLMM01-0387` — `ClarkHall1960, 48`
- `CLMM01-0403`, `CLMM01-0412` — `BosworthToller1898, 614`

No OCR line numbers, file offsets, search-result positions, or guessed PDF page
indexes were used as evidence.

## Source-by-source findings

### Bosworth-Toller

The searchable PDF was materially better than the earlier OCR-only impression.
This pass recovered:

- `hecg` on **p. 495**
- `sculdrum` on **p. 85**
- supplement `sculdra, an` on **p. 699**
- `liccian` on **p. 614**

It also showed where Bosworth was no longer worth carrying. The broad Bosworth
citations in **bone**, **harvest**, **breast**, and **have** were removed
because localized Clark Hall or other already-anchored evidence was sufficient.
Two Bosworth rows remain genuinely blocked: **fly** and **live**, where the
available witnesses still expose examples or cross-references rather than a safe
simplex headword page.

### Clark Hall

Clark Hall yielded one clean recovery in this queue: **borian** on **p. 48**.
The remaining Clark Hall tail is no longer about headword discovery; it is about
page exposure. **windan**, **weald / wold**, **brand**, **lungen**, and
**wiðig** are still visible only in witness states where the printed page number
cannot yet be cited safely.

### Orel

All three targeted Orel rows were recoverable from the PDF witness:

- **fright / fyrhte** — **p. 120**
- **sieve / sife** — **p. 328**
- **spare / sparian** — **p. 362**

### Kroonen 2013 and Kroonen 2011

The Kroonen PDFs were likewise productive:

- **sea / sǣ** — **p. 423**
- **whale / hwæl** — **p. 262**
- **neck / hnecca** (`Kroonen2011`) — **p. 167**

### Seebold and Sweet

The one-off handbook/primer rows were worth revisiting once the PDFs were in
play:

- **ban / bannes** (`Seebold1970`) — **p. 89**
- **whine / hwīnan** (`Seebold1970`) — **p. 280**
- **shove / sċēaf** (`Sweet1953`) — **p. 29**

### Ringe2006

No dedicated local `Ringe2006` witness was recovered. After direct reinspection,
`navel / nafola` was reclassified to `general_background`: the sentence is a
broad literature note about competing accounts of medial `u`, not a locator-
dependent headword or page-anchor claim.

## Examples of successful page-anchor repair

1. **Orel 2003** turned out to be fully recoverable from the local PDF, yielding
   clean locators for `*furxtīn`, `*sibaz`, and `*sparēnan`.
2. **Kroonen 2013** likewise yielded exact printed pages for `*saiwi-` and
   `*hwali-`, closing what had looked like stubborn OCR-anchor cases.
3. **Sweet 1953** preserved a clean printed grammar-table page for `scufan,
   sceaf, scufon, scofen`, which was enough to localize the `shove / sċēaf`
   row safely.

## Examples left broad after direct inspection

1. **fly / flēogan** still lacks a safe Bosworth headword page in the current
   witnesses; the recoverable hits are examples rather than a clean simplex
   dictionary entry.
2. **live / lifeþ** still lacks a safe Bosworth `libban` page; the current
   witness only exposes cross-reference material such as `a-libban` / `lifian`.
3. The remaining **Clark Hall** queue (`windan`, `weald / wold`, `brand`,
   `lungen`, `wiðig`) is now honestly a page-exposure problem, not a search-term
   problem.

## Source preparation still needed

The unresolved tail is now small and specific:

- **Bosworth-Toller:** a better base-dictionary witness or OCR layer for
  simplex **fly** and **live** headwords.
- **Clark Hall:** a witness that preserves printed page numbers more reliably in
  the surviving `windan` / `weald` / `brand` / `lungen` / `wiðig` zones.

## Compliance notes

- Every added locator has primary-source evidence recorded.
- No forbidden locator evidence was used.
- No generated TeX or PDF file was hand-edited.

## Recommendation

**A. create page maps / better OCR for specific sources.** The remaining
source-quality tail is now narrow enough that further progress depends less on
sentence surgery than on better Bosworth-Toller base-dictionary coverage and a
more page-faithful Clark Hall witness.

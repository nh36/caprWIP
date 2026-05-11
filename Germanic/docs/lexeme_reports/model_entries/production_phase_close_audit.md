# Production phase-close audit

## Summary

- **P1 status:** `P1_nonregular_missing_production` has **66** eligible rows, and
  all **66** now have current `.model.md` entries. Four of those current models
  were already on disk when later batches reached them and were therefore
  documented as pre-existing skips rather than newly drafted production outputs:
  `2183 shoulder / sċuldrum`, `2273 wasp / wæfs`, `2296 withy / wīþiġ`, and
  `2300 wool / wull`.
- **P2 status:** `P2_regular_with_note_missing_production` has **70** eligible
  rows, with **69** current `.model.md` entries. Batch 13 correctly reports that
  the remaining workable P2 queue was exhausted, but the repository still has
  one documented P2 exception: `2120 march / mearc` was skipped in
  `production_batch_10_report.md` because its verified
  `SOURCE_MATERIAL_PATHS` list contains a filename/path problem
  (`dev_notes_slices/2120-marrow-mearg.md` is not the row-local march file).
- **P3 status:** `P3_manifest_pilot_review_or_upgrade` has **12** eligible
  manifest-backed rows, and all **12** now have current `.model.md` entries. No
  `.p3_defer.md` notes are present. One row, `2013 fire / fȳre`, was explicitly
  skipped in batch 14 because a current model entry already existed; batch 15
  then reviewed the sole remaining eligible P3 row and records that **P3 is now
  exhausted**.
- **P4 status:** `P4_no_report_required` contains **231** rows. These were
  intentionally **not** drafted in the production phase because P4 is outside
  the selective-report backlog: regular rows without note-driven report demand.
- **Current model-entry inventory:** `model_entries/` contains **147** current
  `.model.md` files.
- **Production-batch contribution:** of those 147 current models, **142** appear
  to have been newly drafted or materially upgraded during production batches
  01–15; **5** were already-present current models encountered and skipped in
  later batches (`2013`, `2183`, `2273`, `2296`, `2300`).
- **Human-review load still visible at phase close:** the explicit “should not
  be scaled from without human review” lists, the final-prose hygiene scan, and
  the documented `2120`/`2183` exceptions produce a combined **110-entry-ID**
  review queue.

## Backlog status by priority tier

| Priority tier | Eligible rows | Model entries present | Deferred / skipped / documented | Remaining unexplained gaps |
| :--- | ---: | ---: | :--- | ---: |
| `P1_nonregular_missing_production` | 66 | 66 | 4 explicit pre-existing current-model skips: `2183`, `2273`, `2296`, `2300` | 0 |
| `P2_regular_with_note_missing_production` | 70 | 69 | 1 documented skip: `2120 march / mearc` (batch-10 source-path problem) | 0 |
| `P3_manifest_pilot_review_or_upgrade` | 12 | 12 | 1 explicit pre-existing current-model skip: `2013 fire / fȳre`; 0 defers | 0 |
| `P4_no_report_required` | 231 | 0 | intentionally out of scope for selective report drafting | n/a |

### Tier conclusions

1. **P1** is fully covered at the level requested by the backlog audit: every
   eligible row has a current model entry.
2. **P2** is **not literally 100% drafted**, because `2120 march / mearc` still
   lacks a current model entry, but it is a **documented** backlog/source-path
   exception rather than an unexplained gap.
3. **P3** is fully covered at the level requested by the review phase: every
   eligible row has a current model entry, and batch 15 correctly closes the
   remaining reviewable queue.
4. **P4** remains intentionally untouched.

## Batch report inventory

| Batch | Phase | Report present? | Revision report? | Notes |
| :--- | :--- | :---: | :---: | :--- |
| 01 | P1 | yes | no | Initial P1 production batch. |
| 02 | P1 | yes | yes | Post-review cleanup for `2086 knight`, `2090 lap`, `2107 live`, `2114 lung`, and `2068 heaven`; removed repository-facing phrasing and tightened normalization wording. |
| 03 | P1 | yes | no | P1 continuation batch. |
| 04 | P1 | yes | yes | `2169 sea / sǣ` OCR/source cleanup; `2216 stem / stefn` spot-check recorded with no substantive change. |
| 05 | P1 | yes | yes | `2286 whine / hwīnan` suspicious-transcription cleanup; batch report also documents pre-existing skips `2273`, `2296`, `2300`. |
| 06 | P2 | yes | no | Finite-form / paradigm-cell batch (`2310`–`2318`) plus `1934 bake / bacan`. |
| 07 | P2 | yes | no | P2 continuation. |
| 08 | P2 | yes | no | P2 continuation. |
| 09 | P2 | yes | no | P2 continuation. |
| 10 | P2 | yes | no | P2 continuation; documents the unresolved `2120 march / mearc` source-path problem. |
| 11 | P2 | yes | no | P2 continuation. |
| 12 | P2 | yes | no | P2 continuation. |
| 13 | P2 | yes | no | States that the remaining workable P2 queue was exhausted. |
| 14 | P3 | yes | yes | P3 batch 01; revision report records the genre-polish pass removing row/project-facing language from final prose. |
| 15 | P3 | yes | yes | P3 tail batch; revision report records the `tdcn` → `tacn` Campbell source cleanup for thistle and confirms P3 exhaustion remains unchanged. |

### Revision-report inventory

The expected revision reports are all present:

- `production_batch_02_revision_report.md`
- `production_batch_04_revision_report.md`
- `production_batch_05_revision_report.md`
- `production_batch_14_revision_report.md`
- `production_batch_15_revision_report.md`

No other revision reports appear to have been part of the actual workflow, and
their absence is not treated as an audit failure.

## Model-entry package completeness

- **No support-package files are missing among entries that appear to have been
  drafted or upgraded during production batches 01–15.**
- **Legacy / pre-existing current-model exception:** `2183 shoulder / sċuldrum`
  has:
  - `.model.md`
  - `.source_ledger.md`
  - `.model_implementation_report.md`
  - **no `.reviewer_checklist.md`**

That `2183` gap is recorded here as a legacy/pre-existing current-model issue,
not as a production-batch packaging failure, because batch 04 explicitly skipped
the row on the grounds that a current model entry already existed.

The other explicit pre-existing current-model skips (`2013 fire / fȳre`,
`2273 wasp / wæfs`, `2296 withy / wīþiġ`, `2300 wool / wull`) all have the full
three-file support package in place.

## Final-prose hygiene scan

Scan scope: all **147** current production-scope `.model.md` files in
`Germanic/docs/lexeme_reports/model_entries/`.

Result: **26 suspicious phrase hits across 25 files.** All hits below occur in
**final prose**, not in metadata blocks, report titles, or obviously acceptable
quoted-source contexts. All therefore merit **human review** before treating the
production phase as fully stylistically closed.

| File | Short phrase hit | Context | Human review? |
| :--- | :--- | :--- | :---: |
| `1962-bow-bēag.model.md` | `the decisive comparison` | final prose | yes |
| `1968-breast-brēost.model.md` | `the decisive point` | final prose | yes |
| `1980-cow-cȳ.model.md` | `the decisive comparison` | final prose | yes |
| `1990-dill-dile.model.md` | `the decisive point` | final prose | yes |
| `2004-fast-festan.model.md` | `the decisive point` | final prose | yes |
| `2009-field-feld.model.md` | `the row` | final prose | yes |
| `2011-find-fundene.model.md` | `the decisive comparison` | final prose | yes |
| `2016-flask-flasce.model.md` | `the decisive point` | final prose | yes |
| `2027-follow-fylġan.model.md` | `the decisive point` | final prose | yes |
| `2030-fowl-fugol.model.md` | `the row` | final prose | yes |
| `2034-fright-fyrhte.model.md` | `the decisive comparison` | final prose | yes |
| `2037-gall-ġealla.model.md` | `the decisive point` | final prose | yes |
| `2152-rest-ræste.model.md` | `the row` | final prose | yes |
| `2181-shilling-sċilling.model.md` | `the row` | final prose | yes |
| `2202-span-spannan.model.md` | `the row` | final prose | yes |
| `2217-still-stillan.model.md` | `the row` | final prose | yes |
| `2230-summer-sumer.model.md` | `the row` | final prose | yes |
| `2232-sunder-sundrian.model.md` | `the row` | final prose | yes |
| `2234-swallow-swealwe.model.md` | `the row` (2 hits) | final prose | yes |
| `2278-weapon-wǣpn.model.md` | `the row` | final prose | yes |
| `2293-will-willa.model.md` | `the row` | final prose | yes |
| `2294-wind-windan.model.md` | `the row` | final prose | yes |
| `2296-withy-wīþiġ.model.md` | `the decisive point` | final prose | yes |
| `2297-wold-weald.model.md` | `the row` | final prose | yes |
| `2305-yarn-ġearn.model.md` | `the row` | final prose | yes |

**Audit judgment:** none of these hits is severe enough to block phase close on
its own, but together they constitute a real **style-debt tail**. If the next
phase is document assembly, a final targeted prose-polish pass should happen
before publication-facing export.

## Recurring caveat types

The batch reports and paired implementation reports continue to show the same
families of caveat across the production corpus:

| Caveat type | Representative entries | Notes |
| :--- | :--- | :--- |
| Selected paradigm cell is less directly attested than the lexeme headword | `1962 bow / bēag`, `2011 find / fundene`, `2034 fright / fyrhte`, `2140 night / niht`, `2203 span / spanne`, `2250 thistle / þistles` | The selected finite/oblique form is philologically useful, but it must stay visibly distinct from the ordinary dictionary headword. |
| Reconstructed or normalized OE target must stay distinct from attested OE form | `2107 live / lifeþ`, `2114 lung / lungen`, `2151 reek / rēac`, `2189 sieve / sife`, `2254 three / þrīe` | These entries work only if the attested vs normalized/reconstructed distinction remains explicit. |
| Comparative headword differs from the selected OE-facing input or source notation | `2086 knight / cniht`, `2090 lap / lappa`, `2133 navel / nafola`, `2216 stem / stefn`, `2284 whale / hwæl` | Comparative labels remain useful background, but they are not always the form that should drive the OE derivation. |
| Stale TSV / PROTO metadata remains visible in supporting materials | `1983 cud / cwedu` | The row-local live metadata still lags behind the philological analysis. |
| Known / unexplained unmodelled entries remain intentionally unresolved | `1973 buck / bucc`, `2030 fowl / fugol`, `2240 tap / tæppa`, `2300 wool / wull` | These entries document genuine exceptions or unresolved problems rather than pretending to solve them. |
| OCR / source-ranking / transcription caution still matters | `2114 lung / lungen`, `2169 sea / sǣ`, `2286 whine / hwīnan`, `2250 thistle / þistles`, `2313`–`2318` finite-form rows | Local OCR/plain-text transcriptions were sometimes noisy enough that source ranking or paraphrase remained necessary. |

## Human-review queue

The batch reports explicitly mark **94 unique rows** as entries that **should
not be scaled from without human review**. The main reason groups are:

1. **Finite-form or paradigm-cell entries that must stay distinct from lemma
   headwords.**  
   `1962`, `2011`, `2034`, `2119`, `2140`, `2184`, `2203`, `2250`,
   `2260`, `2310`–`2318`.
2. **Normalized / reconstructed / selected attested targets that must stay
   visibly distinct from the ordinary citation form.**  
   `2107`, `2143`, `2151`, `2189`, `2230`, `2254`, `2268`, `2274`,
   `2286`.
3. **Comparative-label, source-notation, or stem-class disagreement between the
   cognate-set headword and the selected OE-facing input.**  
   `1965`, `2086`, `2090`, `2133`, `2134`, `2169`, `2181`, `2198`,
   `2212`, `2216`, `2284`.
4. **Lexeme-family separation: noun vs verb, simplex vs related family member,
   or nearby dossier bleed-through.**  
   `1942`, `1951`, `1961`, `1969`, `2186`, `2202`, `2204`, `2217`,
   `2232`, `2293`, `2294`.
5. **Exception-documentation / known-unmodelled rows.**  
   `1973`, `2030`, `2240`, `2300`.
6. **Source or support-material issues that should not be silently normalized
   away.**  
   `2114`, `2120`, `2169`, `2286`, `2313`, `2314`, `2317`, `2318`.

These groups do **not** exhaust every row-local caveat, but they cover the
recurring reasons the reports give for avoiding mechanical scale-up.

## Recommended next step

**Do not draft P4 lexical entries.** P4 remains intentionally outside the
selective-report backlog.

The production-phase closeout instead points to a two-part next step:

1. **Carry forward the documented exception list openly.** In practice that
   means keeping `2120 march / mearc` visible as a backlog/source-path problem
   and keeping the legacy `2183 shoulder / sċuldrum` checklist gap visible
   rather than silently treating either as finished.
2. **Move to the LaTeX/PDF assembly layer.** The next real project step should
   be a stable ordering and inclusion mechanism that can pull the current
   `.model.md` files into a single long-form report or book-style export,
   ideally with one final targeted prose-hygiene pass against the 25 files named
   above before publication-facing output.

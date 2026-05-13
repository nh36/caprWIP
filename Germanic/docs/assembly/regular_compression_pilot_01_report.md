# Regular-entry compression pilot 01 report

## Summary

- regular entries sampled: **12**
- variants produced: **A (current style baseline), B (compact regular style), C (experimental minimal regular style)**
- Markdown, TeX, and PDF were generated
- original model entries were not edited

## Sample selection

The pilot sample is:

1. `1934 bake / bacan` — ordinary weak verb with straightforward regular prose
2. `1942 beech / bōc` — very simple regular noun and strong minimal-style candidate
3. `1949 bier / bǣr` — simple noun with a short Source note
4. `1958 both / bū` — monosyllabic numeral with paradigm complexity and a manual comparison table
5. `1961 bow / bīeġan` — ordinary weak verb with a nontrivial but still regular development chain
6. `2003 fare / faran` — ordinary strong verb with standard evidence/development prose
7. `2049 guest / ġiest` — regular noun with an explicit Dialect note
8. `2095 learn / liornian` — regular verb with dialect framing and a manual comparison table
9. `2104 linden / lind` — very simple noun with a short Form note
10. `2129 mother / mōder` — regular kinship noun whose final section is comparison prose rather than a table
11. `2186 show / sċēawian` — regular verb with an orthographic Form note
12. `2278 weapon / wǣpn` — regular noun with broken/unbroken-form commentary in a Form note

These were chosen to cover:

- very simple regular nouns (`beech`, `bier`, `linden`)
- ordinary verbal entries (`bake`, `bow`, `fare`, `show`)
- entries with added source/dialect/form framing (`bier`, `guest`, `show`, `weapon`)
- comparison-heavy cases (`both`, `learn`, `mother`)

The selection is recorded in `regular_compression_pilot_manifest.tsv`.

## Rendering variants

- **Variant A: current style baseline**
  - reproduces the present assembled regular-entry style:
    - heading
    - derivation line
    - trace box
    - outcome line
    - all current prose sections with current subheadings
- **Variant B: compact regular style**
  - keeps:
    - heading
    - derivation line
    - trace box
  - removes the three repetitive standard headings:
    - `Reconstruction and comparative evidence`
    - `Old English evidence`
    - `Development to Old English`
  - merges their bodies into one `Commentary` block
  - retains shorter note-like sections separately, such as:
    - `Source note`
    - `Dialect note`
    - `Form note`
    - `Development note`
    - `Comparison`
- **Variant C: minimal regular style (experimental)**
  - keeps:
    - heading
    - derivation line
    - trace box
  - omits the merged regular commentary entirely
  - retains only explicit short note sections
  - replaces manual comparison tables with a short mechanical placeholder

## What changed in the compact style

- The repetitive standard headings were removed in Variant B.
- Their prose was merged mechanically into a single `Commentary` block.
- No new philological analysis was written; the pilot reuses or omits existing prose.
- Short note headings were preserved where they already existed in the model entries.
- Manual tables were handled as follows:
  - **Variant A**: kept exactly as in the current style
  - **Variant B**: kept under a normalized `Comparison` heading
  - **Variant C**: omitted and replaced with the short placeholder
    `_Manual comparison retained only in fuller variants._`

This means the pilot tests three real editorial postures:

- keep everything
- merge the standard report-like prose while keeping real notes and comparisons
- collapse very simple regular entries to trace-first catalogue entries, while flagging comparison-heavy cases as unresolved in the minimal form

## Review points

- Is Variant B short enough to feel book-like rather than report-like?
- Is Variant C too terse to carry regular entries responsibly?
- Which headings should remain in regular entries as stable note types?
- Should manual comparison tables be kept, converted, or moved in a fuller compact rollout?
- Should very simple regular entries have any prose after the trace at all?

## Recommendation

**A. Compact style is promising; choose a variant and apply it to all regular entries in a later pass.**

More specifically:

- **Variant B** is the likely production candidate.
- **Variant C** is useful as a lower-bound comparison but probably too terse for general rollout.
- Manual comparison tables remain the main editorial decision before any full regular-entry compression pass.

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, bibliography, OCR/reference, or citation-locator report files were edited
- full lexical alpha outputs were not overwritten

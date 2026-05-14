# Regular prose rollout 01 report

## Summary

- Regular entries processed: 70.
- Regular `.book.md` files created: 70 under `Germanic/docs/assembly/book_prose/regular_all_01/`.
- Pilot 03 sample prose reused: yes, for all 12 previously drafted pilot entries.
- New full alpha outputs generated: `lexical_volume_regular_compact_alpha_01.md`, `lexical_volume_regular_compact_alpha_01.tex`, and `lexical_volume_regular_compact_alpha_01.pdf`.
- Original model entries edited: no.

## Prose style

The rollout uses the approved pilot 03 style for regular entries:

- compact;
- factual;
- citation-preserving;
- non-meta;
- specific to regular-entry treatment.

Each regular entry now uses one compact paragraph, or one paragraph plus a short note where dialect, spelling, paradigm choice, or source disagreement makes that useful. The prose states the reconstruction or comparative basis, the Old English evidence or normalized target, and the reason the development is regular without reverting to full report-export structure.

## Entry coverage

- Total regular entries expected from `manifest_regular.tsv`: 70.
- Total regular prose files created in `book_prose/regular_all_01/`: 70.
- Missing regular prose files: none.
- Entries still needing human review: `both / bū`, `learn / liornian`, `milk / meoloc`, `mother / mōder`, `weapon / wǣpn`, `harvest / hierfest`, `field / feld`, `summer / sumer`.

## Complex cases

Regular entries that required notes or special handling fell into the expected categories:

- **Source note**: `bier / bǣr`, `bone / bān`, `harvest / hierfest`, `coat / rocc`, `swine / swīn`, `thorn / þorn`, `town / tūn`
- **Dialect note**: `give / ġiefan`, `guest / ġiest`, `hold / healdan`, `light / līehtan`, `sheep / sċēap`, `smear / smierwan`, `wold / weald`
- **Form note**: 29 entries, especially normalization and competing citation-form cases such as `show / sċēawian`, `sleep / slǣpan`, `summer / sumer`, `weapon / wǣpn`
- **Development note** folded into compact prose: `begin / beġinnan`, `gold / gold`, `wade / wadan`
- **Lexical note** folded into compact prose: `think / þenċan`, `tide / tīd`, `warp / weorpan`, `wax / weaxan`, `will / willa`, `wind / windan`
- **Comparison note**: `both / bū`, `learn / liornian`, `milk / meoloc`, `mother / mōder`

No large manual tables were carried into the regular book-prose layer. Comparison-heavy cases were compressed into short prose notes.

## Full assembly result

- Total entries assembled: 147.
- Regular entries using the book-prose layer: 70.
- Non-regular entries still using model-entry prose: 77.
- PDF build result: succeeded.
- PDF page count: 110.

The assembled part counts remained correct:

- Part I. Regular derivations: 70
- Part II. Attested variants and selected comparison forms: 4
- Part III. Early analogy and pre-Old-English input selection: 35
- Part IV. Late analogy and paradigm-cell selection: 28
- Part V. Reconstructed Old English comparators: 3
- Part VI. Known but unmodelled remodellings: 2
- Part VII. Unexplained or deliberately unmodelled exceptions: 5

## Quality checks

- **Banned phrase scan**: no banned meta-editorial phrases were found in `book_prose/regular_all_01/` or in Part I of `lexical_volume_regular_compact_alpha_01.md`.
- **Citation check**: citations remained in the compact regular prose where claims were retained; the PDF contains 952 link annotations and a references section.
- **Unicode check**: XeLaTeX build succeeded with the full regular rollout and preserved Old English and reconstructed forms.
- **Trace-box check**: all 147 entries still render boxed traces; the assembled Markdown contains 147 trace boxes, and only the 77 non-regular entries retain the old `#### Derivation trace` wrapper.
- **Bibliography/link check**: bibliography remains present, references are emitted, and PDF link annotations remain live.

## Recommendation

**A. Regular prose rollout is successful; review the full regular section visually.**

The rollout now gives the regular section a consistent compact prose layer in the approved pilot 03 style. The remaining concerns are a small set of substantive philological review points, not a failure of the rollout or assembly method.

## Scope confirmation

- No model-entry prose or metadata was edited.
- No TSV source data, FST files, compact trace outputs, bibliography files, OCR/reference files, or citation-locator report files were edited.
- Changes were limited to `book_prose/regular_all_01/`, `build_full_lexical_volume.py`, the generated compact-regular alpha outputs, and this report.

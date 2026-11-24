# Old English ‘hay’ article

**Status:** Source preparation is complete. The next cycle is for historical
inference, not further philological investigation or general acquisition.

## Start the next research cycle

1. [`SOURCE_PREPARATION_HANDOFF.md`](SOURCE_PREPARATION_HANDOFF.md) is the
   principal operational entry point: it summarizes established
   observations, disputed claims, source locations, checkout dependencies,
   and access limitations.
2. [`RESEARCH_MEMO_CYCLE7.md`](RESEARCH_MEMO_CYCLE7.md) is the principal
   evidence memorandum for the final verification cycle, including Eadwine,
   Faulkner, Hogg, Ritt, and the bounded Farman controls.
3. [`DRAFT.md`](DRAFT.md) is the current article draft.
   [`QUANTITY_EVIDENCE.md`](QUANTITY_EVIDENCE.md) and the **Current status
   after cycle 7** section at the top of [`UNRESOLVED.md`](UNRESOLVED.md)
   state the current evidence assessments and remaining historical questions.

## Current assessments versus historical conclusions

Use the cycle-7 memo and the current-status section of `UNRESOLVED.md` for
present assessments. Earlier cycle memos preserve the research history; they
are not current verdicts where later evidence has superseded them. In
particular:

- The categorical exclusion of Model A on West Saxon vocalism is superseded.
  The two Eadwine ⟨hieg⟩ readings are directly verified, but their dialect and
  exemplar provenance—and the applicable source of ⟨ie⟩—remain unresolved.
  Normalized *hīeġ* is not a manuscript reading.
- The claim that every viable derivation necessarily predicts a long direct
  vowel is withdrawn. The regular development and quantity of the inherited
  direct form remain open.
- Paris Psalter *hege* supplies a late overtly inflected form; older
  statements that no inflected form exists are historical, not current.
- The ‘hay-way’ interpretation of S 1196 *heiweg* is disputed, not an
  uncontested conventional identification.
- Cycle-5/6 Farman sensitivity counts of 6/135 are superseded by the
  expanded cycle-7 count of 6/147. Use
  `FARMAN_ACCENT_CALIBRATION.tsv` and `calibrate_farman_accents.py`.

## Private references and checkout dependency

Registered bibliographic records, holdings, and page maps are indexed in
`docs/references/catalogue.tsv`,
`docs/references/projects/hay-article.tsv`, and
`docs/references/hay-article-literature-2026-11-24/{holdings.tsv,page_map.tsv}`.
The private PDFs and searchable extracts are under the Git-ignored
`docs/references/local/` directory. They were verified in the checkout used
for this handoff: all 13 hay holdings and 26 listed PDF/text files exist and
match their recorded SHA-256 values. `docs/references/validate_catalogue.py`
also checks catalogue paths, hashes, and privacy boundaries. This local
directory is per-worktree and does not automatically appear in a fresh
checkout. Before source-heavy work in another worktree, confirm that its
registered files exist and match the recorded SHA-256 values; do not
redistribute restricted copies.

Dal (1934), Wallenberg (1931), and Brooks & Kelly (2013) are being handled
separately by the project owner. They are not prerequisites for this
handoff.

## Standalone article build

Run from the repository root:

```sh
bash Germanic/articles/hay/build_article_docker.sh
```

The generated PDF is
`.capr-work/hay-article-publication/hay-article.pdf` (ignored build output,
not a tracked source). The build also checks publication references. The
current checkout's PDF is 14 pages.

## Supporting evidence

`CONCORDANCE.tsv`, `DOE_CROSSWALK_2026-11-23.tsv`,
`COOPER_CHARTER_CORPUS.tsv`, `PARADIGM.md`, `LINDISFARNE_EVIDENCE.md`,
`SAME_SCRIBE_CONCORDANCE.tsv`, `FARMAN_ACCENT_CALIBRATION.tsv`, and the
remaining `RESEARCH_MEMO_CYCLE*.md` files provide the underlying
source-specific records. Historical assessments are retained for context;
follow the current evidence status above rather than reviving superseded
conclusions.

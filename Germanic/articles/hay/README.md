# Old English ‘hay’ article

**Status:** Research cycle 8 (the historical-inference cycle) is complete.
The central question — did ‘hay’ require analogy under early nasal apocope?
— is answered: the regular early-apocope outcome of the direct cell is
disyllabic, w-retaining \*\*hewe (established from the *eowu*/*cleweþa*/
*mete*/*mene* controls), so under early apocope the attested paradigm
requires whole-stem levelling in every dialect, while under late apocope it
is regular. The attested word is long-vowelled on all viable derivations.
The apocope chronology itself remains undecided.

## Entry points

1. [`RESEARCH_MEMO_CYCLE8.md`](RESEARCH_MEMO_CYCLE8.md) is the principal
   research memorandum: the established regular development, the refutation
   of the `OEWLossBeforeI` experiment, the thirteen adjudicated verdicts,
   and the production recommendation.
2. [`DRAFT.md`](DRAFT.md) is the current article, rewritten in cycle 8
   around the established result (Sections 5–9 new; Sections 1–4 philology
   from cycles 3–7).
3. [`DERIVATIONS.md`](DERIVATIONS.md) holds the authoritative stage-by-stage
   derivation record; [`experiments/`](experiments/) contains the
   reproducible finite-state verification (research-only, not production).
4. [`SOURCE_PREPARATION_HANDOFF.md`](SOURCE_PREPARATION_HANDOFF.md) and
   [`RESEARCH_MEMO_CYCLE7.md`](RESEARCH_MEMO_CYCLE7.md) document the
   completed source-preparation phase: verified observations, source
   locations, checkout dependencies, and access limitations.

## Current assessments versus historical conclusions

Use the cycle-8 memo and the **Current status after cycle 8** section at the
top of [`UNRESOLVED.md`](UNRESOLVED.md) for present assessments. Earlier
cycle memos preserve the research history; they are not current verdicts
where later evidence has superseded them. In particular:

- The cycle-7 statement that the regular development and quantity of the
  inherited direct form "remain open" is superseded: both are now
  established (\*\*hewe; long on all viable accounts).
- The cycle-4 categorical "every viable derivation predicts a long vowel"
  and its cycle-6/7 withdrawal are both superseded by the cycle-8 result,
  which restores the conclusion on new (derivational-exhaustion) grounds.
- The cycle-2/3 verdict that ‘hay’ is a non-discriminating dependent of the
  apocope chronology is superseded: it now weighs with *nett*/*bedd*/*cynn*
  for late apocope, paired against *mene*.
- The Eadwine ⟨hieg⟩ readings remain directly verified but dialectally
  unassigned; normalized *hīeġ* is not a manuscript reading.
- The ‘hay-way’ interpretation of S 1196 *heiweg* remains disputed, and the
  charter identifications no longer carry weight in the historical argument.
- Farman sensitivity counts: use the cycle-7 6/147 figures,
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
current checkout's PDF is 16 pages.

## Supporting evidence

`CONCORDANCE.tsv`, `DOE_CROSSWALK_2026-11-23.tsv`,
`COOPER_CHARTER_CORPUS.tsv`, `PARADIGM.md`, `LINDISFARNE_EVIDENCE.md`,
`SAME_SCRIBE_CONCORDANCE.tsv`, `FARMAN_ACCENT_CALIBRATION.tsv`, and the
remaining `RESEARCH_MEMO_CYCLE*.md` files provide the underlying
source-specific records. Historical assessments are retained for context;
follow the current evidence status above rather than reviving superseded
conclusions.

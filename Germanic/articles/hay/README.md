# Old English ‘hay’ article

**Status:** Research cycle 9 (critical correction of cycle 8) is
complete. Cycle 8's central claim — that no loss of \*w before
unstressed \*i exists, hence a regular \*\*hewe — was a
source-critical error: Ringe & Taylor 2014: 257–61 (§6.7.1) establish
the change, and the frozen `OEWLossBeforeI` correctly encodes it. The
corrected result: the regular early-apocope direct cell is \*hē (via
hiatus \*he.i and contraction); Anglian *hēġ* may continue it with only
glīg-style analogical restoration of -ġ, while WS *hīeġ* requires the
oblique vocalism; under late apocope no analogy is needed. The necessity
and scope of analogy are dialect-differentiated, and the apocope
chronology remains undecided.

## Entry points

1. [`RESEARCH_MEMO_CYCLE9.md`](RESEARCH_MEMO_CYCLE9.md) is the principal
   memorandum: the cycle-8 errors, the corrected derivation, the
   classified w-loss evidence, and the corrected verdicts.
2. [`DRAFT.md`](DRAFT.md) is the current article (rewritten in cycle 9).
   The built PDF is committed at [`hay-article.pdf`](hay-article.pdf).
3. [`DERIVATIONS.md`](DERIVATIONS.md) holds the stage-by-stage derivation
   record (cycle-9 correction at top); [`experiments/`](experiments/)
   contains the reproducible finite-state verification (14/14 PASS;
   research-only, not production).
4. [`SOURCE_PREPARATION_HANDOFF.md`](SOURCE_PREPARATION_HANDOFF.md) and
   [`RESEARCH_MEMO_CYCLE7.md`](RESEARCH_MEMO_CYCLE7.md) document the
   completed source-preparation phase.

## Current assessments versus historical conclusions

Use the cycle-9 memo and the **Current status after cycle 9** section at
the top of [`UNRESOLVED.md`](UNRESOLVED.md) for present assessments.
Earlier cycle memos (including `RESEARCH_MEMO_CYCLE8.md`, now flagged as
superseded) preserve the research history; they are not current verdicts.
In particular:

- The cycle-8 reconstruction \*\*hewe, the refutation of
  `OEWLossBeforeI`, the eowu/cleweþa "controls", the
  obligatory-whole-stem-levelling verdict, the bedd-equivalent weighting
  of 'hay', and the mene/hay minimal-pair symmetry are all withdrawn.
- Quantity: long in the attested period on all surviving derivations;
  the pre-contraction hiatus stage (⟨ei⟩, streide-type) could persist
  into the earliest written period, so the earliest ⟨hei-⟩ items remain
  unassigned.
- The Eadwine ⟨hieg⟩ readings remain directly verified but dialectally
  unassigned; normalized *hīeġ* is not a manuscript reading.
- The ‘hay-way’ reading of S 1196 *heiweg* remains disputed; no Kentish
  paradigmatic history may be built on it.
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
built PDF is also committed as `Germanic/articles/hay/hay-article.pdf` for review.

## Supporting evidence

`CONCORDANCE.tsv`, `DOE_CROSSWALK_2026-11-23.tsv`,
`COOPER_CHARTER_CORPUS.tsv`, `PARADIGM.md`, `LINDISFARNE_EVIDENCE.md`,
`SAME_SCRIBE_CONCORDANCE.tsv`, `FARMAN_ACCENT_CALIBRATION.tsv`, and the
remaining `RESEARCH_MEMO_CYCLE*.md` files provide the underlying
source-specific records. Historical assessments are retained for context;
follow the current evidence status above rather than reviving superseded
conclusions.

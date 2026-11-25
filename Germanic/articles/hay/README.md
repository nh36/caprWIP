# Old English ‘hay’ article

**Status:** Cycle 11 distinguishes nonfinal /e.i/ contraction from the
unresolved word-final chronology, and documents structural parallels
that do not establish regular final /e.i/ > /ej/. Vespasian ⟨heg⟩
does not prove survival without analogy or wholesale stem replacement.
Consonant restoration after contraction is a narrower Anglian
alternative; West Saxon high vowels favour protected vocalism.

## Entry points

1. [`ARGUMENT_CYCLE11.md`](ARGUMENT_CYCLE11.md) gives the propositions
   and adversarial assessment; [`RESEARCH_MEMO_CYCLE11.md`](RESEARCH_MEMO_CYCLE11.md)
   records the new source collation, census, and limits of the results.
   The Cycle 9 memorandum remains useful for the evidence for w-loss.
2. [`DRAFT.md`](DRAFT.md) is the current, self-contained article.
   The built PDF is committed at [`hay-article.pdf`](hay-article.pdf).
3. [`MORPHOLOGICAL_CONCORDANCE.tsv`](MORPHOLOGICAL_CONCORDANCE.tsv) records
   individual readings and case decisions; [`DERIVATIONS.md`](DERIVATIONS.md)
   and [`experiments/`](experiments/) document the conditional derivations
   (research-only, not production).
4. [`SOURCE_PREPARATION_HANDOFF.md`](SOURCE_PREPARATION_HANDOFF.md) and
   [`RESEARCH_MEMO_CYCLE7.md`](RESEARCH_MEMO_CYCLE7.md) document the
   completed source-preparation phase.

## Current assessments versus historical conclusions

Use the Cycle 11 memo and the **Current status after Cycle 11** section at
the top of [`UNRESOLVED.md`](UNRESOLVED.md) for present assessments.
Earlier cycle memos (including `RESEARCH_MEMO_CYCLE8.md`, now flagged as
superseded) preserve the research history; they are not current verdicts.
In particular:

- The cycle-8 reconstruction \*\*hewe, the refutation of
  `OEWLossBeforeI`, the eowu/cleweþa "controls", the
  obligatory-whole-stem-levelling verdict, the bedd-equivalent weighting
  of 'hay', and the mene/hay minimal-pair symmetry are all withdrawn.
- Quantity: long under contraction or protected-stem derivations;
  earliest Anglian spellings do not independently establish this
  quantity. Farman provides moderate evidence for his own usage only.
- The Eadwine ⟨hieg⟩ readings remain directly verified but dialectally
  unassigned; normalized *hīeġ* is not a manuscript reading.
- ‘Hay-road’ has a provisional evidential advantage for S 1196
  *heiweg*. No hypothesis about a Kentish simplex paradigm follows.
- Farman sensitivity counts: use the cycle-7 6/147 figures,
  `FARMAN_ACCENT_CALIBRATION.tsv` and `calibrate_farman_accents.py`.

## Reproducing the morphological census

The tab-separated concordance has one row per witness reading, including
parallel copies and one record (not two tokens) for a corrected form.
`source` and `locus` identify the edition or corpus locator; `context`
states the grounds for `case`. A `none` case is an isolated equivalent;
`uncertain` is a construction without a decisive case marker.
`ending` describes the visible form, independently of case.
`image` means manuscript inspection, `edition` a printed reading,
`apparatus` a reported correction, `corpus` an additional indexed
reading, `candidate` an incompletely classified indexed result,
`locator` an incompletely identified source, and `excluded` a diagnostic
non-token. `unknown` does not imply absence. The article's dated set is
the 9th–11th-century rows with status `edition`, `image`, or `apparatus`;
all other rows remain available without contributing to its chronology.

```sh
awk -F '\t' 'NR > 1 && $2 ~ /^(09|10|11)c/ && $14 ~ /^(edition|image|apparatus)$/ {
    print $10, $12
}' Germanic/articles/hay/MORPHOLOGICAL_CONCORDANCE.tsv | sort | uniq -c
```

For group counts, count distinct `tradition` values within each case,
not manuscript rows. Century-level date ranges do not resolve the
relative order of overlapping witnesses.

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

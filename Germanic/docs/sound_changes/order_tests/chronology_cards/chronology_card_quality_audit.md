# Chronology card quality audit

## Scope

This audit checks the completed explicit-chain first-break documentation layer after consolidation. No new first-break computations were run.

Files checked:

1. `Germanic/docs/sound_changes/order_sensitivity_first_break_consolidated_overview.md`
2. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
6. `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
7. `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`
8. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC*.md`

## Card count and coverage

The corpus-level coverage claim is consistent across the checked files:

1. `chronology_card_index.tsv` contains `70` rows.
2. `order_tests/chronology_cards/SC*.md` contains `70` card files.
3. Every indexed `SC` card has a corresponding card file.
4. Every `SC*.md` card file is represented in `chronology_card_index.tsv`.
5. `sound_change_order_sensitivity.tsv` also contains `70` first-break-complete rows for the same searchable explicit-chain set.
6. `next_batch_candidates.tsv` contains no `recommended_for_next_batch = yes` rows and no `queued` rows.

No card-count or coverage inconsistencies were found.

## Reciprocal / near-reciprocal audit

The consolidated overview's reciprocal-or-near-reciprocal list is supported by the index and the individual cards for the checked pairs:

1. `SC016` / `SC017`
2. `SC017` / `SC019`
3. `SC019` / `SC020`
4. `SC026` / `SC027`
5. `SC029` / `SC030`
6. `SC030` / `SC032`
7. `SC031` / `SC034`
8. `SC039` / `SC040`
9. `SC042` / `SC043`
10. `SC043` / `SC044`
11. `SC044` / `SC045`
12. `SC047` / `SC048`
13. `SC052` / `SC055`
14. `SC055` / `SC056`
15. `SC064` / `SC072`
16. `SC066` / `SC068`
17. `SC070` / `SC071`
18. `SC072` / `SC073`
19. `SC074` / `SC075`
20. `SC079` / `SC080`
21. `SC081` / `SC082`
22. `SC082` / `SC083`
23. `SC085` / `SC086`

Most of these pairs are explicitly reciprocal in both the index and at least one side of the card prose. A few are documented more asymmetrically in prose even though the pair-level relation is clear from the opposite card and from the crossed-stage symmetry. That is acceptable as long as the summary layer does not overstate them as stronger than the cards support.

### Fix made

One small normalization issue was found and corrected:

1. `SC019` / `SC020` was already treated in the consolidated overview and consolidation report as a reciprocal-or-near-reciprocal `rest` relation, and `SC019` already said its later boundary reciprocates `SC020` earlier.
2. `chronology_card_index.tsv` still had `SC020` marked `has_reciprocal_boundary = no`.
3. The `SC020` card and `sound_change_order_sensitivity.tsv` note also stopped short of stating the reciprocal link explicitly.

This pass normalized those three places so `SC020` now explicitly records that its earlier boundary reciprocates `SC019` later around `rest`.

## Negative / boundary cards

The consolidated overview's negative-card list is accurate and consistent across the card files, index, and summary TSV:

1. `SC014`
2. `SC018`
3. `SC022`
4. `SC025`
5. `SC028`
6. `SC053`
7. `SC058`
8. `SC065`
9. `SC067`
10. `SC076`

For all ten rules:

1. the card describes the result as no historical first break / boundary-only evidence;
2. `chronology_card_index.tsv` records `blocked_by_runner_limitation` earlier and `no_break_before_runner_boundary` later;
3. `sound_change_order_sensitivity.tsv` describes the result as a negative / boundary card rather than a positive chronology constraint;
4. the consolidated overview lists the same ten rules.

## Runner-limited and non-historical cases

The runner-limited and non-historical categories are consistent across the overview, README, consolidation report, plan, index, and individual cards:

1. earlier searches stopping at bundled `PWGmcChanges` are consistently treated as runner-bounded search limits rather than ordinary historical boundaries;
2. `SC031` earlier and `SC033` earlier are consistently described as real computational breaks that cross bundled `PWGmcChanges` and are therefore non-historical;
3. `SC037` later is consistently described as crossing technical-marker `SC038` rather than an ordinary historical sound change.

No place checked rewrites these cases into ordinary historical chronology constraints.

## Later no-break-before-`SC087` cases

The consolidated overview's later no-break list matches the index/cards:

`SC014`, `SC018`, `SC022`, `SC025`, `SC027`, `SC028`, `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, `SC086`

Across the checked documentation layers, these are consistently framed as search-boundary observations only, not as historical claims that the rule must precede `SC087`.

## Broad / far labels

The checked broad/far cases are consistently guarded against adjacency-style overstatement:

1. `SC015` later across `SC036`
2. `SC020` later across `SC040`
3. `SC021` later across `SC040`
4. `SC023` later across `SC047`
5. `SC024` later across `SC056`
6. `SC033` later across `SC044`
7. `SC036` earlier across `SC019`
8. `SC040` later across `SC072`
9. `SC041` earlier across `SC020`
10. `SC047` later / `SC048` earlier
11. `SC069` earlier across `SC023`
12. `SC072` later / `SC073` earlier
13. `SC078` earlier across `SC070`
14. `SC079` earlier across `SC055`
15. `SC081` earlier across `SC055`
16. `SC087` earlier across `SC044`

No contradictory local-adjacency wording was found in the checked summary layers.

## Inconsistencies found

Only one documentation inconsistency was found:

1. `SC020` was missing the reciprocal flag and explicit reciprocal wording even though the rest of the corpus already treated `SC019` / `SC020` as a reciprocal-or-near-reciprocal pair.

No other count, coverage, negative-card, runner-limit, no-break, or broad/far inconsistencies were found in the checked files.

## Remaining questions

None that block reuse of the current corpus.

The only mild stylistic asymmetry that remains is that some reciprocal pairs are stated explicitly on one card but only implicitly on the opposite card via the crossed-stage relation. That is acceptable for now and does not create a contradiction in the current documentation layer.

## Recommendation for the next phase

The documentation layer is now consistent enough to support a **graph export / visualization pass** as the next substantial step.

That would make the reciprocal, one-sided, broad/far, negative, and runner-limited network easier to inspect before any heavier runner work. After that, the next high-value technical phase remains runner work to expose bundled stages such as `PWGmcChanges`.

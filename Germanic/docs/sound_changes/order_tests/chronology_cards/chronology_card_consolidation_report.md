# Chronology card consolidation report

## Completed coverage so far

The current chronology-card set now covers seventeen tested rules:

1. `SC041`, `SC042`, `SC043`, `SC044`, `SC045`, `SC046`, `SC047`, `SC048`
2. `SC050`, `SC051`, `SC052`, `SC055`, `SC056`, `SC059`
3. `SC063`, `SC072`, `SC078`

This means the pilot rules, batch 04, batch 05, and the later scaled batch are all now represented in a single indexed card set. The new `chronology_card_index.tsv` records the current order, safe window, boundary type, failure counts, reciprocal status, and narrative cautions for each completed card.

## Strong reciprocal boundaries found so far

The strongest reciprocal or near-reciprocal relations visible in the current card set are:

1. `SC044` / `SC045`: `SC044` later breaks across `SC045`, and `SC045` earlier breaks across `SC044`.
2. `SC047` / `SC048`: `SC047` later and `SC048` earlier share the same 87-row broad `-en` failure set.
3. `SC050` / `SC052`: `SC050` later and `SC052` earlier form a concrete local relation around `stretch`; `SC050` earlier is still runner-bounded and is not part of a reciprocal historical pair.
4. `SC052` / `SC055`: `SC052` later and `SC055` earlier form a tight reciprocal relation around `cow` and `lung`.
5. `SC055` / `SC056`: `SC055` later and `SC056` earlier form a reciprocal boundary around `gift` and `sheath`.
6. `SC063` / `SC072`: the relation is currently one-sided rather than reciprocal, because `SC063` later breaks across `SC072`, but `SC072` earlier breaks across `SC064`.
7. `SC059` / `SC078`: the TSVs support a one-sided later relation from `SC059` to `SC078`, but not a full reciprocal pair, because `SC078` earlier breaks instead across `SC070`.

The older pilot chain `SC042` / `SC043` and `SC043` / `SC044` also remains important, even though this report foregrounds the newer network that now extends through the mid and late OE corridor.

## Broad computational boundaries

Several boundaries now need explicit broad-boundary handling rather than narrow adjacency prose:

1. `SC041` earlier breaks far away at `SC020` with 64 newly failing rows and a large class of spurious `-a`-final outputs.
2. `SC047` later and `SC048` earlier form the reciprocal 87-row `-en` failure set.
3. `SC072` later breaks across `SC073` with 24 rows taking `-æ` outputs instead of live `-e` outcomes.
4. `SC078` earlier breaks across `SC070` with another 87-row `-en` failure set.

These cards should support later chronology prose, but the prose must not flatten them into single-lexeme adjacency claims. The index marks these sides in `broad_boundary_side` so they can be filtered during later chapter drafting.

## Runner-bounded / no-break sides

Two card sides are not historical first-break boundaries:

1. `SC050` earlier is **blocked by runner limitation**. The runner can move safely down to order `13`, then enters bundled `PWGmcChanges`, so no earlier historical boundary has yet been detected.
2. `SC056` later is a **no-break-before-runner-boundary** result. The runner finds no later real break through last safe order `86`, then stops at the `SC087` corridor without detecting a later historical boundary.

Both sides are now called out explicitly in the cards, the index, and the updated batch plan so later synthesis does not turn them into false must-precede / must-follow claims.

## Cards normalized in this pass

All existing chronology cards were reviewed against the current source TSVs. The card set already shared a common heading order:

1. `Current position`
2. `Earlier boundary`
3. `Later boundary`
4. `Chronology statement`
5. `Caveats`
6. `Source files`

This pass lightly normalized the prose by:

1. adding the directory README and TSV index;
2. preserving the concrete PGmc > expected OE vs variant OE examples already aligned to the failures TSV;
3. tightening broad-boundary wording in `SC041`, `SC047`, `SC048`, and `SC078`;
4. preserving explicit runner-bounded cautions in `SC050` and `SC056`.

## Issues for human review

The current card set is usable, but several issues still need care before these constraints are turned into chapter prose:

1. The 87-row broad failure sets (`SC047` later, `SC048` earlier, `SC078` earlier) need careful narrative treatment.
2. `SC041` earlier breaks far away at `SC020`, so the wording should stay broad and computational rather than local and adjacency-like.
3. `SC050` earlier is a runner-boundary result, not a historical boundary.
4. `SC056` later is a runner-boundary no-break result, not a historical boundary.
5. Cards that still use strong `must follow` / `must precede` wording around broad boundaries may need softer prose during chapter drafting even when the underlying first-break result is historical.

## Recommended next terminal batch

The next terminal batch should be chosen from `next_batch_candidates.tsv`, not ad hoc from the manifest. A good next consolidation-aware batch is the following nine-rule gap-filling set:

1. `SC049` PGmc B Allophony
2. `SC053` OE Post Velar W Loss
3. `SC054` OE W Loss Before I
4. `SC057` OE J Cluster Coalescence
5. `SC058` OE Nasal Dissimilation
6. `SC060` OE Ws Palatal Umlaut
7. `SC061` OE Weak Tail Nasal Loss
8. `SC064` NWGmc In Stem N Loss
9. `SC073` OE Unstressed AE Merger

That batch fills the largest remaining gaps immediately adjacent to already interpreted cards and should extend the current chronology network without yet jumping to an all-remaining run.

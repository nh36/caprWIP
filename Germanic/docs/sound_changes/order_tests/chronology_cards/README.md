# Chronology cards

Chronology cards are compact evidence summaries for individual sound changes that have already been tested with the first-break runner. Each card turns the runner output into prose-ready chronology evidence that can later be reused in the sound-change chapter.

## How to read a card

- **current order** is the rule's live position in the current `EnglishProtoToOE` cascade.
- **safe computational window** is the contiguous range of tested positions in which the rule can move without creating a new baseline-matching failure.
- **earlier boundary** and **later boundary** record the first tested move on each side that creates a real break.

The cards are meant to support chronology prose, not to replace the underlying TSV evidence. When a card says that a move fails, that statement should be recoverable from the summary and failures TSVs.

## What first-break means

A first-break boundary is the first tested earlier or later move where:

- the baseline derivation matches the expected Old English output; and
- the reordered variant no longer matches the expected Old English output.

Those newly failing rows define the stopping point. The cards therefore summarize the first **real** computational break, not just any changed derivation.

## What changed-still-passing means

Some reordered variants change an output while still matching the expected Old English form. Those rows are recorded in `order_sensitivity_first_break_pilot_03_changes.tsv`, but they do **not** count as first breaks and do not end the search. They still matter interpretively because they often show nearby instability or support-stage sensitivity.

## Runner-bounded cases

Not every tested side reaches a historical first-break boundary. Two special cases now exist in the card set:

- `SC050` earlier reaches the current runner limit inside bundled `PWGmcChanges`.
- `SC056` later finds no real break before the current search space ends at the `SC087` corridor.

Those sides are **runner-bounded**. They should not be rewritten as claims that the rule must precede or follow a specific historical stage. They only show that no real break was detected before the current runner boundary.

## How the cards support later prose

The cards are intended as reusable building blocks for the later sound-change write-up. Each card keeps the same section order, records concrete PGmc > expected OE vs variant OE contrasts, and notes whether a boundary is tight and local, broad and computational, reciprocal with another card, or runner-bounded. The index and consolidation report in this directory provide the cross-card view needed before those constraints are turned into chapter prose.

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

## What `+?` means

Some genuine first-break rows do not yield an alternate surface form at all. When the TSV writes the variant output as `+?`, the reordered derivation produced no output / failed derivation. Those rows still define real boundaries when the baseline matched and the variant stopped matching, but the prose should describe them as failed derivations rather than as competing Old English forms.

## Boundary-limited and non-historical cases

Not every tested side reaches an ordinary historical first-break boundary. The current card set now includes five non-ordinary patterns:

- earlier searches blocked by bundled `PWGmcChanges` with no real break (`SC035`, `SC037`, `SC039`, `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, `SC076`);
- real computational earlier breaks that only appear when the move crosses bundled `PWGmcChanges` (`SC031` earlier, `SC033` earlier);
- real computational later breaks that cross technical markers rather than ordinary historical sound changes (`SC037` later over `SC038`);
- later searches that find no real break before the current `SC087` search boundary (`SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, `SC086`);
- the terminal later search for `SC087`, which reaches the current runner limit beyond order `86` with no detected break.

Those sides are boundary-limited or non-historical. They should not be rewritten as claims that the rule must precede or follow a specific ordinary historical stage. They only show that no real break was detected before the current runner boundary, or that the first computational break crosses a bundled / technical stage that the current runner does not yet treat as an ordinary chronology target.

## How the cards support later prose

The cards are intended as reusable building blocks for the later sound-change write-up. Each card keeps the same section order, records concrete PGmc > expected OE vs variant OE contrasts, and notes whether a boundary is tight and local, broad and computational, reciprocal with another card, one-sided in current testing, non-historical because it crosses a bundled or technical stage, or runner-bounded. The index and consolidation report in this directory provide the cross-card view needed before those constraints are turned into chapter prose, including newer upper-early, late-corridor, and far-late reciprocal pairs such as `SC030` / `SC032`, `SC031` / `SC034`, `SC039` / `SC040`, `SC066` / `SC068`, `SC070` / `SC071`, `SC074` / `SC075`, `SC079` / `SC080`, `SC081` / `SC082`, `SC082` / `SC083`, and `SC085` / `SC086`.

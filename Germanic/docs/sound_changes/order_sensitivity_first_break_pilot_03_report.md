# Order-sensitivity first-break pilot 03 report

## Summary

The first-break pilot completed successfully for both target rules after the execution refactor made longer runs safe to perform from a normal terminal.

- target rules tested: `SC043` and `SC063`
- baseline counts: `380` rows tested, `373` expected matches, `7` expected failures
- identity validation used as prerequisite: **yes**
- first-break mode succeeded: **yes**
- SC043 first earlier break: order `42`, crossing `SC042` PWGmc Surviving Bimoric O Unrounding, failure `rest`
- SC043 first later break: order `44`, crossing `SC044` OE Breaking, failure `slay`
- SC063 first earlier break: order `55`, crossing `SC055` OE I Umlaut, `19` newly failing rows including `belly`, `birth`, `breeches`, `bride`, `cow`
- SC063 first later break: order `72`, crossing `SC072` OE Unstressed Long Vowel Shortening, failure `fright`

Files written:

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`

## Method

The runner starts from the validated live `EnglishProtoToOE` order, moves the target rule one slot at a time, compiles a temporary variant, and evaluates the 380-row Old English corpus against the live baseline.

A **real break** is the stopping condition:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

Changed outputs that still include the expected form are recorded in the changes TSV, but they do not stop the search. The live FST order is never edited; only temporary variants are compiled.

## SC043 Anglo Frisian Brightening

Current order: `43`.

The pilot found the first earlier break immediately:

- first earlier break: order `42`
- crossed stage: `SC042` PWGmc Surviving Bimoric O Unrounding
- newly failing lexeme: `rest`

It also found the first later break immediately:

- first later break: order `44`
- crossed stage: `SC044` OE Breaking
- newly failing lexeme: `slay`

No further movement was needed once those breaks appeared. This matches the dossier-level expectation that brightening must precede breaking, and it also fits the literature-backed relation between early fronting and later restoration / retraction.

## SC063 OE High Vowel Apocope

Current order: `63`.

The pilot crossed the adjacent technical / support neighborhood safely before it found real breaks:

- one-step earlier across `SC062` OE Weight Markers: no real break
- one-step later across `SC064` NWGmc In Stem N Loss: no real break

The first earlier real break occurred at order `55`:

- crossed stage: `SC055` OE I Umlaut
- newly failing rows: `19`
- representative failures: `belly`, `birth`, `breeches`, `bride`, `cow`

The first later real break occurred at order `72`:

- crossed stage: `SC072` OE Unstressed Long Vowel Shortening
- newly failing row: `fright`

Both break points are historically interpretable rather than merely technical. They fit the dossier expectation that SC063 belongs after earlier i-umlaut / syncope-related developments but before the later unstressed-vowel shortening and reduction stages.

## Technical/support-stage caveats

The pilot did cross non-final non-reader-facing stages while searching for the SC063 break points, but the first actual break in neither direction landed on a technical marker or support stage.

- `SC062` OE Weight Markers was crossed safely and therefore does not itself supply chronology evidence.
- `SC064` NWGmc In Stem N Loss was also crossed safely in the later direction before the eventual break at `SC072`.

That means the reported first-break boundaries for this pilot are historical-stage constraints, not merely implementation artifacts.

## Files changed

- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv` — direction-level first-break summary for `SC043` and `SC063`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv` — row-level changed outputs for each tested variant up to the break
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv` — failure-only rows where a previously matching baseline row became non-matching
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv` — updated repo-facing summary for `SC043` and `SC063`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_pilot_03_report.md` — this narrative report

## Recommended next task

**A. Run first-break testing for a small batch of high-priority non-bundled rules.**

The method now works cleanly on both a rule with immediate adjacent breaks (`SC043`) and a rule whose first real break appears only after several safe crossings (`SC063`), so the next useful step is to extend the same focused test to a small batch of additional reader-facing non-bundled stages.

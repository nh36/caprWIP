# SC002-SC003 chronology harness 01

## Mature workflow inspected

The current chronology-card workflow was inspected through:

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC014-nwgmc-unstressed-ai-monophthongization.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC015-nwgmc-i-lowering.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC040-oe-med-unstressed-u-lowering.md`
4. `Germanic/tools/sound_change_order_sensitivity.py`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
6. `Germanic/docs/sound_changes/order_tests/chronology_card_template_04.md`
7. `Germanic/fsts/old_english_sandbox.txt`

## What generates mature chronology evidence

### Underlying TSV/order-test evidence

The validated cards depend on the first-break TSV layer written by:

`Germanic/tools/sound_change_order_sensitivity.py`

The mature cards inspected all cite the same source family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
4. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`

### Card generation itself

No dedicated markdown-card generator script was recovered for the existing `SC*.md` chronology cards. The inspected workflow shows:

1. `sound_change_order_sensitivity.py` generates the summary, changes, and failures TSV evidence.
2. The markdown card files are written to the existing card template and cite those TSVs directly.
3. Post hoc graph/index tooling such as `Germanic/docs/sound_changes/order_tests/chronology_graph/build_first_break_graph.py` consumes the card/index layer after the cards already exist; it does not generate the cards themselves.

## How mature cards derive their fields

### Safe computational window

In `sound_change_order_sensitivity.py`, `run_first_break()` tracks a `safe_order` while it steps one move at a time. When a real break is found, the last safe order is encoded in the summary row notes via `last_safe_order=...`.

In card terms, the mature examples show the same logic:

1. current order = live inventory order for the rule;
2. first earlier break and first later break define the first failing move on each side;
3. the safe computational window is the contiguous range between those failing moves or, where no break is found, to the runner boundary.

### First earlier break / first later break

`run_first_break()` stops only when it sees a **real break**:

1. baseline row matches expected Old English form; and
2. reordered variant no longer matches expected.

The first such failure row becomes the earlier or later break. If the search hits the edge of the tested order with no break, the summary row is written as `no_break_before_boundary`.

### Representative failures and wrong-output diagnostics

The summary TSV stores compact representatives via:

1. `representative_changed_lexemes`
2. `representative_new_failures`

The detailed wrong outputs come from the failures TSV rows written per tested variant, which preserve:

1. Proto-Germanic input form
2. expected Old English output
3. variant output or `+?` for no output
4. crossed stage metadata

### Validated status values

The runner treats these summary results as terminal:

- `first_break_found`
- `no_break_before_boundary`
- `compile_failure`
- `blocked_by_runner_limitation`
- `ambiguous_needs_review`

The markdown cards themselves use the visible status convention:

- `status: first_break_complete`

for validated cards.

## Exact blocker for SC002-SC003

SC002 and SC003 are blocked by the current runner architecture in two precise ways.

1. In `Germanic/fsts/germanic.txt`, both rules are hidden inside the bundled stage:

   ```text
   define PGmcConsonantRules PGmcGmSimplification
       .o. PGmcRhotacism;
   ```

2. In `Germanic/tools/sound_change_order_sensitivity.py`, the normal runner only parses and reorders the explicit `EnglishProtoToOE` chain via `parse_english_proto_to_oe_order()`.

That means:

- SC002 and SC003 are present in `sound_change_inventory.tsv`;
- they are marked `historical_sound_change` and `include_in_volume=yes`;
- but they are **not** exposed as reorderable top-level stages in the normal runner;
- and `run_first_break()` requires the target rule name to appear in the parsed live order.

The skip is already recorded in:

`Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv`

where SC002 and SC003 are marked `explicit_chain_member=no` and `skipped`.

## Temporary harness strategy

The temporary harness created in this pass is:

`Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py`

It does **not** change the production FST cascade. Instead it:

1. reads the explicit split order already mirrored in `Germanic/fsts/old_english_sandbox.txt`;
2. builds a temporary full explicit cascade beginning with `EnglishProtoInput` and then composing every split rule one by one, including `PGmcGmSimplification` and `PGmcRhotacism`;
3. reuses the existing evaluation and TSV-writing logic from `sound_change_order_sensitivity.py`;
4. writes first-break summary/changes/failures TSVs to a separate early-rule output family.

This is the preferred temporary expanded-cascade approach rather than a production-cascade edit.

## Expected output files

The harness writes to:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

## Current state

1. The harness exists and supports SC002 and SC003.
2. The exact manual commands to run it are documented in `run_sc002_003_first_breaks_README.md`.
3. Lightweight dry runs succeeded for both targets: SC002 resolved to the left edge of the explicit chain with witnesses `dream, team`, and SC003 resolved immediately after it with witnesses `deer, hoard, learn, berry, learn (3sg)`.
4. No production FST file was changed.
5. No validated SC002/SC003 chronology cards were created in this pass.

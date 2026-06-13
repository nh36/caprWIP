# SC002-SC003 chronology harness 01 report

## Mature chronology workflow inspected

The following mature card examples and support files were inspected:

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC014-nwgmc-unstressed-ai-monophthongization.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC015-nwgmc-i-lowering.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC040-oe-med-unstressed-u-lowering.md`
4. `Germanic/tools/sound_change_order_sensitivity.py`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
6. `Germanic/docs/sound_changes/order_tests/chronology_card_template_04.md`
7. `Germanic/fsts/old_english_sandbox.txt`

## How mature cards connect to TSV/order-test output

1. Mature cards cite the three `order_sensitivity_first_break_pilot_03` TSVs plus `sound_change_order_sensitivity.tsv`.
2. `sound_change_order_sensitivity.py` generates the underlying summary, changes, and failures TSVs.
3. No dedicated markdown-card generator script was recovered; the cards are written to the standard template using the TSV evidence.
4. Post hoc tooling such as `chronology_graph/build_first_break_graph.py` reads the card/index layer after the cards already exist.

## Exact blocker for SC002-SC003

1. SC002 and SC003 are hidden inside `PGmcConsonantRules` in `Germanic/fsts/germanic.txt`.
2. The normal order-sensitivity runner only parses and reorders `EnglishProtoToOE`.
3. `run_first_break()` in `Germanic/tools/sound_change_order_sensitivity.py` requires the target rule name to appear in that parsed live order.
4. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv` already records the result as `explicit_chain_member=no` and `skipped`.

## Harness created

Created:

1. `Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py`
2. `Germanic/docs/sound_changes/order_tests/run_sc002_003_first_breaks_README.md`
3. `Germanic/docs/sound_changes/order_tests/sc002_003_chronology_harness_01.md`

The harness builds a temporary explicit cascade from the already split order in `old_english_sandbox.txt` and reuses the existing TSV-writing logic from `sound_change_order_sensitivity.py`.

## Production FST changes

1. No production FST file was changed.
2. The harness uses temporary appended variant definitions only.

## Dry-run result

Lightweight dry runs are now available through:

```bash
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC002 --dry-run
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC003 --dry-run
```

Observed dry-run results in this pass:

1. `SC002` resolved to inventory order `2`, explicit-chain position `1`, earlier boundary `START_OF_EXPLICIT_CHAIN`, later neighbor `PGmcRhotacism`, witness candidates `dream, team`, corpus rows `380`, and temporary expanded-cascade construction succeeded.
2. `SC003` resolved to inventory order `3`, explicit-chain position `2`, earlier neighbor `PGmcGmSimplification`, later neighbor `PWGmcAiMonophthongization`, witness candidates `deer, hoard, learn, berry, learn (3sg)`, corpus rows `380`, and temporary expanded-cascade construction succeeded.

The heavy search was **not** run. The dry-run path validates:

1. imports;
2. target lookup in the inventory;
3. explicit early-rule order recovery from `old_english_sandbox.txt`;
4. witness selection from the inventory;
5. temporary expanded-cascade construction without compilation or full search.

## Heavy-computation status

1. Heavy first-break computation was **not** run in this pass.
2. The existing early-rule runner still has potentially heavy compile/evaluate cost across a long explicit cascade, so the full search is left for Nathan to run manually in a separate terminal.

## Exact commands for Nathan

See:

`Germanic/docs/sound_changes/order_tests/run_sc002_003_first_breaks_README.md`

The full commands are:

```bash
cd /Users/nathanhill/Code/capr-v3-working
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC002 --direction both --resume
python3 Germanic/docs/sound_changes/order_tests/run_early_rule_first_breaks.py --change SC003 --direction both --resume
```

## Expected output files from Nathan's run

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

## Validated SC002-SC003 cards

1. No validated SC002-SC003 chronology cards were created in this pass.
2. The existing SC002/SC003 cards remain draft-only.

## What remains before validated cards can be created

1. Nathan must run the heavy first-break harness successfully.
2. The resulting TSV outputs must show real terminal results for earlier/later directions.
3. Only then can the draft chronology cards be replaced with validated cards carrying real safe windows, break stages, representative failures, and wrong-output diagnostics.

## Reader-facing and manifest status

1. No reader-facing chapters were created in this pass.
2. `report_manifest.tsv` was not updated.

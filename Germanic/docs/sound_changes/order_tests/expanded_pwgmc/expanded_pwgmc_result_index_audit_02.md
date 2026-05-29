# Expanded PWGmc result index audit 02

## Scope

This audit checks the separate expanded-PWGmc result layer after the index grew to thirty-nine earlier-side rows:

1. `SC014` through `SC037` earlier, excluding technical marker `SC038`
2. `SC039` through `SC049` earlier
3. `SC053` earlier
4. `SC054` earlier
5. `SC057` earlier
6. `SC058` earlier

Files checked:

1. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/README.md`
2. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_result_index.tsv`
3. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_result_index_notes.md`
4. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_SC020_SC029_minibatch_03.md`
5. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_SC030_SC040_minibatch_04.md`
6. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_SC041_SC048_minibatch_05.md`
7. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_SC049_SC058_minibatch_06.md`
8. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc_early_minibatch_02.md`
9. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
10. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
11. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

The older early mini-batch note still remains at the order-tests root rather than inside `expanded_pwgmc/`, so the audit checked that file in its current location.

## Audit result

The audit passes.

One small prose correction was made while auditing: the root `expanded_pwgmc_early_minibatch_02.md` note now states more explicitly that this layer does not revise the default chronology cards, default first-break TSVs, or default graph files. No data rows and no default-profile artifacts were changed.

## 1. Row count and coverage

`expanded_pwgmc_result_index.tsv` contains exactly `39` data rows.

Coverage matches the intended current layer exactly:

1. `SC014` through `SC037` earlier, excluding `SC038`
2. `SC039` through `SC049` earlier
3. `SC053` earlier
4. `SC054` earlier
5. `SC057` earlier
6. `SC058` earlier

No duplicate `(change_id, direction, order_profile)` rows were found.

## 2. Source TSV consistency

Every indexed row agrees with `order_sensitivity_first_break_expanded_pwgmc_01.tsv` for all audited fields:

1. `change_id`
2. `display_name`
3. `rule_name`
4. `baseline_order`
5. `direction`
6. `result`
7. `first_break_variant_id`
8. `first_break_order`
9. `crossed_change_id`
10. `crossed_display_name`
11. `crossed_rule_name`
12. `crossed_entry_type`
13. `variants_tested_before_break`
14. `changed_output_count_at_break`
15. `newly_failing_count_at_break`
16. `representative_changed_lexemes`
17. `representative_new_failures`
18. `notes`

No source/data mismatches were found.

## 3. Controlled vocabulary

The index uses only the intended controlled vocabulary.

`profile_interpretation` values present:

1. `strengthened_negative_evidence`
2. `confirms_default_local_break`
3. `confirms_default_broad_far_break`
4. `expanded_internal_pwgmc_break`

`default_profile_relation` values present:

1. `refines_default_pwgmc_boundary`
2. `matches_default_card`

`integration_status` values present:

1. `expanded_only_pending_policy`

## 4. Category sanity check

The interpretation classes remain internally consistent.

1. `strengthened_negative_evidence` appears only on `no_break_before_boundary` rows that reach `SC004` with `0` changed outputs and `0` new failures.
2. `expanded_internal_pwgmc_break` is still used only for:
   - `SC031` earlier across `SC011`
   - `SC033` earlier across `SC008`
3. `confirms_default_local_break` remains restricted to local or adjacent default-profile confirmations.
4. `confirms_default_broad_far_break` is used for the expected broad/far or non-local confirmations:
   - `SC036` across `SC019`
   - `SC041` across `SC020`
   - `SC042` across `SC020`
   - `SC046` across `SC043`
   - `SC047` across `SC034`
   - `SC049` across `SC037`
   - `SC054` across `SC020`
   - `SC057` across `SC052`

## 5. Failure examples

Representative positive-break failures in the index agree with the committed failures TSV.

Newest mini-batch rows checked:

1. `SC049`: `rainbow`
2. `SC054`: `sea`
3. `SC057`: `bow`; `follow`; `hedge`; `seek`; `singe`

Previously audited rows re-checked:

1. `SC017`: `yoke`
2. `SC019`: `nose`; `shovel`; `sorrow`
3. `SC020`: `rest`
4. `SC027`: `fist`; `goose`; `youth`
5. `SC030`: `hay`; `strew`
6. `SC031`: `hay`
7. `SC032`: `believe`; `bow`; `bread`; `dream`; `flea`
8. `SC033`: `four`
9. `SC034`: `dew`; `hew`
10. `SC036`: `soul`
11. `SC040`: `widow`
12. `SC041`: `beard`; `bosom`; `bottom`; `calf`; `coat`
13. `SC042`: `rest`
14. `SC043`: `rest`
15. `SC044`: `slay`
16. `SC045`: `fee`; `fight`; `flax`; `knight`; `laugh`
17. `SC046`: `bake`; `fare`; `flask`; `grave`; `haw`
18. `SC047`: `straw`
19. `SC048`: `bake`; `begin`; `believe`; `bind`; `bore`

All checked representative failures are present in `order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`.

## 6. Prose consistency

The checked expanded-PWGmc notes consistently state the intended policy after the small root-note wording fix:

1. expanded-profile evidence remains separate from the default 70-card corpus;
2. this layer does not revise default chronology cards, default first-break TSVs, or default graph files;
3. later-direction expanded-profile testing is still not recommended.

## 7. Recommendation

Because the audit passes, the next manual expanded-profile run can proceed with `SC060` through `SC076` earlier only, but it should stay split into smaller chunks.

Recommended starting split:

1. chunk A: `SC060`, `SC061`, `SC064`
2. chunk B: `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`
3. chunk C: `SC073`, `SC074`, `SC075`, `SC076`

That split can still be adjusted if manifest eligibility or technical markers suggest a cleaner boundary, but no later-direction expanded-profile testing is recommended from this layer.

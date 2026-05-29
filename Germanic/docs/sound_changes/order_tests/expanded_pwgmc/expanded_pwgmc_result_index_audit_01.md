# Expanded PWGmc result index audit 01

## Scope

This audit checks the separate expanded-PWGmc result layer after the indexed earlier-side coverage reached twenty-six rows:

1. `SC014` through `SC037` earlier, excluding technical marker `SC038`
2. `SC039` earlier
3. `SC040` earlier

Files checked:

1. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/README.md`
2. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_result_index.tsv`
3. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_result_index_notes.md`
4. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc_early_minibatch_02.md`
5. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_SC020_SC029_minibatch_03.md`
6. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_SC030_SC040_minibatch_04.md`
7. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
8. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
9. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

The early mini-batch note is still stored at the order-tests root rather than inside `expanded_pwgmc/`; the audit checked the existing file in that current location.

## Audit result

The audit passes after two small documentation/data corrections made during the audit itself:

1. `expanded_pwgmc_result_index.tsv` now matches the committed summary TSV exactly in the `notes` field for all indexed rows.
2. The README / notes prose now states more consistently that this expanded-profile layer does not revise the default 70-card corpus, the default first-break TSV corpus, or the default graph export, and that later-direction expanded-profile testing is still not recommended.

## 1. Row count and coverage

`expanded_pwgmc_result_index.tsv` now contains exactly `26` data rows.

Coverage matches the intended current layer exactly:

1. `SC014` through `SC037` earlier, excluding `SC038`
2. `SC039` earlier
3. `SC040` earlier

No duplicate `(change_id, direction, order_profile)` rows were found.

## 2. Source TSV consistency

After the `notes`-field correction, every indexed row agrees with `order_sensitivity_first_break_expanded_pwgmc_01.tsv` for all audited fields:

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

## 3. Controlled vocabulary

The index now uses only the intended controlled vocabulary.

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

The category assignments are internally consistent.

1. `strengthened_negative_evidence` appears only on `no_break_before_boundary` rows that reach `SC004` with `0` changed outputs and `0` new failures.
2. `confirms_default_local_break` is used only for default-profile local confirmations.
3. `confirms_default_broad_far_break` is used only for `SC036` earlier across `SC019`.
4. `expanded_internal_pwgmc_break` is used only for:
   - `SC031` earlier across `SC011`
   - `SC033` earlier across `SC008`

## 5. Failure examples

Representative positive-break failures in the index agree with the committed failures TSV.

Checked rows:

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

All checked representative failures are present in `order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`.

## 6. Prose consistency

The checked expanded-PWGmc notes now consistently state the intended policy:

1. expanded-profile evidence remains separate from the default 70-card corpus;
2. this layer does not revise default chronology cards, default first-break TSVs, or default graph files;
3. later-direction expanded-profile testing is still not recommended.

## 7. Recommendation

Because the audit now passes, the next manual expanded-profile run should remain:

1. `SC041` through `SC048` earlier only

Before any larger expansion or any policy discussion about integration into ordinary chronology cards / graph layers, continue updating this separate expanded-profile index after each mini-batch.

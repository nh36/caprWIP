# Expanded PWGmc smoke pilot 01

## Command / result summary

Nathan manually ran one real expanded-profile first-break smoke pilot for:

- `change_id`: `SC014`
- `display_name`: `NWGmc Unstressed Ai Monophthongization`
- `direction`: `earlier`
- `order_profile`: `expanded-pwgmc`

Observed summary result:

1. `result = no_break_before_boundary`
2. `variants_tested_before_break = 10`
3. crossed boundary: `SC004` `PWGmc Ai Monophthongization`
4. `last_safe_order = 4`
5. `compilation_status = compiled`
6. `total_rows_tested = 380`
7. `baseline_matches = 373`
8. `variant_matches_at_break = 373`
9. `changed_output_count_at_break = 0`
10. `newly_failing_count_at_break = 0`

## Files written

The manual smoke run wrote only the separate expanded-profile output files:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

No default-profile first-break TSVs were modified for this documentation pass.

## Validation summary

All three TSVs are structurally valid:

1. summary TSV: valid header, `23` columns, `1` data row
2. changes TSV: valid header, `18` columns, `0` data rows
3. failures TSV: valid header, `15` columns, `0` data rows

This means the smoke result is not only negative in content, but also clean at the file-structure level: there were no changed-output rows and no newly failing rows to record.

## Interpretation of `SC014` earlier

Under the default bundled profile, `SC014` earlier stopped at the opaque `PWGmcChanges` boundary. Under the expanded profile, the same earlier probe now traverses the internal PWGmc corridor explicitly across `SC013` through `SC004`.

For this smoke pilot, moving `SC014` earlier across that full expanded corridor produced **no changed outputs** and **no newly failing rows**. This is therefore a stronger negative result than the older bundled-boundary result: the expanded profile no longer says only “blocked by `PWGmcChanges`”, but instead shows that this specific earlier-side probe can cross the exposed PWGmc component sequence without finding a real first break.

## Profile warning

This result belongs to the **expanded-PWGmc profile**. It should not overwrite, silently revise, or be folded directly into the current 70-card default-profile corpus. Any future reuse must continue to label it as expanded-profile evidence until the repository explicitly decides how expanded-profile results should interact with default-profile chronology documentation.

## Recommendation for the next step

Do **not** run a large expanded batch yet. The next safe computational step is a **small manually run early earlier-side batch**, probably `SC015` through `SC019` earlier only, using the same separate expanded-profile output files (with resume support if needed). For this task, the result is only documented; no chronology card or corpus-wide reinterpretation is made yet.

# Expanded PWGmc final boundary targets 07

## Scope

Nathan manually ran the final four true remaining bundled-`PWGmcChanges` earlier-side targets under the expanded-PWGmc profile:

1. `SC050` earlier
2. `SC065` earlier
3. `SC067` earlier
4. `SC076` earlier

These runs are the last unresolved rows from the narrow earlier-side bundled-PWGmc boundary-target list.

## Files used

This closure batch is documented from the committed expanded-profile summary TSV:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`

No new rows were added to the companion expanded-profile changes or failures TSVs, because all four rows reached `SC004` with `0` changed outputs and `0` new failures.

## Summary table

| change_id | direction | result | crossed boundary | variants tested | changed outputs | new failures | profile interpretation | note |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| `SC050` | earlier | `no_break_before_boundary` | `SC004` `PWGmc Ai Monophthongization` | 46 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break; last_safe_order=4 |
| `SC065` | earlier | `no_break_before_boundary` | `SC004` `PWGmc Ai Monophthongization` | 61 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break; last_safe_order=4 |
| `SC067` | earlier | `no_break_before_boundary` | `SC004` `PWGmc Ai Monophthongization` | 63 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break; last_safe_order=4 |
| `SC076` | earlier | `no_break_before_boundary` | `SC004` `PWGmc Ai Monophthongization` | 72 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break; last_safe_order=4 |

## Interpretation

All four final true bundled-PWGmc boundary targets resolve the same way:

1. no internal PWGmc first break is exposed;
2. the search reaches `SC004` cleanly;
3. no changed outputs or new failures appear.

So these runs strengthen the negative side of the expanded-PWGmc picture rather than adding new positive internal boundaries.

That matters because it completes the narrow earlier-side bundled-PWGmc boundary-target problem: every default-profile earlier row that previously stopped at opaque bundled `PWGmcChanges` now has an expanded-PWGmc answer.

## Result within the larger expanded layer

The broader expanded-PWGmc index still contains local and broad/far confirmations from the earlier exploratory mini-batches, but those are **not** what makes the boundary-target task complete.

What closes the narrow task is:

1. the two specific internal positive breaks already found earlier:
   - `SC031` earlier across `SC011` `PWGmc Syllabic J`
   - `SC033` earlier across `SC008` `PWGmc Coronal W Assimilation`
2. the fact that the remaining bundled-boundary cases, including these final four, all resolve as stronger no-break-to-`SC004` evidence.

## Scope warning

This note closes only the **earlier-side bundled-PWGmc boundary-target** task.

It does **not** claim that the whole chronology is finished, and it does **not** imply that later-direction expanded-profile testing should begin automatically.

Later-direction expanded-profile testing remains out of scope unless a separate question is explicitly posed.

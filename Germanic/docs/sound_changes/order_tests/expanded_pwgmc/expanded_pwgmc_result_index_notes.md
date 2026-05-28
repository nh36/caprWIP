# Expanded PWGmc result index notes

## Why this index exists

The expanded-PWGmc runner profile now produces results that are useful for chronology interpretation, but those results should not be folded ad hoc into the default bundled-profile chronology-card system. This index exists to accumulate expanded-profile tested directions in a separate review layer until the repository decides on a formal integration policy.

## Current entries

The index currently contains sixteen entries:

1. `SC014` earlier
2. `SC015` earlier
3. `SC016` earlier
4. `SC017` earlier
5. `SC018` earlier
6. `SC019` earlier
7. `SC020` earlier
8. `SC021` earlier
9. `SC022` earlier
10. `SC023` earlier
11. `SC024` earlier
12. `SC025` earlier
13. `SC026` earlier
14. `SC027` earlier
15. `SC028` earlier
16. `SC029` earlier

## Two interpretation classes

The current rows fall into two intentionally different categories.

### `strengthened_negative_evidence`

This label is used when the expanded profile improves on a former bundled `PWGmcChanges` boundary by exposing the internal PWGmc corridor and still finding no real break.

That is the current interpretation for:

1. `SC014` earlier
2. `SC015` earlier
3. `SC016` earlier
4. `SC018` earlier
5. `SC021` earlier
6. `SC022` earlier
7. `SC023` earlier
8. `SC024` earlier
9. `SC025` earlier
10. `SC026` earlier
11. `SC028` earlier
12. `SC029` earlier

These twelve probes now traverse the exposed PWGmc corridor down to `SC004` `PWGmc Ai Monophthongization` without changed outputs or newly failing rows.

### `confirms_default_local_break`

This label is used when the expanded profile reaches the same local first break already visible in the default bundled-profile chronology before it ever reaches the exposed PWGmc corridor.

That is the current interpretation for:

1. `SC017` earlier, which still breaks immediately across `SC016` `OE Ws Palatal Glide`
2. `SC019` earlier, which still breaks across `SC017` `NWGmc U Lowering`
3. `SC020` earlier, which still breaks across `SC019` `NWGmc Final Long O Raising`
4. `SC027` earlier, which still breaks across `SC026` `NWGmc Nasal Spirant Lengthening`

So the expanded profile is not creating a new deeper PWGmc-corridor story for those four rules; it is confirming the same local chronology relations already visible in the default-profile card layer.

## SC020-SC029 mini-batch update

The `SC020` through `SC029` earlier-side mini-batch again split into the same two result classes:

1. `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, and `SC029` strengthened formerly bundled boundary-limited results by traversing the exposed PWGmc corridor down to `SC004` with no changed outputs and no newly failing rows.
2. `SC020` and `SC027` confirmed default-profile local breaks before the search could reach that PWGmc corridor:
   - `SC020` earlier still breaks across `SC019`, with `rest` as the concrete failure.
   - `SC027` earlier still breaks across `SC026`, with `fist`, `goose`, and `youth` as the concrete failures.

Those positive breaks match default-profile local constraints, but they remain indexed here as expanded-profile results rather than being folded into the default 70-card corpus automatically.

## Integration status

All sixteen rows currently carry `integration_status = expanded_only_pending_policy`.

That means:

1. the results are committed and reviewable;
2. the results may refine or confirm default-profile interpretations;
3. the repository has **not** yet decided how expanded-profile evidence should enter the default chronology-card/index system.

## Recommended next step

With this index in place, the next manual computational batch can be `SC030` through `SC040` earlier only, reusing the same expanded-PWGmc TSV outputs with `--resume`.

Before that computation, keep using this separate expanded-profile index as the review layer rather than mixing expanded evidence directly into the default 70-card chronology-card corpus.

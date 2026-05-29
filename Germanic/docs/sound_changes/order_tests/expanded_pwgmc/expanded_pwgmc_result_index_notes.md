# Expanded PWGmc result index notes

## Why this index exists

The expanded-PWGmc runner profile now produces results that are useful for chronology interpretation, but those results should not be folded ad hoc into the default bundled-profile chronology-card system. This index exists to accumulate expanded-profile tested directions in a separate review layer until the repository decides on a formal integration policy.

## Current entries

The index currently contains twenty-six entries:

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
17. `SC030` earlier
18. `SC031` earlier
19. `SC032` earlier
20. `SC033` earlier
21. `SC034` earlier
22. `SC035` earlier
23. `SC036` earlier
24. `SC037` earlier
25. `SC039` earlier
26. `SC040` earlier

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
13. `SC035` earlier
14. `SC037` earlier
15. `SC039` earlier

These fifteen probes now traverse the exposed PWGmc corridor down to `SC004` `PWGmc Ai Monophthongization` without changed outputs or newly failing rows.

### `confirms_default_local_break`

This label is used when the expanded profile reaches the same local first break already visible in the default bundled-profile chronology before it ever reaches the exposed PWGmc corridor.

That is the current interpretation for:

1. `SC017` earlier, which still breaks immediately across `SC016` `OE Ws Palatal Glide`
2. `SC019` earlier, which still breaks across `SC017` `NWGmc U Lowering`
3. `SC020` earlier, which still breaks across `SC019` `NWGmc Final Long O Raising`
4. `SC027` earlier, which still breaks across `SC026` `NWGmc Nasal Spirant Lengthening`
5. `SC030` earlier, which still breaks across `SC029` `OE Awj Glide Formation`
6. `SC032` earlier, which still breaks across `SC030` `OE Au Fronting`
7. `SC034` earlier, which still breaks across `SC031` `OE WW Simplification`
8. `SC040` earlier, which still breaks across `SC039` `OE WI Combinative U Umlaut`

So the expanded profile is not creating a new deeper PWGmc-corridor story for those eight rules; it is confirming the same local chronology relations already visible in the default-profile card layer.

## `confirms_default_broad_far_break`

This label is used when the expanded profile confirms a broader default-profile chronology relation before the search reaches the exposed PWGmc corridor.

That is the current interpretation for:

1. `SC036` earlier, which still breaks across `SC019` `NWGmc Final Long O Raising`

So far this is the only expanded-profile row that clearly lands in the broad/far confirmation class rather than the tighter local-break class.

## SC020-SC029 mini-batch update

The `SC020` through `SC029` earlier-side mini-batch again split into the same two result classes:

1. `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, and `SC029` strengthened formerly bundled boundary-limited results by traversing the exposed PWGmc corridor down to `SC004` with no changed outputs and no newly failing rows.
2. `SC020` and `SC027` confirmed default-profile local breaks before the search could reach that PWGmc corridor:
   - `SC020` earlier still breaks across `SC019`, with `rest` as the concrete failure.
   - `SC027` earlier still breaks across `SC026`, with `fist`, `goose`, and `youth` as the concrete failures.

Those positive breaks match default-profile local constraints, but they remain indexed here as expanded-profile results rather than being folded into the default 70-card corpus automatically.

## SC030-SC040 mini-batch update

The `SC030` through `SC040` earlier-side mini-batch split into three result classes:

1. `SC030`, `SC032`, `SC034`, and `SC040` confirmed default-profile local breaks, while `SC036` confirmed a default-profile broad/far break.
2. `SC031` and `SC033` produced the first clearly useful **expanded internal-PWGmc breaks**, landing on `SC011` `PWGmc Syllabic J` and `SC008` `PWGmc Coronal W Assimilation` respectively.
3. `SC035`, `SC037`, and `SC039` strengthened formerly bundled boundary-limited results by traversing the exposed PWGmc corridor down to `SC004` with no changed outputs and no newly failing rows.

`SC031` and `SC033` are especially important because they are the first cases where opening `PWGmcChanges` yields a more specific positive internal boundary than the default bundled profile could provide.

Even so, these results still remain separate from the default 70-card corpus pending an explicit integration policy.

## Integration status

All twenty-six rows currently carry `integration_status = expanded_only_pending_policy`.

That means:

1. the results are committed and reviewable;
2. the results may refine or confirm default-profile interpretations;
3. the repository has **not** yet decided how expanded-profile evidence should enter the default chronology-card/index system.

## Recommended next step

With this index in place, the next manual computational step is either:

1. a short audit of the expanded-profile index, now that the separate review layer is becoming more substantial; or
2. the next manual mini-batch for `SC041` through `SC048` earlier only, reusing the same expanded-PWGmc TSV outputs with `--resume`.

Do not move to later-direction expanded-profile testing yet, and keep using this separate expanded-profile index as the review layer rather than mixing expanded evidence directly into the default 70-card chronology-card corpus.

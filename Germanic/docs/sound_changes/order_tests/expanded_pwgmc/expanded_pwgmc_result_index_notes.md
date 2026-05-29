# Expanded PWGmc result index notes

## Why this index exists

The expanded-PWGmc runner profile now produces results that are useful for chronology interpretation, but those results should not be folded ad hoc into the default bundled-profile chronology-card system. This index exists to accumulate expanded-profile tested directions in a separate review layer until the repository decides on a formal integration policy.

That means this layer does **not** itself revise the default 70-card chronology-card corpus, the default first-break summary/change/failure TSV corpus, or the default graph export.

## Current entries

The index currently contains thirty-nine entries:

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
27. `SC041` earlier
28. `SC042` earlier
29. `SC043` earlier
30. `SC044` earlier
31. `SC045` earlier
32. `SC046` earlier
33. `SC047` earlier
34. `SC048` earlier
35. `SC049` earlier
36. `SC053` earlier
37. `SC054` earlier
38. `SC057` earlier
39. `SC058` earlier

## Interpretation classes

The current rows now fall into four intentionally different categories.

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
16. `SC053` earlier
17. `SC058` earlier

These seventeen probes now traverse the exposed PWGmc corridor down to `SC004` `PWGmc Ai Monophthongization` without changed outputs or newly failing rows.

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
9. `SC043` earlier, which still breaks across `SC042` `PWGmc Surviving Bimoric O Unrounding`
10. `SC044` earlier, which still breaks across `SC043` `Anglo Frisian Brightening`
11. `SC045` earlier, which still breaks across `SC044` `OE Breaking`
12. `SC048` earlier, which still breaks across `SC047` `OE Heavy Syllable Nasal Apocope`

So the expanded profile is not creating a new deeper PWGmc-corridor story for those twelve rules; it is confirming the same local chronology relations already visible in the default-profile card layer.

### `confirms_default_broad_far_break`

This label is used when the expanded profile confirms a broader default-profile chronology relation before the search reaches the exposed PWGmc corridor.

That is the current interpretation for:

1. `SC036` earlier, which still breaks across `SC019` `NWGmc Final Long O Raising`
2. `SC041` earlier, which still breaks across `SC020` `PGmc Final Z Deletion`
3. `SC042` earlier, which still breaks across `SC020` `PGmc Final Z Deletion`
4. `SC046` earlier, which still breaks across `SC043` `Anglo Frisian Brightening`
5. `SC047` earlier, which still breaks across `SC034` `OE Aw Long Diphthong`
6. `SC049` earlier, which still breaks across `SC037` `OE Compound Linking Syncope`
7. `SC054` earlier, which still breaks across `SC020` `PGmc Final Z Deletion`
8. `SC057` earlier, which still breaks across `SC052` `OE Velar Palatalization`

These should be read as broader or non-local chronology confirmations, not as tight local-adjacency evidence.

### `expanded_internal_pwgmc_break`

This label is used when the expanded profile finds a more specific positive boundary **inside** the corridor that was previously bundled inside `PWGmcChanges`.

That is the current interpretation for:

1. `SC031` earlier, which now breaks across `SC011` `PWGmc Syllabic J`
2. `SC033` earlier, which now breaks across `SC008` `PWGmc Coronal W Assimilation`

These are the first currently indexed cases where opening `PWGmcChanges` gives a more informative positive internal PWGmc boundary than the default bundled profile could expose.

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

## SC041-SC048 mini-batch update

The `SC041` through `SC048` earlier-side mini-batch has a different profile from the earlier expanded-PWGmc batches:

1. all eight rows are positive `first_break_found` rows;
2. no new `strengthened_negative_evidence` cases appear in this batch;
3. no new `expanded_internal_pwgmc_break` cases appear in this batch.

Within that all-positive batch, the rows split into two familiar confirmation classes:

1. `SC043`, `SC044`, `SC045`, and `SC048` confirm default-profile local breaks.
2. `SC041`, `SC042`, `SC046`, and `SC047` confirm default-profile broad/far or otherwise non-local constraints and should not be described as local adjacency evidence.

`SC041` and `SC048` are the large-effect rows in this batch:

1. `SC041` earlier crosses `SC020` with `67` changed outputs and `64` new failures, so it is a large broad/far break rather than a local claim.
2. `SC048` earlier crosses `SC047` with `87` changed outputs and `87` new failures, but it still belongs to the local-break class because the first break is still immediately at `SC047`.

`SC044` also deserves a narrower note: crossing `SC043` changes many outputs, but only `slay` appears as a newly failing row in the committed failures TSV.

These results still remain separate from the default 70-card corpus pending an explicit integration policy.

## SC049-SC058 mini-batch update

The eligible `SC049` through `SC058` earlier-side mini-batch again splits into two result classes:

1. `SC049`, `SC054`, and `SC057` confirm default-profile broad/far or non-local breaks:
   - `SC049` earlier still breaks across `SC037`, with `rainbow`
   - `SC054` earlier still breaks across `SC020`, with `sea`
   - `SC057` earlier still breaks across `SC052`, with `bow`, `follow`, `hedge`, `seek`, and `singe`
2. `SC053` and `SC058` strengthen negative expanded-profile evidence by traversing the exposed PWGmc corridor down to `SC004` with no changed outputs and no newly failing rows.

This batch does **not** add any new `expanded_internal_pwgmc_break` case. It therefore strengthens the separate review layer without changing the current picture that only `SC031` and `SC033` provide clearly useful internal-PWGmc positive boundaries.

These results still remain separate from the default 70-card corpus pending an explicit integration policy.

## Integration status

All thirty-nine rows currently carry `integration_status = expanded_only_pending_policy`.

That means:

1. the results are committed and reviewable;
2. the results may refine or confirm default-profile interpretations;
3. the repository has **not** yet decided how expanded-profile evidence should enter the default chronology-card/index system or whether any of it should revise the default first-break TSV corpus or graph export.

## Recommended next step

With this index in place, the next recommended step is a light index audit before the next larger manual run, because the separate review layer now covers thirty-nine rows.

If that audit passes, the next manual expanded-profile run can move on to `SC060` through `SC076` earlier only, split into smaller chunks if desired.

Do not move to later-direction expanded-profile testing yet, and keep using this separate expanded-profile index as the review layer rather than mixing expanded evidence directly into the default 70-card chronology-card corpus.

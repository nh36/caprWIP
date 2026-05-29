# Expanded PWGmc SC030-SC040 mini-batch 04

## Scope

Nathan manually ran the expanded-PWGmc **earlier-side** mini-batch for:

1. `SC030` earlier
2. `SC031` earlier
3. `SC032` earlier
4. `SC033` earlier
5. `SC034` earlier
6. `SC035` earlier
7. `SC036` earlier
8. `SC037` earlier
9. `SC039` earlier
10. `SC040` earlier

`SC038` is a technical marker and was not part of the batch.

This note documents those rows as expanded-profile evidence only. It does not revise the default 70-card chronology-card corpus.

## Files used

This mini-batch is documented from the committed expanded-profile outputs only:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

## Summary table

| change_id | direction | result | boundary / first break | variants tested | changed outputs | new failures | profile interpretation | note |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| `SC030` | earlier | `first_break_found` | crossing `SC029` `OE Awj Glide Formation` | 1 | 2 | 2 | `confirms_default_local_break` | representative failures: `hay`, `strew` |
| `SC031` | earlier | `first_break_found` | crossing `SC011` `PWGmc Syllabic J` | 20 | 1 | 1 | `expanded_internal_pwgmc_break` | representative failure: `hay` |
| `SC032` | earlier | `first_break_found` | crossing `SC030` `OE Au Fronting` | 2 | 18 | 18 | `confirms_default_local_break` | representative failures: `believe`, `bow`, `bread`, `dream`, `flea` |
| `SC033` | earlier | `first_break_found` | crossing `SC008` `PWGmc Coronal W Assimilation` | 25 | 1 | 1 | `expanded_internal_pwgmc_break` | representative failure: `four` |
| `SC034` | earlier | `first_break_found` | crossing `SC031` `OE WW Simplification` | 3 | 2 | 2 | `confirms_default_local_break` | representative failures: `dew`, `hew` |
| `SC035` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 31 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break |
| `SC036` | earlier | `first_break_found` | crossing `SC019` `NWGmc Final Long O Raising` | 17 | 1 | 1 | `confirms_default_broad_far_break` | representative failure: `soul` |
| `SC037` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 33 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break |
| `SC039` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 35 | 0 | 0 | `strengthened_negative_evidence` | reached earlier boundary with no real break |
| `SC040` | earlier | `first_break_found` | crossing `SC039` `OE WI Combinative U Umlaut` | 1 | 1 | 1 | `confirms_default_local_break` | representative failure: `widow` |

## Main interpretation

This batch contributes three different kinds of evidence.

### 1. Confirmed default-profile local or broad/far breaks

The expanded profile confirms five positive breaks already visible in the default-profile chronology:

1. `SC030` earlier across `SC029`, with `hay` and `strew`
2. `SC032` earlier across `SC030`, with a large set of failures including `believe`, `bow`, `bread`, `dream`, and `flea`
3. `SC034` earlier across `SC031`, with `dew` and `hew`
4. `SC036` earlier across `SC019`, with `soul`
5. `SC040` earlier across `SC039`, with `widow`

These breaks still occur before the search reaches the exposed PWGmc corridor, so the expanded profile is confirming default-profile local or broad/far constraints rather than replacing them.

### 2. Newly informative expanded internal-PWGmc breaks

Two rules now gain a more specific positive boundary because the expanded profile can look inside bundled `PWGmcChanges`:

1. `SC031` earlier now breaks across `SC011` `PWGmc Syllabic J`, with `hay`
2. `SC033` earlier now breaks across `SC008` `PWGmc Coronal W Assimilation`, with `four`

These are the clearest cases so far where opening `PWGmcChanges` yields a genuinely more informative positive internal PWGmc boundary than the default bundled profile could provide.

### 3. Strengthened expanded-profile no-break evidence

`SC035`, `SC037`, and `SC039` now traverse the exposed PWGmc corridor down to `SC004` `PWGmc Ai Monophthongization` without changed outputs or newly failing rows.

These are therefore stronger negative results than the old default-profile wording “blocked at `PWGmcChanges`”.

## Concrete examples from the committed failures TSV

All positive-break examples below are taken directly from the committed expanded-profile failures TSV.

1. `SC030` earlier across `SC029`
   - `hay`: PGmc `*xáwwją` > expected OE `hīeġ`, variant `hauġ`
   - `strew`: PGmc `*stráwjaną` > expected OE `strīeġan`, variant `strauian`
2. `SC031` earlier across `SC011`
   - `hay`: PGmc `*xáwwją` > expected OE `hīeġ`, variant `hēai`
3. `SC032` earlier across `SC030`
   - `believe`: PGmc `*galáubijaną` > expected OE `ġelīefan`, variant `+?`
   - `bow`: PGmc `*báug` > expected OE `bēag`, variant `+?`
   - `bread`: PGmc `*bráudą` > expected OE `brēad`, variant `+?`
   - `dream`: PGmc `*dráugmaz` > expected OE `drēam`, variant `+?`
   - `flea`: PGmc `*fláuxz` > expected OE `flēah`, variant `+?`
4. `SC033` earlier across `SC008`
   - `four`: PGmc `*fédwōr` > expected OE `fēower`, variant `feower`
5. `SC034` earlier across `SC031`
   - `dew`: PGmc `*dáwwō` > expected OE `dēaw`, variant `dawu`
   - `hew`: PGmc `*xáwwaną` > expected OE `hēawan`, variant `hawan`
6. `SC036` earlier across `SC019`
   - `soul`: PGmc `*sáiwalō` > expected OE `sāwol`, variant `sāwel`
7. `SC040` earlier across `SC039`
   - `widow`: PGmc `*wíduwōn` > expected OE `wuduwe`, variant `wudowe`

## Profile warning

These rows remain **expanded-profile** results. They should not overwrite, silently revise, or be folded directly into the default chronology-card corpus, default first-break TSV corpus, or default graph export.

That warning matters especially for `SC031` and `SC033`: the expanded profile now provides more specific internal-PWGmc positive boundaries for those rules, but the repository still needs an explicit policy decision before such evidence is integrated into the ordinary chronology-card system.

## Recommendation

At this point, either:

1. run the next manual expanded-profile mini-batch for `SC041` through `SC048` **earlier only**; or
2. pause for a short audit of the expanded-profile index first, since the separate review layer is starting to grow.

The safer recommendation is a **short audit of the expanded-profile index first**, followed by `SC041` through `SC048` earlier only if the index structure still feels manageable.

Do **not** move to later-direction expanded-profile tests yet.

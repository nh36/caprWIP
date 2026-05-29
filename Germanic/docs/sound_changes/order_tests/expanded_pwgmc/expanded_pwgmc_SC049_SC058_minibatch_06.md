# Expanded PWGmc SC049-SC058 mini-batch 06

## Scope

Nathan manually ran the expanded-PWGmc **earlier-side** mini-batch for the eligible rules in the `SC049` through `SC058` corridor:

1. `SC049` earlier
2. `SC053` earlier
3. `SC054` earlier
4. `SC057` earlier
5. `SC058` earlier

This note documents those rows as expanded-profile evidence only. It does not revise the default 70-card chronology-card corpus.

## Files used

This mini-batch is documented from the committed expanded-profile outputs only:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

## Summary table

| change_id | direction | result | boundary / first break | variants tested | changed outputs | new failures | profile interpretation | note |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| `SC049` | earlier | `first_break_found` | crossing `SC037` `OE Compound Linking Syncope` | 12 | 1 | 1 | `confirms_default_broad_far_break` | broad/far rather than local because it crosses back from `SC049` to `SC037`; representative failure: `rainbow` |
| `SC053` | earlier | `no_break_before_boundary` | boundary `SC004` `PWGmc Ai Monophthongization` | 49 | 0 | 0 | `strengthened_negative_evidence` | strengthened negative evidence down to the exposed PWGmc corridor |
| `SC054` | earlier | `first_break_found` | crossing `SC020` `PGmc Final Z Deletion` | 34 | 1 | 1 | `confirms_default_broad_far_break` | broad/far rather than local because it crosses back from `SC054` to `SC020`; representative failure: `sea` |
| `SC057` | earlier | `first_break_found` | crossing `SC052` `OE Velar Palatalization` | 5 | 7 | 7 | `confirms_default_broad_far_break` | broad/far or non-local rather than adjacent because it crosses back from `SC057` to `SC052`; representative failures: `bow`, `follow`, `hedge`, `seek`, `singe` |
| `SC058` | earlier | `no_break_before_boundary` | boundary `SC004` `PWGmc Ai Monophthongization` | 54 | 0 | 0 | `strengthened_negative_evidence` | strengthened negative evidence down to the exposed PWGmc corridor |

## Main interpretation

This batch splits into two evidence classes.

### 1. Confirmed broad/far positive breaks

Three rows confirm default-profile broad/far or non-local constraints:

1. `SC049` earlier across `SC037`, with `rainbow`
2. `SC054` earlier across `SC020`, with `sea`
3. `SC057` earlier across `SC052`, with `bow`, `follow`, `hedge`, `seek`, and `singe`

These are **not** new internal-PWGmc breaks. They confirm already visible default-profile constraints, but they should be treated as broad/far or non-local rather than as local adjacency evidence.

### 2. Strengthened negative expanded-profile evidence

Two rows strengthen earlier-side negative evidence by traversing the exposed internal PWGmc corridor down to `SC004` with no changed outputs and no newly failing rows:

1. `SC053` earlier
2. `SC058` earlier

So this mini-batch adds both new broad/far confirmations and new negative corridor probes, but **no** new `expanded_internal_pwgmc_break` case of the `SC031` / `SC033` type.

## Concrete examples from the committed failures TSV

All examples below are taken directly from the committed expanded-profile failures TSV.

1. `SC049` earlier across `SC037`
   - `rainbow`: PGmc `*régna-bùgô` > expected OE `reġnboga`, variant `reġnfoga`
2. `SC054` earlier across `SC020`
   - `sea`: PGmc `*sáiwiz` > expected OE `sǣ`, variant `sǣw`
3. `SC057` earlier across `SC052`
   - `bow`: PGmc `*báugijaną` > expected OE `bīeġan`, variant `bēaġan`
   - `follow`: PGmc `*fúlgijaną` > expected OE `fylġan`, variant `fulġan`
   - `hedge`: PGmc `*xágjaz` > expected OE `heġġ`, variant `hægġ`
   - `seek`: PGmc `*sōkijaną` > expected OE `sēċan`, variant `sōċan`
   - `singe`: PGmc `*sángijaną` > expected OE `senġan`, variant `sanġan`
   - optional further examples in the same failure set include `stretch` and `think`

## Profile warning

These rows remain **expanded-profile** results. They should not overwrite, silently revise, or be folded directly into the default chronology-card corpus, default first-break TSV corpus, or default graph export.

This batch also does not change the interpretation that expanded-profile evidence remains a separate review layer from the default 70-card corpus.

## Recommendation

Before the next larger manual run, perform a light audit of the expanded-profile index now that the separate review layer covers thirty-nine rows.

If that audit passes, the next manual expanded-profile run can move on to `SC060` through `SC076` **earlier only**, split into smaller chunks if desired.

Do **not** move to later-direction expanded-profile tests yet.

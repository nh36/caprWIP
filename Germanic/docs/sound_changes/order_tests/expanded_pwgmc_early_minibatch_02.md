# Expanded PWGmc early mini-batch 02

## Scope

Nathan manually ran the expanded-PWGmc **earlier-side** mini-batch for:

1. `SC015` earlier
2. `SC016` earlier
3. `SC017` earlier
4. `SC018` earlier
5. `SC019` earlier

The same expanded-profile output files already contained the earlier `SC014` smoke result, so this note summarizes the committed `SC014` through `SC019` earlier rows together as one early expanded-profile corridor sample.

## Files used

This note is based on the committed expanded-profile outputs only:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

## Summary table

| change_id | direction | result | boundary / first break | variants tested | changed outputs | new failures | note |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| `SC014` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 10 | 0 | 0 | reached earlier boundary with no real break; `last_safe_order=4` |
| `SC015` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 11 | 0 | 0 | reached earlier boundary with no real break; `last_safe_order=4` |
| `SC016` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 12 | 0 | 0 | reached earlier boundary with no real break; `last_safe_order=4` |
| `SC017` | earlier | `first_break_found` | `SC017_earlier_order_16`, crossing `SC016` `OE Ws Palatal Glide` | 1 | 1 | 1 | representative failure: `yoke`; `*júką > ġeoc`, variant `ġoc` |
| `SC018` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 14 | 0 | 0 | reached earlier boundary with no real break; `last_safe_order=4` |
| `SC019` | earlier | `first_break_found` | `SC019_earlier_order_17`, crossing `SC017` `NWGmc U Lowering` | 2 | 5 | 3 | representative failures: `nose`, `shovel`, `sorrow` |

## Main interpretation

The expanded profile is doing two different things in this mini-batch.

### A. Strengthened former boundary-limited earlier results

For `SC014`, `SC015`, `SC016`, and `SC018`, the default bundled profile could only show that the earlier search reached the opaque `PWGmcChanges` boundary. The expanded profile now exposes the internal PWGmc corridor and shows that each of these rules can be moved earlier across the exposed component sequence all the way down to `SC004` without changed outputs or newly failing rows.

This is therefore stronger **negative** evidence than the old bundled-boundary result. The search no longer stops at an opaque bundle; it traverses the exposed `SC013` through `SC004` corridor and still finds no real earlier first break.

### B. Confirmed local first-break relations that appear before the PWGmc corridor

For `SC017` and `SC019`, the expanded profile does **not** reach the internal PWGmc corridor because the first real break is encountered first:

1. `SC017` earlier still breaks immediately across `SC016` `OE Ws Palatal Glide`, with `yoke` as the concrete failure:
   - PGmc `*júką`
   - expected OE `ġeoc`
   - variant `ġoc`
2. `SC019` earlier still breaks across `SC017` `NWGmc U Lowering`, with concrete failures:
   - PGmc `*núsō` > expected OE `nosu`, variant `nusu`
   - PGmc `*skúflō` > expected OE `sċofl`, variant `sċufl`
   - PGmc `*súrgō` > expected OE `sorg`, variant `surg`

These results therefore confirm the same local first-break structure already visible in the default-profile chronology, while the no-break cases gain extra negative evidence from the exposed PWGmc corridor.

## Profile warning

These are **expanded-profile** results. They should not overwrite, silently revise, or automatically fold into the current default-profile chronology cards, index, or graph export.

The expanded evidence is compatible with the default-profile card layer: it strengthens the negative interpretation of the earlier no-break cases while leaving the local `SC017` / `SC016` and `SC019` / `SC017` first-break relations intact. But the repository should decide explicitly later how expanded-profile evidence should be represented in the chronology-card/index system, rather than mixing it into the default 70-card corpus ad hoc.

## Validation / hygiene

The committed expanded-profile outputs remain structurally valid:

1. summary TSV: `6` data rows for `SC014` through `SC019` earlier
2. changes TSV: `6` data rows total (`1` for `SC017`, `5` for `SC019`)
3. failures TSV: `4` data rows total (`1` for `SC017`, `3` for `SC019`)

No default-profile first-break TSVs, chronology cards, or graph outputs are changed by this documentation pass.

## Recommendation

Pause briefly and add an explicit **expanded-profile results index** before running larger expanded batches. That index should remain separate from the default 70-card chronology-card system.

If computation resumes after that design step, the next reasonable expanded-profile run is still a small manual earlier-side batch for `SC020` through `SC029` only, since many of those earlier searches also previously stopped at bundled `PWGmcChanges`.

That separate review layer now exists at `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_result_index.tsv`, where these six earlier-side rows can accumulate without being folded into the default chronology-card system.

Later-direction expanded-profile testing is still not recommended from this layer.

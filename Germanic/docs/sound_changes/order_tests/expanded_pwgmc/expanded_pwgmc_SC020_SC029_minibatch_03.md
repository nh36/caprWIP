# Expanded PWGmc SC020-SC029 mini-batch 03

## Scope

Nathan manually ran the expanded-PWGmc **earlier-side** mini-batch for:

1. `SC020` earlier
2. `SC021` earlier
3. `SC022` earlier
4. `SC023` earlier
5. `SC024` earlier
6. `SC025` earlier
7. `SC026` earlier
8. `SC027` earlier
9. `SC028` earlier
10. `SC029` earlier

This note documents those rows as expanded-profile evidence only. It does not revise the default 70-card chronology-card corpus.

## Files used

This mini-batch is documented from the committed expanded-profile outputs only:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

## Summary table

| change_id | direction | result | boundary / first break | variants tested | changed outputs | new failures | note |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| `SC020` | earlier | `first_break_found` | `SC020_earlier_order_19`, crossing `SC019` `NWGmc Final Long O Raising` | 1 | 1 | 1 | representative failure: `rest`; `*rástōz > ræste`, variant `rast` |
| `SC021` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 17 | 0 | 0 | reached earlier boundary with no real break |
| `SC022` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 18 | 0 | 0 | reached earlier boundary with no real break |
| `SC023` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 19 | 0 | 0 | reached earlier boundary with no real break |
| `SC024` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 20 | 0 | 0 | reached earlier boundary with no real break |
| `SC025` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 21 | 0 | 0 | reached earlier boundary with no real break |
| `SC026` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 22 | 0 | 0 | reached earlier boundary with no real break |
| `SC027` | earlier | `first_break_found` | `SC027_earlier_order_26`, crossing `SC026` `NWGmc Nasal Spirant Lengthening` | 1 | 3 | 3 | representative failures: `fist`, `goose`, `youth` |
| `SC028` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 24 | 0 | 0 | reached earlier boundary with no real break |
| `SC029` | earlier | `no_break_before_boundary` | boundary at `SC004` `PWGmc Ai Monophthongization` | 25 | 0 | 0 | reached earlier boundary with no real break |

## Main interpretation

The expanded profile again separates two distinct outcomes.

### A. Strengthened boundary-limited results

`SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, and `SC029` now traverse the exposed internal PWGmc corridor down to `SC004` `PWGmc Ai Monophthongization` without changed outputs or newly failing rows.

These are therefore stronger negative results than the old default-profile formulation “blocked at `PWGmcChanges`”. The expanded profile exposes the internal corridor explicitly and still finds no real earlier first break.

### B. Confirmed local first-break relations

Two rules still break locally before the search ever reaches the PWGmc corridor:

1. `SC020` earlier still breaks across `SC019` `NWGmc Final Long O Raising`, with `rest` as the concrete failure:
   - PGmc `*rástōz`
   - expected OE `ræste`
   - variant `rast`
2. `SC027` earlier still breaks across `SC026` `NWGmc Nasal Spirant Lengthening`, with concrete failures:
   - PGmc `*fúnxstiz` > expected OE `fȳst`, variant `fyst`
   - PGmc `*gánsz` > expected OE `gōs`, variant `ġeas`
   - PGmc `*júgunθ` > expected OE `ġeoguþ`, variant `ġeogoþ`

These positive breaks therefore confirm default-profile local constraints rather than adding a deeper PWGmc-corridor break story for those two rules.

## Profile warning

These rows remain **expanded-profile** results. They should not overwrite, silently revise, or be folded directly into the default chronology-card corpus, default first-break TSV corpus, or default graph export.

The expanded evidence is compatible with the default-profile card layer: it strengthens the negative interpretation of the boundary-limited cases while preserving the existing local break relations for `SC020` / `SC019` and `SC027` / `SC026`. But the repository should continue to treat that compatibility as a separate review-layer fact, not as automatic integration into ordinary cards.

## Recommendation

The next manual expanded-profile run should be `SC030` through `SC040` **earlier only**, not a larger batch. After each such mini-batch, update the separate expanded-profile index before considering any policy discussion about integration into the ordinary chronology-card or graph layers.

Do **not** move to later-direction expanded-profile tests yet.

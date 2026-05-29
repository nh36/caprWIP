# Remaining expanded-PWGmc boundary targets

## Why the scope needs to narrow

The expanded-PWGmc profile exists to answer one specific default-profile limitation: some **earlier-side** first-break searches in the ordinary chronology-card corpus stopped at the bundled `PWGmcChanges` stage instead of reaching a historical sound change.

So the right expanded-PWGmc question is **not** “what has not yet been rerun under expanded-pwgmc?” The right question is:

1. which default-profile earlier rows stopped at the opaque `PWGmcChanges` boundary;
2. which of those have already been rerun under `expanded-pwgmc`;
3. which of those still remain unresolved.

That is the only target class this note tracks.

## Source basis

This screening uses:

1. the ordinary default-profile first-break summary currently used for the chronology-card corpus:
   - `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
2. the current first-break manifest:
   - `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv`
3. the current expanded-PWGmc index:
   - `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_result_index.tsv`
4. the current expanded-PWGmc summary TSV:
   - `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`

For this purpose, a **true expanded-PWGmc target** is a default-profile earlier row whose ordinary result either:

1. reached `no_break_before_boundary` at bundled `PWGmcChanges`; or
2. found its first break only by crossing bundled `PWGmcChanges` itself.

Rows that already break against an ordinary historical stage before the bundle are **not** default expanded-PWGmc targets and should not be rerun under `expanded-pwgmc` unless a separate question justifies an exception.

## What the screened target set shows

The current default earlier-side corpus has **23** true bundled-`PWGmcChanges` target rows.

Of those:

1. **19** already have expanded-PWGmc results and are now resolved in the separate index.
2. **4** remain genuinely untested under expanded-PWGmc.

The resolved rows are:

1. `SC014`, `SC015`, `SC016`, `SC018`
2. `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`
3. `SC028`, `SC029`
4. `SC031`, `SC033`
5. `SC035`, `SC037`, `SC039`
6. `SC053`, `SC058`

The unresolved rows are:

1. `SC050`
2. `SC065`
3. `SC067`
4. `SC076`

## Why future expanded runs should stop following contiguous mini-batches

The earlier contiguous expanded mini-batches were useful for learning the terrain, but they also pulled in many rows that were **not** true bundled-PWGmc boundary cases. That is why the expanded index now contains local and broad/far confirmations alongside the genuine boundary-resolution rows.

Future expanded-PWGmc work should be narrower by default:

1. rerun only default-profile earlier rows that actually stopped at bundled `PWGmcChanges`;
2. avoid rerunning rows that already broke locally or broadly before the bundle;
3. make an exception only when there is a clearly stated separate reason.

This narrower policy keeps the expanded layer tied to its actual purpose: replacing opaque `PWGmcChanges` boundary results with either:

1. a specific internal PWGmc first break, as in `SC031` and `SC033`; or
2. stronger no-break evidence all the way down to `SC004`, as in the many strengthened-negative rows already indexed.

## Exact next manual run list

Based only on the remaining true bundled-PWGmc boundary targets, the exact remaining earlier-side manual expanded-PWGmc run list is:

1. `SC050` earlier
2. `SC065` earlier
3. `SC067` earlier
4. `SC076` earlier

If those four are completed, then the current ordinary default-profile corpus will have no remaining earlier-side `PWGmcChanges` boundary targets left unresolved under `expanded-pwgmc`.

## Scope warning

This means rows such as `SC051`, `SC052`, `SC055`, `SC056`, `SC059`, `SC060`, `SC061`, `SC063`, `SC064`, `SC066`, `SC068`-`SC075`, `SC078`-`SC083`, `SC085`, `SC086`, and `SC087` should **not** be treated as automatic expanded-PWGmc targets just because they have not yet appeared in the expanded index. In the default earlier profile, they already break against ordinary historical stages before the bundled PWGmc boundary.

The companion TSV in this directory records the screened bundled-boundary target set itself:

1. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/remaining_pwgmc_boundary_targets.tsv`

# Remaining expanded-PWGmc boundary targets

## Why the scope needs to narrow

The expanded-PWGmc profile exists to answer one specific default-profile limitation: some **earlier-side** first-break searches in the ordinary chronology-card corpus stopped at the bundled `PWGmcChanges` stage instead of reaching a historical sound change.

So the right expanded-PWGmc question is **not** “what has not yet been rerun under expanded-pwgmc?” The right question is:

1. which default-profile earlier rows stopped at the opaque `PWGmcChanges` boundary;
2. which of those have already been rerun under `expanded-pwgmc`;
3. which of those were still unresolved before the final closure batch.

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

All **23** now have expanded-PWGmc results and are now resolved in the separate index.

Zero true bundled-PWGmc boundary targets remain unresolved.

The resolved rows are:

1. `SC014`, `SC015`, `SC016`, `SC018`
2. `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`
3. `SC028`, `SC029`
4. `SC031`, `SC033`
5. `SC035`, `SC037`, `SC039`
6. `SC053`, `SC058`

The final four rows that remained unresolved before the closure batch were:

1. `SC050`
2. `SC065`
3. `SC067`
4. `SC076`

All four now resolve as strengthened no-break evidence down to `SC004`.

## Why future expanded runs should stop following contiguous mini-batches

The earlier contiguous expanded mini-batches were useful for learning the terrain, but they also pulled in many rows that were **not** true bundled-PWGmc boundary cases. That is why the expanded index now contains local and broad/far confirmations alongside the genuine boundary-resolution rows.

Future expanded-PWGmc work should be narrower by default:

1. rerun only default-profile earlier rows that actually stopped at bundled `PWGmcChanges`;
2. avoid rerunning rows that already broke locally or broadly before the bundle;
3. make an exception only when there is a clearly stated separate reason.

This narrower policy keeps the expanded layer tied to its actual purpose: replacing opaque `PWGmcChanges` boundary results with either:

1. a specific internal PWGmc first break, as in `SC031` and `SC033`; or
2. stronger no-break evidence all the way down to `SC004`, as in the many strengthened-negative rows already indexed.

## Closure status

The narrow earlier-side bundled-PWGmc boundary-target task is now closed.

That closure rests on the full resolved set:

1. `SC031` and `SC033`, which yielded specific internal PWGmc positive breaks; and
2. the remaining true bundled-boundary targets, which now all resolve as stronger no-break-to-`SC004` evidence, including the final four `SC050`, `SC065`, `SC067`, and `SC076`.

So the current ordinary default-profile corpus now has no remaining earlier-side `PWGmcChanges` boundary targets left unresolved under `expanded-pwgmc`.

## Scope warning

This means rows such as `SC051`, `SC052`, `SC055`, `SC056`, `SC059`, `SC060`, `SC061`, `SC063`, `SC064`, `SC066`, `SC068`-`SC075`, `SC078`-`SC083`, `SC085`, `SC086`, and `SC087` should **not** be treated as automatic expanded-PWGmc targets just because they have not yet appeared in the expanded index. In the default earlier profile, they already break against ordinary historical stages before the bundled PWGmc boundary.

The companion TSV in this directory records the screened bundled-boundary target set and now shows zero `run_expanded_earlier` rows:

1. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/remaining_pwgmc_boundary_targets.tsv`

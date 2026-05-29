# Expanded PWGmc phase synthesis

## 1. Why this phase existed

The default first-break system treated `PWGmcChanges` as a bundled stage. That was workable for the ordinary chronology-card corpus, but it also meant that some earlier-side tests stopped at an opaque bundled boundary rather than showing what happened inside the internal PWGmc corridor.

The expanded-PWGmc profile existed to open that bundled stage for inspection without rewriting the default corpus. Its role was investigative: expose the internal PWGmc corridor, record what the earlier-side tests actually do there, and keep those results in a separate review layer until an explicit integration policy is chosen.

## 2. What question this phase answered

This phase was **not** meant to rerun the whole chronology under `expanded-pwgmc`.

The narrow question was:

1. which default-profile earlier-side rows stopped at bundled `PWGmcChanges`;
2. what happens if those rows are rerun with the internal PWGmc corridor exposed;
3. whether each opaque bundled-boundary result should resolve into:
   - a specific internal PWGmc positive break; or
   - stronger no-break evidence down to `SC004`.

That is the question this phase has now answered.

## 3. What was found

The ordinary default-profile earlier-side corpus had **23** true bundled-PWGmc boundary targets.

All **23** now have expanded-PWGmc results.

The main result is simple:

1. only **2** targets produced specific internal positive PWGmc breaks:
   - `SC031` earlier across `SC011` `PWGmc Syllabic J`
   - `SC033` earlier across `SC008` `PWGmc Coronal W Assimilation`
2. all other genuine bundled-boundary cases resolved as no-break-to-`SC004` evidence.

The final four resolved targets were:

1. `SC050`
2. `SC065`
3. `SC067`
4. `SC076`

All four ended as `no_break_before_boundary` down to `SC004` with `0` changed outputs and `0` new failures.

So opening the bundle changed the interpretation of the earlier-side boundary problem in only two specific places. Everywhere else, it strengthened negative evidence rather than revealing additional internal positive breaks.

## 4. What the earlier exploratory contiguous mini-batches added

The earlier contiguous mini-batches did add useful evidence beyond the narrow boundary-target question.

In particular, they documented:

1. local confirmations where the expanded profile reproduces a nearby default-profile break;
2. broad/far or non-local confirmations where the expanded profile still supports an already known default-profile constraint;
3. the shape of the expanded review layer across a wider earlier-side corridor.

That material is useful context, but it is supplementary.

Those exploratory confirmations are **not** the reason this boundary-target phase is considered complete. The phase is complete because the 23 true bundled-PWGmc boundary targets are now all resolved.

## 5. What this does not mean

This phase result does **not** mean:

1. the entire chronology is finished;
2. the default 70-card chronology corpus should be automatically rewritten;
3. the default first-break TSVs should be automatically replaced;
4. the default graph exports should be automatically regenerated from expanded evidence;
5. later-direction expanded-profile testing should start automatically.

The default chronology-card corpus, default first-break TSV corpus, and default graph export remain unchanged.

Later-direction expanded-profile testing should remain out of scope unless a separate question explicitly asks for it.

## 6. Recommended next phase

The recommended next phase is a **policy/synthesis** phase rather than further computation.

Before changing chronology cards or graph layers, the project should decide how expanded-PWGmc evidence is supposed to appear in the ordinary chronology presentation.

That next phase should:

1. decide how expanded-PWGmc evidence should be represented in the ordinary chronology cards;
2. identify whether `SC031` and `SC033` deserve special card annotations because they exposed specific internal PWGmc positive breaks;
3. decide whether strengthened negative evidence should be recorded in ordinary cards or remain only in the expanded-profile layer;
4. prepare a concise integration-policy document before any card or graph revisions are attempted.

## 7. Concrete next task after this synthesis

The concrete next documentation task should be:

`Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_integration_policy_draft.md`

That draft should be created only when the project is ready to decide how, if at all, expanded-PWGmc evidence should affect the ordinary chronology-card system.

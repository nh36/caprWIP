# SC031 / SC033 expanded-PWGmc card annotation proposal

## 1. Card locations

The ordinary chronology-card files for the two candidate rules are:

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC031-oe-ww-simplification.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC033-oe-ew-long-diphthong.md`

The paths are explicit and already follow the ordinary chronology-card naming pattern, so no ambiguous secondary location had to be inferred.

## 2. Current card structure

Both cards currently use the same basic structure:

1. `## Current position`
2. `## Earlier boundary`
3. `## Later boundary`
4. `## Chronology statement`
5. `## Caveats`
6. `## Source files`

Neither card currently has a dedicated “supplementary evidence” or “expanded-profile note” section, so the cleanest minimal insertion point would be a new short section placed **after `## Chronology statement` and before `## Caveats`**.

### SC031

- **file:** `Germanic/docs/sound_changes/order_tests/chronology_cards/SC031-oe-ww-simplification.md`
- **title / change ID:** `SC031 OE WW Simplification`
- **current earlier-side first-break result:** first earlier break at order `13`, crossing bundled `PWGmcChanges`, stage type `blocked_by_runner_limitation`, with representative failures `four; hay`
- **does it currently mention bundled `PWGmcChanges`?** yes, explicitly in `## Earlier boundary`, `## Chronology statement`, and `## Caveats`
- **does it already have a suitable note slot?** not explicitly, but the card structure would support a concise new section between `## Chronology statement` and `## Caveats`

Current ordinary-card framing says the earlier break is real computationally but non-historical / runner-limited because it only appears when the run reaches bundled `PWGmcChanges`.

### SC033

- **file:** `Germanic/docs/sound_changes/order_tests/chronology_cards/SC033-oe-ew-long-diphthong.md`
- **title / change ID:** `SC033 OE Ew Long Diphthong`
- **current earlier-side first-break result:** first earlier break at order `13`, crossing bundled `PWGmcChanges`, stage type `blocked_by_runner_limitation`, with representative failure `four`
- **does it currently mention bundled `PWGmcChanges`?** yes, explicitly in `## Earlier boundary`, `## Chronology statement`, and `## Caveats`
- **does it already have a suitable note slot?** not explicitly, but the same minimal new section between `## Chronology statement` and `## Caveats` would fit cleanly

Current ordinary-card framing says the earlier-side break is computational but non-historical because it appears only when the runner enters bundled `PWGmcChanges`.

## 3. Proposed annotation text

These are proposal-only annotation drafts. They are intentionally short and framed as supplementary evidence rather than card-rewriting text.

### Proposed SC031 annotation

> **Expanded-PWGmc supplementary note:** The default-profile earlier test reaches bundled `PWGmcChanges`, so the ordinary card records that boundary as non-historical / runner-limited. In the separate expanded-PWGmc profile, the first internal positive break for `SC031` earlier appears when crossing `SC011` `PWGmc Syllabic J`, with `hay` as the representative failure (`*xáwwją` > expected OE `hīeġ`, variant `hēai`). This supplements, but does not replace, the default bundled-profile card evidence.

### Proposed SC033 annotation

> **Expanded-PWGmc supplementary note:** The default-profile earlier test reaches bundled `PWGmcChanges`, so the ordinary card records that boundary as non-historical. In the separate expanded-PWGmc profile, the first internal positive break for `SC033` earlier appears when crossing `SC008` `PWGmc Coronal W Assimilation`, with `four` as the representative failure (`*fédwōr` > expected OE `fēower`, variant `feower`). This supplements, but does not replace, the default bundled-profile card evidence.

## 4. Link targets

The most useful cross-links from the ordinary cards would be:

1. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_integration_policy_draft.md`
   - use as the policy basis for why only `SC031` and `SC033` are candidates for minimal ordinary-card annotation
2. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_boundary_target_closure.md`
   - use as the narrow-task closure summary showing that these two rows are the only internal positive breaks among the true bundled-boundary targets
3. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc/expanded_pwgmc_phase_synthesis.md`
   - use as the higher-level explanation of what the expanded-PWGmc phase answered

`expanded_pwgmc_result_index.tsv` is useful as a backing source, but it is probably **not** the best primary in-card link target because it is a machine-oriented review index rather than a reader-facing narrative note. If the cards later gain a more technical “source files” bullet for expanded evidence, then linking the TSV there would be reasonable; otherwise the three narrative documents above are the better minimal set.

## 5. Recommended insertion point

If the project later decides to apply these annotations, the smallest change would be:

1. leave the existing `## Earlier boundary` wording intact;
2. leave the existing `## Chronology statement` intact;
3. insert a new short section titled `## Expanded-PWGmc supplementary note` between `## Chronology statement` and `## Caveats`.

That approach preserves the current default bundled-profile interpretation while making the two expanded internal-PWGmc results visible as explicitly supplementary evidence.

## 6. No-change recommendation

This task is **reconnaissance and proposal only**.

The next commit should **not** edit the ordinary chronology cards yet. It should first decide whether to approve the proposed minimal wording and link set for `SC031` and `SC033`, then make those two targeted card edits separately if desired.

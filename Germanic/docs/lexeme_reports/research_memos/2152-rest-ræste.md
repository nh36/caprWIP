# Research memo — 2152 rest / ræste

## Starting point

- **ID:** 2152
- **CONCEPT:** rest
- **COUNTERPART:** ræste
- **PROTO:** `*rastō`
- **PROTOFORM:** `*rástōz`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** the live TSV note treats the row as an oblique ō-stem gen.sg. solution `*rastōz > ræste`, cites R/T §6.8.3 plus `DEV_NOTES §17.10.20`, and explains dictionary/headword `ræst` as later leveling from the oblique stem.

No dedicated pilot/full lexeme report for this row turned up in `Germanic/docs/lexeme_reports/pilot/`; the packet and debug snapshots are therefore background evidence, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row's structural choice (`PROTO` `*rastō`, `PROTOFORM` `*rástōz`, target `ræste`); the packet's compact trace; the live FST implementation in `Germanic/fsts/germanic.txt`; and the current publish snapshot showing `*rástōz -> ræste`.
- **Useful background:** the packet's `DEV_NOTES` excerpts at 3191-3197 (the full ō-stem paradigm split), 3457 (the project-level oblique-cell decision), 24149-24218 (the later staged implementation), and 25306-25310 (methodological precedent), plus `compound_archaism_inventory.md` case 8.
- **Stale or superseded:** the packet's preserved mismatch history `*rástōz -> ræst (expected ræste)`; the `§17.10.20` Option γ material that models the ending by direct `{*æ}` output; and the current TSV note insofar as it still cites that older shortcut chronology. Live `germanic.txt` comments explicitly say the bundled `PGmcFinalOZShortening` approach was removed in favour of the later staged `*-ōz > *-ō > *-ā > *-ǣ > *-æ > -e` analysis.
- **Irrelevant or misleading:** lexical-table headword evidence such as `old_english_wiktionary.tsv` `rest = ræst` is useful for citation-form orientation, but it is not an argument against the row's selected oblique target `ræste`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` around lines 3187-3197, 3448-3457, 22705-22760, 23490-23640, 24093-24218, and 25306-25310.
- `Germanic/fsts/germanic.txt`, especially the comments and rules for `PGmcFinalZDeletion`, `PWGmcSurvivingBimoricOUnrounding`, and `AngloFrisianBrighteningLongFinal`.
- `Germanic/docs/analysis/compound_archaism_inventory.md`, case 8.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/tools/oe_paradigm_probe.py`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md`.

Main findings from the extra check:

- The live FST still gives the crucial contrast: manual probe confirms `*rastō -> rast` and `*rástōz -> ræste`.
- `oe_known_problems.tsv` has no live exception entry for this row; this is a retargeted row, not a known-unmodelled mismatch.
- `oe_paradigm_probe.py` has no built-in `rest / ræste` spec; the standardized probe is still missing.
- `old_english_wiktionary.tsv` keeps the lexeme under citation/headword `ræst`, which confirms the headword-vs-selected-cell distinction rather than overruling the row.
- No separate rest-specific dossier file turned up beyond the packeted `DEV_NOTES` material and the later synthesis in `compound_archaism_inventory.md`.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / lexeme-level headword:** TSV `PROTO` `*rastō`, the noun as a lexeme.
2. **Project derivational input:** TSV `PROTOFORM` `*rástōz`, a selected **oblique paradigm cell** rather than the lexeme headword.
3. **OE target form represented by the row:** `ræste`, likewise an **oblique OE form**, not the dictionary citation form.

The most important chronological point from the repo re-check is that the **current** implementation is the later staged one, not the earlier Option γ shortcut. The live chain is:

`*rástōz -> *rástō -> *rástā -> *ræstǣ -> *ræstæ -> ræste`

via final `*-z` deletion, surviving-bimoric `*ō -> *ā`, long-final Anglo-Frisian brightening `*ā -> *ǣ`, OE shortening, and OE unstressed `æ > e`.

The older direct `{*æ}`-output account remains useful project history, but it is no longer the live implementation and should not be treated as the final reconstruction.

Repo-local paradigm discussion also matters here: `DEV_NOTES` 3191-3197 explicitly says nom.sg. `*rastō` gives `rast`, while acc.sg., gen.sg., and dat.sg. converge on `ræste`. So the row's `*rástōz` is one selected oblique cell inside a broader oblique pattern, not the only imaginable source of OE `ræste`.

## Old English philology

`ræste` is an attested OE oblique form, but it is not the default dictionary headword. The packet's own BT-style examples (`tó ræste`, `on ræste`) are prepositional/dative-looking uses, while `old_english_wiktionary.tsv` indexes the lexeme under `ræst`.

That means the memo should keep three philological levels distinct:

- **attested citation/headword:** `ræst`;
- **attested oblique form:** `ræste`;
- **predicted sound-law nominative:** `rast`.

The last of those (`rast`) should be treated here as a reconstructed/project-diagnostic outcome, not as securely attested on the evidence checked for this memo. The row is therefore not claiming that the ordinary OE lemma was `ræste`; it is selecting an oblique form because the headword `ræst` reflects paradigm leveling from the oblique stem.

The packet's current wording also overstates case certainty a little: it labels the row specifically as gen.sg., but the attested examples it cites are dative/prepositional, and repo notes say multiple oblique singular cells yield the same `ræste` surface form.

## Project problem and solution

The project problem is the mismatch between the lexeme's leveled dictionary headword and the underlying paradigm split. If the row targeted the nominative/citation input `*rastō`, the live cascade gives `rast`, not `ræst`. The row therefore cannot represent the OE lexeme well by staying at the nominative level alone.

The current project-level solution is basically right:

- keep lexeme-level `PROTO` as `*rastō`;
- use an oblique `PROTOFORM` that the FST can derive regularly;
- target oblique `ræste`;
- explain headword `ræst` as later leveling from oblique `ræst-`.

What is not fully right yet is the surrounding explanatory prose. The current note still mixes a superseded implementation history (`§17.10.20`) with current row analysis, and it cites dative-style attestations while presenting the row as if the philological evidence were specifically gen.sg.

## Paradigm probe

A paradigm probe **is required** for this row, because the analysis is paradigmatic at its core: the point is precisely that nominative and oblique cells diverge, and that the oblique stem later levels into the headword.

The standardized probe is still **missing**. `Germanic/tools/oe_paradigm_probe.py` currently has built-in specs for `ban`, `berry`, `span`, `thistle`, `fire`, and `tap`, but not for `rest / ræste`.

If the probe is added, it should cover at minimum these cells:

- **nom.sg.** `*rastō -> rast`
- **gen.sg.** `*rastōz -> ræste`
- **acc.sg.** the corresponding ō-stem oblique singular cell discussed at `DEV_NOTES` 3193, which also yields `ræste`
- **dat.sg.** the corresponding ō-stem dative singular cell discussed at `DEV_NOTES` 3195, which also yields `ræste`

Manual probing already confirms the key nom.sg./gen.sg. contrast, but the saved probe should make the full nom.sg. vs. oblique-majority pattern explicit.

## Recommended final report

Recommend a concise final report that presents row 2152 as a paradigm-cell case: lexeme-level `PROTO` `*rastō`, selected oblique `PROTOFORM` `*rastōz`, attested oblique OE `ræste`, and leveled citation/headword `ræst`. It should note that the live implementation now uses the later staged `*-ōz > *-ō > *-ā > *-ǣ > *-æ > -e` chronology, and it should avoid overstating the attested evidence as specifically gen.sg. when the cited uses are prepositional/dative.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended.** `*rastō` is the right lexeme-level headword.
- **TSV `PROTOFORM`:** **no immediate change recommended.** `*rástōz` remains a defensible selected oblique cell, even though repo philology shows that other oblique singular cells also converge on `ræste`.
- **TSV `COUNTERPART`:** **no change recommended.** `ræste` is the right target for the row's selected oblique strategy.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `late_analogy` still fits the oblique-to-headword leveling analysis.
- **TSV `NOTE`:** **change recommended.** Update it to reflect the current staged chronology (`§17.10.23`-style implementation, not the older `§17.10.20` shortcut), and clarify that the cited attested examples are oblique/prepositional uses rather than direct proof of a specifically gen.sg. target.
- **`oe_known_problems.tsv`:** **no change recommended.**
- **`DEV_NOTES` / dossier text:** **change recommended.** `DEV_NOTES` should mark the `§17.10.20` direct-`{*æ}` account more clearly as superseded by the later staged solution, and `compound_archaism_inventory.md` should stop collapsing lexeme-level proto and selected paradigm cell by labelling `*rastōz` as the case's sole `PROTO`; it should distinguish lexeme-level `*rastō` from the chosen oblique input.

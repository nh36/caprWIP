---
row_id: 2152
concept: rest
counterpart: ræste
proto: *rastō
protoform: *rástōz
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2152-rest-ræste.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/compound_archaism_inventory.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2152 rest / ræste

## Current row state

- CONCEPT: `rest`
- COUNTERPART: `ræste`
- PROTO: `*rastō`
- PROTOFORM: `*rástōz`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note (quoted closely): `Oblique (ō-stem gen.sg.) *rastōz > ræste: PGmc gen.sg. *-ōz did not undergo NWGmcFinalLongORaising ... After PWGmc z-loss with vowel shortening and simultaneous AFB-fronting of the unstressed final (*-ōz > {*æ}, R/T §6.8.3 pp.299-300; see DEV_NOTES §17.10.20), suffix is front, no A-restoration, AFB gives ræ-. Attested ræste abundantly in BT (tó ræste, on ræste, etc.). Paradigmatic leveling from oblique ræst- to nom.sg.` [Germanic/data/germanic-aligned-final.tsv:862]
- `oe_known_problems.tsv`: no entry was found for row `2152`, `rest`, `ræste`, `*rastō`, or `*rástōz` during the required source check; both the packet and the memo record `_None_` for matching known-problem entries [Germanic/docs/lexeme_reports/packets/2152-rest-ræste.md:44-46; Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md:37-39].
- Packet status: the compact derivation trace already matches the live row's selected input/output pairing and shows the current staged path `*rástōz -> *rástō -> *rástā -> *ræstǣ -> *ræstæ -> ræste` [Germanic/docs/lexeme_reports/packets/2152-rest-ræste.md:17-41].
- Current DEV_NOTES authority status: securely attachable current material does exist for this row, but it is split across several layers. The strongest current row policy is the oblique-form update at lines 3455-3457 and the later staged worked derivation at lines 24093-24218; the still-cited `§17.10.20` direct-`{*æ}` account is preserved in DEV_NOTES as important history but is no longer the best current implementation explanation [Germanic/docs/DEV_NOTES.md:24093-24218,3455-3457; Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md:17-20,51-57,79-87].

## Development-note summary

Row 2152 must be read as a deliberate paradigm-cell row with three distinct levels, not as a single-form lemma equation. The live TSV keeps lexeme-level `PROTO` as `*rastō`, uses row-level `PROTOFORM` `*rástōz` as a selected **oblique** singular cell, and compares that to OE `ræste`, likewise an oblique form rather than the dictionary headword [Germanic/data/germanic-aligned-final.tsv:862; Germanic/docs/lexeme_reports/packets/2152-rest-ræste.md:21-41]. DEV_NOTES is explicit about why this split is needed: nominative `*rastō` develops regularly to `rast`, because final `*-ō` raises to back `*-u` and triggers A-restoration, whereas acc.sg., gen.sg., and dat.sg. oblique cells all keep a front-vocalic environment and converge on `ræste` [Germanic/docs/DEV_NOTES.md:3171-3208].

That shared paradigm note remains the core philological explanation. DEV_NOTES lays out the full ō-stem contrast in one place: nom.sg. `*rastō -> rast`, acc.sg. `*rastō̃ -> ræste`, gen.sg. `*rastōz -> ræste`, and dat.sg. `*rastōi -> ræste`; it then states the historical consequence directly: only the nominative has the back suffix that triggers restoration, while the oblique singulars keep `ræst-` throughout, and that majority oblique pattern was generalized to the citation form `ræst` [Germanic/docs/DEV_NOTES.md:3191-3197]. The same block also preserves the BT-style philology in compressed form: headword `ræst`, but oblique `ræste` in gen./dat.sg. uses [Germanic/docs/DEV_NOTES.md:3201-3204]. The row should therefore be described as follows: OE headword/citation form `ræst`; selected row target `ræste`; projected sound-law nominative `rast`; later analogical leveling from oblique `ræst-` explains the dictionary form.

For current implementation history, the decisive point is that DEV_NOTES moved beyond the earlier `§17.10.20` shortcut. The older solution wrote the gen.sg. ending directly as `{*æ}` and is the source of the live TSV note's present wording, but the later worked derivation keeps the intermediate stages explicit: `*rástōz -> *rástō -> *rástā -> *ræstǣ -> *ræstæ -> ræste` [Germanic/docs/DEV_NOTES.md:23490-23640,24149-24160]. That later section is now the better authority because it preserves the row's current logic without collapsing the chronology: final `*-z` deletes, surviving bimoric `*ō` unrounds to `*ā`, long-final AFB fronts it to `*ǣ`, OE shortening gives `*æ`, and weak-tail reduction yields final `-e` [Germanic/docs/DEV_NOTES.md:24093-24147,24149-24160]. Any replacement working note should therefore treat `§17.10.20` as superseded implementation history and the staged derivation as the current account.

The row-specific policy statement in DEV_NOTES is also securely current. The update note says that TSV row 2152 now uses genuine PGmc gen.sg. `*rastōz`, target `ræste`, and explicitly groups the row with the project's other oblique-cell precedents such as cow and fire [Germanic/docs/DEV_NOTES.md:3455-3457]. A later methodology summary restates the same rule in general form and names `ræste` directly among the precedents: when an OE form arose by transfer from a specific paradigm cell, encode that cell instead of distorting phonology to force the leveled nominative from the lexeme headword [Germanic/docs/DEV_NOTES.md:25306-25310]. For row 2152, that is the durable current principle.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3167-3208

- Source heading: `Background: A-restoration and paradigmatic leveling` / `Case 1: *rastō -> rast (expected ræst) — ō-stem feminine`
- Source line or section hint: `lines 3167-3208`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `background`
- Issue tags: `A_restoration`; `paradigm_cell`; `oblique_leveling`; `protoform_vs_proto`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `1980; 2013; 2053; 2140`

This is the foundational shared fragment for the row because it states both the sound-law contrast and the paradigm-level explanation in a way later sections assume rather than repeat. DEV_NOTES first gives the general A-restoration principle from R/T: original PGmc suffix `*a` fronts under AFB and therefore does **not** trigger restoration, while suffix `*o/*u/*ō` stay back and do [Germanic/docs/DEV_NOTES.md:3171-3178]. It then applies that directly to `*rastō`: nominative `*rastō -> *rastu -> rast`, but acc.sg., gen.sg., and dat.sg. all yield `ræste`, and the note spells out the historical conclusion in plain language: the majority oblique pattern `ræst-` was generalized to the nominative headword `ræst` [Germanic/docs/DEV_NOTES.md:3180-3199]. For row 2152 this fragment is background rather than the last word on implementation, but it is still the clearest single explanation of why `PROTO` must stay `*rastō` while row-level `PROTOFORM` can be the oblique `*rástōz`.

### DEV_NOTES:line-22705-22732

- Source heading: `Case 3 — *rástōz → ræst (expected ræste)`
- Source line or section hint: `lines 22705-22732`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `literature_consensus`; `genitive_singular`; `ending_survival`; `weak_tail`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment preserves the source-verified consensus that made the row salvageable as a regular oblique-cell derivation. DEV_NOTES quotes R/T §6.8.3 that ō-stem acc.sg./gen.sg. `-e` continues `PGmc ... gen.sg. *-ōz`, then adds Campbell and Brunner to show the narrower disagreement: whether the immediate phonological endpoint was short `-a` later leveled to `-e`, or whether `-e` can be taken as the direct regular result of the historical chain [Germanic/docs/DEV_NOTES.md:22707-22731]. What matters for row 2152 is the shared conclusion stated there: the ending survives and should produce OE `-e`, not zero [Germanic/docs/DEV_NOTES.md:22726-22732]. That consensus remains current even though the surrounding first-pass pipeline diagnosis was later replaced.

### DEV_NOTES:line-24093-24218

- Source heading: `Add PWGmcSurvivingBimoricOUnrounding` / `Worked derivation: *rástōz → ræste under the new pipeline`
- Source line or section hint: `lines 24093-24218`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `staged_chronology`; `worked_derivation`; `A_restoration`; `weak_tail`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest current implementation fragment. DEV_NOTES replaces the earlier shortcut with an explicit staged chronology: z-loss first exposes final `*-ō`, `PWGmcSurvivingBimoricOUnrounding` turns that surviving bimoric `*ō` into `*ā`, Anglo-Frisian Brightening fronts final `*ā` to `*ǣ`, OE shortening gives final `*æ`, and `OEWeakTailReduction3` produces `-e` [Germanic/docs/DEV_NOTES.md:24093-24147]. The worked derivation then writes the row out step by step as `*rástōz -> *rástō -> *rástā -> *ræstǣ -> *ræstæ -> ræste` and explicitly says that row 2152 should now behave as `*rástōz → ræste` [Germanic/docs/DEV_NOTES.md:24149-24218]. For later report writing this fragment should be preferred over `§17.10.20`, because it matches the present pipeline chronology and keeps the intermediate long-vowel stages visible.

### DEV_NOTES:line-3455-3457

- Source heading: `UPDATE: ō-stem gen.sg. *-ōz now properly modeled in pipeline`
- Source line or section hint: `lines 3455-3457`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_policy`; `paradigm_cell`; `tsv_update`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This brief row-specific note is the cleanest current statement of policy. DEV_NOTES says that the ō-stem nominative path remains `rastō -> rast`, then immediately records the row update: TSV row 2152 now uses genuine PGmc gen.sg. `*rastōz`, target `ræste`, and this follows the same oblique-form approach already used for cow and fire [Germanic/docs/DEV_NOTES.md:3455-3457]. Even though the paragraph around it belongs to an earlier implementation stage, this row-policy sentence itself remains current and securely attachable.

### DEV_NOTES:line-25306-25310

- Source heading: `Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)`
- Source line or section hint: `lines 25306-25310`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `project_precedent`; `paradigm_cell`; `analogical_transfer`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1980; 2013; 2119; 2140`

This later methodology summary is important because it shows that `ræste` was not a one-off repair. DEV_NOTES names `ræste` explicitly among the project precedents and states the rule in general form: when the attested OE form arose by morphological transfer in a specific cell, encode that cell rather than rig phonology to generate the analogical nominative directly from the lexeme headword [Germanic/docs/DEV_NOTES.md:25306-25310]. For row 2152 that means the live distinction `PROTO *rastō` versus `PROTOFORM *rástōz` is project method, not accidental metadata noise.

### DEV_NOTES:line-23490-23640

- Source heading: `§17.10.20 — Case 3 implementation: PGmcFinalOZShortening outputs {*æ} directly (Option γ)`
- Source line or section hint: `lines 23490-23640`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `option_gamma`; `stale_implementation`; `tsv_note_cleanup`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This section is still worth preserving, but only as superseded implementation history. It solved the mismatch by making `PGmcFinalOZShortening` write `{*æ}` directly, and it documented a clean no-regression result for `*rástōz → ræste`; that is why the live TSV note still describes the ending in terms of simultaneous shortening plus direct fronting and cites `DEV_NOTES §17.10.20` [Germanic/docs/DEV_NOTES.md:23541-23587,23620-23640; Germanic/data/germanic-aligned-final.tsv:862]. However, DEV_NOTES later replaced this with the staged `*-ōz > *-ō > *-ā > *-ǣ > *-æ > -e` account at lines 24093-24218. This fragment should therefore be used only to explain inherited row-note wording and older project history, not as the present best derivation.

## Superseded or diagnostic material

- The early residual-regression dossier still preserves this lexeme under older row numbering as `row 862 | *rástōz | ræst | ræste`. That material is useful only as pre-fix diagnostics showing what the problem used to be; it should not be cited as if current row 2152 still mismatched [Germanic/docs/DEV_NOTES.md:22552-22560,22705-22732].
- `§17.10.20` Option γ is the main stale implementation hazard. It is historically important because the live TSV note still inherits its wording, but the later staged derivation at lines 24093-24218 is now the authoritative implementation account [Germanic/docs/DEV_NOTES.md:23490-23640,24093-24218; Germanic/data/germanic-aligned-final.tsv:862].
- `Germanic/docs/analysis/compound_archaism_inventory.md` case 8 is useful background but compresses two row levels by labeling `*rastōz` as the case's `PROTO`. The live row, packet, and memo all distinguish lexeme-level `PROTO` `*rastō` from selected oblique `PROTOFORM` `*rástōz`, so the analysis file should be cited cautiously unless that distinction is restated explicitly [Germanic/docs/analysis/compound_archaism_inventory.md:181-196; Germanic/docs/lexeme_reports/packets/2152-rest-ræste.md:21-41; Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md:45-57,109-115].
- The live row note's wording is slightly narrower than the fuller DEV_NOTES paradigm evidence. It labels the row specifically as a gen.sg. solution, but the core ō-stem discussion at lines 3191-3197 says acc.sg., gen.sg., and dat.sg. all converge on `ræste`; the cited BT-style examples in current repo material are also prepositional/dative-looking rather than uniquely gen.sg. [Germanic/docs/DEV_NOTES.md:3191-3197; Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md:63-74,103-115].

## Open questions for later work

- Add a saved `oe_paradigm_probe.py` spec for this lexeme if probe coverage expands. The memo already identifies the minimum useful contrast set as nom.sg. `*rastō -> rast` versus oblique singular cells such as gen.sg. `*rastōz -> ræste`, plus the corresponding acc.sg. and dat.sg. comparators [Germanic/docs/lexeme_reports/research_memos/2152-rest-ræste.md:88-101].
- If the TSV note is later revised, replace its `§17.10.20` citation with the later staged derivation at `Germanic/docs/DEV_NOTES.md:24093-24218` and consider softening the wording from narrowly `gen.sg.` to selected oblique singular, unless a specifically gen.sg. authority is being cited.
- If `compound_archaism_inventory.md` is reused or revised, restore the live row's three-way distinction explicitly: lexeme-level `PROTO` `*rastō`, row-level `PROTOFORM` `*rástōz`, and OE target `ræste` [Germanic/docs/analysis/compound_archaism_inventory.md:181-196; Germanic/data/germanic-aligned-final.tsv:862].

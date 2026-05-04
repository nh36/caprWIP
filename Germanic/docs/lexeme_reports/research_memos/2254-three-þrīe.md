# Research memo — 2254 three / þrīe

## Starting point

- **ID:** 2254
- **CONCEPT:** three
- **COUNTERPART:** þrīe
- **PROTO:** *θréjez
- **PROTOFORM:** *θréjez
- **DERIVATION_CLASS:** attested_variant
- **NOTE:** Target retargeted from þrī (late-WS reduction) to þrīe (regular early-WS m.nom/acc., Campbell §683); see DEV_NOTES §17.43.

No manual pilot/full report for this lexeme turned up in `Germanic/docs/lexeme_reports/pilot/`; the packet and debug-snapshot material are background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*θréjez -> þrīe`; and the `DEV_NOTES.md` extracts from `§17.43`, which explicitly argue that the FST output is correct and that the older target `þrī` was a late West Saxon reduction.
- **Useful background:** the packet's lexical-table hits (`old_english_wiktionary.tsv`, `old_english_swadesh.tsv`) because they show why a dictionary-style headword `þrī` was easy to mistake for the row target; and the bibliography-key suggestions pointing to Campbell and Kroonen.
- **Stale or superseded:** the packet's own "Mismatch as observed" block (`*θréjez -> þrīe (expected þrī)`) is diagnostic history, not current evidence; and any packet use of Wiktionary/Swadesh `þrī` as though it overruled the later row retargeting is superseded by live `DEV_NOTES §17.43`.
- **Irrelevant or misleading:** the packet's generic concept-name hits on unrelated analysis/dossier files are not evidence for this numeral; and the lexical-table headword `þrī` is misleading if treated as the inherited early-WS target rather than as a later/headword normalization.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the full `§17.43` section.
- `Germanic/tools/oe_paradigm_probe.py` to confirm whether a built-in probe spec already exists for this row.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md` and `.publish.missing_reports.md`.
- Repo-local reference extracts in `docs/references/`: `kroonen_etymological_dictionary_pgmc.vision.txt`, `fulk_comparative_grammar_early_germanic.vision.txt`, `ringe_vol1_pie_to_pgmc.txt`, and `bright_anglo_saxon_reader.vision.txt`.

No separate full dossier or analysis file was named in the packet or TSV note beyond `DEV_NOTES §17.43`, so there was no additional dossier file to audit.

Main findings from the extra check:

- `python3` with `oe_full_trace_report.apply_down(normalize_proto('*θréjez'))` confirms the current OE FST still returns `þrīe`.
- Kroonen's comparative entry is lexeme/stem-oriented (`*þri-`, with OE `þrī`, f./n. `þrio/prēo`), whereas the aligned TSV uses the explicitly inflected masculine nom./acc. input `*θréjez`.
- Fulk's comparative paradigm and the `DEV_NOTES` Campbell extract agree that OE `þrīe` is the masculine nom./acc. cell, beside `þrēo`, `þrēora`, and `þrim`.
- Bright's glossary-style entry groups the numeral under a headword-like `þrī`/variant set while listing oblique and gendered forms separately, which confirms that dictionary headword practice and the specific inherited cell are not the same thing.

## Reconstruction and early-stage forms

This row needs a careful three-way distinction, even though the live TSV currently uses the same string in `PROTO` and `PROTOFORM`.

1. **Comparative cognate-set proto / lexeme-level citation:** repo-local comparative sources such as Kroonen cite the numeral as stem-like `*þri-` (or discuss a `*þrī-` base after contraction/analogy), not as a single OE-ready citation form.
2. **Project input form for this row:** TSV `PROTOFORM = *θréjez`, i.e. the inherited masculine nom./acc. form that the OE cascade can derive directly. The live trace is coherent: final `-z` drops, `j` conditions i-umlaut/vocalization, and contraction yields `þrīe`.
3. **OE target form represented by the row:** attested early-WS masculine nom./acc. `þrīe`.

So the live row is not best read as "PGmc had only the citation form `*θréjez`." It is better understood as: the project keeps the derivationally explicit masculine cell `*θréjez` in both TSV proto columns for alignment purposes, while comparative lexica may cite the broader numeral under a stem/headword such as `*þri-`.

## Old English philology

`þrīe` should be treated as an attested OE paradigm cell, not as a mere reconstructed convenience form. The strongest repo-local philological point is Campbell's paradigm as preserved in `DEV_NOTES §17.43`: masculine nom./acc. `þrīe`, feminine/neuter nom./acc. `þrēo`, gen. `þrēora`, dat. `þrim`, with late West Saxon `þry, þri` explicitly treated as reduced forms of `þrīe`.

That means the exact row target is a **specific inherited cell**:

- **attested early/conservative cell:** `þrīe` (masc. nom./acc.);
- **other attested numeral cells:** `þrēo`, `þrēora`, `þrim`;
- **dictionary/headword-style normalization in supplementary tables:** `þrī`.

The key philological warning for the later report is therefore not "is `þrīe` real?" but "do not collapse the late/headword form `þrī` with the inherited masculine cell `þrīe`." This row is closer to an attested paradigm-cell selection than to an unattested reconstruction.

## Project problem and solution

The project problem was a false mismatch caused by treating dictionary-style `þrī` as the governing OE target. The FST was already producing the inherited early-WS masculine form `þrīe`; the mismatch lived in the target selection, not in the sound-change cascade.

The current row-level solution is basically correct:

- keep the OE target as `þrīe`;
- keep the note that `þrī` is a later West Saxon reduction;
- do **not** treat the regular `īe` outcome as an FST bug needing a phonological fix.

What still needs to stay explicit in future prose is that the row represents one attested numeral cell, not the entire OE lexeme abstracted away from gender/case.

## Paradigm probe

A paradigm probe **is required** in the broad sense, because this row is exactly a paradigm-cell-selection case: the project targets masculine nom./acc. `þrīe`, while supplementary lexical tables and comparative dictionaries often foreground `þrī` or the wider numeral paradigm instead.

But the packet is right that the probe is currently **missing** as a built-in `oe_paradigm_probe.py` spec: the live script has pilot specs for `ban`, `berry`, `span`, `thistle`, `fire`, and `tap`, and none for `three / þrīe`.

If a probe is added, it should at minimum cover these OE cells:

- **masc. nom./acc.** `þrīe` (the live row's target cell);
- **fem./neut. nom./acc.** `þrēo`;
- **gen.** `þrēora`;
- **dat.** `þrim`.

The probe should also note explicitly that late West Saxon `þrī/þrȳ` is a later reduced reflex of the masculine cell, not a rival inherited output that the current cascade is supposed to generate.

## Recommended final report

Recommend a concise final report that says row 2254 intentionally targets attested OE masculine nom./acc. `þrīe` from derivational input `*θréjez`, while distinguishing that row-level input from broader comparative headword citations like `*þri-` and from the later/headword-style OE form `þrī`. It should mention the rest of the OE numeral paradigm briefly and avoid presenting `þrī` as the live phonological target.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended for now; keep `*θréjez`, but future prose should explain that comparative lexica may cite the wider numeral under a stem/headword such as `*þri-`.
- **TSV `PROTOFORM`:** no change recommended; `*θréjez` is the right derivational input for the selected masculine cell.
- **TSV `COUNTERPART`:** no change recommended; keep `þrīe`.
- **TSV `DERIVATION_CLASS`:** no change recommended; `attested_variant` is still acceptable for an attested early/conservative target chosen over the later headword-style reduction.
- **TSV `NOTE`:** no change required; the live note already captures the central correction. At most, a later editorial tweak could make the "specific masculine nom./acc. cell" point even more explicit, but that is optional rather than necessary.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no change recommended. `DEV_NOTES §17.43` already reads as the authoritative current source, and no separate dossier file was identified for cleanup.

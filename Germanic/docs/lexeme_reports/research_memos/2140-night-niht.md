# Research memo — 2140 night / niht

## Starting point

- **ID:** 2140
- **CONCEPT:** night
- **COUNTERPART:** niht
- **PROTO:** *náxtz
- **PROTOFORM:** *náxti
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** R/T vol.2 13912-15: OE niht < dat.sg. *nahti (i-umlaut); nom.sg. *nahts > neaht

The live TSV already treats this as a paradigm-cell row rather than a simple citation-form reflex. I found no existing pilot/full lexeme report for this item, so the packet and repo notes remain the main project evidence.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*náxti → niht`; `DEV_NOTES.md` 6211-6223 and 6341-6343 on endingless dat.sg. `niht < *nahti`; Campbell/Brunner excerpts at `DEV_NOTES.md` 15478-15502 showing that palatal umlaut regularly gives `niht` before `ht` but not in plural forms like `neahtas`; and the current phonological note at `DEV_NOTES.md` 39278-39284 that `*xt` is preserved in rows including 2140.

**Useful background:** `analysis/ws_vs_anglian_dialect_differences.md` 709-710 on the OE doublets `neaht / niht` and Anglian `næht / neht`; `old_english_wiktionary.tsv` and `old_english_swadesh.tsv`, which both give lexical `niht`; `analysis/cow_root_noun_investigation.md`, which is not about night directly but usefully confirms the project's broader root-noun/oblique-cell method and already cites `naxti → niht` as a successful comparison; and `analysis/compound_archaism_inventory.md`, which records night as one of the established oblique-cell precedents.

**Stale or superseded:** the packet's purported high-confidence row-ID hit at `DEV_NOTES.md:25307` is stale project history, not live evidence. It explicitly says row 2140 is `spanne`, which shows that the row number belongs to an older table state and should not be used as evidence for night. The packet is correct to surface it diagnostically, but it is not authoritative for this row now.

**Irrelevant or misleading:** the packet's generic note-keyword hits in unrelated analysis/dossier files (for example the broad chronology match in `arestoration_r_l_research.md` and the unrelated `i-umlaut` hits from other dossiers) are not lexeme-specific evidence. They may be useful for general chronology, but they should not be weighed alongside the dedicated night discussions.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 6211-6223, 6341-6343, 15478-15502, 39278-39284, and 3167-3208.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md` 709-710.
- `Germanic/docs/analysis/cow_root_noun_investigation.md` 36-44 and 85-92.
- `Germanic/docs/analysis/compound_archaism_inventory.md` 163-177.
- `Germanic/docs/analysis/arestoration_r_l_research.md` 456-478.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv`.
- `Germanic/data/oe_known_problems.tsv` (no entry for this row).
- `Germanic/tools/oe_paradigm_probe.py`, plus a manual two-cell probe for this row.

That additional checking did not uncover a dedicated night dossier or a pre-existing night pilot report. The strongest repo evidence remains the live TSV, the dedicated `DEV_NOTES` discussion of endingless datives and palatal umlaut, and the dialect/variation summary in `ws_vs_anglian_dialect_differences.md`.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*náxtz`, i.e. the nominative-like root-noun headword for the cognate set.
2. **Project input form:** TSV `PROTOFORM` `*náxti`, the selected **dat.sg.** oblique cell.
3. **OE target form actually represented by the row:** `niht`, the attested OE form that the project derives from the oblique cell.

The compact derivation for the selected input is coherent: `*náxti > *næxti > *neaxti > *niexti > *nixti > *nixt > niht` (fronting, breaking, i-umlaut, WS palatal umlaut/smoothing before `ht`, then apocope/orthographic outcome). By contrast, the cognate-set citation form does **not** give the same target. A manual probe with `oe_paradigm_probe.py` confirms the core split:

- **nom.sg.** `*náxtz → neaht` (non-match)
- **dat.sg.** `*náxti → niht` (match)

So `PROTOFORM` is not a rival proto-lexeme and not a correction to `PROTO`; it is the selected paradigm cell that explains the OE target.

## Old English philology

`niht` is an attested OE form, not a reconstructed placeholder. But it is not the whole philological story. The repo evidence preserves a real alternation:

- West Saxon shows `neaht / niht`;
- Anglian shows `næht / neht`;
- Campbell and Brunner explicitly say the palatal-umlauted form occurs in `niht`, while plural forms such as `neahtas` preserve the non-umlauted stem before a following back vowel.

That matters because the current row should not be read as "the only OE form was `niht`." Rather, `niht` is the attested oblique/palatal-umlauted member of a paradigm/dialect complex, while `neaht` and `neahtas` preserve the nominative-like/non-umlauted side. The lightweight lexical tables checked here use `niht` as the headword, but the handbook evidence shows why the row still has to distinguish citation-form history from the chosen paradigm cell.

## Project problem and solution

The project problem is the mismatch between the cognate-set headword and the OE form the project wants to represent. If the row tried to derive the lexeme directly from `PROTO = *náxtz`, the FST gives `neaht`, not `niht`. The current project solution is therefore to keep the cognate-set proto in `PROTO`, select the dative singular `*náxti` in `PROTOFORM`, and classify the row as `late_analogy`.

That solution looks correct and already works in the live pipeline: unlike a `known_unmodelled` case, the FST does produce `niht` from the selected input. The "late analogy" is the philological reason the row targets an oblique cell, not a sign that the present TSV row is mis-specified.

## Paradigm probe

A paradigm probe **is required in principle**, because the whole case depends on the contrast between citation-form proto and selected oblique input. There is not yet a saved night-specific pilot probe in the repo, but the manual two-cell check is already decisive:

- **nom.sg.** `*náxtz → neaht`
- **dat.sg.** `*náxti → niht`

For the eventual final report, that contrast should be formalized as a small probe table. If the probe is expanded beyond the minimum, the next cell to add is a **plural back-vowel cell behind attested `neahtas`**, so the report can show explicitly why palatal umlaut does not generalize across the whole paradigm.

## Recommended final report

Recommend a concise final report that says row 2140 is a deliberate oblique-cell solution: TSV `PROTO` keeps the cognate-set headword `*náxtz`, TSV `PROTOFORM` uses dat.sg. `*náxti`, and OE `niht` is the attested palatal-umlauted/oblique form, while nominative-like `neaht` and plural `neahtas` belong to the contrasting non-umlauted side of the paradigm. The stale row-number hit in `DEV_NOTES` should be treated only as project history, not as evidence.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no required change; the current note already captures the essential `*nahti` versus `*nahts` contrast, though a later light clarification could mention that `niht` is the selected OE form within a broader `neaht/niht` alternation.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended in `DEV_NOTES.md`**. The stale row-number reference at line 25307 should be marked historical or rewritten so future packets do not treat old row numbering (`2140 = spanne`) as live evidence for night. No separate night dossier text change is currently required, because no dedicated night dossier was found.

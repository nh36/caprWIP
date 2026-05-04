# Research memo — 2183 shoulder / sċuldrum

## Starting point

- **ID:** 2183
- **CONCEPT:** shoulder
- **COUNTERPART:** sċuldrum
- **PROTO:** *skuldrō
- **PROTOFORM:** *skúldramiz
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** DatPl encoding: PROTOFORM is PGmc-proper *-amiz (inst.pl. branch of dat./inst. merger). See DEV_NOTES §17.41.

The live TSV already reflects the revised DatPl solution. No pilot report exists for this lexeme; the packet and shoulder dossiers are the relevant background.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing `*skúldramiz -> sċuldrum`; the current `DEV_NOTES.md` §17.41 implementation notes stating that row 2183 was updated to `PROTOFORM = *skúldramiz`, `COUNTERPART = sċuldrum`, and verified as `*skúldramiz -> sċuldrum`; and `Germanic/docs/dossier-shoulder-paradigm-survey-2026.md`, whose DatPl recommendation matches the live row.
- **Useful background:** `Germanic/docs/dossier-shoulder-2026.md` for the philological dossier on `sculdor / sculdru / sculdrum / sculdra`; `Germanic/docs/dossier-shoulder-cellchoice-2026.md` and `Germanic/docs/dossier-shoulder-lautgesetz-2026.md` as serious earlier analyses of the `*skúldru -> sċuldor` option and the plural-to-singular / back-formation question; Bosworth-Toller, Clark Hall, Campbell, Brunner, Luick, Kroonen, Orel, and Ringe-Taylor as quoted or searchable in the repo; and the packet's note that the row is a DatPl encoding rather than a citation-form entry.
- **Stale or superseded as live row authority:** the packet's older `DEV_NOTES.md:39943-39945` plan to retarget the row to `*skúldru -> sċuldor`; and the recommendation-level conclusions in the older cell-choice / lautgesetz dossiers, which remain worth discussing as alternative analyses but no longer describe the current TSV solution.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `shoulder -> sċuldra`, which is real lexical background but not the current row target; and concept-only `eaxl / *ahslu` hits, which concern a different OE shoulder lexeme.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`, especially the live §17.41 section and its historical/retracted subsections.
- `Germanic/docs/dossier-shoulder-paradigm-survey-2026.md`.
- `Germanic/docs/dossier-shoulder-2026.md`.
- `Germanic/docs/dossier-shoulder-cellchoice-2026.md`.
- `Germanic/docs/dossier-shoulder-lautgesetz-2026.md`.
- `Germanic/tools/oe_paradigm_probe.py` (no built-in shoulder probe yet).
- `Germanic/data/oe_known_problems.tsv` (no entry for this row).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt`.
- `docs/references/luick_historische_grammatik.txt`.

This extra pass matters because the repo preserves several real shoulder analyses, not just noise. The current row is not the older `*skúldrō -> sċuldra` row, but the intermediate `*skúldru -> sċuldor` option was a genuine philological/project option and remains worth noting even though the project ultimately went with the DatPl row.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*skuldrō` is the project's cross-row headword for the Germanic cognate set. Repo reference material is not fully uniform here: Kroonen gives `*skuldra- m.`, Orel gives `*skuldr(j)ō`, and Ringe-Taylor discuss PWGmc `*skuldru` as the stage relevant for OE `sculdor`. So TSV `PROTO` should be read as project headword shorthand, not as the exact staged form fed into the OE derivation.
2. **Project input form for derivation:** TSV `PROTOFORM` `*skúldramiz` is the current derivational input. `DEV_NOTES` is explicit that this is the **PGmc-proper** DatPl/InstrPl shape with thematic `*-a-` plus `*-amiz`, chosen before NWGmc `a > u / _m`. It is therefore distinct from the earlier exploratory `*skúldru` proposal and from the post-raising diagnostic form `*skúldrumiz`.
3. **OE target form:** `sċuldrum` is the attested OE dat.pl. target represented by the row. It is not the citation lemma `sculdor`, and it is not the late weak-feminine singular `sċuldra`.

So the live row is coherent: `PROTO` names the cognate set, `PROTOFORM` names the selected derivational paradigm cell, and `COUNTERPART` names the corresponding OE inflected form.

## Old English philology

The philology is clearer than the older project history suggests.

- **Attested citation/headword:** Bosworth-Toller and Clark Hall give **`sculdor`** as the main OE lemma, masculine.
- **Attested inflected forms:** Bosworth-Toller also gives plural and oblique material including **`sculdru, sculdra, sculdrum`** and collective/i-mutated forms such as `gescyldru`; the dat.pl. `sculdrum` is therefore solid attested evidence for the current row.
- **Late analogical form:** Bosworth-Toller Supplement adds weak feminine **`sculdra, an`**. The shoulder dossier is right to treat this as a late, analogical, probably late-WS form, not as the inherited form the cascade should try to derive directly.
- **Late-WS spelling issue:** Brunner and the shoulder dossier treat **`sceoldor`** as a late-WS spelling/development after `sc-`, not as evidence that the inherited root vowel was regularly lowered to /o/ in the relevant row.

That means the safest philological framing is: the lexeme's ordinary OE headword is `sculdor`, but the current row intentionally targets the attested dat.pl. `sculdrum`, because that is the paradigm cell where the inherited phonology and the attestation converge most cleanly. The weak feminine `sċuldra` belongs in the lexeme history, and the `*skúldru -> sċuldor` option remains a plausible back-formation/plural-to-singular discussion point, but neither is the live row target.

## Project problem and solution

The project problem was that the older row conflated the lexeme's historical headword question with the row's derivational test cell. A direct singular-oriented run from `*skúldrō` produced `sċoldor`, not the older target `sċuldra`. That led to a serious alternative proposal: switch to `*skúldru -> sċuldor`, treating the singular as potentially related to a plural-based or back-formed history. The cell-choice and lautgesetz dossiers show that this was not a silly option; it was a real attempt to respect both handbook evidence and project precedent.

The current solution is still stronger for the row as now encoded: keep the cognate-set `PROTO`, but represent the row by the **masc. a-stem DatPl** `*skúldramiz -> sċuldrum`. The shoulder paradigm survey shows that this is the unique cell-consistent match across the surveyed paradigm, and `DEV_NOTES` records that the cascade now verifies it. In other words, the row no longer asks the analogical weak feminine or the debated singular history to carry the modelling burden; it uses the inherited plural oblique cell where the FST and the attested OE form actually agree.

`late_analogy` still makes sense for the row, because the row's special handling is driven by the lexeme's analogically reshaped singular history even though the chosen DatPl cell itself is the regular/inherited escape hatch.

## Paradigm probe

A paradigm probe **is required** for a `late_analogy` row of this type, but the reusable built-in probe is still missing: `Germanic/tools/oe_paradigm_probe.py` has no shoulder spec yet.

The good news is that the repo already contains the substantive probe work in `dossier-shoulder-paradigm-survey-2026.md` and the later `DEV_NOTES` verification. So no new philological investigation is needed before the final report, but the missing reusable probe should cover at least these cells:

- **masc. a-stem NSg** `*skúldraz` -> expected non-match (`sċoldor` vs attested `sculdor`);
- **post-shortening singular/plural comparison cell** `*skúldru` -> `sċuldor`, to keep the plural-to-singular / back-formation option visible as a real alternative rather than a discarded absurdity;
- **masc. a-stem DatPl** `*skúldramiz` as the winning row input;
- optionally the accepted DatPl variants discussed in the dossier (`*skúldrumiz`, `*skúldrumaz`, `*skúldrum`) once the probe/gate supports them;
- **weak fem. singular control** for `sċuldra`, only to show that it is analogical and not the winning inherited cell.

## Recommended final report

Recommend a concise final report that says row 2183 now represents the attested OE dat.pl. `sċuldrum`, not the lemma `sculdor` and not the late weak-feminine `sċuldra`; that it keeps `PROTO = *skuldrō` as the cognate-set headword; that it uses `PROTOFORM = *skúldramiz` as the selected PGmc DatPl input because this is the cell where the project's OE cascade and the attested evidence align; and that it briefly notes `*skúldru -> sċuldor` as a serious alternative considered during the dossier stage but not the final row choice.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. The philological literature varies (`*skuldra-`, `*skuldr(j)ō`, PWGmc `*skuldru`), but the current `PROTO` still functions acceptably as the project cognate-set headword.
- **TSV `PROTOFORM`:** no change recommended. `*skúldramiz` is the right current derivational input for the row.
- **TSV `COUNTERPART`:** no change recommended. `sċuldrum` is the right OE target for the current analysis.
- **TSV `DERIVATION_CLASS`:** no change recommended. `late_analogy` remains defensible for a row whose special handling is driven by the lexeme's analogical singular history.
- **TSV `NOTE`:** **change recommended.** The present note explains the `*-amiz` encoding, but it should also say explicitly that the row targets the attested masc. a-stem DatPl `sċuldrum` and that older `sċuldra` and `sċuldor` proposals remain background alternatives rather than the live row analysis.
- **`oe_known_problems.tsv`:** no change recommended. This is no longer an unmodelled failure row.
- **`DEV_NOTES` / dossier text:** **change recommended.** Older shoulder materials should be marked even more explicitly as superseded **as live row recommendations** while still preserving the `*skúldru -> sċuldor` path as a serious alternative analysis. The packeting system is still surfacing that older recommendation-level history in a way that can look more current than it is.

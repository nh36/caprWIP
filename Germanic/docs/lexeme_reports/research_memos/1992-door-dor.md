# Research memo — 1992 door / dor

## Starting point

- **ID / concept / counterpart:** 1992, **door**, **dor**.
- **TSV `PROTO`:** `*dúrą`.
- **TSV `PROTOFORM`:** `*dúrą`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** OE has two reflexes, neuter a-stem `dor` and feminine `duru`; the row intentionally targets etymological `dor` as the regular reflex of `*dúrą`.
- There is **no pilot lexeme report** for this row at present, so the memo has to rely on the packet plus wider repo evidence rather than treating any prior report as authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the compact derivation trace are current and mutually consistent: the project now runs `*dúrą` / `*dúrą` to `dor`, and the FST output matches that target.
- **Useful background:** the packet's embedded `DEV_NOTES` section `OE duru 'door': Stem-Class Correction` is still the key repo-local explanation for why the row was retargeted from `duru` to `dor`; the Clark Hall and Ringe-Taylor snippets in that section are also useful background for the coexistence of the two OE lexemes.
- **Stale or superseded:** the packet's supplementary `old_english_wiktionary.tsv` hit (`door -> duru`) is real lexicographic background, but it is not the governing row state and should not override the implemented TSV decision. Likewise, the shoulder dossiers only cite `duru/dor` as precedent, not as fresh row-specific evidence.
- **Irrelevant or misleading if taken at face value:** the generic `u-lowering` dossier/analysis hits in the packet are mostly about other lexemes; they matter only indirectly here, because row 1992 is **not** a live `u-lowering exception` case once the target is `dor`.

## Additional repo research

Files checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the full `OE duru 'door': Stem-Class Correction` section.
- `Germanic/docs/dossier-shoulder-2026.md` and `Germanic/docs/dossier-shoulder-cellchoice-2026.md`, which cite row 1992 as a project precedent for target correction.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/ringe_vol1_pie_to_pgmc.txt`.
- Direct FST verification with `flookup -i old_english.bin` for `durą` and `duruz`.

Main findings from that wider pass:

- `oe_known_problems.tsv` has **no live entry** for this lexeme, which fits the current view that row 1992 is now a solved stem-class targeting issue rather than an unresolved exception.
- Kroonen is the clearest repo-local comparative source for the split: `*dura-` yields OE `dor`, while OE `duru` belongs with a different feminine line (`*durō-`; alongside the wider `*duri-` plural tradition in other Germanic languages).
- Ringe & Taylor, Campbell, and Brunner all support treating OE `duru` as a genuine u-stem noun in Old English morphology, not merely an orthographic variant of `dor`.
- Clark Hall has separate entries for `dor` and `duru`, confirming that the project is choosing between two distinct OE lexemes/stem histories, not between two spellings of one headword.
- The FST confirms the row logic directly: `durą -> dor`, while `duruz -> duru` is also derivable if one intentionally switches to a u-stem input.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction even though the current TSV uses the same string in `PROTO` and `PROTOFORM`.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*dúrą`, corresponding to Kroonen's `*dura-` neuter 'gate, (single) door'. This is the etymological source of OE `dor`.
2. **Project input form for OE derivation:** TSV `PROTOFORM` is also `*dúrą`. That is deliberate: the row is currently set up to model the regular a-stem/neuter reflex, not the later feminine/u-stem lexeme.
3. **OE target form:** `dor`, the OE form the row is intended to represent.

Important non-current or alternative forms should be kept separate from that live row structure:

- `*duri-` is a comparative cognate-set branch for the widespread plural/feminine "door" forms elsewhere in Germanic, but it is **not** the current OE modelling input for row 1992.
- Kroonen explicitly says OE `duru`, OFri. `dore`, and OHG `tura` go back to `*durō-`; this is background evidence for the alternative OE lexeme, not a reason to rewrite the live row.
- `*duruz` appears in `DEV_NOTES` as a possible modelling input if the project wanted to target OE `duru`. That proposal is diagnostic background only; it is not the current TSV choice.

So the present row does **not** collapse `PROTO`, modelling input, and target accidentally. Rather, it intentionally keeps all three aligned on the etymological `dor` line and relegates `duru` to note/report prose as a parallel OE reflex.

## Old English philology

- **Attested vs. reconstructed:** both `dor` and `duru` are supported in repo-local lexicographic materials as Old English forms. The current target `dor` is therefore not a reconstructed convenience form; it is an attested OE noun.
- **Citation form vs. inflected evidence:** Clark Hall gives separate entries for `dor` and `duru` and preserves inflectional information for both. That matters because the row is choosing a citation form tied to one inflectional history, while the note also mentions the other.
- **Morphological status:** Ringe & Taylor explicitly list `duru` among the surviving early OE u-stems, and Campbell/Brunner likewise treat `duru` as a u-stem class member. The memo should therefore not describe `duru` as just a later spelling of `dor`; it is a distinct feminine stem-class outcome.
- **Dictionary/headword issue:** the supplementary lexical table `old_english_wiktionary.tsv` only gives `duru` for “door”. That is useful philological background, but it is incomplete for the project's purposes, because repo-local dictionary sources also attest `dor` 'door, gate'.
- **Dialect/manuscript status:** the checked repo-local sources support the lexical split and stem-class split, but they do not require the memo to make a stronger manuscript-or-dialect claim than that. The safe statement is simply that OE has attested `dor` and attested `duru`, with different morphological affiliations.

## Project problem and solution

The project problem was originally a mismatch between etymology and target selection. A row built as `*durą -> duru` implicitly mixed an a-stem/neuter proto with a feminine u-stem outcome, so the FST quite correctly returned `dor` instead.

The implemented project solution is therefore sound:

- keep `PROTO = *dúrą` as the cognate-set proto represented by the row;
- keep `PROTOFORM = *dúrą` as the OE derivational input;
- keep `COUNTERPART = dor` as the regular attested reflex of that input;
- mention `duru` only as the other OE reflex/stem history, not as the row's main target.

If the project ever wants to model the feminine noun directly, it should do so as a separate row or explicitly separate modelling target, not by reusing the current `*durą` row. In other words, row 1992 is best understood as a **target-choice correction**, not as an unresolved sound-law problem.

## Paradigm probe

**No paradigm probe is required for the current row.**

The live issue is not an uncertain OE paradigm-cell choice of the `late_analogy` type; it is the prior decision about which lexeme/stem history the row should represent. Once the row is defined as `*dúrą -> dor`, the derivation is regular and already confirmed by the FST.

If the project later decides to open a separate `duru` treatment, the cells worth probing would be the u-stem noun's NomSg, GenSg, DatSg, Nom/AccPl, and DatPl, because those are the cells directly discussed in Campbell, Brunner, and the dictionary material for `duru`. But no such probe is needed for the present `dor` row.

## Recommended final report

Recommend a concise final report that treats row 1992 as the **etymological neuter/a-stem line** `*dúrą -> dor`, states explicitly that OE also has a separate feminine/u-stem `duru`, and explains that the project chose the regular attested reflex `dor` rather than mixing stem classes inside one row.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is right for the live `*dúrą -> dor` treatment.
- **TSV `NOTE`:** no change recommended. The existing note already captures the essential project decision and correctly preserves `duru` as background rather than target.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no change required. The main `DEV_NOTES` section is still current for the row's implemented decision, and the shoulder dossiers use it appropriately as precedent rather than as competing authority.

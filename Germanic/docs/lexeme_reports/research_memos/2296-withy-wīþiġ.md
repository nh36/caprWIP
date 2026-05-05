# Research memo — 2296 withy / wīþiġ

## Starting point

- **ID:** 2296
- **CONCEPT:** withy
- **COUNTERPART:** wīþiġ
- **PROTO:** *wáiθiz
- **PROTOFORM:** *wḯθagą
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Campbell §275(7), §376: OE -ig < PGmc *-ag- (cf. *xúnagą → huniġ); see DEV_NOTES §17.10.35 and notable_findings §9. Wiktionary/Kluge *wīþja- cannot derive -ig (heavy ja-stem yields -e/-Ø).

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row and the compact derivation trace are current: the row now distinguishes cognate-set `PROTO = *wáiθiz` from OE modelling input `PROTOFORM = *wḯθagą`, and the current cascade yields `wīþiġ`.
- The later `DEV_NOTES` closure at `§17.10.35` is the decisive project statement. It explicitly rejects older `*wīθijaz` / `*wīþja-` input as the wrong OE derivational analysis and replaces it with the `*-ag-` solution.

**Useful background but not final authority:**

- The older 2026-03-19 `DEV_NOTES` section is useful for reconstructing why the project first treated the row as a Sievers-law / ja-stem problem.
- `analysis/notable_findings.md` §9 is a good background synthesis of the mismatch, but it predates the later row-level closure.
- The packet’s lexical-table material is useful supplementary confirmation that OE `wīþiġ` is a real dictionary headword.

**Stale or superseded material inside the packet:**

- The packet still surfaces older material that assumes `*wīθijaz` is the live `PROTOFORM` and that the repair should come from changing syncope behavior. That is superseded by the later `*-ag-` analysis.
- The diagnostic traces `*wīθijăz -> wīþ` and `*wīθijăz -> wīþeġ` are project-history bug states, not current evidence about the row’s intended input.
- The packet’s Kluge/Wiktionary-derived ja-stem pathway is still valuable as comparative background, but it is superseded as an OE modelling choice.

**Irrelevant or misleading if weighted too heavily:**

- Generic packet/debug-snapshot hits that merely repeat the current output `wīþiġ` without discussing the suffix problem do not add philological value.
- Cross-row keyword hits about syncope or palatalization elsewhere in the repo should not be treated as row-specific authority.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`:
  - the older 2026-03-19 section `OE wīþiġ 'withy': ja-stem Adjective vs Sievers' Law Syncope`;
  - the later closure `§17.10.35`.
- `Germanic/docs/analysis/notable_findings.md` §9.
- `Germanic/docs/analysis/fryhtu_investigation.md` for the older diagnostic use of `wīþiġ` in the syncope test battery.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/data/old_english_wiktionary.tsv`.
- Reference excerpts in:
  - `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`;
  - `docs/references/legacy/orel_handbook_germanic_etymology.txt`;
  - `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`;
  - `docs/references/luick_historische_grammatik.txt`.

No dedicated withy-specific dossier file or pilot lexeme report was found in the repo.

Main findings from that wider check:

- `old_english_wiktionary.tsv` and Clark Hall both support OE `wīþiġ / wiðig` as a real headword; this is not a reconstructed-OE target.
- Kluge explicitly groups OE `wīþig` under a comparative Germanic `*wīþja/ō-` headword, but that reconstruction is best treated as cognate-set shorthand, not as a sound-law-clean OE derivational input.
- Orel reconstructs related feminine forms `*wiþiz` and `*wiþjōn`, not the OE masculine `-ig` noun itself; that supports the idea that the OE form is a secondary derivative within the family rather than a direct reflex of one inherited headword.
- Luick and the older `DEV_NOTES`/Bülbring material confirm that OE `wipiz`/`wiðig` belongs to the `-ig` phonological shape, which aligns with Campbell’s `*-ag- > -ig` account.
- `oe_known_problems.tsv` has no live entry for this row, which is appropriate now that the current `PROTOFORM` matches the target.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction kept explicit.

1. **Cognate-set proto:** `*wáiθiz` is the TSV’s comparative etymological headword for the wider lexeme family.
2. **Project input form for OE derivation:** `*wḯθagą` is the row’s OE-specific modelling input. It is not just a respelling of the cognate-set proto; it is the derivational form chosen because it produces the OE target through the project’s current sound-change cascade.
3. **OE target form:** `wīþiġ` is the attested OE citation form represented by the row.

The important reconstruction point is that the rejected `*wīθijaz` / `*wīþja-` analysis belongs to comparative background, not to the live OE derivation. A heavy ja-stem pathway explains why earlier project history expected suffix loss; it does **not** explain the actual OE `-ig` target. Campbell’s `*-ag-` pathway is the only repo-local analysis that currently survives end-to-end derivational checking.

The root-vowel question is secondary here. Kluge supports long `ī`, and the current row already uses long `ī` in the target and in `*wḯθagą`. Repo-local evidence does not require changing that part of the analysis in order to solve the suffix problem.

## Old English philology

- **Attested vs. reconstructed:** this is an attested-OE row. Repo-local lexical sources support `wīþiġ / wiðig`; the row is not a reconstructed-WS substitute of the kind seen in `reconstructed_oe` cases.
- **Citation form vs. inflected form:** the row targets the citation/headword noun, not a paradigm-dependent oblique cell. Clark Hall gives `wiðig, wiði(g)e m.`, which confirms the lexeme while also showing minor lexical-form variation.
- **Orthographic and normalization issues:** dictionary support appears with both `þ` and `ð`, and older reference files often omit macrons. Those spelling differences do not outweigh the current normalized project target `wīþiġ`.
- **Dialect/manuscript status:** repo-local evidence supports the word’s existence and headword status, but it does not justify strong new dialect claims for this memo. The main philological issue is suffix history, not dialect assignment.
- **Headword issue:** Kluge’s cognate-set `*wīþja/ō-` and Orel’s related feminine reconstructions are comparative-etymological headings; the OE headword represented here is the masculine `wīþiġ` type.

## Project problem and solution

The project problem was created by importing a tidy comparative reconstruction (`*wīθijaz` from the Kluge/Wiktionary line) into a row whose OE target is not its regular outcome. Once the FST treated the form as a heavy ja-stem, the suffix was correctly lost, yielding bare `wīþ` or earlier diagnostic `wīþeġ`-style intermediate expectations. In other words, the older mismatch was not primarily a missing sound rule; it was a wrong morphological input.

The current solution is coherent and should be preserved:

- keep `PROTO = *wáiθiz` as the cognate-set proto;
- keep `PROTOFORM = *wḯθagą` as the OE modelling input;
- keep `COUNTERPART = wīþiġ` as the attested OE target;
- keep `DERIVATION_CLASS = early_analogy`, because the row represents an OE-side derivative/reshaping relative to the broader inherited family, not a direct bare reflex of the comparative ja-stem headword.

So row 2296 is no longer a live Sievers-law bug. It is a case where the project had to separate the comparative headword tradition from the OE derivational form that actually yields the attested noun.

## Paradigm probe

A paradigm probe is **not required** for the row’s current treatment.

This is not a paradigm-cell selection problem. The decisive issue is the choice of derivational input (`*-ag-` derivative vs. heavy ja-stem), and the current input already derives the citation form directly.

If the project later reopens the rejected ja-stem analysis for explanatory comparison, the cells worth probing would be heavy ja-stem masculine **nom.sg.**, **gen.sg.**, and **nom./acc.pl.** forms against the superseded `*wīθijaz` pathway. But that probe is not needed to support the current row.

## Recommended final report

Recommend a concise final report that treats `wīþiġ` as an attested OE noun kept under `early_analogy`: distinguish the cognate-set `PROTO` from the OE `PROTOFORM`, explain that Campbell’s `*-ag- > -ig` account is the only repo-local derivation that reaches the target cleanly, and mention the older `*wīþja-` / Sievers-law discussions only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no essential change recommended. The live note already states the current conclusion clearly enough.
- **`oe_known_problems.tsv`:** no change recommended. The row should remain absent from the known-problems ledger because the current derivation already matches.
- **`DEV_NOTES` text:** light cleanup recommended. The older 2026-03-19 `*wīθijaz` / Sievers-law section should be marked more explicitly as superseded by `§17.10.35`, since packet generation still surfaces both.
- **Dossier text:** no change recommended; no separate withy-specific dossier file was found.

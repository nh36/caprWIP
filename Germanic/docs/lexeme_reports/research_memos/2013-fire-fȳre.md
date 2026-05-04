# Research memo — 2013 fire / fȳre

## Starting point

- **ID:** 2013
- **CONCEPT:** fire
- **COUNTERPART:** fȳre
- **PROTO:** *fūri
- **PROTOFORM:** *fūri
- **DERIVATION_CLASS:** known_unmodelled
- **NOTE:** The live TSV note says inherited dat.sg. `*fūri` triggers i-umlaut and then loses final `*-i` by high-vowel apocope, so the regular phonological outcome is `fȳr`; attested `fȳre` is explained as later analogical restoration of dative `-e` by proportion with regular a-stems.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row and the matching `oe_known_problems.tsv` entry agree on the current project state: `*fūri` is being kept as a documented exception because the FST's `fȳr` output is historically regular, while `fȳre` reflects later analogical remodeling.
- The packet's compact derivation trace is current and useful: it accurately localizes the regular derivation at `*fūri > *fȳri > fȳr`.
- The packet's main `DEV_NOTES` hit (`§` beginning at line 6169) is still the core repo discussion of why the row behaves this way.

**Useful background but not final authority:**

- `pilot/fire.md` is a good short background summary, especially on the need to distinguish lexeme headword, project input cell, and OE target form, but it is still only pilot prose.
- The packet's lexical-table support for `fȳr` from `old_english_wiktionary.tsv` and `old_english_swadesh.tsv` is useful for citation-form orientation, not for settling the row by itself.
- `compound_archaism_inventory.md` is helpful background on the project's broader oblique-cell methodology, but it is a later synthesis document, not the primary evidential dossier for this row.

**Stale or superseded material inside the packet:**

- The packet reproduces the March 2026 `DEV_NOTES` recommendation to change the target to `fȳr` (Option A). That is important project history, but it is no longer the live project decision, because the current TSV row, packet, `oe_known_problems.tsv`, and pilot report all preserve `fȳre` as a documented analogical mismatch rather than adopting a retargeting fix.
- The packet therefore preserves a real chronological split: earlier repo discussion pushed toward target replacement, while the current repo state treats the row as intentionally `known_unmodelled`.

**Irrelevant or misleading packet material:**

- The `DEV_NOTES` line 30617 table hit marked `irrelevant` is diagnostic only and adds no evidence about the row beyond confirming that the packet search found the ID.
- Generic keyword collisions on `i-umlaut` or `dat.sg.` elsewhere in the packet are not row-specific evidence and should not be promoted to equal status with the dedicated fire discussion.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at `§` 6169-6315, including the later four-part-analogy addendum.
- `Germanic/data/oe_known_problems.tsv`, which now explicitly records `*fūri` under `analogical_dat_e`.
- `Germanic/docs/lexeme_reports/pilot/fire.md`, treated as background only.
- `Germanic/docs/analysis/compound_archaism_inventory.md`, Case 7, which frames `fȳr/fȳre` as a paradigm-cell preservation case.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv`, both of which give `fȳr` as the lexical headword/citation form.
- Direct repo search across `Germanic/docs/analysis/` and `Germanic/docs/dossiers/` for `fȳr`, `fȳre`, and `*fūri`.

That wider search did **not** uncover a dedicated fire dossier beyond the packet's cited `DEV_NOTES` discussion. The main additional repo evidence is therefore the newer `oe_known_problems.tsv` normalization of the issue and the methodological synthesis in `compound_archaism_inventory.md`.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

- **Cognate-set proto / etymological headword:** not `*fūri`, but the inherited fire lexeme represented in Kroonen as heteroclitic `*fōr ~ *fun-` (with the older pre-Germanic background also discussed in `DEV_NOTES`).
- **Project input form for OE derivation:** `*fūri`, i.e. the inherited oblique cell descended from PGmc/PWGmc dative-locative material `*fu(w)eri`, because that is the cell whose `*-i` explains the OE umlaut.
- **OE target form represented by the row:** `fȳre`, the attested dative singular with analogically restored `-e`; this is distinct from attested citation-form `fȳr`.

That means the live TSV currently collapses `PROTO` and `PROTOFORM` into the same oblique form. The derivational choice `PROTOFORM = *fūri` is defensible; the etymological headword slot `PROTO = *fūri` is not ideal, because it hides the heteroclitic lexeme-level reconstruction behind one selected paradigm cell.

The early-stage sequence accepted by the current repo is coherent: oblique `*fu(w)eri`/`*fūri` gives umlauted `*fȳri`, high-vowel apocope yields `fȳr`, and only then does later analogical pressure restore dative `-e` to produce attested `fȳre`.

## Old English philology

This is **not** a reconstructed-OE row. Both `fȳr` and `fȳre` are treated in the repo as real Old English forms, but they belong to different functional slots.

- `fȳr` is the ordinary citation/headword form in the lightweight lexical tables checked here.
- `fȳre` is the oblique/dative form targeted by the row.
- The row should therefore not imply that `fȳre` is the default lemma or that `fȳr` is merely an unattested intermediate.

Philologically, the crucial point is that `fȳre` is **attested but not phonologically primary** in the derivation. The sound-law output of the chosen input is `fȳr`; the final `-e` belongs to later paradigm remodeling after the noun had effectively joined regular neuter a-stem behavior. The memo should also avoid overstating stem-class certainty from secondary synthesis files: the secure repo claim is the analogical restoration itself, not a fully settled new stem-class reconstruction for every OE stage.

## Project problem and solution

The project problem is not whether the FST is wrong about the phonology. It is whether the row should target the regular inherited output or the later analogical OE form.

The current repo-level solution is better than the older retargeting proposal:

- keep `PROTOFORM = *fūri` so the row still encodes the umlaut-triggering oblique input;
- keep `COUNTERPART = fȳre` so the row still records the attested OE dative form the project wants to discuss;
- keep `DERIVATION_CLASS = known_unmodelled`, because the mismatch is historically understood but not generated by the present FST;
- explain explicitly that the FST's `fȳr` is the correct inherited output and that `fȳre` is a later analogical restoration.

In other words, row 2013 should remain a documented analogical-exception case, not be silently rewritten into a clean regular match.

## Paradigm probe

A paradigm probe is **required in principle**, because the analysis depends on contrasting paradigm cells rather than on a simple one-form derivation. But the existing evidence is only partially probed: `pilot/fire.md` gives a minimal hand-specified dat.sg. comparison and explicitly omits the wider paradigm contrast.

If the probe is refreshed or expanded for the final report, it should include at least these cells:

- **nom./acc.sg.** lexeme headword cell (`*fōr`, or the project's nearest usable citation-form surrogate) to show that the headword itself does not supply the umlaut trigger;
- **dat./loc.sg.** `*fu(w)eri > *fūri` to show the unique umlaut-triggering cell and the regular FST path to `fȳr`;
- **gen.sg.** `*funins` (or project-normalized equivalent) as a control cell showing that other obliques do not explain `ȳ`.

If the toolchain cannot probe those older forms automatically, the final report should still include a small hand-specified comparison table. The current one-cell pilot probe is not quite enough on its own.

## Recommended final report

Recommend a concise final report that keeps row 2013 as a source-dense `known_unmodelled` case: distinguish lexeme-level proto `*fōr ~ *fun-` from derivational input `*fūri`, say that the regular inherited OE outcome is `fȳr`, and explain that target `fȳre` is an attested dative with post-apocope analogical `-e` restoration. The older proposal to retarget the row to `fȳr` should be mentioned only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** **yes, change recommended.** Replace the current cell-specific `*fūri` with the cognate-set lexeme headword, ideally `*fōr` (or, if the field can tolerate it, a clearer heteroclitic notation such as `*fōr ~ *fun-`).
- **TSV `PROTOFORM`:** **no change recommended.** Keep `*fūri` as the project input form for derivation.
- **TSV `COUNTERPART`:** **no change recommended.** Keep `fȳre`; the current repo state prefers documenting the attested analogical dative rather than retargeting to `fȳr`.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `known_unmodelled` still fits better than `late_analogy`, because the analogical restoration is understood but not generated.
- **TSV `NOTE`:** **yes, light cleanup recommended.** The note should explicitly distinguish lexeme-level `PROTO` from row-level `PROTOFORM`, and it should mention that `fȳr` is the citation/headword form while `fȳre` is the targeted attested dative.
- **`oe_known_problems.tsv`:** **no essential change recommended.** Its current `analogical_dat_e` entry matches the best current understanding.
- **`DEV_NOTES` text:** **yes, light cleanup recommended.** The March 2026 section should be marked more explicitly as superseded where it recommends changing the target to `fȳr`, since the live project state now keeps `fȳre`.
- **Dossier text:** no fire-specific dossier text change is currently required, because direct repo search did not uncover a separate fire dossier. If `compound_archaism_inventory.md` is revised later, its fire case could be tightened so the heteroclitic lexeme-level reconstruction is stated more carefully, but that is optional background cleanup rather than a required fix.

# Research memo — 1946 berry / berġes

## Starting point

- **ID:** 1946
- **CONCEPT:** berry
- **COUNTERPART:** berġes
- **PROTO:** *bázją
- **PROTOFORM:** *bázjas
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** Note: using gen.sg. *bazjas (> berġes); R/T vol.2 §6.8.2: *rj did not geminate in PWGmc

The live TSV already treats this as a paradigm-cell row rather than a straight citation-form match. A pilot report exists at `Germanic/docs/lexeme_reports/pilot/berry.md`, but it is background only, not final authority.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing the current successful input `*bázjas -> berġes`; the packet's pilot paradigm probe showing `*bázją -> bere` versus `*bázjas -> berġes`; and the live `oe_paradigm_probe.py` pilot spec confirming that the row is intentionally framed as a nom.sg./gen.sg. comparison.

**Useful background:** the packet's excerpts from `DEV_NOTES.md` and `analysis/notable_findings.md` on word-final `*ja/*ją -> *i` after a light syllable; the packet's methodological parallels about oblique-cell targeting in `compound_archaism_inventory.md`; and the manifest notice that `pilot/berry.md` already exists.

**Stale or superseded:** the packet's older berry diagnostics that still aim at citation-form OE `berġe` (or earlier `bere`) from `*bázją`, especially `analysis/final_vowel_missing_analysis.md` and the older February 2026 `DEV_NOTES.md` berry trace. Those files document project history, but they predate the current row-level solution of targeting the gen.sg. cell `*bázjas`.

**Irrelevant or misleading:** the packet's supplementary lexical-table hit `old_english_wiktionary.tsv: berry -> berġe`, which is useful for the dictionary/citation form but not direct evidence for the target `berġes`; and broad "gen.sg." hits for unrelated lexemes, which are parallels only.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/lexeme_reports/pilot/berry.md` — useful background, but not final authority.
- `Germanic/docs/DEV_NOTES.md` at 1374-1383, 1500-1548, and 2541-2547 — confirms both the current `*j` chronology and the older pre-row-update berry diagnostics.
- `Germanic/tools/oe_paradigm_probe.py` — confirms the existing probe is hand-specified and currently compares only nom.sg. and gen.sg.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 1946 / `*bázją` / `*bázjas`.
- `Germanic/data/old_english_wiktionary.tsv` — gives citation/headword-style `berġe`, not `berġes`.
- `Germanic/docs/analysis/final_vowel_missing_analysis.md`, `Germanic/docs/analysis/notable_findings.md`, and `Germanic/docs/analysis/compound_archaism_inventory.md` — useful for chronology and methodology, but not equally current.

`DEV_NOTES.md` also points to `session/files/pwgmc_berry_investigation.md`, but no such file is present in the repository, so it cannot be treated as live evidence for this memo.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*bázją`, i.e. the PGmc berry lexeme as represented for the cognate set.
2. **Project derivational input:** TSV `PROTOFORM` `*bázjas`, a selected **gen.sg.** paradigm cell.
3. **OE target form:** `berġes`, likewise a **gen.sg.** target, not the citation lemma.

The repo's older berry dossiers mostly focused on whether citation-form `*bázją` should yield OE `berġe` and how early West Germanic `*j` vocalisation and rhotacism should be ordered. That is useful history, but the live row now solves the OE matching problem differently: the decisive input is not the lexeme headword but the genitive singular `*bázjas`. The note's reference to Ringe-Taylor §6.8.2 matters because it blocks a fake solution via hidden `*rj` gemination; the row instead relies on paradigm choice, not an extra sound change.

## Old English philology

The checked repo-local lexical evidence supports a berry lemma/citation form `berġe`, but the exact target `berġes` is not separately documented in the materials reviewed with the same directness. So the safest philological description is:

- **citation/headword side:** `berġe` in the supplementary lexical table;
- **selected inflected cell:** `berġes`, the row's chosen gen.sg. target;
- **project status of `berġes`:** a regular/inferred OE paradigm cell in current project usage unless a stronger direct citation is added elsewhere.

That means the final report should not present `berġes` as though it were simply the normalized dictionary headword. It is an inflected OE form used because it preserves the derivational contrast the project wants to model.

## Project problem and solution

The project problem is the mismatch between the cognate-set headword and the OE form that the current cascade can derive cleanly. Older project history kept trying to make citation-form `*bázją` line up with a citation-form OE outcome (`berġe`/`bere`), but the live row instead adopts a paradigm-cell solution: keep `PROTO = *bázją` as the lexeme-level headword, set `PROTOFORM = *bázjas` as the derivational input, and target OE gen.sg. `berġes`.

So this `late_analogy` row is best understood as: "berry, represented for CAPR purposes by a conservative/inherited gen.sg. cell." The row is not claiming that `*bázjas` is the lexeme-level proto, and it should not be read as if `berġes` were the citation lemma.

## Paradigm probe

A paradigm probe **is required** for a `late_analogy` row of this type, and one already exists. The current probe is sufficient for the core decision because it tests the decisive contrast:

- **nom.sg.** `*bázją -> bere` (non-match)
- **gen.sg.** `*bázjas -> berġes` (match)

No additional probe is required before the final report. If later expansion is wanted for completeness, the next cells to probe would be **dat.sg.** and **nom./acc.pl.**, since the current pilot explicitly omits dative and plural cells.

## Recommended final report

Recommend a concise final report that says row 1946 keeps PGmc lexeme-level `*bázją` but uses gen.sg. `*bázjas` as the project input, because the selected OE target is inflected `berġes`, not the citation lemma. It should explicitly distinguish current row evidence from the older `berġe`/`bere` diagnostic history and avoid stronger attestation claims for exact `berġes` than the repo currently shows.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `berġes` works as the project's selected gen.sg. target.
- **TSV `DERIVATION_CLASS`:** no change recommended; `late_analogy` still fits.
- **TSV `NOTE`:** **change recommended** — keep the gen.sg. analysis, but tighten the wording so it explicitly says `*bázją` is the cognate-set proto and `*bázjas` is the selected paradigm-cell input, not a rival lexeme proto.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended** — older berry writeups in `DEV_NOTES.md` and `analysis/final_vowel_missing_analysis.md` should be marked more clearly as pre-paradigm-cell history so future packets do not over-weight the stale `berġe`/`bere` diagnostic stage. `pilot/berry.md` can remain as background, but later final prose should not silently inherit any stronger philological claims than the repo currently supports.

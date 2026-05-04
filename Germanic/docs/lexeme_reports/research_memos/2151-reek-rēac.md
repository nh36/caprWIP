# Research memo — 2151 reek / rēac

## Starting point

- **ID / concept / counterpart:** 2151, **reek**, **rēac**.
- **TSV `PROTO`:** `*ráukiz` (the cognate-set etymological proto retained for the wider family).
- **TSV `PROTOFORM`:** `*ráukaz` (the project input form now used for the OE row).
- **`DERIVATION_CLASS`:** `reconstructed_oe`.
- **Current TSV note:** the row was retargeted on 2026-04-30 from attested `rēc` to reconstructed West Saxon `rēac`, because the cascade already derives `rēac` regularly from `*ráukaz`, whereas deriving attested `rēc` would require a smoothing rule that would damage ordinary WS `ēa` outcomes.
- A pilot report already exists (`Germanic/docs/lexeme_reports/pilot/reek.md`), but it is background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the packet’s live TSV row and compact derivation trace are current for the row as it now stands: cognate-set `*ráukiz`, OE input `*ráukaz`, target `rēac`, class `reconstructed_oe`.
- **Useful background:** the packet’s older `DEV_NOTES` excerpts are still useful for reconstructing the abandoned `rēc` analyses, especially the rejected `*rōkiz` workaround and the discussion of smoothing.
- **Stale or superseded:** much of packet §17.22 evidence is historical rather than current. In particular, the `*rōkiz` recommendation in `DEV_NOTES` §17.22.13 is explicitly withdrawn later, and the packet does not surface the later retargeting note that now governs the row.
- **Irrelevant or misleading if taken at face value:** the packet says there are no dossier hits, even though the TSV note names `dossier-reek-2026.md`; and some “exact pair” hits are exact only for older `rēc`-target discussions, not for the row’s current `rēac` treatment.

## Additional repo research

Files checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the early background section `§17.22`, the project-status note at lines 1435-1439, and the later closure `§17.33`.
- `Germanic/docs/dossier-reek-2026.md` (full dossier named in the TSV note).
- `Germanic/docs/lexeme_reports/pilot/reek.md`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.txt` and `oe_known_problems_report.txt`.

Main findings from that wider check:

- The full dossier is important background because it makes the strongest repo-local case that attested `rēc` had **velar** /k/, not palatal /tʃ/: it cites ModE **reek**, OE `wudurēc`, derivative `rēcels`, and the weak verb `rēcan` with pret. `rēhte`.
- `DEV_NOTES` §17.33 treats attested `rēc` as an intractable Anglian-smoothing relic and withdraws the earlier `*rōkiz` solution.
- The still later project-status note at `DEV_NOTES.md:1435-1439` is the clearest current status statement: the cogset was retargeted to reconstructed WS `*rēac`, and the row now counts as a regular match under `reconstructed_oe`.
- `old_english_wiktionary.tsv` still records the attested lexical form as `rēc`, confirming that the manuscript headword and the project target are no longer the same thing.
- `oe_known_problems.tsv` currently has **no live reek entry**, so the §17.33 statement that the row was moved there is historical, not current. The debug snapshot `oe_known_problems_report.txt` preserves that earlier stage, but the source TSV no longer does.
- The pilot report already reflects the three-way distinction `PROTO` / `PROTOFORM` / OE target; it supports the current row treatment but should still be treated only as background.

## Reconstruction and early-stage forms

The row now depends on a three-level distinction that should be kept explicit:

1. **Cognate-set proto:** `*ráukiz`. This is the wider etymological headword for the lexeme family and remains useful because the non-OE family still points back to the older i-stem reconstruction.
2. **Project input form for OE:** `*ráukaz`. This is the form the project now uses to derive the OE row, following the project’s decision to treat the OE-side target as an a-stem-based, reconstruction-friendly input.
3. **OE target form:** `rēac`, understood as a **reconstructed West Saxon citation form**, not as the directly attested manuscript headword.

This also clarifies what is no longer current:

- `*rōkiz` is a **superseded project workaround**, not the current proto choice. It solved the vowel problem for attested `rēc`, but the dossier and later closure reject it because it produces palatal `rēċ`, which conflicts with the velar evidence.
- Attested `rēc` remains philologically real, but it is now treated as a later/dialectally smoothed form outside the row’s main modelling target.

## Old English philology

- **Attested vs. reconstructed:** repo-local philological material supports attested OE **`rēc`**, not attested `rēac`. The current row target `rēac` is reconstructed.
- **Citation form vs. inflected/derived evidence:** the best in-repo support for the attested lexeme comes not only from the noun headword `rēc`, but also from related forms such as `wudurēc`, `rēcels`, and `rēcan` / pret. `rēhte`, all of which support a velar stem.
- **Dialect/manuscript status:** the older packet note “attested Anglian `rēc`” is too narrow. The dossier’s survey and the repo’s supplementary lexical data treat `rēc` as attested across Anglian and WS transmission, even if the project explanation is that the smoothing type is historically Anglian and later diffused.
- **Dictionary/headword issue:** the lexicographic headword in repo-local support data is `rēc`, while the project row now intentionally targets reconstructed `rēac`. The memo should therefore keep manuscript attestation and modelling target strictly separate.

## Project problem and solution

The project problem is not “what was ever attested?” but “what should this row represent without breaking the OE cascade?”

- If the row targets attested `rēc`, the project needs either a smoothing rule or a lexical exception.
- The dossier shows why the older `*rōkiz` fix is unsound: it produces palatal `rēċ`, not the velar form required by the downstream evidence.
- `DEV_NOTES` §17.33 then treats attested `rēc` as a smoothing/lexical-diffusion problem.
- The later retargeting note resolves the modelling issue by changing the row’s intended referent: the row now stands for reconstructed WS `rēac`, which the existing cascade already derives from `*ráukaz`.

So the current project solution is:

- keep `PROTO = *ráukiz` as the cognate-set etymon;
- use `PROTOFORM = *ráukaz` as the OE modelling input;
- keep `COUNTERPART = rēac` as a reconstructed WS target;
- explain attested `rēc` in note/report prose rather than forcing it through the live FST.

## Paradigm probe

**No paradigm probe is required for the row’s current treatment.** The live issue is the choice between an attested smoothed form and a reconstructed regular WS form, not an unresolved paradigm-cell dependency inside the selected `rēac` analysis; the current row is a single reconstructed citation-form target already justified by the cascade and note.

If the project later reopens attested `rēc` as the target, a probe would then be needed for the disputed velar/palatal and smoothing history, especially NomSg, GenPl, DatPl, and derivative cells such as `rēcels` and the weak verb `rēcan` / `rēhte`. But that probe is not required for the current `reconstructed_oe` row.

## Recommended final report

The final lexeme report should present the row as a **reconstructed-WS targeting decision**: retain `*ráukiz` as cognate-set proto, state that the OE derivation is run from `*ráukaz`, mark `rēac` as reconstructed rather than attested, and mention attested `rēc` only as the philological background and the reason earlier `*rōkiz` / smoothing discussions existed.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended**. Keeping `*ráukiz` is useful because it preserves the cognate-set etymological proto distinct from the OE modelling input.
- **TSV `PROTOFORM`:** **no change recommended**. `*ráukaz` is the current project input that matches the retargeted row purpose.
- **TSV `COUNTERPART`:** **no change recommended**. `rēac` is correct for the current `reconstructed_oe` treatment.
- **TSV `DERIVATION_CLASS`:** **no change recommended**. `reconstructed_oe` is the right class for a reconstructed WS target.
- **TSV `NOTE`:** **change recommended**. It should stop calling `rēc` simply “attested Anglian” / “Anglian-only” and should fix the cross-reference to the actual later closure (`§17.33`, plus the later retargeting note), while still explaining that the project now targets reconstructed `rēac`.
- **`oe_known_problems.tsv`:** **no change recommended** for the live row. The present absence of a reek entry is consistent with the row’s retargeting away from the old mismatch bucket.
- **`DEV_NOTES` / dossier text:** **light cleanup recommended**. `DEV_NOTES` should explicitly mark the `§17.33` known-problems triage as historical relative to the later retargeting note, so future packet generation does not mix the old `rēc` triage with the current `rēac` row state. The dossier itself is still valuable as background philology, but it should be read as background to the attested-form problem, not as the final governing project decision.

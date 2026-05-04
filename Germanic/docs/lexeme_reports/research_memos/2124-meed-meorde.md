# Research memo — 2124 meed / meorde

## Starting point

- **ID / concept / counterpart:** 2124, **meed**, **meorde**.
- **TSV `PROTO`:** `*mizdō`.
- **TSV `PROTOFORM`:** `*mízdai`.
- **`DERIVATION_CLASS`:** `late_analogy`.
- **Current TSV note:** the row now targets the directly attested OE oblique `meorde` from dat.sg. `*mízdai`, treating `*mēd` as the competing doublet member and citing `DEV_NOTES` §17.24.11 plus `Germanic/docs/analysis/meord_med_chronological_review.md`.
- No pilot lexeme report exists for this row in `Germanic/docs/lexeme_reports/pilot/`; the packet is therefore only a starting dossier, not a summary of already-settled final prose.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*mízdai -> meorde`; the packet's identification of `meorde` as the current target; and the packet's notice that no `oe_known_problems.tsv` entry is live for this row.
- **Useful background:** the packet's excerpts from `DEV_NOTES` §17.24, the literature review file `meord_med_chronological_review.md`, and the correction-bannered mismatch dossiers. These are important for chronology, attestation checking, and for separating current evidence from abandoned project claims.
- **Stale or superseded:** the packet's diagnostic material built around older `mēd` or bare `meord` targeting; the early mismatch framing in `mismatch_dossier_mizdo.md`; and the supplement's now-withdrawn claim that `meord` is unattested. Those documents remain useful only because they are explicitly corrected later.
- **Irrelevant or misleading if read too quickly:** the packet's lexical-table hit from `old_english_wiktionary.tsv` (`meed -> mēd`) is headword background, not direct support for the current row target `meorde`; and packet snippets about `*meord-gifa` or DOE compound preservation belong to a confabulated earlier strand, not to the live evidence base.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`, especially §17.24.7-11.
- `Germanic/docs/analysis/meord_med_chronological_review.md` (full review named in the TSV note).
- `Germanic/docs/analysis/mismatch_dossier_mizdo.md` and `Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md` (both named in packet excerpts and both read with their correction banners in mind).
- `Germanic/docs/analysis/notable_findings.md` #11.
- `Germanic/docs/analysis/compound_archaism_inventory.md` case 1.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.

Main findings from that wider check:

- `DEV_NOTES` §17.24.10-11 is the clearest current project statement: bare nominative `meord` is reconstructed, but attested oblique `meorde` is real, and the FST already derives `*mizdai -> meorde` without rule changes.
- The chronological review is the strongest repo-local authority on the literature. It confirms direct oblique attestation (`meorde`, `meorda`), distinguishes lexicographers' reconstructed lemma `meord` from actual textual forms, and recommends the present paradigm-cell solution as the lowest-disturbance project fix.
- The mismatch dossier and supplement are **background only**. Their correction banners matter more than their original conclusions: `*meord-gifa` was confabulated, and the supplement's denial of `meord`/`meorde` attestation was wrong.
- `notable_findings.md` and `compound_archaism_inventory.md` have already partly absorbed the corrected view: this is a dialectal/doublet preservation case, not a compound-archaism case.
- `old_english_wiktionary.tsv` still gives only the citation/headword-style form `mēd`, which is useful for philological background but also shows why the current row must keep `PROTO`, `PROTOFORM`, and OE target distinct.
- `oe_known_problems.tsv` has no live entry for this row, which matches the fact that the row has already been retargeted rather than left in the unresolved-problem bucket.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*mizdō`, the lexeme-level PGmc reconstruction used for the wider cognate set.
2. **Project derivational input:** TSV `PROTOFORM` `*mízdai`, a selected **dat.sg. paradigm cell**, not a rival lexeme proto.
3. **OE target form:** `meorde`, likewise a selected **oblique OE form**, not the citation lemma for the lexeme as a whole.

The literature reviewed in `meord_med_chronological_review.md` keeps `*mizdō` as the etymological starting point but disagrees on how `mēd` arose: Campbell, Kroonen, Fulk, Crist, and Ringe-Taylor treat the `mēd` side as some kind of z-loss + compensatory-lengthening development, while Orel/Hirt prefer a PGmc-level doublet, and Kilday 2024 instead argues that `meord` is the regular inherited OE outcome and `mēd` is a Saxono-Frisian loan. None of that overturns the project's current modelling fact that `*mízdai -> meorde` already works in the cascade.

## Old English philology

- **Attested vs. reconstructed:** `meorde` (dat.sg.) and `meorda` (gen.pl.) are directly attested in the repo-local evidence; bare nominative `meord` is a lexicographer's reconstructed lemma; `mēd` is widely attested as the better-known West Saxon doublet member.
- **Citation form vs. inflected form:** the live row intentionally targets an inflected OE form, not the ordinary dictionary headword. That is the key philological fact behind the row's current shape.
- **Dialect/manuscript status:** repo-local evidence supports an Anglian-leaning profile for `meorde`/`meord`, especially OE Bede and Bright's poetic citation. But the memo should not overclaim a neat one-dialect-only distribution: the literature repeatedly describes the doublet as patchy, and Kilday's stronger distributional account is still a 2024 draft, not settled consensus.
- **Dictionary/headword issue:** lexicographers normalize `meord` from oblique evidence and cross-reference it to `mēd`; `old_english_wiktionary.tsv` keeps the everyday headword `mēd`. The row therefore should not be paraphrased as though `meorde` were simply the standard dictionary lemma.
- **Ghost-form issue:** `meord` 'reward' is real in the sense that the lexeme is genuinely evidenced by attested obliques, but `*meord-gifa` and similar compound claims are not supported and should stay excluded from final prose.

## Project problem and solution

The project problem was not whether the lexeme existed, but which OE form the row should represent without inventing a new sound law.

- Older project history treated the row as a mismatch because `*mizdō` yielded FST `meord` while the row targeted `mēd`.
- Current repo work shows that this mismatch was partly self-inflicted by mixing the cognate-set proto and the OE modelling target.
- `DEV_NOTES` §17.24.11 demonstrates that the attested oblique cell already derives cleanly: `*mizdai -> meorde`.
- The current solution is therefore to keep lexeme-level `PROTO = *mizdō`, use paradigm-cell `PROTOFORM = *mízdai`, and target attested OE `meorde`.

This means the row is best read as a **project-level paradigm-cell selection inside a real OE doublet problem**, not as a claim that the literature has settled the `mēd` vs. `meord` controversy. The row's current solution is narrower and safer: it uses a defensible PGmc cell and an attested OE output that the existing cascade already matches.

## Paradigm probe

A paradigm probe **is required** for this row, and the packet is right that a standardized `oe_paradigm_probe.py` spec is still missing even though `DEV_NOTES` already contains ad hoc FST probes.

If the probe is formalized, it should at minimum cover these cells:

- **Nom.sg.** `*mizdō -> meord` (reconstructed lemma outcome; useful contrast case).
- **Dat.sg.** `*mizdai -> meorde` (the decisive attested target cell).
- **Gen.sg.** `*mizdōz -> meorde` (important because the current cascade also converges here on the attested string).
- **Acc.sg.** `*mizdōn` and/or `*mizdą` (to show what nearby singular cells do under the live cascade).
- **Gen.pl.** the cell intended to test attested `meorda` if the grammar can now represent it cleanly; this is the major still-missing attested plural check.

So: **probe required, not yet properly codified in the probe tool.**

## Recommended final report

The final lexeme report should present row 2124 as a **paradigm-cell targeting decision within a genuine OE doublet**: keep `*mizdō` as cognate-set proto, explain that the live OE derivation runs from dat.sg. `*mízdai`, state that `meorde` is directly attested whereas bare `meord` is reconstructed, and treat `mēd` as the competing doublet whose deeper historical analysis remains literature-divided rather than fully settled by the project.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended**. `*mizdō` is still the right cognate-set proto.
- **TSV `PROTOFORM`:** **no change recommended**. `*mízdai` is the correct project input for the current row's intended paradigm-cell solution.
- **TSV `COUNTERPART`:** **no change recommended**. `meorde` is the right OE target for the current row.
- **TSV `DERIVATION_CLASS`:** **no change recommended**. `late_analogy` remains acceptable as the project's bucket for paradigm-cell targeting, even though the underlying philology is a doublet problem rather than a simple analogy story.
- **TSV `NOTE`:** **change recommended**. The note should be tightened so it states more explicitly that `meorde` is the attested oblique target, bare `meord` is reconstructed, and Kilday's loan account is a current project-facing possibility rather than settled consensus. At present the note reads slightly too much like a final verdict on the `mēd` question.
- **`oe_known_problems.tsv`:** **no change recommended**. The row is no longer best treated as an unresolved known-problem entry.
- **`DEV_NOTES` / dossier text:** **change recommended**. The correction-bannered dossiers are still useful, but `mismatch_dossier_mizdo.md`, `mismatch_dossier_mizdo_supplement.md`, and the old compound-archaism framing should be cleaned or more prominently marked as superseded project history so future packet generation does not over-weight withdrawn claims such as `*meord-gifa` or the old "meord unattested" conclusion.

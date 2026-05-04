# Research memo — 2309 make (iptv.2sg) / maca

## Starting point

- **ID:** 2309
- **CONCEPT:** make (iptv.2sg)
- **COUNTERPART:** `maca`
- **PROTO:** `*makōną`
- **PROTOFORM:** `*mákô`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** Class II weak iptv. 2sg test (R/T §5.2). Trimoric *ō → OE -a.

This is a paradigm-cell row for the Class II weak verb 'make'. The live repo also has the ordinary OE lexeme row `2117 make / macian`, whose cognate-set proto is `*mákōjaną`; row 2309 is therefore not the lemma-level make row, but a selected finite-cell companion. I found no make-specific pilot/full lexeme report in `Germanic/docs/lexeme_reports/pilot/`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace `*mákô -> maca`; the live FST implementation in `Germanic/fsts/germanic.txt` showing `{*ô}` in `OEARestorationTriggerVowel` and `OEUnstressedLongVowelShortening`; and live manual probe results confirming `*mákô -> maca`.
- **Useful background:** the packet's `DEV_NOTES` extracts at 2771-2955, which explain why imperative 2sg was explored as a regular weak-II test cell and why `*ô` had to trigger A-restoration; the neighboring row 2310 `*mákōθi -> macaþ`; and the regular lexeme row 2117 `*mákōjaną -> macian`, which provides the lemma-level comparator.
- **Stale or superseded:** the packet's preserved "Current problem: `makô -> mæċa`" stage and the surrounding Option A/B/C discussion were written before the later conditioning fixes now reflected in live code. `DEV_NOTES` 36757-36767 shows a later state where both `*mákô -> maca` and `*mákōjaną -> macian` already work, so the older "change the citation form to iptv. 2sg" proposal is project history, not the current repo decision.
- **Irrelevant or misleading:** the lack of lexical-table hits for `maca` is not evidence against the row; the lexical tables are lemma-oriented and list `macian`, not finite imperative forms. Conversely, the existence of `macian` in lexical tables does not make row 2309 redundant; it simply shows that the packeted imperative row is not a citation-form entry.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2117 and 2309-2310.
- `Germanic/docs/DEV_NOTES.md` at 2771-2955 and 36757-36767.
- `Germanic/fsts/germanic.txt` at `pgrmWeakTailVowel`, `OEARestorationTriggerVowel`, and `OEUnstressedLongVowelShortening`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/tools/oe_paradigm_probe.py`, plus live manual probe runs.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.

No full make-specific dossier or analysis file turned up beyond the packeted `DEV_NOTES` material.

Main findings from the extra check:

- The live repo now cleanly distinguishes the lemma pathway and the selected imperative pathway: a manual probe gives `*mákōjaną -> macian` for the ordinary lexeme row, but `*mákô -> maca` for row 2309.
- The neighboring finite comparator also works in the live repo: `*mákōθi -> macaþ` for row 2310.
- `oe_known_problems.tsv` has no entry for row 2309, so this is not being treated as a live exception row.
- `old_english_wiktionary.tsv` has `make -> macian`, but no lexical-table entry for `maca`; that supports the citation-form vs. inflected-form distinction rather than overruling the row.
- `oe_paradigm_probe.py` still has no built-in `make / maca` spec, so the row's paradigm evidence is only packet/manual at present.

## Reconstruction and early-stage forms

This row needs a sharper three-way distinction than the packet currently gives.

1. **Cognate-set proto / lexeme-level headword:** for the verb 'make', the live comparative row elsewhere in the TSV uses `*mákōjaną` (`make / macian`, row 2117), matching the other West Germanic lexeme rows.
2. **Current row's live TSV `PROTO`:** `*makōną` is best read as a reduced stem-level project label for the weak-II finite paradigm, not as the full comparative lexeme headword.
3. **Project derivational input for this row:** `PROTOFORM` `*mákô`, the imperative 2sg cell with trimoric `*ô`.
4. **OE target form represented by the row:** `maca`, an imperative singular form rather than the dictionary citation form.

For the actual derivation, the live evidence is straightforward:

`*mákô -> *mækô -> *makô -> *maka -> maca`

The crucial current implementation point is that `*ô` is now explicitly treated as an A-restoration trigger, so the earlier diagnostic misderivation `mæċa` is no longer live evidence. The packet is therefore right about the row's current working derivation, but it preserves an older project stage in which the same input was still failing.

## Old English philology

`maca` should be treated here as a selected **OE imperative 2sg target**, not as the lemma for 'make'. The lemma-level OE form in the repo-local lexical material is `macian`, and the regular make row 2117 already covers that citation-form outcome.

For this memo, the repo evidence supports these distinctions:

- **citation/headword form:** `macian`;
- **selected finite paradigm cell:** `maca`;
- **related finite comparator:** `macaþ` in row 2310.

I did not find a repo-local lexical-table entry independently documenting `maca` as a dictionary headword or with manuscript/dialect detail. So the eventual final report should present `maca` confidently as the project's selected imperative-cell outcome, but it should avoid stronger claims about direct lexicographical attestation unless a more explicit source is added.

## Project problem and solution

The project problem is not simply "how do we get any OE form for 'make'?" The live repo already gets lemma-level `*mákōjaną -> macian`. The narrower problem for row 2309 is how to represent the **regular finite weak-II cell with trimoric *ō** that R/T §5.2 discusses.

The current project solution is mostly sound:

- keep a separate late-analogy paradigm-cell row for the imperative 2sg;
- use `PROTOFORM` `*mákô` as the actual derivational input;
- target `maca`;
- treat the row as complementary to, not a replacement for, the lemma-level `macian` row.

What is still muddy is the row's `PROTO` field and some of the preserved packet history. The memo evidence points to the lexeme-level comparative proto being `*mákōjaną`, while live TSV `PROTO` `*makōną` is a stem abstraction. That distinction should be made explicit in the eventual report, and probably in the data itself.

## Paradigm probe

**Yes — a paradigm probe is required.** This row is a paradigm-cell case, and `Germanic/tools/oe_paradigm_probe.py` still has no built-in `make / maca` specification.

At minimum, the missing probe should cover these cells:

- **infinitive / citation comparator:** `*mákōjaną -> macian`
- **imperative 2sg:** `*mákô -> maca`
- **present 2sg:** `*mákōs -> macas` if the project wants the full R/T regular finite set represented
- **present 3sg:** `*mákōθi -> macaþ`

The live manual probe already confirms the decisive contrast for this memo: `*mákōjaną` does **not** match target `maca`, while `*mákô` does. But the standardized saved probe is still missing, so the final report should not rely only on packet prose.

## Recommended final report

Recommend a concise final report that presents row 2309 as a deliberate imperative-cell companion to the ordinary lexeme row `make / macian`: distinguish lexeme-level `*mákōjaną`, row-level input `*mákô`, and OE target `maca`; explain that the old `mæċa` problem is stale implementation history; and keep the focus on the regular trimoric-*ō finite cell rather than on replacing the lemma-level analysis.

## Data-change recommendations

- **TSV `PROTO`:** **change recommended.** The current `*makōną` collapses lexeme-level proto and finite-stem abstraction. If this row is meant to stay tied to the ordinary make lexeme, the more transparent lexeme-level proto is `*mákōjaną`, with `PROTOFORM` left to carry the imperative-cell choice.
- **TSV `PROTOFORM`:** **no change recommended.** `*mákô` is the right project input for the selected imperative 2sg cell.
- **TSV `COUNTERPART`:** **no change recommended.** `maca` is the intended OE target for this row.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `late_analogy` still fits a non-lemma paradigm-cell row created alongside the ordinary lexeme entry.
- **TSV `NOTE`:** **minor change recommended.** Keep the trimoric-*ō point, but clarify that this is a paradigm-cell companion to the lemma-level `macian` row, not the lexeme's citation form.
- **`oe_known_problems.tsv`:** **no change recommended.**
- **`DEV_NOTES` text:** **change recommended.** The older 2026-02-24 Option A/B/C exploration should be marked more explicitly as superseded by the later post-fix state where both `*mákô -> maca` and `*mákōjaną -> macian` already work.
- **Dossier text:** **no change recommended.** I found no make-specific dossier text that needs row-level cleanup.

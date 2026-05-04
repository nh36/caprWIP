# Research memo — 2317 show (iptv.2sg) / sċēawa

## Starting point

- **ID:** 2317
- **CONCEPT:** `show (iptv.2sg)`
- **COUNTERPART:** `sċēawa`
- **PROTO:** `*skawōną`
- **PROTOFORM:** `*skáwô`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** `Class II weak iptv. 2sg test. Trimoric *ō → OE -a. Normalized sċ: Campbell §440.`

This row is a paradigm-cell companion to the ordinary OE lemma row 2186 `show / sċēawian`, not the citation-form entry itself. The main task is to keep apart the lemma-level `scēawian/sċēawian` evidence, the selected imperative input `*skáwô`, and the normalized OE target `sċēawa`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing current `*skáwô -> sċēawa`; and the packet's statement that this is a Class II weak imperative-singular test row with trimoric `*ō > -a`.
- **Useful background:** the packet's copied `DEV_NOTES` material on `OEAwLongDiphthong`, because it preserves why `*skaw-` needed special attention at all; and the neighboring 3sg row 2318, which shows the same non-`j` singular stem family.
- **Stale or superseded:** the packet's supporting `DEV_NOTES` hit at 3649 is older normalization history, not current authority, because it still says `expected scēawa` rather than the row's present normalized `sċēawa`; likewise 26638 is only diagnostic background and is partly misleading now because it labels row 2317 "Class II noun" even though this row is a weak verb imperative.
- **Irrelevant or misleading:** the packet's "no lexical-table hits" result for `sċēawa` is not evidence against the row. The repo's lexical tables are lemma- and source-spelling-oriented, so they miss both the finite imperative cell and the non-project-normalized spelling `scēawa`.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` rows 2186, 2317, and 2318.
- `Germanic/docs/DEV_NOTES.md` at the older `sċawa/scēawa` mismatch discussion, the trimoric-`*ō` Class II imperative discussion, the `OEAwLongDiphthong` fix, and the later safety sweep around rows 2186/2317/2318.
- `Germanic/fsts/germanic.txt` at `OEAwLongDiphthong`, `OEARestorationTriggerVowel`, and `OEUnstressedLongVowelShortening8`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run against `backend/old_english.bin`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.

No show-specific dossier, analysis memo, or pilot/full lexeme report turned up beyond the packeted material.

Main findings from the extra check:

- The ordinary lemma row is 2186 `*skáwōjaną -> sċēawian`; row 2317 is therefore a deliberately separate finite-cell row rather than a replacement headword.
- `old_english_wiktionary.tsv` confirms the lemma spelling `scēawian`, again showing that row 2317 is not the citation form.
- `bright_anglo_saxon_reader.vision.txt` is stronger than the packet: it explicitly glosses `scēawian` with **imp. 2 sg. `scēawa`** and also gives a 3sg `-sceawað`. So the row's finite-cell choice is philologically supported in repo-local reference material, even though the sources spell `sc-`, not project-normalized `sċ-`.
- `oe_known_problems.tsv` has no row-specific entry.
- A manual probe against the current `backend/old_english.bin` gives a unique winner for the row target: `*skáwô -> sċēawa`, while `*skáwōjaną -> sċēawian` and `*skáwōθi -> sċēawaþ`.

## Reconstruction and early-stage forms

Three levels need to remain distinct:

1. **Cognate-set / lemma-level proto comparator:** the repo's ordinary show row uses `*skáwōjaną`, yielding OE `sċēawian`/source-spelled `scēawian`.
2. **Current row's live `PROTO`:** `*skawōną`, best read as the non-`j` Class II stem/base that groups the selected finite singular cells, not as the citation-form OE lemma.
3. **Project input form for this row:** `PROTOFORM` `*skáwô`, the imperative singular cell with trimoric `*ô`.
4. **OE target represented by the row:** `sċēawa`, the normalized imperative 2sg form.

Current repo evidence supports the derivational logic behind the packet. In `Germanic/fsts/germanic.txt`, `OEAwLongDiphthong` now explicitly handles `*aw` before vocalic material **and before `*ô`**, and `OEUnstressedLongVowelShortening8` explicitly maps trimoric `*ô` to late `*a`. With the current backend binary, that yields the row target `sċēawa` from `*skáwô`.

The important historical distinction is therefore not between two competing imperative inputs, but between the **lemma pathway** `*skáwōjaną -> sċēawian` and the **selected finite-cell pathway** `*skáwô -> sċēawa`.

## Old English philology

This row is unusually well supported for a paradigm-cell memo:

- **Citation/headword form:** repo-local lexical material gives `scēawian` (project-normalized row 2186 `sċēawian`).
- **Selected finite cell:** `bright_anglo_saxon_reader.vision.txt` explicitly lists **imp. 2 sg. `scēawa`** under `scēawian`.
- **Related finite comparator:** the same source also gives 3sg `-sceawað`, which aligns with row 2318 `sċēawaþ`.

So `sċēawa` should not be described merely as a project-invented workaround. The form itself is repo-locally attested, but the project normalizes initial `sc-` to `sċ-` in these OE rows. The final report should therefore distinguish:

- **source spelling / dictionary-style form:** `scēawa`, `scēawian`, `-sceawað`;
- **project-normalized target:** `sċēawa`, `sċēawian`, `sċēawaþ`.

I did not assemble a fuller manuscript/dialect dossier for this memo, so the eventual report should avoid over-specific source claims beyond "repo-local reference material lists imperative `scēawa` under `scēawian`."

## Project problem and solution

The project problem is not whether OE "show" exists; the repo already has the ordinary lemma row `sċēawian`. The narrower issue is how to represent the **regular non-`j` Class II singular cell** that preserves trimoric `*ō` and gives OE `-a`.

The current project solution is sound:

- keep the lemma row 2186 for `*skáwōjaną -> sċēawian`;
- keep row 2317 as the imperative-singular companion `*skáwô -> sċēawa`;
- keep row 2318 as the related 3sg comparator `*skáwōθi -> sċēawaþ`.

What still needs cleanup is project chronology. Older `DEV_NOTES` still preserve the pre-fix stage `sċawa / scēawa` and an inaccurate "Class II noun" label, and the packet surfaces that history without clearly downgrading it. The memo evidence shows that those are debugging remnants, not the current lexical analysis.

## Paradigm probe

**Yes — a paradigm probe is required for this row class.** In substance the decisive comparison is already available, because a manual probe against `backend/old_english.bin` gives:

- `*skáwōjaną -> sċēawian`
- `*skáwô -> sċēawa`
- `*skáwōθi -> sċēawaþ`

That is enough to show that the imperative cell, not the lemma row, uniquely matches row 2317. However, the repo still has **no saved built-in show-specific probe** in `oe_paradigm_probe.py`, so the probe is still missing as reusable infrastructure.

If formalized, the saved probe should at minimum include:

- **infinitive comparator:** `*skáwōjaną -> sċēawian`
- **imperative 2sg:** `*skáwô -> sċēawa`
- **3sg present indicative comparator:** `*skáwōθi -> sċēawaþ`

Optional expansion:

- **2sg present indicative:** `*skáwōsi`, since the manual probe currently returns `+?` and would make any remaining gap in the non-`j` singular set explicit.

## Recommended final report

Recommend a short final report that presents row 2317 as a deliberate imperative-singular companion to the lemma row `show / sċēawian`: distinguish lemma-level `*skáwōjaną`, row-level input `*skáwô`, and normalized OE target `sċēawa`; note that repo-local reference material actually lists imperative `scēawa`; and treat older `sċawa/scēawa` debugging history as superseded background only.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*skawōną` is defensible as the project label for the non-`j` finite-cell stem set, so long as the final prose explicitly distinguishes it from the lemma-level `*skáwōjaną`.
- **TSV `PROTOFORM`:** no change recommended. `*skáwô` is the right project input for the selected imperative 2sg cell.
- **TSV `COUNTERPART`:** no change recommended. `sċēawa` matches the current backend output and corresponds to repo-local attested `scēawa` under project normalization.
- **TSV `DERIVATION_CLASS`:** no change recommended. `late_analogy` still fits a non-lemma paradigm-cell row kept alongside the ordinary lemma row.
- **TSV `NOTE`:** minor change recommended. Keep the trimoric-`*ō` and normalization points, but add that this is a paradigm-cell companion to lemma `sċēawian` and that source spelling is `scēawa/scēawian`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** change recommended for `DEV_NOTES`, not for dossier text. Older notes that still expect `scēawa/scēaweþ` against project-normalized `sċ-`, or that label row 2317 "Class II noun," should be marked as superseded/background-only. No separate show-specific dossier text needs change because none was found.

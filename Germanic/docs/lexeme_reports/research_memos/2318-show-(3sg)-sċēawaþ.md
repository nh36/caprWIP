# Research memo — 2318 show (3sg) / sċēawaþ

## Starting point

- **ID:** 2318
- **CONCEPT:** `show (3sg)`
- **COUNTERPART:** `sċēawaþ`
- **PROTO:** `*skawōną`
- **PROTOFORM:** `*skáwōθi`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** `Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ. No i-umlaut: 3sg ending never had -j-. Normalized sċ: Campbell §440.`

This row is not the lemma entry for OE 'show'. The ordinary lemma row is 2186 `show / sċēawian` from `*skáwōjaną`; row 2318 is a deliberately separate finite-cell row for the weak Class II 3sg present indicative, using the project input `*skáwōθi` and the normalized OE target `sċēawaþ`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing current `*skáwōθi -> sċēawaþ`; and the packet's current note that 3sg weak Class II has regular `*-ōθi -> -aþ` with no `j`-triggered i-umlaut.
- **Useful background:** the packet's later `DEV_NOTES` correction at 19602, because it records the project's explicit reversal from older `-eþ` expectations to current `-aþ`; and the packet's 26639 hit, which correctly treats row 2318 as a non-`j` Class II 3sg comparator.
- **Stale or superseded:** the packet's copied 19392 material is old debugging history, not current authority: it still expects `sċēaweþ` and analyzes `-eþ` as the target. The packet's broad keyword hits on unrelated `i-umlaut` discussions are likewise project-history noise unless they directly mention this row.
- **Irrelevant or misleading:** the packet's analysis/dossier keyword hits that merely contain `i-umlaut` without discussing `show`, `*skáwōθi`, or row 2318 do not bear on this row. The absence of lexical-table hits for `sċēawaþ` is also not evidence against the row, since the lexical tables are lemma-oriented and usually do not list this inflected finite cell.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` rows 2186, 2317, and 2318.
- `Germanic/docs/DEV_NOTES.md` at the older `scēaweþ` mismatch stage, the later correction to `sċēawaþ`, and the later show-family safety sweep.
- `Germanic/fsts/germanic.txt` at `OEAwLongDiphthong`, `OEEarlyOShortening`, and `OELateOShortening`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run against `backend/old_english.bin`.
- existing memo `Germanic/docs/lexeme_reports/research_memos/2317-show-(iptv.2sg)-sċēawa.md` as background only.

Main findings from the extra check:

- Row 2186 confirms the simplex lemma pathway `*skáwōjaną -> sċēawian`; row 2318 is therefore a paradigm-cell companion, not the headword row.
- `old_english_wiktionary.tsv` gives the lemma spelling `scēawian`, reinforcing that `sċēawaþ` is not a citation form.
- `bright_anglo_saxon_reader.vision.txt` gives direct simplex evidence for the family via `scēawian` with **imp. 2 sg. `scēawa`**, and gives a 3sg weak-II comparator in the prefixed compound `geond-scēawian` with **3 sg. `-sceawað`**. That is not a direct simplex dossier for row 2318, but it supports the same `-awað` finite-cell shape behind project-normalized `sċēawaþ`.
- `oe_known_problems.tsv` has no row-specific entry.
- A manual probe against the current binary gives a unique winner for this row target: `*skáwōθi -> sċēawaþ`, while `*skáwōjaną -> sċēawian` and `*skáwô -> sċēawa` do not match the 3sg target.
- No show-specific pilot/full lexeme report exists yet; only the neighboring 2317 research memo exists.

## Reconstruction and early-stage forms

Three levels must stay distinct:

1. **Cognate-set / lemma-level proto comparator:** the ordinary show row uses `*skáwōjaną`, yielding OE `sċēawian` (source-spelled `scēawian`).
2. **Current row's project stem label (`PROTO`):** `*skawōną`, best read as the project label for the non-`j` finite-cell stem set grouped by rows 2317/2318, not as the simplex citation-form input.
3. **Current row's selected paradigm-cell input (`PROTOFORM`):** `*skáwōθi`, the specific 3sg present indicative input.
4. **OE target represented by the row:** `sċēawaþ`, the project-normalized 3sg form.

Current repo evidence supports that separation. `OEAwLongDiphthong` now handles `*aw` before a following vowel or `*ô`, which explains the `sċēaw-` stem family, while `OELateOShortening` supplies the weak-II `*ō -> a` development in unstressed endings. So the present project analysis is not "umlauted 3sg `-eþ`" but regular non-`j` `*skáwōθi -> sċēawaþ`.

## Old English philology

This row should be described as a finite-cell row, not as the lexical headword.

- **Citation/headword evidence:** repo-local lexical material gives `scēawian`.
- **Related finite-cell evidence:** `bright_anglo_saxon_reader.vision.txt` lists imperative `scēawa` under simplex `scēawian`, and 3sg `-sceawað` under prefixed `geond-scēawian`.
- **Project normalization:** the TSV writes initial `sc-` as `sċ-` and uses normalized thorn `þ`, so source-spelled `scēawað` / `-sceawað` corresponds to project-normalized `sċēawaþ`.

The important caution is that I did **not** find a repo-local dictionary line explicitly giving simplex 3sg `scēawað` under bare `scēawian`. The philological support is therefore strong for the stem-and-ending pattern, but the final report should avoid overclaiming direct simplex attestation for this exact normalized spelling unless a fuller source dossier is assembled.

## Project problem and solution

The project problem was originally self-inflicted: older `DEV_NOTES` treated weak Class II 3sg forms like `*skáwōθi` as if they should surface with `-eþ`, so row 2318 once targeted `sċēaweþ`. Later project work corrected that analysis and recognized that 3sg weak Class II lacked `-j-`, so the regular project outcome is `-aþ`, not `-eþ`.

The current row is therefore doing the right job:

- keep row 2186 for the lemma `*skáwōjaną -> sċēawian`;
- keep row 2317 for the imperative-singular comparator `*skáwô -> sċēawa`;
- keep row 2318 for the 3sg present indicative `*skáwōθi -> sċēawaþ`.

`DERIVATION_CLASS = late_analogy` should be read here as the project's paradigm-cell management category, not as a claim that the current `-aþ` outcome itself is a stale analogical mistake. On current evidence, the row's phonological target is the corrected one.

## Paradigm probe

**Yes — a paradigm probe is required for this row class.** A manual probe against `backend/old_english.bin` already gives the decisive comparison:

- `*skáwōjaną -> sċēawian`
- `*skáwô -> sċēawa`
- `*skáwōθi -> sċēawaþ`
- optional comparator `*skáwōsi -> +?`

That shows the 3sg input is a unique winner for row 2318. But there is still **no built-in saved show-specific probe** in `oe_paradigm_probe.py`, so the reusable probe is still missing.

If formalized, the saved probe should include at minimum:

- **infinitive comparator:** `*skáwōjaną -> sċēawian`
- **imperative 2sg comparator:** `*skáwô -> sċēawa`
- **3sg present indicative:** `*skáwōθi -> sċēawaþ`

Optional expansion:

- **2sg present indicative:** `*skáwōsi`, to expose that the remaining non-`j` singular cell is still unmodelled in probe infrastructure.

## Recommended final report

Recommend a short final report that presents row 2318 as the corrected weak-Class-II 3sg companion to lemma row `sċēawian`: distinguish lemma-level `*skáwōjaną`, project stem label `*skawōną`, row input `*skáwōθi`, and normalized OE target `sċēawaþ`; cite the old `sċēaweþ` expectation as superseded project history only; and note that repo-local source material supports the `scēaw- / -awað` finite-cell pattern even though the exact project-normalized spelling is editorial.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*skawōną` remains defensible as the project label for the non-`j` singular stem set, provided the final report makes clear that it is not the simplex lemma proto.
- **TSV `PROTOFORM`:** no change recommended. `*skáwōθi` is the right input for the selected 3sg cell.
- **TSV `COUNTERPART`:** no change recommended. `sċēawaþ` matches the current binary and the corrected project analysis.
- **TSV `DERIVATION_CLASS`:** no change recommended. `late_analogy` is still the live project category for this paradigm-cell row, even though the corrected 3sg target itself is now treated as regular within that category.
- **TSV `NOTE`:** minor change recommended. Keep the `*-ōθi -> -aþ` and no-umlaut points, but add that this is a paradigm-cell companion to lemma `sċēawian` and that source support is spelling-normalization-sensitive (`scēawian`, `scēawa`, `-sceawað`).
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** change recommended for `DEV_NOTES`, not for dossier text. Old notes around 2954-2994, 3647-3650, and 19385-19486 that still expect `sċēaweþ` should be explicitly marked as superseded debugging history. No separate show-specific dossier text was found, so no dossier cleanup is currently needed.

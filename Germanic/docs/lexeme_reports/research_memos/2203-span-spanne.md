# Research memo — 2203 span / spanne

## Starting point

- **ID:** 2203
- **CONCEPT:** span
- **COUNTERPART:** spanne
- **PROTO:** `*spannō`
- **PROTOFORM:** `*spánnai`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** Dat.sg. paradigm-cell (Brunner §252). Fem. ō-stem dat.sg. `*-ai` preserves medial geminate; unstressed word-final `*ai -> *ē` (R/T §6.1.5; §17.12).

The live TSV already treats this as a paradigm-cell noun row, distinct from the separate verb row 2202 `spannan`. A pilot report (`Germanic/docs/lexeme_reports/pilot/span.md`) already exists, but it must be treated as background only, not as final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace for `*spánnai -> spanne`; `DEV_NOTES.md` 28061-28135 (`§17.12`), which is the current repo-local resolution of the old breve-marking experiment; and the live built-in probe in `Germanic/tools/oe_paradigm_probe.py`, which still gives `*spannō -> span` but `*spánnai -> spanne`.
- **Useful background:** `DEV_NOTES.md` 13807-14039, which preserves the earlier investigation showing why the gen.sg. route failed and why the dat.sg. route was chosen; `pilot/span.md`, which correctly keeps `PROTO` and `PROTOFORM` distinct but is still only pilot prose; and the implementation report's note that `span.md` is one of the pilot late-analogy entries.
- **Stale or superseded:** the packet's preserved 2026-04-06 material that still experiments with `*spannăi`; the older unaccented spellings `*spannai`; and the stale precedent line at `DEV_NOTES.md` 25306-25308, which still calls `spanne` row 2140 and uses the obsolete breve-marked form. Those are useful project history, not current evidence.
- **Irrelevant or misleading:** the packet's generic `dat.sg.` keyword hits in unrelated analyses (`milk`, `meord`, `cow`, etc.) are methodological background, not lexeme-specific evidence; and `old_english_wiktionary.tsv`'s `spann` hit is only citation-form orientation, not evidence that row 2203 should target `spann` instead of `spanne`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 13807-14039, 25298-25312, and 28061-28135.
- `Germanic/docs/lexeme_reports/pilot/span.md`.
- `Germanic/docs/prosodic_tier_research.md` 1-25.
- `Germanic/data/germanic-aligned-final.tsv` around rows 2202-2203.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/tools/oe_paradigm_probe.py`, plus a live run of the built-in `span / spanne` probe.

Main findings from the extra check:

- No dedicated `span` dossier or span-specific analysis file turned up beyond the packeted `DEV_NOTES` material and the pilot report.
- `oe_known_problems.tsv` has no entry for this row, so this is not being treated as a live exception or unmodelled mismatch.
- The current repo consensus is the **post-§17.12** state: `PROTOFORM` should be plain `*spánnai`, not the older engineering form `*spánnăi`/`*spannăi`.
- The only lexical-table hit I found is `old_english_wiktionary.tsv` `span -> spann`, which supports the citation-form/inflected-form distinction but does **not** by itself document `spanne` as a lexicographical headword.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction.

1. **Cognate-set proto / lexeme-level headword:** TSV `PROTO` `*spannō`, i.e. the noun at citation-form level.
2. **Project derivational input:** TSV `PROTOFORM` `*spánnai`, the selected **dative singular** cell.
3. **OE target represented by the row:** `spanne`, an OE oblique form rather than the noun's citation/headword form.

The crucial current choice is that `PROTOFORM` is **not** an alternative lexeme reconstruction. It is the project input chosen because the citation-form path does not yield the target. The live `§17.12` discussion also matters: earlier repo history tried to encode the unstressed ending with a breve (`*spánnăi` / `*spannăi`), but the current implementation deliberately removed that engineering diacritic and now treats word-final plain `*ai` as sufficient. For this memo, current evidence therefore favors `*spánnai`, not the older breve-marked spellings.

## Old English philology

Repo-local evidence supports reading `spanne` as a **feminine ō-stem dative-singular-type form**, not as a dictionary-style citation form. The separate verb row 2202 (`spannan`) is an important control here: the noun row must not be collapsed into the verbal lexeme.

Just as important, the sources checked for this memo do **not** independently prove the attestation status of `spanne`. The repo note cites Brunner for the morphology, and the probe/FST evidence shows why `spanne` is the chosen OE target, but the lexical tables checked here only give `spann`. So the eventual final report should say confidently that `spanne` is the project's selected OE oblique target, but it should avoid overclaiming direct dictionary/headword attestation unless a stronger lexicographical or textual citation is added.

## Project problem and solution

The project problem is straightforward: lexeme-level `*spannō` gives `span`, not `spanne`. An earlier attempt to use a feminine ō-stem gen.sg. route failed in project testing, because the expected `-e` outcome was not obtained cleanly in the cascade. The current project solution is therefore to keep the cognate-set headword in TSV `PROTO`, switch TSV `PROTOFORM` to the dat.sg. `*spánnai`, and target `spanne` as the row's OE form.

That solution is coherent and already works in the live probe. The `late_analogy` label is still the right project description: the row is intentionally modelling the lexeme through a conservative oblique paradigm cell rather than through the citation-form nominative.

## Paradigm probe

A paradigm probe **is required in principle**, because this row's whole justification is the contrast between the citation-form headword and the selected oblique input. But the minimum probe is **not missing**: `Germanic/tools/oe_paradigm_probe.py` already has a built-in `span / spanne` probe, and a live run still gives the decisive contrast:

- **nom.sg.** `*spannō -> span`
- **dat.sg.** `*spánnai -> spanne`

So no additional probe is required before a final report is drafted. If the project later wants a fuller saved table, the next cell to add would be the **rejected gen.sg. comparator**, so the report can show explicitly why the project chose dat.sg. rather than another ō-stem oblique singular cell.

## Recommended final report

Recommend a concise final report that presents row 2203 as a deliberate dative-singular paradigm-cell solution: keep lexeme-level `PROTO` `*spannō`, keep project-input `PROTOFORM` `*spánnai`, explain that `spanne` is the selected OE oblique target while citation-form `*spannō` yields only `span`, and treat the older `*spannăi` / stale row-number history as superseded project background rather than current evidence. The final report should also avoid claiming independent attestation of `spanne` unless a stronger source is added.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended.** `*spannō` is the right lexeme-level headword.
- **TSV `PROTOFORM`:** **no change recommended.** The current `*spánnai` is the right live project input and is preferable to the older breve-marked experiments.
- **TSV `COUNTERPART`:** **no change recommended.** `spanne` is the intended OE target for this row.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `late_analogy` still fits the paradigm-cell analysis.
- **TSV `NOTE`:** **no required change.** The current note already states the dative-singular solution and the `*ai -> *ē` logic clearly enough.
- **`oe_known_problems.tsv`:** **no change recommended.** This is not a live exception row.
- **DEV_NOTES / dossier text:** **change recommended.** `DEV_NOTES.md` should mark the older `*spannăi` stage more explicitly as superseded by `§17.12`'s current `*spánnai` analysis, and the stale precedent line at 25306-25308 should be corrected so `spanne` is no longer mislabelled as row 2140 with obsolete proto spelling. `Germanic/docs/prosodic_tier_research.md` line 24 also still uses the outdated `*spannăi` example and should be updated if that note is meant to reflect current notation.

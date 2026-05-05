# Research memo — 2270 warp / weorpan

## Starting point

- **ID:** 2270
- **CONCEPT:** warp
- **COUNTERPART:** `weorpan`
- **PROTO:** `*wérpaną`
- **PROTOFORM:** `*wérpaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: wearp→weorpan (inf. of str.v. class III; noun/past 'wearp' in *warpą row)`

This is a note-bearing regular row whose derivation is already producing the intended OE infinitive. The real memo task is to keep the verbal row `weorpan` separate from the related OE form `wearp`, which belongs to the distinct preterite/noun row 2269 with `PROTO = *wárpą`.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row and the compact derivation trace are current: they show `*wérpaną -> weorpan`, with breaking before `r + C` and no present derivational failure.
- The packet's direct row pairing with row 2269 is current and important. It correctly signals that this row is the infinitive/citation form, while `wearp` belongs elsewhere.
- The lexical-table hit in `old_english_swadesh.tsv` (`to throw -> weorpan`) is good supplementary confirmation that the row's OE target is verbal, not nominal.

**Useful background but not final authority:**

- The `old_english_wiktionary.tsv` hit `warp -> wearp` is useful only as evidence for the neighboring `wearp` row and for the lemma overlap; it is not authority against the current row's `weorpan`.
- `DEV_NOTES.md` on late West Saxon `weorpan -> wurpan` is relevant background for later OE variation, but it does not reset the normalized target away from `weorpan`.

**Stale, superseded, or diagnostic-only material in the packet:**

- The packet's `ws_vs_anglian_dialect_differences.md` hit about Northumbrian `uarp warp` is diagnostic only. It concerns dialectal preterite/root-vowel variation in `wearp`, not the citation infinitive of row 2270.
- The packet's emphasis on exact-string matches for `warp` can be misleading unless read together with the TSV note, because the English gloss conflates the noun/past `wearp` row and the verbal `weorpan` row.

**Irrelevant or misleading if over-weighted:**

- The packet's lack of dossier hits should not be mistaken for lack of philological support; the dictionary and handbook files in the repo do support `weorpan` directly.
- The concept label **warp** is only the aligned English gloss. For OE row 2270 the lexical target is specifically the strong verb infinitive `weorpan` 'throw', not the noun `wearp` 'warp' and not the preterite singular `wearp`.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2269-2270, confirming the split between `*wárpą -> wearp` and `*wérpaną -> weorpan`.
- `Germanic/docs/DEV_NOTES.md` at the late-WS `weorpan -> wurpan` note and the breaking discussion using `weorpan` as a canonical example.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`, because it was named in the packet; its `uarp warp` evidence is about dialectal past/root forms, not the normalized infinitive target.
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md`, which includes `*warpą -> wearpa (exp. wearp)` and helps confirm that the `wearp` form belongs to the separate short-form row, not to the infinitive row.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which marks row 2270 as report-requiring because of its non-empty `NOTE`, while row 2269 does not require a report.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, which gives `weorpan` as the verb headword and `wearp` both as noun and as preterite singular of `weorpan`.
- `docs/references/bright_anglo_saxon_reader.txt`, which gives the strong-verb series `weorpan, wearp, wurpon, worpen`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`, which derives both `OE wearp` and `OE weorpan`, and separately discusses Northumbrian `warp`-type variation and late/variant present forms.

No pilot/full lexeme report for this lexeme was found in the repo.

## Reconstruction and early-stage forms

Three levels should be kept distinct, even though two coincide here:

1. **Cognate-set proto / etymological verbal headword:** `*wérpaną`.
2. **Project input form for row 2270:** also `*wérpaną`; this row is not being rescued by a surrogate paradigm cell.
3. **OE target form:** `weorpan`, the OE infinitive/citation form.

That row must then be kept separate from the related but different ablaut-grade row:

- **Related row 2269:** `PROTO = *wárpą`, `COUNTERPART = wearp`.

So the memo should not collapse `*wérpaną` and `*wárpą` into one undifferentiated "proto". The former is the verbal infinitive input for row 2270; the latter is the preterite/noun-side input already represented by row 2269.

For the early OE path, the repo's current derivation is straightforward: `*wérpaną` undergoes OE breaking before `r + C`, giving an early `*wéorpaną`, and later tail reduction/apocope yields `weorpan`. That is different from the short-form path `*wárpą -> wearp`, where the ablaut grade and ending are different from the start.

## Old English philology

`weorpan` is an **attested OE verb headword**, not a reconstructed-only target. Repo-local dictionary material supports that directly.

The main philological issue is headword separation:

- `weorpan` = the strong class-III verb infinitive/citation form 'to throw'.
- `wearp` = both a noun (`'warp,' threads stretched in a loom`) and the preterite singular of `weorpan` in Clark Hall.

That overlap is exactly why the TSV note exists. The row should target the citation infinitive, not the preterite singular and not the noun. `Bright`'s paradigm table reinforces the standard strong-verb interpretation by giving `weorpan, wearp, wurpon, worpen`.

Dialect/stage variation does exist in repo-local sources, but it should be handled cautiously:

- late WS `wurpan` is a later OE variant, not the normalized row target;
- Northumbrian `warp/uarp` material belongs to dialectal discussion of past/root-vowel developments, not to the citation infinitive represented here.

So the final report should keep `weorpan` as the normalized target while mentioning `wearp`, `wurpan`, or `warp/uarp` only as related paradigm or dialect background when genuinely relevant.

## Project problem and solution

The project problem is not an unresolved sound-law failure. It is a **row-identity problem created by lexeme overlap**:

- the English gloss **warp** naturally points to OE `wearp`;
- but the cognate set for row 2270 is verbal `*wérpaną`, and the intended OE target is the infinitive `weorpan`;
- the related `wearp` material already has its own row (2269) under `*wárpą`.

The present project solution is correct:

- keep row 2270 as the **verbal infinitive** row with `COUNTERPART = weorpan`;
- keep row 2269 as the related `wearp` row;
- treat later `wurpan` and dialectal `warp/uarp` material as background only, not as reasons to retarget row 2270.

## Paradigm probe

A paradigm probe is **not required** for this memo.

The core issue is already settled by the live row split plus dictionary/handbook evidence: row 2270 is the infinitive `weorpan`, while `wearp` belongs to a different row and different paradigm cell. If a later final report wants a compact explanatory table anyway, the most useful optional cells would be:

- infinitive `weorpan`;
- preterite singular `wearp`;
- preterite plural `wurpon`;
- past participle `worpen`.

That would be explanatory context, not a prerequisite for the report.

## Recommended final report

Recommend a short final report stating that row 2270 is the attested OE strong-verb infinitive `weorpan` < project input `*wérpaną`, that the current derivation is already regular through OE breaking, and that the note exists only because English **warp** also surfaces related OE `wearp` material now handled separately in row 2269.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** The current note is directionally right but the arrow `wearp→weorpan` risks implying derivation from the preterite/noun form. It would be clearer to say directly that row 2270 targets attested OE infinitive `weorpan`, while related noun/preterite `wearp` belongs to row 2269 / `*wárpą`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** no change recommended; the current notes on breaking and late WS `wurpan` are useful background as long as they are not mistaken for row-targeting instructions.
- **Dossier / analysis text:** no mandatory change recommended. `ws_vs_anglian_dialect_differences.md` is doing legitimate dialect history, but future packets should continue to treat its `uarp/warp` evidence as diagnostic background for `wearp`-type forms rather than as direct authority for row 2270.

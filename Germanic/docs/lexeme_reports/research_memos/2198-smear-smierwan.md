# Research memo — 2198 smear / smierwan

## Starting point

- **ID:** 2198
- **CONCEPT:** `smear`
- **COUNTERPART:** `smierwan`
- **PROTO:** `*smérwijaną`
- **PROTOFORM:** `*smérwijaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Source: Kroonen p.458 *smerwjan- > OE smierwan; R/T §6.7.1 p.289 WS smierwan (Merc. smirwan is Anglian)`

This is a note-bearing `regular` row. The live TSV and compact trace both currently treat the row as the regular West Saxon citation-form target `smierwan`. There is no lexeme-specific pilot/full report in `Germanic/docs/lexeme_reports/pilot/`; the only existing report-like material is the packet plus auto-generated debug snapshots with a placeholder “Project note”, which are background only, not authority.

## Packet evidence assessment

**Authoritative/current**

- The live TSV row is the present project authority: it keeps `PROTO = PROTOFORM = *smérwijaną`, targets `smierwan`, and leaves the row in `regular`.
- The packet's compact derivation trace and exact-pair debug hit are current implementation evidence that the live input derives successfully to `smierwan`.
- The packet's Campbell/Ringe-Taylor material is genuinely relevant for dialect framing: West Saxon `smierwan` is contrasted with Anglian/Mercian `smirwan`.

**Useful background**

- The packet's `DEV_NOTES` section on `*smerwijăną` vs. `*smirwijăną` is useful for understanding a real repo-level reconstruction discussion.
- The packet's lexical-table hit and reference-style background are useful for showing that lexicographic headwords vary (`smierwan`, `smirwan`, `smirian/smyrian`), even though the row targets only one OE form.

**Stale or superseded**

- The packet's many generic `Anglian` keyword hits are not row-specific evidence; they are comparison material accidentally captured by packet matching.
- The debug-snapshot placeholder `### Lexeme report` text is not a finished report and should not be treated as prior editorial authority.
- In `DEV_NOTES`, the sentence that the TSV “may need updating if we prefer R/T's reconstruction” is best treated as older project-history language, not as a current decision already requiring data rewrite.

**Irrelevant or misleading if over-read**

- `old_english_wiktionary.tsv` gives `smerian`, which is useful as dictionary-style background but misleading if treated as evidence that row 2198 should target a different OE verb class or lemma.
- The packet's unrelated `meord`, `widuwe`, and similar Anglian comparison hits should not be promoted into direct evidence for this lexeme.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv`.
- `Germanic/docs/DEV_NOTES.md` around the Campbell and reconstruction-disagreement sections and the later exact-pair audit.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and the debug-snapshot missing-reports list.
- `Germanic/data/oe_known_problems.tsv` (checked; no relevant entry).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.

Main findings from that wider check:

- Kroonen gives the comparative etymological headword as PGmc `*smerwjan-`, which matches the TSV's `*smérwijaną` choice.
- Ringe-Taylor gives a later-stage PNWGmc `*smirwijana` and explicitly derives Mercian `smirwan`, Northumbrian `smiriga`, and WS `smierwan`; this is real evidence for dialectal OE distribution, not by itself proof that the TSV must switch protoforms.
- Campbell's discussion is specifically about Anglian failure of breaking before `r + C` when `-i-` follows; `smirwan` is one of his core examples.
- Clark Hall, Brunner, and Bright show that the lexical family also has variant/headword and class-shift complications (`smierwan` beside `smirwan`, and later `smirian/smyrian`, `smyrode`). Those are important for report prose but do not overturn the live row's target.
- No repo-local `oe_known_problems.tsv` or separate lexeme dossier currently says that row 2198 is unmodelled or wrongly targeted.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** the live TSV uses `*smérwijaną`, reflecting Kroonen's PGmc `*smerwjan-`.
2. **Alternative early-stage comparative reconstruction in the repo:** Ringe-Taylor instead gives PNWGmc `*smirwijana` and derives the OE dialect forms from that stage.
3. **OE target represented by the row:** West Saxon citation-form `smierwan`.

So the apparent disagreement is real, but it is also partly a stage mismatch: Kroonen is cited for a PGmc headword, while Ringe-Taylor gives a later Northwest/Proto-West-Germanic-stage form and then an OE dialect split. Both pathways converge on WS `smierwan`. The current row therefore does **not** collapse proto headword, derivational input history, and OE target into one undifferentiated claim; it simply keeps the Kroonen-style input while targeting the WS outcome.

## Old English philology

- **Attested vs. reconstructed:** repo-local evidence treats `smierwan` and `smirwan` as real OE forms, with WS/Anglian distribution. Ringe-Taylor also gives Northumbrian `smiriga` as part of the same family.
- **Citation form vs. other family members:** row 2198 is the infinitive/citation-form row. Later or alternate family forms such as `smirian/smyrian`, `smyrode`, and related nouns belong in philological discussion, not in the row's `COUNTERPART`.
- **Dialect status:** Campbell explicitly supports Anglian failure of breaking here, so the packet note's contrast “WS `smierwan` vs. Merc./Anglian `smirwan`” is solid. The row should not, however, imply that `smierwan` is the only OE form.
- **Headword issue:** dictionary material is mixed. Clark Hall normalizes under `smierwan` but cross-references `smirewan`, `smirian`, and `smirwan`; Bright shows late WS attraction into class II (`smyrian`, `smyrode`). This means the final report should explain that the row represents the inherited WS citation form, not every later lexicalized lemma choice.

## Project problem and solution

The project problem is not that the FST fails on the live row; it already derives `smierwan`. The real issue is explanatory: the evidence base contains two comparative reconstructions and several OE-family spellings/lemmas, so the row needs careful framing.

The current row solves that problem reasonably well:

1. it keeps a defensible comparative proto/headword (`*smérwijaną`, after Kroonen);
2. it keeps the OE target as WS `smierwan`, which the live derivation already produces;
3. it leaves Anglian/Mercian `smirwan`, Northumbrian `smiriga`, and late WS class-II forms as comparative philological background rather than as competing row targets.

On the current evidence, the row should stay a `regular` WS-target row. The remaining work is editorial: future prose should state explicitly that `smierwan` is the chosen WS target, while other OE family forms remain real but non-target comparators.

## Paradigm probe

A paradigm probe is **not required**.

This is not a late-analogy or hidden-cell case, and the live compact trace already derives the citation form directly. The unresolved questions are dialect labeling and headword/reconstruction framing, not missing paradigm cells. No specific infinitive/present/preterite cells need a saved probe for the memo stage.

## Recommended final report

Recommend a concise final report that keeps `smierwan` as the WS target, distinguishes Kroonen's PGmc `*smerwjan-` from Ringe-Taylor's PNWGmc `*smirwijana`, and briefly contrasts the target with Anglian/Mercian `smirwan`, Northumbrian `smiriga`, and later class-II/headword variants such as `smirian/smyrian`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; keep `smierwan` as the row's WS target.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` still fits.
- **TSV `NOTE`:** **small change recommended.** The note should say more explicitly that the TSV follows Kroonen's PGmc `*smerwjan-`, while Ringe-Taylor gives later-stage `*smirwijana` and the dialect contrast `WS smierwan` vs. `Merc./Anglian smirwan`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **small DEV_NOTES cleanup recommended; no dossier rewrite required.** The `DEV_NOTES` section should distinguish more clearly between PGmc headword choice and later-stage Ringe-Taylor reconstruction, so “may need updating” is not read as a live demand to rewrite the TSV. The general analysis file `ws_vs_anglian_dialect_differences.md` still looks current and does not need lexeme-specific surgery.

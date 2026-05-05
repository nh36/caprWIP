# Research memo — 2088 lade / hladan

## Starting point

- **ID:** 2088
- **CONCEPT:** lade
- **COUNTERPART:** `hladan`
- **PROTO:** `*laθōjaną`
- **PROTOFORM:** `*xláðaną` (project spelling for conventional PGmc/early Germanic `*hlaðaną`)
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** `Wiktionary: PGmc *hlaðaną (Verner) > OE hladan | Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1`

The row already derives to the correct surface form `hladan`. The research question is therefore not whether the current output matches, but how to explain the deliberate split between cognate-set `PROTO = *laθōjaną` and OE-facing `PROTOFORM = *xláðaną`, and which parts of the packet are current evidence versus archived problem-solving.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row and compact derivation trace are current: they show `PROTOFORM = *xláðaną`, expected/output `hladan`, and the explicit note that full-vowel `-aną` is being used to model the OE infinitive with A-restoration.
- The DEV_NOTES analysis at `Germanic/docs/DEV_NOTES.md:10225-10241` is still useful as the clearest repo-local explanation of the voiced dental: OE `hladan` requires Verner-grade `*ð`, not pre-Verner `*θ`.

**Useful background:**
- The packet’s A-restoration pointers are relevant background, because the row note explicitly relies on the infinitival `-aną` to keep the back-vowel environment needed for `a` rather than `æ` [@RingeTaylor2014].
- The lexical-table hit in `old_english_wiktionary.tsv` confirms that `hladan` is an expected OE counterpart for ‘lade’, but it is supplementary rather than decisive.

**Stale or superseded:**
- Packet excerpts that quote the earlier protoform `*xlaθaną` or the earlier note wording `PGmc *hlaθaną > OE hladan` are historical diagnostics only. They document the bug that was fixed; they are not current evidence for the row.
- The progress-log entry “Verner TSV fixes: lade, needle” is historical workflow context, not philological authority.
- `Germanic/docs/DEV_NOTES.md:3151` is now stale for this lexeme because it lists `hlaþan` as an A-restoration verification target from an earlier stage.

**Irrelevant or potentially misleading:**
- Generic packet hits about A-restoration in unrelated nouns and weak verbs are only methodological support. They should not be mistaken for direct lexical evidence about `hladan`.
- The auto-generated debug-snapshot “Lexeme report” stub is not a manual pilot/full report and should not be treated as final authority.

## Additional repo research

Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md:3151`, `10225-10286`
- `Germanic/docs/analysis/arestoration_r_l_research.md`
- `Germanic/data/old_english_wiktionary.tsv`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/legacy/orel_handbook_germanic_etymology.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- `docs/references/bright_anglo_saxon_reader.txt`
- `Germanic/docs/lexeme_reports/pilot/` (no pilot report for this lexeme)

Main findings from that additional research:
- Ringe & Taylor explicitly derive OE `hladan` from a strong pre-OE form with levelled `-d-`, and give the class-VI paradigm `hladan, hlōd, hlōdon, hladen` [@RingeTaylor2014].
- Campbell also treats `hladan` with other class-VI strong verbs showing restored `a` in the citation form, while preserving umlauted present cells such as `hlet` [@Campbell1959].
- Clark Hall and Bosworth-Toller both treat `hladan` as an ordinary attested OE verb meaning ‘load; draw water’ [@ClarkHall1960; @BosworthToller1898].
- Kroonen supports OE `hladan` within the Germanic strong-verb set; Orel’s older comparative form with voiceless `þ` is useful background but should not override the repo’s later Verner-aware correction [@Kroonen2013; @Orel2003].
- No full dossier file was named for this row, and no existing pilot/full lexeme report was found.

## Reconstruction and early-stage forms

This row only makes sense if three levels are kept separate.

1. **Cognate-set proto (`PROTO`):** `*laθōjaną` is the wider comparative headword attached to the English/German/Dutch “lade/laden” set. That is the etymological/cross-language label carried by the cognate table.
2. **Project input form (`PROTOFORM`):** `*xláðaną` is the form actually fed into the OE derivation. In ordinary spelling this is effectively `*hlaðaną`: it has initial `h-`, the Verner-grade voiced dental `*ð`, and infinitival `-aną` as the back-vowel environment.
3. **OE target:** the row aims at the attested OE citation infinitive `hladan`, not at a reconstructed or dialect-smoothed pseudo-form.

The crucial point is that the OE row is not being derived straight from the cognate-set weak verb. It is instead modelling the strong OE cognate as an **early-stage analogical/pre-selection issue**, which is why `DERIVATION_CLASS = early_analogy` is plausible. The packet’s current note captures the `-aną` reason, but the stronger philological distinction is that the OE row uses a different early Germanic stem from the cognate-set citation proto.

## Old English philology

`hladan` is an attested OE strong verb, not a reconstructed target. Repo-local reference material supports the class-VI paradigm `hladan`, past singular `hlōd`, past plural `hlōdon`, past participle `hladen` [@RingeTaylor2014; @Kroonen2013; @BrightCassidyRingler1971]. Clark Hall and Bosworth-Toller likewise treat `hladan` as a dictionary headword meaning ‘to lade, load, draw water’ [@ClarkHall1960; @BosworthToller1898].

The philological subtlety lies in paradigm shape, not in whether the infinitive exists. Handbook material also preserves umlauted present cells such as `hlætst` / `hlet`, which show that class-VI presents could still exhibit front-vowel effects in specific persons while the citation infinitive remained `hladan` [@RingeTaylor2014; @Campbell1959]. That is useful context, but it does not undermine the row target: the counterpart should still be the infinitive `hladan`.

Nothing in the repo-local evidence requires us to recast this as a dialect-specific or reconstructed OE form. The main philological claim is simply that OE `hladan` reflects the voiced Verner-grade and belongs to the attested strong-verb paradigm.

## Project problem and solution

The project problem has two layers.

1. **Verner layer:** an older repo state used `*xlaθaną`, which would predict OE `þ`, not the attested `d`. The March 2026 DEV_NOTES fix correctly moved the OE input to voiced `*ð`.
2. **Lexeme-selection layer:** the cognate set is labelled with `PROTO = *laθōjaną`, but the OE row is actually intended to represent the strong verb `hladan`. That mismatch is exactly why the row needs an explicit lexeme note and should remain an `early_analogy` case rather than being flattened into a regular inheritance line.

So the current project solution is basically right: keep the cognate-set proto for cross-language bookkeeping, but derive OE from the strong Verner-aware input `*xláðaną` and target the attested infinitive `hladan`.

## Paradigm probe

A dedicated paradigm probe is **not required** for this memo. The row’s real issue is early-stage stem selection plus the Verner-grade consonant, not an unresolved late paradigm-cell problem. The key paradigm facts are already explicitly given in repo-local sources: `hladan`, `hlōd`, `hlōdon`, `hladen`, with present `hlætst` / `hlet` cited as supporting forms [@RingeTaylor2014; @Campbell1959; @ClarkHall1960].

If the supervisor later wants a probe for audit completeness, the cells worth probing would be: infinitive, present 2sg, present 3sg, preterite sg, preterite pl, and past participle.

## Recommended final report

Keep the eventual `### Lexeme report` short and source-dense. It should foreground the distinction between `PROTO = *laθōjaną` (cognate-set headword) and OE-facing `PROTOFORM = *xláðaną` / conventional `*hlaðaną`, cite the Verner-aware strong-verb evidence for attested `hladan`, and treat older `*xlaθaną` notes only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** **no change**. `*laθōjaną` can stay as the cognate-set proto/headword.
- **TSV `PROTOFORM`:** **no change**. `*xláðaną` is the correct project input for the OE row.
- **TSV `COUNTERPART`:** **no change**. `hladan` is the correct attested citation form.
- **TSV `DERIVATION_CLASS`:** **no change**. `early_analogy` still best captures the fact that the OE row is not being derived directly from the cognate-set proto.
- **TSV `NOTE`:** **should change**. The current note is usable but under-explains the main issue. It should say explicitly that the OE row uses the strong Verner-grade `*hlaðaną`/`*xláðaną` rather than the cognate-set `*laθōjaną`, and it should prefer Kroonen/Ringe & Taylor over a bare Wiktionary lead.
- **`oe_known_problems.tsv`:** **no change**. The row is currently deriving correctly and does not need a standing known-problem entry.
- **`DEV_NOTES` / dossier text:** **DEV_NOTES cleanup recommended; no dossier change identified.** At minimum, the old `hlaþan` verification mention at `DEV_NOTES.md:3151` and the quoted pre-fix note wording around the `*xlaθaną` discussion should be marked as superseded or clarified as historical workflow, so later packet generation and repo search do not over-weight stale forms.

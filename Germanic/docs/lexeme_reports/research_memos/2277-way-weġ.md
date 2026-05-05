# Research memo — 2277 way / weġ

## Starting point
- **ID:** 2277.
- **CONCEPT:** way.
- **COUNTERPART:** `weġ`.
- **PROTO:** `*wégaz`.
- **PROTOFORM:** `*wégaz`.
- **DERIVATION_CLASS:** `regular`.
- **NOTE:** “Kroonen *wega- m. 'way, road' → OE weġ m.; wē is not attested as OE 'way'.”
- The live row is a regular success case with a non-empty note, so it is lexeme-report-relevant even though the current derivation already lands on `weġ`.
- No standalone pilot/full report for this lexeme was found in `Germanic/docs/lexeme_reports/pilot/`; generated debug-snapshot prose is background only, not final authority.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet's compact derivation showing `*wégaz -> weġ`; the current `DEV_NOTES.md` palatalisation section at §17.50.4, which explicitly treats `*wégaz -> weġ` as a correct front-vowel-plus-word-final case; and the lexical-table hit `way -> weġ` in `old_english_wiktionary.tsv`.
- **Useful background:** the packet's dossier excerpts on the `weġ ~ wegas` contrast, because they explain why singular `weġ` is palatal while plural `wegas` is velar; the coverage/debug-snapshot material, because it shows the row is report-relevant and that the live system still outputs `weġ`.
- **Stale or superseded:** the packet's January 2026 diagnostic note `*wegăz -> weġ (expected wē)`. Per the packet-quality rules, that is diagnostic only, since it names a different expected target from the live `COUNTERPART`; it should not be treated as current lexical evidence.
- **Irrelevant or misleading if over-weighted:** the packet can make the TSV note look like the whole story. It is not: Kroonen's `*wega-` is a comparative stem citation, not by itself the row's derivational input, and the packet's generated mini-report text is just an echo of the TSV note rather than independent evidence.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at 2622-2623 and 43176-43360.
- `Germanic/docs/dossiers/g-palatalisation-conditioning.md`, especially §§1, 4, 5, and 7.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`.
- `Germanic/data/old_english_wiktionary.tsv`, `Germanic/data/old_english_swadesh.tsv`, and `Germanic/data/oe_known_problems.tsv`.
- Repo-local reference extracts in `docs/references/`: `kroonen_etymological_dictionary_pgmc.vision.txt`, `campbell_old_english_grammar.txt`, `hogg_vol1.txt`, and `ringe_taylor_linguistic_history_vol2.txt`.

Main findings from that wider check:
- Kroonen's comparative entry is `*wega- m. 'way, road'`, i.e. stem notation, with OE `weg m.` as the reflex.
- Ringe & Taylor explicitly give `PGmc *wegaz 'way' > PWGmc *weg > OE weg`, and separately give plural/dative outcomes `wegas, wegum`.
- Campbell and Hogg both use the same singular/plural contrast: singular `weġ` is palatal, but `wegas` stays velar because the following back vowel blocks palatalisation.
- `oe_known_problems.tsv` has no row-specific entry, and no separate pilot report was found.

## Reconstruction and early-stage forms
This row needs the usual three-way distinction, even though the two TSV proto columns currently match.

1. **Cognate-set proto / comparative headword:** Kroonen's stem citation `*wega-`, which corresponds to a nominative-singular form `*wégaz` in the row's modelling conventions.
2. **Project input form for OE derivation:** the live TSV `PROTOFORM` `*wégaz`, which the current cascade already handles correctly.
3. **OE target represented by the row:** project-normalized citation form `weġ`.

The checked references support this staging: `*wégaz` is the row-level derivational input, while Kroonen's `*wega-` is the lexicographic stem label for the wider cognate set. Early development is ordinary: PGmc `*wégaz` > PWGmc `*weg` / trace-stage `*wéga` > OE `*wég`, then word-final palatalisation gives normalized `weġ`. Nothing in the checked repo evidence supports replacing the row's proto/input with a long-vowel `*wē-` form.

## Old English philology
The OE lexeme is not a reconstructed convenience form. Repo-local lexical and reference materials support an actual OE noun `weg` 'way', which the project writes as normalized `weġ` when it wants the palatal outcome to be explicit.

Accordingly:
- **attested/dictionary side:** OE `weg` m. 'way' in Kroonen and the lexical table, with ordinary undotted dictionary spelling;
- **project-normalized target:** `weġ`, i.e. the same lexeme with palatal `ġ` made explicit;
- **inflectional contrast relevant to the philology:** singular/coda `weġ` versus plural/dative `wegas, wegum`, where the back-vowel ending keeps the consonant velar.

The important negative point is also secure: `wē` is not supported in the checked repo materials as the OE noun for 'way'. So the memo issue is not attestation versus reconstruction, but accurate interpretation of normalized spelling and of the singular/plural palatalisation contrast.

## Project problem and solution
The project problem here is not that the live FST fails to derive the row. It already derives `weġ` correctly.

The real issue is project chronology and interpretation:
- an older January diagnostic temporarily treated this lexeme as a long-vowel-missing case with `expected wē`;
- the later palatalisation dossier and handbook canvass show that the correct OE target is the ordinary singular `weġ/weg`, contrasted with velar `wegas` in back-vowel inflectional environments;
- Kroonen's `*wega-` stem citation should not be confused with a need to retarget the row away from `*wégaz -> weġ`.

So the current project solution should be: keep the row as a regular success case, explain that `weġ` is the intended normalized OE citation form, and treat the older `expected wē` note as superseded diagnostic history rather than live evidence.

## Paradigm probe
No paradigm probe is required.

This is not a hidden-cell or analogy-selection case. The decisive paradigm contrast (`weġ` sg. versus `wegas/wegum` oblique-plural forms) is already securely documented in Campbell, Hogg, and Ringe & Taylor, so a new probe would only duplicate evidence rather than resolve an open lexical choice.

## Recommended final report
Recommend a short final report stating that row 2277 correctly models regular `*wégaz` (Kroonen stem citation `*wega-`) to OE `weġ`, with `weġ ~ wegas` used as the key philological contrast for final palatalisation; it should also say explicitly that unattested `wē` belongs only to stale diagnostic history, not to the row's target.

## Data-change recommendations
- **TSV `PROTO`:** no change recommended; keep `*wégaz`.
- **TSV `PROTOFORM`:** no change recommended; keep `*wégaz` as the row's derivational input.
- **TSV `COUNTERPART`:** no change recommended; keep `weġ`.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` still fits.
- **TSV `NOTE`:** no substantive change recommended. It already captures the core philological point, though a later editorial tweak could clarify that Kroonen's `*wega-` is stem notation while the row itself models nominative-singular `*wégaz`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** `DEV_NOTES` cleanup is recommended, but dossier text is not. The 2026-01-02 `expected wē` diagnostic should be marked more explicitly as superseded by the later palatalisation review; `Germanic/docs/dossiers/g-palatalisation-conditioning.md` already reflects the current understanding and does not need row-specific cleanup.

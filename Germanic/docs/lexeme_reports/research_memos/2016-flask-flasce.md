# Research memo — 2016 flask / flasce

## Starting point

- **ID:** 2016
- **CONCEPT:** flask
- **COUNTERPART:** `flasce`
- **PROTO:** `*flaskō`
- **PROTOFORM:** `*fláskōn`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** empty

The live row already shows the central project split, but in a slightly unstable way: `PROTOFORM` has been corrected to the weak feminine input that the live FST can derive, while `PROTO` still preserves the older strong-ō analysis. There is no pilot/full lexeme report for this row in `report_manifest.tsv`, and `coverage_audit.md` accordingly still lists it as uncovered.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*fláskōn -> flasce`; the row-specific `DEV_NOTES.md` case at 3799-3852; and the packet’s citation of `analysis/arestoration_r_l_research.md`, which is the current repo-local authority on the broader A-restoration conditioning issue.
- **Useful background:** the packet’s quotations from Campbell, Luick, and Ringe & Taylor; `old_english_wiktionary.tsv`; and the dictionary snippets that show `flasce` plus variant `flaxe`.
- **Stale or superseded:** the packet’s row-ID hit at `DEV_NOTES.md:15558` is a false positive from an unrelated `cniht` note and is not evidence for row 2016; the packet’s preserved regression line `*fláskōn -> flascæ` is only intermediate debugging history; and the `DEV_NOTES` wording at 3830-3831 saying `*r`/`*l` “independently block A-restoration” is superseded by the later dedicated A-restoration analysis.
- **Irrelevant or misleading:** the packet’s “no manifest entry” notice is only coverage metadata, not lexical evidence; and the absence of an `oe_known_problems.tsv` hit should not be read as philological evidence, only as a sign that the row is not currently tracked as an unresolved exception.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 3799-3852 and 15556-15559.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `Germanic/docs/lexeme_reports/report_manifest.tsv`.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/oe_known_problems.tsv`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/luick_historische_grammatik.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.
- a live comparator run against `backend/old_english.bin` for `*flaskō` and `*fláskōn`.

Main findings from that extra pass:

- The live FST still gives the contrast that matters: `*flaskō -> flasc`, but `*fláskōn -> flasce`.
- Campbell explicitly cites `flasce` among the `sC`-cluster words with restored `a`, and does so “after inflected ... flascan”; Luick gives the same singular/plural logic; Ringe & Taylor likewise distinguish earlier `*flæske, *flæskon-` from OE `flasce, flascan`.
- Lexical reference files support `flasce` as an OE headword and also preserve variant `flaxe`; Ringe & Taylor explicitly label `flaxe, flaxan` as late West Saxon.
- No `oe_known_problems.tsv` entry exists, so this is not a live unmodelled-exception row.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** the live TSV still has `PROTO = *flaskō`, but that is the old strong-ō reading, not the best current etymological summary. The row’s own `HISTORY` and the checked repo references instead point to a weak feminine etymon (`Orel *flaskò(n)`, `Kroonen *flaskǭ`).
2. **Project input used for derivation:** `PROTOFORM = *fláskōn` is the current pre-OE modelling input. This is the form the live cascade can actually derive to `flasce`, because it preserves the weak feminine ending that later becomes NWGmc `*ǭ` and still triggers A-restoration in the corrected pipeline.
3. **OE target form represented by the row:** `flasce`, the OE singular target, with plural/oblique `flascan` and later WS variant `flaxe`.

Ringe & Taylor’s `*flæske, *flæskon- > OE flasce, flascan` and Campbell/Luick’s wording both matter here. They show that one should not collapse the levels into a single “PGmc `*flaskōn` straightforwardly became OE `flasce`” claim. The weak feminine stem is the right comparative starting point, but the singular OE form also belongs to a paradigm where restored `a` is supported by the inflected/plural forms.

## Old English philology

`flasce` is an attested OE lexeme, not a reconstructed convenience form. `old_english_wiktionary.tsv`, Clark Hall, and Bosworth-Toller all support the headword, and Brunner plus the dictionaries also preserve `flaxe` as a variant; Ringe & Taylor make that variant specifically late West Saxon.

The key philological distinction is between citation form and paradigm support. Campbell and Luick both present `flasce` with explicit reference to inflected/plural `flascan`, which is exactly the sort of evidence that supports analogical restoration of `a` in the singular. So the final report should treat `flasce` as the OE target, `flascan` as the relevant paradigm support, and `flaxe` only as a later variant, not as the primary row target.

## Project problem and solution

The original project problem was twofold. First, the older strong feminine analysis `*flaskō` produced `flasc`, because heavy-syllable apocope removed the final vowel. Second, once the weak stem `*fláskōn` was adopted, the pipeline still wrongly produced `flæsċe` until `*ǭ` was added to the A-restoration trigger set.

The current project solution is therefore coherent:

- keep the live derivational input as weak feminine `*fláskōn`;
- let the corrected A-restoration logic preserve root `a` before medial `*sk`;
- derive `flasce` as the OE target.

What remains conceptually untidy is the metadata split: `PROTOFORM` now reflects the corrected weak-stem analysis, but `PROTO` still displays the superseded strong-ō form. The row therefore works computationally, but its TSV metadata and explanatory prose still need cleanup so the evidence hierarchy is transparent.

## Paradigm probe

No paradigm probe is required.

This is not mainly a `late_analogy` cell-selection row where the project must choose among OE nominative, genitive, or dative inputs. The decisive contrast is upstream and already visible in the live comparator run: stale `*flaskō -> flasc` versus current `*fláskōn -> flasce`. If a future appendix wants an illustrative table, that comparator is enough; no missing OE paradigm cells need to be probed before a final report is written.

## Recommended final report

Recommend a concise final report that distinguishes the stale strong-ō history from the current weak-feminine analysis, keeps `PROTOFORM = *fláskōn` as the modelling input, treats `flasce` as the attested OE target with plural/oblique support from `flascan`, and notes `flaxe` only as a later variant. The report should also say explicitly that older project prose about `*r`/`*l` blocking A-restoration is superseded and not part of the `flasce` analysis.

## Data-change recommendations

- **TSV `PROTO`: change recommended.** The current `*flaskō` preserves the superseded strong-ō analysis. It should be updated to the weak-feminine cognate-set form cited in the row history and sources (with whatever normalization the project wants to standardize centrally, e.g. Kroonen-style `*flaskǭ` or an agreed project equivalent), so `PROTO` no longer contradicts the current evidence.
- **TSV `PROTOFORM`: no change recommended.** `*fláskōn` is the right live derivational input.
- **TSV `COUNTERPART`: no change recommended.** `flasce` is the correct OE target for this row.
- **TSV `DERIVATION_CLASS`: no change recommended for now.** `early_analogy` still usefully flags that the OE singular is being handled through an already reshaped weak-stem history rather than as a bare citation-form inheritance.
- **TSV `NOTE`: change recommended.** The row currently has no note. Add a short note explaining that the lexeme is weak feminine, that the live derivation uses `*fláskōn`, and that OE singular `flasce` is supported by plural/oblique `flascan` (with late WS `flaxe` only as a later variant).
- **`oe_known_problems.tsv`: no change recommended.** The row is currently solved, not an open exception.
- **DEV_NOTES/dossier text: change recommended.** `DEV_NOTES.md` should (1) fix the unrelated false row-number line at 15558, which currently names row 2016 in a `cniht` note, and (2) mark the old “`*r`/`*l` independently block A-restoration” wording in the `flasce` case as superseded by `analysis/arestoration_r_l_research.md`. No separate dossier rewrite is needed beyond keeping that later analysis as the current authority.

# Research memo — 2090 lap / lappa

## Starting point

- **ID:** 2090
- **CONCEPT:** lap
- **COUNTERPART:** `lappa`
- **PROTO:** `*lábbaz`
- **PROTOFORM:** `*láppô`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** empty

The live row already shows the important split between a cognate-set `PROTO` and an OE-facing `PROTOFORM`, but it does so unevenly. `PROTOFORM = *láppô` and `COUNTERPART = lappa` reflect the current successful derivation, while `PROTO = *lábbaz` is older set-level residue from the wider cognate set and no longer matches the repo-local OE analysis.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*láppô -> lappa`; the later `DEV_NOTES.md` regression-fix material (`36671`, `36704-36725`, `36744`, `36770`) confirming that `*láppô` should restore to `lappa`; and the grammar citations in `analysis/arestoration_r_l_research.md` showing that `lappa` is the regular restored form before geminate `pp`.
- **Useful background:** the dedicated `DEV_NOTES.md` section `14150-14345`; `old_english_wiktionary.tsv` as evidence that the extraction pipeline once preferred `læppa`; the packet’s Brunner/Campbell/Kluge/Orel/Kroonen snippets; and the dialect note from `ws_vs_anglian_dialect_differences.md`.
- **Stale or superseded:** the packet’s preserved earlier row state `*labbăz -> læppa`; the heading “OE læppa 'lap, skirt'” in `DEV_NOTES.md` 14150 ff.; and the implementation summary at `14338-14340`, which reflects the April repair moment but not the still-stale live `PROTO` field. Those are valuable project history, not final row authority.
- **Irrelevant or misleading:** “no manifest entry” and the absence of an `oe_known_problems.tsv` hit are only coverage metadata; `old_english_wiktionary.tsv` is supplementary rather than decisive; and Kroonen’s `*lōfan- ~ *lappan-` entry is supportive for stem shape and `pp`, but not by itself the final authority for the exact OE lemma gloss.

So the packet is a good dossier, but not a final evidence base. Its strongest material is the live trace plus the later A-restoration fix notes; its weakest material is the preserved pre-fix row history.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 14150-14345, 22571-22605, 30393-30405, 36667-36775, 36795-36800.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/docs/lexeme_reports/pilot/tap.md` as background only for the parallel n-stem `tappa/tæppa` issue.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/oe_known_problems.tsv`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.
- a manual `oe_paradigm_probe.py` check against `backend/old_english.bin` for `*láppô`, `*láppan`, and `*láppum`.

Main extra findings:

- Brunner gives `lappa (laeppa; Pl. leappan) swm.` and explicitly treats it as a weak masculine noun, not an a-stem.
- Campbell cites `lappa` as a textbook A-restoration example and separately cites `leappan d.s. skirt`, which shows that the paradigm contains non-citation vocalic variation without displacing nominative `lappa`.
- Clark Hall headwords the noun as `læppa` but cross-references `lappa (GL)=læppa`, so dictionary practice is mixed even though `lappa` itself is attested.
- Orel’s local entry gives `*lappōn sb.m.: OE lappa`; Kluge-Seebold likewise gives OE `lappa`, variant `läppa`, and West Germanic `pp`.
- The quick manual probe shows a unique citation-form match: `*láppô -> lappa`, while representative oblique/plural inputs give `lappan`, `lappum`.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** the live TSV still says `*lábbaz`, but that is the weakest part of the row. Repo-local sources support a weak-noun etymon with `pp`, not a strong a-stem with `bb`; Orel’s local citation is `*lappōn`, while Kroonen’s broader cognate-family material points to `*lappan-` rather than `*labb-`.
2. **Project input form used for derivation:** `PROTOFORM = *láppô`. This is the OE-facing weak masculine nominative singular that the current FST actually handles correctly.
3. **OE target form represented by the row:** `lappa`, i.e. the citation-form nominative singular. `læppa` and `leappan` belong in the philological background, not in the target slot for this row.

So this is an `early_analogy` case in the strong project sense: the row is not asking the FST to derive OE from the stale cognate-set label `*lábbaz`, but from an earlier reshaped weak-noun input `*láppô`. The mistake would be to collapse `*láppô`, `*lappōn`, and `lappa` into one undifferentiated “proto.”

## Old English philology

`lappa` is an attested OE lexeme, not a reconstructed OE convenience form. Campbell and Brunner both cite it directly, and Brunner also gives the variant set `lappa (laeppa; Pl. leappan) swm.`.

Three philological cautions matter:

- **Citation form vs. variant/headword practice:** Clark Hall headwords `læppa` but cross-references `lappa`; this is a dictionary-layout fact, not evidence that `læppa` must be the row target.
- **Citation form vs. inflected form:** `leappan` is an oblique/plural form in the paradigm, not a rival citation form for the row.
- **Attested variation:** `læppa` is real variant evidence, and Campbell/Brunner/Kluge all allow that background. But the repo-local grammar evidence treats `lappa` as the regular restored nominative-singular outcome, with `læppa` as doublet/variant rather than the default target.

The row should therefore be read as representing the attested weak masculine noun with citation-form `lappa`, while preserving `læppa` and `leappan` only as philological context.

## Project problem and solution

The project problem had two layers:

1. the older row state treated the word as strong `*lábbaz`, which was wrong in both voicing (`bb` vs. `pp`) and stem class;
2. the extraction history also targeted `læppa`, which over-weighted a real but non-default variant.

The current project solution is mostly right:

- keep `COUNTERPART = lappa`;
- keep `PROTOFORM = *láppô`;
- keep `DERIVATION_CLASS = early_analogy`, because the special move is an upstream stem-class/shape correction, not a late OE exception;
- treat `læppa` and `leappan` as variant/paradigm background.

What is still untidy is the surviving row metadata. `PROTO = *lábbaz` no longer expresses the row’s own evidential basis, and the empty `NOTE` leaves the row without the explanation that now has to be recovered from packet and `DEV_NOTES` history.

## Paradigm probe

No formal paradigm probe is required before a final report is written.

This is not a hidden-cell search like `late_analogy` rows. A quick manual probe already shows the relevant point: `*láppô -> lappa` is the unique citation-form winner, while representative oblique/plural forms give `lappan` and `lappum`, not some missing better target. If the final report wants a compact diagnostic table anyway, the only useful cells to show would be nom.sg. `*láppô`, representative oblique `*láppan`, and a plural/back-vowel cell such as `*láppum`.

## Recommended final report

Recommend a concise final report that says OE `lappa` is an attested weak masculine noun; that `PROTOFORM = *láppô` is the correct OE-facing input yielding regular `lappa`; that `læppa` and `leappan` are variant/paradigm background rather than the row target; and that the old `*lábbaz -> læppa` state is superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** change recommended. `*lábbaz` is not a good current row-level authority. Replace it with a weak-noun citation form with `pp` (ideally `*láppōn` or the project’s consistent equivalent), rather than leaving the row under a stale strong `*-az` label.
- **TSV `PROTOFORM`:** no change recommended. Keep `*láppô`.
- **TSV `COUNTERPART`:** no change recommended. Keep `lappa`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is still the right bucket.
- **TSV `NOTE`:** change recommended. Add a short note stating that OE `lappa` is a weak masculine n-stem citation form derived from `*láppô`, while `læppa` and `leappan` are variant/oblique evidence and the older `*lábbaz`/`læppa` setup is superseded.
- **`oe_known_problems.tsv`:** no change recommended. This row is currently solved, not a ledger exception.
- **`DEV_NOTES` text:** light cleanup recommended. The 2026-04-06 section should be clarified so readers can see that the live successful state is `PROTOFORM = *láppô`, `COUNTERPART = lappa`, with any wider `PROTO` correction still needing explicit treatment.
- **Dossier / analysis text:** no separate dossier change recommended. I found no dedicated lap-specific dossier; the named analysis files are fine as supporting background.

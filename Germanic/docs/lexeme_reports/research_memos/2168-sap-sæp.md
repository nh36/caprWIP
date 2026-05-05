# Research memo — 2168 sap / sæp

## Starting point

- **ID:** 2168
- **CONCEPT:** sap
- **COUNTERPART:** `sæp`
- **PROTO:** `*sapōn`
- **PROTOFORM:** `*sápą`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** `OE neut. a-stem (Hall, K-S); Kroonen: n-stem *safō dissolved dialectally`

The live row already encodes the key project split: `PROTO` preserves a cognate-set comparative form, while `PROTOFORM` is the pre-OE modelling input that the live FST actually sends to `sæp`. I found no pilot/full lexeme report for this row in `report_manifest.tsv`; `coverage_audit.md` still lists it as a required but uncovered lexeme-report case.

## Packet evidence assessment

**Authoritative/current:**
- The aligned TSV row is the current project state.
- The packet's compact derivation trace is current in substance: the live bins still give `*sapą` / `*sápą -> sæp`.
- The later `DEV_NOTES.md` section `### The Etymology of OE sæp 'sap'` is still the strongest repo-local explanation of why `*sapōn` and `*sapiz` fail but an a-stem input succeeds.
- `old_english_wiktionary.tsv` is modest but current confirmation of the OE headword `sæp`.

**Useful background:**
- The packet's comparative quotations from Kroonen, Kluge-Seebold, Orel, and Hall are useful background once checked against the repo reference files.
- The packet's coverage/manifest notices are useful only as workflow metadata showing that no manual report is already covering the row.

**Stale or superseded:**
- The older `DEV_NOTES.md` material at 3851-3860 is superseded. It still says expected `sæp` is itself problematic and points to OE `*sāpe`; that is older project history, not the current row logic.
- The packet preserves that older bucket-history line because it matches the string pair, but it should be treated as diagnostic implementation history rather than current lexical authority.

**Irrelevant or misleading:**
- `Manifest status: no manifest entry` is not lexical evidence.
- Kroonen's quote is valuable for comparative history, but its masculine OE label should not be treated as the final OE gender authority for this row; the repo's own Hall/Kluge evidence and live row treat the OE target as neuter.
- Orel's normalized `OE sap` is useful as cognate evidence, but not as precise OE orthographic authority against the ash-spelling `sæp`.

## Additional repo research

Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/docs/lexeme_reports/report_manifest.tsv`
- `Germanic/data/old_english_wiktionary.tsv`
- `Germanic/data/oe_known_problems.tsv`
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- live FST artifacts `backend/old_english.bin` and `Germanic/fsts/old_english.bin` via `oe_full_trace_report.py`

Main findings from that extra pass:
- No dedicated dossier or sap-specific analysis file turned up beyond the packeted `DEV_NOTES` material and the reference extracts.
- The live FST still gives the decisive comparator set in both authoritative bins: `*sapōn -> sape`, `*sapiz -> sepe`, `*sapą` / `*sápą -> sæp`.
- Kroonen's repo text does indeed argue for dialectal dissolution of a primary n-stem `*safō`; Orel gives `*sapōn ~ *sapan`; Kluge-Seebold instead gives WGmc `*sapi- m.` while explicitly calling OE `sæp` neuter.
- Clark Hall gives `sæp (e) n. 'sap,' juice`; Bosworth-Toller OCR hits show oblique `sæpe` occurrences, which fit the distinction between lemma `sæp` and inflected forms.
- `oe_known_problems.tsv` has no entry for this row, so the repo is not currently treating `sæp` as an unresolved exception.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction.

1. **Cognate-set proto / comparative headword:** TSV `PROTO = *sapōn` is functioning as a comparative shorthand for the inherited noun and its n-stem/an-stem history. It is not identical to Kroonen's fuller claim, which points behind the daughter forms to a primary n-stem `*safō` that dissolved dialectally.
2. **Project input form used for derivation:** TSV `PROTOFORM = *sápą` is the live pre-OE modelling input. In current project notation this is the early analogical strong neuter a-stem input that actually derives `sæp`. The unaccented comparator `*sapą` behaves the same way in the live bins.
3. **OE target form represented by the row:** `sæp`, the Old English target form of this row.

Kluge-Seebold's `*sapi-` is important comparative background, but it is not a viable direct OE modelling input here: in the live cascade `*sapiz` triggers the expected raising path and lands at `sepe`, not `sæp`. Likewise the older inherited weak/n-stem style input `*sapōn` gives `sape`. So the current project solution should be read narrowly: not as proof that the lexeme was "really" PGmc `*sapą`, but as the project's choice of the pre-OE input needed for the OE outcome.

## Old English philology

`Sæp` is an attested OE lexeme, not a reconstructed convenience form. Repo-local evidence supports that safely:
- `old_english_wiktionary.tsv`: `sap | sæp`
- `Clark Hall`: `sæp (e) n. 'sap,' juice`
- `Bosworth-Toller` OCR snippets: oblique `sæpe` in running-text citations
- `Kluge-Seebold`: `ae. sæp n.`

The safe philological claim is therefore modest but clear: the OE target is neuter `sæp`, with oblique `sæpe` forms visible in the lexical record. Nothing I found requires a special dialect or manuscript claim beyond the source abbreviations already attached by Hall.

Just as important, comparative dictionary normalization should not be mistaken for OE orthographic authority. Kroonen's masculine label and Orel's plain `sap` are relevant to cognate-set history, but the row should still target the attested OE ash-spelling `sæp`.

## Project problem and solution

The project problem was that inherited comparative inputs of the wrong stem type gave the wrong OE outcome: `*sapōn` yielded `sape`, and the tempting i-stem comparator `*sapiz` yielded `sepe`. The current row solves that by separating levels:

- keep a comparative proto in TSV `PROTO`;
- use early analogical a-stem `*sápą` in TSV `PROTOFORM` as the actual OE derivational input;
- target attested OE `sæp`.

So this should remain an `early_analogy` row, not a `late_analogy` paradigm-cell row and not an unresolved exception row. The core move is upstream stem/input selection, not selection among late OE inflectional cells.

## Paradigm probe

No paradigm probe is required.

This is not a row whose justification depends on choosing among OE nominative, genitive, or dative cells. The decisive evidence is already the live comparator contrast between `*sapōn`, `*sapiz`, and `*sapą` / `*sápą`, which is an upstream reconstruction/input question rather than a missing OE paradigm-cell question. If a future appendix wants an illustrative table, those three comparators are enough; no additional OE cells need to be probed for the memo stage.

## Recommended final report

Recommend a concise final report saying that OE `sæp` is the attested neuter target, that comparative sources disagree over the inherited stem history (`*safō`, `*sapōn ~ *sapan`, `*sapi-`), and that the project therefore keeps a comparative `PROTO` while using `PROTOFORM = *sápą` as the pre-OE modelling input because the live FST gives `sape`, `sepe`, and `sæp` for the relevant comparators respectively.

## Data-change recommendations

- **TSV `PROTO`: no change recommended.** Keep `*sapōn` as the row's comparative headword shorthand, but do not read it as the direct pre-OE input.
- **TSV `PROTOFORM`: no change recommended.** `*sápą` is the right live project input for deriving `sæp`.
- **TSV `COUNTERPART`: no change recommended.** `sæp` is the correct OE target.
- **TSV `DERIVATION_CLASS`: no change recommended.** `early_analogy` correctly describes the row.
- **TSV `NOTE`: change recommended.** Revise it so it explicitly distinguishes the comparative stem-history problem from the modelling choice: Kroonen's dissolved n-stem and Kluge-Seebold's `*sapi-` belong to the cognate-set discussion, while the project uses `*sápą` because `*sapōn -> sape`, `*sapiz -> sepe`, and only the a-stem comparator yields `sæp` in the live FST.
- **`oe_known_problems.tsv`: no change recommended.** This row is currently treated as solved, not as a live exception.
- **DEV_NOTES/dossier text: change recommended.** Mark `DEV_NOTES.md` 3851-3860 explicitly as superseded by the later `sæp` analysis and by the live TSV/FST state, so future packets do not recycle the old `*sāpe` claim as if it were current. No separate dossier text change is required, because no dedicated sap dossier is currently in play.

# Research memo — 2286 whine / hwīnan

## Starting point

- **ID:** 2286
- **CONCEPT:** whine
- **COUNTERPART:** hwīnan
- **PROTO:** *wainōjaną
- **PROTOFORM:** *xwḯnaną
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** -

This is a report-requiring row because `DERIVATION_CLASS` is non-regular. `coverage_audit.md` marks row 2286 as uncovered, and no pilot/full lexeme report for `whine / hwīnan` was found.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing that the current cascade maps `PROTOFORM *xwḯnaną` to `hwīnan`; and `Germanic/docs/DEV_NOTES.md` 3660-3685, which is the current repo-local correction note explaining why OE `hwīnan` must be separated from PGmc `*wainōjan-` / OE `wānian`.
- **Useful background:** `old_english_wiktionary.tsv` confirms the OE counterpart `hwīnan`; the packet’s bibliography leads point to the right source family (especially Kroonen); and the packet correctly shows that there is no live `oe_known_problems.tsv` entry.
- **Stale or superseded:** the packet’s row-data line is internally mixed. Its `PROTO = *wainōjaną` reflects the old cognate-set assignment, while its `NOTE/HISTORY` already say that this linkage is spurious. The older `DEV_NOTES.md` table at line 2832 and `non_firing_rules_analysis.md` (`*wainōjăną -> wānēġan (expected hwīnan)`) are diagnostic remains from the pre-correction state, not current lexical authority.
- **Irrelevant or misleading:** the phase/batch note at `DEV_NOTES.md` 42026 is only workflow history, not lexical evidence. Kluge/Seebold’s descendant listing of NE *whine* under German *weinen* is useful only as evidence of earlier conflation, not as positive authority for the OE row.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 2832, 3660-3685, and 42020-42026.
- `Germanic/docs/non_firing_rules_analysis.md` 493-505.
- `Germanic/docs/lexeme_reports/coverage_audit.md` 160-172.
- `Germanic/data/oe_known_problems.tsv` — no relevant entry.
- `Germanic/data/old_english_wiktionary.tsv` — `whine -> hwīnan`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — `*hwinan-` and separately `*wainōn-`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — `*xwinanan` strong verb.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — PNWGmc `*h“inana` / OE `hwinan`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — `hwinan` glossed ‘to hiss, whizz, whistle’.
- `docs/references/seebold_vergleichendes_woerterbuch.vision.txt` — `hwinan` with only a present-tense attestation noted.
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` — `hwinan` listed among strong verbs.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt` — `ne. whine` listed under *weinen*, i.e. evidence of conflation rather than good authority for this OE row.
- Searched `Germanic/docs/analysis/` and `Germanic/docs/dossiers/` for `hwīnan`, `whine`, `*hwīnăną`, and `*wainōjaną`; no dedicated dossier or analysis file for this lexeme was found.

Main result of the wider pass: the live derivation input is now correct, but the row is still framed as if this were an ordinary early-stage reshaping inside the `*wainōjaną` cognate set. The sources instead support a lexeme switch: OE `hwīnan` belongs with PGmc `*hwīnan-/*xwinanan`, while OE `wānian` belongs with PGmc `*wainōjan-`.

## Reconstruction and early-stage forms

This row needs an explicit three-way distinction, but here the first and second layers no longer belong to the same etymon.

1. **Current cognate-set proto in TSV:** `PROTO = *wainōjaną`. This is the older concept-level headword shared with ModE `whine` and German `weinen` in the aligned set.
2. **Project input form for the OE cascade:** `PROTOFORM = *xwḯnaną`, the project’s stress-marked FST input that corresponds to the corrected PGmc/PNWGmc verb cited in the sources (`*hwīnăną`, Kroonen’s `*hwinan-`, Orel’s `*xwinanan`, Ringe-Taylor’s `*h“inana`).
3. **OE target represented by the row:** `hwīnan`.

The crucial point is that `*wainōjaną` and `*xwḯnaną` are not two stages of the same lexeme. They differ in onset (`w-` vs. `hw-/xw-`), vowel (`ai` vs. `ī`), and verb class (weak II vs. strong I). `PROTOFORM` here is not a paradigm-cell rescue and not an analogical stem variant of `PROTO`; it is the replacement of a wrong etymon with the one that actually underlies OE `hwīnan`.

That makes the current row only partly analogous to other `early_analogy` items such as `craft` or `bottom`. In those rows, `PROTO` and `PROTOFORM` are still versions of the same lexeme. Here they are competing lexemes, and the corrected OE input is better understood as a retargeted etymology.

## Old English philology

The OE side is much cleaner than the project-history side.

- `old_english_wiktionary.tsv` and Clark Hall support `hwīnan` / `hwinan` as the OE counterpart.
- Clark Hall glosses it as ‘to hiss, whizz, whistle’, which is slightly broader and noisier than the Modern English concept label *whine*.
- Seebold notes only a present-tense attestation (`Nur ein Präsensbeleg hwinan`), so the repo should avoid claiming a rich attested paradigm that it has not documented.
- Brunner and Orel treat the verb as a strong verb (`stv.` / `str.vb.`), matching the repo-local correction note that contrasts it with weak II `wānian`.

So the philological issue is not whether `hwīnan` is a real OE headword. It is. The issue is that the row’s older cross-Germanic alignment confused that attested OE strong verb with a different lament/weep verb family.

## Project problem and solution

The project has already solved the derivational part of the problem but not fully the row-design part.

1. **Solved:** replacing the live OE input with `PROTOFORM = *xwḯnaną` now yields `hwīnan` in the cascade.
2. **Not fully solved:** the row still carries `PROTO = *wainōjaną` and `DERIVATION_CLASS = early_analogy`, which makes the case look like an internal pre-OE reshaping of one lexeme. The repo-local evidence instead says the old alignment was a wrong cognate assignment.

The best current reading is therefore:

- OE `hwīnan` should be treated as continuing PGmc `*hwīnan-` (project-normalized `*xwīnaną / *xwḯnaną`),
- OE `wānian` belongs to PGmc `*wainōjan-`,
- the old `whine ~ weinen` linkage is a project-history error, not the lexical analysis the final report should preserve.

In other words, the live `PROTOFORM` is right, but the metadata still describes the case as if it were merely an early analogical input choice. The memo evidence supports treating it as a **lexeme-retarget / wrong-cognate** case instead.

## Paradigm probe

A paradigm probe is **not required** for this row.

The dispute is not about choosing among hidden inherited cells. It is about replacing a wrong weak-verb etymon with the correct strong-verb etymon. The existing derivation trace already shows that the corrected citation-form input `*xwḯnaną` yields `hwīnan`; probing additional cells would not answer the cognate-assignment question.

## Recommended final report

Recommend a concise final report that treats this as a lexeme-retarget case: OE `hwīnan` is the attested strong verb ‘hiss/whizz/whistle; whine’ continuing PGmc `*hwīnan-` (project input `*xwḯnaną`), not the `*wainōjan-` family of OE `wānian` / German `weinen`. The final report should cite the correction in `DEV_NOTES` plus Kroonen, Orel, Ringe-Taylor, and OE dictionary evidence, and it should avoid presenting the row as an ordinary early-analogy stem choice.

## Data-change recommendations

- **TSV `PROTO`:** **change recommended** from `*wainōjaną` to the project-normalized form of the corrected etymon, i.e. `*xwīnaną` (or equivalent house-style normalization). Keeping `*wainōjaną` now preserves a spurious cognate assignment, not a useful citation headword for this OE row.
- **TSV `PROTOFORM`:** no change recommended. `*xwḯnaną` is the right live derivational input.
- **TSV `COUNTERPART`:** no change recommended. `hwīnan` is the right OE target.
- **TSV `DERIVATION_CLASS`:** **change recommended** from `early_analogy` to `lexeme_retarget`. The core issue is wrong etymon/cognate assignment, not ordinary early analogical remodeling within one lexeme.
- **TSV `NOTE`:** **change recommended.** Rewrite it to front-load the retargeting diagnosis explicitly (e.g. “Wrong cognate assignment / lexeme retarget: OE `hwīnan` continues PGmc `*hwīnan-`, not `*wainōjan-` ...”). That will also let the derivation-class tooling classify the row more transparently.
- **`oe_known_problems.tsv`:** no change recommended. There is no remaining live FST mismatch once the corrected input is used.
- **DEV_NOTES / dossier text:** no required change to the main correction note at `DEV_NOTES` 3660-3685; it is the current authoritative project record. Optional cleanup only: add a brief “superseded by the correction below” pointer near the older diagnostic `*wainōjăną -> ... expected hwīnan` material if future packet generation keeps surfacing it as background.

# Research memo — 2274 water / wæter

## Starting point

- **ID:** 2274
- **CONCEPT:** water
- **COUNTERPART:** wæter
- **PROTO:** *wátną
- **PROTOFORM:** *wátōr
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Kroonen *watar-/*watan- r/n-stem, nom.sg. *watōr; R/T §3.1.4 *ō→*a before final *r in PWGmc.

This is a note-bearing `early_analogy` row in `coverage_audit.md`. No standalone pilot/full lexeme report for water is present under `Germanic/docs/lexeme_reports/pilot/`; generated debug-snapshot prose is background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*wátōr -> wæter`; the live lexical-table hits in `old_english_wiktionary.tsv` and `old_english_swadesh.tsv`; and the adopted `DEV_NOTES.md` water-fix section at 3120-3147, which explains why the row now derives correctly.
- **Useful background:** `analysis/unstressed_e_o_before_r.md` for `*watar -> wæter` as the regular outcome before `r`; `analysis/notable_findings.md` for the A-restoration trigger correction and for the short-root non-syncope discussion; and `analysis/ws_vs_anglian_dialect_differences.md` for the WS `wæter` versus Mercian `weter` distinction.
- **Stale or superseded:** the packet itself is fairly clean, but additional repo research shows older project stages in which water was tried as `*watną` and then as interim `*watrą`. Those stages are useful history only; they are not the current row analysis. Debug snapshots that merely echo the live trace are likewise secondary.
- **Irrelevant or misleading:** the packet's hit in `docs/dossiers/bugan-scufan-paradigm-cell-review.md` is only a quotation containing the string **wæter** and is not evidence about row 2274. The packet's string-level concept hits elsewhere should not be treated as direct authority unless they discuss this lexeme's own reconstruction.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` at 3120-3150 and 16615-16706.
- Full analysis files named in the packet: `Germanic/docs/analysis/unstressed_e_o_before_r.md`, `Germanic/docs/analysis/notable_findings.md`, and `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2274.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — heteroclitic `*watar-~*watan-`, with reconstructed `*watōr, *watenaz` behind the paradigm.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — PGmc/PWGmc `*watōr > *watar` and OE `weter/weeter`, plus WS/Mercian differentiation and short-stem inflectional examples.
- `docs/references/bright_anglo_saxon_reader.vision.txt` — explicit OE paradigm `wæter, wæteres, wætere, wæter(u), wætera, wæterum`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `Germanic/docs/lexeme_reports/pilot/` — no existing water pilot report.
- A manual `oe_paradigm_probe.py` run for this row: `*wátną -> wætn` (non-match), `*wátōr -> wæter` (exact match).

The wider repo pass confirms that the row's real issue is not the OE target form itself, but the distinction between the generalized cognate-set headword and the specific inherited nominative-singular input needed for the OE derivation.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction kept explicit:

1. **Cognate-set proto / TSV headword:** `PROTO = *wátną`. In the live TSV this is the cross-row cognate-set label, but it is not the form the OE derivation should start from.
2. **Project derivational input:** `PROTOFORM = *wátōr`, i.e. the reconstructed r/n-stem nominative/accusative singular highlighted in the note and in `DEV_NOTES.md`.
3. **OE target represented by the row:** `wæter`, the OE citation form this row is meant to model.

The main reconstruction point is that the row note is more precise than the bare `PROTO` field. Kroonen's etymology is heteroclitic `*watar-/*watan-`, not a simple one-shape `*watną` lemma. The current project solution is therefore to keep the generalized cognate-set headword in `PROTO`, but to drive the OE row from the paradigmatically specific `PROTOFORM` `*wátōr`.

Once that distinction is made, the early-stage derivation is straightforward:

- `*wátōr -> *watar` by PWGmc shortening/lowering of long `*ō` before final `*r`;
- `*watar -> *wætær` by Anglo-Frisian brightening;
- `*wætær -> wæter` by the unstressed `æ/e` merger.

That is the current authoritative analysis. Earlier repo history with `*watrą` was an interim workaround via epenthesis, and the older `*watną` input belongs only to the generalized headword layer, not to the selected OE derivational input.

## Old English philology

- **Attested vs. reconstructed:** exact OE `wæter` is directly supported in the repo's lexical tables and reference material; this is not a merely reconstructed target.
- **Citation form vs. inflected forms:** Bright's paradigm is especially useful here because it shows the row target as the nominative/accusative singular `wæter` and also preserves the expected oblique and plural cells `wæteres`, `wætere`, `wæter(u)`, `wætera`, `wæterum`.
- **Dialect/manuscript caution:** Ringe-Taylor's dialect table supports WS `wæter` versus Mercian `weter`. The row should therefore be described as the WS-compatible OE target, not as a claim that every OE dialect had exact `wæter`.
- **No rival headword problem of the summer/mother type:** unlike rows where the attested lemma tradition competes with the project's regularized target, this row's exact target `wæter` is already the standard OE form in repo-local lexical evidence. The philological complication lies in the proto-side heteroclitic reconstruction, not in the OE citation form.
- **Syncope background:** `notable_findings.md` and Bright's paradigm both support retention of the medial vowel after a short root syllable (`wæter`, `wæteres`), so the row does not need to be framed as a syncopated or exceptional OE shape.

## Project problem and solution

The project problem had two layers.

First, there was a **computational analysis issue**: the FST originally mishandled the word because the project lacked the PWGmc `*ō -> *a / _ r#` step and because A-restoration was over-triggering from unstressed `*æ`, yielding erroneous `water` instead of `wæter`.

Second, there was a **representation issue**: the cognate set can be labelled with a generalized proto headword, but the OE row itself must be derived from the inherited nominative singular `*wátōr`, not from generalized `*wátną` and not from the older interim workaround `*watrą`.

The current solution is coherent:

- keep `PROTOFORM = *wátōr` as the active OE input;
- keep `COUNTERPART = wæter` as the OE target;
- treat `PROTO = *wátną` only as the cognate-set label under the present TSV schema;
- explain in the note/report that the row represents a heteroclitic r/n-stem whose OE reflex depends on the nominative-singular input.

On project-internal grounds, `early_analogy` remains defensible because the row does not simply derive from the generalized lexeme headword; it depends on an inherited paradigm-specific early form.

## Paradigm probe

A paradigm probe is **required in principle** for documentation, because the row's central issue is exactly the contrast between the generalized headword and the selected nominative-singular input.

The crucial comparison has already been confirmed manually:

- `*wátną -> wætn` (**non-match**)
- `*wátōr -> wæter` (**exact match**)

So the philological point is not missing; what is missing is only a reusable built-in probe spec for this lexeme. If the project wants to formalize the probe in `oe_paradigm_probe.py`, the minimum cells should be:

- **generalized headword / n-stem comparison:** `*wátną`
- **nom./acc.sg. r-stem input:** `*wátōr`

An optional fuller probe could add the heteroclitic oblique side (e.g. gen.sg. `*wátenaz`) to make the r/n alternation explicit, but that is not necessary for the present memo.

## Recommended final report

Recommend a short final report that says row 2274 keeps a generalized cognate-set `PROTO` but derives the OE row from heteroclitic nominative-singular `PROTOFORM` `*wátōr`; that once PWGmc pre-final-`r` lowering and the corrected A-restoration analysis are applied, the derivation to attested OE `wæter` is regular; and that Mercian `weter` plus inflected `wæteres/wætere` are supporting background, not reasons to retarget the row.

## Data-change recommendations

- **TSV `PROTO`:** no immediate change recommended. Under the current one-form TSV schema, `*wátną` can remain the cognate-set label, though it is less precise than the heteroclitic stem notation used in the note.
- **TSV `PROTOFORM`:** no change recommended; `*wátōr` is the correct derivational input.
- **TSV `COUNTERPART`:** no change recommended; `wæter` is both derivationally correct and directly supported in repo-local OE evidence.
- **TSV `DERIVATION_CLASS`:** no change recommended; `early_analogy` remains an acceptable project label for a row that depends on a paradigm-specific inherited input rather than the generalized headword.
- **TSV `NOTE`:** **change recommended.** The note should say more explicitly that `PROTO` is the generalized cognate-set headword, that `PROTOFORM` is the inherited nominative singular `*wátōr`, and that the OE target `wæter` is directly attested; it would also help to mention WS `wæter` versus Mercian `weter` so the dialectal background is not flattened.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no required change. The adopted water-fix sections are already sound; older `*watną` and `*watrą` discussion is acceptable as project history so long as future packets continue to treat it as superseded background. There is no dedicated water dossier text that now requires cleanup.

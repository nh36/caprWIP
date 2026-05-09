---
row_id: 2286
concept: whine
counterpart: hwīnan
proto: *wainōjaną
protoform: *xwḯnaną
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2286-whine-hwīnan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2286-whine-hwīnan.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2286 whine / hwīnan

## Current row state

- The live Old English row reads `CONCEPT = whine`, `COUNTERPART = hwīnan`, `PROTOFORM = *xwḯnaną`, `PROTO = *wainōjaną`, `DERIVATION_CLASS = early_analogy`, with the row note already spelling out the correction: “OE `hwīnan` (str. I) 'to whine, hiss' < PGmc `*hwīnăną` ... Not cognate with German `weinen` < PGmc `*wainōjan-` (→ OE `wānian` 'to lament'); cognate linkage is spurious” [Germanic/data/germanic-aligned-final.tsv:1382-1382].
- `PROTO`, `PROTOFORM`, and `COUNTERPART` are therefore **not** three labels for one uncomplicated inheritance chain. In the live TSV state, `PROTO = *wainōjaną` is the older cognate-set headword still shared with ModE `whine` and German `weinen`; `PROTOFORM = *xwḯnaną` is the corrected row-level derivational input for the Old English cascade; `COUNTERPART = hwīnan` is the attested OE strong verb that the row is actually trying to derive [Germanic/data/germanic-aligned-final.tsv:1381-1383].
- The existing packet and research memo are worth linking because both already recognize that mixed state. They preserve the authoritative correction note at `DEV_NOTES` 3660-3685, but they also make clear that the row still carries older metadata from the spurious `*wainōjaną` alignment [Germanic/docs/lexeme_reports/packets/2286-whine-hwīnan.md:5-19; Germanic/docs/lexeme_reports/research_memos/2286-whine-hwīnan.md:15-20].
- No row-specific pilot, dossier, or dedicated analysis file was located beyond those two support files. `coverage_audit.md` still marks row 2286 as uncovered, so the infrastructure status lags behind the actual packet/memo work [Germanic/docs/lexeme_reports/coverage_audit.md:168-168].
- The live derivational snapshot is mechanically clean at the `PROTOFORM` layer: `# whine / PROTO: *xwḯnaną / EXPECTED: hwīnan / OUTPUTS: hwīnan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6842-6855]. `old_english_wiktionary.tsv` likewise supports the counterpart pairing `whine -> hwīnan` [Germanic/data/old_english_wiktionary.tsv:343-343].

## Development-note summary

The surviving DEV_NOTES material for this row is unusually strong on the **cognate correction** itself and much weaker on everything before or after it. The key row-local note is the correction block at lines 3660-3685, which states flatly that “The OE row for 'whine' (ID 2286) had proto `*wainōjăną`, which is the reconstruction for PGmc `*wainōjan-` 'to lament, weep' (→ OE `wānian`, German `weinen`, ON `veina`). But the OE target form `hwīnan` is a Class I strong verb meaning 'to whine, hiss, rush', which Kroonen (2013, s.v. `*hwīnan-`) derives from PGmc `*hwīnăną`, tracing it to PIE `*ḱwey-` 'to hiss, whistle'” [Germanic/docs/DEV_NOTES.md:3662-3666; @Kroonen2013]. That statement, not the older weak-verb diagnostics, is the surviving project authority for row 2286.

The note is important because it does **not** describe a normal analogical repair within one lexeme. It explicitly argues that two different etyma had been conflated. DEV_NOTES continues: “The initial `*hw-` (< PIE `*ḱw-`) vs. `*w-` and the vowel grade (`*ī` vs. `*ai`) confirm that these cannot be the same lexeme” [Germanic/docs/DEV_NOTES.md:3675-3677]. That is the crux of this slice. `PROTOFORM = *xwḯnaną` is not merely an alternate stem of `PROTO = *wainōjaną`; it is the row's corrected derivational input after the project recognized that the previous cognate assignment was wrong. The row's present metadata preserves both stages at once: the old set-level `PROTO`, and the corrected OE-facing `PROTOFORM`.

External handbook and dictionary evidence aligns with that split more cleanly than the TSV metadata does. Kroonen has separate entries for `*hwinan-` (“OE `hwinan` s.v. 'id.'”) and for the lament-family `*kwainōjan-` (“OE `cwānian` w.v. 'to lament, mourn'”) [@Kroonen2013; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:14662-14675,16898-16900]. Orel likewise separates strong `*xwinanan str.vb.` “ON `hvína` 'to whizz, to whistle', OE pres. `hwinan` id.” from the distinct weak lament verb family `*wainōjanan wk.vb.` [@Orel2003; docs/references/orel_handbook_germanic_etymology.vision.txt:23282-23285,48598-48604]. Ringe and Taylor give the Northwest Germanic continuation directly as “PNWGmce `*h“inana` ‘to whine’ (ON `hvina`, OE `hwinan`)” [@RingeTaylor2014; docs/references/ringe_taylor_linguistic_history_vol2.txt:7747-7748]. For the OE lexeme itself, Clark Hall glosses `hwinan¹` as “to hiss, whizz, whistle. ['whine'],” Seebold notes “Nur ein Präsensbeleg `hwinan` 'zischen, sausen',” and Brunner lists `hwinan stv.` as a strong verb [@ClarkHall1960; @Seebold1970; @Brunner1965; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:23879-23880; docs/references/seebold_vergleichendes_woerterbuch.vision.txt:15452-15454; docs/references/brunner_1965_altenglische_grammatik.vision.txt:25449-25449]. All of that supports the DEV_NOTES correction and keeps `hwīnan` away from OE `wānian`.

The one notable complication is that some secondary lexicographic tradition itself helped create the confusion. DEV_NOTES records that “Kluge/Seebold (24th ed., s.v. _weinen_) lists 'ne. whine' among descendants of g. `*wainō-`, but this appears to be a conflation; NE _whine_ continues OE `hwīnan` (str. I), not OE `wānian` (wk. II)” [Germanic/docs/DEV_NOTES.md:3681-3683]. The OCR extract confirms the descendant listing under German `weinen`: “Ebenso nndl. `weenen`, ne. `whine`, nschw. `vena`, nisl. `veina`” [@KlugeSeebold2011; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:98089-98093]. For this slice, that is diagnostic evidence of earlier conflation, not positive authority for the OE row. The working-note conclusion should stay conservative: the row's corrected `PROTOFORM` is well supported, but the surviving `PROTO = *wainōjaną` and `DERIVATION_CLASS = early_analogy` still describe the row as if it were an internal reshaping within the wrong cognate set.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3660-3685

Source heading: `TSV proto correction: *wainōjăną → *hwīnăną (OE hwīnan 'to whine')`
Source line or section hint: lines 3660-3685
Fragment type: row_specific_correction_note
Status: current
Issue tags: wrong_cognate;lexeme_split;proto_vs_protoform;weinen_vs_hwīnan
Recommended next use: cite_in_final_report
Shared with row IDs: 689; 688
Text or paraphrase:
This is the decisive lexeme-local fragment and the only strong candidate for future indexing. It states the full correction in self-contained form: old `*wainōjăną` belongs to the lament/weep family (`OE wānian`, German `weinen`, ON `veina`), while row 2286's actual Old English target `hwīnan` is a Class I strong verb from PGmc `*hwīnăną` [Germanic/docs/DEV_NOTES.md:3662-3666]. The note then makes the distinguishing diagnostics explicit — initial `*hw-` versus `*w-`, and vowel `*ī` versus `*ai` — before concluding that “these cannot be the same lexeme” [Germanic/docs/DEV_NOTES.md:3675-3677]. It also preserves useful project history: the error seems to have come from automatic cognate-linking, German `weinen` is “unaffected,” and the practical row fix was that “Proto changed to `*hwīnăną`; pipeline now produces `hwīnan` ✓” [Germanic/docs/DEV_NOTES.md:3677-3685]. For later work, this fragment is strong enough to stand on its own without importing the rest of DEV_NOTES.

### DEV_NOTES:line-2832-2836

Source heading: `All 8 Class II Weak Verbs in TSV (all produce -eian)`
Source line or section hint: lines 2832-2836
Fragment type: superseded_diagnostic_fragment
Status: superseded
Issue tags: pre_correction_state;weak_verb_misclassification;i_umlaut_missing
Recommended next use: use_only_to_explain_old_project_state
Shared with row IDs: 2286
Text or paraphrase:
This older table preserves the row's **pre-correction** diagnostic state and should not be mistaken for current lexical authority. It lists `*wainōjăną | wāneian | hwīnan | i_umlaut_missing` among Class II weak-verb failures and immediately comments that the shared `-ōja-` issue is “morphological ... not phonological” and outside the FST's remit [Germanic/docs/DEV_NOTES.md:2832-2836]. That is useful evidence for chronology — before the lexeme split was recognized, the project was still trying to force `hwīnan` into the weak `*wainōj-` bucket and treating the mismatch as an umlaut/suffix problem. But it is stale after the 3660-3685 correction, because the real issue was not missing i-umlaut inside one verb family; it was that the row had been attached to the wrong verb family altogether.

### DEV_NOTES:line-42020-42026

Source heading: batch recap table for the `*ḯ` migration work
Source line or section hint: lines 42020-42026
Fragment type: workflow_history_only
Status: diagnostic
Issue tags: workflow_batching;not_lexical_evidence
Recommended next use: ignore_for_lexeme_argument
Shared with row IDs: 2290; 2296
Text or paraphrase:
This table simply records that `hwīnan` was processed in batch 5 of a later workflow pass [Germanic/docs/DEV_NOTES.md:42020-42026]. It is useful only for reconstructing project chronology at a very high level. It does **not** add lexical evidence, does not refine the `hwīnan`/`wānian` split, and should not be used as an index anchor when the stronger row-specific correction note at 3660-3685 already exists.

## Superseded or diagnostic material

The main superseded material is the entire older idea that row 2286 was a weak-verb `*wainōjăną` problem. `non_firing_rules_analysis.md` still gives the old diagnosis in compressed form: “`*wainōjăną -> wānēġan (expected hwīnan)`” under “I-Umlaut Missing” [Germanic/docs/non_firing_rules_analysis.md:493-500]. That line is useful because it shows how the row originally entered the repair queue, but it is plainly pre-correction: the expected form `hwīnan` does not belong to the same etymon as the proposed weak-verb output. It should therefore be cited only as a diagnostic fossil from the old analysis stage.

The packet and memo are mostly current in their argument, but they inherit the same mixed-state problem as the row itself: they can accurately say that the corrected OE input is `*xwḯnaną`, yet the row-level metadata and surrounding coverage infrastructure still preserve `PROTO = *wainōjaną`, `DERIVATION_CLASS = early_analogy`, and an uncovered-audit state [Germanic/docs/lexeme_reports/packets/2286-whine-hwīnan.md:15-20,177-185; Germanic/docs/lexeme_reports/research_memos/2286-whine-hwīnan.md:15-20,92-98; Germanic/docs/lexeme_reports/coverage_audit.md:168-168]. That means later report-writing should quote the correction note and the primary dictionaries directly rather than merely restating packet metadata.

Finally, the Kluge/Seebold descendant list should be preserved only as evidence of conflation. DEV_NOTES already treats it that way, and this slice should do the same. It is not a reason to reunite `hwīnan` with German `weinen`; it is part of the paper trail explaining why that reunion looked plausible in some secondary sources before the project separated the lexemes [Germanic/docs/DEV_NOTES.md:3681-3683; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:98089-98093].

## Open questions for later work

- If the row is ever normalized for final reporting, the metadata should probably be reviewed as a **wrong-cognate / lexeme-retarget** case rather than left framed as ordinary `early_analogy`; this slice records the evidence for that judgment but does not itself change the row.
- A later final lexeme report should keep the three layers explicit near the top: `PROTO = *wainōjaną` as surviving set-level legacy metadata, `PROTOFORM = *xwḯnaną` as the corrected derivational input, and `COUNTERPART = hwīnan` as the attested OE strong verb.
- For indexing work, the only strong DEV_NOTES anchor is the row-specific correction note at `DEV_NOTES:line-3660-3685`. The earlier table at `line-2832-2836` and the batch note at `line-42020-42026` are worth preserving as chronology, but they are too stale or too procedural to serve as primary index anchors.

---
row_id: 1968
concept: breast
counterpart: brēost
proto: *brústz
protoform: *bréustą
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1968-breast-brēost.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1968-breast-brēost.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1968 breast / brēost

## Current row state

- CONCEPT: `breast`
- COUNTERPART: `brēost`
- PROTO: `*brústz`
- PROTOFORM: `*bréustą`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: blank.

## Development-note summary

Row 1968 is only coherent if the project keeps three levels separate. The live row's comparative headword is `PROTO = *brústz`, the wider root-noun cognate set reflected in Gothic `brusts`, continental West Germanic `brust`-type forms, and other non-OE comparators. The row-specific OE derivational input is `PROTOFORM = *bréustą`, and the attested OE target is `brēost`. Early debugging treated `*brustz -> brust/burst` as if it were a broken OE-breaking case, but that was a false comparator: the wrong proto formation had been sent into the OE cascade in the first place [DEV_NOTES:line-1715-1717].

The March 2026 source audit is still the main current evidence for the philological side. It preserves Kroonen's distinction between root-noun `*brust-` and thematic `*breusta-`, carrying over the direct quotation that the second formation includes "ON brjóst n. 'id.', OE bréost n. 'id.', E breast, OFri. briast n. 'id.', OS briost n. 'id.'" while the first lists Gothic, Frisian `brust/burst`, Saxon, and German comparators but no OE reflex [DEV_NOTES:line-5924-5983; @Kroonen2013, pp. 76-77]. The same fragment also preserves Orel's matching split between `*breustan` and `*brustz` [@Orel2003, pp. 57-58], Ringe and Taylor's explicit NWGmc comparator "PNWGmc *breusta 'breast' (ON brjóst, OS briost) > OE bréost (OF briast)" [@RingeTaylor2014, p. 160], and Campbell's use of `brēost` as an example of OE `*eu > ēo` [@Campbell1959, §115]. Taken together, those sources make the core contrast explicit: regular OE outcome from the `*breusta-/*breustą` branch is `brēost`, whereas a true `*brust-` input would point toward `brust`-type outcomes, not `brēost`.

That same March note also preserves one project move that is no longer current as row metadata. Its fix line says "Changed OE PROTO from `*brustz` → `*breustą`" and then verifies `breustąbrēost ✓` in the binary [DEV_NOTES:line-5984-5999]. The verification remains useful because it records the regular comparator that the present row still depends on: `*breustą` does in fact produce `brēost`. But the row-policy wording is superseded. The live TSV does **not** collapse the row to one proto form; it keeps comparative `PROTO = *brústz` while using `PROTOFORM = *bréustą` for the OE-facing derivation.

The April 2026 correction note is also now project chronology rather than current row policy. It was written against an intermediate TSV state where `PROTOFORM` and `PROTO` had been accidentally reversed, so it argued that the row should make `PROTOFORM = *breustą` in order to match a then-current `PROTO = *breustą` [DEV_NOTES:line-15917-15990]. That note is still valuable because it preserves the sharpest statement of the false-problem diagnosis: `*brustz -> burst` is a bad-input mismatch, not evidence that OE breaking failed. Its source quotations from Kroonen and Ringe-Taylor remain compatible with the live row [@Kroonen2013, p. 76; @RingeTaylor2014, p. 174]. What is superseded is only the row-edit conclusion that both columns should converge on `*breustą`. The current project decision is narrower and more explicit: keep `*brústz` as the cognate-set headword, keep `*bréustą` as the OE derivational input, and treat `early_analogy` as an upstream formation choice rather than a late paradigm-cell repair.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1715-1717

- Source heading: `A-Restoration Fix (2026-02-06)`
- Source line or section hint: `lines 1715-1717`
- Fragment type: `diagnostic_trace`
- Status: `diagnostic_only`
- Issue tags: `breaking`; `wrong_input`; `debug_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This short trace is worth preserving because it records the first project-level misdiagnosis in the clearest possible form. It says that `*brustz` for 'breast' shows "no u-breaking," giving `brust` where `brēost` was expected. For row 1968 that is no longer a live phonological claim. The fragment now functions as diagnostic history showing how the project initially mistook a protoform-selection problem for a rule-firing problem. Later notes supersede the implied analysis by showing that OE `brēost` belongs with `*breusta-/*breustą`, not with root-noun `*brust-`.

### DEV_NOTES:line-5924-5983

- Source heading: `OE brēost 'breast': *breustą not *brustz (2026-03-10)`
- Source line or section hint: `lines 5924-5983`
- Fragment type: `source_synthesis`
- Status: `current`
- Issue tags: `proto_vs_protoform`; `reconstruction_disagreement`; `breaking`; `literature_survey`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current fragment for the scholarly argument behind the row. It begins from the concrete mismatch `*brustz -> burst` versus target `brēost`, but the body of the note shows that the real issue is lexical reconstruction, not missing OE breaking. Kroonen's two-formation split is preserved with direct quotations: root-noun `*brust-` covers Gothic and continental `brust`-type forms, while thematic `*breusta-` explicitly includes OE `bréost` [@Kroonen2013, pp. 76-77]. Orel reproduces essentially the same division by listing `*breustan` for the OE/ON/OFri/OS set and `*brustz` separately without an OE reflex [@Orel2003, pp. 57-58]. Ringe-Taylor then supply the exact NWGmc comparator needed for the row, and Campbell confirms that `brēost` exemplifies the regular OE `*eu > ēo` outcome [@RingeTaylor2014, p. 160; @Campbell1959, §115].

The dialect table at the end of this fragment remains especially useful replacement-note material because it spells out the contrast later writers might otherwise flatten: `*brust-` lines up with Gothic and continental `brust` forms, whereas `*breusta-` lines up with ON `brjóst`, OE `brēost`, OFri. `briast`, and OS `briost`. The fragment's conclusion that OE does not attest the root-noun `*brust-` is fully compatible with the live row so long as the row's `PROTO` is read as a cognate-set headword rather than as the direct OE input.

### DEV_NOTES:line-5984-5999

- Source heading: `OE brēost 'breast': *breustą not *brustz (2026-03-10)` / `The fix` and `Verification`
- Source line or section hint: `lines 5984-5999`
- Fragment type: `project_history`
- Status: `superseded`
- Issue tags: `row_edit_history`; `proto_vs_protoform`; `verification_probe`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment preserves an important but superseded project decision. It records the March move "Changed OE PROTO from `*brustz` → `*breustą`" and the accompanying binary check `breustąbrēost ✓`. The second half still matters, because it verifies the row's regular OE-facing comparator and shows that `*breustą` is the correct input if the target is `brēost`. The first half is no longer current row policy, because the live TSV later restored a `PROTO` / `PROTOFORM` split instead of keeping both columns aligned on `*breustą`. Use this fragment to document chronology and to cite the successful probe, not to restate current metadata.

### DEV_NOTES:line-15917-15990

- Source heading: `OE brēost 'breast': TSV PROTOFORM Correction (2026-04-09)`
- Source line or section hint: `lines 15917-15990`
- Fragment type: `superseded_analysis`
- Status: `superseded`
- Issue tags: `proto_vs_protoform`; `row_edit_history`; `false_rule_alarm`; `project_chronology`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This April note was written after the row had drifted into a different inconsistent state: `PROTOFORM` had reverted to `*brustz` while `PROTO` carried `*breustą`. The note is still valuable because it states the false-problem diagnosis with maximal clarity. It tests both inputs, shows `brustz    burst` versus `breustą   brēost`, and explicitly concludes that the FST is correct and the mismatch is in the row data, not in the OE sound laws. Its direct Kroonen quotation on `*breusta-` and its contrast with `*brust-` remain useful background [@Kroonen2013, p. 76], as does its Ringe-Taylor quotation for NWGmc `*breusta` [@RingeTaylor2014, p. 174].

What is superseded is the exact repair it recommends. The note wanted `PROTOFORM = *breustą` so that the row would match a then-current `PROTO = *breustą`. The live row has since settled on a better-articulated arrangement: `PROTO = *brústz` as cognate-set headword, `PROTOFORM = *bréustą` as OE derivational input, and `brēost` as the attested outcome. This fragment should therefore be used when explaining the row's cleanup history, not when stating the current column values.

## Superseded or diagnostic material

The main danger for later report work is collapsing two different superseded stages into one. The February trace is a stale phonology alarm: it acts as though `*brustz` should have broken to `brēost`. The March and April notes are more sophisticated, because they correctly identify `*breusta-/*breustą` as the OE-relevant formation, but both of them also temporarily overcorrect the row metadata by trying to make the comparative and derivational columns identical. The current row keeps the scholarly insight while rejecting that collapse.

## Open questions for later work

- If the final lexeme report discusses the row-level split, state explicitly that comparative `PROTO *brústz` and derivational `PROTOFORM *bréustą` are both intentional.
- If the final report quotes handbook evidence, prefer the March note's preserved Kroonen quotation for `*breusta-` and contrast it directly with the root-noun `*brust-` quotation.
- If later writers mention `burst` or `brust`, label them as regular comparators for the superseded wrong-input path, not as attested OE alternatives to `brēost`.

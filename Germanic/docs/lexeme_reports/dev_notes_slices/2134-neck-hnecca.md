---
row_id: 2134
concept: neck
counterpart: hnecca
proto: *xnákkaz
protoform: *xnékkô
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2134 neck / hnecca

## Current row state

- CONCEPT: `neck` [Germanic/data/germanic-aligned-final.tsv:792].
- COUNTERPART: `hnecca` [Germanic/data/germanic-aligned-final.tsv:792].
- PROTO: `*xnákkaz` [Germanic/data/germanic-aligned-final.tsv:792].
- PROTOFORM: `*xnékkô` [Germanic/data/germanic-aligned-final.tsv:792].
- DERIVATION_CLASS: `early_analogy` [Germanic/data/germanic-aligned-final.tsv:792].
- Live TSV history note (quoted closely): `Proto corrected: weak masc. n-stem with e-grade nom.sg. *xnekkô (Kroonen 2013, PIE *knékō). Kroonen reconstructs root ablaut: nom.sg. *hnekkô (e-grade), gen.sg. *hnukkaz (zero-grade), acc.pl. *hnakkunz (a-grade). OE/OFris/MNdl generalized e-grade; ON/OHG generalized a-grade (Kluge/Seebold s.v. Nacken). TSV had *xnakkăz (wrong class + wrong grade). German row retains a-grade *xnakkăz.` [Germanic/data/germanic-aligned-final.tsv:792].
- Packet state: the compact derivation already shows the live OE-facing modelling input `*xnékkô -> hnecca`, so this row is no longer a live derivational failure even though its comparative `PROTO` metadata still differs from its OE input [Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:17-41].
- `oe_known_problems.tsv`: no row-local entry for `2134`, `hnecca`, or `*xnékkô`; that absence matches the packet's solved-state trace and should not be misread as philological evidence one way or the other [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:43-45].
- Manifest / memo state: the packet records `_No manifest entry._`, while the research memo explicitly warns that current live row policy must keep three levels separate — comparative `PROTO`, OE derivational `PROTOFORM`, and attested OE target [Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:11-13; Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:8-12].
- OE attestation is secure. Clark Hall gives `hnecca m. 'neck'`, and Bosworth-Toller adds glosses `occipitium`, `occiput`, and `cervix, posteriora colli`, so the row target is an attested lexeme, not a project-only reconstruction [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22663-22663; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:89387-89388].

## Development-note summary

Securely attachable current row-specific DEV_NOTES authority **does** survive for row 2134. The controlling note is the dedicated section `Case 2: *xnakkăz → *xnekkô (OE hnecca 'neck, nape')`, which states plainly that the old row input was wrong in two distinct ways: the class was wrong because OE `hnecca` is weak masculine, and the root-vowel grade was wrong because the attested OE form has `e`, not the `a` expected from inherited `*xnakk-` [Germanic/docs/DEV_NOTES.md:3715-3733]. That remains the core row-specific authority for why the OE derivation cannot be rescued by adding another OE sound rule to `*xnakkăz`; the input itself had to change [Germanic/docs/DEV_NOTES.md:3723-3733; Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:77-88].

The note is strongest where it separates **PROTO**, **PROTOFORM**, and **OE target** instead of flattening them. In the live row, `PROTO = *xnákkaz` still functions as the cognate-set comparative label inherited by the table, but the current OE derivation is driven by `PROTOFORM = *xnékkô`, and the target represented by the row is the attested citation form `hnecca` [Germanic/data/germanic-aligned-final.tsv:792; Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:57-68]. DEV_NOTES and the local references agree that the e-grade weak-noun form is the right OE-facing choice: Kroonen's n-stem survey explicitly gives `*hnekkō, *hnukkaz 'neck'`, lists OE `hnecca` among the e-grade descendants, and reconstructs the paradigm `*hnekkō, gsg. *hnukkaz, apl. *hnakkuns` [Germanic/docs/DEV_NOTES.md:3734-3751; docs/references/kroonen_2011_n_stems.vision.txt:7601-7609, 7631-7657]. Kluge/Seebold independently confirms that `ae. hnecca` stands `im Ablaut` beside `Nacken` [Germanic/docs/DEV_NOTES.md:3755-3760; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:65059-65065, 36064-36068].

The computational point that survives as current authority is equally explicit. DEV_NOTES compares three inputs and records the outcomes `*xnakkăz -> hnæcc`, `*xnakkô -> hnacca`, and `*xnekkô -> hnecca`, then states that the e-grade form is not an ad hoc repair but “the **actual PGmc nominative singular** as reconstructed by Kroonen” [Germanic/docs/DEV_NOTES.md:3770-3780]. The packet's live compact trace agrees with that present-state conclusion by already showing `*xnékkô -> hnecca` as the working derivation [Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:17-41]. For the slice, that is the usable present-tense rule: the row is solved at the level of OE derivation once the OE-facing input is the e-grade weak noun.

One DEV_NOTES sentence must now be kept only as labelled project history. The section's `Correction applied` line says that the OE row changed to `*xnekkô` “both PROTOFORM and PROTO columns” [Germanic/docs/DEV_NOTES.md:3782-3785]. That is no longer the live row state: current TSV keeps `PROTO = *xnákkaz` and only uses `PROTOFORM = *xnékkô` as the OE modelling input [Germanic/data/germanic-aligned-final.tsv:792; Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:23-28, 57-64]. The sentence therefore remains valuable only as chronology showing an earlier cleanup stage, not as current row authority.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3715-3733

- Source heading: `Case 2: *xnakkăz → *xnekkô (OE hnecca 'neck, nape')`
- Source line or section hint: `lines 3715-3733`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `stem_class_correction`; `ablaut_grade`; `wrong_input`; `oe_target_attested`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This opening block is the row's main still-current problem statement. DEV_NOTES says the old TSV form `*xnakkăz` was wrong in **declension class** and in **root-vowel grade**: OE `hnecca` is weak masculine (`BT: "HNECCA, an; m."`), and no regular OE sound change will turn inherited `*xnakk-` into OE `hnecc-` with `e` in this environment [Germanic/docs/DEV_NOTES.md:3723-3733]. That remains the correct starting point for any later report prose because it prevents two common distortions at once: treating `hnecca` as if it were a strong a-stem continuation, and treating the OE `e` as if it could be generated by a new late OE sound rule rather than by choosing the right inherited grade [Germanic/docs/DEV_NOTES.md:3725-3733; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22663-22663; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:89387-89388].

### DEV_NOTES:line-3734-3768

- Source heading: `Root vowel ablaut: Kroonen's paradigm`
- Source line or section hint: `lines 3734-3768`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `ablaut_paradigm`; `e_grade_branch`; `bibliography`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest row-local philological fragment and should be carried forward densely rather than compressed. DEV_NOTES reconstructs an ablauting paradigm with `nom.sg. *hnekkô`, `gen.sg. *hnukkaz`, and `acc.pl. *hnakkunz`, then states that the daughter languages generalized different grades: OE, OFris, and Middle Dutch belong to the **e-grade** side, while ON and OHG belong to the **a-grade** side [Germanic/docs/DEV_NOTES.md:3734-3751]. The repo-local Kroonen extract independently supports exactly that picture, giving `*hnekkō, *hnukkaz 'neck'`, listing OE `hnecca` among the e-grade descendants, and explicitly reconstructing the parallel paradigm `*hnekkō, gsg. *hnukkaz, apl. *hnakkuns` [docs/references/kroonen_2011_n_stems.vision.txt:7601-7609, 7631-7657]. Kluge/Seebold then supplies the quotation worth preserving verbatim: `Daneben mit Ablaut ... ae. hnecca`, and the separate `Genick` entry says `Dieses steht im Ablaut zu Nacken` [Germanic/docs/DEV_NOTES.md:3755-3760; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:65061-65065, 36066-36067].

This same fragment also explains why Orel must be used cautiously for this row. DEV_NOTES notes that Orel lists ON, MLG, and OHG material but omits OE `hnecca` and does not discuss the ablaut [Germanic/docs/DEV_NOTES.md:3762-3764]. The repo-local Orel extract confirms that limitation: it gives `*xnakkaz *xnakkōn sb.m.` with ON/MLG/OHG evidence only [docs/references/orel_handbook_germanic_etymology.vision.txt:20861-20866]. For row 2134, Orel is therefore background corroboration for the family, not the controlling OE authority.

### DEV_NOTES:line-3770-3780

- Source heading: `Pipeline verification`
- Source line or section hint: `lines 3770-3780`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `pipeline_verification`; `e_grade_input`; `comparative_testing`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the cleanest current engineering summary for the row. DEV_NOTES compares three candidate inputs and records a decisive contrast: `*xnakkăz -> hnæcc` is wrong in class and vowel, `*xnakkô -> hnacca` fixes the class but still gives the wrong root vowel, and only `*xnekkô -> hnecca` matches the target [Germanic/docs/DEV_NOTES.md:3772-3776]. DEV_NOTES then adds the critical interpretive sentence: “The e-grade form `*xnekkô` is not a `transponent` or ad hoc workaround. It is the **actual PGmc nominative singular** as reconstructed by Kroonen” [Germanic/docs/DEV_NOTES.md:3778-3780]. The live packet trace now reflects that same conclusion operationally by already deriving `hnecca` from `*xnékkô` [Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:17-41].

### DEV_NOTES:line-3787-3797

- Source heading: `Methodological note`
- Source line or section hint: `lines 3787-3797`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `ablaut_selection`; `methodology`; `cognate_table_limit`; `protoform_vs_proto`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This methodological tail is not unique to `hnecca`, but it belongs with the row because it explains why this sort of mismatch recurs in the project. DEV_NOTES warns that etymological dictionaries often cite a single shared proto-form even when daughter branches continue different ablaut grades, so a cognate-table import can silently supply the wrong grade for a given daughter language; in such cases, the mismatch “is not fixable by adding sound rules — it requires correcting the input form to the grade actually continued in that branch” [Germanic/docs/DEV_NOTES.md:3789-3797]. For row 2134 that principle is not abstract: the live row still visibly separates comparative `PROTO = *xnákkaz` from OE-facing `PROTOFORM = *xnékkô`, and the research memo treats exactly that split as the central distinction to preserve [Germanic/data/germanic-aligned-final.tsv:792; Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:8-12, 57-68].

### DEV_NOTES:line-3782-3785

- Source heading: `Correction applied`
- Source line or section hint: `lines 3782-3785`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `stale_row_state`; `protoform_vs_proto`; `project_history`; `metadata_drift`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This short fragment must remain visible only as explicitly superseded project history. DEV_NOTES says the OE row changed from `*xnakkăz` to `*xnekkô` in “both `PROTOFORM` and `PROTO` columns,” with German keeping the a-grade form [Germanic/docs/DEV_NOTES.md:3782-3785]. That sentence no longer describes the live row, which now keeps `PROTO = *xnákkaz` while using `PROTOFORM = *xnékkô` for the OE derivation [Germanic/data/germanic-aligned-final.tsv:792]. The fragment is still worth preserving because it documents an intermediate cleanup stage, but later extraction must not cite it as if it were current row metadata [Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:23-28, 87-88].

## Superseded or diagnostic material

The main superseded material for this row is **not** the ablaut solution itself; that part remains current and well supported. What has aged is the earlier DEV_NOTES wording about how fully the row metadata had already been harmonized. The dedicated section correctly solved the OE derivation by moving the row to e-grade weak-noun `*xnekkô`, but its sentence about both `PROTO` and `PROTOFORM` changing no longer matches the live TSV, so that sentence must stay demoted to project chronology only [Germanic/docs/DEV_NOTES.md:3778-3785; Germanic/data/germanic-aligned-final.tsv:792].

Two other materials need careful framing. First, old `*xnakkăz` / `*xnakkô` comparisons remain useful as diagnostics for why the row once failed, but they are comparator inputs, not surviving row authority now that the packet already shows a solved `*xnékkô -> hnecca` derivation [Germanic/docs/DEV_NOTES.md:3772-3776; Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:17-41]. Second, the packet's Swadesh hit `neck -> swēora` is concept-level lexical competition, not evidence against `hnecca`; it should be kept only as a reminder that concept lists and lexeme rows are not interchangeable [Germanic/docs/lexeme_reports/packets/2134-neck-hnecca.md:153-158].

## Open questions for later work

- Decide whether live TSV `PROTO = *xnákkaz` should eventually be replaced by a weak-noun comparative headword that better matches the row's current philological framing; the present local evidence is strong for OE-facing `PROTOFORM = *xnékkô`, but less happy with a bare strong a-stem as the lexeme-level header [Germanic/data/germanic-aligned-final.tsv:792; docs/references/kroonen_2011_n_stems.vision.txt:7601-7609, 7649-7657; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:65059-65065].
- If a final lexeme report is written later, keep the three-way distinction explicit every time: comparative `PROTO`, derivational `PROTOFORM`, and attested OE target are doing different jobs in this row and should not be silently collapsed [Germanic/data/germanic-aligned-final.tsv:792; Germanic/docs/lexeme_reports/research_memos/2134-neck-hnecca.md:8-12, 57-68].
- If `index.tsv` is updated later, index the stale `Correction applied` sentence separately as superseded metadata, so later extraction can keep the ablaut solution while avoiding the outdated claim that the live row already changed both columns [Germanic/docs/DEV_NOTES.md:3782-3785; Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv:1-1].
- No literature agent is presently required for basic row reporting, but a later cleanup pass could still add the exact Kroonen 2013 dictionary entry behind the DEV_NOTES summary so the row's e-grade citation is backed by both the n-stem study extract and the lexicon entry itself [Germanic/docs/DEV_NOTES.md:3736-3737; docs/references/kroonen_2011_n_stems.vision.txt:7653-7657].

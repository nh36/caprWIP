---
row_id: 2124
concept: meed
counterpart: meorde
proto: *mizdō
protoform: *mízdai
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2124-meed-meorde.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/meord_med_chronological_review.md;Germanic/docs/analysis/mismatch_dossier_mizdo.md;Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md;Germanic/docs/analysis/compound_archaism_inventory.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2124 meed / meorde

## Current row state

- CONCEPT: `meed`; COUNTERPART: `meorde`; PROTO: `*mizdō`; PROTOFORM: `*mízdai`; DERIVATION_CLASS: `late_analogy` [Germanic/data/germanic-aligned-final.tsv:752].
- The live TSV note already encodes the row as a **paradigm-cell switch to the dat.sg.**: `*mízdai > meorde`, with `meorde` identified as the directly attested OE oblique and `*mēd` treated as the competing doublet member; the same note explicitly points readers to `DEV_NOTES` §17.24.11 and to the chronological review file for the broader literature problem [Germanic/data/germanic-aligned-final.tsv:752].
- The packet agrees with the live row state: its compact derivation trace gives `PROTO: *mízdai`, `EXPECTED: meorde`, `OUTPUTS: meorde`, and its stage summary runs `*mízdai > *mírdai > *mérdē > *méordē > *méorde > meorde` [Germanic/docs/lexeme_reports/packets/2124-meed-meorde.md:17-42].
- `oe_known_problems.tsv` has no live entry for row `2124`, `*mizdō`, or `meorde`; that is only current bookkeeping, but it confirms that the row is no longer being carried as an unresolved mismatch ticket [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/packets/2124-meed-meorde.md:45-47].
- The research memo's controlling distinction is three-way and should be preserved here: `PROTO = *mizdō` is the cognate-set etymological headword, `PROTOFORM = *mízdai` is the selected PGmc **dat.sg. paradigm cell**, and OE `meorde` is the selected **attested oblique target**, not the citation lemma for the lexeme as a whole [Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:40-48].
- The same memo also keeps the current caution explicit: the row-level solution is narrower than the full philological problem. `meorde/meorda` are directly attested, bare nominative `meord` is lexicographers' reconstruction from those obliques, and the deeper analysis of competing `mēd` remains literature-divided rather than settled by the project [Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:31-38,50-67,83-95].

## Development-note summary

The securely current DEV_NOTES authority for row `2124` is real but narrow. `DEV_NOTES` now securely supports four points: (1) the older claim that OE `meord`/`meorde` lacked real attestation was wrong; (2) no `*meord-` compounds such as `*meord-gifa` are evidenced; (3) the directly attested OE forms for this lexeme are obliques such as `meorde` and `meorda`, while bare nominative `meord` is a reconstructed lemma; and (4) the current FST already derives `*mizdai -> meorde` without any rule change [Germanic/docs/DEV_NOTES.md:36072-36123,36332-36405,36415-36470].

That means the row's current project logic must keep **PROTO, PROTOFORM, and OE target strictly distinct**. `*mizdō` remains the lexeme-level Proto-Germanic reconstruction for the cognate set; `*mízdai` is not a rival lexeme proto but the row's selected **dat.sg. input cell**; and `meorde` is not the ordinary dictionary headword but the row's selected **attested OE oblique output** [Germanic/data/germanic-aligned-final.tsv:752; Germanic/docs/DEV_NOTES.md:36380-36405,36424-36429,36454-36470; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:40-48,58-67].

What does **not** survive as securely current row-specific DEV_NOTES authority is any final project verdict on the historical origin of the WS doublet `mēd`. `DEV_NOTES` preserves multiple analyses: `§17.24.8` frames a regular `meord` pathway versus a `mēd` pathway with z-loss + compensatory lengthening; `§17.24.10` records Orel/Hirt's PGmc-level doublet as a substantive alternative; and the chronological review concludes that the literature remains divided, with Kilday 2024 offering a serious but still draft-only loan analysis. The row's current solution was adopted precisely because it avoids forcing the project to choose among those larger theories [Germanic/docs/DEV_NOTES.md:36192-36216,36407-36413; Germanic/docs/analysis/meord_med_chronological_review.md:260-278,280-355,378-409,485-520,831-904].

Accordingly, this slice should be read as a **replacement working note for a row-specific targeting decision**, not as proof that the `mēd` problem is solved. The surviving current authority says: the row may safely target attested `meorde` from dat.sg. `*mízdai`; the lexicographic lemma `meord` remains reconstructed from oblique evidence; `mēd` remains the better-known competing OE doublet; and earlier project strands that denied attestation or invoked `*meord-gifa` are project history only and must not be recycled as current evidence [Germanic/docs/DEV_NOTES.md:36072-36123,36338-36405,36433-36470; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:31-38,50-56,58-67,83-95].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-36072-36157

- Source heading: `§17.24.7 Correction: meord IS attested, but no *meord-gifa exists`
- Source line or section hint: `lines 36072-36157`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `compound_confabulation`; `doublet`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `none`

This is the correction fragment that must anchor any current row-specific note. DEV_NOTES now states flatly that `meord 'reward' IS attested` and backs that claim with three repo-local witnesses: BT Supplement, Bright's *Anglo-Saxon Reader*, and Hall's *Concise* [Germanic/docs/DEV_NOTES.md:36091-36117]. It quotes the key forms directly: in BT Supplement, `The Bede gloss has meorde (dative singular)`; in Bright, the reading text contains `mærða tilgaþ þæs him meorde wile`, and the glossary glosses `meorde (dial.) 181, meord, see med.`; Hall likewise gives `meard=(1) meord, méd` [Germanic/docs/DEV_NOTES.md:36096-36112].

The same fragment is equally important for what it excludes. After correcting the attestation question, DEV_NOTES says `No *meord-* compound exists` and notes that searches across BT, BT Supplement, Hall, Bright, and other local references found no `*meord-gifa`, `*meord-sceatt`, or any other `meord-` compound; the first dossier's `*meord-gifa` is therefore confirmed confabulation [Germanic/docs/DEV_NOTES.md:36119-36123]. For the current slice, that means simplex `meorde/meord` evidence is securely usable, while compound-based project history must be kept fenced off as superseded [Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:31-36,50-56].

### DEV_NOTES:line-36160-36216

- Source heading: `§17.24.8 The dialect / smoothing question: why *meord* (with diphthong) is the Anglian-attested form`
- Source line or section hint: `lines 36160-36216`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `dialect_distribution`; `smoothing`; `breaking`; `z_loss`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `none`

This fragment is still useful, but as **background framing rather than row policy**. Its central corrective claim is that the `meord ~ mēd` split is **not** a smoothing problem: Anglian smoothing applies only in velar environments, whereas the diphthong in `meord` stands before `-rd-`, outside the smoothing rule [Germanic/docs/DEV_NOTES.md:36162-36190]. DEV_NOTES therefore separates two pathways instead: `Pathway A (rhotacism + breaking): *mizdō → *mird- → *meord-` and `Pathway B (sporadic z-loss + comp. lengthening + lowering): *mizdō → *mīd- → *mēd-` [Germanic/docs/DEV_NOTES.md:36192-36201].

For row `2124`, the value of this fragment is defensive. It explains why the current target `meorde` can be Anglian-leaning without forcing a claim that `mēd` is simply the WS smoothing reflex of the same form; DEV_NOTES expressly says the doublet's distribution is `rather patchy`, and the row-level targeting decision should not be rewritten into an oversimplified Anglian-vs.-WS rule [Germanic/docs/DEV_NOTES.md:36203-36216; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:52-55].

### DEV_NOTES:line-36332-36414

- Source heading: `§17.24.10 Attestation verification: meord vs. meorde — what the primary texts actually contain`
- Source line or section hint: `lines 36332-36414`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `lemma_vs_oblique`; `protoform_policy`; `paradigm_cell`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `none`

This is the clearest current DEV_NOTES statement of the philological hierarchy the row now depends on. DEV_NOTES says explicitly that `The form meord (bare nom.sg.) does not appear in any primary OE text identified in the in-repo references` and that `The directly attested OE forms are oblique cases`, then tabulates `meorde` dat.sg. from Bede 4.17 and *Phoenix* 17 plus `meorde` and `meorda` variants from Gregory's *Dialogues* [Germanic/docs/DEV_NOTES.md:36338-36352]. It also preserves the OCR warning that `meotée` and `meotda` in BT Supplement are best read as `meorde` and `meorda` because the OCR regularly misreads `rd` in that column [Germanic/docs/DEV_NOTES.md:36349-36352].

The same fragment then makes the lemma-status issue explicit. DEV_NOTES says `Lexicographers and handbooks reconstruct nom.sg. meord uniformly as a strong f. ō-stem, on the basis of these oblique forms`, and it lists BT Supplement, Hall, Bright, Campbell, Kroonen, and Orel as witnesses to that reconstructed lemma tradition [Germanic/docs/DEV_NOTES.md:36354-36379]. The row consequence follows immediately: if the row is understood as an FST target, the input should ideally be a paradigm cell whose OE reflex is directly attested; DEV_NOTES therefore says the note should record that `the attested oblique evidence anchors the form`, and it points toward a paradigm-cell targeting solution rather than a bare-lemma assertion [Germanic/docs/DEV_NOTES.md:36380-36405]. This is the fragment that most clearly authorizes the present distinction `PROTO *mizdō` vs. `PROTOFORM *mízdai` vs. OE target `meorde` [Germanic/data/germanic-aligned-final.tsv:752; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:40-48].

### DEV_NOTES:line-36415-36470

- Source heading: `§17.24.11 FST probe: *mizdai → meorde is lautgesetzlich`
- Source line or section hint: `lines 36415-36470`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `fst_probe`; `paradigm_cell`; `attested_target`; `protoform_vs_proto`
- Recommended next use: `use_for_paradigm_probe`
- Shared with row IDs: `none`

This is the operative row-local implementation fragment. DEV_NOTES says that, because the directly attested form is `meorde` rather than bare `meord`, the compiled cascade was probed against multiple paradigm cells, and the decisive result is `mizdai -> meorde` [Germanic/docs/DEV_NOTES.md:36417-36429]. The probe table also records `mizdō -> meord`, `mizdōz -> meorde`, `mizdōn -> meorde`, and rejected plural-style inputs such as `mizdǭ` or `mizdōnz` [Germanic/docs/DEV_NOTES.md:36424-36431].

DEV_NOTES then gives the project-level verdict in the strongest current form available: `The FST already produces the actually-attested meorde lautgesetzlich from PGmc dat.sg. *mizdai ... No FST change is required` [Germanic/docs/DEV_NOTES.md:36433-36437]. Its implications section is precisely the row policy now visible in the TSV: the old mismatch arose because the row had `PROTOFORM = *mizdō` and target `*mēd`; the `cleanest paradigm-cell-targeting fix` is to switch to `PROTOFORM = *mizdai` and target `meorde`; and this switch is `lowest-disturbance` because it uses the existing FST without taking a final position on the historical analysis of `mēd` [Germanic/docs/DEV_NOTES.md:36454-36470; Germanic/data/germanic-aligned-final.tsv:752; Germanic/docs/analysis/meord_med_chronological_review.md:833-904].

### DEV_NOTES:line-35960-36069

- Source heading: `§17.24.3–§17.24.6 early unattestation / circular-citation / open-question cluster`
- Source line or section hint: `lines 35960-36069`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `unattested_claim_withdrawn`; `circular_citation_withdrawn`; `project_history`; `source_conflict`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `none`

This earlier cluster must remain visible only as **superseded project history**. It preserved two now-withdrawn claims: first, that `meord reward is a handbook entry without surviving primary attestation`, and second, that the main story was a `circular-citation hazard` produced by dictionary recycling rather than real textual evidence [Germanic/docs/DEV_NOTES.md:35960-35965,35975-35980,36020-36027]. `§17.24.7` explicitly overturns that picture by documenting real `meorde` attestations and withdrawing the circular-citation framing as the main explanation [Germanic/docs/DEV_NOTES.md:36072-36135].

The historical value of this superseded fragment is still real: it records how the confabulated `*meord-gifa` claim entered project documents and why older dossier files became contaminated [Germanic/docs/DEV_NOTES.md:35967-35974]. But its operative recommendations — retracting the whole `meord` case or treating attestation as missing pending user direction — are no longer current row authority and should not be used to reopen the live row state [Germanic/docs/DEV_NOTES.md:36045-36069; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:14-17,31-36].

## Superseded or diagnostic material

- The pre-correction DEV_NOTES statement that `meord 'reward'` lacked surviving primary attestation is no longer usable except as a witness to the project's abandoned analysis path; `§17.24.7` explicitly replaces it with direct Bede/Bright/Hall-based attestation checking [Germanic/docs/DEV_NOTES.md:35960-35965,35975-35980,36072-36117].
- The `circular citation hazard` framing is likewise withdrawn as the main lexeme analysis. It remains useful only to explain how bad claims propagated through earlier dossiers; it is not current evidence against `meorde/meord` themselves [Germanic/docs/DEV_NOTES.md:36020-36027,36126-36135].
- `*meord-gifa` and related compound claims are diagnostic contamination only. Current authority is the opposite: simplex `meorde/meord` is evidentially real, but `meord-` compounds are not [Germanic/docs/DEV_NOTES.md:36119-36123; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:35-36,55-56].
- The older row state in which `*mizdō` targeted OE `*mēd` should be retained only as history explaining why the mismatch existed. The live row no longer asks the FST to prove the whole `mēd` theory; it asks for the attested oblique `meorde` from `*mízdai`, which the current cascade already delivers [Germanic/data/germanic-aligned-final.tsv:752; Germanic/docs/DEV_NOTES.md:36454-36470].
- Even within current materials, the strongest caution is that Kilday's loan account should not be cited as if it were settled consensus. The review treats it as serious and economical but still draft-only; future prose should keep it as one live hypothesis among several, not as final closure [Germanic/docs/analysis/meord_med_chronological_review.md:839-898; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:48-49,54,93].

## Open questions for later work

- The row-level targeting issue is solved more securely than the lexeme-level `mēd` problem. If future work revisits the note field, it should keep the current narrow claim — `*mízdai -> meorde` is secure — while stating more cautiously that the historical analysis of competing `mēd` remains disputed among Crist/Kroonen/Ringe-Taylor, Orel/Hirt, and Kilday [Germanic/data/germanic-aligned-final.tsv:752; Germanic/docs/analysis/meord_med_chronological_review.md:839-898].
- A formal paradigm probe is still worth standardizing for this row. `§17.24.11` already probed nominative, dative, genitive, and accusative-style inputs, but it also notes that the plural-style inputs needed for attested `meorda` are not yet handled cleanly by the cascade [Germanic/docs/DEV_NOTES.md:36424-36431,36447-36452; Germanic/docs/lexeme_reports/research_memos/2124-meed-meorde.md:69-81].
- If the project later wants a separate row for the widespread WS headword side of the doublet, that row should be framed separately rather than forcing row `2124` to carry both `meorde` and `mēd` at once; the chronological review explicitly recommends treating `mēd` as a possible future separate lexical-doublet item [Germanic/docs/analysis/meord_med_chronological_review.md:900-904].

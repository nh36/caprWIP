---
row_id: 2240
concept: tap
counterpart: tæppa
proto: *táppô
protoform: *táppô
derivation_class: known_unmodelled
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2240-tap-tæppa.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2240-tap-tæppa.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2240 tap / tæppa

## Current row state

- CONCEPT: `tap`
- COUNTERPART: `tæppa`
- PROTO: `*táppô`
- PROTOFORM: `*táppô`
- DERIVATION_CLASS: `known_unmodelled`
- Live TSV note (quoted closely): `N-stem masc. nom.sg.; attested OE tæppa (Orel s.v. *tappòn; Kroonen n-stems §1381). The æ is analogical — no cell of the nominal paradigm yields lautgesetzlich tæpp- ... the Class I weak j-verb pathway yields teppan via i-umlaut (not tæppan) ... FST's lautgesetzlich output is tappa by A-restoration; mismatch retained as a documented analogical case` [Germanic/data/germanic-aligned-final.tsv:1202].
- `oe_known_problems.tsv` has a matching current ledger entry: `status=exception`, `category=analogical_n_stem_levelling`, and the reason field repeats the same core diagnosis — regular `tappa`, analogical `tæppa`, no PGmc input yielding lautgesetzlich `tæpp-` [Germanic/data/oe_known_problems.tsv:8].
- Current DEV_NOTES authority status: securely attachable current material exists, but it is layered rather than concentrated in one neat lexeme section. The durable row policy is spread across (i) the source-backed rejection of oblique `*táppan -> tæppan`, (ii) the failed j-verb rescue and the revised analogical account, (iii) the later A-restoration verification that now returns `tappa`, and (iv) the closure note that triages the row to the known-problems ledger [DEV_NOTES:line-22569-22629,23080-23225,36676-36775,36938-36975].

## Development-note summary

This row now has a stable three-part interpretation and the slice should preserve the distinction explicitly. `PROTO = *táppô` is the cognate-set headword used for the noun cited by Orel and Kroonen; `PROTOFORM = *táppô` is also the row's active FST input; `COUNTERPART = tæppa` is the attested Old English noun citation form [@Orel2003, s.v. *tappòn; @Kroonen2013, §1381; Germanic/data/germanic-aligned-final.tsv:1202]. The row is **not** a case where the project keeps one proto for comparative bookkeeping but a different protoform for OE derivation. Here proto and protoform coincide; the mismatch lies between regular phonological output and attested OE surface form.

The philological anchor is the noun `tæppa`, not an oblique `tæppan` and not a verbal infinitive. DEV_NOTES records the noun headword from Orel and Kroonen, and the wider OE family also includes `tæppere` and `tæppestre`, which show that `tæpp-` is real in OE lexical usage [@Orel2003, s.v. *tappòn; @Kroonen2013, §1381; @ClarkHall1960, s.v. tæppa; DEV_NOTES:line-22946-22961]. What the sources do **not** provide is an inherited sound-law derivation for that fronted root vowel. DEV_NOTES is explicit that the handbooks attest the forms but do not themselves supply a lexeme-specific explanation of the analogy [DEV_NOTES:line-23090-23103].

The regular nominal derivation is now settled. After the later §17.25 A-restoration repairs, DEV_NOTES verifies `*táppô -> tappa`, not `tæppa` [DEV_NOTES:line-36757-36775]. This is the expected outcome for an n-stem masculine nominative singular with back `*-ô`: Anglo-Frisian Brightening can front the root at an intermediate stage, but A-restoration retracts it again before the back-vocalic tail, yielding `tappa`. DEV_NOTES explicitly aligns this with the ordinary restored n-stem type cited by Ringe and Taylor — `crabba`, `racca`, `maþa` [@RingeTaylor2014, vol. 2, p. 207; DEV_NOTES:line-36940-36952].

The row is kept as `known_unmodelled` because neither the nominal paradigm nor the j-stem pathway provides a regular way to `tæpp-`. The decisive correction to the older oblique rescue is already stated in DEV_NOTES with source quotations: Campbell says that restored `a` is common before geminates and specifically lists forms such as `crabba`, `hnappian`, `racca`, `lappa`, while noting that doublets with `æ` may also occur; DEV_NOTES therefore concludes that oblique `*táppan` should come out as `tappan`, not `tæppan` [@Campbell1959, §158; DEV_NOTES:line-22571-22629]. The earlier proposal that nominal oblique cells could yield `tæppan` is therefore superseded project history, not current analysis [DEV_NOTES:line-3220-3252].

The attempted j-verb rescue is also superseded, but it remains crucial history because it explains why the project finally stopped trying to regularize this row away. DEV_NOTES first proposed reinterpreting the row as Class I weak j-verb `*táppjaną -> tæppan`; then a probe showed that the actual regular output is `teppan`, since `*á` first fronts and then undergoes i-umlaut to `e` [DEV_NOTES:line-22996-23074,23153-23203]. The note preserves Fulk's formulation for the parallel verb `stæppan`: “The form stæppan (rather than the less common steppan) ... æ in the root is due to analogical substitution ...” [@Fulk2018, §12.19 n.6; DEV_NOTES:line-23171-23180]. DEV_NOTES then applies the same lesson to the *tap-* family: even the co-radical j-stems are regular only as `tepp-`, so any OE `tæpp-` in noun, agent noun, or verb is analogical [DEV_NOTES:line-23182-23203].

The current project explanation is therefore conservative and should stay that way. `tæppa` is retained because it is the attested noun actually wanted by the row; `*táppô` is retained because no better inherited PGmc input solves the problem; and `known_unmodelled` is retained because the mismatch is historically intelligible but not something the FST should be asked to generate [Germanic/data/germanic-aligned-final.tsv:1202; Germanic/data/oe_known_problems.tsv:8; DEV_NOTES:line-23204-23225,36954-36975]. DEV_NOTES does offer a plausible source for the analogy — leveling from co-radical j-stems and their derivatives — but it also flags that as an inference, not a directly quoted handbook statement for this exact lexeme [DEV_NOTES:line-23090-23103].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-22569-22629

- Source heading: `Case 1 — *táppan → tappan (expected tæppan)`
- Source line or section hint: `lines 22569-22629`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `oblique_n_stem`; `a_restoration`; `source_audit`; `analogical_target`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the most useful retained source audit for why the older oblique-noun repair fails. DEV_NOTES quotes Campbell §158 on restored `a` before geminates — including `crabba`, `hnappian`, `racca`, `lappa` — and notes his footnote that `æ`-doublets can exist as secondary forms [@Campbell1959, §158; DEV_NOTES:line-22573-22580]. DEV_NOTES then adds Brunner and R/T to the same effect and concludes that n-stem oblique `*-an-` is a normal A-restoration environment, so `*táppan` should yield `tappan` lautgesetzlich, while `tæppan` would already be analogical [DEV_NOTES:line-22581-22629]. For row 2240 this fragment remains current because it explains why the noun cannot be rescued by selecting an oblique paradigm cell.

### DEV_NOTES:line-23080-23103

- Source heading: `§17.10.16a — Clarifications added after review`
- Source line or section hint: `lines 23080-23103`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `analogy_source`; `nominal_paradigm`; `j_stem_family`; `inference_vs_source`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest current statement of the analogy argument. DEV_NOTES says explicitly that no cell of the noun's own n-stem paradigm yields lautgesetzlich `tæpp-`, and it also warns that Fulk's `stæppan` note is about a verb, not directly about a noun [DEV_NOTES:line-23082-23088]. It then gives the project's best explanation anyway: front-vocalic `tæpp-` was most plausibly levelled from co-radical j-stems such as `*tappjaną` and `*tappj-ārijaz`, where fronting is phonologically legitimate at least at an intermediate stage, before the whole family was analogically regularized in OE [DEV_NOTES:line-23090-23103]. This fragment should be preserved because it marks the analogy source as a reasoned inference, not as a falsely over-precise handbook claim.

### DEV_NOTES:line-23153-23225

- Source heading: `§17.10.16b — Probe result: the j-verb proposal does not work`; `§17.10.16c — Revised proposal: accept the mismatch as analogical`
- Source line or section hint: `lines 23153-23225`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `probe_result`; `j_verb_failure`; `known_unmodelled`; `target_selection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the decisive row-level turning point. DEV_NOTES records the actual probe result `*táppjaną -> teppan`, explains the phonology (`*á -> *æ -> *e` under i-umlaut), and then states the consequence plainly: the j-verb proposal was mistaken, and any attested `tæpp-` verbal material would itself be analogical [DEV_NOTES:line-23155-23203]. The immediately following revised proposal is the source of the live row policy: retarget to attested noun `tæppa`, restore `PROTOFORM / PROTO = *táppô`, and keep the mismatch as a documented analogical case rather than a phonology bug [DEV_NOTES:line-23204-23225].

### DEV_NOTES:line-36676-36775

- Source heading: `§17.25.7 Regression after first build — diagnosis and follow-up fix`; `§17.25.8 Post-fix verification`
- Source line or section hint: `lines 36676-36775`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `geminate_handling`; `trimoric_o`; `a_restoration`; `verification`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2090`

This shared implementation fragment matters because it is where the FST's regular output was revalidated after later rule surgery. DEV_NOTES diagnoses the temporary false match `*táppô -> tæppa` as an artefact of a broken geminate definition plus the omission of `*ô` from the strong restoration trigger set [DEV_NOTES:line-36676-36725]. It then records the post-fix probe `*táppô -> tappa` and labels that output “lautgesetzlich-correct,” making clear that the remaining problem is target-side analogical mismatch rather than missing phonology [DEV_NOTES:line-36757-36775].

### DEV_NOTES:line-36938-36975

- Source heading: `§17.27 Closure: *táppô triaged to known-problems ledger (analogical)`
- Source line or section hint: `lines 36938-36975`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `closure`; `ledger_triage`; `analogical_exception`; `known_problems`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the formal closure note for the row. DEV_NOTES restates the whole decision in compressed final form: `*táppô` gives regular `tappa`; a putative `*-i-` path gives `teppan`; no paradigm cell yields lautgesetzlich `tæpp-`; and the attested `æ` is analogical, plausibly levelled from co-radical j-stems with Fulk's `stæppan` as parallel [@RingeTaylor2014, vol. 2, p. 207; @Fulk2018, §12.19 n.6; DEV_NOTES:line-36940-36952]. It then records the operational consequence: the row is triaged to `oe_known_problems.tsv` as `exception / analogical_n_stem_levelling`, so it remains visible but no longer counts as actionable phonology work [DEV_NOTES:line-36954-36975].

### DEV_NOTES:line-3220-3252

- Source heading: `Case 2: *tappô → tappa (expected tæppa) — n-stem masculine`
- Source line or section hint: `lines 3220-3252`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `early_oblique_rescue`; `paradigm_misread`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This earlier fragment should be preserved only as labeled project history. It argued that oblique n-stem cells such as `*tappăn` could yield `tæppan` and proposed changing both proto and OE target accordingly [DEV_NOTES:line-3229-3252]. Later DEV_NOTES work explicitly reverses that claim with handbook support and probe-backed reasoning, so this fragment is no longer current authority for any part of row 2240 [DEV_NOTES:line-22571-22629,23153-23225].

### DEV_NOTES:line-22934-23074

- Source heading: `§17.10.16 — Case 1 resolution: *táppan → tæppan revisited`
- Source line or section hint: `lines 22934-23074`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `j_verb_reparse`; `attestation_chain`; `failed_rescue`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This section preserves the first late-stage attempt to regularize the row by reparsing it as a weak j-verb `*táppjaną -> tæppan`, supported by `tæppere` and `tæppestre` as deverbal family evidence [DEV_NOTES:line-22996-23074]. It is worth keeping because it records why the project looked in the j-stem family in the first place, but it is superseded by the later probe result `teppan`, which invalidates the hoped-for regular derivation [DEV_NOTES:line-23153-23203].

## Superseded or diagnostic material

- The oldest row-specific A-restoration note for `*tappô` is not safe to reuse without warning. Its useful part is only the basic contrast “regular `tappa`, attested `tæppa`”; its specific claim that oblique cells yield `tæppan` was later overturned by the Campbell/R/T source audit [DEV_NOTES:line-3220-3252,22571-22629].
- The first §17.10.16 j-verb proposal is also not safe to quote as current analysis. It correctly recognized that the derivational family matters, but it wrongly assumed the regular j-verb outcome would preserve `æ`; after probing, DEV_NOTES explicitly replaced that with `teppan` and treated all OE `tæpp-` material as analogical [DEV_NOTES:line-22996-23074,23153-23203].
- The temporary apparent match `*táppô -> tæppa` in the first post-§17.25 build is diagnostic only. DEV_NOTES later shows that this was caused by an implementation bug in geminate handling and restoration triggering, not by a true lexical solution [DEV_NOTES:line-36676-36725].
- The ledger line in `oe_known_problems.tsv` is current policy but not full argumentation. It should be cited together with the DEV_NOTES fragments above, not as if the one-line ledger reason by itself replaced the phonological and philological discussion [Germanic/data/oe_known_problems.tsv:8; DEV_NOTES:line-36938-36975].

## Open questions for later work

- If this row is ever indexed, keep the current/superseded split explicit: `*táppô -> tappa` and ledger triage are current; oblique `*tappăn -> tæppan` and j-verb `*táppjaną -> tæppan` are superseded project history.
- A later full report could still add a compact family table (`tæppa`, `tæppere`, `tæppestre`, expected `teppan`) to show exactly where analogical `æ` has spread, but the present evidence does not justify turning that inference into a new protoform or new derivation class.
- If future bibliography work turns up a handbook discussion that explicitly explains the analogical `æ` of noun `tæppa`, replace the present cautious wording (“most plausibly levelled from co-radical j-stems”) with that source-specific claim. For now DEV_NOTES is right to keep the explanation inferential rather than overstate the evidence.

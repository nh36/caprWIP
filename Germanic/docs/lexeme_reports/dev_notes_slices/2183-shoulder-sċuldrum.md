---
row_id: 2183
concept: shoulder
counterpart: sċuldrum
proto: *skuldrō
protoform: *skúldramiz
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2183-shoulder-sċuldrum.md
linked_dossier_or_analysis_files: Germanic/docs/dossier-shoulder-2026.md; Germanic/docs/dossier-shoulder-paradigm-survey-2026.md; Germanic/docs/dossier-shoulder-cellchoice-2026.md; Germanic/docs/dossier-shoulder-lautgesetz-2026.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2183 shoulder / sċuldrum

## Current row state

- The live OE TSV row now reads `2183 | shoulder | sċuldrum | *skuldrō | *skúldramiz | late_analogy`, with the explicit row note: `DatPl encoding: PROTOFORM is PGmc-proper *-amiz (inst.pl. branch of dat./inst. merger). See DEV_NOTES §17.41.` [Germanic/data/germanic-aligned-final.tsv:981-981].
- `coverage_audit.md` still lists row `2183` as a `late_analogy` row with a slice gap (`-` in the report columns), so this file is the replacement working dossier for a row that has live DEV_NOTES material but had not yet been integrated into the index/report layer [Germanic/docs/lexeme_reports/coverage_audit.md:131-131].
- `oe_known_problems.tsv` contains no shoulder-specific entry. That matters because the row is no longer being treated as an unresolved phonological failure or a standing wontfix exception; the current project state is that row `2183` has a working DatPl solution rather than an open mismatch bucket [Germanic/data/oe_known_problems.tsv:1-9].
- The current published derivation trace is an exact match and shows the row's live computational pathway directly: `PROTO: *skúldramiz`, `EXPECTED: sċuldrum`, `OUTPUTS: sċuldrum`, with the intermediate stages `NWGmc A To U Before M: *skúldrumiz`, `PWGmc Early I Apocope: *skúldrumz`, `PGmc Final Z Deletion: *skúldrum`, `OE Sk Palatalization: *ʃúldrum`, and surface `Outcome: sċuldrum` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7462-7482].
- The packet and research memo for this row already agree with the live TSV and with the current §17.41 implementation state: both treat `*skúldramiz -> sċuldrum` as the adopted DatPl solution and preserve the earlier `*skúldru -> sċuldor` route only as superseded project history, not as the live row analysis [Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md:1-289; Germanic/docs/lexeme_reports/research_memos/2183-shoulder-sċuldrum.md:1-99].

## Development-note summary

This row needs an explicit four-way separation, because earlier shoulder work mixed together a cognate-set headword, multiple chronological stages, and several different OE paradigm cells.

First, `PROTO = *skuldrō` in the live TSV is the project's cognate-set label, not the exact staged form consumed by the OE cascade for this row. The row packet makes that visible by listing the live TSV as `PROTO *skuldrō | PROTOFORM *skúldramiz`, while the research memo states that the literature itself is not uniform: Kroonen prefers masculine `*skuldra-`, Orel gives `*skuldr(j)ō`, and Ringe-Taylor cite PWGmc `*skuldru` for the OE branch [Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md:7-10; Germanic/docs/lexeme_reports/research_memos/2183-shoulder-sċuldrum.md:45-53]. In other words, the TSV `PROTO` field here is a lexeme-set headword convention, not a claim that the OE row is being derived directly from that exact notation layer.

Second, `PROTOFORM = *skúldramiz` is the live row-specific derivational input. DEV_NOTES is explicit that this is not just a spelling variant of `*skúldrumiz` or `*skúldrum`; it is a different chronological layer. At lines 39523-39526 the note says: `PROTOFORM is the PGmc-proper form *skúldramiz — the inst.pl. branch of the dat./inst. merger, with thematic *-a- and the *-amiz inst. ending, before NWGmc *a→*u/_m raising` [Germanic/docs/DEV_NOTES.md:39523-39526]. The debug trace confirms that chronology by showing `*skúldramiz` first feeding `NWGmc A To U Before M` to become `*skúldrumiz`, then later losing `*i` and `*z` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7462-7482]. So `*skúldramiz`, `*skúldrumiz`, and `*skúldrum` are not interchangeable notations: they are, respectively, the selected PGmc-proper row input, the post-raising intermediate, and the later post-apocope/post-`*z`-loss stage.

Third, `COUNTERPART = sċuldrum` is an inflected OE target, specifically the attested masculine a-stem dative plural / instrument plural merger form, not the citation lemma and not the late weak-feminine singular. DEV_NOTES states this in implementation form at lines 39502-39504: `TSV row 2183 edit: PROTOFORM *skúldrō → *skúldrumiz, COUNTERPART sċuldra → sċuldrum. Documents this as masc. a-stem DatPl, cell-consistent` [Germanic/docs/DEV_NOTES.md:39502-39504]. The same section then states that `sculdrum` is the target attested in Bosworth-Toller, Hall, and Brunner, with Brunner's `scyldrum` kept as a later i-mutated variant, not the live row target [Germanic/docs/DEV_NOTES.md:39506-39520]. The packet reproduces exactly the same conclusion and adds the current exact trace block [Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md:17-43,143-165].

Fourth, the row's `late_analogy` label still points to the singular history that forced the row away from its earlier target. DEV_NOTES preserves that background very clearly. The section opens by recording that the older setup `*skúldrō -> sċoldor` mismatched the former target `sċuldra`, and that `sċuldra` is an innovative late weak-feminine form: `sċuldra (current COUNTERPART) is innovative late-WS via paradigm-class transfer (Hogg §5.4.5.2); categorically unmodellable` [Germanic/docs/DEV_NOTES.md:39399-39402]. The row therefore remains a `late_analogy` case even though the live DatPl cell itself is the inherited regular escape hatch.

The practical reason the DatPl cell wins is also explicit and should not be flattened into a vague statement about `u` retention. DEV_NOTES says that all the obvious singular candidates still lower root `u` to `o`: `*skúldrō` gives `sċoldor`, `*skúldraz` gives `sċoldor`, `*skúldrą` gives `sċoldor`; the formerly explored `*skúldru` route gives `sċuldor`, but only by crossing cells from a historically prior plural to an OE singular [Germanic/docs/DEV_NOTES.md:39399-39409]. By contrast, the DatPl survives because `*-umiz` protects the relevant vowel environment: `The DatPl is the only surviving cell-consistent path: high *u in *-umiz blocks NWGmcULowering, preserving root /u/` [Germanic/docs/DEV_NOTES.md:39410-39412]. The implementation section then narrows the statement further by preserving the handbook-backed conditioning that medial unstressed `u` is preserved before `m`, not generally immune after stressed `ú` [Germanic/docs/DEV_NOTES.md:39422-39440,39454-39489].

That conditioning is one of the places where notation layers must be kept separate. Earlier exploratory notes used post-raising `*skúldrumiz` or post-apocope `*skúldrum` as probe strings. DEV_NOTES records that those probes were diagnostically useful but not the final row policy: older probes with `*skúldrumiz` produced `sċuldreme`, revealing architecture problems in the old tail handling, whereas the current architecture starts from `*skúldramiz` and derives `sċuldrum` through explicit `a > u / _m`, early third-syllable `*i` loss, and final `*z` deletion [Germanic/docs/DEV_NOTES.md:39589-39607,39611-39660]. So the row's live `PROTOFORM` is not merely a cleaned-up spelling of an earlier probe; it is the project's chosen chronological starting point for the DatPl repair.

The philological dossier preserved in the older shoulder write-up still matters because it explains why `sċuldor`, `sċuldrum`, and `sċuldra` cannot be collapsed into one undifferentiated OE target. The main shoulder dossier quotes Bosworth-Toller as lemmatising `sculdor` m. with plural/oblique forms `sculdru, sculdra, sculdrum`, while the supplement separately adds weak feminine `sculdra, an`; Hall lists `sculdor` as the main lemma; Brunner explains `sceoldor` as a late-West-Saxon post-`sc-` development rather than evidence for inherited NWGmc `u`-lowering [Germanic/docs/dossier-shoulder-2026.md:50-132]. The current row policy therefore does not deny that `sculdor` is the main lemma. It says something narrower and more operational: the attested OE cell that the current cascade can derive regularly is `sċuldrum`, so that is what row `2183` now encodes.

Because of that, the stale chronology line at the head of §17.41 must be read carefully. DEV_NOTES still calls the DatPl repair a `PROPOSED FIX ... awaiting user green-light`, but that heading is now historically stale. The same section later records the actual TSV edit, the implementation log, the verification line `*skúldramiz → sċuldrum ✓`, and the mismatch log entry `sċuldrum: DatPl *-amiz cascade (§17.41)` [Germanic/docs/DEV_NOTES.md:39385-39395,39502-39526,39659-39660,10427-10430]. The slice should therefore treat the substance of the DatPl note as current and treat only the opening status line as stale project chronology.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39383-39660

Source heading: `§17.41 *skúldrō → sċoldor (expected sċuldra 'shoulder'): proposed fix`  
Source line or section hint: `lines 39383-39660`  
Fragment type: `lexeme_specific`  
Status: `current_substance_with_stale_heading`  
Issue tags: `protoform_vs_proto`; `paradigm_cell`; `datpl`; `u_lowering`; `medial_unstressed_u`; `attestation`; `late_analogy`  
Recommended next use: `cite_in_final_report`  
Shared with row IDs:  

This is the core current fragment for the row, even though its first status line is no longer current chronology. The live row policy is already embedded inside it.

The fragment starts by preserving the failure of the old singular setup. It states, in sequence, that `*skúldrō` gives `sċoldor`, that `sċuldra` is the innovative late-WS form, that all nominative-style singular candidates still yield lowered-vowel `sċoldor`, and that the exploratory `*skúldru -> sċuldor` route is cross-cell and therefore no longer the chosen row solution [Germanic/docs/DEV_NOTES.md:39397-39412]. This should be copied forward because it explains why the row is not merely a routine DatPl entry: the DatPl solution exists only because the singular-oriented pathways were audited and found either regular-but-wrong (`sċoldor`) or analogical/unmodellable (`sċuldra`).

The fragment then preserves the exact conditioning claim that makes the DatPl work. The diagnosis block says that the earlier medial-unstressed-`u` rule had been too broad, and it narrows the rule by context, not by morphology: `Medial unstressed *u lowers to *o in OE before /n d t s/ etc., but is preserved before /m/. This is precisely the empirical contrast between past-plural -on (< *-un) and DatPl -um (< *-umiz)` [Germanic/docs/DEV_NOTES.md:39422-39440]. The note immediately anchors that claim in handbook quotations copied into DEV_NOTES itself: Campbell §373 says `u is always well preserved ... before m, e.g. māþum, d.p. -um, -sum as suffix`; Brunner §44 Anm. 7 says `Im Inlaut vor anderen Konsonanten außer -m und -ng ist -o- im Ws. schon früh durchwegs durchgeführt`; Hogg §3.3.1.3 says `before /m/, as in the dative plural inflexion -um ... the ⟨u⟩ was normally preserved` [Germanic/docs/DEV_NOTES.md:39454-39478]. Later reporting should preserve that substance rather than paraphrasing it into a looser statement that `-um keeps u`.

The same fragment also preserves the row's exact encoding decision and the reason for distinguishing `PROTO` from `PROTOFORM`. At lines 39523-39526 DEV_NOTES says `PROTOFORM is the PGmc-proper form *skúldramiz — the inst.pl. branch of the dat./inst. merger, with thematic *-a- and the *-amiz inst. ending, before NWGmc *a→*u/_m raising` [Germanic/docs/DEV_NOTES.md:39523-39526]. It then justifies the choice of `*-amiz` over `*-amaz` with explicit source-based reasoning: Ringe-Taylor's complete dat./inst.pl. syncretism, Campbell/Brunner/Fulk's derivation of OE `-um` from inst.pl. `*-omis/*-amiz`, and runic/Gothic evidence for the `*-am(i)z` chain [Germanic/docs/DEV_NOTES.md:39528-39553]. Those lines should be treated as essential row-policy content, because they explain why the current `PROTOFORM` is `*skúldramiz` rather than the more superficial OE-facing stage `*skúldrum`.

This fragment is also the right place to preserve the live attestation logic. DEV_NOTES says the conservative non-i-mutated target is `sculdrum`, cites Bosworth-Toller, Hall, and Brunner, and explicitly distinguishes Brunner's `scyldrum` as a later i-mutated variant rather than the row target [Germanic/docs/DEV_NOTES.md:39506-39521]. Combined with the exact trace block in the published debug snapshot, this gives a complete current dossier: the row has an attested OE target, a chronologically explicit PGmc `PROTOFORM`, a rule sequence that derives it, and a source-backed explanation for why the key `u` survives [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7462-7482].

Finally, the fragment ends with the implementation log and verification line, which are too specific to omit. DEV_NOTES records the coordinated FST edits, then states: `Verification: *skúldramiz → sċuldrum ✓ (P3 passes)` [Germanic/docs/DEV_NOTES.md:39611-39660]. That line is the cleanest surviving statement that the DatPl solution moved from proposal to verified live behavior.

### DEV_NOTES:line-39746-39950

Source heading: `§17.41-historical: original (retracted) cell-switch draft`  
Source line or section hint: `lines 39746-39950`  
Fragment type: `superseded_or_diagnostic_for_lexeme`  
Status: `superseded`  
Issue tags: `project_history`; `paradigm_cell`; `citation_form`; `plural_to_singular`; `backformation`; `source_conflict`  
Recommended next use: `use_to_explain_superseded_analysis`  
Shared with row IDs:  

This fragment is superseded as live row policy, but it is not noise and should remain indexed if index space allows. It preserves the serious earlier project conclusion that row `2183` ought to target the main OE citation-form side of the lexeme rather than the DatPl.

The fragment inventories the earlier shoulder dossiers and then states the now-retracted finding that `sculdor` should be the preferred counterpart. The note says the project's earlier plural-cell-switch convention required both an unmodellable singular and a historically prior plural; for shoulder, it judged that only the second condition held. It therefore recommended `COUNTERPART = sċuldor`, because the singular back-formation pathway `*skúldru -> sċuldor` was itself a Neogrammarian outcome already reproducible by the cascade [Germanic/docs/DEV_NOTES.md:39750-39788]. That material matters because it shows that the `*skúldru -> sċuldor` option was a principled cell-choice proposal, not a casual discarded guess.

The fragment then classifies `*skúldrō -> *skúldru` not as a new sound law to encode, but as a morphological or analogical cell switch to a historically prior plural cell, with singular `sculdor` understood as a back-formation repaired by epenthesis [Germanic/docs/DEV_NOTES.md:39790-39807]. Later lines continue that same logic and culminate in the abandoned plan to edit the row accordingly: `PROTOFORM *skúldrō -> *skúldru` and `COUNTERPART sċuldra -> sċuldor`, while leaving `PROTO = *skuldrō` as the cognate-set headword [Germanic/docs/DEV_NOTES.md:39943-39946].

What supersedes this fragment is not a discovery that `sculdor` ceased to be philologically important. The main shoulder dossier still makes clear that `sculdor` is the mainstream OE lemma, while `sculdra` is a peripheral weak-feminine doublet [Germanic/docs/dossier-shoulder-2026.md:50-132]. What changed is that the later DatPl work found a strictly cell-consistent, attested, and computationally verified pairing `*skúldramiz -> sċuldrum` that avoided asking a plural-derived singular history to do the row's modelling work [Germanic/docs/DEV_NOTES.md:39385-39660]. So this fragment should be used only as labelled project chronology.

## Superseded or diagnostic material

The main diagnostic danger for this row is false collapsing of four different shoulder items into one narrative. They must remain separate:

- regular singular comparator `*skúldrō -> sċoldor` or, in parallel singular probes, `*skúldraz/*skúldrą -> sċoldor` [Germanic/docs/DEV_NOTES.md:39399-39406];
- live row target `*skúldramiz -> sċuldrum` [Germanic/docs/DEV_NOTES.md:39502-39526,39659-39660; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7462-7482];
- superseded but serious project detour `*skúldru -> sċuldor` [Germanic/docs/DEV_NOTES.md:39772-39788,39943-39946];
- late analogical weak-feminine `sċuldra`, which remains part of lexeme history rather than live row policy [Germanic/docs/DEV_NOTES.md:39400-39402; Germanic/docs/dossier-shoulder-2026.md:72-82,128-131].

Other locally surviving material is useful only with clear warning labels. The packet's `old_english_wiktionary.tsv` hit `shoulder -> sċuldra` is real lexical background but no longer the row target, so it should not be allowed to override the live DatPl row [Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md:183-190]. The DEV_NOTES references to `eaxl` 'shoulder' belong to a completely different OE lexeme (`*ahslu`) and are irrelevant to row `2183` except as a reminder not to search by English gloss alone [Germanic/docs/DEV_NOTES.md:8171-8173,8203-8205].

The only stale element inside the core §17.41 block is the heading status line `awaiting user green-light`. The body of that section, the mismatch log, the packet, the memo, and the live debug snapshot all show that the DatPl solution has already been implemented and verified [Germanic/docs/DEV_NOTES.md:39385-39395,39502-39526,39659-39660,10427-10430; Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md:49-177]. Future reporting should therefore call the heading stale rather than calling the whole section stale.

## Open questions for later work

- If this row is indexed, decide whether index integration should include only the current DatPl fragment or also the superseded `*skúldru -> sċuldor` fragment; the latter is genuinely useful project history, not mere noise.
- Consider tightening the live TSV note someday so it says not only that `PROTOFORM` is PGmc-proper `*-amiz`, but also that the row intentionally targets the attested masc. a-stem DatPl `sċuldrum`, not the citation lemma `sculdor` and not the late weak-feminine `sċuldra` [Germanic/data/germanic-aligned-final.tsv:981-981].
- Add a reusable shoulder paradigm probe if the row is revisited. The current row is well supported by dossiers and the published trace, but `Germanic/tools/oe_paradigm_probe.py` still has no dedicated shoulder configuration [Germanic/docs/lexeme_reports/research_memos/2183-shoulder-sċuldrum.md:74-84].
- If later index prose quotes the `*-amiz` rationale, keep the chronology explicit: `*skúldramiz` is the selected PGmc input, `*skúldrumiz` is the post-raising stage, and `*skúldrum` is the later post-apocope/post-`*z`-loss stage. Treating them as free variants would blur the reason the row was encoded this way in the first place.

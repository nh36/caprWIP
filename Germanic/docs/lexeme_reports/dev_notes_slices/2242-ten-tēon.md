---
row_id: 2242
concept: ten
counterpart: tēon
proto: *téxun
protoform: *téxun
derivation_class: attested_variant
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2242-ten-tēon.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2242-ten-tēon.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2242 ten / tēon

## Current row state

- The live aligned OE row now reads `CONCEPT = ten`, `COUNTERPART = tēon`, `PROTO = *téxun`, `PROTOFORM = *téxun`, `DERIVATION_CLASS = attested_variant`, with an explicit row note saying the entry was retargeted away from West-Saxon `tīen` toward `tēon` as the regular outcome of bare `*tehun` after intervocalic `h`-loss and contraction; the same note explicitly treats `tien` as a secondary i-umlauted form and points to `tēoða` and `-tēontig` as preserving the un-umlauted stem [Germanic/data/germanic-aligned-final.tsv:1210-1210].
- The existing packet and research memo already use the reusable stem `2242-ten-tēon`, and both preserve the same current row framing: the packet gives the compact derivation `*téxun -> *téxon -> *téoxon -> *téoon -> *tḗon -> tēon`, while the memo explicitly distinguishes the bare-cardinal base `*tehun` from the inflectional i-stem material behind `tien/tīen` [Germanic/docs/lexeme_reports/packets/2242-ten-tēon.md:17-41; Germanic/docs/lexeme_reports/research_memos/2242-ten-tēon.md:32-40].
- `oe_known_problems.tsv` has no live exception entry for this row or for `*téxun`; the row is therefore no longer treated as an unresolved OE mismatch bucket item [Germanic/data/oe_known_problems.tsv:1-9].
- Coverage infrastructure already expects report-style handling here rather than a blank regular-row pass-through: row `2242` is flagged as a note-bearing `attested_variant` entry [Germanic/docs/lexeme_reports/coverage_audit.md:149-149].

## Detailed development-note summary

The crucial distinction for this row is not between two competing spellings of one unchanged target, but between **two different historical bases** that later Old English materials can reflect. The live row keeps both `PROTO` and `PROTOFORM` as `*téxun`, i.e. the project’s OE-directed spelling of PGmc `*tehun`, because the row is now intended to model the **bare cardinal**. The later dossier in `DEV_NOTES` repeatedly insists that West-Saxon `tien/tīen` belongs to a different layer: it reflects i-umlaut propagated from inflected i-stem forms such as `*tehuni-`, not the uninflected cardinal itself [Germanic/data/germanic-aligned-final.tsv:1210-1210; Germanic/docs/DEV_NOTES.md:42363-42383,42532-42535]. Fulk’s wording, preserved directly in `DEV_NOTES`, is the clearest short statement of the contrast: “OE tien must show umlaut originating in the inflected forms … The uninflected form without umlaut is reflected in *hund-tēon-tig* ‘100’” [@Fulk2018, §10.2; Germanic/docs/DEV_NOTES.md:42363-42371].

The current project decision is therefore to target `tēon` as the regular phonological development of bare `*tehun`, not to deny the reality of `tien/tīen`. `DEV_NOTES` reconstructs the row’s regular path very explicitly: breaking gives `*téoxun`, weak-tail lowering gives `*téoxon`, intervocalic `h/x`-loss gives `*téoon`, and contraction should then yield `*tḗon`, surfacing as `tēon` [Germanic/docs/DEV_NOTES.md:42385-42399,42457-42460]. The same note stresses that the cascade had originally stalled one step too early because `OEContraction` covered `*eo + a -> *ēo` but not `*eo + o -> *ēo`; the ten fix was framed as filling that specific gap, not as inventing a new special exception for one numeral [Germanic/docs/DEV_NOTES.md:42401-42421,42623-42629].

The strongest source-backed support for that retargeting comes from handbook material embedded directly in the dossier. `DEV_NOTES` preserves Campbell’s contraction rule for front vowel plus following back vowel after intervocalic `x/h`-loss and cites the exact parallel `*slehan -> *sleahan -> *slean -> slēan` as the already-working comparator [@Campbell1959, §238.2; Germanic/docs/DEV_NOTES.md:42376-42379]. It then preserves Brunner’s more directly row-relevant statements. One quotation gives the formal rule: “Urspr. eh + Vokal wird … ws.-kent. zu éo,” with `teoða` and `-tēontig` listed among the outcomes [@SieversBrunner1965, §129.2; Germanic/docs/DEV_NOTES.md:42551-42569]. Another gives the cardinal itself as a paradigm example: “tēon zehn aus *tëhun (got. taihun)” [@SieversBrunner1965, §234; Germanic/docs/DEV_NOTES.md:42543-42549]. A third makes the contrast with the umlauted simplex explicit: “Ws. tien, tȳn … erklärt sich durch i-Umlaut in flekt. Formen; nordh. steht ohne i-Umlaut tēa, tēo …” [@SieversBrunner1965, §129 Anm. 6; Germanic/docs/DEV_NOTES.md:42571-42575].

The wider survey in `DEV_NOTES` is important because it separates **regular outcome** from **attested simplex citation practice** instead of collapsing them. Campbell’s attestation summary gives `tien; nW-S tēn, lNorth. also tēo, tēa` [@Campbell1959, §682; Germanic/docs/DEV_NOTES.md:42372-42375]. Brunner’s dialect table similarly emphasizes `tien/tȳn` in West Saxon but `tēn / tēo / tēa` elsewhere [@SieversBrunner1965, §325; Germanic/docs/DEV_NOTES.md:42577-42581]. Bülbring and Kaluza support the non-WS un-umlauted branch, and Hirt and Ringe-Taylor preserve the analysis that the umlauted form depends on inflected `*tehuni-` material rather than the bare numeral [@Bulbring1902, §557e; @Kaluza1906; @Hirt1931, §92; @RingeTaylor2014; Germanic/docs/DEV_NOTES.md:42583-42597]. The row-level consequence is that `COUNTERPART = tēon` is being used as a **regularized un-umlauted target**, while the more familiar simplex spellings `tien/tīen`, `tēn`, `tēo`, and `tēa` remain crucial comparative and attestation background rather than irrelevant noise.

That is why the ordinal and compound evidence matters so much in this row’s working note. The dossier does not rely only on an abstract sound law; it also preserves the claim that Old English productively kept an un-umlauted `tēon-` stem outside the levelled simplex cardinal. `DEV_NOTES` explicitly points to `tēoða` and `-tēontig` / `hundteóntig` as the same contraction product and uses Bosworth-Toller compound evidence to show that `tēon-` remained productive in Old English composition [@SieversBrunner1965, §129.2; @Kroonen2013, s.v. *tehun-; Germanic/docs/DEV_NOTES.md:42551-42569,42598-42603]. This does not magically turn exact simplex `tēon` into the ordinary dictionary headword, but it does show that the un-umlauted stem the row now targets is philologically real and not a merely ad hoc FST normalization.

Project chronology still matters here, because the row was not always framed this way. The January 2026 note treated `*texun -> teoun` as a high-priority failure with expected `tīen`, and the action checklist was still oriented toward pushing the cascade toward the umlauted West-Saxon form [Germanic/docs/DEV_NOTES.md:2647-2662]. The later April dossier supersedes that position explicitly. Its options table now labels `tien / tīen` “NO” as the regular target because it requires i-umlaut from inflected i-stem cells, while `tēon` is the recommended “YES” outcome for the bare uninflected numeral [Germanic/docs/DEV_NOTES.md:42423-42440]. The older note should therefore be preserved only as project history documenting the abandoned target-selection policy.

The main unresolved tension is classificatory, not phonological. The live row still says `DERIVATION_CLASS = attested_variant` [Germanic/data/germanic-aligned-final.tsv:1210-1210], but the DEV_NOTES dossier repeatedly argues for `tēon` as the **regular** outcome of bare `*tehun`, while also acknowledging that the best directly cited simplex spellings are often `tien/tīen`, `tēn`, `tēo`, and `tēa` rather than exact citation-form `tēon` [Germanic/docs/DEV_NOTES.md:42423-42430,42577-42581,42647-42660]. For working-note purposes, the safest formulation is: the row currently targets a regularized un-umlauted OE form that is well supported by sound law and by `tēoða / -tēontig`, but whose status as a straightforward directly attested simplex headword remains weaker than the row’s current `attested_variant` label suggests.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-2647-2662

- Source heading: `HIGH PRIORITY: PGmc final *-un behavior (2026-01-25)`
- Source line or section hint: `lines 2647-2662`
- Fragment type: `superseded_row_policy`
- Status: `superseded`
- Issue tags: `old_target`; `tien`; `pre-retarget`; `project_history`
- Recommended next use: `preserve_as_diagnostic_history_only`
- Shared with row IDs: `2174`; `2142`

This fragment is important precisely because it is no longer current. It records the older state in which `*texun` was producing `teoun` and the expected target was still `tīen` [Germanic/docs/DEV_NOTES.md:2647-2657]. The checklist that follows is a repair agenda for the old target-selection phase, not for the current row policy [Germanic/docs/DEV_NOTES.md:2658-2662]. Later writers should keep it only as chronology for the abandoned `tīen` target.

### DEV_NOTES:line-42361-42504

- Source heading: `§17.48 — *téxun → tēon (ten): paradigm-cell-matching dossier`
- Source line or section hint: `lines 42361-42504`
- Fragment type: `lexeme_specific_dossier`
- Status: `current`
- Issue tags: `ten`; `tēon`; `tien`; `contraction_gap`; `target_selection`
- Recommended next use: `primary_current_row_anchor`
- Shared with row IDs:

This is the main row-specific dossier. It preserves Fulk’s direct statement that OE `tien` is umlauted from inflected forms and that the uninflected form survives in `*hund-tēon-tig*` [@Fulk2018, §10.2; Germanic/docs/DEV_NOTES.md:42363-42371]. It also gives Campbell’s dialect summary, the failing pre-fix trace, the `tien/tīen` versus `tēon/tēn/tēo` option table, and the explicit recommendation to retarget the row to `tēon` while adding the missing contraction clauses [@Campbell1959, §§238.2, 682; Germanic/docs/DEV_NOTES.md:42372-42504]. For row `2242`, this is the clearest single current fragment.

### DEV_NOTES:line-42505-42629

- Source heading: `§17.48.1 Broader source survey`
- Source line or section hint: `lines 42505-42629`
- Fragment type: `current_source_survey`
- Status: `current`
- Issue tags: `bare_tehun`; `tehuni`; `ordinal_support`; `compound_support`; `contraction_rule`
- Recommended next use: `cite_for_source-backed_regularization`
- Shared with row IDs:

This fragment expands the row from an implementation memo into a proper source dossier. It keeps the reconstruction layer (`*tehun` versus inflected `*tehuni-`) distinct, carries over Brunner’s and related handbook quotations, and explicitly places `tēoða` and `-tēontig` inside the same contraction class as the proposed bare cardinal `tēon` [@SieversBrunner1965, §§129.2, 129 Anm. 6, 234; @Bulbring1902, §557e; @Kaluza1906; @Hirt1931, §92; @RingeTaylor2014; Germanic/docs/DEV_NOTES.md:42511-42629]. It is the best fragment for preserving why regular `tēon` and secondary `tien` must be kept distinct even when both are genuine Old English material.

### DEV_NOTES:line-42631-42676

- Source heading: `§17.48.1 D–E and Verdict`
- Source line or section hint: `lines 42631-42676`
- Fragment type: `current_verdict`
- Status: `current`
- Issue tags: `risk_audit`; `no_new_sound_change`; `verdict`; `productive_stem`
- Recommended next use: `cite_for_final_row_position`
- Shared with row IDs: `2058`; `2195`

This final fragment matters because it turns the survey into an explicit project conclusion. It records that the new contraction environment is lexically isolated in the current dataset, that the rule is not an innovation but a missing part of an already-established `h`-loss + contraction pattern, and that the literature supports `*tēon*` / `tēn` / `tēo` / `tēa` as the regular bare-cardinal branch while treating `tien` as secondary [Germanic/docs/DEV_NOTES.md:42631-42676]. It is also where DEV_NOTES states most clearly that `tēon-` remained productive in compounds and the ordinal family.

## Superseded or diagnostic material

- The January `expected tīen` note is superseded and should stay superseded. It documents the earlier mismatch and the earlier policy assumption, but it no longer matches the live row or the April source dossier [Germanic/docs/DEV_NOTES.md:2647-2662; Germanic/data/germanic-aligned-final.tsv:1210-1210].
- The `§17.48` implementation checklist still says `TSV row 1210: COUNTERPART tīen → tēon` [Germanic/docs/DEV_NOTES.md:42496-42500]. That wording is useful project chronology, but it is stale bookkeeping language: row ID `2242` is the live aligned row, and the slice should not inherit the old row-number framing as if it were current metadata.
- The biggest philological caution is not that `tēon` is unsupported, but that its support is **unevenly distributed**. The sound-law and derivative evidence are strong, especially `tēoða` and `-tēontig`; direct simplex citation-form attestation is less straightforward than for `tien/tīen`, `tēn`, `tēo`, or `tēa` [Germanic/docs/DEV_NOTES.md:42372-42375,42577-42581,42598-42603]. Later reporting should therefore avoid overstating the row as if `tēon` were simply the ordinary directly cited simplex form in every handbook.
- The live `attested_variant` label may itself be partly diagnostic of older framing. The DEV_NOTES dossier argues for a regularized bare-cardinal target, while the memo already warns that the row behaves more like a normalized regular outcome than like a straightforward attested simplex-headword variant [Germanic/docs/lexeme_reports/research_memos/2242-ten-tēon.md:42-50,58-60,74-75].

## Open questions for later work

- Should the row continue to advertise `DERIVATION_CLASS = attested_variant`, or should it eventually move to something like `reconstructed_oe` or another normalized-regular label? The current DEV_NOTES argument for `tēon` is strong, but its strongest support comes from sound law plus `tēoða / -tēontig`, not from the most common simplex citation form [Germanic/docs/DEV_NOTES.md:42537-42603; Germanic/data/germanic-aligned-final.tsv:1210-1210].
- If a final report is drafted, the prose should probably say explicitly that `PROTO = PROTOFORM = *téxun` in the live row, while the real analytical contrast is between bare `*tehun` and inflected `*tehuni-`; otherwise later readers may mistake the `tēon` versus `tīen` contrast for a mere spelling preference instead of a paradigm-cell contrast [Germanic/docs/DEV_NOTES.md:42363-42383,42511-42535].
- If indexing proceeds later, the safest attachable current fragments are the main dossier (`42361-42504`), the broader source survey (`42505-42629`), and the verdict/risk-audit block (`42631-42676`), with the January `2647-2662` note kept separately as superseded chronology rather than merged into a current summary.

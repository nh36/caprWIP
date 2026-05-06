---
row_id: 2136
concept: needle
counterpart: nǣdl
proto: *nḗθlō
protoform: *nḗðlō
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2136-needle-nǣdl.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2136 needle / nǣdl

## Current row state

- Packeted row metadata already separates the three levels that matter here: `PROTO = *nḗθlō`, `PROTOFORM = *nḗðlō`, and OE `COUNTERPART = nǣdl`, with `DERIVATION_CLASS = early_analogy` [Germanic/docs/lexeme_reports/packets/2136-needle-nǣdl.md:7-10].
- The live derivation trace is currently successful. The packet’s compact trace starts from voiced `PROTO: *nḗðlō`, passes through `PWGmc Dental Hardening: *nḗdlō`, `NWGmc Final Long O Raising: *nḗdlu`, `NWGmc Long E Lowering: *nǣdlu`, then `OE High Vowel Apocope: *nǣdl`, yielding exact `Outcome: nǣdl` [Germanic/docs/lexeme_reports/packets/2136-needle-nǣdl.md:17-41].
- The aligned TSV row is consistent with that repaired state: the OE row carries the note `R/T p.435: PGmc *nēdlō has Verner's alternation; OE nǣdl reflects *d variant`, and no row-specific problem entry is carried forward in `oe_known_problems.tsv` [Germanic/data/germanic-aligned-final.tsv:800-800; Germanic/docs/lexeme_reports/packets/2136-needle-nǣdl.md:44-46].
- The research memo is explicit that the remaining task is documentary, not derivational: the row already derives correctly, and the real issue is to explain the split between comparative `PROTO`, OE-facing `PROTOFORM`, and the attested OE target while keeping pre-fix mismatch history separate from current authority [Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:13-18,49-58,73-79].

## Development-note summary

No securely attachable **fully current row-specific** DEV_NOTES fragment survives in isolation for row 2136. The row-numbered March 2026 note is still useful as repair history, but it opens from the pre-fix state (`PROTOFORM: *nēθlō`) and gives an instruction already implemented; read by itself, it is no longer safe current metadata [Germanic/docs/DEV_NOTES.md:10243-10253]. The current working authority therefore has to be composite: live row metadata and trace, the shared March 2026 Verner protoform convention, and the later cluster-attestation audit that explicitly keeps `nǣdl` among the retained unbroken OE nominative targets [Germanic/docs/lexeme_reports/packets/2136-needle-nǣdl.md:7-10,17-41; Germanic/docs/DEV_NOTES.md:10265-10285,29883-29915,30067-30083; Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:55-58,73-79,97-99].

The row has to be written with a strict three-way distinction. `PROTO = *nḗθlō` is the comparative or cognate-set headword; `PROTOFORM = *nḗðlō` is the OE-facing Verner-grade alternant actually fed to the derivational cascade; `nǣdl` is the attested OE citation form [Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:49-57,73-79]. The old row-specific repair line “Change protoform to `*nēdlō` for the OE row” remains valuable only once corrected by the later shared update that insists on PGmc-stage `*ð`, not already-hardened `*d`: “use the post-Verner form in PROTOFORM,” and “`*ð` is the PGmc Verner's Law outcome,” while `*ð -> *d` is delegated to later PWGmc dental hardening [Germanic/docs/DEV_NOTES.md:10253-10253,10267-10275]. On current project terms, the live row is therefore not `*nēθlō -> nǣdl` by OE-side repair, but `*nḗðlō -> *nḗdlō -> *nǣdlu -> *nǣdl -> nǣdl` by choosing the voiced alternant upstream [Germanic/docs/lexeme_reports/packets/2136-needle-nǣdl.md:27-41; Germanic/docs/DEV_NOTES.md:10283-10285].

The consonant explanation also needs to stay explicit. DEV_NOTES says of needle: “The consonant order is `θl` not `lθ`, so `PWGmcLThVoicing` does not apply”; the word is instead a Verner-alternation case where OE `nǣdl` “reflects the `*d` variant” [Germanic/docs/DEV_NOTES.md:1343-1347]. Ringe vol. 1 likewise gives `*nēþlō- ~ *nēdlō- ‘needle’`, and the Ringe-Taylor extract used in the repo gives `PGmc *néplō, *nédlo- ‘needle’ ... > OE nédl`, again preserving a voiced/voiceless alternant rather than an ordinary OE-only fix [docs/references/ringe_vol1_pie_to_pgmc.txt:13220-13228; docs/references/ringe_taylor_linguistic_history_vol2.txt:18848-18849]. This is why `early_analogy` remains workable: the marked move is early alternant selection in the input history, not a late paradigm-cell substitute [Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:73-79,93-97].

Philologically, `nǣdl` should be treated as an attested OE headword with an unbroken `-dl` cluster, not as a provisional reconstruction and not as a row that needs retargeting to an oblique form. The later cluster audit in DEV_NOTES lists `*nēðlō | nǣdl | nǣdl | ✓`, then records `nǣdl` under “Unbroken NomSg attested?” with lemma form `nǣdl`, and the resolved policy retains `nǣdl` among the existing unbroken nominative targets kept unchanged because they are directly attested in early, poetic, or Anglian usage [Germanic/docs/DEV_NOTES.md:29887-29915,30075-30083]. The background references point in the same direction: Campbell lists `nédl needle` among the expected unbroken forms after `t` and `d`; Hogg cites `nidi 'needle'` among forms with possible syllabic sonorants; Clark Hall gives `nædl (ē) f. ‘needle’`; and the Brunner/Sievers quotation copied into DEV_NOTES explicitly says `nǣdl ~ nēdl` is frequent after `t` and `d` [docs/references/campbell_old_english_grammar.txt:9977-9979; docs/references/hogg_vol1.txt:4772-4777; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29177-29177; Germanic/docs/DEV_NOTES.md:31229-31237]. The row’s present target is therefore secure as OE philology; the only thing that needed repair was the upstream choice of the voiced Verner-grade protoform [Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:61-69,81-89].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-10265-10286

- Source heading: `Pattern`
- Source line or section hint: `lines 10265-10286`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `verners_law`; `protoform_convention`; `proto_vs_protoform`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2088`

This is the clearest current DEV_NOTES authority for the live row. It states the general project convention in exactly the form row 2136 now needs: “**use the post-Verner form in PROTOFORM** when the OE reflex shows Verner's Law applied” [Germanic/docs/DEV_NOTES.md:10267-10269]. It then corrects the notation level explicitly: “Used `*ð` ... instead of `*d` ... since `*ð` is the PGmc Verner's Law outcome,” while `*ð -> *d` is a later PWGmc hardening step [Germanic/docs/DEV_NOTES.md:10271-10275]. The results table names row 2136 directly: “`*nēðlō` → `nǣdl` ✓ (was `nǣþl`)” [Germanic/docs/DEV_NOTES.md:10283-10285]. For this slice, that makes the fragment current not because it is needle-only, but because it is the surviving statement of the repo-wide convention that converts the earlier repair note into the live row design.

### DEV_NOTES:line-29883-29915

- Source heading: `§17.18 current dataset state` plus `§17.18.3 Attestation findings`
- Source line or section hint: `lines 29883-29915`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `unbroken_nom_sg`; `cluster_philology`; `attestation`; `row_selection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This later audit is current row authority for the OE target itself. In the FST/TSV consistency table, row 2136 appears as `*nēðlō | nǣdl | nǣdl | ✓`, i.e. the live voiced protoform already produces the desired output with no further workaround [Germanic/docs/DEV_NOTES.md:29887-29893]. The immediately following attestation table strengthens that result with lexical evidence: `nǣdl` is listed as having unbroken nominative-singular attestation, with lemma form `nǣdl` [Germanic/docs/DEV_NOTES.md:29909-29915]. That matters because it blocks any attempt to treat the row as merely a convenient cluster-debug output. In current project usage, `nǣdl` is not just derivable; it is one of the attested unbroken OE lemma targets the dataset is intentionally preserving [Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:61-69].

### DEV_NOTES:line-30067-30083

- Source heading: `§17.18.7.1 Resolved policy`
- Source line or section hint: `lines 30067-30083`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `resolved_policy`; `nom_sg_target`; `cluster_class`; `dataset_register`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This resolved-policy fragment tells later writers what to do with the class after the audit. DEV_NOTES says the “existing unbroken NomSg targets” including `nǣdl` “are all directly attested manuscript spellings” and “are therefore retained unchanged” [Germanic/docs/DEV_NOTES.md:30075-30080]. It immediately adds that the FST’s present behavior “is correct for these ten lemmas: it produces an unbroken cluster which matches the early / poetic / Anglian register chosen by the dataset” [Germanic/docs/DEV_NOTES.md:30080-30083]. For row 2136, this is the strongest current statement that no paradigm-cell rescue is required: the chosen citation target is already the retained dataset norm.

### DEV_NOTES:line-31229-31237

- Source heading: `§154 (line 6306) specifically on syllabic *l`
- Source line or section hint: `lines 31229-31237`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `background`
- Issue tags: `syllabic_l`; `orthographic_background`; `cluster_attestation`; `brunner_sievers`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is background rather than controlling row policy, but it is worth preserving because DEV_NOTES has already excerpted exactly the philological point later reports are likely to need. The quotation says syllabic `*l` is “very frequent after `t` and `d`,” specifically naming `nǣdl ~ nēdl`, `spātl`, `setl`, and `botl`, and adds that these forms occur “almost only in this spelling” [Germanic/docs/DEV_NOTES.md:31229-31237]. That does not by itself decide the reconstruction question, but it does support the current slice’s narrow claim that OE `nǣdl` belongs to an established unbroken `-dl` spelling class rather than needing a special oblique target.

## Superseded or diagnostic material

### DEV_NOTES:line-10243-10253

- Source heading: `Analysis: *nēθlō → nǣdl`
- Source line or section hint: `lines 10243-10253`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `row_repair_history`; `old_protoform`; `implemented_fix`; `verners_law`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This is the key row-specific repair note, but it is no longer safe as standalone current authority. It records the pre-fix state exactly—`PROTOFORM: *nēθlō` with OE `nǣdl` and a note already mentioning Verner alternation—then states the problem plainly: the note acknowledges the `*d`-grade while the row still carried voiceless `*θ` [Germanic/docs/DEV_NOTES.md:10245-10252]. The line “**Fix:** Change protoform to `*nēdlō` for the OE row” remains valuable project history, but only once translated through the later shared correction that the PGmc-stage form should be written with `*ð`, not already-hardened `*d` [Germanic/docs/DEV_NOTES.md:10253-10253,10271-10275]. In other words, this fragment preserves how the row was repaired, not the exact metadata wording later reports should copy.

### DEV_NOTES:line-1343-1356

- Source heading: `Not this rule: *nēθlō → nǣdl ('needle')` plus `Scope of Verner's Law in the project`
- Source line or section hint: `lines 1343-1356`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `verners_law`; `not_lth_voicing`; `old_mismatch_state`; `row_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This earlier note preserves one still-useful philological warning and one outdated workflow claim. The useful part is the statement that needle is “not this rule”: the consonant order is `θl`, not `lθ`, so ordinary `*lþ > ld` reasoning is irrelevant; OE `nǣdl` instead reflects the voiced Verner alternant [Germanic/docs/DEV_NOTES.md:1343-1345]. What is no longer current is the closure: DEV_NOTES then says the item is “currently a mismatch” and “remains a known mismatch,” which ceased to be true once the row adopted voiced `PROTOFORM = *nḗðlō` and the March 2026 repair landed [Germanic/docs/DEV_NOTES.md:1346-1356; Germanic/docs/DEV_NOTES.md:10283-10285]. This fragment should therefore be mined only for the negative methodological point, not for live status.

### DEV_NOTES:line-29993-30012

- Source heading: `Option 3 — Paradigm-cell strategy: target GenSg (or other oblique) for the whole class`
- Source line or section hint: `lines 29993-30012`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `paradigm_cell`; `cluster_strategy`; `nǣdla_proposal`; `rejected_option`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This option is important to preserve precisely because it is no longer the project policy for row 2136. In the middle of the larger `-Cl/-Cn/-Cm#` audit, DEV_NOTES briefly proposed shifting the whole class to oblique targets; for `nǣdl`, because it is a feminine ō-stem, the note floated “the gen.pl. or dat.sg.” and even wrote tentative `nǣdla*(?)` in the sample list [Germanic/docs/DEV_NOTES.md:29993-30000]. The same passage acknowledges the drawback immediately: for `nǣdl`, the truly medial cluster appears only in gen.pl. `nǣdla`, while dat.sg. `nǣdle` already phonotactically separates the cluster [Germanic/docs/DEV_NOTES.md:30002-30012]. Later resolved policy rejected this route for the retained unbroken nominative targets, so this fragment belongs only in the checked history of alternatives [Germanic/docs/DEV_NOTES.md:30067-30083].

## Open questions for later work

- If the live TSV note is ever rewritten, make the three-way distinction explicit in one sentence: comparative `PROTO = *nḗθlō`, OE-facing `PROTOFORM = *nḗðlō`, and attested OE `COUNTERPART = nǣdl`; the present note still compresses that distinction too much [Germanic/data/germanic-aligned-final.tsv:800-800; Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:93-99].
- If `dev_notes_slices/index.tsv` is updated later, index the row as depending on shared current Verner-policy and cluster-attestation fragments (`10265-10286`, `29883-29915`, `30067-30083`), while treating the row-numbered repair note (`10243-10253`) and the old mismatch note (`1343-1356`) as superseded or diagnostic rather than standalone current authority [Germanic/docs/DEV_NOTES.md:1343-1356,10243-10286,29883-29915,30067-30083].
- If a later final report wants wider comparative bibliography, keep Kroonen and Orel in the background-only layer unless the project decides to revisit the comparative headword itself; the current row design deliberately follows the repo’s Ringe/Taylor-style voiced/voiceless alternant framing instead [Germanic/docs/lexeme_reports/research_memos/2136-needle-nǣdl.md:39-45].

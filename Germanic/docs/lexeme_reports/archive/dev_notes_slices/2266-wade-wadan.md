---
row_id: 2266
concept: wade
counterpart: wadan
proto: *wádaną
protoform: *wádaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2266-wade-wadan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2266-wade-wadan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2266 wade / wadan

## Current row state

- CONCEPT: `wade`
- COUNTERPART: `wadan`
- PROTO: `*wádaną`
- PROTOFORM: `*wádaną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1`; the row also carries duplicated Wiktionary-etymology provenance in the source note field [Germanic/data/germanic-aligned-final.tsv:1303-1303].
- The row's direct lexical support is modest but consistent: `old_english_wiktionary.tsv` gives `wade → wadan`, and the shared A-restoration analysis file extracts Luick's list of open-syllable restoration examples with explicit `wadan` [Germanic/data/old_english_wiktionary.tsv:325-325; Germanic/docs/analysis/arestoration_r_l_research.md:206-214].
- Row-specific packet and research memo files already exist. The packet is useful as evidence inventory, but the memo is right that the packet alone underweights the later DEV_NOTES reversal that keeps plain `-aną` rather than the temporary `-ăną` workaround [Germanic/docs/lexeme_reports/packets/2266-wade-wadan.md:15-18,56-190; Germanic/docs/lexeme_reports/research_memos/2266-wade-wadan.md:14-18,20-28,47-50].
- No row-specific pilot file or clearly row-local dossier beyond that shared A-restoration analysis was found during slice preparation.

## Development-note summary

The live row is best treated as a **stable regular Class VI infinitive**, not as a lexeme with unresolved OE headword competition. The present row state is already explicit about the engineering reason: `PROTO = PROTOFORM = *wádaną` because the infinitival suffix must retain plain back-vowel `a` so that OE A-restoration can undo Anglo-Frisian Brightening and deliver `wadan`, not fronted `wæden`-type outputs [Germanic/data/germanic-aligned-final.tsv:1303-1303; Germanic/docs/DEV_NOTES.md:21745-21749]. The surviving DEV_NOTES material is therefore mostly **shared A-restoration debugging history**, not a bespoke `wade` dossier, and the slice needs to keep that shared-history status visible rather than overstating row-specificity.

The distinction among `PROTO`, `PROTOFORM`, and `COUNTERPART` is especially important here because the file history repeatedly blurred them during debugging. `PROTO` is the comparative/project proto label for the cognate set; `PROTOFORM` is the OE-facing derivational input the FST actually consumes; `COUNTERPART` is the attested OE target selected for the row. In the current TSV, `PROTO` and `PROTOFORM` happen to be the same string, `*wádaną`, but they are not conceptually the same field. `COUNTERPART = wadan` is the normalized OE infinitive. Intermediate derivational stages such as `*wædaną` and `*wadaną`, and the later engineering probe `*wadăną`, are **not** counterparts; they are either internal sound-change stages or superseded debugging inputs [Germanic/data/germanic-aligned-final.tsv:1303-1303; Germanic/docs/DEV_NOTES.md:9500-9510,21745-21749].

The handbook baseline is straightforward and should remain explicit in later work. Ringe-Taylor formulate the rule as: “those stressed *æ which were immediately followed by a single or geminate consonant or sC-cluster which was in turn followed by a back vowel became a” [docs/references/ringe_taylor_linguistic_history_vol2.txt:10990-10995; @RingeTaylor2014, §6.3.1]. Campbell gives the same generalization in paradigm terms: `æ` and `a` alternate, with `a` in open syllables “when a back vowel (a, o, u) follows” [docs/references/campbell_old_english_grammar.txt:4698-4704; @Campbell1959, §157]. Luick is even more valuable for this exact lexeme because he lists `wadan` among the ordinary open-syllable A-restoration examples: “*hara, faran, ... macian, wadan, ... grafan*” [docs/references/luick_historische_grammatik.txt:10180-10190; @Luick1914, §161]. Those citations support the current row as a textbook restoration outcome rather than a patched exception.

The important project-history complication is that DEV_NOTES temporarily explored a different encoding. In March 2026 the file rewrote several strong-verb infinitives from `-aną` to `-ăną`, including `*wadaną → *wadăną`, because that local change seemed to fix outputs like `wadăną → wadan ✓ (was wæden)` [Germanic/docs/DEV_NOTES.md:9497-9512]. But that workaround was not kept as row policy. Later DEV_NOTES explicitly reverses the premise behind that migration: “The current TSV has `*bákaną` with plain `a` for exactly this reason” and the same class list explicitly includes `wádaną`; these infinitives “rely on the plain `a` in the infinitival suffix to trigger OEARestoration” [Germanic/docs/DEV_NOTES.md:21745-21749]. For row 2266, that later statement is the governing authority: the live row keeps plain `-aną`, and the earlier breve-marked form survives only as superseded debugging archaeology.

DEV_NOTES also preserves the narrower diagnostic point that earlier wrong `wæden`-type outputs were not evidence of a rival OE lemma. They were modelling failures caused by infinitives being treated too much like participles. One March results block still records `*wadaną → wadan ✓ (was wæden)` [Germanic/docs/DEV_NOTES.md:10087-10090]. A later explanatory note makes the contrast explicit: “The nasalization fix ... was tested on **infinitives** (which worked correctly: `bacan`, `grafan`, `wadan`, etc.). The bug only affects **participles**” [Germanic/docs/DEV_NOTES.md:10204-10205]. That distinction matters for this slice because it keeps `wadan` as the stable infinitival target while labeling `wæden` as a diagnostic implementation error, not a competing counterpart.

The present row therefore looks current and internally coherent, but the documentary basis is mixed in genre. The strongest row-relevant DEV_NOTES anchors are shared notes about the A-restoration system, not a `wade`-only memorandum. That is enough to support the live row, but later reporting should say so plainly: this is a regular restored infinitive with explicit literature support, plus a well-documented history of superseded `-ăną` debugging.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1649-1705

- Source heading: `A-Restoration Fix (2026-02-06)`
- Source line or section hint: `lines 1649-1705`
- Status: `current_but_shared`
- Issue tags: `a_restoration_context`; `chronology_fix`; `infinitives`
- Recommended next use: `cite_as_shared_technical_background`
- Shared with row IDs: `1934`; `2046`; `2268`; `2272`; other A-restoration rows

This is the first still-current technical fragment that matters for row 2266. It records the repair of the broken A-restoration rule context and the chronology change that moved apocope after restoration [Germanic/docs/DEV_NOTES.md:1649-1666]. Crucially for infinitives like `wadan`, the same section also says the trigger environment was expanded where “A-restoration should still apply (infinitives, agent nouns, etc.)” [Germanic/docs/DEV_NOTES.md:1702-1704]. The fragment does not name `wadan`, so it should not be oversold as a lexeme-specific anchor, but it is still part of the current explanation for why a regular Class VI infinitive can now stay on plain `-aną`.

### DEV_NOTES:line-21729-21755

- Source heading: `§17.10.11 — Phase 1d (Role 1) research findings: breve is NOT an engineering tag; rescope`
- Source line or section hint: `lines 21729-21755`
- Status: `current`
- Issue tags: `current_row_policy`; `protoform_encoding`; `class_vi_infinitives`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs: `1934`; `2046`; `2268`; `2272`; `2292`

This is the governing current-policy fragment for row 2266. DEV_NOTES rejects the proposed bulk migration from plain `a` to breve `ă` and says the earlier assumption was “wrong” because the breve/plain contrast is doing real phonological work in the A-restoration/fronting system [Germanic/docs/DEV_NOTES.md:21731-21736]. The decisive lines are the Class VI probe results and the follow-up prose: the current TSV keeps plain `a`, and the affected infinitives explicitly include `wádaną`; they “rely on the plain `a` in the infinitival suffix to trigger OEARestoration,” while the trigger set “includes `{*a}` but not `{*ă}`” [Germanic/docs/DEV_NOTES.md:21742-21749]. For future indexing, this is the strongest DEV_NOTES anchor because it directly explains the live row's present `PROTOFORM`.

### DEV_NOTES:line-3146-3151

- Source heading: `Derivation / Impact`
- Source line or section hint: `lines 3146-3151`
- Status: `current`
- Issue tags: `verification_history`; `trigger_set_correction`; `wadan_named`
- Recommended next use: `secondary_index_anchor`
- Shared with row IDs: `1934`; `2046`; `2272`

This short verification fragment matters because it shows `wadan` remained correct after a later tightening of the A-restoration trigger logic. DEV_NOTES removes fronted `{*æ}` from the trigger logic in the water fix and then reports: “All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct” [Germanic/docs/DEV_NOTES.md:3146-3151]. That sentence is not a full lexeme analysis, but it is valuable as compact current evidence that row 2266 depends on the repaired **regular** trigger environment rather than on the abandoned over-broad hack.

### DEV_NOTES:line-9497-9512

- Source heading: `Changes made / Results (targeted forms)`
- Source line or section hint: `lines 9497-9512`
- Status: `superseded`
- Issue tags: `breve_workaround`; `wæden_bug`; `project_history`
- Recommended next use: `preserve_as_superseded_history`
- Shared with row IDs: `1934`; `2046`; `2268`; `2272`; `2292`

This fragment preserves the abandoned workaround in the clearest row-local form. DEV_NOTES rewrote five strong-verb infinitives, including `*wadaną → *wadăną`, and then celebrated the targeted result `wadăną → wadan ✓ (was wæden)` [Germanic/docs/DEV_NOTES.md:9498-9512]. For row 2266 that history should be retained, but only under a superseded label. It explains where the stale `*wadăną` idea came from, yet it no longer supports the live row because the later §17.10.11 note explicitly restores plain `-aną` as policy.

### DEV_NOTES:line-10087-10090 and line-10204-10205

- Source heading: `Fixed forms (strong verb infinitives)` / `Why This Wasn't Caught Earlier`
- Source line or section hint: `lines 10087-10090, 10204-10205`
- Status: `current_diagnostic`
- Issue tags: `infinitive_vs_participle`; `diagnostic_scope`; `wæden_not_counterpart`
- Recommended next use: `cite_when_explaining_old_wrong_output`
- Shared with row IDs: `1934`; `2046`; `2268`; `2272`

These lines are useful because they preserve both the repaired output and the scope of the bug. The first block lists `*wadaną → wadan ✓ (was wæden)` among the fixed strong-verb infinitives [Germanic/docs/DEV_NOTES.md:10087-10090]. The second then explains the remaining problem precisely: the infinitives already worked, and “The bug only affects **participles**” [Germanic/docs/DEV_NOTES.md:10204-10205]. For row 2266 this is the safest place to explain why `wæden` should be treated as a modelling artifact rather than as evidence against `COUNTERPART = wadan`.

## Superseded or diagnostic material

- The main superseded material is the March 2026 `-ăną` workaround. It was a real project phase and did produce `wadan` locally, but the later §17.10.11 note explicitly rejects the assumption behind it and restores plain-suffix `a` as the correct current encoding for this class [Germanic/docs/DEV_NOTES.md:9497-9512,21729-21755].
- Older `wæden` outputs are diagnostic implementation history, not lexical competition. The row's counterpart did not oscillate between two attested infinitives; rather, the grammar briefly treated infinitives as though participial `-en` behavior should apply to them [Germanic/docs/DEV_NOTES.md:10087-10090,10204-10205].
- The packet should also be used carefully. It contains the needed evidence snippets, but its structure leaves the decisive later plain-`a` policy in background material; the research memo is the necessary corrective because it foregrounds the later rescope and states plainly that `*wadăną` is stale project history [Germanic/docs/lexeme_reports/packets/2266-wade-wadan.md:48-190; Germanic/docs/lexeme_reports/research_memos/2266-wade-wadan.md:33-40,47-50,57-67].

## Open questions for later work

- If a final lexeme report is written, decide whether the best philological quotation is Luick's explicit `wadan` example list or the more abstract Campbell/Ringe-Taylor formulation of the rule. The former is more lexeme-addressable; the latter is better for explaining the phonological mechanism [@Luick1914, §161; @Campbell1959, §157; @RingeTaylor2014, §6.3.1].
- If the row is ever re-indexed, keep the prose explicit that the strongest DEV_NOTES evidence is **shared class evidence** rather than a `wade`-only dossier. That does not weaken the row, but it does affect how confidently one should summarize the note history.
- If later documentation revisits `PROTO` versus `PROTOFORM`, keep the current distinction sharp: both are presently `*wádaną`, but only because the live project analysis wants the same shape both as comparative label and as derivational input. The superseded `*wadăną` form belongs in history sections, not in live metadata.

---
row_id: 2091
concept: last
counterpart: lǣstan
proto: *láistijaną
protoform: *láistijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2091 last / lǣstan

## Current row state

- Live TSV row `2091` is currently `last / lǣstan / *láistijaną / regular`. `PROTO` and `PROTOFORM` coincide; the row carries no live explanatory note; and the row-local source strings are duplicated Wiktionary inheritance provenance rather than a bespoke philological memo [Germanic/data/germanic-aligned-final.tsv:624-624].
- Coverage is explicitly unelevated: `| 2091 | last | lǣstan | regular | no | - | - | - | none |`. In the present workflow this means the row is being sliced even though coverage audit did **not** call for a packet, research memo, or manifest-backed report [Germanic/docs/lexeme_reports/coverage_audit.md:287-287; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` has no entry for row `2091`, for `lǣstan`, or for `*láistijaną`; the current OE exception ledger is still limited to unrelated items such as `*búkkaz`, `*fūri`, and `*táppô` [Germanic/data/oe_known_problems.tsv:1-8].
- Current derivation snapshots are exact and stable. The published/audit OE trace records `PROTO: *láistijaną`, `EXPECTED: lǣstan`, `OUTPUTS: lǣstan`, with the operative path `PWGmc Ai Monophthongization: *lāstijaną` > `OE Heavy Syllable Nasal Apocope: *lāstijan` > `OE Secondary Nasalization: *lāstijąn` > `Sievers Law Syncope: *lāstjąn` > `OE I Umlaut: *lǣstjąn` > `OE Weak Tail Reduction: *lǣstjan` > `OE J Loss After Heavy: *lǣstan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2640-2658; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2912-2924].
- The full trace shows the same result in more granular rule order: almost every earlier NWGmc/OE rule is `[no-change]` until the heavy weak-verb sequence fires, and the derivation closes with `OldEnglishRemoveStars: lǣstan` and `OldEnglishSurface [no-change]: lǣstan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17519-17633].

## Development-note summary

No dedicated row-specific prose block for `2091 last / lǣstan` survives in `DEV_NOTES.md`. The row therefore has to be documented conservatively from shared-but-lexeme-explicit Sievers'-Law material plus the current exact-match derivation trace, not from a bespoke `lǣstan` problem essay [Germanic/docs/DEV_NOTES.md:8763-9044].

The current working position is straightforward. `PROTO = *láistijaną` and `PROTOFORM = *láistijaną` are the live project inputs; `COUNTERPART = lǣstan` is the attested OE target; and the row is treated as a **heavy-stem Class I weak verb**, not as a paradigm-cell substitution or a split-proto case [Germanic/data/germanic-aligned-final.tsv:624-624; Germanic/docs/DEV_NOTES.md:8989-9007]. DEV_NOTES' governing March decision is explicit that `Heavy-stem Class I weak verbs need *-ijăną`, and it preserves the Ringe-Taylor wording that `the sequence *-CijV- was syncopated to *-CjV-` [Germanic/docs/DEV_NOTES.md:8770-8773; Germanic/docs/DEV_NOTES.md:8795-8805]. The live trace for this row then shows exactly that sequence of events: after `*lāstijąn`, syncope yields `*lāstjąn`, i-umlaut gives `*lǣstjąn`, and post-heavy `j` loss gives `lǣstan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17582-17614].

The strongest surviving philological support is still shared-background rather than row-specific, but it names the lexeme directly. DEV_NOTES preserves the Ringe-Taylor entry ``*laistijăną`` | ``*laistijana`` | `lǣstan` | `p.231: "PGmc *laistijana 'to follow'"`, and then classifies ``*laistijăną`` as root `laist- (CVVCC) | heavy | R/T p.231` under the rule `A heavy-stem Class I weak verb should have *-ijăną (Sievers' Law)` [Germanic/docs/DEV_NOTES.md:8974-8981; Germanic/docs/DEV_NOTES.md:8989-9007]. That is enough to anchor the row's present protoform, even though no row-specific DEV_NOTES narrative survives.

Because the live snapshots already derive the OE form exactly and no exception ledger entry exists, this row should be described as **current regular support**, not as a hidden rescue or unresolved mismatch. The only substantial caution is documentary: older project materials used the pre-March notation `*laistjăną`, but DEV_NOTES later superseded that notation when the project adopted PGmc `*-ij-` inputs for heavy Class I weak verbs [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:624-624; Germanic/docs/DEV_NOTES.md:8717-8739; Germanic/docs/DEV_NOTES.md:8907-8930].

## Relevant DEV_NOTES fragments

### DEV_NOTES fragment A

- Source heading: `DECISION UPDATE (2026-03-13): Adopting PGmc Input Notation`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8763-8845`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `sievers_law`; `pgmc_input_notation`; `heavy_class_i_weak_verb`; `cij_syncope`
- Recommended next use: `cite when explaining why the row keeps heavy-stem *-ij- rather than bare *-j-`
- Shared-with rows if relevant: `1961`; `2025`; `2064`; `2098`; other heavy Class I weak verbs

This is shared background, not a bespoke `lǣstan` block, but it is the governing doctrinal note for the row. DEV_NOTES says the project is adopting **PGmc** rather than PWGmc input notation and therefore that `Heavy-stem Class I weak verbs need *-ijăną`, the grammar must accept `*-ij-`, and later sound changes must account for the reduction to `*-j-` [Germanic/docs/DEV_NOTES.md:8767-8773]. It then preserves the primary-source formulation from Ringe and Taylor: `the sequence *-CijV- was syncopated to *-CjV-`, illustrated there with `*sōkijană ... > PWGmc *sōkijan > *sōkjan > OE sēċan` [Germanic/docs/DEV_NOTES.md:8795-8805]. For row `2091`, this fragment is **shared-background-only but still current**, because the live derivation `*lāstijąn > *lāstjąn` is precisely the type of syncope this note was added to justify [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17583-17585].

### DEV_NOTES fragment B

- Source heading: `Sievers' Law Implementation Status (2026-03-13)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8907-8930`
- Fragment type: `lexeme_explicit_shared_support`
- Status: `current substance; older literal row spelling`
- Issue tags: `implementation_history`; `protoform_cleanup`; `tsv_update`; `old_vs_new_notation`
- Recommended next use: `cite when documenting the row's older *laistjăną notation as superseded project history`
- Shared-with rows if relevant: `1963`; `2010`; `2064`; `2098`; other verbs updated in the same sweep

This fragment is the clearest surviving row-explicit record of the notation cleanup. DEV_NOTES says the grammar change `Added *-ijăną pattern` and `Added SieversLawSyncope rule`, and that the TSV `Updated ALL heavy-stem Class I weak verbs to use *-ijăną notation` [Germanic/docs/DEV_NOTES.md:8907-8913]. In the lexeme table it names this row directly as ``*laistjăną`` → ``*laistijăną`` with source `R/T p.231` [Germanic/docs/DEV_NOTES.md:8915-8925]. The spelling here is unaccented and older than the live acute-marked row form `*láistijaną`, so the fragment should be treated as **current in substance but not as the exact live orthographic string** [Germanic/data/germanic-aligned-final.tsv:624-624].

### DEV_NOTES fragment C

- Source heading: `Source Attestation of *-ijăną Forms (2026-03-13)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8972-9007`
- Fragment type: `lexeme_explicit_shared_support`
- Status: `current`
- Issue tags: `ringe_taylor`; `direct_quote`; `stem_weight`; `attestation`
- Recommended next use: `cite as the strongest surviving philological support for the row's current protoform`
- Shared-with rows if relevant: `1963`; `2010`; `2064`; `2098`; all heavy *-ijăną verbs cited in the same March tables

This is the strongest surviving DEV_NOTES evidence for the row. DEV_NOTES preserves the exact Ringe-Taylor line ``*laistijăną`` | ``*laistijana`` | `lǣstan` | `p.231: "PGmc *laistijana 'to follow'"` [Germanic/docs/DEV_NOTES.md:8976-8981]. Immediately below, it states the general criterion `A heavy-stem Class I weak verb should have *-ijăną (Sievers' Law)` and places ``*laistijăną`` in the heavy-stem list as `laist- (CVVCC) | heavy | R/T p.231` [Germanic/docs/DEV_NOTES.md:8989-9007]. This fragment is not row-specific in form, but it is lexeme-explicit and still current, so it should carry the main evidential weight for why `PROTO/PROTOFORM` remain `*láistijaną`.

### DEV_NOTES fragment D

- Source heading: `CVVC Stems and Sievers' Law: The *baug- vs *straw- Distinction`
- Source line hint: `Germanic/docs/DEV_NOTES.md:9098-9110`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `stem_structure`; `vvc_plus_c`; `weight_diagnosis`; `contrast_case`
- Recommended next use: `cite only when the row's heavy status needs explicit structural justification`
- Shared-with rows if relevant: `1963`; `2098`; `2152`; other diphthongal heavy stems

This fragment is a shared structural clarification rather than row-specific commentary, but it names the lexeme directly and can be reused when the row's stem weight is questioned. DEV_NOTES contrasts true VVC+C stems with special `-awj-` cases and lists `*laist- | ai.st | HEAVY → -ijăną | R/T p.231` beside `*baug-` and `*laid-` [Germanic/docs/DEV_NOTES.md:9100-9105]. For row `2091`, the practical value is limited but real: it shows that the project did not assign `*-ij-` here by loose analogy alone; it classified `laist-` as a normal heavy diphthongal stem.

## Superseded or diagnostic material

- The pre-decision March note that treated heavy verbs under post-leveling `-jăną` notation is now superseded for this row. It explicitly listed ``*laistjăną`` in the table of heavy verbs using bare `-jăną`, but the same block is itself marked `SUPERSEDED` immediately after the PGmc-notation decision [Germanic/docs/DEV_NOTES.md:8717-8747]. For row `2091`, that older table is useful only as project-history evidence for why older files may still show `*laistjăną` [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:623-625].
- The backup TSV spelling `*laistjăną` and DEV_NOTES' unaccented March spellings `*laistjăną`, `*laistijăną` are superseded literal forms, not competing etyma. The substantive surviving claim is the heavy-verb `-ij-` analysis, while the live row metadata now uses acute-marked `*láistijaną` [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:624-624; Germanic/docs/DEV_NOTES.md:8924-8924; Germanic/data/germanic-aligned-final.tsv:624-624].
- The current exact-match derivation trace is **diagnostic support**, not the same thing as philological attestation. It proves that the present FST derives `lǣstan` cleanly from the row's current protoform, but the linguistic justification for using `*láistijaną` still comes from the shared DEV_NOTES/Ringe-Taylor material above [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2640-2658; Germanic/docs/DEV_NOTES.md:8972-9007].

## Open questions for later work

- If this row ever receives a packet or final report, keep the evidential hierarchy explicit: no row-specific DEV_NOTES block survives, so the note should continue to distinguish **shared-background-only** support from **lexeme-explicit shared** support rather than overstating the dossier strength [Germanic/docs/DEV_NOTES.md:8763-9007].
- If quotation practice is standardized later, decide whether older DEV_NOTES spellings like ``*laistijăną`` should always be reproduced verbatim and glossed as earlier project notation, or silently normalized in prose to live `*láistijaną`. The slice should not blur those as if they were different proto analyses [Germanic/docs/DEV_NOTES.md:8924-8924; Germanic/data/germanic-aligned-final.tsv:624-624].
- A later semantic audit may want to note that the preserved primary-source gloss is `"PGmc *laistijana 'to follow'"` while the row's concept label is `last`; no row-specific DEV_NOTES discussion survives to explain that semantic packaging, and it is not presently a derivational problem [Germanic/docs/DEV_NOTES.md:8981-8981; Germanic/data/germanic-aligned-final.tsv:624-624].

---
row_id: 2316
concept: "lick (3sg)"
counterpart: liccaþ
proto: "*likkōną"
protoform: "*líkkōθi"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2316-lick-(3sg)-liccaþ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/notable_findings.md
  - Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md
current_status: current_shared_weak_class_ii_3sg_support_plus_lick_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2316 lick (3sg) / liccaþ

## Current row state

- The live TSV row is `2316 | lick (3sg) | liccaþ | PROTO *likkōną | PROTOFORM *líkkōθi | DERIVATION_CLASS late_analogy`, with the current row note: `Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ. No i-umlaut: 3sg ending never had -j-. Root has cc from WGmc gemination.` [Germanic/data/germanic-aligned-final.tsv:1477-1477]
- This row is a **paradigm-cell companion**, not the lick-family lemma row. The ordinary OE lemma remains row `2099 | lick | liccian | *líkkōjaną`, and the paired imperative companion is row `2315 | lick (iptv.2sg) | licca | *líkkô`; row `2316` isolates the non-`j` 3sg present indicative cell `*líkkōθi -> liccaþ` [Germanic/data/germanic-aligned-final.tsv:654-654,1476-1477; Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md:21-38; Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:13-14,67-83]
- PROTO / PROTOFORM / COUNTERPART must stay separate here. `PROTO *likkōną` is the row’s current lexeme-family/stem label in the TSV, `PROTOFORM *líkkōθi` is the selected 3sg cell input, and `COUNTERPART liccaþ` is the OE finite target for that one cell rather than for the whole lexeme [Germanic/data/germanic-aligned-final.tsv:1477-1477; Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md:61-72]
- Coverage bookkeeping still treats this as an uncovered required row: `coverage_audit.md` lists row `2316` under required rows with no report, `report_manifest.tsv` has no manifest entry for it, and `oe_known_problems.tsv` has no lick-family 3sg problem entry [Germanic/docs/lexeme_reports/coverage_audit.md:185-185; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8]
- The current published derivation trace is clean and row-specific: `# lick (3sg) / PROTO: *líkkōθi / EXPECTED: liccaþ / OUTPUTS: liccaþ`, with the pathway `PWGmc Early I Apocope: *líkkōθ`, `OE Late O Shortening: *líkkaθ`, orthographic `*líkkaþ`, and surface `liccaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7277-7297]
- Existing packet/memo infrastructure is already aligned with that live state. Both documents treat `liccaþ` as the current row target, keep older `licceþ` expectations as stale project history, and warn that the strongest evidence is project-internal row/cell evidence rather than a separate manuscript dossier for this specific finite form [Germanic/docs/lexeme_reports/packets/2316-lick-(3sg)-liccaþ.md:15-42,49-58; Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md:17-36,86-100]

## Development-note summary

Row `2316` now has genuine **current DEV_NOTES support**, but most of that support is **shared weak-class-II 3sg evidence**, not a dedicated lick-only essay. The decisive current note is the April 2026 correction that reverses the older `-eþ` analysis: “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506]. For this row, that shared note becomes materially row-specific because DEV_NOTES explicitly lists `2316 | licceþ | liccaþ` and repeatedly includes the exact pair `*líkkōθi -> liccaþ` in its correction and test tables [Germanic/docs/DEV_NOTES.md:19596-19602; Germanic/docs/DEV_NOTES.md:19951-19955].

The current cell-level explanation is therefore straightforward and should replace older direct consultation of DEV_NOTES for this row: `*-ōþi` is a non-`j` weak-II 3sg ending; early loss of final `-i` yields `*-ōþ`; late unstressed `*ō` shortening then gives `-aþ`; and the row should **not** be explained through regular i-umlaut. DEV_NOTES says this explicitly: `1. *-ōþi — PGmc 3sg ending (NO -j- in this paradigm cell)`, `2. *-ōþ — early i-apocope deletes final -i`, `3. *-aþ — late unstressed *ō shortening gives -a-`, and “There is **NO i-umlaut** in the 3sg because: the ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19540-19549].

What is **not** cell-specific is the lick-family stem background. The row inherits from the lemma/family treatment that `licc-` is the expected OE stem and that dorsal geminate `*kk` blocks the sporadic `*i > e` lowering seen elsewhere. Current shared analysis treats `liccian` as a negative control: `*liccian (velar geminate *-kk-): blocking ✓` [Germanic/docs/analysis/notable_findings.md:1065-1080]. That family background is relevant because it explains why older `liċceþ` / `lecca` states are implementation history rather than philological rescue, but it is **not** the reason row `2316` has `-aþ`; that ending is supported independently by the shared weak-II 3sg correction [Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md:34-38,78-94; Germanic/docs/DEV_NOTES.md:19501-19549].

The row should therefore be described narrowly as a **regular non-`j` 3sg cell inside a lexeme family whose lemma row is analogically remodeled elsewhere**. `DERIVATION_CLASS = late_analogy` still reflects the project’s decision to encode a selected finite cell alongside the lemma row, but the current DEV_NOTES record does **not** treat `liccaþ` itself as a live mismatch or a special lick-only analogy [Germanic/data/germanic-aligned-final.tsv:1477-1477; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7277-7297; Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md:93-100].

## Relevant DEV_NOTES fragments

### DEV_NOTES: weak class-II 3sg correction (`§15.1`)

- Source heading: `§15.1: CORRECTION — Weak Class II 3sg Should Be -aþ, Not -eþ`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19497-19602`
- Fragment type: `current_shared_cell_specific`
- Status: `current`
- Issue tags: `weak_class_ii_3sg`; `no_i_umlaut`; `late_unstressed_o_shortening`; `liccaþ_not_licceþ`
- Recommended next use: `cite whenever explaining why row 2316 is now regular at the cell level`
- Shared-with rows if relevant: `2310`, `2312`, `2314`, `2318`

This is the controlling current fragment. DEV_NOTES first quotes the older TSV-style claim that regular phonology gave `-eþ`, then rejects it: “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506]. For row `2316`, that statement is directly applicable because the row’s older expected form was exactly `licceþ`, now replaced by `liccaþ` [Germanic/docs/DEV_NOTES.md:19600-19602].

The most important exact quotations to preserve are Campbell’s and the row-local sound-chain statement copied into DEV_NOTES itself. Campbell is quoted as “forms of weak verbs of Class II, **lufas, -aþ** … (< **-ōsi, -ōþi**)”, and DEV_NOTES immediately adds that there is “**NO i-umlaut** in the 3sg because: the ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19510-19515,19540-19549]. Those quotations are still current and still accurate for this row.

### DEV_NOTES: row-2316 correction/test tables

- Source heading: `### What This Means for Our FST`; `### TSV Corrections Needed`; `### Affected Forms`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19567-19602,19951-19955`
- Fragment type: `current_row_specific_tables`
- Status: `current`
- Issue tags: `row_specific_pair`; `verification`; `tsv_correction_history`; `líkkōθi`
- Recommended next use: `cite as the closest DEV_NOTES equivalent to a row-local acceptance test`
- Shared-with rows if relevant: `2310`, `2312`, `2314`, `2318`, but the `*líkkōθi` line is row-local

These tables are the clearest row-local DEV_NOTES evidence because they name the exact form and exact row. The crucial row-ID line is: `| 2316 | licceþ | liccaþ | Regular *ōθi → -aþ. |` [Germanic/docs/DEV_NOTES.md:19596-19602]. The later affected-forms list then preserves the same target while marking the intervening bug state: ``3. `*líkkōθi → liccaþ` (currently produces `licceþ`)`` [Germanic/docs/DEV_NOTES.md:19951-19955].

These lines matter because they distinguish three different statuses that later readers might otherwise collapse: older TSV expectation `licceþ`, current accepted target `liccaþ`, and a transient implementation state where the grammar still fronted the late `a` incorrectly. For row `2316`, this is materially more useful than generic weak-II background because it shows that the project explicitly repaired this exact row rather than only stating a class-wide rule in the abstract [Germanic/docs/DEV_NOTES.md:19567-19576,19596-19602,19951-19955].

### DEV_NOTES: chronology of late shortening vs. fronting (`§15.2`, `§15.7`, `§15.8`)

- Source heading: `Campbell §355.4`; `Campbell §355 — The Definitive Statement`; `§15.8 Two-Stage *ō Shortening: Early vs Late`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19639-19650,20179-20213,20497-20505`
- Fragment type: `current_diagnostic_implementation_history`
- Status: `current_diagnostic`
- Issue tags: `chronology`; `late_shortening`; `fronting_blocked`; `weak_ii_endings`
- Recommended next use: `cite when explaining why liccaþ is regular without any row-local rescue`
- Shared-with rows if relevant: `2310`, `2312`, `2314`, `2318`

This fragment explains **why** `liccaþ` keeps `-aþ` instead of fronting to `-eþ`. DEV_NOTES quotes Campbell’s chronological statement in full: “**even when shortened late, ō became a**, but that **this a was of too late origin to become æ by Anglo-Frisian fronting** … Thus **ō if shortened early gives OE æ(e), but if shortened late it gives a**” [Germanic/docs/DEV_NOTES.md:20179-20184]. It also repeats the row-relevant consequence that weak-II present forms belong to the late-shortening set: `*-ōsi → -as`, `*-ōþi → -aþ` [Germanic/docs/DEV_NOTES.md:19645-19650,20497-20505].

For row `2316`, this is diagnostic rather than lick-specific philology, but it is still essential. It is the reason the current published trace can stop at `*líkkaθ` and surface as `liccaþ` without any extra analogical repair at the cell level [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7286-7297]. The chronology note should therefore be kept as part of the replacement slice even though it is shared with the other weak-II 3sg rows.

### DEV_NOTES: older class-II paradigm-cell rationale

- Source heading: `Implications for Class II Weak Verbs`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2759-2778`
- Fragment type: `shared_row_rationale_with_partly_superseded_context`
- Status: `mixed`
- Issue tags: `class_ii_paradigm_cells`; `non_j_forms`; `why_companion_rows_exist`
- Recommended next use: `cite only to explain why row 2316 exists as a non-lemma companion row`
- Shared-with rows if relevant: `2315`, `2310`, `2312`, `2314`, `2318`

This older fragment is still worth preserving because it explains the project logic behind rows like `2316`. DEV_NOTES says the weak-II infinitive suffix `*-ōja-` is a morphological innovation and that the “**REGULAR forms (iptv. 2sg, 2sg, 3sg) preserve the original `*-ō-` stem vowel without the `*-ōja-` extension. These are candidates for TSV encoding**” [Germanic/docs/DEV_NOTES.md:2766-2778]. That is still the right high-level rationale for why `*líkkōθi -> liccaþ` is encoded as a separate row beside lemma `*líkkōjaną -> liccian`.

What should **not** be carried forward from the surrounding early note is any older inference that the 3sg cell’s regular OE outcome was necessarily `licceþ`. The reason for creating the row survives; the earlier row-specific target does not [Germanic/docs/DEV_NOTES.md:2761-2778; Germanic/docs/DEV_NOTES.md:19501-19602].

### DEV_NOTES: lick-family geminate-`*kk` warning

- Source heading: `C. Spurious palatalization of geminate *kk (*likkô → liċca vs licca)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2981-2986`
- Fragment type: `family_specific_diagnostic`
- Status: `superseded_but_explanatorily_useful`
- Issue tags: `geminate_kk`; `spurious_palatalization`; `shared_lick_family_history`
- Recommended next use: `cite only as labeled family-level debugging history`
- Shared-with rows if relevant: `2099`, `2315`

This is the one genuinely lick-family-specific DEV_NOTES quotation still worth carrying into the slice. DEV_NOTES says: “**OE palatalization of *k → ċ before front vowels is correct in general, but geminate *kk should NOT be palatalized in this context. The *i in the root is a front vowel, but geminate velars resist palatalization (R/T §6.4.1).**” [Germanic/docs/DEV_NOTES.md:2981-2986]. That remains useful because it explains why older `liċceþ`-type outputs should be read as implementation bugs.

But this support is **family-level only**, not a current cell-level justification for `liccaþ`. It helps explain the stability of `licc-` and why the row stays aligned with lemma `liccian`; it does **not** establish the `-aþ` ending, which is independently supported by the weak-II 3sg correction above [Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md:54-66; Germanic/docs/analysis/notable_findings.md:1065-1080].

## Superseded or diagnostic material

- The early April note at `19381-19486` is now diagnostic, not current authority. It correctly noticed that 3sg `*-ōþi` lacks `-j-`, but it still concluded that the live OE target should be `licceþ` and treated the FST’s `liccoþ` as the main problem. Later DEV_NOTES sections supersede that conclusion by showing that regular weak-II 3sg gives `-aþ`, not `-eþ` [Germanic/docs/DEV_NOTES.md:19381-19449; Germanic/docs/DEV_NOTES.md:19497-19602].
- The February/March class-II exploration and results table are also superseded for this row. They record `likkōθi | liċceþ | licceþ` and the geminate-`*kk` bug history, which is still useful for reconstructing why the family was being watched, but they are not the live philological verdict for row `2316` [Germanic/docs/DEV_NOTES.md:2948-2959,2981-2986].
- The lick-family `*i > e` blocking discussion in `analysis/notable_findings.md` and the companion lemma slice for row `2099` are relevant only as **inherited lexeme background**. They support the stability of `licc-` before geminate `*kk`, but they should not be elevated into cell-specific proof for `liccaþ`; the 3sg ending is justified elsewhere [Germanic/docs/analysis/notable_findings.md:1065-1080; Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md:68-94].
- The existing packet and research memo are accurate secondary scaffolding, not primary authority. They are helpful because they already separate `*likkōną`, `*líkkōθi`, and `liccaþ`, and because they mark stray keyword hits as non-authoritative; however, the primary current evidence still lives in the live TSV, the current DEV_NOTES correction/chronology sections, and the published derivation trace [Germanic/docs/lexeme_reports/packets/2316-lick-(3sg)-liccaþ.md:15-42,49-58; Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md:17-36,120-133].
- No current `oe_known_problems.tsv` entry marks the row as unresolved. Whatever motivated the paradigm-cell workflow originally, the live repo no longer treats `liccaþ` as a tolerated output failure [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7277-7297].

## Open questions for later work

- Should `DERIVATION_CLASS = late_analogy` continue to be read mainly as a **data-model flag for a selected paradigm cell** rather than as a claim that row `2316` itself is still philologically irregular? Current DEV_NOTES and the live trace treat `*líkkōθi -> liccaþ` as regular once the correct cell is chosen [Germanic/data/germanic-aligned-final.tsv:1477-1477; Germanic/docs/DEV_NOTES.md:19501-19549].
- If `index.tsv` is expanded later, should row `2316` receive its own index entry, or should the weak-class-II-3sg correction be indexed once as a **shared note** covering rows `2310/2312/2314/2316/2318`? The strongest evidence here is substantial but mostly shared, so the row currently looks more like a slice-level coverage item than a unique index-worthy note [Germanic/docs/DEV_NOTES.md:19497-19602,20179-20213; Germanic/docs/lexeme_reports/coverage_audit.md:178-185].
- The live TSV still uses `PROTO *likkōną` for this paradigm-cell row while the lemma row uses `*líkkōjaną`. Later cleanup may want to decide whether that stem-level PROTO is a deliberate project shorthand or a candidate for normalization, but the slice should not prejudge that issue now [Germanic/data/germanic-aligned-final.tsv:654-654,1477-1477; Germanic/docs/lexeme_reports/research_memos/2316-lick-(3sg)-liccaþ.md:61-72,124-132].

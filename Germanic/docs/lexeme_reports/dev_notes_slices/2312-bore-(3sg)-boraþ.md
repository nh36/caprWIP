---
row_id: 2312
concept: bore (3sg)
counterpart: boraþ
proto: *burōną
protoform: *búrōθi
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2312-bore-(3sg)-boraþ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/dev_notes_slices/1956-bore-borian.md
current_status: current_shared_weak_class_ii_3sg_support_plus_bore_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2312 bore (3sg) / boraþ

## Current row state

- The live OE row is `2312 | bore (3sg) | boraþ | PROTOFORM *búrōθi | PROTO *burōną | DERIVATION_CLASS late_analogy`, with the current row note: `Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ (Campbell §355.4). No i-umlaut: 3sg ending never had -j-. Forms with -eþ are dialectal.` [Germanic/data/germanic-aligned-final.tsv:1473-1473]
- This is a **paradigm-cell companion row**, not the bore-family lemma row. The lexeme-level citation row remains `1956 | bore | borian | *búrōjaną`, while row `2311` is the paired imperative companion `*búrô → bora`; row `2312` isolates the non-`j` 3sg present indicative cell `*búrōθi → boraþ` [Germanic/data/germanic-aligned-final.tsv:96-96,1472-1473; Germanic/docs/lexeme_reports/dev_notes_slices/1956-bore-borian.md:22-38].
- PROTO / PROTOFORM / COUNTERPART must stay distinct here: `PROTO *burōną` is the row's lexeme-family label, `PROTOFORM *búrōθi` is the project-selected 3sg input, and `COUNTERPART boraþ` is the OE target for that single cell rather than for the whole lexeme [Germanic/data/germanic-aligned-final.tsv:1473-1473; Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:43-53].
- Coverage infrastructure still treats this as an uncovered required row: `coverage_audit.md` lists row `2312` under required late-analogy rows with no report, `report_manifest.tsv` has no manifest entry for it, and `oe_known_problems.tsv` has no bore-family 3sg problem record [Germanic/docs/lexeme_reports/coverage_audit.md:178-181; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is clean and row-specific: `# bore (3sg) / PROTO: *búrōθi / EXPECTED: boraþ / OUTPUTS: boraþ`, with the pathway `PWGmc Early I Apocope: *búrōθ`, `NWGmc U Lowering: *bórōθ`, `OE Late O Shortening: *bóraθ`, then `Old English Orthography: *bóraþ` and `Outcome: boraþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7049-7069].
- The existing packet and research memo already preserve the correct hierarchy for this row: both treat the later weak-II-3sg correction as authoritative, keep older `boreþ` material only as project history, and warn that the row has stronger **project-internal cell support** than direct manuscript-level attestation support [Germanic/docs/lexeme_reports/packets/2312-bore-(3sg)-boraþ.md:15-43,49-97; Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:15-20,37-64,66-70].

## Development-note summary

Row `2312` has genuine **current DEV_NOTES support**, but most of that support is **shared weak-class-II 3sg evidence**, not a bore-specific philological dossier. The decisive current note is the April 2026 correction reversing the old `-eþ` assumption: DEV_NOTES says the weak class II 3sg rows had been analyzed backwards, quotes Campbell's `lufas, -aþ (< -ōsi, -ōþi)` evidence, quotes Ringe/Taylor on class II 3sg `-aþ` with “stable -a-,” and explicitly explains that `*-ōþi` has **no `-j-`** and therefore no basis for regular i-umlaut in this cell [Germanic/docs/DEV_NOTES.md:19497-19549; Germanic/docs/DEV_NOTES.md:20196-20213].

For row `2312`, that shared correction becomes row-local because DEV_NOTES repeatedly names the exact form `*búrōθi → boraþ`. The most useful tables are the correction table `| *búrōθi | boroþ | boreþ ❌ | boraþ ✓ |`, the row-ID table `| 2312 | boreþ | boraþ |`, the post-fix test case `| *búrōθi | boroþ | boraþ |`, and the regression list `*búrōθi → boraþ (currently produces boreþ)` [Germanic/docs/DEV_NOTES.md:19569-19576; Germanic/docs/DEV_NOTES.md:19592-19602; Germanic/docs/DEV_NOTES.md:19704-19710; Germanic/docs/DEV_NOTES.md:19951-19955]. Those are stronger than vague family-level analogies because they directly cover this exact row input/output pair.

The row still needs careful scoping. The repo's bore-family lemma support belongs mainly to `1956 bore / borian`, which documents the analogical infinitive pathway and later transponent-style acceptance of `borian` as the lexeme row [Germanic/docs/lexeme_reports/dev_notes_slices/1956-bore-borian.md:30-38,74-88]. Row `2312` should therefore be described as a **regular workaround cell inside a late-analogy lexeme family**: the lexeme family needed special handling because the citation infinitive is analogically remodeled, but this particular 3sg cell is supported as the regular non-`j` outcome once late unstressed `*ō` shortening is handled correctly [Germanic/docs/DEV_NOTES.md:2759-2778; Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:66-70].

Just as important, the slice must not over-claim the evidence. Current repo materials strongly support `boraþ` as the project's selected OE 3sg present indicative cell, but they do **not** provide a separate bore-specific quotation dossier proving independent manuscript attestation of `boraþ` itself. The strongest evidence is therefore implementation-facing and cell-facing: `*búrōθi` is the chosen input, `boraþ` is the regular modeled output, and older `boreþ` material is now diagnostic history only [Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:55-64,92-104; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7049-7069].

## Relevant DEV_NOTES fragments

### DEV_NOTES: weak class-II 3sg correction (`§15.1`–`§15.2`)

- Source heading: `§15.1: CORRECTION — Weak Class II 3sg Should Be -aþ, Not -eþ` and `§15.2: RESEARCH — Unstressed *ō Shortening: *ō → *a, NOT *o`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19497-19549,19639-19650`
- Fragment type: `current_shared_cell_specific`
- Status: `current`
- Issue tags: `weak_class_ii_3sg`; `no_i_umlaut`; `late_unstressed_o_shortening`; `boraþ_not_boreþ`
- Recommended next use: `cite whenever explaining why row 2312 is now regular at the cell level`
- Shared-with rows if relevant: `2310`, `2314`, `2316`, `2318`

This is the controlling current fragment. DEV_NOTES first quotes the older TSV-style claim that regular phonology gave `-eþ`, then rejects it: “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506]. For this row that matters because `boraþ` is not being defended as a bore-specific analogy; it is being defended as the regular weak-II 3sg reflex of `*-ōþi`.

The same passage preserves the most important exact quotations to carry forward into the slice. Campbell is quoted as “forms of weak verbs of Class II, **lufas, -aþ** … (< **-ōsi, -ōþi**)” and R/T is quoted as saying class II weak 2sg/3sg have “**stable -a-**” [Germanic/docs/DEV_NOTES.md:19510-19515; Germanic/docs/DEV_NOTES.md:19531-19536]. DEV_NOTES then states the sound-change chain explicitly: `*-ōþi` > `*-ōþ` after early `-i` apocope, then `*-aþ` by late unstressed `*ō` shortening, and “There is **NO i-umlaut** in the 3sg because: The ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19540-19549].

### DEV_NOTES: row-2312 correction tables and tests

- Source heading: `### What This Means for Our FST`; `### TSV Corrections Needed`; `### Test Cases`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19567-19602,19704-19710,19951-19955`
- Fragment type: `current_row_specific_tables`
- Status: `current`
- Issue tags: `row_specific_pair`; `verification`; `tsv_correction_history`; `búrōθi`
- Recommended next use: `cite as the closest DEV_NOTES equivalent to a row-local acceptance test`
- Shared-with rows if relevant: `2310`, `2314`, `2316`, `2318`, but the `*búrōθi` line is row-local

These tables are the best row-local DEV_NOTES evidence because they name the exact form repeatedly. The central line is: `| *búrōθi | boroþ | boreþ ❌ | boraþ ✓ |` [Germanic/docs/DEV_NOTES.md:19569-19576]. That line shows both the intermediate pre-fix FST state (`boroþ`), the now-rejected expectation (`boreþ`), and the accepted current target (`boraþ`).

The same section also ties the row directly to TSV repair history: `| 2312 | boreþ | boraþ | Regular *ōθi → -aþ. TSV note was wrong. |` [Germanic/docs/DEV_NOTES.md:19592-19602]. Then the post-fix test table keeps the row visible: `| *búrōθi | boroþ | boraþ |`, and the later regression list remembers the target in the form “`*búrōθi → boraþ` (currently produces `boreþ`)” [Germanic/docs/DEV_NOTES.md:19704-19710; Germanic/docs/DEV_NOTES.md:19951-19955]. Together these passages make the row's project history precise without confusing old `boreþ` diagnostics with the current verdict.

### DEV_NOTES: chronology of late shortening vs. fronting (`§15.7`–`§15.8`)

- Source heading: `Campbell §355 — The Definitive Statement` and `§15.8 Two-Stage *ō Shortening: Early vs Late`
- Source line hint: `Germanic/docs/DEV_NOTES.md:20179-20213,20476-20505`
- Fragment type: `current_diagnostic_implementation_history`
- Status: `current_diagnostic`
- Issue tags: `chronology`; `late_shortening`; `fronting_blocked`; `weak_ii_endings`
- Recommended next use: `cite when explaining why boraþ is regular without any analogical rescue inside the row itself`
- Shared-with rows if relevant: `2310`, `2314`, `2316`, `2318`, plus other late-shortening discussions

This fragment explains **why** `boraþ` is regular once the chronology is right. DEV_NOTES quotes Campbell: “**even when shortened late, ō became a**, but that **this a was of too late origin to become æ by Anglo-Frisian fronting** … Thus **ō if shortened early gives OE æ(e), but if shortened late it gives a**” [Germanic/docs/DEV_NOTES.md:20179-20184]. It then immediately identifies the weak-II endings as belonging to that late-shortening set and repeats Campbell's specific forms `lufas, -aþ` plus R/T's `stable a` wording [Germanic/docs/DEV_NOTES.md:20193-20213].

For row `2312`, the point is not abstract chronology for its own sake. It is the reason `boraþ` should stay `-aþ` rather than being fronted to `boreþ`: the `a` in this ending is late and never enters the Anglo-Frisian fronting window. DEV_NOTES' later two-stage summary states exactly that the late-shortening class includes “Weak II present forms: `*-ōsi → -as`, `*-ōþi → -aþ` (`lufas`, `lufaþ`, `macaþ`)” [Germanic/docs/DEV_NOTES.md:20497-20505]. Bore shares that same cell-level logic even though the example list names `macaþ` rather than `boraþ`.

### DEV_NOTES: early class-II rationale that still matters, but only partly

- Source heading: `Implications for Class II Weak Verbs`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2759-2778`
- Fragment type: `shared_row_rationale_with_partly_superseded_context`
- Status: `mixed`
- Issue tags: `class_ii_paradigm_cells`; `non_j_forms`; `why_companion_rows_exist`
- Recommended next use: `cite only to explain why non-lemma paradigm rows such as 2311/2312 were created`
- Shared-with rows if relevant: `1956`, `2311`, `2310`, `2313`, `2314`, `2315`, `2316`, `2317`, `2318`

This older fragment is still useful for explaining the row's existence. DEV_NOTES states that the analogical infinitive in `*-ōja-` is not the best phonological probe, then says: “The REGULAR forms (iptv. 2sg, 2sg, 3sg) preserve the original `*-ō-` stem vowel without the `*-ōja-` extension. These are candidates for TSV encoding” [Germanic/docs/DEV_NOTES.md:2761-2778]. That rationale still fits row `2312` very well: it is exactly a non-`j` companion cell created because the lemma `borian` belongs to a remodeled infinitival pathway.

What should **not** be carried forward from the surrounding older material is any implication that every early expected form in that exploratory phase remained correct. The rationale for using non-`j` cells survives; the older bore-specific `boreþ` outcome does not [Germanic/docs/DEV_NOTES.md:2761-2778; Germanic/docs/DEV_NOTES.md:2952-2955].

## Superseded or diagnostic material

- The old February results table `| burōθi | boreþ | boreþ | ✓ |` is explicitly superseded for this row. It is useful only as evidence that the project once accepted `boreþ` as regular before the later weak-II-3sg correction overturned that assumption [Germanic/docs/DEV_NOTES.md:2952-2955; Germanic/docs/DEV_NOTES.md:19497-19506].
- The first April discovery note is likewise diagnostic rather than current: it frames the affected forms as `*búrōθi | boroþ | boreþ | -o- not -e-`, which preserves the earlier mistaken expectation that `-eþ` was the correct target [Germanic/docs/DEV_NOTES.md:19381-19392]. That passage still helps reconstruct debugging chronology, but it should never be cited as the live philological verdict.
- The regression note at `§15.5` is current only as **bug history**. It shows that, even after the project had adopted `boraþ` as the correct target, the pipeline temporarily regressed to `boreþ` when `OEWeakTailReduction` fronted the new `a` too late in the cascade [Germanic/docs/DEV_NOTES.md:19974-20003]. This is important implementation context, not evidence for an alternative OE form.
- The bore-family lemma row `1956 bore / borian` remains necessary background but not direct proof for this cell. Its slice explains the analogical infinitive pathway and later transponent policy for `borian`; row `2312` should inherit only the family distinction from that material, not pretend that lemma-level support automatically proves a cell-specific attestation for `boraþ` [Germanic/docs/lexeme_reports/dev_notes_slices/1956-bore-borian.md:30-38,74-88].
- The packet and research memo are accurate secondary scaffolding, not primary authority. They are useful because they already separate `*burōną`, `*búrōθi`, and `boraþ`, and because they mark stray dossier hits as non-authoritative keyword noise; but the primary current evidence still lives in the live TSV, DEV_NOTES correction sections, and the published derivation trace [Germanic/docs/lexeme_reports/packets/2312-bore-(3sg)-boraþ.md:15-43,103-141; Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:15-20,35-40,55-64].

## Open questions for later work

- Should `DERIVATION_CLASS = late_analogy` remain the best label for row `2312` now that DEV_NOTES treats `*búrōθi → boraþ` itself as regular? The label still makes sense at the bore-family level because the lexeme row depends on an analogically remodeled infinitive, but the slice should keep that family-level taxonomy distinct from the cell-level phonology [Germanic/data/germanic-aligned-final.tsv:1473-1473; Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:66-70].
- If `index.tsv` is expanded later, should row `2312` receive its own entry, or should the weak-class-II-3sg correction be indexed once as a **shared note** covering rows `2310/2312/2314/2316/2318`? The evidence is strong, but much of it is shared rather than uniquely bore-specific [Germanic/docs/DEV_NOTES.md:19497-19549,19567-19602,20179-20213; Germanic/docs/lexeme_reports/coverage_audit.md:178-182].
- The memo notes that no built-in paradigm-probe spec currently covers this bore family cell. If that infrastructure is added later, it should keep the lexeme row `*búrōjaną → borian`, the imperative row `*búrô → bora`, and the 3sg row `*búrōθi → boraþ` separate so that lexeme-level and cell-level evidence do not collapse back together [Germanic/docs/lexeme_reports/research_memos/2312-bore-(3sg)-boraþ.md:72-90].

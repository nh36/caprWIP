---
row_id: 2318
concept: "show (3sg)"
counterpart: sċēawaþ
proto: "*skawōną"
protoform: "*skáwōθi"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2318-show-(3sg)-sċēawaþ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2318-show-(3sg)-sċēawaþ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/dev_notes_slices/2186-show-sċēawian.md
current_status: current_shared_weak_class_ii_3sg_support_plus_show_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2318 show (3sg) / sċēawaþ

## Current row state

- The live OE row is `2318 | show (3sg) | sċēawaþ | PROTOFORM *skáwōθi | PROTO *skawōną | DERIVATION_CLASS late_analogy`, with row note `Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ. No i-umlaut: 3sg ending never had -j-. Normalized sċ: Campbell §440.` [Germanic/data/germanic-aligned-final.tsv:1479-1479].
- This row is a **paradigm-cell companion**, not the lemma row for the lexeme. The ordinary show row remains `2186 | show | sċēawian | *skáwōjaną`, and the paired imperative row remains `2317 | show (iptv.2sg) | sċēawa | *skáwô`; row `2318` isolates the non-lemma 3sg indicative cell `*skáwōθi -> sċēawaþ` inside that same family [Germanic/data/germanic-aligned-final.tsv:993-993,1478-1479].
- `PROTO`, `PROTOFORM`, and `COUNTERPART` need to stay separate. `PROTO *skawōną` is the row's family-level label for the non-`j` singular stem set; `PROTOFORM *skáwōθi` is the selected 3sg input; `COUNTERPART sċēawaþ` is the OE target for this one paradigm cell rather than for the lexeme as a whole [Germanic/data/germanic-aligned-final.tsv:1479-1479; Germanic/docs/lexeme_reports/research_memos/2318-show-(3sg)-sċēawaþ.md:46-53].
- Coverage bookkeeping still treats this as an uncovered required row: `coverage_audit.md` lists row `2318` among required late-analogy rows with no report, `report_manifest.tsv` has no row-2318 entry, and `oe_known_problems.tsv` has no surviving show-family 3sg problem entry [Germanic/docs/lexeme_reports/coverage_audit.md:186-187; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is row-specific and clean: `PROTO: *skáwōθi / EXPECTED: sċēawaþ / OUTPUTS: sċēawaþ`, with `PWGmc Early I Apocope: *skáwōθ`, then `OE Aw Long Diphthong: *skḗawōθ`, `OE Sk Palatalization: *ʃḗawōθ`, and `OE Late O Shortening: *ʃḗawaθ` before orthographic `sċēawaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7504-7524].
- Repo-local source material supports the **family-level finite-cell shape**, but not a full simplex 3sg dossier for this exact normalized spelling. `old_english_wiktionary.tsv` gives the lemma `scēawian`, Bright lists simplex `scēawian` with imperative `scēawa`, and Bright also gives prefixed `geond-scēawian ... 3 sg. -sceawað`; this supports the `scēaw- / -awað` pattern while still leaving the exact simplex normalized `sċēawaþ` as a project-normalized reporting form rather than a separately documented dictionary headword [Germanic/data/old_english_wiktionary.tsv:247-247; docs/references/bright_anglo_saxon_reader.vision.txt:24606-24612,20401-20403].

## Development-note summary

The controlling current support for row `2318` is the April 2026 weak-class-II 3sg correction in `DEV_NOTES.md`. That note explicitly rejects the earlier row policy that treated `*-ōθi` as if it should yield `-eþ`: “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506]. The note then quotes Campbell's weak-II paradigm material — “forms of weak verbs of Class II, **lufas, -aþ** ... (< **-ōsi, -ōþi**)” — and Ringe & Taylor's statement that class-II weak present 2sg/3sg have “**stable -a-**” [Germanic/docs/DEV_NOTES.md:19510-19515,19531-19536; @Campbell1959, §355.4; @RingeTaylor2014, p. 80]. For row `2318`, this is genuine **cell-level** support, but it is mostly **shared** with rows `2310/2312/2314/2316` rather than show-specific.

Row `2318` does, however, appear explicitly inside that shared correction. `DEV_NOTES` records the old debugging stage `*skáwōθi | sċēawoþ | sċēaweþ | -o- not -e-`, then later names row `2318` in the TSV correction table: `| 2318 | sċēaweþ | sċēawaþ | Regular *ōθi → -aþ. |` [Germanic/docs/DEV_NOTES.md:19385-19392,19596-19602]. That makes this row stronger than a merely inferred parallel: the project did not just fix the abstract class-II rule and leave show implicit; it directly corrected this exact row from `sċēaweþ` to `sċēawaþ`.

The show-family material must still be scoped carefully. The lemma row `2186` is `*skáwōjaną -> sċēawian`, where the Class II `*-ōjan-` suffix places `*ō` between `*w` and `*j`; later `DEV_NOTES` treats that lemma as a **safe non-problem** in the `*aw+j` audit for exactly that reason [Germanic/data/germanic-aligned-final.tsv:993-993; Germanic/docs/DEV_NOTES.md:26631-26632,26680-26681]. Row `2318` inherits that lexeme-family background, but it is not justified by the lemma row alone. Its own `PROTOFORM` is the non-`j` cell `*skáwōθi`, and its current trace shows the expected cell-specific path `*skáwōθi > *skáwōθ > *skḗawōθ > *ʃḗawōθ > *ʃḗawaθ > sċēawaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7504-7524].

The main show-specific caveat is philological rather than transducer-facing. Repo-local sources strongly support the lemma `scēawian`, the imperative `scēawa`, and the broader weak-II finite-cell pattern `-sceawað`, but the local evidence reviewed here does **not** amount to a dedicated simplex citation for bare 3sg `scēawað` under the simplex headword itself [docs/references/bright_anglo_saxon_reader.vision.txt:24606-24612,20401-20403]. The slice should therefore say explicitly that the strongest support for row `2318` is: (i) shared current class-II 3sg analysis, (ii) a direct project correction naming row `2318`, and (iii) show-family / source-side support for the `scēaw- / -awað` pattern. It should **not** overstate the evidence as if there were a separate row-local manuscript dossier for the exact normalized spelling `sċēawaþ`.

That is also why `DERIVATION_CLASS = late_analogy` should be read cautiously here. The family needed non-lemma paradigm-cell rows because the infinitive in `*-ōja-` is not the best direct phonological probe for regular Class II singular endings [Germanic/docs/DEV_NOTES.md:2761-2778]. But on current evidence the **3sg cell itself** is not being kept because `sċēawaþ` is a live irregular rescue. It is being kept because `PROTO *skawōną`, `PROTOFORM *skáwōθi`, lemma row `2186`, and companion row `2317` together make a three-layer family record in which the 3sg cell now looks **regular once that cell is selected** [Germanic/data/germanic-aligned-final.tsv:993-993,1478-1479].

## Relevant DEV_NOTES fragments

### DEV_NOTES: weak class-II 3sg correction (`§15.1`–`§15.2`)

- Source heading: `§15.1: CORRECTION — Weak Class II 3sg Should Be -aþ, Not -eþ` and `§15.2: RESEARCH — Unstressed *ō Shortening: *ō → *a, NOT *o`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19497-19549,19639-19650`
- Fragment type: `current_shared_cell_specific`
- Status: `current`
- Issue tags: `weak_class_ii_3sg`; `no_i_umlaut`; `late_unstressed_o_shortening`; `sċēawaþ_not_sċēaweþ`
- Recommended next use: `cite whenever explaining why row 2318 is regular at the cell level`
- Shared-with rows if relevant: `2310`, `2312`, `2314`, `2316`

This is the controlling current fragment. DEV_NOTES first quotes the earlier row logic only to overturn it: “Regular phonology: `*ōθi → -eþ` (i-umlaut of `*ō`).” It then states, “**This is BACKWARDS.** The actual regular outcome is `-aþ`” [Germanic/docs/DEV_NOTES.md:19501-19506]. The same section preserves the most useful quotations to carry forward: Campbell's “forms of weak verbs of Class II, **lufas, -aþ** ... (< **-ōsi, -ōþi**)” and R/T's statement that class II weak present 2sg/3sg have “**stable -a-**” [Germanic/docs/DEV_NOTES.md:19510-19515,19531-19536; @Campbell1959, §355.4; @RingeTaylor2014, p. 80].

For row `2318`, the most important row-facing sentence is the one blocking the old `-eþ` analysis: “There is **NO i-umlaut** in the 3sg because: the ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19540-19549]. That is a direct answer to the older `sċēaweþ` expectation and should be treated as current, not merely diagnostic.

### DEV_NOTES: row-2318 correction history and acceptance tables

- Source heading: `### The Problem`; `### What This Means for Our FST`; `### TSV Corrections Needed`
- Source line hint: `Germanic/docs/DEV_NOTES.md:19385-19392,19567-19602`
- Fragment type: `mixed_row_specific_history_and_current_table`
- Status: `mixed — current only in the later correction table`
- Issue tags: `row_specific_pair`; `sċēaweþ_history`; `tsv_correction`; `project_history`
- Recommended next use: `cite current table as row-local evidence; keep earlier table as history only`
- Shared-with rows if relevant: `2310`, `2312`, `2314`, `2316`

This pair of fragments is especially useful because it names the exact show 3sg form in both its superseded and current states. The earlier regression table logs the pre-fix project assumption: `| *skáwōθi | sċēawoþ | sċēaweþ | -o- not -e- |` [Germanic/docs/DEV_NOTES.md:19385-19392]. That belongs in this slice only as history of the problem.

The later table is current and row-local: `| 2318 | sċēaweþ | sċēawaþ | Regular *ōθi → -aþ. |` [Germanic/docs/DEV_NOTES.md:19596-19602]. For row `2318`, that line is the closest thing in surviving DEV_NOTES to an explicit acceptance test: it records the old target, the corrected target, and the project rationale in one place.

### DEV_NOTES: chronology of late `*ō` shortening vs. fronting (`§15.7`–`§15.8`)

- Source heading: `Campbell §355 — The Definitive Statement` and `Late Shortening`
- Source line hint: `Germanic/docs/DEV_NOTES.md:20179-20213,20497-20505`
- Fragment type: `current_diagnostic_implementation_history`
- Status: `current_diagnostic`
- Issue tags: `chronology`; `late_shortening`; `fronting_blocked`; `weak_ii_endings`
- Recommended next use: `cite when explaining why -aþ is regular rather than analogically rescued`
- Shared-with rows if relevant: `2310`, `2312`, `2314`, `2316`

This fragment explains why the current target is `sċēawaþ`, not `sċēaweþ`. DEV_NOTES quotes Campbell: “**even when shortened late, ō became a**, but that **this a was of too late origin to become æ by Anglo-Frisian fronting** ... Thus **ō if shortened early gives OE æ(e), but if shortened late it gives a**” [Germanic/docs/DEV_NOTES.md:20181-20184; @Campbell1959, §355]. It then applies that directly to weak-II present forms: `*-ōsi → -as`, `*-ōþi → -aþ` [Germanic/docs/DEV_NOTES.md:20497-20505].

For this row, the value of the fragment is not that it mentions `show` by name, but that it explains the ending chronology behind the trace `*ʃḗawōθ > *ʃḗawaθ`. The `a` of `sċēawaþ` is a **late-shortening** result and therefore never enters the earlier fronting window that would have produced `e`.

### DEV_NOTES: show-family `*aw > ēaw` rule and safety sweep

- Source heading: `OEAwLongDiphthong: PGmc *aw → OE ēaw before vowels (Campbell §272)` and `§17.10.35 ... wrong suffix etymology`
- Source line hint: `Germanic/docs/DEV_NOTES.md:3625-3650,26631-26639`
- Fragment type: `current_show_family_background_plus_mixed_history`
- Status: `mixed`
- Issue tags: `oe_aw_long_diphthong`; `show_family`; `aw_sequence`; `row_scope`
- Recommended next use: `cite for stem history and family alignment, not as sole proof of the 3sg ending`
- Shared-with rows if relevant: `2186`, `2317`

The `OEAwLongDiphthong` section gives the current vowel rule needed for the stem: `PGmc *aw before a following vowel -> OE ēaw` [Germanic/docs/DEV_NOTES.md:3625-3640]. Inside the same note, the row-local line `*skawōθi → sċēaweþ (expected scēaweþ)` is now stale as a 3sg expectation, but it remains useful as evidence that the project had already fixed the `ēaw` stem before it fixed the weak-II 3sg ending [Germanic/docs/DEV_NOTES.md:3647-3650].

The later safety sweep is the current show-family background note. It marks the lemma row `2186` as safe because `*ō` intervenes between `*w` and `*j`, and it separately logs `2318 *skáwōθi sċēawaþ sċēawaþ ✓ Class II 3sg; *ō intervenes` [Germanic/docs/DEV_NOTES.md:26631-26639]. This is useful because it keeps the show family out of the real `*aw+j` bug bucket, but it should still be labeled **shared background**: it helps explain why the `sċēaw-` stem is stable, not why `*-ōθi` specifically yields `-aþ`.

## Superseded or diagnostic material

- The oldest show-family mismatch note is purely diagnostic now: `*skawô → sċawa (expected scēawa), *skawōθi → sċaweþ (expected scēaweþ)` [Germanic/docs/DEV_NOTES.md:2987-2993]. Its still-usable sentence is only the notation warning that `/sk/ > /ʃ/` is the ordinary OE shift written `<sc>`, so project `sċ-` is editorial normalization rather than a separate attested grapheme [Germanic/docs/DEV_NOTES.md:2991-2993].
- The February exploratory class-II table `*skawōjăną -> sċaweian -> scēawian` and the surrounding rationale for using non-lemma singular cells remain valuable as **row-creation history**, not as the current 3sg analysis [Germanic/docs/DEV_NOTES.md:2761-2778,2821-2834]. That older stage explains why rows `2317/2318` exist, but not why the corrected 3sg target is now `sċēawaþ`.
- The early April regression table line `*skáwōθi | sċēawoþ | sċēaweþ` should be kept only as problem history [Germanic/docs/DEV_NOTES.md:19385-19392]. The live trace and later correction table have superseded it [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7504-7524; Germanic/docs/DEV_NOTES.md:19596-19602].
- The row packet and research memo are current **secondary scaffolding**, not primary authority. They are useful because they already separate lemma `*skáwōjaną`, imperative `*skáwô`, and 3sg `*skáwōθi`, and because they explicitly warn that Bright's `-sceawað` evidence is pattern-level rather than a simplex row-local dossier [Germanic/docs/lexeme_reports/packets/2318-show-(3sg)-sċēawaþ.md:15-20,57-70; Germanic/docs/lexeme_reports/research_memos/2318-show-(3sg)-sċēawaþ.md:37-41,59-63]. But the primary current evidence still lives in the live TSV, DEV_NOTES correction sections, and the published trace.

## Open questions for later work

- Should `DERIVATION_CLASS = late_analogy` continue to be read mainly as a **family-management label** for a non-lemma paradigm row rather than as a claim that row `2318` itself is still philologically irregular? The current row note, correction table, and trace all treat `*skáwōθi -> sċēawaþ` as regular once that cell is chosen [Germanic/data/germanic-aligned-final.tsv:1479-1479; Germanic/docs/DEV_NOTES.md:19596-19602; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7504-7524].
- If `index.tsv` is expanded later, row `2318` probably belongs under a **shared weak-class-II-3sg note** rather than under a show-only indexed note. Most current evidence is shared with rows `2310/2312/2314/2316`, and the show-specific philological support is mostly family-level rather than row-local [Germanic/docs/DEV_NOTES.md:19497-19549,19596-19602; Germanic/docs/lexeme_reports/coverage_audit.md:186-187].
- If the row is ever upgraded beyond slice-only status, the missing ingredient is a stronger simplex 3sg attestation dossier for bare `scēawað` / `sċēawaþ`. Bright's prefixed `-sceawað` evidence is helpful and should be kept, but it is not quite the same thing as a fully row-local simplex citation [docs/references/bright_anglo_saxon_reader.vision.txt:20401-20403,24606-24612].

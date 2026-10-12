---
row_id: 2310
concept: make (3sg)
counterpart: macaþ
proto: *makōną
protoform: *mákōθi
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2310-make-(3sg)-macaþ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2310-make-(3sg)-macaþ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2310 make (3sg) / macaþ

## Current row state

- CONCEPT: `make (3sg)`
- COUNTERPART: `macaþ`
- PROTO: `*makōną`
- PROTOFORM: `*mákōθi`
- DERIVATION_CLASS: `late_analogy`
- Live TSV row: row 2310 currently keeps the lexeme-level proto headword `*makōną` but uses the finite-cell `PROTOFORM = *mákōθi` for the Old English 3sg target `macaþ`; its live note already states the current project position that class-II weak 3sg `*-ōθi` gives `-aþ`, not regular `-eþ`, and that `-eþ` spellings are dialectal [Germanic/data/germanic-aligned-final.tsv:1471-1471].
- Family alignment in the live TSV: the infinitive row 2117 remains a separate lemma-level row (`*mákōjaną` → `macian`), while row 2309 is the imperative-cell companion (`*mákô` → `maca`); row 2310 is therefore a distinct paradigm-cell row rather than a duplicate of the make-lemma slice [Germanic/data/germanic-aligned-final.tsv:725-725,1470-1471].
- Coverage / manifest / known-problems state: `coverage_audit.md` marks row 2310 as a row needing report coverage and notes both `NOTE` and `DERIVATION_CLASS=late_analogy`, but `report_manifest.tsv` still has no row-2310 entry, and `oe_known_problems.tsv` has no make-family entry at all [Germanic/docs/lexeme_reports/coverage_audit.md:178-180; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- Current implementation trace: the published derivation-class snapshot now lands directly on the live target: `*mákōθi` > `*mákōθ` (early `-i` apocope) > `*mækōθ` (AFB) > `*makōθ` (A-restoration) > `*makaθ` (late unstressed `*ō` shortening) > `macaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7339-7359].
- Existing row infrastructure: both the packet and the research memo already separate the three relevant objects — lexeme proto `*makōną`, lemma-level infinitive pathway `*mákōjaną → macian`, and selected 3sg cell `*mákōθi → macaþ` — and both explicitly treat the old `maceþ` story as superseded [Germanic/docs/lexeme_reports/packets/2310-make-(3sg)-macaþ.md:5-23,49-61,179-213; Germanic/docs/lexeme_reports/research_memos/2310-make-(3sg)-macaþ.md:3-13,51-66,68-103].

## Development-note summary

Row 2310 now has **real cell-specific DEV_NOTES support**, but that support is mostly **shared across weak class-II 3sg rows**, not unique to `make`. The decisive current material is the April 2026 correction in DEV_NOTES §15.1–§15.8: it reverses the earlier project claim that regular `*-ōθi` should give `-eþ`, cites Campbell and Ringe/Taylor for regular `-aþ`, and explains that the 3sg cell has no `-j-` and therefore no basis for the old i-umlaut-driven `maceþ` analysis [Germanic/docs/DEV_NOTES.md:19497-19526,19531-19576; Germanic/data/germanic-aligned-final.tsv:1471-1471]. For this row, that is the main **cell-level** evidence.

The row must still keep the lexeme-family distinction explicit. `PROTO` is the comparative/cognate-set verbal headword `*makōną`, but `PROTOFORM` is the selected finite paradigm cell `*mákōθi`, and the OE `COUNTERPART` is the 3sg indicative form `macaþ`, not the lemma `macian` [Germanic/data/germanic-aligned-final.tsv:1471-1471]. The sibling infinitive row 2117 remains the place where the project stores the lemma-level `*mákōjaną → macian` relationship; row 2310 inherits make-family background from that lexeme, but it is not justified by the infinitive row alone [Germanic/data/germanic-aligned-final.tsv:725-725,1471-1471].

The strongest **lexeme-level but not cell-specific** background for row 2310 is the shared A-restoration/class-II material naming `macian` as a canonical restored-`a` verb. DEV_NOTES quotes Campbell §159 on “weak verbs in `*-i-* (< *-ói-*), `lapian, macian, hnappian`” and Ringe/Taylor on class-II verbs always showing retracted `a` rather than `æ`, with `macian` included among the typical examples [Germanic/docs/DEV_NOTES.md:36529-36534]. That material does not by itself prove the 3sg ending `-aþ`; rather, it explains why the make-family stem should pass through `*mak-` rather than stay fronted as `*mæk-/mec-` after Anglo-Frisian brightening, which matches the current 3sg trace `*mækōθ > *makōθ > *makaθ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7350-7359].

Project history matters because row 2310 exists partly to preserve an earlier exploratory workaround. In February 2026 DEV_NOTES proposed using the 3sg present cell as a more regular citation form for class-II weak verbs and explicitly wrote `PGmc *makōθi → OE *maceþ (regular) / macaþ (attested, analogical)` [Germanic/docs/DEV_NOTES.md:2845-2847,2905-2917]. That older claim is now superseded. The current slice should preserve it only as **diagnostic history** explaining why this non-lemma row was created and why `DERIVATION_CLASS` still reads `late_analogy`, not as the live philological verdict [Germanic/docs/DEV_NOTES.md:19497-19526; Germanic/docs/lexeme_reports/coverage_audit.md:178-180].

The current implementation-facing verdict is straightforward. DEV_NOTES' later debugging and fix sequence shows that the issue was not lexical irregularity in `macaþ`, but chronology inside the OE weak-tail pipeline: after early `-i` apocope, late unstressed `*ō` must shorten to `a` in weak-II `*-ōþ(i)` forms, and that new `a` must not be wrongly fronted to `e` [Germanic/docs/DEV_NOTES.md:19639-19650,19750-19766,19974-20002,20436-20505]. The published trace and the packet/memo all agree that the present cascade now handles the row correctly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7339-7359; Germanic/docs/lexeme_reports/packets/2310-make-(3sg)-macaþ.md:17-42; Germanic/docs/lexeme_reports/research_memos/2310-make-(3sg)-macaþ.md:15-36,68-92].

## Relevant DEV_NOTES fragments

### DEV_NOTES: weak class-II 3sg correction (`§15.1` / `§15.2`)

- Source heading: `§15.1: CORRECTION — Weak Class II 3sg Should Be -aþ, Not -eþ` and `§15.2: RESEARCH — Unstressed *ō Shortening: *ō → *a, NOT *o`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:19497-19526,19531-19576,19639-19650`
- Fragment type: `current_shared_cell_specific`
- Status: `current`
- Issue tags: `weak_class_ii_3sg`; `no_i_umlaut`; `late_unstressed_o_shortening`; `macaþ_not_maceþ`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2312`, `2314`, `2316`, `2318`

This is the decisive current fragment for row 2310. DEV_NOTES first quotes the earlier TSV logic only to reject it: “Regular phonology: `*ōθi → -eþ` (i-umlaut of `*ō`). Attested `macaþ` is analogical.” DEV_NOTES then says flatly, “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506].

The most useful direct quotations are the handbook ones copied into the note itself. Campbell §355.4 is quoted as: “forms of weak verbs of Class II, **lufas, -aþ**, -od, -ad (< **-ōsi, -ōþi**, § 331.6)” [Germanic/docs/DEV_NOTES.md:19510-19515]. Ringe/Taylor is then summarized with the direct wording that class-II weak 2sg/3sg endings have “**stable -a-**” and specifically “class II weak pres. 2sg. `-as(t)`, 3sg. `-aþ`” [Germanic/docs/DEV_NOTES.md:19529-19536]. For row 2310 this is the key current cell-specific authority: the 3sg ending itself is regular `-aþ`, and `macaþ` is not being saved by a special make-only analogy.

The same section also gives the row-local sound-change chain in the right shape: `*-ōþi` loses final `-i`, then late unstressed `*ō` shortens to `a`; DEV_NOTES explicitly says there is “**NO i-umlaut** in the 3sg because: the ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19540-19549]. That sentence should be copied forward because it directly blocks the older `maceþ` analysis.

### DEV_NOTES: current make-family A-restoration support (`§17.25` literature table and probes)

- Source heading: literature table inside the A-restoration/class-II discussion; `§17.25.8 Post-fix verification`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:36529-36534,36762-36767`
- Fragment type: `current_shared_lexeme_background`
- Status: `current`
- Issue tags: `make_family`; `class_ii_retracted_a`; `shared_support_not_cell_specific`; `verification`
- Recommended next use: `cite_as_lexeme_background_only`
- Shared with row IDs: `2117`, `2309`, `2205`; broader class-II make-family rows

This fragment is important but should be labeled carefully. It is **not** specific to the 3sg cell; it is shared make-family support inherited from the `macian` dossier space. DEV_NOTES preserves Campbell §159 on “[…] weak verbs in `*-i-* (< *-ói-*), `lapian, macian, hnappian`, &c.” and R/T's stronger statement: “Weak verbs of class II always exhibit retracted `a` rather than `æ` before a non-nasal consonant in a monosyllabic root syllable […]. There are more than fifty examples; the following are typical: `carian`, `talian`, `macian`, `bacian`, `bapian`, `lapian` …” [Germanic/docs/DEV_NOTES.md:36529-36534].

For row 2310 the value of that material is stem-level, not ending-level. It helps explain why the current 3sg trace restores the root to `mak-` after brightening, but it does **not** by itself establish `*-ōθi > -aþ`; that part comes from the weak-II-3sg correction above [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7350-7359].

The associated post-fix probes confirm that the make family is currently stable in the live grammar: DEV_NOTES lists “`*sákōjaną → sacian`, `*mákōjaną → macian` ✓” among successful checks [Germanic/docs/DEV_NOTES.md:36762-36767]. Again, this is inherited lexeme-family verification rather than cell-specific evidence for `macaþ`, but it helps keep the 3sg slice aligned with the existing treatment of `make / macian`.

### DEV_NOTES: late-chronology debugging that now underlies the live trace (`§15.5` / `§15.7` / `§15.8`)

- Source heading: `§15.5 BUG ANALYSIS: Weak II 3sg -aþ → -eþ Regression`; `§15.7 Re-examining the *a vs *ă Solution`; `§15.8 Two-Stage *ō Shortening: Early vs Late`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:19974-20002,20179-20213,20436-20505`
- Fragment type: `current_diagnostic_implementation_history`
- Status: `current_diagnostic`
- Issue tags: `chronology`; `fronting_vs_late_shortening`; `pipeline_fix`; `weak_tail`
- Recommended next use: `cite_when_explaining_why_trace_now_works`
- Shared with row IDs: `2312`, `2314`, `2316`, `2318`, `2121`

This fragment is diagnostic rather than philological, but it is too row-relevant to omit. DEV_NOTES shows the precise failure mode: after the initial fix, `*mákōθi` still became `maceþ` because `OEWeakTailReduction` fronted the new `a` too early; the debugging table states that the bug appears when `*m*a*k*a*θ` turns into `*m*a*k*e*θ` inside weak-tail reduction [Germanic/docs/DEV_NOTES.md:19974-20002].

The key direct quote is Campbell's chronology statement, copied into DEV_NOTES: “even when shortened late, **ō became a**, but that **this a was of too late origin to become æ by Anglo-Frisian fronting** … Thus **ō if shortened early gives OE æ(e), but if shortened late it gives a**” [Germanic/docs/DEV_NOTES.md:20177-20184]. DEV_NOTES then records the current implementation outcome: “`*mákōθi → macaþ` ✓” and classifies weak-II present forms under the late-shortening set: “`*-ōsi → -as`, `*-ōþi → -aþ` (`lufas`, `lufaþ`, `macaþ`)” [Germanic/docs/DEV_NOTES.md:20459-20505].

For this slice, the fragment should be used as current implementation history: it explains why the live trace now reaches `macaþ` without requiring a row-local lexical exception.

## Superseded or diagnostic material

- The oldest make-family class-II exploration is now explicitly superseded for row 2310. DEV_NOTES first floated the 3sg cell as an alternate citation form — “**Option B: Change citation form to 3sg pres. indic.** (e.g., `*makōþi → macaþ`)” — and then claimed “**3sg present indicative** (`*-ōθi`): PGmc `*makōθi` → OE `*maceþ` (regular) / `macaþ` (attested, analogical)” [Germanic/docs/DEV_NOTES.md:2845-2847,2914-2917]. That material is still valuable as project chronology explaining why rows 2309/2310 were created, but it is no longer the live philological analysis.
- The intermediate debugging traces where row 2310 still output `maceþ` are also diagnostic only. DEV_NOTES preserves the failing trace `--- make (3sg) --- / PROTO: *mákōθi / EXPECTED: macaþ / OUTPUTS: maceþ` and then several iterative repairs, including the temporary `*ă` workaround, before the later chronology-based solution replaced it [Germanic/docs/DEV_NOTES.md:19873-19876,20074-20156,20387-20445]. These are useful for understanding implementation history, not for stating the current row result.
- The packet and memo are current secondary scaffolding, not primary authority. They are accurate and helpful because they already separate lexeme proto, lemma row, and 3sg cell, and they flag the older `maceþ` story as stale; however, the authoritative philological claims still live in DEV_NOTES plus the live TSV and trace [Germanic/docs/lexeme_reports/packets/2310-make-(3sg)-macaþ.md:15-85; Germanic/docs/lexeme_reports/research_memos/2310-make-(3sg)-macaþ.md:15-36,68-103].
- `Germanic/docs/analysis/arestoration_r_l_research.md` and `Germanic/docs/analysis/notable_findings.md` are relevant but shared-background only. They restate the class-II/macian A-restoration argument and late chronology, but they do not supply row-2310-specific new evidence beyond what DEV_NOTES already preserves [Germanic/docs/analysis/arestoration_r_l_research.md:85-88,113-128,190-194,208-210; Germanic/docs/analysis/notable_findings.md:756-809].
- No `oe_known_problems.tsv` entry currently marks row 2310 as unresolved. Whatever justified the `late_analogy` taxonomy originally, the live repo no longer treats `macaþ` as a current output failure [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7339-7359].

## Open questions for later work

- Decide whether `DERIVATION_CLASS = late_analogy` still best describes row 2310 now that DEV_NOTES treats `*-ōθi > -aþ` as regular. The label may still be serving a taxonomy purpose (“selected paradigm cell rather than lemma row”), but the slice should not let readers mistake that for a claim that `macaþ` itself is still philologically irregular [Germanic/data/germanic-aligned-final.tsv:1471-1471; Germanic/docs/DEV_NOTES.md:19497-19526].
- Decide whether the weak-II-3sg correction deserves a **shared indexed note** rather than row-by-row slices only. The evidence is strong and current, but most of it is shared with rows 2312/2314/2316/2318 rather than unique to `make` [Germanic/docs/DEV_NOTES.md:19497-19526,20459-20505; Germanic/docs/lexeme_reports/coverage_audit.md:178-183].
- If the make-family documentation is consolidated later, cross-link row 2310 more explicitly with row 2117 (`macian`) and row 2309 (`maca`) so that lexeme-level `macian` support and cell-level `macaþ` support remain clearly separated in reporting [Germanic/data/germanic-aligned-final.tsv:725-725,1470-1471; Germanic/docs/DEV_NOTES.md:36529-36534].

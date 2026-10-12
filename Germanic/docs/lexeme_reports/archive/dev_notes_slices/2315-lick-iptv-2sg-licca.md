---
row_id: 2315
concept: "lick (iptv.2sg)"
counterpart: licca
proto: "*likkōną"
protoform: "*líkkô"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2315-lick-(iptv.2sg)-licca.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/analysis/notable_findings.md
current_status: current_cell_trace_plus_shared_lick_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2315 lick (iptv.2sg) / licca

## Current row state

- The live OE row is `2315 | lick (iptv.2sg) | licca | PROTOFORM *líkkô | PROTO *likkōną | DERIVATION_CLASS late_analogy`, with the note `Class II weak iptv. 2sg test. Trimoric *ō → OE -a.` The three-way distinction must stay explicit: `PROTO *likkōną` is the row’s current TSV label, `PROTOFORM *líkkô` is the actual imperative-cell input, and `COUNTERPART licca` is the selected OE imperative outcome [Germanic/data/germanic-aligned-final.tsv:1476-1476].
- This row is a **non-lemma paradigm-cell companion**, not the lick-family citation form. The lemma row remains `2099 | lick | liccian | *líkkōjaną | regular`, while the sibling 3sg companion is `2316 | lick (3sg) | liccaþ | *líkkōθi | PROTO *likkōną | late_analogy`. The live data therefore already distinguish lexeme-level `liccian` from the finite-cell rows `licca` and `liccaþ` [Germanic/data/germanic-aligned-final.tsv:654-654,1476-1477].
- The current cell-level derivation is clean in the published trace and in the packet: `PROTO: *líkkô`, `EXPECTED: licca`, `OUTPUTS: licca`, with the only named OE step `OE Unstressed Long Vowel Shortening: *líkka`, then surface `licca` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7298-7315; Germanic/docs/lexeme_reports/packets/2315-lick-(iptv.2sg)-licca.md:17-42].
- The same snapshot keeps the family aligned around the shared `licc-` root: lemma row `2099` now derives `*líkkōjaną -> liccian`, and sibling row `2316` derives `*líkkōθi -> liccaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2781-2800,7277-7297].
- Audit state is straightforward but relevant: `coverage_audit.md` lists row `2315` among required rows with no report, `report_manifest.tsv` has no row-local entry, and `oe_known_problems.tsv` has no lick-family exception entry [Germanic/docs/lexeme_reports/coverage_audit.md:184-184; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- The packet and memo add one caution that should remain explicit in the slice: repo-local lexical tables are lemma-oriented and give `liccian`, not the imperative `licca`, so the absence of a lexical-table hit for `licca` is **not** counter-evidence against the row. The memo also says no row-specific dossier or manuscript-level imperative proof was found locally, so the row should be documented as a project-selected finite cell, not overclaimed as a separately dossier-backed headword [Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:13-21,33-36,56-62,85-97].

## Development-note summary

Row `2315` does **not** currently have a dedicated DEV_NOTES acceptance block comparable to the make-family imperative row. The direct row-local DEV_NOTES hits are historical debugging entries (`liċca`, later `lecca`) rather than a current “keep `*líkkô -> licca`” note [Germanic/docs/DEV_NOTES.md:2948-2986,5408-5418]. For current row state, the controlling evidence is therefore the live TSV plus the successful trace/packet, not a fresh row-2315 DEV_NOTES verdict [Germanic/data/germanic-aligned-final.tsv:1476-1476; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7298-7315].

What DEV_NOTES does provide is **shared support at two different levels**. First, it gives a class-II methodology note saying the imperative 2sg in trimoric `*-ō` is a useful regular probe cell: “**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca” [Germanic/docs/DEV_NOTES.md:2905-2912]. That passage is not about `lick` specifically, but it explains why a row like `2315` exists as a paradigm-cell companion instead of relying only on the analogically remodelled lemma pathway.

Second, DEV_NOTES gives current **lick-family / blocker** background. The later i-lowering work treats dorsal geminate `*kk` as a blocker, repeatedly using the lick family as evidence that the root should stay `licc-`, not `lecc-`. In the current shared analysis, `lick` is one of the forms showing that “**every form that retained \*i has a velar or labial consonant in the coda**,” and the refined implementation says the blocker hypothesis “**correctly predicts all observed cases**” [Germanic/docs/DEV_NOTES.md:5365-5378,5740-5750]. That support is lexeme-level / family-level, not imperative-only support, but it is the most current DEV_NOTES reasoning that still bears materially on row `2315`.

The safest replacement reading is therefore layered. Keep `PROTOFORM *líkkô` and OE `COUNTERPART licca` as the row-local imperative-cell solution because the live trace now derives them directly [Germanic/data/germanic-aligned-final.tsv:1476-1476; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7298-7315]. Keep the blocker discussion (`*kk` prevents the old `liċca/lecca` paths) as **shared lick-family support**, not as proof that DEV_NOTES wrote a row-specific essay for `2315` [Germanic/docs/DEV_NOTES.md:5358-5422,5710-5787; Germanic/docs/analysis/notable_findings.md:1065-1080]. And keep the live TSV `PROTO *likkōną` visible as current row state even though the memo recommends eventual normalization to lexeme-level `*líkkōjaną`; that recommendation is not current DEV_NOTES policy and should remain an open question rather than silently promoted into fact [Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:67-84,140-147].

## Relevant DEV_NOTES fragments

### DEV_NOTES: class-II imperative probe rationale

- Source heading: `Class II Weak Verb Exploration (class2-weak-exploration branch)`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:2858-2861,2905-2912`
- Fragment type: `current_shared_cell_rationale`
- Status: `current_background`
- Issue tags: `class_ii_weak_verbs`; `iptv_2sg`; `trimoric_o`; `shared_not_lick_specific`
- Recommended next use: `cite_to_explain_why_row_2315_exists_as_a_probe_cell`
- Shared with row IDs: `2309`, `2311`, `2313`, `2317`

This fragment is the main current DEV_NOTES rationale for the **cell type** represented by row `2315`, even though it is not lexeme-specific. DEV_NOTES recommends “Option A (iptv. 2sg with trimoric *ô) for verbs where it works cleanly” and then states the principle in quotable form: “**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca” [Germanic/docs/DEV_NOTES.md:2858-2861,2907-2912].

For row `2315`, the value is methodological, not lexical. It explains why the project isolates `*líkkô` as a regular imperative probe instead of treating `licca` as a replacement lemma. The fragment therefore supports the row as a **shared class-II imperative-cell solution**, while the actual lick-family root behavior still has to be justified elsewhere [Germanic/data/germanic-aligned-final.tsv:654-654,1476-1476].

> “**Recommendation**: Option A (iptv. 2sg with trimoric *ô) for verbs where it works cleanly …” [Germanic/docs/DEV_NOTES.md:2858-2860]

> “**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca” [Germanic/docs/DEV_NOTES.md:2909-2909]

### DEV_NOTES: lick-family blocker analysis during the i-lowering work

- Source heading: `Applying the Theory to Our Data` / `Experimental Implementation and Results`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:5365-5378,5408-5422`
- Fragment type: `mixed_shared_family_background_and_diagnostic`
- Status: `mixed — current as blocker reasoning, diagnostic as regression table`
- Issue tags: `i_lowering`; `dorsal_blocking`; `lick_family`; `row_2315_regression_history`
- Recommended next use: `cite_to_explain_why_licc-_is_current_but_lecca_is_stale`
- Shared with row IDs: `2099`, `2316`

This is the first current DEV_NOTES section that materially supports the lick family after the old palatalization-only stage. In the corpus test table, `lick` is listed with proto `*likkōną`, coda `-kk-`, and expected `blocking`, and DEV_NOTES generalizes from the table that “**every form that retained \*i has a velar or labial consonant in the coda**” [Germanic/docs/DEV_NOTES.md:5365-5378]. That statement is family-level, but it is exactly the kind of current reasoning that keeps `licc-` as the live root across `liccian`, `licca`, and `liccaþ`.

The same section also preserves the exact row-2315 regression line from the failed experimental rule: `| lick (iptv.2sg) | *likkô | lecca | licca | velar *kk |` [Germanic/docs/DEV_NOTES.md:5410-5418]. That line is diagnostically useful because it shows what happened when the blocker was omitted, but it is not current row authority: `lecca` is stale debugging history, not a live alternative target.

> “The pattern is striking: **every form that retained \*i has a velar or labial consonant in the coda** …” [Germanic/docs/DEV_NOTES.md:5376-5378]

> “| lick (iptv.2sg) | \*likkô | lecca | **licca** | velar \*kk |” [Germanic/docs/DEV_NOTES.md:5416-5418]

### DEV_NOTES: refined blocker hypothesis and successful implementation

- Source heading: `Refined hypothesis (potentially novel)` / `Implementation successful (2026-03-09)`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:5715-5750,5777-5787`
- Fragment type: `current_shared_family_support`
- Status: `current`
- Issue tags: `i_lowering_rule`; `velar_blocking`; `post_fix_verification`; `shared_not_cell_specific`
- Recommended next use: `cite_as_the_best_current_DEV_NOTES_background_for_the_lick_family`
- Shared with row IDs: `2099`, `2316`

This is the strongest **current** DEV_NOTES support for the lick family, but it remains shared-background rather than row-2315-specific. DEV_NOTES says “**Velars block i-lowering regardless of position**” and the test table includes `lick | No | **Yes** (*kk) | Block | liccian ✓`, followed by the verdict: “**The hypothesis correctly predicts all observed cases**” [Germanic/docs/DEV_NOTES.md:5715-5750]. The post-fix results then preserve the clean verification line `*likkōjăną | liccian | liccian | liccian | ✓ No change (velar *kk in coda)` [Germanic/docs/DEV_NOTES.md:5779-5787].

For row `2315`, the fragment matters because it tells later readers that the live project no longer treats the lick family as needing `e`-grade rescue. What it does **not** do is name the imperative row directly. Its support is inherited from the lexeme family: if `*kk` blocks the lowering/palatalization pathway for `liccian`, the same root-level blocker is the current background for `licca`, while the imperative ending itself is handled by the row trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2781-2800,7298-7315].

> “1. **Velars block i-lowering regardless of position** …” [Germanic/docs/DEV_NOTES.md:5715-5718]

> “**The hypothesis correctly predicts all observed cases.**” [Germanic/docs/DEV_NOTES.md:5748-5750]

### DEV_NOTES: direct row-local bug history for `*likkô`

- Source heading: `Results summary`; `C. Spurious palatalization of geminate *kk (*likkô → liċca vs licca)`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:2948-2986`
- Fragment type: `row_specific_superseded_diagnostic`
- Status: `superseded_but_worth_preserving`
- Issue tags: `geminate_kk`; `spurious_palatalization`; `row_2315_history`
- Recommended next use: `use_only_to_explain_old_liċca_history`
- Shared with row IDs: `2316`

This is the clearest surviving DEV_NOTES passage that speaks to row `2315` **directly**, and it is exactly why the slice has to separate current evidence from superseded diagnostics. The results table records `| likkô | liċca | licca | ✗ |`, and the following prose states the historical diagnosis: “OE palatalization of *k → ċ before front vowels is correct in general, but geminate *kk should **NOT** be palatalized in this context” [Germanic/docs/DEV_NOTES.md:2950-2959,2981-2985].

The fragment is still valuable because it preserves the exact old failure mode and the exact row input `*likkô`. But it is no longer current authority for the live row: the published trace now reaches `licca` directly, and later blocker analysis widened the explanation beyond palatalization alone to the whole i-lowering / blocker problem [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7298-7315; Germanic/docs/DEV_NOTES.md:5358-5422,5710-5787].

> “| likkô | liċca | licca | ✗ |” [Germanic/docs/DEV_NOTES.md:2958-2958]

> “OE palatalization of *k → ċ before front vowels is correct in general, but geminate *kk should **NOT** be palatalized in this context.” [Germanic/docs/DEV_NOTES.md:2983-2985]

## Superseded or diagnostic material

- The direct row-local DEV_NOTES outputs `liċca` and `lecca` are superseded debugging states, not current alternatives. `liċca` belongs to the early “spurious palatalization of geminate *kk” stage, and `lecca` belongs to the failed experimental i-lowering stage; the live trace now shows `*líkkô -> licca` cleanly [Germanic/docs/DEV_NOTES.md:2958-2985,5416-5418; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7298-7315].
- The packet already models this evidential hierarchy correctly. Its high-confidence section is the live trace; its DEV_NOTES excerpts are supporting/background evidence only. The memo likewise warns that the old `liċca` / `lecca` material is “historical debugging evidence, not the present implementation state” [Germanic/docs/lexeme_reports/packets/2315-lick-(iptv.2sg)-licca.md:15-42,56-106; Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:17-31,99-112].
- The lexeme-family material should stay aligned with the existing `2099 lick / liccian` slice: family-level blocker reasoning is shared, but lemma-row evidence must not be confused with cell-specific imperative evidence. The `2099` slice already warns against back-projecting the finite-cell diagnostics into the lemma row, and the same caution works in reverse here [Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md:28-38,64-66,96-106].
- The research memo and memo index propose a future cleanup in which row `2315` would align its `PROTO` with lexeme-level `*líkkōjaną`. That is a **memo-level recommendation**, not live row policy. The slice should preserve current TSV `PROTO *likkōną` while flagging the mismatch as unresolved documentation/data-model hygiene rather than quietly rewriting it away [Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:67-84,140-147; Germanic/docs/lexeme_reports/research_memo_index.tsv:146-146].
- The absence of a row-specific lexical-table or dossier hit for imperative `licca` should not be elevated into negative philology. The memo explicitly says the lexical tables are lemma-oriented (`liccian`) and that no stronger manuscript claim for the imperative was found locally; that means the row should be documented conservatively as a project-selected paradigm cell, not rejected [Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:33-36,56-62,85-97].

## Open questions for later work

- Should row `2315` continue to keep live TSV `PROTO *likkōną`, or should the lick-family paradigm rows eventually be normalized so that the lexeme-level proto remains visibly `*líkkōjaną` while `PROTOFORM *líkkô` continues to carry the imperative-cell choice [Germanic/data/germanic-aligned-final.tsv:654-654,1476-1477; Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:67-84,140-147]?
- If `dev_notes_slices/index.tsv` is revised later, should row `2315` remain a **slice-only companion** under the broader lick-family treatment rather than receiving its own index entry? Most surviving support is shared class-II or shared lick-family background, while the direct row-local DEV_NOTES hits are historical diagnostics rather than a current row essay [Germanic/docs/lexeme_reports/coverage_audit.md:184-184; Germanic/docs/lexeme_reports/dev_notes_slices/2099-lick-liccian.md:96-106].
- If later dossier work targets the finite weak-II imperatives, add direct philological support for `licca` itself rather than continuing to rely on lemma-level `liccian`, class-level imperative methodology, and implementation traces. The current repo evidence is enough for a conservative slice, but not for a stronger manuscript-attestation claim [Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:85-97,116-138].

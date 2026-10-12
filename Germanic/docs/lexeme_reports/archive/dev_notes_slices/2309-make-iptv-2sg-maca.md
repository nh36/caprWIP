---
row_id: 2309
concept: "make (iptv.2sg)"
counterpart: maca
proto: "*makōną"
protoform: "*mákô"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2309-make-(iptv.2sg)-maca.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2309-make-(iptv.2sg)-maca.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current_cell_specific_probe_plus_shared_make_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2309 make (iptv.2sg) / maca

## Current row state

- The live OE row is `2309 | make (iptv.2sg) | maca | PROTOFORM *mákô | PROTO *makōną | DERIVATION_CLASS late_analogy`, with the live note `Class II weak iptv. 2sg test (R/T §5.2). Trimoric *ō → OE -a.` [Germanic/data/germanic-aligned-final.tsv:1470-1470].
- This row is a **paradigm-cell companion**, not the make-family lemma row. The ordinary lexeme row remains `2117 | make | macian | PROTO *mákōjaną | PROTOFORM *mákōjaną | regular`, while the neighboring finite-cell companion `2310` keeps the same row-level `PROTO *makōną` but a different `PROTOFORM *mákōθi` and target `macaþ` [Germanic/data/germanic-aligned-final.tsv:725-725,1470-1471].
- The distinction among `PROTO`, `PROTOFORM`, and OE target must stay explicit here: `PROTO *makōną` is the row’s current project-level make-family label; `PROTOFORM *mákô` is the actual derivational input for this imperative probe; `COUNTERPART maca` is the selected OE imperative 2sg outcome. The existing `2117 make / macian` slice already treats `macian` as the lexeme-level citation form and warns against conflating it with the companion paradigm rows [Germanic/docs/lexeme_reports/dev_notes_slices/2117-make-macian.md:27-30,64-82].
- Audit state is quiet but not empty: `coverage_audit.md` flags row `2309` because it has a note and a non-`regular` derivation class; `report_manifest.tsv` still has no row-2309 entry; `oe_known_problems.tsv` has no corresponding problem record [Germanic/docs/lexeme_reports/coverage_audit.md:178-178; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation snapshot succeeds directly on the paradigm-cell input: `PROTO: *mákô`, `EXPECTED: maca`, `OUTPUTS: maca`, with the traced OE steps `Anglo Frisian Brightening: *mækô`, `OE A Restoration: *makô`, `OE Unstressed Long Vowel Shortening: *maka`, then `Outcome: maca` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7360-7379].
- The row packet and research memo agree on the same hierarchy: use the packeted `*mákô → maca` trace as the row’s direct evidence, but keep saying that the philological background for the stem vowel is inherited from the wider `macian` / class-II discussion rather than from a unique imperative-only attestation note [Germanic/docs/lexeme_reports/packets/2309-make-(iptv.2sg)-maca.md:15-42,56-130; Germanic/docs/lexeme_reports/research_memos/2309-make-(iptv.2sg)-maca.md:13-20,46-57,59-69].

## Development-note summary

This row does have genuine **cell-specific DEV_NOTES material**, but it is implementation-facing rather than fully lexicographic. DEV_NOTES explicitly chose the imperative 2sg as a regular class-II probe cell: “**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca” [Germanic/docs/DEV_NOTES.md:2905-2912]. That is stronger than the support available for many slice-only rows, because it directly names the exact paradigm cell represented by row `2309`.

The core row-specific project history is the `*ô` A-restoration bug. DEV_NOTES records the earlier failure as “`makô` → `mæċa` (wrong) instead of `maca` (correct),” explains that `{*ô}` was missing from `OEARestorationTriggerVowel`, and then records the fix and successful outcome: “After fix: `makô → maca` ✓” [Germanic/docs/DEV_NOTES.md:2865-2882; Germanic/docs/DEV_NOTES.md:2921-2932]. For this slice, that history matters because it is the clearest surviving explanation of why a dedicated imperative-cell row existed at all: the project wanted a regular weak-II finite form, but initially could not derive it correctly.

At the same time, the imperative row should **not** be over-claimed as if DEV_NOTES contained a standalone philological dossier for OE `maca`. The broader scholarly support in the repo is still mostly **lexeme-level / class-level**, centered on `macian` and on class-II retracted `a`. DEV_NOTES quotes Campbell and Ringe/Taylor to the effect that class-II weak verbs such as `macian` show restored/retracted `a` before later front-vocalic endings, and the internal A-restoration analysis file repeats the same point with `macian` and related verbs [Germanic/docs/DEV_NOTES.md:36529-36534; Germanic/docs/analysis/arestoration_r_l_research.md:190-194]. That shared material strongly supports the `mac-` stem needed by row `2309`, but it is still inherited support from the make/macian family, not a row-local imperative attestation note.

The right replacement reading is therefore layered. Row `2309` has (a) direct cell-level DEV_NOTES support for using `*mákô → maca` as a regular test form, (b) direct diagnostic history for the old `mæċa` bug and its fix, and (c) shared lexeme-level support from the `macian` literature and debug work explaining why the stem should be `mac-` rather than fronted `mæc-`. The later post-fix probe list that includes `*mákōjaną → macian` confirms the family-wide repair, but that line is still lexeme-level confirmation rather than row-2309-specific evidence [Germanic/docs/DEV_NOTES.md:36757-36767].

## Relevant DEV_NOTES fragments

### DEV_NOTES fragment 1

- Source heading: `### Issues to Resolve` / `### Options for Resolution` / `## Class II Weak Verb Exploration (class2-weak-exploration branch)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2782-2861,2901-2912`
- Fragment type: `row_specific_probe_rationale_with_shared_class_ii_background`
- Status: `mixed — current as rationale, superseded as global policy proposal`
- Issue tags: `make_family`; `class_ii_weak_verbs`; `paradigm_cell_selection`; `iptv_2sg`
- Recommended next use: `cite to explain why row 2309 exists and why its evidence is cell-level rather than lemma-level`
- Shared-with rows if relevant: `2117 make / macian`; `2310 make (3sg) / macaþ`; other class-II finite-cell probes

This fragment is where row `2309` becomes legible as a project decision rather than an arbitrary extra row. DEV_NOTES first diagnoses the broader infinitive problem — “`*makōjăną → maceian (expected macian)`” — and then argues that the regular finite forms are better phonological probes than the remodelled infinitive [Germanic/docs/DEV_NOTES.md:2761-2769]. The key cell-specific line is explicit: “**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca” [Germanic/docs/DEV_NOTES.md:2907-2912].

That line is directly relevant to row `2309`; however, the surrounding “Option A: Change citation form to iptv. 2sg” language is **not** the live global policy anymore, because the live TSV still keeps the ordinary lemma row `2117 make / macian` and uses `2309` only as a companion paradigm row [Germanic/docs/DEV_NOTES.md:2840-2861; Germanic/data/germanic-aligned-final.tsv:725-725,1470-1470]. So the fragment is current for the row’s rationale, but partly superseded if read as a proposal to replace lexeme-level citation forms wholesale.

> “**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca” [Germanic/docs/DEV_NOTES.md:2909-2909]

> “The regular forms (iptv. 2sg, 2sg, 3sg) preserve the original *-ō- stem vowel without the *-ōja- extension. These are candidates for TSV encoding.” [Germanic/docs/DEV_NOTES.md:2777-2778]

### DEV_NOTES fragment 2

- Source heading: `### A-Restoration Gap for {*ô}` / `#### 1. A-restoration fix for {*ô}`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2863-2882,2921-2932`
- Fragment type: `row_specific_bug_history_and_fix`
- Status: `current as implementation history`
- Issue tags: `a_restoration`; `trimoric_o`; `palatalization_avoidance`; `make_family`
- Recommended next use: `cite when explaining why older materials mention mæċa and why that is now stale`
- Shared-with rows if relevant: `other {*ô} probe rows, but the make example is the clearest surviving illustration`

This is the best surviving row-local explanation of the wrong form and the repair. DEV_NOTES states the pre-fix failure exactly: “Current problem: `makô` → `mæċa` (wrong) instead of `maca` (correct).” It then traces the failure to missing A-restoration before `{*ô}`, which allowed brightening and then spurious palatalization to produce `ċ` [Germanic/docs/DEV_NOTES.md:2865-2878]. The later fix note records both the rule change and the successful result: “After fix: `makô → maca` ✓” [Germanic/docs/DEV_NOTES.md:2923-2932].

For replacement-slice purposes, this fragment is important because it is truly **cell-specific**: it is not just saying that the make-family lemma behaves like other class-II verbs, but that the exact imperative probe `makô` once misderived and now succeeds. The row file should therefore preserve `mæċa` as superseded diagnostic history, not as an alternate target [Germanic/docs/DEV_NOTES.md:2865-2882; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7360-7379].

> “Current problem: `makô` → `mæċa` (wrong) instead of `maca` (correct).” [Germanic/docs/DEV_NOTES.md:2865-2865]

> “After fix: `makô → maca` ✓” [Germanic/docs/DEV_NOTES.md:2930-2930]

### DEV_NOTES fragment 3

- Source heading: `#### 4. Results summary`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2948-2952`
- Fragment type: `row_specific_verification_table`
- Status: `current diagnostic verification`
- Issue tags: `verification`; `probe_result`; `iptv_2sg`; `make_family`
- Recommended next use: `cite as the neatest single-line DEV_NOTES proof that the row now works`
- Shared-with rows if relevant: `2310 and the parallel bore/learn/lick finite-cell checks, but this line is row-local`

The results table is terse but unusually useful: it records the exact row input/output pair in one place — “`makô | maca | maca | ✓`” [Germanic/docs/DEV_NOTES.md:2950-2952]. For this slice that line should outrank vaguer later family-level remarks, because it is the closest surviving DEV_NOTES equivalent to a row-local acceptance test.

It is still diagnostic rather than literary authority. The table does not prove manuscript attestation or paradigm frequency; it proves that the project’s intended imperative-cell derivation is currently implemented and judged successful [Germanic/docs/DEV_NOTES.md:2950-2952; Germanic/docs/lexeme_reports/packets/2309-make-(iptv.2sg)-maca.md:17-42].

> “| makô | maca | maca | ✓ |” [Germanic/docs/DEV_NOTES.md:2952-2952]

### DEV_NOTES fragment 4

- Source heading: literature-support table inside the A-restoration/class-II discussion
- Source line hint: `Germanic/docs/DEV_NOTES.md:36529-36534`
- Fragment type: `shared_lexeme_level_background`
- Status: `current`
- Issue tags: `macian`; `class_ii_retracted_a`; `shared_philology`; `not_cell_specific`
- Recommended next use: `cite as the main inherited philological support for the mac- stem, while explicitly labeling it shared rather than imperative-specific`
- Shared-with rows if relevant: `2117 make / macian`; `2310 make (3sg) / macaþ`; class-II rows such as `sparian`, `talian`, `bacian`

This fragment gives the strongest surviving scholarly support for the make-family vowel, but it is shared support, not row-2309-only support. DEV_NOTES quotes Campbell §159 on “weak verbs in *-i-* (< *-ói-*), *lapian, macian, hnappian*, &c.” and Ringe/Taylor §6.3.1 on the decisive class-II pattern: “Weak verbs of class II always exhibit retracted *a* rather than *æ* … typical: *carian, talian, macian, bacian* …” [Germanic/docs/DEV_NOTES.md:36529-36534].

For row `2309`, the value of this fragment is that it justifies the restored `mac-` stem inherited by the imperative probe. It does **not** independently prove that the imperative 2sg is the right citation cell or that `maca` is the only possible editorial form. Those points come from fragment 1 plus the live row/trace evidence. The safest wording is therefore: fragment 4 supports the stem; fragments 1-3 support the specific cell choice and its implementation [Germanic/docs/DEV_NOTES.md:36529-36534; Germanic/docs/analysis/arestoration_r_l_research.md:80-87,190-194].

> “[…] weak verbs in *-i-* (< *-ói-*), *lapian, macian, hnappian*, &c.” [Germanic/docs/DEV_NOTES.md:36532-36532]

> “Weak verbs of class II always exhibit retracted *a* rather than *æ* … typical: *carian, talian, macian, bacian* …” [Germanic/docs/DEV_NOTES.md:36534-36534]

### DEV_NOTES fragment 5

- Source heading: `### §17.25.8 Post-fix verification`
- Source line hint: `Germanic/docs/DEV_NOTES.md:36757-36767`
- Fragment type: `shared_family_level_post_fix_check`
- Status: `current diagnostic background`
- Issue tags: `post_fix_verification`; `macian`; `family_alignment`; `not_cell_specific`
- Recommended next use: `cite only to show that the same repair also restored the lexeme-level make row`
- Shared-with rows if relevant: `2117 make / macian`; other repaired class-II rows

This post-fix probe list matters for alignment with the existing `2117 make / macian` slice, because it records the family-wide success state after the A-restoration work: “`*sákōjaną → sacian`, `*mákōjaną → macian` ✓” [Germanic/docs/DEV_NOTES.md:36762-36767]. But it is not row-2309-specific evidence: the line checks the infinitive/lemma pathway, not the imperative probe.

So the fragment should be used conservatively. It helps show that row `2309` now sits in a coherent make-family treatment alongside `2117`, not that the imperative row inherits all of the lemma row’s evidence automatically [Germanic/docs/DEV_NOTES.md:36757-36767; Germanic/docs/lexeme_reports/dev_notes_slices/2117-make-macian.md:70-82].

## Superseded or diagnostic material

- The older infinitive mismatch `*makōjăną → maceian (expected macian)` is important project history for the make family, but it is **not** evidence that row `2309` itself was ill-chosen. It explains why the repo explored finite cells like `maca`; it does not replace the lemma row or prove anything unique about imperative attestation [Germanic/docs/DEV_NOTES.md:2761-2769; Germanic/data/germanic-aligned-final.tsv:725-725,1470-1470].
- The “Option A: Change citation form to iptv. 2sg” passage is superseded if read as a repository-wide citation-form policy. The live data did **not** replace `2117 make / macian` with `2309 maca`; instead the repo now keeps both the lexeme row and the paradigm-cell row side by side [Germanic/docs/DEV_NOTES.md:2840-2861; Germanic/data/germanic-aligned-final.tsv:725-725,1470-1471].
- `mæċa` belongs in the slice only as diagnostic history of the pre-fix bug. The current trace, packet, and DEV_NOTES verification table all agree on `maca`, so `mæċa` should never be presented as a live alternative target [Germanic/docs/DEV_NOTES.md:2865-2882,2950-2952; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7360-7379; Germanic/docs/lexeme_reports/packets/2309-make-(iptv.2sg)-maca.md:17-42].
- The internal analysis file `arestoration_r_l_research.md` is clearly relevant but remains secondary/supportive. Its quotations on `macian` and `-ōj- > -i-` help explain the shared class-II background, but they should not outrank the row’s own DEV_NOTES fragments or be mistaken for imperative-cell-specific evidence [Germanic/docs/analysis/arestoration_r_l_research.md:80-87,190-194].
- The research memo’s suggestion that TSV `PROTO` might eventually be changed from `*makōną` to `*mákōjaną` is a later recommendation, not the live row state. For the slice, that proposal should remain an open data-model question rather than silently rewritten as current fact [Germanic/docs/lexeme_reports/research_memos/2309-make-(iptv.2sg)-maca.md:101-109; Germanic/data/germanic-aligned-final.tsv:1470-1470].

## Open questions for later work

- Should row `2309` continue to keep `PROTO *makōną`, or should the make-family paradigm rows eventually be normalized so that the lexeme-level proto remains visibly `*mákōjaną` while `PROTOFORM *mákô` continues to carry the imperative-cell choice [Germanic/docs/lexeme_reports/research_memos/2309-make-(iptv.2sg)-maca.md:46-57,82-107; Germanic/data/germanic-aligned-final.tsv:725-725,1470-1471]?
- If `index.tsv` is revised later, should row `2309` get an index entry keyed specifically to the cell-level fragments (`2909-2932`, `2950-2952`) while the shared `macian` literature material stays indexed under the lemma/family discussion rather than duplicated across all make-family rows [Germanic/docs/DEV_NOTES.md:2905-2932,2948-2952,36529-36534]?
- The make-family paradigm probe is still only memo/packet/manual in practice. If `oe_paradigm_probe.py` later gets a reusable built-in spec, it should keep the lemma row `*mákōjaną → macian`, the imperative row `*mákô → maca`, and the 3sg row `*mákōθi → macaþ` distinct so that lexeme-level and cell-level support are not conflated again [Germanic/docs/lexeme_reports/research_memos/2309-make-(iptv.2sg)-maca.md:84-95; Germanic/docs/lexeme_reports/research_memos/2310-make-(3sg)-macaþ.md:78-89].

---
row_id: 2317
concept: "show (iptv.2sg)"
counterpart: sċēawa
proto: "*skawōną"
protoform: "*skáwô"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2317-show-(iptv.2sg)-sċēawa.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2317-show-(iptv.2sg)-sċēawa.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current_trace_plus_shared_class_ii_and_show_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2317 show (iptv.2sg) / sċēawa

## Current row state

- The live OE row is `2317 | show (iptv.2sg) | sċēawa | PROTO *skawōną | PROTOFORM *skáwô | DERIVATION_CLASS late_analogy`, with note `Class II weak iptv. 2sg test. Trimoric *ō → OE -a. Normalized sċ: Campbell §440.` The row therefore already distinguishes the non-lemma project stem label `*skawōną` from the selected imperative-cell input `*skáwô` and from the normalized OE target `sċēawa` (Germanic/data/germanic-aligned-final.tsv:1478-1478).
- This is a **paradigm-cell companion**, not the show-family lemma row. The lemma-level row remains `2186 | show | sċēawian | PROTO = PROTOFORM *skáwōjaną | DERIVATION_CLASS regular`, while the sibling finite-cell row `2318` keeps the same non-lemma `PROTO *skawōną` but a different `PROTOFORM *skáwōθi` and target `sċēawaþ` (Germanic/data/germanic-aligned-final.tsv:993-993,1478-1479; Germanic/docs/lexeme_reports/dev_notes_slices/2186-show-sċēawian.md:18-38).
- The current published trace is exact and cell-specific: `PROTO: *skáwô`, `EXPECTED: sċēawa`, `OUTPUTS: sċēawa`, with the stages `OE Aw Long Diphthong: *skḗawô`, `OE Sk Palatalization: *ʃḗawô`, and `OE Unstressed Long Vowel Shortening: *ʃḗawa`, ending in `Outcome: sċēawa` (Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7525-7545).
- Repo-local philological support is real but must be kept separate from the project normalization. Bright lists the lemma and imperative together as `scēawian ... imp. 2 sg. scēawa` [@BrightCassidyRingler1971, s.v. "scēawian"]. That supports the **cell itself** in source spelling `scēawa`; the TSV's `sċēawa` is the project's normalized spelling under Campbell's initial-`sc` practice [@Campbell1959, §440].
- Coverage bookkeeping still treats row `2317` as needing slice/report material, `report_manifest.tsv` has no row-local manifest entry, and `oe_known_problems.tsv` has no row-specific exception record (Germanic/docs/lexeme_reports/coverage_audit.md:186-186; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8).

## Development-note summary

Row `2317` has enough material for a durable replacement slice, but the support is **layered rather than fully row-local**. The current cell choice is grounded first in the live TSV and published trace, second in Bright's source-spelled imperative `scēawa` [@BrightCassidyRingler1971, s.v. "scēawian"], and only third in shared DEV_NOTES reasoning about weak class-II finite cells and the `*aw > ēaw` repair. There is **no surviving current DEV_NOTES section devoted only to row 2317** in the way some rows preserve a dedicated acceptance block.

The most important current inherited rationale is class-level. DEV_NOTES adopts the Ringe-Taylor view that the infinitive `*-ōja-` is an analogical class-II remodelling, whereas the finite non-`j` cells preserve the older bare `*-ō-` stem [@RingeTaylor2014, §5.2]. In project wording: `The REGULAR forms (iptv. 2sg, 2sg, 3sg) preserve the original *-ō- stem vowel without the *-ōja- extension. These are candidates for TSV encoding` and, more specifically, `Imperative 2sg (*-ō, trimoric) ... does NOT involve the morphological *-ōja- suffix` (Germanic/docs/DEV_NOTES.md:2777-2778,2907-2912). For row `2317`, that is **shared cell-level methodology**, not show-specific attestation.

The current show-family phonology is likewise mostly shared. DEV_NOTES' `OEAwLongDiphthong` repair now explicitly handles `*aw` before a following vowel or trimoric `*ô`, exactly the environment needed for `*skáwô > *skḗawô > sċēawa` [@Campbell1959, §272]. The crucial row hit survives in a mixed-status form: `*skawô → sċēawa (expected scēawa)` (Germanic/docs/DEV_NOTES.md:3647-3649). The vowel history is current; the manuscript-style expectation `scēawa` is stale as row metadata because the live TSV now normalizes initial `sc-` to `sċ-`.

That leaves an important caution. The later show-family safety sweep is useful but not fully authoritative for row `2317`: it says `2317 *skáwô sċēawa sċēawa ✓ no *j; Class II noun` (Germanic/docs/DEV_NOTES.md:26638-26639). The **substance** of that line is still valuable — row `2317` is indeed a non-`j` companion cell outside the true `*aw+j` bug bucket — but the label `Class II noun` is simply wrong for this weak-verb imperative row. So this fragment is best treated as current diagnostic background, not as the row's clean final wording.

The safest replacement reading is therefore layered:

- **cell-level current evidence:** live TSV, published trace, and Bright's source-spelled imperative `scēawa` [@BrightCassidyRingler1971, s.v. "scēawian"];
- **shared class-level rationale:** weak-class-II finite cells are the regular `*-ō-` probe forms, unlike the analogical infinitive [@RingeTaylor2014, §5.2];
- **shared show-family phonology:** `*aw > ēaw` before vocalic material or `*ô`, plus editorial `sc > sċ` normalization [@Campbell1959, §§272, 440];
- **superseded or diagnostic DEV_NOTES history:** earlier `sċawa / scēawa` mismatch language and the later but inaccurate `Class II noun` label (Germanic/docs/DEV_NOTES.md:2987-2993,26638-26639).

## Relevant DEV_NOTES fragments

### DEV_NOTES: shared weak-class-II finite-cell rationale

- Source heading: `Implications for Class II Weak Verbs` and `Test forms: imperative 2sg and 3sg present indicative`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2759-2778,2905-2912`
- Fragment type: `current_shared_cell_rationale`
- Status: `current`
- Issue tags: `class_ii_weak_verbs`; `iptv_2sg`; `trimoric_o`; `shared_not_show_specific`
- Recommended next use: `cite to explain why row 2317 exists as a paradigm-cell companion`
- Shared with row IDs: `2309`, `2311`, `2313`, `2315`, `2318`

This is the controlling current methodology for the row. DEV_NOTES says the infinitive `*-ōja-` is a morphological innovation and that the finite cells preserve the older `*-ō-` stem, following the class-II paradigm logic discussed by Ringe and Taylor [@RingeTaylor2014, §5.2]. For row `2317`, this is what justifies using imperative `*skáwô` beside lemma `*skáwōjaną`; but it remains **shared class-level support**, not evidence unique to the show family.

> `The REGULAR forms (iptv. 2sg, 2sg, 3sg) preserve the original *-ō- stem vowel without the *-ōja- extension. These are candidates for TSV encoding.` (Germanic/docs/DEV_NOTES.md:2777-2778)

> `Imperative 2sg (*-ō, trimoric): PGmc *makō → OE maca` ... `This path does NOT involve the morphological *-ōja- suffix` (Germanic/docs/DEV_NOTES.md:2909-2912)

For this row, the fragment should be cited as a **shared explanation of cell choice** only. It does not by itself show that the show-family imperative is `sċēawa`; that proof comes from the live trace plus Bright's `scēawa` [@BrightCassidyRingler1971, s.v. "scēawian"].

### DEV_NOTES: `OEAwLongDiphthong` repair with a row-local hit

- Source heading: `OEAwLongDiphthong: PGmc *aw → OE ēaw before vowels (Campbell §272)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:3628-3649`
- Fragment type: `mixed_current_rule_and_stale_row_hit`
- Status: `partly_current`
- Issue tags: `oe_aw_long_diphthong`; `show_family`; `sc_vs_sċ`; `trimoric_o`
- Recommended next use: `cite for the vowel repair, but not as live wording for orthographic expectation`
- Shared with row IDs: `2186`, `2318`

This is the most useful surviving DEV_NOTES fragment for the row's actual phonology. It formulates the rule as `{*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}]`, explicitly including trimoric `*ô`, which is exactly why `*skáwô` now passes through `*skḗawô` before later shortening [@Campbell1959, §272]. The row-local hit is also valuable because it preserves the exact project moment when the vowel problem was fixed.

> `Rule: {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}]` (Germanic/docs/DEV_NOTES.md:3632-3637)

> `*skawô → sċēawa (expected scēawa)` (Germanic/docs/DEV_NOTES.md:3647-3649)

The first quotation is current rule material. The second is only **partly current**: it correctly shows the repaired vowel and row target, but its expected spelling `scēawa` belongs to the older source-spelling stage. The live row now intentionally writes `sċēawa`, so the quotation should be preserved as repair history, not as current orthographic policy [@Campbell1959, §440].

### DEV_NOTES: early show-family diagnostic before the `ēaw` repair

- Source heading: `Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2987-2993`
- Fragment type: `superseded_show_family_diagnostic`
- Status: `superseded`
- Issue tags: `missing_eaw`; `sc_vs_sċ`; `diagnostic_history`; `show_family`
- Recommended next use: `preserve only as project history`
- Shared with row IDs: `2186`, `2318`

This older fragment is still worth preserving because it records the earlier broken state in exact terms and also preserves the project's cleanest wording on `sk > sc` as an orthographic issue. But as row `2317` evidence it is fully superseded: the row no longer lacks `ēaw`, and the expected source spelling `scēawa` is no longer the live TSV form.

> `Affected: *skawô → sċawa (expected scēawa)` (Germanic/docs/DEV_NOTES.md:2989-2990)

> `The sk → sċ vs sc: Our FST produces sċ (palatalized) where sc is expected. The sk → sc change is not palatalization but a general OE shift of /sk/ → /ʃ/ spelled ⟨sc⟩.` (Germanic/docs/DEV_NOTES.md:2991-2993)

Only the final sentence remains reusable, and even there the row file should keep separate the **source spelling** `scēawa` and the **project normalization** `sċēawa` [@Campbell1959, §440].

### DEV_NOTES: later safety sweep and its limitation

- Source heading: `§17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology` plus regression-risk note
- Source line hint: `Germanic/docs/DEV_NOTES.md:26631-26639,26680-26681`
- Fragment type: `current_diagnostic_background`
- Status: `current_but_not_clean_final_wording`
- Issue tags: `aw_plus_j_scope`; `show_family`; `diagnostic_table`; `mislabel`
- Recommended next use: `cite only to show that row 2317 is outside the true *aw+j bug bucket`
- Shared with row IDs: `2186`, `2318`

This fragment is useful because it places the whole show family in the project's later `*aw+j` safety sweep. The substantive point is correct: row `2317` is a non-`j` companion cell, and the lemma row `2186` is protected by intervening `*ō`. That helps keep the imperative row aligned with the lemma row and the 3sg companion.

> `2186 *skáwōjaną        sċēawian       sċēawian        ✓ Class II *-ōjan-: *ō intervenes between *w and *j` (Germanic/docs/DEV_NOTES.md:26631-26632)

> `2317 *skáwô            sċēawa         sċēawa          ✓ no *j; Class II noun` (Germanic/docs/DEV_NOTES.md:26638-26638)

The second line should not be reused uncritically. `✓ no *j` is the useful part; `Class II noun` is wrong for this row and should be treated as diagnostic shorthand, not as live analysis. The accompanying risk note is better for maintenance prose than for row wording: `*skáwōjaną (row 2186) — *ō between *w and *j blocks rule` (Germanic/docs/DEV_NOTES.md:26680-26681).

## Superseded or diagnostic material

- The earliest show-family class-II table is now only project history: `*skawōjăną | sċaweian | scēawian | breaking_missing__ea` records the pre-repair state for the lemma family, not current authority for row `2317` (Germanic/docs/DEV_NOTES.md:2821-2829).
- The `2987-2993` note is superseded as a row problem statement. Its only durable reuse is the warning that source `<sc>` and project `sċ` should not be conflated [@Campbell1959, §440].
- The `3647-3649` rule note should be split mentally into two layers: current vowel repair plus stale orthographic expectation. Quoting it without that warning would wrongly imply that the live row still expects manuscript-style `scēawa`.
- The `26638` safety-sweep line is helpful only if explicitly marked as diagnostic. Its `Class II noun` label is inaccurate, so it should never be elevated into the row's final descriptive summary.
- Packet- or lexical-table silence should not be over-read. The packet already warns that not all hits are equally authoritative, and the absence of lexical-table hits for `sċēawa` reflects lemma-oriented resources, not evidence against the imperative row (Germanic/docs/lexeme_reports/packets/2317-show-(iptv.2sg)-sċēawa.md:1-4,77-82).

## Open questions for later work

- If a built-in `oe_paradigm_probe.py` specification is added later, the show family should be probed as a set: lemma `*skáwōjaną -> sċēawian`, imperative `*skáwô -> sċēawa`, and 3sg `*skáwōθi -> sċēawaþ`. Right now that comparison exists only in memo/trace form, not as reusable probe infrastructure (Germanic/docs/lexeme_reports/research_memos/2317-show-(iptv.2sg)-sċēawa.md:85-104).
- If `dev_notes_slices/index.tsv` is revised later, row `2317` still looks **slice-only rather than index-worthy**. The row has good current evidence, but most DEV_NOTES support is shared class-II/show-family background plus trace validation, not a standalone row-local DEV_NOTES dossier.
- If the TSV note is ever revisited, it may be worth making explicit that the row is a companion to lemma `sċēawian` and that direct source support is spelling-sensitive (`scēawa` in source spelling, `sċēawa` in project normalization) [@BrightCassidyRingler1971, s.v. "scēawian"; @Campbell1959, §440].

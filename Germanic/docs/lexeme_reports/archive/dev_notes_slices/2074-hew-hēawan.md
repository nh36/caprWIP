---
row_id: 2074
concept: hew
counterpart: hēawan
proto: *xáwwaną
protoform: *xáwwaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md
  - Germanic/docs/debug_snapshots/oe_mismatch_report_2026-03-11.txt
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2074 hew / hēawan

## Current row state

- The live OE row is `2074`, with `CONCEPT = hew`, `COUNTERPART = hēawan`, `PROTO = *xáwwaną`, `PROTOFORM = *xáwwaną`, and `DERIVATION_CLASS = regular`; the row carries only duplicated Wiktionary inheritance sourcing and no live exception note, so there is no TSV-side sign that this lexeme is being treated as problematic now [Germanic/data/germanic-aligned-final.tsv:557-560].
- `oe_known_problems.tsv` does not list this row or protoform. The tracked OE exceptions there are a short unrelated set, so row 2074 is not currently classified as a known OE non-fix or exception [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking still records `2074 | hew | hēawan | regular | no | - | - | - | none`, and `report_manifest.tsv` still contains only the small pilot list, with no dedicated report entry for row 2074. At slice time there is therefore no linked packet, memo, dossier, or report stem beyond general analysis files [Germanic/docs/lexeme_reports/coverage_audit.md:277-277; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The published derivation trace is an exact match: `PROTO: *xáwwaną`, `EXPECTED: hēawan`, `OUTPUTS: hēawan`. The OE-side sequence is `OE WW Simplification: *xáwaną`, `OE Aw Long Diphthong: *xḗawaną`, `OE Velar Fricative Palatalization: *çḗawaną`, `OE Heavy Syllable Nasal Apocope: *çḗawan`, `OE Secondary Nasalization: *çḗawąn`, `OE Weak Tail Reduction: *çḗawan`, with orthographic surface `Outcome: hēawan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2368-2388].
- The current mismatch snapshot likewise does not list `*xáwwaną` among OE failures, while the audit trace reproduces the same exact-match derivation as the published trace. Current project state therefore treats row 2074 as solved and regular, not merely tolerated [Germanic/docs/debug_snapshots/oe_mismatch_report_2026-03-11.txt:1-17; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2616-2636].

## Development-note summary

No standalone row essay survives for row 2074. The surviving DEV_NOTES material is mostly embedded in shared rule-debugging sections for `*aww`, `*ww`, and later `*aw+j` scoping, with one especially useful direct fix bullet for this lexeme. The closest thing to a row-specific historical note is the earlier repair section that says the rule placement was `After OEEwLongDiphthong, before AngloFrisianBrightening`, and under `Fixes (3 new matches)` records `*xawwăną → hēawan (was heawan) — hew` [Germanic/docs/DEV_NOTES.md:3639-3645]. For this row, that is the key surviving evidence that the former problem was a missing long-diphthong outcome in `*aww`, not any dispute about the OE target.

Later DEV_NOTES material reframes the row from recent fix to established control case. In the `PWGmc Geminate *ww Simplification` verification, DEV_NOTES says: `Note: The existing FST already handles *ww inputs correctly via *ww → ēo. Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` and then repeats `*xawwăną → hēawan` in the list of existing TSV `*ww` entries, followed by `All work. The *eww, *aww sequences are correctly becoming ēo, ēa` [Germanic/docs/DEV_NOTES.md:16308-16327]. That is the strongest surviving current-state DEV_NOTES evidence for row 2074, though DEV_NOTES also cautions that the actual implementation pathway may differ from Ringe–Taylor’s two-step analysis [Germanic/docs/DEV_NOTES.md:16316-16317].

The later `*aw+j` audit is important because it explicitly keeps row 2074 out of the problem bucket that still affects row 2061 `*xáwwją`. In the affected-forms table row 2074 appears as `2074 *xáwwaną          hēawan         hēawan          ✓ Class VII strong, no *j`, and the risk table classifies `Class VII       *kéwwaną, *xáwwaną — no *j present         NONE` [Germanic/docs/DEV_NOTES.md:26619-26627; Germanic/docs/DEV_NOTES.md:26678-26685]. For replacement-note purposes, this is essential: row 2074 is now used in DEV_NOTES as a safe no-`*j` control case, not as a live repair target.

Shared literature-background notes in the later supplement also matter here, but only as background. DEV_NOTES reports that Kroonen reconstructs `*hawwan-` with original geminate `*ww`, explicitly saying the geminate strong verb is the base of the derived `*hauja-` noun, and that Orel likewise treats `*xawwjan` as inheriting `*ww` from base `*xawwanan`, with `No gemination-by-*j machinery posited` [Germanic/docs/DEV_NOTES.md:26979-26988]. That supports keeping strict distinctions between row 2074 `*xáwwaną` (strong verb base, no `*j`) and row 2061 `*xáwwją` (derived `*j` form under separate scrutiny). It is shared background only, not evidence that row 2074 itself remains unresolved [Germanic/docs/DEV_NOTES.md:26979-26993].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3639-3654

- Source heading: `Pipeline placement` / `Fixes (3 new matches)`
- Source line hint: `lines 3639-3654`
- Fragment type: `row_specific_fix_note`
- Status: `row_specific_but_historical`
- Issue tags: `former_output_heawan`; `oe_aw_long_diphthong`; `pipeline_placement`; `j_scope_contrast`
- Recommended next use: `cite_when_explaining_the_exact_pre-fix_failure_and_why_2061_is_different`
- Shared-with rows if relevant: `1989`; `2061`; `2186`; `2227`; `2317`; `2318`

This is the most directly row-specific surviving DEV_NOTES block. DEV_NOTES first fixes the chronology by saying `Pipeline placement: After OEEwLongDiphthong, before AngloFrisianBrightening. At this point *a is still unfronted, so the rule targets *a directly`, then records under `Fixes (3 new matches)` the lexeme-specific outcome `*xawwăną → hēawan (was heawan) — hew` [Germanic/docs/DEV_NOTES.md:3639-3645]. For row 2074, the preserved substance is that the older bad output was `heawan`, i.e. the derivation had not yet reached the long `ēa` result. This is not a competing target; it is the exact historical failure signature.

The same fragment also preserves the scoping boundary that still matters for later work. DEV_NOTES immediately says `Correctly excluded: - *xawwją → heow (expected hīeġ) — *j follows *w, not a vowel` [Germanic/docs/DEV_NOTES.md:3652-3654]. That row 2061 contrast is important enough to carry into the slice: row 2074 belonged to the `*aww` long-diphthong fix, whereas `*xawwją` was already understood to be a different `*aw+j` problem. Treat this second sentence as shared diagnostic context, not as row 2074 evidence in itself.

### DEV_NOTES:line-16308-16327

- Source heading: `Rule 2: PWGmc Geminate *ww Simplification (R/T §3.1.4)` / `Verification of Existing *ww Handling`
- Source line hint: `lines 16308-16327`
- Fragment type: `verification_probe`
- Status: `current`
- Issue tags: `ww_handling`; `verification`; `control_case`; `mechanism_caution`
- Recommended next use: `cite_for_current_DEV_NOTES_position_on_row_2074`
- Shared-with rows if relevant: `1976`; `1989`; `2061`

This is the strongest current DEV_NOTES support for the row. DEV_NOTES says, `Note: The existing FST already handles *ww inputs correctly via *ww → ēo. Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` and then repeats `*xawwăną → hēawan` under `Existing TSV entries with *ww`, concluding `All work. The *eww, *aww sequences are correctly becoming ēo, ēa` [Germanic/docs/DEV_NOTES.md:16310-16327]. For row 2074 specifically, the important substance is not merely “works now,” but that DEV_NOTES treats it as affirmative evidence that inherited `*aww` without following `*j` already reaches the expected OE long diphthong.

The caution in the same block should also be preserved. DEV_NOTES says the system may be handling `*Vww` `via a different mechanism than R/T's two-step analysis` and that `We should verify the derivation path` [Germanic/docs/DEV_NOTES.md:16316-16317]. That means this fragment is current for outcome-verification, but only partly current for explanatory mechanism. Use it to support row status, not to overclaim an exact literature-mirroring derivation architecture.

### DEV_NOTES:line-26619-26685

- Source heading: `Affected forms in our TSV` / `Regression risk assessment`
- Source line hint: `lines 26619-26685`
- Fragment type: `regression_scope_note`
- Status: `current`
- Issue tags: `aw_plus_j_scope`; `class_vii_strong`; `no_j_present`; `safe_control`
- Recommended next use: `cite_when_protecting_row_2074_from_aw_plus_j_rule_changes`
- Shared-with rows if relevant: `1976`; `1989`; `2061`; `2186`; `2227`

This fragment is current and directly row-relevant because it explicitly inventories row 2074 in the course of a later `*aw+j` repair audit. The table entry is `2074 *xáwwaną          hēawan         hēawan          ✓ Class VII strong, no *j` [Germanic/docs/DEV_NOTES.md:26619-26627]. That wording should be preserved nearly verbatim in any later writeup, because it defines how DEV_NOTES wants this lexeme classified: strong Class VII, exact current match, and structurally outside the new rule’s trigger.

The same section then narrows the proposed intervention to the environment `*aw+j (and its post-gemination form *aww+j)` while saying `*aw+w, *aw+a, *Vw without following *j, and Class II *-ōj- are all untouched`, and the regression table assigns `Class VII       *kéwwaną, *xáwwaną — no *j present         NONE` [Germanic/docs/DEV_NOTES.md:26662-26667; Germanic/docs/DEV_NOTES.md:26678-26685]. For row 2074 this is current, not merely historical: it is the clearest surviving DEV_NOTES statement that later fixes for `hīeġ`/`strēgan`-type forms must not disturb `hēawan`.

### DEV_NOTES:line-26979-26993

- Source heading: `Camp B — no gemination of *w before *j; *u was always a glide`
- Source line hint: `lines 26979-26993`
- Fragment type: `shared_background_literature_note`
- Status: `shared_background_only`
- Issue tags: `inherited_geminate`; `base_vs_derived_form`; `kroonen`; `orel`; `kluge_seebold`
- Recommended next use: `cite_when_explaining_why_row_2074_and_row_2061_must_not_be_collapsed`
- Shared-with rows if relevant: `2061`

This is not a row-specific debugging note, but it is valuable shared background because it explains why the `*ww` in row 2074 can be treated as inherited rather than as a transient `*j`-driven artifact. DEV_NOTES says Kroonen reconstructs `*straujan-` and `*kaujan-` with single glide, but that `Geminate *ww in *hawwan- (the strong verb 'to hew') is original — it is the BASE of the noun *hauja-, not an intermediate gemination of a single *w by a *j suffix` [Germanic/docs/DEV_NOTES.md:26979-26983]. For this slice, that directly supports the conceptual separation between the strong verb base `*xáwwaną` and the derived `*xáwwją` problem.

DEV_NOTES then adds, `OREL (2003): reconstructs *strawan / *strawjanan (single *w throughout); *xawwjan with *ww but inherited from base *xawwanan (matching Kroonen's analysis). No gemination-by-*j machinery posited`, and notes Kluge-Seebold’s equivalent split between strong-verb base and reduced `haw-ja-` derivative [Germanic/docs/DEV_NOTES.md:26985-26993]. Treat this as shared-background-only support. It does not show row 2074 is a live issue; it shows why later `*aw+j` literature review kept returning to row 2074 as the stable base-form comparator.

## Superseded or diagnostic material

- The former surface `heawan` is superseded. It is still worth preserving because the DEV_NOTES fix block records `*xawwăną → hēawan (was heawan) — hew`, which is the clearest surviving statement of what the row used to do wrong before the `*aww` long-diphthong repair landed [Germanic/docs/DEV_NOTES.md:3642-3645].
- DEV_NOTES frequently writes this protoform in normalized debug spelling as `*xawwăną`, while the live TSV and current published traces use accented `*xáwwaną`. Nothing in the surviving material suggests a meaningful `PROTO` / `PROTOFORM` split here; for this row both live fields remain `*xáwwaną`, and the DEV_NOTES spelling variation should be treated as notation drift, not philological divergence [Germanic/data/germanic-aligned-final.tsv:557-560; Germanic/docs/DEV_NOTES.md:3642-3645; Germanic/docs/DEV_NOTES.md:16310-16324].
- A stale local sandbox artifact still says `"concept": "hew"`, `"proto": "*xawwăną"`, `"counterpart": "hēawan"`, `"outputs": []`. Because both current audit/publish traces show exact-match `OUTPUTS: hēawan`, this JSON should be treated as obsolete diagnostic residue rather than evidence of current row state [Germanic/tmp/old_english_sandbox_results_current.json:1303-1308; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2369-2388].
- No surviving DEV_NOTES block argues for changing the OE target, for splitting `PROTO` from `PROTOFORM`, or for moving the row out of `regular`. The durable documentary distinction is instead between row 2074 `*xáwwaną` (stable no-`*j` control) and row 2061 `*xáwwją` (live `*aw+j` audit target) [Germanic/docs/DEV_NOTES.md:3652-3654; Germanic/docs/DEV_NOTES.md:26625-26627; Germanic/docs/DEV_NOTES.md:26979-26993].

## Open questions for later work

- If a future full report wants the precise chronology of the old `heawan` failure, it will need to recover an archived pre-fix trace or rule-history commit. The surviving DEV_NOTES material gives placement and before/after outcome, but not a full derivation trace for the bad form [Germanic/docs/DEV_NOTES.md:3639-3645].
- Any future implementation work on `*aw+j` should keep row 2074 as an explicit regression control beside row 2061, not collapse them under a generic `hew` heading. DEV_NOTES is unusually clear that `*aw+j` is the narrow target and that `*xáwwaną` is a no-`*j` non-target [Germanic/docs/DEV_NOTES.md:26662-26667; Germanic/docs/DEV_NOTES.md:26678-26685].
- If later editors normalize DEV_NOTES spellings when building higher-level reports, they should preserve the distinction between notation drift (`*xawwăną` vs. live `*xáwwaną`) and an actual reconstruction change. The surviving evidence points to the former, but the inconsistency is visible enough that it should be handled deliberately [Germanic/data/germanic-aligned-final.tsv:559-559; Germanic/docs/DEV_NOTES.md:16310-16324].

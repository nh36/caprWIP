---
row_id: 2048
concept: ground
counterpart: grund
proto: *grúnduz
protoform: *grúnduz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2048 ground / grund

## Current row state

- CONCEPT: `ground`
- COUNTERPART: `grund`
- PROTO: `*grúnduz`
- PROTOFORM: `*grúnduz`
- DERIVATION_CLASS: `regular`
- The live OE row keeps both proto fields at `*grúnduz`, targets attested OE `grund`, and carries no row-local explanatory note beyond duplicated inherited-etymology placeholders in the source/history columns [Germanic/data/germanic-aligned-final.tsv:456-459].
- The repo OE source list independently matches the same pairing as inherited: `ground -> grund` [Germanic/data/old_english_wiktionary.tsv:112-112].
- Coverage tracking still shows row `2048` as uncovered: `coverage_audit.md` marks `packet = no`, with no memo, no attached DEV_NOTES fragment, and `none` in the notes column; `report_manifest.tsv` has no row-2048 entry to supply a pre-existing packet stem or memo link [Germanic/docs/lexeme_reports/coverage_audit.md:261-261; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` has no entry for `*grúnduz` or `grund`, so the row is not currently tracked as an exception bucket or unresolved OE mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation snapshot succeeds cleanly: `PROTO: *grúnduz`, `EXPECTED: grund`, `OUTPUTS: grund`, with the effective path `PGmc Final Z Deletion: *grúndu` > `OE High Vowel Apocope: *grúnd` > `Outcome: grund` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1886-1905].

## Development-note summary

No full row-specific DEV_NOTES block survives for `ground / grund`. The durable row-local DEV_NOTES footprint is much narrower: one **superseded but row-specific** regression-table line showing that `*grúnduz` temporarily surfaced as `grundo`, plus two **shared-background-only** chronology sections explaining why the bad `-o` appeared and why moving final `*-z` deletion earlier removed that failure again [Germanic/docs/DEV_NOTES.md:24443-24524].

That distinction should stay explicit. `PROTO = *grúnduz` and `PROTOFORM = *grúnduz` are the live project inputs for this OE row, while `COUNTERPART = grund` is the attested OE target now produced by the transducer [Germanic/data/germanic-aligned-final.tsv:456-459; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1886-1905]. The only competing form preserved in DEV_NOTES is `grundo`, and that form is not a rival attested OE lemma; it is a transient debug output from the shared `*-uz` chronology regression [Germanic/docs/DEV_NOTES.md:24451-24464].

A second DEV_NOTES strand is philological rather than pipeline-debugging. In the later systematic `*nd` audit, DEV_NOTES explicitly lists `grund | *grunduz | unknown | original | No`, then concludes that only `*funðanăz` needs `*ð` and that all the other `*nd` rows have original `*d` [Germanic/docs/DEV_NOTES.md:7538-7570]. For row 2048 this matters because it rules out over-correcting the proto input into something like `*grunðuz`: the live `*grúnduz` is being treated as the correct dental representation, not as a placeholder awaiting Verner-style repair.

Accordingly, this slice has to be conservative. What survives is enough to document (i) one superseded row-specific `grundo` regression, (ii) the shared z-loss / `OEMedUnstressedULowering` mechanism behind it, and (iii) a later shared audit confirming that `grund` belongs with original `*d`, not `*ð`. It is **not** enough to reconstruct a lexeme-specific essay from DEV_NOTES, and any search hit outside those functions should be treated as diagnostic only.

## Relevant DEV_NOTES fragments

### DEV_NOTES:24443-24459

- Source heading: `1. Probe outcome (vs. post-§17.10.23 baseline of 38)`
- Source line or section hint: `lines 24443-24459`
- Fragment type: `row_explicit_diagnostic_table`
- Status: `superseded_but_row_specific`
- Issue tags: `cvcuz_regression`; `stray_final_vowel`; `z_loss_ordering`
- Recommended next use: `cite_as_row_history_only`
- Shared-with rows if relevant: `1941, 1960, 2009, 2021, 2048` and the then-unrepaired pre-correction row `1983`

This is the one surviving DEV_NOTES location that names the row's protoform directly inside the regression cohort. DEV_NOTES says there were “Eight **new** mismatches, all sharing the shape *CVCuz,” and the table includes the exact row-local line `| *grúnduz | grundo | grund |` [Germanic/docs/DEV_NOTES.md:24451-24459]. That quotation should be preserved verbatim because it is the clearest evidence that `grundo` existed in project history and also the clearest evidence that it was only a mismatch report, not a proposed replacement counterpart.

The fragment is narrow but important. By the time this table was written, the row was already behaving like a nearly-correct regular reflex: stem `grund-` was intact, and the only visible defect was the unwanted final `-o` [Germanic/docs/DEV_NOTES.md:24453-24464]. So the support here is genuinely **row-specific**, but only as a superseded diagnostic snapshot. It should not be inflated into a claim that OE `grund` was doubtful or that the row ever needed analogical rescue.

### DEV_NOTES:24466-24490

- Source heading: `2. Root-cause: z-loss fires too late, spoofing OEMedUnstressedULowering`
- Source line or section hint: `lines 24466-24490`
- Fragment type: `shared_root_cause_analysis`
- Status: `diagnostic_but_still_explanatory`
- Issue tags: `oemedunstressedulowering`; `pgmc_final_z_deletion`; `false_medial_u`; `shared_cvcuz_cohort`
- Recommended next use: `cite_when_explaining_why_grundo_is_not_a_real_target`
- Shared-with rows if relevant: `1941, 1960, 2009, 2021, 2048` and the then-unrepaired pre-correction row `1983`

This is **shared-background-only** rather than lexeme-local, but it preserves the mechanism behind row 2048's temporary failure. DEV_NOTES quotes the relevant rule as ``{*u} -> {*o} || [V - u/ū] C+ _ C`` and explains that the final trigger slot “matched only truly medial *u” before the reorder, because word-final `*-uz` had already lost `*-z`; after §17.10.24, however, the final `*z` was still present when `OEMedUnstressedULowering` ran, so a word-final `*u` was misread as though “some consonant follows” [Germanic/docs/DEV_NOTES.md:24468-24482].

The worked prose example is `*bébruz`, not `*grúnduz`, but DEV_NOTES immediately generalizes: “Ten different forms fail for this exact reason” [Germanic/docs/DEV_NOTES.md:24480-24489]. Row 2048 belongs to that cohort. Applied here, the mechanism is straightforward: if `PGmcFinalZDeletion` fires too late, `*grúnduz` still looks consonant-final enough to lower the unstressed `u`, producing the spurious pre-surface path toward `grundo` instead of preserving `*grúndu` long enough for the expected apocope to yield `grund`.

### DEV_NOTES:24500-24524

- Source heading: `4. Proposed fix — tighten z-loss to PWGmc stage, not OE stage`
- Source line or section hint: `lines 24500-24524`
- Fragment type: `shared_fix_rationale`
- Status: `current_shared_policy`
- Issue tags: `chronology_repair`; `z_loss_before_oe_rules`; `expected_resolution`
- Recommended next use: `cite_with_current_trace_as_confirmation`
- Shared-with rows if relevant: `1941, 1960, 2009, 2021, 2048` and the then-unrepaired pre-correction row `1983`

This fragment is the surviving DEV_NOTES policy statement that explains why row 2048 is regular again. DEV_NOTES says `PGmcFinalZDeletion` should fire “immediately after raising” in the PNWGmc/PWGmc cluster, not in the OE cluster, because `OEMedUnstressedULowering` is exactly the kind of later rule that must not see final `*z` still standing to the right of a word-final vowel [Germanic/docs/DEV_NOTES.md:24500-24514]. The most portable sentence is the closing chronology claim: OE-stage rules then run against “a z-free input,” and “the ‘OE stage’ begins with word-final *-z already gone” [Germanic/docs/DEV_NOTES.md:24521-24524].

For this row the support remains shared rather than lexeme-specific, but it is still the key explanatory bridge between the old diagnostic line `*grúnduz | grundo | grund` and the live successful trace `*grúnduz > *grúndu > *grúnd > grund` [Germanic/docs/DEV_NOTES.md:24459-24524; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1895-1905]. The fragment should therefore be treated as **current shared background**, not as evidence for any special row-local exception.

### DEV_NOTES:7538-7570

- Source heading: `Systematic Check: TSV Forms with *nd Clusters (2026-03-11)`
- Source line or section hint: `lines 7538-7570`
- Fragment type: `shared_philological_audit`
- Status: `current_shared_background_only`
- Issue tags: `nd_cluster`; `dental_source`; `no_need_for_ð`; `representation_policy`
- Recommended next use: `cite_if_later_work_questions_the_d_in_protoform`
- Shared-with rows if relevant: `bindan`; `windan`; `hund`; `hand`; `land`; `sendan`; `funden` cohort alongside `grund`

This fragment is not a `ground` dossier, but it is the clearest surviving DEV_NOTES statement about the row's dental representation. In the audit table DEV_NOTES lists `| grund | *grunduz | unknown | original | No |`, explicitly under the heading “Reviewed all TSV entries with *nd clusters to confirm none require *nð” [Germanic/docs/DEV_NOTES.md:7538-7549]. The immediate relevance for row 2048 is conservative but real: the project explicitly checked whether `grund` belonged in the `*ð` bucket and answered no.

The prose conclusion should be kept with that table line. DEV_NOTES says, “Having exactly one `*ð` form in the TSV (`*funðanăz`) is **correct and complete**. All other `*nd` forms have original `*d` from PIE sources other than `*t`” [Germanic/docs/DEV_NOTES.md:7567-7570]. For row 2048 this is **shared-background-only** support, not a bespoke lexical argument, but it materially narrows later speculation: unless new literature evidence appears, `*grúnduz` should be read as a deliberate original-`d` representation, not as a known-missing Verner correction.

## Superseded or diagnostic material

- No lexeme-local DEV_NOTES essay for `ground / grund` survives beyond the one regression-table line and the shared background sections above. That absence should be stated plainly; the row's preserved DEV_NOTES footprint is diagnostic/project-historical, not a full philological note block [Germanic/docs/lexeme_reports/coverage_audit.md:261-261; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The superseded form to quarantine is `grundo`. It is a temporary output from the shared `*-uz` chronology regression, not an attested OE alternative, not a replacement `COUNTERPART`, and not a reason to rewrite `PROTOFORM` away from `*grúnduz` [Germanic/docs/DEV_NOTES.md:24451-24524].
- The earlier DEV_NOTES hit at the English-sandbox note — “stops no-op stems (`*bendaną`, `*grunduz`) from dying at the stage boundary” — is **diagnostic only for English tooling**, not OE row authority. It shows that the proto string `*grunduz` was once used as a cross-module test case, but it does not discuss OE `grund`, OE row 2048, or Germanic dental representation for this slice [Germanic/docs/DEV_NOTES.md:1845-1849].
- The current derivation trace is valuable as confirmation of present state, but it is not itself DEV_NOTES material. Its role here is to show that the shared chronology fix described above now yields the expected regular outcome again [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1886-1905].

## Open questions for later work

- If a later packet or memo is created for row 2048, decide whether it needs external lexicographic or textual attestation for OE `grund`; the surviving DEV_NOTES record is mostly implementation chronology plus the `*nd` representation audit, not a standalone lexical dossier.
- If `*-uz` regressions recur in future rule-ordering work, keep row 2048 grouped with the shared *CVCuz cohort rather than treating `grundo` as a row-specific mystery [Germanic/docs/DEV_NOTES.md:24451-24524].
- If later literature review ever challenges the row's dental representation, test that claim against the existing DEV_NOTES audit first: current project policy explicitly treats `grund` as an original-`d` form and reserves `*ð` status for `*funðanăz` alone [Germanic/docs/DEV_NOTES.md:7538-7570].

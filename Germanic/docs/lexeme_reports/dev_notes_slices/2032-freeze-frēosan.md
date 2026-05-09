---
row_id: 2032
concept: freeze
counterpart: frēosan
proto: "*fréusaną"
protoform: "*fréusaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2032 freeze / frēosan

## Current row state

- The live OE row keeps `CONCEPT = freeze`, `COUNTERPART = frēosan`, `PROTO = *fréusaną`, `PROTOFORM = *fréusaną`, and `DERIVATION_CLASS = regular`; the source field is still just inherited-etymology placeholder text rather than a row-local explanation [Germanic/data/germanic-aligned-final.tsv:396-396].
- Coverage infrastructure still treats row 2032 as having no finished packet, no research memo, no attached DEV_NOTES fragment, and no other report scaffolding; this slice therefore has to serve as the replacement working note rather than summarize an existing row dossier [Germanic/docs/lexeme_reports/coverage_audit.md:251-251].
- The current published derivation trace is uncomplicated and successful: `EXPECTED: frēosan`, `OUTPUTS: frēosan`, with the path `*fréusaną -> *frēosaną -> *frēosan -> *frēosąn -> *frēosan` via OE diphthong leveling, heavy-syllable nasal apocope, secondary nasalization notation, and weak-tail normalization [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1603-1622].
- No row-specific exception handling is visible in the current repo state. On present evidence, `frēosan` is being treated as an attested OE infinitive reached from the same comparative protoform that appears in the live row, not as a repaired target, substituted paradigm cell, or reconstructed OE stand-in [Germanic/data/germanic-aligned-final.tsv:396-396; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1603-1622].

## Development-note summary

No lexeme-specific DEV_NOTES section for row 2032 appears to survive in the live documentation, and that absence should be stated plainly. The usable support is shared rule material rather than a dedicated `freeze / frēosan` mini-dossier. In practical terms, that shared material is still enough to explain why the row is currently stable: the repo's OE notes repeatedly treat inherited PGmc `*eu` as a regular source of OE `ēo`, and the live trace shows no disagreement between that policy and the actual FST output for `*fréusaną` [Germanic/docs/DEV_NOTES.md:15975-15980; Germanic/docs/DEV_NOTES.md:43943-43949; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1603-1622].

For this row, the important distinctions are narrow but worth preserving. `PROTO` and `PROTOFORM` are both `*fréusaną`; unlike many repaired rows, there is no surviving evidence here for a split between comparative headword and OE-facing derivational input. `COUNTERPART` is attested OE `frēosan`, and the current trace reaches that form without workaround. The replacement note should therefore avoid inventing hidden analogical history just because other `*eu` lexemes required extra handling elsewhere [Germanic/data/germanic-aligned-final.tsv:396-396; Germanic/docs/lexeme_reports/coverage_audit.md:251-251].

The best shared DEV_NOTES support is the project's repeated statement that OE `ēo` is the regular reflex of inherited PGmc `*eu`. In the `brēost` correction note, DEV_NOTES says flatly that “The diphthong *eu in `*breusta-` explains OE brēost” and glosses the rule as “`*eu -> OE ēo` by regular monophthongization” [Germanic/docs/DEV_NOTES.md:15975-15978]. Later, in the `būgan/sċūfan` dossier, DEV_NOTES makes the same point from the other direction: OE long `ū` there is innovative, “NOT from PGmc *eu, which would regularly give OE *ēo — cf. *béuganą → bēogan attested in early Anglian” [Germanic/docs/DEV_NOTES.md:43946-43949]. Row 2032 belongs on the regular side of that contrast: nothing in the surviving notes suggests that `frēosan` resists or complicates the normal `*eu > ēo` development.

The remaining stages in the current trace also look like shared pipeline behavior, not row-local controversy. DEV_NOTES' archived heavy-syllable apocope note says the model learned that the same heavy/light conditioning affecting final `*-i` and `*-u` “also applied to `*-ą`,” and records the dedicated `OldEnglishHeavySyllableNasalApocope` rule inserted before weak-tail reduction [Germanic/docs/DEV_NOTES.md:1604-1620]. DEV_NOTES' later nasalization note likewise distinguishes primary from secondary nasalization and explains that secondary nasalization is an allophonic notation layer where “the nasal consonant is RETAINED” even though the preceding vowel is nasalized [Germanic/docs/DEV_NOTES.md:9592-9625]. Those shared notes fit the trace sequence for `*fréusaną`, but they are still general mechanism notes, not evidence that row 2032 ever needed bespoke repair.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-15917-15980

- Source heading: `OE brēost 'breast': TSV PROTOFORM Correction (2026-04-09)`
- Source line or section hint: `lines 15917-15980`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `pgmc_eu_to_oe_eo`; `regular_reflex`
- Recommended next use: `cite_as_shared_rule_support_only`
- Shared with row IDs:

This is not a `freeze` note, but it is the cleanest surviving DEV_NOTES statement of the sound law row 2032 needs. The section says, in words that should be preserved almost verbatim, “The diphthong *eu in `*breusta-` explains OE brēost,” then breaks that down as `*breusta-` with `*eu` and “`*eu -> OE ēo by regular monophthongization`” [Germanic/docs/DEV_NOTES.md:15975-15978]. For row 2032, the value of this fragment is specific: it supports taking the `ēo` of `frēosan` as the expected OE reflex of inherited `*eu` in `*fréusaną`, not as an analogical intrusion or a target-selection patch.

The same fragment is also useful because it carefully distinguishes the inherited diphthong from superficially similar forms without it. DEV_NOTES insists that forms without `*eu` cannot yield the `ēo` target and says of the competing `brust-` type that it “would give OE †brust or †bryst ... NOT brēost. The ēo diphthong can only come from *eu” [Germanic/docs/DEV_NOTES.md:15979-15980]. That logic transfers conservatively to row 2032: as long as the OE target really is `frēosan`, the live `PROTOFORM *fréusaną` is at least structurally compatible with the repo's stated sound-law expectations.

### DEV_NOTES:line-43943-43949

- Source heading: `Origin of the 3pl pret. choice`
- Source line or section hint: `lines 43943-43949`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_comparator`; `pgmc_eu_to_oe_eo`; `regular_vs_analogical`
- Recommended next use: `cite_as_negative_control`
- Shared with row IDs:

This fragment is valuable because it states the same rule in explicitly comparative terms. DEV_NOTES explains that the long `ū` of `būgan/sċūfan` is innovative, “NOT from PGmc *eu, which would regularly give OE *ēo — cf. *béuganą → bēogan attested in early Anglian” [Germanic/docs/DEV_NOTES.md:43946-43949]. That sentence is a useful negative control for row 2032: when the project wants to mark a lexeme as non-regular, it says so by contrasting the attested form with the regular `*eu > ēo` output. No analogous warning survives for `frēosan`.

Because the example is verbal rather than nominal, it is especially relevant here. The comparator `*béuganą → bēogan` shows that the repo's `*eu > ēo` expectation is not confined to one noun note like `brēost`; it is a broader OE policy extending to strong verbs as well [Germanic/docs/DEV_NOTES.md:43946-43949]. That makes it a better shared comparator for `frēosan` than a purely nominal example would be, while still stopping short of claiming row-specific documentation that does not exist.

### DEV_NOTES:line-1591-1620

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1620`
- Fragment type: `shared_pipeline_context`
- Status: `background`
- Issue tags: `final_star_a_loss`; `heavy_syllable`; `trace_interpretation`
- Recommended next use: `use_to_explain_trace_only`
- Shared with row IDs:

This fragment matters because the live trace for row 2032 contains `OE Heavy Syllable Nasal Apocope: *frēosan`, and DEV_NOTES preserves the project-side rationale for that label. The note says that existing literature explicitly documented heavy-syllable loss of final short `*-i` and `*-u`, while the model suggested that the same conditioning “also applied to `*-ą`,” leading to a dedicated `OldEnglishHeavySyllableNasalApocope` rule inserted before weak-tail reduction [Germanic/docs/DEV_NOTES.md:1604-1620]. For `*fréusaną`, this is enough to explain why the final nasalized vowel is removed in the trace once the stem has become heavy.

The status needs to stay conservative, though. DEV_NOTES itself labels this note archived and presents it as an empirically learned modeling generalization rather than a settled lexeme-specific philological claim [Germanic/docs/DEV_NOTES.md:1591-1597]. So it should be used here to decode the present transducer path, not to claim that `frēosan` has a bespoke literature argument about final `*-ą` beyond the project's shared pipeline policy.

### DEV_NOTES:line-9592-9625

- Source heading: `Primary vs Secondary Nasalization: The Correct Solution`
- Source line or section hint: `lines 9592-9625`
- Fragment type: `shared_pipeline_context`
- Status: `background`
- Issue tags: `secondary_nasalization`; `trace_notation`; `non_row_specific`
- Recommended next use: `use_to_decode_intermediate_form`
- Shared with row IDs:

This fragment is relevant because the row-2032 trace passes through `*frēosąn` between apocope and the final weak-tail normalization. DEV_NOTES explains that “Secondary Nasalization” is not nasal deletion at all but “ALLOPHONIC nasalization — the nasal consonant is RETAINED but causes the preceding vowel to become phonetically nasalized” [Germanic/docs/DEV_NOTES.md:9610-9625]. That is enough to explain why the trace can show a nasalized vowel notation without implying that row 2032 is undergoing the same kind of primary nasal-loss process seen in forms like `*fimf > fīf`.

For row work, this fragment should be treated as notation support, not as lexical evidence. It helps interpret the transducer's intermediate spelling of `*frēosąn`, but it does not demonstrate that `freeze / frēosan` had an independent DEV_NOTES debate. Its usefulness is therefore diagnostic and explanatory: it tells later readers how to read the trace, while leaving the row's philological status at the more modest “regular derivation, no row-local note preserved.”

## Superseded or diagnostic material

- There is no surviving row-specific DEV_NOTES section for `freeze / frēosan` to supersede. That absence is itself part of the current row state and should not be papered over with invented chronology [Germanic/docs/lexeme_reports/coverage_audit.md:251-251].
- The most concrete row-local evidence presently available is the published derivation snapshot, not DEV_NOTES itself. It shows the exact live cascade for the OE row — `OE Diphthong Leveling`, `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `OE Weak Tail Reduction` — ending in `Outcome: frēosan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1610-1622]. This is diagnostic support for current behavior, not proof of an older lexeme-specific research conclusion.
- The early DEV_NOTES implementation checklist that says “PGmc `*eu/*iu` not mapped to OE long diphthongs → add `*eu/*iu -> *ēo`” is useful project history, but for row 2032 it is weaker than the later, more explicit shared analyses quoted above [Germanic/docs/DEV_NOTES.md:1760-1766]. It can help explain why the modern trace succeeds, but it should not be promoted over the later rule statements.

## Open questions for later work

- If a later lexeme report is written for row 2032, decide whether shared `*eu > ēo` material alone is enough to justify indexed coverage, or whether the row should remain a slice-only “regular, no row-local DEV_NOTES dossier” case.
- If future cleanup adds row-specific packets or memos for the `*leusan- / *freusan- / *beugan-` strong-verb families, check whether `frēosan` needs to be linked into a shared verbal dossier rather than left documented only by generic `*eu > ēo` notes.
- If the OE trace notation is later simplified, preserve at least one explanation of why `*frēosąn` appears as an intermediate stage even though the final row is unproblematic; otherwise the secondary-nasalization label may look like a hidden exception marker when it is not.

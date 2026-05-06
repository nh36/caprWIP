---
row_id: 2170
concept: seam
counterpart: sēam
proto: *sáumaz
protoform: *sáumaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2170 seam / sēam

## Current row state

- The live OE row currently reads `CONCEPT = seam`, `COUNTERPART = sēam`, `PROTO = *sáumaz`, `PROTOFORM = *sáumaz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:931-931].
- `PROTO` and `PROTOFORM` are still identical here. This row is therefore not using a surrogate OE-facing input, a different paradigm cell, or a workaround reconstruction; the same `*sáumaz` serves both as comparative proto label and as the live derivational input for OE `sēam` [Germanic/data/germanic-aligned-final.tsv:931-931].
- `oe_known_problems.tsv` currently has no row-local entry for row `2170`, for `seam`, for `sēam`, or for `*sáumaz`; the file only lists unrelated known-problem items [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match and gives the live pathway now used by the grammar: `PROTO: *sáumaz`, `EXPECTED: sēam`, `OUTPUTS: sēam`, with the staged history `PGmc Final Z Deletion: *sáuma`, `OE Au Fronting: *sáeuma`, `OE Diphthong Leveling: *sēama`, `PWGmc Final Bare A Loss: *sēam` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3873-3892].
- Coverage infrastructure currently shows no linked packet, research memo, or dossier for this row beyond the slice being created here; the coverage audit lists row `2170` as `regular` with all linked-report fields empty and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:338-338].

## Development-note summary

No securely attachable dedicated `seam / sēam / *sáumaz` dossier survives in `Germanic/docs/DEV_NOTES.md`. The row therefore has to be documented from shared current sound-change notes plus the live derivation trace, not from a row-numbered lexeme memo. That is still enough to make the slice self-sufficient, because the live grammar already derives the target exactly as `*sáumaz > *sáuma > *sáeuma > *sēama > sēam`, and DEV_NOTES preserves current shared statements explaining both major parts of that chain [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3873-3892; Germanic/docs/DEV_NOTES.md:21436-21446,26754-26770,35059-35070].

The most important positive point is that the row's long OE diphthong is not a special repair. DEV_NOTES explicitly says that the existing `OEAuFronting (*au → *aeu)` plus `OEDiphthongLeveling (*aeu → *ēa)` rules “handle `*au → *ēa` generally” [Germanic/docs/DEV_NOTES.md:26765-26769]. A separate DEV_NOTES quotation from Ringe & Taylor then states that “most examples of the long diphthong reflected PWGmc `*au`” [Germanic/docs/DEV_NOTES.md:35061-35063]. Read together with the exact-match trace, those notes give the concrete row-level conclusion that OE `sēam` is the regular long-`ēa` outcome of proto `*sáumaz`, not a lexeme-specific exception and not a place where `PROTOFORM` needs to diverge from `PROTO` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3882-3886; Germanic/data/germanic-aligned-final.tsv:931-931].

The final-vowel side of the derivation is likewise regular and should be kept explicit. DEV_NOTES quotes Ringe & Taylor that WGmc underwent “loss of unstressed `*a` and `*ą` word-finally and before final `*-z`,” and immediately restates the chronology as `(1)` loss of `*-z` after unstressed vowels and `(2)` loss of word-final `*-a` and `*-ą`, both at the PWGmc stage [Germanic/docs/DEV_NOTES.md:21436-21446]. That shared chronology maps directly onto the row trace's `*sáumaz > *sáuma ... > *sēam` sequence [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3882-3886]. The row-level distinction should therefore stay simple but explicit: comparative `PROTO = *sáumaz`, identical OE-facing `PROTOFORM = *sáumaz`, and regular OE target `sēam` produced without any special exception handling [Germanic/data/germanic-aligned-final.tsv:931-931].

One scope warning is worth preserving because DEV_NOTES searches can be misleading here. The only literal `seam`-like hit in the current file is the unrelated statement that the breve marker “also marks compound-linking seams (Role 2)” [Germanic/docs/DEV_NOTES.md:21848-21853]. That is not lexical authority for row `2170`. This slice should therefore be used as a shared-support replacement note: it preserves the actual current material that explains why the row is regular, while recording plainly that no richer row-specific DEV_NOTES memorandum currently exists.

## Relevant DEV_NOTES fragments

No securely attachable current row-specific DEV_NOTES fragment survives for `2170`. The fragments below are the shared current notes that materially support the live row.

### DEV_NOTES:line-21436-21446

- Source heading: `Historical reality (R/T vol.2 §3.1.2, pp.59-61)`
- Source line or section hint: `lines 21436-21446`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_z_loss`; `final_a_loss`; `relative_chronology`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest current DEV_NOTES support for the non-lexical ending of the row. DEV_NOTES quotes Ringe & Taylor that “the loss of unstressed `*a` and `*ą` word-finally and before final `*-z`” was a WGmc-wide change and then restates the chronology as `(1)` loss of `*-z` after unstressed vowels and `(2)` loss of word-final `*-a` and `*-ą` [Germanic/docs/DEV_NOTES.md:21436-21443]. For `2170`, that directly supports the trace's first and last non-OE steps: `*sáumaz > *sáuma` by final-`z` loss, and later `*sēama > *sēam` by final bare-`a` loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3882-3886].

What this fragment establishes for the row is not merely abstract chronology. It confirms that the final `-az` portion of `*sáumaz` should not be treated as a special seam-specific problem, because the current project chronology already places both relevant reductions in ordinary PWGmc history before later OE vocalic developments are considered [Germanic/docs/DEV_NOTES.md:21441-21446]. That is why the row can remain fully regular with `PROTO = PROTOFORM = *sáumaz` [Germanic/data/germanic-aligned-final.tsv:931-931].

### DEV_NOTES:line-26754-26770

- Source heading: `STAGE 3 — *au → *éa (existing breaking machinery)`
- Source line or section hint: `lines 26754-26770`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `au_fronting`; `diphthong_leveling`; `long_diphthong`; `regular_pathway`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the most direct current DEV_NOTES statement about the row's main vowel development. After discussing a different lexical environment, DEV_NOTES says explicitly that the existing `OEAuFronting (*au → *aeu)` plus `OEDiphthongLeveling (*aeu → *ēa)` rules “handle `*au → *ēa` generally” [Germanic/docs/DEV_NOTES.md:26765-26769]. Even though the surrounding section concerns `*awj` sequences, that sentence is stated as a general rule-side fact about the grammar's treatment of `*au`.

For row `2170`, this is the shared note that explains the middle of the live derivation trace. It licenses the pathway `*sáuma > *sáeuma > *sēama`, which is exactly what the published trace shows before final `-a` loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3884-3886]. The fragment therefore establishes that the long `ēa` of OE `sēam` is the expected project-wide outcome of proto `*au`, not a row-local correction and not evidence for altering `PROTOFORM` away from `*sáumaz` [Germanic/data/germanic-aligned-final.tsv:931-931].

### DEV_NOTES:line-35059-35070

- Source heading: `§17.22.13.2.2 Ringe & Taylor (2014), A Linguistic History of English, vol. 2: The Development of Old English`
- Source line or section hint: `lines 35059-35070`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `ringe_taylor`; `long_ea`; `pwgmc_au`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best current DEV_NOTES quotation tying the row's OE long diphthong directly to handbook literature. In quoting Ringe & Taylor's discussion of i-umlaut of diphthongs, DEV_NOTES preserves the explicit statement that “most examples of the long diphthong reflected PWGmc `*au`” [Germanic/docs/DEV_NOTES.md:35061-35063]. The local dossier there is about a different lexeme, but the quoted handbook generalization is directly relevant to `*sáumaz > sēam`.

For this row, the fragment establishes a literature-backed reason that the target should contain long `ēa`. `sēam` is precisely the kind of lexeme the quotation is talking about: an OE long diphthong traced back to PWGmc/PGmc `*au`, without any need for analogy, paradigm-cell substitution, or exception status [Germanic/docs/DEV_NOTES.md:35062-35068; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3882-3892]. It is therefore useful as a citation-dense shared-support fragment when the slice needs more than the bare rule names from the trace.

## Superseded or diagnostic material

### DEV_NOTES:line-1760-1765

- Source heading: `Next actionable targets (carryover)` / `Long-vowel-missing deep dive`
- Source line or section hint: `lines 1760-1765`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `long_vowel_missing`; `au_to_ea`; `project_history`; `rule_implementation`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This older note is useful only as project history. DEV_NOTES records an early long-vowel-missing bucket and says one of the “biggest actionable sources” was that “PGmc `*au` not lengthened” needed a change `*aeu -> *ēa` or a dedicated long-diphthong step [Germanic/docs/DEV_NOTES.md:1760-1765]. That is relevant to row `2170` because `sēam` is exactly the sort of output that would have been wrong before the `*au > *ēa` pathway was stabilized.

But this is not the best current authority for the row; it is a historical breadcrumb explaining why later current DEV_NOTES passages talk about `OEAuFronting` plus `OEDiphthongLeveling` as an already-existing solution [Germanic/docs/DEV_NOTES.md:26765-26769]. Use it only if later reporting needs to explain the implementation history behind the now-regular `*sáumaz > sēam` derivation, not as the main citation for the row's present status.

- No dedicated superseded `seam` memorandum has been found in `DEV_NOTES.md`. The closest lexical-looking hit for the English string is the unrelated “compound-linking seams” remark, which should be treated purely as a search false positive and not indexed as row authority [Germanic/docs/DEV_NOTES.md:21848-21853].

## Open questions for later work

- If a packet or memo is later created, keep the row's three layers explicit near the top: comparative `PROTO *sáumaz`, identical OE-facing `PROTOFORM *sáumaz`, and regular OE target `sēam` from the live exact-match derivation [Germanic/data/germanic-aligned-final.tsv:931-931; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3873-3892].
- If later review wants a stronger seam-specific philological note, fresh canvassing would be needed. The present slice securely preserves shared current rule support and chronology, but it should not imply that `DEV_NOTES.md` already contains a dedicated row-numbered seam essay [Germanic/docs/DEV_NOTES.md:21436-21446,26754-26770,35059-35070].
- If `dev_notes_slices/index.tsv` is updated later, the securely attachable current anchors are the shared chronology note (`21436-21446`), the general `*au → *ēa` rule statement (`26754-26770`), and the Ringe & Taylor quotation tying long OE `ēa` to PWGmc `*au` (`35059-35070`). The early long-vowel-missing note (`1760-1765`) is useful only as diagnostic project history [Germanic/docs/DEV_NOTES.md:1760-1765,21436-21446,26754-26770,35059-35070].

---
row_id: 1988
concept: deer
counterpart: dēor
proto: *déuzą
protoform: *déuzą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1988 deer / dēor

## Current row state

- CONCEPT: `deer`
- COUNTERPART: `dēor`
- PROTO: `*déuzą`
- PROTOFORM: `*déuzą`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current Old English row keeps `PROTO = *déuzą`, `PROTOFORM = *déuzą`, `COUNTERPART = dēor`, and `DERIVATION_CLASS = regular`; the source field is still only duplicated inherited-etymology placeholders, not a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:223-223].
- Existing row infrastructure: `coverage_audit.md` still records row 1988 as `regular | no | - | - | - | none`, so no matching packet, research memo, or previously attached DEV_NOTES infrastructure currently exists for this lexeme [Germanic/docs/lexeme_reports/coverage_audit.md:222-222].
- Current implementation trace: the published derivation snapshot already returns the live target without repair — `Proto Input: *déuzą`, `Rhotacism: *déurą`, `OE Diphthong Leveling: *dēorą`, `OE Heavy Syllable Nasal Apocope: *dēor`, with surface `Outcome: dēor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:874-894].

## Development-note summary

DEV_NOTES support for row 1988 is **thin but not absent**. No surviving row-specific DEV_NOTES section discusses `dēor` by name as an Old English lexeme problem, and nothing in the live file suggests a dispute over the row's `PROTO`, `PROTOFORM`, or `COUNTERPART`. The usable material is instead shared rule discussion: DEV_NOTES repeatedly treats inherited PGmc `*eu` as a source of OE `ēo`, and that is exactly the sound-change relation this row needs [Germanic/docs/DEV_NOTES.md:1760-1766,5968-6005,43943-43949].

The earliest directly relevant shared implementation note is the long-vowel-missing triage entry. There DEV_NOTES identifies one of the remaining OE repair targets as: “**PGmc `*eu/*iu` not mapped to OE long diphthongs** → add `*eu/*iu -> *ēo` (WS merge)” [Germanic/docs/DEV_NOTES.md:1763-1766]. That matters for row 1988 because the live successful trace now does exactly that kind of work: after rhotacism creates `*déurą`, the OE side levels it to `*dēorą`, yielding the expected long diphthong before final nasal loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:883-889].

The strongest philological/shared-rule passage is the later `brēost` note. DEV_NOTES writes that “**Campbell confirms that OE has `brēost` as an example of the `*eu > ēo` outcome**” and then treats `*breustą -> brēost` as a regular derivation [Germanic/docs/DEV_NOTES.md:5968-5989]. Row 1988 depends on the same shared outcome, not on a separate exception mechanism: `*déuzą` is not being rewritten to an alternate protoform, and the current row state gives no sign that `dēor` needs special pleading beyond ordinary OE diphthong development plus the later loss of final nasal in a heavy syllable [Germanic/data/germanic-aligned-final.tsv:223-223; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:883-889].

DEV_NOTES later restates the same sound-law more explicitly while discussing another paradigm problem: OE long `ū` in `būgan/sċūfan` is “**NOT from PGmc `*eu`, which would regularly give OE `*ēo` — cf. `*béuganą -> bēogan` attested in early Anglian**” [Germanic/docs/DEV_NOTES.md:43943-43949]. For row 1988 this is useful because it shows that, in current project practice, `*eu > ēo` is not just an isolated patch from the `brēost` note but a standing comparative assumption reused elsewhere. That supports keeping `*déuzą` and `dēor` as a plain regular equation rather than recasting the row as reconstructed-exceptional or source-problematic.

The only place DEV_NOTES mentions `deer` itself is in much later English-sandbox debugging, where modern English `deer` appears inside the `{ɪə}+r` / post-vocalic-`/r/` smoothing cohort (`beard/bier/deer/spear/year`) [Germanic/docs/DEV_NOTES.md:2306-2324]. Those notes should be preserved only as diagnostic chronology. They are about the modern English output bucket, not about OE `dēor`, and they do not challenge the live Old English row's present derivation.

## Relevant DEV_NOTES fragments

### DEV_NOTES: lines 1760-1766

- Source heading: `Next actionable targets (carryover)` / `Long-vowel-missing deep dive`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `eu_to_ēo`; `long_diphthong_mapping`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the most direct shared implementation fragment for row 1988 because it states the exact rule family the row needs:

> “**PGmc `*eu/*iu` not mapped to OE long diphthongs** → add `*eu/*iu -> *ēo` (WS merge).” [Germanic/docs/DEV_NOTES.md:1763-1766]

For `*déuzą -> dēor`, that line is materially relevant even though `deer` is not named. The live trace now shows `*déuzą -> *déurą -> *dēorą -> *dēor`, so the row's current success fits the project-level repair target exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:883-889].

### DEV_NOTES: lines 5968-6005

- Source heading: `Campbell (1959) §115 (OE breaking)`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `eu_to_ēo`; `regular_reflex`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best current DEV_NOTES statement of the comparative sound law behind row 1988. DEV_NOTES says:

> “Campbell confirms that OE has `brēost` as an example of the `*eu > ēo` outcome...” [Germanic/docs/DEV_NOTES.md:5968-5972]

and then:

> “Changed OE PROTO from `*brustz` → `*breustą` ... [this] produces the attested OE `brēost` via regular `*eu > ēo` breaking.” [Germanic/docs/DEV_NOTES.md:5984-5989]

The `brēost` lexeme is different, but the relevance is real and narrow: current DEV_NOTES treats inherited `*eu > ēo` as an ordinary OE development. Row 1988 needs that same shared rule and no stronger special-case argument.

### DEV_NOTES: lines 43943-43949

- Source heading: `Origin of the 3pl pret. choice`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `eu_to_ēo`; `comparative_precedent`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This later fragment is useful because it restates the same point in explicit contrastive form:

> “... the long `ū` in `būgan/sċūfan` is an OE innovation, **NOT from PGmc `*eu`, which would regularly give OE `*ēo` — cf. `*béuganą -> bēogan` attested in early Anglian** ...” [Germanic/docs/DEV_NOTES.md:43946-43949]

For row 1988, this supports a conservative reading of the current data. The row does not need a substitute protoform or analogical explanation; it fits a project-wide regular `*eu > ēo` expectation.

### DEV_NOTES: lines 2306-2324

- Source heading: `KIT sweep (status: reverted to baseline)` and `KIT sweep (WIP)`
- Fragment type: `diagnostic_bucket`
- Status: `diagnostic_only`
- Issue tags: `english_sandbox`; `postvocalic_r_loss`; `modern_english_only`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

These are the only surviving lines that mention `deer` by concept name, but they are not OE-row authority. DEV_NOTES logs the English sandbox's stubborn `{ɪə}+r` cases as “`beard/bier/deer/spear/year`” [Germanic/docs/DEV_NOTES.md:2308-2308] and later repeats that the bucket needs post-vocalic `/r/` smoothing for the same cohort [Germanic/docs/DEV_NOTES.md:2322-2324]. For row 1988 they should be kept only as diagnostic context showing why `deer` appears in the repo's later English engineering notes. They do **not** bear on whether OE `dēor` is the right counterpart.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES argument was located for `dēor`. The absence matters: later writers should not invent a hidden project controversy around row 1988 when the surviving DEV_NOTES record is mostly shared-rule support plus later English diagnostics [Germanic/docs/lexeme_reports/coverage_audit.md:222-222; Germanic/docs/DEV_NOTES.md:1760-1766,5968-6005].
- The modern-English `deer` mentions in the KIT and `/r/`-smoothing notes are diagnostic only. They concern the later English outcome class `{ɪə}+r`, not the Old English lexeme, and should not be cited as if they justify or threaten the OE row state [Germanic/docs/DEV_NOTES.md:2306-2324].
- The published derivation trace is also diagnostic rather than a DEV_NOTES fragment, but it is worth preserving because it shows that the current cascade already derives `dēor` cleanly from the live protoform without workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:874-894].

## Open questions for later work

- If row 1988 is ever considered for indexing, decide whether shared `*eu > ēo` material alone is enough. At present the slice is useful, but the DEV_NOTES support is still mostly generic/shared rather than a true lexeme dossier [Germanic/docs/DEV_NOTES.md:1760-1766,5968-6005,43943-43949; Germanic/docs/lexeme_reports/coverage_audit.md:222-222].
- If a future packet or research memo is created, add external lexicographic citations for OE `dēor` so the row has source-local support beyond the successful trace and shared DEV_NOTES rule statements.
- If later English-sandbox work keeps mentioning `deer`, continue labeling those passages explicitly as modern-English diagnostic history, not as evidence about the Old English row.

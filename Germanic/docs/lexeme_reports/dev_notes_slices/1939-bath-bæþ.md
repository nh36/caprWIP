---
row_id: 1939
concept: bath
counterpart: bæþ
proto: *báθą
protoform: *báθą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1939 bath / bæþ

## Current row state

- The live Old English row is stable and uncomplicated: `CONCEPT = bath`, `COUNTERPART = bæþ`, `PROTO = *báθą`, `PROTOFORM = *báθą`, and `DERIVATION_CLASS = regular`; the row carries only inherited-etymology placeholder sourcing and no row-local explanatory note in the TSV itself [Germanic/data/germanic-aligned-final.tsv:28-28].
- `coverage_audit.md` still classifies row `1939` among the regular rows with empty `NOTE` and `Requirement basis = none`, which matches the present repo state: no pre-existing packet stem, research memo stem, or other attached report infrastructure was identified for this lexeme during this pass [Germanic/docs/lexeme_reports/coverage_audit.md:195-195].
- The published derivation trace already lands on the live target without repair. It shows `PROTO: *báθą`, then `Anglo Frisian Brightening: *bæθą`, then `OE Heavy Syllable Nasal Apocope: *bæθ`, then `Old English Orthography: *bæþ`, yielding `Outcome: bæþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:85-105].
- `oe_known_problems.tsv` was checked because the only potentially relevant DEV_NOTES material concerns `*θ` versus Verner-type voiced alternants; no row-specific known-problems entry for `bath / bæþ` or `*báθą` was found in that file during this pass.

## Development-note summary

DEV_NOTES support for row `1939` is real but thin, and it is **shared comparator material rather than a bath-specific dossier**. No surviving section of `Germanic/docs/DEV_NOTES.md` appears to be devoted to `bath / bæþ` or to `*báθą` directly. The materially relevant passage instead occurs inside the `hladan` mismatch analysis, where DEV_NOTES states the project-level rule explicitly: “If PGmc had voiceless `*θ`, OE would have `þ` (as in `baþan` "to bathe").” That sentence is not about row 1939 by ID, but it bears directly on it because the live row keeps exactly a voiceless `*θ` protoform and exactly an OE `þ` outcome [Germanic/docs/DEV_NOTES.md:10225-10233; Germanic/data/germanic-aligned-final.tsv:28-28].

The important consequence is that row `1939` is best understood as the **non-problem case** that the DEV_NOTES comparator presupposes. In the surrounding `hladan` and `nǣdl` discussion, DEV_NOTES is diagnosing rows where OE `d` implies a voiced Verner alternant and therefore makes a raw `*θ` protoform suspicious or wrong. By contrast, `bæþ` is exactly the kind of form that the note treats as regular evidence for inherited voiceless `*θ > þ`; it does not ask for protoform repair, Vernerization, or exception handling [Germanic/docs/DEV_NOTES.md:10232-10233,10250-10253,1349-1357].

The current implementation trace agrees with that conservative reading. The FST already derives `bæþ` from `*báθą` via ordinary Anglo-Frisian brightening plus routine loss of final nasal material, with no workaround stage and no mismatch flag [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:85-105]. That matters for replacement-note purposes: the slice should preserve the substance of the DEV_NOTES logic, but the substance here is mostly negative. The repo does **not** preserve a rich lexeme-specific bath note; instead it preserves a shared rule statement whose example `baþan` effectively confirms why row `1939` is regular.

Accordingly, this slice should remain cautious. The evidence supports the live row cleanly, but it does not justify inventing a larger project history than the repo actually contains. The best current note is therefore: row `1939` has only thin/shared DEV_NOTES support, that support is consistent with the live `*báθą > bæþ` analysis, and nothing in the current materials suggests promoting the row into an exception or repair bucket [Germanic/docs/DEV_NOTES.md:10225-10233,1349-1357; Germanic/docs/lexeme_reports/coverage_audit.md:195-195].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-10225-10233

- Source heading: `Analysis: *xlaθaną → hladan`
- Source line or section hint: `lines 10225-10233`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `voiceless_theta`; `oe_thorn_reflex`; `verner_comparator`; `regular_reflex`
- Recommended next use: `cite_if_justifying_regular_theta_row`
- Shared with row IDs: `2088`; `1939`

This is the key fragment for row `1939`, even though it survives inside another lexeme's analysis. DEV_NOTES says: “**If PGmc had voiceless `*θ`, OE would have `þ` (as in `baþan` "to bathe").** The OE form `hladan` with `d` shows Verner's Law applied” [Germanic/docs/DEV_NOTES.md:10232-10233]. For `bath / bæþ`, the first sentence is the important one. It states exactly the reflex pattern that the live row already shows: a voiceless PGmc dental fricative continuing as OE thorn. In other words, `bæþ` functions here as DEV_NOTES' own control example for why some other rows are problematic while this one is not [Germanic/data/germanic-aligned-final.tsv:28-28].

### DEV_NOTES:line-10243-10253

- Source heading: `Analysis: *nēθlō → nǣdl`
- Source line or section hint: `lines 10243-10253`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `verner_alternation`; `theta_vs_d`; `protoform_repair_logic`
- Recommended next use: `cite_only_as_contrast`
- Shared with row IDs: `2136`; `1939`

This fragment is relevant by contrast rather than by direct lexical overlap. DEV_NOTES explains that `nǣdl` is problematic because the TSV itself acknowledges “Verner's alternation” and because “OE reflects the `*d` variant,” so a protoform with raw `*θ` is not the right working input there [Germanic/docs/DEV_NOTES.md:10246-10253]. Row `1939` is the opposite configuration: OE has `þ`, not `d`, so this repair logic does **not** activate. The fragment is worth preserving because it shows what the project means, in practice, when a `*θ` row actually needs intervention — and `bath / bæþ` is not one of those cases.

### DEV_NOTES:line-1349-1357

- Source heading: `Scope of Verner's Law in the project`
- Source line or section hint: `lines 1349-1357`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `project_policy`; `case_by_case_verner`; `leave_regular_rows_alone`
- Recommended next use: `cite_for_triage_policy`
- Shared with row IDs: `2136`; `2088`; `1939`

The broader policy note is also materially relevant. DEV_NOTES says that the project has “**NOT yet implemented a general Verner's Law mechanism**” and is therefore working case by case: “Where the regular sound change ... gives the right answer, we use it ... [and] where only Verner's alternation explains the outcome ... the item remains a known mismatch until we decide on a systematic approach” [Germanic/docs/DEV_NOTES.md:1349-1357]. Applied to row `1939`, that policy points in the conservative direction: the regular sound change already gives the right answer (`bæþ`), so the row should stay regular rather than be pulled into the Verner problem set.

## Superseded or diagnostic material

- The surviving DEV_NOTES material is diagnostic-by-comparison, not a bath-specific historical dossier. The `hladan` and `nǣdl` sections should therefore be cited only for the shared `*θ > þ` / `*ð > d` logic they state, not as if they were direct row-1939 analyses [Germanic/docs/DEV_NOTES.md:10225-10253].
- The derivation trace is useful implementation evidence but not a DEV_NOTES fragment. Its role here is to confirm that the current cascade already handles `*báθą > bæþ` as a straightforward regular derivation [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:85-105].
- `coverage_audit.md` is likewise diagnostic rather than argumentative. Its `none` entry for row `1939` accurately reflects the repo's present state and is part of the reason this slice should stay modest in scope [Germanic/docs/lexeme_reports/coverage_audit.md:195-195].

## Open questions for later work

- If later lexeme-report indexing work revisits the `none` rows, decide whether this slice's thin but genuine shared-rule support is enough to make row `1939` index-worthy, or whether it should remain effectively no-index until a bath-specific research note exists.
- If a future Verner sweep audits all OE rows with inherited `*θ`, keep row `1939` explicitly distinguished from the `hladan`/`nǣdl` type: the current evidence supports voiceless `*θ > þ`, not a hidden voiced alternant.
- If later literature work adds explicit lexical citations for PGmc `*báθą` and OE `bæþ`, attach them as lexeme-local support; at present the repo's strongest internal note support is still the shared DEV_NOTES comparator rather than a dedicated bath discussion.

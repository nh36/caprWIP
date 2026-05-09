---
row_id: 1955
concept: book
counterpart: bōc
proto: *bōkz
protoform: *bōkz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1955 book / bōc

## Current row state

- CONCEPT: `book`
- COUNTERPART: `bōc`
- PROTO: `*bōkz`
- PROTOFORM: `*bōkz`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current Old English row keeps `book / bōc / *bōkz` with `DERIVATION_CLASS = regular`; the source field contains only inherited-etymology placeholders and no row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:92-92].
- Existing row infrastructure: `coverage_audit.md` still marks row 1955 as having no packet, no research memo, no attached analysis file, and no prior DEV_NOTES fragment, so this replacement slice is currently the only row-local note infrastructure for the lexeme [Germanic/docs/lexeme_reports/coverage_audit.md:203-203].
- Current implementation trace: the published derivation snapshot already returns the live target without repair — `# book`, `PROTO: *bōkz`, `EXPECTED: bōc`, `OUTPUTS: bōc`, with the trace reducing `*bōkz` to `*bōk` by final `-z` deletion and then surfacing `bōc` orthographically [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:349-368].
- Homograph caution: the repo also has a different Old English row `1942 beech / bōc / *bōkō`; that matters because one of the only other `bōc` mentions in `DEV_NOTES.md` is actually about the beech lexeme and should not be silently reattached to row 1955 [Germanic/data/germanic-aligned-final.tsv:40-40,92-92].

## Development-note summary

No exact row-specific DEV_NOTES dossier for `*bōkz > bōc` survives in the live file, and that absence should be stated plainly rather than papered over. The usable support is thin and mostly shared: the one directly relevant project note is a long-vowel triage entry stating that Old English `ō` before velars should remain long, with `bōc` cited as one of the control examples. In the same repo state, the published derivation trace already yields `bōc` from `*bōkz` without workaround, so the live row is presently a straightforward regular-success row rather than an active exception case [Germanic/docs/DEV_NOTES.md:1760-1766; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:349-368].

The important substance of the DEV_NOTES discussion is therefore not a bespoke philological narrative about `book`, but a project-level implementation claim: when the OE cascade handles long vowels before velars correctly, forms like `bōc` and `bōg` should keep `ō`, so an OE-side velar-shortening rule is misplaced or overbroad [Germanic/docs/DEV_NOTES.md:1760-1766]. For row 1955, that shared claim fits the live data exactly. `PROTO` and `PROTOFORM` are both the ordinary comparative input `*bōkz`; `COUNTERPART` is the ordinary OE reflex `bōc`; and the current derivation trace shows no need for analogical repair, alternate preform selection, or exception tagging [Germanic/data/germanic-aligned-final.tsv:92-92; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:349-368].

The other materially relevant DEV_NOTES passage has to be handled as a warning, not as positive support. A nearby mismatch audit says: “**Palatalization missing**: `*bōkō` (beech) never triggers `VelarPalatalization`; output `bōcō` vs expected `bēċe`.” That line is genuinely relevant to row 1955 only because it uses the same OE spelling `bōc` for a different lexeme. The slice should preserve that homograph warning explicitly so later extraction/indexing work does not mistake beech-specific palatalization troubleshooting for book-specific evidence [Germanic/docs/DEV_NOTES.md:1715-1718; Germanic/data/germanic-aligned-final.tsv:40-40,92-92].

The practical conclusion is conservative. DEV_NOTES does support the current row, but only indirectly and at the level of shared sound-change / rule-placement discussion. There is no surviving lexeme-local note about noun class, semantics, source disagreement, or target selection for `book / bōc`. This slice should therefore preserve the real support that exists while also preserving the negative fact that row 1955 is not backed by a larger row-specific DEV_NOTES chronology [Germanic/docs/DEV_NOTES.md:1760-1766; Germanic/docs/lexeme_reports/coverage_audit.md:203-203].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:1760-1766

- Source heading: `Next actionable targets (carryover)` / `Long-vowel missing`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `long_vowel_preservation`; `velar_context`; `shared_rule_support`; `regular_reflex`
- Recommended next use: `cite_in_final_report`

This is the single clearest current DEV_NOTES passage for row 1955. DEV_NOTES first flags the remaining long-vowel bucket as a general OE problem and then gives the row-relevant control claim in exactly the needed form: “**OE ō before velars should stay long** → move `EnglishVelarShortening` out of the OE block (OE keeps `bōc/bōg`)” [Germanic/docs/DEV_NOTES.md:1760-1766]. For `*bōkz > bōc`, that is the core project-level statement to preserve. It does not narrate the whole lexeme history, but it does say that the expected OE output keeps long `ō` in precisely this environment, which is the phonological point row 1955 depends on.

### Germanic/docs/DEV_NOTES.md:1715-1718

- Source heading: `Concrete “rule not firing” evidence (2026-02-01 trace)`
- Fragment type: `superseded_or_diagnostic_for_homograph`
- Status: `diagnostic_only`
- Issue tags: `homograph_warning`; `beech_not_book`; `palatalization`; `do_not_misattach`
- Recommended next use: `preserve_as_search_trap_warning`

This fragment is materially relevant only because later searches for `bōc` will hit it and may misread it as evidence for row 1955. The line says: “**Palatalization missing**: `*bōkō` (beech) never triggers `VelarPalatalization`; output `bōcō` vs expected `bēċe`. In the trace there is no fronting stage that would supply the trigger, so this is likely a rule/chronology or etymon/expected mismatch” [Germanic/docs/DEV_NOTES.md:1715-1718]. That note belongs to the separate beech row with protoform `*bōkō`, not to the book row with protoform `*bōkz` [Germanic/data/germanic-aligned-final.tsv:40-40,92-92]. It should be kept here as diagnostic anti-evidence so the homographic OE form does not cause cross-row contamination.

## Superseded or diagnostic material

- No exact-hit row-local DEV_NOTES discussion of `book / bōc / *bōkz` was located. The absence of such a note is itself part of the current row state and should remain visible in the replacement slice rather than being replaced by inferred narrative [Germanic/data/germanic-aligned-final.tsv:92-92; Germanic/docs/lexeme_reports/coverage_audit.md:203-203].
- The beech homograph note at `Germanic/docs/DEV_NOTES.md:1715-1718` is diagnostic only. It is useful here because it explains why a naive string search for `bōc` can pull in the wrong lexeme, not because it supplies positive support for row 1955 [Germanic/docs/DEV_NOTES.md:1715-1718; Germanic/data/germanic-aligned-final.tsv:40-40].
- The current derivation trace is supportive but not itself DEV_NOTES material. Its role is implementation-facing: it confirms that the live cascade already derives `bōc` from `*bōkz` without a repair layer or exception mechanism [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:349-368].

## Open questions for later work

- If later indexing work wants row 1955 represented in `index.tsv`, decide whether the shared long-vowel/velar note plus the clean live trace are enough to justify indexing, or whether the row should remain no-index until a more lexeme-specific DEV_NOTES discussion exists.
- If future DEV_NOTES work expands the `EnglishVelarShortening` discussion, attach row 1955 explicitly alongside other `ō + velar` controls such as `bōg`, so the present shared note does not have to carry the whole burden alone [Germanic/docs/DEV_NOTES.md:1766-1766].
- If later audits keep surfacing `bōc` hits from the beech row, consider adding a standardized homograph-disambiguation tag in report infrastructure; this slice already shows why that would help for `bōc` [Germanic/data/germanic-aligned-final.tsv:40-40,92-92].

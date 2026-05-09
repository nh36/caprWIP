---
row_id: 2097
concept: leek
counterpart: lēac
proto: *láukaz
protoform: *láukaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-leek-2026.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt
current_status: current_regular_row_no_row_specific_dev_notes_block
needs_literature_agent: no
---

# DEV_NOTES material — 2097 leek / lēac

## Current row state

- Live row 2097 is fully regular in the TSV: concept `leek`, counterpart `lēac`, `PROTO = *láukaz`, `PROTOFORM = *láukaz`, `DERIVATION_CLASS = regular`, with no live NOTE text attached. The sibling cog-set rows are Dutch `look`, English `leek`, and German `Lauch`, all likewise aligned to `*láukaz` [Germanic/data/germanic-aligned-final.tsv:644-647].
- The coverage audit treats row 2097 as a regular row with empty NOTE and no report requirement (`Requirement basis = none`), which matches the absence of any `*láukaz` ledger entry in `oe_known_problems.tsv` [Germanic/docs/lexeme_reports/coverage_audit.md:286-291; Germanic/data/oe_known_problems.tsv:1-8].
- Current derivation snapshots confirm that the live cascade already lands exactly on the target. The compact trace gives `PROTO: *láukaz`, `EXPECTED: lēac`, `OUTPUTS: lēac`, with the OE-side stages shown as `OE Au Fronting: *láeuka`, `OE Diphthong Leveling: *lēaka`, `PWGmc Final Bare A Loss: *lēak`, and surface `Outcome: lēac`; crucially, `OEVelarPalatalization` is `[no-change]` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:3215-3234; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:15583-15697].
- The dedicated leek dossier reaches the same operational conclusion: “**The FST already produces *lēac* from `*laukaz`**,” so “**this row is not currently a mismatch**,” and the recommendation is Priority 1: leave the row as is [Germanic/docs/dossier-leek-2026.md:31-43,365-390].

## Development-note summary

No row-specific `DEV_NOTES.md` block for row 2097 currently survives. The only explicit live DEV_NOTES mention of `lēac/lēc` is a shared background remark inside the reek closure note, not a dedicated leek section [Germanic/docs/DEV_NOTES.md:37945-37955]. This slice therefore has to be conservative: it uses that surviving DEV_NOTES line as shared background only, and builds the usable row note from the live TSV state, the current derivation traces, and the dedicated leek dossier [Germanic/data/germanic-aligned-final.tsv:644-647; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:3215-3234; Germanic/docs/dossier-leek-2026.md:19-43].

The distinction among row fields is straightforward here and should stay explicit. `PROTO` and `PROTOFORM` are both `*láukaz`; unlike row 2151 `reek / rēac`, there is no current project split between comparative proto and OE modelling input for row 2097 [Germanic/data/germanic-aligned-final.tsv:644-647; Germanic/docs/dossier-leek-2026.md:23-29]. The attested OE target is `lēac`, and the live FST already derives it. The alternative OE form `lēc` is real and philologically important, but it is background, not the live target [Germanic/docs/dossier-leek-2026.md:47-53,61-69,120-127].

The most useful row-specific background now sits outside DEV_NOTES in the dossier. It preserves Campbell §225 verbatim: “The smoothing of éa has still not taken place … in the second element of compounds, **-léac leek**. Smoothing to æ appears in **æc** also, … **læc** leek … **-léec** …” [Germanic/docs/dossier-leek-2026.md:71-80]. The dossier's working conclusion is cautious: both `lēac` and `lēc` are genuine OE forms; `lēac` is an attested WS form and therefore a defensible row target; `lēc` is the smoothed Anglian/late-WS co-form and a plausible ModE-pathway background, but adopting it as the row target would only make sense if the project later adds the same smoothing policy debated for `rēc` [Germanic/docs/dossier-leek-2026.md:82-89,120-127,344-390].

For row mechanics, the dossier's most important negative contrast is the i-stem non-target: it records `laukiz → līeċ`, which is exactly the path this row is **not** using. That matters because it keeps the current note from drifting into a false `*laukiz` analysis: the live row is an a-stem `*láukaz → lēac`, not an i-stem umlaut problem [Germanic/docs/dossier-leek-2026.md:33-39,211-226].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-37945-37955

- Source heading: `*rēc closure (row 859/ID 2151): triaged as intractable (Anglian smoothing relic)`
- Source line hint: `lines 37945-37955`
- Fragment type: `shared_background_only`
- Status: `current_for_background_only`
- Issue tags: `smoothing`; `ws_vs_anglian`; `lexical_diffusion`; `shared_with_reek`
- Recommended next use: `cite_only_as_shared_background_not_as_row_policy`
- Shared-with rows if relevant: `2151`

This is the only surviving direct DEV_NOTES mention that explicitly names the leek forms. In a note whose main target is `rēc`, DEV_NOTES says that an unconditional smoothing rule would regress ordinary West-Saxon `ēa` forms because smoothing was dialectally restricted and only “**lexically diffused into WS for a small set (lēac/lēc, rēc, -lēc)**” [Germanic/docs/DEV_NOTES.md:37945-37955]. For row 2097 this fragment is useful but limited. It supports the background claim that `lēac/lēc` belongs to the same small lexical-diffusion discussion as `rēc`, so `lēc` should remain visible as a real co-form. It does **not** amount to row-specific policy for 2097, because the surrounding note is about why the project refused to stretch the FST for `rēc`, not about changing or defending the live `lēac` row directly.

### DEV_NOTES:line-1901-2065

- Source heading: `Ach-Laut verification`; `Checkpoint 0 — baseline capture`; related 2025-11 German tracer notes
- Source line hint: `lines 1901-2065`
- Fragment type: `diagnostic_only_nonrow`
- Status: `diagnostic`
- Issue tags: `search_false_positive`; `german_pipeline`; `not_oe_row_evidence`
- Recommended next use: `exclude_from_row_argument_except_as_search_hygiene`
- Shared-with rows if relevant:

These entries repeatedly mention plain-string `laukaz`, but they are not about OE `lēac`. They are German stop-shift / ach-Laut diagnostics using `laukaz` as the proto control for German `Lauch`, e.g. tracer commands checking when `{*k}` becomes `{*x}` in the German pipeline [Germanic/docs/DEV_NOTES.md:1901-1909,1924-1938,1945-1966,1975-1980,1984-2065]. They matter here only as a warning for future search work: a grep hit on `laukaz` inside DEV_NOTES is usually German transducer debugging, not row-2097 evidence. Do not treat those notes as support for OE target selection, smoothing chronology, or palatalisation analysis for `lēac`.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES block for `leek / lēac` currently survives. The slice therefore should **not** invent one by promoting the reek material into direct row policy; the reek closure note is shared background only [Germanic/docs/DEV_NOTES.md:37945-37955].
- The main superseded point in the supporting dossier is chronological: the older reek-oriented formulation that smoothing “bleeds” palatalisation is explicitly rejected for `laukaz`. The corrected formulation is that smoothing is later, and that velar `k` survives because palatalisation never had reason to apply in the a-stem paradigm in the first place [Germanic/docs/dossier-leek-2026.md:138-156,202-232,393-407].
- The dossier's paradigm table is diagnostic support, not a live change request. Its value is to explain why velar `k` is expected without needing an exception: six of the eight a-stem cells are back-vowel environments, the nominative singular ends after the back offglide of `ēa`, and the row therefore does not need an i-stem or palatal rescue [Germanic/docs/dossier-leek-2026.md:238-324].
- The derivation traces are likewise diagnostic rather than argumentative literature. They show that the present cascade already does the desired work (`*láukaz → lēac`) and that neither `OEVelarPalatalization` nor `OEIUmlaut` changes the form in the live run [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2741-2760; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:15628-15655].

## Open questions for later work

- If the project later adopts a general Anglian-smoothing policy for the `rēc` problem, decide whether row 2097 should remain on attested WS `lēac` or be retargeted to equally attested smoothed `lēc`. For now the dossier's recommendation is still to keep `lēac`, because the row already matches and needs no repair [Germanic/docs/dossier-leek-2026.md:361-390,439-443].
- If a future final report wants the ModE pathway stated more tightly, it must choose between two background framings already preserved in the dossier: ModE `leek` from Anglian/late-WS `lēc`, or ModE `leek` from WS `lēac` via ordinary early-ME monophthongisation. That choice is downstream of the OE row and should not be collapsed into the current row state [Germanic/docs/dossier-leek-2026.md:45-53,111-127,344-357].
- A later corpus pass (the dossier specifically names DOEC as missing) could still clarify the distribution of `lēc` in late WS and compounds in `-lēc/-lēac`; until then, the conservative note should keep both forms visible but only `lēac` live [Germanic/docs/dossier-leek-2026.md:412-427].

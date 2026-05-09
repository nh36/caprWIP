---
row_id: 2079
concept: honey
counterpart: huniġ
proto: *xúnagą
protoform: *xúnagą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2079 honey / huniġ

## Current row state

- The live OE row reads `2079 | honey | huniġ | *xúnagą | *xúnagą | regular`; in the current TSV, `PROTO` and `PROTOFORM` coincide, but both are distinct from the attested OE target `COUNTERPART = huniġ` [Germanic/data/germanic-aligned-final.tsv:578-578].
- `oe_known_problems.tsv` has no live problem entry for this protoform or counterpart, and the coverage audit likewise classifies the row as a regular row with no note and no report requirement: `| 2079 | honey | huniġ | regular | no | - | - | - | none |` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:280-280].
- The current published derivation trace is an exact match, not an exception path: `PROTO: *xúnagą`, `EXPECTED: huniġ`, `OUTPUTS: huniġ`, with OE-side stages `*xúnægą > *xúnæg > *xúnæʤ > *xúneʤ > *xúniʤ` and orthographic outcome `huniġ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2474-2494].
- The older mismatch state still survives in historical notes. A pre-fix diagnostic list recorded `*xunăgą → hunaga (exp. huniġ)`, so any slice for this row has to distinguish current row state from older debugging snapshots [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:275-287].
- A second distinction also matters: DEV_NOTES cites earlier comparative reconstructions with retained `-ng-` (`*hunanga-`) or with NWGmc `*hunaga`, while the live row’s `PROTO`/`PROTOFORM` are already the dissimilated FST input `*xúnagą`; those are not interchangeable labels even when they belong to the same etymological chain [Germanic/docs/DEV_NOTES.md:12360-12378].

## Development-note summary

For this row, a genuinely row-specific DEV_NOTES block survives and remains the core authority, so this slice does not have to be reconstructed from scraps. The durable substance of that block is straightforward: the old mismatch was `hunag` versus expected `huniġ`, and the notes argued from Ringe/Taylor and Campbell that OE `huniġ` continues a suffixal chain `-ag > -æg > -eg > -ig`, followed by palatalization of final `g` to `ġ` after the new front vowel [Germanic/docs/DEV_NOTES.md:12344-12401]. That linguistic claim still matches the live trace exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2474-2494].

What is no longer current is the block’s immediate debugging posture. The 2026-03-19 note treats the row as an active mismatch and explains the repair in terms of `OEWeakTailReduction1`, sigma pollution, and a then-current input spelling `*xunăgą`; the row is now regular, and a later notation audit explicitly warns that the breve in the `ă g ą` slot was “wrong there relative to the literature” and not obviously load-bearing for `huniġ` [Germanic/docs/DEV_NOTES.md:12414-12478,20701-20713]. So the row-specific block survives, but its phonological content is current while parts of its implementation diagnosis are now historical/diagnostic.

Later shared DEV_NOTES material strengthens rather than displaces the row-specific block. In the withy analysis, Campbell’s `-ig < -eg < -æg < *-ag-` account is restated as general doctrine, and row 2079 is explicitly reused as the positive control: “row 2079 `*xúnagą → huniġ` already uses the correct suffix shape (`*-agą`, neuter)” [Germanic/docs/DEV_NOTES.md:26224-26314]. That later note is shared-background-only, but it confirms that the project’s settled view treats row 2079 as a correct regular exemplar of the `*-ag-` > OE `-iġ` pathway, not as an unresolved exception.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-12344-12401

- Source heading: `OE huniġ 'honey': The -ag > -ig Sound Change (2026-03-19)`
- Source line hint: `lines 12344-12401`
- Fragment type: `lexeme_specific`
- Status: `current core, with historical setup`
- Issue tags: `ag_to_ig`; `palatalization`; `nasal_dissimilation`; `row_specific`
- Recommended next use: `treat as primary row-level linguistic support`
- Shared-with rows if relevant: `none`

This is the main surviving row-specific fragment. It opens with the old mismatch snapshot — `PROTO: *xunăgą / EXPECTED: huniġ / OUTPUTS: hunag` — and then gives the source-backed derivation that still matters now [Germanic/docs/DEV_NOTES.md:12348-12356]. The note preserves R/T’s exact chain: “`PNWGmc *hunaga 'honey' (ON hunang, OHG honag) > *hunæg > *huneg > OE hunig`,” Campbell’s rule statement, “`Contrary to the usual change i > e, there is a change e > i before g. This is seen in the suffix -ig (< -eg < -æg), which except in the earliest texts appears as -ig...`,” and Campbell’s lexical reminder, “`punor thunder, wunap he dwells, hunig (older -æg) honey`” [Germanic/docs/DEV_NOTES.md:12360-12373]. The fragment also preserves the comparative etymological scaffolding: Kroonen’s “`*hunanga- m. 'honey' ... OE hunig n. 'id.' ... The n of the suffix was dissimilated in most Germanic languages`,” Kluge-Seebold’s `*hunanga-`, Orel’s `*xunăgą ... OE huni`, and Luick’s `huniz (aus *hunag)` [Germanic/docs/DEV_NOTES.md:12375-12389].

For row 2079, the controlling substance is the five-step chain copied in the analysis: `*xunangą` > `*hunaga` by nasal dissimilation, then `*hunæg`, then `*huneg`, then OE `hunig`, then orthographic/palatal `huniġ` [Germanic/docs/DEV_NOTES.md:12391-12401]. The row-specific block therefore supports three distinctions that should be kept explicit in later work: (1) earlier etymological preforms with `-ng-` are background, not the live FST input; (2) the OE vowel `-i-` is not analogical noise but the regular `-æg > -eg > -ig` outcome; and (3) the surface `ġ` belongs to the OE palatalized stage, not to the comparative protoform.

### DEV_NOTES:line-12414-12478

- Source heading: `FST Implication` / `Implementation` / `Verification`
- Source line hint: `lines 12414-12478`
- Fragment type: `resolved implementation history`
- Status: `resolved history; partly superseded diagnostically`
- Issue tags: `implementation_fix`; `oeweaktailreduction`; `sigma_pollution`; `verification`
- Recommended next use: `use for project chronology, not as sole current mechanism statement`
- Shared-with rows if relevant: `shared with other -ig-from--ag rows conceptually, but written here for row 2079`

This fragment records how the mismatch was understood and closed on 2026-03-19. DEV_NOTES states that the missing rule was “**unstressed `-ag > -ig` before final `g`**,” associates it with an existing `OELateUnstressedAgSuffix`, and then claims the rule failed because the input contained `{*ă}` instead of `{*a}` and because the earlier parallel definition of `OEWeakTailReduction1` suffered from “Foma sigma pollution” [Germanic/docs/DEV_NOTES.md:12416-12469]. It then preserves the verification probe verbatim: ``$ echo 'xunăgą' | flookup -i old_english.bin`` → ``xunăgą    huniġ  ✓`` and concludes `STATUS: FIXED (2026-03-19) — Mismatch count 58 → 57` [Germanic/docs/DEV_NOTES.md:12471-12478].

For present row work, this fragment is still valuable because it fixes the chronology of the repair and because the “fixed” status matches the live trace and coverage audit [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2474-2494; Germanic/docs/lexeme_reports/coverage_audit.md:280-280]. But its detailed bug diagnosis should be carried with caution, because later DEV_NOTES material questions whether the breve-marked slot was the real load-bearing factor at all [Germanic/docs/DEV_NOTES.md:20701-20713].

### DEV_NOTES:line-26224-26314

- Source heading: `withy analysis rechecking the OE -ig suffix`
- Source line hint: `lines 26224-26314`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `shared_suffix_background`; `campbell`; `positive_control`; `ag_suffix`
- Recommended next use: `reuse as comparative background for other *-ag- > -ig rows`
- Shared-with rows if relevant: `2296 (wīþiġ), and other OE -ig reflexes from *-ag-`

This later shared fragment matters because it restates the general suffix history in a form that explicitly includes `hunig`. DEV_NOTES quotes Campbell §275(7): “`The suffix -ig represents Prim. OE -æg (> -eg, e.g. CH haleg) and -ig... Examples are hunig honey, mōdig brave, hālig holy ...`,” then Campbell §376: “`there is a change *e > *i before *g. This is seen in the suffix -ig (< -eg < -æg)...`” [Germanic/docs/DEV_NOTES.md:26224-26234]. The row-specific value is not that this fragment discovers anything new about honey; it is that later DEV_NOTES treats `hunig` as the paradigm example proving that OE `-ig` here comes from PGmc `*-ag-`, not from a ja-stem or `*-ij-` reconstruction.

The fragment becomes row-explicit at the end: “`Parallel evidence in the TSV: row 2079 *xúnagą → huniġ already uses the correct suffix shape (*-agą, neuter). It works through the existing pgrmWord allow-list ... No allow-list change is needed.`” [Germanic/docs/DEV_NOTES.md:26311-26314]. For row 2079, that sentence is current shared-background support: it confirms that the live row is already in the morphologically correct shape for this derivation class and should not be “improved” into a ja-stem-style protoform.

### DEV_NOTES:line-20701-20713

- Source heading: `input-notation audit of breve-marked vowels`
- Source line hint: `lines 20701-20713`
- Fragment type: `diagnostic`
- Status: `diagnostic only`
- Issue tags: `notation_audit`; `breve_marker`; `superseded_mechanism_warning`
- Recommended next use: `use when explaining why older *xunăgą wording is not itself authoritative`
- Shared-with rows if relevant: `shared with other rows discussed in the input-notation audit`

This later audit is important because it explicitly downgrades part of the original row-specific implementation story. DEV_NOTES says the system had been treating `{*ă}` as if it encoded an active phonological fact, but the literature only supports vowel length distinctions; then it singles out the honey slot: “`the ă g ą slot ... uses breve, but Campbell §333 / R/T p.350 say the a in this position DOES front ... So the breve is wrong there relative to the literature — we get the right output for huniġ via a different pathway that bypasses the breve's intended shielding, suggesting the breve is not actually doing load-bearing work in that slot.`” [Germanic/docs/DEV_NOTES.md:20701-20713].

For row 2079, this means the old mismatch header `PROTO: *xunăgą` should be preserved as historical evidence, not treated as the stable philological representation of the row. The current live row’s `PROTO = PROTOFORM = *xúnagą` and the current successful trace are the operative state; the breve-marked input belongs to older debugging notation [Germanic/data/germanic-aligned-final.tsv:578-578; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2474-2494].

## Superseded or diagnostic material

- The old mismatch itself is superseded as live row state. DEV_NOTES once had `OUTPUTS: hunag`, and the older apocope investigation also logged `*xunăgą → hunaga (exp. huniġ)`, but the current published trace now gives `OUTPUTS: huniġ` and the coverage audit treats the row as ordinary `regular` coverage, not as an unresolved report row [Germanic/docs/DEV_NOTES.md:12348-12356,12471-12478; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:275-287; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2474-2494; Germanic/docs/lexeme_reports/coverage_audit.md:280-280].
- The original 2026-03-19 implementation diagnosis should be read as historically useful but not doctrinally final. It correctly captured that the row belonged to the `-ag > -ig` cluster and that the mismatch was resolved, but the later notation audit undercuts any stronger claim that the breve-marked `ă` itself was the decisive lexical fact for honey [Germanic/docs/DEV_NOTES.md:12438-12469,20701-20713].
- Orel’s cited OE form `huni` is diagnostic rather than controlling for this row. DEV_NOTES itself flags the discrepancy — “`Note: Orel gives OE as huni, not huniġ`” — but the same row-specific block otherwise aligns with Campbell, R/T, Kroonen, and the live FST trace in favor of `huniġ` as the operative OE target [Germanic/docs/DEV_NOTES.md:12383-12389; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2474-2494].

## Open questions for later work

- The live row uses the already dissimilated `PROTOFORM *xúnagą`, while DEV_NOTES also preserves earlier comparative preforms `*hunanga-` and `*hunaga`; if later row-packet work wants fuller etymological staging, decide whether the dossier should spell out the pre-dissimilatory `-ng-` layer more systematically without changing the FST-facing row input [Germanic/docs/DEV_NOTES.md:12360-12378].
- If other `*-ag- > -ig/-iġ` rows are sliced later, decide whether row 2079 should remain the project’s canonical positive control for that suffix class; later DEV_NOTES already uses it that way in the withy analysis [Germanic/docs/DEV_NOTES.md:26224-26314].
- Orel’s `huni` versus the project’s `huniġ` remains worth checking against raw dictionary citation practice and manuscript normalization, but nothing in the current evidence base justifies changing the live OE target away from `huniġ` [Germanic/docs/DEV_NOTES.md:12383-12389; Germanic/data/germanic-aligned-final.tsv:578-578].

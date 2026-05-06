---
row_id: 2158
concept: room
counterpart: rūm
proto: *rūmą
protoform: *rūmą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2158 room / rūm

## Current row state

- CONCEPT: `room` [Germanic/data/germanic-aligned-final.tsv:884-884]
- COUNTERPART: `rūm` [Germanic/data/germanic-aligned-final.tsv:884-884]
- PROTO: `*rūmą` [Germanic/data/germanic-aligned-final.tsv:884-884]
- PROTOFORM: `*rūmą` [Germanic/data/germanic-aligned-final.tsv:884-884]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:884-884]
- `oe_known_problems.tsv` currently has no row-local entry for row `2158`, lexeme `rūm`, concept `room`, or proto/protoform `*rūmą`; this row is not being tracked there as an OE exception or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- The current generated derivation trace is fully regular and already matches the target: `PROTO: *rūmą`, `EXPECTED: rūm`, `OUTPUTS: rūm`, with no PWGmc or NWGmc change and only `OE Heavy Syllable Nasal Apocope: *rūm` on the OE side before surface `Outcome: rūm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3690-3709].
- Coverage infrastructure shows no attached packet, research memo, or dossier for this row beyond the slice being created here; row `2158` appears in the coverage audit as `regular` with all linked-report fields empty [Germanic/docs/lexeme_reports/coverage_audit.md:329-329].

## Development-note summary

No securely attachable dedicated `room / rūm / *rūmą` dossier survives in `Germanic/docs/DEV_NOTES.md`. For row 2158, the usable authority is therefore shared phenomenon-level material plus the live row and current derivation trace. Those sources agree on the practical present-tense point: the row is a clean regular-control item with `PROTO = PROTOFORM = *rūmą` and OE target `rūm`, and the current grammar already derives that target directly by deleting final `*-ą` in OE without any earlier stem change, alternate paradigm cell, or analogical OE-facing protoform [Germanic/data/germanic-aligned-final.tsv:884-884; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3690-3709].

The most useful current DEV_NOTES anchor is the later rule inventory that explicitly lists `OEHeavySyllableNasalApocope: {*ą} → 0 || C _ .#.` and illustrates the chronology in which final `*ą` is removed before later tail-handling rules finish the derivation [Germanic/docs/DEV_NOTES.md:20998-21018]. That is exactly the kind of operation the row trace shows for `*rūmą > rūm`. A separate current DEV_NOTES comparison between `*xaubudą` and `*xemonų` reinforces the same distinction by saying that `héafod` works because it ends in `*ą`, handled by `OEHeavySyllableNasalApocope`, whereas `*ų`-final words belong to a different apocope story [Germanic/docs/DEV_NOTES.md:13312-13324]. For row 2158 this matters because it keeps the explanation precise: the row is not an instance of ordinary OE high-vowel apocope, and it is not a stem-class repair case; it is a straightforward final-`*ą` loss row.

The only DEV_NOTES passage that explains why this rule was added at all is older and explicitly archived, but it is still useful background for this lexeme. The archived discovery note says the project learned from mismatch analysis that heavy stems strongly favored loss of final `*-ą`, and it pairs that empirical finding with Hogg's generalization that neuter strong nouns show zero ending after heavy stems and `-u` after light stems [Germanic/docs/DEV_NOTES.md:1591-1621]. That note should not be over-read as a row-2158 problem history. Still, for `*rūmą` it remains securely relevant because the stem vowel is long `ū`, so the row falls squarely on the heavy-stem side of the contrast even under the older, narrower framing. The distinction among levels should therefore stay explicit but simple: comparative `PROTO = *rūmą`, OE-directed `PROTOFORM = *rūmą`, and selected OE `COUNTERPART = rūm`, all aligned with the current regular derivation [Germanic/data/germanic-aligned-final.tsv:884-884; Germanic/docs/DEV_NOTES.md:1595-1621,20998-21018].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-20998-21018

- Source heading: `Why the baseline rule is already correct`
- Source line or section hint: `lines 20998-21018`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_ą_loss`; `nasal_apocope`; `regular_pathway`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest current DEV_NOTES fragment for row 2158 because it gives the operative rule in explicit transducer-style form: `OEHeavySyllableNasalApocope: {*ą} → 0 || C _ .#.` [Germanic/docs/DEV_NOTES.md:21005-21009]. The worked derivation there is for an infinitive, not for `room`, but the lexical identity of the example is not the important part. What matters for this row is that DEV_NOTES treats final `*ą` deletion as a normal OE stage already built into the baseline analysis, not as a special repair. That is exactly what the current row trace shows for `*rūmą`, where the only OE-side rule named is `OE Heavy Syllable Nasal Apocope` and the surface result is immediately `rūm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3703-3709].

For row 2158 this fragment establishes two concrete points that later reporting should preserve. First, the row does not need a different `PROTOFORM`; the live `*rūmą` already feeds the current OE rule correctly. Second, the row is best treated as a control-case for final `*-ą` loss, because no competing current DEV_NOTES note proposes an analogical OE target, an oblique-cell substitution, or any other lexeme-specific workaround [Germanic/data/germanic-aligned-final.tsv:884-884; Germanic/docs/DEV_NOTES.md:20998-21018].

### DEV_NOTES:line-13312-13324

- Source heading: `Correction after testing`
- Source line or section hint: `lines 13312-13324`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_ą_loss`; `rule_scope`; `contrast_with_high_vowel_apocope`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This current fragment is useful because it distinguishes final `*ą` loss from superficially similar final-vowel cases. DEV_NOTES says `xaubudą → hēafod` works “because it ends in `*ą`, handled by `OEHeavySyllableNasalApocope`,” and immediately contrasts that with `xemonų → heofonu`, which fails because `*ų`-final forms are handled by `OEHighVowelApocope` instead [Germanic/docs/DEV_NOTES.md:13318-13324]. For row 2158, that shared comparison is directly relevant: `*rūmą` belongs to the `*ą`-final side of the split, so the correct explanation is final nasal-vowel apocope, not high-vowel apocope.

The fragment also helps keep the row's apparent simplicity from being described too vaguely. Saying merely that “the last vowel dropped” would flatten an important difference inside the cascade. DEV_NOTES preserves that difference explicitly, and the current `*rūmą > rūm` trace follows the `*ą`-deletion pathway rather than any `*-u/-ų` pathway [Germanic/docs/DEV_NOTES.md:13318-13324; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3699-3709].

### DEV_NOTES:line-1591-1621

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1621`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `heavy_stem`; `final_ą_loss`; `empirical_discovery`; `neuter_pattern`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This archived note is not a current row-specific authority, but it is still the most explicit DEV_NOTES explanation of why the project introduced a final-`*ą` apocope rule in the first place. It says mismatch analysis revealed that words with spurious final vowels were overwhelmingly heavy-stem forms and records the learned generalization that the same heavy/light conditioning that governs final `*-i/-u` also applied to `*-ą`; it then ties that discovery to Hogg's statement that neuter strong nouns show zero ending after heavy stems and `-u` after light stems [Germanic/docs/DEV_NOTES.md:1595-1612]. For `*rūmą`, whose stem is heavy because of long `ū`, that background is securely relevant even though the note is not about `room` specifically.

Later reviewers should use this fragment carefully. It explains the historical motivation of the rule and why a heavy-stem neuter like `*rūmą` is expected to lose its final nasal vowel, but it should not be cited as if row 2158 itself were once a flagged mismatch or as if this archived experiment were the row's governing current policy text [Germanic/docs/DEV_NOTES.md:1591-1621]. The governing current authority for the slice remains the live row plus the later rule inventory and current derivation trace [Germanic/data/germanic-aligned-final.tsv:884-884; Germanic/docs/DEV_NOTES.md:20998-21018; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3690-3709].

## Superseded or diagnostic material

- No securely attachable row-local superseded dossier currently survives for `2158`. The main thing to avoid is inflating the archived 2026-02-06 apocope discovery note into a `room`-specific repair history; it is shared rule background, not evidence that `rūm` remains disputed or mismatching [Germanic/docs/DEV_NOTES.md:1591-1621; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3690-3709].
- There is also a terminology drift inside DEV_NOTES that is harmless for this row but worth recording. The archived note frames the rule as heavy-syllable-conditioned, whereas a later current rule inventory writes it more broadly as `C _ .#.` for final `*ą` [Germanic/docs/DEV_NOTES.md:1617-1621,21005-21009]. For row 2158 both descriptions converge, because `*rūmą` ends in a consonant before the final nasal vowel and its stem is heavy anyway.
- The absence of any `oe_known_problems.tsv` entry matters here. Later writeups should not create an exception dossier merely because the slice is detailed; the row is presently a regular success case, not a tracked OE problem [Germanic/data/oe_known_problems.tsv:1-8; Germanic/data/germanic-aligned-final.tsv:884-884].

## Open questions for later work

- If a later cross-row review revisits final `*-ą` loss, it would be useful to reconcile the older “heavy-syllable nasal apocope” framing with the later current rule statement `C _ .#.`. Row 2158 itself is secure either way, but the terminology and scope should be made explicit for neighboring rows that are less obviously heavy than `*rūmą` [Germanic/docs/DEV_NOTES.md:1595-1621,21005-21009].
- If `dev_notes_slices/index.tsv` is updated later, the securely attachable current anchors are the explicit rule inventory (`20998-21018`) and the `*ą` vs. `*ų` contrast note (`13312-13324`); the archived discovery note (`1591-1621`) is best indexed only as background [Germanic/docs/DEV_NOTES.md:13312-13324,1591-1621,20998-21018].
- If a future packet or memo is created for this lexeme, keep the row-level distinction simple and explicit: `PROTO = PROTOFORM = *rūmą`, and the current OE derivation is just `*rūmą > rūm` by final `*ą` loss, with no evidence at present for a competing OE-directed protoform [Germanic/data/germanic-aligned-final.tsv:884-884; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3690-3709].

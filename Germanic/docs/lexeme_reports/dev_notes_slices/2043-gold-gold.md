---
row_id: 2043
concept: gold
counterpart: gold
proto: *gúlθą
protoform: *gúlθą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2043-gold-gold.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2043 gold / gold

## Current row state

- CONCEPT: `gold`
- COUNTERPART: `gold`
- PROTO: `*gúlθą`
- PROTOFORM: `*gúlθą`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T §5.1.3 p.171: *gulθa-/*gulda- may reflect Verner's alternation or regular PWGmc *lθ→*ld; either gives OE gold.` The note is explanatory rather than corrective: the row already derives successfully, but the project wants to preserve the historical ambiguity behind medial `-ld-` [Germanic/data/germanic-aligned-final.tsv:438].
- Packet evidence confirms that the live derivation is currently stable as `*gúlθą -> *gúldą -> *góldą -> gold`, with `PWGmcLThVoicing`, then regular NWGmc `u`-lowering before a non-high following vowel, then OE heavy-syllable nasal apocope [Germanic/docs/lexeme_reports/packets/2043-gold-gold.md:17-42].
- `oe_known_problems.tsv` has no entry for `*gúlθą` or `gold`, and `report_manifest.tsv` has no row-specific entry, which matches the row's present status as a solved regular derivation rather than a live modelling failure [Germanic/docs/lexeme_reports/packets/2043-gold-gold.md:11-13, 44-46; Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md:38-46].
- The memo's main philological caution should be preserved explicitly: three levels must stay distinct in later work — cognate-set proto `*gúlθą`, project input `*gúlθą`, and attested OE lemma `gold`. The intermediate `*gúldą` is useful as a diagnostic stage in the derivation, but it is **not** a replacement `PROTOFORM` [Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md:48-62, 72-83].

## Development-note summary

Row 2043 does have securely attachable DEV_NOTES authority, but it is narrow and should remain narrow. The controlling current discussion is the early note on PWGmc `*lþ > ld` and its overlap with Verner-style alternation at `DEV_NOTES:line-1334-1356`. That passage is important because it preserves exactly the same ambiguity that the live TSV note still carries: Ringe-Taylor allow OE `gold` to continue either `*gulþa- ~ *gulda-` or the ordinary West Germanic `*lþ > ld` development, and DEV_NOTES explicitly declines to force the row into one prehistoric story when both routes converge on the same Old English result [DEV_NOTES:line-1334-1356; @RingeTaylor2014, §5.1.3, p. 171].

The key replacement-note point is therefore operational, not speculative. DEV_NOTES says of `gold` and `feld`, “EITHER explanation yields the correct OE outcome,” and then states the standing project policy: where the regular sound change already gives the right answer, “we use it (gold, feld, fealdan, etc.)” (DEV_NOTES:line-1340-1355). For row 2043 that means the present workflow should keep `PROTO = *gúlθą`, keep `PROTOFORM = *gúlθą`, keep `DERIVATION_CLASS = regular`, and treat the row note as a reminder of historical ambiguity rather than as a trigger for data repair or a pending global Verner's-Law implementation.

The slice also needs to preserve the rest of the working derivation that DEV_NOTES itself leaves implicit. The packet and memo show that once the project keeps live input `*gúlθą`, the implemented rule stack already reaches the attested target without special pleading: `PWGmcLThVoicing` yields diagnostic `*gúldą`, regular NWGmc/OE `u > o` before a non-high following vowel yields `*góldą`, and OE heavy-syllable nasal apocope gives `gold` [Germanic/docs/lexeme_reports/packets/2043-gold-gold.md:17-42]. That is why the memo insists that `*gúldą` should remain only an intermediate stage. Promoting it into TSV `PROTOFORM` would erase the deliberate distinction between the inherited comparative headword and the model's current decision to let the existing `*lþ > ld` machinery do the work [Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md:48-62, 76-83].

The memo also preserves a second distinction that later report work should not rediscover from scratch: the OE side is secure. `gold` is an attested lemma, not a reconstructed convenience form; the row does not depend on a paradigm probe, an oblique-case substitute, or an analogical rescue. The only live explanatory issue is how to narrate prehistoric medial `-ld-` while keeping the attested OE lemma separate from the comparative `*gulþa- ~ *gulda-` background [Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md:64-89, 91-103]. In other words, this is a **regular but note-bearing** row.

Finally, the slice should preserve an explicit evidence-hygiene warning. The packet caught additional DEV_NOTES hits at `DEV_NOTES:line-2342-2346`, but those are a false positive caused by the string `gold` in a heading about modern English RP/non-rhotic normalization. They are not OE row authority and should never be mistaken for a second `gold` dossier [Germanic/docs/lexeme_reports/packets/2043-gold-gold.md:96-130; Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md:14-17]. Later workflow should therefore keep two facts in view at once: row 2043 **does** have one real current DEV_NOTES fragment on `*lþ > ld` / Verner overlap, and it also has a checked false positive that should remain diagnostic only.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1334-1356

- Source heading: `Ambiguous examples (rule OR Verner's Law)` plus `Scope of Verner's Law in the project`
- Source line or section hint: `lines 1334-1356`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `lth_voicing`; `verners_law`; `regular_derivation`; `protoform_stable`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2009, 2136`

This is the controlling current DEV_NOTES fragment for row 2043. It names `*gulþa- ~ *gulda- -> OE gold` explicitly, places the lexeme inside Ringe-Taylor's discussion of possible `*þ ~ *d` alternation, and then immediately resolves the project-side question by saying that for `gold` the implemented `*lþ > ld` rule is already enough because “EITHER explanation yields the correct OE outcome” [DEV_NOTES:line-1337-1355; @RingeTaylor2014, §5.1.3, p. 171]. For later report writing, this fragment should carry the main burden of the row note: preserve the ambiguity in prose, but do not treat the row as awaiting further repair.

### DEV_NOTES:line-2342-2346

- Source heading: `English gold IPA normalized to RP / non-rhotic baseline`
- Source line or section hint: `lines 2342-2346`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `false_positive`; `english_not_oe`; `search_noise`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This range is kept only as an evidence-control note. The heading contains the string `gold`, but the content is about modern English rhoticity cleanup for rows with orthographic `r`, the validator script added for that policy, and reruns against English TSV data (DEV_NOTES:line-2342-2346). None of that bears on OE `gold`, on `*gúlθą`, or on the `*lþ > ld` / Verner ambiguity. For row 2043 it should remain an explicit checked false positive so later packet or index cleanup does not silently imply a richer second DEV_NOTES dossier.

## Superseded or diagnostic material

Row 2043 has no superseded row-specific analysis in the stronger sense seen elsewhere in these slices. There is no abandoned `PROTOFORM`, no replaced target form, no derivation-class change, and no earlier mismatch state that the current note had to undo. The live row already works as a regular derivation, and the surviving DEV_NOTES authority is explanatory rather than corrective [Germanic/data/germanic-aligned-final.tsv:438; DEV_NOTES:line-1334-1356].

The diagnostic material is therefore mostly evidence hygiene. First, `DEV_NOTES:line-2342-2346` is an English-only false positive and should stay marked as such. Second, the packet's hit in `analysis/four_complex_tsv_items.md` comes only from the phrase “a gold coin,” not from discussion of OE `gold`; the memo is right to reject it as non-authoritative background [Germanic/docs/lexeme_reports/research_memos/2043-gold-gold.md:16-17, 38-46]. If later index cleanup suppresses reviewed-only false positives, preserve at minimum the explicit statement that row 2043 has one real current DEV_NOTES fragment plus one checked non-row false positive.

## Open questions for later work

- Decide whether the final lexeme report should quote the DEV_NOTES formulation “EITHER explanation yields the correct OE outcome” directly, since it captures the project's operational policy with unusual economy.
- Decide whether the final report should spell out the diagnostic intermediate `*gúldą` in a derivation table while also stating explicitly that it is **not** the TSV `PROTOFORM`.
- If central index integration later records reviewed false positives, keep `DEV_NOTES:line-2342-2346` as rejected English-only search noise rather than letting the heading string `gold` create a phantom second dossier for this row.

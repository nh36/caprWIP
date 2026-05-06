---
row_id: 2086
concept: knight
counterpart: cniht
proto: *kníxtaz
protoform: *knéxtaz
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2086-knight-cniht.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2086 knight / cniht

## Current row state

- CONCEPT: `knight`
- COUNTERPART: `cniht`
- PROTO: `*kníxtaz`
- PROTOFORM: `*knéxtaz`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: `Proto corrected to *knextăz per R/T vol.2 p.127, Orel p.220, Kluge-Seebold`; the row therefore already distinguishes a still-stale comparative `PROTO = *kníxtaz` from the corrected OE-facing `PROTOFORM = *knéxtaz` [Germanic/data/germanic-aligned-final.tsv:605-605; Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:13-19].
- Packet status: the compact derivation trace is already successful and explicitly runs `*knéxtaz -> cniht`, with `*xt` preserved and the orthographic output matching the target; the packet also records `_None_` for `oe_known_problems.tsv` and `_No manifest entry._` for the row [Germanic/docs/lexeme_reports/packets/2086-knight-cniht.md:11-13,17-43,45-47].
- Memo status: current repo behavior is described there as a half-cleaned row rather than a live derivational failure, because the corrected `PROTOFORM` and OE target are already aligned while `PROTO` and probably `DERIVATION_CLASS` still preserve older bookkeeping [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:13-19,45-46,69-79,95-101].
- No full knight-specific dossier or separate analysis memo was found elsewhere in repo materials used for the packet/memo workflow, so this slice has to carry the row-specific DEV_NOTES interpretation directly [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:48-48,101-101].

## Development-note summary

Current row-specific DEV_NOTES authority **does exist**, but it has to be split carefully into a still-current philological core and a superseded engineering history. The still-current core is the April 2026 `cniht` note's source dossier and singular/plural phonological interpretation: Ringe-Taylor, Orel, and Kluge-Seebold all support a reconstruction with `*e` (`*kneht/*knextaz/*knehta-`), not `*i`, and Campbell plus Brunner are cited to explain why singular `cniht` can stand beside plural `cneohtas` because `eo` or `io` contracts to `i` before `ht/hs` when no following back vowel blocks the change [Germanic/docs/DEV_NOTES.md:15435-15504]. That material still attaches securely to row 2086, even though the note itself accidentally labels the row as `2016` in its opening mismatch header [Germanic/docs/DEV_NOTES.md:15428-15433].

The live row state is therefore not a current argument for an analogically selected OE paradigm cell. `PROTOFORM = *knéxtaz` already matches the comparative reconstruction cited in the row note and the DEV_NOTES literature bundle, while the target remains the ordinary singular OE form `cniht` [Germanic/data/germanic-aligned-final.tsv:605-605; Germanic/docs/DEV_NOTES.md:15439-15449,15457-15463]. The memo is explicit that this makes the row look less like a genuine `early_analogy` case and more like stale metadata left over after a reconstruction cleanup: the current problem is that `PROTO` still says `*kníxtaz` and `DERIVATION_CLASS` still says `early_analogy`, not that the row still needs a special derivational rescue [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:52-60,67-79,95-99].

The superseded part of DEV_NOTES is the old repair program. In April 2026 the note diagnosed a mismatch `*knixtăz -> cnioht`, proposed correcting the TSV proto to `*knextăz`, and also proposed adding `{*io} -> {*i}` to `OEWsPalatalUmlaut` [Germanic/docs/DEV_NOTES.md:15428-15433,15466-15559]. That history should be preserved, but only as already-acted-on project chronology. The memo records that the live FST now maps both `*knéxtaz` and `*kníxtaz` to `cniht`, so the note's engineering directives are no longer open row policy; they are the explanation for how the repo got from the old mismatch state to the current partially cleaned row [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:26-32,45-46,69-79,101-101].

For later reporting, three layers must stay separate. Comparative/headword `PROTO` is still the stale column value `*kníxtaz`; row-driving `PROTOFORM` is the corrected `*knéxtaz`; OE target is singular `cniht` rather than plural `cneohtas` or some special oblique/paradigm substitute [Germanic/data/germanic-aligned-final.tsv:605-605; Germanic/docs/DEV_NOTES.md:15457-15504; Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:54-65]. DEV_NOTES currently supports the corrected reconstruction and the singular/plural phonological explanation, but it does **not** supply a securely current row-specific argument that the row should still be described as `early_analogy`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-15435-15504

- Source heading: `OE cniht 'knight, servant' — Palatal Umlaut Analysis`
- Source line or section hint: `lines 15435-15504`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `proto_reconstruction`; `palatal_umlaut`; `singular_plural_alternation`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the current row-specific authority that still matters. It preserves the comparative correction in quotable form: Ringe-Taylor give `"PGmc *kneht 'boy, servant'... OE cniht"` and `"cniht 'boy, servant' < *kneht (§2.5.3.1.3)"`, Orel gives `"*knextaz m. 'boy'"`, and Kluge-Seebold gives `"*knehta- 'Bursche, Knecht'"` [Germanic/docs/DEV_NOTES.md:15439-15449]. The same fragment then writes the regular singular path from corrected input to target—`*knextăz > *cneoxtăz > *cniht > cniht`—and anchors the singular/plural split in direct handbook quotations: Campbell says palatal umlaut applies in `cniht` but not in the plural `cneohtas`, while Brunner states that both `eo` and `io` become `i` before `ht/hs` when no following back vowel remains, again using `cniht` versus `cneohtas` as the example [Germanic/docs/DEV_NOTES.md:15457-15504]. For row 2086 this is the attachable philological core: corrected `*e`-reconstruction, singular OE `cniht`, and plural `cneohtas` as comparator/background rather than as the row target.

### DEV_NOTES:line-39278-39280

- Source heading: `Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39278-39280`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `xt_cluster`; `rule_scope`; `shared_control_case`; `verification_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2010,2102,2125,2140`

This shared verification fragment is worth keeping because it confirms how row 2086 is treated after the earlier cleanup. In the `*xt` preservation list, DEV_NOTES explicitly names `2086 *knéxtaz -> cniht` beside other `*xt` rows such as `*féxtaną -> feohtan` and `*náxti -> niht` [Germanic/docs/DEV_NOTES.md:39278-39280]. That matters because it shows the row is no longer being handled as a special unresolved mismatch: once the corrected `PROTOFORM` is in place, `cniht` functions as one of the ordinary control witnesses for the current `*xt` behavior.

### DEV_NOTES:line-42635-42638

- Source heading: `Risk audit` in the later `*x + vowel` contraction discussion
- Source line or section hint: `lines 42635-42638`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `risk_audit`; `x_plus_consonant`; `rule_non_applicability`; `comparator_background`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This later fragment is not a row-specific repair note, but it usefully fences off a tempting false connection. DEV_NOTES says `*séxs, *féxtaną, *wéxtiz, *knéxtaz all have *x + C, not *x + V, and so are unaffected` by the contraction environment under discussion [Germanic/docs/DEV_NOTES.md:42635-42638]. For row 2086 the value is purely contextual: `cniht` belongs to the preserved `*x + consonant` group, so later notes about `*x + vowel` contraction should not be mistaken for additional authority about this row's singular derivation.

### DEV_NOTES:line-15428-15559

- Source heading: `OE cniht 'knight, servant' — Palatal Umlaut Analysis`
- Source line or section hint: `lines 15428-15559`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `stale_row_number`; `resolved_rule_fix`; `old_mismatch`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment must be retained, but only as checked history. It opens with the stale mismatch state `Row: 2016`, `TSV proto: *knixtăz`, `TSV target: cniht`, `FST output: cnioht`, then diagnoses the missing `{*io}` branch in `OEWsPalatalUmlaut` and recommends two fixes: correct the protoform to `*knextăz` and add `{*io} -> {*i}` rules [Germanic/docs/DEV_NOTES.md:15428-15433,15506-15559]. The memo shows that both sides of that repair history have already been absorbed into the live repo: `PROTOFORM` is now `*knéxtaz`, and the grammar now derives `cniht` from both `*knéxtaz` and `*kníxtaz` [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:26-32,45-46]. So this fragment remains valuable for project chronology and for explaining why the row still has mixed metadata, but it is no longer current row policy.

## Superseded or diagnostic material

- The opening mismatch metadata inside the April 2026 `cniht` note is stale in two separate ways: the row number is `2016` rather than `2086`, and the active mismatch it describes (`*knixtăz -> cnioht`) is no longer the live row state once corrected `PROTOFORM = *knéxtaz` and the later `{*io}` handling are taken into account [Germanic/docs/DEV_NOTES.md:15428-15433,15519-15559; Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:26-32,45-46].
- The packet's exact-hit bundle is useful, but it already warns that the `Row: 2016` line is only "possibly stale or diagnostic evidence"; that warning should be preserved rather than silently erased, because raw search hits around `cniht` can otherwise mislead later row-level indexing [Germanic/docs/lexeme_reports/packets/2086-knight-cniht.md:183-197].
- No securely attachable current DEV_NOTES fragment justifies the live `DERIVATION_CLASS = early_analogy`. The memo's source audit instead argues that the row now behaves like an ordinary corrected-input singular derivation and that the analogy label may simply be stale bookkeeping left behind after the proto cleanup [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:52-60,67-79,95-99].
- The plural `cneohtas` material is current philological background, not evidence that row 2086 requires a paradigm probe or alternate `PROTOFORM`. The memo explicitly says a paradigm probe is not required here because the row is about the ordinary singular citation form, not about choosing a special oblique or plural cell [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:61-65,81-87].

## Open questions for later work

- Decide whether the live comparative `PROTO` column should be regularized from `*kníxtaz` to `*knéxtaz` so the headword-level proto no longer conflicts with the already-correct `PROTOFORM` and DEV_NOTES source bundle [Germanic/data/germanic-aligned-final.tsv:605-605; Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:95-99].
- Decide whether `DERIVATION_CLASS = early_analogy` should remain once the row is described strictly as corrected `*knéxtaz -> cniht`; current row-specific DEV_NOTES material supports the reconstruction and the singular/plural phonology, but not a live analogical paradigm-cell intervention [Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:58-60,79-99].
- If a final lexeme report is written before metadata cleanup, state explicitly that singular `cniht` is the row target while plural `cneohtas` is comparator/background evidence for the conditioning of `eo/io -> i` before `ht`; do not collapse the two into one undifferentiated "OE form" claim [Germanic/docs/DEV_NOTES.md:15480-15504; Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:61-65].
- If later documentation maintenance revisits DEV_NOTES itself, annotate the April 2026 `cniht` note so that its stale row number and already-resolved `{*io}` engineering TODO do not continue to look like open row-2086 work [Germanic/docs/DEV_NOTES.md:15428-15433,15525-15559; Germanic/docs/lexeme_reports/research_memos/2086-knight-cniht.md:100-101].

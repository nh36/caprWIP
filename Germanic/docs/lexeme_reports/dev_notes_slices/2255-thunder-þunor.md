---
row_id: 2255
concept: thunder
counterpart: þunor
proto: *θúnraz
protoform: *θúnraz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2255 thunder / þunor

## Current row state

- CONCEPT: `thunder` [Germanic/data/germanic-aligned-final.tsv:1261-1261]
- COUNTERPART: `þunor` [Germanic/data/germanic-aligned-final.tsv:1261-1261]
- PROTO: `*θúnraz` [Germanic/data/germanic-aligned-final.tsv:1261-1261]
- PROTOFORM: `*θúnraz` [Germanic/data/germanic-aligned-final.tsv:1261-1261]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1261-1261]
- This row does not currently split lexeme-level `PROTO` from row-specific `PROTOFORM`: both are the same inherited Germanic input `*θúnraz`, while `COUNTERPART` is the OE output `þunor`, not another proto-level label [Germanic/data/germanic-aligned-final.tsv:1261-1261].
- Coverage/report infrastructure still shows `2255 | thunder | þunor | regular | no | - | - | - | none`, so there was no packet, research memo, or report stem to reuse; the canonical row-based slice filename is therefore appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:394-394].

## Detailed development-note summary

The live row is uncomplicated in the TSV and thinly documented in DEV_NOTES. Row 2255 already treats `*θúnraz -> þunor` as a regular outcome, and DEV_NOTES does not preserve any thunder-specific mismatch dossier, repair proposal, or row-level reversal analogous to the longer notes for `sāwol` or `ræste` [Germanic/data/germanic-aligned-final.tsv:1261-1261]. That absence is itself part of the working note: the row's current status depends on shared handbook evidence rather than on a bespoke project fix.

The main reusable evidence is the Campbell quotation embedded in the later `sāwol` discussion. DEV_NOTES cites Campbell's list of “Normal OE forms” and includes `þunor` among the ordinary West Saxon outcomes: “Normal OE forms are fugol, tungol, cumbol, **sāwol**, nagel, æppel, segel, þunor, wundor, winter, fæger, æcer, hrefen, ofen, bēsum, māþum, westum” [@Campbell1959, §362; Germanic/docs/DEV_NOTES.md:22639-22643]. In that context the point is not thunder-specific etymology but a broader OE pattern: after the relevant stressed back-vowel environments, the parasitic vowel written `o` is treated as the normal West Saxon result, and `þunor` belongs to that ordinary class rather than to an exception file [@Campbell1959, §362; Germanic/docs/DEV_NOTES.md:22637-22643,22659-22660].

A second DEV_NOTES quotation preserves thunder only incidentally, but it is still worth keeping because it gives a direct handbook form rather than a project paraphrase. In the `hunig` note, DEV_NOTES quotes Campbell §118: “punor thunder, wunap he dwells, hunig (older -æg) honey” [@Campbell1959, §118; Germanic/docs/DEV_NOTES.md:12370-12373]. That passage was assembled for a different lexeme and should not be overread as a thunder analysis, yet it does confirm that Campbell uses thunder itself as an ordinary OE comparison form. For row 2255, its value is diagnostic and corroborative, not decisive.

Taken together, the safe current working conclusion is narrow but solid. `PROTO` and `PROTOFORM` remain identical here because no special paradigm-cell input is being selected, `COUNTERPART` remains `þunor`, and the row can stay `regular` because the only recoverable DEV_NOTES evidence aligns the output with Campbell's normal OE `-or` class rather than with a residual mismatch or a disputed lexical reconstruction [@Campbell1959, §§118, 362; Germanic/data/germanic-aligned-final.tsv:1261-1261; Germanic/docs/DEV_NOTES.md:12370-12373,22639-22643]. The note is therefore usable as a replacement working file, but it is still a thin/shared-evidence slice rather than a fully developed lexeme dossier.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-22637-22660

- Source heading: `Case 2 — *sáiwalō → sāwul (expected sāwol)`
- Source line or section hint: `lines 22637-22660`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_handbook_quote`; `parasite_vowel`; `normal_ws_o`; `thin_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2201`

This is the main attachable DEV_NOTES evidence for row 2255 even though the surrounding case is about `sāwol`, not thunder. The important carry-over is Campbell's exact quotation listing `þunor` among the “Normal OE forms” and DEV_NOTES' immediate gloss that, in these back-vowel stressed contexts, the parasite is normally `/o/` in West Saxon [@Campbell1959, §362; Germanic/docs/DEV_NOTES.md:22639-22643,22659-22660]. For thunder, this fragment does not create a new derivation story; it simply records that `þunor` already belongs to the project's shared handbook-backed normal class.

### DEV_NOTES:line-12370-12373

- Source heading: `OE huniġ 'honey': The -ag > -ig Sound Change`
- Source line or section hint: `lines 12370-12373`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `incidental_quote`; `campbell_form`; `non_row_specific`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment is only secondary support. DEV_NOTES was discussing `hunig`, not `þunor`, but it preserved Campbell §118's wording `punor thunder` as part of a direct quotation [@Campbell1959, §118; Germanic/docs/DEV_NOTES.md:12370-12373]. Later work may cite it as corroboration that Campbell treats thunder as an ordinary OE comparator, but it should not be mistaken for a thunder-specific project decision or a dedicated analysis of row 2255.

## Superseded or diagnostic material

- No thunder-specific residual-regression entry, repair proposal, or implementation reversal was located in `DEV_NOTES.md`; the row's thin documentation consists of shared quotations rather than superseded row-level engineering history [Germanic/docs/DEV_NOTES.md:12370-12373,22637-22660].
- The Campbell §118 quotation is diagnostic-only for this row because DEV_NOTES imported it to explain `hunig`, not to settle `þunor` [@Campbell1959, §118; Germanic/docs/DEV_NOTES.md:12370-12373].
- The strongest current authority remains the shared Campbell §362 quotation naming `þunor` as a normal OE form. That supports the live `regular` classification, but it is still only shared handbook evidence and not a dedicated lexeme note [@Campbell1959, §362; Germanic/docs/DEV_NOTES.md:22639-22643].

## Open questions for later work

- If row 2255 later receives a full lexeme report, add a dedicated etymological check for `*θúnraz` / `þunor` so the report does not rely entirely on quotations copied from notes written for other lexemes.
- Decide later whether thunder should stay documented only through Campbell's ordinary `-or` class or whether it should be linked explicitly to the separate `/uRCr/` dossier material on forms like `þunor / þunras`; this slice does not decide that question because the relevant evidence is not developed inside `DEV_NOTES.md`.
- If `dev_notes_slices/index.tsv` is revised later, the safest possible anchor would be the shared fragment `DEV_NOTES:line-22637-22660`; the `DEV_NOTES:line-12370-12373` quotation is too incidental to deserve first-line indexing on its own.

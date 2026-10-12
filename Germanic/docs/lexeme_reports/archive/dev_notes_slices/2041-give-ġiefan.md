---
row_id: 2041
concept: give
counterpart: ġiefan
proto: *gébaną
protoform: *gébaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2041-give-ġiefan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2041-give-ġiefan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2041 give / ġiefan

## Current row state

- CONCEPT: `give`
- COUNTERPART: `ġiefan`
- PROTO: `*gébaną`
- PROTOFORM: `*gébaną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `WS palatalized initial (R/T §6.4.1 rule 1: g before front vowel)`.
- Packet and memo status: both treat the row as a live **regular** derivation with no current mismatch; `oe_known_problems.tsv` has no entry for this lexeme and `report_manifest.tsv` has no row-specific manifest entry.
- Working philological caution: the comparative headword is the verbal stem `*geban-`, but this row's actual FST input is the infinitive `*gébaną`; the OE citation form represented here is the West Saxon infinitive usually written `giefan`, while the row's dotted `ġiefan` is the project's normalization of that palatal initial [@Kroonen2013, p. 173; @Campbell1959, §427; @RingeTaylor2014, §6.5.1; @ClarkHall1960, s.v. giefan].
- Working takeaway: the row should be explained as a regular WS infinitive whose `ie` comes from WS palatal diphthongization after initial palatalization, not from i-umlaut [@Campbell1959, §427; @RingeTaylor2014, §6.4.1, §6.5.1; @Fulk2018].

## Development-note summary

No dedicated DEV_NOTES mismatch dossier was written for row 2041 itself. The securely attachable DEV_NOTES authority instead survives as comparator material inside the `ġift` chronology note and a later implementation check on initial-palatal forms. That material is still worth carrying forward, but it should be presented as background for the regular derivation of `*gébaną > WS giefan / project ġiefan`, not as evidence that row 2041 ever needed its own repair note (DEV_NOTES:line-6496-6521; DEV_NOTES:line-11252-11255; DEV_NOTES:line-11309-11329).

The core DEV_NOTES chronology is straightforward and current. For `*gebaną`, the infinitival ending supplies no `i/j` trigger, so i-umlaut never raises the root vowel. The root still contains `e` when initial `g` palatalizes before that front vowel, and the surviving `e` then undergoes West Saxon palatal diphthongization to `ie`. DEV_NOTES states this in compact contrastive form: "`*gebaną` — the `*-ăną` infinitive has NO i-umlaut trigger ... Result: WS `giefan` (with diphthong) vs. Anglian `gefan` (without)" (DEV_NOTES:line-6496-6504). The packet and memo align this with the handbook account: `giefan` is the expected WS infinitive, while Mercian `for-geofan` and Northumbrian `geafa` belong to later dialect differentiation, not to a rival proto-analysis [@Campbell1959, §427; @RingeTaylor2014, §6.5.1].

The same DEV_NOTES passage matters because it preserves a compact handbook quotation that directly contrasts `giefan` with `gift`: "Examples of initial palatal sounds are: ... **gift** gift, gifre greedy, ginnan begin, **gefan (W-S giefan) give**..." (DEV_NOTES:line-6516-6518; [@Campbell1959, §427]). For row 2041 that quotation is useful because it shows exactly what the project now needs to say: `giefan` keeps `e` long enough for WS diphthongization because `*gebaną` lacks an umlaut trigger, whereas `gift` / `ġift` loses the relevant `e` too early. The positive point is therefore not that `giefan` is difficult, but that it functions inside DEV_NOTES as the regular control example for the chronology of initial palatalization plus WS diphthongization (DEV_NOTES:line-6476-6504; DEV_NOTES:line-11309-11329).

A later implementation note confirms the same thing in narrower project-history terms. After OE i-umlaut was moved earlier in the rule ordering, DEV_NOTES explicitly lists forms like "`*gēbanan → giefan`" among "other forms with initial palatals" that should still diphthongize because "these forms don't have i-umlaut triggers" (DEV_NOTES:line-11252-11255). That remark is not a fresh philological analysis of row 2041, but it is still useful evidence that the reordered chronology was checked against `giefan` and not treated as a regression. Combined with the memo, it supports a conservative row policy: keep `*gébaną` / `ġiefan` as a regular row, explain that dotted `ġ-` is a project normalization of handbook `giefan`, and avoid implying that the `ie` is an i-umlaut outcome [@Campbell1959, §427; @RingeTaylor2014, §6.4.1, §6.5.1; @ClarkHall1960, s.v. giefan].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6496-6521

Source heading: contrastive chronology for `*gebaną` inside the `ġift` investigation  
Source line or section hint: lines 6496-6521  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: ws_palatal_diphthongization;initial_palatalization;no_i_umlaut_trigger;comparator_material  
Recommended use: cite_in_final_report  
Shared with row IDs: 2040  
Text or paraphrase:
This is the main securely attachable DEV_NOTES authority for row 2041. It uses `*gebaną → giefan` as the positive control against `*geftiz → gift`: the infinitive has "NO i-umlaut trigger", so root `*e` survives long enough for initial palatalization and then WS palatal diphthongization, yielding "WS `giefan` (with diphthong) vs. Anglian `gefan` (without)" (DEV_NOTES:line-6496-6504). The later attestation paragraph preserves Campbell's compact contrast — "`gift` ... `gefan (W-S giefan) give`" — which remains the clearest handbook-sized statement of why `giefan` and `gift` diverge despite the same initial palatal environment (DEV_NOTES:line-6516-6521; [@Campbell1959, §427]).

### DEV_NOTES:line-11252-11255

Source heading: regression check after i-umlaut reordering  
Source line or section hint: lines 11252-11255  
Fragment type: phenomenon_context_for_lexeme  
Status: background  
Issue tags: ws_palatal_diphthongization;rule_ordering;regression_check;comparator_material  
Recommended use: keep_as_general_background  
Shared with row IDs: 2040  
Text or paraphrase:
This short implementation note confirms that later rule-order adjustments were not supposed to disturb `giefan`. DEV_NOTES lists forms like "`*gēbanan → giefan`" among "other forms with initial palatals" and states that the WS palatal-diphthongization rule should keep working "regardless of i-umlaut ordering" because these forms "don't have i-umlaut triggers" (DEV_NOTES:line-11252-11255). For row 2041 this is supporting project-history evidence, not a fresh lexical argument, but it is useful when explaining why the row stayed regular through the March 2026 chronology changes.

### DEV_NOTES:line-11309-11329

Source heading: corrected ordering note restating the `*gebaną` control case  
Source line or section hint: lines 11309-11329  
Fragment type: superseded_or_diagnostic_for_lexeme  
Status: diagnostic_only  
Issue tags: ws_palatal_diphthongization;i_umlaut;comparator_material;project_history  
Recommended use: use_as_project_history_only  
Shared with row IDs: 2040  
Text or paraphrase:
The correction note is still worth retaining because it restates the chronology in fully explicit rule-order terms: "`Without i-umlaut trigger (e.g., *gebaną 'to give')` ... `WS palatal diphthongization: *e → *ie after ġ` ... `Result: WS giefan with diphthong ie`" (DEV_NOTES:line-11313-11316). For row 2041 only that control-case portion is securely attachable. The broader fragment primarily belongs to row 2040 `gift`, especially once it moves on to speculative remarks about possible analogical West Saxon `gieft`; those later lines should not be imported as direct evidence about `giefan`.

## Superseded or diagnostic material

- DEV_NOTES contains stray sandbox/debug mentions of `*gebaną` in tracing and surface-filter logs, but those entries are tooling notes rather than lexical analysis or row policy, and they should not be cited as philological evidence for row 2041 (DEV_NOTES:line-1851-1890; DEV_NOTES:line-2338-2338).
- The 2026-03-17 correction note about `gift` is only partly reusable here. Its explicit `*gebaną` control case is current, but its later discussion of possible analogical WS `gieft` belongs to the `gift` row and should remain diagnostic-only for `give` (DEV_NOTES:line-11309-11355).
- No row-specific `oe_known_problems.tsv` entry survives, and no `report_manifest.tsv` entry exists. That absence matches the current row state: this is now a regular WS-target row, not an unresolved mismatch.

## Open questions for later work

- Decide whether the final lexeme report should quote handbook headwords as plain `giefan` while separately explaining project-normalized `ġiefan`, or whether a short normalization note is enough.
- Decide whether to include a brief WS vs. Anglian/Mercian contrast (`giefan` vs. `gefan/geafa/for-geofan`) in the final report or leave dialect variation to shared background prose.
- If central index integration later tracks shared comparator fragments carefully, record explicitly that the main DEV_NOTES evidence here is shared with row 2040 `gift`, not a standalone `give` dossier.

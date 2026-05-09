---
row_id: 2256
concept: tick
counterpart: ticca
proto: *tíkkô
protoform: *tíkkô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2256 tick / ticca

## Current row state

- CONCEPT: `tick`
- COUNTERPART: `ticca`
- PROTO: `*tíkkô`
- PROTOFORM: `*tíkkô`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 2256 now already encodes the retargeted OE form `ticca`, keeps both `PROTO` and `PROTOFORM` as `*tíkkô`, and labels the row `regular` rather than exceptional [Germanic/data/germanic-aligned-final.tsv:1265-1265].
- Live TSV note (quoted closely): `Retarget from gloss-Latinism *ticia* (Épinal/Erfurt/Corpus/Leiden) to the *ticca emendation explicitly proposed by Kroonen EDPG 2013 p. 556 s.v. *tīgan- ~ *tikkan-: "the OE gloss ticia is ambiguous; it has been emended to both *tīca and *ticca." See DEV_NOTES §17.44.` [Germanic/data/germanic-aligned-final.tsv:1265-1265].
- Existing row infrastructure: no existing packet or research-memo stem for row 2256 was found during the required filename check, so the canonical row-based slice filename is the correct choice for this pass.
- Known-problems status: no `oe_known_problems.tsv` entry was needed for this row; the live row is being treated as a resolved target-selection case rather than as a standing exception ledger item.
- Current DEV_NOTES authority status: the usable row-local material is concentrated in `§17.44`, especially the source audit at lines 40180-40203 and the target-choice diagnosis at lines 40209-40243; the immediately following plan/verification block is still useful project chronology, but its mismatch-count forecasts are now diagnostic rather than current policy [DEV_NOTES:line-40180-40279].

## Detailed development-note summary

Row 2256 should now be read as a regular OE row whose only real dispute was the choice of **COUNTERPART**, not the need for a new phonological workaround. The live row keeps `PROTO = *tíkkô` and `PROTOFORM = *tíkkô`; those fields therefore continue to represent the comparative headword and the actual FST input respectively, and they coincide in the current row. What changed is the OE side: the glossary spelling `ticia` is no longer being treated as the row's literal vernacular target, because Kroonen explicitly states that “the OE gloss *ticia* is ambiguous; it has been emended to both *tīca* and *ticca*” [@Kroonen2013, p. 556; Germanic/data/germanic-aligned-final.tsv:1265-1265].

The durable philological support for `ticca` is that the standard etymological tradition already licenses a short-vowel geminate reading of the OE form. DEV_NOTES preserves Kluge--Seebold's wording: “Aus wg. *tekkōn m./f., auch in ae. *ticcia*,” which treats the OE item as a geminate form even when transmitted in glossary spelling with final `-ia` [@KlugeSeebold2011, p. 1014; DEV_NOTES:line-40187-40199]. DEV_NOTES also notes that Orel gives the geminate stem `*tikkōn` and traces English `tick` directly to that branch, so the project is not inventing a one-off OE normalization merely to satisfy the FST [@Orel2003, p. 407; DEV_NOTES:line-40200-40203]. The precise comparative notation differs across sources (`*tekkōn`, `*tikkōn`, live-row `*tíkkô`), but for this slice the important point is narrower and secure: the evidence supports a **geminate OE emendation**, not reliance on the raw gloss spelling `ticia`.

DEV_NOTES is equally clear about why literal `ticia` should not remain the row target. The problem is not just spelling taste; it is morphological and phonological. The note states that gloss-final `-ia` is anomalous for OE morphology in this stem and is not the regular reflex of any inherited PGmc ending that the source dictionaries actually endorse [DEV_NOTES:line-40209-40216]. The probe evidence then reinforces that diagnosis: several plausible candidate inputs were tested, and none yielded literal `ticia`; the nearest live outcomes were `*tikkô -> ticca`, `*tikkōn -> ticce`, and `*tíkjō -> ticċ` [DEV_NOTES:line-40218-40226]. In other words, `ticia` behaves like a documentary gloss spelling that requires editorial interpretation, not like the phonological endpoint the row should force the grammar to generate.

Once that distinction is kept explicit, the present row policy is straightforward. DEV_NOTES says that FST output `ticca` is already “one of the two emendations that the standard etymological dictionaries ... explicitly license for the gloss *ticia*,” and that it matches Kluge--Seebold's `ticcia` apart from the latinizing final `-ia` flourish [DEV_NOTES:line-40227-40236]. The note then states the operational conclusion directly: this is a **target-choice mismatch, not a phonology bug**, so the row should be retargeted to `ticca` and left without any FST change [DEV_NOTES:line-40238-40243]. That conclusion remains current after the live TSV update. `DERIVATION_CLASS = regular` is therefore appropriate: the row now asks the grammar for an OE form that the grammar already produces and that the source tradition already permits [@Kroonen2013, p. 556; @KlugeSeebold2011, p. 1014; @RingeTaylor2014, §6.7.4; Germanic/data/germanic-aligned-final.tsv:1265-1265].

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-40180-40203

- Source heading: `Source audit — ambiguous gloss spelling and dictionary support`
- Source line or section hint: `lines 40180-40203`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `source_audit`; `gloss_emendation`; `geminate_reading`; `counterpart_selection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the key source-audit fragment for the row. It states that the gloss spelling is genuinely ambiguous between a long-vowel non-geminate reading `*tīca` and a short-vowel geminate reading `*ticca`, then preserves the Kluge--Seebold quotation “Aus wg. *tekkōn m./f., auch in ae. *ticcia*” and Orel's geminate-stem entry `*tikkōn` [@KlugeSeebold2011, p. 1014; @Orel2003, p. 407; DEV_NOTES:line-40180-40203]. For row 2256 this fragment remains current because it supplies the source basis for preferring a licensed OE emendation over the raw gloss spelling.

### DEV_NOTES:line-40209-40243

- Source heading: `Phonological problem with *ticia* as a literal target` / `FST output ticca: an attested-and-licensed OE form`
- Source line or section hint: `lines 40209-40243`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `literal_gloss_rejection`; `probe_results`; `target_choice`; `regular_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the decisive current fragment. DEV_NOTES says that gloss-final `-ia` is anomalous for OE morphology here, records the failed probe attempts to derive literal `ticia`, and then states that `*tikkô -> ticca` is both the live FST output and one of the dictionary-licensed emendations [DEV_NOTES:line-40209-40236]. The conclusion at lines 40238-40243 is the present row policy in compressed form: `ticca` is a target correction, not a phonological repair.

### DEV_NOTES:line-40244-40279

- Source heading: `Plan` / `Risk assessment` / `Verification`
- Source line or section hint: `lines 40244-40279`
- Fragment type: `lexeme_specific`
- Status: `diagnostic_only`
- Issue tags: `implementation_chronology`; `tsv_retarget`; `no_fst_change`; `stale_counts`
- Recommended next use: `use_to_explain_project_chronology`
- Shared with row IDs:

This block is still useful, but only as chronology. It records the intended TSV-only retarget, the reason no FST change was needed, and the expected mismatch-report effect once the row was updated [DEV_NOTES:line-40244-40279]. After the live TSV change, the qualitative part remains helpful (`ticca` already matched the grammar; only the row target was wrong), but the forecast counts should not be reused as if they were still live metrics.

## Superseded or diagnostic material

- Literal OE `ticia` should now be treated as documentary gloss spelling only. It remains relevant as the transmitted form that prompted the emendation question, but DEV_NOTES explicitly rejects it as the row's phonological target because the `-ia` ending is not a regular OE outcome for this stem [DEV_NOTES:line-40209-40216].
- The plan/verification note's mismatch totals (`14 -> 13`, `gemination_extra` `2 -> 1`) are no longer row policy. They belong to the historical moment before or during the retarget and should be cited only if later work needs project chronology rather than current lexeme analysis [DEV_NOTES:line-40269-40279].
- Kluge--Seebold's `*tekkōn` and Orel's `*tikkōn` are best read here as support for the geminate branch, not as a mandate to rewrite the live row's `PROTO` spelling inside this slice. The current evidence securely settles the OE **COUNTERPART**; it does not by itself force a separate change to the repo's present `PROTOFORM` normalization.
- DEV_NOTES mentions possible disagreement from Wiktionary, but that is diagnostic-only context. The live row should be governed by the cited etymological dictionaries and the project's regular-output check, not by whether a tertiary source prefers to cite the un-emended gloss spelling [DEV_NOTES:line-40258-40267].

## Open questions for later work

- If a packet or full lexeme report is later written, it should verify whether the live comparative spelling `*tíkkô` ought to remain as-is or be harmonized more explicitly with dictionary notations such as `*tikkōn` / `*tekkōn`. This slice does not argue for such a change; it only records that the current OE target `ticca` is source-licensed.
- If the row is indexed later, keep the attachment narrow and current: the index should foreground the source audit and target-choice diagnosis at `DEV_NOTES:line-40180-40243`, while treating the plan/verification block at `DEV_NOTES:line-40244-40279` as optional project chronology rather than as primary lexeme evidence.
- A later report could profitably add a short glossary-philology note naming the specific gloss witnesses (Épinal/Erfurt/Corpus/Leiden) and explaining why latinizing `-ia` spellings are poor row targets. The present slice keeps that point brief because DEV_NOTES already settles the operational decision without a new manuscript-level investigation.

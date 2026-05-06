---
row_id: 2087
concept: knob
counterpart: cnobba
proto: *knúppaz
protoform: *knúbbô
derivation_class: reconstructed_oe
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2087-knob-cnobba.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2087 knob / cnobba

## Current row state

- CONCEPT: `knob`
- COUNTERPART: `cnobba`
- PROTO: `*knúppaz`
- PROTOFORM: `*knúbbô`
- DERIVATION_CLASS: `reconstructed_oe`
- Live TSV note (abridged): “Unattested Old English cognate; likely *cnobba based on ME knob (Chaucer) and Frisian knobbe.” The live row therefore already separates cognate-set `PROTO = *knúppaz` from OE-facing derivational input `PROTOFORM = *knúbbô`; the row is not modelling an attested OE lemma, but a reconstructed OE target selected for the voiced branch behind Middle English `knob` [Germanic/data/germanic-aligned-final.tsv:609-609; Germanic/docs/lexeme_reports/packets/2087-knob-cnobba.md:5-10].
- `oe_known_problems.tsv`: no row-level entry [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/packets/2087-knob-cnobba.md:44-46].
- Manifest status: no manifest entry [Germanic/docs/lexeme_reports/packets/2087-knob-cnobba.md:11-13].
- Packet status: the packet is strong on current project state and on the April 2026 fix narrative: compact trace `*knúbbô -> cnobba`, no `oe_known_problems` entry, and direct extraction of the DEV_NOTES solution/implementation lines that changed the row away from the older mismatch [Germanic/docs/lexeme_reports/packets/2087-knob-cnobba.md:15-72].
- Memo status: the memo agrees that the live row currently encodes a reconstructed unattested OE form for the voiced branch, but argues that this is only current project policy, not settled OE philology, because repo-local lexicographic material reportedly supports OE `cnopp/cnoppa` on the voiceless branch instead [Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:13-20,52-67,71-99].

## Development-note summary

Current row-specific DEV_NOTES authority **does exist**, but it is narrower than the live row by itself can make it look. The January 2026 note and the dedicated April 2026 section are real row-level authority for the present project decision to keep `COUNTERPART = cnobba` as an unattested reconstructed OE form, to derive it from voiced weak-noun `PROTOFORM = *knúbbô`, and to keep `OE cnæp` out of this family [DEV_NOTES:line-1730-1734; DEV_NOTES:line-14058-14147]. Those notes are sufficient to explain why the live row is encoded as it is now.

What those DEV_NOTES fragments do **not** securely settle is the broader OE-source question raised by the research memo. The memo says repo-local reference files preserve OE `cnopp/cnoppa` evidence on the voiceless weak-noun branch and therefore treat current `cnobba` as a project choice aimed at the direct prehistory of Middle English `knob`, not as the best attested or lexically supported OE counterpart [Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:52-85,87-126]. For this slice, that distinction has to stay explicit: current DEV_NOTES authority supports the **live row policy**, but no securely attachable current DEV_NOTES fragment yet incorporates the memo's later warning that OE-side lexicography may favor `cnopp/cnoppa` instead.

The live DEV_NOTES story itself has two layers. First, the January note records the premise: OE `*cnobba` is unattested, first attested material is Middle English, the relevant family is a PGmc weak noun `*knubban-`, and `cnæp` belongs to different `*knapp-` material [DEV_NOTES:line-1730-1734]. Second, the April section records the engineering consequence: the old mismatch came from feeding the OE row with the wrong etymon, because `*knuppăz` yields `cnopp`, whereas voiced weak-noun `*knubbô` yields `cnobba`; DEV_NOTES therefore changed the row to the latter and logged direct FST confirmation `knubbô    cnobba` [DEV_NOTES:line-14062-14147]. That is the current row-level rationale that later report prose should preserve unless and until the memo's source-audit challenge is adopted elsewhere in the repo.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1730-1734

- Source heading: `Knob (2026-01-22)`
- Source line or section hint: `lines 1730-1734`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `unattested_target`; `source_basis`; `weak_noun`; `family_separation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This short note is the first current row-level authority for why the OE slot was handled as reconstructed rather than attested. DEV_NOTES says explicitly that knob is “**Unattested in Old English**; first attested in Middle English (Chaucer): ‘The knobbes sittynge on his chekes,’” then adds “Reconstructed PGmc weak noun: **`*knubban-`** (knob family)” and the exclusion note “**OE cnæp** (Kroonen p. 335) is **`*knapp-`**, not the knob etymon; keep families distinct” [DEV_NOTES:line-1731-1734]. Together with the live TSV note, this fragment explains why the row is still `reconstructed_oe` and why `cnobba` was chosen as a voiced-branch reconstruction rather than by collapsing the lexeme into the unrelated `cnæp` family [Germanic/data/germanic-aligned-final.tsv:609-609].

### DEV_NOTES:line-14068-14147

- Source heading: `OE cnobba 'knob': Unattested form (2026-04-06)`
- Source line or section hint: `lines 14068-14147`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `proto_vs_protoform`; `voiced_vs_voiceless_branch`; `reconstructed_oe`; `fst_verification`; `implementation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current DEV_NOTES fragment for the live row encoding. It preserves the comparative argument that there are “**two distinct etyma** in the ‘knob’ family”: voiceless strong `*knuppaz`, which yields regular OE `cnopp`, and voiced weak `*knubban-`, represented in the OE derivation as `*knubbô`, which yields regular OE `cnobba` [DEV_NOTES:line-14096-14118]. DEV_NOTES also quotes Kroonen on the related `*knab/ppan-` paradigm — “*knabō, gen. *knappaz ... split up into 1) *knabō, *knabbaz and 2) *knapō, *knappaz” — to justify treating voiced and voiceless formations as ablaut-related but distinct for row purposes [DEV_NOTES:line-14083-14092]. The practical conclusion is spelled out immediately afterward: “**Change the proto-form from `*knuppăz` to `*knubbô`.**” The note then records the row update and direct test `echo "knubbô" | flookup -i Germanic/fsts/old_english.bin` → `knubbô    cnobba` [DEV_NOTES:line-14125-14147]. For present documentation, this fragment is current authority for the live `PROTOFORM`/`COUNTERPART` pairing, not proof that the memo's later `cnopp/cnoppa` challenge has already been answered.

### DEV_NOTES:line-14062-14066

- Source heading: `OE cnobba 'knob': Unattested form (2026-04-06)`
- Source line or section hint: `lines 14062-14066`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_row_state`; `mismatch_history`; `wrong_input`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This opening problem statement should be kept only as labelled mismatch history. It records the pre-fix row state exactly as DEV_NOTES saw it on 2026-04-06: “**TSV row 2087:** `*knuppăz -> cnobba`,” “**FST output:** `*knuppăz -> cnopp`,” and the inherited row note that expected unattested `cnobba` [DEV_NOTES:line-14062-14066]. That wording is no longer current authority because the live row now distinguishes comparative `PROTO = *knúppaz` from derivational `PROTOFORM = *knúbbô` [Germanic/data/germanic-aligned-final.tsv:609-609]. Its value is diagnostic only: it preserves why DEV_NOTES concluded that the row had been fed the wrong branch.

### DEV_NOTES:line-2392-2394

- Source heading: `Old English data population`
- Source line or section hint: `lines 2392-2394`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `bulk_population_history`; `lack_of_oe_cognate`; `source_audit_limit`; `memo_conflict`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This bulk-population note is relevant only as project history and should not be quoted without context. It says that when the helper filled OE rows, `knob` was “marked ... as lacking an OE cognate per the etymology” [DEV_NOTES:line-2392-2394]. That statement fits the later January/April DEV_NOTES policy only if it is read narrowly as “lacking a securely adopted OE cognate for the voiced branch behind Middle English `knob`.” Read broadly, it is misleading, because the research memo reports repo-local evidence for OE `cnopp/cnoppa` on the voiceless branch and treats that as a real outstanding source-audit problem for this row [Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:52-85,87-126].

## Superseded or diagnostic material

- The securely attachable superseded row state is the old mismatch framing `*knuppăz -> cnobba` versus FST `cnopp`; that material remains useful because it explains exactly why April 2026 changed the row's OE-facing input to `*knubbô`, but it is not the live row state anymore [DEV_NOTES:line-14062-14066; DEV_NOTES:line-14125-14147].
- The March/April progress-log entry “TSV fixes: dile, lappa, cnobba” is useful only as chronology showing when row 2087 entered the resolved bucket; it does not add lexeme-specific reasoning beyond the dedicated section [DEV_NOTES:line-10393-10395].
- The bulk note that `knob` lacked an OE cognate is diagnostic/background only. In light of the memo, it is misleading if uncontextualized, because present repo materials distinguish unattested voiced `*cnobba` from lexically supported voiceless OE `cnopp/cnoppa` rather than simply “OE absent” [DEV_NOTES:line-2392-2394; Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:71-99].
- No securely attachable current DEV_NOTES fragment yet integrates the memo's repo-local lexicographic evidence for `cnopp/cnoppa`. That means the current slice should preserve the April 2026 `cnobba` rationale as live row policy while also stating plainly that the philological question may still be open at the memo level [Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:62-99,117-126].

## Open questions for later work

- Decide whether later report work should continue to privilege the direct prehistory of Middle English `knob` (`*knúbbô -> cnobba`) or instead adopt the memo's claim that the best OE counterpart in repo-local lexicography is voiceless `cnopp/cnoppa` [Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:87-126].
- If the live row is retained, keep the three-way distinction explicit in any final report: cognate-set `PROTO = *knúppaz`, OE derivational `PROTOFORM = *knúbbô`, and OE target `COUNTERPART = cnobba` are not interchangeable labels [Germanic/data/germanic-aligned-final.tsv:609-609; Germanic/docs/lexeme_reports/research_memos/2087-knob-cnobba.md:56-60].
- If later editors adopt the memo's `cnoppa` recommendation, the January and April DEV_NOTES notes will need explicit recontextualization rather than silent removal, because they remain the checked history of why the row was first converted into a `reconstructed_oe` voiced-branch solution [DEV_NOTES:line-1730-1734; DEV_NOTES:line-14125-14147].

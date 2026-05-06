---
row_id: 2142
concept: nine
counterpart: nigon
proto: *nígun
protoform: *nígun
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/dossiers/g-palatalisation-conditioning.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2142 nine / nigon

## Current row state

- CONCEPT: `nine`
- COUNTERPART: `nigon`
- PROTO: `*nígun`
- PROTOFORM: `*nígun`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 2142 already encodes the post-innovation northern / Ingvaeonic input in both proto columns, not older PGmc `*néwun`; the row is therefore no longer an open mismatch entry but a resolved regular derivation from `*nígun` to `nigon` [Germanic/data/germanic-aligned-final.tsv:823-823; Germanic/docs/DEV_NOTES.md:42778-42804,42999-43005].
- `oe_known_problems.tsv`: no row-specific problem entry is present for this lexeme; current project status treats the row as solved rather than as a live exception bucket item [Germanic/data/oe_known_problems.tsv:1-8].
- Packet / memo status: no row-specific packet or research memo is currently present under `Germanic/docs/lexeme_reports/packets/` or `.../research_memos/`; this slice therefore needs to stand as the self-sufficient working note for the row.
- Live trace status: the published derivation-class trace now shows `PROTO: *nígun`, `EXPECTED: nigon`, `OUTPUTS: nigon`, with the only visible OE-stage change being medial unstressed `u > o` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3467-3486].
- Repo-local reference extracts checked for this slice: Ringe-Taylor's explicit northern-WGmc reconstruction `*nigun`, Campbell's use of `nigon` as the canonical velar-retention example before a back vowel, Campbell's Northumbrian `hundnéontig` note, Kroonen's `*niwun` + velarization statement, and Bülbring's treatment of `nigon` as a pre-OE velar form [docs/references/ringe_taylor_linguistic_history_vol2.txt:9665-9676; docs/references/campbell_old_english_grammar.txt:11308-11313,19056-19057; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20445-20449; docs/references/bulbring_altenglisches_elementarbuch.txt:4430-4434].

## Development-note summary

Row 2142 now has securely attachable current DEV_NOTES authority. The controlling decision is that the row should no longer feed the OE cascade with older PGmc `*néwun`, because the cascade correctly turns that input into `nēowon`, not `nigon`; the older form remains important only as comparative / superseded project history [Germanic/docs/DEV_NOTES.md:42762-42780,42915-42918]. The live row instead uses NSGmc / Ingvaeonic `*nígun` as both `PROTO` and `PROTOFORM`, because the project has decided to model the already-innovated pre-OE stage directly rather than force the cascade to create medial `-g-` from inherited `-w-` [Germanic/docs/DEV_NOTES.md:42778-42804,42962-43005].

The PROTO / PROTOFORM / OE-target distinction still matters even though the two proto columns now coincide. `PROTO = *nígun` is not being used here as a PIE-to-PGmc headword; it is the row's adopted **stage-appropriate northern-WGmc / Ingvaeonic input**, chosen because that is the earliest securely usable form for the OE derivation the project wants to test [Germanic/docs/DEV_NOTES.md:42779-42798,42964-42968; docs/references/ringe_taylor_linguistic_history_vol2.txt:9665-9676]. `PROTOFORM = *nígun` is the exact same form because no additional row-level paradigm-cell selection is needed once the pre-OE innovation is accepted [Germanic/docs/DEV_NOTES.md:43001-43005]. The OE target `nigon`, by contrast, is the output after ordinary OE-internal development, above all medial unstressed `u > o`; the current trace makes that explicit [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3476-3486].

DEV_NOTES is explicit that this is **not** a bow / shove type paradigm-cell workaround and not a generic “irregular exception” shrug. The dossier repeatedly classifies `nigon` as a shared NSGmc / Ingvaeonic innovation: OE `nigon`, OS `nigun ~ nigon`, and OFris `nigun ~ niugun ~ niogen` stand together against Goth./ON/OHG forms without medial `g` [Germanic/docs/DEV_NOTES.md:42769-42773,42875-42880,42941-42954]. Ringe-Taylor explicitly reconstruct `northern WGmc *nigun`, and Campbell uses `nigon` as a standard example where inherited velar remains velar before a following back vowel [docs/references/ringe_taylor_linguistic_history_vol2.txt:9665-9676; docs/references/campbell_old_english_grammar.txt:11308-11313]. Bülbring likewise presupposes a pre-OE velar stage when he groups `nigon` with forms where `iu` is levelled back to `i` before velars [docs/references/bulbring_altenglisches_elementarbuch.txt:4430-4434].

At the same time, DEV_NOTES deliberately separates **reconstructable current row authority** from unresolved comparative scholarship. Kroonen's formulation is the strongest pro-sound-law statement preserved locally: “The velarization of the *w in West Germanic ... points to a secondary form *niwun with a raised vowel, as velarization only occurred between two high vowels of which one was rounded” [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20445-20449]. But the same DEV_NOTES dossier also keeps the modern skepticism visible: Ringe-Taylor say “No convincing explanation for the shape of ‘nine’ has been advanced,” while Fulk treats the NSGmc `ʒ/g` as inorganic rather than as a regular productive sound law [Germanic/docs/DEV_NOTES.md:42837-42841,43031-43115; docs/references/ringe_taylor_linguistic_history_vol2.txt:9673-9676]. The project's conservative solution is therefore to adopt the post-innovation protoform in the row and **not** to add Bugge-style velarization as a general cascade rule [Germanic/docs/DEV_NOTES.md:42787-42793,43092-43115].

A second row-specific distinction also has to stay explicit. After the row was changed to `*nígun`, the cascade briefly produced `niġon`, because the inherited-`g` palatalization rule was too broad after a front vowel [Germanic/docs/DEV_NOTES.md:43131-43175]. DEV_NOTES first proposed an over-narrow repair, then immediately retracted that proposal after a handbook canvass. The durable current principle is Campbell / Ringe-Taylor / Hogg / Brunner / Bülbring's shared rule: after a front vowel, inherited `g` palatalizes unless the following environment contains a back vowel; therefore `nigon` with `i_g_o` must remain velar, while preconsonantal and word-final cases like `næġl`, `seġl`, `weġ` still palatalize [Germanic/docs/DEV_NOTES.md:43224-43345; docs/references/campbell_old_english_grammar.txt:11308-11313]. The live trace's plain `nigon` confirms that the row is now aligned with that corrected conditioning [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3467-3486].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1451-1454

- Source heading: `Project Status (as of 2026-04-30) — research phase complete`
- Source line or section hint: `lines 1451-1454`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `row_policy`; `project_history`; `protoform_vs_proto`; `palatalization_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

The April-30 project-status recap is short, but it is authoritative about what survived into the closed research state. It lists `*néwun → nigon` as a completed item and says the project adopted NSGmc / Ingvaeonic `*nigun` at the TSV level “after a thorough Bugge's-velarization controversy review”; the very next line pairs that with the `*g`-palatalisation conditioning audit [Germanic/docs/DEV_NOTES.md:1451-1454]. For row 2142 this fragment is useful because it compresses the whole current policy into one statement: older `*néwun` mismatch history is closed, post-innovation `*nigun` is live row metadata, and the later `niġon` side-problem belongs to the same already-resolved closure phase rather than to an open research thread.

### DEV_NOTES:line-42760-43005

- Source heading: `§17.50 — *néwun → nigon* mismatch dossier` / `§17.50.1 — Source canvass dossier`
- Source line or section hint: `lines 42760-43005`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_vs_proto`; `nsgmc_stage_input`; `ingvaeonic_isogloss`; `row_policy`; `literature_survey`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-specific fragment. DEV_NOTES starts from the concrete mismatch: TSV `*néwun` produced `nēowon`, because the cascade treated the form as a regular `*ew` item and then applied medial `u > o` [Germanic/docs/DEV_NOTES.md:42762-42767,42915-42918]. It then states the decisive reclassification: the problem is not stress placement, not a hidden paradigm cell, and not a local OE quirk, but a **shared NSGmc / Ingvaeonic consonantal innovation** in which OE, OS, and OFris have medial `g` where Goth./ON/OHG do not [Germanic/docs/DEV_NOTES.md:42769-42780,42941-42954]. The source canvass makes that attachable rather than speculative: Ringe-Taylor explicitly give “northern WGmc *nigun” [docs/references/ringe_taylor_linguistic_history_vol2.txt:9665-9676]; Bülbring's treatment presupposes pre-OE `nigon` as a velar form [docs/references/bulbring_altenglisches_elementarbuch.txt:4430-4434]; and Kroonen's headword discussion points to secondary `*niwun` feeding velarization [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20445-20449]. The recommendation section then makes the row-level consequence explicit: adopt Option A, replace older PGmc `*newun` with NSGmc / Ingvaeonic `*nigun`, and let the existing cascade derive `nigon` by ordinary medial `u`-lowering only [Germanic/docs/DEV_NOTES.md:42962-43005]. This is exactly why the live row now has `PROTO = PROTOFORM = *nígun` and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:823-823].

### DEV_NOTES:line-43007-43115

- Source heading: `§17.50.2 — Bugge's-law controversy report`
- Source line or section hint: `lines 43007-43115`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `literature_controversy`; `sound_change_scope`; `engineering_policy`; `minority_hypothesis`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This fragment preserves the part of the dossier that explains **why** the project stopped at stage-specific protoform replacement rather than general rule implementation. DEV_NOTES openly records the split in scholarship. On one side stand Kroonen and parts of the older Junggrammatiker tradition, who treat intervocalic `*w > ʒ/g` in high-vowel environments as a regular conditioned change; Kroonen's wording is the sharpest local statement of that view [Germanic/docs/DEV_NOTES.md:43018-43030; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20445-20449]. On the other side stand the modern handbook authorities that matter most for this project: Ringe-Taylor say “No convincing explanation for the shape of ‘nine’ has been advanced,” and Fulk calls the NSGmc `ʒ` “inorganic” and explicitly non-phonological [Germanic/docs/DEV_NOTES.md:43031-43052,43090-43115; docs/references/ringe_taylor_linguistic_history_vol2.txt:9673-9676]. The DEV_NOTES recommendation is correspondingly conservative and remains current for row 2142: **do not implement Bugge's velarization as a productive cascade rule; instead lexicalize the already-innovated form in the row input** [Germanic/docs/DEV_NOTES.md:43092-43115]. This fragment should stay easy to extract because it separates securely current row policy from still-open comparative debate.

### DEV_NOTES:line-43129-43213

- Source heading: `§17.50.3 — Implementation result and a follow-on finding: *g palatalisation before back vowels`
- Source line or section hint: `lines 43129-43213`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `palatal_extra`; `rule_scope`; `niġon_bug`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment is worth preserving because it records the real intermediate bug that arose **after** the row had already been fixed at the protoform level. DEV_NOTES says the updated input `*nígun` briefly produced `niġon`, identifies the over-greedy `OEVelarPalatalization` clause as the cause, and proposes a first repair limited to word-final and front-vowel-following environments [Germanic/docs/DEV_NOTES.md:43131-43213]. The diagnostic value is real: it shows that the row's remaining problem was no longer `*w` versus `*g`, but the later OE handling of inherited `g` after front vowels. But this specific repair proposal is **not** current authority, because the very next DEV_NOTES section retracts it for missing preconsonantal palatalization cases such as `næġl` and `seġl` [Germanic/docs/DEV_NOTES.md:43296-43315]. Later writers should therefore use this fragment only to explain the superseded `niġon` stage in project history.

### DEV_NOTES:line-43214-43361

- Source heading: `§17.50.4 — Scholarly conditioning of the OE *g palatalisation: source canvass`
- Source line or section hint: `lines 43214-43361`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `g_palatalization`; `right_context`; `velar_retention`; `oe_phonology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the current controlling follow-up to the brief `niġon` bug. DEV_NOTES canvasses Campbell, Ringe-Taylor, Hogg, Sievers-Brunner, and Bülbring and concludes that inherited `g` after a front vowel palatalizes iff the right context is **not** a back vowel; thus word-final, preconsonantal, and front-vowel-following environments palatalize, while `front-V _ back-V` remains velar [Germanic/docs/DEV_NOTES.md:43224-43345]. `nigon` is one of the handbook's own minimal-pair examples: Campbell's wording is explicit that velars remain when there is a back vowel “either before or after them, e.g. ... wegas ways, nigon nine, þinga g.p. things” [Germanic/docs/DEV_NOTES.md:43229-43240; docs/references/campbell_old_english_grammar.txt:11308-11313]. The same fragment also retracts the too-narrow two-clause fix from §17.50.3 because it would wrongly depalatalize preconsonantal cases licensed by the same handbook tradition [Germanic/docs/DEV_NOTES.md:43296-43315]. For row 2142 this is not just general phonology background: it is the reason the row's live output is now correctly `nigon`, not `niġon`, while other inherited-`g` rows can still keep palatal outcomes in their own environments [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3467-3486].

## Superseded or diagnostic material

The most important superseded material is the original `*néwun → nēowon` mismatch framing. It remains necessary project history because it preserves the older PGmc comparative form and shows exactly what the cascade does when no NSGmc innovation is encoded; but it is no longer live row authority once `*nígun` has been adopted in the TSV [Germanic/docs/DEV_NOTES.md:42762-42780,42915-42918; Germanic/data/germanic-aligned-final.tsv:823-823].

A second superseded layer is the first `niġon` repair note in §17.50.3. That note correctly localized the new problem to over-broad `g`-palatalization, but its specific repair proposal is no longer safe to cite because §17.50.4 retracts it after checking preconsonantal evidence from Campbell, Ringe-Taylor, and Bülbring [Germanic/docs/DEV_NOTES.md:43131-43213,43296-43345]. The row should therefore preserve `niġon` only as transient diagnostic history, not as a serious alternative target.

Potentially misleading material also includes any prose that silently equates live row `PROTO = *nígun` with the older comparative headword `*néwun`. DEV_NOTES itself does not do that after the final decision: the whole point of Option A is to keep PIE/PGmc etymology and immediate OE-cascade input separate [Germanic/docs/DEV_NOTES.md:42797-42804,42964-42968]. Later reporting should keep the older form visible, but only as superseded upstream history or as comparative etymology outside the live row metadata.

## Open questions for later work

- If a later report wants fuller comparative coverage, check the external items DEV_NOTES itself lists for follow-up—especially Kroonen 2011b, Ross & Berns 1992, Stiles 1985–86, and Frisian-specific numeral work—before saying anything stronger than the current conservative “stage-specific `*nigun`, productive rule not adopted” policy [Germanic/docs/DEV_NOTES.md:43117-43126].
- Decide whether a future final lexeme report should include a compact contrast table showing the three levels explicitly: older PGmc comparative `*néwun` (superseded row input) → regular `nēowon`, adopted NSGmc `*nígun` (live `PROTO/PROTOFORM`) → regular `nigon`, and transient over-palatalized `niġon` as resolved diagnostic history [Germanic/docs/DEV_NOTES.md:42762-42804,43131-43345].
- If the slice is later indexed more granularly, keep the Bugge-controversy fragment and the g-palatalization-conditioning fragment separate; they answer different questions for the row, namely why `*nígun` was adopted and why that input now surfaces as velar `nigon` rather than palatal `niġon`.

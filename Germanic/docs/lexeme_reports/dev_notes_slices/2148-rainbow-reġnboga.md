---
row_id: 2148
concept: rainbow
counterpart: reġnboga
proto: *régna-bùgô
protoform: *régna-bùgô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2148 rainbow / reġnboga

## Current row state

- CONCEPT: `rainbow`
- COUNTERPART: `reġnboga`
- PROTO: `*régna-bùgô`
- PROTOFORM: `*régna-bùgô`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 2148 currently uses grave-marked compound `*régna-bùgô` for Old English and targets `reġnboga`; the daughter-language companion rows now likewise carry the same grave-marked compound, while the older breve-marked form survives only in historical DEV_NOTES discussion [Germanic/data/germanic-aligned-final.tsv:845-848].
- `oe_known_problems.tsv`: no row-local or lexeme-local problem entry for `2148`, `*régna-bùgô`, `*regnă-bugô`, `reġnboga`, or `rainbow` [Germanic/data/oe_known_problems.tsv:1-8].
- Lexeme-report infrastructure: `coverage_audit.md` currently lists row 2148 with packet, memo, dossier, and authority slots all empty (`-` / `none`), so the metadata fields above stay blank rather than pointing to neighboring rows' packets that only quote this material incidentally [Germanic/docs/lexeme_reports/coverage_audit.md:323-323].

## Development-note summary

Current DEV_NOTES authority for row 2148 is real, but it is split across two phases that have to be kept distinct. The earlier phase is the row-specific repair note from 2026-04-11, written when the grammar still used the compound input `*regnă-bugô`. That note diagnoses the then-current bad output `reġnafoga` against target `reġnboga` and says the failure had two parts: the linking vowel survived when it should have syncopated, and `*b` lenited to `f` when it should have remained a stop [Germanic/docs/DEV_NOTES.md:16807-16824]. The note then ties the missing deletion to Ringe & Taylor's general syncope statement that “Nonhigh *æ ... and *e ... were usually lost regardless of the preceding syllable's weight, so long as the preceding syllable was stressed,” and it writes out the derivational chain explicitly: `*regnă-bugô > *regna-bugô > *regnæ-bugô > *regn-bugô > reġnboga` [Germanic/docs/DEV_NOTES.md:16825-16855]. For replacement working notes, that chain is still worth preserving because it explains exactly why the OE compound loses the linking vowel and why the surviving consonant is `b`, not `f`.

The other indispensable point from that first cluster is that the stop consonant is not an extra exception. DEV_NOTES says directly that B-allophony should apply “only after vowels,” so once syncope removes the linking vowel, the `b` of the second member is no longer postvocalic and therefore stays a stop [Germanic/docs/DEV_NOTES.md:16849-16855]. The same cluster quotes Ringe & Taylor on compound structure—“compounds with a-stem first members regularly fail to exhibit their stem vowel”—and cites `elnboga 'elbow'` as the relevant OE parallel for a compound in `-boga` whose `b` remains a stop [Germanic/docs/DEV_NOTES.md:16857-16865]. That means the row should not be summarized merely as “compound syncope fixed rainbow”: the useful row-specific substance is that `reġnboga` depends on both deletion of the linking vowel and bleeding of lenition.

Current row state, however, no longer uses the same symbolic protoform as the 2026-04-11 implementation note. Later DEV_NOTES sections move the OE compound rows into the grave-accent prosodic notation introduced for Nebenton-bearing second elements. In the scope table for §16.6, row 2148 is explicitly listed as `*régnă-bugô` / `reġnboga` with status “match (via OECompoundLinkingSyncope),” and §17.11 then explains that the OE analogue is now written `*régna-bùgô`, with the breve dropped from the linking vowel because “an unaccented `a` is already an unaccented `a` — no diacritic adds phonetic content” [Germanic/docs/DEV_NOTES.md:27614-27627,27746-27754]. This is the crucial row-level PROTO/PROTOFORM caution: the live row's `PROTO = PROTOFORM = *régna-bùgô`, but the older derivational discussion in DEV_NOTES still uses the superseded earlier notation `*regnă-bugô`. The slice has to preserve both levels so later reviewers can read old fragments without mistaking the current row for stale notation.

The later source-audit material also sharpens the explanatory framework. §17.11 says no consulted handbook tradition uses breve `ă` or schwa `ə` for the linking vowel; the literature either writes a plain vowel or uses a hyphen as a mere printing convention, not as a morphophonemic trigger [Germanic/docs/DEV_NOTES.md:27771-27789]. More importantly for the row, DEV_NOTES recasts compound-linking syncope as a prosodic phenomenon of the trough between primary stress and Nebenton: Luick, Brunner, Bülbring, Ringe-Taylor, and Fulk are all marshalled to say that the linking vowel is the weakly stressed or unstressed syllable between the first element and the second element's stressed root [Germanic/docs/DEV_NOTES.md:27791-27830]. Under that account, row 2148's current `*régna-bùgô` is not just a respelling of the old input. It makes explicit why the linking `a` deletes and why the second-element root vowel bears grave accent: syncope targets the trough, while the second element keeps Nebenton.

Finally, §17.11 preserves the cleanest current statement of how the present row should be read. The proposed trough-conditioned rule says `[{*a}|{*i}|{*u}] -> 0` only between an acute-marked stressed syllable and a grave-marked Nebenton syllable, and DEV_NOTES gives row 2148 as its positive example: `*régna-bùgô → reġnboga`, where the linking `a` is syncopated because it is flanked by acute `é` and grave `ù` [Germanic/docs/DEV_NOTES.md:27897-27920,27978-27982]. Even though that section is framed as broader breve-cleanup work, it is current and row-relevant because it explains the live protoform, the reason the row matches now, and why the older breve-triggered implementation should be treated as superseded engineering rather than as the lasting philological account [Germanic/docs/DEV_NOTES.md:27922-27949].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16807-16910

- Source heading: `Compound Words: *regnă-bugô → reġnboga 'rainbow' (2026-04-11)`
- Source line or section hint: `lines 16807-16910`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `compound_syncope`; `lenition_bleeding`; `row_derivation`; `compound_phonology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the foundational row-specific fragment and still the best place to recover the actual derivation. DEV_NOTES records the bad older output `reġnafoga`, isolates the two concrete failures (“Linking vowel `ă` survives” and “`*b → f`”), and then supplies the worked chain `*regnă-bugô > *regna-bugô > *regnæ-bugô > *regn-bugô > reġnboga` [Germanic/docs/DEV_NOTES.md:16814-16824,16841-16855]. It also preserves the rule interaction that later summaries must not lose: syncope happens before B-allophony, so deletion of the linking vowel removes the postvocalic environment and leaves `b` as a stop [Germanic/docs/DEV_NOTES.md:16849-16855]. The Ringe-Taylor quotations embedded here are directly useful for this row as well, because they tie the deletion to general nonhigh-vowel syncope and to the broader compound pattern where a-stem first members regularly fail to show their stem vowel [Germanic/docs/DEV_NOTES.md:16825-16831,16857-16865].

### DEV_NOTES:line-27614-27627

- Source heading: `§16.6.4 Scope in our data (OE rows only)`
- Source line or section hint: `lines 27614-27627`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `protoform_migration`; `compound_rows`; `verification_state`; `row_scope`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2252,2302`

This brief table matters because it is the clearest current checkpoint that row 2148 is already considered solved inside the grave-accent compound programme. The section lists only three hyphenated OE protoforms and marks row 2148 `*régnă-bugô` / `reġnboga` as a match “via `OECompoundLinkingSyncope`” [Germanic/docs/DEV_NOTES.md:27614-27620]. For this slice, the fragment is less about detailed phonology than about state control: it confirms that rainbow belongs to the tiny compound-migration set and that by §16.6 the row was already treated as matching, not as an unresolved exception awaiting a row-local workaround [Germanic/docs/DEV_NOTES.md:27622-27627].

### DEV_NOTES:line-27746-27830

- Source heading: `§17.11.0 Motivation` and `§17.11.1-A/B Notational practice in the literature / What the literature says about the syncope itself`
- Source line or section hint: `lines 27746-27830`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `source_audit`; `notation_policy`; `prosodic_trough`; `proto_vs_protoform`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2252,2302`

This is the controlling source-audit fragment for the live row notation. DEV_NOTES says expressly that the OE analogue for row 2148 is now `*régna-bùgô` and that the earlier `*régnă-bugô` notation was changed because the breve added no phonetic content [Germanic/docs/DEV_NOTES.md:27746-27754]. It then canvasses the handbook tradition and concludes that no consulted source uses breve or schwa for the linking vowel; the accepted conventions are a plain linking vowel, with or without an orthographic hyphen [Germanic/docs/DEV_NOTES.md:27771-27789]. The same fragment is also the best current philological explanation of why row 2148 behaves as it does: the linking vowel sits in the prosodic trough between primary stress and Nebenton, and Luick/Brunner/Bülbring/Ringe-Taylor/Fulk all describe syncope and related raising in that same environment [Germanic/docs/DEV_NOTES.md:27791-27830]. For replacement notes, this fragment is what makes the live `PROTOFORM` intelligible rather than arbitrary.

### DEV_NOTES:line-27897-28005

- Source heading: `§17.11.2 Proposal — Option T (Trough-conditioned syncope)`
- Source line or section hint: `lines 27897-28005`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `current_protoform`; `stress_conditioning`; `compound_linking_syncope`; `row_verification`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2252,2302`

This fragment is the best current explanation of the row in its live notation. DEV_NOTES reformulates `OECompoundLinkingSyncope` so that plain short linking vowels delete only in the acute-to-grave trough and then names row 2148 as the expected positive outcome: `*régna-bùgô → reġnboga` because the linking `a` is flanked by acute `é` and grave `ù` [Germanic/docs/DEV_NOTES.md:27897-27920,27978-27982]. The surrounding TSV-migration note is also row-specific enough to preserve: row 2148 is the OE case whose breve-marked form became the grave-marked `*régna-bùgô`, while the non-OE sister rows received corresponding acute+grave compounds later [Germanic/docs/DEV_NOTES.md:27922-27949]. For this slice, the fragment establishes that the current row's `PROTO`/`PROTOFORM` are not merely tolerated symbols but the intended current representation of the same compound phonology described earlier.

## Superseded or diagnostic material

- The older notation `*regnă-bugô` is not the live row state, even though the 2026-04-11 derivation note remains substantively useful. Later DEV_NOTES explicitly migrates row 2148 to `*régna-bùgô` and treats the breve as dispensable engineering notation rather than as part of the philological representation [Germanic/docs/DEV_NOTES.md:16887-16903,27746-27754].
- The first implementation in the 2026-04-11 note was deliberately conservative: it added `OECompoundLinkingSyncope` for breve-marked `*ă` only, instead of the broader `OEGeneralSyncope` originally sketched for all medial `*æ`/`*e` [Germanic/docs/DEV_NOTES.md:16866-16903]. That implementation history is worth preserving as project chronology, but later notes supersede it as the preferred explanatory frame by recasting the change as acute–grave trough conditioning on plain linking vowels [Germanic/docs/DEV_NOTES.md:27887-27920].
- The mismatch/no-output table that lists `*regna-bugô` as “Compound with hyphen” is useful only as very early diagnostic exposure history. It predates both the row-specific fix and the later grave-accent migration, so it should not be reused as if it still described the row's live protoform or its active failure mode [Germanic/docs/DEV_NOTES.md:8290-8296,10403-10403].
- No current repo-local authority in the inspected row context suggests that row 2148 belongs in `oe_known_problems.tsv`; the row is now documented as a working match inside the compound-prosody material, not as an unresolved exception bucket [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/DEV_NOTES.md:27614-27627].

## Open questions for later work

- If a later full packet or memo is created for row 2148, add an explicit philology paragraph on whether the grave-marked compound notation should also be surfaced in reader-facing prose, or whether report prose should normalize to an unaccented reconstructed compound while keeping the grave marks strictly as input-level derivational notation [Germanic/docs/DEV_NOTES.md:27771-27789,27937-27949].
- The current slice securely explains syncope and stop retention, but it does not independently re-audit the dictionary attestation history of OE `reġnboga`; if a later central review wants fuller lexical-source citation rather than DEV_NOTES-based derivational notes, that would be a separate literature task rather than a change to the row's present derivational status.
- If the broader compound programme is revisited, keep row 2148 paired with rows 2252 and 2302, since DEV_NOTES repeatedly treats those three as the complete OE hyphenated/grave-marked compound set and uses them as the migration-risk boundary [Germanic/docs/DEV_NOTES.md:27614-27627,27922-27949].

---
row_id: 2147
concept: rain
counterpart: reġn
proto: *régną
protoform: *régną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: uncertain
needs_literature_agent: no
---

# DEV_NOTES material — 2147 rain / reġn

## Current row state

- CONCEPT: `rain` [Germanic/data/germanic-aligned-final.tsv:843-843]
- COUNTERPART: `reġn` [Germanic/data/germanic-aligned-final.tsv:843-843]
- PROTO: `*régną` [Germanic/data/germanic-aligned-final.tsv:843-843]
- PROTOFORM: `*régną` [Germanic/data/germanic-aligned-final.tsv:843-843]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:843-843]
- The live row is not documentary-clean. Its note is explicitly machine-transfer / placeholder material: `MT | TODO: replace with attested Old English form`, followed by Wiktionary-based sourcing rather than a row-local project note or literature-backed attestation audit [Germanic/data/germanic-aligned-final.tsv:843-843].
- `oe_known_problems.tsv` currently contains no entry for `2147`, `*régną`, `rain`, or `reġn`; the file's present contents are limited to unrelated `*u`-lowering and analogy exceptions, so this row is not currently being tracked as a known exception bucket there [Germanic/data/oe_known_problems.tsv:1-8].
- The nearest live row-local context is the adjacent compound `2148 rainbow / reġnboga`, whose first member is the same lexical material in compound position: `*régna-bùgô` with OE target `reġnboga` [Germanic/data/germanic-aligned-final.tsv:847-847].

## Development-note summary

No securely current **row-specific** DEV_NOTES section survives for simplex row `2147 rain / reġn`. A direct review of `Germanic/docs/DEV_NOTES.md` does not turn up a dedicated note for row `2147`, for simplex `rain`, for OE `reġn`, or for a row-local correction of `PROTO/PROTOFORM *régną` [Germanic/data/germanic-aligned-final.tsv:843-843]. That absence matters here because the live TSV itself already warns that the OE side is provisional: `COUNTERPART reġn` is carried by an `MT | TODO: replace with attested Old English form` note, so the replacement working note cannot pretend that DEV_NOTES settled the simplex OE citation form when the row metadata itself says the opposite [Germanic/data/germanic-aligned-final.tsv:843-843].

The only securely relevant DEV_NOTES material is **shared**, not row-specific: the rainbow note for adjacent row `2148` shows that the project already uses a `regn-` / `reġn-` stem in compound position and had to repair the compound by deleting the linking vowel before `b`, yielding `reġnboga` rather than `reġnafoga` [Germanic/docs/DEV_NOTES.md:16807-16912]. That is genuinely relevant to row `2147` because it confirms that the project's Old English pipeline already treats `regn-` as a viable first member and expects OE `reġn-` in at least one securely discussed environment [Germanic/docs/DEV_NOTES.md:16841-16912; Germanic/data/germanic-aligned-final.tsv:847-847]. But the compound note is still only **indirect** evidence for the simplex row. It establishes compound linking-vowel syncope and blocked `b`-lenition after `n`; it does **not** establish whether the simplex citation form in row `2147` is the best attested OE form, nor does it resolve the live row's TODO to replace the current placeholder target [Germanic/docs/DEV_NOTES.md:16820-16824,16841-16912; Germanic/data/germanic-aligned-final.tsv:843-843].

Later DEV_NOTES audit material confirms the same limited conclusion. The scope table at `§16.6.4` lists only the three hyphenated OE rows and records `2148 *régnă-bugô > reġnboga` as a match via `OECompoundLinkingSyncope`; this shows that the compound note remained live project authority after later cleanup [Germanic/docs/DEV_NOTES.md:27612-27625]. For row `2147`, however, that later confirmation still governs only the **compound** environment. The safest current row narrative is therefore conservative and level-sensitive: comparative `PROTO` and row-input `PROTOFORM` are both still `*régną`, but the OE target `reġn` remains a provisional project placeholder awaiting attested-form review, and DEV_NOTES currently supplies only adjacent compound-context support rather than a dedicated simplex lexeme ruling [Germanic/data/germanic-aligned-final.tsv:843-843,847-847; Germanic/docs/DEV_NOTES.md:16807-16912,27612-27625].

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-exact-hit-for-rain-reġn

- Source heading: no exact simplex `rain / reġn` heading survives in `DEV_NOTES.md`
- Source line or section hint: no direct row `2147` simplex hit; nearest securely relevant material is at `16807-16912` and `27612-27625`
- Fragment type: `unclear_needs_human_review`
- Status: `uncertain`
- Issue tags: `missing_row_specific_authority`; `mt_placeholder`; `attestation_gap`; `negative_result`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This negative result is the most important current DEV_NOTES fact to preserve. A direct sweep of `DEV_NOTES.md` finds no dedicated row-local discussion for `2147`, no simplex `reġn` correction note, and no source audit that would let later reporting treat the live OE target as already literature-secure [Germanic/data/germanic-aligned-final.tsv:843-843]. Because the row itself still carries `MT | TODO: replace with attested Old English form`, the absence of a DEV_NOTES simplex note is not incidental; it means the present slice must explicitly mark the OE side as provisional rather than silently upgrading placeholder data into reviewed authority [Germanic/data/germanic-aligned-final.tsv:843-843; Germanic/data/oe_known_problems.tsv:1-8].

### DEV_NOTES:line-16807-16912

- Source heading: `Compound Words: *regnă-bugô → reġnboga 'rainbow' (2026-04-11)`
- Source line or section hint: `lines 16807-16912`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `compound_first_member`; `linking_syncope`; `reġn_stem_context`; `not_simplex_attestation`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2148`

This is the closest securely relevant DEV_NOTES authority because it discusses the same lexical material in compound position. The note states the mismatch explicitly — ``*regnă-bugô`` was surfacing as `reġnafoga` instead of `reġnboga` — and then explains why the linking vowel must delete and why `b` must remain a stop after `n`, not lenite to `f` [Germanic/docs/DEV_NOTES.md:16814-16824]. Its worked derivation is concrete: `*regnă-bugô > *regna-bugô > *regnæ-bugô > *regn-bugô > reġnboga`, with the important row-adjacent implication that the project already treats a `regn-` base as yielding OE `reġn-` in compound position [Germanic/docs/DEV_NOTES.md:16841-16854]. For row `2147`, that is useful stem-context evidence, but it must not be overread. The fragment solves compound linking-vowel behavior for row `2148`; it does **not** settle the simplex target `reġn` as the best attested OE citation form for row `2147`, and it does not remove the live TSV note that the simplex row still needs attested-form replacement [Germanic/data/germanic-aligned-final.tsv:843-843,847-847].

### DEV_NOTES:line-27612-27625

- Source heading: `§16.6.4 Scope in our data (OE rows only)`
- Source line or section hint: `lines 27612-27625`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `regression_guard`; `adjacent_row_confirmation`; `compound_match`; `shared_stem_context`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2148,2252,2302`

This later audit matters because it shows the rainbow fix was not a one-off note that later project work abandoned. DEV_NOTES' scope table lists row `2148` with `PROTOFORM *régnă-bugô`, `COUNTERPART reġnboga`, and status `match (via OECompoundLinkingSyncope)` [Germanic/docs/DEV_NOTES.md:27614-27620]. For the present row, that gives a narrow but real current inference: adjacent `reġn-` compound behavior remained stable after later cleanup. What it still does **not** provide is row `2147` simplex authority. The table is about hyphenated protoforms only, so it can be cited as a regression guard for shared stem handling, not as proof that the placeholder simplex target has already been literature-vetted [Germanic/docs/DEV_NOTES.md:27614-27625; Germanic/data/germanic-aligned-final.tsv:843-843].

### DEV_NOTES:line-8290-8298-and-10403-10403

- Source heading: `The Problem` / mismatch progress log entry
- Source line or section hint: `lines 8290-8298 and 10403-10403`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `compound_debug_history`; `hyphen_issue`; `adjacent_row_only`; `do_not_reindex_as_simplex`
- Recommended next use: `ignore_unless_debugging`
- Shared with row IDs: `2148`

These two short fragments are worth preserving only to explain why most surviving `regn-` DEV_NOTES material sits inside compound debugging rather than simplex rain analysis. The earlier mismatch table lists ``*regna-bugô`` among the forms producing no output because it was a "Compound with hyphen," and the progress log later records the implemented repair as `OECompoundLinkingSyncope: *regnă-bugô→reġnboga` [Germanic/docs/DEV_NOTES.md:8290-8298,10403-10403]. For row `2147`, the value is purely diagnostic: they show the project history of the adjacent compound, but they should not be mistaken for dedicated simplex `rain / reġn` authority.

## Superseded or diagnostic material

- The most misleading possible move would be to treat the rainbow note as though it solved the simplex row. Current DEV_NOTES authority does **not** do that: all explicit `regn-` discussion is tied to compound debugging or compound-scope verification for row `2148`, not to a simplex attestation decision for row `2147` [Germanic/docs/DEV_NOTES.md:16807-16912,27612-27625,8290-8298,10403-10403].
- The live row note itself is diagnostic project history in progress: `reġn` is present as the current OE target, but the same row explicitly labels it `MT` and says to replace it with an attested Old English form [Germanic/data/germanic-aligned-final.tsv:843-843]. That warning should remain visible until a later packet/memo or literature-backed revision settles the simplex target more securely.
- `oe_known_problems.tsv` currently offers no exception classification for this row, so the present uncertainty is not “known phonological bug still open”; it is a documentation/attestation gap around the OE target [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- Replace or confirm the live OE target `reġn` against securely attested Old English evidence before treating the row as fully current; the TSV itself says that this replacement work is still outstanding [Germanic/data/germanic-aligned-final.tsv:843-843].
- If a later report cites the rainbow note, keep its scope explicit: it is evidence for shared `reġn-` compound behavior, not direct authority for the simplex citation form of row `2147` [Germanic/docs/DEV_NOTES.md:16807-16912,27612-27625].
- If a packet or research memo is later created for this row, make the three-way framing explicit near the top: comparative `PROTO *régną`, row-input `PROTOFORM *régną`, and still-to-be-verified OE target `reġn` should not be collapsed into a single claim of settled attested identity [Germanic/data/germanic-aligned-final.tsv:843-843].

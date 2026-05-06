---
row_id: 2127
concept: meal
counterpart: melu
proto: unresolved_legacy_request
protoform: unresolved_legacy_request
derivation_class: uncertain
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: uncertain
needs_literature_agent: no
---

# DEV_NOTES material — 2127 meal / melu

## Current row state

- Requested slice identity from the task/file stem: `2127 meal / melu`.
- The live TSV row `2127` is now `month / mōnaþ`, with `PROTO` and `PROTOFORM` `*mḗnōθz`; the requested meal/melu identity does **not** survive at that row number in the current table [Germanic/data/germanic-aligned-final.tsv:764-764].
- The live OE row for concept `meal` is currently `2122`, not `2127`; it has `COUNTERPART` `mǣl`, `PROTO` `*mḗlą`, `PROTOFORM` `*mḗlą`, and `DERIVATION_CLASS` `regular` [Germanic/data/germanic-aligned-final.tsv:745-745].
- Repo-local lexical references split `mǣl` and `melu` into different OE lexemes. `mǣl` belongs with PGmc `*mēla-` ‘point in time; meal’, while `melu` belongs with PGmc `*melwa-` ‘meal, flour’ [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19122,19263-19266; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861,10888-10890].
- The local OE lexicographic extracts preserve that same split: Clark Hall gives `mæl ... time ... 'meal'` but separately `melu ... 'meal,' flour'`; Bosworth-Toller likewise has `melu ... meal, ground grain` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26982-26985,27807-27808; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:102284-102287].
- `old_english_wiktionary.tsv` also follows the live TSV rather than the requested filename, mapping English `meal` to OE `mǣl` [Germanic/data/old_english_wiktionary.tsv:183-183].

## Development-note summary

No securely attachable **current row-specific DEV_NOTES authority** survives for a live OE row that can straightforwardly be described as `2127 meal / melu`. In the current TSV, row `2127` is no longer the meal row at all; it is `month / mōnaþ` [Germanic/data/germanic-aligned-final.tsv:764-764]. The live meal row is `2122`, and its current OE target is `mǣl`, not `melu` [Germanic/data/germanic-aligned-final.tsv:745-745].

That matters because the requested filename conflates two different lexical tracks that repo-local reference material keeps separate. Kroonen distinguishes PGmc `*mēla- 1 n. 'point in time'`, which includes OE `mal n. 'moment; meal'`, from PGmc `*melwa- n. 'meal, flour'`, which includes OE `melo, melu n. 'id.'`; Ringe-Taylor likewise derives OE `mél` from PGmc `*méla` but derives OE `melu, meolw-` / `meolu, meolw-` from PGmc `*melwa` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19122,19263-19266; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861,10888-10890]. Clark Hall's separate entries for `mæl` and `melu` point the same way [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26982-26985,27807-27808].

DEV_NOTES itself does **not** currently preserve a meal/mǣl/melu discussion that can override or refine that split. The only substantial `mel-` passages are about **milk** `*melukz > meoloc/meolc`, not about the live meal row `2122`, and not about a flour-word `melu` [Germanic/docs/DEV_NOTES.md:730-759,17795-17805]. Accordingly, this replacement working note has to be conservative: it should record that the requested slice identity looks like a **legacy or diagnostic conflation**, not present secure row policy. If later report work needs the live OE meal row, the securely current anchor is `2122 meal / mǣl / *mḗlą`; if it needs OE `melu`, that is a different lexeme that local references align with `*melwa-`, not with the live `2122` row state [Germanic/data/germanic-aligned-final.tsv:745-745; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19122,19263-19266; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861,10888-10890].

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-exact-hit-for-meal-melu
- Source heading: no exact meal/melu heading survives in `DEV_NOTES.md`
- Source line or section hint: no direct hit; nearest misleading `mel-` passages are at lines `730-759` and `17795-17805`
- Fragment type: unclear_needs_human_review
- Status: uncertain
- Issue tags: missing_row_specific_authority;row_id_drift;lexeme_split;negative_result
- Recommended next use: check_against_literature
- Shared with row IDs:

A direct review of `DEV_NOTES.md` does **not** yield a row-specific fragment for live meal row `2122`, for requested file label `2127-meal-melu`, or for an OE target `melu` that could safely be attached to the current meal row. That negative result is itself the most important DEV_NOTES fact to preserve here, because later extraction work could otherwise infer authority from mere string proximity. The current slice therefore cannot honestly quote DEV_NOTES as lexical authority for `meal / mǣl` or `meal / melu`; it has to fall back to the live TSV plus reference extracts, while marking the filename as a legacy diagnostic label [Germanic/data/germanic-aligned-final.tsv:745-745,764-764; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19122,19263-19266].

### DEV_NOTES:line-730-759
- Source heading: `The milk problem: *melukz -> meoloc (expected meolc)`
- Source line or section hint: lines `730-759`
- Fragment type: superseded_or_diagnostic_for_lexeme
- Status: misleading_if_uncontextualized
- Issue tags: false_positive_hit;milk_not_meal;lexical_misattachment;search_trap
- Recommended next use: ignore_unless_debugging
- Shared with row IDs: 2126

This is the nearest substantial `mel-` discussion in DEV_NOTES, but it is explicitly a **milk** note. The fragment opens with the heading `The milk problem: *melukz -> meoloc (expected meolc)`, then analyzes a consonant-stem noun with WS `meoloc ~ meolc` and Anglian `milc`; its problem is variable syncope after a light syllable in the milk paradigm, not the lexical identity of OE `mǣl` and not the flour-word `melu` [Germanic/docs/DEV_NOTES.md:730-759]. Because the requested slice name contains `melu`, this milk note is an obvious false-positive trap. It should be recorded here only so later indexing does **not** misattach milk material to this legacy `meal/melu` slice [Germanic/data/germanic-aligned-final.tsv:745-745; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19263-19266].

### DEV_NOTES:line-17795-17805
- Source heading: `Analysis`
- Source line or section hint: lines `17795-17805`
- Fragment type: superseded_or_diagnostic_for_lexeme
- Status: diagnostic_only
- Issue tags: back_mutation_control;milk_false_positive;search_trap;do_not_reindex_as_meal
- Recommended next use: ignore_unless_debugging
- Shared with row IDs: 2126

A later DEV_NOTES audit again mentions `*meluks -> meolc`, but only as a control example for the `*e -> *eo` rule in back-mutation analysis [Germanic/docs/DEV_NOTES.md:17795-17805]. That repeat mention strengthens the same caution rather than changing it: the surviving DEV_NOTES material under `mel-` remains milk-only. It does **not** adjudicate between live `2122 meal / mǣl` and the requested legacy counterpart `melu`, and it certainly does not license collapsing `mǣl` and `melu` into one OE row [Germanic/data/germanic-aligned-final.tsv:745-745; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861,10888-10890].

## Superseded or diagnostic material

- The file stem `2127-meal-melu.md` is itself diagnostic rather than securely current. In the live TSV, row `2127` is `month / mōnaþ`, while `meal` is row `2122` [Germanic/data/germanic-aligned-final.tsv:745-745,764-764].
- The requested counterpart `melu` should not be silently normalized into the live meal row. Local references separate OE `mǣl` ‘time; meal’ from OE `melu` ‘meal, flour’, and they assign them to different proto lineages `*mēla-` and `*melwa-` respectively [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26982-26985,27807-27808; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19122,19263-19266].
- The DEV_NOTES milk passages at lines `730-759` and `17795-17805` are valuable here only as anti-evidence: they show where a string-based sweep would go wrong by pulling in `*melukz > meoloc/meolc` material that belongs to row `2126`, not to this requested slice [Germanic/docs/DEV_NOTES.md:730-759,17795-17805].

## Open questions for later work

- Determine whether this legacy file should eventually be superseded by a live-row slice keyed to `2122 meal / mǣl`, since that is the current TSV row state [Germanic/data/germanic-aligned-final.tsv:745-745].
- Determine whether repo reporting needs a separate lexeme slice for OE `melu` / `meolu` under PGmc `*melwa-`, rather than preserving it inside a legacy `2127-meal-melu` label [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19263-19266; docs/references/ringe_taylor_linguistic_history_vol2.txt:10888-10890].
- If later DEV_NOTES work introduces a genuine meal-specific fragment, index it against the live row it actually governs; do not let the present filename force reattachment to current row `2127`, which now belongs to `mōnaþ` [Germanic/data/germanic-aligned-final.tsv:764-764].

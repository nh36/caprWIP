---
row_id: 2072
concept: help
counterpart: help
proto: '*xélpō'
protoform: '*xélpō'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2072 help / help

## Current row state

- CONCEPT: `help`
- COUNTERPART: `help`
- PROTO: `*xélpō`
- PROTOFORM: `*xélpō`
- DERIVATION_CLASS: `regular`
- Live TSV row: row `2072` currently keeps noun `help` as an Old English reflex of `*xélpō`, with no explanatory `NOTE` and only inherited-etymology placeholders in the source fields; this is a separate row from verbal `2071 help / helpan` [Germanic/data/germanic-aligned-final.tsv:549-551].
- Lexeme split already lives in the TSV itself. Row `2071` says `OE target: help→helpan (inf. of str.v. class III; noun 'help' is in *xelpō row)`, so the noun/verb disambiguation is not a later editorial guess but part of the current dataset state [Germanic/data/germanic-aligned-final.tsv:549-551].
- `oe_known_problems.tsv` has no row-specific entry for `*xélpō`; nothing in the live exception list marks noun `help` as analogical, mismatched, or awaiting repair [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure is still absent. `coverage_audit.md` lists row `2072` as `has_report = no` and `attached_dev_notes = none`, and `report_manifest.tsv` has no row-2072 entry among the currently registered report rows [Germanic/docs/lexeme_reports/coverage_audit.md:275-275; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The published derivation snapshot already lands on the live target with no workaround: `PROTO: *xélpō`, `EXPECTED: help`, `OUTPUTS: help`, via `NWGmc Final Long O Raising: *xélpu`, `OE Velar Fricative Palatalization: *çélpu`, and `OE High Vowel Apocope: *çélp`, followed by orthographic `h*élp` > `help` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2326-2346].
- Repo lexica also preserve the noun/verb split directly. Clark Hall has `help (y) fm. 'help,' succour, aid` immediately followed by separate verbal `helpan³`; Bright likewise lists noun `help, f., help` and separately `helpan, healp hulpon holpen (3)` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21425-21429; docs/references/bright_anglo_saxon_reader.txt:21730-21732].

## Development-note summary

No securely attachable **row-specific DEV_NOTES block** for noun row `2072` survives in the live `DEV_NOTES.md`. That absence should be stated plainly. The usable material is instead shared background on two regular mechanisms that the current trace visibly uses: final long `*ō` raising to `*u`, and later loss of post-tonic high vowels after heavy stressed syllables [Germanic/docs/DEV_NOTES.md:18624-18719,19919-19928; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2333-2346].

For this row, the three levels remain identical and should stay identical unless new evidence appears: comparative/proto headword `PROTO = *xélpō`, project input `PROTOFORM = *xélpō`, and attested/target OE noun `help` [Germanic/data/germanic-aligned-final.tsv:551-551]. There is no current evidence in `DEV_NOTES`, `oe_known_problems.tsv`, or the published trace that the row needs a hidden paradigm-cell substitute, a repaired preform, or reclassification away from `regular` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2326-2346].

The main row-level caution is lexical, not phonological. Because English gloss `help` names both a noun and a verb, later packeting or search passes can easily pull in `helpan` material and treat it as if it governed noun row `2072`. The live TSV, Clark Hall, and Bright all already disagree with that collapse: noun `help` and verb `helpan` are separate lexical items even when they sit beside one another in dictionaries [Germanic/data/germanic-aligned-final.tsv:549-551; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21425-21429; docs/references/bright_anglo_saxon_reader.txt:21730-21732].

The shared DEV_NOTES support that does survive is enough to explain the current derivation conservatively. First, `*xélpō` belongs to the final-long-`ō` pathway, not to weak `-ô > -a` material: DEV_NOTES explicitly says, for another lexeme, that `NWGmcFinalLongORaising` applies as ``*ō → *u`` in final position and that this path is separate from `*ō`-shortening to `*a` [Germanic/docs/DEV_NOTES.md:19921-19928]. Second, once `*xélpō` has raised to `*xélpu`, DEV_NOTES' general high-vowel-apocope discussion gives exactly the conditioning the trace assumes, namely late loss of post-tonic `i/u` after a heavy stressed syllable [Germanic/docs/DEV_NOTES.md:18624-18719]. Since `*xélp-` is heavy by coda `-lp`, the snapshot's `*çélpu > *çélp` is ordinary project phonology, not a row-local exception [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2337-2346].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-18624-18719

- Source heading: `§15.1: Two Distinct Stages of High Vowel Apocope` / `§15.3: Luick §304 — Later Pre-OE Apocope`
- Source line or section hint: `lines 18624-18719`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `heavy_stem_conditioning`; `late_pre_oe_loss_of_u`
- Recommended next use: `cite_as_shared_phonology_only`
- Shared-with rows if relevant: `many heavy-stem rows ending in final *-i/*-u after earlier raising; not specific to 2072`

This is the main surviving DEV_NOTES material that actually explains why row `2072` works. DEV_NOTES distinguishes two apocope stages and then quotes Luick's later rule for post-tonic high vowels: `"In final position, i and u were lost immediately after a long stressed syllable, and also after a short one if another syllable followed (but not immediately after a short one)."` [Germanic/docs/DEV_NOTES.md:18694-18711]. That wording is shared background, not a noun-`help` note, but it maps cleanly onto the current trace: after final-`*ō` raising, row `2072` passes through `*xélpu`; the stressed syllable is heavy because `*xélp-` is closed by `-lp`; and the published trace accordingly drops the final high vowel at `OE High Vowel Apocope: *çélp` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2337-2346].

The important limitation is scope. This fragment supports the **regularity of the mechanism**, not any row-local editorial choice. It does not tell us to rewrite `PROTO` or `PROTOFORM`, it does not imply a hidden suffixal analysis, and it does not collapse noun `help` into verbal `helpan`. Its value is precisely that it lets the slice preserve the phonological substance of the current derivation without pretending that DEV_NOTES ever wrote a dedicated lexeme dossier for this noun [Germanic/docs/DEV_NOTES.md:18624-18719].

### DEV_NOTES:line-19919-19928

- Source heading: `Why *násō Worked Differently`
- Source line or section hint: `lines 19919-19928`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `final_long_o_raising`; `separate_from_o_to_a_shortening`; `final_ō_noun_path`
- Recommended next use: `cite_when_explaining_why_row_2072_uses_the_ō_to_u_path`
- Shared-with rows if relevant: `rows whose final *ō first raises to *u before later OE developments`

This fragment is not about `help` by name, but it is the clearest surviving DEV_NOTES statement of the first step used by row `2072`. DEV_NOTES says of `*násō` that `"The *ō was in final position"`, that `"NWGmcFinalLongORaising applied: *ō → *u (final position)"`, and then adds the key warning: `"This is a different sound change path — final *ō raising to *u is separate from medial/final *ō shortening to *a."` [Germanic/docs/DEV_NOTES.md:19921-19928]. For noun `help`, that distinction matters because it prevents later writers from importing weak-`-ô > -a` reasoning or other `ō`-shortening discussions into a row whose actual trace is `*xélpō > *xélpu > ... > help` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2335-2346].

Use this fragment as shared pathway control only. It supports the current row's interpretation of final `*ō`, but it does not create row-specific historical baggage, and it does not by itself attest OE `help`; the attested noun still has to come from the live row state and local lexica [Germanic/data/germanic-aligned-final.tsv:551-551; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21425-21429].

### DEV_NOTES:line-13445-13451

- Source heading: `FST analysis`
- Source line or section hint: `lines 13445-13451`
- Fragment type: `diagnostic_shared_comparator`
- Status: `diagnostic`
- Issue tags: `comparator_lexeme`; `ō_to_u_then_apocope`; `implementation_control`
- Recommended next use: `keep_as_diagnostic_comparator_not_row_authority`
- Shared-with rows if relevant: `2114 lung / lungen and other final-*ō noun checks`

This comparator is useful because it shows the project had already described essentially the same implementation path elsewhere: ``*lungō  → lung   (high-vowel apocope deletes final *u from *ō → *u)`` [Germanic/docs/DEV_NOTES.md:13445-13451]. That is not evidence that `*xélpō` and `*lungō` are the same lexical type in every respect, but it is good diagnostic confirmation that the published `*xélpō > *xélpu > *çélpu > *çélp` pipeline is not an isolated one-off invented only for row `2072` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2335-2346].

Treat this as implementation-facing background only. It should not be promoted into lexeme-specific authority for noun `help`, but it is worth preserving because it shows that DEV_NOTES already recognized the exact `final *ō > *u > zero` interaction now visible in the live trace.

## Superseded or diagnostic material

- No row-specific noun-`help` DEV_NOTES block survives. That absence is real, and later editors should not fill it by silently importing the neighboring verb's paperwork.
- The most tempting `help`-named DEV_NOTES fragments are actually for **verbal** `helpan`, not for noun row `2072`. The explicit derivational note `*hólpąn → *hólpan → helpan` concerns infinitive `*xélpaną`, and the later AFB probe table row ``*xélpăną` vs `*xélpaną` | `helpan` | `none`` is likewise a verb-only diagnostic; neither fragment should be cited as noun-row authority [Germanic/docs/DEV_NOTES.md:21013-21018,21774-21779].
- The published derivation snapshot is therefore diagnostic support, not superseded row history. Its value is practical: it confirms that current project phonology already derives noun `help` from `*xélpō` without repair or exception handling [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2326-2346].
- Coverage documents are also diagnostic only. `coverage_audit.md` says `none`, and `report_manifest.tsv` has no row entry; that means there is presently no packet/memo/report infrastructure to smuggle in extra row-local conclusions from elsewhere [Germanic/docs/lexeme_reports/coverage_audit.md:275-275; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Open questions for later work

- If a packet or memo is ever created for row `2072`, keep the noun/verb split explicit from the start: noun `help` belongs here under `*xélpō`; verbal `helpan` remains row `2071` under `*xélpaną` [Germanic/data/germanic-aligned-final.tsv:549-551; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21425-21429].
- If future indexing work records this slice in broader manifests, mark the DEV_NOTES support as **shared-background-only plus diagnostic comparator**, not as a surviving row-specific dossier.
- If later literature review is wanted, it should be narrow: confirm whether any source in the repo or added bibliography materially changes the noun-entry picture beyond the already adequate local attestations (`help` noun vs `helpan` verb). Nothing in the current repo makes that review urgent, which is why `needs_literature_agent` remains `no`.

---
row_id: 2138
concept: net
counterpart: nett
proto: *nátją
protoform: *nátją
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2138-net-nett.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2138-net-nett.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2138 net / nett

## Current row state

- CONCEPT: `net` [Germanic/data/germanic-aligned-final.tsv:808].
- COUNTERPART: `nett` [Germanic/data/germanic-aligned-final.tsv:808].
- PROTO: `*nátją` [Germanic/data/germanic-aligned-final.tsv:808].
- PROTOFORM: `*nátją` [Germanic/data/germanic-aligned-final.tsv:808].
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:808].
- Live TSV note: `Orel: OE nett (geminate); Source: Wiktionary etymology (template:inh)`; the row is therefore already pointed at geminate OE `nett`, not at simplified `net` [Germanic/data/germanic-aligned-final.tsv:808].
- The linked packet's compact derivation is in solved state and now gives `EXPECTED: nett`, `OUTPUTS: nett`, with the path `*nátją -> *náttją -> *nættją -> *nettj -> nett` compressed as PWGmc J Gemination, Anglo-Frisian Brightening, heavy-syllable nasal apocope, i-umlaut, and `J Loss After Heavy` [Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42].
- The linked research memo correctly warns that earlier project material temporarily treated `net` as the expected OE form, but that this is now stale relative to the live row and current trace output [Germanic/docs/lexeme_reports/research_memos/2138-net-nett.md:13-23, 69-79, 99-102].
- There is no dedicated row-ID entry for `2138` in `oe_known_problems.tsv`, but the file still preserves an older lexeme-level bug note `*nátją ... nete ... Should be nett per Orel/Hall; FST bug documented in DEV_NOTES`; because the packet already shows `OUTPUTS: nett`, that known-problems line should now be treated as diagnostic history rather than current row state [Germanic/data/oe_known_problems.tsv:5-5; Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42].
- Row-local philological support is secure in repo-local references: Orel gives `*natjan ... OE nett`, Clark Hall has headword `nett`, and Bosworth-Toller likewise treats `nett` as the simplex headword while listing compounds in `-nett` [docs/references/orel_handbook_germanic_etymology.vision.txt:31716-31717; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29693-29695; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:104720-104728].

## Development-note summary

Securely attachable current row-specific DEV_NOTES authority **does** survive for row 2138. The controlling material is the dedicated section `OE nett 'net': ja-stem Gemination Chronology Bug (2026-03-18)`, and the live packet confirms that its repair has already landed: the project now derives and targets `nett`, not `nete`, and not a preferred lexical headword `net` [Germanic/docs/DEV_NOTES.md:12064-12139, 12175-12177; Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42].

This row needs the usual three-way distinction stated explicitly even though live TSV `PROTO` and `PROTOFORM` happen to be identical. In the row metadata, **PROTO** is the comparative table label `*nátją` and **PROTOFORM** is the actual derivational input string supplied to the OE pipeline, also `*nátją`; neither should be collapsed into the **OE target**, which is the attested lexeme/headword `nett` [Germanic/data/germanic-aligned-final.tsv:808; Germanic/docs/lexeme_reports/research_memos/2138-net-nett.md:44-53]. In dictionary-style literature the same cognate set is often cited with a normalized headword such as Orel's `*natjan`, but that difference in citation style does not change the row's OE outcome: Orel still gives `OE nett id.` [docs/references/orel_handbook_germanic_etymology.vision.txt:31716-31717].

The current DEV_NOTES argument is both philological and chronological. Philologically, the repo-local authorities align behind geminate `nett`: Orel has `OE nett`; Clark Hall gives `nett (y) n. 'net'`; Bosworth-Toller uses `nett` as simplex headword and records compounds in `-nett`; Campbell adds the crucial caution that final written simplification of geminates is frequent and is “only a graphic simplification,” so spellings in `net` do not by themselves disprove an underlying geminate [Germanic/docs/DEV_NOTES.md:12082-12091; docs/references/orel_handbook_germanic_etymology.vision.txt:31716-31717; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29693-29695; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:104720-104728; docs/references/campbell_old_english_grammar.txt:2801-2804]. Chronologically, DEV_NOTES identifies the real bug as rule ordering: the old derivation let `PWGmcSyllabicJ` absorb `*j` too early, whereas Fulk states that WGmc gemination applies “before j” after a short vowel, and Ringe-Taylor place syllabic `*j > *i` only upon loss of unstressed `*a/*ą`; the corrected order therefore gives `*natją -> *nattją -> *nattą -> nett` [Germanic/docs/DEV_NOTES.md:12100-12139; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:7596-7603; docs/references/ringe_taylor_linguistic_history_vol2.txt:3372-3373, 13782-13783].

The dedicated section's statement that the heavy stem should lose its final vowel also remains usable current authority. Campbell's ja-stem paradigms contrast light-stem `spere` with heavy-stem `geswinc`, and DEV_NOTES applies that distinction directly: once gemination creates `*natt-`, the stem is heavy and should not continue with final `-e` [Germanic/docs/DEV_NOTES.md:12093-12099; docs/references/campbell_old_english_grammar.txt:15736-15784]. That is why the packet's present solved trace ending in `nett` is not merely a practical patch but the expected result of the chronology argued in the sources [Germanic/docs/lexeme_reports/packets/2138-net-nett.md:27-42].

What must now be separated from current authority is **stale project history inside DEV_NOTES itself**. The same dedicated section still contains a `TSV Data Issue` block saying “The TSV expects `net` (row 2138)” and “This should probably be `nett`”; those sentences are no longer true of the live row, which already has `COUNTERPART = nett` and a note explicitly invoking Orel's geminate form [Germanic/docs/DEV_NOTES.md:12141-12152; Germanic/data/germanic-aligned-final.tsv:808]. The slice should therefore preserve that wording only as superseded project chronology explaining why older packet/memo material flags metadata drift, not as current row policy [Germanic/docs/lexeme_reports/research_memos/2138-net-nett.md:19-23, 93-102].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-12064-12139

- Source heading: `OE nett 'net': ja-stem Gemination Chronology Bug (2026-03-18)`
- Source line or section hint: `lines 12064-12139`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `ja_stem`; `gemination_chronology`; `rule_order`; `orthography`; `oe_target_attested`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current fragment for the row. DEV_NOTES opens with the concrete failure `*natją -> nete` and then anchors the correction in source-backed OE philology: Orel is quoted directly, `"Goth nati 'net', ON net id., **OE nett** id., OFris net, nette id., OS netti id., OHG nezzi id."`; Hall is summarized as listing compounds such as `ælnett`, `fengnett`, and `fisconett`; and Campbell §66 is invoked for the warning that final double consonant symbols are often simplified in writing, so `net` can be graphic while the lexical target remains `nett` [Germanic/docs/DEV_NOTES.md:12068-12091]. The repo-local reference extracts support each of those moves rather than merely repeating them: Orel's entry reads `*natjan sb.n. ... OE nett id.`; Clark Hall has `nett (y) n. 'net'`; and Bosworth-Toller preserves the simplex `nett` plus compound evidence in `-nett` [docs/references/orel_handbook_germanic_etymology.vision.txt:31716-31717; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29693-29695; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:104720-104728].

The same fragment also contains the best current explanation of **why** `nett` is the expected OE target for the project input. DEV_NOTES quotes Fulk §6.15: `"In the WGmc. protolanguage there was consonant doubling before sonorant consonants... Before j the change regularly applies to any consonant other than r ... after a short vowel"`, and pairs that with Ringe-Taylor's statement that syllabic `*j` arises only `"Upon the loss of unstressed *a and *ą"` [Germanic/docs/DEV_NOTES.md:12102-12113; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:7597-7603; docs/references/ringe_taylor_linguistic_history_vol2.txt:3372-3373]. The corrected derivation `*natją -> *nattją -> *nattą -> nett` is therefore not an arbitrary row repair but the sequence expected if gemination precedes j-vocalization/loss [Germanic/docs/DEV_NOTES.md:12128-12139]. DEV_NOTES then adds the heavy-stem point from Campbell's ja-stem neuters: once `*natt-` exists, the stem patterns with heavy forms like `geswinc`, not light `spere`, so final `-e` is not the right citation outcome [Germanic/docs/DEV_NOTES.md:12093-12099; docs/references/campbell_old_english_grammar.txt:15736-15784].

### DEV_NOTES:line-12141-12152

- Source heading: `TSV Data Issue`
- Source line or section hint: `lines 12141-12152`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `stale_row_state`; `metadata_drift`; `project_history`; `target_form`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This block must be preserved, but only under an explicit superseded label. It says: `The TSV expects net (row 2138) ... This should probably be nett`, and it even prints an older row snapshot with `EXPECTED: net` [Germanic/docs/DEV_NOTES.md:12141-12152]. That is now false as a description of live metadata, because the current TSV row already reads `COUNTERPART: nett` and carries a note `Orel: OE nett (geminate)` [Germanic/data/germanic-aligned-final.tsv:808]. The fragment remains useful as project chronology because it explains why the packet and memo both emphasize stale history and why older discussions of `net` versus `nett` cannot be quoted uncontextualized [Germanic/docs/lexeme_reports/packets/2138-net-nett.md:48-72; Germanic/docs/lexeme_reports/research_memos/2138-net-nett.md:13-23, 99-102].

### DEV_NOTES:line-1379-1382

- Source heading: `PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)`
- Source line or section hint: `lines 1379-1382`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `older_rule_order`; `pre_fix_analysis`; `syllabic_j`; `net_vs_nett`
- Recommended next use: `ignore_unless_debugging`
- Shared with row IDs:

This earlier note is valuable only as a record of the pre-fix derivational model. Its worked example says `*natją -> *nati -> net ('net')`, i.e. exactly the non-geminating path later diagnosed as wrong for the OE row [Germanic/docs/DEV_NOTES.md:1379-1382]. Once the dedicated 2026-03-18 section established that WGmc gemination had to precede j-vocalization/loss, this older example ceased to be usable lexical authority for row 2138 and became a diagnostic snapshot of the outdated rule order instead [Germanic/docs/DEV_NOTES.md:12100-12139]. The lingering lexeme-level entry in `oe_known_problems.tsv` belongs with this same older diagnostic layer: it records the now-resolved `nete` failure, not the packet's current `nett` output [Germanic/data/oe_known_problems.tsv:5-5; Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42].

## Superseded or diagnostic material

The main superseded material is not the conclusion `nett`; that conclusion is now well supported and already live in the row [Germanic/data/germanic-aligned-final.tsv:808; Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42]. What has aged is the intermediate project state in which `net` was still printed as the row expectation and `*natją -> *nati -> net` could still be cited as if it were the correct OE-facing derivation [Germanic/docs/DEV_NOTES.md:1379-1382, 12141-12152].

Two materials should therefore stay explicitly demoted. First, the `TSV Data Issue` block in DEV_NOTES is now metadata history only, because live TSV has already adopted `nett` [Germanic/docs/DEV_NOTES.md:12141-12152; Germanic/data/germanic-aligned-final.tsv:808]. Second, `oe_known_problems.tsv` still retains the older lexeme-level `nete` bug line; that file is useful for reconstructing why the row once needed attention, but it is not a current statement of row 2138's output after the fix [Germanic/data/oe_known_problems.tsv:5-5; Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42].

A further caution is lexical rather than computational. Secondary tables may still show simplified `net`, and Campbell's discussion makes clear why such spellings can occur, but those forms should be framed as graphic simplification or weaker normalization, not as stronger authority than the dictionary and grammar evidence for underlying/headword `nett` [docs/references/campbell_old_english_grammar.txt:2801-2804; docs/references/orel_handbook_germanic_etymology.vision.txt:31716-31717; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29693-29695].

## Open questions for later work

- If `DEV_NOTES.md` is cleaned later, update or annotate the stale `TSV Data Issue` block so it no longer states that row 2138 expects `net`; the slice should continue treating that wording as superseded until such cleanup happens [Germanic/docs/DEV_NOTES.md:12141-12152; Germanic/data/germanic-aligned-final.tsv:808].
- If `oe_known_problems.tsv` receives a maintenance pass later, decide whether the lingering `*nátją ... nete` line should be removed or relabelled as resolved history rather than a live OE bug [Germanic/data/oe_known_problems.tsv:5-5; Germanic/docs/lexeme_reports/packets/2138-net-nett.md:17-42].
- If the row note is ever tightened, foreground the stronger local authorities for `nett` (Orel, Clark Hall, Bosworth-Toller, Campbell/Fulk/Ringe-Taylor) rather than leaving the note to lean mainly on Wiktionary wording [Germanic/data/germanic-aligned-final.tsv:808; docs/references/orel_handbook_germanic_etymology.vision.txt:31716-31717; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29693-29695].
- If `index.tsv` is updated later, index the current chronology fragment separately from the superseded `TSV Data Issue` fragment so later extraction can keep the sound-law argument while filtering out stale row-state claims [Germanic/docs/DEV_NOTES.md:12064-12139, 12141-12152; Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv:1-1].

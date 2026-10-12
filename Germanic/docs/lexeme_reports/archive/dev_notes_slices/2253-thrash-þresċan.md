---
row_id: 2253
concept: thrash
counterpart: þresċan
proto: *θréskaną
protoform: *θréskaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2253 thrash / þresċan

## Current row state

- The live OE row is `2253`, `CONCEPT thrash`, `COUNTERPART þresċan`, `PROTO *θréskaną`, `PROTOFORM *θréskaną`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1253-1253].
- `PROTO` and `PROTOFORM` are currently identical. Nothing in the live TSV suggests a substitute modelling stem, a rescued paradigm cell, or a split between cognate-set headword and FST input; the OE-side target remains a separate layer, namely `COUNTERPART þresċan` [Germanic/data/germanic-aligned-final.tsv:1253-1253].
- `oe_known_problems.tsv` has no row-local entry for row `2253`, for `þresċan`, or for `*θréskaną`, so the project is not currently treating this lexeme as an active OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking still lists `2253 | thrash | þresċan | regular | no | - | - | - | none`, so no packet, research memo, or dossier stem is available to reuse; the canonical row-based filename is therefore the correct slice filename here [Germanic/docs/lexeme_reports/coverage_audit.md:393-393].
- The current published derivation trace is an exact match: `PROTO: *θréskaną`, `EXPECTED: þresċan`, `OUTPUTS: þresċan`, with OE-side steps `OE Heavy Syllable Nasal Apocope: *θréskan`, `OE Secondary Nasalization: *θréskąn`, `OE Sk Palatalization: *θréʃąn`, `OE Weak Tail Reduction: *θréʃan`, then orthographic `þ*résċan` and surface `þresċan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5277-5297].
- Repo-local reference texts support the lexeme but also show that source spelling and row spelling must be kept apart. Ringe reconstructs `*þreskaną, *þrask, *þruskun, *þruskanaz` and cites OE `þerscan, þærsc, þurscon, þorscen` [docs/references/ringe_vol1_pie_to_pgmc.txt:11867-11870; @Ringe2006, p. 271]. Orel likewise gives `*þreskanan str.vb.` with OE `ðerscan` [docs/references/orel_handbook_germanic_etymology.vision.txt:47103-47108; @Orel2003, p. 426]. Clark Hall has `þerscan` with broad manuscript variation `(a, æ, ea, i, y)` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:42703-42705; @ClarkHall1960, s.v. "þerscan"]. Those forms support the lexeme, but they are not instructions to overwrite the live row's normalized `COUNTERPART þresċan`.

## Detailed development-note summary

No securely attachable row-dedicated `DEV_NOTES.md` section survives for `2253 thrash / þresċan`. That needs to be stated plainly. The present slice therefore functions as a conservative replacement working note built from four things: the live row state, the exact published derivation trace, a small number of shared DEV_NOTES process fragments, and handbook/dictionary support for the lexical identification [Germanic/data/germanic-aligned-final.tsv:1253-1253; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5277-5297; @Ringe2006, p. 271; @Orel2003, p. 426; @ClarkHall1960, s.v. "þerscan"]. That is enough to document the row responsibly, but it is still thinner than a row with a dedicated mismatch note, packet, or literature memo.

The most important distinction is between row metadata, trace stages, and source spellings. In the live dataset, `PROTO = PROTOFORM = *θréskaną`; the OE target is `COUNTERPART = þresċan` [Germanic/data/germanic-aligned-final.tsv:1253-1253]. In Ringe's comparative presentation the lexeme appears with principal parts `*þreskaną, *þrask, *þruskun, *þruskanaz` and with OE `þerscan, þærsc, þurscon, þorscen` [docs/references/ringe_vol1_pie_to_pgmc.txt:11867-11870; @Ringe2006, p. 271]. Clark Hall and Orel likewise cite source-style `þerscan/ðerscan`, not the dataset's normalized `þresċan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:42703-42705; docs/references/orel_handbook_germanic_etymology.vision.txt:47103-47108; @ClarkHall1960, s.v. "þerscan"; @Orel2003, p. 426]. These are not competing lexical identities. They are different notation and citation layers around the same inherited strong verb.

The live derivation itself is uncomplicated once those layers are kept separate. The trace starts from `*θréskaną`, drops final `*-ą` after the heavy stem to give `*θréskan`, passes through a secondary-nasalization stage `*θréskąn`, shifts `sk` to `ʃ`, and then reduces the weak tail to `*θréʃan`, orthographic `þ*résċan`, surface `þresċan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5284-5297]. Unlike rows such as `sċieran` or `sċeaft`, this row does **not** require West-Saxon palatal diphthongization to explain the vowel, and the live trace shows no `OEIUmlaut` stage at all. The row's short `e` therefore belongs to the ordinary inherited vocalism of the present stem, not to a later `ie/ea` rescue path.

The usable DEV_NOTES support is shared rather than row-local, but it still preserves two points later report writers would otherwise have to reconstruct. First, DEV_NOTES explicitly labels heavy-syllable loss of final `*-ą` an “empirically-derived phonological finding” rather than a rule copied directly from the standard literature [Germanic/docs/DEV_NOTES.md:1595-1615]. That matters because the row's trace uses exactly that step at the start of the OE portion. Second, DEV_NOTES warns that the project's `sk -> sc` label is easy to misread: “The `sk -> sc` change is not palatalization but a general OE shift of `/sk/ -> /ʃ/` spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. For row `2253`, that caution is directly applicable. The trace label `OE Sk Palatalization` is project shorthand for the phonological shift to `ʃ`; the final `-sċ-` spelling belongs to the orthographic layer.

A third DEV_NOTES fragment is worth keeping only as notation history. The secondary-nasalization discussion proposed a distinct symbol `{*ã}` for contact nasalization and explicitly said that this was “NOT yet in FST” at that stage [Germanic/docs/DEV_NOTES.md:9610-9636]. The live trace for row `2253` now does contain `OE Secondary Nasalization`, but it writes the intermediate form with ogonek `*θréskąn`, not with a separate tilde symbol [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5289-5291]. That difference is project chronology, not lexical substance. It should not be allowed to obscure the simple current row verdict: the live row is regular and exact.

The conservative current reading is therefore narrow but stable. `PROTO` and `PROTOFORM` remain `*θréskaną`; `COUNTERPART` remains `þresċan`; the trace already lands exactly on that target; and the surviving DEV_NOTES material is mostly shared rule/notation background rather than a lexeme dossier [Germanic/data/germanic-aligned-final.tsv:1253-1253; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5277-5297]. That makes this a useful replacement working note, but still a weak candidate for index extraction unless stronger row-local DEV_NOTES or packet-level support is added later.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-1591-1645

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1645`
- Fragment type: `archived_shared_rule_fragment`
- Status: `archived_but_still_live_in_trace`
- Issue tags: `heavy_syllable_apocope`; `*-ą`; `shared_phonology`; `project_internal_rule`
- Recommended next use: `use_with_caution_in_final_report`

This fragment is relevant because the live `þresċan` trace begins with exactly the step it discusses: `*θréskaną -> *θréskan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5286-5291]. DEV_NOTES says the rule deleting final `*-ą` after heavy stems was an “empirically-derived phonological finding” and adds that neither Ringe–Taylor nor Hogg explicitly states the extension to `*-ą` [Germanic/docs/DEV_NOTES.md:1595-1615]. For row `2253`, this is useful project-history explanation, but it is weaker than a direct lexeme citation and should be treated as shared modelling background rather than as row-local philological proof.

### DEV_NOTES:line-2991-2993

- Source heading: `Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)`
- Source line or section hint: `lines 2991-2993`
- Fragment type: `notation_layer_fragment`
- Status: `diagnostic_but_reusable`
- Issue tags: `sk_shift`; `notation`; `rule_naming`; `orthography`
- Recommended next use: `cite_for_terminology_only`

This short note is not about `þresċan` by name, but it is the clearest surviving DEV_NOTES statement about the exact change that matters for the row's medial `-sċ-`. DEV_NOTES says: “The `sk -> sc` change is not palatalization but a general OE shift of `/sk/ -> /ʃ/` spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2993-2993]. That sentence should be carried forward because the published trace still labels the step `OE Sk Palatalization` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5289-5291]. For row `2253`, the reusable point is narrow but important: the historical stage is `/sk/ > /ʃ/`; dotted `sċ` is an editorial/project spelling layer.

### DEV_NOTES:line-9592-9650

- Source heading: `Primary vs Secondary Nasalization: The Correct Solution`
- Source line or section hint: `lines 9592-9650`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `secondary_nasalization`; `symbol_proposal`; `notation_history`; `coda_nasal_environment`
- Recommended next use: `use_as_project_history_only`

This fragment is worth preserving only because the live row trace includes `OE Secondary Nasalization: *θréskąn` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5289-5291]. DEV_NOTES distinguishes primary `{*ą}` from a proposed secondary/contact-nasalization symbol `{*ã}` and states that the latter was “NOT yet in FST” at that stage [Germanic/docs/DEV_NOTES.md:9610-9636]. For row `2253`, this is notation history, not current row policy: the running trace now has the stage, but the project still writes the intermediate with ogonek rather than with a separate tilde symbol.

## Superseded or diagnostic material

- No row-specific DEV_NOTES section for `þresċan` currently survives. That absence is itself diagnostically important: the row is supported mainly by an exact live derivation plus shared background notes, not by a dedicated lexeme-level project argument [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5277-5297; Germanic/docs/lexeme_reports/coverage_audit.md:393-393].
- The heavy-syllable `*-ą` apocope note is still partly provisional in evidentiary status. DEV_NOTES explicitly presents it as a modelling discovery rather than a rule directly stated in the handbook literature [Germanic/docs/DEV_NOTES.md:1595-1615]. That does not make row `2253` unstable, but it does limit how strong the row's attachable DEV_NOTES support is.
- The secondary-nasalization symbol proposal `{*ã}` is superseded as live notation. It belongs to project chronology only; the current published trace already uses `OE Secondary Nasalization` while writing the intermediate as `*θréskąn`, and neither notation choice changes the row's current `COUNTERPART þresċan` [Germanic/docs/DEV_NOTES.md:9592-9650; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5289-5291].
- Source-style lexeme spellings such as `þerscan` or `ðerscan` should be treated as dictionary/manuscript citation layers, not as evidence that the live row must be rewritten away from `þresċan` [docs/references/ringe_vol1_pie_to_pgmc.txt:11869-11870; docs/references/orel_handbook_germanic_etymology.vision.txt:47103-47108; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:42703-42705; @Ringe2006, p. 271; @Orel2003, p. 426; @ClarkHall1960, s.v. "þerscan"].

## Open questions for later work

- If this row ever gets fuller report treatment, decide whether the final prose should foreground source-style `þerscan/ðerscan` alongside the dataset's normalized `þresċan`, while making explicit that these are citation/orthography layers rather than different row targets.
- If future indexing work wants stronger support, add a genuinely row-local packet or memo with direct lexicographic quotation for the OE lexeme; the current slice rests mostly on shared DEV_NOTES rule notes plus the exact trace, which is probably too thin for confident indexing.
- If later writeup discusses nasalization, keep chronology separate: older DEV_NOTES proposed `{*ã}` for secondary nasalization, the current running trace writes `*θréskąn`, and neither notation issue changes the row's stable regular outcome `þresċan`.

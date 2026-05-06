---
row_id: 2090
concept: lap
counterpart: lappa
proto: *lábbaz
protoform: *láppô
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2090 lap / lappa

## Current row state

- CONCEPT: `lap`
- COUNTERPART: `lappa`
- PROTO: `*lábbaz`
- PROTOFORM: `*láppô`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: empty. The live row therefore already encodes the successful OE-facing solution only indirectly: `COUNTERPART = lappa` and `PROTOFORM = *láppô` match the current derivational analysis, while `PROTO = *lábbaz` survives as older cognate-set residue from the wider family and is not itself the row's active OE derivational input [Germanic/data/germanic-aligned-final.tsv:621-621; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:13-20,52-59,79-87].
- `oe_known_problems.tsv`: no row-local entry. The required check finds no hit for row 2090 or this lexeme, and the packet records `_None_` under matching `oe_known_problems.tsv` entries [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md:42-45].
- Packet status: the packet is strong on current project state. Its compact derivation trace is exact for the live OE-facing setup — `PROTO: *láppô`, `EXPECTED: lappa`, `OUTPUTS: lappa` — and its OE-side steps explicitly show Anglo-Frisian brightening `*læppô`, OE A-restoration `*lappô`, and unstressed long-vowel shortening `*lappa`; the packet also records `_No manifest entry._` for this row [Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md:11-13,17-40].
- Memo status: the memo treats the row as mostly solved but insists on a three-way distinction that later report prose must preserve: stale comparative/cognate-set `PROTO = *lábbaz`, active project input `PROTOFORM = *láppô`, and OE target `lappa`. It also states that `læppa` and `leappan` are real philological evidence, but as variant/headword or oblique/paradigm background rather than the row target [Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:13-20,44-48,52-70,79-87].
- Current DEV_NOTES authority status: current row-specific DEV_NOTES authority **does exist**, but it is partial. DEV_NOTES securely supports weak-noun `pp`, OE-facing `*lappô/*láppô`, and target `lappa`; no current DEV_NOTES fragment defends the live comparative `PROTO = *lábbaz` as row-level authority [DEV_NOTES:line-14162-14348,36676-36775; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:13-20,54-59,86-87].

## Development-note summary

This row has a real current DEV_NOTES dossier, unlike rows where only shared chronology survives. The dedicated 2026-04-06 section establishes the philological and project-local solution: the old row state `*labbăz → læppa` was wrong both in consonant quality and stem class, because the OE noun is a weak masculine with `pp`, not an a-stem with `bb`; DEV_NOTES then tests the relevant inputs and records that `*lappô` yields `lappa`, while `*lappō` and `*lappăz` do not give the needed noun [DEV_NOTES:line-14154-14221]. The same section preserves the source hierarchy behind that choice: Brunner lists `lappa` with variants `laeppa` and plural `leappan`; Campbell cites “lappa skirt” as an A-restoration example; Kluge-Seebold explicitly contrasts OE `lappa` and `læppa`; Orel keeps a masculine n-stem `*lappōn`; and Kroonen's broader ablauting n-stem analysis supports a weak family with voiceless `p/pp`, not `b/bb` [DEV_NOTES:line-14164-14317].

Later DEV_NOTES material confirms that this was not a one-off April guess. In the §17.25 regression loop, `*láppô → lappa` is named explicitly as a new mismatch only because the first build accidentally broke A-restoration before geminates and failed to treat trimoric `*ô` as a strong restoration trigger. The subsequent fix restores `*láppô → lappa` and preserves it in post-fix verification [DEV_NOTES:line-36676-36775]. For row 2090, that later note matters because it reaffirms that `lappa` is the intended regular outcome of `*láppô`; it does **not** reopen `læppa` as the preferred target.

The slice therefore has to keep three levels separate. `PROTO = *lábbaz` is live row metadata but stale row authority; it reflects older cognate-set bookkeeping and the pre-fix state still visible in the packet and memo [Germanic/data/germanic-aligned-final.tsv:621-621; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:13-20,74-87]. `PROTOFORM = *láppô` is the active project input that the packet trace and later regression fix both validate [Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md:17-40; DEV_NOTES:line-14214-14221,36757-36775]. `COUNTERPART = lappa` is the OE target supported by DEV_NOTES and by the checked grammar/dictionary discussion; `læppa` and `leappan` are not false forms, but they are variant or paradigm background only for this row [DEV_NOTES:line-14164-14317,14320-14345; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:44-48,62-70].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-14162-14317

- Source heading: `OE læppa 'lap, skirt': n-stem with voiceless *pp (2026-04-06)`
- Source line or section hint: `lines 14162-14317`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `stem_class`; `voicing`; `a_restoration`; `attested_variants`; `proto_vs_protoform`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main row-level source-audit fragment. DEV_NOTES first assembles the grammatical and lexicographic evidence that the noun belongs to a weak `pp`-stem family: Brunner “Lists `lappa` (with variants `laeppa`, plural `leappan`) as swm,” Campbell “Cites `lappa` as example of a-restoration before geminate,” and Kluge-Seebold quotes “ae. lappa (vereinzelt); mit anderem Vokal ae. læppa” [DEV_NOTES:line-14164-14176]. DEV_NOTES then uses Kroonen and Orel differently but compatibly: Kroonen is invoked for the deeper ablauting n-stem structure and for the point that the root is voiceless `*p`, not voiced `*b`, while Orel's `*lappōn sb.m.: OE læppa` confirms the n-stem classification and the `pp` consonantism even though Orel preserves the `læppa` citation [DEV_NOTES:line-14178-14317]. For row 2090 this fragment is current authority that the row should be documented as a weak noun with `pp`, with OE `lappa` as the regular restored citation-form target; `læppa` and `leappan` remain comparator/background evidence rather than rival row targets [Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:44-48,62-70].

### DEV_NOTES:line-14318-14348

- Source heading: `OE læppa 'lap, skirt': n-stem with voiceless *pp (2026-04-06)`
- Source line or section hint: `lines 14318-14348`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `target_selection`; `fst_verification`; `implementation`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current implementation fragment for the OE-facing solution. DEV_NOTES states the project conclusion directly: “**Opinio communis:** PGmc `*lappô` (masc. n-stem nom.sg.) with voiceless `*pp`,” “**FST solution:** `*lappô` → `lappa`,” and “Since `lappa` is the phonologically regular outcome and is well-attested, we use it as our target form” [DEV_NOTES:line-14320-14331]. It then preserves the change log and direct verification: “Before: `*labbăz` → `læppa` / After: `*lappô` → `lappa`,” followed by `echo "lappô" | flookup ...` returning `lappô    lappa` and `✓ Match achieved` [DEV_NOTES:line-14333-14348]. This remains current authority for the row's active OE-facing pair, but it must be read with the live TSV distinction made explicit: the row now keeps the same solution as `PROTOFORM = *láppô`, `COUNTERPART = lappa`, while live `PROTO = *lábbaz` is still stale comparative residue rather than the defended row proto [Germanic/data/germanic-aligned-final.tsv:621-621; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:13-20,79-87].

### DEV_NOTES:line-36676-36775

- Source heading: `§17.25.7 Regression after first build — diagnosis and follow-up fix`; `§17.25.8 Post-fix verification`
- Source line or section hint: `lines 36676-36775`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `a_restoration`; `geminate_handling`; `trimoric_o`; `regression_fix`; `verification`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2141`; `2240`

This shared regression note is current because it re-checks the exact pair `*láppô → lappa` after later rule surgery. DEV_NOTES says the first build broke restoration before geminates because `EnglishStarGeminate` had been defined with impossible multi-character symbols and because trimoric `*ô` had been omitted from `OEARestorationStrongOTail`; as a result the new rule “incorrectly bleed[ed] it for `*láppô → læppa` (target `lappa`)” [DEV_NOTES:line-36676-36725]. The same note then predicts and verifies the repair: after fixing geminate matching and adding `{*ô}`, post-fix probes include “`*láppô → lappa` ✓ (Bug A fixed: geminate now matches as two segments)” [DEV_NOTES:line-36742-36775]. For row 2090, this fragment is not new source audit about the lexeme itself; it is current implementation authority showing that `lappa` is the intended regular A-restored outcome of trimoric weak-noun `*láppô`. The parallel mentions of row 2240 `*táppô` and row 2141 `*márōn` are comparator/background only and should not be allowed to blur row 2090's separate target decision [Germanic/data/germanic-aligned-final.tsv:819-819,1202-1202].

### DEV_NOTES:line-14152-14160

- Source heading: `OE læppa 'lap, skirt': n-stem with voiceless *pp (2026-04-06)`
- Source line or section hint: `lines 14152-14160`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_row_state`; `mismatch_history`; `wrong_voicing`; `wrong_stem_class`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This opening problem statement should be preserved only as labelled history. DEV_NOTES records the old row exactly as it stood at the time — “**TSV row 2090:** `*labbăz → læppa`,” “**FST output:** `*labbăz → læbb`,” with two stated problems: wrong voicing (`bb` instead of `pp`) and wrong stem class (a-stem instead of weak n-stem) [DEV_NOTES:line-14154-14160]. That framing is no longer current row authority because the live row already carries `PROTOFORM = *láppô` and `COUNTERPART = lappa` [Germanic/data/germanic-aligned-final.tsv:621-621]. It remains diagnostically important, however, because the live comparative `PROTO = *lábbaz` still preserves part of the older setup; later report work should therefore keep this fragment as checked project history rather than pretending the old `*lábbaz` analysis never existed [Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:74-87].

## Superseded or diagnostic material

- The dedicated April 2026 DEV_NOTES section is current for the OE-facing solution, but its wording “Change proto ... to `*lappō`/`*lappô`” and “Before/After” must not be quoted as if the live row had fully harmonized every metadata field. The live row still carries `PROTO = *lábbaz`, so current row authority is narrower: `*láppô -> lappa` is current; the comparative `*lábbaz` field is stale residue still waiting on explicit cleanup elsewhere [DEV_NOTES:line-14198-14221,14333-14348; Germanic/data/germanic-aligned-final.tsv:621-621; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:98-106].
- The progress-log entry “TSV fixes: dile, lappa, cnobba” is useful chronology only. It confirms when row 2090 entered the resolved bucket, but it adds no row-specific philology beyond the dedicated section and later regression note [DEV_NOTES:line-10393-10395; Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md:80-90].
- `læppa` is not a false positive and should not be erased, but it is misleading if uncontextualized to treat it as the live row target. DEV_NOTES, the packet, and the memo all agree that `lappa` is the regular restored citation-form outcome of `*láppô`, whereas `læppa` is variant/headword tradition and `leappan` is oblique/dialect-paradigm evidence [DEV_NOTES:line-14223-14331; Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md:17-40; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:62-70].
- The analysis files named in packet and memo are supportive background, not row-specific authority. `arestoration_r_l_research.md` reproduces Campbell/Brunner/Luick quotations for `lappa`, and `ws_vs_anglian_dialect_differences.md` preserves the WS/Mercian contrast `lappa` versus `leappa`, but neither file by itself replaces the dedicated DEV_NOTES section for row 2090 [Germanic/docs/lexeme_reports/packets/2090-lap-lappa.md:178-216; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:28-39].

## Open questions for later work

- If the row is ever cleaned up elsewhere, decide how the live comparative `PROTO` should be harmonized with the current row authority. The checked materials support weak-noun `pp`-stem analysis and active `PROTOFORM = *láppô`, but they do not support leaving `*lábbaz` as if it were the row's defended proto [Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:52-59,98-106].
- Any later final report should state explicitly that `lappa` is the selected OE target, `læppa` is a real variant/headword form, and `leappan` is paradigm/dialect background, not a rival citation-form target [DEV_NOTES:line-14164-14176,14250-14293; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:62-70].
- If later report prose wants a compact source hierarchy, keep Kroonen/Orel/Brunner/Campbell distinct rather than collapsing them into one proto label: Kroonen supplies the broader ablauting weak-family background, Orel supports the n-stem with `pp`, and Brunner/Campbell provide the clearest row-local support for OE `lappa` as the regular restored form [DEV_NOTES:line-14164-14317; Germanic/docs/lexeme_reports/research_memos/2090-lap-lappa.md:44-48].

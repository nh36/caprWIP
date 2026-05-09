---
row_id: 2224
concept: straw
counterpart: strēaw
proto: *stráwą
protoform: *stráwą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2224 straw / strēaw

## Current row state

- Live OE row `2224` currently reads `CONCEPT = straw`, `COUNTERPART = strēaw`, `PROTO = *stráwą`, `PROTOFORM = *stráwą`, `DERIVATION_CLASS = regular`; the row carries only duplicated Wiktionary inheritance sourcing and no live exception note [Germanic/data/germanic-aligned-final.tsv:1141-1141].
- The row therefore does **not** currently split comparative `PROTO` from OE-facing `PROTOFORM`. Both project fields use the same input `*stráwą`; the OE target selected for the row is `strēaw` [Germanic/data/germanic-aligned-final.tsv:1141-1141].
- `oe_known_problems.tsv` has no entry for row `2224`, `strēaw`, or `*stráwą`, so the lexeme is not being tracked as a live OE mismatch or documented exception there [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still lists row `2224 | straw | strēaw | regular | no | - | - | - | none`, so there is no existing packet, research memo, dossier, or full report stem to reuse; the canonical row-based filename is therefore appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:376-376].
- The current published OE derivation trace is an exact match and makes the active rule ordering explicit: `PROTO: *stráwą`, `EXPECTED: strēaw`, `OUTPUTS: strēaw`, with `OE Aw Long Diphthong: *strḗawą` followed by `OE Heavy Syllable Nasal Apocope: *strḗaw` before surface `Outcome: strēaw` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4806-4825].
- Comparative and lexical source support aligns with the live target while using different notation layers. Kroonen gives the noun as `*strawa- n. 'straw'` with `OE strēa(w) n. 'id.'`; Campbell derives `*straua- > *strau > OE *stréa straw` and immediately adds that the form is “Usually found with addition of w from inflected forms, stréaw”; Clark Hall lists `strēaw (ē) n. 'straw,' hay` [@Kroonen2013, p. 483; @Campbell1959, §§120.3, 584; @ClarkHall1960, s.v. "strēaw"].

## Detailed development-note summary

The surviving DEV_NOTES support for row 2224 is very thin, but it is still usable because it records the exact row-level correction that matters. The only securely attachable lexeme mention is the fix list under the introduction of the `OE Aw Long Diphthong` rule: `*strawą → strēaw (was streaw) — straw` [Germanic/docs/DEV_NOTES.md:3642-3645]. For replacement-note purposes, that one line means the row's earlier problem was **not** uncertainty about which OE lexeme to target. The problem was that the old derivation undergenerated the expected long diphthong outcome and had been landing at `streaw`; once the new rule was placed “After OEEwLongDiphthong, before AngloFrisianBrightening,” the noun began deriving as `strēaw` instead [Germanic/docs/DEV_NOTES.md:3639-3645].

That narrow DEV_NOTES fix lines up well with both the live row and the current trace. The row now keeps `PROTO = PROTOFORM = *stráwą` and `COUNTERPART = strēaw`, with no active need for a surrogate protoform or analogical label [Germanic/data/germanic-aligned-final.tsv:1141-1141]. The trace then shows the exact two-step OE-side path: `*stráwą > *strḗawą > *strḗaw > strēaw` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4815-4825]. In other words, the present project treatment is simple and fully regular: inherited `*aw` is converted to OE `ēaw` by the long-diphthong rule, and the final nasalized vowel then drops in the ordinary heavy-syllable environment.

The notation layers need to stay distinct so the slice does not import confusion from dictionary headword formats. Kroonen's `*strawa-` is a comparative stem citation, not the row's literal FST input; the live row's OE-facing input is `*stráwą` [Germanic/data/germanic-aligned-final.tsv:1141-1141; @Kroonen2013, p. 483]. Likewise Kroonen's `OE strēa(w)` and Campbell's historical `*stréa` are not reasons to replace the row target with a different counterpart. Campbell explicitly says that the form was “Usually found with addition of w from inflected forms, stréaw,” which is exactly the normalization the row now uses as `strēaw` [@Campbell1959, §120.3]. Clark Hall's straightforward lemma `strēaw` supports that current target choice directly [@ClarkHall1960, s.v. "strēaw"].

Because the DEV_NOTES evidence is so slight, later report writers should resist overclaiming. There is no surviving row-dedicated essay in `DEV_NOTES.md` on stem class, paradigm rebuilding, or dialectal competition. The secure current conclusion is only that the row once surfaced incorrectly as `streaw`, that the `OE Aw Long Diphthong` rule was added to fix exactly that kind of case, and that the live grammar now produces the attested/selected OE noun `strēaw` regularly [Germanic/docs/DEV_NOTES.md:3639-3645; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4806-4825].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3639-3645

- Source heading: `Pipeline placement` / `Fixes (3 new matches)`
- Source line or section hint: `lines 3639-3645`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `oe_aw_long_diphthong`; `exact_match_fix`; `former_output_streaw`; `regular_row`
- Recommended next use: `cite_if_documenting_row_fix`
- Shared with row IDs: `2050`; `2059`

This is the controlling DEV_NOTES fragment for row 2224 because it gives both the rule context and the lexeme-specific correction in one place. DEV_NOTES says the new rule is placed “After OEEwLongDiphthong, before AngloFrisianBrightening” and then lists among the three new matches: `*strawą → strēaw (was streaw) — straw` [Germanic/docs/DEV_NOTES.md:3639-3645]. For this row, the line should be read as a precise project-history statement: the OE target `strēaw` was already the intended target, and the correction was to the derivational path that had previously produced `streaw`.

The fragment is also best read together with the current trace and handbook support. Campbell's `*straua- > *strau > OE *stréa` plus the note that the word is usually found as `stréaw`, and Kroonen's `OE strēa(w)`, both match the DEV_NOTES direction of travel: the noun belongs with the `ēa/ēaw` outcome, not with the earlier short-vowel-like project output `streaw` [@Campbell1959, §§120.3, 584; @Kroonen2013, p. 483].

## Superseded or diagnostic material

- The superseded item here is the older output `streaw` preserved in the DEV_NOTES fix list. It is useful as project chronology, but it should not be treated as a competing OE target or as evidence that the live row needs further repair [Germanic/docs/DEV_NOTES.md:3644-3644].
- Campbell's historical intermediate `*stréa` is also diagnostic rather than row-replacing. Campbell immediately notes that the noun is usually found with analogical or paradigm-supported `-w`, i.e. `stréaw`; Kroonen likewise writes `strēa(w)` to signal that relationship rather than to set up a rival lemma against `strēaw` [@Campbell1959, §120.3; @Kroonen2013, p. 483].
- No surviving row-local DEV_NOTES material suggests a `PROTO`/`PROTOFORM` split, an analogical exception label, or a different counterpart. The live row and live trace both point instead to a solved regular derivation [Germanic/data/germanic-aligned-final.tsv:1141-1141; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4806-4825].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited later, the only strong fragment to consider is `DEV_NOTES:line-3639-3645`; even that fragment is short and shared, so the row likely remains better kept as no-index unless the project decides to index concise rule-fix notes.
- If a fuller lexeme report is ever written, it would be useful to cite the handbook contrast explicitly as `dictionary headword *strawa- / historical *stréa / attested-normalized strēaw`, because that is the only real interpretive trap left in the row's documentation [@Kroonen2013, p. 483; @Campbell1959, §§120.3, 584; @ClarkHall1960, s.v. "strēaw"].
- No current evidence supports changing `PROTO`, `PROTOFORM`, `COUNTERPART`, or `DERIVATION_CLASS`; later work here is more likely to be indexing cleanup than lexical reanalysis.

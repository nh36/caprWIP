---
row_id: 2233
concept: sup
counterpart: sūpan
proto: *sūpaną
protoform: *sūpaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
filename_basis: canonical_row_based_filename
---

# DEV_NOTES material — 2233 sup / sūpan

## Current row state

- The live OE row reads `CONCEPT = sup`, `COUNTERPART = sūpan`, `PROTO = *sūpaną`, `PROTOFORM = *sūpaną`, and `DERIVATION_CLASS = regular`; the `NOTE` field is empty, while the history field preserves duplicate Wiktionary-etymology provenance text [Germanic/data/germanic-aligned-final.tsv:1176-1176].
- `PROTO` and `PROTOFORM` are currently identical. The live project input is therefore the infinitive-shaped PGmc form `*sūpaną`, not a separate rescue `PROTOFORM`, not a comparative dictionary stem `*sūpan-`, and not Orel's citation form `*sūpanan` [Germanic/data/germanic-aligned-final.tsv:1176-1176; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25302-25310; @Kroonen2013, p. 493; docs/references/orel_handbook_germanic_etymology.vision.txt:43157-43160; @Orel2003].
- `oe_known_problems.tsv` has no row-local entry for `2233`, `sup`, `sūpan`, or `*sūpaną`; the current ledger only lists unrelated exception and wontfix items [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` still shows the row as uncovered and records no attached packet, memo, or fragment infrastructure: `| 2233 | sup | sūpan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:382-382].
- The published derivation traces are exact matches. The compact trace gives `PROTO: *sūpaną`, `EXPECTED: sūpan`, `OUTPUTS: sūpan`; the full trace shows no changes until ordinary OE infinitive-tail handling, then `OEHeavySyllableNasalApocope`, `OESecondaryNasalization`, `OEWeakTailReduction`, and `OldEnglishRemoveStars: sūpan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4968-4978; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:33644-33756].
- Local reference works support the verbal target directly. Clark Hall glosses `supan²` as “to swallow, sip, taste, 'sup,' drink”; Bright gives the strong-verb paradigm `supan, sēap supon sopen (2), sup, drink`; Kroonen gives PGmc `*sūpan-` “to guzzle, soak” with OE `supan`; Fulk cites the same strong-verb set through OIcel. `súpa`, OE `sūpan`, OFris. `sūpa`, MLG `sūpen`, and OHG `sufan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:38864-38865; @ClarkHall1960; docs/references/bright_anglo_saxon_reader.vision.txt:25476-25477; @BrightCassidyRingler1971; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25302-25310; @Kroonen2013, p. 493; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:16495-16496; @Fulk2018, §12.18].

## Detailed development-note summary

No attachable row-specific DEV_NOTES note currently survives for row `2233`. Literal searching turns up no `sūpan`, `*sūpaną`, or `sup` discussion in `Germanic/docs/DEV_NOTES.md`, and there is no existing packet or research memo stem to reuse. This slice therefore has to function as a replacement working note built from the live row, the current derivation traces, and basic lexical support, rather than as a compression of an older in-repo argument.

The main point to preserve is that the row is presently uncomplicated and regular, but its notation layers still need to stay distinct. The live row stores `PROTO = PROTOFORM = *sūpaną`, i.e. the project's infinitive-shaped PGmc input [Germanic/data/germanic-aligned-final.tsv:1176-1176]. Comparative reference works cite the same lexeme in different formats: Kroonen uses headword `*sūpan-`, while Orel uses infinitive-like `*sūpanan` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25302-25310; @Kroonen2013, p. 493; docs/references/orel_handbook_germanic_etymology.vision.txt:43157-43160; @Orel2003]. Those are citation-format differences, not evidence that the live row needs a distinct `PROTOFORM` or a different OE target.

The OE target itself is also straightforwardly verbal. Clark Hall's wording is worth preserving because it captures the semantic range later writers might otherwise have to reassemble: `supan²` is “to swallow, sip, taste, 'sup,' drink” [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:38864-38865; @ClarkHall1960]. Bright confirms that the row target is the infinitive of a strong verb, not an extracted noun or participial citation form: `supan, sēap supon sopen (2), sup, drink` [docs/references/bright_anglo_saxon_reader.vision.txt:25476-25477; @BrightCassidyRingler1971]. Kroonen and Fulk keep the broader comparative set aligned with that same verb [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25306-25310; @Kroonen2013, p. 493; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:16495-16496; @Fulk2018, §12.18].

The derivation trace matters because it shows that row `2233` is not hiding a silent workaround. The full trace leaves the root vowel and consonants untouched through Proto-Germanic, Proto-West-Germanic, and Northwest Germanic stages, then applies only the ordinary OE tail rules: `OEHeavySyllableNasalApocope: *s*ū*p*a*n`, `OESecondaryNasalization: *s*ū*p*ą*n`, `OEWeakTailReduction: *s*ū*p*a*n`, and finally `OldEnglishRemoveStars: sūpan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:33644-33756]. That exact-match result agrees with the compact trace and with the absence of any reservation in `oe_known_problems.tsv` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4968-4978; Germanic/data/oe_known_problems.tsv:1-8].

Because there is no row-specific DEV_NOTES prose to attach, this row should presently remain a no-index slice. The evidence bundle is sufficient to justify the live row and to explain its notation, but not to support an `index.tsv` fragment entry. The only DEV_NOTES material found during preparation was a neighboring but different lexeme (`sūcan`), and that should stay explicitly non-authoritative for `sūpan`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-14372-14404

- Source heading: `research note on NWGmc analogical *ū verbs`
- Source line or section hint: `lines 14372-14404`
- Fragment type: `unrelated_search_hit`
- Status: `not_row_relevant`
- Issue tags: `search_false_positive`; `neighboring_lexeme`; `analogical_u`
- Recommended next use: `do_not_index`
- Shared with row IDs:

This is the only nearby DEV_NOTES hit that can mislead later work, so it is worth parking explicitly as non-row material. DEV_NOTES quotes Ringe & Taylor and Campbell on verbs with innovative present-system `*ū`, preserving the list `*brūcan* 'use', *būgan* 'bend', *lūcan* 'lock', *strūdan* 'rob', *sūcan* 'suck'` [Germanic/docs/DEV_NOTES.md:14374-14404; @RingeTaylor2014, pp. 39-40; @Campbell1959, §740]. That fragment is about `sūcan`, not `sūpan`, and about analogical remodeling of `*eu/*ū` ablaut in another verbal set. Its only value for row `2233` is diagnostic: the shared long `ū` must not be mistaken for evidence that `sūpan` participates in the `sūcan` discussion.

## Superseded or diagnostic material

No superseded row-local proposal is currently recoverable. There is no surviving DEV_NOTES correction narrative of the kind seen for rows with a former wrong counterpart, a rescued paradigm cell, or an abandoned sound-law detour. The absence itself is the main diagnosis: the row appears stable and regular in the live system, but the older internal rationale was never written up as a dedicated DEV_NOTES item.

The only diagnostic caution worth preserving is bibliographic rather than phonological. Comparative sources cite the same lexeme as `*sūpaną`, `*sūpan-`, or `*sūpanan`; those are not competing project policies, only different citation conventions [Germanic/data/germanic-aligned-final.tsv:1176-1176; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25302-25310; @Kroonen2013, p. 493; docs/references/orel_handbook_germanic_etymology.vision.txt:43157-43160; @Orel2003]. Later report work should keep that distinction explicit instead of silently treating one dictionary headword shape as a reason to edit the live row.

## Open questions for later work

- If a future internal note is added, it should state plainly that the live project input is `*sūpaną`, while comparative dictionaries may cite `*sūpan-` or `*sūpanan`; that notation distinction is the main thing later writers would otherwise have to rediscover [Germanic/data/germanic-aligned-final.tsv:1176-1176; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25302-25310; @Kroonen2013, p. 493; docs/references/orel_handbook_germanic_etymology.vision.txt:43157-43160; @Orel2003].
- If a later lexeme report wants a source quotation, Clark Hall and Bright already provide concise reusable wording for the OE verb and paradigm, and those quotations are better evidence than trying to mine unrelated DEV_NOTES material [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:38864-38865; @ClarkHall1960; docs/references/bright_anglo_saxon_reader.vision.txt:25476-25477; @BrightCassidyRingler1971].
- `index.tsv` should remain untouched for now. Until there is a real row-specific DEV_NOTES fragment rather than the unrelated `sūcan` hit, there is nothing worth indexing for `2233`.

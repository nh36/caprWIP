---
row_id: 2022
concept: fly
counterpart: flēogan
proto: *fléuganą
protoform: *fléuganą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2022 fly / flēogan

## Current row state

- CONCEPT: `fly`
- COUNTERPART: `flēogan`
- PROTO: `*fléuganą`
- PROTOFORM: `*fléuganą`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T 10088: PGmc *fleugaṇ > OE flēogan; flȳġe is derived form` [Germanic/data/germanic-aligned-final.tsv:357].
- `oe_known_problems.tsv`: no entry was found for `*fléuganą`, `flēogan`, or this row during the required source check.
- `report_manifest.tsv`: no row-specific manifest entry is currently attached; the packet records manifest status as `_No manifest entry._` [Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:11-13].
- Packet state is internally clean and regular: `EXPECTED: flēogan`, `OUTPUTS: flēogan`, with the OE-side derivation shown as diphthong leveling plus ordinary tail reduction from `*fléuganą` to `flēogan` [Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:17-42].
- The research memo makes the row-level distinction explicit: this is a note-bearing regular row whose real working problem is lexical disambiguation, not a broken sound change; `flēogan` is the attested OE verb, while `flȳġe`, `fléoge/flége`, and Anglian `flégan` are related but non-row forms [Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:13-20, 49-89].

## Development-note summary

No securely attachable **row-specific** DEV_NOTES authority survives for row 2022. The live row is already coherent as a regular verbal derivation `*fléuganą -> flēogan`, and the only DEV_NOTES material that surfaced in the required review is not about the row's own infinitive/citation form at all. Instead, it concerns a hypothetical related derivative `*fláugiz -> flīeġ`, cited during a broader FST probe of `*au + i` outcomes [DEV_NOTES:line-35460-35475; Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:56-70].

That absence of row-local DEV_NOTES argument matters because the replacement note still has to preserve the real project distinction. The row's `PROTO` and `PROTOFORM` are the same verbal input `*fléuganą`, and the target is the attested OE verb `flēogan`, not some repaired comparator or paradigm-cell workaround [Germanic/data/germanic-aligned-final.tsv:357; Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:17-42]. The memo is therefore right to treat this as a **lexeme-disambiguation** file: the danger is not that the transducer fails on row 2022, but that the English gloss `fly` points to more than one Old English form in repo-local materials [Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:77-89].

The current row note already encodes the key policy succinctly: `flȳġe is derived form` [Germanic/data/germanic-aligned-final.tsv:357]. The packet and memo unpack why that warning is needed. Repo-local lexical material splits between verbal `to fly = flēogan` and a separate lexical-table hit `fly = flȳġe`, while dialect/background notes also preserve West Saxon `fléogan` beside Anglian `flégan` and related noun-like forms `fléoge/flége` [Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:76-88, 98-115; Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:17-20, 42-47, 57-75]. Those are all relevant family forms, but none justifies retargeting row 2022 away from verbal `flēogan`.

The replacement-note conclusion should therefore stay explicit on three points. First, row 2022 is a **regular** derivation and does not belong in `oe_known_problems.tsv` [Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:44-46; Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:77-89, 111-119]. Second, there is no surviving DEV_NOTES dossier that argues for a different `PROTOFORM`, a different paradigm cell, or a different OE target. Third, the only DEV_NOTES hit worth recording is derivative-family background: it helps explain why forms such as `flīeġ` or `flȳġe` can appear elsewhere in the repo, but it is **not** authority against `*fléuganą -> flēogan` for this row [DEV_NOTES:line-35460-35475; Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:19-20, 57-63, 77-89].

## Relevant DEV_NOTES fragments

No securely attachable **current** row-specific DEV_NOTES fragment survives. The reviewed range below is kept only because later packet or index work may need an explicit record of the one derivative-family hit that was checked and rejected as row authority.

### DEV_NOTES:line-35460-35475

- Source heading: `FST probes for *au + i outcomes`
- Source line or section hint: `lines 35460-35475`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `derived_form`; `hypothetical_derivative`; `lexeme_disambiguation`; `packet_hygiene`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This range is useful only as controlled background. DEV_NOTES records the probe `*fláugiz -> flīeġ` and labels it a “hypothetical i-stem derivative of *flēogan* 'to fly'”; it then groups that derivative with other `*au + i` cases and concludes that such lexemes “ALL show WS īe (as predicted)” [DEV_NOTES:line-35468-35475]. That confirms something about a related derivative class, not about the row's own verbal infinitive `*fléuganą -> flēogan`.

For row 2022, the important point is negative. This fragment does **not** compete with the live row note, does **not** propose a different counterpart, and does **not** document a modelling failure. It survives here only so future packet work does not mistake a derivative-family comparison for direct authority on the verbal row.

## Superseded or diagnostic material

There is no surviving row-specific superseded analysis in DEV_NOTES comparable to the abandoned paradigm-cell repairs seen in other slices. The non-current material here is instead project-history noise around **gloss collision**. The memo records an older debugging phase in which regular output `flēogan` was being compared against `EXPECTED: flȳġe`; that history is now superseded by the live row note and the clean exact-match packet trace [Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:17-20, 77-89].

The other diagnostic caution is category confusion. Packet evidence shows `old_english_wiktionary.tsv` giving `fly = flȳġe`, while `old_english_swadesh.tsv` gives `to fly = flēogan` [Germanic/docs/lexeme_reports/packets/2022-fly-flēogan.md:76-88]. The memo's reading is the correct one for current workflow: `flȳġe` is a related derived/headword form and should remain background only, not a reason to rewrite the row [Germanic/docs/lexeme_reports/research_memos/2022-fly-flēogan.md:18-20, 45-47, 69-89].

## Open questions for later work

- If a final lexeme report is drafted, state part of speech explicitly as **verb** `flēogan` so the English gloss `fly` cannot be confused with noun-like or derived forms such as `flȳġe`.
- If later index cleanup prefers to suppress reviewed-only false positives, preserve at minimum the explicit statement that row 2022 has **no securely attachable row-specific DEV_NOTES authority**, rather than implying that a richer DEV_NOTES dossier was omitted.
- If later family-level discussion cites Anglian `flégan` or related `fléoge/flége`, keep those forms clearly subordinate to the row's own normalized West Saxon target `flēogan`.

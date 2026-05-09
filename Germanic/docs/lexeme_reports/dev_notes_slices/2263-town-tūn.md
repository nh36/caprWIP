---
row_id: 2263
concept: town
counterpart: tūn
proto: *tūną
protoform: *tūną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2263-town-tūn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2263 town / tūn

## Current row state

- CONCEPT: `town`
- COUNTERPART: `tūn`
- PROTO: `*tūną`
- PROTOFORM: `*tūną`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current OE row keeps both proto fields at `*tūną`, targets attested OE `tūn`, and carries the note `Proto: oblique *tūnăn→*tūną (n. a-stem nom.sg.; Kroonen)` [Germanic/data/germanic-aligned-final.tsv:1292-1292].
- Coverage status: `coverage_audit.md` marks row `2263` as needing report coverage because the row has a `NOTE`, not because of a known derivational failure or pre-existing attached fragment [Germanic/docs/lexeme_reports/coverage_audit.md:157-157].
- Packet status: the row-level packet is already clean on the derivational side: `PROTO: *tūną`, `EXPECTED: tūn`, `OUTPUTS: tūn`, with the only OE-side change shown as `OE Heavy Syllable Nasal Apocope: *tūn` [Germanic/docs/lexeme_reports/packets/2263-town-tūn.md:17-42].
- Memo status: the row-specific memo correctly reframes the problem as representational rather than phonological. It distinguishes comparative lemma conventions such as Kroonen's `*tūna-` and Orel's `*tūnan ~ *tūnaz` from the live project input `*tūną`, and it explicitly warns that the current note's `*tūnăn` wording is not supported by the checked Kroonen entry [Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md:25-35,42-48,58-80].
- DEV_NOTES support status: the packet's DEV_NOTES section is `_None_` for this row, and that is materially accurate apart from a concept-name false positive discussed below [Germanic/docs/lexeme_reports/packets/2263-town-tūn.md:48-60].

## Development-note summary

No securely attachable **current row-specific DEV_NOTES analysis** survives for `town / tūn`. That absence should be stated plainly. The live row is already a successful regular derivation, and the only string-level DEV_NOTES hit found during packet generation is an unrelated Old Frisian `burch 'town' < PWGmc *burg` quotation that matches the English gloss `town` but not the lexeme `tūn` or the proto input `*tūną` [Germanic/docs/DEV_NOTES.md:10939-10942; Germanic/docs/lexeme_reports/packets/2263-town-tūn.md:78-92]. This slice therefore cannot honestly present a lexeme-local DEV_NOTES dossier where none exists.

The durable row-level content comes instead from the live TSV row, the packet/memo pair, and the comparative dictionaries already checked in the memo. Those sources support a conservative three-way distinction that should remain explicit in any later report. `PROTO = *tūną` is the row's current cognate-set label in the TSV; `PROTOFORM = *tūną` is the actual OE-facing derivational input currently fed to the transducer; and `COUNTERPART = tūn` is the attested Old English citation form produced by the regular pipeline [Germanic/data/germanic-aligned-final.tsv:1292-1292; Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md:42-48]. The fact that `PROTO` and `PROTOFORM` currently contain the same string should not blur those roles.

The checked comparative sources also show why the TSV note needs to be read cautiously rather than repeated as if it were established DEV_NOTES authority. Kroonen's repo-local entry gives `*tūna- n. 'fenced area'` and daughter-language OE `tūn m. 'enclosed piece of ground, yard; town'`, which supports the lexical equation but does **not** itself give the row note's wording `oblique *tūnăn→*tūną` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26863-26864; @Kroonen2013]. Orel uses a different headword convention again: `*tūnan` / `*tūnaz sb.m./n.` with OE `tún 'enclosure, court, yard'` [docs/references/orel_handbook_germanic_etymology.vision.txt:45729-45734; @Orel2003]. For this row, those are best treated as **comparative headword conventions**, not as reasons to rewrite the live project input away from `*tūną`.

On the OE side, nothing in the checked material suggests a problematic counterpart. The packet trace already shows the current derivation succeeding regularly, and the memo is right that no paradigm-cell substitution is being used or needed here [Germanic/docs/lexeme_reports/packets/2263-town-tūn.md:17-42; Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md:64-68]. Brunner's phonological summary is fully compatible with that straightforward reading: `Dem westgerm. ū entspricht regelmäßig ae. u, so hūs Haus, tūn` [docs/references/brunner_1965_altenglische_grammatik.vision.txt:2825-2825; @SieversBrunner1965]. The row's philological caution is therefore not about deriving OE `tūn`; it is about keeping comparative proto headwords, possible paradigm background, and the live OE-facing input separate in the documentation.

That is why this replacement slice should remain more conservative than many exception-focused slices. There is no surviving DEV_NOTES argument for changing `COUNTERPART`, no evidence that the row should be reclassified out of `regular`, and no strong basis for treating `*tūnăn` as the row's real project input. The memo's formulation is the safest current reading: preserve the live regular derivation `*tūną -> tūn`, cite Kroonen and Orel only as background headword conventions, and label the existing note's `oblique *tūnăn` wording as diagnostic/project-metadata residue rather than settled row authority [Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md:58-80; @Kroonen2013; @Orel2003].

## Relevant DEV_NOTES fragments

No securely attachable **current** DEV_NOTES fragment for lexeme `tūn` survives in the live file. The single reviewed range below is kept only so later packet or index work has an explicit record of the concept-name false positive that was checked and rejected.

### DEV_NOTES:line-10939-10942

- Source heading: `Source Research`
- Source line or section hint: `lines 10939-10942`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `false_positive`; `concept_gloss_collision`; `not_row_authority`; `old_frisian_burg`
- Recommended next use: `keep_as_negative_evidence_only`
- Shared with row IDs:

This passage is **not** a `tūn` note. DEV_NOTES quotes Ringe-Taylor on Old Frisian final devoicing and includes the comparator `burch 'town' < PWGmc *burg` [Germanic/docs/DEV_NOTES.md:10939-10942]. Because the English gloss `town` appears there, the packet surfaced it as a possible hit; but lexically and historically it belongs to the `burg/burch` family, not to OE `tūn` or PGmc `*tūną` [Germanic/docs/lexeme_reports/packets/2263-town-tūn.md:78-92].

The value of preserving this fragment is negative but real. It documents that the required DEV_NOTES review was performed and that the only apparent hit is a concept-name collision, not usable row evidence. Later indexing or packet cleanup should therefore **not** cite DEV_NOTES:line-10939-10942 as support for row 2263.

## Superseded or diagnostic material

- The live TSV note `Proto: oblique *tūnăn→*tūną (n. a-stem nom.sg.; Kroonen)` should currently be treated as **diagnostic wording**, not as verified row-local authority. The checked Kroonen excerpt in the repo gives `*tūna-`, not the note's `*tūnăn`, and the memo explicitly flags that mismatch [Germanic/data/germanic-aligned-final.tsv:1292-1292; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26863-26864; Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md:21-24,31-35,74-80].
- The packet's repetition of that note is useful as provenance tracking, but it is not independent confirmation. For later work, the packet should be read as evidence that the live row derives correctly while the note text remains philologically overcompressed [Germanic/docs/lexeme_reports/packets/2263-town-tūn.md:5-10,17-42].
- No pilot file, dossier, or analysis file clearly specific to row 2263 was found in the required support-file check. That absence is part of the current documentary state and should not be silently padded out with generic town-related material from elsewhere in the repo [Germanic/docs/lexeme_reports/research_memos/2263-town-tūn.md:38-39,82-82].

## Open questions for later work

- If the TSV note is revised later, decide whether it should cite comparative headwords as `*tūna-` (Kroonen) and `*tūnan ~ *tūnaz` (Orel) rather than asserting `oblique *tūnăn` as if that wording came directly from Kroonen [@Kroonen2013; @Orel2003].
- If a final lexeme report is written, keep OE `tūn` as the attested target and state explicitly that the row's issue is note hygiene, not derivational rescue.
- For `index.tsv`, keep the standard conservative threshold: row 2263 currently has no strong attachable DEV_NOTES anchor, only a checked false positive at `DEV_NOTES:line-10939-10942`.

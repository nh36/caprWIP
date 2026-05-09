---
row_id: 1970
concept: bride
counterpart: brȳd
proto: *brūdiz
protoform: *brūdiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1970 bride / brȳd

## Current row state

- The live OE row currently reads `CONCEPT = bride`, `COUNTERPART = brȳd`, `PROTO = *brūdiz`, `PROTOFORM = *brūdiz`, and `DERIVATION_CLASS = regular`; the row note is blank, while the history field preserves duplicated Wiktionary-etymology provenance text [Germanic/data/germanic-aligned-final.tsv:151-151].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not presently using a paradigm-cell substitute, a proxy OE-facing input, or any separate repair protoform. The stored project input is simply `*brūdiz` [Germanic/data/germanic-aligned-final.tsv:151-151].
- The current published OE traces are exact matches. The compact trace gives `PROTO: *brūdiz`, `EXPECTED: brȳd`, `OUTPUTS: brȳd`, and compresses the key path to `PGmc Final Z Deletion: *brūdi`, `OE I Umlaut: *brȳdi`, `OE High Vowel Apocope: *brȳd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:571-590]. The full trace shows the same ordered result, with `OEIUmlaut: *b*r*ȳ*d*i`, `OEHighVowelApocope: *b*r*ȳ*d`, and surface `brȳd` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:4018-4027,4058-4061].
- `oe_known_problems.tsv` has no row-local entry for `1970`, `bride`, `brȳd`, or `*brūdiz`; the current ledger only lists unrelated exception/wontfix items [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still shows no row-local documentation packet or memo: `coverage_audit.md` lists `| 1970 | bride | brȳd | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:211-211]. No matching packet, research memo, dossier, or analysis file for row `1970` or the `bride / brȳd` stem was found during row-local repo inspection.

## Development-note summary

DEV_NOTES support for row `1970` is real but thin. No dedicated `bride / brȳd` section survives in `Germanic/docs/DEV_NOTES.md`, no row-specific repair narrative is preserved, and no packet or memo currently backs the row [Germanic/docs/lexeme_reports/coverage_audit.md:211-211]. The materially relevant current DEV_NOTES support is instead a shared OE i-umlaut status note from 2025-12-22, where the project explicitly recorded that `OldEnglishIUmlaut` had just been expanded to cover `*ū → *ȳ` and used this lexeme as one of the positive ordering-probe examples [Germanic/docs/DEV_NOTES.md:2565-2572].

The substance to preserve from that note is not just the end result `brȳd`, but the project claim about why the row now works. DEV_NOTES states: “expanded `OldEnglishIUmlaut` to cover `*æ → *e`, `*e → *i`, and `*ū → *ȳ`,” then says, under “What works now (ordering probe),” that “i-umlaut fires inside the PGmc→OE block before weak-tail cleanup/apocope,” giving the explicit probe sequence ``brūdiz → *b*r*ȳ*d`` [Germanic/docs/DEV_NOTES.md:2566-2568]. For row `1970`, that means the surviving development-note evidence is phenomenon-level but directly applicable: the lexeme was one of the internal confirmation cases showing that the newly broadened OE i-umlaut rule was firing early enough to produce the expected `ȳ` before later tail loss [Germanic/docs/DEV_NOTES.md:2566-2568; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:4018-4027].

That same fragment also has to be read with its limitation intact. DEV_NOTES immediately adds that “fronting/raising does not trigger in many common i/j contexts ... so the **trigger environment is still too narrow**” [Germanic/docs/DEV_NOTES.md:2568-2568]. In other words, the note is not a general declaration that OE i-umlaut problems were solved across the board; it is a narrower claim that some probe items, including `brūdiz`, were now behaving correctly in the intended location of the cascade. The row should therefore be documented as a current exact-match success inside a still-incomplete broader umlaut program, not as evidence that all related OE fronting questions were closed repo-wide [Germanic/docs/DEV_NOTES.md:2567-2568].

One additional DEV_NOTES hit is worth preserving, but only cautiously. In an unrelated discussion of compounds and syncopation, DEV_NOTES quotes Campbell on Kentish `brydelíc` among “exceptions to the syncopation of -i- in compounds... with i-nouns” [Germanic/docs/DEV_NOTES.md:6523-6527]. That is not a row-specific note on `brȳd`, but it is still an in-repo quotation that presupposes an OE `bryd-`/`brȳd` lexical family. It supports lexical plausibility and family continuity only; it does not explain the row's derivation, justify the derivation class, or add a separate row policy.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2565-2572

- Source heading: `OE i-umlaut status (2025-12-22)`
- Source line or section hint: `lines 2565-2572`
- Fragment type: `shared_rule_discussion_with_explicit_row_probe`
- Status: `current`
- Issue tags: `oe_i_umlaut`; `ū_to_ȳ`; `rule_ordering`; `probe_example`
- Recommended next use: `cite_if_explaining_why_row_now_derives_cleanly`
- Shared with row IDs: other OE rows used in the same ordering probe, including `mouse` and `foot`

This is the core surviving DEV_NOTES support for row `1970`. DEV_NOTES records the rule change explicitly: “expanded `OldEnglishIUmlaut` to cover `*æ → *e`, `*e → *i`, and `*ū → *ȳ`; added `*ȳ` to starred vowel inventories + `OldEnglishRemoveStars`” [Germanic/docs/DEV_NOTES.md:2566-2566]. It then gives the row's own probe sequence in direct form: “i-umlaut fires inside the PGmc→OE block before weak-tail cleanup/apocope (e.g., `mūsiz → *m*ȳ*s`, `brūdiz → *b*r*ȳ*d`, `fōtiz → *f*ē*t`)” [Germanic/docs/DEV_NOTES.md:2567-2567].

For this slice, the fragment should be read as an implementation-status note that directly bears on the lexeme. It preserves a clear project claim that `brūdiz` was used to verify the ordering and coverage of OE `*ū → *ȳ` umlaut, and that the expected OE-side shape was already emerging before later apocope/cleanup [Germanic/docs/DEV_NOTES.md:2566-2568]. It does **not** preserve a full philological note on noun class, attestation, or comparative source selection, and it should not be inflated into a richer row dossier than the source actually provides.

### DEV_NOTES:line-6523-6527

- Source heading: `Campbell (1959) §348 fn.2 attests giftelic`
- Source line or section hint: `lines 6523-6527`
- Fragment type: `indirect_lexeme_family_hit`
- Status: `diagnostic_only`
- Issue tags: `compound_derivative`; `brydelic`; `i_noun`; `indirect_support`
- Recommended next use: `use_only_if_lexeme_family_attestation_needs_mention`
- Shared with row IDs:

This fragment is not a derivation note for row `1970`, but it is the only other live DEV_NOTES passage that materially touches the same OE lexical family. DEV_NOTES quotes Campbell: “exceptions to the syncopation of -i- in compounds... with i-nouns, e.g. `brydelíc`, gebyrdetíd, gewyrdelic, **giftelic**, tidelíce, hlípeget, ærdelond” [Germanic/docs/DEV_NOTES.md:6523-6525]. The presence of `brydelíc` makes the hit worth preserving because it is an in-repo primary-source quotation that is at least consistent with the expected OE stem `bryd-`/`brȳd`.

The caution is essential. This fragment does not discuss `*brūdiz`, does not address OE `*ū → *ȳ`, and does not say anything row-specific about why the aligned TSV keeps `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:151-151]. Its value is therefore diagnostic and contextual only.

## Superseded or diagnostic material

- No superseded row-local DEV_NOTES proposal is currently recoverable. There is no surviving bride-specific correction narrative, no abandoned paradigm-cell retargeting, and no packet or memo history to summarize; the main documentary fact is simply that current support is shared-rule support rather than row-dedicated support [Germanic/docs/lexeme_reports/coverage_audit.md:211-211].
- The `brydelíc` quotation should be kept, if at all, as diagnostic/contextual material only. It shows that the wider `bryd-` lexical family appears elsewhere in the notes, but it is not evidence for the derivational chain actually used in row `1970` [Germanic/docs/DEV_NOTES.md:6523-6527].
- The i-umlaut status note itself also needs disciplined reading. It is strong evidence that `brūdiz` was a successful internal ordering probe, but DEV_NOTES simultaneously says the broader i/j-trigger system remained incomplete and “still too narrow” in many other contexts [Germanic/docs/DEV_NOTES.md:2567-2568]. Later writers should therefore cite the fragment as row-relevant implementation history, not as a blanket closure statement about OE umlaut in the whole grammar.

## Open questions for later work

- If a later packet or memo is created, it should add explicit philological support for the noun itself, because the surviving DEV_NOTES material is implementation-oriented and thin on lexical documentation.
- If `dev_notes_slices/index.tsv` is reconsidered later, the safest current judgment is probably **no-index**. This slice is useful as a replacement working note, but its DEV_NOTES anchors are mostly one shared rule-status fragment plus one indirect lexical-family quotation, not a genuine row-local dossier.
- If future documentation wants a compact one-line derivation explanation near the top, the current trace already supports it: `*brūdiz > *brūdi > *brȳdi > brȳd` via final-`z` loss, OE i-umlaut, and high-vowel apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:578-590; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:3980-3980,4018-4027].

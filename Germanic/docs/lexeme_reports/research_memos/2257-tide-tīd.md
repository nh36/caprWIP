# Research memo — 2257 tide / tīd

## Starting point

- **ID:** 2257
- **CONCEPT:** tide
- **COUNTERPART:** `tīd`
- **PROTO:** `*tī́diz`
- **PROTOFORM:** `*tḯdiz`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Kroonen *tīdiz f. i-stem 'time, hour' → OE tīd f.; tīdan is the verb 'to happen'`

This row is already close to stable. The live TSV distinguishes the OE noun `tīd` from the separate verb `tīdan`, and the row also preserves the usual project split between the cognate-set `PROTO` spelling and the OE-facing `PROTOFORM` used by the derivation.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*tḯdiz -> tīd`; and the packet's cited `DEV_NOTES.md` verification material showing `tḯdiz -> tīd` as a checked stressed-`*ḯ` case.
- **Useful background:** the packet's Kroonen bibliography key; the migration-batch `DEV_NOTES.md` references showing why this row participates in the `*ḯ` cleanup; and the packet's `old_english_wiktionary.tsv` hit as evidence of a known extraction pitfall.
- **Stale or superseded:** there is no strong stale lexical claim inside the packet itself, but the repo's generated debug snapshot only preserves the original TSV note and does not count as an authoritative prior lexeme report.
- **Irrelevant or misleading:** `_No manifest entry_` and `_None_` under `oe_known_problems.tsv` are coverage metadata, not philological evidence; the `old_english_wiktionary.tsv` hit is misleading if treated as lemma evidence, because it points to the verb `tīdan`, not the noun represented by row 2257.

So the packet is useful but thin: it gives the correct derivational center of gravity, but the memo still has to verify the noun/verb distinction and the noun's attested OE paradigm from other repo sources.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 42017-42041.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/bammesberger_1990_morphologie.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.

Main extra findings:

- Kroonen's local entry distinguishes the noun `*tīdi-` 'time' from OE `tidan` 'to betide, happen', so the TSV note's noun/verb warning is well grounded [@Kroonen2013].
- Orel likewise gives a feminine nominal etymon `*tīđiz` and treats the related verb separately, again supporting noun/verb separation rather than row revision [@Orel2003].
- Bammesberger's nominal-morphology file also supports a nominal `*tī-di-` preform for OE `tīd`, which aligns with the current noun analysis [@Bammesberger1990].
- Bright explicitly lists attested OE paradigm cells `tīd` (nom.sg.), `tīde` (dat.sg./instr.sg.), and `tīda` (nom.pl.), so the row target is an attested noun, not a reconstructed convenience form [@BrightCassidyRingler1971].
- Clark Hall glosses `tid` as 'time, period, season, while ... hour', which matches the noun row and not the verb [@ClarkHall1960].
- `coverage_audit.md` shows that row 2257 requires a lexeme report because of its non-empty `NOTE`, but no pilot/full report currently exists.
- The generated `with_lexeme_reports` debug snapshot contains only the carried-over TSV note for this row; it is background history, not final authority.

No full dossier or analysis file was named in the packet or TSV note, so there was no lexeme-specific dossier to audit beyond these repo sources.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction, but here the three levels are compatible rather than in conflict.

1. **Cognate-set proto / etymological headword:** `PROTO = *tī́diz`, i.e. the PGmc feminine i-stem 'time'. Kroonen's `*tīdi-` and Orel's `*tīđiz` are compatible comparative notations for the same noun family [@Kroonen2013; @Orel2003].
2. **Project input form used for derivation:** `PROTOFORM = *tḯdiz`. This is the OE-facing derivational input used in the current FST, with the stressed `*ḯ` notation that the project verified in the migration/verification notes.
3. **OE target form represented by the row:** `tīd`, the noun 'time, season, hour'. It is not the verb `tīdan`, and it is not an inflected oblique form.

Fulk's comparative discussion of `tīd` under a PGmc form written `*tī-ðá-` is useful etymological background, but it does not by itself require changing the live row. For project purposes, the current Kroonen-aligned noun analysis and the derivational input `*tḯdiz` are coherent and already produce the correct OE outcome [@Fulk2018].

## Old English philology

`tīd` is an attested OE noun. Bright gives explicit paradigm evidence: nominative singular `tīd`, dative/instrumental singular `tīde`, and nominative plural `tīda` [@BrightCassidyRingler1971]. Clark Hall likewise treats `tid` as a noun meaning 'time, period, season, while ... hour' [@ClarkHall1960].

Three philological distinctions matter here:

- **Attested vs. reconstructed:** `tīd` is attested; this row is not using a reconstructed OE noun.
- **Citation form vs. inflected form:** the row target `tīd` is the citation-form singular; `tīde` and `tīda` are paradigm evidence, not rival headwords.
- **Dictionary/extraction noise:** `old_english_wiktionary.tsv` gives English `tide -> tīdan` via a derivational template, but that is exactly the wrong lexeme for this row. It is useful as a warning about pipeline noise, not as evidence against `tīd`.

I found no repo-local support for a narrower dialect or manuscript claim that would need to be built into the memo or later final report.

## Project problem and solution

The project problem here is lexical disambiguation, not failed sound change. The derivation itself is already regular and verified: `*tḯdiz -> tīd`.

What needed protection was the lexical identity of the OE target. English `tide` can attract misleading lexical-table matches to the verb `tīdan`, but the row is plainly intended to represent the noun meaning 'time, season, hour'. The current project solution is therefore the right one:

- keep the noun `COUNTERPART = tīd`;
- keep the noun-facing `PROTOFORM = *tḯdiz`;
- keep `DERIVATION_CLASS = regular`;
- preserve the TSV note because it blocks confusion with the separate verb `tīdan`.

## Paradigm probe

No paradigm probe is required.

This is not a hidden-cell or analogy problem. The row's issue is lexical disambiguation, and repo-local attestation already supplies the relevant noun cells (`tīd`, `tīde`, `tīda`) [@BrightCassidyRingler1971]. If a compact illustrative probe were ever wanted anyway, the only sensible cells would be citation-form nom.sg., a singular oblique cell, and a plural cell; but no such probe is needed to recommend the final report.

## Recommended final report

Recommend a short final report saying that row 2257 is a regular noun case: PGmc feminine i-stem `*tīdiz/*tīdi-` yields OE `tīd` regularly; the note is needed only to distinguish this attested noun from the separate weak verb `tīdan` and from misleading lexical-table extraction noise. Citations should come from Kroonen/Orel for the etymology and Bright/Clark Hall for the OE noun evidence.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. The current cognate-set proto is consistent with the repo's noun analysis.
- **TSV `PROTOFORM`:** no change recommended. Keep `*tḯdiz`.
- **TSV `COUNTERPART`:** no change recommended. Keep `tīd`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is correct.
- **TSV `NOTE`:** no change recommended. The current note already states the key noun/verb distinction succinctly.
- **`oe_known_problems.tsv`:** no change recommended. This row is not an unresolved exception ledger item.
- **`DEV_NOTES` text:** no change recommended. The current migration and verification notes are adequate background and not misleading.
- **Dossier text:** no change recommended. I found no dedicated tide-specific dossier, and no dossier cleanup is needed.

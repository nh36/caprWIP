---
row_id: 2218
concept: stilt
counterpart: "*stilte"
proto: "*stéltjōn"
protoform: "*stéltjōn"
derivation_class:
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2218 stilt / *stilte

## Current row state

- The live OE row reads `CONCEPT = stilt`, `COUNTERPART = *stilte`, `PROTO = *stéltjōn`, `PROTOFORM = *stéltjōn`, with `DERIVATION_CLASS` left blank. The row note is explicit that the OE target is not attested: `Unattested OE; reconstructed *stilte.` [Germanic/data/germanic-aligned-final.tsv:2218-2218].
- The row's source strings are only duplicated Wiktionary inheritance provenance, not a row-specific project argument: `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:2218-2218].
- The same live cognate set still contains German `Stelze`, English `stilt`, and Dutch `stelt`, all aligned under the same comparative proto label `*stéltjōn` in the concept-level columns [Germanic/data/germanic-aligned-final.tsv:447-449].
- Repo OE source infrastructure remains explicitly non-attested here. `old_english_wiktionary.tsv` gives `OE_FORM = -` with detail `template:inh (unattested; reconstructed *stilte)` [Germanic/data/old_english_wiktionary.tsv:278-278].
- `oe_known_problems.tsv` has no entry for `*stéltjōn`, `*steltjōn`, `*stilte`, or row `2218`, so the row is not currently managed as an open OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].

## Detailed development-note summary

No row-specific DEV_NOTES dossier currently survives for this item. Searches for `stilt`, `stilte`, `*stéltjōn`, and `*steltjōn` in `Germanic/docs/DEV_NOTES.md` did not locate a lexeme-specific paragraph, source audit, or implementation note that can be cleanly attached to row 2218. This slice therefore has to function as a replacement working note built from the live TSV state plus minimal comparator/source audit, not as a tidy extraction from an existing DEV_NOTES section.

The first thing to keep explicit is the category split. In the live row, `PROTO` and `PROTOFORM` currently coincide as `*stéltjōn`, while the OE-facing `COUNTERPART` is reconstructed `*stilte` and is overtly marked unattested in the row note [Germanic/data/germanic-aligned-final.tsv:2218-2218]. That means the file should not talk as if `*stilte` were an attested dictionary lemma. It is the row's OE target reconstruction, whereas `*stéltjōn` is the comparative/input label. Nothing in surviving DEV_NOTES argues for a different OE proxy input, paradigm-cell substitution, or analogical rescue; the documentary problem is absence of row-specific note support, not evidence of a competing derivational policy.

External lexical support is thin but coherent. Orel's entry gives `*steltjōn *staltjōn sb.f.` with comparators including Norwegian dialect `stilta`, Middle English `stilte`, Middle Low German `stelte`, and Old High German `stelza`, which is enough to confirm that the project's row belongs to a feminine `-jōn` lexical family [@Orel2003, p. 374; docs/references/orel_handbook_germanic_etymology.vision.txt:41618-41620,63857-63857]. Kluge-Seebold's `Stelze` entry points the same way: `mhd. stelze, ahd. stelza, mndd. stelte, mndl. stelte`, with the explicit note that Middle English `stilte` “wohl auf eine j-Bildung zurückgeht” [@KlugeSeebold2011; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:89958-89960]. Those comparators do not by themselves prove an attested OE lemma, but they do support the live row's choice to keep the cognate set under a `*steltjōn/*stéltjōn`-type reconstruction and to treat OE `*stilte` as a plausible unattested continuation rather than an arbitrary invention.

The repo's own OE evidence remains explicitly negative rather than positive. `old_english_wiktionary.tsv` does not preserve an attested OE form here; it preserves only the inheritance template with the gloss `unattested; reconstructed *stilte` [Germanic/data/old_english_wiktionary.tsv:278-278]. That is fully consistent with the live row note, but it also means this row currently lacks the kind of OE-specific philological support that would justify treating the target as anything stronger than a working reconstruction. The live note is therefore best read conservatively: the project is not claiming that OE `*stilte` is textually attested, only that it is the row's current reconstructed OE counterpart.

One notation caution should also be preserved. The live row writes `*stéltjōn`, whereas Orel and the stale sandbox JSON still show unaccented `*steltjōn` [Germanic/data/germanic-aligned-final.tsv:2218-2218; docs/references/orel_handbook_germanic_etymology.vision.txt:41618-41620; Germanic/tmp/old_english_sandbox_results_current.json:2711-2715]. In the absence of a row-specific DEV_NOTES discussion, this should be treated conservatively as house-notation drift, not as evidence for two different etymological analyses. The important distinction is not acute versus unaccented spelling, but comparative `*stéltjōn/*steltjōn` versus unattested OE target `*stilte`.

Taken together, the row is documentable but not well supported by DEV_NOTES. The comparative family is real and source-backed, the OE target is overtly reconstructed, and there is no sign that the row is currently failing inside `oe_known_problems.tsv` [Germanic/data/oe_known_problems.tsv:1-8]. But the surviving project documentation does not yet provide a row-specific note explaining the OE reconstruction in the same detailed way available for stronger slices. That is exactly the kind of situation that should remain no-index unless later memo work creates a clean attachable argument.

## Relevant DEV_NOTES fragments

No attachable row-specific DEV_NOTES fragment was found for `stilt` / `*stilte`. The only line in `DEV_NOTES.md` likely to mislead a later string search is a false friend that mentions **line 2218** as a grammar-file line number, not as lexical row 2218:

### DEV_NOTES:line-39471-39479

- Source heading: `u-lowering blocking discussion`
- Source line or section hint: `lines 39471-39479`
- Fragment type: `diagnostic_only_false_friend`
- Status: `diagnostic_only`
- Issue tags: `false_friend_row_number`; `grammar_line_reference`; `not_lexeme_specific`
- Recommended next use: `exclude_from_oe_indexing`
- Shared with row IDs:

This fragment discusses Brunner-style blocking before `*ng` and says that the behavior would be parallel to `our existing OEMedUnstressedILowering (line 2218: *e → *i before *ng for cyning, sċilling, etc.)` [Germanic/docs/DEV_NOTES.md:39471-39479]. The phrase `line 2218` there refers to a line in `germanic.txt`, not to OE lexical row 2218, and the lexemes under discussion are `cyning`/`sċilling`-type forms, not `stilt`. It should therefore be preserved only as a search trap to avoid accidental index attachment.

## Superseded or diagnostic material

- `Germanic/tmp/old_english_sandbox_results_current.json` is stale/diagnostic for this row. It still carries unaccented `proto: "*steltjōn"`, reconstructed `counterpart: "*stilte"`, and `outputs: []`, so it is useful only as evidence that older sandbox infrastructure did not yet give a live OE output for the item [Germanic/tmp/old_english_sandbox_results_current.json:2711-2715].
- The duplicated Wiktionary source strings in the live TSV row are provenance only. They do not amount to a project-authored defense of the OE reconstruction and should not be mistaken for a DEV_NOTES-level argument [Germanic/data/germanic-aligned-final.tsv:2218-2218].
- The row currently has no packet or research memo stem to reuse, which is why this slice uses the canonical row-based filename rather than inheriting an existing report stem.

## Open questions for later work

- If row 2218 is ever to become indexable, a dedicated memo or packet should state explicitly why `*stéltjōn` is the right OE-facing comparative input and why unattested `*stilte` is the preferred OE reconstruction rather than some other jō-stem continuation.
- If later report prose cites handbook evidence, keep the distinction explicit between comparative family support (`*steltjōn/*staltjōn`, ME `stilte`, MLG `stelte`, OHG `stelza`) and OE attestation status; the current evidence bundle supports the family, not an attested OE headword [@Orel2003, p. 374; @KlugeSeebold2011].
- If the project later standardizes accenting/diacritics for this family, add a note explaining whether live `*stéltjōn` is just normalized house spelling for handbook `*steltjōn`, so later readers do not overinterpret the notation difference.

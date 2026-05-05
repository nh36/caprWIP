# Research memo — 2252 thousand / þūsend

## Starting point

- **ID:** 2252
- **CONCEPT:** thousand
- **COUNTERPART:** þūsend
- **PROTO:** *θūs-undī
- **PROTOFORM:** *θūs-èndi
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Kroonen *θūsundī- f. 'thousand' → OE þūsend; medial -e- is analogical (Vorbild: ærende < *arundiiu); preserved ū (not ȳ) proves -ī lost before i-umlaut (double umlaut would give *þȳsend); OS/OHG retain -u-

The row already encodes the crucial three-way distinction, but it needs to be stated explicitly. TSV `PROTO` is the cognate-set / etymological PGmc headword; TSV `PROTOFORM` is the **project input transponent** currently used to make the OE cascade land on the right form; the OE target is the citation-form numeral/noun `þūsend`, not an inflected paradigm cell.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the compact derivation trace showing that the current input `*θūs-èndi` now yields `þūsend`; `DEV_NOTES.md` §16.6.4 / §17.11.0-1 showing that the current hyphenated grave-accent OE-side compound inputs include `*θūs-èndi`; and the lexical-table confirmation in `old_english_wiktionary.tsv` that the OE lexeme is `þūsend`.

**Useful background:** the packet's April 2026 `DEV_NOTES` dossier on the earlier `*θūs-undī -> þūsynde` mismatch; the excerpts from Fulk, Campbell, Luick, Kroonen, and the later Viredaz source note. These are good research leads, but they are not all equally current as project-state evidence.

**Stale or superseded:** the packet preserves an earlier debugging stage where the row still mismatched and `*θūsendi` was floated as an ad hoc fix. That is no longer the live row state: the repo has already moved to the current transponent `*θūs-èndi`, and the row now matches. The packet's mismatch-era framing is therefore historical background, not the present project decision.

**Irrelevant or misleading:** the packet includes many analysis/dossier hits triggered only by generic note keywords such as `i-umlaut`. Files like `mismatch_dossier_mizdo.md` and its supplement are about other lexemes and even carry their own correction banners; they should not be treated as evidence for `þūsend` beyond showing that the packet's broad keyword harvesting can surface unrelated material.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at §14.7 (17936-18404), plus §16.6.4 and §17.11.0-1 for the later transponent migration to `*θūs-èndi`.
- `Germanic/data/old_english_wiktionary.tsv` — citation form `þūsend`.
- `Germanic/data/oe_known_problems.tsv` — no live exception entry for this row.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — row 2252 correctly remains in lexeme-report coverage because it has both a non-empty `NOTE` and `DERIVATION_CLASS=early_analogy`.
- `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt` — Fulk treats the word as PGmc `*þūsund-`, a compound with varied later inflectional remodeling across Germanic.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — Kroonen gives `*þūsundī-` with OE `þūsend`.
- `docs/references/campbell_old_english_grammar.txt` — §689 gives OE `þūsend` as a neuter noun; §203 notes `þyslic` beside `þuslic`, i.e. mutation of medial `-u-` is recorded in the derivative, not in the simplex.
- `docs/references/luick_historische_grammatik.txt` — §198 material on `ærende`, and §492 grouping `þūsend` with `ærende` as a reshaped form.
- `docs/references/2025_Germanic_Slavic_and_Baltic_thousand.txt` — Viredaz's alternative that OE `e` here may simply spell unstressed schwa and need not prove analogical `-end-`.

No dedicated row-specific dossier or pilot/full lexeme report for `thousand / þūsend` was found. The packet's named analysis/dossier files are broad keyword collisions rather than a true row dossier.

## Reconstruction and early-stage forms

This row requires a strict separation of levels:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*θūs-undī`, matching the Kroonen-style PGmc feminine/jō-stem reconstruction cited in the row note.
2. **Project input form:** TSV `PROTOFORM` `*θūs-èndi`, which is **not** the same claim as the etymological reconstruction. It is a project-side OE-oriented transponent: short final `-i` so apocope can apply, grave-accented second member per the later compound/Nebenton notation, and medial `e` already built in.
3. **OE target form:** `þūsend`, the OE citation form.

Fulk's handbook evidence is useful here because it reminds us that the comparative headword can also be framed as a stem-level `*þūsund-`, with daughter languages reshaping the inflection differently. That does not force a TSV change, but it does mean the memo and any later report should avoid pretending that project input `*θūs-èndi` is itself the comparative reconstruction. It is a modelling input chosen to represent the OE-side outcome after early restructuring.

## Old English philology

Repo-local philology supports the following points:

- `þūsend` is the OE lexical form.
- Campbell §689 treats it as a **neuter noun** with ordinary OE case forms (`g.s. -es`, `d.s. -e`, plural forms in `-u/-o/-a`, etc.), and it can also function as an uninflected numeral/adjective.
- The row target is therefore a **citation form**, not a selected oblique workaround.

The main philological issue is the medial vowel. Cross-Germanically, Gothic, Old Norse, Old Saxon, and Old High German keep `u`; OE alone shows `e`. Campbell's derivative `þyslic` is important negative evidence: medial `u` can show mutation in a derivative with a front-vocalic suffix, but the simplex `þūsend` itself does not show the expected full regular i-umlaut pattern. The preserved root `ū` remains a strong argument against a straightforward path where final `-ī` survives long enough to trigger ordinary umlaut throughout, since that would point toward a form like `*þȳsend`, not attested `þūsend`.

What is still uncertain is **why** OE has `e`. Luick supports the classic `ærende`-type analogical Vorbild; Viredaz instead argues that OE `e` in this weak position could simply spell schwa and reflect any short PGmc vowel. So the row's current project solution is more secure than the row note's current level of explanatory certainty.

## Project problem and solution

The project problem was originally concrete: with older input `*θūs-undī`, the FST produced `þūsynde`, not `þūsend`. The repo then explored whether the issue was final-vowel length, compound parsing, analogical `-end-` reshaping, or some other vowel development. The live project solution is now clear: preserve the etymological PGmc headword in TSV `PROTO`, but use the OE-oriented transponent `*θūs-èndi` in TSV `PROTOFORM`, which derives the correct target.

That solution should be described as a **project modelling compromise**, not as a settled claim that the actual pre-OE form was literally `*þūsèndi`. The present row is best read as:

- etymological source tradition: `*þūsundī-` / stem `*þūsund-`;
- OE historical result: `þūsend`;
- current project input: `*θūs-èndi`, a transponent that encodes the already-resolved OE-side vowel and apocope conditions.

The project note is therefore directionally right in rejecting a simple regular i-umlaut derivation, but it is too categorical in treating `ærende`-type analogy as the only viable explanation for medial `e`.

## Paradigm probe

A paradigm probe is **not required** for the main decision. This row is not using a selected paradigm cell to rescue the output; it already targets the OE citation form, and the hard problem is the pre-OE stem history / project transponent, not uncertainty about which inflectional cell should stand for the lexeme.

If the team later wants a small illustrative probe for the final report, it would be diagnostic rather than necessary. The most relevant comparison would be the old mismatch input versus the current transponent, not a noun paradigm table.

## Recommended final report

Recommend a concise final lexeme report. It should distinguish clearly between PGmc headword reconstruction (`*þūsundī-` / stem `*þūsund-`), the project input `*θūs-èndi`, and the OE target `þūsend`; state that the current project row models an early reshaped/pre-resolved OE-side form; note that preserved `ū` excludes a simple surviving-`-ī` i-umlaut path; and present the medial `e` explanation cautiously, with Luick's `ærende` analogy and Viredaz's schwa-spelling analysis both acknowledged.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended. `*θūs-èndi` is the current working project transponent and is now integrated into the later compound/Nebenton notation.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended for now; `early_analogy` still fits the current in-project modelling better than `regular`, even if the exact historical explanation of medial `e` should be softened.
- **TSV `NOTE`:** **change recommended.** The note should distinguish more carefully between (a) what is well supported, namely that the OE form cannot reflect a simple regular surviving-`-ī` umlaut pathway, and (b) what remains interpretive, namely whether medial `e` is specifically analogical on the model of `ærende` or can be treated as unstressed schwa spelling as in Viredaz/Brunner.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** **change recommended in `DEV_NOTES.md`.** §14.7 should be marked more explicitly as mismatch-era research history, and its later Viredaz update should be integrated into the main conclusion instead of leaving the analogical account as the apparent default conclusion. No row-specific dossier text was identified that needs separate editing.

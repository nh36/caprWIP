# Research memo — 1962 bow / bēag

## Starting point
- ID `1962`; CONCEPT `bow`; COUNTERPART `bēag`.
- TSV `PROTO` = `*béuganą`; TSV `PROTOFORM` = `*báug`; TSV `DERIVATION_CLASS` = `late_analogy`.
- TSV note: the row was retargeted from 3pl pret. `*búgun → bugon` to the 1/3 sg. pret. `*báug → bēag`, citing DEV_NOTES §17.51.A1.4 and `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`; the note also states that OE `būgan` has analogical `ū` back-formed from the singular preterite stem.

## Packet evidence assessment
- **Authoritative/current:** the current TSV row; the packet's compact derivation trace `*báug → bēag`; DEV_NOTES §17.51.A1.4; and `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`, which is the full rationale for the retargeting.
- **Useful background:** `Germanic/docs/dossiers/bugun-scufun-attestation.md`, because it shows why the old 3pl solution failed as a lexeme-specific OE target even though older general work on `-un` endings had made it look defensible.
- **Stale/superseded:** the earlier April-2026 state with row 1962 as `*búgun → bugon`. The packet preserves some of that project history; it is diagnostic background only, not current guidance.
- **Irrelevant or misleading:** the packet's lexical-table hit `bow = boga` from `old_english_wiktionary.tsv` is a different lexeme (the noun `boga`), not the verbal preterite `bēag` represented by this row.

## Additional repo research
Checked beyond the packet: `Germanic/docs/DEV_NOTES.md` (especially §17.51.A1.4 at lines 43938-43998, plus older superseded notes around 14508), `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`, `Germanic/docs/dossiers/bugun-scufun-attestation.md`, `Germanic/docs/analysis/final_vowel_missing_analysis.md`, `Germanic/data/germanic-aligned-final.tsv`, and `Germanic/data/old_english_wiktionary.tsv`. I also checked `Germanic/data/oe_known_problems.tsv`; this row no longer has an active entry there after the retargeting.

## Reconstruction and early-stage forms
`*béuganą` is the etymological headword/cognate-set anchor and belongs in TSV `PROTO`. The row-specific derivational input is instead `*báug`, the PGmc 1/3 sg. preterite cell. That distinction matters: the OE infinitive/citation form `būgan` is not the clean sound-law output of `*béuganą`, because the present stem shows analogical `ū`; the singular preterite stem is the historically earlier, cleaner input and gives OE `bēag` by the regular class-II strong-verb singular-preterite development `*au > ēa`.

## Old English philology
`bēag` here is an attested verbal form, not a reconstructed stand-in and not the noun `bēag` 'ring'. The dossier treats it as universally attested for the verb, citing poetic and prose witnesses including *Beowulf*, *Genesis B*, and Ælfric. The dictionary citation form is still `būgan`, but that headword is an analogical present-system form; this row intentionally targets a different paradigm cell because that cell is both attested and Lautgesetzlich.

## Project problem and solution
The project first moved away from infinitive `*beuganą / būgan` because the OE infinitive is analogical. It then used 3pl pret. `*búgun / bugon`, but the later stem-`u` harmony work showed that the regular early output there is `bugun`, while the attested `bugon` forms are late analogical overlay and there is no secure lexeme-specific attestation of `bugun`. The retargeting to `*báug / bēag` solves both issues: the row no longer depends on a late leveled plural ending, and the chosen OE form is both corpus-attested and derivable by regular sound change.

## Paradigm probe
A new probe is optional rather than required, because `bugan-scufan-paradigm-cell-review.md` already performs the relevant cell-by-cell audit. If one is wanted for the eventual report, it should compare at least infinitive `*beuganą → bēogan`, 1/3 sg. pret. `*báug → bēag`, pret. pl. `*búgun → bugun`, and past participle `*búganaz → bogen`, explicitly marking which outputs are regular, which are attested, and which are analogically overlaid.

## Recommended final report
Recommend a concise final report that explicitly distinguishes three layers: cognate-set headword `*béuganą`, analogical OE citation form `būgan`, and the row-specific regular preterite `*báug → bēag`; it should also note that the former `*búgun → bugon` solution is superseded project history.

## Data-change recommendations
- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** no required change.
- **`oe_known_problems.tsv`:** no change; the old problem entry was correctly removed when the row was retargeted.
- **DEV_NOTES/dossier text:** no required change; §17.51.A1.4 already records the supersession clearly.

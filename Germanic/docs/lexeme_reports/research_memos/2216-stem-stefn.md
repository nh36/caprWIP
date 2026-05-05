# Research memo — 2216 stem / stefn

## Starting point

- **ID:** 2216
- **CONCEPT:** stem
- **COUNTERPART:** stefn
- **PROTO:** *stámnaz
- **PROTOFORM:** *stébnō
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Pre-OE transponent *stebn- (citation form *stebnō per R/T p.330) > OE stefn. The form stemn is a later WS variant (fn > mn assimilation, Bülbring §445: “erst in Alfreds Zeit”). The deeper PGmc reconstruction remains disputed (see DEV_NOTES); this entry uses the local pre-OE transponent and defers cross-branch analysis.

The live row is internally split. The cognate-set side (`CONCEPT = stem`, `PROTO = *stámnaz`, sibling rows Dutch `stam`, English `stem`, German `Stamm`) points to the “stem/trunk/prow” set, but the derivational side (`PROTOFORM = *stébnō`, note text, packet dossier) points to the separate OE lexeme `stefn/stemn` “voice”. That split is the main issue.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the compact trace proving that the current OE pipeline derives `*stébnō -> stefn`; `coverage_audit.md`, which correctly shows that row 2216 requires a report because it has a note and non-regular derivation class.
- **Useful background:** `DEV_NOTES.md` §§3254ff and `analysis/notable_findings.md` §5 as a real dossier for OE `stefn/stemn` “voice”; `old_english_wiktionary.tsv`, which at least shows that the repo has independently associated concept `stem` with OE `stemn`; and the older `DEV_NOTES.md` A-restoration section, which preserves project history from the period when the row still used `*stamnăz -> stemn`.
- **Stale or superseded for this row as currently glossed:** the packet’s implication that the voice dossier settles row 2216 as a cognate-set item. It settles only the homographic voice lexeme. It does not show that `*stébnō` belongs in the `stem` set.
- **Irrelevant or misleading:** treating packet “high-confidence” hits about `stefn/stemn` “voice” as if they overrode the row’s own cognate-set proto `*stámnaz`; and reading the successful `*stébnō -> stefn` derivation as proof that the lexeme identification is correct. The packet is strong on phonological fit for one OE form, weak on whether that OE form belongs to the right lexical set.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` §§3155–3167 (`*stamnăz -> stemn` in the old A-restoration mismatch bucket) and §§3254–3415 (the full voice dossier).
- `Germanic/docs/analysis/notable_findings.md` §5.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and the publish missing-reports snapshot.
- `Germanic/data/old_english_wiktionary.tsv` (`stem -> stemn`).
- `Germanic/data/oe_known_problems.tsv` (no row-2216 entry).
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bulbring_altenglisches_elementarbuch.txt`.
- `docs/references/luick_historische_grammatik.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.

This extra pass changes the picture materially. Repo-local reference material supports **two different OE lexeme clusters**:

1. **Voice:** `stebn/stefn/stemn`, with the well-developed dossier behind current `PROTOFORM = *stébnō`.
2. **Stem / trunk / prow:** `stefn` III / `stefna`, `stemn`, and `stofn`, linked in different sources to `Ger. Stamm`, OS `stamn`, ON `stafn`, or related forms.

So the row’s real problem is not merely an uncertain protoform; it is homograph conflation plus cross-source lexical drift.

No pilot report already exists for this lexeme.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / headword:** TSV `PROTO = *stámnaz`. Whatever its exact refinement later becomes (`*stamnaz/*stamniz` is allowed in Orel), it belongs to the `stem` cognate set with Dutch `stam`, English `stem`, German `Stamm`.
2. **Project input form used for derivation:** the current TSV `PROTOFORM = *stébnō` is not a mere stage of that stem set. It is the citation form used in the repo’s separate dossier for OE `stefn/stemn` “voice”.
3. **OE target form represented by the row:** the current `COUNTERPART = stefn` is ambiguous on its face because OE dictionaries also have `stefn` entries outside the voice sense. But the row’s current note justifies it only through the voice dossier, not through a stem/trunk/prow dossier.

The strongest present conclusion is therefore negative but important: `PROTO = *stámnaz` and `PROTOFORM = *stébnō` should not coexist as if they described one derivational chain. They encode different lexical analyses.

For the stem-side lexeme, repo sources point in more than one direction: Orel gives `*stamnaz/*stamniz` with OE `stefna` “prow, stern”; Clark Hall has `stefn` III “stem, trunk ... prow or stern of a vessel”; Luick and Brunner note `stemn Stamm` beside the better-known `stefn/stemn` voice material; Clark Hall also has separate `stofn` “trunk, stem, branch, shoot”. That is enough to show that the current voice transponent is wrong for the set, but not enough to choose a final OE row target without a dedicated stem-side dossier.

## Old English philology

Philologically, the packet collapses at least two different OE entries.

- **Attested/dictionary-backed voice lexeme:** `stebn`, `stefn`, `stemn` “voice, sound”; earliest `stebn`, standard early `stefn`, late WS `stemn`. This is the lexeme treated by R/T, Bülbring, Luick, Fulk, Orel, and the current repo dossier.
- **Stem/trunk/prow lexeme(s):** repo dictionaries and grammars also show OE material for the semantic field “stem/trunk/prow”: `stefn` III, `stefna`, `stemn Stamm`, and `stofn`. These are not automatically identical with the voice lexeme just because some forms overlap graphically.
- **Citation-form problem:** for the stem set, the likely dictionary headword may be `stefna` or `stofn` in some sources, while `stemn` appears as a later or variant form in others. That is different from the voice dossier’s citation-form logic built around `*stébnō -> stefn`.
- **Manuscript/dialect caution:** the Alfredian `fn > mn` chronology is solid for the voice dossier, but it should not be imported wholesale as the row’s final stem-side solution without stem-specific evidence.

So the correct philological warning is: the current packet is rich evidence for one OE homograph, not for the lexeme identity of row 2216 as a `stem` entry.

## Project problem and solution

The project problem is that a successful OE-surface repair for `stefn/stemn` “voice” appears to have been used to patch a different cognate set whose concept and cross-language proto still point to `stem`.

That gave the row a derivationally neat OE output, but at the cost of lexical coherence:

- cross-language set: `stem / stam / Stamm` with `PROTO = *stámnaz`;
- OE derivation actually being run: `*stébnō -> stefn` from the voice dossier.

The solution should be to restore lexical coherence, not to polish the current mismatch explanation. Concretely:

1. keep the row tied to the `stem` cognate set rather than the voice dossier;
2. reopen the OE lexeme choice from stem-side evidence (`stefn` III / `stefna` / `stemn` / `stofn`);
3. replace the current note, which is about the wrong lexeme;
4. treat the present `*stébnō -> stefn` analysis as background on a homograph, not as the authority for row 2216.

## Paradigm probe

A paradigm probe is **not required at this stage**. The blocking issue is not a missing paradigm-cell comparison; it is lexeme identification and homograph disambiguation.

If a later stem-side solution ends up depending on a particular inflectional cell rather than a straightforward citation form, then a probe could be useful. In that later scenario the cells to probe would be the chosen stem lexeme’s **nom.sg., gen.sg., dat.sg., and at least one plural/oblique control form**. But that is downstream of the present correction.

## Recommended final report

Do **not** draft the final report from the current packet as if it were already a settled stem entry. The eventual final report should first state that the old packet evidence mostly belongs to homographic OE `stefn/stemn` “voice”, then explain which OE stem/trunk/prow lexeme the row has actually been retargeted to and why.

## Data-change recommendations

- **TSV `PROTO`:** **no immediate change recommended.** `*stámnaz` is at least in the right cognate family for concept `stem`, unlike the current `PROTOFORM`. It may later need refinement against sources that allow `*stamniz`, but it is not the main problem.
- **TSV `PROTOFORM`:** **change recommended.** `*stébnō` is the voice-word transponent and should not remain as the derivational input for the `stem` row.
- **TSV `COUNTERPART`:** **change recommended.** Even if plain `stefn` ultimately survives, it needs to be re-justified from the stem/trunk/prow lexeme, not inherited from the voice dossier. A stem-side target such as `stefn` III, `stemn`, `stefna`, or `stofn` must be chosen explicitly.
- **TSV `DERIVATION_CLASS`:** **change recommended after retargeting.** The current `early_analogy` label belongs to the present voice-based workaround; once the row is put back on the correct lexeme, the class should be reconsidered from scratch.
- **TSV `NOTE`:** **change recommended.** The current note is about OE `stefn/stemn` “voice” and should be replaced with a note about the actual stem-side lexeme chosen for row 2216.
- **`oe_known_problems.tsv`:** **change recommended if the TSV is not corrected immediately.** Add a temporary row-level warning that 2216 currently conflates the `stem` cognate set with the separate OE `stefn/stemn` voice dossier.
- **`DEV_NOTES` / dossier text:** **change recommended.** The existing stefn/stemn dossier should be marked explicitly as a **voice** dossier, not as authority for row 2216 `stem`; and the project needs either a short DEV_NOTES clarification or a dedicated stem-side dossier before a final lexeme report is written.

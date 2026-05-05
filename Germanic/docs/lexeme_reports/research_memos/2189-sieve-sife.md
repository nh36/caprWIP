# Research memo — 2189 sieve / sife

## Starting point

- **ID:** 2189
- **CONCEPT:** sieve
- **COUNTERPART:** sife
- **PROTO:** `*síbaz`
- **PROTOFORM:** `*síbi`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** `Kroonen 2013:429 gives only *sebjō- (ja-stem fem. 'kinship' > OE sibb); 'sieve' is absent. Consensus reconstruction PGmc *sibi- (neuter i-stem, orig. s-stem *sib-iz, PIE *seib-/*seip- 'to drip, strain', Pokorny IEW I 889–890, 894). Kluge/Seebold (s.v. Sieb) WGmc *sibi- n.; Brunner §288 Anm. (orig. s-stem absorbed into i-decl.); Campbell §§608–609 (short neut. i-stem, cf. spere, gedyre). Early Corpus Glossary form sibi (Campbell §444, archaic ⟨b⟩) confirms the *-i ending. Cannot be *sibja- (would feed WGG → OE **sibb, cf. OE sibb 'kinship' < *sibjō). Cannot be *sibaz a-stem (would give OE **sif). PROTOFORM corrected 2026-04-24 from *síbaz to *síbi per §17.15 three-agent research (Kroonen, Orel, Kluge, Brunner, Campbell, R/T, Hogg, Fulk, Pokorny).`

The live row already separates the modelling input from the older project headword, but the row still needs a careful distinction between inherited cognate-set reconstruction, OE derivational input, and the attested OE target. No pilot or full lexeme report exists for this row; the packet is only a starting dossier.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace `*síbi -> sife`; and `DEV_NOTES.md` §17.15, which is the current repo-local synthesis for why the OE row moved from `*síbaz` to `*síbi`.
- **Useful background:** the packet’s `old_english_wiktionary.tsv` hit; the bibliography-key suggestions; and the older `DEV_NOTES` notes about labial blocking in unstressed-i lowering, which help explain why `sife` is phonologically plausible once the right stem class is chosen.
- **Stale or superseded:** packet snippets treating `*síbaz` as the relevant OE derivational input; the older mismatch framing that expected `sife` from an a-stem; and the generic “stubborn cases” English-harness mention, which is implementation history rather than lexical evidence.
- **Irrelevant or misleading:** any reading of the packet’s older `*sibaz` tables as proof that a-stem `*sibaz` is still acceptable for this OE row; and any conflation of `sife` with the separate kinship lexeme `sibb < *sibjō-`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`, especially §17.15 and the earlier labial-blocking notes at 5371-5374 and 17459-17470.
- `Germanic/data/germanic-aligned-final.tsv` for all concept-479 cognate-set rows.
- `Germanic/docs/lexeme_reports/coverage_audit.md` (no existing pilot/full report coverage for row 2189).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- live FST check via `flookup -i backend/old_english.bin`.

No full dossier or analysis file was named in the packet or TSV note, and targeted repo searches did not surface a row-specific dossier beyond `DEV_NOTES`.

The extra pass confirms four important points. First, the live FST still gives `síbi -> sife`, `síbiz -> sife`, `síbaz -> sif`, and `sibja -> sibb`, so the row problem is stem-class/input selection rather than a missing OE rule. Second, Campbell and Clark Hall both support OE `sife` and archaic `sibi`; Kluge/Seebold gives WGmc `*sibi-`; and Ringe & Taylor plus Fulk support the contrasting geminated kinship line `sibj- > sibb`. Third, Orel’s printed `*sibaz` is best read here as cover notation, not as decisive evidence for an OE-relevant a-stem. Fourth, the non-OE cognate-set rows for Dutch, English, and German still carry legacy `*síbaz`, so the OE row is currently cleaner than the wider concept set.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / comparative headword:** the live TSV still has `PROTO = *síbaz`, but the strongest current repo-local evidence points instead to an i-/old s-stem line, i.e. PGmc `*síbiz` or stem-form `*sibi-`, not a true a-stem. `*síbaz` survives mainly as legacy project shorthand and as the value retained in the non-OE cognate rows.
2. **Project input form used for derivation:** `PROTOFORM = *síbi` is the correct OE modelling input under current project conventions (acute stress, no final `*-z`).
3. **OE target form:** `sife` is the attested Old English lemma represented by the row.

So the memo should not collapse the levels into “PROTOFORM corrected, everything else settled.” The narrower conclusion is: the OE derivation must run from i-stem/s-stem material `*síbi`, while the row’s surviving `PROTO = *síbaz` looks like inherited project bookkeeping rather than the best current reconstruction.

## Old English philology

`sife` is an attested OE citation form, not a reconstructed West-Saxon convenience form and not a late paradigm-cell substitute. Repo-local lexicographic evidence is straightforward:

- `old_english_wiktionary.tsv`: `sieve | sife`
- `Clark Hall`: `sife (y) n. 'sieve'`, with `sibi (GL) ... = sife`
- Campbell §444: Corpus Glossary `sibi`, explicitly useful as early orthographic evidence for the voiced spirant later written `f`
- Campbell §609: `sife` grouped with short neuter i-stems such as `spere`

The key philological distinction is between `sife` and `sibb`. `sibb` belongs to the kinship lexeme from `*sibjō-` / `sibj-`, where West Germanic gemination is expected; `sife` does not. The minimal pair is therefore genuine evidence against treating sieve as a ja-stem. Nothing in the repo material requires a dialect-specific or manuscript-specific special claim beyond the normal note that `sibi` is the early glossary spelling and `sife` the classical normalized spelling.

## Project problem and solution

The project problem was that the older row used a-stem `*síbaz`, which the FST rightly turns into `sif`; the target lexeme, however, is attested `sife`. The current solution is the correct type of solution for an `early_analogy` row: keep the OE derivation on the historically appropriate i-stem/s-stem line by feeding `PROTOFORM = *síbi`, rather than trying to repair `*síbaz` with later OE-side adjustments.

So row 2189 is best understood as an upstream stem-selection case. It is **not** a `late_analogy` row, because no special OE inflectional cell is being substituted; and it is **not** a `reconstructed_oe` row, because the target `sife` is attested. The real remaining project issue is whether the row’s surviving `PROTO = *síbaz` should continue as legacy headword shorthand or be brought into line with the reconstruction that the note itself now argues for.

## Paradigm probe

No paradigm probe is required.

This is not a nominative-vs-genitive or oblique-cell selection problem. The decisive contrast is earlier: i-stem/s-stem `*síbi` versus a-stem `*síbaz` and ja-stem `*sibja`. The live FST comparator already answers that question directly (`*síbi/*síbiz -> sife`, `*síbaz -> sif`, `*sibja -> sibb`), so there are no missing OE paradigm cells that need probing for the memo stage.

## Recommended final report

Recommend a concise final report stating that OE `sife` is an attested short neuter i-stem, with early Corpus Glossary `sibi`, and that the project correctly derives it from `PROTOFORM = *síbi` while distinguishing this OE modelling input from the row’s older comparative `PROTO` bookkeeping.

## Data-change recommendations

- **TSV `PROTO`: change recommended.** The strongest current repo-local evidence no longer supports a true a-stem `*síbaz` for this lexeme. To match existing PGmc citation-style conventions, the row should probably use `*síbiz` in `PROTO` (or else a clearly marked stem-form `*sibi-` if the column policy permits), rather than retaining legacy `*síbaz`.
- **TSV `PROTOFORM`: no change recommended.** `*síbi` is the right derivational input.
- **TSV `COUNTERPART`: no change recommended.** `sife` is the correct OE target.
- **TSV `DERIVATION_CLASS`: no change recommended.** `early_analogy` is the right class for this upstream stem-choice problem.
- **TSV `NOTE`: change recommended.** The note is rich and mostly right, but it should explicitly separate the recommended cognate-set proto from the OE modelling input. If `PROTO` is updated, the note should say so directly instead of only recording a `PROTOFORM` correction.
- **`oe_known_problems.tsv`: no change recommended.** The row is handled coherently once the stem class is fixed.
- **`DEV_NOTES` / dossier text: change recommended.** `DEV_NOTES` §17.15 should be lightly updated so its conclusion is not read as “only PROTOFORM changed while PROTO *síbaz remains philologically sound.” If the broader concept set keeps legacy `*síbaz` in non-OE rows for now, that should be marked explicitly as project bookkeeping rather than current reconstruction. No separate dossier text change is needed, because no row-specific dossier exists.

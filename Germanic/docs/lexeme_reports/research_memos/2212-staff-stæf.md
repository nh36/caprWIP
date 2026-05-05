# Research memo — 2212 staff / stæf

## Starting point

- ID: 2212
- CONCEPT: staff
- COUNTERPART: stæf
- PROTO: *stábiz
- PROTOFORM: *stábaz
- DERIVATION_CLASS: early_analogy
- NOTE: Kroonen gives an a-stem `*staba-`; the row note says OE `stæf` has `æ`, not `e`, so the project uses an a-stem input rather than inherited `*-iz`.

The live row already distinguishes the cognate-set proto (`*stábiz`) from the modelling input (`*stábaz`). The memo question is whether that distinction is still the best account of the OE target `stæf`, and whether the surrounding documentation now needs cleanup.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row is current and already encodes the key project decision: `PROTO = *stábiz`, `PROTOFORM = *stábaz`, `COUNTERPART = stæf`, `DERIVATION_CLASS = early_analogy`.
- The packet’s compact derivation trace is current for the **project input form**: `*stábaz` yields `stæf` in the present FST.
- The packet’s main DEV_NOTES section (the stem-class audit at `DEV_NOTES.md:4689-4810`) is current and gives the real evidential core: dictionary disagreement over PGmc stem class, plus the OE phonological argument against straight i-stem `*stabiz`.
- `analysis/notable_findings.md` is also current and summarizes the same disambiguation clearly.

**Useful background:**
- `analysis/arestoration_r_l_research.md` is useful because it situates `stæf` among closed monosyllables that keep `æ`, and it also cites plural `stafas` as a contrasting open-syllable form.
- `old_english_wiktionary.tsv` is a light confirmation that the repo treats `stæf` as the ordinary OE lexeme/headword.
- `coverage_audit.md` is useful workflow context: this row requires a lexeme report but currently has no pilot/full report covering it.

**Stale or superseded:**
- The packet’s diagnostic references to the older wrong input `*stábiz` and output `stefe` are valuable as project history, but not as current lexical modelling.
- The DEV_NOTES TSV-update bullet still says “Row 1094 (ID 2212),” where `1094` is legacy line-order bookkeeping, not the row ID to cite now.
- Regression/debug-snapshot mentions such as `*stábaz -> staf` are diagnostic implementation history, not authority on the lexeme itself.

**Irrelevant or misleading:**
- The packet’s unrelated late DEV_NOTES hit about a parasite-word / Old Frisian discussion is not evidence for OE `stæf`.
- Later ME/ModE `staff` with `a` is not evidence for the OE target vowel.

## Additional repo research

Beyond the packet, I checked:
- `Germanic/docs/DEV_NOTES.md` around the full stem-class discussion and update notes.
- `Germanic/docs/analysis/notable_findings.md` for the project-level summary of the `*kraft- / *stab-` stem-class problem.
- `Germanic/docs/analysis/arestoration_r_l_research.md` for the closed-monosyllable vs. open-syllable behavior relevant to `stæf` / `stafas`.
- `Germanic/data/old_english_wiktionary.tsv` for supplementary lexical confirmation.
- `Germanic/data/oe_known_problems.tsv`, which has no entry for this lexeme.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and the published debug trace, which show that the row is in mandatory-report scope but still lacks a manual pilot/full report.
- `Germanic/tools/oe_paradigm_probe.py`, which currently has no built-in probe spec for `staff / stæf`.

I did not find a dedicated dossier or an existing pilot report for this lexeme. So the best repo evidence remains the live TSV row, the DEV_NOTES stem-class audit, and the two analysis files above.

## Reconstruction and early-stage forms

Three levels need to stay separate:

1. **Cognate-set proto / etymological headword:** `*stábiz` in TSV `PROTO`. This preserves the comparative stem-class problem rather than pretending it is fully settled at PGmc level.
2. **Project input form for derivation:** `*stábaz` in TSV `PROTOFORM`. This is the form the FST actually needs in order to reach the OE target without spurious i-umlaut.
3. **OE target form:** attested citation-form `stæf`.

The repo evidence supports keeping that split. Kroonen favors an a-stem (`*staba-`), while Orel and Kluge-Seebold explicitly allow i-/a-stem uncertainty. The project therefore does **not** need to claim that comparative PGmc is fully resolved as a-stem; it only needs to state that the OE branch must be modeled with a non-`*-iz` input. That is exactly what the present `PROTO` / `PROTOFORM` distinction does.

## Old English philology

`stæf` is treated in the repo as an attested OE citation form, not a reconstruction. The main philological issue here is not attestation status, dialect, or manuscript form, but the vowel: OE `æ` rules out a straightforward inherited i-stem input that would predict `e` (`stefe`).

The most useful supporting contrast is the repo’s discussion of plural `stafas`: closed monosyllabic singular `stæf` keeps `æ`, while open-syllable plural material can show restored `a`. That supports the row’s being about the singular headword, not about flattening the whole paradigm to one vowel outcome. I found no repo evidence justifying stronger claims about dialect or manuscript distribution, so the final report should avoid such claims.

## Project problem and solution

The project problem was a modelling mismatch: inherited `*stábiz` produced `stefe`, but the OE target is `stæf`. The solution already adopted in the live data is the right one: keep `*stábiz` as the cognate-set proto, but feed the cascade `*stábaz` as an early analogical / stem-class-adjusted OE input.

That makes `early_analogy` the right derivation label. The row is not a still-unmodelled exception and not a late OE paradigm-cell substitution; it is an upstream choice about which early Germanic stem configuration best fits the English outcome.

## Paradigm probe

A paradigm probe is **not required** for this memo or for the eventual final report. The row’s core issue is stem-class disambiguation for the citation form, and the existing repo evidence already resolves that without needing a new probe table.

It is still worth noting that there is currently no built-in `oe_paradigm_probe.py` spec for this lexeme. If a future editor wants a supplementary probe, it should be framed as optional supporting material rather than as missing required evidence.

## Recommended final report

The final `### Lexeme report` should be brief and source-dense: say that comparative dictionaries disagree on whether the preform was i-stem or a-stem, but OE `stæf` with `æ` excludes a direct `*-iz` input for English. Then state that the project keeps `PROTO = *stábiz` as the cognate-set label while using `PROTOFORM = *stábaz` as the modelling input, which correctly yields attested OE `stæf`.

## Data-change recommendations

- **TSV PROTO:** **No change.** `*stábiz` is still useful as the cognate-set proto/headword precisely because the comparative stem class remains disputed.
- **TSV PROTOFORM:** **No change.** `*stábaz` is the right project input for the OE derivation.
- **TSV COUNTERPART:** **No change.** `stæf` is the correct OE target/headword.
- **TSV DERIVATION_CLASS:** **No change.** `early_analogy` still fits the project’s solution.
- **TSV NOTE:** **Yes, improve it.** The current note should be expanded so it does not sound as if Kroonen alone settled the matter; it should mention that Orel and Kluge-Seebold preserve i-/a-stem uncertainty, while the OE vowel still forces the project’s a-stem modelling input.
- **`oe_known_problems.tsv`:** **No change.** This row is now a resolved modelling choice, not an outstanding exception ledger item.
- **`DEV_NOTES` / dossier text:** **No substantive change required.** The current DEV_NOTES discussion is still useful; at most, a future cleanup could normalize legacy labels like “Row 1094” to the stable row ID `2212`. There is no dedicated dossier file to revise.

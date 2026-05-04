# Research memo — 2227 strew / strīeġan

## Starting point
- ID: 2227
- CONCEPT: strew
- COUNTERPART: `strīeġan`
- TSV `PROTO`: `*stráwjaną`
- TSV `PROTOFORM`: `*stráwjaną`
- TSV `DERIVATION_CLASS`: `reconstructed_oe`
- TSV `NOTE`: the row already frames the target as an unattested West Saxon reconstruction, contrasts attested Anglian `strēgan`, and says West Saxon remodelled the verb as class II `strewian`; it cites `DEV_NOTES §17.10.36`.

## Packet evidence assessment
- **Authoritative/current:** the TSV row; the current compact derivation trace and debug snapshot, which now derive `strīeġan`; the changelog entry at `DEV_NOTES.md` line 10411; and the later `DEV_NOTES` material at `§17.10.36-q3` and `§17.10.36-q3-probes`, which reflects the implemented rule and the current row design.
- **Useful background:** the broader `DEV_NOTES §17.10.36` audit and its chronology/research subsections. They preserve the literature review and the earlier decision tree, even where the final project choice changed later.
- **Stale or superseded:** packet hits from `DEV_NOTES.md` around lines 26825–26856, where row 2227 was still being treated as an Anglian `strēgan` target or as an open option set; and `Germanic/docs/non_firing_rules_analysis.md`, which still treats `strewian` as the expected output from an older project state.
- **Irrelevant or misleading:** generic packet keyword hits on unrelated Anglian material. Per `packet_quality_notes.md`, those are not high-confidence lexical evidence for this row.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at line 10411, `§17.10.36`, `§17.10.36-chronology`, `§17.10.36-research`, `§17.10.36-q3`, and `§17.10.36-q3-probes`
- `Germanic/fsts/germanic.txt` around `OEJStrengtheningAfterFrontDiphthong`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/data/old_english_wiktionary.tsv`
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`
- `Germanic/docs/non_firing_rules_analysis.md`
- `Germanic/data/oe_known_problems.tsv` (checked; no relevant entry)

The packet did not name any separate full dossier file for this row.

## Reconstruction and early-stage forms
The row’s etymological headword and project input are both still inherited class-I `*stráwjaną`; repo-local variation such as `*strawjan-` / `*straujan-` is not a substantive disagreement. The current WS-default derivation in the debug snapshot is:

`*stráwjaną > *stráujaną > *strēajaną > *strīejąn > *strīejan > *strīeʒan > strīeġan`.

That chain is a reconstruction of the regular West Saxon reflex after the later `OEJStrengtheningAfterFrontDiphthong` rule now implemented in `germanic.txt`. Attested Anglian `strēgan` represents the same inherited class-I verb after Anglian smoothing. Attested West Saxon `strewian / streowian / strēawian` does not continue the row’s direct PGmc-to-OE phonological chain; it belongs to the later class-I → class-II remodelling discussed in `DEV_NOTES`.

The exact mechanism behind medial `-ġ-` is not presented as fully settled in the literature: `DEV_NOTES §17.10.36-q3` records competing analyses (gemination residue, direct j-retention, analogical spread). The current repo conclusion is narrower: after the relevant `*aw`-derived front diphthongs, the OE output for this class preserves the glide and spells it with `ġ`.

## Old English philology
The crucial distinction is three-way:
- **Attested Anglian inherited class-I form:** `strēgan`
- **Attested West Saxon remodelled class-II forms:** `strewian`, `streowian`, `strēawian`
- **Unattested reconstructed West Saxon inherited class-I reflex:** `*strīeġan`

`old_english_wiktionary.tsv` gives the ordinary dictionary lemma `strewian`, which is useful as evidence for the attested WS citation form but not decisive for the project’s row target. The row is intentionally not modelling that attested class-II lemma. It is modelling the predicted inherited WS reflex of the PGmc class-I verb.

The memo therefore has to keep attested and reconstructed material separate. `strīeġan` is not an attested manuscript lemma for this verb in repo-local evidence. Its support is philological and comparative: the repo’s `DEV_NOTES` survey cites grammarians who explicitly group `strēgan/strīeġan` with `cīeġan`, `hīeġ`, and similar `-ġ-` outcomes, while also agreeing that the actual WS verb was remodelled.

## Project problem and solution
The project problem was whether row 2227 should target:
1. attested Anglian `strēgan`,
2. attested remodelled WS class-II material,
3. or reconstructed WS class-I `strīeġan`.

Current repo state has already chosen (3). The FST is WS-default elsewhere, Anglian smoothing is deliberately not modelled, and the row now matches once the narrow aw-series `j`-retention/`ġ` rule is added. The recommended memo should therefore treat the older `strēgan`-target discussions in `DEV_NOTES` as diagnostic project history, not as the live recommendation.

## Paradigm probe
No new paradigm probe is needed. `DEV_NOTES §17.10.36-q3-probes` already exhausts the relevant trigger class and shows that only two OE rows contain `*Vw + *j` inputs; for row 2227, the new rule changes exactly this form and nothing else in the corpus. What matters now is explanatory framing, not further enumeration.

## Recommended final report
Recommend a final report that presents `strīeġan` as a reconstructed West Saxon class-I reflex now supported by the current FST, while explicitly contrasting attested Anglian `strēgan` and attested remodelled WS class-II `strewian/streowian/strēawian`.

## Data-change recommendations
- TSV `PROTO`: no change.
- TSV `PROTOFORM`: no change.
- TSV `COUNTERPART`: no change.
- TSV `DERIVATION_CLASS`: no change.
- TSV `NOTE`: no required change; an optional editorial improvement would be to name the wider WS variant set (`strewian/streowian/strēawian`), not just `strewian`.
- `oe_known_problems.tsv`: no change.
- `DEV_NOTES` or dossier text: yes, editorial cleanup would help. The earlier option-analysis portions of `§17.10.36` should be marked more explicitly as superseded by the later implemented `q3` solution so future packets do not over-weight obsolete `strēgan`/`strewian` decision branches.

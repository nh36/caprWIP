# Research memo — 2204 spar / spearra

## Starting point

- **ID:** 2204
- **CONCEPT:** spar
- **COUNTERPART:** spearra
- **PROTO:** *spárrô
- **PROTOFORM:** *spárrô
- **DERIVATION_CLASS:** regular
- **NOTE:** Kroonen *sparran- m. 'rafter, spar' → OE spearra m.; sperran is the verb 'to bar'

This is a regular noun row whose current derivation already matches cleanly. The memo issue is not a live phonological mismatch, but source control: the noun **spearra** must be kept separate from the verb dossiers for row 2205 (*sparian* 'spare') and from the unrelated verb **sperran** 'to bar'.

## Packet evidence assessment

**Authoritative/current:** the TSV row; the packet's compact derivation trace showing `*spárrô -> spearra`; `DEV_NOTES.md` line 30633, where row 2204 is listed as a successful breaking-before-geminate case; and `analysis/arestoration_r_l_research.md` lines 530-531 and 741, which confirm the current pipeline output `spárrô -> spearra` and classify it as "breaking before geminate *rr*" under the Luick-based exclusion.

**Useful background:** the TSV note's pointer to Kroonen's noun reconstruction `*spar(r)an-`; the coverage/debug material showing that row 2204 still needs lexeme-report coverage because it has a non-empty `NOTE`; and Kroonen's broader discussion that sets the noun beside, but distinct from, the adjective/verb `*spara- / *sparēn-`.

**Stale or superseded:** the packet's concept-name hits to `DEV_NOTES §17.32` and the two `dossier-spar-2025` files are about row 2205, the verb 'spare', not row 2204. They are useful only as diagnostics for packet overreach. They should not be treated as current lexical evidence for **spearra**.

**Irrelevant or misleading:** `old_english_wiktionary.tsv` gives `spar -> sperran`, which is the verb 'to bar' and not this noun. For this row it is a homograph trap, not corroboration.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around line 30633 and the full `§17.32` block around lines 37755-37890.
- `Germanic/docs/dossier-spar-2025.md`.
- `Germanic/docs/dossier-spar-apocope-2025.md`.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports*.md`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, which explicitly gives `*spar(r)an- m. 'bar, beam, rafter'` and notes related ON/Far. `sperra` and ON `sparr`.

No pilot or full lexeme report for row 2204 appears to exist yet; current coverage files still show it as report-required and uncovered.

## Reconstruction and early-stage forms

Three levels should be kept distinct:

1. **Cognate-set proto / etymological headword:** Kroonen's `*spar(r)an-` m. 'bar, beam, rafter'.
2. **Project input form:** TSV `PROTO`/`PROTOFORM` `*spárrô`, i.e. the specific early nominal form the OE pipeline maps forward.
3. **OE target form:** `spearra`, the Old English noun targeted by this row.

Those are compatible, not contradictory. The packet's derivation path is straightforward: `*spárrô > *spærrô` by Anglo-Frisian brightening, then `*spearrô` by OE breaking before geminate `*rr`, then `spearra` by unstressed long-vowel shortening. The important contrast is that the noun belongs with Kroonen's nominal `*spar(r)an-` set, whereas the nearby repo dossiers concern the distinct verbal set `*sparēn- / *spárōjaną`.

## Old English philology

Repo-local evidence supports **spearra** as the OE noun intended here, but the packet does not supply a manuscript-specific attestation dossier; the strongest direct authority inside the repo is the etymological citation through Kroonen plus the aligned nominal cognate set. That is enough to justify the row, but not to make stronger claims about dialect or manuscript distribution.

Philologically, this row is a **noun citation-form row**, not a paradigm-cell row. Nothing in the repo suggests that `spearra` is an inflected-cell workaround or a reconstructed unattested OE form of the kind seen in some verb dossiers. The main lexical hygiene point is disambiguation:

- **spearra** = noun 'spar, rafter, bar' for row 2204.
- **sparian** = verb 'to spare' for row 2205.
- **sperran** = verb 'to bar, shut' and should not be imported into this noun row just because English glosses overlap.

## Project problem and solution

The project problem is mostly a dossier-boundary problem. Because the English gloss **spar** overlaps with the verbal lexemes 'spare' and 'bar', packet extraction pulls in concept-name hits from row-2205 verb research and a Wiktionary gloss for **sperran**. If those are read uncritically, they blur three separate lexemes.

The correct project solution is conservative: keep row 2204 as the regular noun derivation `*spárrô -> spearra`, treat the row-2205 verb dossiers as unrelated background noise for this memo, and make the final report explicitly distinguish the noun from both `sparian` and `sperran`.

## Paradigm probe

**No paradigm probe is required.** This is not a paradigm-cell case, not a late-analogy choice, and not a row whose correctness depends on comparing competing OE cells. The current issue is lexical-source disambiguation, not paradigm selection.

## Recommended final report

Recommend a short final lexeme report that says the row is a regular nominal pathway from project input `*spárrô` to OE `spearra`, while explicitly separating that noun from the verb dossiers for `sparian` and from the unrelated verb `sperran`. A paradigm-probe section is unnecessary.

## Data-change recommendations

- **TSV `PROTO`:** **No change.** `*spárrô` is a workable project input for the current derivation.
- **TSV `PROTOFORM`:** **No change.** Same reasoning: the forward derivation already lands on `spearra`.
- **TSV `COUNTERPART`:** **No change.** `spearra` is the intended OE noun target.
- **TSV `DERIVATION_CLASS`:** **No change.** `regular` is correct; the row is not a paradigm-cell or analogy exception.
- **TSV `NOTE`:** **Yes, minor clarification recommended.** It would be better to say explicitly that Kroonen's etymological headword is `*spar(r)an-` while TSV input is `*spárrô`, and to warn against confusion with both `sparian` 'spare' and `sperran` 'bar'.
- **`oe_known_problems.tsv`:** **No change.** This row is not a live known-problem case.
- **`DEV_NOTES` text:** **Minor cleanup recommended.** The `§17.32` block already says it is about row 2205, but packet extraction still drags it into row 2204 via concept-name hits; stronger row-ID labelling of those dossier references as verb-only material would reduce future false positives.
- **Dossier text:** **Minor cleanup recommended.** `dossier-spar-2025.md` and `dossier-spar-apocope-2025.md` are about the verb *spar-* only; adding an explicit "not the noun row 2204 `spearra`" disclaimer near the top would make their scope clearer and reduce misleading packet spillover.

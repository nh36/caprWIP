# Research memo — 2030 fowl / fugol

## Starting point
- ID `2030`; CONCEPT `fowl`; COUNTERPART `fugol`.
- TSV `PROTO` = `*fúglaz`; TSV `PROTOFORM` = `*fúglaz`; TSV `DERIVATION_CLASS` = `unexplained_unmodelled`.
- TSV note: `fugol` is treated as a documented exception to regular u-lowering/a-umlaut; regular sound change gives `fogol`, and no Lautgesetzlich paradigm-cell substitute has survived scrutiny.

## Packet evidence assessment
- **Authoritative/current:** the current TSV row; the packet's compact trace showing `*fúglaz` regularly yields `fogol`; the live `oe_known_problems.tsv` entry; the early DEV_NOTES u-lowering exception review; and especially DEV_NOTES §17.10.34a, which overturns the attempted paradigm-cell rescue and restores row 2030 to exception status.
- **Useful background:** the earlier literature review of u-lowering exceptions near labials, and the notes on OE parasite/epenthetic vowels in `-gl` clusters, because they help isolate what part of `fugol` is regular and what part is exceptional.
- **Stale/superseded:** DEV_NOTES §17.10.34's proposal to retarget the row to gen.sg. `*fúglis → fugles`. The packet includes that material because it matched the row history, but it is no longer current after §17.10.34a.
- **Irrelevant or misleading if not contextualized:** the stale "chosen approach" passage at DEV_NOTES 26053 is not an authoritative recommendation anymore; it must be read together with the explicit reversal in §17.10.34a.

## Additional repo research
Checked beyond the packet: `Germanic/data/oe_known_problems.tsv`; `Germanic/docs/DEV_NOTES.md` at the main u-lowering exception section (lines 63-142), §17.10.34-§17.10.34a (25940-26197), and the notes that distinguish regular `OEGLInsertion`/parasite-vowel behavior from the root-vowel problem; `Germanic/data/germanic-aligned-final.tsv`; `Germanic/data/old_english_wiktionary.tsv`; and `Germanic/data/old_english_swadesh.tsv` (no relevant hit).

## Reconstruction and early-stage forms
Here TSV `PROTO` and TSV `PROTOFORM` correctly coincide: the row is still anchored to the nominative a-stem headword `*fúglaz`, not to a surrogate oblique cell. The regular derivational chain is straightforward: `*fúglaz` should undergo u-lowering before the low-vowel ending and then, after later OE cluster treatment, surface as `fogol`. The abandoned rescue strategy mattered because it tested the whole paradigm space and showed the trap clearly: low-vowel cells give `**fogol`, while high-vowel cells that block u-lowering then feed i-umlaut and give fronted outcomes such as `**fygl-`, not attested `fugl-`.

## Old English philology
`fugol` is the ordinary OE lexical form and is supported by the local lexical table. The medial `-o-` is not the core irregularity: OE epenthetic/parasite vowel insertion in a final `-gl` cluster is regular, so `-gol` by itself is expected once the word reaches the relevant OE stage. The real philological problem is the root vowel: the attested form keeps `u` where regular pre-OE/NWGmc development predicts `o`. That is why `fugel`-type spellings or `fugles`-type inflected forms do not rescue the row; they do not eliminate the same historical tension.

## Project problem and solution
The project initially treated these u-retention items as genuine lexical exceptions. It then briefly tried the now-rejected strategy of switching several rows, including this one, to high-vowel oblique cells such as `*fúglis → fugles`. The revision in §17.10.34a showed that this does not solve the problem: the high vowel blocks a-umlaut, but it also triggers i-umlaut, so the proposed rescue forms are not Lautgesetzlich sources for `fugl-` either. The correct project solution is therefore to leave the row as a documented exception, preserve the honest headword `*fúglaz`, and record the failure in `oe_known_problems.tsv` rather than inventing a pseudo-regular derivation.

## Paradigm probe
A new probe is optional. The methodological question has already been settled in §17.10.34a. If the eventual report wants a small demonstration table, it should compare nom.sg. `*fúglaz` with one high-vowel oblique such as `*fúglis` or `*fúgli`, so the two failure modes are visible: low-vowel cells produce the regular lowered form `fogol`, high-vowel cells preserve `u` only at the cost of i-umlaut and therefore miss `fugol` in a different way.

## Recommended final report
Recommend a concise exception report: keep `*fúglaz / fugol` as a documented non-derivable OE lexeme, state explicitly that `fogol` is the regular phonological outcome, and separate the regular epenthetic `-o-` from the exceptional retention of root `u`.

## Data-change recommendations
- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change.
- **TSV `DERIVATION_CLASS`:** no change; `unexplained_unmodelled` remains the correct label for a documented but non-derivable exception of this type.
- **TSV `NOTE`:** recommend updating the citation so it points to §17.10.34a, or to §§17.10.34-17.10.34a together, rather than citing only the earlier section that still contains the reverted `*fúglis → fugles` plan.
- **`oe_known_problems.tsv`:** recommend expanding the refs for `*fúglaz` so they cite DEV_NOTES §17.10.34a as well as the broader `notable_findings#2` pointer.
- **DEV_NOTES/dossier text:** no substantive rewrite required; future packets and notes should simply continue to treat §17.10.34a as the authoritative conclusion and §17.10.34 as superseded background.

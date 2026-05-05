# Research memo — 2278 weapon / wǣpn

## Starting point

- **ID:** 2278
- **CONCEPT:** weapon
- **COUNTERPART:** wǣpn
- **PROTO:** *wḗpną
- **PROTOFORM:** *wḗpną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *wēpnăn→*wēpną (n. a-stem nom.sg.; Kroonen)

The live row is a note-bearing `regular` row. Unlike `thistle`, it has not been moved to an oblique paradigm cell: the current target is still the unbroken OE nominative/accusative singular `wǣpn`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet derivation trace showing that the present cascade derives `*wḗpną -> wǣpn`; and `DEV_NOTES.md` §17.18.7.1, which records the current project decision to retain the ten attested unbroken `-Cl/-Cn/-Cm#` nom.sg. rows, including `wǣpn`, as the dataset's chosen early/poetic/Anglian-style targets.
- **Useful background:** the packet's excerpts from `DEV_NOTES.md` §17.18.1–§17.18.5, because they preserve the handbook contrast `wǣpn ~ wǣpen / wǣpnes` and the dictionary-headword point that BT/DOE lemmatize `wǣpen`; `old_english_wiktionary.tsv`; `bright_anglo_saxon_reader.vision.txt`; and Brunner's grammar text on secondary vowels.
- **Stale or superseded as live-row authority:** the option-analysis material in `DEV_NOTES.md` §17.18.4–§17.18.5 if read as a current recommendation to move the whole class to broken nominatives or to gen.sg. targets. Those sections are valuable project history, but §17.18.7 is the later decision actually governing row 2278.
- **Irrelevant or misleading:** the packet's sandbox-era `weapon` hit at `DEV_NOTES.md:2249`, which is just generic tooling history; and any reading of the BT/DOE headword `wǣpen` as if it automatically overrode the row's deliberately chosen unbroken target.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`, especially §17.18.4–§17.18.7.
- `Germanic/data/oe_known_problems.tsv` (no entry for this row).
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.missing_reports.md` (confirm row 2278 needs memo/report coverage because `NOTE` is non-empty).
- `docs/references/bright_anglo_saxon_reader.vision.txt` (paradigm table with `wapen`, `wæpnes`, `wapne`, `wapnu`).
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` (secondary-vowel discussion; long-syllable `-n` words tend toward broken forms, but unbroken spellings remain part of the evidence base).
- `Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md` and `Germanic/docs/dossier-shoulder-cellchoice-2026.md` for collateral project treatment of related cluster/paradigm issues; neither changes the row-2278 conclusion.

No row-specific pilot report or dedicated dossier for `weapon / wǣpn` appears to exist in the repo at present.

## Reconstruction and early-stage forms

This row still needs the three-way distinction, even though two columns coincide.

1. **Cognate-set proto:** TSV `PROTO = *wḗpną` is the Proto-Germanic headword for the cognate set.
2. **Project input form:** TSV `PROTOFORM = *wḗpną` is the actual derivational input for this row. Here it happens to be the same string as `PROTO`; unlike `thistle`, there is no separate paradigm-cell input.
3. **OE target form:** `wǣpn` is the selected Old English target, specifically the unbroken nominative/accusative singular form chosen by the project.

The row note's Kroonen-style remark about oblique `*wēpnăn` is etymological background, not an instruction that the row is secretly an oblique-cell entry. The live derivation still runs from nominative `*wḗpną` through NWGmc lowering to `*wǣpną`, then OE heavy-syllable nasal apocope to `wǣpn`. The later broken simplex `wǣpen` belongs to the OE parasite-vowel problem discussed in `DEV_NOTES` §17.18, not to the current TSV `PROTOFORM`.

## Old English philology

The philology is a headword/register problem, not an unattested-form problem.

- **Attested unbroken form:** `wǣpn` is attested, especially in compounds and poetic/simplex early material. `DEV_NOTES` treats it as directly attested and therefore eligible for retention.
- **Attested broken form / dictionary lemma:** `wǣpen` is also attested and is the standard BT/DOE lemma; `Bright`'s paradigm table likewise gives `wapen` beside gen.sg. `wæpnes`.
- **Attested oblique stem:** `wǣpnes` is the regular unbroken gen.sg. and is part of the textbook contrast cited in the repo's grammar notes.
- **Register/dialect value:** the broken nominative is the late West Saxon prose norm, while the unbroken nominative belongs to earlier, poetic, or Anglian-looking evidence. The project has deliberately chosen the latter register for this row.
- **Citation-form issue:** dictionary convention points to `wǣpen`, but the current row does not aim to reproduce the normalized dictionary headword; it aims to preserve one attested OE variant that the present FST already derives cleanly.

So the safest philological description is: `wǣpn` is an attested OE nominative variant, `wǣpen` is the more standard dictionary/late-WS lemma, and `wǣpnes` is the regular oblique form. The row represents the first of those three, not the second or third.

## Project problem and solution

The project problem is that the current OE cascade does not model general parasite-vowel insertion for this cluster class, while handbook and dictionary evidence show that forms like `wǣpen` became standard in later West Saxon. That creates a potential mismatch between "most normalized headword" and "current derivable target."

The current project solution is already recorded in `DEV_NOTES` §17.18.7.1 and is internally coherent:

- retain unbroken `wǣpn` because it is attested;
- treat it as one of the ten rows intentionally kept in an early/poetic/Anglian-style unbroken nominative set;
- avoid changing this row to a paradigm-cell solution, because unlike `thistle`, its unbroken nominative is not unattested;
- use the memo/report layer to explain that `wǣpen` is the dominant dictionary and late-WS prose headword.

In other words, row 2278 is not a hidden modelling failure. It is a deliberate editorial choice about which attested OE variant the dataset wants to represent.

## Paradigm probe

A paradigm probe is **not required** for the current row state.

This row is still a `regular` nominative target, not a paradigm-cell workaround, and the live project decision is to keep `wǣpn` as the selected form rather than to choose among cells. If the project later reopens the policy question, the informative comparison would be:

- nom.sg. unbroken `*wḗpną -> wǣpn`;
- nom.sg. broken late-WS target `wǣpen` (not currently modeled by the FST);
- gen.sg. `wǣpnes`.

But that is a future policy probe, not a blocker for the present memo.

## Recommended final report

Recommend a concise final report that says row 2278 intentionally keeps attested unbroken OE `wǣpn` as the dataset target, while acknowledging that BT/DOE and late West Saxon prose prefer broken `wǣpen` and that `wǣpnes` is the regular unbroken oblique form. The report should stress that `PROTO`/`PROTOFORM` here remain nominative PGmc `*wḗpną`, and that the issue is editorial register choice rather than a paradigm-cell repair.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended. `wǣpn` remains defensible as the project's chosen attested OE variant.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is still defensible because the derivation itself is regular under the chosen target/register.
- **TSV `NOTE`:** **change recommended.** The current note only gives Kroonen-style proto background. It should also say explicitly that the row deliberately targets attested unbroken OE `wǣpn`, whereas dictionary and late-WS prose usage usually lemmatize broken `wǣpen`, with oblique `wǣpnes`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** no change required. `DEV_NOTES.md` §17.18.7 already states the current policy clearly enough; the problem is that the live TSV note does not yet summarize that policy for this specific row.

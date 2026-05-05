# Research memo — 2294 wind / windan

## Starting point

- **ID:** 2294
- **CONCEPT:** wind
- **COUNTERPART:** `windan`
- **PROTO:** `*wíndaną`
- **PROTOFORM:** `*wíndaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: wind→windan (inf. of str.v. class III 'to wind, turn')`

This is a note-bearing regular row. The live row already derives cleanly to `windan`; the memo question is therefore mainly evidential: keep the verb row separate from noun `wind` noise and from older project history that briefly treated this lexeme as if it might involve Verner alternation.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and compact derivation trace are current; they show `PROTO = PROTOFORM = *wíndaną`, expected/output `windan`, and a note explicitly stating that the row targets the strong-verb infinitive.
- **Useful background:** the packet's later `DEV_NOTES` excerpts on the `wi -> wu` conditioning and on `*nd` clusters are still useful because they explain why the project must **not** over-fire to `wundan` and why `windan` is not a Verner case.
- **Stale or superseded:** the packet's older `DEV_NOTES` hit at `7233` (`*winþan-`, `*đ (?)`) is exploratory history, not current analysis. The later March 2026 sections explicitly replace that uncertainty with the conclusion that `windan` has original `*d` from PIE `*wendh-`, not a `*þ/*ð` alternation.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` and `old_english_swadesh.tsv` hits are for the noun `wind`, not the verb `windan`, so they should not be treated as row-level lexical evidence. The `widuwe-u-preservation` dossier hit is relevant only indirectly, as negative evidence that `windan` does **not** show the `wi -> wu` outcome.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md:7339-7381`, `7538-7560`, `7879-7882`, `43596-43645`
- `Germanic/docs/dossiers/widuwe-u-preservation.md:1102-1138` (full dossier named in the packet)
- `Germanic/docs/analysis/notable_findings.md:352-380`
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry)
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/docs/lexeme_reports/pilot/` (no pilot report for this lexeme found)
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`
- `docs/references/seebold_vergleichendes_woerterbuch.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`

Main findings from that wider check:

- Later `DEV_NOTES` now state clearly that `bindan, windan` continue PIE roots with aspirated `*dh > PGmc *d`, so they were never `*nþ/*nð` Verner rows [@Fulk2018; @RingeTaylor2014].
- The `widuwe-u-preservation` dossier is useful as a cross-check on project chronology: it explicitly treats `windan` as a non-`wu` form and uses it as a counterexample against over-broad `wi -> wu` triggering.
- `analysis/notable_findings.md` gives broader phonological context: before nasal + consonant, OE often retains `u` rather than lowering it, which fits later forms like `wunden` but does not challenge the infinitive `windan`.
- Comparative and OE lexical sources agree that the verb exists as ordinary OE `windan`; Seebold gives the principal parts `windan, wand, wundon, wunden`, and Clark Hall/Bosworth-Toller treat `windan` as a normal dictionary headword [@Kroonen2013; @ClarkHall1960; @BosworthToller1898].

## Reconstruction and early-stage forms

Three levels should still be kept distinct, even though this row happens to collapse the first two into the same TSV form.

1. **Cognate-set proto / etymological headword:** the row's `PROTO` is `*wíndaną`. Repo-local comparative dictionaries often cite lemma-style forms such as `*windan-` or `*wenda-` instead of the exact project spelling with `-aną`; those are lexicographic headword conventions, not direct rivals to the row's input [@Kroonen2013].
2. **Project input form for OE derivation:** `PROTOFORM` is also `*wíndaną`. Unlike paradigm-cell rows, there is no separate oblique or analogical input here.
3. **OE target form represented by the row:** the row targets the attested OE infinitive `windan`.

What is now superseded is not the row's live protoform but an older project hypothesis: `*winþan-`/`*đ (?)` was a temporary exploratory guess. Later repo work rejects that and restores `*d` as original, so the current `*wíndaną` analysis should be treated as the authoritative one.

## Old English philology

This is an **attested** OE verb, not a reconstructed OE target. Repo-local lexical sources treat `windan` as the citation infinitive and also preserve the ordinary strong-verb paradigm `wand`, `wundon`, `wunden` [@ClarkHall1960]. Seebold's comparative dictionary gives the same OE principal parts, which is enough to show that the lexeme is not a doubtful reconstruction but a standard inherited strong verb.

The main philological caution is lexical disambiguation, not attestation. Because English **wind** is also a noun, packet searches easily pull in noun evidence that is irrelevant to this row. The row note is therefore doing real work: it identifies the OE target specifically as the infinitive of the class-III verb 'to wind, turn'.

The prefixed participial example `awunden` in `DEV_NOTES` is useful only as background. It shows that the wider verb family can surface with the expected `u` vocalism in past-participial environments, but row 2294 itself is not targeting that cell; it is targeting the infinitive `windan`.

## Project problem and solution

The project problem here is modest but real: the row needs to stay insulated from two kinds of repo noise.

1. **Homograph noise:** searches for concept `wind` pull in noun material.
2. **Superseded Verner history:** early notes briefly grouped `windan` with genuine `*nþ/*nð` cases such as `findan`, but later notes explicitly reject that comparison.

The current project solution is correct:

- keep `PROTO = *wíndaną` as the cognate-set proto;
- keep `PROTOFORM = *wíndaną` as the OE modelling input;
- keep `COUNTERPART = windan` as the attested OE infinitive;
- keep `DERIVATION_CLASS = regular`;
- use the note/report prose only to explain that this is the verb, not the noun, and that older Verner-style discussion is historical only.

So this row is not a hidden paradigm-cell workaround and not a known-unmodelled exception. It is a regular citation-form verb row with some stale project history attached to it.

## Paradigm probe

A paradigm probe is **not required** for the current row treatment. The live issue is not an unresolved paradigm-cell dependency but simple row identification: attested infinitive `windan` versus irrelevant noun hits and superseded Verner speculation.

If the supervisor later wants a purely explanatory appendix probe, the most informative cells would be infinitive, preterite singular, preterite plural, and past participle (`windan`, `wand`, `wundon`, `wunden`). But that is optional background, not a prerequisite for the final report.

## Recommended final report

Recommend a short final report that treats row 2294 as a regular attested strong verb: distinguish the verb row from noun `wind` noise, state that `PROTO` and `PROTOFORM` are both `*wíndaną`, and note briefly that earlier `*winþan-` / Verner-style discussion is superseded by the later conclusion that the dental is original.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended. The current note already does the main disambiguating work by identifying the row as the infinitive of the verb, not the noun.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** light `DEV_NOTES` cleanup is recommended, but no dossier change is needed. In particular, the older `*winþan-` / `*đ (?)` table entry should be marked more explicitly as superseded exploratory history so future packet generation does not give it undue weight beside the later March 2026 conclusion.

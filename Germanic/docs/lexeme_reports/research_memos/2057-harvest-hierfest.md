# Research memo — 2057 harvest / hierfest

## Starting point

- **ID:** 2057
- **CONCEPT:** harvest
- **COUNTERPART:** hierfest
- **PROTO:** *xárbistuz
- **PROTOFORM:** *xárbistuz
- **DERIVATION_CLASS:** regular
- **NOTE:** R/T 14594-14603: hærfest is Anglian loan (Bammesberger 1997); WS hierfest attested (Toller); regular PGmc *harbistuz > WS hierfest via AFB+breaking+i-umlaut.

This is a note-bearing regular row. `coverage_audit.md` marks it as lexeme-report-requiring, and no pilot/full lexeme report for harvest was found.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing the current FST derivation `*xárbistuz -> hierfest`; and the packet’s link to `DEV_NOTES.md` §6585, which is the current implementation record for the `hierfist -> hierfest` fix.
- **Useful background:** the packet’s citation of Bammesberger 1997 and Ringe-Taylor on the `hærfest/herfest` problem; the exact-pair `DEV_NOTES` hit at line 38379; and the packet’s reminder that this row has no `oe_known_problems.tsv` entry.
- **Stale or superseded as lexical authority:** the packet’s treatment of `hierfest` as if it were straightforwardly attested OE. The repo’s reference files and the fuller `DEV_NOTES` section support `hierfest` as the expected **native WS outcome**, but Bammesberger and Ringe-Taylor treat attested `hærfest/herfest` as the real manuscript forms and explicitly say native WS `*hierfest/*hyrfest` is not securely attested.
- **Irrelevant or misleading:** the packet’s “no analysis and dossier hits” line is too narrow, because relevant repo analysis files do exist; and the packet’s compact derivation trace is good evidence for the cascade, but not by itself for attestation or dictionary headword status.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at §6585 (“OE hierfest 'harvest' — Unstressed Front Vowel Merger”) and the later summary table at line 38379.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/analysis/fryhtu_investigation.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv` — no row 2057 entry.
- `Germanic/data/old_english_wiktionary.tsv` — gives OE `hærfest`, not `hierfest`.
- `docs/references/bammesberger_1997_herfest.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt`.

Main result of this wider pass: the implementation question and the philological question are not the same. Repo-local phonological work now explains why the FST should output `hierfest`, but the dictionaries and Bammesberger article still point to attested OE `hærfest` with variant `herfest`, not to unproblematic attested `hierfest`.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction.

1. **Cognate-set proto / etymological headword:** `PROTO = *xárbistuz`, i.e. PGmc `*harbistuz/*harbista-` ‘harvest, autumn’. Kroonen and Bammesberger support the `*harbist-` family; Orel also records a variant reconstruction with medial `*u`, but that is background etymological history, not the live project choice.
2. **Project input form for derivation:** `PROTOFORM = *xárbistuz`, the same PGmc citation-form input currently fed to the OE cascade.
3. **OE target represented by the row:** currently `hierfest`.

The chronology of the regular native WS derivation is well supported inside the repo: PGmc `*harbist-` > Anglo-Frisian fronting `*hærbist-` > breaking `*hearbist-` > i-umlaut `*hierbist-` > late unstressed front-vowel merger `*hierbest-` > `hierfest`. The crucial point from `DEV_NOTES` is that the medial `*i` first triggers umlaut and only later lowers to `e`; that is why `hierfest`, not `hierfist`, is the expected regular WS output.

So the reconstruction itself is coherent. The real question is whether the row is meant to represent that reconstructed regular WS outcome or the attested OE lexical tradition.

## Old English philology

The repo-local philology does **not** support treating `hierfest` as the ordinary attested OE headword.

- **Attested dictionary/headword evidence:** `old_english_wiktionary.tsv`, Orel, Bosworth-Toller, and Clark Hall all point to `hærfest`, with `herfest` also recognized as a variant.
- **Bammesberger 1997:** this is the strongest repo-local authority on the exact problem. It argues that regular WS `*hierfest/*hyrfest` is what the sound laws would predict from `*harbist-`, but that those native WS forms are not securely transmitted; attested `hærfest` and `herfest` are instead explainable as non-WS, especially Anglian, forms and loans into WS.
- **Ringe-Taylor:** the repo text at 14594-14603 follows Bammesberger and treats `hærfest/herfest` as the difficult attested forms; again, the issue is lack of breaking in the attested tradition, not proof of attested `hierfest`.
- **Bosworth-Toller / Clark Hall:** both support `hærfest` as the lexical entry, and both acknowledge `herfest`. They do not provide strong clean support for exact `hierfest` as the normal headword.
- **Legacy/OCR noise:** scattered `heerfest`/`hierfeste` strings exist in older OCR-derived files, but they are not strong enough to override Bammesberger’s explicit statement that native WS `*hierfest/*hyrfest` is not transmitted.

So the safest philological statement is: `hærfest` and `herfest` are attested OE forms; `hierfest` is best treated as a **reconstructed native WS outcome**, not as securely attested manuscript OE.

## Project problem and solution

The project solved one real problem but still masks another.

1. **Solved problem:** the FST used to output `hierfist`; `DEV_NOTES` §6585 correctly fixed this by adding medial unstressed `i > e`, giving regular native WS `hierfest`.
2. **Remaining row-design problem:** the live TSV still presents `hierfest` as if it were an ordinary attested OE counterpart. The repo’s philological sources do not support that claim. They support `hierfest` as the expected regular WS reconstruction, while the attested lexical tradition is `hærfest/herfest` and is entangled with Anglian borrowing / non-WS transmission.

The cleanest current project reading is therefore:

- keep the derivational solution that the cascade yields `hierfest` from `*xárbistuz`;
- stop calling `hierfest` straightforwardly attested;
- treat the row, if kept as-is, as a **reconstructed native WS target** rather than a plain regular attested row.

That would align this lexeme with the project’s existing reconstructed-WS logic elsewhere better than the current `regular` label does.

## Paradigm probe

A paradigm probe is **not required** for this row.

The dispute is not about hidden paradigm-cell selection; it is about whether the row should represent a reconstructed regular WS citation form (`hierfest`) or the attested OE lexical forms (`hærfest/herfest`). A probe of additional inflectional cells would not resolve that source question.

If the final report wants a compact comparison anyway, it should be presented as a source note rather than a paradigm probe: current derivational target `*xárbistuz -> hierfest` versus attested lexical headword tradition `hærfest/herfest`.

## Recommended final report

Recommend a concise final report that says the cascade now correctly derives **reconstructed native WS** `hierfest` from `*xárbistuz`, but that the attested OE lexical tradition is `hærfest` with variant `herfest`, which Bammesberger and Ringe-Taylor treat as Anglian/non-WS material borrowed into WS. The report should explicitly distinguish reconstructed WS target from attested headword evidence and should not claim unqualified attestation for `hierfest`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no immediate change recommended **if** the project intends this row to stand for reconstructed native WS `hierfest`. If the supervisor instead wants attested lexical OE in column 6, then a later retargeting decision between `hærfest` and `herfest` will be needed; the memo evidence favors treating the current row as reconstructed rather than silently attested.
- **TSV `DERIVATION_CLASS`:** **change recommended** from `regular` to `reconstructed_oe`, because the best-supported reading of current `hierfest` is reconstructed native WS, not ordinary attested OE.
- **TSV `NOTE`:** **change recommended.** Remove the claim “WS hierfest attested (Toller)” or qualify it much more carefully; say instead that `hierfest` is the regular native WS outcome, while attested OE headword evidence is `hærfest/herfest` and is usually interpreted as Anglian/non-WS.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no major change required. `DEV_NOTES` §6585 already makes the crucial distinction better than the TSV note does, though the summary-table treatment of `hierfest` as a canonical fix could be lightly annotated later as “regular WS reconstructed outcome” if the supervisor wants packet generation to surface that nuance more clearly.

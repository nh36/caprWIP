# Research memo — 2310 make (3sg) / macaþ

## Starting point

- ID: 2310
- CONCEPT: make (3sg)
- COUNTERPART: macaþ
- PROTO: *makōną
- PROTOFORM: *mákōθi
- DERIVATION_CLASS: late_analogy
- NOTE: Class II weak 3sg present indicative; current TSV note says `*-ōθi → -aþ`, no `-j-`, and treats `-eþ` forms as dialectal rather than regular.

The starting row already encodes the crucial distinction: the cognate-set headword is the verbal proto `*makōną`, but the project input for this row is the 3sg present cell `*mákōθi`, whose OE target is the inflected form `macaþ`, not the lemma `macian`.

## Packet evidence assessment

Authoritative/current packet material:

- the live TSV row;
- the compact derivation trace in the packet, which now yields `*mákōθi → macaþ`;
- packet excerpts from `DEV_NOTES.md` §15.1 and §15.5ff showing the later correction that weak-II 3sg `*-ōþi` gives `-aþ`, not regular `-eþ`.

Useful background:

- the packet's older `DEV_NOTES.md` excerpts on the class-II-verb problem and on why the project explored imperative/3sg cells at all;
- the packet's diagnostic debugging excerpts showing intermediate outputs like `macoþ` and the chronology problem around late `*ō` shortening.

Stale or superseded:

- the packet excerpt from `DEV_NOTES.md` 2914–2917 claiming regular `*makōθi → maceþ` and analogical `macaþ`; later repo work explicitly reverses this;
- the packet's older debugging expectations where `maceþ` is still treated as the target.

Irrelevant or misleading:

- broad packet keyword hits for unrelated `i-umlaut` dossiers and analyses; they are packet noise, not row-specific evidence for `macaþ`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` around the early class-II exploration, the later correction in §15.1, and the two-stage `*ō`-shortening discussion in §15.5–15.8.
- `Germanic/docs/analysis/arestoration_r_l_research.md`, especially the sections citing Ringe-Taylor, Brunner, and Luick on `macian` and on `a`-restoration before later-fronted class-II endings.
- `Germanic/docs/analysis/notable_findings.md`, which summarizes the same chronological point with `macian` as an example.
- `Germanic/data/old_english_wiktionary.tsv`, which confirms the expected lemma/headword `macian`.
- `Germanic/data/germanic-aligned-final.tsv` rows 2117 (`macian`) and 2309 (`maca`) for the related infinitive and imperative cells.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which shows row 2310 requires a lexeme report and currently has no pilot/full report.
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run against `backend/old_english.bin`.

No row-specific full dossier was named in the TSV note, and no existing pilot/full lexeme report for this lexeme appears in the repo.

## Reconstruction and early-stage forms

The forms need to be kept separate:

- `PROTO` `*makōną` is the cognate-set headword / lexical proto.
- The inherited lemma-level weak-II input relevant to OE `macian` is `*mákōjaną` (seen in row 2117), not this row's `PROTOFORM`.
- `PROTOFORM` `*mákōθi` is the selected 3sg present indicative cell for row 2310.
- The OE target here is the inflected form `macaþ`.

Current repo evidence supports the following chain for the selected cell: `*mákōθi → *makōθ` (early loss of final `-i`) → `*mækōθ` / `*makōθ` in the regular brightening-plus-restoration sequence → late shortening of unstressed `*ō` to `a` in this weak-II ending → `macaþ`. The important point is that this 3sg cell is not the same problem as the infinitive `*mákōjaną → macian`: the lemma row involves the class-II `-ōj-` suffix and the analogical OE `-ian` outcome, while row 2310 uses a different paradigm cell with no need to derive `macian`.

## Old English philology

`macaþ` is an inflected 3sg present indicative form, not a citation lemma. The citation/headword form in repo-local lexical material is `macian`. The row therefore should not be read as claiming that the cognate-set headword `*makōną` directly yields the dictionary form `macaþ`; it claims that a specific inherited present-tense cell yields the OE 3sg form.

The safest philological wording is that `macaþ` is the normalized OE class-II 3sg form supported by the handbook paradigm evidence cited in the TSV note, while `-eþ` spellings belong to dialectal or secondary variation. This memo does not add a manuscript-specific attestation claim beyond what the current note and handbook-based project history support.

## Project problem and solution

The project problem is not that `macaþ` itself is now thought irregular. The problem is that the cognate-set proto / lemma pathway and the OE target row are different kinds of objects:

- cognate-set headword: `*makōną`;
- OE lemma pathway: `*mákōjaną → macian`;
- selected row target: `*mákōθi → macaþ`.

Earlier project history briefly treated `macaþ` as analogical against regular `maceþ`, but the current evidence base rejects that. The present row still belongs in `late_analogy` for project purposes because it is a paradigm-cell row rather than a lemma-to-lemma row: the selected OE counterpart is an inflected 3sg form, and the project intentionally stores that cell in `PROTOFORM`.

## Paradigm probe

A paradigm probe is required for this row class, because the memo needs to show that the winning form comes from a specific paradigm cell rather than from the cognate-set headword or the OE lemma row.

A manual probe was run with `Germanic/tools/oe_paradigm_probe.py` against the current `backend/old_english.bin`:

- infinitive `*mákōjaną → macian` (no match for this row's target);
- imperative 2sg `*mákô → maca` (regular related cell, but not this row's target);
- 3sg present indicative `*mákōθi → macaþ` (unique match).

So a probe is needed, but it is no longer missing in substance. What is still missing is a reusable built-in probe spec for this lexeme. If one is later formalized in `oe_paradigm_probe.py`, it should minimally cover infinitive and 3sg present, and preferably also imperative 2sg plus 2sg present `*mákōsi`.

## Recommended final report

The final report should present row 2310 as a paradigm-cell case: keep `*makōną` as the cognate-set proto, identify `*mákōθi` as the selected 3sg input, explain that `macaþ` is the normalized OE 3sg present form, and explicitly mark the older `maceþ` analysis in `DEV_NOTES` as superseded project history rather than live evidence.

## Data-change recommendations

- TSV `PROTO`: no change recommended.
- TSV `PROTOFORM`: no change recommended.
- TSV `COUNTERPART`: no change recommended.
- TSV `DERIVATION_CLASS`: no change recommended; `late_analogy` still fits the project taxonomy because this is a selected paradigm-cell row.
- TSV `NOTE`: no required philological correction. An optional clarification could mention that the row uses a 3sg cell while the lemma row remains `macian`, but this is not necessary for correctness.
- `oe_known_problems.tsv`: no change recommended; the row is not a current unresolved-model problem.
- `DEV_NOTES` text: change recommended. The earlier class-II exploration passage that still says regular `maceþ` / analogical `macaþ` should be marked as superseded or cross-linked to the later correction, because packet generation currently surfaces that stale history as if it were live evidence.
- dossier text: no change recommended; no row-specific dossier currently needs correction.

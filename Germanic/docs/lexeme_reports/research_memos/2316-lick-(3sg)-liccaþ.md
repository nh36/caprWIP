# Research memo — 2316 lick (3sg) / liccaþ

## Starting point

- ID: 2316
- CONCEPT: lick (3sg)
- COUNTERPART: liccaþ
- PROTO: *likkōną
- PROTOFORM: *líkkōθi
- DERIVATION_CLASS: late_analogy
- NOTE: Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ. No i-umlaut: 3sg ending never had -j-. Root has cc from WGmc gemination.

The live row already encodes the main distinction this memo has to preserve: `*likkōną` is the cognate-set / stem-level proto label for the lick-verb family, `*líkkōθi` is the selected 3sg present indicative input for this row, and `liccaþ` is the OE finite target form. This row is therefore not the same object as the ordinary OE lemma row `2099 lick / liccian`.

## Packet evidence assessment

Authoritative/current packet material:

- the live TSV row itself;
- the packet’s compact derivation trace and the current published trace snapshot, both of which now give `*líkkōθi -> liccaþ`;
- the later `DEV_NOTES.md` correction sequence that explicitly rewrites row 2316 from older `licceþ` expectations to regular `liccaþ`.

Useful background:

- the packet’s older `DEV_NOTES` excerpts on why the project explored weak-II imperative/3sg cells in the first place;
- the packet’s preserved debugging history around geminate `*kk`, because earlier repo work did briefly mis-handle the lick-family stem before the current output was fixed;
- the packet’s note that the stem has `cc` from West Germanic gemination.

Stale or superseded:

- older `DEV_NOTES` passages that still say regular weak-II 3sg should be `licceþ`, especially the early class-II write-up and the later regression table that still lists `*líkkōθi -> licceþ`;
- the older full trace/debug snapshot material where `EXPECTED: licceþ` is still baked in.

Irrelevant or misleading:

- the packet’s long list of generic `i-umlaut` analysis/dossier hits. After auditing the named files, almost all are just keyword noise for this row. Only `analysis/notable_findings.md` has a genuine `*likk-` mention, and even there it is only background on preserved stem `i` before `-kk-`, not row-specific evidence for `liccaþ`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` around the early class-II exploration (`licceþ` stage), the correction at §15.1, and the later debugging around weak-II `-aþ`;
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md`, which now shows `EXPECTED: liccaþ / OUTPUTS: liccaþ`;
- `docs/debug_snapshots/oe_full_trace_report.txt`, which still preserves the older `EXPECTED: licceþ` state and is therefore stale project history;
- `Germanic/data/germanic-aligned-final.tsv` rows 2099 (`liccian`), 2315 (`licca`), and 2316 (`liccaþ`);
- `Germanic/data/old_english_wiktionary.tsv`, which confirms the lemma/headword `liccian`;
- `Germanic/data/oe_known_problems.tsv` (no relevant entry);
- `Germanic/tools/oe_paradigm_probe.py`, plus a manual live-FST probe;
- repo-local reference files: Ringe-Taylor, Campbell, Bosworth-Toller, Kroonen, Orel, and Kluge/Seebold on `liccian` / `*likkōn-`.

I also audited the full analysis/dossier files named in the packet. Result:

- `analysis/notable_findings.md` is mildly relevant as methodological background because it notes that velar geminate `-kk-` blocks the sporadic `*i > e` lowering in the `liccian` family;
- `analysis/mismatch_dossier_mizdo.md`, `dossiers/bugan-scufan-paradigm-cell-review.md`, and `dossiers/widuwe-u-preservation.md` are only general project precedents about paradigm-cell targeting and analogical outcomes;
- the other named analysis/dossier files are irrelevant keyword noise for row 2316 and provide no row-specific evidence.

I found no existing pilot/full lexeme report for this lexeme; the only row-specific materials are the packet, current traces, and the `DEV_NOTES` history.

## Reconstruction and early-stage forms

The three levels must stay separate:

1. `PROTO` `*likkōną` is the cognate-set / etymological proto label for the lick-family as this row currently stores it; repo-local etymological references also support a short `*likkōn-` type for the verb.
2. The ordinary OE lemma row elsewhere in the TSV uses `*líkkōjaną -> liccian`, which is the citation-form comparator, not this row’s `PROTOFORM`.
3. `PROTOFORM` `*líkkōθi` is the selected non-`j` 3sg present indicative input for row 2316.
4. The OE target represented here is the finite form `liccaþ`.

For the selected cell, the current repo evidence supports a regular non-`j` derivation:

`*líkkōθi -> *líkkōθ` (early loss of final `-i`) -> late unstressed `*ō > a` in this weak-II ending -> `*líkkaθ` -> orthographic `liccaþ`.

The important contrast is with the lemma pathway `*líkkōjaną -> liccian`: that comparator belongs to the citation form and the analogically remodeled weak-II infinitive, while row 2316 intentionally models a different paradigm cell. The stem `i` is not a row-level problem here; the only directly relevant background note from repo analysis is that `-kk-` blocks the sporadic `*i > e` lowering that affects some other lexemes.

## Old English philology

`liccaþ` is a finite 3sg present indicative form, not a citation/headword. Repo-local lexical material and dictionaries give `liccian` as the headword form for “lick,” not `liccaþ`.

The safe philological claims supported by the repo are:

- the lick-verb family is real and well represented by lemma `liccian`;
- the stem consonantism `cc` is expected in OE;
- row 2316 is intended to represent the normalized weak-II 3sg form with `-aþ`, not a dictionary lemma.

What the repo does **not** currently give is a row-specific dossier proving direct manuscript attestation of `liccaþ` itself. So the eventual final report should present `liccaþ` as the project’s selected OE 3sg target, but should avoid stronger lexicographical-attestation claims than the current evidence base supports.

## Project problem and solution

The project problem was partly philological and partly historical:

- earlier project history briefly treated weak-II 3sg `*-ōθi` as if regular OE should be `-eþ`, producing older expectations like `licceþ`;
- the lick-family also passed through an earlier root-level debugging stage where geminate `*kk` was mishandled.

Current repo evidence supersedes both problems. The present solution is:

- keep the lick family distinct from the ordinary lemma row `liccian`;
- use `*líkkōθi` as the row-specific 3sg input;
- derive regular `liccaþ` with no `j`-triggered umlaut in this singular ending;
- treat the older `licceþ` material as stale project history, not live evidence.

`late_analogy` still makes sense operationally, because this row is a selected paradigm-cell companion to the ordinary lexeme row rather than a lemma-to-lemma entry, even though the chosen 3sg phonology is now regular once the right cell is selected.

## Paradigm probe

Yes — a paradigm probe is required, because this is a paradigm-cell row and the memo needs to show that the winning OE form comes from the selected 3sg cell rather than from the citation-form lexeme row.

A manual live-FST probe already gives a clean unique winner:

- infinitive `*líkkōjaną -> liccian`
- imperative 2sg `*líkkô -> licca`
- 3sg present indicative `*líkkōθi -> liccaþ`
- 2sg present indicative `*líkkōsi -> +?`

So the substantive probe result is already clear: `*líkkōθi` uniquely matches row 2316. However, the repo still lacks a built-in saved probe spec for this lexeme in `oe_paradigm_probe.py`. If one is added, it should at minimum probe:

- citation-form infinitive comparator `*líkkōjaną`
- imperative 2sg `*líkkô`
- 3sg present indicative `*líkkōθi`
- 2sg present indicative `*líkkōsi`

## Recommended final report

Recommend a short final report that treats row 2316 as a paradigm-cell case: distinguish cognate-set `*likkōną`, row-specific input `*líkkōθi`, and OE target `liccaþ`; note that the lemma comparator is `liccian`; and explicitly mark older `licceþ` expectations as superseded project history only.

## Data-change recommendations

- TSV `PROTO`: no change recommended. `*likkōną` is defensible for this row as the cognate-set / stem-level proto label, even though the ordinary lemma comparator elsewhere in the TSV is `*líkkōjaną`.
- TSV `PROTOFORM`: no change recommended.
- TSV `COUNTERPART`: no change recommended.
- TSV `DERIVATION_CLASS`: no change recommended.
- TSV `NOTE`: minor change recommended. The current note is basically right, but one extra sentence clarifying that this is a selected 3sg paradigm-cell row paired with lemma `liccian` would make the row’s purpose clearer.
- `oe_known_problems.tsv`: no change recommended.
- `DEV_NOTES` text: change recommended. Older passages that still present `licceþ` as the expected weak-II 3sg outcome should be marked as superseded or explicitly cross-linked to the later correction sequence.
- dossier text: no change recommended. The packet-named dossier/analysis files are not row-specific evidence and do not need lick-specific textual revision.

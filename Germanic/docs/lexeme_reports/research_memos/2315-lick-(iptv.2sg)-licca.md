# Research memo — 2315 lick (iptv.2sg) / licca

## Starting point

- **ID:** 2315
- **CONCEPT:** `lick (iptv.2sg)`
- **COUNTERPART:** `licca`
- **PROTO:** `*likkōną`
- **PROTOFORM:** `*líkkô`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** `Class II weak iptv. 2sg test. Trimoric *ō → OE -a.`

This row is not the ordinary OE lexeme row for “lick.” The live TSV already has row 2099 `lick / liccian` with lexeme-level `PROTO` `*líkkōjaną`; row 2315 is a selected finite paradigm-cell companion whose OE target is the imperative singular `licca`.

## Packet evidence assessment

**Authoritative/current**

- the live TSV row itself;
- the packet’s compact derivation trace, which now shows `*líkkô -> licca`;
- the current debug snapshot state behind that trace, which also shows the related lemma row `*líkkōjaną -> liccian` and neighboring 3sg row `*líkkōθi -> liccaþ`.

**Useful background**

- the packet’s `DEV_NOTES.md` excerpts on the earlier spurious-palatalization bug, because they preserve why this lexeme family was being watched;
- the packet’s regression-era `DEV_NOTES` table showing how `lick`, `lick (iptv.2sg)`, and `lick (3sg)` behaved during the i-lowering experiments.

**Stale or superseded**

- the packet excerpts at `DEV_NOTES.md` 2958 / 2981ff. and 5417ff. are no longer current evidence for the live row: they record earlier stages where the system produced `liċca` or `lecca`, not the current `licca`;
- the linked 3sg diagnostics in the same packet material (`licceþ` vs. `liccaþ`) are likewise historical debugging evidence, not the present implementation state.

**Irrelevant or misleading**

- the lack of a lexical-table hit for inflected `licca` is not evidence against the row; repo lexical tables are lemma-oriented and list `liccian`;
- the packet has no row-specific dossier/analysis hit, but that absence should not be overread as philological evidence either way.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` rows 2099, 2315, and 2316;
- `Germanic/data/old_english_wiktionary.tsv`;
- `Germanic/data/oe_known_problems.tsv`;
- `Germanic/docs/DEV_NOTES.md` around the old palatalization/regression discussions and the later weak-II cleanup tables;
- `Germanic/docs/analysis/notable_findings.md`;
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md`;
- `Germanic/tools/oe_paradigm_probe.py`, plus a live manual probe against `backend/old_english.bin`;
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`;
- `docs/references/campbell_old_english_grammar.txt`;
- `docs/references/brunner_1965_altenglische_grammatik.txt`;
- `docs/references/legacy/orel_handbook_germanic_etymology.txt`.

Main findings from that wider check:

- row 2099 confirms that the lemma/headword side of the lexeme is already modeled separately as `*líkkōjaną -> liccian`;
- `old_english_wiktionary.tsv` also gives only `liccian`, reinforcing that row 2315 is a finite-cell row, not a dictionary-headword row;
- current debug snapshots show `*líkkōjaną -> liccian`, `*líkkô -> licca`, and `*líkkōθi -> liccaþ`, so the packet’s old `liċca`/`lecca` material is diagnostic history only;
- `oe_known_problems.tsv` has no entry for this lexeme family;
- Ringe-Taylor lists the weak verb as PWGmc `*li/ekkōn > OE liccian`, while Orel gives a full infinitive-style reconstruction `*likkōjanan`; either way, the comparative headword belongs with the `liccian` lexeme row, not with the inflected imperative target [@RingeTaylor2014];
- Campbell’s weak-II summary says the imperative is the bare `*-ō` stem and that late-shortened `ō` gives OE `a`, which matches the project’s use of `*líkkô -> licca` [@Campbell1959].

I found no row-specific dossier file and no existing pilot/full lexeme report for this lexeme.

## Reconstruction and early-stage forms

This row needs the same three-way distinction as the other weak-II paradigm-cell memos:

1. **Cognate-set proto / lexeme-level headword:** repo-local comparative materials and row 2099 point to the weak verb “lick” as `*líkkōjaną` (or stem-level `*likkōn-` in handbook shorthand), i.e. the source of OE `liccian`.
2. **Project input form for row 2315:** `PROTOFORM` `*líkkô`, the imperative singular cell.
3. **OE target represented by the row:** `licca`, the selected imperative singular outcome.

For the row itself, the live derivation is simple:

`*líkkô -> *líkka -> licca`

The crucial early-stage points are:

- the root remains `likk-`, not an e-grade workaround;
- geminate `*kk` stays non-palatalized in the current output, giving `cc`, not `ċċ`;
- late shortening of trimoric `*ō` yields final `-a`, exactly the row note’s project rationale [@Campbell1959].

The live TSV `PROTO` `*likkōną` is therefore best read as a project stem abstraction for the finite weak-II row, not as the clearest lexeme-level cognate-set proto. The lexeme-level comparator in the repo is still `*líkkōjaną`.

## Old English philology

`licca` should be treated as an **imperative 2sg / selected finite form**, not as the lemma for “lick.” The repo-local lexical evidence supports `liccian` as the headword; I did not find a row-specific dossier giving manuscript-level documentation for imperative `licca`.

So the cautious philological position is:

- **headword / citation form:** `liccian`;
- **selected finite cell here:** `licca`;
- **related finite comparator:** `liccaþ` in row 2316.

The memo should also preserve that `licc-` is philologically expected. Campbell and Brunner both cite `liccian` with geminate `cc`, and the current repo analysis explicitly treats dorsal geminate `*kk` as blocking the lowering/palatalization pathway that once produced diagnostic `liċca`/`lecca` states [@Campbell1959].

I found no secure repo-local basis for a stronger manuscript or dialect claim about the imperative form specifically, so the eventual final report should avoid overclaiming direct attestation.

## Project problem and solution

The main project problem was not the existence of `licca` itself, but the interaction between paradigm-cell modeling and earlier implementation bugs:

- the repo already had the ordinary lexeme row `*líkkōjaną -> liccian`;
- row 2315 was added to represent a regular weak-II imperative cell with trimoric `*ō`;
- older implementation stages misgenerated this family as `liċca` or `lecca`, mainly because of spurious palatalization / i-lowering interactions around geminate `*kk`.

The current solution is now coherent:

- keep the lexeme row `lick / liccian` for the headword pathway;
- keep row 2315 as the finite imperative companion with `PROTOFORM` `*líkkô`;
- treat the older `liċca` / `lecca` stages as superseded debugging history, not as live evidence;
- read `late_analogy` here as a paradigm-cell flag within the project workflow, not as evidence that the current `licca` output is still a live phonological problem.

What remains slightly muddy is the row’s `PROTO` field, which still looks more like a stem abstraction than the lexeme-level cognate-set proto.

## Paradigm probe

**Yes — a paradigm probe is required.** This is a paradigm-cell row, and the important question is whether the target comes uniquely from the selected imperative cell rather than from the lexeme headword or a neighboring finite form.

A live manual probe against `backend/old_english.bin` already gives the decisive contrast:

- infinitive comparator `*líkkōjaną -> liccian`
- imperative 2sg `*líkkô -> licca`
- present 3sg comparator `*líkkōθi -> liccaþ`

So the substantive probe result is already clear: `*líkkô` is the unique winner for target `licca`.

However, the repo still has **no built-in saved probe spec** for `lick / licca`. If that missing built-in probe is added, it should minimally cover:

- **infinitive / lemma comparator:** `*líkkōjaną -> liccian`
- **imperative 2sg:** `*líkkô -> licca`
- **present 3sg comparator:** `*líkkōθi -> liccaþ`

Optional expansion: add a present 2sg weak-II comparator once the project settles the preferred probe template for that cell.

## Recommended final report

Recommend a concise final report that presents row 2315 as an imperative-cell companion to `lick / liccian`: distinguish lexeme-level `*líkkōjaną`, row-level `PROTOFORM` `*líkkô`, and OE target `licca`; note that earlier `liċca`/`lecca` material in `DEV_NOTES` is superseded debugging history; and avoid claiming more direct attestation for the imperative than the current repo sources support.

## Data-change recommendations

- **TSV `PROTO`: change recommended.** The current `*likkōną` obscures the distinction between cognate-set proto and row-level cell input. For clarity and consistency with row 2099, this row should use lexeme-level `*líkkōjaną` in `PROTO`, leaving `PROTOFORM` to carry the imperative-cell choice.
- **TSV `PROTOFORM`: no change recommended.** `*líkkô` is the right project input for the selected imperative singular cell.
- **TSV `COUNTERPART`: no change recommended.** `licca` is the intended OE target and matches the live derivation.
- **TSV `DERIVATION_CLASS`: no change recommended.** `late_analogy` still works as the project’s marker for a non-lemma paradigm-cell row.
- **TSV `NOTE`: change recommended (minor clarification).** The current note should say more explicitly that this is a paradigm-cell companion to lemma `liccian`, not the citation form, and that the row is testing the weak-II imperative `*-ō > -a` pathway.
- **`oe_known_problems.tsv`: no change recommended.** This is not a current unresolved-model row.
- **`DEV_NOTES` text: change recommended.** The older `liċca` / `lecca` regression sections should be marked more explicitly as superseded or cross-linked to the current fixed state, because packet generation can still surface them as if they were live evidence.
- **dossier text: no change recommended.** I found no row-specific dossier text that currently needs cleanup.

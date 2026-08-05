# SC004 / SC014 component chronology cards (corrected PROTOFORM pass)

> **Corrected.** An earlier version of this card (from the pre-correction pass)
> read the components off the cognate-set `PROTO` field and concluded that
> Component A (`*ai > *ē`) had zero corpus applications and that `loam`/`whine`
> were unaccented `*ai > *ā` cases. The production input is the Old-English-row
> `PROTOFORM`; under it the components are re-attributed as below. Empirical
> basis: `sc004_component_application_report.tsv`,
> `sc004_sc014_interaction_report.md`, and the first-break summaries
> `summaries/sc004corr_first_break_sc004.tsv` and `..._sc014.tsv`.

The two production rules are now the historically cleaner pair:

* **SC014** `PNWGmcUnstressedAiMonophthongization` : `{*ai} -> {*ē}` (unstressed
  `*ai`, final AND nonfinal; Ringe-Taylor's rule), at cascade pos 1.
* **SC004** `EAFAiMonophthongization` : `{*ái} -> {*ā}` (stressed/root `*ái`), at
  cascade pos 25.

---

## Card: SC014 unstressed `*ai > *ē`

Rewrite: `{*ai} -> {*ē}` (final and nonfinal unstressed `*ai`).

- **Corpus applications:** `2`. By PROTOFORM: `span` (`*spánnai`, fem. o-stem
  dat.sg → OE `spanne`) and `meed` (`*mízdai`, dat.sg → OE `meorde`). Both are
  unstressed word-final `*-ai` endings; the NOTE fields cite Ringe-Taylor
  §6.1.5 / Brunner §252. The rule is **not** corpus-inert (the pre-correction
  card's claim of zero applications was a PROTO-field artefact).
- **Lexical witnesses:** `span`, `meed`.
- **Handbook support for the nonfinal environment:** Ringe-Taylor's rule covers
  nonfinal unstressed `*ai` too (e.g. `*berain > *berēn`, `*habaisi > *habēs`,
  `*gōdaimaz > *gōdēmaz`); the Foma probes confirm SC014 monophthongizes those
  (see `sc004_component_behaviors.tsv`). No corpus lexeme instantiates a nonfinal
  unstressed `*ai`, so the nonfinal environment is corpus-inert while the
  final one carries the two witnesses.
- **Earlier boundary:** none — SC014 executes at the cascade head (pos 1).
- **Later boundary:** order `69`, crossing **SC072 OE Unstressed Long Vowel
  Shortening**. First-break testing confirms that delaying SC014 past SC072
  leaves the `*-ē` (from `*-ai`) unshortened, so `span` surfaces as `spannē`
  instead of `spanne` and `meed` as `meordē` instead of `meorde` (370/372 match
  at the break; `sc004corr_first_break_sc014.tsv`). Both corpus witnesses break
  at exactly this stage.
- **Interpretation:** SC014 is a real, corpus-active early PNWGmc change with an
  interpretable later boundary at the unstressed-long-vowel shortening (SC072);
  its historical stage (early PNWGmc, `*ē` merging with long mid `*ē`) rests on
  both the two corpus endings and the comparative record.

---

## Card: SC004 stressed `*ái > *ā`

Rewrite: `{*ái} -> {*ā}` (stressed/root `*ái`).

- **Corpus applications:** `24` — every stressed-`*ái` corpus witness (23 attested
  + `roe` `*ráixōn`, unattested). Includes `loam` (`*láimą`, stressed by its
  PROTOFORM, previously misfiled as unaccented).
- **Lexical witness (later boundary):** `soul` `*sáiwalō`.
- **Earlier boundary:** none found toward the head (boundary-limited); SC004's
  formal earlier non-commutations (`PNWGmcILowering`, `PNWGmcULowering`) are
  feeding artefacts on non-corpus `EnglishProtoInput` forms only.
- **Later boundary:** order `33`, crossing **SC036 OE Inter Stress Raising**.
  First-break testing with the corrected stressed-only rule confirms that
  delaying SC004 past SC036 makes `*sáiwalō` yield `sāwel` instead of `sāwol`
  (371/372 match at the break; `sc004corr_first_break_sc004.tsv`). This is a
  genuine lexical failure, hence historical evidence.
- **Interpretation:** SC004 carries the stressed monophthongization and its one
  real boundary (SC036), consistent with a later North-Sea-Germanic / EAF
  placement. Its stressed target `*ái` is disjoint from SC014's unstressed `*ai`,
  so the two rules are independent.

---

## Summary

1. **SC014 corpus load:** 2 (span, meed) — corrected from the pre-correction
   "zero." SC014 is corpus-active and has a later boundary at unstressed-long-
   vowel shortening.
2. **SC004 corpus load:** 24 stressed (23 attested + roe); `loam` is stressed;
   `whine`/`withy` are not ai cases.
3. **SC036 soul boundary:** carried by SC004 (stressed), reproduced with the
   corrected rule; not by SC014.
4. **Separability:** the split is behaviour-neutral on the corpus (frozen
   `outputs_sha256` `aaf19ba9…480e`); the components' only genuine historical
   dependencies are SC014 < unstressed-long-vowel shortening and SC004 < SC036.

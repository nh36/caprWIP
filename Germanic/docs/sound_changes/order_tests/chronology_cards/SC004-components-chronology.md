# SC004 component chronology cards (research)

Research only. The existing `SC004-pwgmc-ai-monophthongization.md` chronology card
covers the **bundled** rule and cannot decide whether the components belong to
different stages. These per-component cards separate them. Empirical basis: the
deterministic application report (`sc004_component_application_report.tsv`) and the
proven behaviour-neutral split (`sc004_split_candidate_and_proof.md`).

---

## Card: SC004.final-ai-to-e  (Component A)

Rewrite: `{*ai} -> {*ē} || _ .#.`  (word-final unstressed `*ai`)

- **Corpus applications:** `0`. No Old English corpus lexeme carries word-final
  unstressed `*-ai`; A's historical witnesses are inflectional endings (dat.sg
  `*-ai`, subjunctive `*-ai`, strong-adj pl `*-ai`) not present as standalone
  lexemes.
- **Lexical witnesses:** none in the corpus.
- **Earlier boundary:** none — no witness can be crossed.
- **Later boundary:** none — no witness can be crossed.
- **Safe computational window:** unconstrained by any corpus output. Because A
  fires on zero corpus lexemes, moving it to any position leaves every corpus
  output unchanged; it has **no positive chronology boundary of any kind**.
- **Downstream dependency creators:** none (no corpus feed).
- **Historical placement:** early — (P)NWGmc, outcome `*ē` merging with long mid
  `*ē` [@RingeTaylor2014, pp. 40--41; @Fulk2018, §5.2; Versloot 2017 verify].
- **Interpretation:** A is chronologically **inert on the CAPR corpus**. Its
  correct historical stage (early PNWGmc) is a fact about the endings it targets,
  established by comparison, not by any CAPR derivational witness. Its cascade
  position is therefore free and cannot be constrained (or justified) by
  first-break testing.

---

## Card: SC004.general-ai-to-a  (Components B + C)

Rewrite: `[{*ai} -> {*ā}] .o. [{*ái} -> {*ā}]`  (`*ai`/`*ái` elsewhere → `*ā`)

- **Corpus applications:** `26` — all SC004 corpus witnesses. C (stressed) 24;
  B (unstressed nonfinal) 2 (loam, whine, both `early_analogy`).
- **Lexical witnesses (later boundary):** `soul` `*sáiwalō` (Component C).
- **Earlier boundary:** none found before the left edge of the tested
  expanded-PWGmc chain (order 4) — **boundary-only**, not a positive historical
  constraint (inherited from the bundled card; the general component carries the
  witnesses that card tested).
- **Later boundary:** order `36`, crossing **SC036 OE Inter Stress Raising**.
  Delaying the general component past SC036 makes `*sáiwalō` yield `sāwel`
  instead of `sāwol`. This is a genuine lexical failure (not mere
  non-commutation), hence historical evidence.
- **Safe computational window:** `4–35` (earlier boundary-only; later broad/far
  across SC036).
- **Downstream dependency creator:** SC036 OE Inter Stress Raising (consumes the
  `*ā` output of the *soul* derivation).
- **Historical placement:** later than A — North Sea Germanic / Anglo-Frisian
  `*ai > *ā` (OE `ā`, front `ǣ` by later fronting) [@Campbell1959; @Hogg1992;
  Versloot 2017 verify: areal, wave-diffused].
- **Interpretation:** the general component carries the entire empirical
  chronology of SC004. Its one real boundary (SC036) is historically consistent
  with a later, North-Sea-Germanic placement.

---

## Summary — the five §7 questions

1. **Does the final component (A) have any positive chronology boundary?** No. A
   applies to 0 corpus lexemes, so no earlier or later break exists; its stage is
   fixed only by external (ending) comparison, not by CAPR derivation.
2. **Does the general component alone produce the SC036 `soul` failure?** Yes.
   `soul` is a Component C application; the general component (B+C) alone yields
   `*sāwalō` and reproduces the SC036 boundary. A plays no part.
3. **Can the two components be separated computationally without changing
   outputs?** Yes — proven behaviour-neutral (`test equivalent` TRUE, unrestricted
   and over `EnglishProtoInput`; `sc004_split_candidate_and_proof.md`).
4. **Can either component be placed in a historically preferable position?**
   - A: already effectively early; being inert, it can sit at its historically
     preferable early (PNWGmc) position with zero output effect.
   - General (B+C): historically *later* than its current bundle position 1;
     it can move later (safe through order 35) toward a more historically accurate
     North-Sea-Germanic / EAF position without changing any output.
5. **Does any historically preferable movement conflict with a technical FST
   dependency?** No. The general component's only computational boundary is
   SC036, which is itself an Old English change *later* than the Anglo-Frisian
   `*ai > *ā`; the historically preferable (later) placement is therefore
   **bounded above by, and consistent with**, the FST dependency — not blocked by
   it. A has no dependency at all.

Non-commutation caveat (task §7): the SC036 boundary is retained here because it
is a real lexical derivational failure (`soul`), not merely a non-commuting pair.

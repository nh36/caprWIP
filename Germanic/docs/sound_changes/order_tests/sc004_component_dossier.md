# SC004 component dossier — inventory and application

Research-only. This dossier decomposes the production rule
`PWGmcAiMonophthongization` (SC004) into its component rewrites and reports every
corpus application, as the basis for the retain/split/remodel decision. It does
**not** modify the production rule. Provisional research identifiers only:

```
SC004.final-ai-to-e     A   {*ai} -> {*ē} || _ .#.     word-final unstressed *ai
SC004.general-ai-to-a   B+C [{*ai} -> {*ā}] .o. [{*ái} -> {*ā}]   *ai / *ái elsewhere
   B  (unstressed sub-tier)  {*ai} -> {*ā}
   C  (stressed sub-tier)    {*ái} -> {*ā}
```

## Existing CAPR research

- **Reader chapter** (`reader_facing/004-…md`): "historical support is strongest
  for unstressed `*ai`, especially word-finally"; the nonfinal `*ai > *ā` is "a
  generalization stated more sharply than in the current handbook discussion."
  The *soul* form fixes the relation to interstress raising (SC036).
- **Change report / literature dossier**: word-final `*ai > *ē` maps directly onto
  R/T pp.40–41 and Fulk §5.2 (unstressed `*ai` monophthongization, a shared
  NWGmc innovation illustrated by inflectional endings dat.sg `*-ai`, subjunctive
  `*-ai`, strong-adjective pl `*-ai`); the wider `*ai > *ā` side is "more explicit
  in the implementation than in the currently assembled handbook prose."
- **Chronology card**: `safe window 4–35`; earlier side boundary-only (SC004 is
  first in the tested expanded-PWGmc chain); one later break at **SC036** OE Inter
  Stress Raising (`*sáiwalō` → `sāwol`, else `sāwel`), broad/far not local.
- **Audit table**: `granularity_status = definitely_conflated`,
  `required_action = split_rule`, `proposed_hist_stage = pnwgmc (word-final *e
  component) / uncertain (nonfinal *a generalization)`,
  `proposed_hist_scope = pan_nwgmc (word-final) / uncertain (nonfinal)`,
  confidence B. Registry currently labels the whole rule
  `hist_stage = pnwgmc_pwgmc_transition`, `hist_scope = pan_wgmc`.

## Already established (this dossier's deterministic application report)

Source: `tools/sc004_component_report.py` →
`order_tests/sc004_component_application_report.tsv` (flookup over the corpus,
run in-container). Candidate set: **26** Old English corpus lexemes whose proto
carries `*ai`/`*ái`. Each lexeme is affected by **exactly one** component (no
lexeme takes two):

| Component | Rewrite | Corpus applications |
| --- | --- | --- |
| A `final-ai-to-e` | `{*ai} -> {*ē} \|\| _ .#.` | **0** |
| B `general-ai-to-a` (unstressed) | `{*ai} -> {*ā}` | **2** — loam `*laimōn`, whine `*wainōjaną` |
| C `general-ai-to-a` (stressed) | `{*ái} -> {*ā}` | **24** — bone, deal, dough, flesh, ghost, heal, heath, home, last, lead, loath, mean, one, roe, rope, sea, sheath, snow, **soul**, spread, stone, toe, token, withy |

Answers to the enumerated questions (task §4):

1. The `bone / deal / dough / flesh / ghost` examples are all **Component C**
   (stressed `*ái > *ā`); *soul* is likewise Component C.
2. **21 further affected words** beyond the five examples: the remaining 19 C
   lexemes above plus the 2 B lexemes (loam, whine). The prose's five examples
   are not the full application set.
3. **No** lexeme is affected by more than one component (each is A xor B xor C;
   here only B or C fire on lexemes).
4. **Component A has zero independent corpus applications.** No corpus lexeme has
   word-final unstressed `*-ai`; A's historical support rests entirely on
   inflectional endings (dat.sg `*-ai`, subjunctive `*-ai`, strong-adj pl `*-ai`)
   that are not present as standalone lexemes in the corpus.
5. The **soul** boundary at SC036 is produced by **Component C** (stressed
   `*sáiwalō → *sāwalō`, feeding the `sāwol` derivation). B and A play no part in it.

Necessity: for all 26 affected lexemes the applied component is **necessary** for
the correct Old English output — Old English has no `*ai`/`*ái`; leaving the
diphthong unmonophthongised strands the wrong nucleus (e.g. without C, `*stáinaz`
would not reach `stān`). The `*ā` output is consumed downstream by the
front/back A-developments (Anglo-Frisian brightening `*ā > *ǣ` for the
front-fronting set such as `dǣl`, `hǣþ`; A-restoration / retention for the back
set such as `bān`, `stān`). Component A's `*ē` output would feed the long-mid
`*ē` line, but has no lexical instance here.

## Contradictions among CAPR layers

1. **Outcome mismatch, single rule.** A yields `*ē`; B and C yield `*ā`. One Foma
   `define` currently packages two *different* mergers (`*ai → *ē` vs `*ai → *ā`)
   under one SC number and one `hist_stage`.
2. **Support vs load inversion.** The best-attested component (A, word-final
   `*ai > *ē`, explicit in R/T/Fulk) carries **0** corpus lexemes; the
   "generalization stated more sharply than the handbooks" (B+C, `*ai/*ái > *ā`)
   carries **all 26**. Source strength and empirical load point in opposite
   directions.
3. **Stage label.** The registry files the whole rule as
   `pnwgmc_pwgmc_transition` / `pan_wgmc`, but the audit table already proposes
   `pnwgmc` for the word-final `*ē` component and *uncertain* for the `*ā`
   generalization — the single label cannot be simultaneously correct.
4. **B vs C are not two changes.** B (unstressed) and C (stressed) produce the
   *same* outcome `*ā` and differ only by the stress accent carried on the input
   segment (`*ai` vs `*ái`); they are two stress-tier rewrites of **one**
   development, split only because the FST marks stress on the vowel.

## Open questions (for the source pass, §5)

1. Is word-final `*-ai > *-ē` (A) chronologically and genealogically the **same**
   event as nonfinal `*ai/*ái > *ā` (B+C), or an earlier / separately-shared one?
2. Is the `*ai > *ā` merger (B+C) a Proto-West-Germanic / Anglo-Frisian
   inheritance, or a later, geographically diffused development that CAPR must
   still assign a modelling stage?
3. Does the stressed/unstressed split (C vs B) reflect any real chronological or
   dialectal difference, or purely the FST's stress marking?
4. Does English/Frisian sharing `*ai > ā` prove an inherited Proto-Anglo-Frisian
   innovation, or convergence in a dialect continuum?

## Additional source research required

R/T; Fulk; Hogg; Campbell; Luick; Sievers–Brunner; **Versloot 2017** ("Proto-
Germanic *ai in North and West Germanic"); runic evidence for English/Frisian
`*ai > ā`. Recorded, per component/environment, in the source reconciliation
dossier (§5 deliverable). This inventory does not itself settle the historical
question; it establishes that any split is **A vs (B+C)**, not A vs B vs C.

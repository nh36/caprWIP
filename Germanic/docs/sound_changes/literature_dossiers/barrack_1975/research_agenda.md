# Barrack integration: next research agenda (post-SC087)

Status: prepared 2026-10, immediately after the SC087 adjudication
(`audits/sc087-adjudication.md`, verdict RETAIN). Ranked by evidence
strength and likely scientific payoff against the complete 231-row
reverse index (`barrack_to_capr.tsv`). Nothing below is authorised to
start without a separate assignment; each item names the SCs whose
adjudication protocol run it would feed.

Accounting at preparation time: reverse index 231/231 dispositioned
(2 ADJUDICATED_SC087_RETAIN, 144 NO_ACTION, 4 NO_ACTION_CITED,
3 CHAPTER_DISCUSSION, 22 RESEARCH_QUEUE, 56 VERIFY_SOURCE); citation
ledger 97/97 dispositioned (12 CITED_OK, 23 CITE_WARRANTED,
32 CHAPTER_LEVEL, 24 NO_CITATION_NEEDED, 6 DEFER_TO_ADJUDICATION).

## Ranked queue

### 1. Late consonant-cluster complex: SC065–SC068, SC080 (with SC087 residue)

- **Historical question:** are CAPR's late syncope, degemination and
  cluster-simplification laws (spindle, lung, þirda families) correctly
  conditioned and ordered against each other, and do Barrack's
  unaccented-vowel and cluster rules describe the same events or a
  competing decomposition?
- **Barrack rules:** 476 (p. 122; cluster simplification in the
  bærnan derivation and þirda), 475b (p. 122; r-deletion in rn(C)#
  clusters — reading still needs original verification), 468a, 481.7,
  484a/b/d (currently UNRESOLVED), plus the 459.1 PES (C) early free
  variation before d (þirda, p. 116).
- **CAPR treatment:** SC065–SC068 and SC080 are live; the registry
  records reciprocal chronology RG16 (SC066/SC068) and RG20
  (SC079/SC080). SC067, SC068 and SC080 are DEFER_TO_ADJUDICATION in the
  citation ledger.
- **Source disagreements:** Barrack decomposes the cluster developments
  into more, smaller ordered rules than Campbell/Hogg; Hogg treats much
  of the rn/rnn material under syncope plus analogical levelling.
- **Diagnostic lexemes:** spinl, lungen, þirda/þridda, bærnan-family
  cluster outputs, iron (īsern/īren), -ern compounds.
- **Required tests:** per-SC `--prepare`/`--evidence`; counterfactual
  reorderings inside the cluster block; witness additions only if a
  cluster change is currently unwitnessed.
- **Payoff:** high — several adjacent SCs, two frozen reciprocal edges,
  and five unresolved Barrack headings would be settled together.

### 2. Early-vowel discrepancies: SC005, SC015, SC017 (and SC076)

- **Historical question:** does CAPR's account of final/unstressed
  vowel developments from PGmc into NWGmc (nasalized *ą, *ō(n), high-
  vowel lowering) survive confrontation with Barrack's alternative
  staging, including his *om → um treatment?
- **Barrack rules:** 331.6a (p. 81; *om → um — census corrected this
  cycle), 331.6b (p. 81), 331.4a (p. 77; misprint corrected), 114 (p. 41),
  115/117 (p. 42), 123 (p. 45; ēm → īm raising belongs to 117),
  320 (pp. 75–76)/333b (p. 83; SC036 alternatives).
- **CAPR treatment:** SC005 adjudication history exists; SC015/SC017
  have completed adjudications (wether input, rust input) — reopening
  requires the new-evidence bar of the protocol, which Barrack's
  alternative staging may or may not meet.
- **Source disagreements:** Barrack's feature-matrix staging of
  unstressed vowel reduction differs from Ringe–Taylor's; his *om → um
  is framed as NWG where CAPR places the corresponding development
  differently.
- **Diagnostic lexemes:** dative plurals in -um, *sebun/*nigun family,
  wether, rust, final -ō(n) nouns.
- **Required tests:** source verification first (several VERIFY_SOURCE
  rows), then targeted `--evidence` runs; no reopening without a
  concrete discrepancy witness.
- **Payoff:** medium-high — three SC families and the largest block of
  VERIFY_SOURCE rows; but two completed adjudications raise the bar.

### 3. z-loss, rhotacism and the mēd/meord variation: SC003, SC020, SC096, SC097

- **Historical question:** does CAPR correctly separate final *-z loss
  from medial rhotacism, and is the mēd~meord doublet evidence for a
  distinct conditioning or chronology (Barrack's 404b/404c complex)?
- **Barrack rules:** 404b (pp. 101–02; vowel + sonorant development —
  census corrected this cycle), 404c (p. 102; final R-loss),
  404e (p. 102; rhotacism), 400z (pp. 100–101),
  406 (p. 104), 409 (p. 106; neighbouring rules re-verified in the QC pass).
- **CAPR treatment:** SC020 was SPLIT in an earlier adjudication;
  SC003 carries rhotacism; SC096/SC097 are distinct final-z-loss operations.
- **Source disagreements:** the corrected census shows Barrack's 404b is
  not a change producing m; his ordering of z-loss against apocope
  differs from Ringe's.
- **Diagnostic lexemes:** mēd~meord, lamb/lǭmb forms, r-stem plurals,
  -es genitives vs -as plurals.
- **Required tests:** `--evidence` for SC003/SC020/SC096/SC097; counterfactual
  swap of z-loss and apocope; mēd/meord would need a witness row with an
  independently reconstructed input before any law work.
- **Payoff:** medium-high — a real doublet with competing published
  accounts; bounded scope.

### 4. Back mutation and SC039/SC059 interaction

- **Historical question:** is CAPR's back mutation correctly restricted
  and ordered against velar umlaut and breaking, given Barrack's rules
  210/212/220 which condition differently?
- **Barrack rules:** 210 (pp. 63–64), 212 (p. 64), 220 (pp. 65–66).
- **CAPR treatment:** SC039 and SC059 live; ledger holds SC039/SC059
  chapter-level citation items.
- **Source disagreements:** Campbell's dialect-graded back mutation
  (restricted in WS, general in Mercian) vs Barrack's single staged
  account.
- **Diagnostic lexemes:** seofon, heofon, eofor, medu/meodu, sidu/siodu.
- **Required tests:** firing census of SC039/SC059; dialect-variant
  controls kept out of the executable WS target.
- **Payoff:** medium — conditioning precision, limited corpus effect.

### 5. Late West Saxon sk ~ ks and sibilant-cluster variation (440b, 460b)

- **Historical question:** is the áscian~ácsian (sk > ks) development,
  or the separate sibilant-cluster phenomenon at 460b, a sound law in any
  variety CAPR models, or late variable metathesis of the wasp-row kind?
- **Barrack rules:** 440b (p. 113), 460b (p. 118). Barrack discusses
  cyrps under 459.1 (pp. 115–117); that r-metathesis derivation is not
  itself the separate consonant-order change formulated at 460b.
- **CAPR treatment:** none executable; wasp row 2273 documents the
  deliberate non-implementation precedent. Attested alternative orders
  require a historically delimited explanation, not optional rewrites.
- **Source disagreements:** Campbell §440 treats áscian/ácsian as
  dialectal/orthographic variation; Hogg likewise; Barrack writes a
  rule.
- **Diagnostic lexemes:** áscian~ácsian, fisc~fix spellings, wæps~wæsp.
- **Required tests:** lexical and attestation survey first; establish
  phonological, chronological and dialectal domains before deciding
  whether an executable law is justified.
- **Payoff:** medium — distinguishes documentation of byforms from a
  justified categorical operation.

### 6. Burn-family residue: Anglian metathesis, rounding after labial (300b)

- **Historical question:** the SC087 memo's residue — the Anglian
  pre-breaking metathesis of the burn/run family and Barrack's i → y
  rounding after labials (byrnan, cyrps) — can these be documented
  (prose/dossier) without an executable WS law?
- **Barrack rules:** 459.1 discussion III A–E (pp. 116–17), 300b
  (pp. 72–73).
- **CAPR treatment:** none; outside the WS executable target by the
  SC087 verdict.
- **Diagnostic lexemes:** beornan/biernan/byrnan, iernan/iornan, cyrps.
- **Required tests:** none executable unless an Anglian branch is ever
  added; chapter-level discussion candidate.
- **Payoff:** low-medium — documentation completeness.

### 7. Remaining source hygiene (standing tasks)

- Verify the 56 VERIFY_SOURCE reverse-index rows against page images
  (largest block: the unresolved headings 122b–484d).
- Work through the 23 CITE_WARRANTED ledger rows and the 32
  CHAPTER_LEVEL items (chapter-intro integration is already done for
  chapters 1–5; these are per-entry enrichments).
- The 6 DEFER_TO_ADJUDICATION ledger rows (SC015, SC017, SC028, SC067,
  SC068, SC080) require explicit review; items 1 and 2 address several,
  not automatically all six (SC028 remains a separate question).
- The p. 136 ordering chart's interior chords remain unresolved at
  600 dpi; no ordering edge may be inferred from them (QC report).

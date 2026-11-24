# Direct-cell experiments ('hay')

Research-only finite-state verification of the derivations in
`../DERIVATIONS.md`. Nothing here is a production cascade; nothing may be
composed into `Germanic/fsts/germanic.txt` or any adopted model.

## Cycle-9 revision

The cycle-8 version of these experiments encoded the erroneous premise
that loss of *w before unstressed *i has no historical support. Ringe &
Taylor 2014: 257–61 (§6.7.1) establish the change (after i-umlaut, before
general syncope), with Campbell 1959: §§237.1.b, 406, pp. 327–8 and Hogg
1992: §5.133 in agreement, and the frozen production definition
`OEWLossBeforeI` already cites them. The cycle-8 "overgeneration"
demonstration misread *eowu* (saved by ō-stem transfer before w-loss,
R&T p. 259) and *cleweþa* (R&T's own flagged lexical exception,
pp. 260–1) as counterexamples. See `../RESEARCH_MEMO_CYCLE9.md`.

## Networks

- `wloss_contract.bin` — the regular post-umlaut chain: w-loss
  (R&T 6.7.1) + contraction (R&T 6.9.3 p. 318) + final-vowel weakening.
  Verified against *glī*, *pyle*, *ēde*, *mete*, *mene*; derives the
  early-apocope direct cell of 'hay' to **\*hē**. The ō-stem transfer of
  'ewe' is modelled explicitly (input `ewu`); the regular prediction
  \*\*clēþa for 'itch' records that attested *cleweþa* is the exception.
- `hiatus_stage.bin` — the pre-contraction hiatus stage (⟨ei⟩; Campbell
  §237.1.b, early Merc. *streide*; Hogg §5.133).
- `g_restore.bin` — the analogical restoration of final -ġ from the
  protected cells, kept separate from the phonology (precedent:
  *glī* → *glīg*, Campbell §§411, 579(4)).
- `late_b2.bin` — late-apocope geminate route (*hauj* → *hīeġ*; *auju* →
  *īeġ*), unchanged from cycle 8.

## Run

From the repository root, with the backend container up:

```sh
bash Germanic/articles/hay/experiments/run_direct_cell.sh
```

Compiles in a container tmpdir and checks every pair in `expected.tsv`
(currently 14/14); exits nonzero on any mismatch.

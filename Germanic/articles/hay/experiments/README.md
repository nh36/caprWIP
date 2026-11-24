# Research-only formal experiments (cycle 8)

This directory verifies the cycle-8 reconstruction of the regular
direct-cell development of OE 'hay' (see `../DERIVATIONS.md`, section
"Cycle 8 — the regular direct cell established"). Nothing here is a
production cascade; nothing here may be composed into
`Germanic/fsts/germanic.txt` or the frozen SC047 models.

## Contents

- `direct_cell.foma` — three small cascades, each rule cited to
  Ringe–Taylor, Hogg–Fulk or Campbell:
  1. `regular_early.bin` — the regular early-apocope development of
     post-apocope \*hawi with the attested minimal-pair controls
     \*awi ('ewe'), \*klawiþa (> attested *cleweþa* 'itch'),
     \*mani (> *mene*), \*mati (> *mete*). Contains **no w-loss rule**,
     because none is documented before \*i.
  2. `wloss_variant.bin` — reproduces the frozen Model A step
     `OEWLossBeforeI` and demonstrates its overgeneration: it derives
     \*\*ei for attested *eowu* and \*\*cleiþa for attested *cleweþa*.
  3. `late_b2.bin` — the late-apocope diphthongal reference chain
     (\*hauj > *hīeġ*) with the attested control \*auju > *īeġ* 'island'.
- `expected.tsv` — the ten input/expected pairs with notes.
- `run_direct_cell.sh` — compiles the cascades with `foma` inside the
  backend container (in `/tmp`, nothing written to the repository or
  `/usr/app`) and checks every pair; exits non-zero on any mismatch.

## Reproduction

```sh
bash Germanic/articles/hay/experiments/run_direct_cell.sh
```

Requires the default `docker compose` stack to be up. Last verified:
all 10 checks PASS.

## Result

The regular early-apocope outcome of the direct cell is disyllabic
\*\*hewe with retained w (segment-for-segment the twin of attested OHG
*hewi* and OE *mene*); it is unattested in Old English and cannot
underlie any attested spelling of 'hay'. The Model A rule
`OEWLossBeforeI` is contradicted by *eowu* and *cleweþa* and must not be
promoted to production in any form.

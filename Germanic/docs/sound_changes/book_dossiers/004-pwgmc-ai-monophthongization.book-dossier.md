# SC004 EAF ai-monophthongization — book dossier

> **Split note (SC004 Outcome-C).** SC004 now covers **only** the later
> general/root `*ai/*ái > *ā` development (Chapter 3, Early Anglo-Frisian /
> North Sea Germanic). The word-final unstressed `*-ai > *-ē` change is separate
> and earlier — SC014 (see `014-015-opening-vowel-prelude.book-dossier.md`).
> Implemented on branch `historical-cascade-order` (FST split commit
> `f59b758d`).

## Historical phenomenon

SC004 isolates the general monophthongization of inherited `*ai` to `*ā` in the
English line — stressed/root `*ái` and unaccented nonfinal `*ai` — a North Sea
Germanic / Anglo-Frisian areal development. The `*ā` is later fronted to `ǣ` in
the relevant OE environments.

## Relevant CAPR rule

- `EAFAiMonophthongization` (former identifier `PWGmcAiMonophthongization`, retained as a documented alias)
- `[{*ai} -> {*ā} || _ ?] .o. [{*ái} -> {*ā}]`
- hist_stage `eaf`; hist_scope `north_sea_germanic`; Chapter 3; executable position 25 (after SC028)

## Example lexemes

1. `soul` (SC036 boundary witness)
2. `stone`
3. `bone`
4. `loam` (unaccented nonfinal `*ai`)
5. `whine` (unaccented nonfinal `*ai`)

## Source support

1. Ringe and Taylor place the `*ai` monophthongization among the post-PNWGmc
   English-line vowel developments [@RingeTaylor2014, pp. 40--41, §6.1.5].
2. Fulk treats `ai`/`au` among the North/West-Germanic shared developments
   [@Fulk2018, §5.2].
3. Campbell describes Anglo-Frisian `*ai > ā` (later fronted) [@Campbell1959,
   §§133--134, §417].
4. Versloot 2017 (verified directly): stressed `*ai` monophthongization as a
   two-wave North Sea Germanic areal diffusion (c. AD 400--900), not a discrete
   Proto-Anglo-Frisian node; supports the general/root side only.

## Chronology / order-test status

1. Later boundary `SC036` OE Inter Stress Raising: `*sáiwalō` yields `sāwel`
   instead of `sāwol` if SC004 is delayed past it (executable pos 25 < 33).
2. Earlier side boundary-only (pre-split expanded-PWGmc window artefact).

## Cautions for reader-facing prose

1. Present the general `*ai/*ái > *ā` change only; the final `*-ai > *-ē` change
   is SC014.
2. Characterise EAF as an operational modelling corridor for a North Sea
   Germanic areal development, not a demonstrated discrete node.
3. Note the two unaccented protoforms routed through the unaccented rewrite
   because stress is absent from the data.

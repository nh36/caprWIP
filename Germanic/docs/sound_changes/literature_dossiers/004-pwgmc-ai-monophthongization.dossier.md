# SC004 EAF ai-monophthongization — literature dossier

> **Split note (SC004 Outcome-C).** This dossier now covers **only** the later
> general/root development `*ai/*ái > *ā`. The word-final unstressed
> `*-ai > *-ē` development that the former bundled rule also packaged is a
> separate, earlier change, now **SC014** (see
> `014-015-opening-vowel-prelude.dossier.md`). SC004 no longer claims that final
> `*-ai > *-ē` is one conditioned outcome of the same historical change.
> Implemented on branch `historical-cascade-order` (FST split commit
> `f59b758d`).

## Historical phenomenon

The general (root/stressed and unaccented nonfinal) monophthongization of
inherited `*ai` to `*ā` in the English line. In Old English the `*ā` is later
fronted to `ǣ` in the relevant environments; the change is best understood as a
North Sea Germanic / Anglo-Frisian areal development rather than a single dated
node.

## CAPR rule

- change_id: `SC004`
- display_name: `EAF Ai Monophthongization`
- rule_name: `EAFAiMonophthongization`
- former identifier: `PWGmcAiMonophthongization` (bundled final+general rule; retained as a documented compatibility alias)
- FOMA definition: `[{*ai} -> {*ā} || _ ?] .o. [{*ái} -> {*ā}]` (nonfinal unaccented `*ai`, and stressed `*ái`, both to `*ā`)
- cascade: executable position 25, EAF corridor, immediately after SC028 `PNWGmcPreconsonantalXLoss`
- hist_stage `eaf`; hist_scope `north_sea_germanic`; book Chapter 3

## Example lexemes

1. `soul` (`*sáiwalō`; the SC036 boundary witness)
2. `stone` (`*stáinaz`)
3. `bone` (`*báiną`)
4. `loam` (`*laimōn`; unaccented nonfinal `*ai`)
5. `whine` (`*wainōjaną`; unaccented nonfinal `*ai`)

The full witness set is 26 corpus protoforms (24 stressed `*ái`, 2 unaccented
nonfinal `*ai`; `roe` `*ráixōn` is unattested in OE, giving the 25 attested / 26
total reconciliation). See `sc004_component_application_report.tsv`.

## Source support

1. Ringe and Taylor treat the monophthongization of `*ai` among the pervasive
   post-PNWGmc vowel developments of the English line [@RingeTaylor2014,
   pp. 40--41, §6.1.5].
2. Fulk lists the development of `ai`/`au` among the North/West-Germanic shared
   innovations against Gothic [@Fulk2018, §5.2].
3. Campbell describes the Anglo-Frisian monophthongization of `*ai > ā` (later
   fronted) as an English-line development [@Campbell1959, §§133--134, §417].
4. **Versloot 2017** (verified directly; see the reconciliation dossier) argues
   that stressed/root `*ai` monophthongization spread in two areal waves through
   a North Sea Germanic dialect continuum (c. AD 400--900), a diffusion rather
   than a single inherited Proto-Anglo-Frisian node; Old English is among the
   broadest monophthongizers. Versloot supports the **stressed/general** side
   treated here, not the early unstressed/final side (that is SC014's evidence).

## Chronology / order-test status

1. The general component carries the entire empirical chronology of the former
   bundled rule.
2. Later boundary: `SC036` OE Inter Stress Raising. Delaying SC004 past SC036
   makes `*sáiwalō` yield `sāwel` instead of `sāwol` — a genuine lexical failure,
   hence historical evidence (executable pos 25 < 33).
3. Earlier side: boundary-only (an artefact of the pre-split expanded-PWGmc
   window); no positive earlier constraint on the general component.

## Cautions for reader-facing prose

1. Present SC004 as the general/root `*ai/*ái > *ā` change only; do **not**
   reintroduce word-final `*-ai > *-ē` (that is SC014).
2. Characterise the EAF placement as an operational modelling corridor for a
   North Sea Germanic areal development, not as a demonstrated discrete
   Proto-Anglo-Frisian node.
3. Note the two unaccented protoforms (`loam`, `whine`) routed through the
   unaccented rewrite because stress is absent from the data.
4. Treat the `SC036` relation as broad/far rather than a local seam.

See also: `014-015-opening-vowel-prelude.dossier.md` (SC014, the early final
change); `sc004_historical_options_report.md`; `sc004_split_movement_proofs.md`;
`SC004-components-chronology.md`.

# SC004 EAF ai-monophthongization — literature dossier

> **Corrected PROTOFORM pass.** This dossier covers **only** the stressed/root
> development `*ái > *ā`. The unstressed development `*ai > *ē` (final and
> nonfinal) is the separate, earlier **SC014** (see
> `014-015-opening-vowel-prelude.dossier.md`). An earlier version of this dossier
> misclassified `loam` and `whine` using the cognate-set `PROTO` field; the
> production input is the Old-English-row `PROTOFORM`, under which `loam`
> (`*láimą`) is stressed `*ái` and `whine` (`*xwḯnaną`) carries no `*ai` at all.
> Implemented on branch `historical-cascade-order` (FST split commit `f59b758d`;
> PROTOFORM correction commit `9c71aed3`).

## Historical phenomenon

The monophthongization of stressed/root `*ái` to `*ā` in the English line. In Old
English the `*ā` is later fronted to `ǣ` in the relevant environments; the change
is best understood as a North Sea Germanic / Anglo-Frisian areal development
rather than a single dated node.

## CAPR rule

- change_id: `SC004`
- display_name: `EAF Ai Monophthongization`
- rule_name: `EAFAiMonophthongization`
- former identifier: `PWGmcAiMonophthongization` (bundled rule; retained as a documented compatibility alias)
- FOMA definition: `{*ái} -> {*ā}` (stressed/root `*ái` only)
- cascade: executable position 25, EAF corridor, immediately after SC028 `PNWGmcPreconsonantalXLoss`
- hist_stage `eaf`; hist_scope `north_sea_germanic`; book Chapter 3

## Example lexemes

1. `soul` (`*sáiwalō`; the SC036 boundary witness)
2. `stone` (`*stáinaz`)
3. `bone` (`*báiną`)
4. `loam` (`*láimą`; stressed `*ái` by its PROTOFORM)
5. `one` (`*áinaz`)

The witness set is **24 stressed corpus protoforms** (23 attested + `roe`
`*ráixōn`, which has no attested OE counterpart). See
`sc004_component_application_report.tsv`. The two dat.sg `*-ai` endings
(`span`, `meed`) are unstressed and belong to SC014, not SC004.

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
   broadest monophthongizers. Versloot supports precisely the **stressed** side
   treated here.

## Chronology / order-test status

1. Later boundary: `SC036` OE Inter Stress Raising. First-break testing with the
   corrected stressed-only rule confirms that delaying SC004 past SC036 makes
   `*sáiwalō` yield `sāwel` instead of `sāwol` (order 33; 371/372 match at the
   break). SC004 at executable pos 25 sits safely before it.
2. Earlier side: no corpus break toward the head (boundary-limited); SC004's only
   corpus-relevant boundary is SC036.
3. Formal interactions (`sc004_sc014_interaction_report.md`): SC004 non-commutes
   with `PWGmcEarlyIApocope`, `PNWGmcILowering`, `PNWGmcULowering` only on
   non-corpus `EnglishProtoInput` forms (feeding artefacts) and genuinely with
   `SC036` (the soul dependency).

## Cautions for reader-facing prose

1. Present SC004 as the stressed/root `*ái > *ā` change only; do **not**
   reintroduce unstressed `*ai` (that is SC014).
2. Characterise the EAF placement as an operational modelling corridor for a
   North Sea Germanic areal development, not as a demonstrated discrete
   Proto-Anglo-Frisian node.
3. `loam` (`*láimą`) is a stressed witness; `whine` is not an ai-monophthongization
   case at all.
4. Treat the `SC036` relation as broad/far rather than a local seam.

See also: `014-015-opening-vowel-prelude.dossier.md` (SC014, the unstressed
change); `sc004_historical_options_report.md`; `sc004_sc014_interaction_report.md`;
`SC004-components-chronology.md`.

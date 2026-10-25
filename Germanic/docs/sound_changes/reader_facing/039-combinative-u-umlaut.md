# Combinative u-umlaut in wi-forms

## Historical discussion

The history of *wuduwe* ‘widow’ orders these two changes within the same
low-stress vocalic development. Campbell discusses both the
\emph{w}-conditioned \emph{u} forms and the later *weorold* 'world' / *weoruld* 'world'
alternation, while Ringe and Taylor give the same connection comparatively in
\emph{*widuwon-}, [weraldu]{.recon} 'world', and [jugunþi]{.recon} 'youth'
[@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332;
@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267;
@RingeTaylor2014, p. 322, §6.3.3].

[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) feeds the vowel
sequence subsequently reshaped by
[SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).
Initial \emph{w} conditions the first change.

## SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

```foma
define OEWICombinativeUUmlaut Ctx([
    {*í} -> {*ú} || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
]);
```

The *wuduwe* ‘widow’ derivation answers one narrow question about \emph{wi}-forms. If [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [wíduwōn]{.recon} ‘widow’ yields [*wudowe*]{.pred} rather than expected OE *wuduwe*. This one-sided witness requires combinative u-umlaut to precede medial lowering and supplies no lower boundary.

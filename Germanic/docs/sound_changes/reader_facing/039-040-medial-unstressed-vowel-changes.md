# Medial unstressed vowel changes

## Historical discussion of medial unstressed vowel changes

The history of *wuduwe* ‘widow’ orders these two changes within the same
low-stress vocalic development. Campbell discusses both the
\emph{w}-conditioned \emph{u} forms and the later *weorold* / *weoruld*
alternation, while Ringe and Taylor give the same connection comparatively in
\emph{*widuwon-}, \emph{*weraldu}, and \emph{*jugunþi}
[@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332;
@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267;
@RingeTaylor2014, p. 322, §6.3.3].

[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) feeds the vowel
sequence subsequently reshaped by
[SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).
Initial \emph{w} conditions the first change.

## SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

```foma
define OEWICombinativeUUmlaut [
    {*í} -> {*ú}
        || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
];
```

The *wuduwe* ‘widow’ derivation answers one narrow question about \emph{wi}-forms. If [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) follows [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe*; earlier placement changes no checked output. The witness requires combinative u-umlaut to precede medial lowering and supplies no lower boundary.

## SC040. Lowering of medial unstressed \emph{*u} (`OEMedUnstressedULowering`) {#rule-OEMedUnstressedULowering}

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

The two witnesses date medial unstressed \emph{*u} > \emph{*o} at very different scales. Before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe* ‘widow’; after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. The local *weorold* ‘world’ and *widow* evidence places lowering after combinative u-umlaut, while the youth form supplies only the distant requirement that lowering precede unstressed long-vowel shortening.

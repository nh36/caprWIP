# Medial unstressed vowel changes

## Historical discussion of medial unstressed vowel changes

These two rules belong together because the same low-stress vocalic region supplies their witnesses, and the order evidence ties them together through *wuduwe* ‘widow’. Campbell discusses both the \emph{w}-conditioned \emph{u} forms and the later *weorold* / *weoruld* alternation, while Ringe and Taylor give the same connection comparatively in \emph{*widuwon-}, \emph{*weraldu}, and \emph{*jugunþi} [@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332; @Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267; @RingeTaylor2014, p. 322, §6.3.3].

The pair is therefore historically tighter than a merely adjacent grouping. [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) is the narrower rule, but it feeds the exact vowel sequence that [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) must then reshape.

## SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

The implementation keeps the \emph{w}-conditioned adjustment very small.

```foma
define OEWICombinativeUUmlaut [
    {*í} -> {*ú}
        || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
];
```

In prose, the rule changes the first vowel of \emph{wi}-forms under the following back-vowel conditions. This is the step that helps produce OE *wuduwe* ‘widow’.

Its chronology is clear on the later side. If the rule is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe* ‘widow’. This shows that [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the `widow` material belongs to the same low-stress vocalic sequence as the following medial lowering.

## SC040. Lowering of medial unstressed \emph{*u} (`OEMedUnstressedULowering`) {#rule-OEMedUnstressedULowering}

The implementation states the lowering rule directly.

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

In prose, the rule lowers medial unstressed \emph{*u} to \emph{*o} in the relevant consonantal environment. This is the stage behind forms such as *weorold* ‘world’.

Its chronology is explicit on both sides. If the rule is moved before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe* ‘widow’. If it is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. This shows that [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), and that [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).

The later relation to [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) is real, but it is much broader than the local *widow* pair. The closest chronological result inside this chapter is still the reciprocal relation between [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) and [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

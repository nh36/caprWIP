# Awj glide formation and au-fronting

## Historical discussion of awj glide formation and au-fronting

These two rules belong together because the same *hay* and *strew* material passes through both of them. [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) reshapes the older \emph{awj} sequence, and [SC030 OEAuFronting](#rule-OEAuFronting) then fronts the resulting \emph{au}. Campbell's discussion of these outcomes and Ringe and Taylor's derivations of *hīeġ* and *strīeġan* describe the same sequence in ordinary historical terms [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

That relation is close enough to justify one paired chapter, but the two rules still need separate historical discussions and separate chronology paragraphs. The first rule prepares the sequence; the second carries it forward into [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

## Historical discussion of awj glide formation

Older \emph{awj} sequences are the source of forms such as *hīeġ* ‘hay’ and *strīeġan* ‘strew’. Campbell treats the relevant developments directly, and Ringe and Taylor likewise trace the same material through intermediate \emph{auj}-type stages [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

This makes [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) historically clear even though its current order evidence is one-sided.

## SC029. Glide formation in \emph{*awj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

The implementation keeps the glide-formation step explicit.

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

In prose, the rule turns older \emph{awj} material into the glide sequence that the following fronting rule can read. This is the step behind forms such as *hīeġ* and *strīeġan*.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC030 OEAuFronting](#rule-OEAuFronting), PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. This shows that [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) must come before [SC030 OEAuFronting](#rule-OEAuFronting). The earlier direction remains boundary-limited in current testing: the search reaches bundled earlier material without a real break.

## Historical discussion of au-fronting

Once the glide sequence is in place, \emph{au}-fronting produces the fronted diphthongal outcomes that carry this material into the broader West Saxon vowel history. Campbell's account of \emph{au} > \emph{ēa} keeps that larger setting in view [@Campbell1959, pp. 53--54, §135].

That is why [SC030 OEAuFronting](#rule-OEAuFronting) matters beyond the immediate pair: it reciprocates [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) and then passes a wider set of derivations forward into [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

## SC030. Fronting of \emph{*au} (`OEAuFronting`) {#rule-OEAuFronting}

The implementation states the fronting step directly.

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

In prose, the rule fronts \emph{au} so that later Old English diphthongal outcomes can develop in the expected way. It is the step that connects the *hay* / *strew* material to the wider diphthongal region that follows.

Its chronology is explicit on both sides. If the rule is moved before [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation), PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. If it is delayed until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*galáubijaną}, \emph{*bráudą}, and \emph{*dráugmaz}, together with sixteen other derivations, fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. This shows that [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) must come before [SC030 OEAuFronting](#rule-OEAuFronting), and that [SC030 OEAuFronting](#rule-OEAuFronting) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

The later failure set is broad and is best read as failed derivations. It does not present a competing set of Old English surface forms.

# Early unstressed fronting

## Historical discussion

Campbell distinguishes the shortening of unaccented long vowels, while Hogg,
Ringe and Taylor, and Fulk place fronting and shortening within a later history
of syncope and final-vowel adjustment [@Campbell1959, p. 148, §355;
@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7]. Earlier unstressed fronting precedes later
o-shortening.

[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) has both an
earlier and a later lexical breakpoint.
[SC071 OELateOShortening](#rule-OELateOShortening) confirms their reciprocal
order, but no lexical evidence fixes its later boundary.

## SC070. Early fronting of unstressed \emph{*a} (`OEUnstressedFrontingEarly`) {#rule-OEUnstressedFrontingEarly}

```foma
define OEUnstressedFrontingEarly FootCtx(OEUnstressedAFronting);
```

The rule fronts unstressed \emph{*a} to \emph{*æ} after the earlier shortening
has created a frontable vowel but before the later shortening of unstressed
\emph{*ō}. It produces endings such as OE \emph{-en} in *lungen* ‘lungs’.

If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc [búrōθi]{.recon} ‘bears’ yields [*boreþ*]{.pred} rather than expected OE *boraþ* ‘bears’, and PGmc [mḗnōθz]{.recon} ‘month’ yields [*mōneþ*]{.pred} rather than expected *mōnaþ* ‘month’. The witness forms require [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) to follow [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and precede [SC071 OELateOShortening](#rule-OELateOShortening).

The relation to [SC071 OELateOShortening](#rule-OELateOShortening) is local.
The earlier boundary at
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) places fronting after
the older palatal developments.

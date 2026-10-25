# Late o-shortening

## SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening Ctx([
    # LATE: *ō → *o elsewhere (runs AFTER fronting; Campbell §355: the late
    # product is "of too late origin to become æ").
    # Stausland Johnsen 2015:28-30: unstressed long vowels shorten regularly in
    # pre-OE AFTER the loss of short unstressed vowels (the *bursti-/*burstīz
    # argument). The shortened vowel is a plain short *o — the ONLY source of
    # unstressed *o at this stage (the earliest OE texts have just two
    # unstressed back vowels, u and a: Stausland Johnsen 2015:21; classical-OE
    # unstressed o arises only from the later 9th-c. lowering, SC040). Its
    # split — u in medial syllables, a in final syllables — is carried out by
    # OEMedUnstressedORaising (SC099) and OEFinalUnstressedOLowering (SC100)
    # immediately below, replacing the old one-step *ō → *a compression that
    # hard-coded the final-syllable outcome for all positions (van Helten's
    # refuted conditioning aside, medial *ō would have surfaced wrongly as a:
    # **wundade).
    {*ō} -> {*o} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
]);
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting. The
shortened vowel is then resolved by the following medial/final distribution,
not directly as \emph{a} [@StauslandJohnsen2015, pp. 28--31].

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc [búrōθi]{.recon} ‘bears’ yield [*boreþ*]{.pred} rather than expected OE *boraþ* 'bears'. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly).

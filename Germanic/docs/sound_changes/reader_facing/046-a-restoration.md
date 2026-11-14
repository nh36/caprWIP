# A-restoration

## Historical discussion of A-restoration

Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's later retraction describe the same post-brightening development [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. Some outcomes of Anglo-Frisian fronting survive only in environments where restoration does not return them to back \emph{a}.

[SC046 OEARestoration](#rule-OEARestoration) has firmer handbook support than the two following nasal rules.

## SC046. Restoration of \emph{*a} before following back vowels (`OEARestoration`) {#rule-OEARestoration}

```foma
define OEARestoration FootCtx((
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
));
```

Restoration must receive fronted \emph{*æ} and return \emph{*a} before the nasal-tail changes. Before [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [bákaną]{.recon} ‘bake’ yields [*bæcan*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc [fáraną]{.recon} ‘fare’ yields [*færan*]{.pred} rather than expected *faran* ‘fare’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), [bákaną]{.recon} again yields [*bæcan*]{.pred} instead of *bacan*, while PGmc [wádaną]{.recon} ‘wade’ yields [*wædan*]{.pred} instead of *wadan* ‘wade’. These independent witness pairs place restoration after brightening and before secondary nasalization.

The weak-noun plural must be distinguished from its nominative citation
form. A protected secondary nasal leaves \emph{*flæskōn} 'flasks'
with a back-vowel trigger, and restoration gives \emph{*flaskōn}.
The subsequent predicted ending \emph{-en} concerns shortening and
nasalization, not a failure of root restoration. The
[weak-paradigm comparison](#weak-n-paradigms-after-apocope) separates
that ending dispute from Campbell's and Luick's analysis of singular
*flasce* 'flask' after inflected *flascan*
[@Campbell1959, p. 61, §158; @Luick1914, pp. 152--153, §161;
@RingeTaylor2014, pp. 163--164, 192].

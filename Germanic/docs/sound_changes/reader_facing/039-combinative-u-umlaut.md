# Combinative u-umlaut in wi-forms

## Historical discussion

The history of *wuduwe* ‘widow’ orders these two changes within the same
low-stress vocalic development. Campbell discusses both the
\emph{w}-conditioned \emph{u} forms and the later *weorold* 'world' / *weoruld* 'world'
alternation, while Ringe and Taylor give the same connection comparatively in
\emph{*widuwon-}, [weraldu]{.recon} 'world', and [jugunþi]{.recon} 'youth'
[@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332;
@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267;
@RingeTaylor2014, p. 322, §6.9.4].

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


## Historical limits of the represented account

The phonetic relevance of preceding *w* and a following back vowel is
independently supported by *wudu* 'wood', *wuduwe* 'widow' and West Saxon
*wucu* 'week'. Unlike ordinary West Saxon back umlaut, this retraction can
occur across a dental or velar. These comparisons do not, however,
establish that every inherited short *i* in that environment acquired *u*
[@Campbell1959, pp. 92--93, §§218--221; @HoggGrammar2011, pp. 158--163,
§§5.108--5.112; @SieversBrunner1965, pp. 93--94, §114;
@RingeTaylor2014, pp. 322--324; @Fulk2018, pp. 68--69, §4.8].

The independently reconstructed \emph{*witun} 'they know' supplies a
substantive limit: the present rule predicts a root *u*, whereas the cited
West Saxon forms *witon* and *wioton* retain *i* or show ordinary back
umlaut. This is a historical comparison, not a rejected artificial word.
The general conditioning is therefore deferred; the selected widow
derivation is retained without claiming a complete account of all these
reflexes. No lexical exception, grammatical condition or optional
sound law is introduced. Brunner's specific optative-based explanation
of *witon* 'let us' cannot simply be transferred to 'they know'.

Barrack distinguishes combinative retraction from ordinary back umlaut
and expressly leaves their relative order in West Saxon uncertain.
His early-glossary argument does not by itself establish an earlier
historical date for the combinative change; Hogg explicitly questions
that inference. Bülbring's account places a two-step development around
700, but the present representation does not establish those separate
steps or a new ordering against ordinary back umlaut
[@Barrack1975, pp. 63--65, rules 210, 212, 218, 220;
@Bulbring1902, pp. 106--107, §264; @HoggGrammar2011, pp. 162--163, §5.112].

# Northwest Germanic u-lowering

## Historical discussion

Northwest Germanic lowered \emph{*u} to \emph{*o} when the following
syllable contained a non-high vowel. Campbell describes the change and
lists *ġeoc* 'yoke' among its regular outcomes [@Campbell1959, pp. 42--43,
§115]; Fulk gives the same word as a standard example — "OIcel. ok, OE
geoc, OHG joh beside juh and OS juk" — and notes the paradigmatic
alternation between lowered and unlowered stems that the conditioning
produced [@Fulk2018, p. 56, §4.3]. A word-initial \emph{*j} does not block
the change: the blocking effect of \emph{j} concerns only a consonantal
\emph{j} standing between the target vowel and the conditioning vowel, as
in the class I weak verbs of the *cnyssan* 'strike' type
[@Fulk2018, p. 56, §4.3]. Ringe and Taylor accordingly reconstruct the
Proto-West Germanic paradigm of 'yoke' with the lowering applied
[@RingeTaylor2014, p. 129].

Regular corpus witnesses include [ġeoc]{.iv lang=oe sort=geoc role=evidence_form} 'yoke', *nosu* 'nose',
*sċofl* 'shovel', and *sorg* 'sorrow'. Where the following syllable kept a
high vowel the lowering did not apply, as in *ġeoguþ* 'youth', whose root \emph{u}
survived [@SieversBrunner1965, pp. 64--65, §92.1].

Regular lowering does not imply that every attested inherited word preserves
the lowered vowel. The masculine noun
[rust]{.iv lang=oe sort=rust role=comparison_form} 'rust' is a lexical residue:
selected PGmc [rústaz]{.recon} 'rust' regularly predicts
[rost]{.recon form_role=regular_output} 'rust'. Orel's alternative
[rustō]{.recon} 'rust' gives the same lowered root; his masculine alternative
is independently supported by Ringe [@Orel2003, p. 309;
@Ringe2017, pp. 247--248]. Since [frústą]{.recon} 'frost' regularly gives
[forst]{.iv lang=oe sort=forst role=comparison_form} 'frost', a general
_-st-_ exemption is unwarranted. The retained *u* remains unexplained,
alongside the other retained-*u* cases such as *bucc* 'buck', *fugol*
'bird', *wulf* 'wolf' and *wulle* 'wool'; their consonantal environments
do not establish a general replacement law [@Campbell1959, p. 43, §115;
@RingeTaylor2014, pp. 27--34]. The lowering law is retained; its non-high
conditioning class includes nasalized long \emph{*ǭ}, not just oral
\emph{*ō}. The independently reconstructed accusative \emph{*wullǭ}
therefore lowers just as the nominative \emph{*wullō} does under the
preferred chronology [@Ringe2017, pp. 242--243]. This does not merge either
ending with trimoric \emph{*ô}. The
[rust lexical discussion](#rust-oe-rust) distinguishes the selected
masculine citation, Orel's alternative and diagnostic paradigm constructions.

## SC017. Lowering of \emph{*u} before following non-high vowels (`PNWGmcULowering`) {#rule-PNWGmcULowering}

```foma
define PNWGmcULowering Ctx([
    [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
    ]
]);
```

The implementation lowers the first nucleus through a consonantal interval
without \emph{*j}; the immediately following consonant must not be nasal.
This literal guard is not a claim that every nasal anywhere in the interval
blocks the historical process. Fulk distinguishes tautosyllabic and
heterosyllabic nasal environments [@Fulk2018, p. 56].

The lowering feeds the much later West Saxon palatal-glide spelling
([SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide)): the \emph{o} that the
scribes wrote in *ġeoc* 'yoke' is the output of this change, so PGmc
[júką]{.recon} 'yoke' passes through \emph{*joką} on its way to the
attested spelling [@Fulk2018, p. 56, §4.3; @RingeTaylor2014, p. 129].
If lowering is placed after
[SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), selected
[núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected *nosu*,
PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected
*sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather
than expected *sorg*. These are conditional computational consequences,
not independent proof that those paradigms underwent no levelling.
CAPR provisionally prefers lowering before final raising because it
regularly accounts for these low-root forms without additional,
individually unproved analogical generalizations. Nose already involves
earlier stem remodelling, and the retained high vowels of wool and love
remain a genuine cost of that preference. The main comparison of Fulk,
Ringe and Taylor, and Stiles, including the Runic evidence and the
plausible but unproved nominative-generalization account of wool, is in
[SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising).

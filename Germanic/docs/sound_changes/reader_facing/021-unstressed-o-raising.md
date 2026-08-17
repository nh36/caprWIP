# Unstressed \emph{*o}-raising

## Historical discussion

In the Northwest Germanic period an unstressed \emph{*o} was raised to \emph{*u}
when \emph{*u} followed in the next syllable. The clearest case is the
\emph{n}-stem accusative singular, where inherited \emph{*-onų} was regularly
raised to \emph{*-unų} before the following high vowel; Campbell treats the
resulting unstressed \emph{u} and \emph{o} alternations for Old English
[@Campbell1959, pp. 155--156, §§373--374]. The change is a general development of
the unstressed suffix, not tied to any single lexeme.

## SC021. Raising of unstressed \emph{*o} before later \emph{*u} (`PNWGmcUnstressedORaising`) {#rule-PNWGmcUnstressedORaising}

```foma
define PNWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

No word in the present selected corpus supplies this environment: no selected
input carries an unstressed \emph{*o} before a following \emph{*ų}, so
[SC021 PNWGmcUnstressedORaising](#rule-PNWGmcUnstressedORaising) fires in no
current derivation. The earlier witness [*heofon*]{.iv lang=oe sort=heofon role=evidence_form}
'heaven' no longer applies here: its selected input is now Ringe and Taylor's
northern West Germanic [hebun]{.recon .iv lang=nsgmc sort=hebun role=evidence_form}
'heaven', which already carries the generalized labial and contains no unstressed
\emph{*o} before \emph{*ų} [@RingeTaylor2014, p. 287]. The rule is retained as a
genuine Northwest Germanic change, but it is presently unwitnessed and
boundary-limited: no lexical form now constrains its position within the Old
English sequence, and moving it earlier or later leaves every output unchanged.

One candidate witness was examined and declined. The early Northumbrian
accusative *galgu* 'gallows' (Ruthwell Cross) stands among the "very few"
\emph{n}-stem forms preserving a \emph{u}-vowel in this ending, and if its
\emph{-u} continued raised \emph{*-unų} it would witness this change directly.
But Ringe and Taylor themselves hedge the form — "masc. acc. galgu is not
necessarily relevant", since its \emph{-u} may instead connect with the Old
High German masculine accusative singular ending \emph{-un} ~ \emph{-on} on
Bammesberger's analogical account [@RingeTaylor2014, pp. 62--63; @Bammesberger1990,
p. 169] — they judge the raising hypothesis phonetically sensible but resting
on "too small a basis" [@RingeTaylor2014, p. 63], and they conclude of the
competing analyses of these \emph{n}-stem relics that "a decisive choice
between those alternatives does not seem possible" [@RingeTaylor2014, p. 164].
A single dialectally marked inflected relic whose ending admits an analogical
source cannot responsibly anchor a sound law, so the rule remains unwitnessed
and its coverage status is recorded as a research issue.

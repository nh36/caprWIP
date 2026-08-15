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

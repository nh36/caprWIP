# Early o-shortening

## Historical discussion

After the principal palatal and umlautal changes, unstressed vowels undergo
shortening, fronting, merger, and sometimes complete loss. Campbell describes
the early shortening of unaccented long vowels, while Hogg, Ringe and Taylor,
and Fulk relate it to apocope, syncope, and the later reductions
[@Campbell1959, p. 148, §355; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

Earlier displacement tests concerned the unrestricted nasal environment;
they are not current constraints on the restricted rule. The rules that follow,
especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
have more closely defined relations.

## SC069. Early shortening of unstressed \emph{*ō} before m and nonfinal n (`OEEarlyOShortening`) {#rule-OEEarlyOShortening}

```foma
define OEEarlyOShortening Ctx([
    # Final *ōn survives to SC071/SC100, after unstressed fronting.
    # Adopted northern ending route: Ringe/Taylor 2014:164, scenario 3.
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
    [{*m} | {*n} ContextSegments]
]);
```

The rule shortens unstressed long \emph{*ō} before \emph{m}, and before
\emph{n} when another segment follows. Its product can undergo later
unstressed fronting. It does not shorten \emph{*ō} before word-final
\emph{n}; this is a phonological condition, not a declension restriction.

The distinction admits the regular northern ending history discussed by
Ringe and Taylor. In nominative plural \emph{*fláskōniz} and dative
singular \emph{*fláskōni}, early apocope exposes secondary final
\emph{*n}, protected by the earlier completion of
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss).
Restoration gives \emph{*flaskōn}; the long vowel survives this rule
and fronting, then
[SC071 OELateOShortening](#rule-OELateOShortening) and
[SC100 OEFinalUnstressedOLowering](#rule-OEFinalUnstressedOLowering)
give attested *flascan* 'flasks' and 'flask', respectively.
The [weak-paradigm discussion](#weak-n-paradigms-after-apocope)
sets out the adopted history and Hill's raising-and-redistribution
alternative [@RingeTaylor2014, pp. 163--164;
@Hill2010, pp. 433--443].

The older unrestricted rule, applied to a protected secondary nasal,
gave predicted [flascen]{.pred}. Earlier shortening before nasalization
and early unrounding also reproduced \emph{-an} in experiments, but are
not adopted. Likewise, the old broad displacement failures for
*nǣdre* 'adder', *eorþe* 'earth', *flasce* 'flask',
*heorte* 'heart' and *līne* 'line' measured that unrestricted rule,
not the final-n exemption now implemented. They establish no new
local boundary for the restricted rule.

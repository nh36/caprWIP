# Noninitial w-loss before unstressed i

## SC054. Noninitial \emph{*w}-loss before unstressed \emph{*i/ī} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

```foma
define OEWLossBeforeI Ctx([
    {*w} -> 0 || EnglishStarVocalic EnglishStarConsonant* _ [{*i}|{*ī}]
]);
```

The history of *sǣ* ‘sea’ exemplifies noninitial \emph{*w}-loss before
unstressed \emph{*i}. Campbell describes the loss, Ringe and Taylor derive
the form from \emph{*saiwi-}/\emph{*sawi-}, and Luick gives the parallel
trajectory [@Campbell1959, pp. 166--167, §406;
@RingeTaylor2014, pp. 258--260, §6.7.1; @Luick1914, p. 173, §187].
The environment is neither exclusively postvocalic nor exclusively final:
Ringe and Taylor also give weak-verb forms in \emph{*-Cwi-} and
\emph{*pulwīn > *pylwī > *pylī}, yielding *pyle* 'pillow'.
The preceding nucleus distinguishes noninitial *w* from an initial cluster;
the unaccented target excludes stressed high vowels. No lexical exemption
or loanword-specific clause is used.

Ringe and Taylor independently place this loss after i-umlaut and before
general syncope: the histories of *eowu* 'ewe' and *gierede* 'prepared'
supply the chronology, rather than successful output alone
[@RingeTaylor2014, pp. 258--260]. The early final-n loss in
[SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) and this distinct
glide loss together explain *pyle*.

The former sea-only displacement supplies two distant implementation limits. Before [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion) or after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI) yields [*sǣw*]{.pred} rather than expected OE *sǣ* 'sea'. The loss must therefore follow final \emph{z}-deletion and precede high-vowel apocope, while its exact position within that broad interval remains source-based.

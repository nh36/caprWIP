# Sievers-law syncope

## Historical discussion

Sievers' Law concerns a prosodic and morphological adjustment in heavy stems.
It is a distributional rule distinct from b-allophony ([SC049 PGmcBAllophony](#rule-PGmcBAllophony)). Adamczyk treats
the Old English reflexes of the law as historical evidence from weak verbs and
related formations [@Adamczyk2001, pp. 61--72]. Fulk gives the compact
comparative summary through familiar forms such as *biddan* 'ask', *sellan*
'give', and *nerian* 'save' [@Fulk2018, p. 127, §6.15].

Sievers-law syncope is narrow in scope, but its relation to the following
palatalization is lexically secure. Its earlier limit is less sharply defined
than that of the preceding allophony rule.

## SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

The Sievers-law reduction \emph{*-CijV-*} > \emph{*-CjV-*}, including loss of \emph{*i} before \emph{*j}, must precede palatalization. If [SC050 SieversLawSyncope](#rule-SieversLawSyncope) follows [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [strákkijaną]{.recon} 'stretch' yields [*strecċan*]{.pred} rather than expected OE *streċċan* 'stretch'; earlier placement creates no comparably precise error. The single cluster witness therefore places syncope before velar palatalization.

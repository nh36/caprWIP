# Compound linking syncope

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) captures this
pattern in compounds such as *reġnboga* ‘rainbow’. The only boundary the lexical evidence supplies
is the immediately following technical stress-stripping stage, which is not a
sound change.

## SC037. Syncope of compound linking vowels (`OECompoundLinkingSyncope`) {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

The *reġnboga* 'rainbow' test exposes a bookkeeping dependency rather than a historical sound-change boundary. After SC038 OEStripSecondaryStress, PGmc [régna-bùgô]{.recon} ‘rainbow’ yields [*reġnefoga*]{.pred} rather than expected OE *reġnboga* ‘rainbow’, because the technical stage has erased the stress information that licenses syncope. The handbooks instead place weakened compound junctures with the behavior described under [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).

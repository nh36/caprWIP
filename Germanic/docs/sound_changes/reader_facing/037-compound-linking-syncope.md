# Compound linking syncope

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) captures this
pattern in compounds such as *reġnboga* 'rainbow'. Its second-root vowel
has already lowered under subordinate stress:
\emph{*régna-bùgô > *régna-bògô}. The grave survives that early
change and licenses deletion of the linking vowel, giving
\emph{*régnbògô}; ordinary accent stripping then gives
\emph{*régnbogô}. The full account and its reconstruction qualifications
belong to [SC017 PNWGmcULowering](#rule-PNWGmcULowering), not to late
unstressed lowering. The only boundary the lexical evidence supplies
is the immediately following technical stress-stripping stage, which is not a
sound change.

## SC037. Syncope of compound linking vowels (`OECompoundLinkingSyncope`) {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope Ctx([
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _ OEAnyConsonant+ PGmcStarGraveVowel
]);
```

The *reġnboga* test exposes an annotation dependency rather than an
independently dated historical sound-change boundary. If the grave is
removed before syncope, its licensing information is lost. Early lowering
changes the vowel, not this dependency; the annotation's lifetime does not
date a universal loss of compound secondary stress. The handbooks place
weakened compound junctures with the behavior described under
[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and
[SC036 OEInterStressRaising](#rule-OEInterStressRaising).

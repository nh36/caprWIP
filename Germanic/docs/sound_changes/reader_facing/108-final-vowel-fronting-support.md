# Technical support: retained final-vowel representation

## SC108. Retained final-vowel representation (`EAFBrighteningLongFinal`) {#rule-EAFBrighteningLongFinal}

```foma
define EAFBrighteningLongFinal Ctx([
    {*ā} -> {*ǣ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
]);
```

In *ræste* ‘rest’, this helper receives the length-preserved outcome of
[SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding).
The preceding-nucleus guard excludes stressed monosyllabic *hwā* ‘who’.
Later shortening and merger complete the ending; the carried long vowel
does not establish a separate dated long-a law
[@RingeTaylor2014, pp. 58--59, 299--300; @Campbell1959, p. 49, §125].

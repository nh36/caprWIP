# Technical support: late palatal diphthongization

## SC105. Retained late palatal-diphthongization approximation (`OELatePalatalDiphthong`) {#rule-OELatePalatalDiphthong}

```foma
define OELatePalatalDiphthong [
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

This support operation retains exactly the former postmutation long-vowel
clause. Its sole current application is *sċēaþ* 'sheath'. The four initial
triggers are an unchanged approximation, not a source-proven complete
historical conditioner. Campbell and Ringe–Taylor distinguish the later
class [@Campbell1959, pp. 68–69; @RingeTaylor2014, p. 235];
the incremental implementation does not claim to have resolved it.

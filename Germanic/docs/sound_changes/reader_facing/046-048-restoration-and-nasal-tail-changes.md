# A-restoration and nasal changes

## Historical discussion of A-restoration

The first member of this chapter is the clearest historical hinge in the post-brightening region. Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's discussion of later retraction describe the same phenomenon that the transducer keeps explicit here [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. The rule matters because Anglo-Frisian fronting is often visible only through the later environments that restore some of its outcomes to back \emph{a}.

That makes [SC046 OEARestoration](#rule-OEARestoration) the source-backed hinge of the chapter. The nasal rules that follow belong in the same neighborhood, but they do not carry quite the same historical weight in the handbooks.

## SC046. Restoration of \emph{*a} before following back vowels (`OEARestoration`) {#rule-OEARestoration}

The implementation keeps the restoration step explicit.

```foma
define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

In prose, the rule changes earlier fronted \emph{*æ} back to \emph{*a} before the relevant following back-vowel environments. This is the step that turns fronted forms such as *bæcan* back into the attested OE *bacan* ‘bake’.

Its chronology is explicit on both sides. If the rule is moved before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*bákaną} yields *bæcan* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*fáraną} yields *færan* rather than expected *faran* ‘fare’. If it is delayed until after [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc \emph{*bákaną} again yields *bæcan* instead of *bacan*, and PGmc \emph{*wádaną} yields *wædan* instead of *wadan* ‘wade’. This shows that [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) must come before [SC046 OEARestoration](#rule-OEARestoration), and that [SC046 OEARestoration](#rule-OEARestoration) must come before [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization).

The rule is therefore not a decorative aftereffect of brightening. It is a real restoration hinge with a positive local window on both sides.

## Historical discussion of heavy-syllable nasal loss and secondary nasalization

The remaining two rules are more tightly paired inside the model than they are in ordinary handbook naming. Their connection is derivational and broad. [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) removes the final nasalized vowel in heavy syllables, while [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) marks the preceding \emph{a} before final \emph{n}. The result is a large reciprocal failure set if the two are inverted. Campbell's discussion of later nasal loss and the later back-mutation environment gives the broader background, while Ringe and Taylor help with the later cross-reference toward [SC059 OEBackMutation](#rule-OEBackMutation) [@Campbell1959, pp. 86, 166, §§205--206, 403; @RingeTaylor2014, p. 319, §6.9.4].

That shared discussion is justified because the two rules interact directly inside the derivation. Even so, the hierarchy remains visible: the pair is a strong computational core, but less like a classical textbook chapter than [SC046 OEARestoration](#rule-OEARestoration).

## SC047. Heavy-syllable nasal apocope of final \emph{*ą} (`OEHeavySyllableNasalApocope`) {#rule-OEHeavySyllableNasalApocope}

The implementation keeps the apocope step short.

```foma
define OEHeavySyllableNasalApocope [
    {*ą} -> 0 || OEAnyConsonant _ .#.
];
```

In prose, the rule deletes final nasalized \emph{*ą} after a heavy syllable. This is the step that prevents a large class of forms from retaining spurious weak final vowels.

Its chronology is real on both sides, though not equally local. If the rule is moved before SC034 OEAwLongDiphthong, PGmc \emph{*stráwą} yields *stræw* rather than expected OE *strēaw* ‘straw’. If it is delayed until after [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside a very broad \emph{-en} failure set. This shows that SC034 OEAwLongDiphthong must come before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), and that [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) must come before [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization).

The earlier side is narrow, but the later side is one of the broadest reciprocal failure sets in this part of the model.

## SC048. Secondary nasalization before final \emph{*n} (`OESecondaryNasalization`) {#rule-OESecondaryNasalization}

The following rule states the nasalization step directly.

```foma
define OESecondaryNasalization [
    {*a} -> {*ą} || _ {*n} .#.
];
```

In prose, the rule nasalizes \emph{*a} before final \emph{n}. This is the step that helps keep the live \emph{-an} outcomes distinct from the spurious \emph{-en} forms that appear if the late nasal rules are misordered.

Its chronology is explicit on both sides. If the rule is moved before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan*, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan*, representing the same broad reciprocal failure set. If it is delayed until after [SC059 OEBackMutation](#rule-OEBackMutation), PGmc \emph{*stélaną} yields *steolan* rather than expected OE *stelan* ‘steal’, and PGmc \emph{*wébaną} yields *weofan* rather than expected *wefan* ‘weave’. This shows that [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) must come before [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), and that [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) must come before [SC059 OEBackMutation](#rule-OEBackMutation).

That combination explains the chapter’s internal hierarchy. [SC046 OEARestoration](#rule-OEARestoration) is the clearest historical hinge, while [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) and [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) form the stronger reciprocal nasal core.

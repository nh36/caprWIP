# Postmutation high-vowel syncope

## Historical discussion

The regular high-vowel core loses a short unstressed high vowel in an open
medial syllable after a heavy syllable. Light-root retention and the
earlier light-root contractions must remain distinguished; the latter
are not explained away as optionality, grammatical conditioning or
unsupported analogy [@SieversBrunner1965, pp. 137--138, §§167--168;
@Campbell1959, pp. 145--146, §§348--349;
@HoggGrammar2011, pp. 222--225, §§6.18--6.21].

Ringe and Taylor reconstruct pre-Old-English
[ūtumist]{.recon .iv lang=preoe sort=utumist role=source_protoform},
then [ȳtymist]{.recon .iv lang=preoe sort=ytymist role=source_protoform},
and attested [*ȳtmest*]{.iv lang=oe sort=ytmest role=evidence_form}
'furthest'. Mutation precedes the loss of the medial high vowel.
Skipping that loss, while preserving subsequent unrounding and lowering,
gives [ȳtemest]{.pred}. That variant is also attested: Ringe and Taylor
explicitly analyse it by analogy with *yfemest* and similar forms.
It fails the specified regular history to *ȳtmest*, not the entire Old
English lexicon [@RingeTaylor2014, p. 267].
The transmitted mutation is independently described by Hogg and Campbell;
it is not inferred from the need to make this derivation succeed
[@HoggGrammar2011, pp. 120--121, §5.76, p. 219, §6.10;
@Campbell1959, pp. 80--81, §203].

Hogg's [gaduling]{.recon .iv lang=preoe sort=gaduling role=source_protoform}
gives [*gædeling*]{.iv lang=oe sort=gaedeling role=evidence_form}
'companion'. Its light first syllable preserves the medial high vowel
through syncope; mutation-produced *y* then unrounds and lowers.
Unrestricted deletion predicts [gædling]{.pred}; omitting weak unrounding
leaves [gædyling]{.pred}. This supplies an independent later-stage
light-root retention control without presuming a new inherited compound
[@HoggGrammar2011, pp. 120--121, §5.76, p. 219, §6.10].

The bailiff reconstruction provides a second, strictly stage-level
control: [skuldihātijā]{.recon .iv lang=preoe sort=skuldihatija role=source_protoform}
becomes [sċyldihǣtjā]{.recon .iv lang=preoe sort=scyldihatja role=source_protoform},
with medial *i* lost in [*sċyldhǣta*]{.iv lang=oe sort=scyldhaeta role=comparison_form}
'bailiff' [@RingeTaylor2014, p. 267].
The syncope component correctly deletes that *i*. Its complete suffix
derivation is not certified: subordinate prominence on the long second
root is not fully represented, and the current model shortens its vowel.
This limitation must not be concealed by substituting a convenient short
reconstruction or adding a lexical repair.

The inherited [wiđuwōn]{.recon .iv lang=pgmc sort=widuwon role=source_protoform}
and Old English [*widuwe*]{.iv lang=oe sort=widuwe role=comparison_form}
'widow' independently corroborate the retained medial vowel
[@Orel2003, p. 462].
The selected root-vowel variant
[*wuduwe*]{.iv lang=oe sort=wuduwe role=evidence_form} retains that same *u*.
Removing the weight restriction predicts [wudwe]{.pred}. This is a complete
selected negative control for the general high-vowel component, not a
complete discriminator of the former early compound-only formulation.
Its root-vowel history remains with
[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut).

## SC115. The bounded high-vowel component (`OEHighLinkSyncope`) {#rule-OEHighLinkSyncope}

```foma
define OEHighLinkSyncope FootCtx([
    [{*i}|{*u}|{*y}] -> 0
        || .#. OEAnyConsonant* [
            [EnglishStarLongVowel | EnglishStarLongDiphthong] OEAnyConsonant+ |
            [EnglishStarShortVowel | EnglishStarShortDiphthong]
                OEAnyConsonant OEAnyConsonant+
        ] _ OEAnyConsonant EnglishStarVocalic
]) .o. FootCtx([{*y} -> {*i} || EnglishStarVocalic OEAnyConsonant+ _])
    .o. Ctx([{*ì} -> {*i}, {*ù} -> {*u}, {*ỳ} -> {*y}]);
```

This support component serializes the high-vowel part of
[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) after
mutation and before weak-vowel lowering. It is not a new older-name law.
The following singleton consonant and vowel identify a bounded open
medial domain; arbitrary onset clusters are not silently treated as a
complete syllabification. The existing adjacent-*l* component retains
its own source-backed scope. The support component also serializes short weak *y* unrounding before
the ordinary *i/e* merger. Hogg independently describes *u* mutation,
early unrounding, and eventual *e*; the selected site after syncope is a
technical serialization, not a demonstrated unrounding-after-syncope
edge. Both operations preserve the relevant high-vowel weight contrast.
Initial root *y* and subordinate *ỳ* are excluded from weak unrounding
[@HoggGrammar2011, p. 219, §6.10 and note 1].
Final decoding removes surviving secondary
high-vowel stress annotations, not historical stress itself.

The conditional *seleweard* derivation now retains *i*, allows its regular
mutation of the first root, and lowers it to unstressed *e* without
breaking. It does not independently prove that the compound preceded
syncope. Older names therefore remain substantive historical evidence
outside the completed account, not a list of lexical exceptions.

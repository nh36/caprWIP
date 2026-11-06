# Compound linking syncope

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

Those discussions concern several distinct developments: modification and
shortening within obscured second roots, connecting-vowel insertion, and
weak-vowel quality changes do not by themselves demonstrate deletion of a
linking vowel. For syncope, the relevant distinction is between short
nonhigh vowels, whose loss does not require a heavy first syllable, and
high linking *i/u*, whose loss requires that weight condition. The handbooks compare retention in
light-root *Winifrið/Winefrið* and *duruweard* 'doorkeeper'
with loss in *dælnimend* 'partaker' and *handclāð* 'towel'
[@Campbell1959, p. 143, §341; @Campbell1959, pp. 145--146, §§348--353;
@HoggGrammar2011, pp. 220--223, §§6.14--6.19;
@RingeTaylor2014, pp. 266--267; @SieversBrunner1965, pp. 137--138, §§167--168].
These are comparison forms, not additional selected
derivations. Variant first stems and the *hild-/hilde-* material require
source-critical analysis rather than an automatic rule conditioned by the
identity or weight of the second member [@RingeTaylor2014, p. 303].

The handbook comparisons do not yet provide a selected complete history
testing the newly restricted high-vowel clause. In particular, Orel
reconstructs Proto-Germanic [đura-warđaz]{.recon .iv lang=pgmc sort=durawardaz role=source_protoform} 'doorkeeper', with an *a*-linker,
and compares Gothic [*daura-wards*]{.iv lang=goth sort=daurawards role=comparison_form} 'doorkeeper'; Kroonen derives the
Old English simplex [*duru*]{.iv lang=oe sort=duru role=comparison_form} 'door' from [durō-]{.recon .iv lang=pgmc sort=duro role=source_protoform}. Neither fact
establishes an inherited short linking *u* in [*duruweard*]{.iv lang=oe sort=duruweard role=comparison_form} 'doorkeeper', nor an
independently demonstrated change supplying it before syncope.
Its attested vowel cannot simply be substituted into the earlier
compound reconstruction. The retained name vowels also need their own
formation histories: Sievers and Brunner distinguish metrically old
name forms with light-root vowel loss. These qualifications do not
revoke the handbook weight contrast, but they prevent schematic
stage controls from becoming complete lexical certificates by
assumption [@Orel2003, p. 79; @Kroonen2013, p. 110;
@SieversBrunner1965, pp. 137--138, §168].

No new lexical selection is made on that incomplete basis. The selected
high-vowel domain remains untested by an independently established
complete compound history. [*reġnboga*]{.iv lang=oe sort=regnboga} 'rainbow' and [*eorþcunde*]{.iv lang=oe sort=eorthcunde} 'earthly'
remain genuine selected *a*-deletion witnesses, not evidence for the
new high-vowel restriction. The executable correction has component
controls, but that is a different evidential claim from full lexical
validation.

Barrack's weak-vowel fronting and quality rules 333a/b and his rounding
rule 335 belong to this wider discussion, but are not equivalent
linking-vowel deletion laws. Their formal ordering is not independent
evidence for dating syncope or removal of secondary stress
[@Barrack1975, pp. 82--84].

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
    {*a} -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _ OEAnyConsonant+ PGmcStarGraveVowel
] .o. [
    [{*i}|{*u}] -> 0
        || [
            [PGmcStarAcuteVowel & EnglishStarLongVowel] OEAnyConsonant+ |
            [PGmcStarAcuteVowel & EnglishStarShortVowel] OEAnyConsonant OEAnyConsonant+
        ] _ OEAnyConsonant+ PGmcStarGraveVowel
]);
```

The two clauses keep nonhigh deletion separate from high-vowel loss.
For the latter, the represented heavy patterns are a long primary vowel
followed by consonant(s), or a short primary vowel followed by at least
two consonants. The annotated stress inventory and consonant strings
are a bounded executable proxy, not a complete syllabification of all
historical compounds. In particular, the right-hand consonant sequence
does not independently guarantee an open linking syllable, and not every
historical long or diphthongal stressed vowel has a corresponding accent
token. The cited handbooks' historical conditions remain distinct from
those representational limits.

The *reġnboga* test exposes an annotation dependency rather than an
independently dated historical sound-change boundary. If the grave is
removed before syncope, its licensing information is lost. Early lowering
changes the vowel, not this dependency; the annotation's lifetime does not
date a universal loss of compound secondary stress. The handbooks place
weakened compound junctures with the behavior described under
[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and
[SC036 OEInterStressRaising](#rule-OEInterStressRaising).

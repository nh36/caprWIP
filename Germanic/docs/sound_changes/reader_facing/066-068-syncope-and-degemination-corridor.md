# Late syncope and degemination

## Historical discussion of late syncope and degemination

Once later medial syncope begins to bite, the language inherits new consonant clusters that do not always remain stable. Hogg and Ringe and Taylor both describe this connection between vowel loss and later consonant simplification, while Brunner's discussion of *netle* ‘nettle’ beside later *netele* keeps the syncope evidence tied to a concrete lexical type [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2; @SieversBrunner1965, pp. 144--145, §§158--159]. Fulk is especially useful for the larger timing, because he places this syncope after i-umlaut [@Fulk2018, p. 91, §5.6].

The resulting chapter has an uneven center of gravity. Syncope itself is well motivated, one downstream degemination rule has a clear lexical breakpoint, and the dental assimilation step between them is plausible without yet being independently well anchored. That imbalance is part of the point. The sequence shows how the transducer can make a narrow chain of consequences explicit without pretending that every member has the same evidential weight.

## SC066. L-adjacent syncope in medial syllables (`OELAdjacentSyncope`) {#rule-OELAdjacentSyncope}

The syncope rule is stated directly.

```foma
define OELAdjacentSyncope [
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
];
```

In prose, it deletes medial \emph{*i} before \emph{*l}, creating forms such as *netle* ‘nettle’ and *spinl* ‘spindle’.

Its chronology is explicit on both sides. If the rule is moved before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*nátilōn} yields *nætle* rather
than expected OE *netle* ‘nettle’, and PGmc \emph{*spénnilō} yields *spenl*
rather than expected *spinl* ‘spindle’. If the rule is delayed until after
[SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination), PGmc \emph{*spénnilō} yields *spinnl* rather than expected *spinl*. This shows that
[SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope), and that
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) must come before
[SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination).

The checked forms therefore place the rule in a wider late-syncope interval. The later relation to [SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination) is the nearer local result; the earlier boundary at [SC055 OEIUmlaut](#rule-OEIUmlaut) mainly shows that this syncope belongs after the umlautal phase described in the handbooks. CAPR keeps it here as the opening step in the syncope-and-cluster-simplification sequence.

## SC067. Dental assimilation in newly formed clusters (`OEDentalAssimilation`) {#rule-OEDentalAssimilation}

The dental repair step is formally very short.

```foma
define OEDentalAssimilation [
    {*θ} -> 0 || {*t} _
];
```

In prose, it removes \emph{*θ} after \emph{*t} when syncope has created an over-heavy dental cluster. That kind of cluster simplification is historically plausible as part of the same late sequence that follows syncope [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC067 OEDentalAssimilation](#rule-OEDentalAssimilation) before or after any specific neighboring change.

That makes the rule best read as a narrow intermediate step inside the late syncope sequence. It is useful in the derivation, but the present evidence does not justify treating it as a stronger chronology anchor than it is. The handbooks support the broader pattern of syncope followed by cluster simplification, while CAPR states this dental simplification as a separate step. The placement is therefore historically plausible but approximate, not a tightly fixed local ordering.

## SC068. Preconsonantal degemination before sonorants (`OEPreconsonantalDegemination`) {#rule-OEPreconsonantalDegemination}

The final degemination rule is written as one composed definition.

```foma
define OEPreconsonantalDegemination OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN;
```

In prose, it simplifies doubled \emph{*tt} or \emph{*nn} before a following sonorant. The historical logic is straightforward enough. Once syncope has created a cluster such as the one behind *spinl* ‘spindle’, the doubled consonant does not remain [@RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

Its positive evidence is one-sided but exact. If the rule is moved before
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope), PGmc \emph{*spénnilō}
yields *spinnl* rather than expected OE *spinl* ‘spindle’. No later real break
is currently available before the current search boundary. This places
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) before
[SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination),
while the later side remains one-sided.

That one-sided profile is still meaningful. The rule is clearly later than the syncope that creates the offending cluster, but the current evidence does not yet force a sharper later boundary beyond that.

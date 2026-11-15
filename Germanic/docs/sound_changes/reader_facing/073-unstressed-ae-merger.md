# Unstressed ae-merger

## SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger SentenceCtx([
    [{*æ} -> {*e} || .#. {*ᶠ} OEAnyConsonant* _]
    .o. FootCtx(OEWeakTailReduction3)
]);
```

The rule merges unstressed \emph{*æ} with \emph{*e} after shortening has
produced the weak final vowels, yielding the ordinary OE \emph{-e} spellings.

Pretonic vowels also participate. A positively identified weak initial
syllable is eligible without the preceding-vowel condition appropriate
to post-tonic endings. The superscript `*ᶠ` records this prosodic
information, not a segment or a grammatical prefix. Stressed roots are
not thereby included in the merger. Later lowering of pretonic
\emph{*i}, including the early *gi-* of *gistīga* 'climb into/onto',
belongs to [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction);
Hogg places it marginally after the earlier merger
[@Campbell1959, pp. 153--155, §§369--370;
@HoggGrammar1992, §§6.50--6.54 (held 2011 reprint, pp. 237--239);
@RingeTaylor2014, pp. 334--335].

The earlier displacement tests expose implementation dependencies. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [nḗdrōn]{.recon} ‘adder’ yields [*nǣdræ*]{.pred} rather than expected OE *nǣdre* 'adder', and PGmc [fádēr]{.recon} ‘father’ yields [*fædær*]{.pred} rather than expected *fæder* 'father'. That experiment requires shortening before merger in its tested implementation; it is not newly remeasured here.

The toe boundary has also been rechecked on the
[reviewed final-nasal candidate](https://github.com/nh36/caprWIP/commit/4b232d22ad3d55ecf0eb2111b736dcf4349a4bde).
Its unperturbed derivation has a palatal fricative and unstressed
\emph{æ}, then merger supplies \emph{e} before loss creates hiatus.
Contraction yields OE *tā* 'toe'. Two separately executed displacements,
moving [SC085 OEHLoss](#rule-OEHLoss) before merger and moving merger after
loss, both instead leave \emph{ā + æ}: the merger's consonantal context is
gone, and contraction does not resolve that sequence. Both yield
[*tāæ*]{.pred} rather than *tā* 'toe'. This reproduces the endpoint in the
[earlier merger-displacement record](https://github.com/nh36/caprWIP/commit/25ca025f5b065671092fc8c7a4107611588cdcf9),
but now with the candidate's actual intermediate forms. It remains a
computational boundary observation, not independently demonstrated
historical merger-before-loss chronology.

Clay makes the distinction important. Corpus 207 *thoae* 'clay', beside
Épinal 3 *thohae* 'clay', is read as hiatus *thōæ* 'clay' beside
h-bearing *thōhæ* 'clay' [@Sweet1885, pp. 36, 41;
@RingeTaylor2014, p. 314, §6.9.3].
If written \emph{ae} preserves distinct unstressed \emph{æ}, this form
instead places loss before merger. If the spelling does not distinguish
\emph{æ} from \emph{e} here, it cannot decide their relative order.
The spelling question remains open: the current stage trial has
\emph{e}, not \emph{æ}, in hiatus, and its successful contraction is
not a philological argument for identifying the two.
The parallel account under [SC085 OEHLoss](#rule-OEHLoss) keeps this
conditional historical interpretation separate from the toe displacement.

# The Conditioning of Early Germanic *i > e*: Historiography, Comparative Evidence, Chronology, and Computational Adjudication

Adoption cross-reference, 16 October 2026: the explicit subsequent decision
adopts Candidate B and independently attested *leorn-* selections; see
[`sc015-adjudication.md`](../sc015-adjudication.md).
The recommendations, counts and receipts below describe the historical
research state, not the subsequently adopted corpus or canonical verdict.
Its counterevidence remains substantive and is retained in the adoption.

**Internal research report on SC015 (`PNWGmcILowering`).** Research and
experimental adjudication only. No production sound law, lexical selection,
chronology edge, registry verdict, frozen baseline or reader-facing chapter
was changed. The earlier bundle
`Germanic/docs/sound_changes/audits/sc015-hill-investigation/` is preserved
as the historical record of the first (pre-*wether*-correction) round; this
report supersedes its experimental figures but not its archival status.

**Supplementary assessment, 16 October 2026.** Read
[`COUNTEREVIDENCE_SUPPLEMENT.md`](COUNTEREVIDENCE_SUPPLEMENT.md) for the
current research recommendation. It withdraws the unrestricted B/C adoption
recommendation below: *twizna-* challenges the broad *z* component, the
numeral adverbs remain conditional controls, *beðinn* corrects the Norse
participle evidence, and a corrected nasal-plus-consonant A has now been
tested. The historical experimental observations below are preserved.
Production and the canonical verdict remain unchanged.

| Item | Value |
|---|---|
| Base commit | `a4c4aa5a803d5c6004a3ea92220d798c5c91ad92` (`update`) |
| `Germanic/fsts/germanic.txt` sha256 | `6c33b3c723150b61de4a41c89e228f32eeceb8280114b573e182eb8baf6ff51f` |
| `Germanic/data/germanic-aligned-final.tsv` sha256 | `1fd8ec257581a54603b59835a46ca764ee2ba0f438c9b497b874a58ee2fe8f73` |
| Selected rows / baseline mismatches | 387 / 8 (IDs 1973, 2013, 2030, 2162, 2224, 2240, 2298, 2300) |
| Live SC015 firings (canonical census) | 3: meed (2124), nest (2137), world (2302) |
| Protected-file digest before == after | yes (215 files, `canonical_protection.unchanged = true`) |
| Receipts | `experiments.json.gz`, `chronology.json`, `provenance.json` |

---

## 1. Research question and methodological principles

SC015 is the executable proxy for the disputed early Germanic lowering of
stressed short *i* to *e*, historically known as the "a-umlaut of *i*". The
production rule lowers a stressed first-syllable *i* when a coronal cluster
intervenes between it and a following non-high vowel, provided no velar
consonant precedes the vowel anywhere in the word-initial interval
(`germanic.txt` l. 2417–2421; see §9 for the exact text). The research
question is whether that formulation represents the best-supported historical
generalization, and if not, which of three historically motivated alternatives
does.

The three hypotheses compared are:

- **Traditional:** stressed *i > e* before a non-high vowel in the next
  syllable, blocked by intervening *j* or nasal+consonant
  [@Streitberg1896, pp. 56–57; @Noreen1923, pp. 50–51; @Campbell1959,
  pp. 43–44].
- **Hill:** lowering conditioned by the immediately following consonant,
  specifically tautosyllabic *z*, the cluster *st*, and *r*, not by the
  following vowel [@Hill2017, pp. 153–158].
- **Hybrid/layered:** a narrower common innovation (or innovations) followed
  only by independently justified later processes — i-mutation, Gothic
  breaking, Norse a-umlaut, southern West Germanic lowering before
  labials/velars — each with its own positive evidence
  [@RingeTaylor2014, pp. 33–36; @Fulk2018, pp. 56–59; @Cercignani1980,
  pp. 129–131].

Methodological principles followed throughout (per
`RESEARCH_ADJUDICATION_PROTOCOL.md`):

1. Historical stage and conditioning are decided from cited secondary
   literature and comparative data, never from the position of the
   executable proxy or from output fit.
2. A shared Proto-Germanic or Proto-Northwest-Germanic innovation is a
   serious explanatory hypothesis; independent dialectal innovations and
   analogy are invoked only with positive evidence.
3. The project is neogrammarian: candidate rules are exceptionless and
   phonologically conditioned; no lexical or grammatical conditioning.
4. Supplementary comparative probes are kept separate from the live CAPR
   corpus; probes never become corpus rows.
5. Candidates are evaluated on four independent dimensions (§13), not a
   single weighted score.
6. All experiments ran as isolated temporary Foma builds through the
   protected runner `Germanic/tools/anglo_frisian_experiments.py` inside the
   backend container, with protected-file digests checked before and after.

Six reference works were newly ingested for this study (see
`INGESTION_MANIFEST.md`): Cercignani 2022, Howell 2024, Jasanoff 1973
(Google Vision OCR, because the JSTOR text layer destroyed macrons),
Kostakis 2025, Tarsi & Laker 2026, Scheungraber 2010. Hill 2017 was already
held and byte-identical. Hock 1973 and Howell 1988a/b, 1991a/b are not held
and are cited only through Hill and Fulk.

---

## 2. History of the traditional *a*-umlaut hypothesis

The handbook rule descends from the neogrammarian treatment of Germanic
vowel harmony. Streitberg's §68 is the sharpest early common-Germanic
formulation: before *ă ā* of the following syllable Proto-Germanic *i*
became *e* ("a-Umlaut") unless separated from it by *j* or nasal + consonant;
his examples are *nest*, *hegre*, *stege*, *bedenn*, *nedan*, and *wer*
[@Streitberg1896, pp. 56–57]. Two features of this original statement are
often lost in later compression. First, the blocker is explicitly
*nasal + consonant* ("Nasal Konsonanz"), not any nasal and not any cluster
[@Streitberg1896, p. 57]. Second, Streitberg immediately concedes that the
"lautgesetzliche Verhältnis" has been heavily disturbed by analogy
[@Streitberg1896, p. 56] — the rule and the escape clause were born together.

Hirt's §34 generalizes the harmony: a second-syllable *a* (also *ā, o*)
pulls the stressed vowel "in der Richtung nach *a*", so *i > e* and *u > o*;
he calls the *i/e* part perhaps common Germanic outside Gothic but much
disturbed by analogy and by unknown conditions [@Hirt1931, pp. 45–46]. He
already records the two facts that would later dominate the debate: the
class I participles "durchaus *i* haben", even in Old High German, and Kock's
observation that in Norse the lowering fails after immediately preceding
palatal *k/g* [@Hirt1931, p. 46]. Hirt reports the latter as a *North
Germanic* restriction.

Noreen's Old Icelandic grammar is the classic Norse statement: stressed *i*
in a short syllable becomes *e* when the next syllable contains *a* or open
*o*, without intervening *j* or nasal + consonant, "ausser wol nach *g* und
*k*" [@Noreen1923, pp. 50–51]. This is the textual source of the
preceding-velar restriction. It is restricted to short syllables and to
Norse.

Luick is noticeably more sceptical for English. He states the *u > o*
conditions in the traditional way [@Luick1914, pp. 104–105], but separates
*i > e* from it: IE *i* became *e* only "in einigen Fällen" before a
mid-height following vowel when not blocked by *i* or "gedeckter Nasal", and
Old English offers only *wer*, *nest* and isolated *spec*; the change "seems
bound to further unknown conditions" and may have differed by dialect
[@Luick1914, pp. 108–109]. Bülbring gives the following triggers as *ă, ŏ, z*
or *ë* with no long/covered nasal and no *i/j* intervening, contrasting
*nest, wer* with *bite, biddan* [@Bulbring1902, §81, pp. 34–35].
Sievers–Brunner frame the matter as a redistribution of Germanic *e, i, u*
and note that Old English has *e* for *i* only in some cases before following
*a*, chiefly *wer* and *nest*, while many comparable words keep *i*
[@SieversBrunner1965, pp. 34–35].

Campbell is the most compact English formulation: "*i > e* before mid and
low vowels", shown in Old English only by *nest*, *wer*, and *spec* beside
*spic*; §§115–116 make the parallel *u > o* more regular and state that the
redistribution does not occur before a nasal followed by another consonant
[@Campbell1959, pp. 43–44]. Hogg (with Fulk) repeats the Old English
minimalism — *nest*, *wer*, one *speċes* beside usual *spiċ* — and observes
that weak class II verbs like *clipian* and *leofaþ* show no trace of the
change [@HoggGrammar2011, p. 54].

Lloyd's survey summarizes the pre-1966 field: Streitberg, Osthoff, Kluge,
Hirt and Prokosch treated the change as Proto- or Common Germanic (Kluge,
Hirt and Prokosch already limiting it); Paul, Kock and Krahe assigned it to
separate dialect prehistories; Bremer denied the sound law; Braune–Mitzka and
Wilmanns merely registered the *e*-forms [@Lloyd1966, p. 738]. The
"traditional" hypothesis was therefore never a single consensus; it was
always divided between common-Germanic, dialectal, limited and sceptical
versions.

**Precise traditional rule.** Synthesizing the sources: stressed short *i*
in a short syllable > *e* / _ C₀ V[−high], where C₀ contains no *j* and no
nasal + consonant; Norse additionally blocks after immediately preceding
*g/k*. No traditional West Germanic source was found that blocks lowering
after a preceding velar, or that blocks it after an intervening labial or
velar; the labial/velar material belongs to the *u > o* literature and to
umlaut-failure studies [@Cercignani1980, p. 130; @HowellSalmons1988,
pp. 84–87]. This matters for §9: the production rule's onset-velar guard
has no traditional WGmc pedigree.

---

## 3. Structuralist and analogical critiques

The structuralist reinterpretation began from phonemic status. Marchand's
theory — adopted by Moulton and initially Antonsen — treated early "umlaut"
as producing complementary *i/e* and *u/o* distributions, later phonemicized
in North and West Germanic when the determinants were lost, and levelled away
in pre-Gothic [@Cercignani1979, pp. 72–74]. Van Coetsem doubted full
complementarity even if *u*-umlaut was Proto-Germanic [@Cercignani1979,
p. 72]. Antonsen later abandoned the one-phoneme position, and Cercignani
stresses that *e > i* before *u* is secure only in Old Saxon and Old High
German, not in North Germanic or Anglo-Frisian [@Cercignani1979, pp. 74–75].

Lloyd 1966 is the decisive sceptical treatment and must be represented
precisely. He asks whether a phonetic change can be maintained when *e* and
*i* vary chaotically between and within dialects: either a sound change was
later obscured by analogy, or there was no change and every *e*-form is
analogical [@Lloyd1966, p. 739]. His first counterexample is the class I
strong participle: OHG *rītan, reit, ritum, giritan* keeps *i* throughout,
whereas class II regularly shows *u > o* in *gilogan* [@Lloyd1966, p. 739].
He rejects Streitberg's defence (zero-grade presents shifting to class V,
OHG *wesan*) on morphological grounds [@Lloyd1966, pp. 739–740] and restores
the participles as "vitally important" evidence that no regular change
occurred [@Lloyd1966, p. 740]. His methodological points follow: Latin
loans with *e* for *i* may reflect Vulgar Latin lowering [@Lloyd1966,
p. 741]; noun doublets like *spic/spec*, *skif/skef* do not prove a phonetic
alternation [@Lloyd1966, pp. 741–742]; and, most damagingly for a
following-vowel law, uninflected adverbs *hina, hinana, nidana* keep *i*
before *a* where no paradigm offers a source for analogy [@Lloyd1966,
p. 741].

Lloyd's positive alternative is systemic analogy: IE *e* split into Germanic
*e* and *i* by environment while IE *i* stayed /i/, creating partial overlap;
occasional extension of the *e* allophone into inherited /i/ words produced
*nest, spec, skef* without a sound law [@Lloyd1966, pp. 742–744]. He
concludes that "the so-called a-umlaut of *i* in Proto-Germanic did not
exist" [@Lloyd1966, pp. 744–745]. Two qualifications are essential. Lloyd
disproves a *wholly regular vowel-conditioned* law, not every early
lowering; and he himself allows a special influence of following *r* in
*wer* [@Lloyd1966, p. 744 n. 9]. That footnote is the seed of the consonantal
hypothesis.

Cercignani's 1979 and 1980 articles are anti-complementarity arguments, not
denials of all lowering. He argues that *i* and *e* remained independent
phonemes, that *e*-raising before *u* is OS/OHG only, and that positions
such as original *-e* and monosyllables preserve the contrast
[@Cercignani1979, pp. 73–76]. In 1980 he rejects Proto-Germanic allophony,
assigns early "umlauts" to the individual prehistories, states that *i > e*
before *a* was consonantally influenced, and — crucially for CAPR — warns
that the North Germanic retention after *k/g* cannot be transferred to West
Germanic, since OHG has *skif/skef* and *ginēn/genēn* [@Cercignani1980,
pp. 129–130]. He explains the scarcity of *e* by resistance to merger with
inherited *e*, not by absence of assimilation [@Cercignani1980, p. 131].

On the specific morphological battleground, Jasanoff's third-weak-class
article makes *learn* a problem of inherited morphology. He derives CGmc
*liznaiþ(i)* as the regular middle 3 sg. to an IE nasal present, parallel to
*kunnaiþ(i)*, tying OHG *lirnēn, lernēn* (= OE *liornian*) to Gothic *lais*
[@Jasanoff1973, p. 865]. On p. 868 he warns that Upper German *lirnēn* "for
phonologically regular *lernēn*" can as easily come from a lost 3 sg.
*lizniþ* as from a questionable 1 sg. *lizn(i)jō* [@Jasanoff1973, p. 868].
Jasanoff thus *assumes* that *lernēn* is the phonologically regular outcome
and treats the *i*-forms as paradigmatically motivated.

Seebold's entry *BEID-A-* gives ON *bíða, beið, biðo, bedenn (!)* and says
the participle either uniquely preserves the sound-law-expected *e* of a
class I participle or, "more probably", was formally influenced by *bed-ja-*
'ask', as in Old English [@Seebold1970, pp. 94–95]. Hock 1973 (not held) is
reported by Hill as rejecting older morphological explanations of the
participles but proposing influence of the infinitive, which Hill rejects
because it would yield *bītanaz*, not short-vowel *bitanaz* [@Hill2017,
pp. 151–152]; Fulk finds Hock insufficiently discriminating among classes of
forms [@Fulk2018, p. 58 n. 5].

---

## 4. Modern comparative accounts: Ringe–Taylor, Fulk, Cercignani, Hill

**Ringe & Taylor** prefer a restricted West Germanic history. They formulate
Northwest Germanic *u > o* as broadly regular before a non-high vowel unless
*j* or a coda nasal intervened [@RingeTaylor2014, pp. 33–34]. For *i* they
posit only a modest *southern* West Germanic lowering, usually before labial
and velar obstruents followed by non-high vowels — OHG *quec, wehha, lebēn,
spek, lebara, klebēn, leckōn, stegōn* — with conditioning that is "messy"
but partly phonological and with later Frankish spread northward
[@RingeTaylor2014, pp. 34–35]. For *nest* and *wer* they reconstruct PGmc
*nistaz* (*nestaz??*) and *wiraz* (*weraz??*) and call the reason for *e*
"unrecoverable" if a WGmc-wide rule is not accepted [@RingeTaylor2014,
p. 34]. Zero-grade class I presents (*wigana, stikana*) are treated by
Lloyd-style analogical reinterpretation [@RingeTaylor2014, pp. 35–36]. For
*hēr* they infer short *hir* only indirectly and suspect that
lengthening/lowering is post-PNWGmc or has an alternative ablaut explanation
[@RingeTaylor2014, p. 36]. In his 2017 Proto-Germanic volume Ringe likewise
calls OE/OHG *wer* an "irregular, and therefore unexpected" lowering
[@Ringe2017, p. 97] and leaves *nest* as reconstructing *nestaz??*
[@Ringe2017, p. 121].

**Fulk** is more hospitable to a real Northwest Germanic (or Proto-Germanic)
lowering, but with heavy analogy. PGmc *i* "might be lowered" to *e* before
a mid or low vowel; undeniable examples are *nest* and *wer*, with *spec*
beside *spic* the only other secure OE example [@Fulk2018, pp. 56–57]. He
stresses that *i/e* results are far less systematic than *u/o*, so inter- and
intraparadigmatic levelling is expected [@Fulk2018, p. 57]; his footnote
records Kock's preceding *g/k* restriction explicitly as North Germanic and
the standard *j* / nasal+consonant blockers [@Fulk2018, p. 57 n. 3]. He uses
the participles differently from Lloyd: retained *i* in *gistigan* demands
explanation, but analogical influence from the present is plausible, and ON
*beðinn* "probably" preserves the expected lowered participle
[@Fulk2018, pp. 58–59].

**Cercignani 2022** reframes the same facts as "distance assimilation":
*e > i* before nasal+consonant or high front sounds, and *i > e* before a
low or mid vowel as in OHG *spek, lebēn, leccōn*; complementary distribution
is still rejected because contrasts and analogical reintroductions presuppose
independent phonemes [@Cercignani2022, pp. 45–47]. His 2022 examples are
again southern WGmc labial/velar cases — the same stratum Ringe–Taylor
isolate.

**Hill 2017** is the fullest consonant-conditioned alternative. Hill argues
that following-vowel lowering fails most clearly in the class I participles
(*u* lowers in class II; *i* does not in class I) [@Hill2017, pp. 150–151]
and in the uninflected adverbs *hina, hinana, nidana* [@Hill2017, p. 152].
He proposes that lowering depended on the immediately following consonant:
before tautosyllabic *z* (*iz > er*, *hiz > hē/her*, *mizdōn > meord/mēd,
miata*), before *st* (*nistan > nest*), and before *r* (*wiraz > wer*,
probably *hir > hēr*), but *not* before *sk* (*fiskaz, wiskō, diskaz*)
[@Hill2017, pp. 153–156]. He explains *nistan* 'to nest', *list*
(< *lẹstiz*), and *liornian/lirnēn* as lowered forms later raised by North
and West Germanic i-mutation [@Hill2017, p. 153]. He restricts the *sk/st*
contrast to stressed syllables, noting that unstressed *-isk, -isto* keep *i*
[@Hill2017, p. 155]. On date he is cautious: before *r* the change may be
Proto-Northwest-Germanic or Proto-Germanic, since Gothic *wair* is explicable
either by inherited lowering or by Gothic breaking, and Gothic *is, mizdo*
could have raised secondary *ẹ* back to *i* [@Hill2017, p. 156]. His
chronological argument for *hēr* is treated in §8.

---

## 5. Howell and the phonetics of consonant-conditioned lowering

Howell 2024 concerns Gothic breaking, not a new pan-Germanic *i > e* law, but
it supplies the phonetic rationale that Hill's proposal otherwise lacks.
Howell describes Gothic breaking as the lowering of PGmc *i/e* to ⟨ai⟩ and
*u* to ⟨au⟩ before ⟨h⟩, ⟨ƕ⟩ and ⟨r⟩, with few exceptions [@Howell2024,
pp. 76–77]. He notes analogous consonantally conditioned lowerings across
Germanic but insists each change be viewed as independent even though the
phonetics recur [@Howell2024, p. 77]. His account emphasizes rhotics —
especially *coda* rhotics, which are the primary lowering environment
cross-linguistically, with onset rhotics secondary — and velar/post-velar
fricatives [@Howell2024, pp. 81–82]. More generally he argues that Gothic
breaking is one manifestation of a broader Germanic tendency for approximants,
especially *r* and weakened *h*, to condition vowel lowering [@Howell2024,
pp. 75–76, 90–91]. His "late Proto-Germanic" remark concerns the weakening
of *x* to [h] by c. AD 500 [@Howell2024, p. 85], not *i > e*.

Three consequences follow for SC015. (i) Lowering before *r* is
phonetically natural and attested independently in Gothic; it is the best
candidate among Hill's three environments for a genuinely old, possibly
common development. (ii) Lowering before *z* and before *st* has no
comparable phonetic rationale in Howell; *z* and *s* are coronal fricatives,
not approximants. If they lowered a preceding *i*, that must be argued on
distributional, not phonetic, grounds. (iii) Howell's insistence that similar
phonetics recur independently means that Gothic *wair* cannot by itself
date *wiraz > weraz* to Proto-Germanic; Hill concedes exactly this
[@Hill2017, p. 156].

Kostakis 2025 bears on the nasal blocker rather than on *i > e* itself: he
argues that early Germanic coda nasals were specified [low], which explains
why Northwest Germanic a-umlaut (of *u*) was blocked by a coda nasal and
links this to pre-nasal raising and Old Norse lowering [@Kostakis2025,
pp. 1–7]. This gives the traditional *nasal + consonant* blocker a
phonological rationale, but only as a *coda* nasal: it does not support
excluding every nasal. Howell & Salmons similarly show that umlaut failure
can be phonologically coherent (vowel-space distance, intervening geminate
velars/labials), so a monolithic structuralist rule forced too much analogy
[@HowellSalmons1988, pp. 84–87].

---

## 6. Comparative analysis of the positive and negative evidence

This section evaluates each probe lexeme from the dictionaries and grammars.
Probes are supplementary comparative evidence and are not CAPR corpus rows;
the three live corpus witnesses are marked.

**nest (live, 2137, `*nístą` → `nest`).** PIE *nisdós* > PGmc *nistaz*,
but OE/OS/OHG *nest* "reconstruct" *nestaz??*, North and East Germanic
lacking the noun [@Ringe2017, p. 121; @RingeTaylor2014, p. 34]. Kroonen
*nista-* [@Kroonen2013, p. 391]; Orel *nistan* with Skt. *nīḍá-*, Lat.
*nīdus*, Lith. *lizdas* [@Orel2003, p. 287]. Environment: stressed *i*, *st*
from PIE *sd*, following *a*. Both the traditional rule and Hill's *st*
component predict *e*. It is the sole secure positive for *st*.

**meed (live, 2124, `*mízdai` → `meorde`).** PIE *misdʰó-* > PGmc *mizdō*,
OE *mēd ~ meord* [@Ringe2017, p. 121]; Kroonen explains WGmc *mēdō/miadō*
by sporadic loss of *z* before dentals with OE retaining a doublet
[@Kroonen2013, p. 370]; Orel *mizđō(n) ~ mēđō* [@Orel2003, p. 272]; later
cluster history in Ringe–Taylor [@RingeTaylor2014, p. 85]. Hill's positive
for tautosyllabic *z* [@Hill2017, p. 153]. Both traditional (following
*ō/ai*) and Hill (*zd*) predict *e*. Discriminates only together with
*fiskaz/wiskō*.

**wer 'man' (probe `wiraz`; in corpus only via world).** PIE *wih₁rós* >
PGmc *wiraz*, OE/OHG *wer* "irregular" lowering [@Ringe2017, p. 97];
Kroonen *wira-* with Goth *wair*, ON *verr* [@Kroonen2013, p. 588]; Orel
[@Orel2003, p. 463]; RT *wiraz* (*weraz??*) [@RingeTaylor2014, p. 34]. Hill's
paradigm *r* case [@Hill2017, p. 156]. Both hypotheses predict *e*; Gothic
*wair* is ambiguous because of breaking [@Hill2017, p. 156; @Howell2024,
pp. 76–82].

**iz, hiz, hir / hēr.** Hill's table gives OHG *er* 'he' and OE/OS/OHG
*hē/her* from *hiz*, grouped with *mizdōn* [@Hill2017, p. 153]; for *hēr* he
argues PGmc *hir > hẹr > hẹ̄r* before monosyllabic *-r* lengthening, yielding
Goth *hēr*, ON *hér*, OHG *hiar*, OE *hēr* [@Hill2017, pp. 156–158]. Kroonen
*hiar* notes Goth *hiri* presupposes *ki-r* [@Kroonen2013, p. 225]; Hill
analyses *hiri* as *hi-ri* with a morpheme boundary [@Hill2017, pp. 157–158].
*iz/hiz* are **not** following-*a* cases: a traditional rule cannot lower
them without an additional assumption (the following vowel is absent or
high). They are therefore genuine discriminants *for z*, provided the
pronominal forms are accepted as reflecting a lowered stage rather than
Gothic-like *is*. *hir* is the chronology probe for *r* (§8).

**wether (2283, `*wéθruz` → `weþer`).** Now reconstructed with inherited
*e*-vocalism (masc. u-stem *weþruz*, Kroonen p. 584; Orel *weþruz ~ weþraz*
pp. 459–460; previous adoption record in the lexical dossier). Not a lowering
witness under any hypothesis; `experiments.json` confirms `*wéθruz`,
`*wéθraz` and the superseded `*wéθrą` all yield *weþer* in every variant.
It is excluded from the diagnostics.

**world (live, 2302, `*wír-àldu` → `weorold`).** Orel *wira-aldiz*,
explicitly "compound of *wiraz* and *aldiz*", with ON *verǫld*, OE *weorold*,
OFris *warld*, OHG *weralt* [@Orel2003, p. 462]. The first member is
either inherited *wir-* (a parallel to *wiraz*) or already-established
*wer-*. Because *wer* 'man' is secure independently, world adds no evidence
beyond *wiraz*; it is a weak discriminant. Its role in CAPR is purely
chronological (§8, §12).

**fish, wisp, dish (negative controls).** Kroonen *fiska-* with Goth
*fisks*, ON *fiskr*, Lat. *piscis* [@Kroonen2013, p. 142]; Orel
[@Orel2003, p. 103]. Hill emphasizes that *fiskaz* is an a-stem secured by
Goth *fiskam, fiskans* and ON *fiska* with no lowering before *sk*
[@Hill2017, p. 154]. Orel *wiskō* with ON *visk*, OE *wisc* [@Orel2003,
p. 463]; Hill uses it likewise [@Hill2017, p. 154]. *diskaz* is a Latin loan
[@Hill2017, pp. 154–155; @RingeTaylor2014, p. 135] and so is weaker. These
are the strongest negatives against any rule in which the following vowel
alone suffices; they are the reason the production rule restricts the
intervening material to coronals.

**class I participles *bitanaz, biðanaz*; ON *beðinn*.** Hill reviews OHG
*gibizzan/gibitan*, OE *gebiten/gebiden*, ON *bitinn/stiginn/biðinn*, Goth
*bitans/stigans/bidans*: none shows the *e* a general following-vowel rule
predicts [@Hill2017, pp. 151–152]; Lloyd made this the principal argument
[@Lloyd1966, pp. 739–741]. ON *bedenn* is for Seebold either the lone
regular *e* participle or, more probably, influenced by *bed-ja-*
[@Seebold1970, pp. 94–95]; Fulk leans toward genuine preservation
[@Fulk2018, p. 59]. Negatives for the traditional rule unless wholesale
analogical restoration is assumed; neutral for Hill (single dental, no
*r/z/st*).

**nidana, hina.** Hill lists OHG *nidana*, OE *niðan, nioðan* and OHG *hina*,
OE *hinan, hionan* as unlowered *i* before *a* [@Hill2017, p. 152]; Orel
*niþanē*, *niþr(a)* [@Orel2003, pp. 287–288]; Kroonen *niþera-*
[@Kroonen2013, p. 391]. The ON *neðan* a-umlaut variation is Norse-specific
and cannot be projected to WGmc [@Noreen1923, pp. 53–54; @Hill2017, p. 152
n. 24]. Strong negatives against the traditional rule; neutral for Hill.

**lid (`*xlídą`, live corpus row 2100, not an SC015 witness).** Lloyd's
list of unchanged *i* includes OE *hlid*, OHG *(h)lit* [@Lloyd1966,
p. 738]; cf. Orel *xliđan* [@Orel2003, p. 176] (Kroonen has no
lemma for this noun). Single *d* + *a*: a negative for the traditional rule, neutral for
Hill. In CAPR it is protected only by the onset-velar guard (§9, §10).

**irh- 'chamois leather'.** Hill notes OHG *irh* would contradict lowering
before *r* if inherited, as Kroonen assumes, but judges it probably a loan
[@Hill2017, p. 156 n. 30]. Not a reliable counterexample.

**learn (live corpus rows 2095 `*líznōjaną`, 2313 `*líznô`, 2314
`*líznōθi`; targets *liornian, liorna, liornaþ*).** Kroonen *liznōn-* with
OE *leornian*, OFris *lirna/lerna*, OS *līnōn*, OHG *lernōn/lernēn/lirnēn*
[@Kroonen2013, p. 340]; Orel *liznōjanan ~ liznēnan* [@Orel2003, p. 247];
Jasanoff's *liznaiþ(i)* and the *lizniþ* explanation of *lirnēn*
[@Jasanoff1973, pp. 865, 868]; Scheungraber's rhotacism derivation
[@Scheungraber2010, pp. 74–75]; Tarsi–Laker's lexical-semantic placement of
'learn' as a West Germanic nasal present [@TarsiLaker2026, pp. 40–47];
Ringe–Taylor *liznō- ~ lizna-* > OE *liornian ~ leornian*
[@RingeTaylor2014, pp. 38, 84]. Environment *i + zn*. Under Hill's *z*
component *lezn-* is expected and the *i*-forms require a paradigm cell with
*i/j* (Jasanoff) or i-mutation (Hill). Under the traditional rule *zn* is
nasal + consonant… in reverse order; the classical blocker (*nasal*
followed by consonant) does not apply, but an intervening nasal is present
and the handbooks are silent on *zn*. CAPR's selected targets are the
*io*-forms, which do **not** show lowering. This lexeme is the most
consequential probe for the executable comparison (§10).

**nest-derivative, list, thistle (masking tests).** Hill treats OE/OHG
*nistan*, *list* and *liornian/lirnēn* as forms whose *i* may result from
later i-mutation after earlier lowering [@Hill2017, p. 153]; Kroonen *listi-*
[@Kroonen2013, p. 339]; Orel *listiz* [@Orel2003, p. 246]; Orel
*þe(x)stilaz* for thistle [@Orel2003, p. 419]. These cannot discriminate
unless the chronology of i-mutation is fixed; §12 tests whether CAPR's
`OEIUmlaut` actually performs the recovery.

**Southern WGmc *quec, wehha, lebara, spek*.** Campbell, Fulk and
Ringe–Taylor all list these [@Campbell1959, §114, pp. 42–43; @Fulk2018,
p. 57; @RingeTaylor2014, p. 34]. They are labial/velar environments, not
*r/z/st*; they belong to a separate, later-looking, dialectally bounded
stratum and must not be folded into SC015.

---

## 7. The evidence of strong-verb participles and weak class III morphology

**Correction, 16 October 2026:** the attested Norse participle of *bíða*
is *beðinn*, not *biðinn*. The supplement §3 reassesses this evidence
against Noreen pp. 326, 332, Seebold pp. 94–95 and Fulk pp. 58–59, 286;
its §4 qualifies the earlier confidence in the reconstructed *learn*
paradigm. The old experimental inputs and outputs remain unchanged.

Two morphological systems carry disproportionate weight.

**Class I participles.** The participle *-anaz* supplies the textbook
trigger (*a* in the next syllable) with only a single dental intervening, in
a category with many members and a secure paradigm. The uniform *i*
(*bitanaz, biðanaz, stiganaz*; OHG *giritan*) is therefore either (a) the
regular outcome, refuting a following-vowel rule, or (b) analogically
restored from the present and preterite plural. Lloyd takes (a)
[@Lloyd1966, pp. 739–740]; Fulk takes (b), aided by ON *beðinn*
[@Fulk2018, pp. 58–59]; Hill takes (a) and makes it his first argument
[@Hill2017, pp. 150–152]. Within CAPR's neogrammarian framework, (b) is
admissible only as a specific paradigmatic levelling with positive evidence.
The positive evidence for (b) is exactly one word, ON *beðinn*, which has an
equally good alternative explanation (contamination with *biðja*,
Seebold). The participles therefore count as evidence *against* the
traditional rule and are neutral to Hill. Note that CAPR holds no class I
participle with *-anaz* as a selected row; the probes `bitanaz`/`biðanaz`
are supplementary.

**Weak class III and *learn*.** Jasanoff's reconstruction of *liznaiþ(i)*
as a middle 3 sg. to a nasal present [@Jasanoff1973, p. 865], and his
explicit allowance that *lirnēn* may continue a lost *lizniþ*
[@Jasanoff1973, p. 868], means that the *i ~ e* alternation in 'learn' can
be morphological: cells with *-i-* (3 sg. *-iþ*, or a *-ja-* present) would
be protected from lowering or re-raised by i-mutation, cells with *-ō/-ai-*
would lower. Scheungraber's rhotacism argument [@Scheungraber2010,
pp. 74–75] confirms *z* was present when the WGmc forms were created.
Tarsi–Laker add that the nasal present for 'learn' is probably a West
Germanic lexical innovation [@TarsiLaker2026, pp. 42–43] — if so, the
lexeme postdates any Proto-Germanic lowering and could witness only a
PNWGmc/PWGmc stage. CAPR currently selects *líznōjaną*, *líznô*, *líznōθi*
→ *liornian, liorna, liornaþ*: the chosen *io*-forms are the *unlowered*
variants. Any candidate that lowers before *zn* will change these three rows
unless the selected inputs are revisited — a lexical question, not a
sound-law question, and outside this brief's authorization.

---

## 8. The three possible consonantal components and their relative chronology

Hill presents *z*, *st*, *r* as one rule. The comparative evidence supports
them unequally and dates them differently.

**Before *r*.** Positives: *wiraz > wer* (all NWGmc; Goth *wair*
ambiguous), *hir > hēr*. Negatives: only *irh-*, probably a loan. Phonetics:
natural (Howell). Chronology: Hill's *hēr* argument requires lowering before
*r* to precede the lengthening of monosyllabic place adverbs, which he
argues is Proto-Germanic because Goth *hēr* shows *ē* (not *ī*) and Gothic
otherwise merges *e/i* except by breaking [@Hill2017, pp. 156–158].
Ringe–Taylor doubt the inference [@RingeTaylor2014, p. 36]. If Hill is
right, *r*-lowering is Proto-Germanic and precedes monosyllabic
lengthening; the component experiment confirms the ordering dependency
(§12). This is the **strongest** component: multiple independent positives,
a cross-branch chronology argument, a phonetic rationale, no secure
counterexample.

**Before tautosyllabic *z*.** Positives: *iz > er*, *hiz > hē/her*,
*mizdōn > meord*; probably *liznōn-* (masked). Negatives: none secure.
Phonetics: no approximant rationale. Chronology: must precede the stage at
which *z* is no longer recoverable — i.e. before monosyllabic final *z*-loss
(which gives *ī*, not *ē*, if lowering has not applied; §12) and before the
sporadic *z*-loss before dentals that produces *mēd* [@Kroonen2013, p. 370;
@RingeTaylor2014, p. 85]. Rhotacism is a different matter: once *z > r*, the
*r*-component itself would lower *mird- > merd-* (§12), so the *z*
component is strictly necessary only for word-final *z* (*iz, hiz*) where
*z* is lost rather than rhotacized. Date: not demonstrably Proto-Germanic
(Gothic *is, mizdo* may be raised or unlowered). This is the **second**
component: good positives, but the pronominal evidence (*er, hē*) is from
forms with complex sandhi/stress histories, and the only non-pronominal
witness is *mizdō*.

**Before *st*.** Positives: *nistaz > nest* only; *list, nistijan, þistil*
are masked. Negatives: none, but *fiskaz/wiskō* show that the generalization
cannot be extended to *s* + obstruent. Phonetics: none. Chronology: must
precede i-mutation to be masked in *list*. This is the **most conjectural**
component: one lexeme, a tailor-made contrast *st ≠ sk*, no phonetic
rationale.

**Relative chronology among the components.** No comparative evidence
orders *r*, *z* and *st* relative to each other. The six orderings tested
(§10) give identical results on all 387 rows and all probes, because no input
contains two of the three environments competing for the same vowel. The
split is therefore historically meaningful (different confidence, possibly
different dates) but executably inert.

---

## 9. Formal definitions of Candidates A, B and C

All definitions use the stage-specific alphabet of `germanic.txt`
(`EnglishStarConsonant`, `EnglishStarNasal`, `EnglishStarNonHighVowel`,
`EnglishStarCoronal`). Only the unaccented and acute-accented *i* are
targeted, mirroring the incumbent. Full text is in Appendix B.

**Incumbent** (`germanic.txt` 2417–2421):

```foma
define EnglishStarNonVelarConsonant [EnglishStarConsonant - EnglishStarVelar];
define PNWGmcILowering Ctx([
    {*i} -> {*e} || .#. EnglishStarNonVelarConsonant* _ EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é} || .#. EnglishStarNonVelarConsonant* _ EnglishStarCoronal+ EnglishStarNonHighVowel
]);
```

Conditions: first-syllable *i*; one or more coronals (*d l r s t z ð θ*)
intervening; following non-high vowel; **no velar anywhere in the onset
interval**.

**Candidate A — traditional vowel-conditioned (`AFTradA`)**:
`_ [EnglishStarConsonant - EnglishStarNasal - {*j}]* EnglishStarNonHighVowel`,
onset `EnglishStarConsonant*` (no velar guard). Declared approximation: all
nasals are excluded from the intervening set, which is slightly stricter
than the handbooks' *nasal + consonant* (it also blocks single *n*, as in
*hina*). A second variant `AFTrad` keeps the incumbent's coronal restriction
but drops the velar guard, isolating the guard's effect.

**Candidate B — Hill unified (`AFHillB`)**:
`_ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}]`, onset
`EnglishStarConsonant*`, no vowel condition, no velar guard.
Preconsonantal/word-final *z* is the local proxy for "tautosyllabic". The
sensitivity variant `AFHillBz` admits any *z* (including intervocalic).

**Candidate C — decomposed**: `AFHillR` (`_ {*r}`), `AFHillZ`
(`_ {*z} [EnglishStarConsonant | .#.]`), `AFHillSt` (`_ {*s} {*t}`), composed
in all six orders (`AFCRZS` … `AFCSZR`) at the incumbent position, and
`AFCRZS` repositioned early (after `EAFLThVoicing`, before
`PWGmcDentalHardening`) and late (after `PWGmcUnstressedWordFinalIApocope`,
before `MonosyllabicFinalZLoss`).

Controls: `skip` (rule removed), `late-current` (incumbent rule moved after
`OEInterStressRaising`), `late-hill` (`AFHill` after `OEInterStressRaising`).

---

## 10. Complete-corpus experimental results

387 selected rows; canonical mismatches 8. "Changed finals" are rows whose
final output differs from the canonical output; "mismatch set" is the set of
rows whose final differs from the selected OE target. All figures from
`experiments.json.gz` (`variants[].changed_final_ids`,
`variants[].mismatch_ids`).

| Variant | Changed finals | Mismatches | Baseline 8 preserved | New mismatches |
|---|---|---|---|---|
| incumbent | 0 | 8 | yes | — |
| **A-trad** (`AFTradA`) | 8 | 16 | yes | fish 2014 *fesċ*; lick 2099 *leccian*, 2315 *lecca*, 2316 *leccaþ*; lid 2100 *hled*; live 2107 *lefeþ*; liver 2108 *lefer*; tick 2256 *tecca* |
| A-trad-coronal-noguard (`AFTrad`) | 1 | 9 | yes | lid 2100 *hled* |
| **B-hill-tauto** (`AFHillB`) | 3 | 11 | yes | learn 2095 *leornian*, 2313 *leorna*, 2314 *leornaþ* |
| B-hill-immediate-z (`AFHillBz`) | 3 | 11 | yes | same three |
| **C-RZS … C-SZR** (6 orders) | 3 | 11 | yes | same three (identical in all six) |
| C-early | 3 | 11 | yes | same three |
| C-late-z-before-zloss | 3 | 11 | yes | same three |
| skip | 3 | 11 | yes | meed 2124 *miorde*; nest 2137 *nist*; world 2302 *wuruld* |
| late-current | 1 | 9 | yes | world 2302 *wuruld* |
| late-hill | 3 | 11 | yes | learn ×3 |

**Reading the table.**

1. A faithful traditional rule (Candidate A) overgenerates heavily on the
   selected corpus: eight new wrong finals, all before labials or velars
   (*fisk-, likk-, xlid-, lib-, libr-, tikk-*). Of these only *fish* has a
   Hill-style account (no *sk* lowering); *lick*, *live*, *liver*, *tick* are
   precisely the southern WGmc labial/velar stratum where OHG *does* lower
   (*leckōn, lebēn, lebara*) and Old English does not. No paradigmatic
   explanation rescues them: *lid* and *liver* are nouns without
   *i*-bearing cells. Candidate A is refuted for Old English as a regular
   law.
2. Dropping the velar guard alone (`AFTrad`) breaks exactly one row, *lid*
   `*xlídą`. The guard is therefore a single-lexeme protector. Under
   Candidates B and C, *lid* is unaffected because single *d* is not a
   trigger — the guard becomes unnecessary under selective consonantal
   conditioning, as predicted. The synthetic grid (Appendix A.3) shows that
   the incumbent guard blocks *x-, k-, xl-* onsets before *r, st, zd* as well
   — environments where the comparative evidence (*hir > hēr*!) demands
   lowering. The guard is both historically unsupported (§2) and
   predictively wrong for *hēr*.
3. Hill's unified rule (B) and every Candidate C configuration produce
   **identical** corpus results: three changed finals, all the *learn* rows.
   The *wether* correction has removed the fourth change seen in the prior
   investigation. The residual learn change is a genuine prediction of the
   *z*-component — *lezn-* — and is historically *expected* (Jasanoff's
   "phonologically regular *lernēn*"; OE *leornian* is amply attested beside
   *liornian*). It conflicts with CAPR's *selected* targets, which are the
   *io*-variants. Whether to re-select *leornian* or to reconstruct the
   PROTOFORM with an *i*-bearing suffix cell is a lexical adjudication, not
   authorized here.
4. The tautosyllabic and unrestricted *z* variants agree on all 387 rows
   (and differ only on the intervocalic probe `wizana`, as before).
5. Removing the rule (`skip`) costs three rows; the incumbent earns its keep
   on meed, nest and world only.
6. `late-current` breaks world (*wuruld*): the vowel-conditioned incumbent
   depends on the second member's *à* still being present. `late-hill` does
   **not** break world: consonantal conditioning (*r*) fires regardless of
   the later vowel. The SC015→SC036 chronology edge is therefore an
   artefact of the vowel condition (§12).

**Intermediate changes without final change.** `C-early` and
`C-late-z-before-zloss` also alter intermediate checkpoints for meed, nest
and world (lowering simply happens at a different stage) and for *thistle*
2250 `*θístilas`: the *st*-component lowers it to `*θéstilas` and `OEIUmlaut`
restores *i* (*þistles* unchanged). B and C likewise lower thistle
intermediately at the incumbent position; the incumbent does not (following
*i*). Thistle is thus a live demonstration of Hill's masking mechanism
inside the production cascade.

---

## 11. Supplementary controls and historical counterexamples

Probe outputs through the full cascade (`supplementary_full_prefix_outputs`;
inputs normalized *h → x, þ → θ*; "CAPR OE output" is the string the complete
cascade emits, which for probes without a selected target is compared with
the comparative reflex).

| Probe (input) | Comparative reflex | incumbent | A-trad | B / C | skip | Verdict |
|---|---|---|---|---|---|---|
| *iz* | OHG *er* | *ī* | *ī* | **ē** | *ī* | B/C correct in timbre; length is the monosyllabic-lengthening proxy's business |
| *hiz* | OE *hē* | *hī* | *hī* | **hē** | *hī* | B/C correct; incumbent and A wrong |
| *hir* | OE *hēr* | *hir* | *hir* | *her* | *hir* | B/C correct timbre; no lengthening law in cascade |
| *wiraz* | OE *wer* | *wer* | *wer* | *wer* | *wir* | all candidates correct |
| *nístą* | *nest* | *nest* | *nest* | *nest* | *nist* | all correct |
| *mízdōn* | *meord* | *meorde* | *meorde* | *meorde* | *miorde* | all correct |
| *fískaz* | *fisċ* | *fisċ* | **fesċ** | *fisċ* | *fisċ* | A wrong |
| *wískō* | *wisċ* | *wisċu* | **wesċu** | *wisċu* | *wisċu* | A wrong |
| *dískaz* | *disċ* | *disċ* | **desċ** | *disċ* | *disċ* | A wrong (loan; weak) |
| *bítanaz* | *biten* | **betan** | **betan** | *bitan* | *bitan* | incumbent and A wrong |
| *bíðanaz* | *biden* | **bedan** | **bedan** | *bidan* | *bidan* | incumbent and A wrong |
| *nístjaną* | *nistan* | *nistan* | *nistan* | *nistan* | *nistan* | masked; all correct |
| *lístiz* | *list* | *list* | *list* | *list* | *list* | masked; all correct |
| *xína* | *hin-* | *hin* | *hin* | *hin* | *hin* | all correct (nasal excluded) |
| *wéθruz* | *weþer* | *weþer* | *weþer* | *weþer* | *weþer* | not a witness |

Component-level probes (Appendix A.1) add: *nidana* → incumbent/A *nedana*
(wrong), B/C *nidana*; *xlidą* → A *xledą* (wrong), incumbent/B/C *xlidą*;
*irxa* → A/B/C *erxa*, incumbent *irxa* (the incumbent's velar guard happens
to protect the probable loan); *bedinn* (`*bíðinaz`) unchanged in all
(following *i*).

**Important counterexamples to each hypothesis.**

- *Against the traditional rule (A):* the entire labial/velar set of §10
  item 1 plus *fiskaz, wiskō, bitanaz, biðanaz, nidana, hlidą*. Eleven
  secure negatives against three positives.
- *Against the incumbent:* *bitanaz, biðanaz, nidana* (lowered wrongly:
  single coronal + *a* suffices), *hiz, hir* (not lowered: no following
  non-high vowel; onset-velar guard), *iz* (not lowered). Five wrong
  predictions on the comparative set despite zero corpus cost.
- *Against Hill (B) and C:* *learn* (if the *io*-forms are regular rather
  than i-mutated); *irh-* (if inherited). Both are disputed in the
  literature on independent grounds [@Jasanoff1973, p. 868; @Hill2017,
  p. 156 n. 30]. No undisputed counterexample was found.

**Forms on which all candidates agree** (non-discriminating): *wiraz*,
*nístą*, *mízdōn*, *nístjaną*, *lístiz*, *xína*, *wéθruz*, and in the
corpus every row except learn ×3, lid, and the labial/velar set.

**Forms for which no candidate gives a satisfactory prediction:** none
among the probes once length is excluded. The *ē* of *hēr* and the *ē* of
*hē* are not produced by any variant because no monosyllabic lengthening law
exists in the cascade; that is a separate, unmodelled development
[@Hill2017, pp. 156–158], and is flagged in §14.

---

## 12. Chronology, interactions and the question of splitting Hill's rule

Component-pair ordering tests (`chronology.json`) isolate each interaction.
Notation: X→Y means component X applied before Y.

**12.1 Monosyllabic *r*-lengthening (Hill's *hēr* argument).** With a
schematic lengthening proxy `AFRLength` (all short vowels lengthen before
word-final *r* in a monosyllable):

| Input | Lower→Lengthen | Lengthen→Lower |
|---|---|---|
| *xir* under `AFHillR`/`AFHillB` | **xēr** | xīr |
| *xír* under `AFHillR`/`AFHillB` | **xḗr** | xīr |
| *xir* under incumbent | xīr | xīr |

Hill's ordering is reproduced: only lowering-before-lengthening yields *hēr*.
The incumbent cannot yield *hēr* in either order (no following vowel; velar
onset). This establishes an ordering dependency **for the *r*
component only**: it says nothing about *z* or *st*.

**12.2 SC036 `OEInterStressRaising` and *world*.**

| Candidate | *wír-àldu*: Lower→SC036 | SC036→Lower |
|---|---|---|
| incumbent | *wéruldu* | **wíruldu** (order-sensitive) |
| `AFTradA` | *wéruldu* | **wíruldu** (order-sensitive) |
| `AFHillB`, `AFHillR` | *wéruldu* | *wéruldu* (order-insensitive) |
| any, *wér-àldu* | *wéruldu* | *wéruldu* |

The production chronology edge SC015→SC036 ("displacement witness: world")
exists only because the incumbent needs the second member's *à* before SC036
raises it to *u*. Under consonantal conditioning the edge disappears; under
a reconstruction with *wer-* already established it is vacuous. The edge is
a **category 4** dependency in the brief's typology — a purely executable
interaction without independent historical force — and should be
re-labelled accordingly whenever SC015 is adjudicated. It does not change
the recommendation here, because no reordering is proposed.

**12.3 *z*-loss and rhotacism.**

| Input | Component | Lower→`MonosyllabicFinalZLoss` | ZLoss→Lower |
|---|---|---|---|
| *iz*, *hiz* | `AFHillZ`/`AFHillB` | **ē, xē** | ī, xī |
| *iz*, *hiz* | incumbent | ī | ī |
| *mízdē* | any | mézdē | mézdē (not monosyllabic) |

| Input | Component | Lower→`EAFRhotacism` | Rhotacism→Lower |
|---|---|---|---|
| *mízdē* | `AFHillZ` | mérdē | **mírdē** |
| *mízdē* | `AFHillR` | mírdē | **mérdē** |
| *mízdē* | `AFHillB` | mérdē | mérdē |
| *líznōjaną* | `AFHillZ` / `AFHillR` | lérn- / lírn- | lírn- / lérn- |

The *z* component must precede monosyllabic final *z*-loss (else *iz > ī*);
`EAFFinalZDeletion` (polysyllabic) does not interact. Relative to rhotacism
the unified rule is order-insensitive, because whichever of *z* or *r* is
present at the time triggers lowering. Historically this means the *z*
component is **strictly required only for word-final *z***; preconsonantal
*zd*/*zn* cases could in principle be handled by *r*-lowering after
rhotacism — but that alternative would date the lowering of *mizdō* after
rhotacism, contradicting *mēd* (z-loss variant without *r*) which shows *e*
before *z* was lost [@Kroonen2013, p. 370]. The *z* component is therefore
retained as a pre-rhotacism process.

**12.4 i-mutation recovery.**

| Input | Component | Lower→`OEIUmlaut` | Umlaut→Lower |
|---|---|---|---|
| *nistijana*, *listiz* | `AFHillSt`/`AFHillB` | nistijana, listiz | **nestijana, lestiz** |
| *liznijana* | `AFHillZ`/`AFHillB` | liznijana | **leznijana** |

CAPR's `OEIUmlaut` does raise lowered *e* back to *i* before *i/j*. Hill's
masking account is therefore executable without any additional machinery,
provided lowering precedes i-mutation (which every variant tested does).

**12.5 Early vs late placement.** `C-early` (before dental hardening) and
`C-late-z-before-zloss` (after apocope) produce identical finals to the
incumbent-position C variants. The decomposed rule is executably robust
across the entire window from `EAFLThVoicing` to `MonosyllabicFinalZLoss`.
Nothing in the cascade forces a particular position within that window; the
historical date must come from §8, not from serialization.

**12.6 Should Hill's rule be split?** Executably, no: all six orderings and
the unified rule are indistinguishable on 387 rows and all probes.
Historically, yes: the three components have different evidential weight
(*r* > *z* > *st*), different phonetic plausibility, and — if Hill's *hēr*
argument is accepted — potentially different dates (*r* Proto-Germanic; *z*
and *st* not demonstrably so). The correct representation is one executable
rule carrying a split historical gloss, not three executable rules
pretending to a chronology the evidence does not supply.

---

## 13. Comparative evaluation and recommended historical reconstruction

**Historical assessment, superseded in part:** the supplement §§2–10
withdraws “no secure counterexample”, the claim that the *z/st* domain is
securely NWGmc, and the implication that only the *learn* paradigm blocks
adoption. Its corrected traditional comparator replaces the any-nasal
implementation for evaluation of that specific classical formulation.

Evaluated on the four independent dimensions required by the brief.

**A. Exact selected-target accuracy (387 rows).** Incumbent 379/387;
A 371/387; B and all C 376/387; skip 376/387. The incumbent wins by three
rows, all *learn*, where its advantage derives from *not* lowering before
*zn* — a prediction the literature regards as the irregular one.

**B. Historically acceptable Old English outcomes.** Treating OE
*leornian* as an attested, regular alternative to *liornian*
[@Kroonen2013, p. 340; @RingeTaylor2014, pp. 38, 84], B/C produce 379/387
acceptable outcomes — equal to the incumbent. Candidate A produces eight
outcomes (*fesċ, leccian, hled, lefeþ, lefer, tecca …*) that are not
attested in any Old English dialect: 371/387.

**C. Comparative positive and negative controls (15 full-cascade probes +
component probes).** B/C: all timbres correct; no secure counterexample.
Incumbent: five wrong (*bitanaz, biðanaz, nidana* lowered; *hiz, hir* not).
A: eleven wrong. On this dimension B/C are decisively superior.

**D. Historical explanatory economy.** A requires analogical restoration of
*i* in every class I participle, every uninflected adverb, *fish*, *wisp*,
*lid* and the OE labial/velar set — Lloyd's "all *e*-forms are analogical"
in reverse, with no positive evidence. The incumbent requires an onset-velar
prohibition with no WGmc source, an all-coronal class with no source, and
still mispredicts the participles. B/C require: (i) a paradigmatic/i-mutation
account of *learn* (Jasanoff; Hill — independently proposed), (ii) *irh-* as
a loan (Hill), and (iii) nothing else. B/C are the most economical.

**Recommended historical reconstruction.** Stressed short *i* was lowered
to a close *e* in early Germanic when immediately followed by *r*, by
tautosyllabic *z*, or by *st*. The following vowel was not the conditioning
factor. The *r*-lowering is probably Proto-Germanic (Hill's *hēr* argument,
Gothic *wair* compatible); the *z*- and *st*-lowerings are securely
Northwest Germanic and not demonstrably older; the *st*-lowering rests on a
single lexeme. Southern West Germanic lowering before labials and velars
(*quec, lebēn, spek*), Norse a-umlaut with its *g/k* restriction, and
Gothic breaking are separate later developments and are not part of this
rule. Apparent exceptions with high-vowel or *j* suffixes (*nistan, list,
liornian, þistel*) reflect later i-mutation of the lowered vowel. No
preceding-velar restriction operated in West Germanic.

---

## 14. Outstanding questions and the precise evidence needed to resolve them

**Historical question list:** supplement §10 replaces this list for the
current recommendation. In particular, *learn* is no longer considered the
only obstacle to adopting B/C.

1. **The *learn* selections (rows 2095, 2313, 2314).** Must *liornian* be
   derived regularly, or is *leornian* the regular form with *liornian*
   from a lost *-iþ/-ja-* cell (Jasanoff) or from i-mutation? Needed: a
   lexical adjudication of the three PROTOFORMs against Jasanoff 1973
   pp. 865, 868, Ringe–Taylor pp. 38, 84, Kroonen p. 340, with an explicit
   stage decision (Tarsi–Laker's WGmc-innovation dating, pp. 42–43). This
   is the *only* corpus obstacle to adopting B/C.
2. **Monosyllabic lengthening.** The cascade contains no law producing
   *hē, hēr, mē, þē* from short-vowel monosyllables. Adopting *r*-lowering
   as Proto-Germanic entails a position relative to a lengthening law that
   does not yet exist (Hill pp. 148–149, 156–158). Needed: a separate
   adjudication of monosyllabic lengthening with its own witnesses.
3. ***st* beyond *nest*.** One lexeme carries the component. Needed: any
   further NWGmc *i + st + non-high* lexeme without i-mutation trigger, or
   acceptance that the component is provisional.
4. **Representation of close *ẹ*.** Hill's lowered vowel is a close *ẹ*
   distinct from inherited open *e*; CAPR merges them as *e*. Needed: a
   decision whether any later rule in the cascade distinguishes them (none
   found in this study).
5. **The SC015→SC036 edge.** Shown to be executable-only (§12.2). Needed:
   relabelling at adjudication; no reordering.
6. **Hock 1973 and Howell 1988/1991.** Not held; cited only through Hill and
   Fulk. Should be ingested before publication prose asserts their
   positions.

---

## Verdict

**Supersession notice, 16 October 2026:** this is the preceding research
recommendation, not the current adoption proposal. The supplement §10
recommends RETAIN executable / DEFER replacement. In particular, the exact
broad-*z* patch below is no longer recommended for adoption; the narrower
diagnostic tested in the supplement is not independently licensed either.

A prospective, evidence-weighted recommendation; not an adopted registry
verdict. The incumbent executable rule is **retained unchanged** for now,
and the four axes are distinguished as follows.

**Historical reconstruction — REFORMULATE (recommended, not adopted).**
The best-supported generalization is consonant-conditioned lowering before
*r*, tautosyllabic *z* and *st*, as in Candidate B/C, with the three
components carrying unequal confidence (*r* > *z* > *st*). The traditional
vowel-conditioned rule is refuted for Old English on the selected corpus
(eight unattested outcomes) and on the comparative controls. The incumbent's
all-coronal class and onset-velar prohibition have no support in the
literature and mispredict five comparative controls; they should not be
described as established phonology.

**Historical chronology — SPLIT the gloss, do not REORDER.** Lowering
before *r* is possibly Proto-Germanic and must precede monosyllabic
*r*-lengthening (if that law is ever modelled); lowering before *z* must
precede monosyllabic final *z*-loss and the sporadic pre-dental *z*-loss;
all components must precede i-mutation. No evidence orders the components
relative to each other. The SC015→SC036 edge is an executable artefact of
the vowel condition and carries no historical force. No change to production
order is recommended.

**Foma implementation — RETAIN the executable rule; defer REFORMULATE
until question 1 is settled.** `AFHillB` (equivalently any `AFC*`) is
faithfully representable in the existing alphabet without lexical exceptions
or velar guard, compiles cleanly, preserves 384 of 387 canonical finals, and
changes only the three *learn* rows, whose selected targets are the disputed
*io*-variants. Because those targets are a lexical selection outside this
brief's authorization, and because adoption would alter canonical firing
counts and the frozen fingerprint, the executable change is **not adopted**.
If and when the *learn* adjudication selects *leornian*-type targets or
*i*-bearing inputs, the exact proposed rule is:

```foma
define PNWGmcILowering Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}],
    {*í} -> {*é} || .#. EnglishStarConsonant* _ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}]
]);
```

at the incumbent position, with `EnglishStarNonVelarConsonant` retired if
unused elsewhere. Affected inputs/outputs: 2095 `*líznōjaną` → *leornian*
(was *liornian*); 2313 `*líznô` → *leorna*; 2314 `*líznōθi` → *leornaþ*;
2250 `*θístilas` intermediate `*θéstilas`, final unchanged. Regression risk:
confined to those rows; `canonical_protection` digests unchanged in this
study. The expected live-firing population under the proposed rule would
be meed, nest, world, learn ×3 and (intermediately) thistle.

**Publication treatment — QUALIFY.** The reader-facing chapter already
cites Cercignani's warning about the Norse velar restriction and presents
*wiraz* with the Gothic caveat. It should additionally (at adjudication, not
now): state that the executable coronal/vowel conditioning is a proxy, not a
claim that the following vowel conditioned the change; present the
participles and *nidana/hina* as evidence against vowel conditioning; give
the *r/z/st* decomposition with its unequal confidence; mark *st* as resting
on *nest* alone; and remove any implication that the onset-velar restriction
is Old English phonology. The three-witness census (meed, nest, world) is
correct and stands.

---

## Appendix A. Diagnostic test matrix

### A.1 Component-level probes (`components`; stage-local, before any later rule)

Columns: inc = incumbent `PNWGmcILowering`; A = `AFTradA`; B = `AFHillB`;
R/Z/St = `AFHillR`/`AFHillZ`/`AFHillSt`. Cell = root vowel after the
component. Interpretation per §6.

| Probe | Input | Comparative reflex | inc | A | B | R | Z | St | Interpretation |
|---|---|---|---|---|---|---|---|---|---|
| iz | *iz | OHG *er* | i | i | **e** | i | **e** | i | *z#* positive |
| hiz | *xiz | OE *hē* | i | i | **e** | i | **e** | i | *z#* positive |
| hir | *xir | OE *hēr* | i | i | **e** | **e** | i | i | *r* positive; chronology probe |
| wiraz | *wiraz | OE *wer* | **e** | **e** | **e** | **e** | i | i | *r* positive; non-discriminating vs A |
| nistan | *nistan | OE *nest* | **e** | **e** | **e** | i | i | **e** | *st* positive |
| mizdon | *mizdōn | OE *meord* | **e** | **e** | **e** | i | **e** | i | *zC* positive |
| fiskaz | *fiskaz | OE *fisc* | i | **e**✗ | i | i | i | i | *sk* negative |
| wisko | *wiskō | OE *wisc* | i | **e**✗ | i | i | i | i | *sk* negative |
| diskaz | *diskaz | OE *disc* | i | **e**✗ | i | i | i | i | loan; weak negative |
| bitanaz | *bitanaz | OE *biten* | **e**✗ | **e**✗ | i | i | i | i | participle negative |
| bidanaz | *biðanaz | OE *biden* | **e**✗ | **e**✗ | i | i | i | i | participle negative |
| nidana | *nidana | OHG *nidana* | **e**✗ | **e**✗ | i | i | i | i | adverb negative |
| hina | *xina | OHG *hina* | i | i | i | i | i | i | nasal; non-discriminating |
| lid | *xlidą | OE *hlid* | i | **e**✗ | i | i | i | i | A fails; inc saved by guard only |
| irha | *irxa | OHG *irh* | i | **e** | **e** | **e** | i | i | probable loan; not decisive |
| bedinn | *biðinaz | ON *beðinn* | i | i | i | i | i | i | following *i*; non-discriminating |
| liznon | *liznōn | OE *leorn-/liorn-* | i | i | **e** | i | **e** | i | *zC* positive, masked |
| nestijan | *nestijan | — | e | e | e | e | e | e | e-control |
| nistijana | *nistijana | OE *nistan* | i | i | **e** | i | i | **e** | masking test (→ i after umlaut) |
| listiz | *listiz | OE *list* | i | i | **e** | i | i | **e** | masking test (→ i after umlaut) |
| liznijana | *liznijana | OHG *lirnēn* | i | i | **e** | i | **e** | i | masking test (→ i after umlaut) |
| wether_current | *wéθruz | OE *weþer* | é | é | é | é | é | é | not a witness |
| wether_old | *wíθrą | — | **é** | **é** | í | í | í | í | superseded input; A/inc lowered it |
| world_current | *wír-àldu | OE *weorold* | **é** | **é** | **é** | **é** | í | í | *r* positive |

### A.2 Full-cascade probe outputs

See §11 table. Raw strings in `experiments.json.gz` →
`variants[].supplementary_full_prefix_outputs`.

### A.3 Synthetic onset × coda × vowel grid (following *a*; "e" = lowered)

Rows where at least one component lowers. Onsets: ∅, *x*, *k*, *xl*, *b*;
codas *r, st, d, θr, sk, b, z, zd* (nasal codas *nt, n* and *sj* never
lower under any component).

| onset-coda | inc | A | `AFTrad` | B | Bz | R | Z | St |
|---|---|---|---|---|---|---|---|---|
| ∅/b – r | e | e | e | e | e | e | i | i |
| ∅/b – st | e | e | e | e | e | i | i | e |
| ∅/b – d, θr | e | e | e | i | i | i | i | i |
| ∅/b – sk, b | i | e | i | i | i | i | i | i |
| ∅/b – z | e | e | e | i | e | i | i | i |
| ∅/b – zd | e | e | e | e | e | i | e | i |
| x/k/xl – r | **i** | e | e | e | e | e | i | i |
| x/k/xl – st | **i** | e | e | e | e | i | i | e |
| x/k/xl – d, θr | **i** | e | e | i | i | i | i | i |
| x/k/xl – sk, b | i | e | i | i | i | i | i | i |
| x/k/xl – z | **i** | e | e | i | e | i | i | i |
| x/k/xl – zd | **i** | e | e | e | e | i | e | i |

Bold *i* marks the onset-velar guard's effect: the incumbent fails to lower
*xir-, kir-, xlist-* etc. With following *i* or *u*, inc/A/`AFTrad` never
lower; B/C lower before *r, st, zd* (and Bz before *z*) regardless of vowel.
Extra controls: unstressed second-syllable *i* (`*baristaz`) never lowers;
long *ī* never lowers; the proclitic marker `*ᵘxiz` lowers under B only.

### A.4 Corpus rows changed by any variant

| Row | Concept | PROTOFORM | Target | Variant(s) | Output |
|---|---|---|---|---|---|
| 2014 | fish | *fískaz | fisċ | A | fesċ |
| 2099 | lick | *líkkōjaną | liccian | A | leccian |
| 2100 | lid | *xlídą | hlid | A, `AFTrad` | hled |
| 2107 | live | *líbēθi | lifeþ | A | lefeþ |
| 2108 | liver | *líbrō | lifer | A | lefer |
| 2256 | tick | *tíkkô | ticca | A | tecca |
| 2315 | lick (iptv.2sg) | *líkkô | licca | A | lecca |
| 2316 | lick (3sg) | *líkkōθi | liccaþ | A | leccaþ |
| 2095 | learn | *líznōjaną | liornian | B, Bz, C×8, late-hill | leornian |
| 2313 | learn (iptv.2sg) | *líznô | liorna | same | leorna |
| 2314 | learn (3sg) | *líznōθi | liornaþ | same | leornaþ |
| 2124 | meed | *mízdai | meorde | skip | miorde |
| 2137 | nest | *nístą | nest | skip | nist |
| 2302 | world | *wír-àldu | weorold | skip, late-current | wuruld |
| 2250 | thistle | *θístilas | þistles | B, C (intermediate only) | þistles |

---

## Appendix B. Exact experimental Foma definitions and reproduction

### B.1 Definitions (verbatim from `experiment.py` → `DEFINITIONS`)

```foma
define AFTradA [ Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ [EnglishStarConsonant - EnglishStarNasal - {*j}]* EnglishStarNonHighVowel,
    {*í} -> {*é} || .#. EnglishStarConsonant* _ [EnglishStarConsonant - EnglishStarNasal - {*j}]* EnglishStarNonHighVowel
]) ];
define AFTrad [ Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é} || .#. EnglishStarConsonant* _ EnglishStarCoronal+ EnglishStarNonHighVowel
]) ];
define AFHillB [ Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}],
    {*í} -> {*é} || .#. EnglishStarConsonant* _ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}]
]) ];
define AFHillBz [ Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ [{*z} | {*s} {*t} | {*r}],
    {*í} -> {*é} || .#. EnglishStarConsonant* _ [{*z} | {*s} {*t} | {*r}]
]) ];
define AFHillR  [ Ctx([ {*i} -> {*e} || .#. EnglishStarConsonant* _ {*r},
                        {*í} -> {*é} || .#. EnglishStarConsonant* _ {*r} ]) ];
define AFHillZ  [ Ctx([ {*i} -> {*e} || .#. EnglishStarConsonant* _ {*z} [EnglishStarConsonant | .#.],
                        {*í} -> {*é} || .#. EnglishStarConsonant* _ {*z} [EnglishStarConsonant | .#.] ]) ];
define AFHillSt [ Ctx([ {*i} -> {*e} || .#. EnglishStarConsonant* _ {*s} {*t},
                        {*í} -> {*é} || .#. EnglishStarConsonant* _ {*s} {*t} ]) ];
define AFCRZS [AFHillR .o. AFHillZ .o. AFHillSt];
define AFCRSZ [AFHillR .o. AFHillSt .o. AFHillZ];
define AFCZRS [AFHillZ .o. AFHillR .o. AFHillSt];
define AFCZSR [AFHillZ .o. AFHillSt .o. AFHillR];
define AFCSRZ [AFHillSt .o. AFHillR .o. AFHillZ];
define AFCSZR [AFHillSt .o. AFHillZ .o. AFHillR];
define AFSkip [?*];
define AFLate [PNWGmcILowering];
define AFLength [Ctx([{*e} -> {*ē} || .#. EnglishStarConsonant* _ {*r} .#.,
                      {*é} -> {*ḗ} || .#. EnglishStarConsonant* _ {*r} .#.])];
```

`chronology.py` adds the four-vowel schematic `AFRLength` (Appendix in
`chronology.json` → `recipe.definitions`).

### B.2 Reproduction (inside the backend container; `/usr/app` mounts `Germanic/`)

```bash
B=/usr/app/docs/sound_changes/audits/sc015-a-ablaut-investigation
docker compose exec -T backend python3 $B/experiment.py $B/experiments.json      # ~35 min
docker compose exec -T backend python3 $B/chronology.py $B/experiments.json $B/chronology.json
gzip -k $B/experiments.json                                                       # on host
```

Both drivers abort if `Germanic/fsts/germanic.txt` does not hash to the
value in the header, if the 387-row baseline does not reproduce the 8
canonical mismatches, or if any protected file digest changes during the run.

### B.3 Baseline census commands

```bash
python3 Germanic/tools/adjudicate.py SC015 --prepare
python3 Germanic/tools/adjudicate.py SC015 --evidence
```

---

## Bibliography of principal sources checked

Keys as in `docs/refs.bib`. Page references are printed pagination.

- Bülbring, K. D. 1902. *Altenglisches Elementarbuch*. §81, pp. 34–35. [@Bulbring1902]
- Campbell, A. 1959. *Old English Grammar*. §§111, 114–116, pp. 42–44. [@Campbell1959]
- Cercignani, F. 1979. "Proto-Germanic */i/ and */e/ Revisited." pp. 72–76. [@Cercignani1979]
- Cercignani, F. 1980. "Early 'Umlaut' Phenomena in the Germanic Languages." pp. 126–132. [@Cercignani1980]
- Cercignani, F. 2022. "Distance Assimilation in Germanic." pp. 45–47. [@Cercignani2022]
- Fulk, R. D. 2018. *A Comparative Grammar of the Early Germanic Languages*. pp. 55–59. [@Fulk2018]
- Hill, E. 2017. "West Germanic Monosyllabic Lengthening and Gothic Breaking as Partially Proto-Germanic Developments." pp. 148–158. [@Hill2017]
- Hirt, H. 1931. *Handbuch des Urgermanischen* I. §34, pp. 45–46. [@Hirt1931]
- Hogg, R. M. (with R. D. Fulk). 2011. *A Grammar of Old English* I. p. 54. [@HoggGrammar2011]
- Howell, R. B. 2024. "Gothic Breaking." pp. 75–82, 85, 90–91. [@Howell2024]
- Howell, R. B. & J. C. Salmons. 1988/1997. "Umlautless Residues in Germanic." pp. 84–87. [@HowellSalmons1988]
- Jasanoff, J. 1973. "The Germanic Third Weak Class." pp. 865, 868. [@Jasanoff1973]
- Kostakis, A. 2025. "Early Germanic Coda Nasals." pp. 1–7. [@Kostakis2025]
- Kroonen, G. 2013. *Etymological Dictionary of Proto-Germanic*. pp. 142, 225, 339, 340, 370, 391, 584, 588. [@Kroonen2013]
- Lloyd, A. L. 1966. "Is There an a-Umlaut of i in Germanic?" pp. 738–745. [@Lloyd1966]
- Luick, K. 1914. *Historische Grammatik der englischen Sprache* I. pp. 104–105, 108–109. [@Luick1914]
- Noreen, A. 1923. *Altnordische Grammatik* I. pp. 50–51, 53–54. [@Noreen1923]
- Orel, V. 2003. *A Handbook of Germanic Etymology*. pp. 103, 176, 246–247, 272, 287–288, 419, 459–460, 462–463. [@Orel2003]
- Ringe, D. 2017. *From Proto-Indo-European to Proto-Germanic*. pp. 97, 121. [@Ringe2017]
- Ringe, D. & A. Taylor. 2014. *The Development of Old English*. pp. 33–36, 38, 84–85, 135. [@RingeTaylor2014]
- Scheungraber, C. 2010. *Die Nasalpräsentien im Germanischen*. pp. 74–75. [@Scheungraber2010]
- Seebold, E. 1970. *Vergleichendes und etymologisches Wörterbuch der germanischen starken Verben*. pp. 94–95. [@Seebold1970]
- Sievers, E. & K. Brunner. 1965. *Altenglische Grammatik*. pp. 34–35. [@SieversBrunner1965]
- Streitberg, W. 1896. *Urgermanische Grammatik*. §68, pp. 56–57. [@Streitberg1896]
- Tarsi, M. & S. Laker. 2026. "Know, Teach, Learn." pp. 40–47. [@TarsiLaker2026]

Not held (cited via Hill 2017 and Fulk 2018 only): Hock 1973; Howell 1988a,
1988b, 1991a, 1991b.

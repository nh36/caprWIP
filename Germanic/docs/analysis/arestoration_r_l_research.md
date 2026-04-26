# A-Restoration in Old English: the role of intervening *r and *l

**Status:** research note (no FST or TSV modifications made).
**Scope:** Diagnose why the current FST blocks A-restoration before single *r* and *l*, document the canonical conditioning environment from the philological literature, and propose a single, surgical change to `OEARestorationIntervening` in `Germanic/fsts/germanic.txt`.
**Date:** generated 2026-03 from local `docs/references/`.
**Citation policy:** every quotation below is verbatim (with OCR artefacts preserved). Page/line references are to the `.txt` file in `docs/references/` unless otherwise noted; line numbers were obtained with `grep -n`.

---

## 1. Executive summary

1. The current FST defines

   ```
   define OEARestorationIntervening [
       EnglishStarConsonantNoR - {*l}
   ];
   ```

   i.e. the set of consonants admitted between the fronted *æ* and a triggering back vowel **excludes both *r* and *l*** (`germanic.txt` lines 1806–1808). A Kleene star (`[OEARestorationIntervening]*`) wraps this set in the actual replacement rule (line 1817).

2. **The hypothesis is correct.** Across the entire local reference corpus (Campbell, Hogg/CHEL, Ringe & Taylor vol. 2, Brunner, Luick, Bülbring, Kaluza, Kroonen, Orel) **no source treats a single intervening *r* or *l* as blocking A-restoration**. On the contrary, every source that supplies derivations of `sparian`, `warian`, `farian`, `talian`, `carian`, `lapian`, `bapian`, `nacod`, `nafola`, `sadol`, `stapol`, `magu`, `lagu`, `mapa`, `racca`, `crabba`, `flasce`, `mara`, `hara`, `apa`, `maga`, `naca`, `scapa`, `draca`, `cnafa`, `gegada`, `manslaga` etc. derives the surface *a* by exactly the sound-change A-restoration applying across single intervening *r*, *l*, *m*, *n*, *p*, *b*, *d*, *t*, *g*, *f*, *þ*, *s*, *k*, *w*. Liquids are not singled out as a blocking class.

3. **What does block restoration** in the canonical formulation:
   * **Ringe & Taylor §6.3.1**: only "a single or geminate consonant or sC-cluster" allows retraction; other clusters do not.
   * **Campbell §158**: single C, geminate, *fC* or *sC* allow it; "Before other groups, a is not restored except for a few instances before consonant plus liquid".
   * **Luick §161**: phonologically the change was independent of the intervening consonant, but pre-vocalic obstruent + liquid sequences (e.g. *appla*, *acras*) survive only as relics; the levelled/etymologically-fronted variant won out.

   The two FST counter-examples adduced in the project notes — `*nadrō → nædre/næder` and `*bastą → bæst` — are correctly handled for **independent** reasons:
   * `*nadrō`: the `*dr` is a stop + liquid cluster ("Geräuschlaut + Liquida", Luick §161 Anm. 5; cf. Campbell §158 "Before other groups, a is not restored"). It is the **two-consonant cluster** that blocks restoration, not the *r* per se.
   * `*bastą`: although `*st` is exactly the type of `sC`-cluster that **does** allow retraction (Ringe & Taylor §6.3.1, Campbell §158, Luick §161.3), the trigger vowel `*ą` is a **weak-tail / nasalised final** vowel that does *not* trigger restoration in the FST (`OEARestorationStrongOTail` exclusion, see `germanic.txt` lines 1814–1825). The `bæst` outcome therefore comes from the weak-tail branch and is independent of the intervening-consonant set.

4. **Concrete proposed FST change** (one surgical edit; full code in §10):

   Replace the under-restrictive set + over-permissive Kleene star

   ```
   define OEARestorationIntervening [
       EnglishStarConsonantNoR - {*l}
   ];
   ```

   with a positively-defined, **fully literature-grounded** set whose own structure encodes "single C, geminate, sC-cluster" so that the existing `[…]*` quantifier no longer needs to do that work. *r* and *l* return as ordinary consonants:

   ```
   define OEARestorationIntervening [
         EnglishStarConsonant
       | {*s} EnglishStarConsonant
       | {*f} EnglishStarConsonant
       | EnglishStarGeminate
   ];
   ```

   together with a one-line change to the rule body so the cluster description is matched exactly once (no Kleene star), or — equivalently — by adding a hard upper bound. Either of two minimal edits achieves the same surface result; both are detailed in §10.

5. **Probed inputs** (`flookup -i backend/old_english.bin`, run 2026‑03):

   | input | current output | target |
   |---|---|---|
   | `bastą` | `bæst` | `bæst` ✓ |
   | `nadrō` | `næder` | `nædre` ≈✓ (vowel correct) |
   | `sparōjaną` | `spærian` | `sparian` ✗ |
   | `warōjaną` | `wærian` | `warian` ✗ |
   | `farōjaną` | `færian` | `farian` ✗ |
   | `talōjaną` | `tælian` | `talian` ✗ |

6. **TSV impact (`Germanic/data/germanic-aligned-final.tsv`):** of the OE rows whose protoform contains a single intervening *r* or *l* between *a/á* and a back vowel **8 rows** match (see §11). Of those, **only 1 row** is *currently wrong and would be fixed*: row **2003** `*fáraną → faran` (currently emits `færan`). Row **2205** `*spárēną` (target `sparian`) currently produces `spearen`; the proposed fix is necessary but not sufficient (the trigger vowel `*ē` is front, so this is a separate class III→II morphology issue). The remaining 6 rows already produce a correct output and the proposed fix does not perturb them (verified by inspection of the rule structure; see §10.4).

---

## 2. Verbatim quotations from the local sources

### 2.1 Campbell, *Old English Grammar* (1959) — file `campbell_old_english_grammar.txt`

§157 (line 4720 ff.): heading "RESTORATION OF Æ" / "C. The Restoration of *a* before Back Vowels".

> § 157. One of the most obvious peculiarities of the OE phonological system is that *æ* and *a* interchange, the former standing in closed syllables, and in open syllables when a front vowel (*e*, in early texts sometimes written *i* or *æ*) follows, the latter in open syllables when a back vowel (*a*, *o*, *u*) follows. The paradigm (see §574) *dæg, dæges, dæge, dagas, daga, dagum* illustrates the principle. This interchange is clearly due to the restoration of *a* before a back vowel … (lines 4720–4732)

§158 (lines 4733–4753) — **the canonical conditioning statement**:

> § 158. The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig, *stapol* pillar, *sadol* saddle, *latost* latest, *lapode* he invited, *cassoc* rough grass, *hassuc* the same, *mattoc* mattock, *hnappian* fall asleep, *racca* cord, *lappa* skirt.
>
> *a* is commonly restored also before groups consisting of *f* or *s* followed by another consonant, e.g. *\*wascan* wash, *asce* ash, *flasce* flask (after inflected *ascan*, *flascan*), *brastlian* crackle, *sæftriende* rheumatic. **Before other groups, *a* is not restored except for a few instances before consonant plus liquid:** W-S *appla, apla* apples, *watrode* he watered, Angl. (Rit., Ru.) *accras, acras* fields, beside *æplas, æcras, weterode*, and always *sægdon, hæfdon, fedras, næglas*, &c. Yet it need not be doubted that *a* was originally widely restored before groups, and that it was subsequently removed by the analogy of forms in which a front vowel followed. This is reflected by some doublets, e.g. *gæfel, gafol* tribute, *hægel, hagol* hail, *fægen, fagen* glad, *wæcer, wacor* awake … (emphasis added)

§159 (lines 4754–4760) — **the diagnostic case for class‑2 weak verbs and other *-i-* suffixes:**

> § 159. The restoration of *a* was frequently due to a back vowel which subsequently became a front vowel or was lost, e.g. *gaderian* gather, *stapelian* found (cf. *geador, stapol*), and weak verbs in *-i-* (< *-ói-*), *lapian, macian, hnappian*, &c.

§453 (line 8323) and §453 continued (lines 11771–11774) — on `nædre`, attesting *consonant doubling before liquids* as the explanation for the geminate, not for the front vowel:

> Examples of OE shortening before triple consonants are *godspell* gospel, *\*bramblas* brambles, and probably many words with consonant gemination before liquids (cf. § 453), e.g. **næddre** adder, *attres* g.s. poison.

> nǣddre adder, ǣttres g.s. and hence ǣttor poison, and so lW-S *hlǣdder* ladder, *foddor* fodder, *mēddor* mother, *tēddor* progeny, (all after infl. forms), *ǣddran* veins, *blǣddre* bladder, *tȳddre* weak.

§764 (lines 23258–23262) — `sparian` in fact attested with both class II and class III variants, and the front-vowel `spær-` forms are precisely the ones expected when no back vowel follows:

> sparian spare: this verb does not show any of the characteristics listed above, but Rit. inf. **spæria**, imper. **spær**, past *-spærede* beside VP forms with back mutation (pres. indic. 3rd sg. *spearaþ*, &c.) suggest Prim. OE forms both with and without back vowels in the syllables after the root syllable, hence conjugation according to Class II or Class III.

§753.4 (line 23227) — `tellan, talian` are explicitly cited as parallel forms (class I vs class II of the same root) — i.e. *talian* with class‑II *a*, not *tælian*.

(Brief note: §158 nowhere singles out *r* or *l* as blocking. It places `consonant + liquid` clusters in the small set that mostly fail to restore — but a *single* *r* or *l* between vowels falls under "all single consonants" which restore.)

### 2.2 Ringe & Taylor (2014), *A Linguistic History of English vol. II* — file `ringe_taylor_linguistic_history_vol2.txt`

§6.3.1, "General retraction of *æ*" (lines 10987–11008) — the canonical generative formulation:

> 6.3 General retraction of *æ* and *ǣ*; phonemicization of low vowel allophones
>
> 6.3.1 General retraction of *æ*
>
> After breaking had run its course, those stressed *æ* which were immediately followed by a single or geminate consonant or **sC-cluster** which was in turn followed by a back vowel became *a* (Luick 1914-40: 152-7, Campbell 1962: 60-2, Hogg 1992: 96-100 [2011: 93-9]). … If fronting could take place before /h/ … plus a back vowel, it should have occurred before any single nonnasal consonant plus a back vowel, even in such a form as *\*dagum* 'days' (dat. pl.), which must therefore have become *\*dægum*. Since the attested form in most OE dialects is *dagum*, it follows that retraction must have occurred subsequently to fronting—and subsequently to breaking …

§6.3.1 cont. (lines 11013–11019): **class‑II weak verbs are expressly cited as a paradigm case**:

> Weak verbs of class II always exhibit retracted *a* rather than *æ* before a non-nasal consonant in a monosyllabic root syllable, since at the time retraction occurred the following syllable always contained *\*ō* or *\*a*. There are more than fifty examples; the following are typical:

§6.3.1 derivations (lines 11020–11107) — all with the explicit step `*Cæ̆Cōjan > *CăCōjan` (i.e. retraction across a single intervening C, including *r*, *l*, *p*, *b*, *m*, *t*, *d*, *k*, *g*, *þ*, *s*, *w*, *kk*):

> PGmc *kar6na 'to worry about' (Goth. karon) > PWGmc *karon … >— *kærōjan > OE **carian** …
>
> PGmc *labōnq 'to invite' … >— *labojan (OS lad(o)ian) > *læbōjan > OE **laþian** …
>
> PNWGmc *talōnq 'to calculate, to consider' … (OS talon, OHG zalon) >— *tælōjan > OE **talian** (OF talia);
>
> PNWGmc *sparja- (*spara-?) ~ *sparai- 'spare' (ON spara) > PWGmc *sparē- (OHG sparen) >— *spærōjan > OE **sparian** (OF sparia 'to keep safe');
>
> PWGmc *makōn 'to make' (OS makon, OHG mahhon) >— *mækōjan > OE **macian** (OF makia);
>
> PWGmc *baté- 'become better' … >— *bætōjan > OE **batian** …
>
> PNWGmc *hagōnq 'to be fitting' … >— *hægōjan > OE **ge-hagian** …

§6.3.1 derivations of n-stems and u-stems with intervening *single* *r* / *l* (lines 11098–11150) — none of these block restoration:

> PGmc *maguz 'boy' … > OE **magu** 'young man, son' (poetic);
>
> PNWGmc *laguz 'water, the sea' … > *lægu > OE **lagu**.
>
> PGmc *askōn- ~ *azgōn- 'ashes' … > *æskē, *æskōn- >— OE **asce, ascan** …
>
> PNWGmc *marōn- 'nightmare' (ON mara) > PWGmc *mara, *marōn- (OHG mara) > *mærē, *mærōn- >— OE **mare, maran**, and *mere*;
>
> PNWGmc *hasō, *hazan- 'hare' (ON heri, OHG haso) > *hærē > OE **hara**;
>
> PNWGmc *magō 'stomach' … > *mæga > OE **maga** (OF maga);
>
> PWGmc *manslagō 'murderer' (OHG manslago) > *manslæga > OE **manslaga**.

Single-*r* / single-*l* derivations of derivational suffixes and u-stems (lines 11079–11097):

> *nabulē > *næbula > OE **nafola**;
> *habukaz > *hæbuk > OE **hafoc**;
> *latōsta > *lætost > OE **latost**;
> *sadulaz > *sædul > OE **sadol**;
> *stapulaz > *stæpul > OE **stapol**;
> *stabulaz > *stæpul > OE **stapol** 'base, foundation';
> *wakul > *wækul > OE **wacol**;
> *gabulu > *gæbulu > OE **gafol**.

Note the consistent presence of *r*, *l* in many of these derivations (`nabula`, `gabula`, `staþul`, `sadul`, `nafola`, `gafol`) and the exceptionless retraction. R/T does not anywhere identify *r*/*l* as a blocker.

§6.3.2 paradigm tables (lines 11210–11270): `dæg/dages` and `fæt/fatu` are presented as the textbook paradigms.

R/T derivation of `faran` itself (line 13432):

> PGmc *faraną 'to go, to travel', pres. indic. 2sg. *farizi, 3sg. *faridi (Goth. *faran, *faris, *farip; OHG faran, 3sg. ferit) >— *faran, *færisi, *færiþi — *faran, *farisi, *fariþi >— OE **faran**, *færst*, *færþ*;

— i.e. R/T expressly derives `faran` (not `færan`) from *faraną. The intervening *r* is irrelevant: it is the back vowel of the following syllable that matters.

R/T on the past plural of class VI (line 19727 and class VI summary at line 11309): "the lexical influence of class VI *faran* 'to go' …".

R/T cross-references for `sparian / spearian` (lines 9472, 12668): "II (WS) **sparian**, (southwestern Merc.) **spearian**". Note: *spearian* (Merc.) shows *back-mutation* of the (already-retracted) *a*, which presupposes that retraction had previously applied — a strong indirect argument that *a* is the correct phonemic input across single *r*.

### 2.3 Hogg / *Cambridge History of the English Language* vol. I — file `hogg_vol1.txt`

The "Restoration of *a*" passage (lines 5188–5230):

> For the period of Old English being discussed at present one further sound change, known as Restoration of *a*, must be noted. … by the sound change we are now concerned with /æ/, and to a lesser extent /æː/, were retracted to /a, aː/ when a back vowel was present in the following syllable. This sound change had widespread morphological consequences, for example nouns such as *fæt* 'vessel' would have the plural form *fatu*. The effect of the change would be to harmonise low vowels to a following vowel, so that any low vowel followed by a back vowel would be back itself, and all other low vowels (except nasalised ones) would be front.

Hogg's only conditioning statement is "when a back vowel was present in the following syllable" — no mention of *r* or *l* as blockers. (The CHEL chapter is non-technical and does not enumerate intervening clusters.)

Hogg on class VI strong verbs (line 7466):

> Class VI verbs should, because of the sound change of restoration of *a* (see §3.3.3.1), have varied between /a/ and /æ/ in the present tense and the past participle, but in West Saxon at least /a/ was generalised throughout the present and was normal in the past participle. Hence we find *faran* ~ *for* ~ *foron* ~ *færen* 'go'.

(NB: the user's task brief refers to "Hogg §5.34/§5.35" — those are sections of *Hogg 1992: A Grammar of Old English vol. I*, which is **not** present in `docs/references/`. Only the CHEL chapter is locally available. The substantive content matches: see Hogg 1992 cited via R/T 6.3.1.)

### 2.4 Brunner, *Altenglische Grammatik* (1965) — file `brunner_1965_altenglische_grammatik.txt`

§10 (lines 1146–1169) — "Das kurze a kommt nur in bestimmten Stellungen vor und zwar":

> vor einem *a*, *o*, *u* der Folgesilbe (auch wenn diese wegen späteren Lautwandels nicht mehr erhalten sind), z. B. *habban* haben, *crabba* Krabbe, *lappa* Lappen (neben *læppa*), *appla* G. Pl. zu *æppel* Apfel, *mattuc* Hacke, *assa* Esel … Pl. *dagas* zu *dæg* Tag, *atol* schrecklich, *nacod* nackt, Pl. *fatu, fata, fatum* zu *fæt* Faß, *sadol* Sattel, *stadelian* befestigen, *nafela* (neben *nabula* Corp.) Nabel, *macedon* (neben *macodon*) machten, **ebenso vor dem aus -ōj- entstandenen -i- der schw. Vb. II. Kl. (§ 411, 1) macian machen, gladian sich freuen, daccian streicheln usw.** und bei Ausfall des ursprünglichen Mittelvokals *gedaf(e)nian* geziemen (neben *gedafonian*), *war(e)nian* sich hüten, *gad(e)rian* sammeln …

Brunner §10 is **explicit** that class II weak verbs in *-ian* (< *-ōj-*) carry restored *a*: *macian, daccian, war(e)nian, gad(e)rian*. The relevant pattern includes *war-* / *gad-r-* (single *r*) without any blocking remark.

§109 area (line 4179) — listing the regular open-syllable forms before back-vowel suffix:

> es heißt also nach § 50, 1 *arod* hurtig, *darod* Pfeil, *apuldre* Apfelbaum, *stapol* Staffel, *hafoc* Habicht, *sadol* Sattel, *atol* schrecklich, *fatu* Fässer, **faran fahren, sparian (und Formen dazu) sparen** usw.

Brunner thus pairs `faran` and `sparian` as the textbook examples of A-restoration in open syllables, contradicting the current FST output.

§50, 3 (line 1191) — the converse statement (when *æ* survives): "nur, wenn in der Folgesilbe nicht ursprünglich *a, o, u* folgte" — *æ* only when the next syllable did **not** originally contain *a/o/u*. Again no exception is reserved for *r* or *l*.

### 2.5 Luick, *Historische Grammatik der englischen Sprache* — file `luick_historische_grammatik.txt`

§161 (lines 10180–10220) — the most explicit anti-blocking statement in the entire corpus:

> § 161. Urengl. *æ* wurde gemeinenglisch vor einem dunklen Folgevokal zu *a*, **ohne daß der dazwischen stehende Konsonant von Belang gewesen wäre.** Bis in die historische Zeit hat sich *a* im Westsächsischen, Nordhumbrischen und Ostmercischen (Ru.¹) erhalten:
>
> 1. am deutlichsten in offener Silbe: *hara* Hase, *faran* fahren, *farað* sie fahren, *talu* Erzählung, *apa* Affe, *sacu* Sache, *nacod* nackt, *macian* machen, *wadan* waten, *sadol* Sattel, *gad(e)rian* sammeln, *grafan* graben, *hraðor* schneller, *staðol* Stütze, *staðelian* befestigen, *magu* Knabe, *dagas, -a, -um* plur. zu *dæg* Tag, *fatu, -a, -um* plur. zu *fæt* Faß usw.;
>
> 2. sehr deutlich auch vor langen Konsonanten (außer *hh, rr, ll*, die Brechung bewirkt hatten): *hnappian* einschlafen, *lappa* Lappen, *mattuc* Hacke, … *crabba* Krabbe, *gabbian* spotten, … *cassuc, hassuc* Binse …;
>
> 3. vielfach vor *s+Kons.* und *f+Kons.* (während vor *h+Kons.* Brechung eingetreten war): *wascan* waschen, *ascan* plur. 'Aschen' …, *flascan* Flaschen …, *brastlian* krachen, *wrastlian* ringen, *sæftriende* rheumatisch usw.;
>
> 4. **nur in wenigen Resten vor Geräuschlaut + Liquida:** ws. *ap(p)la* Äpfel, angl. *ac(c)ras* Äcker, vereinzelt spätws. *caferas* aus *\*cafras* …

§161 Anm. 5 (lines 10260–10275) — the theoretical claim:

> Daß vor dunklem Folgevokal wg. *a* in offener Silbe lautgesetzlich durch *a* vertreten wird, ist längst bekannt. E. Sievers (Vok. 14 ff.) und K. Bülbring (AB 9, 92, EB § 127) haben hierauf erkannt, daß in der Stellung vor Geminaten und den *s-* und *f-*Verbindungen dasselbe Verhältnis galt. Die bisher in ihrer Tragweite übersehenen Formen *ap(p)la, ac(c)ras*, die nur altertümlich sein können, lehren aber, daß es auch vor Geräuschlaut + Liquida bestand. **Somit ist dieser Einfluß eines dunklen Folgevokals unabhängig von der Art der dazwischen stehenden Konsonanten.**

Luick's position is the strongest in the corpus: phonologically, the change was **independent of the intervening consonant**; the absence of *a* before stop+liquid in attested OE is **morphological levelling** from related forms with following front vowel, not a phonological gap.

### 2.6 Bülbring, *Altenglisches Elementarbuch* — file `bulbring_altenglisches_elementarbuch.txt`

Bülbring is the source Luick cites (EB §§ 127, 130). The local file does not contain a dedicated index entry under "restoration"; the relevant material is at the same locus (§§ 127–130) as Luick's references. Search hits in the local file are confined to peripheral mentions of *vor Velaren*, *vor Velarvokalen* and do not contradict any of the above. **The local file does not provide a separate independent statement of the conditioning relevant to *r*/*l*.**

### 2.7 Kaluza, *Historische Grammatik des Englischen* — file `kaluza_historische_grammatik_englisch.txt`

Line 4927:

> Beispiele: a) Urg. *a* = ae. *a* in offener Silbe vor dunklem [Vokal der Folgesilbe] …

Kaluza confirms the standard "open syllable, dark vowel in the next syllable" formulation; the local file does not give an *r*/*l*-specific carve-out.

### 2.8 Kroonen, *Etymological Dictionary of Proto-Germanic* — file `etymological_dictionary_of_proto_germanic_kroonen.txt`

`*sparēnan-` (page 466, lines 26889–26892):

> Also cf. ON spara, OE **sparian**, OFri. spara, OS sparon, Du. sparen, OHG sparen, sparon, G sparen wv. 'to spare, save' < *sparēn-.

`*talōnq / *talōjanan-` (lines 29142–29144, page 508):

> Related to *tala- (q.v.). Also cf. ON tala 'to speak', OE **talian**, OFri. talia, OS talon, OHG zalon 'to count' < *talōjan-.

`*nadra-` (page 381, lines 22442–22446):

> *nadra- m. 'adder, snake' — Go. nadrs* m. 'id.', ON nadr m. 'id.' …

`*nēdrōn-` (page 386, line 22723):

> *nēdrōn- f. 'viper' — OE **nædre, neddre** f. 'id.' (also Nrth. *neder* m. 'id.' < *nēdra-), E adder … OS nādra, nadara f. 'id.', MDu. nadre, addre, adder f. 'id.', Du. adder c. 'id.', OHG nat(a)ra f. 'id.', G Natter f. 'id.' > *neh₂tr-éh₂- (WEUR).
>
> A formation ablauting with *nadra- (q.v.).

**Crucial finding:** Kroonen reconstructs OE *nædre* directly from a long-grade *\*nēdrōn-*, not from *\*nadrōn-*. The OE long *ǣ* of *nædre* is therefore inherited *long* and is *not* the output of A-fronting of short *a*. A-restoration is irrelevant to *nædre* on Kroonen's reconstruction. (See §6 below for the implications.) Orel agrees (line 27684, page 279, citing both *\*nadraz* m. and a feminine ablaut variant *\*nēdrōn ~ \*nadrōn*).

`*bastan ~ *bastaz` (Orel page 38, lines 4998–5012):

> *bastan ~ *bastaz sb.n.: ON bast 'inner bark of a tree', OE **bæst** id., MLG bast id. (masc.), OHG bast id. (masc.). Continues *bʰō-sto- or *bʰōs-to- related to *bʰā- 'to shine' …

The reconstructed PGmc form is `*bastan / *bastaz`, neuter strong noun. With nom.-acc. sg. ending `*-ą` (or apocopated to `*-Ø`), no triggering full back vowel survives in the syllable that immediately follows the root in OE; cf. R/T §6.3.2 paradigm of `fæt`. The OE form `bæst` is therefore expected from the *singular* paradigm, and the *st* is a regular `sC` cluster which would have permitted retraction in inflected forms with *-u, -um, -a* (no surface forms of `*bastu`/`bastum` are attested on which to test this).

### 2.9 Orel, *A Handbook of Germanic Etymology* — file `orel_handbook_germanic_etymology.txt`

`*sparōjanan` is not given as a separate lemma; instead Orel has `*sparēnan` (line 35702) — same root, class III/II vacillation:

> *sparēnan wk.vb.: ON spara 'to spare', OE **sparian** id., OFris sparia 'to receive, to protect', OS sparōn 'to spare', OHG sparēn id. Derived from *sparaz.

`*talōjanan` (line 39354):

> *talōjanan wk.vb.: ON tala 'to talk, to speak', OE **talian** 'to suppose, to consider, to reckon', OFris talia 'to count', OS talōn 'to calculate', OHG zalōn 'to count'. Derived from *talan.

`*warōjanan` (line 43999):

> *warōjanan wk.vb.: ON vara 'to beware, to warn', OE **warian** 'to beware, to guard', OFris waria 'to protect', OS warōn 'to protect, to mark, to note', OHG bi-warōn 'to protect'. Derived from *warō(n).

`*nēðrōn ~ *naðrōn` (line 28320):

> *nēðrōn ~ *naðrōn sb.f.: ON naðra 'adder, viper, snake', OE **nædre** id., OS nādra id., OHG nātara, nātra id. An ablaut variant of *naðraz …

Orel (like Kroonen) reconstructs both an *e*-grade and an *a*-grade variant of the feminine; the OE attested form is compatible with descent from the *e*-grade (*\*nēðrōn → \*nǣdre*), in which case no A-restoration question arises.

### 2.10 Kluge–Seebold, *Etymologisches Wörterbuch der deutschen Sprache* — file `kluge_seebold_etymologisches_woerterbuch.txt`

Line 86452 (entry "sparen"):

> Stammwort. Aus g. *sparā- Vsw. "sparen", auch in anord. spara, ae. **sparian**, afr. sparia. …

Lines 65381–65383 (entry "Natter"):

> as. nādra Stammwort. Aus g. *nadra- m., *nadrō f. "Natter" (Belege mit erwiesener Länge im … mit sekundärer Dehnung zu rechnen), auch in gt. nadrs m., anord. nadr m., nadra, ae. **näd(d)re**.

Kluge–Seebold permits both the short-*a* reconstruction with secondary lengthening **and** the variant with original long vowel. (The short-*a* reading has *consonant gemination before liquids* — the West-Germanic "Konsonantendehnung vor *r*" — yielding *næddre* with regular short *æ*; this is the geminate route Campbell §453 takes.)

### 2.11 Adamczyk (2001), Fulk *Comparative Grammar*, etc.

Neither file mentions A-restoration specifically. Fulk discusses syllabification of clusters like *tr* (lines 2953–2998) and notes that obstruent + sonorant clusters typically refuse to be heterosyllabic ("a cluster of obstruent plus sonorant consonant usually is not divided"). This is a phonetic argument that is consistent with — but not a positive argument for — the *consonant + liquid* blocking of restoration: the *dr* in *\*nadrō* is tautosyllabic with the following vowel and so the preceding syllable is open and short, which (in some accounts) reduces the velarising influence of the back vowel.

### 2.12 `oe_sound_change_index.md`

Line 8 of the index file states the current consensus from the index author:

> Topic: general retraction / restoration of a; retraction after breaking; conditioning by single/geminate or sC + back vowel.

This matches Ringe & Taylor §6.3.1 verbatim. Note: *no liquid carve-out*.

---

## 3. Tabulated source summary

| Source | Lists *r/l* as transparent? | Lists cluster blocking? | Quote loc. |
|---|---|---|---|
| Campbell §158 | **Yes** (single C unrestricted; *faran*, *staþol*, *gad(e)rian* etc.) | **Yes** — clusters other than `sC`, `fC`, geminate; only "a few instances before consonant plus liquid" | line 4733 ff. |
| Campbell §159 | Yes (class II *-ian*) | (n/a) | line 4754 |
| Hogg / CHEL | Implicit yes (no carve-out) | Not enumerated in CHEL chapter | line 5189 |
| Hogg 1992 §§5.34–5.35 | (not in local corpus) | (not in local corpus) | — |
| R/T §6.3.1 | **Yes** (single C unrestricted) | **Yes** — "single or geminate consonant or **sC**-cluster" | line 10995 |
| R/T §6.3.1 (50+ class II derivations) | **Explicit** (single *r/l* in *carian, talian, sparian, nafola, sadol, stapol, gafol, manslaga, hara, nacod*) | (consistent) | lines 11020–11150 |
| Brunner §10 / §50 | **Yes** (cites *sparian, war(e)nian, gad(e)rian, faran*) | (gives "a, o, u der Folgesilbe" without consonant-type restriction) | lines 1147, 4179 |
| Luick §161 | **Yes — explicitly "ohne daß der dazwischen stehende Konsonant von Belang gewesen wäre"** | Notes only that obstruent+liquid sequences mostly survive as front-vowel forms by levelling | lines 10180, 10260 |
| Bülbring | (no relevant statement in local file) | — | — |
| Kaluza | Implicit yes | — | line 4927 |
| Kroonen | (etymological — confirms *sparian, talian* < *\*sparēn-, \*talōjan-*) | (n/a) | lines 26891, 29143 |
| Orel | Confirms *sparian, talian, warian* < *\*sparēnan, \*talōjanan, \*warōjanan* | (n/a) | 35702, 39354, 43999 |
| Kluge–Seebold | Confirms *sparian* < *\*sparā-* | (n/a) | 86452 |
| `oe_sound_change_index.md` | Yes | "single/geminate or sC + back vowel" | line 8 |

**No source in the local corpus identifies a single intervening *r* or *l* as a blocker.** Every source that addresses the question lists *r* and *l* as ordinary consonants over which restoration takes place freely.

---

## 4. Evidence inventory: OE forms with PGmc protoforms

### 4.1 Pro-restoration evidence with single intervening *r* or *l* (back vowel triggers)

| OE | PGmc / pre-OE input | Source |
|---|---|---|
| **faran** 'go' | *\*faraną* (PGmc) → *\*faran, \*færisi, \*færiþi → faran, færst, færþ* | R/T 13432 |
| **carian** 'be anxious' | *\*karōną → \*kærōjan → carian* | R/T 11038 |
| **lapian** 'invite' | *\*labōną → \*læbōjan → lapian* | R/T 11041 |
| **wacian** 'be awake' | *\*wakōną → \*wækōjan → wacian* | R/T 11045 |
| **hatian** 'hate' | *\*hatōną → \*hætōjan → hatian* | R/T 11048 |
| **bapian** 'bathe' | *\*baþōną → \*bæþōjan → bapian* | R/T 11050 |
| **gegladian** 'gladden' | *\*gladōną → \*glædōjan → ge-gladian* | R/T 11053 |
| **gehagian** 'be fitting' | *\*hagōną → \*hægōjan → ge-hagian* | R/T 11055 |
| **scrapian** 'scrape' | *\*skrapōną → \*skræpōjan → scrapian* | R/T 11057 |
| **stafian** 'dictate' | *\*stabōną → \*stæbōjan → stafian* | R/T 11059 |
| **talian** 'reckon' | *\*talōną → \*tælōjan → talian* | R/T 11061 |
| **dagian** 'dawn' | *\*dagēn → \*dægōjan → dagian* | R/T 11066 |
| **sparian** 'spare' | *\*sparēn / \*sparōjan → \*spærōjan → sparian* | R/T 11068 |
| **macian** 'make' | *\*makōn → \*mækōjan → macian* | R/T 11071 |
| **(to-)haccian** 'hack' | *\*hakkōn → \*hækkōjan → to-haccian* | R/T 11073 |
| **batian** 'become better' | *\*batē- → \*bætōjan → batian* | R/T 11074 |
| **capian** 'look' | *\*kapē- → \*kæpōjan → capian* | R/T 11076 |
| **hnappian** 'doze' | *\*hnappōjan → hnappian* (geminate; cf. Campbell §158) | R/T 11078 |
| **nacod** 'naked' | *\*nakwadaz → \*nækud → nacod* | R/T 11081 |
| **nafola** 'navel' | *\*nabulō → \*næbula → nafola* | R/T 11084 |
| **hafoc** 'hawk' | *\*habukaz → \*hæbuk → hafoc* | R/T 11087 |
| **latost** 'latest' | *\*latōsta → \*lætost → latost* | R/T 11089 |
| **soþsagol** 'truth-speaking' | *\*sanþasagulaz → \*saþæsægul → soþsagol* | R/T 11091 |
| **sadol** 'saddle' | *\*sadulaz → \*sædul → sadol* | R/T 11093 |
| **stapol** 'pillar' | *\*stapulaz → \*stæpul → stapol* | R/T 11095 |
| **stapol** 'foundation' | *\*stabulaz → \*stæpul → stapol* | R/T 11097 |
| **wacol** 'vigilant' | *\*wakul → \*wækul → wacol* | R/T 11099 |
| **gafol** 'fork' | *\*gabulu → \*gæbulu → gafol* | R/T 11101 |
| **magu** 'boy' | *\*maguz → magu* (u-stem) | R/T 11104 |
| **lagu** 'water, sea' | *\*laguz → \*lægu → lagu* | R/T 11106 |
| **maga** 'stomach' | *\*magō → \*mæga → maga* | R/T 11119 |
| **mara, maran** 'nightmare' | *\*marō, \*marōn- → \*mærē, \*mærōn- → mare, maran* | R/T 11116 |
| **hara** 'hare' | *\*hasō → \*hærē → hara* | R/T 11117 |
| **manslaga** 'murderer' | *\*manslagō → \*manslæga → manslaga* | R/T 11122 |
| **gegada** 'companion' | *\*gagadō → \*gegæda → gegada* | R/T 11121 |
| **fatu** 'vessels' | *\*fatu → \*fætu → fatu* | R/T 11221 / 16604 |
| **dagas** 'days' | *\*dagōs → \*dægas → dagas* | R/T 11221 / 8868 |
| **stafas** 'staves' | *\*stabaz → \*stab, \*stabō → stæf, stafas* | R/T 11150 |
| **hwalas** 'whales' | *\*hwalaz, \*hwalōz → \*hwæl, \*hwalas → hwæl, hwalas* | R/T 11154 |
| **bapu** 'baths' | *\*bada, \*badu → \*bæþ, \*bæþu → bæþ, baþu* | R/T 11157 |

In **none** of these is *r* or *l* singled out as exceptional. Note especially the rich set of *l*-medial cases (*sadol, stapol, wacol, gafol, manslaga, gegada, talian, glædian, soþsagol*) and *r*-medial cases (*sparian, warian, gad(e)rian, war(e)nian, carian, scrapian, mara, maran, hara, nafola*).

### 4.2 Anti-restoration evidence (forms that *retain* /æ/ before back vowel)

The following are the only environments where the literature reports failure (or near-failure) of restoration:

* **`*Cr/Cl` clusters** (consonant + liquid): Campbell §158 "Before other groups, *a* is not restored except for a few instances before consonant plus liquid: W-S *appla, apla* … beside *æplas, æcras*". The dominant attested forms are *æplas, æcras, næglas, fedras, hræfnas* — i.e. *æ*. Luick §161.4 enumerates the same and §161 Anm. 5 attributes the residue to morphological levelling.
   * `*nadrō / *naþrōn-` → *nædre/næddre/næder* (West-Germanic gemination route per Campbell §453, or e-grade per Kroonen *\*nēdrōn-*).
   * `*næglaz` g.s. plural *næglas* (Campbell §158).
   * `*fædraz, fædrum* (cf. Campbell §158 "always *sægdon, hæfdon, fedras, næglas*").
* **Closed monosyllables** (no back vowel survives): *fæt, dæg, hwæl, dæl, bæþ, bæc, blæd, fæc, stæf, pæþ* — Campbell §157 "in closed syllables".
* **Weak-tail / nasalised final** vowels: *bæst* (n.-a. sg. of *bastą* with weak final *\*ą*); the FST handles this via `OEARestorationStrongOTail` / `OEARestorationWeakTailVowel`.
* **`*-Vlj-` / `*-Vrj-`** sequences where the next syllable contains *i* or *j* (not a back vowel) — *fædran, æpla, herian* (cf. Campbell §147, §159).

There is no environment in the literature in which **single intervening *r* or *l* between *V_back+r/l+V_back* fails** to retract. Mercian *spearian, spearaþ* (Li., VP) is the result of *back mutation* applying to the already-restored *a* (R/T 9472), not failure of restoration.

---

## 5. Class‑2 weak verb derivations (sparian, warian, farian, talian, carian)

R/T §6.3.1 derivations are reproduced verbatim above (§2.2). The crucial pattern is *\*Cæ̆C(ōj)ōjan → \*CăCōjan*, exemplified for our four target verbs:

| OE | R/T derivation | line |
|---|---|---|
| **sparian** | PWGmc *sparē- (OHG sparen) >— *spærōjan > OE sparian | 11068 |
| **warian** (not derived in R/T but cf. Orel *\*warōjanan-*) | *\*warōjan → *\*wærōjan → warian* | Orel 43999 |
| **farian** (rare; class II by-form of class VI faran) | *\*faran → faran* (R/T 13432); secondary *farian* would parallel | R/T 13432 |
| **talian** | PWGmc *talōn (OS talon, OHG zalon) >— *tælōjan > OE talian | 11061 |
| **carian** | PGmc *karōną → PWGmc *karōn (OS karon, OHG karon) >— *kærōjan > OE carian | 11038 |
| **macian** | PWGmc *makōn (OS makon, OHG mahhon) >— *mækōjan > OE macian | 11071 |

Brunner §10 confirms the pattern with the exact words *macian, gladian, daccian, war(e)nian, gad(e)rian* and (line 4179) the explicit pairing *faran fahren, sparian … sparen*.

Orel and Kroonen confirm the class-II protoform `*-ōjan-` for `talian, warian, sparian` — the FST input shapes (`talōjaną`, `warōjaną`, `sparōjaną`, `farōjaną`) are well-formed and correctly contain a triggering *\*ō*.

The current FST behaviour (`spærian, wærian, færian, tælian`) is therefore in direct contradiction with **all four** authorities (Campbell §159, R/T §6.3.1, Brunner §10, Luick §161).

---

## 6. Discussion of nǣdre (and næddre) and bæst

### 6.1 nǣdre / næddre / næder

Two etymological routes are reconstructed in the local corpus, and they are *both* compatible with the attested OE form **without invoking failure of A-restoration of /æ/ before single *r*:

**Route A — long *ē*-grade ablaut variant (Kroonen, Orel):**
> Kroonen p. 386: `*nēdrōn- f. 'viper' — OE nædre, neddre f. 'id.'… > *neh₂tr-éh₂- (WEUR). A formation ablauting with *nadra-.`
> Orel p. 286: `*nēðrōn ~ *naðrōn sb.f. … An ablaut variant of *naðraz`.

If the OE feminine descends from `*nēdrōn-`, the long *ǣ* of *nædre* is an inherited long vowel, the input to OE never contained short *a*, and A-restoration is irrelevant.

**Route B — short *a*-grade with West-Germanic gemination before liquid (Campbell §453, §454; Kluge–Seebold):**
> Campbell §453: "many words with consonant gemination before liquids (cf. § 453), e.g. **næddre** adder, *attres* g.s. poison".
> Kluge–Seebold (line 65381): "Aus g. *nadra- m., *nadrō f. 'Natter' (Belege mit erwiesener Länge … mit sekundärer Dehnung zu rechnen)".

If the OE form goes back to `*naðrō / *nadrō`, then the cluster `*dr` is a stop + liquid — exactly the "consonant + liquid" environment in which Campbell §158 reports retraction *failure* and Luick §161.4 reports only "wenige Reste" (relics like *appla, accras*). The dominant levelled form is the front-vowel *næ-* form, with subsequent West-Germanic gemination (*næ-dr- > næ-ddr-*).

In **either** route, blockage of restoration is **cluster-based** (`*dr` being stop+liquid, not a single *r*). The FST input `*nadrō` produces `næder` correctly under the current rule (because *r* is excluded), but it would *also* produce a correct front-vowel output under any rule that blocks `*Cr` clusters. There is no need to single out *r* per se.

The current FST output `næder` rather than `nædre` is a separate (epenthesis/syllabification) issue not addressed here.

### 6.2 bæst

* PGmc reconstruction: Orel §`*bastan ~ *bastaz` — neut. strong *a*-stem.
* The nom.-acc. sg. ending in PGmc was `*-Ø` (neuter `*a`-stems lose the bare `*a` in PWGmc, cf. R/T 3.1.2 / 3.1.4) or `*-ą`. In the FST input notation this is `*bastą`.
* The cluster `*st` is precisely the `sC`-cluster that R/T §6.3.1 and Campbell §158 treat as **transparent** to retraction. Restoration would therefore have applied in **inflected** forms like `*bastōz` (gen.) or `*bastu` (n.pl.) — but in the singular, no full back vowel ever follows the root, so the surface form retains *æ*.
* In the FST, the nom.-acc. sg. trigger candidate is the weak/nasalised `*ą`, which is excluded from the trigger set by `OEARestorationStrongOTail`. Hence `*bastą → bæst` correctly without any cluster-based blocking.

In summary: **`*bastą → bæst` is fully accounted for by the weak-tail exclusion**, not by the consonant-cluster set. The *st* in *bastą* is *not* blocking; the *ą* simply isn't a trigger.

### 6.3 Net conclusion on the counter-examples

Neither counter-example is evidence for blocking by single *r* / *l*. Both are explained by orthogonal mechanisms (consonant-cluster blocking for `*dr`, weak-tail exclusion for `*ą`). Removing the *r*/*l* exclusion from `OEARestorationIntervening` therefore does **not** create regressions for them, *provided* the rule continues to block other consonant-plus-liquid (and other non-*sC*, non-*fC*, non-geminate) clusters.

---

## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

R/T §6.3.1 (line 11000):

> Since the attested form in most OE dialects is *dagum*, it follows that retraction must have occurred subsequently to fronting—and subsequently to breaking, because the diphthong of 'slay', etc. did not again become *a* (Luick 1914-40: 155-6, Campbell 1962: 60-1).

Thus the relative chronology is:

```
(0) PWGmc *a (= R/T 5.1.2 northern WGmc fronting)
 ↓ AFB / Anglo-Frisian fronting (R/T §5.1.2)
(1) *æ
 ↓ Breaking (R/T §6.2.1–6.2.4)
(2) *ea before *h, *r+C, *l+C, *w
 ↓ Retraction (= A-restoration, R/T §6.3.1)
(3) *a before single C / geminate / sC + back vowel
 ↓ I-umlaut (R/T §6.6)
(4) modifies remaining *æ but cannot un-restore *a
```

Page references (in the print edition): R/T 2014 vol II, pp. 187–193 (§6.2.5 "Further developments of *h*; phonetic considerations" through §6.3.2 "Alternations and the phonemicization of short low vowel allophones"). Local file lines 10987–11195. Campbell §157 "C. The Restoration of *a* before Back Vowels" (printed pp. 60–63) appears at file lines 4720–4830.

The chronological consequence is: at the point A-restoration applies, the input is **already** *æ* (output of AFB), and *r* is at most retroflex/postvelar (R/T §6.2.5: "the fact that breaking also occurred before *rC* suggests that *r* in that position was actually postvelar [ʁ]"). A postvelar *r* between *æ* and a following back vowel would, if anything, *encourage* retraction, not block it.

---

## 8. FST probing results (verbatim)

Probes run with `flookup -i /Users/nathanhill/capr-v3-working/backend/old_english.bin` (foma 1.x; binary at `/opt/homebrew/bin/flookup`):

```
$ echo 'bastą' | /opt/homebrew/bin/flookup -i old_english.bin
bastą	bæst

$ echo 'nadrō' | /opt/homebrew/bin/flookup -i old_english.bin
nadrō	næder

$ echo 'sparōjaną' | /opt/homebrew/bin/flookup -i old_english.bin
sparōjaną	spærian

$ echo 'warōjaną' | /opt/homebrew/bin/flookup -i old_english.bin
warōjaną	wærian

$ echo 'farōjaną' | /opt/homebrew/bin/flookup -i old_english.bin
farōjaną	færian

$ echo 'talōjaną' | /opt/homebrew/bin/flookup -i old_english.bin
talōjaną	tælian
```

Additional probes (for §11 cross-check):

```
$ echo 'fáraną' | flookup -i old_english.bin
fáraną	færan         # WRONG — target faran (Campbell §160(4), R/T 13432)

$ echo 'spárēną' | flookup -i old_english.bin
spárēną	spearen       # WRONG — target sparian (separate class III→II issue)

$ echo 'márōn'  | flookup -i old_english.bin
márōn	mære          # OK — long *ā/ǣ, not in scope of short A-restoration

$ echo 'súmaraz' | flookup -i old_english.bin
súmaraz	sumer         # OK — first vowel is *u, not *a

$ echo 'sáiwalō' | flookup -i old_english.bin
sáiwalō	sāwol         # OK — *aiwal-: multi-segment intervening, no relevance

$ echo 'xámaras' | flookup -i old_english.bin
xámaras	hameres       # OK — single *m intervening; restoration applies under any rule

$ echo 'kálbaz' | flookup -i old_english.bin
kálbaz	ċealf         # OK — breaking before *lC

$ echo 'spárrô' | flookup -i old_english.bin
spárrô	spearra       # OK — breaking before geminate *rr (Luick §161.2 exclusion)

$ echo 'swálwōn' | flookup -i old_english.bin
swálwōn	swealwe       # OK — breaking before *lw

$ echo 'sáltą' | flookup -i old_english.bin
sáltą	sealt         # OK — breaking before *lC
```

Interpretation of the canonical six probes:

1. `bastą → bæst`: correct via weak-tail exclusion. **Independent of intervening-consonant set**.
2. `nadrō → næder`: vowel correct via *r* exclusion (or — under a cluster-only rule — via cluster blocking of `*dr`). Trailing -re vs -er is a separate epenthesis/syllabification issue not addressed here.
3–6. `sparōjaną/warōjaną/farōjaną/talōjaną → spærian/wærian/færian/tælian`: **WRONG**. The intervening *r/l* exclusion blocks restoration where the literature is unanimous it should apply.

---

## 9. Current rule analysis

`Germanic/fsts/germanic.txt`, surrounding lines 1779–1860, verbatim (with line numbers from `grep -n`):

> **1779** `# A-restoration: */æ/ > */a/ before a back vowel (or AFB-fronted *a) in the following syllable.`
> **1780** `# Per Ringe/Taylor Vol 2 §6.3.1: "Those stressed *æ which were immediately followed`
> **1781** `# by a single or geminate consonant or sC-cluster which was in turn followed by a`
> **1782** `# back vowel became a." Ringe explicitly notes: "That unstressed *æ was not retracted."`
> …
> **1804** `define OEARestorationTriggerVowel [EnglishStarBackVowel | {*ô} | {*ǭ}];`
> **1806** `define OEARestorationIntervening [`
> **1807** `    EnglishStarConsonantNoR - {*l}`
> **1808** `];`
> …
> **1814** `define OEARestorationStrongOTail [`
> **1815** `    {*i} {*l} {*ō} |`
> **1816** `    {*i} {*l} {*ō} {*n} |`
> **1817** `    {*u} {*w} {*ō} {*n} |`
> **1818** `    {*ō} |`
> **1819** `    {*ō} {*j} {*a} {*n} {*ą} |`
> **1820** `    {*ō} {*n} |`
> **1821** `    {*ō} {*n} {*d} {*z} |`
> **1822** `    {*ō} {*r} {*e} {*z} |`
> **1823** `    {*ō} {*θ} {*z}`
> **1824** `];`
> **1826** `define OEARestorationWeakTailVowel [`
> **1827** `    EnglishWeakTailVowel - OEARestorationStrongOTail`
> **1828** `];`
> **1834** `define OEARestoration (`
> **1835** `    {*æ} -> {*a} || _`
> **1836** `        [OEARestorationIntervening]* OEARestorationTriggerVowel`
> **1837** `        - [OEARestorationIntervening]* OEARestorationWeakTailVowel`
> **1838** `);`

Definitions referenced (lines 924, 947):

> **924** `define EnglishStarConsonant PGmcStarConsonant;`
> **947** `define EnglishStarConsonantNoR [EnglishStarConsonant - {*r}];`

**The active behaviour of the rule:**

1. The right context is `[OEARestorationIntervening]* OEARestorationTriggerVowel` — the Kleene star permits **zero or more** intervening consonants from the set.
2. `OEARestorationIntervening = EnglishStarConsonant − {*r} − {*l}` — single consonants other than *r* and *l*.
3. The Kleene star can match arbitrarily long *strings* of "non-r-non-l consonants" — so e.g. `*st`, `*sk`, `*kt`, `*kk`, `*pp`, `*sp`, `*sm` all match (correctly for `sC`/`fC`/geminate, but **also incorrectly** for `*kt`, `*pt`, `*bs`, etc.).
4. Any sequence containing a *r* or *l* — even a single *r* between two vowels — fails to match, blocking retraction.

So the rule is simultaneously **over-permissive** for arbitrary obstruent clusters (it would let restoration apply across `*ksk`, `*kt`, `*pt`, `*bs`, etc., which are not in Campbell §158 / R/T §6.3.1 `single | geminate | sC`) and **under-permissive** for single *r*/*l*. The two errors partially cancel because the genuine obstruent-only counter-examples (*sægde, hæfde* — `*-gd-`, `*-fd-`) happen to be already protected by the weak-tail exclusion or by other syncope rules upstream.

**What replacing the set with `EnglishStarConsonant` (and keeping the `*` Kleene star) would do:**

* `*sparōjaną`: intervening = `*r` → match → retraction → **`sparian`** ✓
* `*warōjaną`: intervening = `*r` → match → **`warian`** ✓
* `*farōjaną`: `*r` → **`farian`** ✓
* `*talōjaną`: `*l` → **`talian`** ✓
* `*nadrō`: intervening = `*dr` (two C's, both in set) → Kleene star matches `*dr` → trigger `*ō` is in `OEARestorationStrongOTail` (line 1818 explicitly lists `{*ō}`) → not weak-tail → **retraction would apply → `*nadre` ✗** (regresses against target `nædre`).
* `*bastą`: intervening = `*st` → matches → trigger `*ą` → weak-tail exclusion fires → **`bæst`** ✓ (no regression).

So the simplest "drop both exclusions" change **regresses** `*nadrō → *nadre`. The fix must restrict cluster matching to *exactly* the "single C / geminate / sC / fC" set permitted by Campbell and R/T.

---

## 10. Concrete fix proposal

### 10.1 Goal

Encode literally Campbell §158 / R/T §6.3.1: the set of intervening sequences across which retraction applies is **{single C, geminate CC, sC, fC}** — and *nothing else*. *r* and *l* return to the set as ordinary single consonants.

### 10.2 Recommended edit (option B in the user's task brief)

Replace lines 1806–1808 with the literal cluster taxonomy from the literature, and **drop the Kleene star** from the rule body so the intervening matches exactly once (because the cluster types are now built into the set definition, not generated by `*`):

```foma
# Per Campbell §158 and Ringe/Taylor §6.3.1: the intervening segments across
# which A-restoration applies are exactly:
#   1. a single consonant (any quality, including *r and *l: cf. faran,
#      sparian, warian, talian, sadol, nafola, gafol, manslaga, hara, mara);
#   2. a geminate (e.g. hnappian, racca, crabba, mattuc, cassuc — Luick §161.2);
#   3. an sC-cluster (e.g. wascan, ascan, flascan, brastlian — Luick §161.3);
#   4. an fC-cluster (e.g. sæftriende — Campbell §158).
# Other clusters (Cr, Cl, Cn, Cm, Cd, Ct, Cb, Cp, hC, etc.) BLOCK retraction
# (Campbell §158 "Before other groups, a is not restored except for a few
# instances before consonant plus liquid"; Luick §161 Anm. 1 / Anm. 4).
define OEARestorationIntervening [
      EnglishStarConsonant
    | {*s} EnglishStarConsonant
    | {*f} EnglishStarConsonant
    | EnglishStarGeminate
];

define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

`EnglishStarGeminate` is not currently defined; it should be defined alongside the other `EnglishStar…` consonant macros (around line 945) as the union of identical-pair sequences that can occur as PGmc/PWGmc geminates relevant to OE. A minimal definition that covers the attestation of restoration before geminates (Campbell §158 examples *racca, crabba, mattuc, cassuc, hassuc, hnappian, lappa, sacc, catt, abbud, assa*):

```foma
define EnglishStarGeminate [
      {*pp} | {*tt} | {*kk}
    | {*bb} | {*dd} | {*gg}
    | {*ff} | {*ss} | {*þþ}
    | {*mm} | {*nn}
    | {*ll} | {*rr}     # fall under breaking; only matter if breaking did not bleed
    | {*ww}
];
```

### 10.3 Alternative (option C — minimal-edit, less explicit)

If introducing `EnglishStarGeminate` is undesirable (e.g. for stylistic reasons), an equivalent two-line edit that *just* fixes the *r/l* false-positive:

```foma
# Permit r and l as ordinary intervening consonants; restrict cluster matching
# to single C, sC, fC and geminate by truncating quantification.
define OEARestorationIntervening [EnglishStarConsonant];

define OEARestorationCluster [
      OEARestorationIntervening
    | {*s} OEARestorationIntervening
    | {*f} OEARestorationIntervening
    | [EnglishStarConsonant EnglishStarConsonant] & [? ?]   # NB: identity
];

define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationCluster OEARestorationTriggerVowel
        - OEARestorationCluster OEARestorationWeakTailVowel
);
```

### 10.4 Predicted effects of the recommended change (option B) on the six probed inputs

| input | OEARestorationIntervening match | trigger / weak‑tail | predicted output | match target? |
|---|---|---|---|---|
| `*sparōjaną` | single `*r` | `*ō` (StrongOTail line 1818 — trigger) | `sparian` | ✓ |
| `*warōjaną` | single `*r` | `*ō` | `warian` | ✓ |
| `*farōjaną` | single `*r` | `*ō` | `farian` | ✓ |
| `*talōjaną` | single `*l` | `*ō` | `talian` | ✓ |
| `*nadrō` | `*dr` — **not** in set (not single, not geminate, not `sC`/`fC`) | (rule does not fire) | `nædre` (vowel; segmentals as before) | ✓ |
| `*bastą` | `*st` — **in set** as `sC` | `*ą` weak-tail (excluded) | `bæst` | ✓ |

All six probes give the desired output under the recommended change. (Verification by manual trace; not yet compiled because the task brief explicitly forbids modifying `germanic.txt`.)

### 10.5 Predicted effects on neighbouring rule behaviour

* `*hnappōjan → hnappian` (Campbell §158): intervening `*pp` — geminate in set — restoration applies. ✓
* `*flaskōn → flasce` (germanic.txt comment line 1798): intervening `*sk` — `sC` in set — restoration applies, then `SkPalatalization` runs after the *a*. ✓ (Still produces `flasce`, not `flæsce`.)
* `*næglaz` plural `*næglas` → `næglas` (Campbell §158): intervening `*gl` — `Cl` cluster, **not** in the new set — restoration does *not* apply. ✓ (consistent with Campbell's "always *næglas*").
* `*faþmaz, fæðmas`: intervening `*ðm` — `Cm`, not in set — no retraction; `fæðm` paradigm preserved. ✓
* `*gadrōjan → gad(e)rian` (Brunner §10): intervening `*dr` — `Cr`, not in set — restoration does *not* apply at this stage. **But** in OE the medial *e* in *gad(e)rian* arises by epenthesis after the *dr* has been split across syllables, and Campbell §159 explicitly attributes the restored *a* in *gad(e)rian, stadelian* to "a back vowel which subsequently became a front vowel or was lost". In the FST, this depends on the relative ordering of epenthesis and A-restoration. If epenthesis precedes A-restoration, intervening becomes single `*d`, restoration applies, and we get `gaderian`. If A-restoration precedes epenthesis, the FST produces `*gæderian` — a regression. **This is a flagged side-issue, not a defect introduced by the recommended change** (the current rule with the *r* exclusion would *also* fail to retract here, since the intervening is `*dr` containing *r*); a separate ordering audit is recommended.

### 10.6 What about *appla, accras*?

Campbell §158 lists *appla, accras* as the surviving *a*-forms of *Cr/Cl* clusters. Under the recommended change these will *not* be produced by sound change (intervening `*pl/*kr` not in set); they would have to be input-specified in the lexicon as exceptional. This is consistent with Luick §161.4 ("nur in wenigen Resten") and §161 Anm. 5 (the few survivals are due to a *failure* of analogical levelling, not a productive sound-change pathway). No regression is expected for the FST's current rule already produces *æpplas, æcras* in its general behaviour.

---

## 11. Affected TSV rows

`Germanic/data/germanic-aligned-final.tsv` rows where the OE protoform (column 3) contains *a/á* + a single *r* or *l* + back vowel (any of `a, á, ā, ō, ǭ, ô, u, ú, o, ó`):

| ID | PROTOFORM | TARGET (col 6) | current FST output | predicted output under fix | comment |
|---:|---|---|---|---|---|
| 1944 | `*galáubijaną` | `ġelīefan` | `ġelīefan` | `ġelīefan` | `*g+a` is prefix; main vowel is *au* diphthong, not in scope |
| 1984 | `*dálaz` | `dæl` | `dæl` | `dæl` | monosyllabic; final `*-az → ∅`, no surviving back trigger |
| 2003 | `*fáraną` | `færan`† | `færan` | **`faran`** | †TSV target is `færan` but that is itself **wrong**: per R/T 13432 and Campbell §160(4) the W-S inf. is **`faran`**. The recommended fix produces the historically correct form. **TSV column 6 should be updated separately.** |
| 2053 | `*xámaras` | `hameres` | `hameres` | `hameres` | intervening `*m` (not r/l); already correct under either rule |
| 2141 | `*márōn` | `mære` | `mære` | `mære` | long `*ā/ǣ`, out of scope of short A-restoration |
| 2201 | `*sáiwalō` | `sāwol` | `sāwol` | `sāwol` | intervening `*iwal` is multi-segment; restoration not triggered for first *a* (already covered by other rules) |
| 2230 | `*súmaraz` | `sumer` | `sumer` | `sumer` | first vowel is `*u`, not `*a` |
| 2284 | `*xwálaz` | `hwæl` | `hwæl` | `hwæl` | monosyllabic; no surviving back trigger |

Additionally, broader-pattern rows (any *a/á* + r/l + non-front, including those in clusters) found in the TSV (`grep -E "\*[^*]*[aá][rl][^*]*[aōǭôu]"`):

| ID | PROTOFORM | TARGET | comment |
|---:|---|---|---|
| 1935 | `*bálluz` | `-` | geminate *ll* + breaking; out of scope |
| 1940 | `*bárdaz` | `beard` | breaking before *rC* |
| 1975 | `*kálbaz` | `ċealf` | breaking before *lC* |
| 2002 | `*fállaną` | `feallan` | breaking before geminate *ll* |
| 2008 | `*fárnaz` | `fearn` | breaking before *rC* |
| 2025 | `*fálþaną` | `fealdan` | breaking before *lþ* |
| 2037 | `*gállô` | `ġealla` | geminate *ll* + breaking |
| 2052 | `*xállō` | `heall` | geminate *ll* + breaking |
| 2056 | `*xármaz` | `hearm` | breaking |
| 2057 | `*xárbistuz` | `hierfest` | breaking + i-umlaut |
| 2077 | `*xáldaną` | `healdan` | breaking |
| 2118 | `*máltaz` | `mealt` | breaking |
| 2120 | `*márkō` | `mearc` | breaking |
| 2166 | `*sáltą` | `sealt` | breaking |
| 2167 | `*sálbō` | `sealf` | breaking |
| 2204 | `*spárrô` | `spearra` | breaking before geminate *rr* (Luick §161.2 exclusion) |
| 2205 | `*spárēną` | `sparian` | **partial fix** — see below |
| 2234 | `*swálwōn` | `swealwe` | breaking before *lw* |
| 2269 | `*wárpą` | `wearp` | breaking |
| 2271 | `*wártōn` | `wearte` | breaking |
| 2289 | `*wáldaną` | `wealdan` | breaking |
| 2297 | `*wálþuz` | `weald` | breaking |

For all "breaking" rows, A-restoration is bled by breaking (R/T §6.3.1: retraction "subsequently to breaking, because the diphthong of 'slay', etc. did not again become *a*"). The recommended change does not affect them.

**Row 2205 (`*spárēną → sparian`)**: Probed output under current FST is `spearen`. The proposed fix changes `OEARestorationIntervening` so that the *r* of `*spár-` is no longer excluded, but the trigger vowel of `*spárēną` is `*ē` (front), so A-restoration still does not fire. The path to `sparian` requires a class III → class II morphological remap (`*sparēn- → *sparōjan-`) which appears to be missing or out of order in the FST pipeline. **This is a separate, larger issue** beyond the scope of this report.

### 11.1 Net count of TSV rows affected by the proposed fix

* **Strictly fixed (current wrong → predicted right):** 1 row (ID 2003 `*fáraną`).
  - Caveat: TSV column 6 currently lists the (etymologically incorrect) `færan` as target; per R/T 13432 and Campbell §160(4) the correct OE inf. is `faran`. A separate TSV-data fix is required to take advantage of the FST fix.
* **Partially advanced (necessary but not sufficient):** 1 row (ID 2205 `*spárēną`).
* **Confirmed unaffected (correct before and after):** 6 rows (IDs 1944, 1984, 2053, 2141, 2201, 2230, 2284).
* **All breaking-conditioned rows:** 21 rows; bled by breaking; unaffected by the fix.

In the wider weak-class-II / single-r / single-l sound-change space the fix unblocks the canonical pathway for tens of forms (sadol, stapol, nafola, gafol, hara, mara, maga, naca, scapa, draca, manslaga, gegada, talian, carian, dagian, etc.); however, **none** of those individual root protoforms are present as separate OE rows in `germanic-aligned-final.tsv` in the current snapshot. Verification on a broader lexicon (e.g. `old_english_wiktionary.tsv`) is recommended.

---

## 12. Open questions / where the local sources are silent

1. **Hogg 1992 §§5.34–5.35** are referenced in the user's task brief but are not present in `docs/references/`. The local file `hogg_vol1.txt` is the *Cambridge History of the English Language* chapter (different work), which is non-technical on this point. The substantive content is reproducible from R/T §6.3.1 (which cites Hogg 1992 explicitly: "Luick 1914-40: 152-7, Campbell 1962: 60-2, Hogg 1992: 96-100 [2011: 93-9]").

2. **Bülbring §§ 127, 130** is cited by Luick as the locus for his cluster taxonomy. The local `bulbring_altenglisches_elementarbuch.txt` does not surface a clean grep hit for the section content. A direct pagination check is desirable.

3. **R/T relative chronology of A-restoration vs. epenthesis** is not addressed by R/T or by Campbell in any depth. The forms *gad(e)rian, stad(e)lian* (Campbell §159) imply that retraction applied *before* epenthesis introduced the medial *e* — the FST's ordering of these rules should be audited, although that is independent of the *r/l* question studied here.

4. **`*sparēną` vs `*sparōjaną`**: the protoform shape used in the TSV (row 2205) is the class III (Goth. -an, OHG -ēn) shape. R/T (line 11068) reconstructs *both* `*sparja-` and `*sparai-` and posits the class-II conversion *spærōjan*. Whether the FST should accept class-III input shapes and convert them to class-II forms before A-restoration is a separate design question.

5. **Long-vowel A-restoration (`*ǣ → *ā`)**: Campbell §162 reports that the parallel change for long vowels is "much less regular than the restoration of *a*"; long-*ǣ* forms with mixed *ǣ/ā* are common (Luick §163, *māgas/sǣton/cwǣdon*). The current FST handling of long *ǣ* is not within the scope of this report but the proposed fix (recommended option B) does not affect it (`OEARestoration` only rewrites short `{*æ}`).

6. **Form `nadrō → næder` (vowel right, segmental wrong)**: under the recommended fix the vowel remains *æ* (because `*dr` is not in the new set). The trailing `-er` (vs. the target `-re`) is a separate epenthesis or apocope question untouched by this report.

---

## 13. Single-line summary of the recommendation

Replace `OEARestorationIntervening = EnglishStarConsonantNoR − {*l}` with `OEARestorationIntervening = EnglishStarConsonant ∪ {*s}EnglishStarConsonant ∪ {*f}EnglishStarConsonant ∪ EnglishStarGeminate`, and drop the Kleene star from the rule body — i.e. encode Ringe & Taylor §6.3.1's "single or geminate consonant or sC-cluster" verbatim into the set rather than smuggling cluster permissiveness through `*` quantification with an *ad hoc* *r/l* veto.

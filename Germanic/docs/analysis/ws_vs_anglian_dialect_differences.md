# West Saxon vs. Anglian: dialect differences in Old English

Working reference for the CAPR FST PGmc → OE pipeline. Every citation below
has been verified against the in-repo handbook texts; line-number references
point into the `.txt` OCR files in `docs/references/`. OCR noise is preserved
in quotations (and flagged where it is severe). Section/§ numbers cite
Campbell's printed sectioning as it appears inside the OCR.

Cross-references inside the repository:
- `Germanic/docs/DEV_NOTES.md §15` — `swustor`/`swester` smoothing/back-mutation
  discussion, including Campbell §210 fn. 1 on combinative back umlaut after `w`.
- `Germanic/docs/DEV_NOTES.md §17.24` — `*mizdō` dialectal-doublet discussion
  (méd vs. meord) and z-loss before dentals.
- `Germanic/docs/analysis/notable_findings.md #10` — OE `rēc` 'smoke' and the
  missing WS `rīec` problem.
- `Germanic/docs/analysis/notable_findings.md #11` — PGmc `*mizdō` `méd`/`meord`
  dialectal doublet.

The three primary handbooks consulted (with internal line-number ranges
relevant to dialect material):

| Handbook | File | Key range |
|---|---|---|
| Hogg, *A Grammar of OE*, vol. 1: Phonology | `docs/references/hogg_vol1.txt` | §3 (breaking, BM) ll. 5050–5780; ch. 6 (dialects) ll. 20330–21260 |
| Campbell, *Old English Grammar* (1959) | `docs/references/campbell_old_english_grammar.txt` | §§139–169 (breaking, retraction, second fronting) ll. 4360–4940; §§205–233 (BM, smoothing) ll. 6140–6920 |
| Ringe & Taylor, *The Development of Old English* (2014) | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | §6.5 (PD + 2nd fronting) ll. 12450–12800; §6.9.2 (smoothing) ll. 17660–17850; §6.9.4 (back umlaut) ll. 18300–18500 |
| Brunner, *Altenglische Grammatik* (1965) | `docs/references/brunner_1965_altenglische_grammatik.txt` | §119 (Ebnung) ll. 4745–4840 |

---

## 1. Smoothing (Anglian monophthongisation before velars)

Smoothing is the monophthongisation of the OE diphthongs `ea, eo, io` and
their long counterparts `éa, éo, ío` when they stand before a velar
consonant `c, g, h (= /x/)`, either directly or with intervening `r` or `l`.
It does **not** apply before dental clusters or non-velar environments. It
is the diagnostic Anglian feature.

### Campbell §222 (repo lines 6658–6691)

Verbatim (OCR `2` = `æ`, `J` = `l`):

> "§ 222. One of the most marked characteristics of the Anglian dialects
> developed at the end of the prehistoric period. The back consonants c, 3, x
> would no longer tolerate diphthongs of the usual OE type
> (accented front+unaccented back vowel) before them, and such diphthongs
> accordingly rejected their second elements when these consonants followed,
> either directly, or with an intervening r or l, so that ⟨ea⟩ (= æa), éo, io
> became respectively æ, ǽ, í. This process is termed smoothing. Very soon a
> further change took place: æ, produced by smoothing, became e before r or l
> plus back consonant, but remained directly before a back consonant, while ǽ,
> produced by smoothing, became é everywhere."  
> (Campbell §222, repo ll. 6659–6672)

The contrast set Campbell gives in §222 itself is verified at ll. 6674–6691:

> "VP the forms mæht might, merg marrow, feh money, were work, gesihð sight,
> birhtu' brightness, héh high, néh (< *néoh) near, betwih between,
> corresponding to W-S meaht, mearg, feoh, weorc, gesiehþ, bierhtu, héah,
> néah, betwioh."
> (Campbell §222, repo ll. 6685–6691)

So the canonical contrast pairs (Anglian | West Saxon), all verified in
Campbell §222:

| gloss | Anglian | West Saxon |
|---|---|---|
| might | mæht | meaht |
| marrow | merg | mearg |
| money/cattle | feh | feoh |
| work | were | weorc |
| sight | gesihð | gesiehþ |
| brightness | birhtu | bierhtu |
| high | héh | héah |
| near | néh | néah |
| between | betwih | betwioh |

Further canonical Anglian smoothing forms verified in Campbell §225 (repo
ll. 6768–6792): éac > æc > Merc., North. **éc** 'also'; *-béacn > **bécn**
'beacon'; *léac > **léc** 'leek'; *éagan > **égan** 'eyes'; *flége 'fly';
*léht- 'lumen'; *þégh 'thigh' (Cp.: ll. 6810–6814).

### Hogg vol. 1 (repo ll. 20836–20940)

Hogg presents smoothing as a quantitative variable from the Épinal–Erfurt
Glossaries through Corpus to the Vespasian Psalter. Repo ll. 20836–20868:

> "Anglian smoothing (a monophthongisation) and velar umlaut (a
> diphthongisation) have long been documented... The velar spirant plays a
> major role in the operation of these two competing sound changes; it
> triggers smoothing and inhibits velar umlaut."
> (Hogg, ll. 20836–20842)

Hogg's progress table (ll. 20856–20865; selected, percentages = % attestation
of smoothed variants):

```
                            Epinal  Erfurt  Corpus  VPs
                            ca700   ca750   ca800   ca825
Smoothing of /i:o/             +       +      +      +
Smoothing of /io/              +       +      +      +
Smoothing of /eo/              80      90     +      +
Smoothing of /æa/              60      +      +      +
Smoothing of /æ:a/             60      80     +      +
Smoothing of /e:o/             0        0     70     +
```

Two general tendencies are noted (ll. 20871–20875): "Short diphthongs were
smoothed before the long ones. Among the short diphthongs, a height
hierarchy is to be observed /io > eo > æa/."

### Ringe & Taylor §6.9.2 (repo ll. 17663–17760)

R/T explicitly reject the term "smoothing" in favour of "monophthongization"
(repo ll. 17677–17678 fn.):

> "In place of the traditional term 'smoothing', which is not used for any
> other sound change in any language, I have used the standard term
> 'monophthongization'."
> (R/T fn. 46, ll. 17677–17678)

Their formal statement (repo ll. 17671–17675):

> "éaK > æK > éK; éoK > éK; íoK > íK;
> eah > æh; eoh > eh; ioh > ih;
> earK > ærK > erK; eorK > erK;
> eolh > elh."
> (R/T §6.9.2, ll. 17671–17675; "K" = velar consonant)

R/T verify the canonical examples from PGmc/PWGmc preforms (ll. 17695–17760):

- `*auk` > WS éac, Merc./North. **éc** 'also'
- `*augon-` > WS éage, Merc. **ége**, North. **égo** 'eye'
- `*hauhaz` > WS héah, Merc./North. **héh** 'high'
- `*flauh` > WS fléah, Merc./North. **ge-fleh** 'fled'
- `*þauh` > WS þéah, Merc./North. **þeh** 'though'
- `*baukn` > WS béacn, Merc. **béc(e)n**, North. **bécon** 'sign'
- `*leuht` > WS léoht, Merc./North. **léht** 'light' (noun)
- `*næh-` > WS néah, Merc./North. **néh** 'near'
- `*þeuhg` > WS þéoh, early Merc. **þégh** 'thigh' (CorpGl 556)
- `*liuhtaz` > WS léoht, Merc./North. **liht** 'light(-weight)'
- `*bitwih` > WS betwéoh, Merc./North. **betwih** 'between'

R/T note an asymmetry (ll. 17769–17772): the raising `æ > é` operated only
on `æ < éa` (smoothing-output), **not** on `æ < *a` (i-umlaut output). Hence
WS, Merc., North. all keep `ǽht` 'possession', `tǽcnan`, `fǽcne` etc.

### Brunner §119 "Ebnung" (repo ll. 4745–4811)

Brunner states the rule (repo ll. 4776–4811):

> "§ 119. Vor c, 3, h stehen in den anglischen Mundarten für die aus germ.
> au, eu, iu entstandenen ea, eo, io und für die wegen 'Brechung' vor h
> (§ 86) zu erwartenden ea, eo, io, eo, io einfache Vokale, und zwar e
> für ea und eo jeder Herkunft (für ea in ganz alten Texten aber æ ...),
> i für io, æ für ea (bei i-Umlaut aber e ...), e für eo, i für io. Solche
> anglische Formen sind demnach: ... becen Zeichen, ec auch, leg Seil, ege
> Auge, heh hoch, fleh / fleg flog (entsprechend ws. beacen, eac, teag, eage,
> heah, fleah); ... sec krank, flege Fliege, flegan fliegen, legan lügen, þeh
> Schenkel, liht Licht ... lihtan leuchten, lixan leuchten, cicen ... gesæh
> sah, geðæht Gedanke, æhta acht, hlæhtor Lachen, nordh. tæhher Träne,
> sæhher Ähre (§ 228), mæht Macht, næht Nacht ..."
> (Brunner §119, repo ll. 4776–4801; OCR `3` = `g`, `Z`/`z`/`ZE` = `g`/`æ`)

Brunner Anm. 1 (ll. 4812–4824) traces the term: "Die Bezeichnung 'Ebnung'
für diese Erscheinung wurde als Übersetzung des von H. Sweet dafür
gebrauchten engl. 'smoothing' von K. Bülbring, Angl. Beibl. 10, 3, in die
deutsche grammatische Literatur eingeführt." He explicitly notes (Anm. 1)
that the consonants involved are velar, not palatal, so the older label
"Palatalumlaut" is "sachlich unrichtig".

### Geographical sub-distribution: Mercian vs. Northumbrian

- VP (Mercian) and Ru.¹ (Mercian): smoothing of éa "practically universal"
  (Campbell §225, ll. 6779–6780).
- Lindisfarne, Rit., Ru.² (Northumbrian): "éa is smoothed to é in
  practically all words except `ac` (Li., Rit., Ru.²) and `ðah` (Li., Rit.)
  beside `gc, déh`" (Campbell §225, ll. 6783–6785).
- Northumbrian additionally raises smoothed `æ` > `e` before final `-hs`
  (Campbell §224, ll. 6731–6735): "smoothing of ea before final -hs was
  frequently followed by a change of æ to e caused by the final consonant
  group, which was becoming palatalized. Hence BH has Sex- more frequently
  than Sax- in names ..."
- Northumbrian texts often show the further development `cnǽht` for `cneht`
  'servant' (Campbell §229 fn. 2, ll. 6847–6848): "Ru.² and the
  tenth-century North. texts have very frequently cnǽht servant for cneht
  (which Ru.¹ and Rit. have also). The cause of this development is
  unknown."

### Negative environments

- Smoothing applies only before `c, g, h` (with optional `r/l` between).
- Dental-cluster environments: not smoothed; the WS/Anglian distinction
  there is governed by breaking and back mutation, not smoothing.
- Smoothing does *not* operate when the velar was lost before back vowels:
  Campbell §230 (ll. 6873–6883): "in a number of forms, however, h before
  a consonant disappeared early, and a preceding diphthong was not
  affected: ... VP héanis highness, gored troop, néosian visit ..."
- Smoothing of long `é(:)o` lags behind smoothing of short `eo`: Hogg's
  table (ll. 20860, 20864) has `eo: 80/90` already in Épinal but `é:o:
  0/0/70` only catching up at Corpus.

---

## 2. Breaking environments: WS vs. Anglian

Breaking diphthongises front vowels before `l+C, r+C, h, hC` (Campbell
§§139–148; Hogg ll. 5060–5159). The dialects diverge in the following
specific environments:

### 2.1 `æ + lC`: WS breaks; Anglian retracts

Campbell §143 (repo ll. 4429–4444):

> "æ is retracted before l followed by a consonant in Angl. texts ... In
> Kt. and W-S, on the other hand, while a appears freely for Prim. OE æ in
> early texts, ea rapidly asserts itself as the prevailing spelling ...
> Examples in normal W-S spelling are eall all, healdan hold, healf half,
> sealfian anoint, wealh foreigner, weall wall; the corresponding Angl.
> forms are all, haldan, &c."
> (Campbell §143, ll. 4429–4445, 4467–4468)

Hogg ll. 20357–20359:

> "Fronted /ae/ was retracted to /a/ in general Anglian texts before [l + C]
> (not geminated [ll]), and in Northumbrian also before [r + C]."

Toon's Lord's Prayer table in Hogg (l. 20417):

```
2c 'old'      WS eald     North. ald     Merc. ald     Kt. eald
```

### 2.2 `æ + rC`: WS breaks; Northumbrian (only) retracts to `a`

Campbell §144 (repo ll. 4469–4473):

> "æ was broken, and appears as ea with very great regularity, before r
> followed by a consonant. Retraction to a is practically limited to North.,
> where it is especially common when a labial consonant (f, p, b, m, w)
> precedes the vowel or follows the r."
> (Campbell §144, ll. 4469–4471)

Northumbrian retraction examples (Campbell §144 fn. 1, ll. 4484–4498):
`warþ`, `barnum`, `arm` 'arm', `barm` 'bosom', `farr` 'bull', `harm`,
`naru` 'narrow', `parf`, `warþ`, `ward`. Mercian and (mainly) Ru.¹
preserve breaking: `bearn`, `heard`, `hearg`, `mearh`, `wearm`.

This produces the key triple distinction:

| gloss | WS | Mercian | Northumbrian |
|---|---|---|---|
| 'old' | eald | ald | ald |
| 'child' | bearn | bearn | barn |
| 'hard' | heard | heard | hard (often) |

### 2.3 `i + rC`: Anglian fails to break

Campbell §154.3 (repo ll. 4628–4638):

> "(3) In Angl. dialects the breaking of i regularly failed before r
> followed by a consonant if -i- stood in the next syllable. The occurrences
> are various forms and derivatives of smirwan smear, afirran remove,
> hirtan encourage in VP; ... in tenth-century North. and Ru.¹ ..."
> (Campbell §154.3, ll. 4628–4636)

Hogg discusses the same phenomenon at l. 5092: a palatal consonant
inhibited breaking ("nerian save" vs. "nearwe narrow"). Hogg explains
breaking conditioning in terms of velarised vs. palatalised liquids
(ll. 5085–5101).

### 2.4 `i, e + rC` with metathesised `r`: Anglian breaks; WS does not

Campbell §155 (repo ll. 4681–4684):

> "Metathesis of r (§ 459) usually took place too late for secondary r-groups
> to cause breaking, e.g. gers grass, berst he burst, berstan burst, þerscan
> thresh, ferst fresh. But in Angl., when the vowel is i, metathesis of r is
> early enough for breaking to occur, e.g. North. biorna burn, iorna run, VP
> beornan, eornan; but W-S birnan, irnan."
> (Campbell §155, ll. 4681–4686)

So: WS **birnan, irnan** vs. Anglian **biorna(n), iorna(n) / beornan,
eornan**.

### 2.5 Long `ǽ` and breaking before `h`

Campbell §151 (repo ll. 4581–4586): `ǽ < PGmc *ǽ` is "peculiar to W-S" and
breaks to `éa` before `h`: WS **néah** 'near'. In Anglian/Kentish the long
vowel is `é` (Campbell §152, ll. 4588–4592), not subject to retraction; its
breaking to `éo` before `h` is typically obscured by smoothing. Cf. R/T's
preform `*næh-` (l. 17736): pre-WS *nǽh > néah; pre-Anglian *néh > *néoh
> Merc./North. **néh** (after smoothing).

### 2.6 `ǽ + ht` with `i` in the next syllable: breaking fails in Anglian/Kentish

Campbell §154.4 (repo ll. 4676–4680):

> "(4) In Angl. and Kt., the breaking of ǽ (< Prim. Gmc. ǽ) did not take
> place before h when i stood in the next syllable; hence Prim. OE *néhist-
> appears as nést nearest, in most Angl. texts ... But in W-S in this
> position ǽ was broken to éa, which later became ie (§ 200), e.g. niehst."
> (Campbell §154.4, ll. 4676–4680)

So WS **niehst** vs. Anglian **nést**.

---

## 3. Back mutation / back umlaut (a/u-umlaut)

PGmc-stage front `i, e, æ` are diphthongised to `io, eo, ea` when a back
vowel stood in the following syllable.

### Campbell §205 (repo ll. 6144–6160) — the canonical statement

> "At the close of the prehistoric period of OE an extensive group of
> changes occurred, whereby the short front vowels, æ, e, i, were
> diphthongized to ea (= æa), eo, io, when a back vowel stood in the
> following syllable. In W-S these changes take place only when the
> consonant intervening between the vowel affected, and the back vowel which
> causes the change, is a labial or liquid (f, p, w, m, l, r). In Anglian
> they take place before all consonants except perhaps the back ones (c, g),
> which were about to cause the monophthongization of all diphthongs
> standing before them ... In Kentish they could take place before any
> consonant. Before geminates and consonant groups they are everywhere rare."
> (Campbell §205, ll. 6144–6159)

### Hogg vol. 1 (repo ll. 5678–5694) — WS restriction explicit

> "In West Saxon back mutation was even more restricted, for it occurred
> only if there was a single intervening consonant which was either a labial
> or a liquid ... Although o-mutation was regular, in West Saxon a-mutation
> occurred only if the preceding vowel was /i/ ... Typical examples are:
> *sifon > siofon 'seven', *hefon > heofon 'heaven', *lifað > leofað 'he
> lives', but a word such as fela 'many', since it had /e/ before /a/ rather
> than /o/, was unmutated."
> (Hogg, ll. 5678–5688)

### Ringe & Taylor §6.9.4 (repo ll. 18306–18467)

R/T (l. 18306):

> "By 'back umlaut' OE specialists mean the partial or complete velarization
> of a [front vowel before back vowel]..."

R/T confirm WS restriction to labial/liquid intervening consonant and the
much wider Anglian distribution; they also acknowledge the priority of
combinative back umlaut over normal back umlaut (ll. 18318–18327):

> "between normal back umlaut, in which i > io, e > eo, æ > ea, and
> 'combinative back umlaut' (in German, 'gesteigerter Velarumlaut') in which
> a preceding w and a following back umlaut environment cause i to become u
> and e to ... [become o]. ... [Combinative] back umlaut occurred
> significantly earlier than normal back umlaut, at least when the [vowel
> was] ..."
> (R/T §6.9.4, ll. 18318–18324)

R/T also note (l. 18340) that "back umlaut followed Anglian
mono[phthongization]". Examples in Anglian texts where WS lacks the umlaut
(repo ll. 18367+, Mercian Ps(A)).

### Campbell §210 — concrete dialect contrast

Campbell §210 (repo ll. 6319–6336): in WS u-umlaut occurs before labials
and liquids (`heofon, eofor, beofor, heorot`) but not generally before other
consonants; a-umlaut is mostly absent (`fela, helan, beran, nefa, sefa,
weras, wela`). In Anglian (l. 6337): "both u- and a-umlaut of e are general
before all consonants except c and g."

VP examples (Campbell §210, ll. 6354–6358): `ofergeotul` 'forgetful',
`feodur-` 'four', `weorud` 'troop', `weolure` 'lips', `eofor-` 'boar',
`weoruld` 'world', `heorut` 'hart', `heofen` 'heaven', `weolan` 'wealth',
`geofu` 'gift', `gebeodu` 'prayers', `weoras` 'men'. WS counterparts have
`-e-` in many of these (`weras`, `wela`, etc.).

### Combinative BM after `w`

Campbell §210.1 fn. 1 (repo ll. 6360–6366; verbatim):

> "The preceding w apparently helps combinative back umlaut or, if this
> failed, back umlaut to take place in this word, although the consonant
> group st would not normally permit it."
> (Campbell §210 fn. 1, ll. 6360–6362)

This is the source for `swustor` (lW-S, recorded), `swostor` (general WS),
and the Anglian variation `swester / swuster` (Ru.²: l. 6423–6426). See
DEV_NOTES §15 for the FST implications.

---

## 4. Retraction and a-restoration

a-restoration: Prim. OE `æ` reverts to `a` in open syllables when a back
vowel follows in the next syllable. Campbell §157 introduces this as "one
of the most obvious peculiarities of the OE phonological system... that æ
and a interchange" (ll. 4697–4700).

The WS/Anglian dimension surfaces in two places:

1. **Retraction before `lC`** (already covered in §2.1 above): Anglian and
   Northumbrian retract to `a`; WS breaks to `ea`. Hence Angl. `ald, all,
   haldan, fallan, halm, salt`; WS `eald, eall, healdan, feallan, healm,
   sealt` (Campbell §143, ll. 4445–4468; R/T ll. 12670–12674: "ald 'old',
   all 'all', fallan 'to fall', haldan 'to keep', halm 'straw', salt 'salt',
   etc. (with retraction rather than WS breaking, see 6.2.3) remained
   identical with the Northumbrian forms").
2. **Anglian unrounding `o > a`**: Campbell §156 (repo ll. 4688–4695):
   "for reasons not clear, Prim. Gmc. o is sometimes unrounded to a in
   Angl. dialects. This a is never subject to fronting and breaking before
   l or r followed by a consonant, e.g. past and pass. part. warhte,
   gewarht worked, VP, Cp., Mortain Casket; pret. walde would, nalde would
   not, VP, Ru², beside wolde ..." Campbell explicitly says these forms
   "occur sporadically elsewhere, not only in texts with an Angl. element
   ... but also in more purely W-S texts."

Of separate (but related) interest: Toon's overview in Hogg ll. 20345–20356
states that Mercian "exhibits the effects of a change which is an actual
fronting of /a/ to /a/ or /æ/" — i.e. this is the input to second fronting
(see §6 below), distinct from a-restoration proper.

---

## 5. Palatal diphthongisation (PD)

PD is a WS feature: after initial palatalised `ġ-, sċ-, ċ-`, front vowels
diphthongise.

### Campbell §170 ff., §253

Campbell, summary of dialect status (§253, repo ll. 7617+; verified at
ll. 7623, 7675):

> "palatals could develop and produce éa, gea. Second fronting is by..."
> (Campbell §253, l. 7623)

Campbell §258 (l. 7675): list of Mercian features explicitly includes
"Second fronting (mainly VP). **Palatal diphthongization of front vowels
absent.**" — i.e. PD is a WS, not an Anglian, feature.

Campbell §253 examples (ll. 7621–7623, and §170 ff.): WS `ġiefan, ġiest,
ġearu, sceal, sceaft, scieran, sċieppan` from earlier `*gefan, *gæst,
*gæru, *skæl, *skæft, *skeran, *skæpjan`.

### Ringe & Taylor §6.5.1 (repo ll. 12450–12541)

> "After initial velars and *sk had been palatalized, any following
> stressed non-high front vowel was diphthongized in WS; the outcomes were
> *æ > ea, *ǽ > éa, *e > ie, *é > íe."
> (R/T §6.5.1, ll. 12454–12456)

R/T's verified example pairs (l. 12462–12541) — WS vs. Merc./North./Kent.:

| PGmc/PWGmc | WS | Anglian / Kent. |
|---|---|---|
| `*geban-` | `ġiefan` | Merc. `for-ġeofan` (with BM); North. `ġeafa` |
| `*geldan-` | `ġieldan` | Merc. `geldan`; North. `gelda` |
| `*skal` | `sceal` | (Merc. via *scæl = scal in BM environments; cf. Ru. `scal`) |
| `*skattaz` | `sceatt` | — |
| `*skelduz` | `scield` | Merc. `sceld` |
| `*ja` | `ġéa` | — |
| `*jér-` | `ġéar` | Merc., North., Kent. **`gér`** |
| `*kasi` | early `*ċiese`, late `cyse` | Merc., Kent. **`cése`** |
| `*kabisi` | `ċiefes` | Merc. `cebis`; North. pl. `cefissa` |
| `*gastiz` | `ġiest` | North. `gest`; Merc. dat. pl. `gesthúsum` |
| `*skapjan-` | `scieppan` | Merc. `sceppend` |
| `*skeran-` | `scieran, scear, scéaron` | — |
| `*skaft-` | `sceaft` | — |
| `*skap` 'sheep' | `sċéap` | Merc., Kent. **`scép`** |
| `*katil-` | early `*ċietil`, late `cytel` | Anglian `cetel` |
| `*jiz` 'ye' | `ġie ~ ġé` | Merc. `ġé` |

R/T (ll. 12566–12574) note that Northumbrian shows "apparently a similar
change [PD] independently" but only in the 10th century: "Northumbrian
palatal diphthongization was a 10th-century change, historically
unconnected with the similar but much earlier change in WS" (ll.
12572–12574). Hence in standard Anglian texts (VP, Ru.¹) PD is absent.

### Hogg ll. 20396–20402

> "(7) West Saxon texts (and to some extent, Anglian and Kentish texts of
> the period of West Saxon hegemony) exhibit a further change. Under the
> influence of an initial palatal consonant [j, ʃ] — spelled <g> and <sc>,
> the mid and low front vowels /e:, e, æ:, æ/ were diphthongized to <ie>
> and <ea>. This process, common in Northumbrian texts for /æ/ after <sc>,
> is called palatal diphthongisation."
> (Hogg, ll. 20396–20402)

---

## 6. Second fronting (Mercian sub-dialect)

This is **not pan-Anglian**. It is restricted to a Mercian subdialect, most
clearly the language of the Vespasian Psalter (VP) gloss.

### Campbell §164–169

Campbell §164 (repo ll. 4811–4820):

> "The position whereby Prim. OE æ, when not subject to breaking or
> retraction by the influence of the following consonant or consonant-group,
> appears as æ or a in historical forms ... is modified in the dialect of
> VP. There æ became raised to e, and a became fronted to æ, so that, for
> example, the normal OE paradigm dæg, dagas, appears as deg, dægas. Other
> examples are bec back, feder father, efter after, hefde he had, segde he
> said ..."
> (Campbell §164, ll. 4811–4836)

Campbell §165 (l. 4847): "The second fronting does not take place before l."
Hence Anglian/Mercian `ald, haldan` are immune, and so is retracted `a`
before `lC`.

Campbell §168 (ll. 4885–4893):

> "Second fronting is not a general Merc. change, for it is practically
> absent in Ru.¹, and ME sources show that it was limited to a small part of
> the vast Midland area. In OE the change of æ to e, in addition to its
> practically universal appearance in VP, is fairly common in Ep. and Cp.,
> and very frequent in RG and St. Chad. The change of a to æ, on the other
> hand, apart from sporadic forms, is not to be traced outside VP except in
> the early glossaries (see § 207). Ru.¹, RG, and St. Chad all have dagas, &c."

So: VP shows both halves (`æ > e` and `a > æ`); Ep./Cp./RG/St. Chad show
only the first half robustly; Ru.¹ shows neither.

### Ringe & Taylor §6.5.2 (repo ll. 12601–12674)

R/T explicit (ll. 12601–12614):

> "Palatal diphthongization did not occur in Kentish and seems also to have
> been foreign to Mercian. But in a part of the Mercian-speaking area,
> including the dialect in which the glosses to the Vespasian Psalter were
> written (apparently the southwest), there occurred a second fronting of
> low vowels ... surviving stressed *æ > e; surviving stressed *a > *æ
> unless l followed immediately."

R/T's `*æ > e` table (ll. 12619–12636): WS `hwæt, fæt, wæter, fæder, bæc,
æfter, hæfde, hreþ, æsce, wæstm, dæg, mæg, sægde` ← → Merc. (VP) `hwet,
fet, weter, feder, bec, efter, hefde, hreð, esce, westem, deg, meg, segde`.

R/T's `*a > æ` table before velars (ll. 12643–12648): WS `cwacian, wracu,
dagas, magan` ← → Merc. `cwecian, wræcu, dægas, mægan`. With back umlaut
(ll. 12654–12668): WS `lappa, fatu, gatu, gladian, hafoc, swaþu, sparian`
← → Merc. **`leappa, featu, geatu, gleadian, heafuc, sweaþu, spearian`**.

R/T's exclusions (ll. 12670–12674): hwalas, ald, all, fallan, haldan, halm,
salt all unaffected (l blocks fronting; retracted `a` unaffected).

### Hogg vol. 1 (l. 20349–20352)

> "(b) In Mercian and Kentish influenced texts, we regularly find this
> /ae/ raised to /e/, spelled <e>. This latter process is usually called
> 'the second fronting', even though it involves a raising rather than
> fronting."
> (Hogg, ll. 20349–20352)

### Texts showing second fronting

- **Vespasian Psalter (VP)** — both halves, robustly
- **Royal Glosses (RG)** and **St. Chad** — first half (æ > e) frequent
- **Épinal–Erfurt and Corpus glossaries** — first half present
- **Ru.¹** — no robust second fronting (Campbell §168, l. 4886, 4893)
- ME continuations: dialect of *Ancrene Riwle* / Katherine Group
  (R/T l. 12686–12700; d'Ardenne 1936 cited)

---

## 7. i-mutation outcomes

For most front vowels, i-umlaut outcomes are uniform across dialects.
Differences emerge mainly with the diphthongs `ea, eo, io` and with `ǽ`:

### i-umlaut of `ea, éa`

- **WS / Kentish**: `ea > ie`, `éa > íe` (later WS y/i; Campbell §200 ff.).
- **Anglian (Mercian, Northumbrian)**: `ea > e`, `éa > é`.

Campbell §200 fn. (l. 5252):

> "In North., since the mutation of ea is e, it is not possible..."
> (Campbell §200, l. 5252)

R/T (l. 17774–17786): WS, Merc., North. all have **`ǽht`** 'possession'
and **`tǽcnan`**, **`fǽcne`**, because here the input is `*aiht-, *taikn-,
*faikn-` with i-umlaut applied to PGmc `*ai`, not via the diphthong route.
But the *productive* i-umlaut of ea/éa diverges: WS `ġesiehþ`, `niehst`,
`gehíeran`, `mǽġden ← *magdin > maġden ← *magdin`, contrast Anglian
`ġesið(VP), nést, ġehéran`.

Verified i-umlaut contrast pairs from Campbell §200 (ll. 5825–5827):

> "ciegan call, gieman care for, hieran hear, liefan allow, nied need;
> nW-S cégan, &c."
> (Campbell §200, ll. 5825–5827)

| gloss | WS | non-WS (Anglian/Kt.) |
|---|---|---|
| call | ciegan | cégan |
| care for | gieman | géman |
| hear | hieran | héran |
| allow | liefan | léfan |
| need | nied | néd |

### i-umlaut of `io, ío`

Campbell §201 (l. 5842):

> "io, ío: the i-umlaut of these sounds in W-S is ie, but in nW-S they were
> not changed."
> (Campbell §201, l. 5842)

WS `liehtan, biet, gesiene, onsien, ġestieran, undertheodan, getriewe,
ðiestru, friend, fíend`; corresponding Anglian/Kentish `lihtan, ġesíen,
onsíon, eldíodig, ðíostro, friond, fíond` (Campbell §201, ll. 5878–5887).

### i-umlaut of `éa < PD output`

Campbell §200(7) (ll. 5831–5832): "éa due to palatal influence is subject
to i-umlaut only in eW-S *ċiese, cheese, inferred from lW-S cyse." Hence
WS `*ciese > cyse`, Anglian (no PD input) `cése` (cf. R/T's `*kasi` series).

---

## 8. The WS digraph `ie` (later WS `y, i`) ~ Anglian `e`

This is essentially a corollary of §§5 and 7: WS `ie/íe` arises both from
PD (`ġiefan, sceaft`) and from i-umlaut of `ea, éa, io, ío` and of the
diphthong from PD (`ċiese`). Anglian lacks PD altogether and has plain
`e/i` for the i-umlaut of the relevant inputs.

Hogg's summary of the late-WS history (ll. 5715–5749): early WS `<ie>`
representing /iy/ merged with /i/ in early WS (`fird` ~ `fierd`,
`hiran` ~ `hieran`); in late WS `<ie>` appears as `<y>` except before
palatals where it surfaces as `<i>`. Hence late WS `fyrd, hyran` but
`miht` (mieht > miht). Anglian `fird, héran, miht` lack the `ie`/`y`
stage entirely.

| Source | WS (early / late) | Anglian |
|---|---|---|
| i-umlaut of ea (e.g. *gæste) | ġiest / *ġyst* (cf. R/T l. 12504) | gest |
| i-umlaut of éa (e.g. *hærjan > hieran) | hieran / hyran | héran |
| i-umlaut of ío (e.g. *liohtjan) | liehtan / lyhtan | lihtan |
| PD output, then i-umlaut (*kasi) | ċiese / cyse | cése |
| io+r (i-umlaut, broken) | hierde / hyrde | hirde / heorde |
| io+r unmutated | (lost to umlaut) | wyrs(a) [WS]; werst(um) [Kt.]; smirwan [Anglian, no umlaut] |

---

## 9. u-mutation vs. back mutation; dialect distribution

"Back mutation" = "back umlaut" = "velar umlaut" = umbrella term for
u-umlaut + a/o-umlaut (Campbell §205, ll. 6167–6172). The dialect
distributions are:

- **WS**: u-umlaut general before single labial/liquid (`heofon, eofor,
  beofor, heorot`); a-umlaut "generally absent" (`fela, helan, beran, nefa,
  weras, wela`; Campbell §210.1, l. 6332). Combinative back umlaut after
  `w` is the source of `woruld, swostor, swolop` (Campbell §210.1,
  ll. 6326–6328).
- **Anglian**: u- and a-umlaut "general before all consonants except c and
  g" (Campbell §210.2, l. 6337). Hogg's overview (ll. 20381–20389):

  > "[5] The short, front vowels [i, e, æ] were diphthongised to [io, eo,
  > æa], written <io, eo, ea>, when they were found in closed syllables
  > before a back vowel ... The change is most general in Anglian
  > (especially Mercian) varieties, but common in all late texts ... West
  > Saxon texts also show velar umlaut of /e/ before labials and liquids
  > and non-low back vowels (<heofon>), but the change is rare before other
  > consonants or before a low back vowel (<nefa>)."
  > (Hogg ll. 20381–20389)

- **Kentish**: "back umlaut is found before all consonants" (Campbell
  §210.3, l. 6414).
- **Velar consonants block**: in all dialects, c/g block back mutation,
  because smoothing was about to remove diphthongs there anyway (Campbell
  §205, l. 6154).

### Combinative back mutation (gesteigerter Velarumlaut)

R/T §6.9.4 (ll. 18318–18323): preceding `w` + back-vowel environment causes
`i > u` and `e > o`. R/T note: "occurred significantly earlier than normal
back umlaut." This is what converts `*werald-` > **woruld** (general OE),
`*swester-` > WS **swostor / swustor**.

`*sweostor` itself is recorded once (Oros. 126.6, Campbell §210.2 fn. 3,
l. 6426). VP lacks the word; Ru.² has `swester` (no BM) but also `swuster`
(combinative BM). North. (Li.) has `suoester, soester` — no BM.
(Cf. DEV_NOTES §15.)

---

## 10. Other minor but important differences — lexical doublets

Verified in the sources (citations in parentheses).

| gloss | WS | Anglian | source/cause | citation |
|---|---|---|---|---|
| 'old' | eald | ald | breaking vs. retraction before lC | Campbell §143, l. 4467; R/T l. 12670 |
| 'all' | eall | all | id. | Campbell §143, l. 4445; R/T l. 12670 |
| 'fall' | feallan | fallan | id. | R/T l. 12670–12671 |
| 'hold/keep' | healdan | haldan | id. | Campbell §143, l. 4468; R/T l. 12671 |
| 'shall' | sceal | (Merc.) scal / North. scal | retraction; absence of PD in Anglian | R/T l. 12485–12486 (`*skal > *scæl > scal` in Anglian; WS `sceal`) |
| 'shaft' | sceaft | (Anglian) scæft / scaft | absence of PD in Anglian | R/T l. 12519–12520 (`*skaft > *skæft > sceaft (WS)`) |
| 'shield' | scield | sceld (Merc.) | absence of PD | R/T l. 12491–12492 |
| 'sheep' | scéap | scép (Merc., Kent.) | absence of PD | R/T l. 12522–12523 |
| 'year' | géar | gér (Merc., North., Kent.) | absence of PD | R/T l. 12497–12498 |
| 'cheese' | ċiese / cyse | cése (Merc., Kent.) | PD + i-umlaut | R/T l. 12528–12529 |
| 'hawk' | hafoc | (Merc.) heafuc | second fronting + back umlaut | R/T l. 12664; cited at l. 11094 too |
| 'gate' | geat (sg.), gatu (pl.) | get / geatu (Merc.) | PD vs. SF + back umlaut | R/T l. 12581–12584 |
| 'might' (n.) | meaht | mæht / mæcti / North. mæcti | smoothing | Campbell §222, l. 6685; Brunner §119 l. 4796 |
| 'night' | neaht / niht | næht / neht | smoothing + i-umlaut alternation | Campbell §223, ll. 6715–6720 |
| 'high' | héah | héh | smoothing of éa | Campbell §222, §225, ll. 6685, 6776; R/T l. 17705 |
| 'eye' | éage | ége / égo | smoothing | R/T l. 17699–17700 |
| 'thigh' | þéoh | (early Merc.) þégh / þéh | smoothing | R/T l. 17747–17748 |
| 'light' (adj.) | léoht | liht / léht | smoothing | R/T l. 17757 |
| 'between' | betwéoh | betwih | smoothing | R/T l. 17760 |
| 'fly' (vb.) | fléogan | flégan | smoothing | R/T l. 17725 |
| 'sister' | swostor / swustor (lW-S) | (Merc. Ru²) swester / swuster; (North.) suoester | combinative BM after w (WS); largely absent Anglian | Campbell §210 fn. 1, ll. 6326–6328, fn. 3 ll. 6423–6426 |
| 'world' | woruld | weoruld / woruld | combinative vs. ordinary BM | Campbell §210, ll. 6326–6328 (WS), l. 6357 (VP `weoruld`) |
| 'guest' | ġiest | gest | absence of PD in Anglian | R/T l. 12504–12506 |
| 'give' | ġiefan | (Merc.) for-ġeofan; (North.) ġeafa | absence of PD; Merc. has BM in pres. | R/T l. 12462–12466 |
| 'six' | siex / six | sex | smoothing of eo before x; Brunner §119 l. 4801–4803 | Brunner §119 l. 4801–4803 |
| 'work' (n.) | weorc | were | smoothing | Campbell §222 l. 6686 |
| 'heaven' | heofon (with BM) | heofen / heafun (Merc., back umlaut of e/æ) | dialect distribution of BM | Campbell §210 ll. 6322, 6354 |

A few entries the user listed (`heafod` 'head' / `hafud`) deserve a note:
the WS form is `héafod`, not the back-mutated short-vowel form. R/T do
include `hafoc` 'hawk' / Merc. `heafuc` (l. 12664), which is the same
phenomenon (second fronting + BM in Mercian). The user's ⟨hafud⟩ suggests
the head-/hafud type was conflated with hawk/hafoc — only `hafoc/heafuc`
is verified in the in-repo sources I have searched, so I list that pair,
not `heafod/hafud`.

---

## 11. Dialect of the canonical OE literary texts

Verified ascriptions from Campbell's introduction (repo ll. 1404–1742, with
spot-checks):

| Text | Dialect | Source citation |
|---|---|---|
| Vespasian Psalter (VP) gloss | Mercian (with second fronting) | Campbell ll. 1545–1548 ("Vespasian Psalter and the Rushworth Gospels (Matthew; Mark...)"); ll. 1552 ("Mercian nature of the Vespasian Psalter gloss"); R/T l. 12605 ("the dialect in which the glosses to the Vespasian Psalter were written") |
| Lindisfarne Gospels (Li.) gloss | Northumbrian | Campbell l. 1429 ("the glosses on the Lindisfarne Gospels"), ll. 1740–1742 |
| Rushworth² (Mark from §6 onwards, Luke, John) | Northumbrian | Campbell l. 1429 ("Rushworth..."); ll. 1740–1742 |
| Rushworth¹ (Matthew + early Mark) | Mercian | Campbell ll. 1411–1412 ("two dialects in the Rushworth Gospels, decided that Ru. was probably Merc."), 1548 |
| Durham Ritual (Rit.) | Northumbrian | Campbell l. 1472 fn. 3 ("The glosses on the Lindisfarne Gospels and the Durham Ritual were written..."), ll. 1742 |
| Old English Bede (BH/OEB) | Mercian (with mixed transmission) | Campbell ll. 4446 (early Bede MSS) and citations ll. 6263 ("Beadu- in MS. Cott. Tib. C ii of BH"), ll. 6346 (BH Herut-) — corroborates Mercian core |
| Cædmon's Hymn (CH) | Northumbrian (early) | Campbell ll. 6755 ("CH"); also Brunner §119 Anm. 2 l. 4826 ("maecti Cædmon Hymn (Cambridge Ms.)") |
| Leiden Riddle (LR) | Northumbrian | Brunner §119 Anm. 2 l. 4826 ("heh, deh Leid. Rätsel"); Campbell ll. 6816 |
| Ruthwell Cross | Northumbrian | Brunner §119 Anm. 2 l. 4827 ("almëttis Ruthwell-Kreuz") |
| Bewcastle Cross/Franks Casket | Northumbrian | (FC = Franks Casket) Campbell §144 fn. 1 l. 4485 ("uarp warp, FC ... fegtap they fight"); l. 6817 |
| Épinal Glossary (Ep.) | Anglian (early; Mercian-tinged glossary tradition) | Hogg ll. 20856–20862 (treats EpGl as part of the Anglian smoothing/velar-umlaut sequence); Campbell §225 ll. 6768–6772 (preserves unsmoothed forms beside smoothed ones) |
| Erfurt Glossary (Erf.) | continental copy of an English (Anglian) original | Hogg ll. 20856–20862; Campbell §225 |
| Corpus Glossary (Cp.) | Mercian (Anglian) | Hogg ll. 20880–20892 ("Corpus we find only /æa/ unsmoothed..."; treats CorpGl as Mercian alongside VP); Campbell ll. 6772–6779 |
| Beowulf and other major poetic codices | conventionally treated as a "general OE poetic koiné" with Anglian substrate features | Campbell §207 l. 6271 ("Instances of back umlaut of æ are practically unknown in W-S texts but they are quite a feature of the W-S transcripts of OE poems: Beow. alone has beadu- heapu-, eafora, eafod, eatol, heafo, geheaderod, heafola"); Campbell ll. 6262–6263 (LV, BH have name-elements `Headu-`, `Beadu-` "due to the use of poetical forms, ultimately derived from the Mercian area") |

The standard textbook treatment of Beowulf's "poetic koiné" — i.e. that the
extant text is a late WS scribal copy of a poem with detectable Anglian
(largely Mercian) phonological features — is supported but not formally
labelled "koiné" by Campbell §207; the Anglian residue evidenced by
back-umlauted forms (`beadu-, heaþu-, eafora`, etc.) is exactly what makes
the poetic corpus diagnostically mixed.

The Lord's Prayer trio in Hogg (ll. 20444–20479) is reproduced with Toon's
numerical annotations (ll. 20481–20505) marking each dialectal feature
visible (general fronting, breaking before rC, velar umlaut, NWS retraction
before rC, Mercian second fronting, non-Anglian dev. of *a before nasals,
non-WS failure of contraction of /i:e/, Anglian dev. of *a before nasals,
WS retraction of /y/, WS `<ie>` written `<y>`, North. rounding of /e/ after
/w/, Anglian forms of personal pronouns).

---

## 12. Implications for the CAPR FST

(Brief, no citations — flag only.)

The CAPR FST currently produces forms that are **dialectally inconsistent**:
some outputs are WS-leaning, others are Anglian-leaning, even within the
same lexical entry set. Concretely:

- `*mizdō` → `meord` (broken `e+rC` to `eo+rC`) is the **non-WS** outcome
  (WS would predict `*méd` via a different chain; cf. notable_findings #11).
- Lexical pairs like `eald/ald`, `sceal/scal`, `sceaft/scæft`,
  `weorc/were`, `héah/héh`, `betwéoh/betwih`, `gást/gest`, `cése/ċiese`
  illustrate axes along which the FST's implicit dialect should be made
  explicit. If the FST is to produce one canonical output, the choice is
  effectively WS or Anglian, with the orthogonal toggle of PD on/off being
  the most visible single discriminator after smoothing.
- Smoothing is **not** currently applied: outputs like `héah, néah, féoh,
  léoht, betwéoh` would all reduce to Anglian forms `héh, néh, feh, léht,
  betwih` if a smoothing rule were toggled on for an Anglian-target
  variant.
- Second fronting is a sub-Mercian feature and probably never the right
  default; if Mercian (VP) outputs are desired, second fronting must be
  triggered after retraction but before back umlaut (R/T's chronology,
  l. 12733).
- Combinative back umlaut after `w` (`woruld, swostor, swustor`) is the
  source of attested WS forms and should not be confused with non-mutated
  Anglian `weorold / swester`. (DEV_NOTES §15.)
- The WS `ie/y` digraph is a late, narrowly diagnostic surface feature; if
  the FST targets late WS, `ie` outputs of i-umlaut and PD should be
  optionally rewritten `y` (with special handling before palatals, where
  the output is `i`).

These notes are observational; concrete rule-ordering proposals belong
elsewhere in the repo.

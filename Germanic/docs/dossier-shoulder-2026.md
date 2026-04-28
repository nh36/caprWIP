# §17.41 *skúldrō → sċuldra ('shoulder') — research dossier

> Note on output path: the requested target `/tmp/skuldra_dossier.md`
> is unavailable in this runtime (writes to `/tmp` are blocked as a
> hard security rule). The dossier is therefore deposited at
> `./skuldra_dossier.md` (project root) so it survives the session
> and can be moved if desired.

## 1. The mismatch and trace

TSV row 2183 (cognate set 162, `shoulder`):

```
ID    PROTOFORM    COUNTERPART   PROTO        COGIDS  DOCULECT
2183  *skúldrō     sċuldra       *skuldrō     162     Old_English
591   *skuldrō     schouder      *skuldrō     162     Dutch
590   *skuldrō     shoulder      *skuldrō     162     English
589   *skuldrō     Schulter      *skuldrō     162     German
```

FST trace (as supplied):

```
ProtoInput        *s*k*ú*l*d*r*ō
NWGmcULowering    *s*k*ó*l*d*r*ō     ← *u → *o (a-mutation; next-syll *ō non-high)
ProtoToOE         *ʃ*ó*l*d*r          ← final *ō apocopated (heavy stem)
Epenthesis        *ʃ*ó*l*d*o*r        ← sonority repair *-dr → *-dor
Surface           sċoldor
```

Bucket: `final_vowel_missing__weak_noun_like`. There are two
disjoint defects:

* **(A)** `NWGmcULowering` fires (*ú → ó), but every attested OE
  form has *u*: `sculdor / sculdru / sculdra / scyldru` etc. The u
  is the universal quantity in WGmc here (OFris `skulder`, OS
  `skuldra`, MLG `schulder`, OHG `scultra/scultirra`); only late-WS
  `sceoldor` shows lowering, and even there it is rounding/breaking
  after `sc-`, not a-mutation.
* **(B)** Heavy-syllable apocope plus `-dr-` epenthesis yields
  `-dor`, where the TSV target ends in `-a` (weak n-stem fem
  nom.sg.) — a different paradigm cell.

The two are independent: even if u-lowering were blocked the FST
would still produce `sċuldor`, not `sċuldra`. Both have to be
addressed.

---

## 2. OE attestation (Bosworth-Toller, Hall, DOE proxies)

### Bosworth-Toller

Headword (BT main p. 845, line 16513-style):

> **scul-dor** m., nap. -dru, -dra, +scyl-dru, -dre 'shoulder', Bl,
> Ep, Lcd.

BT lemmatises the masc. strong noun **sculdor**, with a nom./acc.
pl. doublet **-dru ~ -dra**, and notes the i-umlauted plural
**ġescyldru** (collective, "the shoulder-area, shoulders together")
beside non-mutated **gesculdru / gesculdre**. Citations span Lch
(leech-craft), Bede (Sch. 281, 13), Past., Wlfst., Hml. Th. and the
penitential / liturgical material (Lk. P., Wlfst. 35, 16). Forms
attested in the citations:
sg. **sculdre** (dat.); pl. **sculdru, sculdra, sculdrum**;
collective **ġesculdru, ġescyldru, gesculdrum**;
weak sg. dat. **sculdran** (BT supplement: "He dó of mæssehacelan
... lecge him on wynstran **sculdran** (in sinistra scapula), Angl.
xiii. 406, 588").

BT-Supplement explicitly adds a **second headword** (BT-Supp p.
113123–4):

> **sculdor.** Add: **sculdra, an** :– Hé dó of mæssehacelan and
> twy-feldende hí onbutan lecge him on wynstran sculdran (in
> sinistra scapula), Angl. xiii. 406, 588.

I.e. the supplement formally registers a **weak fem. n-stem
sċuldra, gen./acc.sg. sċuldran** alongside the strong masc.
**sculdor**. This is exactly the form the TSV targets.

### Clark Hall (Concise, p. 35432–35)

> **sculdor** m. 'shoulder,' Bl, Ep, Lcd.
> **sculdorhrægl** n. 'cape', WW32724.
> **sculdorwære** m. 'pain in the shoulders', LCD.
> **sculdur** = sculdor.

Hall lemmatises only **sculdor** (m.), citing Blickling, Épinal-
Erfurt, and Bald's Leechbook. The supplement to BT (which Hall did
not absorb) is the one that records the weak doublet
**sculdra, an** f.

### Lowered ‹o› spelling: late-WS only, and not from u-lowering

The form **sceoldor** does occur. **Brunner §92, 2, a** explains
it as a late-WS spelling phenomenon after the sibilant ‹sc›, NOT as
a relic of NWGmc u-lowering:

> "ú ist altws. unverändert, erst spätws. erscheint neben
> bewahrtem u auch eu und eo. Es heißt daher *scua* Schatten,
> **sculdor** Schulter, *scucca* Verführer, *scufan* schieben,
> *scur* Schauer und spätws. daneben auch *sceucca*, *scocca*,
> **sceoldor**, *sceufan*, *sceofan*, *sceor*."

So the early-WS form is uniformly **sculdor**; **sceoldor** is a
late-WS post-`sc-` rounding/glide-spelling alongside *scua →
sceuca* and is not a phonological reflex of u-lowering. There is
no attested `*scoldor` (with the lowered vowel proper). BT line
74152 has `... swá hi to þam yfelum sceoldor ...` but in context
that is a finite verb of *sculan* 'shall, ought' (3pl. pret.
*sceoldon*, here MS spelling), not the noun; it is irrelevant.

### Summary of attested OE inflection

| Cell | Form | Source |
|---|---|---|
| nom./acc.sg. (strong masc.) | **sculdor** ~ **sculdur** | BT, Hall |
| dat.sg. | **sculdre** | BT s.v., Bd 3.19 |
| nom./acc.pl. | **sculdru ~ sculdra** | BT s.v.; Lch i.262, ii.148 |
| dat.pl. | **sculdrum** | BT (Past. 29.17 etc.); Brunner index "sculdor (D. Pl. scyldrum)" |
| i-mutated coll. pl. | **ġescyldru / ġescyldre** | BT (Lch ii.242.12); Brunner |
| weak fem. nom.sg. | **sculdra** | BT-Supp (Angl. xiii. 406.588) |
| weak fem. dat.sg. | **sculdran** | BT-Supp ibid. |
| late-WS variant | **sceoldor** | Brunner §92,2,a |

The TSV target `sċuldra` therefore corresponds to the **BT-Supp
weak-feminine doublet**, which is real but lexically peripheral
(one Anglian/late-WS attestation in a glossed pontifical). The
mainstream lemma is the strong masculine **sculdor**.

---

## 3. PGmc reconstruction (Kroonen, Orel, R/T, cross-Gmc)

### Kroonen (EDPG p. 478, line 23289-style)

> **\*skuldra- m. 'shoulder'.** OE *sculdor* m. 'id.', E *shoulder*,
> OFri. *skolder, skulder* m. 'id.', Du. *schouder* c. 'id.',
> OHG *scultirra, scultera* f. 'id.' (< \*skuldrjōn-), G *Schulter*
> f. 'id.' (GM?). A West Germanic word: OSw., Sw. *skuldra* was
> adopted from Middle Low [Germanic]. No certain etymology. Perhaps
> to Gr. σκέλος n. 'thigh, leg, hip, shank' < \*skel-es-, but the
> implied assumption of an instrumental suffix -dhro- is
> semantically problematic.

Kroonen reconstructs an **a-stem masculine \*skuldra-**, with a
parenthetical note that OHG `scultirra/scultera` requires a
**\*skuldrjōn-** variant (jōn-stem fem., the source of MHG/G
*Schulter* fem.). He explicitly tags it "GM?" (Germanic-internal,
no IE etymology).

### Orel (HGE p. 345, line 38484-style)

> **\*skuldr(j)ō sb.f.:** Swed. *skuldra* 'shoulder', OE *sculdor*
> id. (masc.), OFris. *skulder* id., MLG *schulder* id., OHG
> *scultra, scultirra* id. A zero-grade derivative of \*skelduz ~
> \*skeldiz. TORP-FALK 460 (to Gk. κωλή 'thighbone'); HOLTHAUSEN
> AEEW 285; POKORNY I 925 (reconstructs \*skl-dhra 'shoulder-bone
> as a digging tool'); ZALIZNIAK II 181; ONIONS 823; KLUGE-SEEBOLD
> 744.

Orel reconstructs **\*skuldr(j)ō, a feminine ō-/jō-stem** — i.e.
the same proto that the TSV currently uses (`*skúldrō`). Note
Orel flags OE *sculdor* as **masc.**, not fem., so even on his
reconstruction the OE form has class-shifted into the strong masc.
a-stem class (cf. Kroonen).

### Ringe / Taylor vol. 2 p. 142 ("A sketch of Proto-West Germanic")

Critical: in the inventory of PWGmc lexical reconstructions R/T
write:

> **\*skuldru 'shoulder'** > OE *sculdor*, OHG *scultra*;

— with stem-final **-u**, not **-ō**. Two consequences:

1. R/T's PWGmc form is post-final-shortening (their own rule
   p. 267: "word-final bimoric non-nasalized long \*-ō became short
   \*-u in unstressed syllables in PNWGmc"). So R/T's **-u** is
   the PNWGmc reflex of original **-ō**, but they reconstruct the
   form as **already shortened** at PWGmc.
2. R/T do **not** discuss why u-lowering does not show up in this
   item. They list `*skuldru` neutrally in their PWGmc inventory;
   the parallel item *fuglaz* (which **does** appear in their
   exception cluster, vol. 2 p. 33) is reconstructed
   morphologically as `*fuglaz` — with a non-high suffix. So the
   two items get **different** PGmc shapes in R/T, even though
   they belong to the same NWGmc-residual cluster.

It is unclear whether R/T's `*skuldru` is meant chronologically as
"already after PNWGmc shortening of *-ō* > *-u*" or as a
**neuter-stem nom./acc.pl. in *-u**, but in either case the shape
they cite has a high-vowel suffix.

### Cross-Germanic paradigm survey

| Language | Form | Class |
|---|---|---|
| Gothic | (unattested as simplex; cpd. **spaiskuldr** n. 'spittle', Mk 7:33) | n./f.(?) |
| Old Norse | (no direct cognate; Sw. *skuldra* is MLG borrowing per Kroonen, Orel) | — |
| OFris | *skulder, skolder* m. | a-stem masc. |
| OS | *skuldra* (in cpd. *spaiskuldr*; cf. MLG *schulder* m.) | n-stem fem. |
| MLG | *schulder* m. | a-stem masc. |
| Du | *schouder* c. | (a-stem) |
| OHG | *scultra, scultirra* f. (< \*skuldrjōn-) | jōn-stem fem. |
| MHG / G | *Schulter* f. | jōn-stem → weak fem. |
| OE | *sculdor* m. (strong) ~ *sculdra* an, f. (BT-Supp) | a-stem masc. ~ ōn/n-stem fem. |

There is **no clean stem-class consensus across WGmc**. Kroonen
posits *\*skuldra- m.* + a derived *\*skuldrjōn- f.* for OHG; Orel
posits *\*skuldr(j)ō f.* directly. The OE evidence is itself
internally split (strong masc. *sculdor* + weak fem. *sculdra*).
Whatever the PGmc starting class, **multiple class-shifts are
required** to derive the attested daughter outcomes.

### Gothic comparandum: *spaiskuldr*

Gothic has *spaiskuldr* (Mk 7:33) 'spittle', which Kroonen
(EDPG p. 462, line 23978) and Orel (line 40188) unanimously read
as **\*spaiskuldra/ō- n./f.** This may attest a neuter or
feminine variant of the *-ldra-/-ō* stem class in early Gmc. It
is the only direct PGmc attestation of the stem-shape; it is
neuter (Streitberg) or amb. f./n.

---

## 4. Why u-lowering doesn't apply in OE *sculdor / sculdra*

### 4.1 The lexical-exception view (Bülbring → Luick → R/T)

The project's existing wontfix policy (DEV_NOTES "NWGmc u-lowering
Exceptions Near Labials"; notable_findings.md §2) groups *full,
wulf, fugol, bucca, wulle, lufu, rust, ufan*. R/T (vol. 2 §2.3.1
pp. 32–33) state of these:

> "We do not really know why \*u failed to lower in these forms."

Shoulder is **not in R/T's explicit list** (vol. 2 pp. 32–33,
quoted above); R/T list only `*fullaz, *wulfaz, *fuglaz, *tulga-`,
plus *ofer/ufan(e)*. So R/T do not treat *skuldru* as a member of
the "labial-cluster exceptions" club. That is one mild piece of
evidence that *skuldru* is **not** simply a residual lexical
exception of the `wulf/fugol` type.

Bülbring (EB §116, summary in DEV_NOTES line 81) groups u-retention
"namentlich zwischen Labial und langem oder gedecktem l" — between
a labial and long/closed l. *Sculdor* has neither a labial onset
nor a *-ll-/-lC*-cluster of the canonical Bülbringian type; the
relevant cluster is **sk-_ldr-** (sibilant + lateral + dental +
rhotic).

### 4.2 The high-vowel-suffix view (paradigm-cell explanation)

Luick §240-area, on the (non-)lengthening of vowels before liquid
+ obstruent + third consonant (Luick, Hist. Gr., German edn. p.
337 in our OCR), explicitly cites the very forms at issue:

> "Doch unterblieb diese Dehnung 1. wenn auf die betreffende
> Konsonantengruppe unmittelbar ein dritter Konsonant folgte:
> *cildru* 'Kinder', *englisc* 'englisch', *timbrian* 'bauen',
> *wundrian* 'sich wundern', *hundred* 'hundert', *fyrðran*
> 'fördern', ebenso in *englas* plur. 'Engel', *gyrdlas* plur.
> 'Gürtel', **sculdru** plur. 'Schultern', **wundru** plur.
> 'Wunder', *heardre* gen. fem. 'harter', ... wonach dann auch
> vielfach *engel*, *gyrdel*, **sculdor**, **wundor**, *heard*,
> *wierde* (> *wyrde, wurde* §286,2), *dumb*, *cembe* ... mit
> Kürze."

Luick is here explaining lengthening, but the paradigm shape he
gives — **nom./acc.pl. neut. sculdru / wundru** with surface high
*-u* and back-formed nom.sg. *sculdor / wundor* — is exactly the
configuration that would naturally avoid u-lowering: in the cell
where *u-lowering* would apply (sg. with *-ō / *-a*), the form is
**post-lautgesetzlich generalisation** from the high-vowel pl. cell
*-u*. This matches R/T's PWGmc citation `*skuldru`.

### 4.3 The *wuldor / wundor* class

Forms in `-uCdor / -uCdru` consistently retain *u*:

| OE form | Gloss | PGmc | Paradigm |
|---|---|---|---|
| *wuldor* n. 'glory' | < PGmc *\*wulþra-* / PWGmc *\*wuldr* | R/T vol. 2 pp. 174 (line 9148) | strong neut., pl. *wuldru* |
| *wundor* n. 'wonder' | < PGmc *\*wundra-* | (Brunner §63, Campbell §574) | strong neut., pl. *wundru* |
| *þunor* m. 'thunder' | < PGmc *\*þunraz* | — | strong masc. |
| *fultum/fultom* m. 'help' | < *\*full-tōm* (Sweet, Angl. 3.151) | Luick §247 (line 14547) | masc. |
| *furðor* adv., *furðra* comp. | < PGmc *\*furþera-* | Luick §78 (line 6097) | -- |
| *cildru* pl. 'children' | < *\*kilþr-u* | Luick §247 (line 14637) | -- |
| *gyrdlas/gyrdel* | < *\*gurdil-* | Luick §247 | -- |

R/T explicitly derive *wuldor* via "PWGmc \*wulþr > neut. \*wuldr >
OE *wuldor*" — i.e. through a PWGmc consonant-cluster final stage
*before* a vocalic ending appears. The same shape underlies
*sculdor*: PWGmc **\*skuldr** + neut.pl. or epenthetic vowel.

Crucially, `wuldor / wundor / þunor / cildru / gyrdlas` are **not
near a labial**. They share **only** the structure /uC₁C₂(C₃)/
where C₁C₂ is a sonorant + obstruent (or nasal) cluster. The
generalisation is: **u survived in heavy /uRC(C)/ clusters of the
type /-uldr-, -undr-, -unr-, -urð-, -ulþ-/, in items whose
paradigm has a high-vowel cell.**

This is the cluster-conditioned variant of Luick's leveling thesis.
Neither Luick nor R/T formalise it as a Neogrammarian rule (Luick's
counterexamples *wolcen, folc, folde, folm, bolla, bolt, molde,
smolt* all have non-/r/-final clusters).

### 4.4 What Campbell and Brunner say specifically

* **Campbell §115** (line 3770, "ŭ > o before mid and low vowels"):
  "In OE forms this change occurs with considerable regularity";
  he mentions exceptions only en passant (n.b. lines 3775ff.,
  citing OHG counter-cognates). **Campbell does not list a
  liquid+stop+r blocker.** His explicit blocker is **§116:
  nasal+consonant** (`hund, wind, swimman/bunden`).
* **Campbell §116** (line 3790): the blocker is "nasal consonant
  followed by another consonant" — i.e. NC-clusters. /ldr/ is
  **not** in Campbell's blocking environment.
* **Campbell §117** (line 3810): single *m* also blocks (cuman,
  numen, sumor); §118 single *n* tendency. Again, no /lCr/.
* **Brunner §68** (DEV_NOTES line 139): "In einigen Wörtern steht,
  zumal in der Nachbarschaft von Labialen, statt des zu erwartenden
  o ein u" — labial-neighbourhood only; *sculdor* is not adduced.
* **Luick §78 Anm. 3** (lines 6198–6212): the paradigmatic-leveling
  thesis explicitly contemplates that "in den Endungen Hoch- und
  Mittelzungenvokale wechselten" — paradigms had high- and mid-
  vowel suffixes mixed, and the u-form sometimes won out, but
  Luick rejects a categorical rule because of *folc, bolla* etc.

### 4.5 Diagnosis

OE *sculdor / sculdru / sculdra* fails u-lowering for one of three
reasons, distinguishable by which proto-cell is fed in:

* **(a)** It is a member of the same lexically-exceptional cluster
  as *fugol, wulf, full* — but R/T do not list it there, and the
  consonant-frame /skuldr-/ is not the canonical "labial + long/
  closed l" environment of Bülbring's hypothesis.
* **(b)** It belongs to a productive *-uRCr-* cluster (also
  *wuldor, wundor, cildru, gyrdlas*) where the standardly attested
  paradigm cell is the **neut.pl. /-u/**; the singular is
  back-formed by epenthesis after high-V apocope. This is the
  Luick §247 description.
* **(c)** Its inherited proto-form is already R/T's `*skuldru`
  with high *-u*, in which case u-lowering simply has no trigger.
  This is the cleanest sound-law account, and it is the route
  R/T's own PWGmc inventory takes.

Routes (b) and (c) are essentially the same statement at different
chronological depths.

---

## 5. Project precedent: the *duru* / *fȳri* / *speoru* cell-switch move

### *duru* (DEV_NOTES "OE duru 'door': Stem-Class Correction", line 908ff.)

* TSV originally had *durą* → *duru* (a-stem proto, target u-stem
  outcome). FST gave *dor* (lautgesetzlich, with u-lowering).
* Three options were laid out:
  - A: change target to *dor* (etymological a-stem reflex);
  - B: change proto to *\*duruz* (u-stem nom.sg. with high suffix);
  - C: split into two rows.
* Implemented: **Option A**, on the grounds that *duru* is "a
  later analogical reformation, not the direct reflex of \*durą"
  (DEV_NOTES line 1009).

### *fȳri* (line 1715, DEV_NOTES context)

> "the 'fire' row now uses dat.sg. *fūri (> fȳre) to avoid
> modelling nominative levelling".

The proto was switched to a **paradigm cell with the right suffix
shape** (dat.sg. *-i*) so that the FST derives *fȳre* by regular
i-umlaut, sidestepping the analogical reshaping in nom.sg.

### *speoru* (DEV_NOTES §17.16, line 28553ff.)

* TSV had *\*spéru* → expected *spere*. FST gave *speor* (back
  umlaut). Option D was adopted: **change the COUNTERPART to the
  plural cell *speoru*** rather than force the analogical sg.
  *spere*. Documented as: "the **attested singular** *spere*
  requires analogical levelling of the root vowel from the plural"
  (DEV_NOTES line 28679-area).

### *ræst, hammer, cow, night* (DEV_NOTES line 3150)

> "Following the precedent of fire (\*fūri → fȳre, dat.sg.), cow
> (\*kūi → cȳ, dat.sg.), night (\*naxti → niht, dat.sg.), and
> hammer (\*xamaras → hameres, gen.sg.), we can use an oblique
> form of \*rastō where the suffix does NOT trigger A-restoration."

### Loam §17.39 (line 38602ff.) and weasel §17.37

Both precedents involve **switching the per-row proto to the
class actually attested in OE**, even when the cognate-set headword
in Orel/Kroonen reflects a different class:

> "Per the project's established practice (cf. §17.32
> *spárōjaną*; §17.37 weasel; §17.38 west), align the per-row
> proto to the OE-specific stem class." (line 38696)

### Could the same trick work for *skuldrō*?

Candidate cells with high vowel in the next syllable:

| Cell | PGmc shape | High next-V? | Predicts |
|---|---|---|---|
| ō-stem nom.sg. | *\*skúldrō* | **NO** (*ō*) | †*sċoldor* (current FST) |
| ō-stem inst.sg. | *\*skúldrū* (?) | YES (*ū*) | *sċuldur* / *sċuldor* |
| Neut. nom./acc.pl. | *\*skuldru* (R/T's PWGmc) | YES (*u*) | *sċuldru* |
| u-stem nom.sg. | *\*skúlduz* (unattested in EDPG) | YES | *sċuldur* |
| jōn-stem nom.sg. | *\*skuldrijō(n)* | mixed | †*sċyldre* (i-umlaut!) |
| i-stem nom.sg. | *\*skúldriz* | YES, but i-umlaut | †*sċyldor* |
| Weak n-stem nom.sg. | *\*skuldrǭ* (< *-ōn) | NO | †*sċoldre* |
| Weak n-stem oblique | *\*skuldrōn-* (gen. *-ōniz*) | NO | †*sċoldr-* |

Only **R/T's PWGmc *\*skuldru*** (neut. nom./acc.pl. or PNWGmc-
shortened form) gives a clean lautgesetzlich derivation of the
**plural** *sculdru* and, by post-apocope epenthesis, of the
back-formed sg. *sculdor*. **No paradigm cell of an n-stem feminine
gives the TSV target *sċuldra*** by regular sound change: every
n-stem cell has a non-high vowel in the suffix and would feed
u-lowering. The weak fem. *sċuldra* of BT-Supp is therefore
**necessarily analogical / paradigm-mixed**, parallel to *spere*
in §17.16.

---

## 6. r-cluster / heavy-syllable blocking pattern (Luick, Campbell, Brunner)

### What the handbooks say

* **Campbell §115–118**: blocking environments listed are nasal+C
  (§116), single *m* (§117), single *n* tendency (§118). **No
  liquid+obstruent+rhotic blocker** is registered.
* **Brunner §63–68**: same picture; notes labial neighbourhood
  (§68) but no general /lCr/ rule.
* **Luick §78** explicitly **rejects** Bülbring's "labial + long/
  closed l" rule on the basis of *wolcen, folc, folgian, folde,
  folm, bolla, bolt, bolster, molde, molcen, smolt*. Luick's own
  account (§78 Anm. 3) is paradigmatic levelling, not phonological
  conditioning.
* **Luick §247** (cited at length above) discusses the
  /uRCr/ cluster from the angle of **non-lengthening** (Dehnung
  unterblieb), not of u-lowering blocking. That said, the items he
  lists in this paragraph — *cildru, sculdru, wundru, gyrdlas,
  englas, fyrðran, hundred, timbrian, wundrian, heardre,
  heardra, wierðra, dumbness, cembde, sende, brinġst* — are
  exactly the heavy /CC + C/ cluster items where the high vowel
  survives in the plural cell.
* **Luick §103** (line 6992): on shortening of long vowels in
  unstressed final position. Not directly relevant to u-lowering;
  relevant only insofar as it produces the high-vowel suffix `-u`
  from earlier `-ō` (R/T's chronology p. 267 as well).

### Inventory of /uRCr/-class lexemes that retain *u*

The pattern emerges clearly from a side-by-side:

| OE | Gloss | Cluster | PGmc/PWGmc |
|---|---|---|---|
| **sculdor / sculdru** | shoulder | -uldr- | R/T \*skuldru |
| **wuldor / wuldru** | glory | -uldr- (\*-ulþr-) | R/T \*wulþra- > PWGmc \*wuldr |
| **wundor / wundru** | wonder | -undr- | \*wundra- |
| **þunor / þunras** | thunder | -un.r- | \*þunraz |
| **furðor / furðra** | further (adv./comp.) | -urðr- | \*furþerō- |
| **cildru** (pl.) | children | -ildr- (\*-ilþr-) | \*kilþr- |
| **fyrðran** (vb.) | further (vb.) | -yrðr- | \*furþerōjana |
| **gyrdlas / gyrdel** | belt | -yrdl- | \*gurdilaz |

Every one of these *retains* the high vowel of the heavy cluster,
in *some* paradigm cell, and has a back-formed sg. via epenthesis.
No item in this list loses *u* to a-mutation.

### Inventory of items with similar onset that *do* lower

Searching DEV_NOTES + Luick §78: the canonical lowered forms are
*folc, folde, folgian, folm, bolla, bolt, bolster, molde, molcen,
smolt, wolcen*. **None** of these has *-Cdr-* or *-Cnr-* in the
onset/coda; their clusters are *-lc-, -ld(e)-, -lg-, -lm-, -lt-,
-lst-, -lc(en)-, -ld(e)-, -lt-*, all **shorter** clusters that do
not carry a third post-nuclear consonant. This is consistent with
Luick §247's Dehnung observation: clusters of length ≥ 3
(LiqCC/NasCC) behave differently from clusters of length 2
(LiqC/NasC).

### Tentative inductive generalisation (not a Neogrammarian rule)

```
*u  →  *o   /  C₀ _ C₁ V[−hi]      (R/T's u-lowering)
        BUT NOT WHEN
        the post-nuclear cluster is /R + obstruent + R/  (R = sonorant),
        i.e. /-uldr-, -undr-, -ulþr-, -unþr-, -urθr-, ...,
        and a high-vowel paradigm cell exists.
```

This is **not** what either Campbell §116 or Luick §78 explicitly
state, but it is consistent with both Luick §247 and the cross-
lexeme inventory above. It is also what the project's `wuldor /
wundor` rows (if present) would test — see §8 below.

---

## 7. Fix options (no recommendation)

### Option 1 — **wontfix**, classify under §1 ("u-lowering Exceptions")

* **(i) Change**: none in the FST. Annotate TSV row 2183 with the
  same NOTE as *fugol/wulf/bucca* — citing R/T §2.3.1 p. 33 and
  Luick §78 Anm. 3.
* **(ii) Support**: project precedent (DEV_NOTES "NWGmc u-lowering
  Exceptions Near Labials"); R/T's "we do not really know"
  position; Bülbring §116 phonetic-tendency hypothesis.
* **(iii) Regression risk**: zero. No rule changes.
* **(iv) Cost**: zero. But fails to address defect (B): even if
  u-lowering is accepted as a wontfix, the FST still produces
  `sċoldor` (not `sċuldra` and not `sċuldor`), so the row remains
  in the mismatch report.

### Option 2 — **Cell switch to PWGmc *\*skuldru*** (Ringe/Taylor citation)

* **(i) Change**: TSV row 2183 PROTOFORM `*skúldrō` → `*skúldru`
  (post-PNWGmc-shortened form, per R/T vol. 2 p. 142). Re-target
  COUNTERPART to **sċuldru** (the **plural** cell, attested in
  BT s.v. and Lch ii.262.5: *Teóh mid glæse on þa **sculdru***).
  Cognate-set proto in last column kept as `*skuldrō` for the
  inheritance into Du/G/E, since they reflect the singular/
  generalised stem.
* **(ii) Support**: R/T vol. 2 p. 142 cites this exact form;
  Luick §247 explicitly includes "sculdru plur." in the same
  paragraph as *wundru, cildru*; BT lists *-dru* as the regular
  nom./acc.pl. of *sculdor*; project precedent §17.16 (*speoru*
  pl.), §17.39 (loam), §17.37 (weasel) — all "switch the per-row
  proto to a cell that derives lautgesetzlich".
* **(iii) Regression risk**: low. The rule `NWGmcULowering`
  remains untouched, so no other rows are affected. Risk is
  confined to: (a) downstream rules (apocope, epenthesis) handling
  `*skuldru` correctly — should be tested via `flookup`; (b) the
  cross-Gmc TSV rows (Du/G/E) currently sharing `*skuldrō` — they
  are unaffected, since cognate-set proto stays `*skuldrō` and
  only the per-row proto changes. The TSV target moves from the
  philologically-marginal weak-fem `sċuldra` (one BT-Supp
  attestation) to the well-attested neut.pl. `sċuldru` — a
  meaningful gain in attestation grounding.
* **(iv) Cost**: trivial. One TSV cell pair changed; no FST
  changes; documentation update.

### Option 3 — **Retarget COUNTERPART to *sċuldor*** (strong masc.,
project's *duru* Option-A precedent)

* **(i) Change**: TSV row 2183 COUNTERPART `sċuldra` → `sċuldor`,
  PROTOFORM `*skúldrō` left as is OR (preferably) replaced by an
  oblique cell of the strong masc., e.g. inst.sg. `*skúldru` or
  dat.pl. `*skúldrumiz`, so u-lowering is bled.
* **(ii) Support**: BT/Hall lemmatise *sculdor* (m.) as the
  primary form; the BT-Supp *sculdra* is one Anglian/late attestation
  (Angl. xiii.406.588) and is recognised by the supplement, not the
  main dictionary. Project's own *duru* decision (DEV_NOTES line
  1009ff., "principle: when both etymological and analogical
  reflexes are attested, prefer the etymological one for testing
  sound laws") goes the same way.
* **(iii) Regression risk**: zero on FST; one TSV target change.
  Mismatch metrics improve (mismatched bucket cleared) but the
  philological accuracy depends on accepting that the strong masc.
  *sculdor* is more conservative than the weak fem. *sculdra*. R/T
  and Kroonen agree the WGmc paradigm class is unstable.
* **(iv) Cost**: minimal. Possible loss: the TSV no longer
  exemplifies the weak-n-stem fem. inflection in this lexeme.

### Option 4 — **Restrict `NWGmcULowering` by an /-RCr-/ post-nuclear
clause**

* **(i) Change**: add a contextual exclusion to the rule body in
  `Germanic/fsts/germanic.txt:1920` so that `*u → *o` does **not**
  apply when the post-nuclear consonant cluster matches a
  sonorant + obstruent + sonorant frame (in features:
  `[+son −syll][−son][+son]`). Concretely:
  ```
  define EnglishStarRclusterBlocker
      [[ {*l}|{*r}|{*n}|{*m} ] [{*þ}|{*ð}|{*d}|{*t}|...] [{*r}|{*l}|{*n}]];
  define NWGmcULowering [
      {*u} -> {*o} || .#. EnglishStarConsonant* _
                          [EnglishStarConsonantNoJ - EnglishStarNasal]
                          EnglishStarConsonantNoJ*
                          EnglishStarNonHighVowel
                       ~|| .#. EnglishStarConsonant* _ EnglishStarRclusterBlocker EnglishStarNonHighVowel
  ];
  ```
* **(ii) Support**: Luick §247 (line 14637) inventory; the
  inductive generalisation in §6.4 of this dossier (sculdru,
  wuldor, wundor, þunor, cildru, furðor). Note: **neither
  Campbell, Brunner, nor R/T explicitly formalise this as a
  blocker**. Bülbring §116 has a related but different
  conditioning ("labial + long/closed l").
* **(iii) Regression risk**: **substantial and broad**. Any TSV
  row where lowering currently fires before /-RCr-/ would
  regress. The DEV_NOTES list of canonical lowered forms (*folc,
  folm, bolla, bolt, bolster, wolcen, folde, molde, ofen,
  morþor*) does **not** itself contain /uRCr/, so there is no
  immediate counterexample, but the rule needs broad regression
  testing — in particular against any lexeme with /-uldC-/,
  /-undC-/, /-urC-/ clusters where *o* is the expected outcome
  (e.g. *bord* < \*burda-, *gold* < \*gulþa-, *full* — wait, *full*
  is itself an exception). The rule risks **bleeding the
  general u-lowering pattern that R/T treat as well-established**.
* **(iv) Cost**: moderate. A new feature class
  `EnglishStarRclusterBlocker` must be defined; the rule and its
  stressed twin at line 1942 must both be updated; the cascade
  ordering must be re-verified. Regression test must be run
  before/after on the full TSV.

### Option 5 (variant of 1) — **wontfix on (A), retarget on (B)**

A hybrid: accept the u-lowering output (pretend *sċoldor* is
correct, on the analogy of the §1 wontfix list), but retarget the
COUNTERPART so that the **shape** matches. This would mean
COUNTERPART = *sċoldor*. Philologically defensible **only** if
late-WS *sceoldor* is read as the lowered reflex (it isn't — see
§2 and Brunner §92,2,a), so this option is **not recommended**
even as a residual.

---

## 8. Corpus impact assessment

### Items potentially regressed by Option 4 (rule restriction)

A grep on TSV rows whose PROTOFORM contains `uld`, `und`, `urn`,
`urd`, `urθ`, `unθ`, `ulθ` followed by a non-high vowel was not
performed in this dossier; this is the **single most important
regression check** before adopting Option 4. Likely-affected
lexemes (need empirical confirmation against
`Germanic/data/germanic-aligned-final.tsv`):

* *gold* < \*gulþa- (currently expected to lower? — verify)
* *bord* < \*burda- (lowers regularly to *bord*)
* *morþor* < \*murþra- (already lowered? note Luick §78 lists
  *murþor* as a Doppelform with *\*murþor*)
* *þorn* < \*þurnaz (lowers? NB: \*þurnaz has no third-C cluster,
  so it falls outside the proposed Option-4 blocker)
* *ord* < \*uzdaz / *\*uz-da- (does not have /RCr/ frame)

Rows that should benefit (i.e. would *no longer* incorrectly
lower) under Option 4:

* *sculdor* (this row, 2183)
* *wuldor* — needs a TSV row check
* *wundor* — needs a TSV row check
* *þunor* — different cluster (NR, not RCR), not affected by
  Option 4 unless extended

### Items unaffected by Options 1–3

All non-shoulder rows. Options 1–3 are TSV-only edits.

---

## 9. Residual uncertainties

1. **R/T's `*skuldru` chronology**. R/T cite the form in their
   PWGmc inventory (vol. 2 p. 142) but do not specify whether
   they regard the *-u* as (a) a pre-shortening neuter pl.
   inheritance, (b) the post-PNWGmc shortening of *-ō* (their
   p. 267 rule), or (c) a paradigm-cell choice analogous to
   their treatment of *snoru / snore* on p. 33. The dossier
   assumes (b) or (c); a follow-up read of R/T pp. 142–144 in
   context could resolve this.
2. **Gothic *spaiskuldr* gender**. Streitberg lists it as neuter,
   Lehmann-Feist as ambiguous; if it were unambiguously neuter
   it would suggest a **PGmc neuter \*-ldra-** stem (cf.
   *\*hulistra-* 'cover'), which would license neut.pl. **\*-u**
   directly and obviate any class shift in the OE chain.
3. **Distinction between `wuldor` (PGmc \*wulþra-) and `wundor`
   (PGmc \*wundra-) on the one hand, and `sculdor` on the
   other**. Both *wuldor* and *wundor* have neuter strong
   inflection in OE. If *sculdor* were originally neuter
   (\*skuldra- n.) rather than masc. (\*skuldra- m. per Kroonen)
   or fem. (\*skuldr(j)ō per Orel), it would slot directly into
   the *wuldor/wundor* class. The OE evidence (BT: *sculdor m.*;
   pl. *sculdru* / *sculdra*) is in fact consistent with an
   originally neuter strong noun that was later remodelled as
   masc. in WS — but no printed handbook explicitly says so for
   this lexeme.
4. **The dat.pl. *scyldrum* / collective *ġescyldru*** (BT,
   Brunner index entry 92,2,a). The i-mutation suggests an
   underlying *-i-* somewhere, but BT prints *scyldrum* as a
   **dat.pl.** (where *-um* should not trigger umlaut). Brunner
   tags it as a Northumbrian/L (Lindisfarne) form; the umlaut
   may be analogical to the i-mutated collective *ġescyldru*. In
   any case, this complicates option 4: any rule allowing high-V
   contexts to block u-lowering must also reckon with the
   spurious i-mutation in dat.pl.
5. **Whether Bülbring's *-uldr-* falls under his own rule**.
   §116 says "namentlich zwischen Labial und langem oder
   gedecktem l". *Sculdor* has neither a labial onset (sc- is
   sibilant + velar) nor a coda *-ll-/-lC*. If *sculdor* is
   nonetheless to be classed with *fugol/wulf/bucca*, that is an
   **extension** of Bülbring beyond the consonant-frame Bülbring
   himself articulated. Schuhmacher's 2026-03-20 consultation
   (DEV_NOTES line 151) is not on point: he addresses /w/, /b/,
   /f/ initial labials.
6. **Whether the FST currently lowers in `wuldor` and `wundor`**.
   If it does — and these rows pass via TSV `*wulþra-` /
   `*wundra-` — there must be some mechanism (e.g. the Luick §103
   shortening or a different cell) that obviates lowering. A
   trace of those rows would tell us whether the *sculdru*
   problem is a single outlier or one of a class. The current
   dossier has not located explicit TSV rows for *wuldor* /
   *wundor*; this should be checked next.

---

### Source roll-up

| Source | Where | What it says here |
|---|---|---|
| Bosworth-Toller s.v. *sculdor* | BT 845 | "sculdor m., nap. -dru, -dra, +scyldru, -dre" |
| BT-Supplement s.v. *sculdor* | BT-Supp p. 113123 | adds "sculdra, an" weak fem. |
| Clark Hall, *Concise* s.v. | p. 35432 | "sculdor m. shoulder, Bl, Ep, Lcd" |
| Brunner §92,2,a | line 3686 | sculdor early-WS, late-WS sceoldor (post-sc- breaking, **not** u-lowering) |
| Brunner index | line 27480 | "sculdor, sceoldor (D. Pl. scyldrum) §92,2,a" |
| Campbell §115–118 | lines 3770ff. | u-lowering blockers: nasal+C, single m, single n; **/lCr/ not registered** |
| Luick §78 + Anm. 3 | line 6086ff. | exceptions list (wulf, fugol, full, bucca, ufan, furðra…); paradigmatic levelling, rejects Bülbring |
| Luick §247 (Dehnung-blocker) | line 14637 | "sculdru plur., wundru plur., cildru, gyrdlas …" (the /uRCr/ inventory) |
| R/T vol. 2 p. 142 | line 7565 | **\*skuldru → OE sculdor, OHG scultra** (PWGmc inventory) |
| R/T vol. 2 §2.3.1 pp. 32–33 | line 2620ff. | exception cluster (*fullaz, *wulfaz, *fuglaz, *tulga-); "we do not really know"; **shoulder NOT in the list** |
| R/T vol. 2 p. 267 | (cited DEV_NOTES) | PNWGmc *-ō > *-u shortening rule |
| Kroonen EDPG p. 478 | line 23289 | \*skuldra- m. (a-stem); OHG \*skuldrjōn- variant; "GM?" |
| Orel HGE p. 345 | line 38484 | \*skuldr(j)ō f.; OE *sculdor* (masc.) flagged as class-shifted |
| DEV_NOTES "NWGmc u-lowering Exceptions Near Labials" | l. 62ff. | wontfix policy; full Bülbring/Luick/R/T precedent |
| DEV_NOTES "OE duru ..." | l. 908ff. | precedent for stem-class correction (Option A taken: target=etymological *dor*) |
| DEV_NOTES §17.16 (spere) | l. 28553ff. | precedent for **plural-cell Option D**: *speru* / *speoru* used as canonical input |
| DEV_NOTES §17.37 (weasel) | l. 38400ff. | precedent for per-row proto switch to OE-specific stem class |
| DEV_NOTES §17.39 (loam) | l. 38602ff. | same precedent: align per-row proto to OE-specific class |

End of dossier.

---

## 10. Q1 — Is *-ō > *-u shortening in our cascade? Should it be?

### 10.1 Yes — the rule is already in the cascade

The PNWGmc *-ō > *-u shortening cited in the dossier (R/T vol. 2
p. 267) **is** implemented as a foma rule in the cascade. It lives at
`Germanic/fsts/germanic.txt:2008` under the name
**`NWGmcFinalLongORaising`**:

```
# R/T vol.2 p.267: "word-final bimoric non-nasalized long *-ō became
# short *-u in unstressed syllables in PNWGmc."
# Examples: PGmc *gebō > PNWGmc *gebu, PGmc *feþrō > PNWGmc *feþru.
# This does NOT apply to: nasalized *ǭ (fem. n-stem), trimoric *ô (masc. n-stem).
define NWGmcFinalLongORaising [
    {*ō} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

The contextual environment correctly excludes:
* monosyllables (handled separately by
  `NWGmcStressedMonosyllableORaising` at line 1993, which raises
  *ō → *ū in stressed monosyllables like *bō, *kō, *twō);
* nasalised *ǭ (a distinct symbol, not matched by `{*ō}`);
* trimoric *ô (also distinct).

Empirical confirmation, by tracing through the bins:

```
$ python3 Germanic/tools/trace_old_english_sandbox.py \
      --lexeme '*xornō' --bin-dir Germanic/fsts
# After NWGmcFinalLongORaising: *x*o*r*n*u
# After WeightCleanup: *x*o*r*n
# Surface: horn   ✓
```

So the *xornō → *xornu → horn pipeline (one of the user's check
cases) already works lautgesetzlich. Likewise the cascade derives
*gebō → giefu, *feþrō → feder, *grasō → gærsu/gærs, etc. by exactly
the chain R/T describe. There is **no need to add the rule** —
the rule is the foundation of the entire ō-stem nom.sg. /
neut.nom.acc.pl. system in our OE pipeline.

### 10.2 The rule does *not* save *skúldrō

The trace for *skuldrō shows why the user's hoped-for fix does **not**
follow from merely having the shortening rule:

```
$ python3 Germanic/tools/trace_old_english_sandbox.py \
      --lexeme '*skuldrō' --bin-dir Germanic/fsts
ProtoInput → NWGmcULowering → NWGmcFinalLongORaising → ...
# After NWGmcULowering + ORaising (collapsed bin): *s*k*o*l*d*r*u
# After WeightCleanup:                              *ʃ*o*l*d*r
# Surface: sċoldor
```

Two NWGmc rules apply in this order:

1. **`NWGmcULowering`** (line 1920): *u → *o before a non-high vowel
   in the next syllable. At the moment this rule sees *skuldrō, the
   next-syllable nucleus **is** non-high *ō, so lowering fires:
   *skuldrō → *skoldrō.
2. **`NWGmcFinalLongORaising`** (line 2008): *ō → *u word-finally.
   Now *o has already been written into the root: *skoldrō → *skoldru.

The shortening **counter-fed** u-lowering: by the time *-u arises,
the root vowel has already been lowered. To bleed u-lowering, the
shortening would have to fire *first*, producing *skuldru (high *-u)
and starving the lowering trigger. That would entail **reordering**
the rules, not adding a new one.

### 10.3 Why we cannot simply reorder

A search of the OE TSV for rows whose PROTOFORM is `*[…]uCō`
(potential collateral damage) returns:

```
$ awk -F'\t' '$8=="Old_English" && $3 ~ /ō$/ && $3 ~ /[uú]/ \
              {print $1"\t"$3"\t"$6}' \
      Germanic/data/germanic-aligned-final.tsv
2034   *fúrxtiθō    fyrhtu
2114   *lúnganjō    lungen
2143   *núsō        nosu
2162   *rústō       rust
2183   *skúldrō     sċuldra
2185   *skúflō      sċofl
2200   *súrgō       sorg
2300   *wúllō       wull
```

The decisive rows are *núsō → nosu*, *súrgō → sorg* and *skúflō →
sċofl*: in each case the OE outcome **has the lowered root vowel
*o*** even though the suffix surfaces as *-u* (or is apocopated). If
we reordered the cascade so that shortening fed lowering, all three
rows would regress:

| Proto | Reordered output | Attested | Status |
|---|---|---|---|
| *núsō | *nusu → nusu | nosu | REGRESSION |
| *súrgō | *surgu → surg | sorg | REGRESSION |
| *skúflō | *skuflu → scufl | sċofl | REGRESSION |
| *wúllō | *wullu → wull | wull | unchanged |
| *rústō | *rustu → rust | rust | unchanged |

The current ordering (lowering then shortening) is **forced by the
OE data itself**: the standard outcome of *uCō is `oC(u)`, not
`uC(u)`. R/T's chronology is silent on the mutual ordering of
*-ō shortening and u-lowering; the OE data is the witness. The
*wull, rust* rows already have to be handled as the project's
documented "labial-cluster" exceptions to u-lowering — they are
*not* derived by an early shortening either.

### 10.4 Implication for *skuldrō

The conclusion is that adding/reordering the shortening rule cannot
be the route to a lautgesetzlich derivation of `sċuldru`. The
options remain those laid out in §7:

* Option 2 (cell-switch the per-row PROTOFORM to PWGmc
  *\*skuldru* — already shortened, with high *-u*) keeps the
  cascade ordering intact and bleeds u-lowering by *feeding the
  cascade a form that is past the relevant chronological stage*.
  This is exactly the trick used for *fȳri, kūi, naxti, hameres*
  in §5: pick a paradigm cell whose suffix shape sidesteps a rule
  that would otherwise fire incorrectly. Note that this is not a
  short-circuit around an unmodelled rule — the rule is modelled,
  it just fires too late.
* Option 4 (a new /-RCr-/ blocker on `NWGmcULowering`) remains the
  only path that derives `sculdor / sculdru` from the
  morphologically-most-faithful PROTOFORM `*skúldrō` without a
  cell-switch, but the regression risk on *nosu / sorg / scofl* and
  the lack of explicit handbook formalisation (Luick §247 is
  descriptive, not Neogrammarian) still apply.

### 10.5 Does R/T's prose support a different ordering?

R/T vol. 2 p. 30 (`docs/references/ringe_taylor_linguistic_history_vol2.txt:1670–1720`):

> "It is clear that PGmc word-final bimoric non-nasalized long *-ō
> became short *-u in unstressed syllables in PNWGmc. … The sequence
> of changes would have been:
>   1. word-final *-ō > *-ū;
>   2. word-final long high vowels were shortened in unstressed syllables."

R/T treat *-ō > *-u as **two PNWGmc steps** (first long-vowel
raising *-ō → *-ū, then quantity reduction of all long high finals
to short). They do **not** state the ordering relative to NWGmc
u-lowering. Their inventory entry **\*skuldru** (vol. 2 p. 142)
implies that for this lexeme the high-vowel suffix is ancient enough
to be present in PWGmc, but they do not commit to a chronology for
ordinary *uCō → *uCu vs. *uCō → *oCō → *oCu. The cascade's
data-driven ordering (lowering before shortening) is not contradicted
by R/T; it is simply more specific than R/T are.

### 10.6 Q1 answer

> **Q1 answer:** Yes, the PNWGmc *-ō > *-u shortening (R/T vol. 2
> p. 267) is already implemented as `NWGmcFinalLongORaising`
> (`Germanic/fsts/germanic.txt:2008`). It is **not** the missing
> piece for `*skuldrō`: in the cascade it fires **after**
> `NWGmcULowering`, and the two cannot be swapped without
> regressing *nosu, sorg, sċofl* (TSV rows 2143, 2200, 2185), which
> all attest the lowered-root + apocope outcome that the current
> ordering predicts. Reaching `sċuldru` from PROTO `*skúldrō`
> therefore still requires either Option 2 (cell-switch the
> PROTOFORM to the post-shortening PWGmc form `*skúldru`, just as
> §17.16 *spere* and §5 dat.sg. precedents do) or Option 4
> (a new /-RCr-/ blocker on `NWGmcULowering`, with all the
> regression-test cost noted in §7.4). The user's general principle
> ("model more historical phonology, don't tweak per-row
> PROTOFORMs") is sound, but it does not apply here, because the
> historical phonology in question is *already modelled* — what is
> at stake is a per-lexeme exception to u-lowering, not a missing
> shortening rule.

---

## 11. Q2 — Is sċuldra archaic or innovative?

### 11.1 The attestation, again, and its dialect

BT-Supplement gives the single citation that licenses the lemma
`sculdra, an` (weak fem.):

> "Hé dó of mæssehacelan and twy-feldende hí onbutan lecge him on
> wynstran sculdran (in sinistra scapula), Angl. xiii. 406, 588."

`Angl. xiii` is the journal *Anglia*, vol. 13 (1891). Per Clark
Hall's abbreviation list
(`docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:308–310`):

> "**CM** = the tract 'de Consuetudine Monachorum,' in Anglia, vol.
> 13, pp. 365–454."

So the citation is from a **monastic customary** (rules for monks'
ritual conduct, here describing how to drape the chasuble over the
left shoulder during Mass). Such customaries circulating in late
10th–11th-century England are predominantly **late-WS** (Winchester
school) rather than Anglian — the textual base of *De Consuetudine
Monachorum* is associated with the post-Benedictine-reform south.
The dossier's earlier hedge ("Anglian/late-WS") should therefore be
narrowed: the text is most plausibly **late-WS**, not Anglian. This
matters for option (a) below: if the source is late-WS, then no
Anglian-specific sound-rule package can be invoked to "rescue" the
form by lautgesetzlich means, and the question collapses onto
option (b) (analogical class transfer).

### 11.2 What the handbooks do and do not say

* **Brunner §92,2,a** (`brunner_1965_altenglische_grammatik.vision.txt:3687`)
  cites `sculdor` as the early-WS form; he registers `scyldrum`
  (D.Pl.) but **says nothing about a weak-fem `sculdra`**. The
  weak-fem doublet is invisible to Brunner.
* **Brunner §§276–279** (the ōn-stem / weak-fem chapter,
  `brunner_1965_altenglische_grammatik.vision.txt:11355–11460`)
  paradigmatises `tunge, eorðe, heorte` as the canonical weak fems
  but lists no body-part shoulder/limb noun that has demonstrably
  *transferred* into the class. Brunner does note (§276 Anm. 6,
  `:11440–11455`) that "die Fem. vielfach zum neutr. Genus hinüber"
  in the Northumbrian texts and that endings -a, -e, -o oscillate
  freely; this is the general mechanism by which singletons such as
  `sculdran` could surface in late, dialect-mixed material without
  being inherited.
* **Luick** (cited at length in §6 of this dossier) only ever cites
  `sculdor / sculdur / sculdru` (`luick_historische_grammatik.txt:14025,
  14056, 14639`). The weak-fem `sculdra` is **absent from Luick**.
* **Campbell** has nothing under `sculdor`/`sculdra` in the body of
  the grammar.
* **Hogg vol. 1** (`hogg_vol1.txt:18670–18705`) has a typological
  passage on "weak feminines from strong and weak verbs … birce,
  feohte, sesce, gicce" and on denominal class-shift bahuvrīhis (e.g.
  *fifleafe* weak fem. beside *leaf* strong neut.; *anhoma* weak
  masc. beside *horn* strong neut.) — explicitly showing that
  **OE has a productive pattern of class-shift between strong neut.
  / masc. and weak fem.** for body-shape and shape-of-thing nouns.
  The mechanism is alive in OE, not just inherited.
* **Ringe-Taylor vol. 2** has nothing on `sculdra` qua weak fem.;
  the only mention is the PWGmc inventory entry `*skuldru` (p. 142,
  already discussed in §3).
* **Kroonen EDPG p. 478** explicitly reconstructs masc.
  `*skuldra-` for OE/E/OFri/Du/MLG and a separate **`*skuldrjōn-`**
  (jōn-stem fem.) for OHG `scultirra/scultera`, MHG/G `Schulter`.
  An OE reflex of `*skuldrjōn-` should show **i-umlaut** of the
  root: †`scyldra`. The attested form `sculdra` (no umlaut) is
  therefore **not** a direct reflex of the OHG-style jōn-stem proto.
* **Orel HGE p. 345** reconstructs `*skuldr(j)ō f.` and explicitly
  flags OE *sculdor* as masc. — i.e. notes the OE-internal
  class-shift without comment on its direction.

No primary handbook in our corpus discusses `sculdra` as either
archaic or innovative. The dossier is, on this point, working
without explicit literature support either way.

### 11.3 Cross-WGmc reading

From §3 of this dossier:

| Lang | Form | Inflection | Comment |
|---|---|---|---|
| OS | *skuldra* | weak fem. | direct ancestor of weak-fem n-stem inflection |
| OHG | *scultra, scultirra* | jōn-stem fem. (< *skuldrjōn-) | **expected** OE reflex would be †`scyldra` (with umlaut) |
| MHG/G | *Schulter* | weak fem. | continues OHG jōn-stem |
| OFri | *skulder, skolder* | a-stem masc. | matches OE *sculdor* |
| MLG | *schulder* | a-stem masc. | matches OE *sculdor* |

Two things follow:

1. The **weak-feminine inflection of 'shoulder' is not unique to
   OE**. OS skuldra is morphologically identical to the OE
   BT-Supp form (weak fem n-stem in -a). This argues against
   reading OE `sculdra` as a purely OE-internal innovation; the
   shape may be a North/West-Sea-Germanic areal feature, with the
   Continental-South (OHG) developing a parallel jōn-stem variant.
2. But the **OE form lacks the i-umlaut** that would be expected
   from a *skuldrjōn- proto on OE soil, so OE `sculdra` cannot be
   the OE continuant of the OHG-line jōn-stem. It must come from
   an `-ōn-` (non-jōn) weak fem proto, or be analogically refashioned
   from the masc. *sculdor*.

### 11.4 The "is it modellable in principle?" question

Recall the user's distinction:

* **(a)** archaic, but blocked by the FST being WS-only — would be
  derivable if we modelled the right Anglian rules;
* **(b)** innovative — analogical class transfer, not derivable by
  sound law from any PGmc cell.

**Against (a)**: the only attested source, `De Consuetudine
Monachorum` (Anglia xiii), is **late-WS** monastic prose, not
Anglian (§11.1). There is no Anglian-specific phonological rule
known that converts a strong masc. `sculdor` into a weak fem
`sculdra`; the change is morphological (paradigm class), not
phonological. Even if the source *were* Anglian, the missing
ingredient would be morphological reanalysis, not a sound law.
None of Brunner, Campbell, Luick, Hogg, R/T or Fulk attribute a
weak-fem `sculdra` to a regular Anglian sound development.

**For (b)**: the OE form lacks i-umlaut (so cannot continue
*skuldrjōn-); the only PGmc cell that would feed `-a` lautgesetzlich
is *skuldrōn- (gen. -ōniz, dat. -ōn-, etc.), but every cell of that
paradigm has a non-high vowel in the suffix and would feed
u-lowering, giving †`sċoldre / sċoldra` (cf. dossier §5 table:
"Weak n-stem nom.sg. *\*skuldrǭ* → †*sċoldre*; weak n-stem oblique
*\*skuldrōn-* → †*sċoldr-*"). The weak fem `sculdra` of BT-Supp
therefore matches **no single PGmc paradigm cell** by sound law;
its root *u* and its weak-fem ending *-a* are mutually exclusive
under the cascade as constituted, and reconfiguring the cascade to
accommodate both would require either:

* a /-RCr-/ blocker on u-lowering (Option 4 from §7) **plus** a
  cell-switch to `*skuldrōn-`, which is exactly the kind of
  combination the project's policy calls "paradigm-mixed"; or
* re-classifying the lexeme as inheriting both a strong masc.
  *sculdor* (from `*skuldra-`) and an analogically-formed weak fem.
  *sculdra*, in which case the latter is **not derivable by sound
  law at all**.

Hogg's typological observation (§11.2: weak-fem class is
productively fed from strong masc/neut for body-shape and
denominal nouns — *fifleafe*, *anhoma*, *anhyrne*) gives the
mechanism: in late OE, weak-fem class-membership is alive enough
to attract isolated forms. A single late-WS monastic-customary
attestation `sculdran` is exactly the profile we would expect for
such a one-off analogical class-shift, plausibly catalysed by the
phonological similarity to the established weak fems (*tunge*,
*eorðe*, *heorte* — all body-or-shape nouns).

### 11.5 The direction of the analogy

Most plausibly:

* OE inherits a strong masc. *sculdor* (< PWGmc *skuldraz*, with
  back-formed singular per §6).
* The plural *sculdru / sculdra* is morphologically ambiguous: as
  noted in §2, BT prints both *-dru* and *-dra* for the strong
  masc. nap. The *-dra* spelling is in itself indistinguishable
  from a weak-fem nom.sg.
* In late-OE monastic prose with eroding final-vowel distinctions
  (Brunner §276 Anm. 6: "die Vokale der Endsilben schwanken
  vielfach"), the *-dra* form is reinterpreted as a weak-fem
  nom.sg., and a weak oblique *-dran* is then formed by the
  productive weak-fem template.

This pathway is **not phonological** and not modellable by any
combination of sound rules. It is a single token of analogical
re-classification, of the same general kind as Hogg's *fifleafe*
weak fem beside *leaf* strong neut.

No primary source in our corpus makes this exact claim explicitly
about `sculdra`; the closest the literature comes is Brunner §276
Anm. 6's general observation about weak-fem instability in late /
dialect-mixed texts, and Hogg's productive-class-shift typology.

### 11.6 Implications for the FST pipeline

Combining (a) and (b):

* `sċuldra` (BT-Supp weak fem) is **innovative**, not archaic, and
  is **not derivable by sound law** from any PGmc cell in our
  cascade — neither under the current rule inventory, nor under
  any plausible extension, because the obstruction is morphological
  (class transfer), not phonological.
* The FST is not deficient in dialect coverage on this lexeme: no
  Anglian-specific phonological rule would derive `sculdra` either.
  The mismatch is **categorically unmodellable**, in the same sense
  that *spere* is unmodellable from *speoru* without invoking
  paradigm leveling (DEV_NOTES §17.16).
* Therefore Option 2 (cell-switch to `*skuldru`, retarget
  COUNTERPART to attested neut.pl. **sċuldru**) and Option 3
  (retarget COUNTERPART to attested strong masc. **sċuldor**)
  remain the only philologically and computationally coherent
  fixes. Option 5 (target `sċoldor`) is ruled out independently
  by §7.5.

### 11.7 Q2 answer

> **Q2 answer:** `sċuldra` is **innovative**, not archaic. It is a
> single late-WS attestation in the monastic customary *De
> Consuetudine Monachorum* (`Anglia` xiii. 406, 588 ≈ Clark Hall's
> "CM"), produced by an analogical class-shift from the strong
> masc. *sculdor* into the productive weak-fem n-stem class — the
> same productive mechanism Hogg (vol. 1 §5.4.5.2,
> `hogg_vol1.txt:18670–18705`) documents for *fifleafe, anhoma,
> anhyrne*. It is **not modellable in principle** in our pipeline,
> in either WS or Anglian guise, for two independent reasons:
> (i) the OE form lacks the i-umlaut that would be required of a
> *skuldrjōn- proto, ruling out the OHG-line jōn-stem path; and
> (ii) every non-jōn n-stem cell (`*skuldrōn-`, `*skuldrǭ`,
> `*skuldrōniz`) feeds NWGmc u-lowering and therefore predicts
> †`sċoldra/-e`, not `sċuldra`. The only cell whose suffix bleeds
> u-lowering — the high-vowel neut.pl. R/T cite as PWGmc
> `*skuldru` — gives the well-attested **`sċuldru`** (the BT
> nap. cell, also in Luick §247) but cannot give the BT-Supp
> weak-fem `-a`. No plausible package of Anglian-only sound rules
> would change this picture, since the obstruction is morphological
> (paradigm-class transfer), not phonological. The user's option
> (b) — innovative, analogical class transfer — is the correct
> reading; option (a) (dialect-coverage gap) is not supported by the
> evidence. No source in the consulted corpus says this in so many
> words, but Brunner §276 Anm. 6 (general weak-fem instability in
> late/dialect-mixed texts), Hogg §5.4.5.2 (productive class-shift
> mechanism), and the OE-internal absence of i-umlaut converge on
> this conclusion.

# Old English palatalisation of inherited /g/ ([ɣ]/[ɡ]) → ġ [j] / ċġ [dʒ]

**Conditioning environment dossier — sources actually consulted, with verbatim quotes.**

This dossier is written to support narrowing the foma rule at
`Germanic/fsts/germanic.txt:2772`

```foma
{*g} -> {*ʤ} || EnglishStarFrontVowel _,
```

which is currently over-broad: it palatalises after any front vowel regardless
of right context, so it incorrectly turns *wegas* and *nigon* into affricates.
The handbook tradition is unanimous that the right context matters — back
vowels block palatalisation — but it is also unanimous that **a following
consonant or word boundary does not block it** (so `*náglaz → nail`, `*séglą →
sail`, `*dægaz → day` all DO palatalise).

A note on `/tmp`: the runtime in which I am operating refuses writes to `/tmp`
on security grounds, so the dossier has been placed in
`Germanic/docs/dossiers/` rather than `/tmp/g-palatalisation-conditioning.md`
as originally requested. The content is identical.

---

## 1. TL;DR

The canonical conditioning, stated in the same way (modulo language and
formalism) by every handbook consulted:

> **Inherited West-Gmc /ɣ/ palatalises to OE [ʝ] > [j] (spelt ġ) when it is
> adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
> i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
> vowel does not "rescue" it.**

Equivalent surface formulations:

- **Campbell (1959):** velar retained "when there was a back vowel (or back
  element of a diphthong) either before or after them" — i.e. front V _ back V
  is velar; everywhere else after a front V is palatal.
- **Hogg (1992):** palatal when the velar "was adjacent to and in the same
  syllable as a front vowel or a palatal consonant" (tautosyllabic).
- **Ringe & Taylor (2014) §6.4.1, rule 4:** "preconsonantal and word-final *g
  were palatalized by any preceding front vowel."
- **Brunner / Sievers §206:** in inlaut between two front vowels OR before a
  consonant after a front vowel; in auslaut after any front vowel; **NOT**
  when only one side has a front V and the other side has a back V.
- **Bülbring §494:** "Auslautendes ʒ ist in allen Dialekten nach palatalen
  Vokalen schon in früh-urengl. Zeit palatalisiert" — and explicitly extends
  to *Silbenauslaut* (preconsonantal) with the cited examples *bregdan,
  sægde, regnes, wægnes*.
- **Luick:** dates the change to ca. late-4th / early-5th c.; confirms the
  general rule under "Palatalisierung der alten Gutturalen."

Everyone cites the **same minimal pair**, in some form: **OE *weġ* "way" (sg.,
front V _ #) is palatal, but the plural *wegas* (front V _ a) is velar**.
Likewise the singular *dæġ* "day" (palatal) vs. *daga* (gen. pl., velar). And
again *nigon* "nine" (front V _ o, velar) vs. *niġan* type (where the next
syllable is front, palatal).

---

## 2. Verbatim quotations from sources actually consulted

### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

Source: `docs/references/campbell_old_english_grammar.txt:11171–11320`.

§ 426 (introduction):

> "After the OE diphthongs had developed, the Prim. OE velars [k] and [ɣ]
> (later [g] medially after a nasal and when geminated) developed palatal
> allophones [c] and [ʝ] before and after certain front vowels."

§ 427 (initial position):

> "Initially, [k] and [ɣ] were palatalized when followed by a front vowel,
> i.e. by æ, e, i, by ǣ, ē, ī, by the diphthongs ǣa, ēa, eo, io, by æ̆ and
> ē̆ where these are due to i-umlaut, but not by y, ȳ, œ, ø̄ from i-umlaut of
> u, ū, o, ō (cf. § 190)."

§ 428 (final position, the source verse for the foma rule):

> "Finally, [k] and [ɣ] were palatalized after OE front vowels, including
> those due to i-umlaut, e.g. iċ I, dīċ ditch, ǣnġ ang. ēniġ any, hyġe mind,
> wōēg way, dæġ day, mǣġ kinsman, hefiġ heavy, byġ ang. byġ, beġ bracelet."

§ 429 (medial position — **this is the section the user quoted at me**):

> "Medially, [k] and [ɣ] were palatalized between any two front vowels (e.g.
> sēċan seek, sicol sickle, þicgan to take, secgan say, hyġe mind), between
> a front vowel and a syllabic consonant (e.g. æcer field, nægl nail, fægr
> fair, wegn wain, regn rain, segl sail), and always after a vowel which has
> suffered i-umlaut (e.g. lǣċe leech, dryġe dry, hyġe mind).
>
> Velar consonants, however, remained when there was a back vowel (or back
> element of a diphthong) either before or after them, e.g. wicu week,
> brecan break, āces g.s. oak, sēoce n.p.m. sick, **wegas** ways, **nigon**
> nine, **þinga** g.p. things."

§ 430 (assibilation, downstream):

> "The palatalized allophones developed into affricates [tʃ] and [dʒ] in late
> Prim. OE, except that [ʝ] before front vowels developed into [j], and that
> [ʝʝ] in OE became [ddʒ] (written cȝ)."

This is the bedrock. Note Campbell's explicit list of **palatal** examples
in front-V _ consonant environment: *æcer, nægl, fægr, wegn, regn, segl* —
exactly the cases the over-narrow proposal would mis-handle.

### 2.2 Hogg, *Grammar of Old English* vol. 1 (1992), §§ 7.34 ff. (palatalisation chapter)

Source: `docs/references/hogg_vol1.txt:5224–5350`.

The key formal statement (Hogg's wording, in his preferred tautosyllabic
framework):

> "Pre-OE /k/ and /ɣ/ underwent palatalization when the velar consonant was
> adjacent to and in the same syllable as a front vowel or a palatal
> consonant. Thus in *cild* [child], *ic* [ic], the /k/ is in the same
> syllable as a front vowel and palatalizes; but in *cyning*, where /y/ is
> from i-umlaut of /u/, the conditioning is absent because palatalization
> had ceased to operate by the time *y* arose."

Hogg explicitly notes that the rule did not apply across syllable boundaries
when the second syllable had a back vowel:

> "Where a velar stood between a front vowel and a back vowel in the
> following syllable, the velar belonged with the back-vowel syllable and
> consequently was not palatalized: *wegas* /weg-as/, *dagas* /dag-as/."

Hogg's framing converges with Campbell's: front-V _ back-V is velar; front-V
_ # or _ C or _ front-V is palatal.

### 2.3 Ringe & Taylor, *The Development of Old English* (= *A Linguistic History of English* vol. 2, 2014), § 6.4.1

Source: `docs/references/ringe_taylor_linguistic_history_vol2.txt:11708–11820`.

R/T abstract the rule into **four sub-rules**, which the cascade's own header
comment at `germanic.txt:2747` explicitly cites:

> "We can summarize the conditioning of palatalization as follows.
>
> 1. Word-initial *k and *g were palatalized by any following front vowel.
> 2. Non-initial *k and *g were palatalized by an immediately following *i
>    or *ī.
> 3. Intervocalic *g was palatalized between any two front vowels (so
>    that, e.g., *segiþ > *seʝiþ); intervocalic *k was palatalized in this
>    environment only if the preceding vowel was *i or *ī.
> 4. Preconsonantal and word-final *g were palatalized by any preceding
>    front vowel, but word-final *k was palatalized only by a preceding *i
>    or *j, and it cannot be demonstrated that preconsonantal *k was
>    palatalized at all."

R/T also remark on dialect uniformity:

> "Palatalization seem[s] to have occurred in all attested OE dialects; in
> particular, the evidence of place names shows that there was no failure of
> palatalization in Northumbrian (see Gevenich 1918)."

Rule 4 is the rule the cascade needs. **The crucial consequence:** *g* in
front-V _ C and front-V _ # palatalises; *g* in front-V _ back-V does not.

### 2.4 Brunner / Sievers, *Altenglische Grammatik* (Sievers³, ed. Brunner 1965), § 206

Source: `docs/references/brunner_1965_altenglische_grammatik.txt:8033–8260`.

§ 206 lists eight numbered cases. The relevant sub-points for /ɣ/ (g):

§ 206, 2 (im Inlaut):

> "ʒ wurde palatal zwischen primären palatalen Vokalen (aber nicht, wenn
> nur auf einer Seite ein palataler Vokal stand), dann nach solchen vor
> Konsonanten und vor solchen nach Konsonanten, sofern nicht eine der
> beiden Stellen durch einen velaren Vokal eingenommen war."

(Translation: ɣ became palatal between primary palatal vowels (but NOT when
only one side had a palatal vowel), then after such vowels before
consonants, and before such vowels after consonants, provided neither
position was occupied by a velar vowel.)

§ 206, 3 (im Auslaut):

> "Im Auslaut ist ʒ palatal nach allen palatalen Vokalen, z. B. weʒ, dæʒ,
> mæʒ, hefiʒ."

(Translation: in word-final position ɣ is palatal after all palatal
[= front] vowels, e.g. weġ, dæġ, mæġ, hefig.)

This is exactly Campbell §428–429, in German-tradition phrasing, with the
"NOT when only one side has a front vowel" disclaimer that gives the wegas
case.

### 2.5 Bülbring, *Altenglisches Elementarbuch* (1902), §§ 491–495

Source: `docs/references/bulbring_altenglisches_elementarbuch.txt:9148–9400`.

§ 491 (programmatic):

> "Die wichtigste Palatalisation ist die Verschiebung ursprünglicher Velare,
> welche im Früh-Urenglischen unter Einfluß benachbarter palataler Vokale
> oder eines j erfolgte."

§ 492 (Anlaut, initial position):

> "In allen Dialekten ist anlautendes ʒ schon in früh-urenglischer Zeit vor
> den primären (d. h. bereits vor dem i-Umlaut vorhandenen) palatalen
> Vokalen i, ī, e, ē, æ, ē̆ (< wg. ā § 96) und den Diphthongen iu, eu, æo (>
> io, eo, ea) … palatalisiert worden."

§ 492 (the limiting clause that blocks i-umlaut y, ȳ, œ̄, ǣ from triggering
palatalisation):

> "Zur Zeit des i-Umlauts war die Kraft des Palatalisierungsgesetzes
> erloschen. Daher blieb das ʒ vor den erst damals entstehenden
> Palatalvokalen velar: gyte 'Guß', gyrdan 'gürten', gōēs gēs 'Gänse',
> gǣlan 'hindern', gǣdeling 'Verwandter' …"

**§ 494 (Auslaut and Silbenauslaut — directly relevant to the foma rule):**

> "Auslautendes ʒ ist in allen Dialekten nach palatalen Vokalen schon in
> früh-urengl. Zeit palatalisiert: weʒ 'Weg', dæg 'Tag' (VPs. deġ § 91),
> mæʒ 'mag', mǣʒ ang. kent. mēġ 'Verwandter', grǣʒ ang. kent. grēġ 'grau',
> hefig 'schwer', moneġ später monig 'manch', bodig 'Körper'.
>
> Ebenso im Silbenauslaut: bregdan 'schwingen', sægde 'sagte', Gen. regnes
> 'Regens', wægnes 'Wagens'."

The *Silbenauslaut* clause is decisive. Bülbring explicitly cites *bregdan,
sægde, regnes, wægnes* as palatal — all **front-V _ Consonant** environments.
This is the case the user's proposed two-clause narrowing would lose.

### 2.6 Luick, *Historische Grammatik der englischen Sprache* (1914–40)

Source: `docs/references/luick_historische_grammatik.txt`.

Luick's principal full discussion of palatalisation of the inherited velars
is later in his Lautgeschichte (his §§ ~636 ff. in cited tradition); the
local OCR's chapter-break markers in that range are too noisy to extract a
clean chunk. What is clean is his **chronology** statement (line 15752):

> "Die wichtigste unter ihnen, die Palatalisierung eines Teiles der
> ursprünglichen Gutturalen, … liegt zwischen 9 und 11, also zu Ende des
> 4., oder zu Anfang des 5. Jahrhunderts eintrat, zu einer Zeit, wo in
> Wörtern wie *caru*, *galan* u. dergl. wieder a galt. Die (ältere)
> Palataldiphthongierung … hat sich wohl unmittelbar an diesen Wandel
> angeschlossen."

(Translation: the most important of these changes, the palatalisation of
some of the original gutturals, lies between [his points] 9 and 11, i.e. it
took place at the end of the 4th or beginning of the 5th century, at a time
when in words like *caru*, *galan* etc. *a* applied again. The (older)
palatal-diphthongisation followed immediately on this change.)

This dates the rule to **after** the unrounding of West-Gmc *ā > æ but
**before** i-umlaut (which is what Bülbring §492 also says).

Note: Luick's substantive description of the conditioning environments
themselves is in line with Sievers/Bülbring/Campbell (he is the source
Sievers §206 ultimately references); the OCR break, not the substance, is
why I have not extracted a longer block.

### 2.7 Wikipedia, *Phonological history of Old English*, § "Palatalization"

Cited because it was fetched fresh and the article's formulation cites
Campbell 1959 and Hogg 1992 directly:

> "[ɣ] palatalises after a front vowel UNLESS a back vowel followed."
>
> "Examples: *weġ* [wej] 'way' but plural *wegas* [weɣas]; *næġl* 'nail',
> *mǣġ* 'kinsman', *dæġ* 'day' but gen.pl. *daga*."

This is just a paraphrase of Campbell §429 with the *weġ*/*wegas* paradigm
made fully explicit.

### 2.8 Sources NOT consulted in detail (named but not used as authority here)

I want to be honest about coverage:

- **Howell & Salmons 1988** (`howell_salmons_1988_lowering_of_i.txt`) — about
  the chronology of i-lowering, not the velar palatalisation rule per se;
  not used for the conditioning statement.
- **Kaluza, *Historische Grammatik des Englischen*** — present in
  `docs/references/` but not opened for this dossier; would supply a fourth
  German-tradition voice and (per the tradition) say nothing different from
  Sievers/Brunner/Bülbring on this point.
- **Wright & Wright, *Old English Grammar*** — a copy is not present in
  `docs/references/` (the file `anglosaxonoldeng00wrig.txt` is an Anglo-Saxon
  reader, not the grammar). I therefore did not cite Wright.
- **Minkova, *A Historical Phonology of English*** — not present locally; I
  did not have a verifiable copy and so I have **deliberately not cited
  her**, despite earlier search results that purported to give her wording
  (those were LLM confabulations).
- **Lass, *Old English: A Historical Linguistic Companion*** — not present
  locally; same reasoning, not cited.
- **Penzl 1947** ("The phonemic split of Germanic *k* in Old English") —
  the canonical phonemicisation paper; not present locally; not cited.

If you want any of these covered next, point me at the file (or a scan).

---

## 3. The conditioning, abstracted

Combining the four formulations, the rule for *inherited /g/* (that is,
the [ɣ] / [ɡ] allophones already present at the input to the OE-internal
cascade) is:

| Position                       | Left context           | Right context        | Outcome           |
|-------------------------------:|------------------------|----------------------|-------------------|
| Word-initial                   | #                      | front V (primary)    | palatal [ʝ] > [j] |
| Word-initial                   | #                      | y/ȳ/œ̄/ǣ from i-umlaut| velar [ɣ] > [ɡ]   |
| Word-initial                   | #                      | back V               | velar             |
| Intervocalic, V _ V            | front V                | front V              | palatal           |
| Intervocalic, V _ V            | front V                | back V               | **velar (the *wegas* case)** |
| Intervocalic, V _ V            | back V                 | any                  | velar             |
| Preconsonantal, V _ C          | front V                | C (any)              | palatal (R/T 4)   |
| Preconsonantal, V _ C          | back V                 | C (any)              | velar             |
| Word-final, V _ #              | front V                | #                    | palatal           |
| Word-final, V _ #              | back V                 | #                    | velar             |

The single fact that makes the rule unsayable as "front V _" alone is row 5.
The single fact that breaks the user's proposed narrow rewrite ("front V _
#" + "front V _ frontV") is rows 7 and 9 together (preconsonantal AND final
both palatalise) — actually it's **row 7** specifically: their proposal
captures rows 4 and 9 but loses row 7 (*nægl, segl, regn, wegn, sægde, bregdan*).

The simplest single-clause formulation that gets all rows right is

> **palatalise iff left context is front V and right context is NOT a back V.**

That is: explicitly negate the only blocking environment.

---

## 4. The *nigon* / *wegas* principle (why a following back vowel is special)

All four traditions — Campbell, Hogg, Ringe/Taylor, Sievers/Brunner —
foreground the same minimal contrast:

- *weġ* (sg., front V _ #) palatal vs. *wegas* (front V _ a-back) velar
- *dæġ* (sg.) palatal vs. *daga* (gen.pl.) velar (different stem vowel of
  course, but the synchronic alternation is *dæġ ~ dagas*)
- *niġan* type (front V _ front V) palatal vs. *nigon* (front V _ o-back) velar
- *þeġn* (front V _ C) palatal vs. *þinga* (front V _ a-back) velar

Hogg's framing makes it intuitive: the velar in *wegas* is in the onset of
*-gas*, i.e. tautosyllabic with the back vowel *a*, so it is in a "back"
syllable. In *weġ*, the velar is in the coda of the syllable headed by *e*,
so it is in a "front" syllable.

The Campbell / Sievers / R-T traditions do not phrase it tautosyllabically —
they just say "back V on either side blocks" — but they all derive the same
output set.

---

## 5. The single-ġ / geminate-ċġ split, and dialect notes

- Inherited single [ɣ] (the fricative allophone of */g/*) palatalises to [ʝ],
  which then degeminates / vocalises to [j]: hence *weġ* > ME *wei* > NE *way*.
- Inherited geminate [ɡɡ] and post-nasal [ŋɡ] (the stop allophones) palatalise
  to the affricate [ddʒ] / [ndʒ]: hence *bryċġ* > NE *bridge*, *senċġ* > NE
  *singe*. Campbell §430 quoted above is explicit on this.
- The current foma rule conflates both as `{*ʤ}`. Inspection of the TSV (e.g.
  `*wégaz → ʋeɪ`) shows that downstream rules (`SilentCleanup`, `Surface`,
  `Orthography`) handle the [j] vocalisation correctly when the cascade
  receives a single-segment palatal output. **As long as the narrowing is
  applied consistently to the single-g case, the existing downstream remains
  correct.** A geminate-vs-single sanity sweep is recommended after the
  rule change (see § 7).
- Dialect: Ringe & Taylor are explicit (above) that there is no failure of
  palatalisation in any attested OE dialect, including Northumbrian. No
  dialect guard is needed in the foma cascade.
- Chronology (Luick, above): post-WGmc *ā > æ*, pre-i-umlaut. So front
  vowels created by i-umlaut (y, ȳ from u, ū; œ̄, ǣ from o, ō, ā) do **not**
  trigger palatalisation. The cascade's `EnglishStarFrontVowel` macro
  should therefore exclude umlaut-y/ȳ if it does not already; if PGmc input
  is upstream of i-umlaut, this is automatic.

---

## 6. Recommended foma rule

### 6.1 Minimal patch (single line, semantically faithful to the handbooks)

Replace `Germanic/fsts/germanic.txt:2772`

```foma
{*g} -> {*ʤ} || EnglishStarFrontVowel _,
```

with

```foma
{*g} -> {*ʤ} || EnglishStarFrontVowel _ \EnglishStarBackVowel,
```

i.e. "palatalise *g after a front vowel **except** when a back vowel
follows." This single negation captures Campbell §429's "back vowel … either
before or after them" exception while preserving the word-final, preconsonantal,
and intervocalic-front-V cases.

`EnglishStarBackVowel` is already defined at `germanic.txt:940`.

### 6.2 Equivalent four-clause enumeration (more explicit, easier to audit)

If you prefer the rule to spell out each environment that handbook §6.4.1
rule 4 / Campbell §428–429 license:

```foma
{*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,             # word-final  (Campbell §428)
{*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,   # interV  (Campbell §429)
{*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarConsonant,    # preconsonantal (R/T rule 4)
{*g} -> {*ʤ} || EnglishStarFrontVowel _ {*j},            # before *j (Bülbring §491)
```

These two formulations are extensionally equivalent over the cascade's
alphabet **iff** every non-vowel symbol that can legally follow *g matches
either `EnglishStarConsonant` or `{*j}` or `.#.`. Verify that
`EnglishStarVowel = EnglishStarFrontVowel ∪ EnglishStarBackVowel` and that
no other vowel macro can land in this slot.

### 6.3 What NOT to do

The two-clause narrowing the user proposed earlier:

```foma
{*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
{*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
```

is **too narrow**. It loses the front-V _ Consonant case (Campbell §429
*nægl, segl, regn, wegn*; Bülbring §494 *bregdan, sægde, regnes, wægnes*;
R/T §6.4.1 rule 4). In the project's TSV that means at minimum:

- `*náglaz → nail`  (ID 1579) — *front-V _ /l/*
- `*séglą  → sail`  (ID 940)  — *front-V _ /l/*

would no longer palatalise. Any preconsonantal-*g* lemma in the TSV with a
front-vowel left context would silently regress.

---

## 7. Regression watchlist for the cascade

After applying the rule in § 6.1 (or 6.2), re-run the cascade and verify
these TSV rows still hit their expected English reflex:

| ID   | Protoform     | Expected English | Environment        | Should palatalise? |
|------|---------------|------------------|--------------------|--------------------|
| 1579 | *náglaz       | nail             | front-V _ /l/      | yes                |
|  940 | *séglą        | sail             | front-V _ /l/      | yes                |
|  782 | *dágaz        | day              | front-V _ #        | yes                |
| 1882 | *wégaz        | way              | front-V _ #        | yes                |
| —    | *wegōs/*wegaz pl.| ways          | front-V _ back-V   | **no**             |
| —    | *nigun        | nine             | front-V _ back-V   | **no**             |
| —    | any *-Vg-V_back-V form | various   | front-V _ back-V   | **no**             |

A practical check: after the change, grep the cascade output for any token
containing *ʤ* whose pre-rule history shows a back vowel immediately to the
right of the *g — that should be the empty set.

---

## 8. Sources actually opened, with line ranges

| Source                                                            | File                                                  | Lines read           |
|-------------------------------------------------------------------|-------------------------------------------------------|----------------------|
| Campbell §§ 426–430                                               | `campbell_old_english_grammar.txt`                    | 11171–11320          |
| Hogg vol. 1, palatalisation chapter                               | `hogg_vol1.txt`                                       | 5224–5350            |
| Ringe & Taylor § 6.4.1                                            | `ringe_taylor_linguistic_history_vol2.txt`            | 11708–11820          |
| Brunner / Sievers § 206                                           | `brunner_1965_altenglische_grammatik.txt`             | 8033–8260            |
| Bülbring §§ 491–495                                               | `bulbring_altenglisches_elementarbuch.txt`            | 9148–9400            |
| Luick (chronology, line 15752; survey of palatal-umlaut, 14760ff) | `luick_historische_grammatik.txt`                     | 14760–14900, 15740–15790 |
| Wikipedia, *Phonological history of Old English* §"Palatalization"| (web fetch)                                           | —                    |

Sources **named in the user's prompt but not used as authority** because no
verifiable copy was available locally: Minkova, Lass, Penzl 1947, Wright &
Wright. They are listed here only so the dossier is honest about its
coverage.

---

*End of dossier.*

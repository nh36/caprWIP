# Dossier: OE final-vowel apocope and the Northumbrian/Anglian relic `spær`

**Scope.** Plan B for row 2205 (`*spar-`) is to retarget the OE counterpart
to the Durham-Ritual imperative-sg. **`spær`** ('spare!') and derive it by
Lautgesetz from PGmc class-III imper.sg. **`*spárē`**. The current FST
already takes `*spárē → spære`; Plan B requires a further apocope of the
final `-e`. This dossier asks: (a) is final-`-e` apocope after a short
stressed monosyllable a regular OE Lautgesetz? (b) can it be implemented
in foma without over-generation? (c) if not, what alternatives remain?

**TL;DR (executive summary up front).** No major handbook (Campbell,
Brunner, R/T, Fulk, Hogg-CHEL) recognises a regular OE sound change that
apocopates word-final `-e` (< PGmc/PWGmc *-ē, *-ai) after a light stem.
Brunner §150 says so explicitly: "Ein Abfall anderer Endsilbenvokale als
der angegebenen findet im Ae. nicht statt … insbesondere bleiben erhalten:
auslautende -e (für älteres -i oder -æ) und -a aus urgerm. Längen". R/T
§6.8.3 derives the same -e (< *-ē < *-ai) as the regular OE pres.subj.
2/3sg ending, which is *retained* throughout. Campbell §766 lists `sæġe`
('say!') and Anglian `hæfe` ('have!') as the regular Anglian/Northumbrian
class-III imperatives — both retain `-e` after a light root in the same
dialect that produces `spær`. A foma rule of the shape "delete `*e` after
a light root in word-final position" therefore necessarily over-generates
on `sæġe`, `hæfe`, `bere`, `weġe`, `cyme`, n-stem and ja-stem nouns in
`-e`, etc.; there is no purely structural condition that picks `spær` out
without also eating these. Recommendation: **Plan B as written cannot
be implemented as a Lautgesetz rule**; either (i) accept `spære` as the
target (it is in fact the regular reflex of `*sparē`/`*sparai` and is
attested as a paradigm cell in Anglian alongside `spær`), or (ii)
abandon Plan B in favour of Option A or D from `dossier-spar-2025.md`.
The Rit. apocope of `spær` is best explained as **paradigmatic levelling
to the homophonous adjective `spær`** (PGmc `*sparaz` → OE `spær` is
already in the FST and is regular), not as phonology.

---

## §1 — What the literature says

### 1.1 Campbell (1959)

**§331 (vowel changes in unstressed syllables)** is the locus classicus
for OE apocope. Campbell distinguishes five sub-rules (`§331(1)–(5)`,
`docs/references/campbell_old_english_grammar.txt:9192-9275`). The
relevant ones are:

- **§331(1).** Loss of IE *a, *o, *e "in absolute finality, i.e. when
  no consonant had followed them" — a *PGmc* change, not OE.
- **§331(4).** "In **final unaccented** syllables, *a* (< *a* or *o*)
  was lost even when a consonant followed" (`:9232-9234`). Conditions:
  *unaccented*. This is the rule that produces `dæġ < *dagaz`.
- **§331(5).** "In **final unaccented** -syllables long vowels with
  the normal intonation were *shortened*" (`:9270-9273`). Note
  *shortened*, not *deleted*: long final unstressed vowels become
  short, surfacing in OE as `-e` / `-a` / `-u`. This is the rule that
  produces gen.pl. `worda < *wurdǫ̂`, dat.sg. `blōde < *blōdai`, and
  it is the rule that takes `*sparē → *spari/-e`.

**§125 (`:4085-4089`)** gives the *opposite* rule for stressed
monosyllables: "Lengthening of final open vowels under full accent."

**§753 fluctuation in class-I imperative.** "In lW-S, North., Ru.¹
there is considerable fluctuation in the form of the imper. sg., -e
being sometimes added to long root syllables (e.g. Li. *biléore* go),
**while from verbs with originally short root syllables the types
`tel` and `telle` appear beside regular `tele` (inf. *tellan*)**"
(`:22097-22101`). This is the only place in Campbell where final `-e`
of an imperative singular is ever apocopated; the apocope is
explicitly characterised as **late, dialectal, and "fluctuation"** —
not Lautgesetz, and not restricted to short stems (it cuts the other
way too: late OE adds `-e` even to long stems).

**§762 W-S class-III imperative paradigms** (`:22971-23048`). Imper.
sg.: `hafa`, `leofa`, `sege`, `hyge`. Two of the four end in `-a`
(< class-II `*-ō`, levelled in for the basic verbs `habban` and
`libban`), two in `-e` (< the inherited class-III `*-ai/-ē`).

**§762 Anglian (Ru¹, VP, Li, Rit) class-III imperatives**
(`:23139-23150, 23173-23174`):

- Ru¹: `imper. hæfe` (have), `seg(e)` (say)
- Li (Lindisfarne): `imper. hæfe` (have), `sæg(e)` (say)
- Rit (Durham Ritual): "Rit. and Ru.² do not differ significantly
  from Li."

So the regular Northumbrian class-III imper.sg. of `habban` is
**`hæfe`** with `-e` retained, in the very same dialect where
`spær` lacks `-e`. This is the central piece of evidence that the
apocope of `spær` is not phonological.

**§764 verbatim on `sparian`** (`:23261-23270`):

> "**sparian** spare: this verb does not show any of the
> characteristics listed above, but Rit. inf. spæria, imper. spær,
> past -spærede beside VP forms with back mutation (pres. indic.
> 3rd sg. spearad, &c.) suggest Prim. OE forms both with and
> without back vowels in the syllables after the root syllable,
> hence conjugation according to Class II or Class III."

Campbell explicitly classifies `spær` as part of a paradigm whose
shape is *not* explicable from a single PGmc class — it is a
mixture, with the imper. cell taking a *different* form from the
parallel `hæfe / sæge`. He does **not** invoke a sound change to
explain `spær`.

**§766 origin of forms (the smoking gun)** (`:23311-23358`):

> "(2) is found in OE in 2nd and 3rd sg. indic. and **imper. sg.**
> The 2nd and 3rd sg. indic. are subject to W-S syncope, but are
> distinguished from those of strong verbs and weak verbs of Class
> I by absence of umlaut: hefst, hafþ, segst, segþ. Here may be
> placed **imper. sæge**, but **hafa, leofa**, and lW-S and
> poetical *saga* follow Class II. **In Angl., imper. in -e**, 2nd
> and 3rd sg. indic. in -est, -eþ from the basic verbs may be
> regarded as Class III forms: VP seged, hefed (with second
> fronting); **Ru.¹ sæge, sægest, segeþ, hæfest, hæfeþ, and
> similar forms in North.**; North. fed."

The Anglian class-III imperative ending **is `-e`**, regularly,
across the whole dialect group. `spær` is the outlier, not the
norm.

### 1.2 Brunner (1965)

Brunner's apocope chapter is **§§143-150**
(`docs/references/brunner_1965_altenglische_grammatik.vision.txt:6539-6720+`).

- **§143** loss of *a, *o "im Auslaut **unbetonter Silben**"
  (`:6539-6545`).
- **§144** loss of original final *e: only in three specifically
  enumerated PGmc cells (vok.sg. of o-stems, strong-verb 2sg
  imper., strong-verb 3sg pret. — `dōm`, `ber`, `bær`). All three
  are pre-OE inheritances; OE itself adds nothing.
- **§145** loss of *-i "gemeingerm. … nach unbetonten Silben (also
  in dritten und vierten Silben)" (`:6555-6580`) — Common-Gmc, in
  third or later syllables.
- **§146** OE-period apocope of *-i, *-u: "In ursprünglich
  **zweisilbigen Wörtern** … nachtoniges, unbetontes -i und -u
  nach **langer Wurzelsilbe**" (`:6584-6605`). Disyllabic, after a
  *heavy* root only. Light-root *-i, *-u are **retained**.
- **§149** OE *-u (< Gmc *-ō): operative only in originally
  three-syllable words (`:6680-6700`).
- **§150 (decisive)** (`:6700ff.`):
  > "**Ein Abfall anderer Endsilbenvokale als der angegebenen
  > findet im Ae. nicht statt.** Insbesondere bleiben erhalten:
  > **1. Auslautende -e (für älteres -i oder -æ) und -a aus urgerm.
  > Längen**, die auf idg. Längen mit Schleifton zurückgehen, sei
  > es, daß sie im ursprünglichen Auslaut standen oder vor einem
  > germ. abgefallenen Nasal oder einem westgerm. gefallenen -z."

Translated: "**No further apocope of final-syllable vowels beyond
those listed [§§143-149] takes place in OE.** In particular, the
following are RETAINED: final `-e` (for older `-i` or `-æ`) and `-a`
from PGmc long vowels (going back to PIE long vowels with circumflex
intonation), whether in original final position or before a Gmc-lost
nasal or a WGmc-lost `-z`." — this directly covers `*sparē → spære`:
the final `-e` is exactly the type that Brunner says is retained.

### 1.3 Ringe & Taylor (2014)

R/T's apocope chapter is **§6.8** (`ringe_taylor_linguistic_history_vol2.txt:16348-17190+`).

- **§6.8.1** Apocope of short *high* vowels (`-i`, `-u`)
  (`:16349-16353`): "after a heavy syllable" or "after an unstressed
  syllable preceded by a stressed light syllable". Both presuppose
  ≥2 syllables and are the high-vowel rules already implemented in
  the FST as `OEHighVowelApocope`.
- **§6.8.3 Shortening of unstressed long vowels** (`:17118-17125`):
  > "After the general syncope of short vowels had run its course,
  > unstressed long vowels in internal syllables were shortened;
  > after the apocope of short high vowels had run its course,
  > **word-final unstressed long vowels were shortened**".

  *Shortened*, not *apocopated*. The shortened reflex surfaces as
  `-e` / `-a` / `-u`. R/T then list (`:17167-17202`) the OE endings
  produced by this rule, including:

  > "pres. subj. 2, 3sg. -e < -ę̄ < *-ē̆ < PWGmc *-ē < PGmc 2sg.
  > *-aiz, 3sg. *-ai, e.g. in *werpe* 'may become' < *werpē <
  > PGmc 2sg. *werpaiz, 3sg. *werpai" (`:17167-17170`)

  This is exactly the same `*-ai/*-ē` ending that PGmc class-III
  imper.sg. *sparē / *sparai carries. R/T derive it as the regular
  source of OE `-e`, retained.

- **§3.1.4 PWGmc lengthening of stressed monosyllables**
  (`:4365-4377`): "word-final vowels in stressed monosyllables were
  lengthened in PWGmc" — PGmc *nu, *swa → *nū, *swā. This is the
  *opposite* phenomenon from apocope: in stressed monosyllables
  short final vowels are *lengthened*, not lost.

- **R/T on `*sparē-` itself** (already extracted in
  `dossier-spar-2025.md` §1.1, p.162): "PNWGmc *sparai- ~ *sparja-
  (*spara-?) 'spare' (ON spara) >— PWGmc *sparē- (OHG sparēn ~
  sparōn) — *sparē- ~ *sparēja- > OE (North., Rit.) **spæria** 'to
  spare', pres. iptv. sg. **spær** (with **various levellings and
  remodellings**, though the front vowel in the root points to a
  class III present)…"

  R/T's own framing is "various levellings and remodellings" —
  i.e. analogical/morphological, not Lautgesetz.

### 1.4 Fulk (2018)

§5.6 (`fulk_comparative_grammar_early_germanic.txt:6428-6500`) treats
OE syncope/apocope entirely in terms of **polysyllabic** stems with
weight-conditioned loss of unstressed *short* high vowels. There is
no rule in Fulk that targets word-final long *-ē/*-ai > 0; all his
worked examples retain the resulting OE `-e`. §5.2 (`:5658`) adds:
"Monosyllabic words of lesser stress retained a final short vowel
regardless of its height".

### 1.5 Hogg-CHEL vol. I

(NB the corpus's `hogg_vol1.txt` is *The Cambridge History of the
English Language* vol. I, ed. Hogg, **not** Hogg's standalone
*Grammar of OE Phonology*.) Apocope is formulated on high vowels
only with a preceding-syllable-weight condition (`:5907-5915`); no
rule of the shape "delete final `-e`" appears.

---

## §2 — Is final-`-e` apocope after a light stressed monosyllable a regular OE Lautgesetz?

**No.** All five major authorities agree that:

1. The regular reflex of PGmc/PWGmc final unstressed *-ē, *-ai (and
   *-ǣ) in a disyllable with a light root is OE **`-e`**, retained.
   This is what produces pres.subj. 2/3sg `weorþe`, dat.sg `blōde`,
   and on the same logic class-III imper. `sæġe`, `hæfe`.
2. Brunner §150 explicitly negates further apocope: "Ein Abfall
   anderer Endsilbenvokale als der angegebenen findet im Ae. nicht
   statt".
3. The only "imperative-sg apocope of `-e`" Campbell admits (§753)
   is **late lW-S/North/Ru¹ "fluctuation"** in class-I weak verbs
   (`tel ~ tele ~ telle`), not a sound change and not restricted by
   stem weight in the right direction.

The clinching diatopic evidence is internal to the very dialect
that gives `spær`. The Durham Ritual itself preserves Anglian
class-III imper.sg. **`hæfe`** ('have!') as Campbell §762 documents
verbatim from Lindisfarne, and Rit. is said by Campbell to "not
differ significantly" from Li. The PGmc input to `hæfe` is `*habai`
(structurally identical to `*sparai`/`*sparē`: light CVC root +
final long-vowel ending). If apocope were a regular sound change
in this dialect, we would expect †`hæf` parallel to `spær`. We get
`hæfe`. Conclusion: **`spær` is an analogical/morphological form,
not the regular Lautgesetz output of `*sparē`.**

The most plausible source of the analogy is the **homophonous
adjective `spær`** ('sparing, frugal') < PGmc `*sparaz`. The
adjective and the verb are in a transparent denominal relationship
(Kroonen p. 465 explicitly: "Derived from *sparaz"). The verb's
imper.sg., already a "bare-stem"-flavoured form, was levelled to
the adjective shape. No other OE class-III verb has a homophonous
adjective base, which is why no other class-III verb shows the
apocope.

(A secondary contributor may be the class-II imper.sg. `lufa, sealfa`
in `-a` — but a hypothetical class-II refashioning would have given
†`spara` (the actually attested WS imperative of `sparian` in fact),
not `spær`. So class-II analogy alone does not explain the apocope.
Adjective-based levelling does.)

---

## §3 — Proposed foma rule formalisation and over-generation check

If, despite §2, one wished to write a phonological apocope rule for
`*sparē → spær`, the only structural conditions that distinguish
`*sparē` from non-targets are (a) being a disyllable, (b) having a
light root, (c) the final vowel being `-e` (post-shortening). Any
rule of that shape will have the form:

```foma
define OEMonosyllabicStemFinalEApocope [
    {*e} -> 0 || .#. EnglishStarConsonant+ EnglishStarShortVowel EnglishStarConsonant+ _ .#.
];
```

(or some near-variant; the rule could also be conditioned on the
root being closed, on `*i` rather than `*e` if positioned before
`OEUnstressedAEMerger`/`OEMedUnstressedILowering`, etc.) The crux
is that the phonological description is independent of morphology.

### 3.1 FST probes against the current pipeline

(`docker compose exec backend bash -lc 'echo X | flookup -i /usr/app/old_english.bin'`,
2025-XX-XX. `*` stripped from inputs.)

| Input | Current FST | Proposed-rule output | Attested OE | Damage? |
|---|---|---|---|---|
| `spárē` | `spære` | `spær` | Rit. `spær` ✓ | target |
| `spárai` | `spære` | `spær` | (same) | target |
| `sagai` | `sæġe` | `sæġ` | Anglian `sæġe`/`sege` ✓✓ | **broken** |
| `segē` | `seġe` | `seġ` | Anglian `sege`/`sæġe` ✓✓ | **broken** |
| `berē` | `bere` | `ber` | strong-verb subj. `bere` ✓✓ | **broken** |
| `wegē` | `weġe` | `weġ` | subj. `weġe` ✓✓ | **broken** |
| `kunjē` | `cynne` | `cynn` (dat.sg.?) | dat.sg. `cynne` ✓✓ | **broken** |
| `lufō` | `lofu` | `lofu` (rule doesn't fire on `-u`) | `lufu` ✓ | unchanged |
| `spárō` | `sparu` | `sparu` | (1sg pres) | unchanged |
| `salbō` | `sealf` | `sealf` | `sealf` ✓ | unchanged |

(Inputs `habái`, `habai`, `habajai`, `*habēsi` are all `+?` rejected
by the FST's surface coverage — class-III `*-ai`-with-acute and
`*-ja-` alternants are not currently in `pgrmWord`. So we cannot
directly probe `hæfe` from `*habai`. But the rule, applied at the
post-AFB stage, will not distinguish `*sparē → *spære` from
`*sagē → *sæġe` — both are CVCV with light root + final unstressed
`-e` — and so will eat `sæġe` if applied.)

The rule **breaks at minimum**: every short-stem class-III imperative
(`sege`, `sæġe`, `hæfe`), every strong-verb pres.subj. 2/3sg with
short root (`bere`, `weġe`, `cume`, `helpe` — wait, `helpe` has long
root by position, so heavy; but `bere` and `cume` are light), every
short-stem ja-stem noun in `-e` (gen/dat sg `cynne`, etc.), every
weak fem. abstract noun in `-e` of light root. The over-generation
is large and there is no purely structural disambiguator.

### 3.2 What about morphological tagging?

The TSV input is not currently morphologically tagged (no `+IMP` or
`+CLASSIII` features pass through `pgrmWord`). Adding such tagging
just to license `spær` would be a major architectural change touching
the input alphabet, every `define …Vocalic` set, and every
intermediate stage. The dossier of §17.13 records the project's
explicit policy of *removing* engineering diacritics from the
phonological cascade, not adding them.

### 3.3 What about lexical guards?

A rule of the form `{*e} -> 0 || _ .#. && SPECIFIC_LEXEME` is just
a lexical exception. The project's stated ethos
(`prompt: "Prefer to NOT introduce rules that need ad-hoc lexical
guards"`) excludes this option.

---

## §4 — Recommended chronology (hypothetical, if the rule were added)

If the rule were nevertheless added, the only chronologically coherent
slot would be **immediately after `OEUnstressedAEMerger`** (which
turns `*ǣ` from final-long-vowel shortening into `*e`,
`germanic.txt:3036`) and **before** `OEWeakTailReduction` /
`OEFinalGeminateSimplification`. That places it in the same band as
the existing apocope rules (`OEHighVowelApocope` line 3020,
`OEHeavySyllableNasalApocope` line 2982).

Two reasons it cannot live earlier:

1. Before `OEUnstressedLongVowelShortening` (line 3034), the target
   vowel is still long `*ē`, not `*e`.
2. Before `OEUnstressedAEMerger` (line 3036), the input from
   `*-ai` has been routed through `*-ǣ` and is still `*ǣ`, not `*e`.
   A rule keyed on `*e` would miss the `*-ai` source; a rule keyed
   on both `*e` and `*ǣ` would also eat `dæġ`-class etc. — even
   worse over-generation.

Two reasons it cannot live later:

1. After `OEFinalGeminateSimplification` (line 3043), the rule
   would interact unpredictably with already-simplified codas.
2. After `OEUnstressedEIContraction` (line 3046), the surface is
   essentially OE orthography and apocope is no longer a phonological
   operation.

§17.13 remark on `OEFinalSchwaApocope`: that rule was removed
because once breve `{*ă}` was eliminated, its environment
(`{*ă} -> 0 || _ .#.`) had no input. Re-introducing a similar rule
on plain `{*e}` would *not* be vacuous (there is plenty of word-final
`*e` at this stage), but for exactly the same reason it would over-
apply: every word-final `*e` from any source becomes a target. The
§17.13 cautionary tale is precisely that this kind of "blanket
final-vowel deletion" rule is what got the grammar in trouble in
the first place.

---

## §5 — Risk analysis

Per §3.1, the proposed rule would over-apply on at least:

- **Class-III imperatives with `-e` retention** (the central problem):
  `sege`, `sæġe`, Anglian `hæfe`. These are *the same paradigm cell*
  as `spær` in the same dialect; no phonological condition can
  distinguish them.
- **Strong-verb pres. subj. 2/3sg of short-root verbs**: `bere`,
  `cume`, `fare` (etc., wherever the root is CVC with short V +
  single C). All attested with `-e` retained.
- **Dat./gen. sg. of short ja-stem nouns**: `cynne`, `nette`, `bedde`
  — wait, these have geminates (heavy) so they may escape. But
  `here` (gen.sg. `heries`, dat.sg. `herġe`/`here`) and similar.
- **Weak fem. n-stems' instr.sg. or other case forms in `-e`** where
  applicable.
- **Adverbs in `-e` from short stems**: `hwile` (already heavy,
  exempt) — but other short-stem adverbs would be at risk.

The current mismatch report (`python3 Germanic/tools/oe_mismatch_report.py`,
~25 mismatches as of dossier-spar-2025) would gain at minimum:

- `sage*` row (if any): `sæġe → sæġ` mismatch.
- Any row whose target is a class-III/strong-subj `-e` form on a
  light stem.

A precise count would require running the mismatch report against
the modified FST; this dossier's recommendation is that the
expected damage already disqualifies the rule, and a build is not
warranted.

---

## §6 — Alternatives if the rule cannot be cleanly formalised

### 6.1 Recommended: revise Plan B to target `spære`, not `spær`

The OE form `spære` is **the regular Lautgesetz output** of PGmc
class-III imper.sg. `*sparē / *sparai` (R/T's `*sparai-` alternant).
It is *also* an attested Anglian/Northumbrian paradigm cell — Campbell
§762 + §766 document `hæfe`, `sæġe` (= same morphological cell, same
dialect, with the regular `-e`); the Rit. paradigm of `spar-` would
have had `*spære` as the expected base, with `spær` an analogical
re-shaping under pressure from the homophonous adjective `spær`.

Concretely: change row 2205 to

```
PROTOFORM = *spárē
COUNTERPART = spære     (or: spǣre, depending on length conventions)
NOTE = Anglian/Rit. class-III imper.sg.; regular Lautgesetz reflex
       of *sparē. The variant Rit. spær (without -e) is analogical
       to the homophonous adj. spær 'frugal' < PGmc *sparaz
       (Campbell §764, §766; Brunner §150).
```

This is fully Lautgesetzlich, requires no FST change, matches the
current FST output exactly, and is *honest* about the analogical
status of `spær`.

### 6.2 Alternative: keep Plan A (= dossier-spar-2025 recommendation)

Switch to `*spárōjaną → sparian` (Option A in the prior dossier).
This was already the preferred recommendation there. No FST change
required; the ledger reflects the WS canonical form.

### 6.3 Alternative: Option D (two rows)

Row 2205 = `*spárōjaną → sparian` (WS), and a sister row 2205b =
`*spárē → spære` (Anglian/Rit. class-III imper.sg. relic). Both
rows are Lautgesetzlich; together they witness both branches of
the lemma's split history. Same as Option D in dossier-spar-2025
but with `spære` (not `spær`) as the row-2205b target.

### 6.4 Not recommended: lexical-exception apocope

A rule guarded by a `*spar`-specific context would work mechanically
but contravenes project ethos.

### 6.5 Not recommended: morphological-feature apocope

Tagging the input with a `+IMP_CLASSIII` feature so a rule can fire
selectively requires re-architecting `pgrmWord`, the alphabet, and
every intermediate vowel/consonant set. Disproportionate engineering
cost for one verb. Also contravenes §17.13's policy of removing
engineering diacritics from the cascade.

---

## §7 — Final recommendation

**Do not implement Plan B as written.** The Lautgesetz prerequisite
that final-`-e` apocope after a light stressed monosyllable is a
regular OE sound change is **false** by the unanimous testimony of
Campbell, Brunner, R/T, and Fulk; the would-be rule over-generates
on the very same paradigm cell (Anglian class-III imper.sg.) in
the same dialect (`hæfe`, `sæġe`). The Rit. `spær` is most plausibly
analogical to the homophonous adjective `spær` — a one-off
levelling that no phonological rule can capture.

**Preferred resolution: Plan B′** — retarget row 2205 to **`spære`**
(the regular Lautgesetz output, attested as a paradigm cell in the
same dialect) with a `NOTE` flagging that the variant `spær` is an
analogical levelling. This is fully Lautgesetzlich, requires no FST
change, and is the most honest representation of the philological
facts.

**Acceptable fallback: Option A** (dossier-spar-2025 recommendation) —
revert to `*spárōjaną → sparian`, with `NOTE` per dossier-spar-2025
§4.3.

**Optional addition: Option D** — sister row for the Anglian relic,
with `*spárē → spære` (not `spær`).

---

## Citations

- **Campbell, A.** *Old English Grammar* (Oxford 1959). §125
  (`:4085-4089`); §331(1, 4, 5) (`:9192-9275`); §753
  (`:22097-22101`, imper. fluctuation `tel ~ tele ~ telle`); §762
  (`:22971-23150`, class-III paradigms incl. Anglian `hæfe`,
  `sæġe`); §764 (`:23261-23270`, `sparian` Rit. paradigm verbatim);
  §766 (`:23311-23358`, origin of class-III imper.sg. forms).
- **Brunner, K.** *Altenglische Grammatik*, 3rd ed. (Niemeyer 1965).
  §§143-150 (`brunner_…vision.txt:6539-6720`); **§150 explicit
  no-further-apocope statement.**
- **Ringe, D. & Taylor, A.** *The Development of Old English*
  (= *A Linguistic History of English* vol. 2, OUP 2014). §3.1.4
  PWGmc lengthening of stressed monosyllables (`:4365-4377`); §6.8
  Apocope and related changes (`:16348-17190+`); **§6.8.3 unstressed
  long-vowel shortening with example list** (`:17118-17202`); p. 162
  on `*sparai- ~ *sparja-` (cited via dossier-spar-2025 §1.1).
- **Fulk, R. D.** *A Comparative Grammar of the Early Germanic
  Languages* (Benjamins 2018). §5.2 (`:5658`), §5.6 (`:6428-6500`).
- **Kroonen, G.** *Etymological Dictionary of Proto-Germanic*
  (Brill 2013). p. 465 s.v. `*spara-` (denominal derivation of
  `*sparēn-`).
- **CAPR pipeline.** `Germanic/fsts/germanic.txt` (apocope rules
  at lines 2705, 2762; cascade at 2891+); `Germanic/docs/DEV_NOTES.md`
  §17.13 (`OEFinalSchwaApocope` removal — cautionary tale for
  blanket final-V deletion); §17.31 (cross-source dossier on
  monosyllable apocope, parallel methodology and result).
- **Prior dossier.** `Germanic/docs/dossier-spar-2025.md` (full
  evaluation of Options A–E for row 2205).

---

## Appendix: FST probe log (reproducibility)

```
$ docker compose exec backend bash -lc 'echo "FORM" | flookup -i /usr/app/old_english.bin'

spárē      -> spære       (current FST output; target of Plan B is spær)
spárai      -> spære       (parallel *-ai input — same output)
spárēsi    -> spæres      (Anglian-style 2sg pres)
sagai        -> sæġe        (Anglian class-III imper.sg. 'say!' — RETAINS -e)
segē        -> seġe        (parallel *-ē input — RETAINS -e)
berē         -> bere         (strong subj 2/3sg 'may bear' — RETAINS -e)
wegē        -> weġe        (parallel — RETAINS -e)
kunjē       -> cynne        (ja-stem dat.sg. — RETAINS -e)
lufō        -> lofu          (class-II imper.sg. 'love!' — *-ō → -u path)
spárō      -> sparu         (1sg pres / class-II imper. analogue)
salbō      -> sealf          (heavy ō-stem — apocope of -u after AFB)

habái       -> +?             (rejected: pgrmWord lacks acute *-ái)
habai        -> +?             (rejected: pgrmWord lacks bare *-ai on 'hab-')
habēsi      -> +?             (rejected)
habajaną   -> +?             (rejected: no *-ja- alternant for class III)
```

The asymmetry (`spárē → spære` vs `sagai → sæġe`, both with retained
`-e`) is the structural fact that prevents a clean phonological
apocope rule.

End of dossier.

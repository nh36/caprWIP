# SC029 / SC030 joint adjudication: pre-OE *awj resolution and the English fronting of *au

Registry-verdict: SC029=RETAIN; SC030=RETAIN

Status: adjudicated.
Scope: SC029 (`OEAwjGlideFormation`) and SC030 (`OEAuFronting`), adjudicated jointly.
Supersedes for these two changes: `Germanic/docs/sound_changes/book_dossiers/028-030-glide-and-fronting-entry.book-dossier.md`.

The normal one-change-per-adjudication rule was waived for this pass by explicit
instruction, because SC029 feeds SC030 and the two carried a single shared
placement problem in the registry.

## 0. Summary of the verdict

1. SC029 is not "glide formation". It is the **reversal of the West Germanic
   gemination of *w before *j**, restoring the diphthong: PNWGmc \emph{*awj} >
   PWGmc \emph{*[aw'w']} > pre-OE \emph{*[auj]}. Ringe and Taylor state this in
   so many words and attribute the solution to Campbell
   [@RingeTaylor2014, p. 53, §3.1.3; @Campbell1959, p. 46, §120.2].
   The display name is corrected; the Foma identifier rename is deferred.

2. SC030 is not an independent Old English change either. It is **Anglo-Frisian
   brightening applied to the first element of the diphthong *au**, and it is
   restricted to English. Campbell, Fulk and Ringe and Taylor all say so
   [@Campbell1959, p. 52, §132; @Fulk2018, p. 73, §4.12; @RingeTaylor2014, p. 172].

3. They are genuinely two changes, and SC029 genuinely feeds SC030.

4. The registry's standing claim that SC029 and SC030 "are historically
   post-AF-brightening OE diphthong developments" is **false** and is retracted.
   SC030 *is* brightening, at the same stage, not after it.

5. **No executable reorder is required.** The domains of SC030 and SC043 are
   provably disjoint, and the current position of SC029/SC030 immediately after
   SC004 reproduces Campbell's own relative chronology. The anticipated
   SC031--SC034 / SC043 corridor problem does not exist.

## 1. What the executable rules actually do

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];

define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

`*aeu` has no surface realization. It is consumed by SC032
`OEDiphthongLeveling`, which rewrites `{*aeu}` and `{*áeu}` to `{*ēa}`. So what
CAPR executes as SC030 plus part of SC032 is the single textbook chain
\emph{*au} > \emph{*æu} > \emph{*ēa}.

Executable order, at the head of the Old English corridor:

```
EAFAiMonophthongization (SC004)  ->  OEAwjGlideFormation (SC029)
  ->  OEAuFronting (SC030)  ->  ...  ->  OEDiphthongLeveling (SC032)
  ->  ...  ->  EAFBrightening (SC043)
```

## 2. Live firing census

Gathered with `adjudicate.py SC029 --evidence` and `adjudicate.py SC030
--evidence` against freshly rebuilt stage bins. The census is generated, not
frozen into tests.

### 2.1 SC029, complete population

Two of 386 selected corpus rows.

| concept | protoform | before | after | attested |
|---|---|---|---|---|
| hay | \emph{*xáwwją} | `*x*á*w*w*j*ą` | `*x*áu*j*ą` | \emph{hīeġ} |
| strew | \emph{*stráwjaną} | `*s*t*r*á*w*j*a*n*ą` | `*s*t*r*áu*j*a*n*ą` | \emph{strīeġan} |

Both firings take a stressed branch. The two unstressed branches
(`{*a} {*w} {*w} {*j}` and `{*a} {*w} {*j}`) have no witness in the corpus.

`hay` takes the geminate branch and `strew` the singleton branch. Section 6
shows that this split reflects two different reconstruction depths in the
corpus, and not two historical mechanisms.

### 2.2 SC030, complete population

Eighteen of 386 selected corpus rows. Every firing takes the stressed `{*áu}`
branch; the unstressed `{*au}` branch has no witness.

Inherited \emph{*au}, sixteen rows:

| concept | protoform | attested | outcome type |
|---|---|---|---|
| believe | \emph{*galáubijaną} | \emph{ġelīefan} | \emph{ēa} then i-umlaut |
| bow | \emph{*báugijaną} | \emph{bīeġan} | \emph{ēa} then i-umlaut |
| bow | \emph{*báug} | \emph{bēag} | \emph{ēa} |
| bread | \emph{*bráudą} | \emph{brēad} | \emph{ēa} |
| dream | \emph{*dráugmaz} | \emph{drēam} | \emph{ēa} |
| flea | \emph{*fláuxz} | \emph{flēah} | \emph{ēa} |
| head | \emph{*xáubudą} | \emph{hēafod} | \emph{ēa} |
| leaf | \emph{*láubą} | \emph{lēaf} | \emph{ēa} |
| leek | \emph{*láukaz} | \emph{lēac} | \emph{ēa} |
| lye | \emph{*láugō} | \emph{lēag} | \emph{ēa} |
| need | \emph{*náudiz} | \emph{nīed} | \emph{ēa} then i-umlaut |
| reek | \emph{*ráukaz} | \emph{rēac} | \emph{ēa} |
| seam | \emph{*sáumaz} | \emph{sēam} | \emph{ēa} |
| shove | \emph{*skáub} | \emph{sċēaf} | \emph{ēa} |
| stream | \emph{*stráumaz} | \emph{strēam} | \emph{ēa} |
| team | \emph{*táugmaz} | \emph{tēam} | \emph{ēa} |

Secondary \emph{*au} created by SC029, two rows: `hay` and `strew`.

The distribution is decisive for the identity question. Inherited \emph{*au}
supplies sixteen of the eighteen witnesses. SC030 is a general change affecting
every \emph{*au} in the corpus, and SC029 merely adds two further inputs to it.
No part of SC030's historical identity may be read off `hay` and `strew`.

Every row is a positive witness. There is no row in the population whose only
support is downstream acceptance by the transducer; all eighteen have attested
Old English reflexes recorded in the corpus.

## 3. The literature on SC029

### 3.1 Campbell

Campbell §120.2 [@Campbell1959, p. 46] treats the whole context under West
Germanic consonant gemination:

> A similar development took place when u was doubled before j by the West Gmc.
> gemination of consonants (see § 407): auj > auuj > auj, and iuj > iuuj >
> iuuj. In OE the diphthongs are developed normally: au- > ēa- (cf. § 135),
> which was then mutated to ē- in nW-S, ie- in W-S by the following j.

His examples are exactly CAPR's witnesses and their relatives: Prim. Gmc.
\emph{*hauja-} > West Gmc. \emph{*hauuj} > OE \emph{hēg}, \emph{hīg} 'hay', and
likewise \emph{ēg}, \emph{ieg} 'island', \emph{cēgan}, \emph{ciegan} 'call',
\emph{strēgan} 'strew'.

Three things follow. The input to the Old English development is already
\emph{auj}, with a diphthong. The step CAPR calls SC029 is Campbell's
\emph{auuj} > \emph{auj}, which undoes the gemination. And the subsequent
development is explicitly the *ordinary* one, cross-referenced to §135.

### 3.2 Ringe and Taylor

Ringe and Taylor are more explicit still [@RingeTaylor2014, p. 53, §3.1.3]:

> When the preceding vowel was *a the usual OE outcome seems to reflect not
> *aw'w' but *auj, with *j surviving and the diphthong developing normally
> [...] But because gemination was not a merger, it involved no loss of
> contrasts, and did not alter underlying forms, it was reversible: a sequence
> of changes PNWGmc *awj > PWGmc *[aw'w'] > pre-OE *[auj] can have occurred,
> and I suggest that that is exactly what happened. This solution is in
> principle the same as that of Campbell 1962: 46, though we differ about the
> details.

"It was reversible" is the historical content of SC029. The change is a
reversion of a West Germanic gemination, dated by them to pre-OE.

Their derivations of the two CAPR witnesses [@RingeTaylor2014, p. 173] are:

> PGmc *hawja 'grass, hay' (Goth. hawi, ON hey) > PWGmc *hawi, *[haw'w'-] (OS
> hoi, OHG hewi, the inherited nom.-acc. sg., and houwi, with gemination
> levelled in from the oblique forms) > *hawi, *hauj- > *hæwi, *héaj- > WS OE
> hieg;
>
> PGmc *strawjaną 'to spread out' (Goth. straujan) > PWGmc *strawwjan (OHG
> gistrouwen 'to bestrew') > *straujan > *stréajan > Angl. OE strégan 'to
> strew'.

The `hay` derivation contains an internal control of real value. The same
etymon splits into \emph{*hawi}, where the following vowel is \emph{*i} and no
gemination occurred, and \emph{*haw'w'-} before \emph{*j}. The first branch
gives \emph{*hæwi} by ordinary brightening of a plain \emph{*a}; the second
gives \emph{*héaj-} through the diphthong. One paradigm therefore shows the
same fronting operating in both of its environments.

### 3.3 The dissenting account

Fulk denies that \emph{*w} ever geminated before \emph{*j}, holding that the
\emph{*u} was a glide throughout [@Fulk2018, §4.10 n. 1]. On that account there
is no gemination to reverse, and \emph{*auj} was simply always there.

CAPR's rule is deliberately neutral between the two accounts, since both
converge on \emph{*auj} as the pre-OE input. The dispute is nevertheless the
reason SC029's confidence stays at B; see section 8.

## 4. The literature on SC030

### 4.1 The change is brightening

Campbell reaches the point by way of relative chronology
[@Campbell1959, p. 52, §132]. Arguing about the order of \emph{*ā} > \emph{ǣ},
\emph{*ai} > \emph{ā} and \emph{*a} > \emph{æ}, he remarks parenthetically:

> (The normal development of Prim. Gmc. au to OE ēa, written éa, shows that the
> change a > æ would affect the first element of a diphthong.)

and then gives the ordered list:

> (1) West Gmc. ā > OE ǣ/ē [...]
> (2) West Gmc. ai > OE ā, by loss of the second element, accompanied by
> lengthening of the first.
> (3) West Gmc. a > OE æ; West Gmc. au > OE æu.

Plain \emph{*a} > \emph{æ} and \emph{*au} > \emph{æu} are one and the same
numbered step. Campbell does not present the diphthongal fronting as a separate
later change.

Fulk says it outright [@Fulk2018, p. 73, §4.12]. Having described the fronting
of \emph{a} to \emph{æ} as Anglo-Frisian Brightening, he continues:

> This fronting of a applied also to the diphthong au in OE, producing ēa, at
> first a diphthong with a rounded off-glide, as shown by early spellings, e.g.
> ⟨aeodbald⟩ (i.e. Eadbald, name) in Bede, with rounding persisting in late
> Northumbrian.

Ringe and Taylor supply the intermediate stage that CAPR encodes as `*aeu`
[@RingeTaylor2014, p. 172]:

> PWGmc *au appears in most dialects as ēa. It seems clear that *au was first
> tensed and fronted to æu, which is still attested occasionally in
> 8th-century documents; later the offglide was unrounded and lowered, and the
> spelling æa, which is also attested, was simplified to éa.

So SC030 is the fronting half of Anglo-Frisian brightening as it applies to a
diphthong, and CAPR's two-step SC030 plus SC032 is the reconstruction these
sources give.

### 4.2 The scope is English, not Anglo-Frisian

This is the one point on which SC030 and SC043 come apart, and the comparative
evidence is unambiguous. Fulk, immediately after the passage just quoted
[@Fulk2018, p. 73, §4.12]:

> There probably was no such fronting in the development of au in OFris., where
> it produces ā, before which there is no palatalization. Examples: OE ēac
> 'also', ēage 'eye', bēam 'tree' : OFris. āk, āge, bām (Go. áuk, áugō, OHG
> boum), but OE gēac 'cuckoo' (with palatal initial) : OFris. gāk.

Two independent arguments are present. The direct reflexes differ, Old English
\emph{ēac}, \emph{ēage}, \emph{bēam} against Old Frisian \emph{āk}, \emph{āge},
\emph{bām}. And there is a diagnostic from a later change: Old English
\emph{gēac} 'cuckoo' has a palatalized initial, which requires a front vowel to
have followed it, while Old Frisian \emph{gāk} has none.

Ringe and Taylor agree, adding "(OF hāw(a))", "(OF lāf)", "(OF rād)" and the
like to each of their examples and concluding "In this case too OF exhibits a
different outcome, namely ā" [@RingeTaylor2014, p. 172].

Brightening of plain \emph{*a} is shared with Old Frisian; brightening of the
first element of \emph{*au} is not. SC030 and SC043 are therefore the same
phonetic development with two different isoglosses, which is a positive reason
to keep them as separate registry rows.

The registry's existing `hist_stage` of `preoe` and `hist_scope` of
`english_specific` for SC030 are confirmed correct by this evidence. What was
wrong was the identity and the placement claim, not the stage or the scope.

## 5. Are SC029 and SC030 two changes?

Yes, on every account in the literature.

Ringe and Taylor separate them in the plainest possible way
[@RingeTaylor2014, p. 173]:

> It was noted in 3.1.3 that PWGmc *[-aww'-], which had developed from PGmc
> *-awj-, apparently became *[-auj-] at some point in pre-OE. These new *au
> also underwent the development to éa.

The word "also" carries the argument. The resolution of the geminate creates
new instances of \emph{*au}, and those new instances then undergo a change that
already existed and that applies overwhelmingly to inherited \emph{*au}. The
two operations have different inputs, different domains and different
comparative scopes: SC029 is about a West Germanic gemination and its
undoing, while SC030 is about the Old English treatment of a diphthong.

This also settles the SC029 to SC030 relation. It is genuine historical
feeding, attested in the sources' own ordered derivations
(\emph{*hauj-} > \emph{*héaj-}), and not merely an artefact of the transducer.

## 6. Do geminate and singleton *wj belong to the same change?

**Resolved by the follow-up repair.** See
`audits/sc010-w-gemination-and-hay-depth-adjudication.md`. The account below
records what this adjudication found; the repair has since removed the
inconsistency it describes.

At the time of this adjudication CAPR's two witnesses were reconstructed at
different depths.

- `hay` carried \emph{*xáwwją} with a geminate. Ringe and Taylor give PGmc
  \emph{*hawja} with a single \emph{*w}, and Gothic \emph{hawi} and Old Norse
  \emph{hey} both show a single \emph{*w} [@RingeTaylor2014, p. 53; p. 173].
  The gemination is a West Germanic development, so a geminate in a
  Proto-Germanic protoform slot was an anachronism.
- `strew` carried \emph{*stráwjaną} with a single \emph{*w}, which matches
  Ringe and Taylor's Proto-Germanic form exactly.

Meanwhile CAPR's own `PWGmcJGemination` geminated thirteen consonants before
\emph{*j} and excluded \emph{*w}, which is Fulk's position.

The corpus therefore asserted the gemination lexically for `hay`, denied it in
the rule inventory, and denied it lexically for `strew`. The four-branch shape
of SC029 existed to absorb that inconsistency. The geminate branch and the
singleton branch were **not** two historical mechanisms.

The repair adopted the Ringe-Taylor and Campbell account throughout: `hay` now
enters as \emph{*xáwją}, SC010 supplies the West Germanic geminate for both
witnesses, and the two singleton branches of SC029 were removed as
unwitnessed. Campbell §407 p. 167 is decisive that \emph{*w} is an ordinary
member of the gemination law, "every consonant except r being affected after
short syllables". SC029's input is now always the geminate.

## 7. Relation to SC043 Anglo-Frisian brightening

The registry asserted that SC029 and SC030 execute before SC043 but belong
historically after it. Both halves of that are wrong.

**Did ordinary brightening affect the a of *awj?** The question is malformed for
the pre-OE stage. By the time brightening applies there is no plain \emph{*a}
in these forms; SC029 has already made the sequence a diphthong. The \emph{*a}
is fronted, but as the first element of \emph{*au}, which is SC030. Ringe and
Taylor's \emph{*hæwi} beside \emph{*héaj-} shows both routes in one paradigm
(section 3.2).

**Does SC029 necessarily follow brightening?** No. Nothing requires it, and
nothing forbids it. The two have disjoint inputs.

**Does SC030 necessarily follow brightening?** No. SC030 *is* brightening,
applied to a diphthong. Campbell's step (3) contains both.

**Do the sources give an actual chronology?** They give compatible stages rather
than a demonstrated interval. Campbell bundles the two in one numbered step;
Fulk presents them in one sentence as one fronting; Ringe and Taylor treat them
in adjacent sections. No source separates them in time.

**Machine evidence for disjointness.** `EAFBrightening` was compiled on its own
and applied to test strings. It leaves \emph{*áu} untouched and fronts plain
\emph{*á} correctly:

```
*x*áu*j*ą       ->  *x*áu*j*ą
*l*áu*b*ą       ->  *l*áu*b*ą
*s*t*r*áu*j*a   ->  *s*t*r*áu*j*a
*d*á*g*a        ->  *d*æ*g*a
```

The reason is structural. Every element of `EnglishStarConsonant` begins with
`*`, and the segment following `*á` inside `*áu` is a bare `u`, so no clause of
`EAFBrightening` can find its context inside the digraph. SC030 and SC043 are
provably non-interacting, and their executable order is free.

**Consequence for placement.** SC029 and SC030 execute immediately after SC004
`EAFAiMonophthongization`. That is Campbell's step (2) followed by his step
(3), in his order [@Campbell1959, p. 52, §132]. The current placement is not
merely tolerable; it reproduces the relative chronology of the source.

The verdict is therefore RETAIN, with no reorder, and the corridor
re-evaluation that the registry anticipated is not needed. The old
`chronology_problem` text and the `possible_fst_reorder_later` action status are
retracted as resting on a misidentification of SC030.

## 8. Relation to SC032

Bounded question only; SC032 is not adjudicated here.

The historical relation is real. Ringe and Taylor's "*au was first tensed and
fronted to æu [...] later the offglide was unrounded and lowered"
[@RingeTaylor2014, p. 172] is an explicit sequence, and the second step cannot
precede the first because it operates on a segment the first step creates.
SC030 feeds SC032 historically.

The *executable* evidence recorded for the relation is a different matter and
must not be promoted. Displacing SC030 after SC032 yields eighteen rows with no
output. That happens because `*aeu` is an internal symbol with no surface
realization: if SC032 runs first there is nothing for it to consume, and the
`*aeu` that SC030 then creates survives to the surface and is rejected. The
failure demonstrates that `*aeu` is a non-surface intermediate. It does not
independently demonstrate a historical interval. The historical direction is
established by the source, and the edge notes now say so.

One observation is recorded without acting on it. SC032 is registered as
`ws_oe` / `west_saxon`, but the \emph{*æu} > \emph{ēa} clause within it is
general Old English [@Campbell1959, p. 53, §135; @RingeTaylor2014, p. 172],
whereas the West Saxon element in SC032 is the merger of \emph{iu} and
\emph{eo}. That is a question for a future SC032 adjudication.

## 9. Hypotheses compared

| # | Hypothesis | Verdict |
|---|---|---|
| A | Current two-change architecture essentially correct | **Partly.** Two changes, correct stage and scope, but both identities misdescribed and the placement claim false. |
| B | SC029 correct, SC030 historically misidentified | **Closest to the truth,** except that SC029 is misidentified too. |
| C | SC030 belongs to Anglo-Frisian brightening | **Accepted as to identity, rejected as to merger.** It is brightening, but its isogloss is narrower, so the rows stay separate. |
| D | SC029 itself contains several historical mechanisms | **Rejected.** The four branches reflect reconstruction depth, not mechanism (section 6). |
| E | SC029 and SC030 are two operations implementing one development | **Rejected.** Ringe and Taylor's "these new *au also underwent" separates them, and inherited \emph{*au} dominates SC030's population. |
| F | Identities sound, executable placement wrong | **Rejected.** The placement is right and the identities were wrong, which is the reverse. |
| G | Historical placement sound, "post-brightening" assumption wrong | **Accepted.** This is the operative result for the cascade. |

## 10. Stage, scope and confidence

| | SC029 | SC030 |
|---|---|---|
| hist_stage | `preoe` (unchanged) | `preoe` (unchanged) |
| hist_scope | `english_specific` (unchanged) | `english_specific` (unchanged) |
| confidence | B (unchanged, new reason) | A (raised from B) |

SC029's scope is confirmed by the West Germanic comparanda, which retain the
geminate: OHG \emph{houwi}, \emph{gistrouwen}, OS \emph{hoi}
[@RingeTaylor2014, p. 173]. The resolution to \emph{*auj} is English.

SC029 keeps B, and the dimensions differ sharply. That \emph{*auj} was the
pre-OE input is secure and would rate A on its own, since both camps converge
on it and the Old English reflexes require it. That a discrete *change* took
place is not secure, because it holds only on the gemination account; on Fulk's
account \emph{*auj} was there from the start and nothing happened. Luick's own
verdict on the gemination story, quoted in the rule comment, is "wahrscheinlich
aber nicht strikte zu erweisen". The B summarizes the mechanism dispute, not
any doubt about the input or the domain.

SC030 is raised to A. Its existence, its domain, its stage and its scope are
each independently secure: three handbooks state the change in the same terms
[@Campbell1959, p. 52, §132; @Fulk2018, p. 73, §4.12; @RingeTaylor2014, p. 172],
the Old Frisian reflexes and the \emph{gēac} palatalization diagnostic fix the
scope, and sixteen inherited-\emph{*au} witnesses in the corpus confirm the
domain. The one residual uncertainty is not about SC030 at all. It is whether
the split between SC030 and SC032 falls at exactly the point the sources
intend, since Fulk collapses \emph{au} > \emph{ēa} into one step while Campbell
and Ringe and Taylor give the \emph{æu} intermediate. CAPR follows the latter
two, and that uncertainty belongs to SC032.

## 11. Deferred work

1. **Foma identifier renames.** `OEAwjGlideFormation` is now a misnomer twice
   over, since the change is not glide formation and the glide is being made
   vocalic. `OEAuFronting` is accurate but understates the identification with
   brightening. This commit changes rule metadata and prose, so the
   behaviour-neutral rename gate cannot be satisfied here. Both renames are
   deferred to an isolated pass.

2. **`hay` protoform depth. Now discharged.** \emph{*xáwwją} encoded a West
   Germanic geminate in a Proto-Germanic slot (section 6). The follow-up
   adopted the Campbell and Ringe-Taylor position against Fulk's: `hay` now
   enters as \emph{*xáwją} and `PWGmcJGemination` geminates \emph{*w} before
   \emph{*j}. See
   `audits/sc010-w-gemination-and-hay-depth-adjudication.md`.

3. **SC032 scope.** Recorded in section 8.

4. **Bibliography defect, unrelated to these changes.** `docs/refs.bib` entry
   `Hogg1992` is titled "A Grammar of Old English. Volume 1: Phonology" but its
   `file` field points at `docs/references/hogg_vol1.txt`, which is *The
   Cambridge History of the English Language*, volume 1, edited by Hogg. The key
   is currently uncited in the Germanic documents, so nothing is misattributed
   today. Hogg's chapter in that volume corroborates section 4.1 at p. 101,
   where he gives \emph{au} > \emph{æu} and lists \emph{æu} in the post-fronting
   vowel system, but it is not cited in the reader prose until the entry is
   fixed.

5. **Citation defect, corrected here.** The reader chapter cited
   `[@RingeTaylor2014, p. 188]`. CAPR cites Ringe and Taylor by printed page,
   and 188 is the PDF sheet for printed page 173. Corrected to the printed
   pages 53, 172 and 173.

## 12. Corpus effect

No new lexeme was added. The corpus already contains a geminate witness, a
singleton witness and sixteen independent inherited-\emph{*au} witnesses, which
covers every distinction the adjudication needed. Adding vocabulary would have
padded the count without testing anything new.

No Foma rule was changed and no rule was moved by this adjudication, so it
produced no derivation changes. The follow-up repair recorded in
`audits/sc010-w-gemination-and-hay-depth-adjudication.md` subsequently
corrected `hay`'s protoform and added the \emph{*w} branch of SC010. That
changed the corpus and rule fingerprints and made SC010 fire for `hay` and
`strew`, but left every Old English surface output unchanged.

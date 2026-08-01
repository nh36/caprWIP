# Audit: Evidential Uses of *Family* in Historical Chapters

**Branch:** `family-evidence-audit`
**Scope:** Reader-facing Part I chapter files (`Germanic/docs/sound_changes/reader_facing/*.md`, excluding generated section files), supporting literature dossiers, staging documents, and assembly-layer introduction files.
**Status:** Second-pass audit. Sources inspected and reconciled. No manuscript files changed.

---

## 1. Problem Statement

The word *family* appears in the reader-facing chapters and supporting documents to mean several structurally different things:

1. **Single cognate set**: one inherited etymon whose reflexes survive in multiple branches (*friend*, *heofon*).
2. **Multiple independent etyma** sharing a sound change (*field/fold/gold/wold* for SC012).
3. **One morphological paradigm or set of inflectional endings** (*shoulder* for SC005).
4. **A small multi-item set spanning different grammatical categories** (*four* + pronominal forms for SC008).
5. **CAPR ordering witness only**: a word that provides a chronological constraint but is not itself the primary comparative evidence for the sound law.
6. **Genealogical label**: the Germanic *language* family — not an evidential claim.

Configurations 3 and 5 are the most misleading. SC005 (*shoulder*) is the clearest case: the word "shoulder" functions solely as a CAPR ordering witness; the comparative evidence for the sound change consists entirely of inflectional endings. Calling it "the `shoulder` family" implies that the comparative base is a group of cognate forms of the word 'shoulder', which is false.

SC008 (*four*) is less misleading but still incomplete: the current phrasing foregrounds one numeral while the evidence for one of the two input clusters (*zw*) comes from pronominal case forms — two case cells of a single pronominal paradigm, not two independent etyma.

---

## 2. Complete Occurrence Inventory

Scope: `Germanic/docs/sound_changes/reader_facing/*.md` (excluding generated `reader_facing_local_section_*.md`), `Germanic/docs/assembly/capr_book_intro_alpha_01.md`, `Germanic/docs/assembly/section_introductions_draft.md`.

Supporting staging documents included: `reader_facing_sc005_009_012_inclusion_01_report.md`, `reader_facing_chronology_confidence_audit_01.md`, `reader_facing_pilot_02.md`, `README.md`.

| # | Location | Current label | Evidential structure | Evidence sufficient? | Scale |
|---|----------|--------------|---------------------|---------------------|-------|
| 1 | `005-unstressed-a-raising-before-final-m.md:18` | "the `shoulder` family…tests the chronology" | CAPR ordering witness; the sound law is supported by inflectional endings, not shoulder cognates | Partly: needs explicit statement | One sentence |
| 2 | `007-final-o-lowering-before-r.md:5` | "the families behind *fēower* 'four' and *wæter* 'water'" | Two independent single cognate sets (numerals/nouns) | Yes, with minor clarification | Terminology only |
| 3 | `007-final-o-lowering-before-r.md:20` | "*fēower* 'four' and *wæter* 'water' families" | Two independent single cognate sets | Yes, with minor clarification | Terminology only |
| 4 | `008-coronal-w-assimilation.md:5` | "the `four` family and plural-pronominal forms" | Composite: one numeral (*dw*) + one pronominal paradigm two case forms (*zw*); R&T note one example of each cluster | Partly: "four family" obscures that pronouns are the evidence for *zw*; "two pronouns" overstates independence | One sentence |
| 5 | `009-ij-contraction-in-friend.md:5` | "a change…in the `friend` family" | Single cognate set; R&T explicitly restrict generalization; Luick's page-118 discussion involves related lexemes not identical in environment | Yes: limitation stated; could be made structurally explicit | Terminology only |
| 6 | `009-ij-contraction-in-friend.md:7` | "confined to the `friend` family" | Same | Yes | Pass |
| 7 | `009-ij-contraction-in-friend.md:18` | "Only the `friend` family tests this contraction" | Same | Yes | Pass |
| 8 | `009-ij-contraction-in-friend.md:20` | "beyond this family" | Same | Yes | Pass |
| 9 | `012-lth-voicing.md:18` | "The `field`, `fold`, `gold`, and `wold` families" | Four independent etyma preserving the same development | Yes; each is a separate word | Terminology only |
| 10 | `013-dental-hardening.md:8` | "extends beyond any one lexical family" | Negative comparative statement; not an evidential claim | Yes (negative use) | Pass |
| 11 | `021-unstressed-o-raising.md:5` | "the same family" (heofon/heaven) | Single cognate set (OE *heofon*, OS *heban*, NWGmc *\*hebun*) | Yes | Terminology only |
| 12 | `064-065-post-apocope-tail.md:6` | "inherited *furht-* family" | Single root (*\*prk-to-*) with multiple derived forms | Yes | Terminology only |
| 13 | `064-065-post-apocope-tail.md:20` | "family behind *fyrhte* 'fright'" | Same | Yes | Terminology only |
| 14 | `064-065-post-apocope-tail.md:30` | "depend upon one lexical family" | Explicit acknowledgment of narrow base | Yes | Pass |
| 15 | `chap1-pgmc-to-pnwgmc-intro.md:7` | "rest of the Germanic family" | Genealogical language family | — (genealogical, not evidential) | Pass |
| 16 | `chap1-pgmc-to-pnwgmc-intro.md:34` | "two lexical families: *draugma-* and *taugma-*" | Two distinct etyma (SC002) | Yes: exemplary use | Pass |
| 17 | `chap1-pgmc-to-pnwgmc-intro.md:43` | "visible across the Germanic family" | Genealogical | — | Pass |
| 18 | `README.md:276` | "`friend` family" | Build/tech documentation reference | — (non-manuscript) | Pass |
| 19 | `reader_facing_sc005_009_012_inclusion_01_report.md:28` | "friend family alone" | Internal staging note; correctly identifies the narrow base | — (staging doc) | Pass |
| 20 | `reader_facing_chronology_confidence_audit_01.md:20` | "*ij*-contraction in *friend*" | Staging audit reference | — | Pass |
| 21 | `reader_facing_pilot_02.md:646` | "does not create a large family of lexical breakpoints" | Negative comparative statement re SC011-area | — (pilot) | Pass |
| 22 | `reader_facing_broad_window_chronology_review_01.md:91` | "`fright` family" | Review document reference | — | Pass |
| 23 | `reader_facing_one_direction_chronology_review_01.md:99` | (no substantive "family" claim) | Staging | — | Pass |

**Summary of audit-relevant occurrences:** Items 1 (shoulder, SC005), 4 (four, SC008), and 5–8 (friend, SC009) require attention. Items 2–3, 9, 11–14 are correct in substance but could be clarified. Items 10, 14–17, 19–23 are acceptable or non-manuscript.

---

## 3. Three Mandatory Deep Dives

### 3.1 SC009: *ij*-contraction in *friend*

#### 3.1.1 Identification

| Field | Value |
|---|---|
| Sound-change ID | SC009 |
| Rule name | `PWGmcIjContraction` |
| Chapter | `009-ij-contraction-in-friend.md` |
| Literature dossier | `Germanic/docs/sound_changes/literature_dossiers/009-pwgmc-ij-contraction.dossier.md` |
| Current label | "`friend` family" |

Current sentence (line 5):
> "Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc *\*frijond-* > PWGmc *friund* 'friend' > OE *frēond* 'friend'."

#### 3.1.2 Citation mismatch: Luick "§118" resolved

R&T cite "Luick 1914-40: 118" for SC009. This is a **page reference to printed page 118** of Luick's *Historische Grammatik der englischen Sprache*, not to section §118.

Evidence: In the OCR at `docs/references/luick_historische_grammatik.txt`, the scan-page marker `--- PAGE 166 ---` is immediately followed by the running header "118 / Lautgeschichte. I A. Die betonten Sonanten bis ins 11. Jh." — confirming that scan page 166 = printed page 118. The discussion on that page is Luick **§102** (section number, not page number), which treats the relevant *-iju-* contraction. The OCR section marked `§118` (at scan page 178 = printed page 130) concerns Anglo-Frisian brightening of *\*ā* and is entirely unrelated to SC009.

**[Source statement]** The R&T citation "Luick 1914-40: 118" is a standard page citation and refers correctly to the Luick §102 discussion.

**[Source statement]** The OCR `§118` (Anglo-Frisian brightening) is a different section on a different printed page and has no bearing on SC009. Previous audit entries treating this as evidence of a "citation mismatch" were mistaken.

#### 3.1.3 What Luick §102 (printed page 118) actually says

**[Source statement]** Luick §102 (`docs/references/luick_historische_grammatik.txt`, lines 6964–6993, scan pages 166–167, printed pages 118–119):

Luick derives WGmc *iu* in several environments:
1. By transfer of the ending *-u*: WGmc/OS *siu* 'she', *þius* 'this', *\*hiu* 'she'.
2. When *u* fell before following *u*: WGmc/OHG *niun* 'nine'.
3. "durch Schwund des j in der Folge -iju-" (by loss of *j* in the sequence *-iju-*): WGmc/OS *driu* neut. 'three'.

For the third environment, Luick explicitly names: **\*frijōnd-** 'Freund', **\*fijand-** 'Feind', **\*frija-** 'frei', **\*blija-** 'Farbe'. He states that *iu* was then "verallgemeinert" (generalized) within these paradigms: WGmc *friund* for 'friend' (OE/OS), WGmc *fiund* 'fiend' (OE/OS only), OE *\*bliu* 'colour' (OE only), OE *friu* (before front vowels in OE).

#### 3.1.4 Classifying Luick's additional forms

The key question is whether *fijand-*, *frija-*, and *blija-* constitute **additional independent lexical witnesses** to stressed *\*ijo > \*iu* in the same sense as *frijōnd-*.

They do not. The analysis is as follows:

**\*fijand- 'fiend'**: The sequence that produced *iu* is the oblique case forms of a *nd*-participial stem where the stem had *\*ij*. The underlying sequence is morphologically parallel to *\*frijōnd-* but not phonologically identical. Luick specifies that *iu* arose in "some cases" of these stems and was then generalized. **[Auditor inference from source structure]** The process is analogical generalization within the paradigm, not repeated application of a phonological rule to an identical input string. Both *frijōnd-* and *fijand-* have *j* in the stem, but the vowel preceding *j* differs (the key distinction R&T draw is the "stressed *\*i*" in *\*frijōnd-*).

**\*frija- 'free'**: An adjective stem. Luick notes that *friu* appears "in OE before front vowels" (e.g., gen. *frīzes*), suggesting the development is part of a larger paradigmatic adjustment in contact with front vowels — not the same phenomenon as *frijōnd-*.

**\*blija- 'colour'**: OE only; Luick explicitly flags this as restricted (*"nur im Altenglischen"*). This is the weakest witness.

**[Source statement — R&T]**: "the uniqueness of the sequence *ijo (with stressed *i*) makes it inadvisable to attempt any generalizations based on the history of this word" (R&T vol.2 p.62, lines 4226–4228).

**Reconciliation**: Luick and R&T are not contradictory but focus on different phenomena. Luick describes a broader West Germanic development involving several stems where *-iju-* sequences arose and *iu* was generalized. R&T are making a narrower claim: the specific sequence *\*ijo* with stressed *\*i* followed by *j* followed by *\*ō* — the exact phonological environment in *\*frij-ōnd-* — is unique. The other Luick forms (*\*fijand-*, *\*frija-*) involve unstressed or differently conditioned *j*-adjacent vowels and are not identical phonological environments. Luick is documenting the paradigmatic spread of *iu*; R&T are restricting the phonological generalization.

#### 3.1.5 Evidential Classification

- **Single cognate set across languages** — primary classification.
- **CAPR chronological witness** — secondary: the derivation places SC009 before SC032 (OE Diphthong Leveling).

The evidence consists of one inherited etymon, PGmc *\*frijond-*, whose reflexes survive in multiple West Germanic branches. Luick's additional items (*\*fijand-*, *\*frija-*, *\*blija-*) illustrate the paradigmatic generalization of *iu* within stems containing *j*, but none constitutes an **independent parallel example of stressed \*ijo > \*iu throughout WGmc in the same environment as \*frijōnd-**. R&T's restriction is correct.

#### 3.1.6 Comparative Evidence

| Input | Language/Stage | Form | Gloss | Status | Source |
|---|---|---|---|---|---|
| PGmc *\*frijond-* | Gothic | *frijonds* | 'friend' | Conservative (no *ij*-contraction) | R&T vol.2 p.62, l.4220 |
| PWGmc *\*friund* | Old English | *frīond, frēond* | 'friend' | Innovative (*\*ij > \*iu*) | R&T vol.2 p.62, l.4221 |
| PWGmc *\*friund* | Old Frisian | *frīund* | 'friend' | Innovative | R&T vol.2 p.62, l.4221 |
| PWGmc *\*friund* | Old Saxon | *friund* | 'friend' | Innovative | R&T vol.2 p.62, l.4221 |
| PWGmc *\*friund* | Old High German | *friunt* | 'friend' | Innovative | R&T vol.2 p.62, l.4221 |
| PGmc *\*fijand-* | WGmc (OE/OS) | *fiund* (OE/OS) | 'fiend, enemy' | Parallel generalization of *iu* in paradigm; not identical phonological environment | Luick §102, l.6969–6975 |
| PGmc *\*frija-* | OE | *friu* (before front V) | 'free' | Restricted OE paradigmatic form; not WGmc-wide | Luick §102, l.6972–6975 |
| PGmc *\*blija-* | OE only | *\*bliu* | 'colour' | OE only; paradigmatic | Luick §102, l.6971 |

**Source locator (primary):** R&T vol.2 p.62 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 4217–4228.
**Source locator (Luick):** `docs/references/luick_historische_grammatik.txt`, lines 6964–6993 (scan pages 166–167, printed pages 118–119; section §102).

#### 3.1.7 Argument

**What the comparative evidence establishes:**
The reflexes of PGmc *\*frijond-* demonstrate that the *\*ijo* sequence was simplified to *\*iu* in Proto-West Germanic. Gothic *frijonds* preserves the earlier form and confirms the development is a WGmc innovation. The evidence is geographically wide (all four major WGmc branches) but etymologically narrow (one inherited word). Luick's additional items confirm that paradigmatic *iu* generalization occurred in several *j*-stem formations, but in different phonological environments from the *\*ijo* sequence that is unique to *\*frijōnd-*.

**What the CAPR derivation establishes:**
The derivation of OE *frēond* from PGmc *\*fríjōndz* places SC009 before SC032 (OEDiphthongLeveling). Without contraction before leveling, the intermediate form *\*friund* would be caught by the leveling rule. This ordering relation is specific to this one lexical item.

**What the evidence does not establish:**
- A second, etymologically independent etymon showing the identical *\*ijo* > *\*iu* development throughout WGmc.
- A productive rule for stressed *\*ijo*.
- Any broader scope beyond the 'friend' etymon for the R&T-formulated change.

R&T themselves declare: "the uniqueness of the sequence *ijo (with stressed *i*) makes it inadvisable to attempt any generalizations based on the history of this word."

#### 3.1.8 Source Assessment

- Primary source: `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 4217–4231 (p.62).
- Luick source: `docs/references/luick_historische_grammatik.txt`, lines 6964–6993, scan pages 166–167, **printed pages 118–119**, section **§102** (not §118).
- R&T's "Luick 1914-40: 118" is a page citation; it correctly refers to Luick §102. There is no citation error.
- Repository sources are now sufficient for the SC009 analysis.
- The *additional* Luick items (*fijand*, *frija*, *blija*) confirm paradigmatic generalization but do not constitute independent witnesses to the narrow SC009 environment. R&T's restriction stands.

#### 3.1.9 Status

`ready for reader-facing revision`

#### 3.1.10 Editorial Recommendation

The current chapter prose is correct: the restriction is stated. The improvement is to name the actual forms:

**Current:**
> "Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc *\*frijond-* > PWGmc *friund* 'friend' > OE *frēond* 'friend'."

**Proposed:**
> "Ringe and Taylor describe a change of *\*ijo* to *\*iu* in the ancestor of *friend*, with the pathway PGmc *\*frijond-* (Gothic *frijonds*) > PWGmc *\*friund* > OE *frēond*, Old Frisian *frīund*, Old Saxon *friund*, Old High German *friunt* [@RingeTaylor2014, p. 62]."

**Scale:** One-sentence insertion of comparative forms; terminology clean-up; no restructuring needed.

---

### 3.2 SC005: Unstressed *\*a*-raising before final *\*m*

#### 3.2.1 Identification

| Field | Value |
|---|---|
| Sound-change ID | SC005 |
| Rule name | `NWGmcAToUBeforeM` |
| Chapter | `005-unstressed-a-raising-before-final-m.md` |
| Literature dossier | `Germanic/docs/sound_changes/literature_dossiers/005-nwgmc-a-to-u-before-m.dossier.md` |
| Current label | "the `shoulder` family" |

#### 3.2.2 Evidential Classification

- **Several morphological categories sharing an ending** — primary classification for the comparative evidence.
- **CAPR chronological witness only** — the word 'shoulder' provides an ordering constraint (SC005 must precede SC017 NWGmcULowering); it is not itself part of the comparative evidence.

#### 3.2.3 Comparative Evidence

**Source:** R&T vol.2 pp.17–18 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 1785–1835.

| Input form | Language(s) | Form | Gloss | Morphological category | Status | Source |
|---|---|---|---|---|---|---|
| PGmc *\*dagamaz/*-miz | ON/OE/OS/OHG | *dogum/dagum/dagun/tagum* | 'days' (dat.pl.) | a-stem dat.(inst.) pl. | Innovative: *\*a > \*u* before *m* | R&T vol.2 p.17, l.1786–1791 |
| PGmc *\*godammai* | ON/OE/OS | *godum/godum/godum(u)* | 'good' (dat.sg. masc./neut.) | Strong adj. dat.sg. | Innovative | R&T vol.2 p.17, l.1792–1798 |
| PGmc *\*beramaz* | ON/OHG | *berum/berumés* | 'we carry' | 1pl. present indicative | Innovative | R&T vol.2 p.17, l.1799–1806 |
| Gothic | Gothic (conservative) | *-amma* (sg. adj.) | — | Strong adj. dat.sg. | Conservative (*\*-am-*) | R&T vol.2 p.17 |

**CAPR ordering witness — shoulder:**
OE *sċuldrum* 'shoulders' exposes the feeding relation SC005 → SC017. If SC017 (NWGmcULowering) precedes SC005, the intermediate *\*a* in *\*skúldramiz* 'shoulders' becomes *\*o* through lowering before it can be raised to *\*u* through SC005, yielding wrong *\*sċoldrum*.

#### 3.2.4 Argument

**What the comparative evidence establishes:** Three morphological categories (dat.pl., dat.sg. adj., 1pl. verb) across NWGmc branches demonstrate a regular raising of unstressed *\*a* to *\*u* before *\*m*. Gothic preserves conservative forms.

**What the CAPR derivation establishes:** The ordering SC005 before SC017.

**What the evidence does not establish:** That 'shoulder' cognates are part of the comparative argument. Shoulder is incidental — the right structure to create an ordering constraint with SC017.

#### 3.2.5 Source Assessment

- Primary source: R&T vol.2 pp.17–18 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 1785–1835. Repository evidence sufficient.
- Current chapter correctly identifies inflectional endings as the comparative base, but the "shoulder family" label contradicts this.

#### 3.2.6 Status

`ready for reader-facing revision`

#### 3.2.7 Editorial Recommendation

**Proposed revision:**
> "The CAPR derivation of *sċuldrum* 'shoulders' tests the chronology: if [SC017 NWGmcULowering] applies before this rule, PGmc *\*skúldramiz* 'shoulders' yields *\*sċoldrum* rather than expected OE *sċuldrum* 'shoulders'. The inflectional evidence — the a-stem dat.pl., strong-adjective dat.sg., and 1pl. present forms uniformly showing *-um* across ON, OE, OS, and OHG — justifies restricting the change to noninitial unstressed material before *\*m*."

**Scale:** One-sentence clarification; no structural change.

---

### 3.3 SC008: Assimilation of coronal consonants before *\*w*

#### 3.3.1 Identification

| Field | Value |
|---|---|
| Sound-change ID | SC008 |
| Rule name | `PWGmcCoronalWAssimilation` |
| Chapter | `008-coronal-w-assimilation.md` |
| Literature dossier | `Germanic/docs/sound_changes/literature_dossiers/008-pwgmc-coronal-w-assimilation.dossier.md` |
| Current label | "the `four` family and plural-pronominal forms" |

#### 3.3.2 What Stiles actually says about the pronoun evidence

Stiles NOWELE 6 §1.3.3, pp.91–92 (original PDF `docs/references/stiles_1985_four_part1_nowele6.pdf`, in Git history at commit `11c20529`, later untracked in `971d1d88`; no tracked text extract exists in current checkout):

**[Source statement — Stiles §1.3.3]:** "there is also the supporting evidence of the parallel development of the sequence *-zw-, which is generally acknowledged to yield WGmc. *-ww- in **the oblique cases of the second person plural pronoun**."

He then gives: "Go. acc., dat. *izwis* → OE *eow*, OFr. *iu*, OS *iu*, OHG *iu*; Go. gen. *izwara* → OE *eower*, OFr. *iuwer*, OS *euwar*, OHG *iuwer*."

The pronoun forms *izwis* and *izwara* are **two case cells of a single pronominal paradigm** (acc./dat. sg. and gen. sg. of the 2nd-person plural pronoun), not two independent etyma. Stiles treats them together as "the second person plural pronoun" and uses the plural *oblique cases* to describe both.

**[Source statement — R&T]:** R&T list them as separate numbered items (lines 3114–3118) but state: "There is really only one example of each input cluster" (l.3106). For *\*zw*, R&T present *izwiz* and *izweraz* as the evidence — these are the acc./dat. and gen. forms of the same pronoun, not independent formations. R&T's "one example" of the *\*zw* cluster is the pronominal paradigm as a whole, not two independent etyma.

#### 3.3.3 Corrected Evidential Classification

- **Cross-category small set** — one numeral for *\*dw*, one pronominal paradigm for *\*zw*.
- **NOT "three etymologically independent items"** — the prior audit classification was wrong on this point.

The correct classification is:
- One numeral (*\*fedwor* 'four') providing the sole secure *\*dw* example.
- One second-person plural pronominal paradigm (*\*iz-wiz/\*iz-weraz*), supplying two related case forms as evidence for *\*zw*. These forms are paradigmatically related, not independent etyma.

#### 3.3.4 Comparative Evidence

**Primary source:** R&T vol.2 pp.56–57 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 3104–3158. Key passage (l.3105–3108): "the intervocalic sequences *zw and *dw were assimilated to *ww (Stiles 1985-6, NOWELE 6: 89-94). There is really only one example of each input cluster, but the basic nature of the lexemes involved makes the change virtually certain."

*\*dw* cluster:

| Input | Language | Form | Gloss | Status | Source |
|---|---|---|---|---|---|
| PGmc *\*fedwor* | Gothic | *fidwor* | 'four' | Conservative (*\*dw* preserved) | R&T l.3110 |
| PWGmc *\*feuwar* | Old English | *fēower* | 'four' | Innovative | R&T l.3111 |
| PWGmc *\*feuwar* | Old Frisian | *fiuwer* | 'four' | Innovative | R&T l.3111 |
| PWGmc *\*feuwar* | Old Saxon | *fiuwar* | 'four' | Innovative | R&T l.3111 |
| OHG *fior* | Old High German | *fior* | 'four' | Innovative (secondary via ordinal) | R&T l.3112 |

*\*zw* cluster — single pronominal paradigm, two case cells:

| Input | Language | Form | Gloss | Paradigm cell | Status | Source |
|---|---|---|---|---|---|---|
| PGmc *\*izwiz* | Gothic | *izwis* | 'you (acc./dat.pl.)' | 2pl.pron. acc./dat. | Conservative | R&T l.3114; Stiles §1.3.3 |
| PWGmc *\*iuwi/\*iuw* | OE/OFris/OS/OHG | *eow/iu/iu/iu* | 'you (acc./dat.pl.)' | 2pl.pron. acc./dat. | Innovative | R&T l.3114–3115 |
| PGmc *\*izweraz* | Gothic | *izwar* | 'your (gen.pl.)' | 2pl.pron. gen. | Conservative | R&T l.3117; Stiles §1.3.3 |
| PWGmc *\*iuwar* | OE/OFris/OS/OHG | *eower/iuwer/euwar/iuwer* | 'your (gen.pl.)' | 2pl.pron. gen. | Innovative | R&T l.3117–3118 |

**Apparent counterexamples (Stiles pp.92–94):** The wa/wo-stem nouns (*\*gaiðwa-* 'lack', *\*skaðwa-* 'shade', possible *\*kcwiðwa-* 'cud'; wo-stems *\*mēðwō-* 'meadow', *\*baðwō-* 'battle') would have provided *\*-dw-* environments but do not show the assimilation. Stiles discusses these at length (pp.92–94) and offers tentative explanations (some may have been u-stems; some rebuilt before the change; possible Sievers' Law effect for heavy syllables). **[Source statement — Stiles p.94]:** "I must confess, therefore, that I am not wholly sure how these exceptions are to be explained, though I am sure that the development posited for '4' is phonological."

#### 3.3.5 Argument

**What the comparative evidence establishes:**
One numeral (*four*) and one pronominal paradigm supply the sole direct evidence for the *\*dw > \*ww* and *\*zw > \*ww* assimilations respectively. Gothic conservative forms confirm the innovations are WGmc. R&T and Stiles are confident the change is real despite the limited data, because of the fundamental nature of the vocabulary and the independent parallel of the two clusters.

**What the CAPR derivation establishes:**
OE *fēower* exposes the feeding relation SC008 → SC031 (OEWWSimplification). The pronouns do not supply the same ordering constraint; the numeral alone drives it.

**What the evidence does not establish:**
- The pronominal evidence is **not** two independent etyma; it is two case forms of one paradigm.
- More than one independent *\*dw* example.
- Resolution of the wa/wo-stem counterexamples — Stiles leaves these tentative.

#### 3.3.6 Source Assessment

- Primary source: R&T vol.2 pp.56–57 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 3104–3158.
- Stiles source: original PDF `docs/references/stiles_1985_four_part1_nowele6.pdf`, Git blob at commit `11c20529`, journal pp.89–94. **No tracked text extract in current checkout.** Original PDF present in Git history; pdftotext extraction performed for this analysis.
- The Stiles §1.3.3 language "the oblique cases of the second person plural pronoun" is decisive: this treats both pronominal case forms as members of one paradigm.
- Repository evidence is sufficient for the corrected classification.

#### 3.3.7 Status

`ready for reader-facing revision`

#### 3.3.8 Editorial Recommendation

**Proposed revision:**
> "Ringe and Taylor treat the assimilation of *\*dw* and *\*zw* to *\*ww* as a shared Proto-West-Germanic innovation, supporting it with one example of each cluster: the numeral *\*fedwor* 'four' (Gothic *fidwor* vs. OE *fēower*) for *\*dw*, and the oblique case forms of the second-person plural pronoun (Gothic *izwis* acc./dat. vs. OE *eow*; Gothic *izwar* gen. vs. OE *eower*) for *\*zw* [@RingeTaylor2014, pp. 56–57]."

**Scale:** One-sentence clarification; removes "four family"; makes the two-cluster structure and pronoun relationship explicit.

---

## 4. Shorter Dossiers for Remaining Occurrences

### 4.1 SC007: Lowering of final bimoric *\*ō* before *\*r* ("four and water families")

**Location:** `007-final-o-lowering-before-r.md:5` and `007-final-o-lowering-before-r.md:20`.

**Evidential structure:** Two independent etyma — *\*fedwor* 'four' and *\*watōr* 'water' — each showing that final *\*ō* was lowered before word-final *\*r*. R&T also cite kinship-term *r*-stems (PGmc *\*fadér* 'father' > PWGmc *\*fader* with short vowel in OHG) as the primary evidence for the shortening; 'four' and 'water' demonstrate the ordering relative to unrounding.

**Source:** R&T vol.2 p.59–60 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 4130–4165.

**Assessment:** The "families" label means one cognate set each. The use is not misleading. A minor improvement: note that kinship-term r-stems (father, etc.) supply the primary historical evidence for the change's occurrence; 'four' and 'water' supply ordering information.

**Recommendation:** One sentence addition. Low priority.

---

### 4.2 SC012: *lþ*-voicing ("field, fold, gold, and wold families")

**Location:** `012-lth-voicing.md:18`.

**Assessment:** Four independent etyma. The use is accurate. Minor: R&T's list also includes *wild*, *bold*, and *glory*, which may be clearer witnesses. **Recommendation:** Consider extending list. Low priority.

---

### 4.3 SC013: Dental hardening ("extends beyond any one lexical family")

**Location:** `013-dental-hardening.md:8`. Negative comparative use. Correct. **Recommendation:** No action.

---

### 4.4 SC021: Unstressed *\*o*-raising ("the same family" for *heofon*)

**Location:** `021-unstressed-o-raising.md:5`. Single cognate set; "the same family" refers anaphorically. Accurate but slightly vague. **Recommendation:** Name OE *heofon* and OS *heban* directly. Very low priority.

---

### 4.5 SC064–065: Post-apocope tail ("*furht-* family", "family behind *fyrhte*")

**Location:** `064-065-post-apocope-tail.md:6,20,30`.

**Evidential structure and morphology — resolved:**

The morphological status of OE *fyrhte* 'fright' has been investigated in detail against Orel, Kroonen, R&T, and Campbell.

**What Orel supplies** (`docs/references/orel_handbook_germanic_etymology.vision.txt`, line 14554; legacy `docs/references/legacy/orel_handbook_germanic_etymology.txt`, line 12585):

> `*furxtīn sb.f.: Goth faurhtei 'fright, fear', OE fyrhtu id.`

**[Source statement — Orel]** Orel explicitly reconstructs *\*furxtīn* as a feminine *in*-stem abstract noun, citing Gothic *faurhtei* and OE *fyrhtu*.

**What Kroonen supplies** (`docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, lines 9656–9678; legacy `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt`, lines 10835–10860):

Kroonen gives: *furhta-* adj. 'fearful' (Gothic *faurhts*, OS *for(a)ht*, OHG *foraht*), *furhtō-* f. 'fright' (OFris *fruchta*, OS *forhta*, OHG *forhta*), *furhtjan-* wk.vb. 'to fear'.

**[Source statement — Kroonen]** Kroonen does not give an independent *in*-stem entry. He gives *furhtō-* (ō-stem), which is the remodeled form in the continental WGmc languages. The Gothic *faurhtei* and OE *fyrhtu* forms that Orel assembles under an *in*-stem reconstruction appear in Kroonen only as cognate citations under the ō-stem and adjective entries, not as a reconstructed *in*-stem lemma.

**What R&T supply** (`docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 5516–5525, p. 104):

> "We would therefore expect in-stems in the daughter languages to exhibit reflexes of a nom. sg. in *\-ī*, acc., gen., and dat. sg. in *\-in*."

And at lines 21538–21553 (p.380):
> "Inherited fem. abstract nouns in *\-in* had lost the *\-n* of the oblique sg. caseforms… [yielding OE] fyrhtu 'fear', hetu 'heat', strengu 'strength', etc."

**[Source statement — R&T]** R&T confirm that OE *fyrhtu* belongs to the *in*-stem class. They give the paradigm as: nom. sg. *\*-ī*, oblique sg. *\*-in* (before *n*-loss after unstressed *i*), yielding OE *-e* for all forms.

**What Campbell supplies** (Campbell §589.7, `docs/references/campbell_old_english_grammar.txt`, lines starting at 620162):

> "In OE fem. abstract nouns of the in-declension (cf. Gothic *managei* multitude, acc. *managein*) would normally have -e < *i* < *-in* (§473) in the acc., gen., and dat. sg."

Campbell §473 (`docs/references/campbell_old_english_grammar.txt`, lines 510600–510610):
> "The same tendency explains oblique cases of abstract fem. nouns, e.g. *strenge* a.s. 'strength', cf. Goth. *managein*."

**[Source statement — Campbell]** OE *fyrhte* (oblique sg.) is a regular product of the in-stem paradigm: OE oblique *-e* < pre-OE *\*-i* < PGmc/PWGmc *\*-in* (with *n* lost after unstressed *i*).

**Assessment of CAPR input `*fúrxtīnaz`:**

The PGmc in-stem paradigm has:
- Nom. sg.: *\*-ī*
- Acc./gen./dat. sg.: *\*-in*

The form `*fúrxtīnaz` ends in `-az`. This is **not a standard in-stem case ending**. The gen.sg. in-stem ending is `*-in` (not `*-inaz`). The `-az` ending belongs to a-stems. R&T's paradigm description (l.5517) gives acc./gen./dat. as `*-in`, not `*-inaz`.

**[CAPR observation]** The CAPR TSV (row 2034, `Germanic/data/germanic-aligned-final.tsv`) explains: the gen.sg. `*fúrxtīnaz` was chosen specifically to exercise the longest oblique tail through the cascade. The DEV_NOTES entry states: "Gen.sg. was selected specifically to exercise the longest oblique tail (-naz, requiring NWGmcZLoss, PWGmcFinalBareALoss, NWGmcInStemNLoss...)."

**[Auditor inference — implementation review flag]** The suffix `-naz` on the CAPR input treats the in-stem gen.sg. as if it had a secondary a-stem gen.sg. ending `-az` appended to the in-stem oblique form `*-in-`. This may be a legitimate pre-apocope form (before PWGmc loss of final *-z* in unstressed syllables, if in-stems had `*-inaz` at the oldest stage, cognate with Gothic gen. *heitins* < *\*haitanas*). However:
- R&T (l.5517) give the PWGmc gen.sg. as `*-in` (with *n* retained at the post-PWGmc stage, lost by NWGmcInStemNLoss).
- The source record for whether PGmc in-stem gen.sg. was `*-in` or `*-inaz` at the oldest stage reconstructible by comparison is not resolved in the inspected sources.
- **This form should be flagged for implementation review** to confirm the ending `-az` is derivable from a documented PGmc paradigm cell or is a CAPR-specific cascade choice that requires an explicit justification comment.

The use of "family" in the chapter (`064-065-post-apocope-tail.md`) is defensible. The morphological status of OE *fyrhte* as an in-stem oblique is well-sourced (Orel, R&T, Campbell). The precise CAPR input form `*fúrxtīnaz` is a **paradigm-cell inference** (from the in-stem reconstruction) that may involve a non-standard gen.sg. ending requiring explicit documentation.

**Source Assessment:**
- Orel *\*furxtīn* (in-stem, nom.): `docs/references/orel_handbook_germanic_etymology.vision.txt`, l.14554. **[Source statement]**
- Kroonen *furhtō-* (ō-stem): `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, l.9674. Kroonen does not reconstruct an independent in-stem lemma. **[Source statement]**
- R&T OE *fyrhtu* as in-stem: `docs/references/ringe_taylor_linguistic_history_vol2.txt`, l.21553. **[Source statement]**
- Campbell §589.7 OE in-stem oblique *-e*: `docs/references/campbell_old_english_grammar.txt`, §589.7 section. **[Source statement]**
- CAPR TSV row 2034: `Germanic/data/germanic-aligned-final.tsv`, row 2034. **[CAPR observation]**

**Status:** Morphological basis for OE *fyrhte* as in-stem oblique: well-sourced. CAPR input `-az` ending: flagged for implementation review.

**Recommendation:** Chapter wording is defensible. For precision: "inherited *\*furht-* root" could replace "inherited *\*furht-* family." The CAPR-level question about `*fúrxtīnaz` vs. a more standard in-stem gen.sg. form should be investigated separately in an implementation review, not in the manuscript. Do not change chapter prose until the CAPR input question is resolved.

---

### 4.6 Chapter 1 intro: SC002 Gm-simplification ("two lexical families")

**Assessment:** Exemplary use — two distinct etyma labeled correctly as two families. No action.

---

### 4.7 Genealogical uses

**Assessment:** Standard linguistic terminology. No action.

---

## 5. Synthesis: Evidential Configurations Hidden by *Family*

Six distinct configurations appear in the corpus:

**A. Single cognate set, historical scope established.** *Friend* (SC009), *heofon* (SC021), *fright* (SC064/65), and *four* (as the *\*dw* evidence in SC008) all fall here for their respective cognate sets. The "family" label is technically accurate but may imply more breadth than exists.

**B. Multiple independent etyma for one sound change.** *Field, fold, gold, wold* (SC012); *draugma-*, *taugma-* (SC002). Label "families" is correct when multiple distinct etyma are listed.

**C. Inflectional or morphological categories, not cognate sets.** SC005: the comparative base is paradigm endings across many lexemes; 'shoulder' is not part of this evidence. The "shoulder family" label is misleading.

**D. Cross-category set with one cognate item and one paradigmatic item.** SC008: one numeral (*four*) and one pronominal paradigm (two case forms of *\*izwiz/\*izweraz*). The "four family" label foregrounds the wrong element; the "two pronouns" description overstates independence.

**E. CAPR ordering witness only.** *Shoulder* for SC005: the word provides a chronological constraint, not comparative evidence. The *four* numeral partly falls here for the ordering constraint with SC031.

**F. Genealogical / no evidential claim.** "The Germanic family" (language family). Correct.

---

## 6. Prioritized List of Manuscript Interventions

1. **SC005 `shoulder` family — highest priority.** Factual correction: distinguish the CAPR ordering witness from the comparative inflectional evidence. One sentence.

2. **SC008 `four` family — high priority.** Factual correction: replace "four family + two pronouns" with "one numeral and one pronominal paradigm." Name the Gothic/WGmc forms. One sentence.

3. **SC007 'four and water families' — moderate priority.** Add kinship-term r-stems as primary evidence. One sentence.

4. **SC009 friend — low priority.** Name the actual WGmc forms. One sentence.

5. **SC012 field/fold/gold/wold — low priority.** Consider R&T's fuller list. Minor.

6. **SC021 heofon — very low priority.** Name OE *heofon* and OS *heban*. Terminology only.

7. **SC064–065 *furht-* root — very low priority.** Chapter prose defensible. CAPR input review separate.

---

## 7. Implementation-Readiness Table

| SC | Current problem | Comparative evidence complete? | CAPR ordering evidence complete? | Remaining uncertainty | Proposed revision ready? | Implementation risk |
|---|---|---|---|---|---|---|
| SC005 | "shoulder family" label implies cognate set is the evidence | yes | yes | none | yes | low |
| SC008 | "four family + two pronouns" overstates evidence; treats paradigm cells as independent etyma | yes | yes | counterexamples tentative in Stiles | yes | low |
| SC009 | Luick extra forms implication; old "Luick absent" stale claim | yes (Luick resolved) | yes | none | yes | low |
| SC064–065 | CAPR input `*fúrxtīnaz` uses non-standard `-az` suffix for in-stem gen.sg. | yes (in-stem basis sourced) | yes | gen.sg. ending requires implementation review | partly: chapter prose ready; CAPR input flagged | requires model-input review |

---

## 8. Source Status

### Source present and fully inspected

1. **Luick** at `docs/references/luick_historische_grammatik.txt`. R&T's "Luick 1914-40: 118" is a page citation to printed page 118 (= scan page 166 in this OCR), which contains Luick §102. The section discusses *-iju-* contraction and names *frijōnd-*, *fijand-*, *frija-*, *blija-* as stems affected by paradigmatic *iu* generalization. R&T's narrower claim about stressed *\*ijo* uniqueness is consistent with Luick: the additional forms involve different phonological environments and/or are paradigmatically restricted.

2. **Orel** at `docs/references/orel_handbook_germanic_etymology.vision.txt` and legacy copy. Explicitly gives *\*furxtīn* as in-stem abstract with Gothic *faurhtei* and OE *fyrhtu*. Sufficient for the in-stem identification.

3. **Kroonen** at `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and legacy copy. Gives *furhta-*, *furhtō-*, *furhtjan-*. Does not independently reconstruct an in-stem lemma for 'fright'. The absence of a Kroonen in-stem entry reflects the lexicographic focus on the ō-stem; it does not contradict the in-stem analysis supported by Orel and R&T.

4. **R&T** at `docs/references/ringe_taylor_linguistic_history_vol2.txt`. Gives the PWGmc in-stem paradigm (acc./gen./dat. sg. `*-in`), cites OE *fyrhtu* as an in-stem example. Decisive.

5. **Campbell** at `docs/references/campbell_old_english_grammar.txt`. §589.7 describes OE in-stem declension; §473 gives oblique *-e* < `*-i` < `*-in`.

### Source present in Git history, no tracked text extract

6. **Stiles 1985, NOWELE 6 pp.89–94**: `docs/references/stiles_1985_four_part1_nowele6.pdf`, Git blob at commit `11c20529`, untracked in `971d1d88`. Inspected via `pdftotext` for this analysis. No tracked `.txt` extract exists in the current checkout. The key finding (Stiles §1.3.3 describes the *\*zw* evidence as "the oblique cases of the second person plural pronoun") is based on the historical PDF blob. Characterization: *original PDF present in Git history; no tracked text extract identified.*

### Reconstruction inferred, not directly sourced as that exact form

7. **CAPR input `*fúrxtīnaz`**: The in-stem identification is directly sourced (Orel, R&T, Campbell). The specific gen.sg. form with `-az` ending is a CAPR cascade-design choice that extrapolates from the in-stem reconstruction. The standard PWGmc gen.sg. in-stem ending in R&T is `*-in`, not `*-inaz`. The `-az` element requires a dedicated implementation review to confirm its morphological derivation.

---

## 9. Source-to-Statement Transparency Note

Throughout this audit, the following conventions are observed:

- **[Source statement]:** reproduces or closely paraphrases what the source text says.
- **[Source inference]:** follows by comparison of forms the source provides.
- **[CAPR observation]:** concerns the implementation or ordering constraint, not the historical claim.
- **[Auditor inference]:** analytical conclusion not directly stated by any source.

Key observations with designations:

- That shoulder is a CAPR ordering witness and not part of the comparative evidence for SC005: **[auditor inference]**, supported by R&T's treatment of the rule and the chapter's own statement.
- That *izwiz* and *izweraz* are case forms of one pronominal paradigm, not two independent etyma: **[source statement]** — Stiles §1.3.3 explicitly uses "the oblique cases of the second person plural pronoun."
- That R&T's "one example of each cluster" is consistent with treating both pronominal case forms as one paradigmatic witness: **[source inference from R&T l.3106 + Stiles §1.3.3]**.
- That the *\*ijo* sequence with stressed *\*i* is unique to friend among the Luick examples: **[source statement]** — R&T p.62 explicit. Luick's other forms have different phonological environments: **[auditor inference from comparison of Luick §102 and R&T restriction]**.
- That CAPR's `*fúrxtīnaz` uses a non-standard in-stem gen.sg. suffix: **[auditor inference from comparison of CAPR TSV and R&T paradigm description]**.

---

*Report prepared and reconciled on `family-evidence-audit` branch. No reader-facing manuscript, FST, model entry, staging map, or generated book artifact was modified.*

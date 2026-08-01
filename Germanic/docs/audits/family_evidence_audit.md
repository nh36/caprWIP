# Audit: Evidential Uses of *Family* in Historical Chapters

**Branch:** `family-evidence-audit`
**Scope:** Reader-facing Part I chapter files (`Germanic/docs/sound_changes/reader_facing/*.md`, excluding generated section files), supporting literature dossiers, staging documents, and assembly-layer introduction files.
**Status:** First-pass audit. No manuscript files changed.

---

## 1. Problem Statement

The word *family* appears in the reader-facing chapters and supporting documents to mean several structurally different things:

1. **Single cognate set**: one inherited etymon whose reflexes survive in multiple branches (*friend*, *heofon*).
2. **Multiple independent etyma** sharing a sound change (*field/fold/gold/wold* for SC012).
3. **One morphological paradigm or set of inflectional endings** (*shoulder* for SC005).
4. **A small multi-item set spanning different grammatical categories** (*four* + pronouns for SC008).
5. **CAPR ordering witness only**: a word that provides a chronological constraint but is not itself the primary comparative evidence for the sound law.
6. **Genealogical label**: the Germanic *language* family — not an evidential claim.

Configurations 3 and 5 are the most misleading. SC005 (*shoulder*) is the clearest case: the word "shoulder" functions solely as a CAPR ordering witness; the comparative evidence for the sound change consists entirely of inflectional endings. Calling it "the `shoulder` family" implies that the comparative base is a group of cognate forms of the word 'shoulder', which is false.

SC008 (*four*) is less misleading but still incomplete: the current phrasing foregrounds one numeral while the evidence for one of the two input clusters (*zw*) comes entirely from pronominal forms.

---

## 2. Complete Occurrence Inventory

Scope: `Germanic/docs/sound_changes/reader_facing/*.md` (excluding generated `reader_facing_local_section_*.md`), `Germanic/docs/assembly/capr_book_intro_alpha_01.md`, `Germanic/docs/assembly/section_introductions_draft.md`.

Supporting staging documents included: `reader_facing_sc005_009_012_inclusion_01_report.md`, `reader_facing_chronology_confidence_audit_01.md`, `reader_facing_pilot_02.md`, `README.md`.

| # | Location | Current label | Evidential structure | Evidence sufficient? | Scale |
|---|----------|--------------|---------------------|---------------------|-------|
| 1 | `005-unstressed-a-raising-before-final-m.md:18` | "the `shoulder` family…tests the chronology" | CAPR ordering witness; the sound law is supported by inflectional endings, not shoulder cognates | Partly: needs explicit statement | One sentence |
| 2 | `007-final-o-lowering-before-r.md:5` | "the families behind *fēower* 'four' and *wæter* 'water'" | Two independent single cognate sets (numerals/nouns) | Yes, with minor clarification | Terminology only |
| 3 | `007-final-o-lowering-before-r.md:20` | "*fēower* 'four' and *wæter* 'water' families" | Two independent single cognate sets | Yes, with minor clarification | Terminology only |
| 4 | `008-coronal-w-assimilation.md:5` | "the `four` family and plural-pronominal forms" | Composite: one numeral (*dw*) + two pronouns (*zw*); R&T explicitly note one example of each cluster | Partly: "four family" obscures that pronouns are the evidence for *zw* | One sentence |
| 5 | `009-ij-contraction-in-friend.md:5` | "a change…in the `friend` family" | Single cognate set; R&T explicitly restrict generalization | Yes: limitation stated; could be made structurally explicit | Terminology only |
| 6 | `009-ij-contraction-in-friend.md:7` | "confined to the `friend` family" | Same | Yes | Pass |
| 7 | `009-ij-contraction-in-friend.md:18` | "Only the `friend` family tests this contraction" | Same | Yes | Pass |
| 8 | `009-ij-contraction-in-friend.md:20` | "beyond this family" | Same | Yes | Pass |
| 9 | `012-lth-voicing.md:18` | "The `field`, `fold`, `gold`, and `wold` families" | Four independent etyma preserving the same development | Yes; each is a separate word | Terminology only |
| 10 | `013-dental-hardening.md:8` | "extends beyond any one lexical family" | Negative comparative statement; not an evidential claim | Yes (negative use) | Pass |
| 11 | `021-unstressed-o-raising.md:5` | "the same family" (heofon/heaven) | Single cognate set (OE *heofon*, OS *heban*, NWGmc *hebun*) | Yes | Terminology only |
| 12 | `064-065-post-apocope-tail.md:6` | "inherited *furht-* family" | Single root (*prk-to-) with multiple derived forms | Yes | Terminology only |
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

#### 3.1.2 Evidential Classification

- **Single cognate set across languages** — primary classification.
- **CAPR chronological witness** — secondary: the derivation places SC009 before SC032 (OE Diphthong Leveling).

The evidence consists of one inherited etymon, PGmc *\*frijond-*, whose reflexes survive in multiple West Germanic branches. There is no second, etymologically independent item that would demonstrate the productivity of the *\*ijo > \*iu* change.

#### 3.1.3 Comparative Evidence

| Input | Language/Stage | Form | Gloss | Status | Source |
|---|---|---|---|---|---|
| PGmc *\*frijond-* | Gothic | *frijonds* | 'friend' | Conservative (no *ij*-contraction) | R&T vol.2, p. 62 |
| PWGmc *\*friund* | Old English | *frīond, frēond* | 'friend' | Innovative (*\*ij > \*iu*) | R&T vol.2, p. 62 |
| PWGmc *\*friund* | Old Frisian | *frīund* | 'friend' | Innovative | R&T vol.2, p. 62 |
| PWGmc *\*friund* | Old Saxon | *friund* | 'friend' | Innovative | R&T vol.2, p. 62 |
| PWGmc *\*friund* | Old High German | *friunt* | 'friend' | Innovative | R&T vol.2, p. 62 |

**Source locator:** R&T vol.2 p.62 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 4217–4231. The source reads: "A roughly similar change of *ijo to *iu appears to have occurred in the word 'friend' in PWGmc (Luick 1914-40: 118): PGmc *frijond- 'loving, friend' (Goth. frijonds 'friend') > PWGmce *friund 'friend' > OE friond, OF frīund, OS friund, OHG friunt."

The immediately following passage reads: "Note also that the latter word is the only one in which a nonfinal long ō-vowel can be shown to have become a u-vowel throughout WGmc… the uniqueness of the sequence *ijo (with stressed *i) makes it inadvisable to attempt any generalizations based on the history of this word." This is the key limiting statement.

No second etymon is cited in R&T. The repository's `009-pwgmc-ij-contraction.dossier.md` confirms: "The present source base is effectively one lexical family."

#### 3.1.4 Argument

**What the comparative evidence establishes:**
The reflexes of PGmc *\*frijond-* demonstrate that the *\*ijo* sequence was simplified to *\*iu* in Proto-West Germanic. Gothic *frijonds* preserves the earlier form and confirms the development is an innovation of the West Germanic branch. The evidence is geographically wide (all four major WGmc branches) but etymologically narrow (one inherited word).

**What the CAPR derivation establishes:**
The derivation of OE *frēond* from PGmc *\*fríjōndz* places SC009 (PWGmcIjContraction) before SC032 (OEDiphthongLeveling). Without contraction before leveling, the intermediate form *\*friund* would be caught by the leveling rule and yield *\*friund* rather than the expected *frēond*. This ordering relation is specific to this one lexical item.

**What the evidence does not establish:**
- The existence of a second, etymologically independent etymon showing the same development.
- A productive rule extending beyond this word.
- Any information about the earlier boundary of SC009.

R&T themselves declare broader generalization inadvisable.

#### 3.1.5 Source Assessment

- Primary source: `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 4217–4231 (p.62, §3.1 "Proto-West Germanic sound changes").
- The repository source is sufficient for the present historical claim.
- The literature dossier correctly captures the restriction but does not reproduce the precise R&T phrasing.
- No contradictions found between the chapter and the source.
- Luick 1914-40 §118 is cited by R&T but the Luick text is not in the repository; the R&T discussion is self-contained for the present purpose.

#### 3.1.6 Editorial Recommendation

The current chapter prose is largely correct: the restriction is stated ("cannot safely be generalized") and the unique sequence is mentioned ("rare sequence confined to the `friend` family"). The use of "`friend` family" labels this correctly as a cognate set, not as multiple etyma.

The only substantive improvement is to name the forms directly rather than relying on the family label, making explicit what "the family" actually consists of:

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

Current sentence (line 18):
> "The `shoulder` family therefore tests the chronology, while the inflectional endings justify restricting the change to noninitial unstressed material before *\*m*."

This sentence is correct that shoulder "tests the chronology" and that "inflectional endings justify" the rule; but the label "shoulder family" suggests that the shoulder cognate set constitutes the evidential base, which is false.

#### 3.2.2 Evidential Classification

- **Several morphological categories sharing an ending** — primary classification for the comparative evidence.
- **CAPR chronological witness only** — the word 'shoulder' provides an ordering constraint (SC005 must precede SC017 NWGmcULowering), nothing more.

The comparative evidence for this sound change comes entirely from inflectional endings across multiple paradigms, demonstrated with data from North Germanic and West Germanic branches. The word 'shoulder' is used only as a CAPR ordering witness.

#### 3.2.3 Comparative Evidence

**Source:** R&T vol.2, pp.17–18 (§2, NWGmc changes) = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 1785–1825. The source reads: "Throughout NWGmc, unstressed *a merged with *u when immediately followed by *m. The examples are the a-stem dat. (and inst.) pl., strong adj. masc. and neut. dat. sg., and pres. indic. 1pl. endings."

| Input form | Language(s) | Form | Gloss | Morphological category | Status | Source |
|---|---|---|---|---|---|---|
| PGmc *\*dagamaz/*-miz | ON/OE/OS/OHG | *dogum/dagum/dagun/tagum* | 'days' (dat.pl.) | a-stem dat.(inst.) pl. | Innovative: *\*a > \*u* before *m* | R&T vol.2 p.17, l.1786–1791 |
| PGmc *\*godammai* | ON/OE/OS | *godum/godum/godum(u)* | 'good' (dat.sg. masc./neut.) | Strong adj. dat.sg. | Innovative | R&T vol.2 p.17, l.1792–1798 |
| PGmc *\*beramaz* | ON/OHG | *berum/berumés* | 'we carry' | 1pl. present indicative | Innovative | R&T vol.2 p.17, l.1799–1806 |
| Gothic *\*godammai* | Gothic (conservative) | *-amma* (sg. adj.) | — | Strong adj. dat.sg. | Conservative (*\*-am-*) | R&T vol.2 p.17, l.1807 |
| Gothic *ainummehun* | Gothic (partial) | *ainummehun* | 'any, anyone' (dat.sg.) | Pronoun (position before *-m-* between stresses) | Partial parallel | R&T vol.2 p.18, l.1820–1829 |

**Additional source:** Campbell §373 (`docs/references/campbell_old_english_grammar.txt`, lines 10189–10228): "u is always well preserved… before m, e.g. mapum, d.p. -um, -sum as suffix."

**Additional source:** Fulk §1.10 (`docs/references/fulk_comparative_grammar_early_germanic.vision.txt`, lines 1658–1664): lists "development of early PGmc. unstressed *o to u before m, as in the dat. pl. inflection -um (Go. -am; §5.2)" as one of the defining NWGmc shared innovations distinguishing NWGmc from Gothic.

**CAPR ordering witness — shoulder:**
PGmc *\*skúldramiz* 'shoulders' is used in CAPR derivation. If SC005 is delayed until after SC017 (NWGmcULowering), the derivation yields *\*sċoldrum* rather than the expected OE *sċuldrum*. This ordering constraint is specific to this one lexeme and its inflectional form.

#### 3.2.4 Argument

**What the comparative evidence establishes:**
The inflectional evidence demonstrates a NWGmc change of unstressed *\*a* to *\*u* immediately before *\*m*, attested across three distinct morphological categories (dat.pl., dat.sg. adj., 1pl. verb) and multiple NWGmc branches (North Germanic and all major WGmc languages). Gothic preserves the conservative forms in most environments but shows a partial parallel in *ainummehun*, suggesting the change may have had a pan-NWGmc precursor before generalization. The geographic and morphological width of the evidence constitutes strong support for a regular sound law.

**What the CAPR derivation establishes:**
The derivation of OE *sċuldrum* places SC005 before SC017 (NWGmcULowering): if unstressed *\*u* lowering precedes the raising of *\*a* to *\*u* before *m*, the intermediate *\*a* would become *\*o* through lowering rather than *\*u* through the raising rule, yielding the wrong output. This ordering relation is established by one lexical form in one morphological cell.

**What the evidence does not establish:**
- That the word 'shoulder' is part of the comparative argument for the sound law.
- That 'shoulder' cognates provide any evidence for the rule's historical scope or morphological conditioning.
- Any restriction on the rule to the shoulder word or its paradigm.
- The earlier boundary of SC005's placement.

The sound law is justified entirely by morphological endings. 'Shoulder' is incidental — it happens to be the right length and structure to create an ordering constraint with SC017.

#### 3.2.5 Source Assessment

- Primary source: R&T vol.2 pp.17–18 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 1785–1835.
- Secondary: Campbell §373 = `docs/references/campbell_old_english_grammar.txt`, lines 10189–10228.
- Secondary: Fulk §1.10 = `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`, lines 1658–1664.
- Repository evidence is sufficient to fully document the sound change.
- Current chapter correctly identifies inflectional endings as the comparative base, but the "shoulder family" label contradicts this in the same sentence.

#### 3.2.6 Editorial Recommendation

The sentence "The `shoulder` family therefore tests the chronology, while the inflectional endings justify restricting the change to noninitial unstressed material before *\*m*" is internally contradictory: it correctly says inflectional endings justify the rule but uses "the `shoulder` family" as if shoulder were a comparative item.

**Proposed revision:**
> "The CAPR derivation of *sċuldrum* 'shoulders' tests the chronology: if raising is delayed until after [SC017 NWGmcULowering], PGmc [skúldramiz]{.recon} 'shoulders' yields [\*sċoldrum]{.pred} rather than expected OE *sċuldrum* 'shoulders'. The inflectional evidence — the a-stem dat.pl., strong-adjective dat.sg., and 1pl. present forms uniformly showing *-um* across ON, OE, OS, and OHG — justifies restricting the change to noninitial unstressed material before *\*m*."

**Scale:** One-sentence clarification; no structural change; removes the misleading "shoulder family" label and makes the distinction between ordering witness and comparative evidence explicit.

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

Current sentence (line 5):
> "Ringe and Taylor treat the assimilation of `*dw` and `*zw` to `*ww` as a shared Proto-West-Germanic innovation and support it through the `four` family and plural-pronominal forms such as `you` and `your` [@RingeTaylor2014, pp. 56--57]."

#### 3.3.2 Evidential Classification

- **Multiple independent lexical witnesses** — across distinct grammatical categories: one numeral, two pronouns.
- **CAPR chronological witness** — 'four' exposes the ordering constraint with SC031.

The evidence is not a "family" in any standard sense. It comprises three morphologically independent items:
1. *\*fedwor* 'four' — a cardinal numeral, source of the *\*dw* example.
2. *\*izwiz* 'you (dat.pl.)' — a 2nd-person plural dative pronoun, source of one *\*zw* example.
3. *\*izweraz* 'your (pl.)' — a 2nd-person plural genitive pronoun, source of a second *\*zw* example.

These are not cognates of one another. They are etymologically unrelated items that share the structural property of containing a coronal before *\*w*.

#### 3.3.3 Comparative Evidence

**Source:** R&T vol.2, pp.56–57 (§3.1.1 "Changes of coronal consonants") = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 3100–3160. Key statement: "There is really only one example of each input cluster, but the basic nature of the lexemes involved makes the change virtually certain."

*\*dw* cluster:

| Input | Language | Form | Gloss | Status | Source |
|---|---|---|---|---|---|
| PGmc *\*fedwor* | Gothic | *fidwor* | 'four' | Conservative (*\*dw* preserved) | R&T vol.2 p.56, l.3110 |
| PWGmc *\*feuwar* | Old English | *fēower* | 'four' | Innovative (*\*dw > \*ww > \*uw*) | R&T vol.2 p.56, l.3111 |
| PWGmc *\*feuwar* | Old Frisian | *fiuwer* | 'four' | Innovative | R&T vol.2 p.56 |
| PWGmc *\*feuwar* | Old Saxon | *fiuwar* | 'four' | Innovative | R&T vol.2 p.56 |
| OHG *fior* | Old High German | *fior* | 'four' | Innovative (backformed from *fiordo* 'fourth') | R&T vol.2 p.56, l.3112 |

*\*zw* cluster (two examples):

| Input | Language | Form | Gloss | Status | Source |
|---|---|---|---|---|---|
| PGmc *\*izwiz* | Gothic | *izwis* | 'you (dat.pl.)' | Conservative (*\*zw* preserved) | R&T vol.2 p.56, l.3114 |
| PWGmc *\*iuwi/\*iuw* | Old English | *iow* | 'you (dat.pl.)' | Innovative | R&T vol.2 p.56, l.3115 |
| PWGmc *\*iuwi/\*iuw* | Old Frisian | *iu* | 'you (dat.pl.)' | Innovative | R&T vol.2 p.56 |
| PWGmc *\*iuwi/\*iuw* | OS/OHG | *iu* | 'you (dat.pl.)' | Innovative | R&T vol.2 p.56 |
| PGmc *\*izweraz* | Gothic | *izwar* | 'your (pl.)' | Conservative | R&T vol.2 p.57, l.3117 |
| PWGmc *\*iuwar* | Old English | *iower* | 'your (pl.)' | Innovative | R&T vol.2 p.57 |
| PWGmc *\*iuwar* | Old Frisian | *iuwer* | 'your (pl.)' | Innovative | R&T vol.2 p.57 |
| PWGmc *\*iuwar* | Old Saxon | *iuwar* | 'your (pl.)' | Innovative | R&T vol.2 p.57 |
| PWGmc *\*iuwar* | Old High German | *iuwer* | 'your (pl.)' | Innovative | R&T vol.2 p.57 |

**CAPR ordering witness — 'four':**
OE *fēower* 'four' exposes the feeding relation SC008 → SC031 (OEWWSimplification). If SC008 is delayed until after SC031, *\*fedwōr* yields *\*fēowwer* rather than OE *fēower*. This constraint is demonstrated by one lexical item.

#### 3.3.4 Argument

**What the comparative evidence establishes:**
Three etymologically independent items — one numeral (*four*) and two pronouns (*you*, *your*) — demonstrate that voiced coronal fricatives (*\*d* as fricative, *\*z*) were assimilated to a following *\*w* in Proto-West Germanic. Gothic preserves the unassimilated clusters, confirming the innovation is WGmc. The numeral provides the only example of *\*dw*; both pronouns exemplify *\*zw*. R&T characterize this as "really only one example of each input cluster" but consider the change "virtually certain" given the fundamental nature of the vocabulary items.

**What the CAPR derivation establishes:**
The derivation of OE *fēower* places SC008 before SC031: *\*ww* from assimilation must be created before *\*Vww* simplification can reduce it. This feeding ordering is demonstrated by the 'four' numeral alone; the pronouns do not produce the relevant output contrast.

**What the evidence does not establish:**
- A *family* of related cognates: 'four', 'you', and 'your' are morphologically and etymologically independent.
- More than one example of the *\*dw* cluster.
- The earlier boundary of SC008.
- Any counterexamples that were resisted by paradigm leveling within one word family (R&T discuss *\*badwō* 'battle' and *\*skadwa-* 'shadow' as apparent exceptions accounted for by leveling or u-stem status, not by the *four family*).

#### 3.3.5 Source Assessment

- Primary source: R&T vol.2 pp.56–57 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 3100–3165.
- Literature dossier (`008-pwgmc-coronal-w-assimilation.dossier.md`) correctly names the three witnesses.
- Repository evidence is sufficient.
- No contradictions between chapter and source.
- The chapter already correctly notes "plural-pronominal forms such as `you` and `your`" alongside "the `four` family," which is an improvement over pure focus on four.

#### 3.3.6 Editorial Recommendation

The current sentence is partially correct: it names the pronouns alongside 'four'. The problem is leading with "the `four` family" and grouping the pronouns as secondary support, when the pronouns are the only evidence for the *\*zw* cluster.

**Proposed revision:**
> "Ringe and Taylor treat the assimilation of *\*zw* and *\*dw* to *\*ww* as a shared Proto-West-Germanic innovation and support it with a small cross-category set: the numeral *\*fedwor* 'four' (Gothic *fidwor* vs. OE *fēower*) as the only *\*dw* example, and the 2nd-person plural forms *\*izwiz* 'you (dat.pl.)' (Gothic *izwis* vs. OE *iow*) and *\*izweraz* 'your (pl.)' (Gothic *izwar* vs. OE *iower*) as the *\*zw* examples [@RingeTaylor2014, pp. 56--57]."

**Scale:** One-sentence clarification plus insertion of the Gothic and WGmc forms; removes the misleading "four family" label; makes the two-cluster structure and the small evidential base explicit.

---

## 4. Shorter Dossiers for Remaining Occurrences

### 4.1 SC007: Lowering of final bimoric *\*ō* before *\*r* ("four and water families")

**Location:** `007-final-o-lowering-before-r.md:5` and `007-final-o-lowering-before-r.md:20`.

**Evidential structure:** Two independent etyma — *\*fedwor* 'four' and *\*watōr* 'water' — each showing that final *\*ō* was lowered to *\*a* before word-final *\*r*. R&T also use kinship-term *r*-stems (PGmc *\*fadér* 'father' > PWGmc *\*fader*) as primary evidence that shortening occurred in WGmc; 'four' and 'water' demonstrate the ordering relative to unrounding.

**Source:** R&T vol.2 p.59–60 (§3.1.4) = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 4130–4165. "The most cogent indication that this shortening occurred is the fact that the nom. sg. forms of the r-stem kinship terms exhibit short vowels before -r in OHG, which did not normally shorten vowels in closed final syllables; that the shortening followed the unrounding of *ō is demonstrated by the outcome of 'four', and perhaps of 'water'."

**Assessment:** "Families" here = "one cognate set each." The use is not misleading since 'four' and 'water' are different words. The kinship term evidence (father, etc.) is a third independent set not mentioned in the chapter; it provides the primary evidence for the change's occurrence, while 'four' and 'water' supply the ordering. This is a substantive omission.

**Recommendation:** Mention that the kinship-term r-stems (e.g., *\*fadér* 'father' → OHG *fater* with short vowel before *-r*) provide the primary historical evidence for the change; 'four' and 'water' establish the ordering relative to unrounding. Scale: one sentence.

---

### 4.2 SC012: *lþ*-voicing ("field, fold, gold, and wold families")

**Location:** `012-lth-voicing.md:18`.

**Evidential structure:** Four independent etyma: *\*falbang* 'fold', *\*gulþa-* ~ *\*gulda-* 'gold', *\*felþu-* ~ *\*feldaw-* 'field', and *\*walda-* 'wold'. R&T (p. 170–171) also cite *\*wilþijaz* 'wild', *\*balþaz* 'bold', and *\*wulþraz* 'worth' → *wuldor* 'glory' as clear examples, and *\*gulþinaz* 'golden' as a fifth. The chapter's list ("field, fold, gold, and wold") is a subset of R&T's examples.

**Source:** R&T vol.2 pp. 170–171 = `docs/references/ringe_taylor_linguistic_history_vol2.txt`, lines 9115–9155. "It does seem that word-internal *lþ became *ld by regular sound change in NORTHERN WGmc; the following clear examples can be cited: *falbang 'to fold'… *wilbijaz 'wild'… *balbaz 'bold'… *wulbraz adj. 'worth'… *gulpinaz 'golden'."

**Assessment:** Each word is an independent etymon; "families" here means "cognate sets." The use is accurate but the choice of examples omits the clearest witnesses (R&T's list includes *wild* and *bold* which are transparent to modern readers). 'Gold' and 'field' are complicated by possible Verner alternation (*gulþ-* ~ *gulda-*; *felþu-* ~ *feldaw-*), which R&T mention but the chapter does not. R&T scope the rule to *northern* WGmc, not all PWGmc; the chapter correctly says "northern West Germanic."

**Recommendation:** The "field, fold, gold, and wold" list is serviceable but omitting R&T's simpler examples (*wild*, *bold*, *glory*) may seem arbitrary. Consider replacing with R&T's own list (fold, wild, bold, glory, golden). Minor: note the Verner complication for *gold* and *field*. Scale: one sentence or minor list revision.

---

### 4.3 SC013: Dental hardening ("extends beyond any one lexical family")

**Location:** `013-dental-hardening.md:8`.

**Text:** "The change is systemic across early West Germanic and extends beyond any one lexical family."

**Evidential structure:** This is a negative comparative statement: it explicitly says the change is NOT limited to one family. The label "lexical family" is used as a contrast term, not as an evidential claim.

**Assessment:** No problem. This use is correct. The source (R&T p.57: "PWGmc voiced dental fricative *ð became stop *d in all positions") confirms the systemic scope.

**Recommendation:** No action needed.

---

### 4.4 SC021: Unstressed *\*o*-raising ("the same family" for *heofon*)

**Location:** `021-unstressed-o-raising.md:5`.

**Text:** "Ringe and Taylor place the same family within the wider West Germanic record."

**Evidential structure:** Single cognate set: OE *heofon*, OS *heban*, NWGmc *\*hebun* 'sky, heaven'. R&T describe "northern WGmc *hebun 'sky, heaven', gen. *hebunas, etc. (OS heban, hebanas, etc.) > OE heofon, heofones" (lines 15697–15699).

**Assessment:** "The same family" refers back to the *heofon* cognate set mentioned in the preceding clause. The use is accurate (one inherited word with reflexes). The chapter's chronological claim (the witness places SC021 before medial unstressed-*u* lowering) is correctly distinguished from the historical claim.

**Recommendation:** The label is accurate but "the same family" is slightly vague — it refers to a pronoun ("same") whose antecedent is two sentences back. Minor: clarify with "the *heofon*/*heaven* cognates" or name OE *heofon* and OS *heban* directly. Scale: terminology only.

---

### 4.5 SC064–065: Post-apocope tail ("*furht-* family", "family behind *fyrhte*")

**Location:** `064-065-post-apocope-tail.md:6,20,30`.

**Evidential structure:** The "*furht-* family" consists of a single root (*\*prk-to-*) with several related derivatives: the adjective *\*furhta-* (Gothic *faurhts*, OS *for(a)ht*, OHG *foraht*), the feminine *\*furhtō-* (OFri. *fruchta*, OS *forhta*, OHG *forhta*), and the verb *\*furhtjan-* (Gothic *faurhtjan*, OE *fyrhtan*, OFri. *fruchta*, OHG *furihtan*). OE *fyrhte* 'fright' is an *in*-stem nominalization. The chapter's label "inherited *furht-* family" correctly identifies this as one etymological family of related derivatives, not multiple independent etyma.

**Source:** Kroonen EDG p.161 = `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, lines 9656–9678.

**Assessment:** The use of "family" here is accurate in the sense of a morphological family (adj., noun, verb) derived from one root. The limitation the chapter acknowledges ("depend upon one lexical family") is correct: the ordering argument for SC064 and SC065 rests on the single form OE *fyrhte* / PGmc *\*furhtin-az*. The Gothic adjective *faurhts* and the OS/OHG forms confirm the root's antiquity but do not themselves provide ordering information.

**Recommendation:** The current use is defensible. For precision: "inherited *\*furht-* root" could replace "inherited *\*furht-* family" to avoid the ambiguity between a linguistic family (multiple etyma) and a morphological family (derivations from one root). However, this is a minor terminological preference, not a substantive error.

---

### 4.6 Chapter 1 intro: SC002 Gm-simplification ("two lexical families: *draugma-* 'dream' and *taugma-* 'team'")

**Location:** `chap1-pgmc-to-pnwgmc-intro.md:34`.

**Evidential structure:** Two etymologically independent forms: PGmc *\*draugma-* (ON *draumr* 'dream') and PGmc *\*taugma-* (ON *taumr* 'team'). Both show *\*gm > \*um/m*, but they are separate roots.

**Source:** chap1 text references Kroonen 2013 pp. 101, 511.

**Assessment:** This is the most accurate use of "families" in the corpus: two distinct lexical items, correctly labeled as two separate families. An exemplary deployment.

**Recommendation:** No action.

---

### 4.7 Genealogical uses ("the Germanic family")

**Locations:** `chap1-pgmc-to-pnwgmc-intro.md:7,43`.

**Assessment:** Both instances use "Germanic family" to mean the set of languages descended from Proto-Germanic. This is standard linguistic terminology and does not make an evidential claim. No action needed.

---

### 4.8 Staging/support documents

Items 18–23 are in build instructions (README), internal staging reports, or audit files. They are not reader-facing manuscript content and require no manuscript action. Two of them (items 19 and 20 in the inventory) correctly characterize the friend evidence as narrow, consistent with this audit's findings.

---

## 5. Synthesis: Evidential Configurations Hidden by *Family*

Six distinct configurations appear in the corpus:

**A. Single cognate set, historical scope established.** One inherited etymon with reflexes across multiple branches. The "family" label is technically accurate but may give a false impression of evidential width. *Friend* (SC009), *heofon* (SC021), *fright* (SC064), *four* as the numeral (the *dw* cluster in SC008) all fall here for their respective cognate sets.

**B. Multiple independent etyma for one sound change.** Several unrelated words each providing an instance of the same change. *Field, fold, gold, wold* for SC012 (though R&T's full list is longer). The label "families" is not wrong but can be improved by listing the words explicitly.

**C. Inflectional or morphological categories, not cognate sets.** The comparative base consists of paradigm endings shared across many lexemes, not cognates of one word. SC005 (unstressed *\*a*-raising before *\*m*): the evidence is the dat.pl. *-um*, strong-adj. dat.sg., and 1pl. verb ending in ON, OE, OS, and OHG. "The `shoulder` family" is misleading here because shoulder is not part of this evidence.

**D. Cross-category small set, etymologically heterogeneous.** SC008: one numeral (*four*, for *\*dw*) and two pronouns (*you* and *your*, for *\*zw*). These are not cognates of each other. The label "four family" hides that the pronoun forms are the only evidence for the *\*zw* part of the rule.

**E. CAPR ordering witness only.** The word provides a chronological constraint in the computational cascade but is not itself part of the comparative evidence for the sound law. *Shoulder* for SC005: the change is documented by inflectional endings; shoulder merely exposes the ordering relation with SC017. The *four* numeral partly falls here for SC008 (it provides the ordering constraint with SC031, while the pronouns support the generalization of *\*zw*-assimilation); the friend cognates partly fall here for SC009 (they confirm the development in one word but are the sole evidence for the rule).

**F. Genealogical / no evidential claim.** "The Germanic family" (language family). Correct.

---

## 6. Prioritized List of Manuscript Interventions

Listed by priority (1 = most important):

1. **SC005 `shoulder` family — highest priority.** The label is structurally misleading. Revise one sentence to distinguish the CAPR ordering witness (shoulder/sċuldrum) from the comparative evidence (inflectional endings). Name the inflectional categories and branches. This is a factual correction, not a stylistic choice.

2. **SC008 `four` family — high priority.** Revise one sentence to make the two-cluster structure visible and to present the pronouns as co-equal witnesses for *\*zw*, not as secondary support. Insert the Gothic conservative forms and OE/WGmc innovative forms to give readers the actual evidence.

3. **SC007 'four and water families' — moderate priority.** Add one sentence noting that kinship-term r-stems (PGmc *\*fadér* → OHG *fater*) provide the primary historical evidence for the shortening; 'four' and 'water' supply ordering information.

4. **SC009 friend — low priority.** The current prose correctly states the limitation. Optionally insert the four WGmc reflexes explicitly rather than relying on the cognate-set label. One sentence.

5. **SC012 field/fold/gold/wold — low priority.** Consider extending the example list to include R&T's clearer items (*wild*, *bold*, *glory*). Note the Verner complication for *gold* and *field*. Minor.

6. **SC021 heofon — very low priority.** Replace the pronoun "the same family" with an explicit reference to OE *heofon* and OS *heban*. Terminology only.

7. **SC064–065 *furht-* family — very low priority.** Consider "inherited *\*furht-* root" for precision. Defensible as-is.

---

## 7. Source Status Reconciliation (Luick, Stiles, *fyrhte*)

### Source present and inspected

1. **Luick is present in the repository** at `docs/references/luick_historische_grammatik.txt`.
   - The OCR's `§118` (marker `--- PAGE 178 ---`) discusses Anglo-Frisian brightening of *a*/*ā* and is not about *ijo*.
   - The relevant passage for SC009 is `§102` (`--- PAGE 167 ---`, lines around 6965-6995 in this OCR): Luick derives WGmc *iu* via loss of *j* in `-iju-` and explicitly cites forms beyond the friend etymon (*frijōnd-*, *fijand-*, *frija-*, *blija-*; outcomes including *friund*, *fiund*).
   - **Qualification needed:** SC009 should no longer treat Luick as missing; it should note that this repository Luick witness broadens the lexical comparison beyond 'friend', while not by itself proving broad productivity of stressed *\*ijo*.

2. **Stiles 1985 NOWELE 6 article is present in repository history** at path `docs/references/stiles_1985_four_part1_nowele6.pdf` (added in commit `11c20529`, later untracked in `971d1d88`).
   - Journal pp. 89-94 are available in that file as PDF pp. 9-14 and were inspected.
   - Those pages explicitly argue WGmc assimilation `*\-ðw- > *\-ww-` from 'four' and parallel `*\-zw- > *\-ww-` from pronoun forms (Go. *izwis* vs OE/OFris/OS/OHG *eow/iu/iu/iu*), then discuss apparent wa/wo-stem counterexamples (*gaiðwa-*, *skaðwa-*, *mēðwo-*, *baðwo-*, possible *kcwiðwa-*), leaving their full explanation tentative.
   - **Qualification needed:** the prior "Stiles missing" claim is incorrect for repository history; the evidential summary should distinguish "not in current checkout" from "present in Git history and inspectable."

### Source present but not yet conclusive

3. **Luick citation alignment remains imperfect:** R&T cite Luick `§118` for the SC009 claim, but in this OCR the directly relevant *-iju-* material is in `§102`. This supports a cautious qualifier until citation alignment is independently verified against the printed pagination.

### Source genuinely absent after exhaustive search

4. **No additional currently tracked copy** of Stiles NOWELE 6 (or a differently named duplicate PDF) was found in this checkout after path-name, full-tree text, PDF-metadata/PDF-text, and Git-history filename searches. The usable witness is the historical blob above.

### Reconstruction inferred rather than explicitly sourced

5. **`\*furhtin-az` is not explicitly reconstructed in the inspected dictionary sources.**
   - Kroonen (`legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` and `kroonen_etymological_dictionary_pgmc.vision.txt`) gives *furhta-*, *furhtō-*, *furhtjan-* but not `*furhtin-az`.
   - Orel (`legacy/orel_handbook_germanic_etymology.txt`, `orel_handbook_germanic_etymology.vision.txt`) explicitly gives *furxtīn* (in-stem abstract) with Goth *faurhtei* and OE *fyrhtu*.
   - Therefore CAPR's selected input `*fúrxtīnaz` for OE *fyrhte* is best treated as a **transparent paradigm-cell inference** from an in-stem reconstruction plus OE oblique attestation, not as a directly cited lemma in the inspected sources.

---

## 8. Source-to-Statement Transparency Note

Throughout this audit, the following conventions are observed:

- **[Source statement]:** reproduces or closely paraphrases what the source text says.
- **[Source inference]:** follows by comparison of forms the source provides.
- **[CAPR observation]:** concerns the implementation or ordering constraint, not the historical claim.
- **[Auditor inference]:** analytical conclusion not directly stated by any source.

The key observations above that carry these designations are:

- That shoulder is a CAPR ordering witness only and is not part of the comparative evidence for SC005: **[auditor inference from source structure]**, supported by R&T's failure to mention shoulder in §2.1 (unstressed *\*a*-raising) and by the chapter's own statement that "inflectional endings justify" the rule.
- That 'four', 'you', and 'your' are etymologically independent: **[source statement]** — R&T p.57: "one example of each input cluster."
- That the *\*ijo* sequence is unique to friend: **[source statement]** — R&T p.62 explicit.
- That the inflectional categories for SC005 span three morphological types: **[source statement]** — R&T p.17 explicit.

---

*Report prepared on `family-evidence-audit` branch. No reader-facing manuscript or implementation files were modified.*

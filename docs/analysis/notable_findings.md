# Notable findings and contributions

This document collects instances where the FST implementation process led to
observations, refinements, or discoveries that go beyond what is stated in the
standard secondary literature. These are flagged as potential contributions for
discussion in the eventual write-up of the project.

---

## 1. Medial high-vowel syncope: dental-obstruent conditioning

**Date discovered:** Session 039 (fyrhtu investigation)

**Background:** OE medial syncope deletes short unstressed vowels in medial
position after heavy syllables. The standard references (Campbell OEG
§§389-393; Luick Hist. Gr. §§114-121; Hogg vol.1 §3.3.3.2; R/T vol.2 §6.7.3)
all formulate the rule in terms of syllable weight and stress position. None of
them state that the identity of the consonant following the syncopated vowel
is relevant.

**What happened:** When we implemented medial high-vowel syncope as the
literature describes it — deleting medial *i after heavy syllables before any
consonant — the pipeline produced four regressions:

- *θestilaz → þistl (expected: þistel — vowel preserved before *l)
- *skellinaz → sċielln (expected: sċiellen — vowel preserved before *n)
- *wīθijaz → wīþ (expected: wīþeġ — vowel preserved before *j)
- *xarbistuz → +? (crash — vowel deleted before *s, creating impossible cluster)

When we restricted the rule to fire only before dental obstruents (*θ, *ð,
*d, *t), all regressions disappeared and all attested syncope forms (dozens of
Class 1 weak preterites in R/T pp.267-268, all *-iθō- abstracts, and the
comparatives) produced correct output.

**The observation:** Syncope is consistently regular before dental obstruents
and irregular or blocked before laterals, glides, sibilants, and nasals. This
may reflect:

1. A genuine phonological conditioning — syncope is favoured when the
   resulting cluster is homorganic (dental + dental) and blocked when it would
   create heterorganic or phonotactically difficult clusters
2. A chronological difference — earlier syncope before dentals, later
   (sporadic) syncope elsewhere
3. Post-syncope analogical restoration in forms with difficult resulting clusters

**What the literature says:**

- **Campbell (OEG §§389-393, pp.143-147):** "Short medial vowels are
  syncopated after a long stressed syllable." Does not discuss the following
  consonant. Notes "much irregularity" and levelling by analogy but does not
  connect this to specific consonant environments.

- **Hogg (vol.1 §3.3.3.2, pp.120-121):** "The high vowels were also subject
  to syncope in medial positions after a heavy syllable." Describes syncope
  and apocope as interacting changes causing irregularity. Does not mention
  conditioning by following consonant.

- **R/T (vol.2 §6.7.3, pp.264-270):** "High *i and *u were lost only if the
  preceding syllable was both heavy and stressed." Give the most detailed
  treatment. Note a complication with CR-clusters (p.269): "if a CR-cluster
  in a weak class I verb is preceded by a stressed short vowel, syncope
  occurs; otherwise it does not." This concerns the cluster formed AFTER
  syncope (preceding C + following sonorant R), not the consonant immediately
  following the syncopated vowel. It is the closest any source comes to
  noting that consonantal context matters.

- **Luick (Hist. Gr. §§114-121, pp.279-288):** Foundational treatment;
  discusses paradigmatic alternations in detail but formulates conditioning in
  terms of syllable weight and stress, not following consonant.

**Significance for the project:** This is a clear case where the FST methodology
functioned as a hypothesis-testing engine. The traditional prose formulation
("after heavy syllable") is too imprecise to implement directly; the FST forces
exact specification and the dataset provides immediate feedback. The dental-
obstruent conditioning is a pattern that only emerged when the rule was
formalized and tested at scale — it was invisible to over a century of
traditional scholarship.

**Pipeline implementation:** `OEMedialSyncope` in germanic.txt. Rule fires
before `[{*θ}|{*ð}|{*d}|{*t}]` only.

**Full analysis:** See `docs/analysis/fryhtu_investigation.md`, §5.

---

## 2. (Placeholder for future findings)

As additional sound changes are implemented and tested against the dataset,
further observations of this kind should be documented here.

---

## How to add new entries

When the FST pipeline reveals a conditioning environment, chronological
ordering, or interaction that is not discussed in the standard literature:

1. Verify the observation against R/T, Campbell, Hogg, and Luick
2. Document exactly what each source says (with page/section numbers)
3. Describe how the FST testing revealed the pattern
4. Add an entry to this document with date, background, observation, and
   literature review
5. Cross-reference the detailed analysis document

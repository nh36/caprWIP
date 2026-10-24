# Pretonic front-vowel raising

## Historical discussion of prefixal \emph{*a}-reduction

Old English *ġelīefan* 'believe' continues a formation with inherited
\emph{*ga-}. Gothic *ga-* preserves the older vowel, while Old Saxon and
Old High German *gi-* and Old English *ge-* exhibit reduced reflexes;
Ringe and Taylor reconstruct \emph{*ga-} for both Proto-Germanic and
Proto-West-Germanic. Comparable reduced prefixes do not by themselves
establish a single shared West Germanic reduction event
[@RingeTaylor2014, p. 206].

The English development comprises several changes, not an immediate
replacement of \emph{*a} by \emph{*e}. Ordinary unstressed fronting supplies
\emph{*æ}; early *gi-* and later *ge-* attest subsequent changes in the
weak vowel. Campbell distinguishes fronting from the later merger,
and Ringe and Taylor explicitly consider regular raising of pretonic
\emph{*æ} after a palatal fricative. CAPR adopts that regular account
as its working reconstruction: fronting, palatalization, raising, and
later lowering. It does not formulate a sound law conditioned by the
identity of a prefix
[@Campbell1959, pp. 140--141, §§333--334; @Campbell1959, pp. 153--155,
§§369--370; @RingeTaylor2014, pp. 334--335].

Stress supplies the decisive distinction. The ordinarily weak vowel
must be distinguished from the exceptional accented form in
*ġeatwe* 'armour'. Metrical evidence independently supports the weakness
of *ge-* and *be-* alongside stress on the following root; grammatical
structure can help recover that stress, but is not itself the condition
of the vowel change
[@Campbell1959, p. 31, §74 and n. 5; @HoggPhonology1992, pp. 99--100;
@RingeTaylor2014, p. 335; @MinkovaZhou2022, pp. 535--536].

Morphological and prosodic boundaries need not coincide. Manuscript
grouping in Old English, Old Saxon and Old High German sometimes joins
weak *ge-* to preceding material rather than to the following root.
This supports distinguishing the weak syllable from the headed root
foot, not a universal prosodic boundary at every morpheme boundary.
The accompanying modern German experiment concerns a different period
and does not date English vowel raising. Here the derivations represent
citation words with one weak pretonic syllable, not every possible
sentence-level regrouping
[@RieggerBogelWalkden2024, pp. 2065--2068].

## SC035. Raising of pretonic \emph{*æ} after a palatal fricative (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

```foma
define OEPrefixAReduction SentenceCtx([
    {*æ} -> {*i} || .#. {*ᶠ} OEAnyConsonant* {*ʝ} _
]);
```

The vowel raises because it is short, pretonic and immediately follows
the palatal fricative, not because it belongs to inherited
\emph{*ga-}. The superscript `*ᶠ` is a nonsegmental annotation of
one weak syllable before a positively identified headed foot. It is
not a reconstructed sound. The context operations preserve that
information after vowel changes consume the original accent marks;
they do not introduce a phonetic intermediate vowel. The reconstruction
itself has ordinary \emph{*æ} and \emph{*i}, not a protected breve-e.

Ringe and Taylor's regular-raising proposal provides the phonological
account adopted here. They also mention possible influence from
*bi-*. Berg prefers analogy because he finds the direct development
unattractive, but does not supply positive evidence of substitution in
that discussion. His Pforzen *ga-* is important comparative evidence
against projecting *gi-* back indiscriminately into common West Germanic;
it does not refute a later English development after palatalization.
Regular phonology therefore has explanatory priority in the present
account. The precise date of raising and its independently attested
breadth remain less secure than the early *gi-* and later *ge-* sequence:
no independent non-*ga-* word sharing the complete early environment
has yet supplied a positive comparison
[@RingeTaylor2014, p. 335; @Berg2014, pp. 60--61].

The later evidence is wider than one derivation. Early Northumbrian
*gistīga* 'climb into/onto' becomes *gestīga* 'climb into/onto', beside
West Saxon *ġestīgan* 'climb into/onto'. Early Mercian *gidyrstig* 'bold'
and *gibēaten* 'beaten' likewise have later *ge-* forms.
These are historical spellings, not records of every reconstructed
intermediate. The English *gi-* evidence is not exclusively Northumbrian.
Hogg places the later lowering of unstressed *i*, including *be-* and
*ge-*, marginally after the earlier front-vowel merger. Accordingly
[SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) merges weak
\emph{*æ} with \emph{*e}, while
[SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) subsequently lowers
pretonic \emph{*i}. Neither process changes a stressed root vowel
[@RingeTaylor2014, pp. 334--335;
@HoggGrammar1992, §§6.50--6.54 (held 2011 reprint, pp. 237--239)].

The absence of diphthongization in a weak vowel follows from the
conditioning of
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization),
not from an exceptional ban on particular prefixes. Hogg requires a
palatal immediately before a stressed vowel at the beginning of a stress
foot, not necessarily at the beginning of a word. Thus *sċeaft* 'shaft'
and *ġesċeaft* 'creation' both diphthongize the root vowel after the
sh-sound, but the weak first vowel of the latter does not diphthongize
after its j-sound. The adopted model derives both this comparison and
*ġestīgan* 'climb into/onto'; the earlier compressed rule did not
[@HoggGrammar1992, §5.48 n. 1 (held 2011 reprint, p. 104);
@RingeTaylor2014, p. 335].

In *ġelīefan* 'believe', ordinary weak fronting gives a pretonic
\emph{*æ}, palatalization supplies the fricative trigger, raising gives
\emph{*i}, and late lowering gives *ge-*. The independently supported
root-vowel history continues separately. This derivation establishes
that the phonological account is coherent, not the unique date of
raising. A fronting-and-merger account without raising reaches the same
late vowel but leaves early *gi-* unexplained; the earlier protected-vowel
compression obscures the distinction and excludes genuine clustered
forms. These are the reasons for preferring the staged account, not
merely its agreement with one final form
[@RingeTaylor2014, pp. 245, 267, 335].

Preserving stress-foot structure also preserves the real stressed
developments: *ġiest* 'guest', *ġiefan* 'give' and *sċēap* 'sheep'
retain ordinary palatal diphthongization, whereas *ġealla* 'gall'
already has a diphthong from breaking. A plain vowel symbol is not
therefore assumed to be weak: earlier fronting or diphthong leveling
may have consumed its accent. [SC107 EAFBrighteningUnstressed](#rule-EAFBrighteningUnstressed) supplies
the pretonic front vowel; the old requirement that a protective
operation precede it was computational, not a historical date before
[SC043 EAFBrightening](#rule-EAFBrightening)
[@Campbell1959, pp. 69--70, §§185--188;
@RingeTaylor2014, pp. 215--217, 335].

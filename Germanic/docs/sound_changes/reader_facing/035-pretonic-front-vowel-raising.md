# Pretonic front-vowel raising

## Inheritance and manuscript distribution

Old English *ġelīefan* 'believe' continues a formation with inherited
\emph{*ga-}. Gothic *ga-* preserves the older vowel, while Old Saxon and
Old High German *gi-* and Old English *ge-* exhibit reduced reflexes;
Ringe and Taylor reconstruct \emph{*ga-} for both Proto-Germanic and
Proto-West-Germanic. Comparable reduced prefixes do not by themselves
establish a single shared West Germanic reduction event
[@RingeTaylor2014, p. 206]. The Pforzen buckle independently preserves
continental *ga-* in the usual segmentation of *gasokun*. Its current
external archaeological date is 585--610; the complete inscription's
interpretation remains disputed. It supplies no English palatal trigger
or date for English raising
[@RuneSPforzen, find 201, inscription and external dating;
@Berg2014, pp. 60--61].

The oldest spellings do not form an unmixed chronological succession.
Toller's supplement identifies nine paired examples on one page of
Sweet's Épinal--Erfurt edition: four have *gi-* in both witnesses, one
has *ge-* in both, two Épinal *gi-* beside Erfurt *ge-*, and two the
reverse. The corresponding Corpus entries all have *ge-*.
Thus Épinal *giroefan* 'reeves' corresponds to Erfurt and Corpus
*geroefan*, whereas Épinal *gesuirgion* 'cousins' corresponds to Erfurt
*gisuirgian* and Corpus *gesuigran*. In another Épinal example Sweet
reports correction of the initial vowel from *i* to *e*. A correction
in a manuscript is not itself a dated phonological change. These related
glossaries transmit inherited material, not independent replications of
nine separate sound laws
[@Toller1921, p. 284, s.v. ge-;
@Sweet1885, pp. 48--49, 51, 53, EE 189--214 and Corpus 439, 503, 505,
517, 520, 522, 524--525, 530].

The familiar *gidyrstig* 'bold' has Erfurt *gedurstip* and Corpus
*gedyrstig* beside it. Sweet prints Épinal *gibeataen* 'beaten', not
the handbook's vowel-length-normalized form, beside Erfurt *gebeatten*
and Corpus *gebeaten*. Corpus is not categorically *ge-*:
*gibrec* occurs there too. Épinal *gybyrdid* 'born' has *ge-* in the
related witnesses; *y* in that spelling alone does not establish a
separate rounded-vowel sound law. The exceptional Erfurt *gaeadun*,
beside Épinal *gibiodun* and Corpus *geeodun*, deserves scrutiny, but
does not securely attest an unraised short \emph{*æ} after an already
palatal fricative: the root is vowel-initial, and transmission,
vowel quantity and the consonant's value remain material uncertainties
[@Sweet1885, pp. 39--40, 43--44, 50--51, 107, EE 76, 81, 140, 228,
Corpus 78, 245, 265, 487, 2152;
@Toller1921, p. 284].

The dates of copies must be distinguished from their linguistic layers.
The modern catalogue places Épinal around or just before 700 and
Corpus in the first half of the ninth century, revising the older
absolute dates. Corpus is an expanded revision of a precursor of
Épinal--Erfurt, not an unrelated later sample. The conventionally
Mercian attribution does not securely localize every gloss; Erfurt's
continental copying introduces an additional source of interference.
Its manuscript dating is inconsistent in the older accounts and does
not date its early English exemplar
[@LucasLucas2012, p. 67; @Lucas2016, p. 11;
@Sweet1885, pp. 3--4; @HoggGrammar2011, pp. 5--6].

The distribution extends beyond these glossaries. Early Northumbrian
runic *gistiga* 'climb into/onto' supplies an actual early *gi-* spelling.
The Vespasian gloss has *geseted* 'set' beside *bibod* 'command'.
Alfredian West Saxon *gemynd* 'mind' and *geðencean* 'remember'
contrast with much later Northumbrian *giher* 'hear' and *gitrivadon*
'we trust' in the Durham Ritual. These are different textual and
regional traditions, not successive observations of one speaker
population. Hogg explicitly recognizes both early spelling confusion
and late Northumbrian *i* spellings, including the possibility of a
raised allophone. The best description is a historically motivated
weak-vowel development whose surviving distribution also reflects
variety, orthography and transmission, not a universal date after which
every *gi-* became *ge-*
[@Sweet1885, pp. 125, 188--189; @Sweet1871, p. 3;
@Stevenson1840, p. 7, collects 2--3;
@HoggGrammar2011, pp. 4--7, 238--239, §§6.53--6.54].

## Regular reconstruction and prosody

The adopted English reconstruction comprises several changes, not an
immediate replacement of \emph{*a} by \emph{*e}. Ordinary unstressed
fronting independently supplies \emph{*æ}. Campbell distinguishes
fronting from the later merger; Ringe and Taylor explicitly consider
regular raising of pretonic \emph{*æ} after a palatal fricative.
Raising in this short weak vowel is compatible with the preceding
high front articulation. That phonetic motivation does not establish
the exact intermediate height from the spellings themselves.
The regular account adopted here is fronting, palatalization, raising
and later lowering, never a sound law conditioned by prefix identity
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

In the adopted reconstruction the vowel raises because it is short,
pretonic and immediately follows
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
account. The preference is not independent proof of every part of the
pathway. The precise date of raising and its independently attested
breadth remain less secure than the existence of *gi-* and *ge-*:
no independent non-*ga-* word sharing the complete early environment
has yet supplied a positive comparison
[@RingeTaylor2014, p. 335; @Berg2014, pp. 60--61].

The evidence is wider than one derivation but narrower than independent
confirmation in several unrelated phonological environments. All these
words repeat the inherited weak syllable. No securely dated example
sharing its full early short-vowel and palatal-fricative environment
has been shown to escape raising. Conversely, the mixed spelling record
does not establish a distinct phoneme for every written vowel.
The English *gi-* evidence is not exclusively Northumbrian.
Hogg places the later lowering of unstressed *i*, including *be-* and
*ge-*, marginally after the earlier front-vowel merger. Accordingly
[SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) merges weak
\emph{*æ} with \emph{*e}, while
[SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) subsequently lowers
pretonic \emph{*i}. Neither process changes a stressed root vowel
[@RingeTaylor2014, pp. 334--335;
@HoggGrammar1992, §§6.50--6.54 (held 2011 reprint, pp. 237--239)].

The formal domain is deliberately bounded: an initial short weak
syllable with a consonantal bridge to a positively headed syllable.
It admits onsetless and clustered onsets, but does not infer a weak
syllable from a missing accent. Hiatus, two pretonic syllables, long
weak vowels and internal weak syllables in more complex compounds
require independently justified prosodic analysis; the formula is not
a complete parser for all such words. The internal *gi-* of *modgidanc*
'thought' is therefore evidence about spelling, not automatic proof
of the same word-initial domain. Nor does the evidence license
extending raising indiscriminately to every palatal consonant
[@Sweet1885, p. 149; @RingeTaylor2014, p. 335;
@MinkovaZhou2022, pp. 535--536;
@RieggerBogelWalkden2024, pp. 2065--2068].

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
late vowel but leaves early *gi-* unexplained unless a further regular
phonetic or orthographic account is supplied. Hogg's later allophonic
possibility does not independently establish an alternative pathway for
all the earliest *gi-* evidence. No source examined establishes a more
discriminating regular alternative or positive *bi-* substitution.
The proposed \emph{*æ > i} remains a preferred, qualified reconstruction:
the distribution establishes the spellings more securely than their
precise early vowel quality or chronology. This evidential distinction,
not agreement with one final form, justifies retaining the staged account
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

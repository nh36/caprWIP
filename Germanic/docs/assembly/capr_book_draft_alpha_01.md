\mainmatter

# Introduction

## Sound laws as explicit derivations

This book is about a familiar historical-linguistic practice made explicit enough that it can be checked mechanically. Historical linguists have long described the history of languages through ordered sound laws, inherited morphological forms, lexical comparison, and exceptions that turn out to require other explanations [@OsthoffBrugmann1881]. A form is accepted as inherited when its phonological shape follows from the reconstruction and the relevant history of the branch. A form becomes suspicious when the expected development fails. The method is old; the difficulty is that its moving parts are numerous. Once a project contains hundreds of lexical items and dozens of ordered changes, even a careful scholar can lose track of what follows from what.

CAPR, computer-assisted phonological reconstruction, is one way to make this situation tractable. It supplements the comparative method by forcing a proposed historical phonology to take the form of explicit rules that can be applied to concrete reconstructed inputs. A rule either produces the expected output in a particular word or misses it. A rule can be moved earlier or later in an ordered sequence, and the lexical consequences of that movement can be inspected. A proposed input form can be compared with the Old English target it is meant to explain. When the formal system fails, the failure often becomes the most useful part of the inquiry, because it tells us where the regular history ends and where analogy, lexical replacement, borrowing, dialect mixture, uncertain attestation, or a mistaken reconstruction must be considered.

The present book applies that idea to the development from Proto-Germanic and early West Germanic forms into Old English. The empirical object is modest enough to be inspected and large enough to be useful. The implemented Germanic pipeline currently derives the overwhelming majority of the Old English comparison forms in its dataset. Its remaining failures are documented exceptions, so the present write-up explains a stabilized system and leaves further phonological patching aside. It asks which sound changes are being modeled, why they stand in the order they do, which lexical items support those choices, and which words require lexical or morphological explanation beyond the regular cascade.

The book has three parts. This introduction explains the method, the empirical scope, and the conventions used in the following sections. The first main part presents the sound-change sequence itself. It gives the historical discussion, the formal rule, and the chronological evidence for the modeled changes. The second main part turns from the rules to the words. It follows individual lexical items, especially those whose derivation is philologically or morphologically informative, and asks what must be true of the reconstruction, paradigm cell, attestation, or analogical history if the Old English form is to be understood.

The two main parts answer different questions. The sound-change part asks how a coherent chronological system is built. The lexical part asks how that system accounts for individual words. A reader should be able to move in both directions. When a rule chapter says that a particular ordering is supported by *learn*, *field*, *soul*, or *shoulder*, the lexical entries show what those words require. When a lexical entry says that a form is regular, analogical, a reconstructed Old English target, or a known unmodeled exception, the sound-change chapters show what the regular expectation would have been.

## What CAPR formalizes

The central claim behind CAPR is deliberately simple. A regular sound change can be treated as a relation between strings. A reconstructed form is given as an input string. An ordered sequence of sound changes maps that input to an output string. If the output matches the relevant Old English form, the derivation is successful at that level. If it fails, the failure has to be explained.

The string relation is literal. The formal background for treating phonological rules as finite-state relations is the regular-model approach to phonological rule systems developed by Kaplan and Kay [@KaplanKay1994]. In the implementation, a sound change is written as a finite-state transducer. A rule has a target, an output, and a conditioning environment. A series of rules is composed into a larger transducer. The resulting cascade represents a historical phonology. The details of the syntax matter for implementation, but the linguistic idea is the ordinary one. The formal rule is a way of making explicit what a historical grammar already says in prose.

A simple toy rule looks like this.

```foma
define ToyFinalZLoss [{*z} -> 0 || _ .#.];
```

This toy rule is only a compact illustration of the form of an explicit sound law. It says that starred \emph{*z} is deleted before the end of a word. It has a target, an output, and an environment. Real rules, written in the Foma finite-state toolkit, are often more complex [@Hulden2009]. They may refer to classes of vowels or consonants, stress, syllable weight, word boundaries, or previously defined transducers. The important point is that the prose statement and the formal statement remain accountable to one another.

A CAPR history has two kinds of structure. First, there is a phonological inventory and phonotactic definition for possible ancestral forms. The system must know what counts as a possible input. Without that restriction, backward reconstruction produces many formally possible but linguistically absurd ancestors. Second, there is an ordered list of changes. The order matters because many sound changes feed or bleed one another. If an early change creates the environment for a later change, the order is feeding. If an early change removes the environment for a later change, the order is bleeding. Both relations are central to historical explanation.

The original CAPR work was designed for Burmish and made this point through a web interface that combined cognate assignment, forward projection, backward projection, and visual marking of forms that had become regular or irregular after a change to the transducers. The same methodological lesson carries over to Germanic. A formal system is useful because it makes the consequences of a proposal immediate. A new rule can make a formerly irregular item regular. It can also break a word that used to work. Both outcomes are evidence. The researcher still decides what the evidence means.

For Old English, the input side of the problem differs from the situation in a young or poorly documented language family. The comparative and philological literature is deep. The grammar of Old English has been described repeatedly, and the earlier Germanic stages have been reconstructed with great sophistication by many scholars [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018]. That makes the formal implementation more demanding. The model must respect well-known handbooks and etymological dictionaries, and it must also explain its own deviations from citation forms when a particular paradigm cell is needed to reach the attested Old English comparison form [@Orel2003; @Kroonen2013].

## Scope of this book

This book gives a formal account of a particular historical path from Proto-Germanic and early West Germanic forms into Old English. The historical grammar comes from philology, comparative grammar, and the long tradition of work on Germanic and Old English [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018]. CAPR contributes a way of testing whether a large set of such claims can be made to cohere.

The lexical entries are selective accounts of the words that matter for the formal and historical argument. They do not attempt to give a full history of every English word, every Germanic cognate set, or every semantic development. Some entries are short because the derivation is ordinary. Some are longer because the comparison depends on a paradigm cell, an analogical form, a dialectal or attested variant, or an inherited form that differs from the dictionary citation form.

The model includes morphology where it is necessary to choose the relevant input. It includes orthography where the model must map phonological outputs to Old English surface forms. It remains a targeted derivational model with a narrower scope than a full parser of Old English, a full generator of paradigms, or a theory of all Old English variation.

The most important limitation is also one of the method's strengths. A deterministic sound-change model should keep irregularity visible. If a form is analogical, borrowed, dialectally mixed, or outside the regular path, it should remain visible as such. A model that explains too much by inventing small ad hoc sound laws has ceased to be useful. The aim is to show exactly which words are regular under a stated history, and what kind of explanation the others require.

## Why formalization helps historical linguists

The traditional comparative method already contains an implicit formal discipline [@OsthoffBrugmann1881; @SimsWilliams2018b]. When we say that Proto-Germanic \emph{*p} gives Old English \emph{f}, or that West Germanic \emph{*z} becomes \emph{r} in the relevant environment, we are describing a relation between earlier and later forms. When we say that a change must precede another change, we are making a claim about the ordering of operations. When we reject an etymology because it would produce the wrong vowel or consonant, we are using a mental derivation.

The problem is scale. A small derivation can be checked by hand. A single famous etymology can be discussed in a footnote. A network of hundreds of lexical items and many ordered sound changes is different. Sims-Williams's discussion of mechanising historical phonology makes this point directly, showing how explicit forward application of sound changes can uncover new cognates and sharpen relative chronology [@SimsWilliams2018a; @SimsWilliams2018b]. Errors can persist because each local step is familiar while the whole path is not inspected at once. A reconstruction may be plausible in isolation but fail after three later rules apply. A rule may work in the example for which it was introduced but damage other words. A relative chronology may seem harmless until a witness form forces a different order.

Formalization helps by turning these implicit derivations into inspectable objects. Judgment remains central, but it moves to explicit decisions about the input form, the source evidence, the interpretation of an Old English spelling, the status of a mismatch, and the historical reality of a narrow formal rule. The computer supplies consistency. It applies the rules as written, in the order given, to all relevant forms. It applies conditions uniformly, keeps every word in view, and preserves inconvenient consequences.

This is why CAPR is especially useful in the middle stage of historical work. At the beginning, one may not know enough to formalize much. At the end, one may imagine that the grammar is settled. In the middle, the investigator has many plausible sound changes, many reconstructed forms, and many lexical comparisons, but their interaction is unclear. A formal cascade creates pressure. It asks every part of the hypothesis to meet every other part.

## The Germanic and Old English case

The present Germanic model begins from Proto-Germanic and West Germanic reconstructions and derives Old English comparison forms through an ordered sequence of changes [@RingeTaylor2014; @Fulk2018]. The sequence includes large familiar developments such as West Germanic rhotacism, Anglo-Frisian brightening, breaking, i-umlaut, high-vowel apocope, and r-metathesis. It also includes smaller steps that matter because they fix particular derivations. Some changes are broad historical processes. Others are narrow formal notes whose value lies in a small group of witness forms.

The empirical dataset contains hundreds of Old English comparison forms. The current project state treats the research phase as complete. The major phonological system has moved out of debugging, and the remaining mismatches are documented as exceptions. This status matters for the prose. The book should read as an explanation of a stabilized model, with the residual problems presented honestly.

The Old English case also brings morphology to the foreground. A dictionary citation form sometimes differs from the form that should be fed to the sound-change cascade. The attested Old English comparison form may correspond to a dative plural, a genitive singular, a present-tense verbal form, or another paradigm cell. If the wrong cell is chosen, the formal derivation may fail for reasons that have little to do with phonology. The lexical entries therefore distinguish the citation reconstruction from the actual transducer input. This distinction is crucial for forms such as [*sċuldrum*]{.iv lang=oe sort=sculdrum} 'shoulders, dative plural', where a plural case form gives the regular Old English target more directly than a singular citation form.

Old English spelling adds another layer. Some outputs are phonological forms. Some are orthographic normalizations. A form may be attested with a spelling that reflects dialect, manuscript practice, or later reshaping. The model must keep these questions separate. When the lexical section identifies an Old English target, it distinguishes attested forms, normalized forms, reconstructed Old English forms, and selected comparison forms. The formal derivation is strongest when the status of the target is clear.

The result is a model that is both stricter and more modest than a prose grammar. It is stricter because every rule must run. It is more modest because it has to say when an output is only a model output, when a lexical entry requires an analogical account, and when the evidence supports only an approximate placement in the sequence.

## Rules, forms, and accountability

The basic unit in the sound-change section is a rule. Each rule is presented with a historical discussion, a formal definition, and a prose explanation of what the definition does. The historical discussion explains why the change belongs in the grammar. The formal definition states the modeled operation. The chronology paragraph explains what happens if the rule is moved too early or too late, when such tests are informative.

The basic unit in the lexical section is a word or comparison form. Each entry begins with the relevant reconstruction, transducer input, Old English target, and derivation class. It then explains the comparative evidence, the Old English evidence, and the development from the selected input to the target. Complex entries may include paradigm comparison. Simple regular entries may not need one.

The relation between these two units is the main intellectual structure of the book. The rules are justified by the words. The words are explained by the rules. A sound law without lexical consequences is an empty formal gesture. A lexical derivation without an explicit rule sequence is too easy to adjust after the fact. CAPR brings the two kinds of claim into the same space.

This accountability is clearest when a rule is moved. Suppose a change currently stands before breaking. If it is delayed until after breaking, several words may produce the wrong outcome. Those words then become witnesses for a terminus ante quem. The change must have applied before breaking in the modeled sequence. If the same rule can be moved earlier with no effect on any checked form, the model has only a one-sided chronological constraint. The rule may still be historically real, and its placement may still be motivated by handbooks, branch history, or structural coherence. The checked forms by themselves fix only part of its position.

This distinction recurs throughout the sound-change section. Some rules have tight two-sided evidence. Some have a close relation on one side and a broad interval on the other. Some are placed chiefly because the sources treat a development as belonging to a historical cluster, even though the checked forms leave the nearest neighbor unresolved. The prose tries to preserve these differences. A formal model can make chronology look sharper than the evidence warrants. The book therefore separates what the forms prove, what the sources motivate, and what the implementation chooses in order to keep a coherent cascade.

## Relative chronology

Relative chronology is one of the main reasons to formalize sound change. A sound law is rarely just a statement that one segment becomes another. It is also part of a history in which earlier outputs become later inputs. The order of changes determines whether a form survives, feeds a later process, escapes a later process, or becomes opaque.

The sound-change section uses lexical consequences to explain order. The argument comes from the derivational effect of moving the rule; the number assigned to it is only a reference handle. If a delayed rhotacism produces the wrong form for \emph{learn}, then \emph{learn} is evidence about the relative order of rhotacism and the later change that it must precede. If moving an unstressed-vowel rule earlier makes no difference to any checked item, then the earlier side of the rule is not fixed by the current lexical tests.

This method is powerful because it makes negative space visible. Traditional prose often says that one change came before another because the result requires it. CAPR can show how broad that requirement is. A rule may need to precede some later development, but that later development may be far away in the sequence. Such a result is real evidence, although weaker than local adjacency. Conversely, a rule may need to follow an earlier change because the earlier change creates exactly the environment that the later rule consumes. That is a stronger local relation.

The book therefore avoids symbolic order notation in the main prose. It uses ordinary temporal language such as before, after, earlier, and later, then gives the lexical forms that break when the order is changed. This keeps the chronology tied to historical evidence. The formal model supplies the test; the prose explains the linguistic reason.

Some changes remain approximate. This is unavoidable. Handbooks may agree that a development belongs to an early West Germanic stage without fixing its position relative to every other early change. A small rule may be needed for a particular group of forms but lack enough witnesses to anchor both sides of its chronology. A technical stage may be useful in the implementation while lacking the status of an ordinary historical sound law. The draft says so where relevant. Formalization should clarify uncertain history, not convert it into false precision.

## The lexical entries

The lexical section answers a different kind of question. A sound-change chapter may say that a rule is supported by a set of witness forms, but a reader also needs to know what those forms are doing. Is the Proto-Germanic input a citation form or a particular inflectional cell? Is the Old English target a headword, a normalized spelling, an attested variant, or a reconstructed form? Do the handbooks agree on the reconstruction? Does the derivation depend on regular sound change, analogy, or a known unmodeled development?

The lexical entries make those distinctions explicit. Each entry begins with a small amount of metadata because the reader needs to know the selected input and target. The entry then turns to historical prose. The expected structure is simple. First, establish the transducer input and output. Then compare the reconstruction and the relevant source evidence. Then establish the Old English evidence. Then explain the development to Old English. If the argument depends on morphology, add a paradigm comparison.

The model entry for \emph{shoulder} shows why this structure is needed. The ordinary Old English headword is \emph{sculdor}, but the relevant comparison form for the successful derivation is the dative plural \emph{sċuldrum}. The sources differ in the reconstruction and stem-class implications of the Germanic word. A dative or instrumental plural input of the type [*skúldramiz*]{.iv lang=pgmc display=*skúldramiz sort=skuldramiz} aligns with the inherited plural ending and produces the Old English target. A singular-oriented input answers a different question. The lexical entry is where the model's choice of input becomes philologically accountable.

The derivation classes help keep the entries honest. A \emph{regular} entry is one in which the selected input and the deterministic rule path produce the Old English target. An `early_analogy` entry uses an input that reflects reshaping before the modeled Old English path. A `late_analogy` entry often depends on a paradigm cell whose form was later generalized or otherwise analogically important. An `attested_variant` entry reaches a real Old English form that may differ from the default dictionary headword. A `reconstructed_oe` entry uses a reconstructed target when that is the useful comparison. A `known_unmodelled` entry names an understood historical process that falls outside the deterministic FST. An `unexplained_unmodelled` entry preserves a real problem without inventing a solution.

These labels are working categories for accountability, deliberately narrower than a typology of all historical change. They tell the reader what kind of explanation the entry is offering. They also prevent the regular system from being quietly expanded to cover phenomena that should remain outside the sound-change cascade.

## The role of failure

A failed derivation is often more informative than a successful one. If the system derives \emph{dæg} from the selected input by the expected sequence, the entry may be straightforward. If it derives \emph{sċoldor} when the relevant Old English form is \emph{sċuldrum}, the mismatch forces a question. Was the wrong input chosen? Is the relevant Old English form a different paradigm cell? Is an analogical development involved? Is the target itself wrong? Is the sound-change rule missing a condition?

CAPR is useful because it makes these questions concrete. A failure has a shape. The output differs in a particular vowel, consonant, ending, or orthographic normalization. That difference points toward a type of problem. A wrong root vowel may indicate an ordering issue or a stem-class issue. A wrong ending may indicate the wrong paradigm cell. A plausible but non-attested output may point to analogy. A form that works only by suppressing a general rule may be a loan or a dialectal intrusion.

The original CAPR Burmish work made this point through the automatic detection of loanwords. If a rigorous model of regular sound change fails for a word while succeeding for the inherited vocabulary around it, the failure can reveal a non-inherited item. The Old English case is different in detail, but the logic is the same. A good regular model isolates irregularity and keeps it visible.

This is why the remaining mismatches in the Germanic model are treated as documented exceptions, which closes the route of adding more phonology for its own sake. A model with a few well-understood failures can be better than a model that achieves total coverage through artificial rules. The governing question is whether each success and each failure has the right kind of explanation.

## Formalization and philology

The formal model and the philological sources have different strengths. The model is good at consistency. The sources are good at historical interpretation, attestation, dialect, morphology, and comparison. The book depends on both.

The rule chapters cite the major handbooks and specialist sources where they are needed. Hogg, Campbell, Ringe and Taylor, Fulk, Luick, Brunner, Kroonen, Orel, and others provide the historical grammar and etymological framework within which the formalization makes sense [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018; @Luick1914; @SieversBrunner1965; @Orel2003; @Kroonen2013]. The FST operationalizes claims from these sources and asks what follows.

The lexical entries likewise begin from dictionaries, grammars, etymological works, and the Old English record. Attestation requires source support beyond appearance as a model target. A reconstruction requires historical support beyond a successful transducer output. When sources differ, the entry should identify the point of disagreement, such as stem class, gender, root vowel, suffix, branch stage, paradigm cell, or Old English attestation. Vague language about "source disagreement" is too weak.

This division of labor also matters for uncertainty. A source may support the historical reality of a change without fixing its exact position in the modeled sequence. A transducer may require a formal step whose historical scope is smaller than its code name suggests. A lexical entry may reach the target only by choosing a morphologically specific input. These facts should be visible. The book's prose therefore tries to write neither as code documentation nor as unformalized narrative. It is historical-linguistic prose under formal constraint.

## The formal sequence

The sound-change section begins with early West Germanic consonant and vowel changes and ends with Old English r-metathesis. The numbering follows the CAPR sound-change inventory. The numbers are useful because they keep the prose, the FST, and the chronology tests aligned. The argument itself lies in the historical discussion, the formal rule, and the lexical consequences.

Several internal numbers are technical or weight-marking stages, and the inventory also contains a numbering gap. This is normal in a formal system. Some implementation steps help the model run without corresponding to a historical sound law that deserves prose treatment. The introduction flags this so that the reader expects discontinuity in the internal labels.

The assembled sound-change section now covers the active manifest-backed sequence from the early West Germanic material through r-metathesis. Its chapters differ in scale. West Germanic rhotacism, Anglo-Frisian brightening, breaking, i-umlaut, apocope, and r-metathesis are large historical developments familiar from the literature. Other chapters treat narrower matters, including vowel adjustments, final-vowel behavior, cluster simplification, and special contexts needed to keep witness words regular. The book preserves this unevenness because the history itself is uneven.

A formal sound-change chapter normally has three obligations. It must identify the historical development, show the formal rule, and say how the modeled order is supported. If one of these obligations is weak, the prose should say so. A rule may be historically secure but chronologically loose. A rule may be chronologically useful but lexically narrow. A rule may be a formal convenience whose historical interpretation is cautious. Such cases are useful precisely because formalization clarifies the evidence.

## The word-by-word sequence

The lexical section gives a complementary view of the same system. It begins from a word and consults the sound laws through the derivation. For each word, the reader sees the selected Proto-Germanic or early input, the Old English comparison form, the derivation class, and the path through the modeled sound changes. Where a word needs further discussion, a lexeme report explains the sources and the reasoning.

This organization is especially important because many words are formally regular but historically interesting. A word may derive successfully only because the selected input is a particular inflected form. A word may be regular in the phonology but require a note about the Old English target. A word may have a straightforward output but a complex comparative background. Conversely, a word may be phonologically uninteresting and need no extended report.

The selective-report policy reflects this. Ordinary regular rows with no note can remain short. Rows with a note, a non-regular derivation class, or a manually supplied report need fuller discussion. The point is to spend attention where the historical argument needs it. A complete book should spare the reader identical descriptions of regular derivations while also explaining difficult words in prose.

The lexical section can therefore be read in two ways. It can be read as a derivation report, showing how the system maps inputs to outputs. It can also be read as a set of philological case studies. The second use is the more important for publication. A formal output is only as good as the input and target it connects. The lexical entries show why those inputs and targets were chosen.

## How to read the formal notation

The book uses several kinds of notation. Reconstructed forms are marked with an asterisk and usually appear in emphasis. Old English forms appear in emphasis in ordinary prose. FST rule names appear in the rule headings and in cross-references. Formal code appears in fenced `foma` blocks. The code blocks are the place where implementation details are visible. The surrounding prose explains the linguistic content.

The formal code should be read as a compact version of a historical claim. A line such as a vowel change before a particular class of following segments means that the model applies the change wherever the stated environment is met. If the rule is too broad, it will damage words. If it is too narrow, it will fail to derive words. If its order is wrong, it may feed or bleed later rules incorrectly.

The derivation tables in the lexical section divide the path into earlier Germanic developments and Old English developments. This division is sometimes approximate, but it helps the reader see the architecture of the model. Some words pass through many changes. Others pass through almost none. The absence of a change in a given word is as important as its presence, because it shows that the rule's environment was absent.

The book avoids treating formal labels as historical explanations by themselves. A label such as `OEIUmlaut` is a reference handle. The explanation lies in the surrounding prose, the code, and the witness forms. This is why the rule chapters give ordinary titles as well as FST names. The reader should be able to understand the linguistic development before inspecting the code.

## What counts as success

A successful derivation is one in which the selected input, passed through the ordered sound-change cascade, yields the target form. That statement needs unpacking. The input must be historically defensible. The target must be identified correctly. The rule path must be regular under the model. A success that depends on a bad input or an uncertain target has only formal value.

For this reason, the book treats success as layered. A purely formal success means that the transducer output matches the target string. A philological success means that the input and target are the right objects to compare. A historical success means that the derivation also makes sense in the broader evidence of Germanic and Old English. Many entries satisfy all three. Some satisfy only the formal condition and therefore need more explanation.

The reverse is also true. A formal failure can be historically informative. If the attested Old English form is analogical, a regular sound-change model should fail to derive it from the inherited input. If the target is a dialectal or later variant, the failure may reflect the limited scope of the modeled path. If a word is borrowed, the inherited cascade is the wrong explanation. Such cases are successful diagnoses when they are labeled correctly.

The derivation classes are therefore part of the argument. They keep different kinds of success and failure apart. A `known_unmodelled` item has a different status from an unexplained mismatch. A `late_analogy` item has a different status from a regular sound-change witness. A `reconstructed_oe` target has a different status from direct attestation. These distinctions make the book more cautious, but also more useful.

## Why a book is needed

CAPR is a database and a set of tools, but the present work also needs book prose. A database can tell us that an output matches or fails. It can store traces, classes, notes, and citations. Prose explains why a particular comparison matters, why a rule is historically plausible, and why an apparently small mismatch changes the analysis of a word.

The prose also lets the reader see the scale of the argument. In a table, a rule with one decisive witness and a rule with dozens of familiar examples may look similar. In a book, the difference can be stated. A narrow note can remain narrow. A broad historical change can be given fuller context. A rule whose placement is source-based can be marked as such. The written form prevents the formal system from projecting false symmetry.

The book format also makes the work contestable. A reader can disagree with a source interpretation, a selected input, a rule environment, or a derivation class. Because the claims are explicit, such disagreement has a place to attach. The ideal outcome is a set of decisions public enough to be corrected.

## Scope and limits of the present draft

The present draft reflects a stabilized phase of the Germanic-to-Old-English work. The main sound-change system is treated as fixed for publication purposes unless a serious error is found. The active work is writing the sound-change chronology, explaining lexical derivations, and making the relation between formal output and philological evidence clear.

The system remains open to future improvement. A future version may add more lexeme reports, improve bibliography, refine the treatment of morphology, or extend the model to dialectal variation. A future version may also separate some compact rule groupings or rewrite some chapters in fuller historical prose. The present book has a narrower goal. It offers a coherent account of the current model and the lexical evidence that matters most for understanding it.

The lexical write-up is also at a different stage from the sound-change write-up. The sound-change sequence has received sustained prose review. The lexical section contains a mixture of generated derivation views and manifest-backed production reports. This introduction is written to support the intended combined draft, which will contain an opening methodological section, a formal chronology section, and a word-by-word section. It should be revised after the combined PDF has been read as a whole.


## A small example of rule evidence

It may help to spell out the logic of a chronology test without making the introduction depend on any one rule. Imagine a rule that changes an inherited consonant before a later vowel development. If the consonant change applies first, the later vowel rule sees the right environment and the word reaches its Old English target. If the consonant change is postponed, the later vowel rule misses that environment, and the output has the wrong vowel. The word is then evidence that the consonant change must be earlier than the vowel rule.

The same reasoning also works in the other direction. If a rule creates a segment that a later rule would incorrectly alter, the rule must be placed after that later rule or else the derivation breaks. If a rule can be moved through a large stretch of the sequence without altering any checked form, the current lexical evidence leaves its position inside that stretch open. The rule may still belong there historically, but the book should report the limit of the order test.

This way of arguing is close to ordinary historical grammar. What CAPR adds is exhaustive application within the chosen dataset. A scholar can always test a rule against one or two examples by hand. The formal system tests it against the whole active set of comparison forms. The resulting evidence may confirm the expected history, expose a bad environment, or reveal that a traditional explanation is correct but less tightly ordered than the prose had suggested.

The recent revision of the sound-change chapters was largely an exercise in this kind of discipline. Earlier wording sometimes treated a broad interval as if it were a close local boundary. The revised prose says more carefully when the checked forms establish only a later relation, only an earlier relation, or a wide range within which source-based placement is still needed. This strengthens the argument by separating evidence from presentation.

## Morphology as part of the input

A sound-change model can only derive the form it is given. This fact is obvious in computation and easy to overlook in etymological prose. A dictionary headword is often a useful citation form, but a real Old English comparison may descend from a particular inflected form. Nouns have case and number. Verbs have tense, mood, person, and number. Stem classes and suffixes matter. If the input form has the wrong ending, the phonology may produce the wrong word for the right historical reason.

The Germanic model therefore distinguishes the citation reconstruction from the selected transducer input. The citation reconstruction identifies the lexical family. The input form identifies the form whose regular development is being tested. Sometimes these are the same. Sometimes they diverge. When they diverge, the lexical entry has to explain why the selected input is legitimate.

This distinction is especially important for analogical cases. A late analogical form may be phonologically regular from a particular paradigm cell while the citation form gives a different result. The entry must then show both sides of the argument. It must say what the ordinary citation comparison would produce, why that output misses the Old English target, and why the chosen cell or reshaped form is a plausible historical source for the attested form. A table of outputs can make the difference clear, while the historical interpretation belongs in prose.

The same point applies to early analogy. If a form was already reshaped before the modeled Old English sound changes, the model should begin from the reshaped input. This is legitimate when the reshaping is independently motivated and stated plainly. A silent adjustment of the input merely to make the output work would be illegitimate. The lexical entries expose the chosen input and ask whether it is historically defensible.

## Orthography and surface form

Old English orthography is another reason why derivational success has to be interpreted carefully. The model may produce a phonological output that then requires orthographic normalization. Some outputs contain symbols used internally by the model to represent phonetic or phonological values. Some Old English targets are normalized editorial forms. Some spellings are dialectal, manuscript-specific, or late. A visible spelling mismatch can be compatible with phonological success, and a visible spelling match may still need historical explanation.

The orthography-and-surface part of the derivation report records the final mapping from model output to Old English comparison form. In simple cases this is almost trivial. In others, it is where the reader sees that the regular phonology has produced a form that still needs editorial interpretation. The lexical entries then decide how much of that interpretation matters for the historical argument.

This matters because computational systems are exact about strings. A human reader may see immediately that two spellings are equivalent for the purpose at hand. The program needs that equivalence to be encoded. Exactness is useful when it catches real problems, but unhelpful when it mistakes notation for history. The book therefore treats orthographic normalization as a distinct layer. It is part of the pipeline and distinct from sound change.

## Loanwords, analogy, and the boundary of the regular

The Neogrammarian commitment to regular sound change is often misunderstood as a claim that every word must obey the same history [@OsthoffBrugmann1881]. In practice, the point is methodological. If sound change is regular, then departures from the regular path are meaningful. They may indicate borrowing, analogy, expressive reshaping, dialect mixture, textual variation, or error. The regular model is the instrument that lets us see those departures.

In the original Burmish CAPR setting, this logic made loanwords stand out. A word that resisted derivation by the inherited sound changes, while its neighbors succeeded, became a candidate for borrowing. In the Old English setting, analogy is more often the central issue. A word may be inherited, but the attested form may reflect leveling from another paradigm cell. A form may preserve a vowel because of a morphological environment that the simple citation form lacks. A verb may require a finite form as input because the infinitive citation form answers a different question.

The book therefore treats the boundary of the regular as a positive result. A known unmodeled item is resolved when the relevant process is named and supported. An unexplained unmodeled item remains a problem, but it is a contained problem. A lexeme retargeting is a substantive historical claim that the previous cognate or target assignment was inferior. These categories keep the non-regular material visible without letting it dissolve the regular grammar.

## Local decisions and global coherence

A historical grammar is often written locally. One chapter discusses breaking. Another discusses i-umlaut. A dictionary entry discusses a word. Each discussion may be correct in isolation. CAPR asks whether all of them can be true at once. This is the global question.

Global coherence allows rules with different status. A model can contain major rules, minor rules, technical stages, and lexical exceptions. The key requirement is that the interaction among them has been tested. A change that works only because an earlier rule has already removed a segment has a different status from a change that can float across twenty positions unnoticed. A word that supports a local order relation carries more chronological weight than a word that merely remains regular throughout a broad interval.

The introduction of explicit rules also encourages a useful kind of humility. It is easy to write prose that sounds settled. It is harder to write code that derives the forms. When the code fails, the prose must change. When the code succeeds too easily because a rule is overbroad, the prose must also change. The formal model is a check on the coherence of philological claims and remains subordinate to philology.

## Reproducibility and disagreement

One of the most important virtues of a formalized reconstruction is that it can be disagreed with precisely. A reader may think a rule is too broad. A different reader may accept the rule but reject its order. Another may object to the selected input for a particular lexical item. Another may think the Old English target has been normalized too aggressively. These are productive disagreements because each one points to an explicit part of the system.

Purely narrative accounts can leave more work implicit. If a grammar says that a development "regularly" gives a certain form, the reader may have to reconstruct the intermediate steps mentally. If an etymological note says that a word is analogical, the relevant paradigm comparison may remain implicit. CAPR aims to make those hidden steps public.

The model remains scholarly and inspectable. Every formalization reflects decisions about the inventory of symbols, the segmentation of forms, the selected reconstructions, the ordering of changes, the treatment of morphology, and the interpretation of Old English evidence. The point is that these decisions are recorded in a way that lets others inspect them. Reproducibility here means the reproducibility of consequences. Given these inputs and these rules in this order, the stated outputs follow.

## From tool to argument

The project began as a tool, but the book must become an argument. Its argument is that traditional rule-based reconstruction gains clarity when its derivations are made explicit. The Old English material is a historically rich case in which the strengths and limits of formalization can be seen.

The sound-change section argues that a large part of the Proto-Germanic to Old English path can be represented as an ordered sequence of explicit rules, with the relative chronology supported by identifiable lexical consequences. The lexical section argues that individual words can be made accountable to that sequence without erasing the philological complexity of reconstruction, attestation, and analogy. The introduction argues that these two forms of accountability belong together.

The book should be judged by both standards. If the formal system derives the words while the prose hides uncertainty, it fails as historical linguistics. If the prose is philologically subtle while the formal system fails to reproduce the derivations, it fails as a formal account. The goal is to hold both demands at once.

## How the parts fit together

The introduction gives the reader the method. The sound-change section gives the rule sequence. The lexical section gives the word evidence. None of the three is complete without the other two.

The method matters because formal derivations can look forbidding without an explanation of their purpose. The rule sequence matters because lexical entries can become arbitrary without an explicit sound-change history. The lexical entries matter because a rule sequence can become detached from evidence unless it is held against actual words.

A reader interested primarily in historical phonology should begin with the sound-change section, then follow the cross-references into the lexical entries. A reader interested in an individual Old English word should begin with the lexical entry and then consult the rule chapters for the changes mentioned in the derivation. A reader interested in computational method should read the whole book as an example of how a traditional historical grammar can be made operational without surrendering philological judgment.

The aspiration is practical. Historical linguistics already has a rich tradition of rigorous argument. CAPR gives that tradition a test bench. It lets us ask whether the rules we say we believe actually derive the words we claim they derive, in the order we claim they occurred. That question is simple. Answering it carefully is the work of the book.

\part{Sound changes, formalization, and relative chronology}

# The ordered sound-change sequence

## Scope and orientation

This section follows a continuous sequence from early West Germanic consonant and vowel changes to the Old English developments that culminate in r-metathesis.

Some chapters treat large familiar changes such as rhotacism, brightening, breaking, umlaut, and apocope. Others are smaller ordered notes whose importance lies in the witness words that fix the sequence.

Not every numbered step has the same historical weight. Each section either represents a meaningful change of its own or helps explain why neighboring changes stand where they do.

### Numbering note

The rule numbers follow the CAPR sound-change inventory so that each chapter remains traceable to the implementation and the chronology tests.

A few internal numbers do not become sound-change chapters. SC038, SC062, and SC084 are technical or weight-marking stages, and SC077 is a numbering gap.

## West Germanic rhotacism

### Historical discussion

Hogg states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Hogg1992, p. 37]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

That historical label matters here. CAPR keeps the implementation name [SC003 PGmcRhotacism](#rule-PGmcRhotacism), but the historical change treated in this chapter is a later West Germanic rhotacism, not a Proto-Germanic one. It must also remain distinct from [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant is turned into \emph{*r}.

### SC003. West Germanic rhotacism (`PGmcRhotacism`) {#rule-PGmcRhotacism}

The implementation keeps the rhotacism step explicit.

```foma
define PGmcRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

In prose, the rule turns surviving medial \emph{*z} into \emph{*r} in the West Germanic line. CAPR keeps the label [SC003 PGmcRhotacism](#rule-PGmcRhotacism) for the modeled rewrite, but the historical interpretation is later than the name suggests.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*líznōjaną} yields *lirnian* rather than expected OE *liornian* ‘learn’, PGmc \emph{*líznōθi} yields *lirnaþ* rather than expected *liornaþ*, PGmc \emph{*líznô} yields *lirna* rather than expected *liorna*, and PGmc \emph{*mízdai} yields *merde* rather than expected OE *meorde* ‘meed’. This shows that [SC003 PGmcRhotacism](#rule-PGmcRhotacism) must come before [SC044 OEBreaking](#rule-OEBreaking) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat West Germanic rhotacism as a later development after the earlier \emph{*z}-loss material described above.

\newpage

## Proto-West-Germanic ai-monophthongization

### Historical discussion

Ringe and Taylor treat the reduction of unstressed \emph{*ai} as one of the major early vowel shifts shared across the Northwest Germanic area [@RingeTaylor2014, pp. 40--41].

That historical support is strongest for the unstressed and especially word-final side of the change. CAPR makes a wider inherited \emph{*ai} treatment explicit in one rule, but the broader nonfinal \emph{*ai > *ā} side is more sharply packaged in the implementation than in the current handbook discussion.

### SC004. Proto-West-Germanic ai-monophthongization (`PWGmcAiMonophthongization`) {#rule-PWGmcAiMonophthongization}

The implementation keeps the monophthongization step explicit.

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

In prose, the rule monophthongizes inherited \emph{*ai}. The clearest source support is for the word-final unstressed outcome, where \emph{*ai} merges with long mid \emph{*ē}; CAPR then keeps the broader inherited \emph{*ai} treatment visible in the same modeled step.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’. This shows that [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the broader inherited \emph{*ai} treatment here because the clearest source support places unstressed \emph{*ai} reduction among the early Northwest Germanic vowel shifts.

\newpage

## Unstressed \emph{*a}-raising before final \emph{*m}

### Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise treats the development of early unstressed \emph{*o} to \emph{u} before \emph{m} as one of the important similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

That makes this a small but real unstressed-vowel development in inflectional material. It belongs here as a short morphophonological note, and the strongest evidence concerns noninitial unstressed material before final \emph{*m}. The internal CAPR label is narrower and more technical than the title used here.

### SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`NWGmcAToUBeforeM`) {#rule-NWGmcAToUBeforeM}

The implementation keeps the pre-\emph{*m} raising step explicit.

```foma
define NWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

In prose, the rule raises unstressed noninitial \emph{*a} before final \emph{*m} in ending material. It preserves a narrow morphophonological step that remains visible in the `shoulder` family, but the historical case is broader than that single compact-trace witness because the strongest support comes from inflectional endings.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*skúldramiz} yields *sċoldrum* rather than expected OE *sċuldrum*. This shows that [SC005 NWGmcAToUBeforeM](#rule-NWGmcAToUBeforeM) must come before [SC017 NWGmcULowering](#rule-NWGmcULowering) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources place pre-\emph{*m} unstressed \emph{u} inside the same early ending history. The note remains a small inflectional development, not a broad lexical sound law.

\newpage

## Early i-apocope

### Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* and *geogup* examples belong to the same pattern [@Campbell1959, §332].

This is therefore a specific kind of final-vowel loss. The crucial point is that the ending vowel disappears in a weak suffixal environment early enough to block later umlaut. That anti-umlaut timing is the historical center of the rule.

### SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

The implementation keeps the early apocope step explicit.

```foma
define PWGmcEarlyIApocope [
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
];
```

In prose, the rule deletes final \emph{*i} in remote unstressed syllables. That timing matters because later umlaut no longer sees the lost ending vowel, which is why forms like *geoguþ* ‘youth’ preserve the expected vocalism.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*skáwōθi} yields *sċēaweþ* rather than expected OE *sċēawaþ*. This shows that [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope) must come before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat this suffixal loss as an early step in the ending history before the later diphthongal developments.

\newpage

## Final \emph{*ō}-lowering before \emph{*r}

### Historical discussion

Ringe and Taylor treat the West Germanic lowering of final bimoric \emph{*ō} before word-final \emph{*r} as a specific inherited development and illustrate it above all with the families behind *fēower* ‘four’ and *wæter* ‘water’ [@RingeTaylor2014, pp. 58--59].

That makes the rule historically real, but narrow. This is not a broad long-vowel chapter. The relevant environment is final or pre-final \emph{*ō} before word-final \emph{*r}, and the clearest evidence remains concentrated in the `four` and `water` material.

### SC007. Lowering of final bimoric \emph{*ō} before \emph{*r} (`PWGmcFinalOrLowering`) {#rule-PWGmcFinalOrLowering}

The implementation keeps the final-\emph{*ō} lowering step explicit.

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

In prose, the rule lowers final bimoric \emph{*ō} before word-final \emph{*r}. This is the adjustment that lies behind the West Germanic vocalism of *fēower* ‘four’ and *wæter* ‘water’.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*wátōr} yields *water* rather than expected OE *wæter* ‘water’. This shows that [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the `four` and `water` material belongs to the same early West Germanic final-vowel history described above.

\newpage

## Coronal-w assimilation

### Historical discussion

Ringe and Taylor treat the assimilation of `*dw` and `*zw` to `*ww` as a shared Proto-West-Germanic innovation and support it through the `four` family and plural-pronominal forms such as `you` and `your` [@RingeTaylor2014, pp. 56--57].

That historical support is real, but the witness set is small. CAPR models both coronal inputs explicitly before \emph{*w}, while the historical prose should keep the reader's attention on the narrow cluster of forms that actually supports the change.

### SC008. Assimilation of coronal consonants before \emph{*w} (`PWGmcCoronalWAssimilation`) {#rule-PWGmcCoronalWAssimilation}

The implementation keeps the coronal-w assimilation step explicit.

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

In prose, the rule assimilates coronal consonants before \emph{*w} so that the sequence behaves as \emph{*ww}. The lexical evidence is concentrated in the pathway to *fēower* ‘four’, while the pronominal material shows that the change is not confined to one isolated noun.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*fédwōr} yields *fēowwer* rather than expected OE *fēower* ‘four’. This shows that [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) must come before [SC031 OEWWSimplification](#rule-OEWWSimplification) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the `four` and pronominal material places this assimilation in the same early West Germanic cluster before the later diphthongal developments.

\newpage

## \emph{ij}-contraction in \emph{friend}

### Historical discussion

Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc \emph{*frijond-} > PWGmc \emph{*friund} > OE *frēond* 'friend' [@RingeTaylor2014, p. 62]. The same source immediately warns that the `*ijo` sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62].

That narrowness is part of the history. This is a short lexical sound-change note on a rare sequence in the `friend` family, and it belongs in a continuous account of the early sequence even though it is not a broadly productive rule.

### SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

The implementation keeps the contraction step explicit.

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

In prose, the rule contracts the rare \emph{*ijō} sequence in the family behind OE *frēond* 'friend'. The section belongs here because a continuous account of the early sequence should explain that development openly, even though the source base remains effectively one family.

Its chronology is useful but one-sided. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If it is delayed until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*fríjōndz} yields *friund* rather than expected OE *frēond*. This shows that [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) in the modeled sequence.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat the `friend` development as a narrow early change within the same sequence. It remains a one-family note, not a productive sound law. From here the sequence passes into the tighter local seam between [SC010 PWGmcJGemination](#rule-PWGmcJGemination) and [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ).

\newpage

## West Germanic j-gemination

### Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

That historical support is good, but the environment must stay explicit. This is not a general chapter on doubled consonants. The relevant setting is a short vowel before \emph{*j}.

### SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

The implementation keeps the j-gemination step explicit.

```foma
define PWGmcJGemination [
    {*p} -> {*p} {*p} || EnglishStarShortVowel _ {*j},
    {*b} -> {*b} {*b} || EnglishStarShortVowel _ {*j},
    {*t} -> {*t} {*t} || EnglishStarShortVowel _ {*j},
    {*d} -> {*d} {*d} || EnglishStarShortVowel _ {*j},
    {*k} -> {*k} {*k} || EnglishStarShortVowel _ {*j},
    {*g} -> {*g} {*g} || EnglishStarShortVowel _ {*j},
    {*f} -> {*f} {*f} || EnglishStarShortVowel _ {*j},
    {*s} -> {*s} {*s} || EnglishStarShortVowel _ {*j},
    {*m} -> {*m} {*m} || EnglishStarShortVowel _ {*j},
    {*n} -> {*n} {*n} || EnglishStarShortVowel _ {*j},
    {*l} -> {*l} {*l} || EnglishStarShortVowel _ {*j},
    {*ŋ} -> {*ŋ} {*ŋ} || EnglishStarShortVowel _ {*j},
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}
];
```

In prose, the rule doubles consonants before \emph{*j} after a short vowel. It preserves one of the steps behind OE *nett* 'net' and related West Germanic outcomes in this narrow environment.

Its chronology is useful but asymmetric. If the rule is moved earlier within the tested range, no checked form yields a form different from the expected one. If [SC010 PWGmcJGemination](#rule-PWGmcJGemination) is delayed past [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), PGmc \emph{*nátją} yields *nete* rather than expected OE *nett* 'net'. This shows that [SC010 PWGmcJGemination](#rule-PWGmcJGemination) must come before [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ). The checked forms therefore fix the close relation between [SC010 PWGmcJGemination](#rule-PWGmcJGemination) and [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), but do not identify a corresponding earlier constraint. CAPR keeps the rule here because the sources treat West Germanic j-gemination as the consonantal step that must already be in place before the following syllabic-\emph{j} development.

\newpage

## Syllabic j after final-vowel loss

### Historical discussion

Ringe and Taylor state directly that after final unstressed `*a` and `*ą` were lost, postconsonantal `*j` became syllabic `*i`, with outcomes behind OE *here* 'army' and *rice* 'kingdom' [@RingeTaylor2014, p. 46].

That source support is good, but the compact trace layer contributes very little live evidence of its own. This therefore stays a modest singleton note. It does not expand into a broad chapter on high-vowel vocalization.

### SC011. Syllabic \emph{*j} after final-vowel loss (`PWGmcSyllabicJ`) {#rule-PWGmcSyllabicJ}

The implementation keeps the syllabic-j step explicit.

```foma
define PWGmcSyllabicJ [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
];
```

In prose, the rule turns postconsonantal \emph{*j} into syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} has been lost. It keeps explicit a small but historically real step behind forms such as *here* and *rice*.

Its chronology is mixed. If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) is moved before [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc \emph{*nátją} yields *nete* rather than expected OE *nett* 'net'. This shows that [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) must come after [SC010 PWGmcJGemination](#rule-PWGmcJGemination). If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one. The checked forms therefore fix the earlier relation between [SC010 PWGmcJGemination](#rule-PWGmcJGemination) and [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), but do not identify a corresponding later constraint. CAPR keeps the rule here because the sources treat syllabic \emph{*j} as the follower to final-vowel loss once the earlier consonant adjustments are already in place.

The source support is real, but the live trace remains thin. That is why the chapter stays narrow and does not turn into a broader discussion of high-vowel behavior.

\newpage

## \emph{lþ}-voicing

### Historical discussion

Ringe and Taylor treat word-internal \emph{*lþ} > \emph{*ld} as a regular sound change in northern West Germanic and illustrate it with forms such as *fealdan*, *beald*, *wuldor*, and *gylden* [@RingeTaylor2014, pp. 170--171]. Campbell gives a similar West-Germanic-facing formulation with examples such as *fealdan*, *wuldor*, *beald*, *gold*, and *feld* [@Campbell1959, p. 169, §414].

That makes the change substantial enough for a short chapter, but the scope should stay cautious. The internal CAPR implementation places the rule at this early stage, while the source discussion points most clearly to a northern West Germanic development. It does not support an unqualified pan-PWGmc law.

### SC012. \emph{lþ}-voicing (`PWGmcLThVoicing`) {#rule-PWGmcLThVoicing}

The implementation keeps the \emph{lþ > ld} step explicit.

```foma
define PWGmcLThVoicing [
    {*θ} -> {*d} || {*l} _
];
```

In prose, the rule voices \emph{*lþ} to \emph{*ld}. This is the development behind families such as `field`, `fold`, `gold`, and `wold`, while the historical discussion keeps the scope cautious about how widely the rule should be projected.

Its chronology is deliberately modest. If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC012 PWGmcLThVoicing](#rule-PWGmcLThVoicing) before or after any specific neighboring stage.

That does not make the change itself doubtful. The comparative evidence for northern West Germanic \emph{lþ > ld} is strong, so CAPR keeps the rule here as an early consonant note. The placement should be read as approximate and source-based, not as a local ordering forced by the checked forms. After this scope-limited note, [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) returns to a broader systemic consonant adjustment.

\newpage

## Dental hardening

### Historical discussion

Ringe and Taylor state directly that in PWGmc voiced dental fricative `*ð` became stop `*d` in all positions [@RingeTaylor2014, p. 43].

That makes the change historically clear and systemic. The chapter treats an explicit consonantal adjustment in the early West Germanic sequence, not one narrow lexical family.

### SC013. Dental hardening (`PWGmcDentalHardening`) {#rule-PWGmcDentalHardening}

The implementation keeps the dental-hardening step explicit.

```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```

In prose, the rule turns voiced dental fricative \emph{*ð} into stop \emph{*d}. It preserves a systemic step in the consonant history, not a single isolated lexical anecdote.

Its chronology is deliberately modest. If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) before or after any specific neighboring stage.

That does not make the change itself doubtful. The comparative history of dental hardening in early West Germanic is clear, so CAPR keeps the rule here as a broad systemic consonant development. The placement should be read as approximate and source-based, while the tested forms leave the exact local neighborhood open. From here the sequence turns to [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) and [SC015 NWGmcILowering](#rule-NWGmcILowering), where the first unstable unstressed vowels come into view.

\newpage

## Early unstressed vowel changes

### Historical discussion of the earliest unstressed vowel changes

These two rules stand at the start of the current sequence. One removes the remaining diphthongal quality of unstressed \emph{*ai}; the other carries early unstressed front-vowel leveling farther in forms such as *weorold* ‘world’. They do not carry equal chronological weight: [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) is historically clear but not closely fixed by the tested forms, whereas [SC015 NWGmcILowering](#rule-NWGmcILowering) has the stronger diagnostic constraint.

### Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. That is enough to make [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) historically recognizable even though the order test does not by itself determine a closer relative position.

### SC014. Monophthongization of unstressed \emph{*ai} (`NWGmcUnstressedAiMonophthongization`) {#rule-NWGmcUnstressedAiMonophthongization}

The implementation keeps the monophthongization step explicit.

```foma
define NWGmcUnstressedAiMonophthongization [
    {*ăi} -> {*ē}
];
```

In prose, the rule removes the unstressed diphthongal quality of \emph{*ai} and merges the result with unstressed \emph{*e}. It preserves a historically plausible opening step in the early Northwest Germanic vowel history.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) before or after any specific neighboring change. CAPR places it at the beginning of the unstressed-vowel prelude because the comparative sources treat unstressed \emph{*ai} monophthongization as part of the earliest Northwest Germanic simplification of unstressed vowels. The placement should be read as approximate, not as a local ordering forced by the tested forms.

### Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* and *weoruld* [@Campbell1959, pp. 141--142, 154--155]. That gives [SC015 NWGmcILowering](#rule-NWGmcILowering) a clearer historical center than the change beside it.

### SC015. Leveling of early unstressed front vowels (`NWGmcILowering`) {#rule-NWGmcILowering}

The implementation keeps the lowering step explicit.

```foma
define NWGmcILowering [
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

In prose, the rule lowers or levels early front-vowel quality in unstressed syllables. In the current sequence, that adjustment is especially visible in the pathway to *weorold* ‘world’.

Its chronology is real but one-sided. If the rule is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*wír-àldu} yields *wuruld* rather than expected OE *weorold* ‘world’. This shows that [SC015 NWGmcILowering](#rule-NWGmcILowering) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one. The checked forms therefore do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the cited `weorold` material places it inside the same early unstressed-vowel sequence.

Together these two early notes hand the sequence forward to [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 NWGmcULowering](#rule-NWGmcULowering), where the local chronology becomes tighter and the derivations more crowded.

\newpage

## West Saxon palatal glide and u-lowering

### Historical discussion of West Saxon palatal glide and u-lowering

These two rules belong together because the same *ġeoc* ‘yoke’ derivation passes through both of them. Campbell treats the West Saxon rising-diphthong spellings before back vowels, and the standard lowering of \emph{u} before a following non-high vowel is described separately in the same handbook tradition [@Campbell1959, p. 17, §44; @Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

That relation is enough to justify one paired chapter, but the two changes still need their own historical discussions and rule sections. The first creates the West Saxon \emph{ġeoc} type; the second carries the same material into the broader vowel history that follows.

### Historical discussion of West Saxon palatal glide

West Saxon spellings such as *ġeoc* ‘yoke’, *ġeong* ‘young’, and *ġeoguþ* ‘youth’ reflect a real early development before back vowels. Campbell's short account is still the clearest handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

This makes [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) historically clear even though its current order evidence is one-sided.

### SC016. West Saxon palatal glide before back vowels (`OEWsPalatalGlide`) {#rule-OEWsPalatalGlide}

The implementation states the West Saxon glide insertion directly.

```foma
define OEWsPalatalGlide [
    {*j} {*u} -> {*j} {*e} {*u} || .#. _,
    {*j} {*ú} -> {*j} {*é} {*u} || .#. _
] .o. [
    {*ʤ} {*u} -> {*ʤ} {*e} {*u} || .#. _,
    {*ʤ} {*ú} -> {*ʤ} {*é} {*u} || .#. _
] .o. [
    {*ʧ} {*u} -> {*ʧ} {*e} {*u} || .#. _,
    {*ʧ} {*ú} -> {*ʧ} {*é} {*u} || .#. _
] .o. [
    {*ʃ} {*u} -> {*ʃ} {*e} {*u} || .#. _,
    {*ʃ} {*ú} -> {*ʃ} {*é} {*u} || .#. _
];
```

In prose, the rule inserts a front glide after an initial palatal before back-vocalic \emph{u}. This is the step that helps produce West Saxon forms such as *ġeoc* ‘yoke’.

Its chronology is real but one-sided. If the rule is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*júką} yields *ġoc* rather than expected OE *ġeoc* ‘yoke’. This shows that [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) must come before [SC017 NWGmcULowering](#rule-NWGmcULowering). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one. The checked forms therefore do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the `ġeoc` / `ġeong` / `ġeoguþ` material belongs to the same early West Saxon palatal-glide development described above.

### Historical discussion of u-lowering

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

This gives [SC017 NWGmcULowering](#rule-NWGmcULowering) a broader source base than the more narrowly West Saxon rule beside it.

### SC017. Lowering of \emph{*u} before following non-high vowels (`NWGmcULowering`) {#rule-NWGmcULowering}

The implementation keeps the lowering step explicit.

```foma
define NWGmcULowering [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

In prose, the rule lowers \emph{u} to \emph{o} before a following non-high vowel. This is the change behind forms such as *ġeoc* ‘yoke’, *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Its chronology is explicit on both sides. If the rule is moved before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc \emph{*júką} yields *ġoc* rather than expected OE *ġeoc* ‘yoke’. If it is delayed until after [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*núsō} yields *nusu* rather than expected *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. This shows that [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) must come before [SC017 NWGmcULowering](#rule-NWGmcULowering), and that [SC017 NWGmcULowering](#rule-NWGmcULowering) must come before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising).

\newpage

## Stressed monosyllable \emph{*ō}-raising

### Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

That is enough for a short note. The change is historically legible, but the tested forms do not by themselves determine a closer position for it.

### SC018. Raising of final stressed monosyllabic \emph{*ō} (`NWGmcStressedMonosyllableORaising`) {#rule-NWGmcStressedMonosyllableORaising}

The implementation keeps the monosyllabic raising step explicit.

```foma
define NWGmcStressedMonosyllableORaising [
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
];
```

In prose, the rule raises final stressed monosyllabic \emph{*ō} to \emph{*ū}. It preserves a historically recognizable step behind forms such as *cū*, *hū*, and *tū*.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC018 NWGmcStressedMonosyllableORaising](#rule-NWGmcStressedMonosyllableORaising) before or after any specific neighboring change. The handbooks document the raising of stressed monosyllabic \emph{*ō} as part of the early history of long vowels, and CAPR accordingly keeps it in this early vowel section. The placement should be read as approximate, not as a local ordering forced by the tested forms.

\newpage

## Final long-\emph{o} raising and final \emph{z}-deletion

### Historical discussion of final long-\emph{o} raising and final \emph{z}-deletion

These two rules belong together because the same final-syllable structure passes through both. Ringe and Taylor describe the change of unstressed final non-nasalized long \emph{*ō} to short \emph{*u}, while Hogg and Crist treat word-final \emph{*z} loss as a separate later step in West Germanic [@RingeTaylor2014, p. 30; @Hogg1992, p. 37; @Crist2002, p. 1].

That shared final-syllable history becomes especially visible in *ræste* ‘rest’: [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must still see final \emph{*ō}, and [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must remove final \emph{*z} only afterward.

### Historical discussion of final long-\emph{o} raising

The first change in the pair is the Northwest Germanic raising of unstressed final long \emph{*ō} to \emph{*u}. Ringe and Taylor state that development directly in comparative terms [@RingeTaylor2014, p. 30].

This is the stage that carries forms such as *nosu*, *sċofl*, and *sorg* into the later Old English sequence.

### SC019. Raising of final unstressed long \emph{*ō} (`NWGmcFinalLongORaising`) {#rule-NWGmcFinalLongORaising}

The implementation states the final-vowel raising directly.

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

In prose, the rule raises final unstressed long \emph{*ō} to \emph{*u}. This is the step behind forms such as *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Its chronology is explicit on both sides. If the rule is moved before [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*núsō} yields *nusu* rather than expected OE *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. If it is delayed until after [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*rástōz} yields *rast* rather than expected *ræste* ‘rest’. This shows that [SC017 NWGmcULowering](#rule-NWGmcULowering) must come before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), and that [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must come before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion).

### Historical discussion of final \emph{z}-deletion

The second change removes word-final \emph{*z}. Standard handbook tradition and Crist's West Germanic discussion both make that development clear, even though CAPR packages it more tightly than the morphology-heavy historical descriptions usually do [@Hogg1992, p. 37; @Crist2002, p. 1].

This is the step that closes the small final-syllable sequence and also opens the way to later final-vowel consequences farther to the right.

### SC020. Deletion of word-final \emph{*z} (`PGmcFinalZDeletion`) {#rule-PGmcFinalZDeletion}

The implementation keeps the deletion step short.

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
```

In prose, the rule deletes word-final \emph{*z}. In the current sequence, this is the step that turns the protected final structure of *ræste* into its attested Old English shape after the raising rule has already applied.

Its chronology is explicit on both sides. If the rule is moved before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*rástōz} yields *rast* rather than expected OE *ræste* ‘rest’. If it is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*bébruz} yields *befro* rather than expected *befer* ‘beaver’, PGmc \emph{*kwéðuz} yields *cwedo* rather than expected *cwedu* ‘cud’, and PGmc \emph{*félθuz} yields *feldo* rather than expected *feld* ‘field’, alongside eight other newly failing rows. This shows that [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must come before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), and that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The checked forms therefore keep the rule within a wider final-syllable interval. The earlier seam with [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) is the closer local result, while the later constraint at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) mainly shows that word-final \emph{*z}-loss cannot be postponed indefinitely into the later weak-syllable sequence. CAPR keeps the rule here because the handbooks treat final \emph{*z}-loss as part of the same West Germanic ending history that follows final \emph{*ō}-raising.

\newpage

## Unstressed \emph{*o}-raising

### Historical discussion

The older history of *heofon* ‘heaven’ preserves a small but real unstressed-vowel adjustment before the later reshaping of medial vowels in Old English. Campbell derives the visible \emph{-o-} from an earlier unstressed environment, and Ringe and Taylor keep the same family legible in the wider West Germanic record [@Campbell1959, pp. 155--156, §373; @RingeTaylor2014, p. 287].

That is enough for a short note. The change is historically recognizable, but its current order evidence is one-sided and reaches outward to a later chapter.

### SC021. Raising of unstressed \emph{*o} before later \emph{*u} (`NWGmcUnstressedORaising`) {#rule-NWGmcUnstressedORaising}

The implementation keeps the unstressed raising step explicit.

```foma
define NWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

In prose, the rule raises unstressed \emph{*o} to \emph{*u} before a later \emph{*u}. This is the adjustment that helps keep the *heofon* derivation on its attested path.

Its chronology is real but one-sided. If the rule is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xémonų} yields *heofun* rather than expected OE *heofon* ‘heaven’. This shows that [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the *heofon* family belongs to the same early unstressed-vowel history described above.

\newpage

## \emph{mn}-dissimilation

### Historical discussion

The history of \emph{mn} sequences is historically legible, but the handbooks describe it more as a small descriptive pattern than as a major isolated sound change. Campbell discusses both loss of unstressed material and later assimilation in forms of this type, including the special status of *month*-type evidence [@Campbell1959, pp. 189, 195, §§470, 484].

That is enough for a short note. The change deserves explicit prose, but the current order evidence does not make it a strong chronological marker.

### SC022. Dissimilation of \emph{mn} sequences (`NWGmcMnDissimilation`) {#rule-NWGmcMnDissimilation}

The implementation keeps the dissimilation rule explicit.

```foma
define NWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _
           EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

In prose, the rule turns an earlier \emph{m} into \emph{β} when another nasal follows later in the word. It preserves a small but historically recognizable step in the prehistory of forms such as *heofon* and *month*.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC022 NWGmcMnDissimilation](#rule-NWGmcMnDissimilation) before or after any specific neighboring change. The handbooks document \emph{mn}-dissimilation as a real but limited tendency, but they do not give it a close relative chronology. CAPR therefore keeps the note here as a small early consonant adjustment. The placement should be read as approximate, not tightly fixed.

\newpage

## N-stem \emph{n}-loss

### Historical discussion

The broader history is the reduction and leveling of older n-stem endings in West Germanic. Ringe and Taylor describe the resulting syncretism in the n-stems, which is the wider morphological setting for the narrower step isolated here [@RingeTaylor2014, p. 72].

Within the current sequence, the clearest witness is the path to *dōn* ‘do’. That makes the change historically legible, but still modest in scope.

### SC023. Loss of n-stem \emph{*n} in final position (`NWGmcNStemNLoss`) {#rule-NWGmcNStemNLoss}

The implementation states the n-loss directly.

```foma
define NWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

In prose, the rule removes the final \emph{n} of the relevant n-stem ending and leaves the nasalized long vowel that later developments can reshape. In the current sequence, this is the step that keeps the derivation of *dōn* on track.

Its chronology is real but one-sided. If the rule is delayed until after [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*dōną} no longer yields expected OE *dōn* ‘do’, and the row records no output at all (\emph{+?}). This shows that [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must come before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources place this n-stem reduction in the same early final-ending history that eventually feeds the later apocope material. The bad outcome on the supported side must still be read as a failed derivation, not as a competing Old English surface form.

\newpage

## Long \emph{ē}-lowering

### Historical discussion

The later West Saxon forms *sċēap* ‘sheep’ and *ġēar* ‘year’ imply an earlier lowering of long \emph{ē} before the palatal diphthongal outcomes described more fully later in the sequence. Campbell and Ringe and Taylor discuss those later West Saxon outputs directly [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1].

That is enough for a short note. The change remains historically legible, but its positive chronology points outward to a later chapter.

### SC024. Lowering of long \emph{ē} before non-nasal consonants (`NWGmcLongELowering`) {#rule-NWGmcLongELowering}

The implementation keeps the lowering step explicit.

```foma
define NWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

In prose, the rule lowers long \emph{ē} to \emph{ǣ} before non-nasal consonants. This is the earlier adjustment behind the later West Saxon outputs seen in *sċēap* and *ġēar*.

Its chronology is real but one-sided. If the rule is delayed until after [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), PGmc \emph{*skḗpą} yields *sċīep* rather than expected OE *sċēap* ‘sheep’, and PGmc \emph{*jḗrą} yields *ġīer* rather than expected *ġēar* ‘year’. This shows that [SC024 NWGmcLongELowering](#rule-NWGmcLongELowering) must come before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat the lowering as the earlier stage behind the later West Saxon outputs *sċēap* and *ġēar*.

\newpage

## Long \emph{ē} nasal-rounding

### Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* ‘month’ and *mōna* / *mōn*-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

That is enough for a short note. The change is historically legible, but the tested forms do not make it a close chronological anchor.

### SC025. Rounding of long \emph{ē} before nasals (`NWGmcLongENasalRounding`) {#rule-NWGmcLongENasalRounding}

The implementation states the rounding step directly.

```foma
define NWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

In prose, the rule rounds long \emph{ē} to \emph{ō} before nasals. It preserves a historically intelligible step behind month-type and moon-type outcomes without claiming more chronology than the current testing supports.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC025 NWGmcLongENasalRounding](#rule-NWGmcLongENasalRounding) before or after any specific neighboring change. The handbooks document month-type and moon-type outcomes from older long \emph{ē} before nasals, but they do not give the change a close local chronology of its own. CAPR keeps the note here beside the surrounding \emph{ē}-developments for that reason. The placement should be read as approximate and source-based.

\newpage

## Nasal spirant changes

### Historical discussion of nasal loss before spirants and compensatory lengthening

These two rules belong together because they are CAPR's formal articulation of one older development. Campbell describes the process as nasal loss before voiceless spirants with compensatory lengthening and nasalization of the preceding vowel, and Ringe and Taylor treat the same outcomes within inherited northern West Germanic development, not as an isolated late Old English innovation [@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

That shared history also explains the local interaction. [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) adjusts the vowel while the nasal plus spirant sequence is still present, and [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) then removes the nasal. The pair is therefore more than a mere adjacency in the cascade: the first rule prepares the environment that the second rule closes.

### SC026. Lengthening before nasal plus spirant (`NWGmcNasalSpirantLengthening`) {#rule-NWGmcNasalSpirantLengthening}

The implementation keeps the vowel change explicit across the relevant nasal-spirant environments.

```foma
define NWGmcNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*á} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*é} -> {*ḗ} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ó} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];
```

In prose, the rule lengthens and reshapes the vowel before nasal plus voiceless spirant sequences. This is the stage that helps produce OE *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss), PGmc \emph{*fúnxstiz} yields *fyst* rather than expected OE *fȳst* ‘fist’, PGmc \emph{*gánsz} yields *ġeas* rather than expected *gōs* ‘goose’, and PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. This shows that [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) must come before [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat vowel lengthening and nasal loss as two parts of the same inherited nasal-spirant development.

### SC027. Loss of the nasal before spirants (`NWGmcNasalSpirantLoss`) {#rule-NWGmcNasalSpirantLoss}

The implementation then removes the nasal from the same environment.

```foma
define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

In prose, the rule deletes the nasal before a voiceless spirant after the vowel has already been adjusted. This is the stage that completes the same inherited development behind *fȳst*, *gōs*, and *ġeoguþ*.

Its ordinary historical chronology is one-sided in the opposite direction. If the rule is moved before [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening), PGmc \emph{*fúnxstiz} yields *fyst* rather than expected OE *fȳst* ‘fist’, PGmc \emph{*gánsz} yields *ġeas* rather than expected *gōs* ‘goose’, and PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. This shows that [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) must come before [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss). If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only the earlier relation: [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) must follow [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening). They do not identify a corresponding later constraint, and CAPR keeps the rule here because the same inherited development requires the nasal to disappear only after the preceding vowel has already been adjusted.

\newpage

## Preconsonantal \emph{*x}-loss

### Historical discussion

Campbell explicitly treats loss of \emph{x} and gives forms such as *fléam* ‘flight’ and *hēla* ‘heel’ as examples of the same broad development [@Campbell1959, p. 186, §461]. That is enough to make this a historically legible change.

The present order evidence is much lighter than the historical description. This chapter therefore stays brief: the change belongs in the sequence, but current testing does not make it a strong chronological marker.

### SC028. Loss of preconsonantal \emph{*x} (`NWGmcPreconsonantalXLoss`) {#rule-NWGmcPreconsonantalXLoss}

The implementation keeps the deletion rule explicit.

```foma
define NWGmcPreconsonantalXLoss [
    {*x} -> 0 || _ {*s} EnglishStarConsonant
];
```

In prose, the rule deletes \emph{*x} before \emph{*s} plus another consonant. It preserves a historically recognizable part of the older consonant history without assigning it more order-testing force than the current evidence supports.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC028 NWGmcPreconsonantalXLoss](#rule-NWGmcPreconsonantalXLoss) before or after any specific neighboring change. The handbooks make preconsonantal \emph{x}-loss historically recognizable, but they do not place it precisely within this local stretch. CAPR therefore keeps it here as a short prefatory note before the better-constrained glide and fronting rules that follow. The placement should be read as approximate, not tightly fixed.

\newpage

## Awj glide formation and au-fronting

### Historical discussion of awj glide formation and au-fronting

These two rules belong together because the same *hay* and *strew* material passes through both of them. [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) reshapes the older \emph{awj} sequence, and [SC030 OEAuFronting](#rule-OEAuFronting) then fronts the resulting \emph{au}. Campbell's discussion of these outcomes and Ringe and Taylor's derivations of *hīeġ* and *strīeġan* describe the same sequence in ordinary historical terms [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

That relation is close enough to justify one paired chapter, but the two rules still need separate historical discussions and separate chronology paragraphs. The first rule prepares the sequence; the second carries it forward into [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

### Historical discussion of awj glide formation

Older \emph{awj} sequences are the source of forms such as *hīeġ* ‘hay’ and *strīeġan* ‘strew’. Campbell treats the relevant developments directly, and Ringe and Taylor likewise trace the same material through intermediate \emph{auj}-type stages [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

This makes [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) historically clear even though its current order evidence is one-sided.

### SC029. Glide formation in \emph{*awj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

The implementation keeps the glide-formation step explicit.

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

In prose, the rule turns older \emph{awj} material into the glide sequence that the following fronting rule can read. This is the step behind forms such as *hīeġ* and *strīeġan*.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC030 OEAuFronting](#rule-OEAuFronting), PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. This shows that [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) must come before [SC030 OEAuFronting](#rule-OEAuFronting). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat `awj` reshaping as the preparatory step before the fronted diphthongal outcomes develop.

### Historical discussion of au-fronting

Once the glide sequence is in place, \emph{au}-fronting produces the fronted diphthongal outcomes that carry this material into the broader West Saxon vowel history. Campbell's account of \emph{au} > \emph{ēa} keeps that larger setting in view [@Campbell1959, pp. 53--54, §135].

That is why [SC030 OEAuFronting](#rule-OEAuFronting) matters beyond the immediate pair: it reciprocates [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) and then passes a wider set of derivations forward into [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

### SC030. Fronting of \emph{*au} (`OEAuFronting`) {#rule-OEAuFronting}

The implementation states the fronting step directly.

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

In prose, the rule fronts \emph{au} so that later Old English diphthongal outcomes can develop in the expected way. It is the step that connects the *hay* / *strew* material to the wider diphthongal region that follows.

Its chronology is explicit on both sides. If the rule is moved before [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation), PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. If it is delayed until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*galáubijaną}, \emph{*bráudą}, and \emph{*dráugmaz}, together with sixteen other derivations, fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. This shows that [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) must come before [SC030 OEAuFronting](#rule-OEAuFronting), and that [SC030 OEAuFronting](#rule-OEAuFronting) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

The later failure set is broad and is best read as failed derivations. It does not present a competing set of Old English surface forms.

\newpage

## West Saxon diphthong sequence

### Historical discussion of the West Saxon diphthong sequence

The four rules gathered here belong to one West Saxon diphthongal zone, but they do not all arise from a single historical event. Campbell discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered diphthongization, and later Anglian smoothing in connected but separate parts of the vowel history, and Hogg likewise treats the palatal-diphthong side as real yet uneven [@Campbell1959, pp. 46, 53--54, 65--70, 95--96, §§120, 135--136, 170--176, 185, 223--227; @Hogg1992, pp. 106--107, 111--112].

The closest interaction inside the sequence is between [SC031 OEWWSimplification](#rule-OEWWSimplification) and [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), which together shape *dēaw* ‘dew’ and *hēawan* ‘hew’. [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) and [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) still belong here, but they point to different parts of the same history: [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) regularizes a wider diphthongal field, while [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) carries the long \emph{ēow} side into the later environment of [SC044 OEBreaking](#rule-OEBreaking).

### Historical discussion of WW simplification

West Germanic \emph{ww} sequences lie behind forms such as *dēaw* ‘dew’ and *hēawan* ‘hew’, and Campbell treats them as part of the early West Germanic diphthong history [@Campbell1959, p. 46, §120].

[SC031 OEWWSimplification](#rule-OEWWSimplification) is the first explicit step in that sequence. It is small in form, but the later long-diphthong outcomes depend on it.

### SC031. Simplification of \emph{*ww} sequences (`OEWWSimplification`) {#rule-OEWWSimplification}

The implementation states the simplification directly.

```foma
define OEWWSimplification [
    {*w} {*w} -> {*w}
];
```

In prose, the rule reduces a doubled \emph{w} to a single \emph{w}. That simplification is what allows the later \emph{ēaw} rule to work with the shape seen in *dēaw* and *hēawan*.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*dáwwō} yields *dawu* rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields *hawan* rather than expected *hēawan* ‘hew’. This shows that [SC031 OEWWSimplification](#rule-OEWWSimplification) must come before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong). If the rule is moved earlier within the ordinary tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier historical constraint, and CAPR keeps the rule here because the `dēaw` / `hēawan` material belongs to the same West Saxon diphthong zone that the following rule develops further.

### Historical discussion of diphthong leveling

By the time the sequence reaches forms such as *hēafod* ‘head’, diphthongal outcomes are already being redistributed across a wider set of words. Campbell's discussion of smoothing and related later monophthongization is the clearest handbook anchor for that layer of the history, even though the rule kept here is more tightly drawn than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

This makes [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) a real member of the sequence, even if its evidence is less self-contained than the *dēaw* / *hēawan* pair.

### SC032. Leveling of diphthongal outputs (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

The implementation keeps the leveling rule explicit.

```foma
define OEDiphthongLeveling [
    {*aeu} -> {*ēa},
    {*áeu} -> {*ēa},
    {*eu} -> {*ēo},
    {*éu} -> {*ēo},
    {*iu} -> {*ēo},
    {*íu} -> {*ēo},
    {*e} {*u} -> {*eo},
    {*é} {*u} -> {*éo},
    {*i} {*u} -> {*eo}
];
```

In prose, the rule regularizes several diphthongal outcomes into the West Saxon patterns that appear later in the sequence. It is the step that helps keep forms such as *hēafod* ‘head’ in their expected shape.

Its chronology is explicit on both sides. If the rule is moved before [SC030 OEAuFronting](#rule-OEAuFronting), PGmc \emph{*galáubijaną}, \emph{*báug}, and \emph{*bráudą} fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. If it is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xáubudą} yields *hēafud* rather than expected *hēafod* ‘head’. This shows that [SC030 OEAuFronting](#rule-OEAuFronting) must come before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), and that [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). The earlier side is real, but it is expressed as failed derivations rather than as alternate surface forms.

### Historical discussion of long \emph{ēow}

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow* ‘knee’ belong to the same West Saxon vowel region, though their clearest ordering relation points forward. Campbell's treatment of early \emph{eu} in Old English and Ringe and Taylor's examples from *chew*, *four*, and *knee* show that this is a real part of the diphthong history [@Campbell1959, pp. 53--54, §136; @RingeTaylor2014, pp. 188, 202].

That makes [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) an essential member of the sequence, even though its strongest boundary lies ahead at [SC044 OEBreaking](#rule-OEBreaking).

### SC033. Long \emph{ēow} before following vowels and weak endings (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

The implementation states the long-diphthong development directly.

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

In prose, the rule turns \emph{ew} and \emph{iw} sequences into long \emph{ēow}. This is the step behind forms such as *ċēowan*, *fēower*, and *cnēow*.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*kéwwaną} yields *ċeowan* rather than expected OE *ċēowan* ‘chew’, PGmc \emph{*fédwōr} yields *feower* rather than expected *fēower* ‘four’, and PGmc \emph{*knéwą} yields *cneow* rather than expected *cnēow* ‘knee’. This shows that [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) must come before [SC044 OEBreaking](#rule-OEBreaking). If the rule is moved earlier within the ordinary tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier historical constraint, and CAPR keeps the rule here because the sources treat long \emph{ēow} as part of the same diphthong region even though its strongest ordering relation points forward to breaking.

### Historical discussion of long \emph{ēaw}

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* and *hēawan*. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) therefore closes the nearest local pair in the chapter and also points onward to [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

### SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

The implementation keeps the long-\emph{ēaw} step explicit.

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

In prose, the rule turns \emph{aw} before a following vowel into long \emph{ēaw}. This is the stage that yields forms such as *dēaw* and *hēawan*.

Its chronology is explicit on both sides. If the rule is moved before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*dáwwō} yields *dawu* rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields *hawan* rather than expected *hēawan* ‘hew’. If it is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*skáwōjaną} yields *sċawian* rather than expected OE *sċēawian* ‘show’, PGmc \emph{*skáwōθi} yields *sċawaþ* rather than expected *sċēawaþ*, and PGmc \emph{*stráwą} yields *stræw* rather than expected *strēaw* ‘straw’. This shows that [SC031 OEWWSimplification](#rule-OEWWSimplification) must come before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), and that [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

The checked forms therefore place the rule within a wider West Saxon diphthong interval. The earlier relation to [SC031 OEWWSimplification](#rule-OEWWSimplification) is the closer local seam, while the later edge at [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) chiefly shows that the \emph{dēaw} / \emph{hēawan} / \emph{sċēawian} material must be in place before the brightening region begins. CAPR keeps the rule here because the handbooks treat those forms as one part of the West Saxon diphthong zone before the later brightening development.

\newpage

## Prefix and compound adjustments

### Historical discussion of prefixal \emph{*a}-reduction

Weakly stressed prefixes can lose their older low vowel early in Old English, and that is the historical setting for [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction). Campbell treats the small but real class of pretonic losses directly, while Ringe and Taylor's derivation of \emph{*galaubijana} gives the clearest comparative witness for the same development [@Campbell1959, p. 147, §354; @RingeTaylor2014, p. 245; @RingeTaylor2014, p. 267].

The result is a modest rule with a narrow historical range. It matters because it gives prefixed forms the weak vowel shape that later vocalic rules inherit.

### SC035. Reduction of prefixal \emph{*a} (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

The implementation states the prefixal reduction directly.

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ}
        || .#. {*g} _
           [EnglishStarConsonant | EnglishPalatalConsonant]
           EnglishStarVocalic
];
```

In prose, the rule reduces prefixal \emph{*ga-} to unstressed \emph{*ge-}. This is the step that gives forms such as *ġelīefan* ‘believe’ their expected prefix vowel.

Its chronology is one-sided but concrete. If the rule is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*galáubijaną} yields *ġealīefan* rather than expected OE *ġelīefan* ‘believe’. This shows that [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). The earlier direction is not yet fixed by the checked forms, so the card does not yet show what this rule must follow.

### Historical discussion of inter-stress raising

The strongest member of this chapter is [SC036 OEInterStressRaising](#rule-OEInterStressRaising). Campbell's discussion of *weorold* / *weoruld* and Ringe and Taylor's derivation of \emph{*weraldu} > \emph{*weruldu} > OE *weorold* place the rule squarely in the history of low-stress medial vowels [@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 322, §6.3.3].

This is more than a small spelling adjustment. The rule changes the vowel that stands between stronger stress peaks, which is why its witnesses remain so useful for chronology.

### SC036. Raising of medial \emph{*a} between stress peaks (`OEInterStressRaising`) {#rule-OEInterStressRaising}

The implementation keeps both parts of the raising rule together.

```foma
define OEInterStressRaising [
    {*a} -> {*u}
        || PGmcStarVowel EnglishStarConsonant* _
           [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
];
```

In prose, the rule raises medial unstressed \emph{*a} to \emph{*u} in the low-stress position between stronger syllables. This is the stage behind forms such as *sāwol* ‘soul’ and *weorold* ‘world’.

Its chronology is explicit on both sides. If the rule is moved before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’. If it is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*sáiwalō} yields *sāwul* rather than expected *sāwol*, and PGmc \emph{*wír-àldu} yields *weoruld* rather than expected *weorold* ‘world’. This shows that [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising), and that [SC036 OEInterStressRaising](#rule-OEInterStressRaising) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The checked forms therefore place the rule within a broader low-stress interval. The later boundary at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) is the more local result inside this stretch, while the earlier relation to [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) mainly shows that \emph{world}- and \emph{soul}-type vocalism belongs after the earlier final-vowel developments. CAPR keeps the rule here because the handbooks treat these medial unstressed vowels as one historical grouping.

### Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

That is the historical setting for [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope). The rule is worth stating explicitly because compounds such as *reġnboga* ‘rainbow’ depend on it, even though its chronology is narrower and less ordinary-historical than the rule beside it.

### SC037. Syncope of compound linking vowels (`OECompoundLinkingSyncope`) {#rule-OECompoundLinkingSyncope}

The implementation deletes the weak linking vowel in the relevant compound environment.

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

In prose, the rule removes a weak linking vowel inside compounds before a following grave-stressed member. This is the step that yields forms such as *reġnboga* ‘rainbow’.

The order test does not yet identify an ordinary historical stage that this rule must follow. If it is delayed until after SC038 OEStripSecondaryStress, PGmc \emph{*régna-bùgô} yields *reġnefoga* rather than expected OE *reġnboga* ‘rainbow’. That result shows only that compound-linking syncope must precede the later technical stress-stripping stage built into the implementation. Because SC038 OEStripSecondaryStress is not an ordinary sound change, this is not a historical local order in its own right. CAPR keeps the rule here because the handbooks treat reduced compound junctures and unstable linking vowels as part of the same weakened-compound behavior discussed around [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).

\newpage

## Medial unstressed vowel changes

### Historical discussion of medial unstressed vowel changes

These two rules belong together because the same low-stress vocalic region supplies their witnesses, and the order evidence ties them together through *wuduwe* ‘widow’. Campbell discusses both the \emph{w}-conditioned \emph{u} forms and the later *weorold* / *weoruld* alternation, while Ringe and Taylor give the same connection comparatively in \emph{*widuwon-}, \emph{*weraldu}, and \emph{*jugunþi} [@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332; @Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267; @RingeTaylor2014, p. 322, §6.3.3].

The pair is therefore historically tighter than a merely adjacent grouping. [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) is the narrower rule, but it feeds the exact vowel sequence that [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) must then reshape.

### SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

The implementation keeps the \emph{w}-conditioned adjustment very small.

```foma
define OEWICombinativeUUmlaut [
    {*í} -> {*ú}
        || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
];
```

In prose, the rule changes the first vowel of \emph{wi}-forms under the following back-vowel conditions. This is the step that helps produce OE *wuduwe* ‘widow’.

Its chronology is clear on the later side. If the rule is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe* ‘widow’. This shows that [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the `widow` material belongs to the same low-stress vocalic sequence as the following medial lowering.

### SC040. Lowering of medial unstressed \emph{*u} (`OEMedUnstressedULowering`) {#rule-OEMedUnstressedULowering}

The implementation states the lowering rule directly.

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

In prose, the rule lowers medial unstressed \emph{*u} to \emph{*o} in the relevant consonantal environment. This is the stage behind forms such as *weorold* ‘world’.

Its chronology is explicit on both sides. If the rule is moved before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe* ‘widow’. If it is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. This shows that [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), and that [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).

The later relation to [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) is real, but it is much broader than the local *widow* pair. The closest chronological result inside this chapter is still the reciprocal relation between [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) and [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

\newpage

## Final bare-\emph{a} loss

### Historical discussion

The handbooks treat loss of final short low vowels as part of a broader erosion of final syllables, but that broader background still supports a short explicit rule here [@Campbell1959, p. 143, §341; @RingeTaylor2014, pp. 60--61].

This change belongs after the medial unstressed vowel changes because it affects final syllables and leaves the low-stress interior of the word behind. It also belongs before restoration because later fronted forms depend on the environment it leaves behind.

### SC041. Loss of final bare \emph{*a} (`PWGmcFinalBareALoss`) {#rule-PWGmcFinalBareALoss}

The implementation keeps the loss of the final vowel explicit.

```foma
define PWGmcFinalBareALoss [
    {*a} -> 0 || _ .#.
];
```

In prose, the rule deletes a surviving final bare \emph{*a}. This is the step that prevents a large class of words from carrying a spurious final vowel into Old English.

Its chronology is broad on the left and sharper on the right. If the rule is moved before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*bárdaz} yields *bearda* rather than expected OE *beard* ‘beard’, and PGmc \emph{*kámbaz} yields *camba* rather than expected *camb* ‘comb’. If it is delayed until after [SC046 OEARestoration](#rule-OEARestoration), PGmc \emph{*kráftaz} yields *craft* rather than expected OE *cræft* ‘craft’, and PGmc \emph{*dágaz} yields *dag* rather than expected *dæġ* ‘day’. This shows that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before [SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), and that [SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss) must come before [SC046 OEARestoration](#rule-OEARestoration).

The earlier boundary reaches across a wide stretch of the cascade and is best read as a broad limit, not a local pair. The later boundary is the nearer result: restoration needs final bare-\emph{a} loss to have happened already.

\newpage

## Surviving bimoric \emph{*ō} unrounding

### Historical discussion

This is a narrow prefatory rule. The handbooks do not isolate one large independent sound change under exactly this label. Still, the surviving bimoric \emph{*ō} pathway behind forms such as *ræste* ‘rest’ needs to be stated explicitly if the sequence is to begin cleanly before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). Campbell, Hogg, and Ringe and Taylor all make the surrounding fronting and restoration region historically intelligible even when this particular feeder step remains model-shaped [@Campbell1959, pp. 52, 60, §§131, 157--158; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190].

That is enough for a short reader-facing note. The rule belongs here because it closes a small architectural seam on the left side of the brightening chapter, not because it should rival the broader historical weight of the chapters that follow.

### SC042. Unrounding of the surviving bimoric \emph{*ō} (`PWGmcSurvivingBimoricOUnrounding`) {#rule-PWGmcSurvivingBimoricOUnrounding}

The implementation keeps the step very small and explicit.

```foma
define PWGmcSurvivingBimoricOUnrounding [
    {*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

In prose, the rule unrounds a surviving bimoric \emph{*ō} to \emph{*ā} in the environment that later feeds the fronted and restored outcome in forms such as *ræste* ‘rest’.

Its chronology is real on both sides, but not equally local. If the rule is moved before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*rástōz} yields *rasta* rather than expected OE *ræste* ‘rest’. If the rule is delayed until after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), the same PGmc form again yields *rasta* instead of *ræste*. This shows that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), and that [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

The later relation to [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) is the closer local handoff. The earlier constraint at [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) mainly shows that this feeder step belongs somewhere after the earlier final-\emph{*z} sequence. CAPR keeps the rule here as a short context note immediately before brightening, and its entire chronology is still carried by the single *rest* derivation.

\newpage

## Anglo-Frisian brightening

### Historical discussion

This chapter carries more historical weight than the narrow note before it. The change usually called Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments, and later Old English developments repeatedly presuppose that fronted stage even when they partly conceal it. Campbell gives the classical statement of the fronting itself, Hogg supplies the standard modern label pair, and Ringe and Taylor make the local chronology with breaking and restoration unusually clear [@Campbell1959, p. 52, §131; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

That is why the chapter is more than a general handbook excursus. The finite-state evidence shows that the rule fronts a vowel and also creates the input that [SC044 OEBreaking](#rule-OEBreaking) must read and that [SC046 OEARestoration](#rule-OEARestoration) later partly reverses before back vowels.

### SC043. Fronting of low \emph{*a} outside nasal environments (`AngloFrisianBrightening`) {#rule-AngloFrisianBrightening}

The implementation keeps the brightening as one composed rule.

```foma
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

In prose, the rule fronts low \emph{*a} to \emph{*æ}-type outcomes outside nasal environments. The composed definition reflects the fact that the transducer handles stressed, unstressed, and long-final branches separately even though the historical rule is normally discussed more compactly.

Its chronology is explicit on both sides. If the rule is moved before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), PGmc \emph{*rástōz} yields *rasta* rather than expected OE *ræste* ‘rest’. If it is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. This shows that [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding) must come before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), and that [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) must come before [SC044 OEBreaking](#rule-OEBreaking).

That position is historically apt. The rule is early enough to feed later breaking, but not so early that the surviving-bimoric \emph{*ō} pathway on its left can be ignored. It is one of the main vocalic pivots of this part of the sequence.

\newpage

## Breaking and velar-fricative palatalization

### Historical discussion of breaking and velar-fricative palatalization

These two rules belong together because the first establishes the local vocalic environment that the second must read. Breaking creates the \emph{eo}-type outputs before \emph{h}, \emph{rC}, and \emph{lC}, and the following velar-fricative palatalization then operates in that already reshaped environment. Campbell, Ringe and Taylor, and Fulk all make breaking a standard part of the post-brightening sequence, while the local fricative palatalization is historically narrower but still clear enough to stand beside it [@Campbell1959, pp. 54, 166, §§139, 405--406; @RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2; @Fulk2018, pp. 73--74, §4.13].

That interaction is close enough to justify a shared historical discussion. Even so, the hierarchy remains uneven. Breaking is the clearer handbook center, while velar-fricative palatalization is the tighter local follower whose chronology becomes especially visible through the *feoh* and *feohtan* type derivations.

### SC044. Breaking before \emph{h}, \emph{rC}, and \emph{lC} (`OEBreaking`) {#rule-OEBreaking}

The implementation keeps the breaking stage as one composed rule.

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

In prose, the rule breaks front vowels into diphthongal outcomes before the relevant consonantal environments. This is the step that yields forms such as *feoh* ‘fee’ and *feohtan* ‘fight’.

Its chronology is concrete on both sides. If the rule is moved before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. If it is delayed until after [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc \emph{*féxu} yields *fehu* rather than expected OE *feoh* ‘fee’, and PGmc \emph{*féxtaną} yields *fehtan* rather than expected *feohtan* ‘fight’. This shows that [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) must come before [SC044 OEBreaking](#rule-OEBreaking), and that [SC044 OEBreaking](#rule-OEBreaking) must come before [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization).

That two-sided local seam is why [SC044 OEBreaking](#rule-OEBreaking) works so well as the main center of the pair.

### SC045. Palatalization of velar fricatives beside front vowels (`OEVelarFricativePalatalization`) {#rule-OEVelarFricativePalatalization}

The following rule handles the local fricative palatalization.

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*ɣ} -> {*j} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*ɣ} -> {*j} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j},
    {*ɣ} -> {*j} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

In prose, the rule palatalizes \emph{*x} and \emph{*ɣ} beside front vowels or before \emph{*j}. In this chapter it is the local follower to breaking, not a general article on all Old English palatalization.

Its chronology is explicit on both sides. If the rule is moved before [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*féxu} yields *fehu* rather than expected OE *feoh*, and PGmc \emph{*féxtaną} yields *fehtan* rather than expected *feohtan*. If it is delayed until after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut), PGmc \emph{*séxs} yields *sihs* rather than expected OE *six*. This shows that [SC044 OEBreaking](#rule-OEBreaking) must come before [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), and that [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization) must come before [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut).

The later relation to [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut) remains a cross-reference, not a reason to enlarge the chapter. The core local pair is still [SC044 OEBreaking](#rule-OEBreaking) and [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization).

\newpage

## A-restoration and nasal changes

### Historical discussion of A-restoration

The first member of this chapter is the clearest historical hinge in the post-brightening region. Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's discussion of later retraction describe the same phenomenon that the transducer keeps explicit here [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. The rule matters because Anglo-Frisian fronting is often visible only through the later environments that restore some of its outcomes to back \emph{a}.

That makes [SC046 OEARestoration](#rule-OEARestoration) the source-backed hinge of the chapter. The nasal rules that follow belong in the same neighborhood, but they do not carry quite the same historical weight in the handbooks.

### SC046. Restoration of \emph{*a} before following back vowels (`OEARestoration`) {#rule-OEARestoration}

The implementation keeps the restoration step explicit.

```foma
define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

In prose, the rule changes earlier fronted \emph{*æ} back to \emph{*a} before the relevant following back-vowel environments. This is the step that turns fronted forms such as *bæcan* back into the attested OE *bacan* ‘bake’.

Its chronology is explicit on both sides. If the rule is moved before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*bákaną} yields *bæcan* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*fáraną} yields *færan* rather than expected *faran* ‘fare’. If it is delayed until after [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc \emph{*bákaną} again yields *bæcan* instead of *bacan*, and PGmc \emph{*wádaną} yields *wædan* instead of *wadan* ‘wade’. This shows that [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening) must come before [SC046 OEARestoration](#rule-OEARestoration), and that [SC046 OEARestoration](#rule-OEARestoration) must come before [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization).

The rule is therefore not a decorative aftereffect of brightening. It is a real restoration hinge with a positive local window on both sides.

### Historical discussion of heavy-syllable nasal loss and secondary nasalization

The remaining two rules are more tightly paired inside the model than they are in ordinary handbook naming. Their connection is derivational and broad. [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) removes the final nasalized vowel in heavy syllables, while [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) marks the preceding \emph{a} before final \emph{n}. The result is a large reciprocal failure set if the two are inverted. Campbell's discussion of later nasal loss and the later back-mutation environment gives the broader background, while Ringe and Taylor help with the later cross-reference toward [SC059 OEBackMutation](#rule-OEBackMutation) [@Campbell1959, pp. 86, 166, §§205--206, 403; @RingeTaylor2014, p. 319, §6.9.4].

That shared discussion is justified because the two rules interact directly inside the derivation. Even so, the hierarchy remains visible: the pair is a strong computational core, but less like a classical textbook chapter than [SC046 OEARestoration](#rule-OEARestoration).

### SC047. Heavy-syllable nasal apocope of final \emph{*ą} (`OEHeavySyllableNasalApocope`) {#rule-OEHeavySyllableNasalApocope}

The implementation keeps the apocope step short.

```foma
define OEHeavySyllableNasalApocope [
    {*ą} -> 0 || OEAnyConsonant _ .#.
];
```

In prose, the rule deletes final nasalized \emph{*ą} after a heavy syllable. This is the step that prevents a large class of forms from retaining spurious weak final vowels.

Its chronology is real on both sides, though not equally local. If the rule is moved before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*stráwą} yields *stræw* rather than expected OE *strēaw* ‘straw’. If it is delayed until after [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside a very broad \emph{-en} failure set. This shows that [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) must come before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), and that [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) must come before [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization).

The earlier side is narrow, but the later side is one of the broadest reciprocal failure sets in this part of the model.

### SC048. Secondary nasalization before final \emph{*n} (`OESecondaryNasalization`) {#rule-OESecondaryNasalization}

The following rule states the nasalization step directly.

```foma
define OESecondaryNasalization [
    {*a} -> {*ą} || _ {*n} .#.
];
```

In prose, the rule nasalizes \emph{*a} before final \emph{n}. This is the step that helps keep the live \emph{-an} outcomes distinct from the spurious \emph{-en} forms that appear if the late nasal rules are misordered.

Its chronology is explicit on both sides. If the rule is moved before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan*, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan*, representing the same broad reciprocal failure set. If it is delayed until after [SC059 OEBackMutation](#rule-OEBackMutation), PGmc \emph{*stélaną} yields *steolan* rather than expected OE *stelan* ‘steal’, and PGmc \emph{*wébaną} yields *weofan* rather than expected *wefan* ‘weave’. This shows that [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) must come before [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), and that [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) must come before [SC059 OEBackMutation](#rule-OEBackMutation).

That combination explains the chapter’s internal hierarchy. [SC046 OEARestoration](#rule-OEARestoration) is the clearest historical hinge, while [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) and [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) form the stronger reciprocal nasal core.

\newpage

## B allophony and Sievers-law syncope

### Historical discussion of B allophony

The first change is the positional alternation of Germanic \emph{*b}. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@Hogg1992, pp. 101--102]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

This is a narrow consonantal distribution with limited independent scope, but it
matters because later derivations already assume that the alternation is in
place.

### SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

The first rule formalizes the stop-fricative alternation of Germanic \emph{*b}.

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

In prose, the rule says that \emph{*b} becomes a fricative after vowels and
liquids, while geminate \emph{*bb} keeps the stop value.

Historically, this is the sort of narrow distributional statement that the
handbooks place within the consonant system and discuss only briefly on its own.
Even so, it matters because later derivations assume that the
alternation is already in place. The clearest tested consequence appears in
*reġnboga* ‘rainbow’. If the rule is moved before the earlier linking-vowel
adjustment, the derivation yields *reġnfoga* ‘rainbow’ rather than expected OE
*reġnboga* ‘rainbow’. This shows that [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) must come
before [SC049 PGmcBAllophony](#rule-PGmcBAllophony).
No equally sharp later lexical breakpoint emerges within the tested sequence, so
the rule has no explicit later boundary within the present sequence.

### Historical discussion of Sievers-law syncope

Sievers' Law belongs to a different historical problem. It is a prosodic and
morphological adjustment in heavy stems, not a distributional allophone of a
stop consonant. Adamczyk treats the Old English reflexes of the law as real
historical material in weak verbs and related formations
[@Adamczyk2001, pp. 61--72]. Fulk gives the compact comparative summary through
familiar forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 127, §6.15].

That makes the change historically narrower but chronologically important. It is
the last small feeder before the palatalization sequence begins in earnest, and
its place in the cascade is clearer than that of the preceding allophony rule.

### SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

The second rule removes the Sievers-law \emph{*i} before \emph{*j} after a consonant.

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

In plain language, the rule contracts the heavier \emph{*-CijV-*} sequence to
\emph{*-CjV-*}. That is why it belongs to the historical aftermath of Sievers' Law and
stands apart from the earlier stop-fricative distribution.

Its place in the sequence is clearer than that of the allophony rule. If the
change is delayed until after [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), the cluster
behind *streċċan* ‘stretch’ is affected too late. With PGmc
\emph{*strákkijaną} in the wrong order, the derivation yields *strecċan*
‘stretch’. The expected Old English form is *streċċan* ‘stretch’. That is a real chronological
consequence. No equally precise earlier lexical breakpoint fixes how far back
the syncope must stand, so the historical picture remains asymmetric. The rule
is secure as an immediate feeder into the palatalization zone, even though its
earlier limit is less sharply bounded. The evidence therefore places
[SC050 SieversLawSyncope](#rule-SieversLawSyncope) before
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization).

\newpage

## Palatalization of \emph{*sk} to \emph{*sc}

### Historical discussion

The palatalization of \emph{*sk} to Old English \emph{*sc} is one of the recognizable early
cluster changes in the larger palatalization zone. Campbell distinguishes the
cluster from plain velars when he remarks that \emph{*sk} is especially prone to
palatalization and assibilation [@Campbell1959, p. 278, §440]. Hogg gives the
same change a clearer structural place by treating \emph{*sk} beside the palatalization
of plain velars and before the later West Saxon diphthongal developments
[@Hogg1992, pp. 106--107, 111--112]. Ringe and Taylor make the same sequence
explicit when they distinguish the earlier palatalization of velars and \emph{*sk} from
the later diphthongization after already palatal consonants
[@RingeTaylor2014, pp. 213--216, §§6.4.1, 6.5.1].

Luick is especially useful for the larger frame. He treats
the cluster change as part of a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
excuse to merge the whole palatalization and umlaut region into one undivided
chapter.

### SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

The implementation states the \emph{*sk} rule explicitly.

```foma
define OESkPalatalization [
    {*s} {*k} -> {*ʃ} || .#. _
] .o. [
    {*s} {*k} -> {*ʃ} || EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)
] .o. [
    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel
] .o. [
    {*s} {*k} -> {*ʃ} || _ {*j}
] .o. [
    {*s} {*k} -> {*ʃ} || {*j} _
];
```

In prose, the rule turns \emph{*sk} into a palatal outcome in the environments
that lead to Old English \emph{*sc}.

Its historical place is between the earlier restoration and the later palatal
vowel developments. If it is moved too early, the forms behind *flasce* ‘flask’
and *wascan* ‘wash’ are fronted too soon, yielding *flæsce* ‘flask’ and
*wæscan* ‘wash’ rather than expected OE *flasce* and *wascan*. This gives the
earlier result. This shows that [SC046 OEARestoration](#rule-OEARestoration) must come before
[SC051 OESkPalatalization](#rule-OESkPalatalization). If it is moved too late, the cluster no longer feeds the later
West-Saxon diphthongal outcomes that appear in *sċeaft* ‘shaft’, *sċēar*
‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’. That is why
the rule sits naturally beside [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

No single later wrong form is isolated for the whole group of
\emph{*sċea-*} / \emph{*sċie-*} witnesses, but the current notes do show that the cluster
must already be palatalized before the later West-Saxon diphthongal rule
applies. This places [SC051 OESkPalatalization](#rule-OESkPalatalization)
before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

The narrower chapter shape matters. The cluster rule is real and historically
visible, but it is still only one part of the broader palatalizing sequence. The
change should therefore be read as a distinct cluster development inside that
sequence, not as a complete account of Old English palatalization.

\newpage

## Velar palatalization before front vowels

### Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168]. His emphasis falls on the environment first: velars
before bright vowels and in the vicinity of the palatal glide belong to one
early phonological sequence. The examples associated with that sequence, such as
*ceaster* ‘town’, *geaf* ‘gave’, *giefan* ‘give’, and *giest* ‘guest’, already
show that consonantal palatalization and later vowel effects stand close
together historically, even when they must be distinguished analytically
[@Luick1914, pp. 157--167, §§168--182].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440]. Elsewhere in the same part of the grammar he uses
forms such as *cild* ‘child’, *dæg* ‘day’, *giefan* ‘give’, and *giest*
‘guest’, which show how palatalized velars, palatal influence, and later
umlautal outcomes meet in the same region of the lexicon without collapsing
into one process [@Campbell1959, pp. 69--72, 89, §§170, 190--191].

Hogg makes the conditioning sharper still. He states that the change takes place
when the velar consonant is adjacent to and in the same syllable as a front
vowel or the palatal consonant `j` [@Hogg1992, pp. 103--104]. This formulation
is important because it moves the discussion from a broad list of palatal
outcomes to a more precise phonological environment involving adjacency and
syllable structure.

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and \emph{*sk} had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1]. Their own examples of the plain-velar rule,
such as \emph{weccan} ‘wake’, \emph{licgan} ‘lie’, \emph{lecgan} ‘lay’,
\emph{secg} ‘retainer’, \emph{ecg} ‘edge’, \emph{wicg} ‘horse’, and
\emph{brycg} ‘bridge’, illustrate the same point in lexical detail: front
vowels and `j` create the palatal environment in which plain `k` and `g` cease
to behave as plain velars [@RingeTaylor2014, pp. 213--214, §6.4.1].

Taken together, these accounts show a gradual tightening of focus. Luick treats
palatalization as a broad early movement. Campbell distinguishes more sharply
between plain velars and the `sk` complex. Hogg specifies the adjacency and
syllable conditions more directly. Ringe and Taylor then place the plain velar
change in an explicit sequence that leads forward to later West-Saxon
diphthongization. The literature therefore supports two claims at once: the
change belongs to a larger palatalizing environment, and it must be kept
distinct from neighboring processes if the sequence of developments is to be
described accurately.

### SC052. Palatalization of \emph{*k} before front vowels and \emph{*j} (`OEVelarPalatalizationKFront`) {#rule-OEVelarPalatalizationKFront}

The first part of the implementation isolates the `k`-side environments of the
change.

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
] ;
```

In prose, the rule turns plain `k` into a palatal outcome before front vowels
and `j`, including the geminated environment before `j`.

Historically, this section corresponds to the core of the older discussion of
palatalized velars. It captures the environments behind forms such as *weccan*
‘wake’, *licgan* ‘lie’, and *lecgan* ‘lay’, where front vowels or `j` trigger
the palatal outcome in the first place [@RingeTaylor2014, pp. 213--214,
§6.4.1]. It is also the part of the process that prepares forms later assumed by
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and, farther on, by
[SC055 OEIUmlautFronting](#rule-OEIUmlautFronting).

Within the present implementation, this helper rule is not ordered separately
from the broader velar-palatalization rule below. Its chronology is therefore
that of the larger rule it feeds. If the palatalization complex is moved before
Sievers-law syncope, PGmc \emph{*strákkijaną} yields *strecċan* ‘stretch’ rather
than expected OE *streċċan* ‘stretch’. If it is delayed beyond the umlautal
core, PGmc \emph{*kūi} and \emph{*lúnganjō} yield *ċȳ* ‘cows’ and *lunġen*
‘lungs’ rather than expected OE *cȳ* and *lungen*. The shared boundary pattern
is therefore clear. [SC050 SieversLawSyncope](#rule-SieversLawSyncope) must
come before [SC052 OEVelarPalatalizationKFront](#rule-OEVelarPalatalizationKFront), and the
palatalization complex must in turn come before [SC055 OEIUmlautFronting](#rule-OEIUmlautFronting).

### SC052. Velar palatalization before front vowels (`OEVelarPalatalization`) {#rule-OEVelarPalatalization}

The broader rule adds the `g` environments and composes them with the `k`
palatalization rule above.

```foma
define OEVelarPalatalization [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

In prose, the rule palatalizes plain `k` and `g` in front-vocalic and
`j`-adjacent environments. Writing it as a separate rule clarifies the relative
order of plain-velar palatalization, `sk`-palatalization, and umlautal
developments.

The rule belongs after the earlier syncope that prepares forms like *streċċan*
‘stretch’ and before the later umlautal rules that would otherwise
over-palatalize forms such as *cȳ* ‘cows’ and *lungen* ‘lungs’. See
[SC055 OEIUmlautFronting](#rule-OEIUmlautFronting) and
[SC055 OEIUmlaut](#rule-OEIUmlaut) below.

If the rule is moved too early, before the syncope that prepares the consonant
cluster, it breaks the derivation that should yield *streċċan* ‘stretch’. With
PGmc \emph{*strákkijaną} in the wrong order, the model produces *strecċan*
‘stretch’; the expected Old English form is *streċċan* ‘stretch’.

If it is moved too late, after i-umlaut, it over-palatalizes forms such as
*cȳ* ‘cows’ and *lungen* ‘lungs’. PGmc \emph{*kūi} then yields *ċȳ* ‘cows’;
the expected form is *cȳ* ‘cows’. PGmc \emph{*lúnganjō} yields *lunġen*
‘lungs’; the expected form is *lungen* ‘lungs’.

These lexical failures show that [SC050 SieversLawSyncope](#rule-SieversLawSyncope)
must come before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization)
and that [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) must come
before [SC055 OEIUmlaut](#rule-OEIUmlaut).

Once the rule is in place, plain velars before front vowels and `j` no longer
remain plain. They become the palatal outcomes presupposed by later
developments, including the umlautal rules discussed in
[SC055 OEIUmlautFronting](#rule-OEIUmlautFronting). That matters for
dictionary-like forms such as *cild* ‘child’ or *dæg* ‘day’ and for the broader
relation between consonantal palatalization and later vowel-fronting processes
[@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440; @RingeTaylor2014,
pp. 203--215, §§6.4.1, 6.5.1].

The evidence places the rule within a wider palatalizing environment, but it
does not require every neighboring palatal process to be merged with it. `sk`
belongs to a related but distinct development, and the later umlautal material
poses a different historical problem. The relation to the earlier syncope rule
is likewise specific and limited: the *streċċan* ‘stretch’ evidence shows a real
dependency without turning the feeder process into a coequal sound law of the
same scope.

\newpage

## Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}

### Historical discussion of early \emph{*w}-loss before umlaut

The two rules gathered here are unequal in weight. The first is a narrow loss of
\emph{*w} after velars in the \emph{*ngw} sequence. Ringe and Taylor make the historical core
clear when they derive PGmc \emph{*singwan} to Old English *singan* ‘sing’
[@RingeTaylor2014, p. 214, §6.4.2]. That gives the change a real comparative anchor, but
it does not turn it into a large chapter of its own. It is the kind of small
local sound change that needs a place in the sequence without claiming the status of a
major handbook law.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The chapter therefore belongs in the
stretch between plain palatalization and the umlautal core, but it should keep
the asymmetry visible: the first rule is a narrow loss in the \emph{*ngw} sequence, and the second is a
stronger glide-loss development with a specific lexical witness.

### SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

The first rule handles the \emph{*ngw} simplification.

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

In prose, the rule removes \emph{*w} after the velar cluster in forms of the
\emph{*singwan} type.

Historically, this is a very small rule. It keeps developments such as *singan*
‘sing’ visible in the sequence, but it does not create a large family of lexical
breakpoints. If the rule is moved earlier or later within the tested sequence,
no checked form yields a form different from the expected one. The tested forms
therefore do not place [SC053 OEPostVelarWLoss](#rule-OEPostVelarWLoss) before
or after any specific neighboring change. CAPR keeps it here because the
comparative evidence for `*singwan > singan` makes a narrow post-velar
\emph{*w}-loss historically plausible in this pre-umlaut stretch. Even so, the
placement should be read as approximate: the rule is a small prefatory note
before the better-attested glide-loss and umlautal developments to the right.

### SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

The second rule is the more historically legible member of the pair.

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

In prose, the rule removes non-initial \emph{*w} before final unstressed \emph{*i}.

The best witness is *sǣ* ‘sea’. Campbell's discussion of the loss of \emph{*w} before
\emph{*i}, Ringe and Taylor's derivation from earlier \emph{*saiwi-} / \emph{*sawi-}, and Luick's
parallel account all point to the same historical consequence
[@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. The glide has
to disappear early enough for the preceding vowel to continue into the later
fronted and lengthened outcome. If the glide survives too long, the derivation
retains \emph{*w} and misses *sǣ* ‘sea’. If the rule is moved before
[SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), the same witness yields *sǣw* ‘sea’ rather than
expected OE *sǣ*. This shows that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before
[SC054 OEWLossBeforeI](#rule-OEWLossBeforeI). If the rule is delayed until after
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), the same witness again yields *sǣw*
rather than expected *sǣ*. This places [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI)
before [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope).

The checked forms therefore place the rule within a wide pre-umlaut interval:
after [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) and before
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), without fixing close
neighbors on both sides. CAPR keeps it here because the handbooks treat the loss of
\emph{*w} before unstressed \emph{*i} as part of the pre-umlaut history behind
*sǣ* ‘sea’. The modeled placement should be read as a source-based choice
within that interval, with the chapter serving as a lead-in to the umlautal
material and not as a locally pinned pair on both sides.

\newpage

## The Old English i-umlaut and West Saxon palatal diphthongization

### Historical discussion of i-umlaut and West Saxon palatal diphthongization

Luick gives the change its traditional scale:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> [@Luick1914, pp. 166--167, §182]

Campbell gives the most compact classical formulation in English when he writes
that “the process known as i-umlaut or i-mutation operates on practically all
the sounds which it could theoretically affect in OE” [@Campbell1959, p. 69,
§190]. He immediately defines the core conditioning environment as a following
`i` or `j`, and he goes on to trace the consequences across much of the vowel
system, including forms such as *giest* ‘guest’, *giefan* ‘give’, *hierde*
‘shepherd’, and *ieldra* ‘older’ [@Campbell1959, pp. 69--72, §§190--197].

Hogg continues in the same vein: “we come now to a change which is almost as
uncontroversial as it is important” [@Hogg1992, p. 112]. His examples, such as
*bryd* ‘bride’, *trymman* ‘strengthen’, *bedd* ‘bed’, *ciest* ‘chest’, and
*wiersa* ‘worse’, likewise emphasize that the change is a broad redistribution
of vowel quality across the Old English vowel system [@Hogg1992,
pp. 112--114].

The narrower palatal-diphthongal material is described differently. Ringe and
Taylor treat West-Saxon diphthongization after initial palatals as a distinct
process [@RingeTaylor2014, p. 215, §6.5.1], and Fulk is even more explicit about
its chronological delicacy when he calls it “diphthongization by initial
palatal consonants (which precedes front umlaut but not breaking)”
[@Fulk2018, p. 74, §4.13]. Ringe and Taylor’s examples such as *gieldan* ‘pay’,
*scield* ‘shield’, and *scieppan* ‘create’ show that this narrower process is
triggered by already palatal consonants and leads to specifically West-Saxon
diphthongal outputs [@RingeTaylor2014, pp. 215--216, §6.5.1].

The sequence of discussion is fairly clear. Luick, Campbell, and Hogg all give
i-umlaut primary importance. Ringe and Taylor and Fulk then help separate that
major change from the narrower West-Saxon diphthongization that stands beside
it. The literature therefore establishes a large, system-wide umlautal change
and a narrower adjoining process affecting words after initial palatals. That
distinction matters because the two processes act in different environments and
produce different lexical consequences.

### SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

The first component of the implementation handles the broad fronting of vowels
under the influence of following `i` or `j`.

```foma
define OEIUmlautFronting [
    {*a} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ā} -> {*ǣ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*e} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*o} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ō} -> {*ē} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*u} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ū} -> {*ȳ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*á} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*é} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ó} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ú} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

In prose, the rule fronts and raises the relevant simple vowels when a following
`i` or `j` provides the trigger.

Historically, this is the most central part of the umlautal development
described by Luick, Campbell, Hogg, Ringe and Taylor, and Fulk. Within the
present implementation it stands after [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and before the narrower
West-Saxon palatal-diphthongization rule discussed below.

The handbooks describe the same conditioning environment in different ways but
with the same phonological consequence: a following high front vocoid triggers
the fronting of earlier back vowels. That is why forms such as *fylgan*
‘follow’, *gylden* ‘golden’, *wyrm* ‘worm’, and *giest* ‘guest’ can all be
treated inside the same formal rule even though they belong to different lexical
classes [@RingeTaylor2014, p. 222, §6.6.1; @Campbell1959, pp. 69--72,
§§190--191].

The same ordering logic that governs the umlaut complex governs this component.
If the umlautal rule set is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc \emph{*kūi} yields *ċȳ*
‘cows’ rather than expected OE *cȳ*, and \emph{*lúnganjō} yields *lunġen*
‘lungs’ rather than expected OE *lungen*. At the other edge, the later
West-Saxon diphthongization must follow the umlautal rule set: if that later
rule is moved too early, PGmc \emph{*géftiz} yields *ġieft* ‘gift’ rather than
expected OE *ġift*, and \emph{*skáiθiz} yields *sċǣþ* ‘sheath’ rather than
expected *sċēaþ*. This shows that [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization)
must come before [SC055 OEIUmlautFronting](#rule-OEIUmlautFronting), and that
[SC055 OEIUmlautFronting](#rule-OEIUmlautFronting) must come before
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

As a component rule, it shares the chronology of [SC055 OEIUmlaut](#rule-OEIUmlaut).

### SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

The second component handles the raising of umlauted `æ` to `e`.

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

In plain language, this rule takes the fronted low vowel created by the earlier
fronting rule and raises it further where the same umlaut trigger still holds.

Historically, this belongs inside the same broad i-umlaut development. It is
part of the same chronological development and shares the evidence base of
[SC055 OEIUmlaut](#rule-OEIUmlaut).

Like the fronting component, this raising rule falls between
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). If the umlaut complex is moved before
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), \emph{*kūi} yields *ċȳ*
instead of expected *cȳ* and \emph{*lúnganjō} yields *lunġen* instead of
expected *lungen*. If the later West-Saxon diphthongization is moved too early,
\emph{*géftiz} yields *ġieft* rather than expected *ġift*, and \emph{*skáiθiz}
yields *sċǣþ* rather than expected *sċēaþ*.

These outcomes show that [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization)
must come before [SC055 OEIUmlautRaising](#rule-OEIUmlautRaising), and that
[SC055 OEIUmlautRaising](#rule-OEIUmlautRaising) must come before
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

This narrower subrule matters because the sources do not describe umlaut as
simple fronting alone. Campbell explicitly notes that the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@Hogg1992, p. 112].

### SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

The third component handles the diphthongal outcomes that also undergo
i-umlaut.

```foma
define OEIUmlautDiphthong [
    {*ea} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēa} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*io} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*īo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*eo} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éa} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éo} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ío} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

In prose, the rule states that diphthongal inputs are subject to umlaut as well:
the vowel change is not confined to simple vowels.

This matters historically because the handbooks describe i-umlaut as a
system-wide assimilatory development. The rule therefore stands inside the same
chronological bracket as [SC055 OEIUmlautFronting](#rule-OEIUmlautFronting) and
[SC055 OEIUmlautRaising](#rule-OEIUmlautRaising), even though its outputs are
shaped differently.

The relevant examples are the recurring West-Saxon `ie` forms cited in the
handbooks, including *giest* ‘guest’, *giefan* ‘give’, and *hierde*
‘shepherd’ in Campbell and *ciest* ‘chest’ in Hogg
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @Hogg1992,
pp. 112--114]. The present formalization keeps those diphthongal outcomes
visible as a distinct part of the general umlautal development and does not
leave them implicit under the broad description of fronting.

Chronologically, this component also shares the same evidence as the umlaut
complex as a whole. If the umlaut complex is moved before
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), it
over-palatalizes
\emph{*kūi} and \emph{*lúnganjō}; too-early West-Saxon diphthongization yields
*ġieft* and *sċǣþ* instead of expected *ġift* and *sċēaþ*. The rule therefore
belongs between [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). This places
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) before
[SC055 OEIUmlautDiphthong](#rule-OEIUmlautDiphthong), and it places
[SC055 OEIUmlautDiphthong](#rule-OEIUmlautDiphthong) before
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

### SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

The implementation also defines a composite rule that composes the three
preceding parts.

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

In prose, this says that the implementation treats the umlaut as a sequence of
fronting, raising, and diphthongal adjustments composed in order.

Chronologically, the composite rule must follow
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization). If it is
moved too early, forms such as *cȳ* ‘cows’ and *lungen* ‘lungs’ become
over-palatalized. PGmc \emph{*kūi} yields *ċȳ* ‘cows’; the expected form is
*cȳ* ‘cows’. PGmc \emph{*lúnganjō} yields *lunġen* ‘lungs’; the expected form
is *lungen* ‘lungs’.

The same local network gives the later boundary. If West-Saxon palatal
diphthongization is moved too early, PGmc \emph{*géftiz} yields *ġieft* ‘gift’
rather than expected OE *ġift*, and \emph{*skáiθiz} yields *sċǣþ* ‘sheath’
rather than expected *sċēaþ*. The composite umlaut rule therefore must apply
after [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and before
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).

Those failures show that the broad umlautal rule needs an earlier terminus post
quem in the palatalization sequence, even though it remains the main vowel
change within the present chapter.

The composite rule is important because the literature presents the umlaut as a
single historical development even while the implementation decomposes it into
formal parts. The composite definition is the point at which the separate
fronting, raising, and diphthongal effects are treated as one chronological
event in the Old English sequence.

### SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

The narrower West-Saxon rule is treated separately from the broader umlautal
complex.

```foma
define OEWsPalatalDiphthongization [
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

In prose, this rule diphthongizes certain vowels after already palatal
consonants in West Saxon. It therefore has a narrower dialectal and
chronological scope than the broader umlaut rule.

The historical evidence for that narrower scope is concrete. Ringe and Taylor
illustrate the rule with forms such as *gieldan* ‘pay’, *scield* ‘shield’, and
*scieppan* ‘create’, where an already palatal consonant triggers the diphthongal
outcome [@RingeTaylor2014, pp. 215--216, §6.5.1]. Hogg’s *giefan* ‘give’ and
*sceap* ‘sheep’ material belongs to the same phonological zone
[@Hogg1992, pp. 108--109], while Fulk distinguishes this
palatal-consonant-triggered diphthongization from the broad front-mutation
process [@Fulk2018, p. 74, §4.13].

Its place is later than [SC055 OEIUmlaut](#rule-OEIUmlaut).
If this rule is moved too early, the later ordering is constrained by forms such
as *ġift* ‘gift’ and *sċēaþ* ‘sheath’. PGmc \emph{*géftiz} then yields
*ġieft* ‘gift’; the expected form is *ġift* ‘gift’. PGmc \emph{*skáiθiz}
yields *sċǣþ* ‘sheath’; the expected form is *sċēaþ* ‘sheath’.

This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). No
comparably sharp later boundary is available.

No tested lexical item provides a comparably precise later terminus ante quem.
The available evidence therefore establishes the rule’s relation to the earlier
umlautal process much more clearly than it fixes a later point by which it must
already have applied.

The two rules should accordingly be kept distinct. The broad umlautal rule
accounts for a system-wide assimilatory change; the West-Saxon rule accounts for
a narrower palatal-consonant-conditioned diphthongization whose chronological
and dialectal scope is more restricted.

\newpage

## J-cluster coalescence

### Historical discussion

This chapter belongs to the later part of the palatalization and fronting
region. Campbell, Ringe and Taylor, and Fulk all discuss the same neighborhood
of palatalized and fronted outcomes that underlies forms such as *bīeġan*
‘bend’ and *sēċan* ‘seek’ [@Campbell1959, pp. 89, 107--108, §§170, 248--251;
@RingeTaylor2014, pp. 213--251, §§6.4.1, 6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75, §§4.7, 4.13]. None
of them turns this later cluster adjustment into a major independent headline.
The historical interest lies in the fact that it remains a real part of the
sequence even though the larger palatalization and umlaut chapters carry more of
the explanatory weight.

That narrower scale matters. Earlier chapters have already established the plain
velar and \emph{*sk} palatalizations, and the umlaut chapter has already handled the
major vowel consequences. The present rule is a later coalescence inside that
same neighborhood. It deserves explicit prose because the lexical outcomes are
clear, not because it eclipses the larger processes around it.

### SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence}

The implementation keeps the later cluster coalescence very small and explicit.

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

In prose, the rule coalesces \emph{*gj} and \emph{*kj} into the palatal outcomes that later
surface in forms such as *bīeġan* ‘bend’ and *sēċan* ‘seek’.

Its earlier dependency is clearer than its later limit. If the rule is moved
before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization),
the developments behind *bīeġan* ‘bend’ and *sēċan* ‘seek’ are lost. Related forms such as *fylġan* ‘follow’,
*heċġ* ‘hedge’, and *sengan* ‘singe’ fail in the same broader palatalization
zone. PGmc `*báugijaną` yields *bēaġan* ‘bend’ rather than expected OE *bīeġan*,
and PGmc `*sōkijaną` yields *sōċan* ‘seek’ rather than expected *sēċan*. This
shows that [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) must come
before [SC057 OEJClusterCoalescence](#rule-OEJClusterCoalescence). No comparably sharp later lexical
breakpoint emerges within the remaining sequence, so the chronology remains
short and one-sided.

That modest shape is historically appropriate. The rule is a real later member
of the palatalization region, but it does not need to absorb the umlautal
chapter behind it or the nasal-dissimilation chapter that follows it. The
later coalescence remains visible in the sequence once the
larger neighboring chapters are already in place.

\newpage

## Nasal dissimilation

### Historical discussion

Luick preserves individual outcomes such as *enetre* ‘yearling’ (with the
spelling *enitre* in his text) without isolating a separate law around them
[@Luick1914, p. 166]. Campbell likewise reaches forms such as *heofon* ‘heaven’
in a discussion of suffixal variation and does not set them off in any special
section on nasal dissimilation [@Campbell1959, p. 155]. Hogg mentions *heofon*
‘heaven’ in the course of his account of back mutation, again without isolating
a separate law [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that *enetre* ‘yearling’ reflects “loss of the second
\emph{*n} by dissimilation” [@RingeTaylor2014, p. 282].

The discussion therefore develops from scattered lexical observations to a more
explicit but still cautious generalization. Luick preserves the kind of form the
rule is meant to capture. Campbell and Hogg show that related outcomes enter the
handbooks, but only incidentally, as part of larger accounts of other changes.
Fulk makes the recurrent `mn` tendency explicit, while Ringe and Taylor provide
an exact lexical case in *enetre* ‘yearling’. What emerges is a limited but
recurring dissimilatory pattern whose scope is far smaller than that of the
major Old English vowel laws.

### SC058. Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation}

The implementation formalizes the change as a narrow rule applying in short
vowel environments before a following `n`.

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

In plain language, the rule turns medial `m` into `f` in a restricted
short-vowel environment before a following syllable containing `n`.

Historically, the rule captures the limited type of dissimilation reflected in
forms such as *heofon* ‘heaven’, *fæstenn* ‘fasting’, and *enetre* ‘yearling’.
It is much narrower than the major vowel changes and is best understood as a
recurring but partly lexicalized pattern.

The relation between the sources and the formalization is correspondingly close
but not exact. Fulk formulates the tendency at the level of `mn` clusters and
illustrates it with *heofon* ‘heaven’ and *fæstenn* ‘fasting’
[@Fulk2018, p. 121, §6.11]. Ringe and Taylor show the same kind of development
in *enetre* ‘yearling’ [@RingeTaylor2014, p. 282]. Campbell’s “heofon is for
older hefzen” and Hogg’s sequence \emph{*hefon > heofon} preserve outcomes
of the same kind as those modeled here [@Campbell1959, p. 155;
@Hogg1992, p. 112]. The formal rule is therefore narrower than the total set of
handbook remarks: it models one plausible recurrent environment and does not
claim to exhaust every dissimilatory development involving nasals.

Chronologically, the order test does not by itself determine a sharper position
within the Old English sequence. If the rule is moved earlier or later within
the tested sequence, no checked form yields a form different from the expected
one. The tested forms therefore do not place
[SC058 OENasalDissimilation](#rule-OENasalDissimilation) before or after any
specific neighboring change.

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the *heofon* ‘heaven’, *fæstenn* ‘fasting’,
and *enetre* ‘yearling’ type discussed in the literature [@Fulk2018, p. 121,
§6.11; @RingeTaylor2014, p. 282; @Campbell1959, p. 155; @Luick1914, p. 166;
@Hogg1992, p. 112]. Without an explicit rule, those outcomes would be left to
diffuse analogy or to unexplained exception lists.

The evidence points to a narrow dissimilatory tendency, especially in `mn`-type
clusters and a small group of lexical outcomes. There is no support for a
regular change operating across a broad phonological field. The rule is secure
enough to model, but the available tests leave its position within the Old
English sequence underdetermined. CAPR keeps it in this middle Old English
stretch because the relevant lexical outcomes are discussed alongside
surrounding weak-vowel and suffixal developments, not because the handbooks fix
a closer relative chronology.

\newpage

## Back mutation

### Historical discussion

Back mutation is the substantive center of this part of the sequence. Campbell treats
it as a later Old English diphthongizing development before following back
vowels, and his examples already show why forms such as *heofon* ‘heaven’ are
historically legible outcomes in their own right
[@Campbell1959, p. 86, §207]. Hogg treats the same development as a later change with
clear parallels to breaking [@Hogg1992, p. 112]. Ringe and Taylor sharpen the
picture by distinguishing West Saxon forms such as *giefan* ‘give’ and *wefan*
‘weave’ from non-West-Saxon forms such as *geofad* and *weofan*
[@RingeTaylor2014, p. 319, §6.9.4]. Fulk likewise treats back mutation as a distinct
historical phenomenon with its own profile beside the earlier umlautal
changes [@Fulk2018, p. 69, §4.8].

That makes back mutation different from the short notes that follow it. Back
mutation belongs to the same local stretch of the sequence, but it carries more
historical weight and clearer lexical consequences. Even so, its later relation
lies beyond this immediate stretch of the sequence, and the later weak-tail
region is best kept as a forward reference only.

### SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

The implementation keeps the change as one explicit rule.

```foma
define OEBackMutation [
    {*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger,
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
];
```

In prose, the rule backs and diphthongizes earlier front vowels before a
following labial or liquid plus a back-vocalic trigger.

Its chronology is real on both sides, but not equally local. The earlier side is
already fixed by the preceding vowel and weak-tail material. If the rule is
moved too early, forms such as \emph{*gébaną} produce *ġeofan* ‘give’; the
expected form is *ġiefan* ‘give’. \emph{*stélaną} likewise produces *steolan*
‘steal’; the expected form is *stelan* ‘steal’. The later side is different. If
the rule is pushed too far to the right, \emph{*wébaną} yields *weofan*
‘weave’; the expected form is *wefan* ‘weave’.
That later edge is real, but it points beyond the present stretch of the sequence into the
later weak-tail reductions, so here it should remain only a forward reference.

These lexical failures show that [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) must come before
[SC059 OEBackMutation](#rule-OEBackMutation) and that
[SC059 OEBackMutation](#rule-OEBackMutation) must come before
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction).

The checked forms therefore place the rule within a wider later-vowel interval.
The nearer earlier
constraint is [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization);
the later relation to [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction)
mainly shows that back mutation must precede the wider weak-tail reductions.
CAPR keeps the rule here because the handbooks treat back mutation as a distinct
later vowel development between the earlier mutation/restoration material and
the closing weak-tail reductions.

\newpage

## West Saxon palatal umlaut

### Historical discussion

The evidence is narrow enough that the discussion can stay brief. Campbell and Ringe and Taylor both support the
development behind forms such as *miht* ‘might’ and *niht* ‘night’, while Fulk's
broader chronology makes clear that this material belongs beside the umlaut and
palatal-vowel region as a subordinate note beside it
[@Campbell1959, pp. 107--108, §§248--251; @RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4;
@Fulk2018, pp. 65, 75, §§4.7, 4.13].

That is why the note belongs here after back mutation even though its clearest
historical tie still reaches back to the earlier umlautal chapter. The
phenomenon is real, yet its place in the sequence is one-sided. The evidence is
clear enough to state and narrow enough to remain brief.

### SC060. West Saxon palatal umlaut before \emph{*h}-clusters (`OEWsPalatalUmlaut`) {#rule-OEWsPalatalUmlaut}

The implementation treats the West Saxon change as one explicit rule.

```foma
define OEWsPalatalUmlaut [
    {*eo} -> {*i} || _ OEHCluster .#.,
    {*io} -> {*i} || _ OEHCluster .#.,
    {*ie} -> {*i} || _ OEHCluster .#.,
    {*eo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*io} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ie} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*éo} -> {*i} || _ OEHCluster .#.,
    {*ío} -> {*i} || _ OEHCluster .#.,
    {*íe} -> {*i} || _ OEHCluster .#.,
    {*éo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ío} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*íe} -> {*i} || _ OEHCluster EnglishStarFrontVowel
];
```

In prose, the rule reduces short diphthongs to \emph{*i} before the relevant \emph{*h}
clusters.

The crucial point is its earlier dependency. The rule must follow
[SC055 OEIUmlaut](#rule-OEIUmlaut), because if it is moved too early
the forms behind *miht* ‘might’ and *niht* ‘night’ remain at the overdeveloped
stage *mieht* and *nieht* rather than expected OE *miht* and *niht*. No comparably sharp later lexical breakpoint emerges
within the remainder of the section. The note therefore belongs here as a short
afterpiece to the umlaut chapter, not as the start of a new larger unit.

This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut). No comparably sharp later
boundary is available.

\newpage

## Weak-tail nasal loss

### Historical discussion

The development belongs to the narrower end of the later weak-tail sequence. It is historically
legible through the pathway that leads to *dōn* ‘do’, and the broader late
weak-tail setting is supported by the usual handbook discussions of apocope and
related reduction [@Campbell1959, pp. 144--145, §§345--349; @Hogg1992, pp. 120--121;
@Fulk2018, p. 91, §5.6]. But the decisive lexical tie lies much farther back in the
sequence, in the older development of \emph{*dōną}. That keeps the note real,
while also keeping it small.

Within this later run of changes it follows back mutation and West Saxon
palatal umlaut, but the evidence remains slighter than theirs.

### SC061. Reduction of final nasal weak-tail endings (`OEWeakTailNasalLoss`) {#rule-OEWeakTailNasalLoss}

The implementation keeps the change as one short rule.

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

In prose, the rule reduces final weak-tail endings of the type \emph{*-ną} and
\emph{*-mą} to plain final \emph{*-n} and \emph{*-m}.

The clearest lexical witness is the pathway to *dōn* ‘do’. If the rule is moved
too early, before the older reduction that already shapes the \emph{*dōną}
sequence,
the derivation records no output instead of expected OE *dōn* ‘do’. No equally
sharp later breakpoint appears within the tested sequence. That is why the note remains
one-sided and why its earlier relation should be understood as a distant
cross-reference only and should not reshape the broader sequence.

This shows that [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must come before
[SC061 OEWeakTailNasalLoss](#rule-OEWeakTailNasalLoss). No comparably sharp later
boundary is available.

The development is best treated as a small late weak-tail adjustment. It remains
visible in the sequence because it affects the pathway to *dōn* ‘do’, but the
evidence does not support treating it as the center of a wider historical
development.

\newpage

## High-vowel apocope

### Historical discussion

By this point in the sequence the main palatal and umlautal changes are already in place, but weak-tail reduction is not finished. Final high vowels still survive in many forms until a late apocope removes them after heavy syllables and in the relevant trisyllabic patterns. Campbell, Hogg, Ringe and Taylor, and Fulk all describe this as a real Old English development, even when they differ over how much of the surrounding syncope material should be grouped with it [@Campbell1959, pp. 144--145, §§345--349; @Hogg1992, p. 120; @RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].

The rule matters because it makes many familiar Old English forms look abruptly shorter than their earlier stages. It is also a good place to show how finite-state chronology works. The derivation can say exactly which forms fail if apocope is moved too early or too late, so the late weak-tail sequence becomes visible through concrete lexical breakpoints and explicit ordering statements.

### SC063. High-vowel apocope after heavy syllables and in trisyllables (`OEHighVowelApocope`) {#rule-OEHighVowelApocope}

The implementation keeps the whole apocope system in one explicit rule.

```foma
define OEHighVowelApocope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
];
```

In prose, the rule deletes final \emph{*i}, \emph{*u}, and \emph{*ų} when the preceding structure is heavy enough, or when a trisyllabic form behaves as equivalent to a heavy environment. The longer code box makes visible how many separate environments the transducer has to distinguish in order to realize what the handbooks describe more compactly.

Its chronology is explicit on both sides. If the rule is moved before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*kūi} yields *cū* rather than
expected OE *cȳ* ‘cow’, and PGmc \emph{*brūdiz} yields *brūd* rather than
expected OE *brȳd* ‘bride’. If the rule is delayed until after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*fúrxtīnaz} yields *fyrht*
rather than expected OE *fyrhte* ‘fright’. This means that
[SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), and that
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope) must come before
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).

That placement is historically apt. The rule must come late enough for umlautal effects to have already been created, but it is not the last weak-tail event in the language. Apocope removes a major set of final high vowels, yet later weak-tail reductions still remain.

\newpage

## Post-apocope \emph{*n}-loss and medial syncope

### Historical discussion of post-apocope \emph{*n}-loss and medial syncope

After high-vowel apocope the weak tail is still not entirely settled. Hogg, Ringe and Taylor, and Fulk all describe a late region in which further medial reduction and cluster pressure remain active, even though the evidence is much less even than it was for the main apocope rule [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4; @Fulk2018, p. 91, §5.6]. The inherited \emph{*furht-} family adds one especially narrow witness of its own, because it shows that a single surviving nasal can still decide whether the weak-tail output is right or wrong [@Kroonen2013, p. 201].

This chapter is therefore intentionally modest. One rule has real positive chronology on both sides, but only through a single witness family. The other belongs naturally to the same late region without yet producing a comparably sharp first-break result. Keeping both visible makes the weak-tail aftermath more honest than either silence or overstatement would.

### SC064. Loss of stem-final \emph{*n} after long \emph{*ī} (`NWGmcInStemNLoss`) {#rule-NWGmcInStemNLoss}

The first rule is extremely narrow in form.

```foma
define NWGmcInStemNLoss [{*n} -> 0 || {*ī} _ .#.];
```

In prose, it removes a final \emph{*n} after long \emph{*ī}. That looks tiny on the page, but the effect is real in the inherited family behind *fyrhte* ‘fright’.

The chronology is two-sided even though the witness base is not broad. If the
rule is moved before [SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), PGmc \emph{*fúrxtīnaz} yields
*fyrhten* rather than expected OE *fyrhte* ‘fright’. If the rule is delayed
until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the same PGmc form again
yields *fyrhten* rather than expected *fyrhte*. This shows that
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss) must come before
[SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), and it places
[SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) before
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).

That symmetry does not make the rule large. Both boundaries are carried by the same witness family, so the evidence is real but narrow. The checked forms therefore place [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) within a wider post-apocope interval between earlier final-loss material and later unstressed-vowel shortening. CAPR keeps the rule here because the `fright` family belongs to that broader weak-tail aftermath.

### SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

The second rule formalizes one narrower slice of late medial syncope.

```foma
define OEMedialSyncope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
];
```

In prose, it deletes medial \emph{*i} before a following dental after a heavy syllable. The broader historical background is secure enough, since the handbooks do treat late medial syncope as part of the same weak-tail region [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4; @Fulk2018, p. 91, §5.6].

The finite-state chronology is much weaker, however. If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC065 OEMedialSyncope](#rule-OEMedialSyncope) before or after any specific neighboring change. CAPR places it here because the handbooks treat late medial syncope as part of the post-apocope weak-tail sequence that continues into the later syncope-and-cluster-simplification material. The placement should be read as approximate, not as a local ordering forced by the tested forms.

That limitation is worth stating plainly. Late medial syncope belongs in the history of the weak tail, but this particular rule does not yet have a diagnostic constraint of its own on either side.

\newpage

## Late syncope and degemination

### Historical discussion of late syncope and degemination

Once later medial syncope begins to bite, the language inherits new consonant clusters that do not always remain stable. Hogg and Ringe and Taylor both describe this connection between vowel loss and later consonant simplification, while Brunner's discussion of *netle* ‘nettle’ beside later *netele* keeps the syncope evidence tied to a concrete lexical type [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2; @SieversBrunner1965, pp. 144--145, §§158--159]. Fulk is especially useful for the larger timing, because he places this syncope after i-umlaut [@Fulk2018, p. 91, §5.6].

The resulting chapter has an uneven center of gravity. Syncope itself is well motivated, one downstream degemination rule has a clear lexical breakpoint, and the dental assimilation step between them is plausible without yet being independently well anchored. That imbalance is part of the point. The sequence shows how the transducer can make a narrow chain of consequences explicit without pretending that every member has the same evidential weight.

### SC066. L-adjacent syncope in medial syllables (`OELAdjacentSyncope`) {#rule-OELAdjacentSyncope}

The syncope rule is stated directly.

```foma
define OELAdjacentSyncope [
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
];
```

In prose, it deletes medial \emph{*i} before \emph{*l}, creating forms such as *netle* ‘nettle’ and *spinl* ‘spindle’.

Its chronology is explicit on both sides. If the rule is moved before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*nátilōn} yields *nætle* rather
than expected OE *netle* ‘nettle’, and PGmc \emph{*spénnilō} yields *spenl*
rather than expected *spinl* ‘spindle’. If the rule is delayed until after
[SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination), PGmc \emph{*spénnilō} yields *spinnl* rather than expected *spinl*. This shows that
[SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope), and that
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) must come before
[SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination).

The checked forms therefore place the rule in a wider late-syncope interval. The later relation to [SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination) is the nearer local result; the earlier boundary at [SC055 OEIUmlaut](#rule-OEIUmlaut) mainly shows that this syncope belongs after the umlautal phase described in the handbooks. CAPR keeps it here as the opening step in the syncope-and-cluster-simplification sequence.

### SC067. Dental assimilation in newly formed clusters (`OEDentalAssimilation`) {#rule-OEDentalAssimilation}

The dental repair step is formally very short.

```foma
define OEDentalAssimilation [
    {*θ} -> 0 || {*t} _
];
```

In prose, it removes \emph{*θ} after \emph{*t} when syncope has created an over-heavy dental cluster. That kind of cluster simplification is historically plausible as part of the same late sequence that follows syncope [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC067 OEDentalAssimilation](#rule-OEDentalAssimilation) before or after any specific neighboring change.

That makes the rule best read as a narrow intermediate step inside the late syncope sequence. It is useful in the derivation, but the present evidence does not justify treating it as a stronger chronology anchor than it is. The handbooks support the broader pattern of syncope followed by cluster simplification, while CAPR states this dental simplification as a separate step. The placement is therefore historically plausible but approximate, not a tightly fixed local ordering.

### SC068. Preconsonantal degemination before sonorants (`OEPreconsonantalDegemination`) {#rule-OEPreconsonantalDegemination}

The final degemination rule is written as one composed definition.

```foma
define OEPreconsonantalDegemination OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN;
```

In prose, it simplifies doubled \emph{*tt} or \emph{*nn} before a following sonorant. The historical logic is straightforward enough. Once syncope has created a cluster such as the one behind *spinl* ‘spindle’, the doubled consonant does not remain [@RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

Its positive evidence is one-sided but exact. If the rule is moved before
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope), PGmc \emph{*spénnilō}
yields *spinnl* rather than expected OE *spinl* ‘spindle’. This shows that
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) must come before
[SC068 OEPreconsonantalDegemination](#rule-OEPreconsonantalDegemination). If the
rule is moved later within the tested sequence, no checked form yields a form
different from the expected one.

That one-sided profile is still meaningful. The checked forms fix the earlier
relation but do not identify a corresponding later constraint. CAPR keeps the
rule here because the sources treat this simplification as a follower to the
syncope-created cluster sequence.

\newpage

## Early o-shortening

### Historical discussion

By the time the sequence reaches this point, the language has already undergone the larger palatal and umlautal reorganizations to the left. What now comes into view is a later weak-tail region in which unstressed vowels are shortened, fronted, merged, and in some forms lost altogether. Campbell's discussion of early shortening of unaccented long vowels helps place this material in the larger history, while Hogg, Ringe and Taylor, and Fulk all describe the same late region through the intertwined history of apocope, syncope, shortening, and later reductions [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--96, §§5.6--5.7].

Early o-shortening belongs at the opening of that region, but it is not its strongest hinge. The evidence is broader and more distant than it is for the rules that follow, especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening). The rule therefore works best as an opening note that makes the chronology legible without pretending that the whole late weak tail begins and ends here.

### SC069. Early shortening of unstressed \emph{*ō} before nasals (`OEEarlyOShortening`) {#rule-OEEarlyOShortening}

The implementation isolates the early shortening step as one rule.

```foma
define OEEarlyOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ EnglishStarNasal
];
```

In prose, the rule shortens unstressed long \emph{*ō} before a following nasal. Because this shortening happens early, the resulting \emph{*a} can still participate in the later fronting and merger that shape many weak final syllables.

Its chronology is real, but it is one-sided. If the rule is moved before [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss), PGmc \emph{*nḗdrōn} yields *nǣdran* rather than expected OE *nǣdre* ‘adder’, PGmc \emph{*érθōn} yields *eorþan* rather than expected *eorþe* ‘earth’, and PGmc \emph{*fláskōn} yields *flascan* rather than expected *flasce* ‘flask’. The same earlier shift also disrupts forms such as *heorte* ‘heart’ and *līne* ‘line’. This broad set of failures shows that [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must come before [SC069 OEEarlyOShortening](#rule-OEEarlyOShortening).

If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one. The checked forms therefore do not identify a corresponding later constraint. CAPR keeps the rule here because the sources treat early \emph{*ō}-shortening as an opening step in the later weak-tail sequence, not as the central chronology seam of the region.

\newpage

## Early unstressed fronting and later o-shortening

### Historical discussion of early unstressed fronting and later o-shortening

The next pair forms a clearer local hinge. Campbell's account of shortening of unaccented long vowels is still relevant here, but the real value of the pair lies in the way the finite-state derivation separates an earlier fronting stage from a later shortening stage. Hogg, Ringe and Taylor, and Fulk all place these developments inside the same late weak-tail region in which shortening, syncope, and final-vowel adjustment continue to interact [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--96, §§5.6--5.7].

The hierarchy inside the pair is not flat. [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) is the stronger hinge because it has an earlier and a later lexical breakpoint. [SC071 OELateOShortening](#rule-OELateOShortening) confirms the same seam from the right, but its later side remains open within the tested range. That imbalance is historically useful: it shows how the late weak tail is held together by small but concrete lexical breakpoints, not by one single undifferentiated rule.

### SC070. Early fronting of unstressed \emph{*a} (`OEUnstressedFrontingEarly`) {#rule-OEUnstressedFrontingEarly}

The implementation gives the early fronting stage its own named step.

```foma
define OEUnstressedFrontingEarly OEUnstressedAFronting;
```

In prose, the rule fronts unstressed \emph{*a} to \emph{*æ} at the point where the earlier shortening has already created a frontable vowel, but the later shortening of unstressed \emph{*ō} has not yet happened. This is the step that makes endings such as OE \emph{-en} possible in forms like *lungen* ‘lungs’.

Its chronology is explicit on both sides. If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc \emph{*lúnganjō} yields *lunġen* rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc \emph{*búrōθi} yields *boreþ* rather than expected OE *boraþ* ‘bears’, and PGmc \emph{*mḗnōθz} yields *mōneþ* rather than expected *mōnaþ* ‘month’. This shows that [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) must come before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), and that [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) must come before [SC071 OELateOShortening](#rule-OELateOShortening).

That two-sided pattern is why [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) serves as the hinge of the pair. The later relation to [SC071 OELateOShortening](#rule-OELateOShortening) is the closer local result, while the earlier boundary at [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) mainly shows that this fronting belongs after the older palatal developments. CAPR keeps it here as an early stage inside the later unstressed-vowel sequence.

### SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

In prose, the rule shortens the remaining unstressed long \emph{*ō} after the earlier fronting stage has already done its work. This is the stage that leaves the later “stable a” endings behind forms such as OE *boraþ* ‘bears’ and *liornaþ* ‘learns’.

Its earlier boundary is the reciprocal side of the [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) relation. If the rule is moved before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc \emph{*búrōθi} yields *boreþ* rather than expected OE *boraþ*, and PGmc \emph{*líznōθi} yields *liorneþ* rather than expected *liornaþ*. No equally sharp later breakpoint appears within the tested range, so the available evidence shows only that [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) must come before [SC071 OELateOShortening](#rule-OELateOShortening).

This one-sided profile is appropriate to the chapter. [SC071 OELateOShortening](#rule-OELateOShortening) is a real follower in the same pair, but it does not need to carry more chronology than the evidence supports.

\newpage

## Unstressed long-vowel shortening and ae-merger

### Historical discussion of unstressed long-vowel shortening and ae-merger

This pair is the strongest internal seam in the late weak tail. Campbell's discussion of shortening of unaccented long vowels gives the classical background, while Ringe and Taylor place shortening of unstressed long vowels among the last prehistoric Old English changes and then carry the story forward into the immediately following developments [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--96, §§5.6--5.7]. What the finite-state derivation adds is a very sharp distinction between the shortening itself and the later merger of unstressed \emph{*æ} with \emph{*e}.

That is why this chapter can be more substantial than the opening note or the earlier pair. [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) have a real reciprocal relation in the cards, and the chapter can show both sides of it directly. The pair also keeps its outward relations in view: [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) remains the earlier prerequisite for shortening, while [SC085 OEHLoss](#rule-OEHLoss) remains the later outward handoff from the merger.

### SC072. Shortening of unstressed long vowels (`OEUnstressedLongVowelShortening`) {#rule-OEUnstressedLongVowelShortening}

The implementation keeps the shortening stage as one composed rule.

```foma
define OEUnstressedLongVowelShortening OEUnstressedLongVowelShortening1
    .o. OEUnstressedLongVowelShortening2
    .o. OEUnstressedLongVowelShortening3
    .o. OEUnstressedLongVowelShortening5
    .o. OEUnstressedLongVowelShortening6
    .o. OEUnstressedLongVowelShortening7
    .o. OEUnstressedLongVowelShortening8;
```

In prose, the rule shortens the remaining unstressed long vowels before the weak final outcomes settle into their later forms. The broad effect is visible in many weak endings, but the chronology can still be pinned down by a few particularly clear witnesses.

Its chronology is explicit on both sides. If the rule is moved before [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), PGmc \emph{*fúrxtīnaz} yields *fyrhten* rather than expected OE *fyrhte* ‘fright’. If the rule is delayed until after [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*nḗdrōn} yields *nǣdræ* rather than expected OE *nǣdre* ‘adder’, and PGmc \emph{*fádēr} yields *fædær* rather than expected *fæder* ‘father’. This shows that [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), and that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

That two-sided relation makes [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) the historical center of the pair. It still depends on earlier weak-tail preparation to the left, but within the local chapter it is the shortening stage that creates the strongest seam.

### SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger OEWeakTailReduction3;
```

In prose, the rule merges unstressed \emph{*æ} with \emph{*e} after shortening has already produced the vulnerable weak final vowels. This is the stage that turns a broad set of final outcomes toward the ordinary OE \emph{-e} spellings.

Its earlier and later relations are both concrete. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*nḗdrōn} yields *nǣdræ* rather than expected OE *nǣdre*, and PGmc \emph{*fádēr} yields *fædær* rather than expected *fæder*. If the rule is delayed until after [SC085 OEHLoss](#rule-OEHLoss), PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. This means that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), and that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss).

The checked forms therefore give the pair a close internal seam on the left and a broader outward limit on the right. [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) is the adjacent partner that fixes the local order; the later relation to [SC085 OEHLoss](#rule-OEHLoss) mainly shows that the merger must precede the closing h-loss and contraction region. That is why this pair works as the strongest local core in the late weak tail without absorbing the later closing cluster into the chapter.

\newpage

## Medial unstressed-i lowering

### Historical discussion of medial unstressed-i lowering and \emph{*ng} retention

The next pair belongs to the same late weak-tail region as the shortening and merger chapter to the left, but it is smaller and more locally conditioned. Hogg and Ringe and Taylor both treat the late weakening and merger of unstressed vowels as part of a continuing history, and that background helps explain why the present chapter reads best as a narrow follow-on, not a new center of gravity [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 327--332, §§6.9.5--6.9.6]. The specific value of the pair is derivational. [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) generalizes a medial unstressed-\emph{i} lowering, while [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering) immediately narrows that result by preserving \emph{i} before \emph{*ng} in words of the *sċilling* ‘shilling’ type.

That close interaction is why the two rules still belong in one small chapter. The history is not simply adjacency in the cascade. The second rule directly repairs the overbroad outcome that the first would otherwise leave behind in the \emph{*ng} environment. Even so, the pair remains narrower and more witness-limited than [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

### SC074. First medial unstressed-\emph{i} lowering (`OEMedUnstressedILowering1`) {#rule-OEMedUnstressedILowering1}

The implementation gives the first lowering step its own rule.

```foma
define OEMedUnstressedILowering1 [
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];
```

In prose, the rule lowers medial unstressed \emph{*i} to \emph{*e} after a preceding vocalic syllable. This is the broader step that would spread the \emph{e}-outcome through the late weak tail if it were left uncorrected.

Its chronology is explicit on both sides. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*fúrxtīnaz} yields *fyrhti* rather than expected OE *fyrhte* ‘fright’. If it is delayed until after [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering), PGmc \emph{*skíllingaz} yields *sċilleng* rather than expected *sċilling* ‘shilling’. This shows that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1), and that [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) must come before [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

The evidence is narrow on each side, but it is still real. The rule belongs between the stronger shortening/merger chapter and the more specific \emph{*ng} preservation that follows it.

### SC075. Preservation of medial unstressed \emph{*i} before \emph{*ng} (`OEMedUnstressedILowering`) {#rule-OEMedUnstressedILowering}

The following rule gives the local \emph{*ng} restriction its own explicit step.

```foma
define OEMedUnstressedILowering [
    {*e} -> {*i} || _ {*n} {*g}
];
```

In prose, the rule restores \emph{*i} before \emph{*ng}, preventing the broader lowering from producing the wrong medial vowel in forms such as *sċilling* ‘shilling’.

Its earlier boundary is the reciprocal side of the [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) relation. If the rule is moved before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1), PGmc \emph{*skíllingaz} yields *sċilleng* rather than expected OE *sċilling*. No equally sharp later breakpoint appears within the tested range, so the available evidence shows only that [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) must come before [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

That one-sided profile is enough for a follower rule of this kind. It is historically useful because it keeps the \emph{*ng} forms from being swallowed by the broader lowering, but it does not need to carry more chronology than the evidence supplies.

\newpage

## Prefix i-reduction

### Historical discussion

Late weak-tail reduction does not affect only inflectional endings and medial vowels. Unstressed prefixes also weaken, and that smaller development deserves a visible place in the sequence even though its chronology is much less sharply fixed. Fulk is the clearest source here, since his discussion of vowels in prefixes makes forms like OE \emph{*be-} and \emph{*ne-} historically legible outcomes in their own right [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and Taylor supply the broader late environment in which such weakening belongs, even though they do not isolate this rule as a major center of the late-tail history [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--332, §§6.8.3--6.9.6].

That is enough for a short note, but not for a major chronology anchor. Prefix reduction belongs in the late weak tail, yet the tested forms do not by themselves determine a closer position for this specific rule.

### SC076. Reduction of prefixal \emph{*i} in unstressed position (`OEPrefixIReduction`) {#rule-OEPrefixIReduction}

The implementation keeps the prefixal reduction as one rule.

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

In prose, the rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the \emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following vowel. This is the development that helps make later prefix spellings such as OE \emph{*be-} and \emph{*ne-} historically intelligible.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) before or after any specific neighboring change.

That modest result is still useful. The handbooks give real support for late prefix-vowel weakening, and CAPR places the rule in this late weak-tail stretch on those historical grounds. The placement should be read as approximate and source-based, not as a local ordering forced by the tested forms.

\newpage

## Weak-tail reduction

### Historical discussion

The last rule in the present late weak-tail cluster is stronger than the small prefix note that precedes it. Campbell, Hogg, Ringe and Taylor, and Fulk all support a late region in which apocope, shortening, contraction, and further weak-tail reductions continue to reshape final syllables [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3; @Fulk2018, pp. 90--91, §5.6]. What makes the present rule stand out is that the finite-state chronology gives it a real boundary on both sides.

That does not make it a license to absorb later material. The later relation to [SC086 OEContraction](#rule-OEContraction) is meaningful, but it remains a cross-reference to the next cluster, not a reason to pull that cluster into the present chapter.

### SC078. Reduction of remaining weak-tail vowels (`OEWeakTailReduction`) {#rule-OEWeakTailReduction}

The implementation keeps the last weak-tail reduction as one explicit step.

```foma
define OEWeakTailReduction OEWeakTailReduction1;
```

In prose, the rule carries the remaining weak-tail reductions that prevent a broad class of spurious \emph{-en} or extra-vowel outcomes from surviving too late in the derivation.

Its chronology is real on both sides, though the two sides are not equally local. If the rule is moved before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside a much wider set of comparable \emph{-en} failures. If the rule is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon* ‘flee’, and PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan* ‘slay’. This shows that [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) must come before [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction), and that [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) must come before [SC086 OEContraction](#rule-OEContraction).

The asymmetry of those two boundaries is important. The earlier side covers a very wide interval and should be read as a broad diagnostic range, not as a close neighboring constraint. The later side is narrower and more directly interpretable. Together they make [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) substantial enough for its own chapter, but still not a reason to merge the next cluster into the present section.

\newpage

## Final-j loss and final geminate simplification

### Historical discussion of final-j loss and final geminate simplification

The first closing pair belongs to the late verbal and weak-tail region that follows [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction), but it is not yet the strongest center of the closing cluster. Its coherence comes from a genuine derivational interaction. Once [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) removes \emph{*j} after the relevant heavy environments, forms such as *lungen* ‘lungs’ can end up with an unwanted final geminate that [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) immediately removes. That interaction is close enough to justify one shared historical discussion.

The hierarchy inside the pair is still uneven. The heavier historical load lies on [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy), whose broad earlier relation reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut), while [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) is the narrower follower that resolves the final \emph{nn} outcome in one sharply diagnostic derivation. The chapter therefore remains compact and explicit.

### SC079. Loss of \emph{*j} after heavy syllables (`OEJLossAfterHeavy`) {#rule-OEJLossAfterHeavy}

The implementation gives the \emph{*j}-loss step its own rule.

```foma
define OEJLossAfterHeavy [
    {*j} -> 0 || (EnglishStarLongVowel | EnglishStarDiphthong) [EnglishStarConsonantNoR | EnglishPalatalConsonant] _,
    {*j} -> 0 || EnglishStarShortVowel [EnglishStarConsonant | EnglishPalatalConsonant] [EnglishStarConsonantNoR | EnglishPalatalConsonant] _
];
```

In prose, the rule removes \emph{*j} after the relevant heavy-syllable configurations. This is the step that lets a broad set of late verbal forms move beyond earlier umlaut-sensitive vocalism.

Its chronology is explicit on both sides. If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*galáubijaną} yields *ġelēafan* rather than expected OE *ġelīefan* ‘believe’, PGmc \emph{*báugijaną} yields *bēaġan* rather than expected *bīeġan* ‘bow’, and PGmc \emph{*fúlgijaną} yields *fulġan* rather than expected *fylġan* ‘follow’. If it is delayed until after [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification), PGmc \emph{*lúnganjō} yields *lungenn* rather than expected OE *lungen* ‘lungs’. This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy), and that [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) must come before [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

The left side is broad, but the right side is sharply local. Together they explain why [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) is the stronger member of the pair.

### SC080. Simplification of final geminates (`OEFinalGeminateSimplification`) {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

In prose, the rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Its earlier boundary is the reciprocal side of the [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) relation. If the rule is moved before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy), PGmc \emph{*lúnganjō} yields *lungenn* rather than expected OE *lungen*. No later real break appears within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis), so the available evidence shows only that [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) must come before [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

That is enough for a follower rule of this kind. It is historically useful because it prevents the unwanted final geminate from surviving, but it does not need to carry more chronology than the evidence supplies.

\newpage

## J-strengthening, vocalization, and ei-contraction

### Historical discussion of j-strengthening, vocalization, and ei-contraction

The middle closing sequence is technically tighter than the opening pair, but it is also more internally uneven. Its real center is [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) prepares the consonantal stage that the later vocalization must not erase too early, and [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) then removes the extra \emph{ei}-like sequence that would otherwise survive too long in the resulting weak verbal endings.

That hierarchy is historically meaningful. The three rules form one local chain because the output of each immediately conditions the next, but the chain is not flat. [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is the strongest member because it has the clearest local evidence on both sides, while [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) is the broad earlier flank and [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) is the one-sided follower on the right.

### SC081. Strengthening of \emph{*j} after front diphthongs (`OEJStrengtheningAfterFrontDiphthong`) {#rule-OEJStrengtheningAfterFrontDiphthong}

The implementation keeps the strengthening step as one explicit rule.

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

In prose, the rule keeps \emph{*j} as a strengthened consonantal outcome after the relevant front diphthongs and so prevents too-early vocalization.

Its chronology is explicit on both sides. If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*stráwjaną} yields *strēaġan* rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields *strīeian* rather than *strīeġan*. This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong), and that [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) must come before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and therefore defines a wide interval, not a close neighboring pair. The later relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is the real local seam in the *strīeġan* derivation, which is why CAPR keeps [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) here as the flank on the left side of the chain.

### SC082. Intervocalic vocalization of \emph{*j} (`OEIntervocalicJVocalization`) {#rule-OEIntervocalicJVocalization}

The implementation then turns the consonantal \emph{*j} into a vocalic outcome between vowels.

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} || EnglishStarVocalic _ EnglishStarVocalic
];
```

In prose, the rule vocalizes intervocalic \emph{*j} to \emph{*i}. This is the step that creates the extra \emph{ei}-like sequence later removed by [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) in many weak verb forms.

Its chronology is concrete on both sides. If the rule is moved before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong), PGmc \emph{*stráwjaną} yields *strīeian* rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction), PGmc \emph{*búrōjaną} yields *boreian* rather than expected OE *borian* ‘bore’, PGmc \emph{*xándlōjaną} yields *handleian* rather than expected *handlian* ‘handle’, and PGmc \emph{*mákōjaną} yields *maceian* rather than expected *macian* ‘make’. This shows that [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) must come before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), and that [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) must come before [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

That two-sided local seam is why [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is the center of the three-rule chain.

### SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

In prose, the rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Its earlier boundary is the reciprocal side of the [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) relation. If the rule is moved before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), PGmc \emph{*búrōjaną} yields *boreian* rather than expected OE *borian*, PGmc \emph{*líznōjaną} yields *liorneian* rather than expected *liornian*, and PGmc \emph{*líkkōjaną} yields *licceian* rather than expected *liccian*. No later real break appears within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis), so the available evidence shows only that [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) must come before [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

That one-sided profile is appropriate to the right follower in this chain. The rule is historically real, but it does not need to carry a stronger later boundary than the evidence provides.

\newpage

## H-loss and contraction

### Historical discussion of h-loss and contraction

This adjacent pair is the clearest compact core in the closing cluster. The interaction is direct. Once [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, the derivation is left with hiatus that [SC086 OEContraction](#rule-OEContraction) immediately resolves. That derivational dependence is exactly the kind of close interaction that justifies one shared historical discussion.

The pair is also stronger and more book-legible than the more technical three-rule chain to its left. Ringe and Taylor give the clearest modern account of the late sequence of \emph{h}-loss and contraction [@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk's discussion of contracted verbs places the same outcomes into a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick's treatment of West Germanic contractions gives older grammatical support for the same family of outcomes [@Luick1914, p. 165].

### SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

The implementation keeps the consonant loss as one explicit rule.

```foma
define OEHLoss [
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarVocalic
];
```

In prose, the rule removes intervocalic \emph{*h}, creating the hiatus that later contraction must resolve.

Its chronology is explicit on both sides. If the rule is moved before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. If it is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon* ‘flee’, PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan* ‘slay’, PGmc \emph{*téxun} yields *teoon* rather than expected *tēon* ‘draw’, and PGmc \emph{*táixōn} yields *tāe* rather than expected *tā*. This shows that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss), and that [SC085 OEHLoss](#rule-OEHLoss) must come before [SC086 OEContraction](#rule-OEContraction).

The earlier side is narrow, but the later side is a tight four-row reciprocal seam that clearly feeds the following contraction rule.

### SC086. Contraction of the resulting hiatus (`OEContraction`) {#rule-OEContraction}

The following rule contracts the hiatus left by [SC085 OEHLoss](#rule-OEHLoss).

```foma
define OEContraction [
    {*a} {*a} -> {*ā},
    {*e} {*e} -> {*ē},
    {*i} {*i} -> {*ī},
    {*o} {*o} -> {*ō},
    {*u} {*u} -> {*ū},
    {*ea} {*a} -> {*ēa},
    {*ēa} {*a} -> {*ēa},
    {*eo} {*a} -> {*ēo},
    {*ēo} {*a} -> {*ēo},
    {*eo} {*o} -> {*ēo},
    {*ēo} {*o} -> {*ēo},
    {*éo} {*o} -> {*ḗo},
    {*ḗo} {*o} -> {*ḗo},
    {*ā} {*a} -> {*ā},
    {*ā} {*e} -> {*ā},
    {*ē} {*a} -> {*ē},
    {*ē} {*e} -> {*ē},
    {*ḗ} {*a} -> {*ḗ},
    {*ḗ} {*e} -> {*ḗ},
    {*ī} {*a} -> {*ī},
    {*ī} {*e} -> {*ī},
    {*ḯ} {*a} -> {*ḯ},
    {*ḯ} {*e} -> {*ḯ},
    {*ō} {*a} -> {*ō},
    {*ō} {*e} -> {*ō},
    {*ū} {*a} -> {*ū},
    {*ū} {*e} -> {*ū}
];
```

In prose, the rule contracts the vowel sequences created after \emph{h}-loss. This is the step that turns over-long transitional forms into outcomes such as *flēon* ‘flee’, *slēan* ‘slay’, and *tēon* ‘draw’.

Its earlier boundary is the reciprocal side of the [SC085 OEHLoss](#rule-OEHLoss) relation. If the rule is moved before [SC085 OEHLoss](#rule-OEHLoss), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon*, PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan*, PGmc \emph{*téxun} yields *teoon* rather than expected *tēon*, and PGmc \emph{*táixōn} yields *tāe* rather than expected *tā*. No later real break appears within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis), so the available evidence shows only that [SC085 OEHLoss](#rule-OEHLoss) must come before [SC086 OEContraction](#rule-OEContraction).

That one-sided profile is still substantial because the earlier reciprocal seam is so clear. The already visible [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) relation also points here, but it remains a cross-reference, not a reason to absorb [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) into the same chapter.

\newpage

## R-metathesis

### Historical discussion

R-metathesis closes the present sequence, but it does not behave like the second half of a tidy local pair. The historical process is real enough to deserve explicit prose, yet its chronology reaches much farther back on the left than it does on the right. Sievers-Brunner gives a clear page-safe grammatical statement of the phenomenon through forms such as *berstan* ‘burst’, *forst* ‘frost’, and *cærse* ‘cress’ [@SieversBrunner1965, p. 159, §179]. Luick likewise treats metathesis as a later rearrangement whose interaction with breaking remains variable and not tightly local [@Luick1914, p. 201].

That is why the chapter stays short. The note belongs after the contraction chapter in the assembled order, but the evidence does not justify inventing a positive claim that [SC086 OEContraction](#rule-OEContraction) must come before [SC087 OERMetathesis](#rule-OERMetathesis) simply because the two are adjacent.

### SC087. Metathesis of \emph{*r} with a following short vowel (`OERMetathesis`) {#rule-OERMetathesis}

The implementation states the metathesis directly.

```foma
define OERMetathesis [
    {*r} {*e} -> {*e} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*u} -> {*u} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*i} -> {*i} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*o} -> {*o} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*a} -> {*a} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*é} -> {*é} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*ó} -> {*ó} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*á} -> {*á} {*r} || EnglishStarConsonant _ {*s} {*t}
];
```

In prose, the rule moves \emph{*r} across a following short vowel in the relevant late clusters, producing forms such as *berstan* ‘burst’ where an earlier order would still show a broken vowel sequence.

Its chronology is one-sided. If the rule is moved before [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*bréstaną} yields *beorstan* rather than expected OE *berstan* ‘burst’. That shows that [SC044 OEBreaking](#rule-OEBreaking) must come before [SC087 OERMetathesis](#rule-OERMetathesis). If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one.

That profile is exactly why the chapter remains modest. The checked forms fix the earlier relation but do not identify a corresponding later constraint. CAPR keeps the rule here because the sources treat r-metathesis as a late rearrangement that follows the earlier breaking and contraction history without being fixed immediately beside either one.

\newpage

\part{Lexical derivations}

# Word-by-word derivations

## Introduction

The lexical catalogue is organized by derivation class rather than as a single
undifferentiated list. This makes the interpretive burden of each entry
explicit. Regular derivations establish the baseline relation between earlier
Germanic forms and Old English reflexes under the sound history followed here. The variant,
analogy, reconstructed-comparator, and exception classes then show where that
baseline does not by itself explain the attested form.

This lexical catalogue is a word-centered volume. It traces individual earlier
Germanic forms to Old English reflexes and groups them by the kind of
comparison each entry requires. A separate sound-change study would remain
rule-centered, treating chronology, rule interaction, and broader exception
patterns.

## Data and sources

This volume assembles the lexical corpus from the aligned Germanic dataset and the compact derivation traces that accompany each entry. Comparative dictionaries, Old English dictionaries, and historical grammars are cited in the prose where they bear on particular lexical arguments.

The result is a lexical catalogue rather than a separate report on citation method or trace machinery.

## Transducer and derivation method

Each lexical entry keeps the pilot structure: a generated derivation summary, a boxed derivation trace split into Earlier Germanic changes and Old English changes, and the current entry prose. The summary distinguishes citation reconstruction, selected input, transducer outcome, and selected target where those differ, and the boxed trace remains a compact PDF-oriented rendering of the current compact trace data.

## Derivation classes

The lexical catalogue is ordered by seven derivation classes in the current manifest. Counts in this alpha are:

- Regular derivations: **70**
- Attested variants: **4**
- Early analogy: **35**
- Late analogy: **28**
- Reconstructed Old English comparators: **3**
- Known but unmodelled remodellings: **2**
- Unexplained or deliberately unmodelled exceptions: **5**

\clearpage

## Regular derivations

Regular derivations are entries where the earlier Germanic form and the Old
English reflex stand in a straightforward relation under the sound history followed here.
These entries form the baseline against which the analogy and exception classes
are interpreted.

### adder — OE nǣdre

\index[oe]{naedre@nǣdre}
\index[pgmc]{nedron@*nḗdrōn}

Derivation: _\*nḗdrōn_ > _nǣdre_ (regular).

#### Derivation trace

Proto input: _\*nḗdrōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*nḗdrǭ} \\
\mbox{NWGmc Long E Lowering} & \emph{*nǣdrǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*nǣdræ} \\
OE Unstressed AE Merger & \emph{*nǣdre} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nǣdre_

#### Reconstruction and comparative evidence

Kroonen distinguishes the masculine snake word [_\*nadra-_]{.iv lang=pgmc sort=nadra role=source_protoform} from a feminine
ablauting formation [_\*nēdrōn-_]{.iv lang=pgmc sort=nedron role=source_protoform}, and gives Old English [_nǣdre_]{.iv lang=oe sort=naedre}, [_næddre_]{.iv lang=oe sort=naeddre} under the
latter [@Kroonen2013, 426]. Orel likewise points from the masculine entry to a
feminine [_\*nēdrōn_]{.iv lang=pgmc sort=nedron role=source_protoform} ~ [_\*nadrōn_]{.iv lang=pgmc sort=nadron role=source_protoform} type [@Orel2003, 325].

The derivational input therefore is not a reshaped convenience form. It is the
comparative reconstruction that specifically underlies the Old English noun.

#### Old English evidence

The Old English word is securely represented by [_nǣdre_]{.iv lang=oe sort=naedre}, with [_næddre_]{.iv lang=oe sort=naeddre} as a
secondary variant. Clark Hall cross-references [_næddre_]{.iv lang=oe sort=naeddre} to [_nædre_]{.iv lang=oe sort=naedre}, and Fulk
treats [_næddre_]{.iv lang=oe sort=naeddre} as the later geminated form beside the older base [@ClarkHall1960,
225; @Fulk2018, 149].

#### Development to Old English

From [_\*nḗdrōn_]{.iv lang=pgmc sort=nedron role=selected_input}, the stressed long mid vowel develops to Old English [_nǣdre_]{.iv lang=oe sort=naedre}, and
the weak feminine ending remains as final _-e_, giving [_nǣdre_]{.iv lang=oe sort=naedre}. The doubled
consonant of [_næddre_]{.iv lang=oe sort=naeddre} is secondary and does not alter the inherited base form.

### bake — OE bacan

\index[oe]{bacan@bacan}
\index[pgmc]{bakana@*bákaną}
\index[ohg]{backan@backan}
\index[ohg]{bahhan@bahhan}

Derivation: _\*bákaną_ > _bacan_ (regular).

#### Derivation trace

Proto input: _\*bákaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*bækaną} \\
OE A Restoration & \emph{*bakaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*bakan} \\
OE Secondary Nasalization & \emph{*bakąn} \\
OE Weak Tail Reduction & \emph{*bakan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bacan_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as [_\*bakanan_]{.iv lang=pgmc sort=bakanan} and cites Old English [_bacan_]{.iv lang=oe sort=bacan} beside Old High German _backan, bahhan_ [@Orel2003]. Campbell gives [_bacan_]{.iv lang=oe sort=bacan} as one of the standard examples of Old English A-restoration before a single consonant, and Ringe and Taylor state the same development from [_\*bakan_]{.iv lang=preoe sort=bakan} to Old English [_bacan_]{.iv lang=oe sort=bacan} [@Campbell1959, 61; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall both record [_bacan_]{.iv lang=oe sort=bacan} as the ordinary Old English verb 'to bake' [@BosworthToller1898, 72; @ClarkHall1960]. The target in this entry is therefore the attested infinitive headword itself, not a selected oblique or finite paradigm cell.

#### Development to Old English

From [_\*bákaną_]{.iv lang=pgmc sort=bakana}, Anglo-Frisian brightening first gives _\*bækaną_. A-restoration then returns the stem vowel to _a_ before single _k_ plus the back-vocalic infinitive suffix, and later apocope and weak-tail reduction yield [_bacan_]{.iv lang=oe sort=bacan} [@Campbell1959, 61; @RingeTaylor2014]. The development is therefore straightforward: [_\*bákaną_]{.iv lang=pgmc sort=bakana} > [_bacan_]{.iv lang=oe sort=bacan}.

### beech — OE bōc

\index[oe]{boc@bōc}
\index[pgmc]{boko@*bōkō}

Derivation: _\*bōkō_ > _bōc_ (regular).

#### Derivation trace

Proto input: _\*bōkō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*bōku} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*bōk} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bōc_

#### Reconstruction and comparative evidence

Kroonen gives the beech noun as _\*bōk(j)ō-_ and cites Old English _boc_, [_bēce_]{.iv lang=oe sort=bece} among its reflexes [@Kroonen2013]. The form followed here, _\*bōkō_, is the nominative-singular shape of that family, which is the relevant comparison form here.

#### Old English evidence

Kroonen's Old English evidence already separates the paradigm material: _boc_ as the nominative form and [_bēce_]{.iv lang=oe sort=bece} as an oblique form [@Kroonen2013]. The relevant comparator is therefore _bōc_; [_bēċe_]{.iv lang=oe sort=bece} remains related paradigm evidence rather than the form chosen for this comparison.

#### Development to Old English

With nominative input _\*bōkō_, the development is compact. Northwest Germanic final long _ō_ raises to _u_, and later high-vowel apocope leaves _bōc_. The regular comparison is therefore _\*bōkō_ > _bōc_.

### begin — OE beġinnan

\index[oe]{beginnan@beġinnan}
\index[pgmc]{biginnana@*bigínnaną}

Derivation: _\*bigínnaną_ > _beġinnan_ (regular).

#### Derivation trace

Proto input: _\*bigínnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*bigínnan} \\
OE Secondary Nasalization & \emph{*bigínnąn} \\
OE Velar Palatalization & \emph{*biʤínnąn} \\
OE Prefix I Reduction & \emph{*bĕʤínnąn} \\
OE Weak Tail Reduction & \emph{*bĕʤínnan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _beġinnan_

#### Reconstruction and comparative evidence

The verb is modeled here as inherited [_\*bigínnaną_]{.iv lang=pgmc sort=biginnana}. Ringe and Taylor state that intervocalic _\*g_ is palatalized between front vowels in Old English [@RingeTaylor2014], and Campbell lists [_ginnan_]{.iv lang=oe sort=ginnan} among familiar examples of palatal _g_ in this verb family [@Campbell1959, 174].

#### Old English evidence

Bosworth-Toller and Clark Hall lemmatize the verb as [_be-ginnan_]{.iv lang=oe sort=beginnan} / [_beginnan_]{.iv lang=oe sort=beginnan} [@BosworthToller1898, 84; @ClarkHall1960]. Those plain-_g_ dictionary spellings support the same verb that appears here in normalized form as [_beġinnan_]{.iv lang=oe sort=beginnan}.

#### Development note

The prefix deserves separate notice. Ringe and Taylor explicitly cite _bi- > be-_ as an Old English unstressed-prefix development [@RingeTaylor2014].

#### Development to Old English

From [_\*bigínnaną_]{.iv lang=pgmc sort=biginnana}, heavy-syllable nasal apocope yields _\*bigínnan_. Intervocalic _\*g_ between front vowels then palatalizes to _ġ_, and the unstressed prefix reduces _bi-_ to _be-_, giving [_beġinnan_]{.iv lang=oe sort=beginnan}.

### bier — OE bǣr

\index[oe]{baer@bǣr}
\index[pgmc]{bero@*bḗrō}

Derivation: _\*bḗrō_ > _bǣr_ (regular).

#### Derivation trace

Proto input: _\*bḗrō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*bḗru} \\
\mbox{NWGmc Long E Lowering} & \emph{*bǣru} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*bǣr} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bǣr_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as [_\*bērō-_]{.iv lang=pgmc sort=bero} f. 'bier' and cites Old English [_bar_]{.iv lang=oe sort=bar}, [_bær_]{.iv lang=oe sort=baer} among the reflexes [@Kroonen2013, 717]. The derivational input [_\*bḗrō_]{.iv lang=pgmc sort=bero} is the same lexeme in the accent notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller lemmatize the noun as [_bær_]{.iv lang=oe sort=baer}, and Kroonen also records [_bar_]{.iv lang=oe sort=bar} beside it [@ClarkHall1960; @BosworthToller1898, 73; @Kroonen2013, 717]. The target [_bǣr_]{.iv lang=oe sort=baer} is therefore a normalized long-vowel spelling of the same noun.

#### Source note

Lexicographic spellings vary between [_bær_]{.iv lang=oe sort=baer} and [_bar_]{.iv lang=oe sort=bar}. The normalized target [_bǣr_]{.iv lang=oe sort=baer} simply marks the same long vowel explicitly [@ClarkHall1960; @BosworthToller1898, 73; @Kroonen2013, 717].

#### Development to Old English

From [_\*bḗrō_]{.iv lang=pgmc sort=bero}, Northwest Germanic final long _ō_ raises to _u_, long _ē_ lowers to _ǣ_, and high-vowel apocope yields [_bǣr_]{.iv lang=oe sort=baer}. The resulting noun matches the normalized Old English target.

### birth — OE byrd

\index[oe]{byrd@byrd}
\index[pgmc]{burdiz@*búrdiz}

Derivation: _\*búrdiz_ > _byrd_ (regular).

#### Derivation trace

Proto input: _\*búrdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*búrdi} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*byrdi} \\
\mbox{OE High Vowel Apocope} & \emph{*byrd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _byrd_

#### Reconstruction and comparative evidence

Kroonen cites the noun under stem-level _\*burdi-_ and gives Old English _(ge-)byrd_ among the reflexes [@Kroonen2013]. The form followed here, _\*búrdiz_, is the nominative-style form that stands behind that stem label.

#### Old English evidence

Clark Hall and Bosworth-Toller both attest simplex _byrd_ as an Old English noun meaning 'birth' [@ClarkHall1960; @BosworthToller1898, 125]. The prefixed form _gebyrd_ is also well established in the tradition: Kroonen lists _(ge-)byrd_, Bosworth-Toller has a separate _ge-byrd_ entry, and Campbell cites _gebyrd_ and _gebyrdu_ in his grammatical discussion [@Kroonen2013; @BosworthToller1898, 125; @Campbell1959].

#### Form note

The relevant comparator here is the simplex noun _byrd_. The prefixed forms remain related attested material within the same lexical family, and Hogg's discussion of deverbal feminines provides the broader derivational setting [@Hogg1992].

#### Development to Old English

From _\*búrdiz_, loss of final _z_ gives _\*búrdi_. I-umlaut fronts _u_ to _y_, and high-vowel apocope then yields _byrd_. The result is the ordinary simplex Old English noun.

### bone — OE bān

\index[oe]{ban@bān}
\index[pgmc]{baina@*báiną}

Derivation: _\*báiną_ > _bān_ (regular).

#### Derivation trace

Proto input: _\*báiną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*bāną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*bān} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bān_

#### Reconstruction and comparative evidence

Kroonen cites the noun as [_\*baina-_]{.iv lang=pgmc sort=baina}, and Orel gives the same lexeme under [_\*bainan_]{.iv lang=pgmc sort=bainan} [@Kroonen2013; @Orel2003]. Both are comparative headword conventions for the same neuter noun whose Old English reflex is [_bān_]{.iv lang=oe sort=ban}.

#### Old English evidence

Clark Hall and Bosworth-Toller record [_bān_]{.iv lang=oe sort=ban} as the ordinary Old English noun [@ClarkHall1960; @BosworthToller1898]. Bright's glossary also distinguishes citation-form [_bān_]{.iv lang=oe sort=ban} from oblique [_bāne_]{.iv lang=oe sort=bane}, which keeps the nominative-accusative singular separate from the rest of the paradigm [@BrightCassidyRingler1971].

#### Source note

The comparative headwords [_\*baina-_]{.iv lang=pgmc sort=baina} and [_\*bainan_]{.iv lang=pgmc sort=bainan} provide lexeme background. The relevant comparison form here is the nominative-accusative singular [_\*báiną_]{.iv lang=pgmc sort=baina}.

#### Development to Old English

West Germanic monophthongization turns stressed _\*ai_ into _ā_, giving _\*bāną_; heavy-syllable nasal apocope then yields [_bān_]{.iv lang=oe sort=ban}. The resulting form matches the attested Old English citation noun.

### both — OE bū

\index[oe]{bu@bū}
\index[pgmc]{bo@*bō}

Derivation: _\*bō_ > _bū_ (regular).

#### Derivation trace

Proto input: _\*bō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc Stressed Monosyllable O Raising & \emph{*bū} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bū_

#### Reconstruction and comparative evidence

Kroonen treats the Germanic numeral under _\*ba-_ and gives the inherited
paradigm _\*bai_, _\*bans_, _\*bōz_/_\*bōns_, _\*bō_, with Old English [_bēġen_]{.iv lang=oe sort=begen role=comparison_form}, [_bā_]{.iv lang=oe sort=ba role=comparison_form}, and
neuter [_bū_]{.iv lang=oe sort=bu role=target_form} [@Kroonen2013, 47]. For the present entry, the relevant inherited
form is the unextended neuter dual [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input}.

The older explanation of [_bēġen_]{.iv lang=oe sort=begen role=comparison_form} derives it from _\*bō-jen-_, and Orel still
gives OE _bezen_ (< _\*bō-jenō)_ beside _ON_ [_báðir_]{.iv lang=on sort=badir role=comparison_form}, _OFris_ [_bēthe_]{.iv lang=ofris sort=bethe role=comparison_form}, _OS_ [_be-thia_]{.iv lang=os sort=bethia role=comparison_form},
and _OHG_ [_bēde_]{.iv lang=ohg sort=bede role=comparison_form} [@Orel2003, 65]. Fulk reports that explanation
cautiously and notes Seebold's preference for a _\*bō-þ-_ analysis instead
[@Fulk2018, §10.1]. That debate matters for [_bēġen_]{.iv lang=oe sort=begen role=comparison_form} and for the extended forms
behind Modern English [_both_]{.iv lang=modeng sort=both role=comparison_form}, German [_beide_]{.iv lang=german sort=beide role=comparison_form}, and Dutch [_beide_]{.iv lang=dutch sort=beide role=comparison_form}; it does not
displace the inherited neuter [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input} > [_bū_]{.iv lang=oe sort=bu role=target_form} treated here.

#### Old English evidence

The Old English dual paradigm is well established. Brunner gives masculine
[_bēġen_]{.iv lang=oe sort=begen role=comparison_form}, feminine [_bā_]{.iv lang=oe sort=ba role=comparison_form}, and neuter [_bū_]{.iv lang=oe sort=bu role=target_form} beside _bā_, with compounds such as
_bā_ _twā_, _bū_ _tū_, and _bām_ _twām_ [@SieversBrunner1965, §324 Anm. 2].
Campbell and Fulk present the same basic pattern: masculine [_bēġen_]{.iv lang=oe sort=begen role=comparison_form}, feminine
_bā_, neuter _bā_, _bū_, genitive _bēġra_, _bēġ(e)a_, and dative [_bǣm_]{.iv lang=oe sort=baem role=comparison_form}
[@Campbell1959, §683; @Fulk2018, §10.1].

[_bū_]{.iv lang=oe sort=bu role=target_form} is therefore an attested neuter dual form, not a reconstruction. It is the
cleanest target for this entry because [_bēġen_]{.iv lang=oe sort=begen role=comparison_form} belongs to the historically more
contested _\*bō-jen-_ / analogical zone, while _bā_ remains a partner form
within the dual paradigm rather than the most straightforward monosyllabic
comparison.

#### Development to Old English

[_\*bō_]{.iv lang=pgmc sort=bo role=selected_input} is a stressed monosyllabic form. Campbell cites _cū_, _hū_, _tū_, and
[_bū_]{.iv lang=oe sort=bu role=target_form} as examples of final accented _ō_ > _ū_ in the West Germanic stage leading
to Old English [@Campbell1959, §122]. Brunner states the same development more
directly: Auslautendes _ō_ erscheint als û in _bū_ ... cu ... _hū_, _tū_
[@SieversBrunner1965, §69].

The development is therefore straightforward: [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input} > [_bū_]{.iv lang=oe sort=bu role=target_form}.

#### Form comparison

The comparison below sets the relevant forms side by side. It separates the inherited OE target from the
other forms that belong to the same broader lexical history.

| Form | Source / stage | Status | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input} > [_bū_]{.iv lang=oe sort=bu role=target_form} | PGmc neuter dual > OE neuter dual | selected regular comparison | main line of the entry |
| [_bēġen_]{.iv lang=oe sort=begen role=comparison_form} | OE masculine dual | attested, but historically contested and at least partly analogical in Kroonen | real OE evidence, not the Old English form here |
| [_bā_]{.iv lang=oe sort=ba role=comparison_form} | OE feminine dual; also neuter variant | attested partner form | part of the OE paradigm, but not the chosen monosyllabic comparator |
| [_báðir_]{.iv lang=on sort=badir role=comparison_form}, German [_beide_]{.iv lang=german sort=beide role=comparison_form}, Dutch [_beide_]{.iv lang=dutch sort=beide role=comparison_form}, Modern English [_both_]{.iv lang=modeng sort=both role=comparison_form} | Norse, continental West Germanic, Modern English extended forms | related but different formation | useful background, not the direct continuation of OE _bū_ |

### bow — OE bīeġan

\index[oe]{biegan@bīeġan}
\index[pgmc]{baugijana@*báugijaną}

Derivation: _\*báugijaną_ > _bīeġan_ (regular).

#### Derivation trace

Proto input: _\*báugijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*báeugijaną} \\
OE Diphthong Leveling & \emph{*bēagijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*bēagijan} \\
OE Secondary Nasalization & \emph{*bēagijąn} \\
Sievers Law Syncope & \emph{*bēagjąn} \\
OE Velar Palatalization & \emph{*bēaʤjąn} \\
OE I Umlaut & \emph{*bīeʤjąn} \\
OE Weak Tail Reduction & \emph{*bīeʤjan} \\
OE J Loss After Heavy & \emph{*bīeʤan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bīeġan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the weak verb as _\*baugjan-_ 'to (make) bend' and cites Old English _biegan_ among its reflexes [@Kroonen2013]. Ringe and Taylor give the northwest Germanic preform _\*baugijana_, with later _\*béagjan_ behind West Saxon Old English _biegan_ [@RingeTaylor2014]. The entry therefore concerns the weak causative member of the bend-family, alongside the related strong verb and noun.

#### Old English evidence

Clark Hall lemmatizes _biegan_, and Bosworth-Toller records _bigan_ with examples such as Ic _bēge_ _mīne_ _cneówa_ and Se ord _bīgde_ upp _tō_ _þām_ hiltum [@ClarkHall1960; @BosworthToller1898, 102]. The form _bīeġan_ used here is a normalized spelling of that attested Old English weak verb.

#### Development to Old English

From _\*báugijaną_, the stem reaches pre-Old-English _\*bēagjan_, after which palatalization of _\*gj_ and i-umlaut yield West Saxon _biegan_; Campbell lists _biegan_ among the regular _ie_ outcomes of _\*éa_ under i-umlaut [@RingeTaylor2014; @Campbell1959, 80]. The development is therefore straightforward: _\*báugijaną_ > _bīeġan_.

### breeches — OE brēċ

\index[oe]{brec@brēċ}
\index[pgmc]{brokiz@*brōkiz}

Derivation: _\*brōkiz_ > _brēċ_ (regular).

#### Derivation trace

Proto input: _\*brōkiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*brōki} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Velar Palatalization & \emph{*brōʧi} \\
OE I Umlaut & \emph{*brēʧi} \\
\mbox{OE High Vowel Apocope} & \emph{*brēʧ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _brēċ_

#### Reconstruction and comparative evidence

Kroonen cites the noun under _\*brōk-_, with Old English _brōc_ and plural 'breeches' among its reflexes [@Kroonen2013]. Ringe and Taylor give the plural development directly as PNWGmc _\*brokiz_ > _\*breeci_ > OE _bréc_ [@RingeTaylor2014]. The deeper verbal base belongs to the noun's etymological background, while the derivational input here is the plural noun form _\*brōkiz_.

#### Old English evidence

Bright notes _brōc_ with plural _brēc_, and Clark Hall gives _brēc_ fp. breeches while also listing _broc_ as a feminine noun probably represented chiefly in the plural [@BrightCassidyRingler1971; @ClarkHall1960, 64]. The spelling _brēċ_ used here makes the long vowel and palatal consonant explicit; the Old English evidence itself is the attested plural _brēc_.

#### Development to Old English

After loss of final _-z_, the stem ends in _-ki_, so the velar palatalizes and _ō_ undergoes i-umlaut to _ē_; final high-vowel apocope then yields _brēċ_ [@RingeTaylor2014]. The development is therefore regular: _\*brōkiz_ > _brēċ_.

### calf — OE ċealf

\index[oe]{cealf@ċealf}
\index[pgmc]{kalbaz@*kálbaz}

Derivation: _\*kálbaz_ > _ċealf_ (regular).

#### Derivation trace

Proto input: _\*kálbaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*kálba} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*kálb} \\
Anglo Frisian Brightening & \emph{*kælb} \\
OE Breaking & \emph{*kealb} \\
PGmc B Allophony & \emph{*kealβ} \\
OE Velar Palatalization & \emph{*ʧealβ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ċealf_

#### Reconstruction and comparative evidence

Kroonen treats the noun under _\*kalbiz-_ and notes an older s-stem _\*kalbaz_, pl. _\*kalbizō_, while Orel cites _\*kalbaz_ as the citation form and Ringe and Taylor derive West Saxon _Cealf_ from _\*kalbaz_, _\*kalbiz-_ [@Kroonen2013; @Orel2003, 248; @RingeTaylor2014, 220]. The derivational input here is the singular _\*kálbaz_, since the entry concerns the citation-form noun.

#### Old English evidence

Clark Hall gives [_cealf_]{.iv lang=oe sort=cealf} I. (æ, e) nm. (nap. [_cealfru_]{.iv lang=oe sort=cealfru}), and Bosworth-Toller likewise records _Caelf_ / _Cealf_ beside plural forms such as _calfur_ and [_cealfru_]{.iv lang=oe sort=cealfru} [@ClarkHall1960; @BosworthToller1898, 131]. Campbell and Fulk show the same singular-plus-_-r-_ plural pattern [@Campbell1959; @Fulk2018, 193]. The spelling _ċealf_ used here makes the palatalized initial explicit; the ordinary attested dictionary headword is [_cealf_]{.iv lang=oe sort=cealf}.

#### Development to Old English

After loss of final _-z_ and bare _-a_, Anglo-Frisian brightening gives _\*kælb_, and breaking before _l_ plus consonant yields _\*kealb_. Ringe and Taylor's account of the lexeme and their rule for initial _k_ in front-vocalic environments support the West Saxon palatalized onset represented here as _ċ-_, so _\*kálbaz_ develops regularly to _ċealf_ [@RingeTaylor2014, 220].

### corn — OE corn

\index[oe]{corn@corn}
\index[pgmc]{kurna@*kúrną}

Derivation: _\*kúrną_ > _corn_ (regular).

#### Derivation trace

Proto input: _\*kúrną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*kórną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*kórn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _corn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*kurna-_, and Orel gives the citation form _\*kurnan_, both with Old English _corn_ among the reflexes [@Kroonen2013; @Orel2003, 264]. The singular form _\*kúrną_ is the nominative-accusative singular appropriate to the citation noun.

#### Old English evidence

Clark Hall gives _corn n. 'corn,' grain_, Bright's glossary lists _corn, n._ with genitive singular _cornes_, and Bosworth-Toller treats _corn_ as an ordinary noun headword [@ClarkHall1960; @BrightCassidyRingler1971, 347; @BosworthToller1898, 144]. The target is therefore an attested citation form, while forms such as _cornes_ simply provide paradigm background.

#### Development to Old English

With northwest Germanic lowering, _\*kúrną_ becomes _\*kórną_, and later loss of final nasal after a heavy syllable yields _\*kórn_, whence _corn_. The oblique form _\*kurnăn_ belongs to comparative background rather than to the derivational input of this entry.

### deed — OE dǣd

\index[oe]{daed@dǣd}
\index[pgmc]{dediz@*dḗdiz}

Derivation: _\*dḗdiz_ > _dǣd_ (regular).

#### Derivation trace

Proto input: _\*dḗdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*dḗdi} \\
\mbox{NWGmc Long E Lowering} & \emph{*dǣdi} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*dǣd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _dǣd_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*dēdiz_, and Ringe and Taylor derive the same inherited i-stem from Proto-Germanic _\*dédiz_ through northwest Germanic _\*dadiz_ [@Orel2003; @RingeTaylor2014]. The stress-marked form _\*dḗdiz_ represents that same inherited noun in a notation that keeps the stressed long vowel explicit.

#### Old English evidence

Campbell states that Primitive Germanic _ē_ appears as West Saxon _ǣ_ but in other Old English dialects mostly as _ē_, and Brunner gives the contrast explicitly as West Saxon _dǣd_ beside non-West-Saxon _dēd_ [@Campbell1959; @SieversBrunner1965]. Clark Hall likewise lists _dæd_ and cross-refers Anglian _dēd_ to it [@ClarkHall1960]. West Saxon _dǣd_ is therefore the relevant Old English form here, with Anglian _dēd_ as a dialectal doublet.

#### Development to Old English

From inherited _\*dēdiz_, loss of final _-z_ and the West Saxon lowering of stressed long _ē_ yield _dǣd_; Anglian _dēd_ preserves the non-West-Saxon outcome [@Campbell1959; @SieversBrunner1965]. The development treated here is therefore the regular West Saxon line.

### door — OE dor

\index[oe]{dor@dor}
\index[pgmc]{dura@*dúrą}
\index[ohg]{tura@tura}
\index[ofris]{dore@dore}

Derivation: _\*dúrą_ > _dor_ (regular).

#### Derivation trace

Proto input: _\*dúrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*dórą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*dór} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _dor_

#### Reconstruction and comparative evidence

Kroonen reconstructs a neuter _\*dura-_ 'gate, (single) door' and cites Old English _dor_ among its reflexes. In the same entry he separates Old English _duru_, Old Frisian _dore_, and Old High German _tura_ as reflexes of _\*durō-_ instead [@Kroonen2013].

#### Old English evidence

Clark Hall records _dor_ as a neuter noun and separately records feminine _duru_ with its own inflection [@ClarkHall1960]. Ringe and Taylor likewise treat _duru_ as an early Old English u-stem, originally a root noun shifted into that class [@RingeTaylor2014]. The Old English form here is therefore the attested neuter _dor_, while _duru_ remains a parallel Old English reflex from another stem history.

#### Development to Old English

From _\*dúrą_, Northwest Germanic u-lowering gives _\*dórą_, and heavy-syllable nasal apocope then yields _dor_. The regular development treated in this entry is therefore _\*dúrą_ > _dor_; the feminine _duru_ belongs to the separate line identified by Kroonen and Ringe-Taylor [@Kroonen2013; @RingeTaylor2014].

### fare — OE faran

\index[oe]{faran@faran}
\index[pgmc]{farana@*fáraną}

Derivation: _\*fáraną_ > _faran_ (regular).

#### Derivation trace

Proto input: _\*fáraną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*færaną} \\
OE A Restoration & \emph{*faraną} \\
OE Heavy Syllable Nasal Apocope & \emph{*faran} \\
OE Secondary Nasalization & \emph{*farąn} \\
OE Weak Tail Reduction & \emph{*faran} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _faran_

#### Reconstruction and comparative evidence

Kroonen gives the inherited strong verb as _\*faran-_, and Orel gives the same lexeme as _\*faranan_, both with Old English _faran_ among the reflexes [@Kroonen2013; @Orel2003, 132]. Campbell also uses _faran_ as a standard example of Old English A-restoration [@Campbell1959, 61].

#### Old English evidence

Clark Hall lemmatizes the strong verb as _faran_ and separately records weak _færan_ 'to frighten'; [_fære_]{.iv lang=oe sort=faere}, [_færst_]{.iv lang=oe sort=faerst}, and [_færð_]{.iv lang=oe sort=faerd} belong to present-tense forms of _faran_ rather than to the infinitive itself [@ClarkHall1960]. Bosworth-Toller preserves the same distinction [@BosworthToller1898, 108]. The Old English form here is therefore the attested citation infinitive _faran_.

#### Development to Old English

From _\*fáraną_, Anglo-Frisian brightening first gives _\*færaną_, but A-restoration before single _r_ returns _\*faraną_; later apocope and weak-tail reduction yield _faran_ [@Campbell1959, 61]. Fulk's contrast with participial faren- < _\*faræn-_ < _\*faran-_ shows why fronting elsewhere in the paradigm does not alter the infinitive headword [@Fulk2018].

### fell — OE fell

\index[oe]{fell@fell}
\index[pgmc]{fella@*féllą}

Derivation: _\*féllą_ > _fell_ (regular).

#### Derivation trace

Proto input: _\*féllą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*féll} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fell_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*fella-_ 'membrane, skin, hide' and cites Old English _fell_ beside Dutch _vel_ and German _Fell_ [@Kroonen2013]. The form followed here, _\*féllą_, is the derivable singular form of that same inherited noun.

#### Old English evidence

Clark Hall records _fell_ as the noun 'fell, skin, hide', and Bright's glossary likewise gives _fell_ with inflected forms such as accusative singular _fel_ and dative plural _fellum_ [@ClarkHall1960; @BrightCassidyRingler1971]. The target is therefore the attested noun _fell_, not the verb _fellan_ or the preterite _feoll_.

#### Development to Old English

With _\*féllą_, no special earlier reshaping is needed: heavy-syllable nasal apocope yields _\*féll_, surfacing as _fell_. The regular development treated here is therefore _\*féllą_ > _fell_.

### fern — OE fearn

\index[oe]{fearn@fearn}
\index[pgmc]{farnaz@*fárnaz}

Derivation: _\*fárnaz_ > _fearn_ (regular).

#### Derivation trace

Proto input: _\*fárnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*fárna} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*fárn} \\
Anglo Frisian Brightening & \emph{*færn} \\
OE Breaking & \emph{*fearn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fearn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as masculine _\*farna-_ and gives Old English _fearn, fern_, while Orel gives the same lexeme as neuter _\*farnan_ with Old English _fearn_ [@Kroonen2013; @Orel2003, 133]. Those are comparative headword conventions rather than competing Old English outcomes; the modeled input here is the nominative-style _\*fárnaz_.

#### Old English evidence

Clark Hall gives _fearn_ as an Old English noun, and Bosworth-Toller records _fearn_ with inflected forms such as _fearnes_, _fearna_, and _fearne_ [@ClarkHall1960; @BosworthToller1898, 219]. Kroonen's additional _fern_ remains useful comparative background, but the best-supported citation target in the local lexical sources is _fearn_ [@Kroonen2013].

#### Development to Old English

From _\*fárnaz_, loss of final _-z_ and final _-a_ gives _\*fárn_; Anglo-Frisian brightening then yields _\*færn_, and breaking before _r_ plus consonant gives _fearn_ [@Campbell1959; @RingeTaylor2014]. The development treated here is therefore the regular _rC_-breaking line.

### field — OE feld

\index[oe]{feld@feld}
\index[pgmc]{felthuz@*félθuz}

Derivation: _\*félθuz_ > _feld_ (regular).

#### Derivation trace

Proto input: _\*félθuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc L Th Voicing & \emph{*félduz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*féldu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*féld} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _feld_

#### Reconstruction and comparative evidence

Ringe and Taylor treat Old English _feld_ as one of the cases where earlier _\*felþu-_ ~ _\*feldu-_ may reflect either inherited _\*þ_ ~ _\*d_ alternation or the regular West Germanic development _\*lþ_ > _ld_ [@RingeTaylor2014, 170]. The broader proto label _\*félθuz_ can remain as comparative background, while that narrower historical ambiguity does not affect the regular classification.

#### Old English evidence

Clark Hall records _feld_ with oblique forms such as _felda_ and _felde_, and Campbell notes early place-name spellings in _-felth_ beside the later standard form [@ClarkHall1960, 114; @Campbell1959, 169]. The Old English form here is therefore the attested citation noun _feld_, with the older _-felth_ spellings as historical support rather than as rival targets.

#### Development to Old English

In the modeled pathway, medial _\*lþ_ becomes _ld_, final _-z_ is lost, and high-vowel apocope then yields _feld_. Whether the voiced dental ultimately reflects inherited alternation or the regular _\*lþ_ > _ld_ development, both accounts converge on the same Old English form [@RingeTaylor2014, 170].

### fly — OE flēogan

\index[oe]{fleogan@flēogan}
\index[pgmc]{fleugana@*fléuganą}

Derivation: _\*fléuganą_ > _flēogan_ (regular).

#### Derivation trace

Proto input: _\*fléuganą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*flēoganą} \\
OE Heavy Syllable Nasal Apocope & \emph{*flēogan} \\
OE Secondary Nasalization & \emph{*flēogąn} \\
OE Weak Tail Reduction & \emph{*flēogan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _flēogan_

#### Reconstruction and comparative evidence

Ringe and Taylor derive the verb as _\*fleugana_ > OE _fléogan_ and elsewhere contrast West Saxon _fléogan_ with Anglian _flégan_, alongside related forms _fléoge_ / _flége_ [@RingeTaylor2014]. The form followed here, _\*fléuganą_, represents that inherited strong verb in the notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller record _flēogan_ as the ordinary Old English strong verb, and Bright gives the familiar paradigm _flēag_, flugon, flogen with present _fleogeð_ [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971]. The target in this entry is therefore the attested verbal infinitive itself.

#### Form note

Ringe and Taylor also list related _fléoge_ / _flége_ and Anglian _flégan_, which belong to the same family but do not replace the infinitive _flēogan_ treated here [@RingeTaylor2014].

#### Development to Old English

From _\*fléuganą_, Old English diphthong leveling gives _\*flēoganą_; heavy-syllable nasal apocope and weak-tail reduction then yield _flēogan_ [@RingeTaylor2014]. The development is therefore regular: _\*fléuganą_ > _flēogan_.

### forlorn — OE lēosan

\index[oe]{leosan@lēosan}
\index[pgmc]{leusana@*léusaną}

Derivation: _\*léusaną_ > _lēosan_ (regular).

#### Derivation trace

Proto input: _\*léusaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*lēosaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*lēosan} \\
OE Secondary Nasalization & \emph{*lēosąn} \\
OE Weak Tail Reduction & \emph{*lēosan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lēosan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the verb under _\*leusan-_ and cites prefixed daughters such as Gothic _fra-liusan_ and Old English _for-lēosan_; Orel likewise gives Old English _for-leósan_ [@Kroonen2013; @Orel2003]. The inherited verbal base is therefore clear, though the daughter set often appears with the prefix.

#### Old English evidence

The direct Old English evidence behind English _forlorn_ lies in the prefixed verb _forlēosan_ and especially in the participle _forloren_, recorded by Ringe and Taylor and in the dictionaries [@RingeTaylor2014; @ClarkHall1960; @BosworthToller1898]. The simplex infinitive _lēosan_ represents the verbal base itself.

#### Form note

As a base-form comparison, the simplex infinitive is _lēosan_, while the English adjective continues the prefixed Old English family _forlēosan_ / _forloren_ [@RingeTaylor2014].

#### Development to Old English

From _\*léusaną_, Old English diphthong leveling gives _\*lēosaną_, and later nasal apocope and weak-tail reduction yield _lēosan_ [@RingeTaylor2014]. The prefixed forms follow the same verbal base with added _for-_.

### gang — OE gang

\index[oe]{gang@gang}
\index[pgmc]{gangaz@*gángaz}
\index[on]{gangr@gangr}

Derivation: _\*gángaz_ > _gang_ (regular).

#### Derivation trace

Proto input: _\*gángaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*gánga} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*gáng} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _gang_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*gangaz_ and cites Old English _gang_ beside Old Norse _gangr_, Old Frisian _gang_ / _gong_, Old Saxon _gang_, and Old High German _gang_ [@Orel2003]. The form followed here, _\*gángaz_, is the same lexeme in the accent notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller both record _gang_ as the noun 'going, journey, way', and Bright's glossary gives _gong (gang), m., path, course_ [@ClarkHall1960; @BosworthToller1898, 159; @BrightCassidyRingler1971, 392]. The target is therefore the attested noun headword itself.

#### Form note

This entry concerns the noun _gang_, not the separate verb _gangan_ [@ClarkHall1960; @BosworthToller1898, 159].

#### Development to Old English

From _\*gángaz_, loss of final _-z_ gives _\*gánga_, and later loss of final bare _-a_ yields _gang_. The development is therefore regular: _\*gángaz_ > _gang_.

### give — OE ġiefan

\index[oe]{giefan@ġiefan}
\index[pgmc]{gebana@*gébaną}

Derivation: _\*gébaną_ > _ġiefan_ (regular).

#### Derivation trace

Proto input: _\*gébaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*géban} \\
OE Secondary Nasalization & \emph{*gébąn} \\
PGmc B Allophony & \emph{*géβąn} \\
OE Velar Palatalization & \emph{*ʤéβąn} \\
OE Ws Palatal Diphthongization & \emph{*ʤíeβąn} \\
OE Weak Tail Reduction & \emph{*ʤíeβan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġiefan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the strong verb as _\*geban-_ and cites Old English _giefan_ among its reflexes [@Kroonen2013]. Ringe and Taylor contrast West Saxon _giefan_ with Mercian _for-geofan_ and Northumbrian _geafa_, showing that the inherited verb takes different later dialectal shapes [@RingeTaylor2014].

#### Old English evidence

Campbell gives _gefan_ (W-S _giefan_) among examples of initial palatalization, and Clark Hall records the verb under plain _giefan_ with forms such as _geaf_ and _giefen_ [@Campbell1959; @ClarkHall1960]. The spelling _ġiefan_ used here makes the palatal initial explicit.

#### Dialect note

West Saxon _ie_ here reflects palatal diphthongization after initial palatalization; non-West-Saxon forms such as _geafa_ or _for-geofan_ continue the same verb without the West Saxon vocalism [@RingeTaylor2014].

#### Development to Old English

From _\*gébaną_, initial _g_ palatalizes before _e_; West Saxon palatal diphthongization then yields _ie_, and later tail reduction gives _giefan_ [@Campbell1959; @RingeTaylor2014]. The result is therefore the regular West Saxon infinitive.

### gold — OE gold

\index[oe]{gold@gold}
\index[pgmc]{gultha@*gúlθą}

Derivation: _\*gúlθą_ > _gold_ (regular).

#### Derivation trace

Proto input: _\*gúlθą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc L Th Voicing & \emph{*gúldą} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*góldą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*góld} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _gold_

#### Reconstruction and comparative evidence

Ringe and Taylor cite the noun as _\*gulþa-_ / _\*gulda-_, and Kroonen gives the same pair [@RingeTaylor2014, 42; @Kroonen2013]. The form followed here, _\*gúlθą_, preserves the older consonantal form while leaving open whether the medial stop reflects inherited alternation or regular West Germanic development.

#### Old English evidence

Bosworth-Toller and Clark Hall both record _gold_ as the ordinary Old English neuter noun [@BosworthToller1898, 121; @ClarkHall1960, 152]. The target is therefore the attested citation form itself.

#### Development note

Ringe and Taylor note that the medial stop can be understood either as alternation _\*gulþa-_ / _\*gulda-_ or as the ordinary West Germanic change _\*lþ_ > _ld_; both routes lead to the same Old English consonantism [@RingeTaylor2014, 42].

#### Development to Old English

From _\*gúlθą_, the regular consonant development gives _\*gúldą_; Northwest Germanic / Old English lowering then yields _\*góldą_, and apocope gives _gold_ [@Campbell1959; @RingeTaylor2014, 42].

### grave — OE grafan

\index[oe]{grafan@grafan}
\index[pgmc]{grabana@*grábaną}

Derivation: _\*grábaną_ > _grafan_ (regular).

#### Derivation trace

Proto input: _\*grábaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*græbaną} \\
OE A Restoration & \emph{*grabaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*graban} \\
OE Secondary Nasalization & \emph{*grabąn} \\
PGmc B Allophony & \emph{*graβąn} \\
OE Weak Tail Reduction & \emph{*graβan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _grafan_

#### Reconstruction and comparative evidence

Campbell gives _grafan_ among the standard examples of Old English a-restoration before a single consonant and a following back vowel, and Ringe and Taylor describe the same development for Class VI infinitives [@Campbell1959, 61; @RingeTaylor2014].

#### Old English evidence

Clark Hall records _grafan_ as the verb 'to dig, grave' and separately records noun _græf_ 'grave, trench' [@ClarkHall1960]. The target here is the attested infinitive headword of the verb.

#### Development to Old English

From _\*grábaną_, Anglo-Frisian brightening first gives a fronted stem vowel. A-restoration then returns _a_ before single _b_ plus the back-vocalic infinitive ending, and later apocope and weak-tail reduction yield _grafan_ [@Campbell1959, 61; @RingeTaylor2014].

#### Form note

Noun _græf_ and verbal forms such as _græfð_ or past participial _græfen_ belong to other lexical or paradigm positions and do not replace the infinitive _grafan_ as the target here [@ClarkHall1960].

### guest — OE ġiest

\index[oe]{giest@ġiest}
\index[pgmc]{gastiz@*gástiz}

Derivation: _\*gástiz_ > _ġiest_ (regular).

#### Derivation trace

Proto input: _\*gástiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*gásti} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*gæsti} \\
OE Velar Palatalization & \emph{*ʤæsti} \\
OE I Umlaut & \emph{*ʤesti} \\
OE Ws Palatal Diphthongization & \emph{*ʤiesti} \\
\mbox{OE High Vowel Apocope} & \emph{*ʤiest} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġiest_

#### Reconstruction and comparative evidence

Campbell and Ringe-Taylor treat the noun as an ordinary i-stem whose West Saxon development shows palatal diphthongization, while non-West-Saxon evidence preserves forms of the _gest_ type [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall record the word under forms such as _gist_, _gest_, _giest_, and _gyst_ [@BosworthToller1898; @ClarkHall1960]. The Old English form here, _ġiest_, is the normalized West Saxon form within that attested family.

#### Development to Old English

From _\*gástiz_, Anglo-Frisian brightening gives a _gæst-_ stage, and i-mutation affects the front vowel before the lost high-vocalic ending. In West Saxon the initial palatal environment then produces _ie_, so the regular outcome is _ġiest_ [@Campbell1959; @RingeTaylor2014].

#### Dialect note

West Saxon _ġiest_ is the Old English form here. Anglian _gest_ and related spellings remain real Old English comparators rather than corrections to that choice [@RingeTaylor2014; @BosworthToller1898].

### hair — OE hǣr

\index[oe]{haer@hǣr}
\index[pgmc]{xera@*xḗrą}

Derivation: _\*xḗrą_ > _hǣr_ (regular).

#### Derivation trace

Proto input: _\*xḗrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*xǣrą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Velar Fricative Palatalization & \emph{*çǣrą} \\
OE Heavy Syllable Nasal Apocope & \emph{*çǣr} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hǣr_

#### Reconstruction and comparative evidence

Kroonen cites the ordinary Proto-Germanic hair word as _\*hēra-_ [@Kroonen2013]. The form followed here, _\*xḗrą_, represents that same long-ē stem in the present derivation.

#### Old English evidence

Clark Hall and Bosworth-Toller record _hær_ / _hǣr_ as the ordinary Old English noun 'hair' [@ClarkHall1960, 158; @BosworthToller1898, 510]. The target is therefore the attested headword itself.

#### Development to Old English

From _\*xḗrą_, Northwest Germanic lowering gives a long front vowel, and later loss of the final nasal leaves the Old English form _hǣr_. The development treated here is straightforward and does not require any special paradigm choice.

#### Form note

Older references to _\*xazwăz_ belong to a different lexeme, and the separate _haddr_ / _heordan_ / _hād-_ material does not displace the ordinary simplex _hǣr_ treated here [@Kroonen2013; @ClarkHall1960, 158].

### harvest — OE hierfest

\index[oe]{hierfest@hierfest}
\index[pgmc]{xarbistuz@*xárbistuz}

Derivation: _\*xárbistuz_ > _hierfest_ (regular).

#### Derivation trace

Proto input: _\*xárbistuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*xárbistu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xærbistu} \\
OE Breaking & \emph{*xearbistu} \\
OE Velar Fricative Palatalization & \emph{*çearbistu} \\
PGmc B Allophony & \emph{*çearβistu} \\
OE I Umlaut & \emph{*çierβistu} \\
OE High Vowel Apocope & \emph{*çierβist} \\
OE Med Unstressed I Lowering1 & \emph{*çierβest} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hierfest_

#### Reconstruction and comparative evidence

Bammesberger and Ringe-Taylor treat _\*harbist-_ as the inherited base and explain that the regular native West Saxon development would be of the _hierfest_ / _hyrfest_ type [@Bammesberger1997; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall record _hærfest_, with _herfest_ as a variant in the lexical tradition [@BosworthToller1898; @ClarkHall1960]. Those attested forms remain the main dictionary evidence for the noun.

#### Development to Old English

From _\*xárbistuz_, Anglo-Frisian brightening, breaking, and i-mutation produce a _hierbist-_ stage, and later lowering of unstressed medial _i_ to _e_ gives _hierfest_. That is the regular West Saxon development treated here [@RingeTaylor2014; @Campbell1959].

#### Source note

The Old English form here, _hierfest_, represents the regular native West Saxon outcome discussed by Bammesberger and Ringe-Taylor. The attested Old English lexical tradition, however, is chiefly _hærfest_ / _herfest_, commonly treated as non-West-Saxon or Anglian material in West Saxon transmission [@Bammesberger1997; @RingeTaylor2014].

### hedge — OE heġġ

\index[oe]{hegg@heġġ}
\index[pgmc]{xagjaz@*xágjaz}

Derivation: _\*xágjaz_ > _heġġ_ (regular).

#### Derivation trace

Proto input: _\*xágjaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*xággjaz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*xággja} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*xággj} \\
Anglo Frisian Brightening & \emph{*xæggj} \\
OE Velar Fricative Palatalization & \emph{*çæggj} \\
OE Velar Palatalization & \emph{*çæʤʤj} \\
OE I Umlaut & \emph{*çeʤʤj} \\
OE J Loss After Heavy & \emph{*çeʤʤ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _heġġ_

#### Reconstruction and comparative evidence

The derivational input models a palatal _\*-gj-_ noun whose Old English development includes gemination, palatalization, and i-mutation. The current derivation therefore reaches a palatal-geminate outcome of the _heġġ_ type [@Campbell1959].

#### Old English evidence

Bosworth-Toller and Clark Hall record the noun under standard spellings _hecg_ / _heċġ_ [@BosworthToller1898; @ClarkHall1960]. The lexical item itself is therefore well attested even though the form compared here is normalized.

#### Development to Old English

From _\*xágjaz_, West Germanic j-gemination first yields a geminate stop, and later Old English palatalization and loss of final _j_ produce _heġġ_. The development is treated as regular rather than exceptional.

#### Form note

Standard dictionary spelling is _heċġ_ or _hecg_. Normalized _heġġ_ is the Old English form here, while the ordinary lexicographic forms remain the main Old English citation evidence [@BosworthToller1898; @ClarkHall1960].

### helm — OE helm

\index[oe]{helm@helm}
\index[pgmc]{xelmaz@*xélmaz}

Derivation: _\*xélmaz_ > _helm_ (regular).

#### Derivation trace

Proto input: _\*xélmaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*xélma} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*xélm} \\
OE Velar Fricative Palatalization & \emph{*çélm} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _helm_

#### Reconstruction and comparative evidence

Kroonen cites the helmet noun as _\*helma-_ and separately distinguishes a different lexeme _\*helman-_ 'rudder' [@Kroonen2013]. The form followed here, _\*xélmaz_, is the nominative-style form used for the helmet noun itself.

#### Old English evidence

Clark Hall and Bosworth-Toller record _helm_ as the ordinary Old English noun for 'helmet', while _helma_ belongs to a separate rudder lexeme [@ClarkHall1960; @BosworthToller1898, 542].

#### Development to Old English

From _\*xélmaz_, loss of final _z_ and later loss of the short final vowel yield _helm_. The development is therefore a straightforward citation-form match.

#### Form note

Comparative _\*helma-_ is headword notation for the helmet cognate set. It should not be confused with Old English _helma_, which is a different noun meaning 'helm, rudder' [@Kroonen2013; @ClarkHall1960].

### help — OE helpan

\index[oe]{helpan@helpan}
\index[pgmc]{xelpana@*xélpaną}

Derivation: _\*xélpaną_ > _helpan_ (regular).

#### Derivation trace

Proto input: _\*xélpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Velar Fricative Palatalization & \emph{*çélpaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*çélpan} \\
OE Secondary Nasalization & \emph{*çélpąn} \\
OE Weak Tail Reduction & \emph{*çélpan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _helpan_

#### Reconstruction and comparative evidence

The entry treats the strong verb itself rather than the separate noun _help_. Bright's principal parts _helpan, healp, hulpon, holpen_ show the ordinary Old English strong-verb family continued by this input [@BrightCassidyRingler1971].

#### Old English evidence

Clark Hall and Bosworth-Toller record _helpan_ as the verbal headword 'to help' [@ClarkHall1960; @BosworthToller1898, 542]. The target is therefore the attested infinitive citation form.

#### Development to Old English

From _\*xélpaną_, no special repair is needed beyond the ordinary reduction of the infinitive ending. The derivation therefore reaches _helpan_ directly.

#### Form note

Noun _help_ belongs to a separate lexical line and should not replace verbal _helpan_ as the target here [@ClarkHall1960; @BosworthToller1898, 542].

### hind — OE hind

\index[oe]{hind@hind}
\index[pgmc]{xendjo@*xéndjō}

Derivation: _\*xéndjō_ > _hind_ (regular).

#### Derivation trace

Proto input: _\*xéndjō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*xéndju} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Velar Fricative Palatalization & \emph{*çéndju} \\
OE I Umlaut & \emph{*çindju} \\
\mbox{OE High Vowel Apocope} & \emph{*çindj} \\
OE J Loss After Heavy & \emph{*çind} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hind_

#### Reconstruction and comparative evidence

Kroonen cites the animal name as _\*hindō-_ f. 'hind' [@Kroonen2013]. The form followed here, _\*xéndjō_, represents that same noun in the present derivation.

#### Old English evidence

Clark Hall and Bosworth-Toller record _hind_ as the noun 'hind, female deer' [@ClarkHall1960; @BosworthToller1898, 554]. The target is therefore the attested lexical item itself.

#### Development to Old English

From _\*xéndjō_, i-mutation produces the front-vocalic Old English stem, and later apocope plus loss of final _j_ yield _hind_. The outcome is therefore a regular citation-form derivation.

#### Form note

_hindan_ 'from behind, behind' is a different Old English lexeme and does not belong to the noun history of _hind_ [@ClarkHall1960; @BosworthToller1898, 554].

### hold — OE healdan

\index[oe]{healdan@healdan}
\index[pgmc]{xaldana@*xáldaną}

Derivation: _\*xáldaną_ > _healdan_ (regular).

#### Derivation trace

Proto input: _\*xáldaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xældaną} \\
OE Breaking & \emph{*xealdaną} \\
OE Velar Fricative Palatalization & \emph{*çealdaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*çealdan} \\
OE Secondary Nasalization & \emph{*çealdąn} \\
OE Weak Tail Reduction & \emph{*çealdan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _healdan_

#### Reconstruction and comparative evidence

Campbell and Ringe-Taylor treat the verb as a regular _\*a_ + lC breaking case, with West Saxon _healdan_ opposed to Anglian and Mercian _haldan_ [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bright gives the ordinary strong-verb citation form and principal parts _healdan, heold, heoldon, healden_ [@BrightCassidyRingler1971]. The target is therefore the attested infinitive headword itself.

#### Development to Old English

From _\*xáldaną_, Anglo-Frisian brightening first yields a fronted vowel, and West Saxon breaking then produces _ea_ before _ld_. Later reduction of the infinitive ending gives _healdan_ [@Campbell1959; @RingeTaylor2014].

#### Dialect note

West Saxon _healdan_ is the Old English form here. Anglian and Mercian _haldan_ are genuine non-West-Saxon doublets rather than corrections to that choice [@Campbell1959; @RingeTaylor2014].

### horn — OE horn

\index[oe]{horn@horn}
\index[pgmc]{xurna@*xúrną}

Derivation: _\*xúrną_ > _horn_ (regular).

#### Derivation trace

Proto input: _\*xúrną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*xórną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*xórn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _horn_

#### Reconstruction and comparative evidence

Kroonen and Orel cite lemma-style Proto-Germanic headwords of the _\*hurna-_ / _\*xurnan_ type for this noun [@Kroonen2013; @Orel2003, 234]. The form followed here, _\*xúrną_, is the nominative-style form used in the derivation here.

#### Old English evidence

Clark Hall, Bosworth-Toller, and Bright all record _horn_ as the ordinary Old English noun [@ClarkHall1960; @BosworthToller1898, 108; @BrightCassidyRingler1971]. The target is therefore the attested citation form.

#### Development to Old English

From _\*xúrną_, Northwest Germanic u-lowering gives _\*xórną_, and later loss of the final nasal leaves _horn_. The development treated here is fully regular.

#### Form note

The note's oblique _\*xurnăn_ belongs to comparative stem background only. It does not replace the derivational input _\*xúrną_ as the derivational form used here [@Kroonen2013; @Orel2003, 234].

### lead — OE lǣdan

\index[oe]{laedan@lǣdan}
\index[pgmc]{laidijana@*láidijaną}

Derivation: _\*láidijaną_ > _lǣdan_ (regular).

#### Derivation trace

Proto input: _\*láidijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*lādijaną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*lādijan} \\
OE Secondary Nasalization & \emph{*lādijąn} \\
Sievers Law Syncope & \emph{*lādjąn} \\
OE I Umlaut & \emph{*lǣdjąn} \\
OE Weak Tail Reduction & \emph{*lǣdjan} \\
OE J Loss After Heavy & \emph{*lǣdan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lǣdan_

#### Reconstruction and comparative evidence

Ringe and Taylor derive Old English _lǣdan_ from Proto-Germanic _\*laidijaną_, and Kroonen likewise cites a weak verb of the _\*laidjan-_ type for 'lead' [@RingeTaylor2014; @Kroonen2013, 363].

#### Old English evidence

Clark Hall and Bosworth-Toller both record _lædan_ / _lǣdan_ as the ordinary Old English verb 'to lead, guide, conduct' [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*láidijaną_, monophthongization of _\*ai_ first gives a _\*lād-_ stage. Later syncope, i-mutation, weak-tail reduction, and loss of _j_ after a heavy stem yield _lǣdan_, so the development represented here is fully regular [@RingeTaylor2014].

### learn — OE liornian

\index[oe]{liornian@liornian}
\index[pgmc]{liznojana@*líznōjaną}

Derivation: _\*líznōjaną_ > _liornian_ (regular).

#### Derivation trace

Proto input: _\*líznōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*líornōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*líornōjan} \\
OE Secondary Nasalization & \emph{*líornōjąn} \\
OE I Umlaut & \emph{*líornējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*líornejąn} \\
OE Weak Tail Reduction & \emph{*líornejan} \\
OE Intervocalic J Vocalization & \emph{*líorneian} \\
OE Unstressed EI Contraction & \emph{*líornian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liornian_

#### Reconstruction and comparative evidence

Ringe and Taylor place the verb in a class-II weak family of the _\*liznō-_
type [@RingeTaylor2014], and Kroonen keeps the same comparative base for the
Germanic lexeme [@Kroonen2013]. The derivational input therefore requires no change
of stem class or paradigm cell.

The non-obvious issue is dialectal. Campbell records Northumbrian _liornian_
beside _leornian_, and he states that the _eo_ of _leornian_ is secondary,
while Northumbrian preserves forms with _io_, where original _eo_ and _io_
remain distinct [@Campbell1959, §123 n. 2].

#### Old English evidence

The form modeled here is _liornian_, the Northumbrian member of the Old
English family. Dictionary practice more often privileges _leornian_ as the
ordinary headword [@ClarkHall1960; @BrightCassidyRingler1971], but Campbell's
dialect evidence shows that _liornian_ is a genuine Old English form
[@Campbell1959, §123 n. 2].

This entry therefore remains compact. The point is to state clearly that the
Old English form here belongs to the Northumbrian side of the OE evidence rather than
to the leveled _leornian_ headword tradition.

#### Development to Old English

From _\*líznōjaną_, the expected Old English developments include rhotacism of
_z_, followed by breaking before _r_ plus consonant, and the ordinary reduction
of the weak verbal ending. The result is _liornian_, preserving the _io_
spelling that Campbell associates with Northumbrian where original _eo_ and
_io_ remain distinct [@Campbell1959, §123 n. 2].

_Leornian_ reflects the later _eo_ development that Campbell treats as
secondary [@Campbell1959, §123 n. 2; §296]. The selected Northumbrian target is
therefore the regular comparison form for the _i_-grade member of the family.

#### Form comparison

The comparison below sets the relevant forms side by side. It distinguishes the regular Northumbrian form
modeled here from the better-known West Saxon headword.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*líznōjaną_ > _liornian_ | computed regular output; attested Northumbrian comparison form | selected comparison |
| _leornian_ | attested later _eo_ form and dictionary headword | useful control, but not the target of this entry |

### lid — OE hlid

\index[oe]{hlid@hlid}
\index[pgmc]{xlida@*xlídą}
\index[on]{hlitho@hliþó}

Derivation: _\*xlídą_ > _hlid_ (regular).

#### Derivation trace

Proto input: _\*xlídą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*xlíd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hlid_

#### Reconstruction and comparative evidence

Orel cites a neuter lexeme of the _\*xliđ-_ type with Old English _hlid_, and Lloyd includes OE _hlid_ beside ON _hliþó_ and OHG _(h)lit_ among forms that retain _i_ [@Orel2003; @Lloyd1966].

#### Old English evidence

Clark Hall and Bosworth-Toller record _hlid_ as the noun 'lid, cover, door, gate' [@ClarkHall1960; @BosworthToller1898, 563].

#### Development to Old English

The derivational input already represents the later Germanic _hliđ-_ stage used for the derivation here. From _\*xlídą_, heavy-syllable apocope yields _hlid_, and the form belongs to the retained-_i_ set noted by Lloyd rather than to the lowered _e_ type [@Lloyd1966].

#### Form note

An earlier etymological stage _\*liþuz_ belongs to comparative background only. The form represented here is the later _\*xlídą_ > _hlid_ line that matches the attested Old English noun [@Orel2003; @Lloyd1966].

### light — OE līehtan

\index[oe]{liehtan@līehtan}
\index[pgmc]{leuxtijana@*léuxtijaną}

Derivation: _\*léuxtijaną_ > _līehtan_ (regular).

#### Derivation trace

Proto input: _\*léuxtijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*lēoxtijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*lēoxtijan} \\
OE Secondary Nasalization & \emph{*lēoxtijąn} \\
Sievers Law Syncope & \emph{*lēoxtjąn} \\
OE I Umlaut & \emph{*līextjąn} \\
OE Weak Tail Reduction & \emph{*līextjan} \\
OE J Loss After Heavy & \emph{*līextan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _līehtan_

#### Reconstruction and comparative evidence

Fulk gives Proto-Germanic _\*liuxtijanan_ with Old English _līehtan_ 'illuminate', and Ringe and Taylor likewise derive West Saxon _liehtan_ from the same weak-verb formation [@Fulk2018; @RingeTaylor2014].

#### Old English evidence

Clark Hall and Bosworth-Toller preserve the verb family under spellings such as _liehtan_, _lihtan_, and _līhtan_, distinct from the related noun _lēoht_ and adjective _leoht_/_liht_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*léuxtijaną_, the regular verbal line preserves _\*xt_, passes through a West Saxon _liehtan_ stage, and is represented here by normalized _līehtan_. The word treated in this entry is therefore the verb 'to light, illuminate', not the related noun from _\*leuxtą_ [@Fulk2018; @RingeTaylor2014].

#### Dialect note

Ringe and Taylor and Campbell distinguish West Saxon _liehtan_ from Anglian _lihtan_, while later West Saxon also shows _lyhtan_ [@RingeTaylor2014; @Campbell1959].

### linden — OE lind

\index[oe]{lind@lind}
\index[pgmc]{lindo@*líndō}

Derivation: _\*líndō_ > _lind_ (regular).

#### Derivation trace

Proto input: _\*líndō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*líndu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*línd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lind_

#### Reconstruction and comparative evidence

Kroonen cites _\*lindō-_ 'lime tree' and gives Old English _lind_ as the relevant reflex [@Kroonen2013].

#### Old English evidence

Clark Hall and Bosworth-Toller both record _lind_ as the noun 'lime-tree, linden' [@ClarkHall1960; @BosworthToller1898, 630].

#### Development to Old English

From _\*líndō_, Northwest Germanic final _\*ō_ raising first gives a _\*líndu_ stage, and later high-vowel apocope yields _lind_. The development is therefore straightforward and regular.

#### Form note

The Old English noun represented here is _lind_. Clark Hall also has a separate adjectival _linden_ 'made of linden-wood', but that is not the noun counterpart for this entry [@ClarkHall1960].

### milk — OE meoloc

\index[oe]{meoloc@meoloc}
\index[pgmc]{melukz@*mélukz}

Derivation: _\*mélukz_ > _meoloc_ (regular).

#### Derivation trace

Proto input: _\*mélukz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*méluk} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*mélok} \\
OE Back Mutation & \emph{*méolok} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _meoloc_

#### Reconstruction and comparative evidence

Kroonen and Orel reconstruct the noun as _\*meluk-_ / _\*melukz_, and the nominative-style input used here is _\*mélukz_ [@Kroonen2013; @Orel2003, 306].

#### Old English evidence

Old English preserves a mixed dossier for this noun. Ringe and Taylor describe West Saxon _meolc_ < _meoluc_ < _\*meluk_, Campbell likewise discusses _meoluc_ and _meoloc_, and Anglian shows _milc_ [@RingeTaylor2014; @Campbell1959].

#### Development to Old English

The unsyncopated line from _\*mélukz_ loses final _\*z_, lowers unstressed _u_ to _o_, and with back mutation yields _meoloc_. That fuller unsyncopated outcome is the form represented here [@RingeTaylor2014].

#### Form comparison

Syncopated _meolc_ and Anglian _milc_ belong to the competing leveled tradition associated with oblique forms, whereas _meoloc_ / _meoluc_ preserves the fuller nominal shape [@Campbell1959; @RingeTaylor2014].

### mother — OE mōder

\index[oe]{moder@mōder}
\index[pgmc]{moder@*mōdēr}

Derivation: _\*mōdēr_ > _mōder_ (regular).

#### Derivation trace

Proto input: _\*mōdēr_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*mōdǣr} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*mōdær} \\
OE Unstressed AE Merger & \emph{*mōder} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _mōder_

#### Reconstruction and comparative evidence

Kroonen and Orel cite the Proto-Germanic r-stem kinship noun as _\*mōder-_ / _\*mōdēr_ [@Kroonen2013; @Orel2003].

#### Old English evidence

The transmitted Old English headword tradition is _mōdor_ / _modor_, with oblique _mēder_ in the paradigm. Clark Hall, Campbell, and Ringe and Taylor all preserve that contrast [@ClarkHall1960; @Campbell1959; @RingeTaylor2014].

#### Development to Old English

From _\*mōdēr_, the regular suffixal development yields _mōder_. That regular nominative reflex is the form represented here, while the more familiar citation form _mōdor_ reflects later levelling within the r-stem paradigm [@Campbell1959; @RingeTaylor2014].

#### Form comparison

The note therefore concerns inherited vocalism rather than a different lexeme: _mōder_ is the regularized nominative represented here, but dictionaries usually print _mōdor_ / _modor_, and the oblique evidence survives in _mēder_ [@ClarkHall1960; @RingeTaylor2014].

### net — OE nett

\index[oe]{nett@nett}
\index[pgmc]{natja@*nátją}

Derivation: _\*nátją_ > _nett_ (regular).

#### Derivation trace

Proto input: _\*nátją_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*náttją} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*nættją} \\
OE Heavy Syllable Nasal Apocope & \emph{*nættj} \\
OE I Umlaut & \emph{*nettj} \\
OE J Loss After Heavy & \emph{*nett} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nett_

#### Reconstruction and comparative evidence

Orel gives _\*natjan_ with Old English _nett_, and Fulk's account of West Germanic gemination before _j_ explains the geminate outcome after a short vowel [@Orel2003; @Fulk2018].

#### Old English evidence

Clark Hall and Bosworth-Toller record _nett_ as the noun, and Campbell notes that final geminates are often graphically simplified in Old English spelling [@ClarkHall1960; @BosworthToller1898, 29; @Campbell1959].

#### Development to Old English

From _\*nátją_, West Germanic j-gemination first gives _\*náttją_. Later brightening, loss of the weak ending, and loss of final _j_ after a heavy stem yield _nett_, so the development represented here is regular [@Fulk2018].

#### Form note

Spellings in _net_ can therefore be graphic simplifications, but the lexical target supported by the dictionary evidence is _nett_ [@Campbell1959; @Orel2003].

### nightmare — OE mare

\index[oe]{mare@mare}
\index[pgmc]{maron@*márōn}

Derivation: _\*márōn_ > _mare_ (regular).

#### Derivation trace

Proto input: _\*márōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*márǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mærǭ} \\
OE A Restoration & \emph{*marǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*maræ} \\
OE Unstressed AE Merger & \emph{*mare} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _mare_

#### Reconstruction and comparative evidence

Ringe and Taylor treat the lexeme as Proto-Germanic / Proto-Northwest-Germanic _\*marōn-_, with Old English _mare, maran_, and variant _mere_; Orel preserves the same comparative lemma though with a different Old English headword tradition [@RingeTaylor2014; @Orel2003].

#### Old English evidence

Clark Hall records _mare_ 'nightmare, monster' and also preserves related variant forms _mera_ / _mere_ [@ClarkHall1960, 213].

#### Development to Old English

The selected simplex input _\*márōn_ regularly gives _mare_ after brightening, A-restoration before the n-stem ending, and later reduction of the final vowel. The word represented here is the attested simplex noun, not an attested compound [@RingeTaylor2014].

#### Form note

The concept corresponds to an unattested compound _\*nihtmare_, but the Old English lexical evidence is for simplex _mare_, with oblique _maran_ and variant _mere_ / _mera_ [@RingeTaylor2014; @ClarkHall1960, 213].

### coat — OE rocc

\index[oe]{rocc@rocc}
\index[pgmc]{rukkaz@*rúkkaz}

Derivation: _\*rúkkaz_ > _rocc_ (regular).

#### Derivation trace

Proto input: _\*rúkkaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*rókkaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*rókka} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*rókk} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _rocc_

#### Reconstruction and comparative evidence

Orel cites a masculine _\*rukkaz_ for the garment word, while Kroonen gives _\*hrukka-_. Both treat this as the garment lexeme and not as the separate stone word [@Orel2003; @Kroonen2013, 290].

#### Old English evidence

Clark Hall and Bosworth-Toller record _rocc_ as an over-garment or tunic and preserve compounds such as _bisceoprocc_ and _breóstrocc_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

With _\*rúkkaz_ as the derivational input, Northwest Germanic u-lowering and later loss of final _-a_ yield _rocc_ as a regular outcome.

#### Source note

This entry concerns the garment noun only. The stone word seen in _stānrocc_ belongs to a different lexical history [@ClarkHall1960; @BosworthToller1898].

### sheep — OE sċēap

\index[oe]{sceap@sċēap}
\index[pgmc]{skepa@*skḗpą}

Derivation: _\*skḗpą_ > _sċēap_ (regular).

#### Derivation trace

Proto input: _\*skḗpą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*skǣpą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*skǣp} \\
OE Sk Palatalization & \emph{*ʃǣp} \\
OE Ws Palatal Diphthongization & \emph{*ʃēap} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēap_

#### Reconstruction and comparative evidence

Ringe and Taylor cite a later West Germanic _\*skap_ > WS _scéap_, while Orel preserves a Proto-Germanic noun of the _\*skēp-_ type for the same lexeme [@RingeTaylor2014; @Orel2003].

#### Old English evidence

Clark Hall records _scēap_ with spelling variation, and Campbell likewise lists West Saxon _scéap_ among the palatal-diphthongized forms [@ClarkHall1960; @Campbell1959].

#### Development to Old English

From _\*skḗpą_, Northwest Germanic lowering gives _\*skǣpą_; after apocope and palatalization the West Saxon branch diphthongizes to _sċēap_. The development represented here is therefore fully regular.

#### Dialect note

Ringe and Taylor contrast West Saxon _scéap_ with Mercian and Kentish _scép_, and Campbell also notes Northumbrian _scip_. The form represented here is the West Saxon headword [@RingeTaylor2014; @Campbell1959].

### shilling — OE sċilling

\index[oe]{scilling@sċilling}
\index[pgmc]{skillingaz@*skíllingaz}

Derivation: _\*skíllingaz_ > _sċilling_ (regular).

#### Derivation trace

Proto input: _\*skíllingaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*skíllinga} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*skílling} \\
OE Sk Palatalization & \emph{*ʃílling} \\
OE Med Unstressed I Lowering1 & \emph{*ʃílleng} \\
OE Med Unstressed I Lowering & \emph{*ʃílling} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċilling_

#### Reconstruction and comparative evidence

Kroonen treats the cognate set under _\*skellinga-_ ~ _\*skillinga-_ and connects it with _\*skeld-linga-_, while Orel likewise gives the coin word with OE _scilling_ among the reflexes [@Kroonen2013; @Orel2003]. The form followed here, _\*skíllingaz_, is the nominative-style form used here to represent that inherited _\*-ing-_ derivative.

#### Old English evidence

Clark Hall records _scilling_, and Campbell cites _scilling_ among nouns whose derivational _-ing_ keeps _i_ in unstressed syllables [@ClarkHall1960; @Campbell1959]. The target represented here is the ordinary OE citation form, normalized as _sċilling_.

#### Development to Old English

From _\*skíllingaz_, loss of final _-az_ yields _\*skílling_. Old English palatalization of initial _sk_ before front vocalism then gives _sċilling_. The note matters because derivational _-ing-_ keeps _i_, so the regular outcome is _sċilling_, not _\*sċilleng_ [@Campbell1959; @Hogg1992].

#### Form note

Kroonen's _\*skellinga-_ ~ _\*skillinga-_ and his internal analysis _\*skeld-linga-_ belong to the etymological background of the cognate set. The form followed here, _\*skíllingaz_, is the specific form used for the derivation represented here [@Kroonen2013].

### show — OE sċēawian

\index[oe]{sceawian@sċēawian}
\index[pgmc]{skawojana@*skáwōjaną}

Derivation: _\*skáwōjaną_ > _sċēawian_ (regular).

#### Derivation trace

Proto input: _\*skáwōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Aw Long Diphthong & \emph{*skḗawōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*skḗawōjan} \\
OE Secondary Nasalization & \emph{*skḗawōjąn} \\
OE Sk Palatalization & \emph{*ʃḗawōjąn} \\
OE I Umlaut & \emph{*ʃḗawējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*ʃḗawejąn} \\
OE Weak Tail Reduction & \emph{*ʃḗawejan} \\
OE Intervocalic J Vocalization & \emph{*ʃḗaweian} \\
OE Unstressed EI Contraction & \emph{*ʃḗawian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēawian_

#### Reconstruction and comparative evidence

Orel and Kroonen cite a Class II verb of the type [_\*skawōjan-_]{.iv lang=pgmc sort=skawojan role=source_protoform}, with OE [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form} among the reflexes [@Orel2003; @Kroonen2013, 482]. Brunner likewise records the Old English family as [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form}, [_scāwian_]{.iv lang=oe sort=scawian role=comparison_form}, which places this entry in the ordinary show-verb set rather than in a special finite-cell workaround [@SieversBrunner1965].

#### Old English evidence

Bright lists [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form} (W. II.) and also the related form [_scēawa_]{.iv lang=oe sort=sceawa role=comparison_form} [@BrightCassidyRingler1971]. The source tradition therefore uses [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form}, while the target represented here is the normalized project spelling [_sċēawian_]{.iv lang=oe sort=sceawian role=target_form}.

#### Development to Old English

From [_\*skáwōjaną_]{.iv lang=pgmc sort=skawojana role=selected_input}, Old English _aw_ before a following vowel yields _ēaw_, and the Class II suffix keeps _\*ō_ between _\*w_ and _\*j_. The development therefore runs regularly to [_sċēawian_]{.iv lang=oe sort=sceawian role=target_form}, without the direct _\*aw+j_ problem seen in other verb types [@Campbell1959; @Orel2003].

#### Form note

The difference between [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form} and [_sċēawian_]{.iv lang=oe sort=sceawian role=target_form} is orthographic normalization of initial <_sc_>, not a difference of lexeme or paradigm cell [@Campbell1959; @Hogg1992].

### sleep — OE slǣpan

\index[oe]{slaepan@slǣpan}
\index[pgmc]{slepana@*slḗpaną}

Derivation: _\*slḗpaną_ > _slǣpan_ (regular).

#### Derivation trace

Proto input: _\*slḗpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*slǣpaną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*slǣpan} \\
OE Secondary Nasalization & \emph{*slǣpąn} \\
OE Weak Tail Reduction & \emph{*slǣpan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _slǣpan_

#### Reconstruction and comparative evidence

Kroonen preserves the comparative verb as _\*slēpan-_, and Fulk cites the same family under root _\*slēb-_ [@Kroonen2013; @Fulk2018, 120]. The form followed here, _\*slḗpaną_, is the infinitive-style form used here for that inherited sleep-verb.

#### Old English evidence

Clark Hall gives _slæpan_ with preterite _slēp_, _slēap_, and Bright likewise lists _slæpan_ _(slāpan)_, _slēp_ _slēpon_ _slēpen_ [@ClarkHall1960; @BrightCassidyRingler1971, 435]. The target represented here is therefore the normalized infinitive _slǣpan_, not the preterite forms and not the separate noun _slǣp_.

#### Development to Old English

From _\*slḗpaną_, Northwest Germanic lowering gives _\*slǣpaną_. The later OE tail developments then yield _slǣpan_ regularly. Brunner and Bülbring show that the OE tradition also has variant spellings such as West Saxon _slāpan_/_slæpan_ and Anglian or Kentish _slēpan_, but those do not displace the infinitive chosen here [@SieversBrunner1965; @Bulbring1902].

#### Form note

The note concerns lemma type rather than a special derivational problem: this row represents the verb _slǣpan_, whereas _slǣp_ belongs to noun or lookup background and _slēp_/_slēap_ are preterite forms [@ClarkHall1960; @BrightCassidyRingler1971, 435].

### smear — OE smierwan

\index[oe]{smierwan@smierwan}
\index[pgmc]{smerwijana@*smérwijaną}

Derivation: _\*smérwijaną_ > _smierwan_ (regular).

#### Derivation trace

Proto input: _\*smérwijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*sméorwijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*sméorwijan} \\
OE Secondary Nasalization & \emph{*sméorwijąn} \\
Sievers Law Syncope & \emph{*sméorwjąn} \\
OE I Umlaut & \emph{*smíerwjąn} \\
OE Weak Tail Reduction & \emph{*smíerwjan} \\
OE J Loss After Heavy & \emph{*smíerwan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _smierwan_

#### Reconstruction and comparative evidence

Kroonen gives the comparative headword as _\*smerwjan-_ [@Kroonen2013]. Ringe and Taylor instead cite a later-stage _\*smirwijana_, from which they derive West Saxon _smierwan_, Mercian _smirwan_, and Northumbrian _smiriga_ [@RingeTaylor2014]. The form followed here, _\*smérwijaną_, therefore represents the Kroonen-aligned PGmc layer, while the later-stage dialect split belongs to a different chronological level.

#### Old English evidence

The target represented here is the West Saxon citation form _smierwan_. Campbell's Anglian discussion explains the contrasting _smirwan_, and Clark Hall, Brunner, and Bright show that the same lexical family later also includes forms such as _smirian_, _smyrian_, and preterite _smyrode_ [@Campbell1959; @ClarkHall1960; @SieversBrunner1965; @BrightCassidyRingler1971].

#### Development to Old English

From _\*smérwijaną_, breaking before _r + consonant_ yields _eo_, and later i-umlaut produces _ie_. The result is West Saxon _smierwan_. Anglian _smirwan_ reflects the well-known failure of breaking in this environment, not a different lexeme [@Campbell1959; @RingeTaylor2014].

#### Dialect note

The entry therefore represents the West Saxon member of a broader OE family: _smierwan_ in West Saxon, _smirwan_ in Anglian or Mercian, and related later class-II forms such as _smirian_ or _smyrian_ in the same lexical field [@RingeTaylor2014; @ClarkHall1960].

### span — OE spannan

\index[oe]{spannan@spannan}
\index[pgmc]{spannana@*spánnaną}

Derivation: _\*spánnaną_ > _spannan_ (regular).

#### Derivation trace

Proto input: _\*spánnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*spánnan} \\
OE Secondary Nasalization & \emph{*spánnąn} \\
OE Weak Tail Reduction & \emph{*spánnan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _spannan_

#### Reconstruction and comparative evidence

Kroonen cites the inherited verb as _\*spannan-_, with OE _spannan_ among the reflexes [@Kroonen2013]. The form followed here, _\*spánnaną_, is the infinitive-style form used here for that same verbal lexeme.

#### Old English evidence

Clark Hall keeps noun _spann_ and verb _spannan_ separate, and Brunner likewise records _sponnan, spannan stv._ [@ClarkHall1960; @SieversBrunner1965]. This entry treats the strong-verb infinitive, not the separate noun.

#### Development to Old English

From _\*spánnaną_, the final nasal ending is lost and the regular OE weak-tail steps surface _spannan_. No paradigm-cell substitution is needed: the current derivation already lands on the infinitive directly.

#### Form note

The note matters because English _span_ can also reach noun _spann_ in local lookup material. The entry represented here is the verb _spannan_, with the noun treated elsewhere [@ClarkHall1960].

### spar — OE spearra

\index[oe]{spearra@spearra}
\index[pgmc]{sparro@*spárrô}

Derivation: _\*spárrô_ > _spearra_ (regular).

#### Derivation trace

Proto input: _\*spárrô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*spærrô} \\
OE Breaking & \emph{*spearrô} \\
OE Unstressed Long Vowel Shortening & \emph{*spearra} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _spearra_

#### Reconstruction and comparative evidence

Kroonen and Orel place this noun in the beam or rafter set _\*spar(r)an-_, with cognates such as Old Saxon and Old High German _sparro_ [@Kroonen2013; @Orel2003]. The form followed here, _\*spárrô_, is the OE-facing nominal form used here for that same lexeme.

#### Old English evidence

The noun represented here is _spearra_. The important lexical point is negative: English gloss overlap also reaches the unrelated verb _sperran_ 'to bar', but that verb does not belong to this row.

#### Development to Old English

From _\*spárrô_, Anglo-Frisian brightening gives _\*spærrô_, and OE breaking before geminate _rr_ yields _\*spearrô_, later _spearra_. The development is therefore regular for a breaking-conditioned noun of this type [@Luick1914].

#### Form note

This entry concerns the noun _spearra_ only. It should be kept separate from verb _sperran_, even though the Modern English glosses overlap [@Kroonen2013; @Orel2003].

### still — OE stillan

\index[oe]{stillan@stillan}
\index[pgmc]{stellijana@*stéllijaną}

Derivation: _\*stéllijaną_ > _stillan_ (regular).

#### Derivation trace

Proto input: _\*stéllijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*stéllijan} \\
OE Secondary Nasalization & \emph{*stéllijąn} \\
Sievers Law Syncope & \emph{*stélljąn} \\
OE I Umlaut & \emph{*stilljąn} \\
OE Weak Tail Reduction & \emph{*stilljan} \\
OE J Loss After Heavy & \emph{*stillan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _stillan_

#### Reconstruction and comparative evidence

The wider West Germanic family includes adjective _still_ and verb _stillen_ [@KlugeSeebold2011]. The form followed here, _\*stéllijaną_, represents the verbal j-formation used for the OE row.

#### Old English evidence

Clark Hall gives _stillan_ as the verb and separately _stille_ as the adjective [@ClarkHall1960]. Bosworth-Toller likewise preserves a substantial prefixed verbal family under _ge-stillan_ and related forms [@BosworthToller1898, 724]. The Old English form here is the verb _stillan_, not the adjective.

#### Development to Old English

As a heavy-stem Class I weak verb, _\*stéllijaną_ undergoes the expected syncope and i-umlaut, and later loss of _j_ after a heavy stem yields _stillan_. The development represented here is regular.

#### Form note

The note concerns lexical framing rather than sound law: _stillan_ is the verb represented here, while _stille_ belongs to the related adjectival branch of the family [@ClarkHall1960; @KlugeSeebold2011].

### summer — OE sumer

\index[oe]{sumer@sumer}
\index[pgmc]{sumaraz@*súmaraz}

Derivation: _\*súmaraz_ > _sumer_ (regular).

#### Derivation trace

Proto input: _\*súmaraz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*súmara} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*súmar} \\
Anglo Frisian Brightening & \emph{*súmær} \\
OE Unstressed AE Merger & \emph{*súmer} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sumer_

#### Reconstruction and comparative evidence

Kroonen gives the lexeme as _\*sumara-_, and Ringe and Taylor likewise use _\*sumaraz_, while Orel preserves an alternate _\*sumeraz_ [@Kroonen2013; @RingeTaylor2014; @Orel2003, 425]. The form followed here, _\*súmaraz_, follows the _\*a_ vocalism that underlies the regular development represented here.

#### Old English evidence

Clark Hall gives _sumor m., gs. sumeres, ds. sumera, sumere_, and Bright likewise lists _sumor (sumer)_ with genitive _sumeres_ [@ClarkHall1960; @BrightCassidyRingler1971, 440]. The tradition therefore preserves both _sumor_ and _sumer_, with the oblique forms strongly supporting second-syllable _e_.

#### Development to Old English

From _\*súmaraz_, loss of final _-az_ is followed by fronting and merger in the unstressed second syllable, yielding _sumer_. The form compared here is the regularized _e_-form, while the common citation form _sumor_ remains part of the attested OE tradition [@RingeTaylor2014].

#### Form note

The entry does not deny _sumor_. It represents _sumer_ as the regular outcome chosen here, while _sumor_ remains a common headword spelling and _sumeres_/_sumere_ show that the _e_-vocalism was also real in Old English [@ClarkHall1960; @BrightCassidyRingler1971, 440].

### sunder — OE sundrian

\index[oe]{sundrian@sundrian}
\index[pgmc]{sundrojana@*súndrōjaną}

Derivation: _\*súndrōjaną_ > _sundrian_ (regular).

#### Derivation trace

Proto input: _\*súndrōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*súndrōjan} \\
OE Secondary Nasalization & \emph{*súndrōjąn} \\
OE I Umlaut & \emph{*súndrējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*súndrejąn} \\
OE Weak Tail Reduction & \emph{*súndrejan} \\
OE Intervocalic J Vocalization & \emph{*súndreian} \\
OE Unstressed EI Contraction & \emph{*súndrian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sundrian_

#### Reconstruction and comparative evidence

Orel distinguishes three related formations: adverbial _\*sunþraz_ > _sundor_, Class I verbal _\*sunþrjanan_ > _syndrian_, and Class II verbal _\*sunþrōjanan_ > _sundrian_ [@Orel2003]. Kluge-Seebold aligns the cognate set with German _sondern_ and OE _gesundrian_, so this entry belongs with the Class II verb, not the adverb [@KlugeSeebold2011].

#### Old English evidence

Clark Hall and Bosworth-Toller keep _sundrian_ and _syndrian_ separate from adverbial _sundor_, and both preserve the prefixed verbal family _ā-sundrian_ [@ClarkHall1960, 296; @BosworthToller1898]. The target represented here is therefore the weak verb _sundrian_.

#### Development to Old English

From _\*súndrōjaną_, the Class II weak-verb suffix yields regular OE _-ian_, producing _sundrian_. Because this is the _\*-ōjan-_ verb and not the Class I _\*-jan-_ formation, the form represented here does not belong to the umlauted _syndrian_ branch.

#### Form note

The earlier confusion was lexical, not phonological: _sundor_ is the separate adverb, and _syndrian_ is a related but different verb. The verb treated here is the Class II verb _sundrian_ [@Orel2003; @ClarkHall1960, 296].

### swallow — OE swealwe

\index[oe]{swealwe@swealwe}
\index[pgmc]{swalwon@*swálwōn}

Derivation: _\*swálwōn_ > _swealwe_ (regular).

#### Derivation trace

Proto input: _\*swálwōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*swálwǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*swælwǭ} \\
OE Breaking & \emph{*swealwǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*swealwæ} \\
OE Unstressed AE Merger & \emph{*swealwe} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _swealwe_

#### Reconstruction and comparative evidence

Kroonen gives the bird name as _\*swalwōn-_, and Ringe and Taylor cite the later West Germanic stage _\*swalwa_, from which West Saxon _swealwe_ and Mercian _swalwe_ develop [@Kroonen2013, 535; @RingeTaylor2014, 200]. The selected etymological comparison belongs to the swallow-bird family, not to the verb _swelgan_.

#### Old English evidence

Clark Hall records _swealwe (a, o)_ as the noun headword [@ClarkHall1960]. Campbell and Brunner also preserve later or oblique-family forms such as _swaluwe_, _swalewan_, and _swealuwe_, but those belong to wider variation around the noun rather than to the citation form represented here [@Campbell1959; @SieversBrunner1965].

#### Development to Old English

From _\*swálwōn_, brightening yields _\*swælw-_, and breaking before _lw_ gives _\*swealw-_. The later noun ending develops regularly to _swealwe_. The relevant point is that the bird name has no inherited _\*g_: that consonant belongs to the separate verb _swelgan_ [@RingeTaylor2014, 200; @Kroonen2013, 535].

#### Form note

The final prose keeps the citation form _swealwe_ separate from two different kinds of background material: the unrelated verb _swelgan_, and later or oblique spellings such as _swaluwe_ or _swalewan_ [@ClarkHall1960; @Campbell1959].

### swine — OE swīn

\index[oe]{swin@swīn}
\index[pgmc]{swina@*swī́ną}
\index[pgmc]{swina@*swḯną}

Derivation: citation reconstruction _\*swī́ną_; form followed here _\*swī́ną_ > _swīn_ (regular).

#### Derivation trace

Proto input: _\*swī́ną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*swī́n} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _swīn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*swina-_ 'pig' [@Kroonen2013]. The selected comparative form here is the bare neuter citation cell _\*swī́ną_, which matches the singular noun aimed at in Old English rather than an oblique stem form.

#### Old English evidence

Clark Hall records _swin (y)_ as the ordinary noun headword [@ClarkHall1960]. The target here is that singular citation form _swīn_, not a plural glossed in Modern English as *swine*.

#### Development to Old English

From _\*swī́ną_, loss of the final nasal vowel yields _swīn_. The outcome is therefore the regular monosyllabic noun with preserved long root _ī_.

#### Source note

The derivational input writes stressed long _ī_ as _\*ī́_, so comparative _\*swī́ną_ and derivational _\*swī́ną_ represent the same lexical form.

### think — OE þenċan

\index[oe]{thencan@þenċan}
\index[pgmc]{thankijana@*θánkijaną}

Derivation: _\*θánkijaną_ > _þenċan_ (regular).

#### Derivation trace

Proto input: _\*θánkijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*θánkijan} \\
OE Secondary Nasalization & \emph{*θánkijąn} \\
Sievers Law Syncope & \emph{*θánkjąn} \\
OE Velar Palatalization & \emph{*θánʧjąn} \\
OE I Umlaut & \emph{*θenʧjąn} \\
OE Weak Tail Reduction & \emph{*θenʧjan} \\
OE J Loss After Heavy & \emph{*θenʧan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þenċan_

#### Reconstruction and comparative evidence

Kroonen gives the verb as _\*þankjan-_ 'to think', and Ringe and Taylor cite fully inflected _\*þankijaną_ beside OE _þenċan_ [@Kroonen2013; @RingeTaylor2014]. The noun _\*þankaz_ belongs only to the wider derivational background.

#### Old English evidence

Bosworth-Toller preserves the verb under _þencan_/_geþencan_, and the citation form here is the ordinary infinitive _þenċan_ [@BosworthToller1898].

#### Development to Old English

From _\*θánkijaną_, palatalization before _\*j_ and i-umlaut produce _þenċan_. The infinitive is therefore a straightforward weak-verb outcome.

#### Lexical note

Campbell's assibilation discussion uses the same verb _þencan_; the class-III relic _hycgan_ is a different lexeme [@Campbell1959; @Hogg1992].

### thorn — OE þorn

\index[oe]{thorn@þorn}
\index[pgmc]{thurnaz@*θúrnaz}

Derivation: _\*θúrnaz_ > _þorn_ (regular).

#### Derivation trace

Proto input: _\*θúrnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*θórnaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*θórna} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*θórn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þorn_

#### Reconstruction and comparative evidence

Kroonen gives _\*þurna-_ 'thorn, briar', while Orel preserves the masculine pair _\*þurnuz_ ~ _\*þurnaz_ [@Kroonen2013; @Orel2003]. The form followed here, _\*θúrnaz_, belongs to that same comparative family.

#### Old English evidence

Bright lists _þorn_, m., and Clark Hall likewise treats _þorn_ as the ordinary noun headword [@BrightCassidyRingler1971; @ClarkHall1960].

#### Development to Old English

The inherited stem shows regular lowering of _u_ to _o_ before _r_, and final loss yields _þorn_. The noun is therefore a regular Old English continuation of the Proto-Germanic thorn-family.

#### Source note

The comparative sources preserve more than one stem formation, but the Old English target itself is simply the citation form _þorn_.

### tide — OE tīd

\index[oe]{tid@tīd}
\index[pgmc]{tidiz@*tī́diz}
\index[pgmc]{tidiz@*tḯdiz}

Derivation: citation reconstruction _\*tī́diz_; form followed here _\*tī́diz_ > _tīd_ (regular).

#### Derivation trace

Proto input: _\*tī́diz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*tī́di} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*tī́d} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tīd_

#### Reconstruction and comparative evidence

Kroonen gives _\*tīdi-_ 'time', and Orel's _\*tīđiz_ points to the same feminine noun [@Kroonen2013; @Orel2003]. The related verb _tīdan_ is separate.

#### Old English evidence

Bright records _tīd_ with singular _tīde_ and plural _tīda_, and Clark Hall treats _tīd_ as the ordinary noun 'time, period, season' [@BrightCassidyRingler1971; @ClarkHall1960, 309].

#### Development to Old English

From _\*tī́diz_, final _z_ is lost and the high final vowel drops, leaving _tīd_. The development is straightforward for a feminine i-stem.

#### Lexical note

The note matters only because English *tide* can pull in the separate weak verb _tīdan_; the noun targeted here is _tīd_.

### token — OE tācn

\index[oe]{tacn@tācn}
\index[pgmc]{taikna@*táikną}

Derivation: _\*táikną_ > _tācn_ (regular).

#### Derivation trace

Proto input: _\*táikną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*tākną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*tākn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tācn_

#### Reconstruction and comparative evidence

Kroonen cites _\*taikna-_ and Orel _\*taiknan_ for the noun 'sign, token' [@Kroonen2013; @Orel2003, 438]. The form followed here, _\*táikną_, is the simple citation-form noun used for the derivation.

#### Old English evidence

Campbell and Sievers-Brunner preserve both unbroken _tācn_ and broken _tācen_, with oblique _tācnes_ remaining unbroken [@Campbell1959; @SieversBrunner1965].

#### Development to Old English

Monophthongization of _ai_ yields _ā_, and loss of the final nasal vowel leaves _tācn_. The unbroken form is therefore a regular Old English outcome.

#### Form note

_tācn_ is the attested unbroken citation form selected here. Later West Saxon prose often prefers _tācen_, but that does not displace the older unbroken form [@Campbell1959; @SieversBrunner1965].

### town — OE tūn

\index[oe]{tun@tūn}
\index[pgmc]{tuna@*tūną}

Derivation: _\*tūną_ > _tūn_ (regular).

#### Derivation trace

Proto input: _\*tūną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*tūn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tūn_

#### Reconstruction and comparative evidence

Kroonen cites _\*tūna-_ 'fenced area', while Orel gives _\*tūnan_ ~ _\*tūnaz_ [@Kroonen2013; @Orel2003, 452]. The form followed here, _\*tūną_, is the simple citation-form noun used in the derivation.

#### Old English evidence

Clark Hall records _tūn_ as the ordinary headword 'enclosure, yard, village, town' [@ClarkHall1960].

#### Development to Old English

The inherited long _ū_ is preserved, and loss of the final nasal vowel yields _tūn_ regularly [@SieversBrunner1965].

#### Source note

The comparative headwords vary, but the Old English target here is the direct citation form _tūn_, not an oblique _\*tūnăn_.

### wade — OE wadan

\index[oe]{wadan@wadan}
\index[pgmc]{wadana@*wádaną}

Derivation: _\*wádaną_ > _wadan_ (regular).

#### Derivation trace

Proto input: _\*wádaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wædaną} \\
OE A Restoration & \emph{*wadaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wadan} \\
OE Secondary Nasalization & \emph{*wadąn} \\
OE Weak Tail Reduction & \emph{*wadan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wadan_

#### Reconstruction and comparative evidence

Campbell and Ringe and Taylor describe A-restoration before a following back vowel, and Luick explicitly includes _wadan_ among the standard open-syllable examples [@Campbell1959; @RingeTaylor2014; @Luick1914, 239].

#### Old English evidence

Clark Hall gives _wadan_ as the verb 'to go, move, stride, advance', and Bright lists the same infinitive in the strong-verb paradigm [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

From _\*wádaną_, Anglo-Frisian brightening first gives _\*wædaną_. A-restoration before the back-vocalic infinitive ending then returns _a_, and later reduction yields _wadan_ [@Campbell1959; @RingeTaylor2014].

#### Development note

The note matters because this infinitive belongs to the A-restoration class. The citation form is therefore _wadan_, not a fronted _wæden_-type output.

### warp — OE weorpan

\index[oe]{weorpan@weorpan}
\index[pgmc]{werpana@*wérpaną}

Derivation: _\*wérpaną_ > _weorpan_ (regular).

#### Derivation trace

Proto input: _\*wérpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*wéorpaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wéorpan} \\
OE Secondary Nasalization & \emph{*wéorpąn} \\
OE Weak Tail Reduction & \emph{*wéorpan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weorpan_

#### Reconstruction and comparative evidence

Ringe and Taylor distinguish preterite _\*warp_ from infinitive _\*werpana_, and the derivational input here is the verbal form _\*wérpaną_ [@RingeTaylor2014].

#### Old English evidence

Clark Hall records _weorpan_ as the strong verb headword and separately lists _wearp_ as both noun and preterite. Bright gives the paradigm _weorpan, wearp, wurpon, worpen_ [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

Breaking before _r + C_ yields _weor-_, and the infinitive develops regularly to _weorpan_ [@Campbell1959; @Hogg1992].

#### Lexical note

The note matters because English *warp* also points to related _wearp_ material. Here the target is specifically the infinitive _weorpan_.

### wash — OE wascan

\index[oe]{wascan@wascan}
\index[pgmc]{waskana@*wáskaną}

Derivation: _\*wáskaną_ > _wascan_ (regular).

#### Derivation trace

Proto input: _\*wáskaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wæskaną} \\
OE A Restoration & \emph{*waskaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*waskan} \\
OE Secondary Nasalization & \emph{*waskąn} \\
OE Weak Tail Reduction & \emph{*waskan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wascan_

#### Reconstruction and comparative evidence

Kroonen cites _\*waskan-_, Orel _\*waskanan_, and Ringe and Taylor likewise derive Old English _wascan_ from the same verb family [@Kroonen2013; @Orel2003, 489; @RingeTaylor2014, 142].

#### Old English evidence

Clark Hall heads the verb as _wascan_, while Sievers-Brunner also notes the variant _wæscan_ [@ClarkHall1960; @SieversBrunner1965].

#### Development to Old English

From _\*wáskaną_, brightening gives _\*wæskaną_. A-restoration before the _sC_ cluster restores _a_, and medial _sc_ remains unpalatalized before the following back vowel, yielding _wascan_ [@Campbell1959; @RingeTaylor2014, 142].

#### Form note

The conservative citation form _wascan_ is selected here. Spellings such as _wæscan_ or _wasċan_ belong to variant or normalized background rather than to the target of this entry.

### wax — OE weaxan

\index[oe]{weaxan@weaxan}
\index[pgmc]{waxsana@*wáxsaną}

Derivation: _\*wáxsaną_ > _weaxan_ (regular).

#### Derivation trace

Proto input: _\*wáxsaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wæxsaną} \\
OE Breaking & \emph{*weaxsaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*weaxsan} \\
OE Secondary Nasalization & \emph{*weaxsąn} \\
OE Weak Tail Reduction & \emph{*weaxsan} \\
OE Xs Merge & \emph{*weaXSan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weaxan_

#### Reconstruction and comparative evidence

Kroonen cites the verb as _\*wahs(j)an-_, Orel as _\*waxsanan_, and Ringe and Taylor discuss the prehistory of Old English _weaxan_ within the same verbal family [@Kroonen2013; @Orel2003, 478; @RingeTaylor2014].

#### Old English evidence

Clark Hall gives _weaxan_ as the verb headword and separately records bare _wax_ as a preterite form; Bright likewise treats _weaxan_ as the infinitive [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

From _\*wáxsaną_, brightening and breaking yield _weax-_, and the infinitive develops regularly to _weaxan_. The cluster is preserved here, since _xs_ > _s_ belongs to forms where another consonant follows, such as _wæstm_, not to the infinitive itself [@Campbell1959; @SieversBrunner1965].

#### Lexical note

The target here is the infinitive _weaxan_. Noun _weax_ and preterite _wax_/_wēox_ belong to different lexical or paradigm slots.

### way — OE weġ

\index[oe]{weg@weġ}
\index[pgmc]{wegaz@*wégaz}

Derivation: _\*wégaz_ > _weġ_ (regular).

#### Derivation trace

Proto input: _\*wégaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*wéga} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*wég} \\
OE Velar Palatalization & \emph{*wéʤ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weġ_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*wega-_ 'way, road', while the selected derivational form here is nominative-singular _\*wégaz_ [@Kroonen2013]. Campbell, Hogg, and Ringe and Taylor use the same word as the standard contrast between singular palatal _weġ_ and inflected _wegas_/_wegum_ [@Campbell1959; @Hogg1992; @RingeTaylor2014, 341].

#### Old English evidence

The Old English singular is the ordinary noun _weg_, here normalized as _weġ_ to show the palatal final. The contrasting plural and oblique forms _wegas, wegum_ keep a velar stop before the following back vowel [@Campbell1959; @RingeTaylor2014, 341].

#### Development to Old English

From _\*wégaz_, final _\*z_ is lost and the weak tail apocopates, leaving word-final _\*g_ after a front vowel. In that environment Old English palatalization yields _weġ_, whereas _wegas_ remains velar because the following _a_ blocks the same outcome [@Campbell1959; @Hogg1992; @RingeTaylor2014, 341].

#### Form note

Normalized _weġ_ and dictionary _weg_ represent the same noun. _wē_ is not supported in the checked Old English evidence for 'way'.

### weapon — OE wǣpn

\index[oe]{waepn@wǣpn}
\index[pgmc]{wepna@*wḗpną}

Derivation: _\*wḗpną_ > _wǣpn_ (regular).

#### Derivation trace

Proto input: _\*wḗpną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*wǣpną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*wǣpn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wǣpn_

#### Reconstruction and comparative evidence

Kroonen reconstructs a double-stem noun _\*wēbna-_ ~ _\*wēpna-_ and cites OE _wæpn_ among its reflexes [@Kroonen2013, 617]. The form followed here, _\*wḗpną_, represents the unbroken citation-form noun rather than the later broken simplex.

#### Old English evidence

Campbell's cluster-noun discussion preserves unbroken _wépn_ beside broken
_wépen_-type forms [@Campbell1959, 150; @Campbell1959, 226–227]. Bright
contrasts broken nominative _wǣpen_/_wapen_ with unbroken oblique _wǣpnes_,
while Clark Hall lemmatizes the noun under _wapen_ and also preserves unbroken
forms in compounds and related spellings
[@BrightCassidyRingler1971, 29; @ClarkHall1960, 355].

#### Development to Old English

Northwest Germanic lowering gives _wǣpn_, and loss of the final nasal vowel leaves the unbroken cluster word-finally. The Old English form here is the attested unbroken form _wǣpn_.

#### Form note

The ordinary late West Saxon simplex headword is _wǣpen_, but Campbell's
noun-class discussion also preserves unbroken _wépn_ beside broken
_wépen_-type forms [@Campbell1959, 150; @Campbell1959, 226–227]. _wǣpnes_
remains the regular unbroken oblique comparator
[@BrightCassidyRingler1971, 29; @ClarkHall1960, 355].

### will — OE willa

\index[oe]{willa@willa}
\index[pgmc]{weljo@*wéljô}

Derivation: _\*wéljô_ > _willa_ (regular).

#### Derivation trace

Proto input: _\*wéljô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*wélljô} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*willjô} \\
OE Unstressed Long Vowel Shortening & \emph{*willja} \\
OE J Loss After Heavy & \emph{*willa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _willa_

#### Reconstruction and comparative evidence

Kroonen separates noun _\*weljan-_ 2 'will, wish' from verb _\*weljan-_ 1 'to want', while Orel and Kluge represent the noun as _\*weljōn_ [@Kroonen2013; @Orel2003; @KlugeSeebold2011]. The selected derivational form _\*wéljô_ is the noun-side input used for this row.

#### Old English evidence

Clark Hall lemmatizes noun _willa m._ separately from verb _willan_ [@ClarkHall1960, 368]. The Old English form here is the noun citation form, not the related verb.

#### Development to Old English

From _\*wéljô_, j-gemination yields a heavy stem, i-umlaut gives _will-_, and later shortening plus j-loss produce _willa_. The noun is therefore a regular weak masculine outcome.

#### Lexical note

The target here is the noun _willa_ 'will, wish'. Related verb _willan_ belongs to a separate lexeme and should not be substituted for the noun row [@Kroonen2013; @ClarkHall1960, 368].

### wind — OE windan

\index[oe]{windan@windan}
\index[pgmc]{windana@*wíndaną}

Derivation: _\*wíndaną_ > _windan_ (regular).

#### Derivation trace

Proto input: _\*wíndaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*wíndan} \\
OE Secondary Nasalization & \emph{*wíndąn} \\
OE Weak Tail Reduction & \emph{*wíndan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _windan_

#### Reconstruction and comparative evidence

Kroonen distinguishes noun _\*winda-_ from verb _\*windan-_, and the present row belongs to the verb [@Kroonen2013]. Later handbook discussion keeps the dental original from PIE _\*wendh-_, not a Verner alternant [@Fulk2018; @RingeTaylor2014].

#### Old English evidence

Clark Hall and Bosworth-Toller record _windan_ as the verb headword [@ClarkHall1960; @BosworthToller1898, 101]. The Old English form here is the ordinary infinitive of the strong verb.

#### Development to Old English

The form followed here, _\*wíndaną_, yields the regular infinitive _windan_ by ordinary heavy-syllable apocope and weak-tail reduction. The form is therefore a straightforward strong-verb outcome.

#### Lexical note

The note matters because English *wind* also names the noun. This row targets the class-III verb, not the noun [@Kroonen2013; @ClarkHall1960].

### wold — OE weald

\index[oe]{weald@weald}
\index[pgmc]{walthuz@*wálθuz}

Derivation: _\*wálθuz_ > _weald_ (regular).

#### Derivation trace

Proto input: _\*wálθuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc L Th Voicing & \emph{*wálduz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*wáldu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wældu} \\
OE Breaking & \emph{*wealdu} \\
\mbox{OE High Vowel Apocope} & \emph{*weald} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weald_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*walþu-_ and gives OE _weald_ beside other West Germanic _wald_ forms [@Kroonen2013]. The form followed here, _\*wálθuz_, is the nominative singular used for the derivation.

#### Old English evidence

Clark Hall makes _weald_ the main noun headword and cross-refers _wald_ and _wold_ to it [@ClarkHall1960]. The Anglian-looking _wald_ therefore remains variant background rather than the main target.

#### Development to Old English

_\*lþ_ voices to _ld_, Anglo-Frisian brightening yields _wæld-_, and breaking before the cluster gives _weald-_; apocope then yields _weald_. The noun is therefore a regular breaking outcome.

#### Dialect note

The note matters because _wald_ survives as an Anglian-type variant in the same family. The Old English form here is normalized _weald_, not the variant form [@ClarkHall1960; @RingeTaylor2014].

### yarn — OE ġearn

\index[oe]{gearn@ġearn}
\index[pgmc]{garna@*gárną}

Derivation: _\*gárną_ > _ġearn_ (regular).

#### Derivation trace

Proto input: _\*gárną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*gærną} \\
OE Breaking & \emph{*gearną} \\
OE Heavy Syllable Nasal Apocope & \emph{*gearn} \\
OE Velar Palatalization & \emph{*ʤearn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġearn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*garna-_, and Ringe and Taylor give the early chain _\*garna_ > _\*geern_ > _\*gearn_ > OE _gearn_ [@Kroonen2013; @RingeTaylor2014, 220]. The form followed here, _\*gárną_, is the nominal citation form used here, while oblique _\*garnăn_ belongs only to comparative background.

#### Old English evidence

Clark Hall records _gearn (e) n._ 'yarn, spun wool', and Bosworth-Toller glosses _gearn_ as _filatum_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*gárną_, brightening and breaking before _rn_ yield _gearn_; palatalization of initial _g_ before the resulting front-vocalic sequence gives normalized _ġearn_. The derivation is regular.

#### Form note

Dictionary _gearn_ and normalized _ġearn_ refer to the same noun. The comparative stem _\*garna-_ and oblique _\*garnăn_ do not replace the derivational input _\*gárną_.

\clearpage

## Attested variants and comparison forms

These entries treat the attested Old English form as one member of an attested
or historically documented variant set. The lexical comparison must therefore
account for variation rather than for a single unproblematic citation form.

### cud — OE cwedu

\index[oe]{cwedu@cwedu}
\index[pgmc]{kweduz@*kwéðuz}
\index[pgmc]{kwithuz@*kwíθuz}

Derivation: citation reconstruction _\*kwíθuz_; form followed here _\*kwéðuz_ > _cwedu_ (attested variant).

#### Derivation trace

Proto input: _\*kwéðuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*kwéduz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*kwédu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cwedu_

#### Reconstruction and comparative evidence

Kroonen reconstructs the resin word as _\*kwedu-2_ and gives Old English
variants [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form}, [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form}, and [_c(w)udu_]{.iv lang=oe display=c(w)udu sort=cwudu role=comparison_form} [@Kroonen2013, 355]. Orel likewise
lists [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form} under the cognate set [@Orel2003, 266]. The derivational input
[_\*kwéðuz_]{.iv lang=pgmc sort=kweduz role=selected_input}
therefore represents the older e-grade, voiced-dental form behind the chosen
variant [_cwedu_]{.iv lang=oe sort=cwedu role=target_form}.

#### Old English evidence

The Old English word survives in a wider variant set than one dictionary
headword suggests. Ringe and Taylor discuss [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form} > [_cwudu_]{.iv lang=oe sort=cwudu role=comparison_form} > [_cudu_]{.iv lang=oe sort=cudu role=comparison_form} and also
note late West Saxon [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form}; Clark Hall gives [_cwudu_]{.iv lang=oe sort=cwudu role=comparison_form}, [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form}, and [_cudu_]{.iv lang=oe sort=cudu role=comparison_form}
[@RingeTaylor2014, 338; @ClarkHall1960, 84]. Attested _cwedu_ is treated here
as the
conservative variant within that set.

#### Development to Old English

From [_\*kwéðuz_]{.iv lang=pgmc sort=kweduz role=selected_input}, the West Germanic voiced dental hardens in the expected way and
the regular Old English development yields [_cwedu_]{.iv lang=oe sort=cwedu role=target_form}. The other Old English
spellings belong to the same lexical family, but reflect later leveling,
back-umlaut, or further reduction rather than a need to replace the selected
input.

#### Variant comparison

| Variant type | Old English form | Comment |
| :--- | :--- | :--- |
| conservative target | [_cwedu_]{.iv lang=oe sort=cwedu role=target_form} | selected attested variant represented here |
| leveled i-grade form | [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form} | common lexical variant in the same family |
| back-umlauted forms | [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form}, [_cwudu_]{.iv lang=oe sort=cwudu role=comparison_form} | later developments within the same OE tradition |
| reduced form | [_cudu_]{.iv lang=oe sort=cudu role=comparison_form} | further reduced member of the same variant set |

### ten — OE tēon

\index[oe]{teon@tēon}
\index[pgmc]{texun@*téxun}

Derivation: _\*téxun_ > _tēon_ (attested variant).

#### Derivation trace

Proto input: _\*téxun_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*téxon} \\
OE Breaking & \emph{*téoxon} \\
OE H Loss & \emph{*téoon} \\
OE Contraction & \emph{*tḗon} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tēon_

#### Reconstruction and comparative evidence

Fulk states that Old English _tien_ shows umlaut from the inflected forms,
whereas the uninflected form without umlaut is reflected in
_hund-tēon-tig_ [@Fulk2018, §10.2]. Brunner gives the same contrast more
broadly: _tēon_ develops from _\*tëhun_, while West Saxon tien, _tȳn_ belong to
a different, umlauted branch of the numeral history [@SieversBrunner1965,
§§129.2, 129 Anm. 6, 234].

The comparison form _tēon_ therefore represents the bare cardinal's
un-umlauted line, not the later umlauted simplex tradition.

#### Old English evidence

The attested simplex forms are varied. Campbell gives _tien_, north-western
West Saxon _tēn_, and late Northumbrian _tēo_, _tēa_
[@Campbell1959, §682]. Brunner likewise lists West Saxon tien, _tȳn_ beside
_tēn_, _tēo_, _tēa_ in other dialects [@SieversBrunner1965, §325].

Exact simplex _tēon_ is weaker as a directly cited headword than those
spellings. The un-umlauted stem is, however, explicit in _tēoða_ and
_-tēontig_ [@SieversBrunner1965, §129.2; @Fulk2018, §10.2]. The comparison
form _tēon_ is therefore a normalized spelling of that un-umlauted base.

#### Development to Old English

From _\*téxun_, lowering of medial unstressed _u_ gives _\*téxon_,
breaking gives _\*téoxon_, loss of intervocalic _h_/_x_ yields _\*téoon_,
and contraction produces _\*tḗon_, written _tēon_. This is the regular
bare-cardinal path.

The umlauted forms _tien_ / _tīen_ belong to a different branch, created when
the numeral was levelled from inflected forms with a front-vocalic trigger
[@Fulk2018, §10.2; @SieversBrunner1965, §129 Anm. 6].

#### Variant comparison

The comparison below sets the relevant forms side by side. It distinguishes the normalized un-umlauted base
from the attested simplex variants.

| Form or branch | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _tēon_ | normalized un-umlauted comparison form; trace-supported | Old English form here |
| _tien_ / _tīen_ | attested West Saxon umlauted simplex forms | genuine OE variants, but not the bare-cardinal line modeled here |
| _tēn_ / _tēo_ / _tēa_ | attested un-umlauted simplex variants in other dialects | support the same branch as the comparison form |

### three — OE þrīe

\index[oe]{thrie@þrīe}
\index[pgmc]{threjez@*θréjez}

Derivation: _\*θréjez_ > _þrīe_ (attested variant).

#### Derivation trace

Proto input: _\*θréjez_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*θréje} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*θrije} \\
OE Intervocalic J Vocalization & \emph{*θriie} \\
OE Contraction & \emph{*θrīe} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þrīe_

#### Reconstruction and comparative evidence

Kroonen cites the numeral under a broader stem-style reconstruction rather than
under one Old English-ready paradigm cell [@Kroonen2013, 586]. The input
_\*θréjez_ is therefore best understood as the inherited masculine
nominative-accusative singular.

That distinction matters because the Old English numeral does not have one
uniform citation form across the paradigm. The masculine singular line must be
kept apart from feminine-neuter _þrēo_ and from later reduced spellings of
the masculine form.

#### Old English evidence

Campbell gives masculine nominative-accusative _þrīe_, feminine and neuter
nominative-accusative _þrēo_, genitive _þrēora_, and dative
_þrim_, adding that late West Saxon has _þry_, _þri_ for _þrīe_
[@Campbell1959, §683]. Fulk presents the same masculine _þrīe_ beside the
wider numeral paradigm [@Fulk2018, §10.1].

The target is therefore an attested Old English paradigm cell. _þrī_
belongs to later reduction or headword-style citation, whereas _þrīe_ is
the conservative masculine nominative-accusative form.

#### Development to Old English

From _\*θréjez_, loss of final _-z_ leaves a form of the _\*θréje_
type. The following _j_ fronts the stem vowel, then vocalizes between
vowels, and contraction yields _þrīe_. The compact trace records the same
sequence as _\*θrije_ > _\*θriie_ > _þrīe_.

#### Variant comparison

The comparison below sets the relevant forms side by side. It separates the selected masculine cell from
the later reduced form and from the rest of the numeral paradigm.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _þrīe_ | attested masculine nom./acc.; regular output | Old English form here |
| _þrī_ / _þry_ | later reduced masculine variant | genuine OE variant, but not the conservative comparison form |
| _þrēo_ | attested feminine-neuter nom./acc. | same numeral, different paradigm cell |
| _þrēora_, _þrim_ | attested genitive and dative forms | confirm the wider paradigm, not the cell compared here |

### wasp — OE wæfs

\index[oe]{waefs@wæfs}
\index[pgmc]{wabsaz@*wábsaz}

Derivation: _\*wábsaz_ > _wæfs_ (attested variant).

#### Derivation trace

Proto input: _\*wábsaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*wábsa} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*wábs} \\
Anglo Frisian Brightening & \emph{*wæbs} \\
PGmc B Allophony & \emph{*wæβs} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wæfs_

#### Reconstruction and comparative evidence

The Proto-Germanic form _\*wábsaz_ reaches Old English without any special
change of stem or paradigm cell. The question in this entry is instead which
attested Old English member of the variant set should serve as the comparison
form.

Fulk presents the Old English forms together as _wæfs_ with variants _wæsp_ and
_wæps_ [@Fulk2018, §6.5]. Bülbring and Brunner then make the chronology more
explicit by deriving later _wæps_ and late West Saxon _wasp_ from earlier
_waefs_ / _wæfs_ through restricted metatheses [@Bulbring1902, §484 Anm. 3;
@SieversBrunner1965, §§193, 204].

#### Old English evidence

The earliest directly cited Old English form is _wæfs_, written _waefs_ in
the Épinal-Corpus material discussed by Bülbring and Brunner
[@Bulbring1902, §484 Anm. 3; @SieversBrunner1965, §193]. Later Old English also
shows _wæps_ and _wæsp_ / _wasp_, and dictionary practice often favors
_wæps_ or later spellings as headwords [@ClarkHall1960, 341].

This entry therefore distinguishes chronological priority from headword habit.
_wæfs_ is not a convenient reconstruction: it is an attested Old English form
and also the one that matches the regular development most closely.

#### Development to Old English

From _\*wábsaz_, the regular Old English path passes through loss of final _z_,
Anglo-Frisian fronting, and the allophonic development of _b_ to a fricative
before _s_, yielding _wæfs_.

The later forms _wæps_ and _wæsp_ / _wasp_ belong to subsequent, lexically
restricted metatheses. They are genuine Old English forms, but they are later
within the variant history.

#### Variant comparison

The comparison below sets the relevant forms side by side. It separates the earliest attested and regular
form from the later metathesized doublets.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _wæfs_ | earliest attested OE form; regular output | Old English form here |
| _wæps_ | later attested metathesized variant | genuine OE doublet, but secondary |
| _wæsp_ / _wasp_ | later West Saxon metathesized variant | genuine OE doublet, but not the form compared here |

\clearpage

## Early analogy and pre-Old-English input selection

These entries involve a distinction between the lexeme-level citation
reconstruction and the earlier form carried through the Old English derivation.
The issue is upstream of Old English: the form compared here is the
pre-Old-English shape that yields the attested target under the sound
history followed here.

### bottom — OE botm

\index[oe]{botm@botm}
\index[pgmc]{budmaz@*búdmaz}
\index[pgmc]{buttmaz@*búttmaz}

Derivation: citation reconstruction _\*búdmaz_; form followed here _\*búttmaz_ > _botm_ (early analogy).

#### Derivation trace

Proto input: _\*búttmaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bóttmaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*bóttma} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*bóttm} \\
OE Preconsonantal Degemination & \emph{*bótm} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _botm_

#### Reconstruction and comparative evidence

Kroonen reconstructs the word as a stem complex _\*budmō_, gen. _\*buttaz_,
summarized as _\*budman-_ ~ _\*buttman-_, and gives Old English _botm_ as the reflex
[@Kroonen2013, 120]. The comparative label _\*búdmaz_ names the lexeme-level stem
complex, while the derivational input _\*búttmaz_ represents the pre-Old-English
form with oblique _\*butt-_ generalized into the nominative formation.

Orel likewise preserves both sides of the comparison under _\*budmaz_ _\*butmaz_
[@Orel2003, 100]. The derivational input is thus a historical stem choice, not an
arbitrary respelling.

#### Old English evidence

The Old English noun itself is secure. Clark Hall gives _botm_
[@ClarkHall1960, 63]. Bosworth-Toller cross-references _bodan_ to _botm_,
showing the wider reflex family without weakening the attested lemma
[@BosworthToller1898, 112].

#### Development to Old English

Once the oblique _\*butt-_ stem has been generalized, the derivational input
_\*búttmaz_ develops regularly to _botm_. The analogical step is therefore early:
it belongs to pre-Old-English stem formation rather than to a later choice
among Old English paradigm cells.

### brand — OE brandes

\index[oe]{brandes@brandes}
\index[pgmc]{brandas@*brándas}
\index[pgmc]{brandaz@*brándaz}

Derivation: citation reconstruction _\*brándaz_; form followed here _\*brándas_ > _brandes_ (early analogy).

#### Derivation trace

Proto input: _\*brándas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*brándæs} \\
OE Unstressed AE Merger & \emph{*brándes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _brandes_

#### Reconstruction and comparative evidence

The inherited noun is the masculine a-stem [_\*brándaz_]{.iv lang=pgmc sort=brandaz}, continued by Old English
[_brand_]{.iv lang=oe sort=brand} and its continental cognates [@Orel2003, 53]. The selected
input [_\*brándas_]{.iv lang=pgmc sort=brandas} is not a different lexeme but the genitive singular of that
same a-stem noun.

What matters here is therefore not a stem-class disagreement but the difference
between the citation form and a specific inherited inflectional cell. The
derivational input preserves the same root and declension as the headword while
making the oblique ending explicit.

#### Old English evidence

Old English dictionaries lemmatize the noun as [_brand_]{.iv lang=oe sort=brand} [@ClarkHall1960, 49;
@BosworthToller1898, 116]. Bosworth-Toller also records inflectional forms such as
[_brandas_]{.iv lang=oe sort=brandas}, [_branda_]{.iv lang=oe sort=branda}, and [_brandum_]{.iv lang=oe sort=brandum} under the same entry [@BosworthToller1898, 116].

The specific comparison form in this entry, [_brandes_]{.iv lang=oe sort=brandes}, is the expected
genitive singular of that a-stem noun. It is therefore an inferred Old English
paradigm form rather than the ordinary dictionary headword.

#### Development to Old English

From [_\*brándas_]{.iv lang=pgmc sort=brandas}, the regular Old English development passes through the usual
unstressed-vowel weakening of the inflectional ending, yielding [_brandes_]{.iv lang=oe sort=brandes}.
Nothing in the stem itself requires a special repair. The root consonants and
the stressed vowel are the same as in the citation lemma [_brand_]{.iv lang=oe sort=brand}.

The analytical weight of the entry lies in the ending. By choosing the oblique
singular rather than the nominative citation form, the entry presents the same
lexeme in a different inherited cell.

#### Form comparison

The comparison below sets the relevant forms side by side. It separates the citation lemma from the
selected oblique singular.

| Form / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*brándaz_]{.iv lang=pgmc sort=brandaz} | expected OE lemma [_brand_]{.iv lang=oe sort=brand} | [_brand_]{.iv lang=oe sort=brand} | regular headword-level outcome |
| genitive singular | [_\*brándas_]{.iv lang=pgmc sort=brandas} | regular output: [_brandes_]{.iv lang=oe sort=brandes} | [_brandes_]{.iv lang=oe sort=brandes} | exact match for the oblique cell |

The noun itself is straightforwardly inherited. The main point of the entry is
that [_brandes_]{.iv lang=oe sort=brandes} belongs to the same regular a-stem paradigm as [_brand_]{.iv lang=oe sort=brand}, even
though the citation lemma remains the nominative singular.

### breast — OE brēost

\index[oe]{breost@brēost}
\index[pgmc]{breusta@*bréustą}
\index[pgmc]{brustz@*brústz}

Derivation: citation reconstruction _\*brústz_; form followed here _\*bréustą_ > _brēost_ (early analogy).

#### Derivation trace

Proto input: _\*bréustą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*brēostą} \\
OE Heavy Syllable Nasal Apocope & \emph{*brēost} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _brēost_

#### Reconstruction and comparative evidence

The word family shows two related but distinct Proto-Germanic formations. The
root noun [_\*brust-_]{.iv lang=pgmc sort=brust role=source_protoform} lies behind forms such as Gothic [_brusts_]{.iv lang=goth sort=brusts role=comparison_form}, whereas Old
English [_brēost_]{.iv lang=oe sort=breost role=target_form} belongs to a thematic formation [_\*breusta-_]{.iv lang=pgmc sort=breusta role=source_protoform}, alongside Old
Norse [_brjóst_]{.iv lang=on sort=brjost role=comparison_form} and Old Saxon [_briost_]{.iv lang=os sort=briost role=comparison_form} [@Kroonen2013, 114; @Orel2003, 95;
@RingeTaylor2014, 43].

The derivational input [_\*bréustą_]{.iv lang=pgmc sort=breusta role=selected_input} therefore differs from the citation label
[_\*brústz_]{.iv lang=pgmc sort=brustz role=source_protoform} because Old English reflects the thematic branch rather than the root
noun. The morphological choice comes before the Old English sound changes
themselves.

#### Old English evidence

Clark Hall records the noun as [_brēost_]{.iv lang=oe sort=breost role=target_form} / [_breóst_]{.iv lang=oe sort=breost role=comparison_form}
[@ClarkHall1960, 65]. The form is an established Old English
lexeme, not a reconstructed target assembled from comparative evidence alone.

What requires explanation is not the Old English attestation but the relation
between that attested noun and the broader Germanic word family. The relevant
comparison form is therefore the thematic Old English noun [_brēost_]{.iv lang=oe sort=breost role=target_form}.

#### Development to Old English

From [_\*bréustą_]{.iv lang=pgmc sort=breusta role=selected_input}, the regular Old English development gives [_brēost_]{.iv lang=oe sort=breost role=target_form}, with the
expected _eu_ > _ēo_ vowel history [@Campbell1959, §115]. No special repair is needed
once the correct thematic formation is chosen.

The earlier mismatch arose only if the word was forced into the root-noun line.
The Old English noun itself continues the thematic branch cleanly and directly.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the broader root-noun family label
from the thematic formation actually continued in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader root-noun family | [_\*brústz_]{.iv lang=pgmc sort=brustz role=source_protoform} | root-noun type outcomes outside OE | non-OE comparanda | useful family label, but not the direct source of _brēost_ |
| selected thematic formation | [_\*bréustą_]{.iv lang=pgmc sort=breusta role=selected_input} | regular output: _brēost_ | [_brēost_]{.iv lang=oe sort=breost role=target_form} | exact match between formation and attested OE noun |

The relevant point is the formation split. [_brēost_]{.iv lang=oe sort=breost role=target_form} is the regular Old English
outcome of the thematic [_\*breusta-_]{.iv lang=pgmc sort=breusta role=source_protoform} branch, not of the root noun [_\*brust-_]{.iv lang=pgmc sort=brust role=source_protoform}.

### craft — OE cræft

\index[oe]{craeft@cræft}
\index[pgmc]{kraftaz@*kráftaz}
\index[pgmc]{kraftiz@*kráftiz}

Derivation: citation reconstruction _\*kráftiz_; form followed here _\*kráftaz_ > _cræft_ (early analogy).

#### Derivation trace

Proto input: _\*kráftaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*kráfta} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*kráft} \\
Anglo Frisian Brightening & \emph{*kræft} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cræft_

#### Reconstruction and comparative evidence

Comparative sources disagree about the older stem class. Kroonen gives a u-stem
_\*kraftu-_, while Orel prints _\*kraftiz_ ~ _\*kraftuz_ [@Kroonen2013, 340; @Orel2003,
259].
The comparative label _\*kráftiz_ remains in view as a lexeme-level shorthand,
while _\*kráftaz_ is the pre-Old-English form used for the Old English
derivation.

#### Old English evidence

The Old English noun itself is secure. Clark Hall and Bosworth-Toller both give
_cræft_ as the headword [@ClarkHall1960, 19; @BosworthToller1898, 145].

#### Development to Old English

The comparison is between possible pre-Old-English inputs. The i-stem
comparator _\*kráftiz_ gives _creft_, while the u-stem comparator _\*kráftuz_
gives _craft_. The a-stem-shaped input _\*kráftaz_ yields _cræft_ and is
therefore the form used for the Old English derivation. This does not require
treating the comparative dictionaries as identical; it shows the narrower point
that the Old English derivation needs a pre-Old-English form without the
i-umlaut trigger of _\*-iz_ and without the back-vowel outcome associated with
the u-stem comparator.

#### Form comparison

| Candidate input | OE output | Result |
| :--- | :--- | :--- |
| *kráftiz | _creft_ | non-match; i-stem comparator |
| *kráftuz | _craft_ | non-match; u-stem comparator |
| *kráftaz | _cræft_ | exact match; selected pre-OE input |

### dill — OE dile

\index[oe]{dile@dile}
\index[pgmc]{deliz@*déliz}
\index[pgmc]{deljaz@*déljaz}

Derivation: citation reconstruction _\*déljaz_; form followed here _\*déliz_ > _dile_ (early analogy).

#### Derivation trace

Proto input: _\*déliz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*déli} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*dili} \\
OE Med Unstressed I Lowering1 & \emph{*dile} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _dile_

#### Reconstruction and comparative evidence

Comparative evidence preserves both an i-stem and a ja-stem formation, with Old
English [_dile_]{.iv lang=oe sort=dile role=target_form} on one side and continental forms such as Old Saxon [_dilli_]{.iv lang=os sort=dilli role=comparison_form} and
Old High German [_tilli_]{.iv lang=ohg sort=tilli role=comparison_form} on the other [@Fulk2018, 170]. The derivational input
[_\*déliz_]{.iv lang=pgmc sort=deliz role=selected_input} therefore represents the i-stem side of the paradigm,
whereas the citation label [_\*déljaz_]{.iv lang=pgmc sort=deljaz role=source_protoform} is a broader comparative headword.

That stem-class distinction matters for the Old English consonant shape. A
ja-stem with _\*-lj-_ would be expected to produce gemination, but the Old
English noun shows a single _l_. Fulk's discussion of ja-stems transferred to
the i-stems provides the relevant morphological background for the OE side
[@Fulk2018, 170].

#### Old English evidence

Old English dictionaries record the plant name as [_dile_]{.iv lang=oe sort=dile role=target_form}, alongside the variant
[_dili_]{.iv lang=oe sort=dili role=comparison_form} [@BosworthToller1898, 164; @ClarkHall1960, 95]. The form discussed here is
therefore an attested Old English noun with single _l_.

The Old English evidence is the relevant point. Whatever broader comparative
headword is chosen for the family, the inherited form reflected in OE is the
i-stem type [_dile_]{.iv lang=oe sort=dile role=target_form}, not a geminated [_dill_]{.iv lang=oe sort=dill role=comparison_form} outcome.

#### Development to Old English

From [_\*déliz_]{.iv lang=pgmc sort=deliz role=selected_input}, regular loss of final _z_ and the later lowering of unstressed
_i_ yield [_dile_]{.iv lang=oe sort=dile role=target_form}. The stem itself remains ungeminated throughout that path.

The important contrast is negative rather than phonological. If the word were
forced through a ja-stem _\*-lj-_ pathway, the expected result would show _ll_.
The attested Old English noun instead matches the i-stem development.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the stem class actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative ja-stem label | [_\*déljaz_]{.iv lang=pgmc sort=deljaz role=source_protoform} | ja-stem type outcome with gemination | [_dill_]{.iv lang=oe sort=dill role=comparison_form}-type comparison | useful comparative label, but not the OE form |
| selected i-stem formation | [_\*déliz_]{.iv lang=pgmc sort=deliz role=selected_input} | regular output: [_dile_]{.iv lang=oe sort=dile role=regular_output} | [_dile_]{.iv lang=oe sort=dile role=target_form} | exact match between formation and attested OE noun |

The single _l_ is the decisive diagnostic. It identifies [_dile_]{.iv lang=oe sort=dile role=target_form} with the i-stem
formation rather than with the continental ja-stem branch.

### fast — OE festan

\index[oe]{festan@festan}
\index[pgmc]{fastena@*fastēną}
\index[pgmc]{fastijana@*fástijaną}

Derivation: citation reconstruction _\*fastēną_; form followed here _\*fástijaną_ > _festan_ (early analogy).

#### Derivation trace

Proto input: _\*fástijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*fæstijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*fæstijan} \\
OE Secondary Nasalization & \emph{*fæstijąn} \\
Sievers Law Syncope & \emph{*fæstjąn} \\
OE I Umlaut & \emph{*festjąn} \\
OE Weak Tail Reduction & \emph{*festjan} \\
OE J Loss After Heavy & \emph{*festan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _festan_

#### Reconstruction and comparative evidence

Kroonen places the verb within the wider [_\*fastu-_]{.iv lang=pgmc sort=fastu role=source_protoform} adjective family and its
derived [_\*fasten-_]{.iv lang=pgmc sort=fasten role=source_protoform} verbal line, the comparative background behind Old English
'to fast' [@Kroonen2013, 171]. Ringe and Taylor, however, distinguish the Old English verb
more closely: they treat OE 'to fast' as originally a class-I weak verb that
later acquired the stative meaning through lexical confusion [@RingeTaylor2014, 110].

The derivational input [_\*fástijaną_]{.iv lang=pgmc sort=fastijana role=selected_input} therefore represents the inherited class-I
formation reflected in Old English, whereas the citation label [_\*fastēną_]{.iv lang=pgmc sort=fastena role=source_protoform}
belongs to the broader comparative presentation of the lexeme.

#### Old English evidence

Old English dictionaries record forms such as [_festan_]{.iv lang=oe sort=festan role=target_form}, alongside related
[_fæstan_]{.iv lang=oe sort=faestan role=comparison_form} / [_fǣstan_]{.iv lang=oe sort=faestan role=comparison_form} spellings and meanings [@BosworthToller1898, 213]. The form selected here is [_festan_]{.iv lang=oe sort=festan role=target_form}, which fits the regular
class-I phonological development.

The _æ_-forms remain relevant, but they do not control the entry. In the
present analysis they belong to a later analogical reshaping under the
adjective [_fæst_]{.iv lang=oe sort=faest role=comparison_form}, whereas [_festan_]{.iv lang=oe sort=festan role=target_form} is the regular inherited class-I comparison
form.

#### Development to Old English

From [_\*fástijaną_]{.iv lang=pgmc sort=fastijana role=selected_input}, Anglo-Frisian brightening and subsequent i-umlaut produce the
fronted vowel seen in [_festan_]{.iv lang=oe sort=festan role=target_form}. The later weak-tail reductions and loss of _j_
after a heavy syllable complete the regular Old English outcome.

What makes the entry non-regular is not the phonology of [_festan_]{.iv lang=oe sort=festan role=target_form} itself, but
the choice of formation. Old English continues the class-I verb, even though
the comparative headword is often given under the parallel [_\*fastēn-_]{.iv lang=pgmc sort=fasten role=source_protoform} family.

#### Class comparison

The comparison below sets the relevant forms side by side. It distinguishes the comparative class-III
headword from the class-I formation actually reflected in Old English.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative class-III headword | [_\*fastēną_]{.iv lang=pgmc sort=fastena role=source_protoform} | class-III type outcome, not [_festan_]{.iv lang=oe sort=festan role=target_form} | wider family context | useful family label, but not the direct source of the target |
| selected class-I weak verb | [_\*fástijaną_]{.iv lang=pgmc sort=fastijana role=selected_input} | regular output: [_festan_]{.iv lang=oe sort=festan role=regular_output} | [_festan_]{.iv lang=oe sort=festan role=target_form} | exact match between formation and attested OE verb |
| later analogical reshaping | adjective-driven [_fæst_]{.iv lang=oe sort=faest role=comparison_form} influence | [_fæstan_]{.iv lang=oe sort=faestan role=comparison_form} / [_fǣstan_]{.iv lang=oe sort=faestan role=comparison_form} type spellings | fæstan-type evidence | genuine later OE reshaping, but secondary to the Old English form here |

The relevant point is the class split. [_festan_]{.iv lang=oe sort=festan role=target_form} is the regular Old English
outcome of the class-I formation, while the better-known _æ_-forms belong to a
later analogical layer.

### flask — OE flasce

\index[oe]{flasce@flasce}
\index[pgmc]{flasko@*flaskō}
\index[pgmc]{flaskon@*fláskōn}

Derivation: citation reconstruction _\*flaskō_; form followed here _\*fláskōn_ > _flasce_ (early analogy).

#### Derivation trace

Proto input: _\*fláskōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*fláskǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*flæskǭ} \\
OE A Restoration & \emph{*flaskǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*flaskæ} \\
OE Unstressed AE Merger & \emph{*flaske} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _flasce_

#### Reconstruction and comparative evidence

The wider Germanic family is often cited under a form such as [_\*flaskō_]{.iv lang=pgmc sort=flasko role=source_protoform}, but
the evidence relevant for Old English points instead to a weak feminine
formation [_\*fláskōn_]{.iv lang=pgmc sort=flaskon role=selected_input} / [_\*flaskǭ_]{.iv lang=pgmc sort=flasko role=source_protoform} [@Orel2003, 104]. That distinction is
crucial for the suffixal history of the noun.

The derivational input therefore differs from the citation label in stem class. Old
English [_flasce_]{.iv lang=oe sort=flasce role=target_form} belongs with the weak feminine line, and the plural or oblique
forms [_flascan_]{.iv lang=oe sort=flascan role=comparison_form} support that analysis [@RingeTaylor2014, 192].

#### Old English evidence

Old English dictionaries record the noun as [_flasce_]{.iv lang=oe sort=flasce role=target_form}, with inflectional support
from forms such as [_flascan_]{.iv lang=oe sort=flascan role=comparison_form}; a later West Saxon [_flaxe_]{.iv lang=oe sort=flaxe role=comparison_form} is also noted as a
secondary variant [@BosworthToller1898, 235; @ClarkHall1960, 121].

The relevant comparison form is therefore the weak feminine noun [_flasce_]{.iv lang=oe sort=flasce role=target_form}.
The plural and oblique evidence matters because it helps explain why the vowel
and ending are preserved as they are in the singular.

#### Development to Old English

From [_\*fláskōn_]{.iv lang=pgmc sort=flaskon role=selected_input}, the weak feminine passes through the expected loss of _n_ and
the later Old English development of the unstressed ending, reaching [_flasce_]{.iv lang=oe sort=flasce role=target_form}.
Campbell cites restored _a_ in exactly this environment, including [_flasce_]{.iv lang=oe sort=flasce role=target_form}
after inflected [_flascan_]{.iv lang=oe sort=flascan role=comparison_form} [@Campbell1959, §158]. Once the weak feminine
formation is chosen, the noun follows a regular path to its Old English shape.

The decisive issue is morphological rather than phonological. A simple strong
feminine citation form does not capture the OE weak noun as cleanly as the
selected _\*fláskōn_ does.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the weak feminine formation actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader comparative headword | [_\*flaskō_]{.iv lang=pgmc sort=flasko role=source_protoform} | broader family label | wider family context | useful lexeme label, but not the cleanest OE-facing derivation |
| selected weak feminine formation | [_\*fláskōn_]{.iv lang=pgmc sort=flaskon role=selected_input} | regular output: [_flasce_]{.iv lang=oe sort=flasce role=regular_output} | [_flasce_]{.iv lang=oe sort=flasce role=target_form} | exact match between formation and attested OE noun |

The weak feminine suffix is the relevant point. It aligns the inherited form
with attested [_flasce_]{.iv lang=oe sort=flasce role=target_form} and its supporting paradigm forms.

### follow — OE fylġan

\index[oe]{fylgan@fylġan}
\index[pgmc]{fulgena@*fulgēną}
\index[pgmc]{fulgijana@*fúlgijaną}
\index[on]{fylgja@fylgja}

Derivation: citation reconstruction _\*fulgēną_; form followed here _\*fúlgijaną_ > _fylġan_ (early analogy).

#### Derivation trace

Proto input: _\*fúlgijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*fúlgijan} \\
OE Secondary Nasalization & \emph{*fúlgijąn} \\
Sievers Law Syncope & \emph{*fúlgjąn} \\
OE Velar Palatalization & \emph{*fúlʤjąn} \\
OE I Umlaut & \emph{*fylʤjąn} \\
OE Weak Tail Reduction & \emph{*fylʤjan} \\
OE J Loss After Heavy & \emph{*fylʤan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fylġan_

#### Reconstruction and comparative evidence

Kroonen keeps the verb under _\*fulgen-_ and gives Old English [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form}, [_folgian_]{.iv lang=oe sort=folgian role=comparison_form},
adding that Old Norse [_fylgja_]{.iv lang=on sort=fylgja role=comparison_form} and Old English [_fylg(e)an_]{.iv lang=oe display=fylg(e)an sort=fylgean role=comparison_form} continue a formation
_\*fulgjan-_ [@Kroonen2013, 159]. The comparative headword and the class-I formation
are therefore related but not identical.

Ringe and Taylor make the split explicit as PNWGmc _\*fulgija-_ ~ _\*fulgai-_ > OE _fylgan_ ~ _folgian_ and describe it as a dual formation that probably reflects an
older alternation between j-present and e-stative [@RingeTaylor2014, 293-294].
This is a stem-class choice, not a spelling choice. The derivational input
[_\*fúlgijaną_]{.iv lang=pgmc sort=fulgijana role=selected_input} belongs to the class-I _\*fulgija-_ / _\*fulgjan-_ branch; the citation
form [_\*fulgēną_]{.iv lang=pgmc sort=fulgena role=source_protoform} belongs to the parallel class-II history behind [_folgian_]{.iv lang=oe sort=folgian role=comparison_form}.

#### Old English evidence

The Old English evidence preserves both formations. Clark Hall lists [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form}
with variant spellings [_fylgian_]{.iv lang=oe sort=fylgian role=comparison_form} and [_fyligan_]{.iv lang=oe sort=fyligan role=comparison_form} [@ClarkHall1960, 125].
Bosworth-Toller likewise has a separate [_fylgean_]{.iv lang=oe sort=fylgean role=comparison_form} entry
[@BosworthToller1898, 275].

Bright notes traces of the older conjugation in [_fylg(e)an_]{.iv lang=oe display=fylg(e)an sort=fylgean role=comparison_form}
[@BrightCassidyRingler1971, 77] and lists [_folgian_]{.iv lang=oe sort=folgian role=comparison_form} ([_fylgean_]{.iv lang=oe sort=fylgean role=comparison_form}) in the glossary
[@BrightCassidyRingler1971, 364]. The relevant comparison form in this entry is
therefore the class-I verb [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form} / [_fylgean_]{.iv lang=oe sort=fylgean role=comparison_form}, here normalized as [_fylġan_]{.iv lang=oe sort=fylgan role=target_form}.
The spelling with ġ represents the palatalized velar before a front-vocalic
environment.

#### Development to Old English

[_\*fúlgijaną_]{.iv lang=pgmc sort=fulgijana role=selected_input} is a class-I weak-verb formation. In the class-I branch the _\*j_
blocks NWGmc lowering of _u_ to _o_, since Ringe and Taylor formulate that
lowering for environments in which no _\*j_ intervened [@RingeTaylor2014, 96].
The same front-vocalic environment then triggers i-umlaut, so _u_ becomes _y_
[@RingeTaylor2014, §6.6.2].

The subsequent Old English developments are palatalization of the velar,
weak-tail reduction, and loss of _j_ after a heavy syllable, yielding
[_fylġan_]{.iv lang=oe sort=fylgan role=target_form}. This is the regular outcome of the class-I formation. The class-II
form [_folgian_]{.iv lang=oe sort=folgian role=comparison_form} belongs to the parallel _\*-ē-_ / _\*-ai-_ branch and is not the
form modeled here.

#### Class comparison

A class comparison identifies which inherited formation corresponds to the
established Old English form under discussion. The comparison below is manual;
no full automatic class probe is presented here.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation class-II formation | [_\*fulgēną_]{.iv lang=pgmc sort=fulgena role=source_protoform} | probe output: [_folgon_]{.iv lang=oe sort=folgon role=regular_output} | [_folgian_]{.iv lang=oe sort=folgian role=comparison_form} | mismatch: the regular output is not the remodeled infinitive _folgian_ |
| parallel class-II branch | PNWGmc _\*fulgai-_ | Ringe-Taylor: OE [_folgian_]{.iv lang=oe sort=folgian role=comparison_form} | [_folgian_]{.iv lang=oe sort=folgian role=comparison_form} | documents the separate class-II branch, but not the target of this entry |
| selected class-I formation | [_\*fúlgijaną_]{.iv lang=pgmc sort=fulgijana role=selected_input} | regular output: [_fylġan_]{.iv lang=oe sort=fylgan role=regular_output} | [_fylġan_]{.iv lang=oe sort=fylgan role=target_form} / [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form} | exact match between input, output, and class |

The relevant point is the class split. [_fylġan_]{.iv lang=oe sort=fylgan role=target_form} is the regular Old English
outcome of the class-I _\*fulgija-_ / _\*fulgjan-_ formation, whereas [_folgian_]{.iv lang=oe sort=folgian role=comparison_form}
belongs to the parallel class-II branch.

### gall — OE ġealla

\index[oe]{gealla@ġealla}
\index[pgmc]{galla@*gállą}
\index[pgmc]{gallo@*gállô}

Derivation: citation reconstruction _\*gállą_; form followed here _\*gállô_ > _ġealla_ (early analogy).

#### Derivation trace

Proto input: _\*gállô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*gællô} \\
OE Breaking & \emph{*geallô} \\
OE Velar Palatalization & \emph{*ʤeallô} \\
OE Unstressed Long Vowel Shortening & \emph{*ʤealla} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġealla_

#### Reconstruction and comparative evidence

The wider cognate family can be presented under a form such as _\*gállą_, but
the Old English noun itself belongs with a weak noun _\*gallōn-_, cited here as
_\*gállô_ [@Kroonen2013, 165]. The derivational input therefore differs from the broader
comparative headword in stem class.

That stem-class distinction matters directly for the Old English shape. The weak
masculine pathway preserves the ending needed for _ġealla_, whereas a simple
strong-noun headword does not align as closely with the attested OE noun.

#### Old English evidence

Old English dictionaries record the noun as _gealla_, and Bright also gives the
dative _geallan_, confirming a weak-noun paradigm [@BosworthToller1898, 297;
@ClarkHall1960, 145; @BrightCassidyRingler1971, 372]. The form used here, _ġealla_, is
a normalized spelling with macrons omitted and palatal ġ made explicit.

Campbell also notes dialectal variation, contrasting West Saxon or Kentish
_gealla_ with Anglian _galla_ [@Campbell1959, §486]. The target of this entry is the
West Saxon type _ġealla_.

#### Development to Old English

From _\*gállô_, the weak noun develops through the expected Old English history
of the suffix and the regular breaking environment before _ll_, yielding
_ġealla_ [@Campbell1959, §486]. Once the weak masculine input is chosen, the noun
follows a regular path to its attested Old English form.

The decisive issue is therefore morphological. Old English reflects the weak
noun, while the broader family label belongs to a different way of presenting
the cognate set.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the weak noun formation actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader family label | *gállą | broader cognate-set headword | wider family context | useful lexeme label, but not the direct source of _ġealla_ |
| selected weak noun | *gállô | regular output: _ġealla_ | ġealla | exact match between formation and attested OE noun |
| dialectal Anglian continuation | weak noun branch | Anglian _galla_ type | galla | genuine OE variant, but not the West Saxon form used here |

The weak-noun stem class is the relevant point. It gives a direct route to
attested _ġealla_, while the broader comparative label serves only as a family
heading.

### knight — OE cniht

\index[oe]{cniht@cniht}
\index[pgmc]{knextaz@*knéxtaz}
\index[pgmc]{knixtaz@*kníxtaz}

Derivation: citation reconstruction _\*kníxtaz_; form followed here _\*knéxtaz_ > _cniht_ (early analogy).

#### Derivation trace

Proto input: _\*knéxtaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*knéxta} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*knéxt} \\
OE Breaking & \emph{*knéoxt} \\
OE Ws Palatal Umlaut & \emph{*knixt} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cniht_

#### Reconstruction and comparative evidence

The comparative sources align on an _e_-grade reconstruction for this noun.
Ringe and Taylor cite _\*kneht_, and Orel gives [_\*knextaz_]{.iv lang=pgmc sort=knextaz role=selected_input}
[@RingeTaylor2014, 142; @Orel2003, 256]. Kluge-Seebold likewise points to
_\*knehta-_ [@KlugeSeebold2011, 506]. The derivational input [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input} follows that
comparative evidence.

A competing citation reconstruction [_\*kníxtaz_]{.iv lang=pgmc sort=knixtaz role=source_protoform} remains possible as a label for
the word family, but it is not the reconstruction followed here. The Old
English development discussed below is based on [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input}.

#### Old English evidence

Old English dictionaries record the noun as [_cniht_]{.iv lang=oe sort=cniht role=target_form} [@ClarkHall1960, 63;
@BosworthToller1898, 71]. Campbell cites plural [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form} among the broken
forms, showing the same vowel environment from another point in the paradigm
[@Campbell1959, §146].

The target is therefore an ordinary attested Old English noun. No reconstructed
OE comparator is needed here.

#### Development to Old English

From [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input}, the relevant Old English changes include breaking before the
velar cluster and then the later reduction that yields [_cniht_]{.iv lang=oe sort=cniht role=target_form}. Campbell later
notes the early West-Saxon alternation [_cniht_]{.iv lang=oe sort=cniht role=target_form} beside plural [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form}
[@Campbell1959, §305]. Sievers-Brunner gives the same contrast as _cniht ... cneohtas_ [@SieversBrunner1965, §122]. With that corrected input, the
derivation is straightforward.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the handbook-supported _e_-grade
input from a competing citation reconstruction.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing citation reconstruction | [_\*kníxtaz_]{.iv lang=pgmc sort=knixtaz role=source_protoform} | not the reconstruction followed here | broader citation tradition | useful as a competing label, but not the source-based choice used for the OE derivation |
| handbook-supported reconstruction | [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input} | regular output: [_cniht_]{.iv lang=oe sort=cniht role=regular_output} | [_cniht_]{.iv lang=oe sort=cniht role=target_form} | exact match between comparative reconstruction and attested OE noun |
| related plural evidence | same stem family | plural [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form} type background | [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form} | supports the vowel environment, but not the Old English form here cell |

### lade — OE hladan

\index[oe]{hladan@hladan}
\index[pgmc]{lathojana@*laθōjaną}
\index[pgmc]{xladana@*xláðaną}

Derivation: citation reconstruction _\*laθōjaną_; form followed here _\*xláðaną_ > _hladan_ (early analogy).

#### Derivation trace

Proto input: _\*xláðaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*xládaną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xlædaną} \\
OE A Restoration & \emph{*xladaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*xladan} \\
OE Secondary Nasalization & \emph{*xladąn} \\
OE Weak Tail Reduction & \emph{*xladan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hladan_

#### Reconstruction and comparative evidence

Ringe and Taylor cite the strong verb _hladan_ directly [@RingeTaylor2014, 248].
The citation label _\*laθōjaną_ is used here only as a broader family heading,
not as the direct source of the OE derivation.

The derivational input therefore marks an early stem choice. The entry follows the
strong Verner-grade form that reaches Old English _hladan_ directly.

#### Old English evidence

Bosworth-Toller records the verb as _hladan_ and preserves the expected
strong-verb paradigm material around it [@BosworthToller1898, 559]. Clark Hall
likewise records _hladan_ [@ClarkHall1960, 159].
The target is an attested infinitive rather than a reconstructed paradigm cell.

For this entry the relevant comparison form is the infinitive _hladan_ itself.
The question is how that attested strong verb relates to the broader comparative
family.

#### Development to Old English

From _\*xláðaną_, the verb passes through the expected early voiced stop stage,
Anglo-Frisian brightening, and the later A-restoration that returns the root
vowel to _a_ before the full infinitival ending. Campbell treats verbs such as
_hladan_ as showing restored _a_ in the present system [@Campbell1959, §744].
Ringe and Taylor likewise derive _hladan_ from the voiced strong-verb line
[@RingeTaylor2014, 248]. The resulting Old English infinitive is _hladan_.

#### Class comparison

The comparison below sets the relevant forms side by side. It separates the wider weak-verb family label
from the strong verb actually reflected in Old English.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative weak-verb label | *laθōjaną | wider family background | broader family context | useful family label, but not the direct source of _hladan_ |
| selected strong Verner-grade input | *xláðaną | regular output: _hladan_ | hladan | exact match between formation and attested OE infinitive |

### lap — OE lappa

\index[oe]{lappa@lappa}
\index[pgmc]{labbaz@*lábbaz}
\index[pgmc]{lappo@*láppô}

Derivation: citation reconstruction _\*lábbaz_; form followed here _\*láppô_ > _lappa_ (early analogy).

#### Derivation trace

Proto input: _\*láppô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*læppô} \\
OE A Restoration & \emph{*lappô} \\
OE Unstressed Long Vowel Shortening & \emph{*lappa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lappa_

#### Reconstruction and comparative evidence

The comparative sources point to a weak noun with _pp_: Orel gives _\*lappōn_,
and the Old English dictionary tradition preserves variant _læppa_
[@Orel2003, 236; @ClarkHall1960, 180]. The derivational input _\*láppô_
follows that evidence.

A competing comparative label _\*lábbaz_ has also circulated for the word
family, but the cited handbooks do not make it the direct source of the Old
English weak noun. The form relevant to the OE development is the weak
masculine input _\*láppô_.

#### Old English evidence

Campbell cites _lappa_ as a case of restored _a_
[@Campbell1959, §158]. Sievers-Brunner records _lappa_ beside variant _læppa_
[@SieversBrunner1965, §10]. The dictionary tradition also preserves _læppa_
[@ClarkHall1960, 180; @BosworthToller1898, 613].

The target of this entry is the restored singular _lappa_. The variant _læppa_
and the oblique or plural _leappan_ remain part of the Old English record and
help frame the noun's vowel history.

#### Development to Old English

Campbell explicitly lists _lappa_ among the forms with restored _a_
[@Campbell1959, §158]. Sievers-Brunner records _lappa_ beside variant _læppa_
at the same Old English stage [@SieversBrunner1965, §10]. With the weak
masculine input chosen, the selected _lappa_ outcome is therefore the regular
project comparison.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the weak masculine formation from
a competing voiced comparative label.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing voiced comparative label | *lábbaz | not the form followed for the OE weak-noun derivation | broader comparative background | useful as a competing label, but not the source-based choice used here |
| selected weak masculine noun | *láppô | regular output: _lappa_ | lappa | exact match between formation and attested OE noun |
| attested OE variant line | same noun family | _læppa_, _leappan_ | læppa / leappan | useful control forms within the same OE tradition |

### laugh — OE hliehhan

\index[oe]{hliehhan@hliehhan}
\index[pgmc]{lakana@*lákaną}
\index[pgmc]{xlaxjana@*xláxjaną}

Derivation: citation reconstruction _\*lákaną_; form followed here _\*xláxjaną_ > _hliehhan_ (early analogy).

#### Derivation trace

Proto input: _\*xláxjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.470\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.470\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*xláxxjaną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xlæxxjaną} \\
OE Breaking & \emph{*xleaxxjaną} \\
OE Velar Fricative Palatalization & \emph{*xleaxçjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*xleaxçjan} \\
OE Secondary Nasalization & \emph{*xleaxçjąn} \\
OE I Umlaut & \emph{*xliexçjąn} \\
OE Weak Tail Reduction & \emph{*xliexçjan} \\
OE J Loss After Heavy & \emph{*xliexçan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hliehhan_

#### Reconstruction and comparative evidence

The wider Germanic family includes a non-j branch represented here by the
citation label _\*lákaną_, while the derivational input _\*xláxjaną_ reflects the
j-present line behind Old English _hliehhan_.

This branch choice matters because it brings with it the geminate fricative and
the vowel development characteristic of the Old English verb. The comparative
family label and the OE-facing input are therefore related but not identical.

#### Old English evidence

Bosworth-Toller records _hlihhan_ as the verb 'to laugh'
[@BosworthToller1898, 551]. Clark Hall cross-references _hlæhan_,
_hlehhan_, and _hlihhan_ to _hliehhan_ [@ClarkHall1960, 160-161]. Bright's
glossary likewise gives _hlihhan (hliehhan, hlyhhan)_
[@BrightCassidyRingler1971, 315]. The target of this entry is the West Saxon
_hliehhan_.

The variant set matters as background, but the argument of the entry rests on
the attested lemma _hliehhan_ itself.

#### Development to Old English

From _\*xláxjaną_, West Germanic j-gemination yields the doubled consonant
[@Campbell1959, §407]. Ringe and Taylor derive Old English _hliehhan_ from the
j-present branch via breaking before the palatalized geminate
[@RingeTaylor2014, 240]. They separately compare the related noun _hleahtor_
as the outcome of _\*hlahtraz_ [@RingeTaylor2014, 328].

#### Branch comparison

The comparison below sets the relevant forms side by side. It separates the wider non-j family label from
the j-present branch actually reflected in Old English.

| Formation / branch | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| wider non-j family | *lákaną | comparative background outside the selected OE line | wider family context | useful family label, but not the direct source of _hliehhan_ |
| selected j-present branch | *xláxjaną | regular output: _hliehhan_ | hliehhan | exact match between branch and attested OE lemma |
| attested OE variants | same OE verb line | _hlæhhan_, _hlehhan_ | hlæhhan / hlehhan | genuine variant evidence, but secondary to the form compared here |

### loam — OE lām

\index[oe]{lam@lām}
\index[pgmc]{laima@*láimą}
\index[pgmc]{laimon@*laimōn}

Derivation: citation reconstruction _\*laimōn_; form followed here _\*láimą_ > _lām_ (early analogy).

#### Derivation trace

Proto input: _\*láimą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*lāmą} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*lām} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lām_

#### Reconstruction and comparative evidence

The inherited comparative noun is given as _\*laimōn_ or _\*laiman-_, and both
Orel and Kroonen identify Old English _lām_ as a neuter reflex of that family
[@Orel2003, 272; @Kroonen2013, 363]. The form followed here, _\*láimą_, differs from the
comparative headword because it represents the stem class that matches the Old
English noun most directly.

This is therefore a class shift within the history of the English branch rather
than a dispute about the OE target itself.

#### Old English evidence

Old English dictionaries record the noun as _lām_, a neuter word for 'loam,
clay, mud' [@BosworthToller1898, 604; @ClarkHall1960, 196]. The target is an attested
citation form rather than a reconstructed comparator.

The relevant question is not whether _lām_ is Old English, but which inherited
formation best accounts for that attested neuter noun.

#### Development to Old English

From _\*láimą_, regular monophthongization of _ai_ and the later loss of the
final nasal syllable yield _lām_. With that OE-facing input, the phonological
development is straightforward.

#### Class comparison

The comparison below sets the inherited comparative n-stem label beside the
OE-facing stem class used to derive the attested noun.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| inherited comparative noun | *laimōn | comparative family background | wider family context | useful headword, but not the direct OE-facing input |
| OE-facing stem class followed here | *láimą | regular output: _lām_ | lām | exact match between the form followed here and the attested OE noun |

### lung — OE lungen

\index[oe]{lungen@lungen}
\index[pgmc]{lunganjo@*lúnganjō}
\index[pgmc]{lungo@*lungō}

Derivation: citation reconstruction _\*lungō_; form followed here _\*lúnganjō_ > _lungen_ (early analogy).

#### Derivation trace

Proto input: _\*lúnganjō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.470\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.470\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*lúngannjō} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
NWGmc Final Long O Raising & \emph{*lúngannju} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*lúngennju} \\
OE High Vowel Apocope & \emph{*lúngennj} \\
OE J Loss After Heavy & \emph{*lúngenn} \\
OE Final Geminate Simplification & \emph{*lúngen} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lungen_

#### Reconstruction and comparative evidence

Kroonen treats the basic noun as _\*lungōn-_ and also cites an OE-facing
derivative _\*lungunjō-_, continued by Old English _lungen_ and close West
Germanic cognates [@Kroonen2013, 384]. The form followed here, _\*lúnganjō_, models that
derived feminine formation rather than the base noun. The notation differs
slightly from Kroonen's _\*lungunjō-_, but both point to the same derived
feminine line.

The difference between the citation label and the derivational input is therefore
derivational. Old English _lungen_ is not a direct reflex of the bare base noun
_\*lungō_; it belongs to an expanded feminine formation.

#### Old English evidence

Old English dictionaries record the noun as _lungen_, with inflected forms such
as _lungenne_ and _lungena_ [@BosworthToller1898, 634]. Clark Hall also preserves a
small family of compounds such as _lungenādl_, _lungensealf_, and _lungenwyrt_
[@ClarkHall1960, 191].

The target is an attested Old English lexeme with its own paradigm, not a
rescued inflectional cell.

#### Development to Old English

From the selected derived input, the expected derivational consonant and vowel
adjustments lead to _lungen_. Once the expanded feminine formation is chosen,
the Old English outcome is regular.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the base noun from the derived
feminine formation reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| base noun | *lungō | base-noun outcome without the OE derivative suffix | broader family context | useful headword, but not the direct source of _lungen_ |
| derived OE-facing formation | *lúnganjō | regular output: _lungen_ | lungen | exact match between the derived formation and the attested OE noun |
| Kroonen's cited derivative | _\*lungunjō-_ | comparative support for the same OE-facing formation | lungen and cognate set | supports the derived feminine formation, with notation differing from the normalized input form used here |

### navel — OE nafola

\index[oe]{nafola@nafola}
\index[pgmc]{nablo@*nablô}
\index[pgmc]{nabulo@*nábulô}

Derivation: citation reconstruction _\*nablô_; form followed here _\*nábulô_ > _nafola_ (early analogy).

#### Derivation trace

Proto input: _\*nábulô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*nábolô} \\
Anglo Frisian Brightening & \emph{*næbolô} \\
OE A Restoration & \emph{*nabolô} \\
PGmc B Allophony & \emph{*naβolô} \\
OE Unstressed Long Vowel Shortening & \emph{*naβola} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nafola_

#### Reconstruction and comparative evidence

Kroonen instead gives a nasal-suffix navel formation with Old English [_nafela_]{.iv lang=oe sort=nafela role=comparison_form}
among its reflexes [@Kroonen2013, 420], while Ringe and Taylor give the
derivational pathway _\*nabulō_ > _\*næbula_ > _nafola_ [@RingeTaylor2014, 270]. The
difference is one of stage and notation rather than of lexeme identity: the
derivational input [_\*nábulô_]{.iv lang=pgmc sort=nabulo role=selected_input} is the pre-syncope form needed for the Old English
development.

For the Old English comparison, the crucial point is simply that the pre-OE form
still contains a medial vowel.

#### Old English evidence

Ringe and Taylor note the early West Saxon shift [_nafola_]{.iv lang=oe sort=nafola role=target_form} > [_nafela_]{.iv lang=oe sort=nafela role=comparison_form}
[@RingeTaylor2014, 336]. Campbell likewise records _nafela_ beside Corpus
[_nabula_]{.iv lang=oe sort=nabula role=comparison_form} [@Campbell1959, §159]. The target of this entry is the nominative
singular [_nafola_]{.iv lang=oe sort=nafola role=target_form}, the form that matches the selected derivational pathway
most directly.

[_nafela_]{.iv lang=oe sort=nafela role=comparison_form} is the better-known later West Saxon spelling, while [_nabula_]{.iv lang=oe sort=nabula role=comparison_form} preserves
a less reduced medial vowel. These forms belong to the same lexical history, but
this entry is centered on [_nafola_]{.iv lang=oe sort=nafola role=target_form}.

#### Development to Old English

Ringe and Taylor give the pre-OE line _\*nabulō_ > _\*næbula_ > OE _nafola_
[@RingeTaylor2014, 270]. The trace represents that same development with
stress-marked notation and explicit intermediate weakening. Intervocalic _b_
then surfaces as _f_, and final weak-tail shortening gives _nafola_.

The medial vowel is still present when A-restoration applies. That is why the
selected pre-syncope input differs from the syncopated comparative headword.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the comparative citation form from
the pre-syncope input and from the later OE spellings.

| Formation / stage | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| syncopated comparative headword | [_\*nablô_]{.iv lang=pgmc sort=nablo role=source_protoform} | reduced _næfla_-type outcome rather than [_nafola_]{.iv lang=oe sort=nafola role=target_form} | not the Old English form here | useful citation form, but too reduced for the pathway modeled here |
| selected pre-syncope input | [_\*nábulô_]{.iv lang=pgmc sort=nabulo role=selected_input} | regular output: [_nafola_]{.iv lang=oe sort=nafola role=regular_output} | [_nafola_]{.iv lang=oe sort=nafola role=target_form} | exact match between derivational input and target |
| later OE reduction stages | same lexical history | attested [_nafela_]{.iv lang=oe sort=nafela role=comparison_form}; Corpus [_nabula_]{.iv lang=oe sort=nabula role=comparison_form} | [_nafela_]{.iv lang=oe sort=nafela role=comparison_form} / [_nabula_]{.iv lang=oe sort=nabula role=comparison_form} | related OE spellings, but not the chosen comparator |

### neck — OE hnecca

\index[oe]{hnecca@hnecca}
\index[pgmc]{xnakkaz@*xnákkaz}
\index[pgmc]{xnekko@*xnékkô}

Derivation: citation reconstruction _\*xnákkaz_; form followed here _\*xnékkô_ > _hnecca_ (early analogy).

#### Derivation trace

Proto input: _\*xnékkô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*xnékka} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hnecca_

#### Reconstruction and comparative evidence

The noun belongs to an ablauting n-stem family. Kroonen reconstructs a paradigm
with nominative _\*hnekkō_, genitive _\*hnukkaz_, and accusative plural
_\*hnakkuns_, and he places Old English _hnecca_ among the e-grade descendants
[@Kroonen2011, 167]. Kluge-Seebold likewise identifies _ae. hnecca_ as an ablaut
partner of the a-grade _Nacken_ family [@KlugeSeebold2011, 347].

A competing comparative label [_\*xnákkaz_]{.iv lang=pgmc sort=xnakkaz role=source_protoform} remains useful for the wider family, and
Orel also gives an a-grade headword line [@Orel2003, 218]. The derivational input
[_\*xnékkô_]{.iv lang=pgmc sort=xnekko role=selected_input}, however, is the form that matches the Old English branch.

#### Old English evidence

Clark Hall records the weak masculine noun _hnecca_ [@ClarkHall1960, 162].
Bosworth-Toller likewise records _hnecca_ [@BosworthToller1898, 567]. The target is therefore an attested
citation form, not an oblique cell or a reconstructed lemma.

The phonological question is upstream of the Old English evidence. The attested
noun already shows that the branch continued an e-grade form rather than the
a-grade seen in much of the continental material.

#### Development to Old English

From [_\*xnékkô_]{.iv lang=pgmc sort=xnekko role=selected_input}, the derivation is straightforward. The trace shortens the final
long vowel to _\*xnékka_, and Old English orthography gives [_hnecca_]{.iv lang=oe sort=hnecca role=target_form}.

The derivation depends on the earlier selection of the e-grade weak-noun form
continued by Old English.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the wider a-grade family from the
selected e-grade Old English branch.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing comparative label | [_\*xnákkaz_]{.iv lang=pgmc sort=xnakkaz role=source_protoform} | broader a-grade family rather than the selected OE source | continental [_Nacken_]{.iv lang=german sort=nacken role=comparison_form} line | useful family label, but not the input followed for the Old English derivation |
| weak noun with a-grade | [_\*xnakkô_]{.iv lang=pgmc sort=xnakko role=comparison_form} | expected [_hnacca_]{.iv lang=oe sort=hnacca role=comparison_form} type outcome | [_hnacca_]{.iv lang=oe sort=hnacca role=comparison_form} | fixes the class, but not the vowel grade |
| selected e-grade nominative | [_\*xnékkô_]{.iv lang=pgmc sort=xnekko role=selected_input} | regular output: [_hnecca_]{.iv lang=oe sort=hnecca role=regular_output} | [_hnecca_]{.iv lang=oe sort=hnecca role=target_form} | exact match between derivational input and attested OE noun |
| oblique paradigm background | [_\*hnukkaz_]{.iv lang=pgmc sort=hnukkaz role=comparison_form}, [_\*hnakkuns_]{.iv lang=pgmc sort=hnakkuns role=comparison_form} | ON/OHG/German a-grade continuation | [_hnakki_]{.iv lang=on sort=hnakki role=comparison_form} / [_Nacken_]{.iv lang=german sort=nacken role=comparison_form} | shows the wider ablaut family, but not the chosen OE branch |

### needle — OE nǣdl

\index[oe]{naedl@nǣdl}
\index[pgmc]{nedlo@*nḗðlō}
\index[pgmc]{nethlo@*nḗθlō}

Derivation: citation reconstruction _\*nḗθlō_; form followed here _\*nḗðlō_ > _nǣdl_ (early analogy).

#### Derivation trace

Proto input: _\*nḗðlō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*nḗdlō} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*nḗdlu} \\
\mbox{NWGmc Long E Lowering} & \emph{*nǣdlu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*nǣdl} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nǣdl_

#### Reconstruction and comparative evidence

Ringe and Taylor treat the word as a voiced/voiceless alternant, citing
PGmc _\*nēþlō_, _\*nēdlō-_ 'needle' ... > OE _nédl_ [@RingeTaylor2014, 329]. The
form followed here, [_\*nḗðlō_]{.iv lang=pgmc sort=nedlo role=selected_input}, is the voiced Verner-grade form used for the Old
English comparison, while the citation form [_\*nḗθlō_]{.iv lang=pgmc sort=nethlo role=source_protoform} remains the broader
lexeme label.

The development discussed here follows the Ringe-Taylor alternant framework.

#### Old English evidence

Clark Hall records the attested citation form _nǣdl_ [@ClarkHall1960, 210].
Campbell lists _nédl_ among the expected unbroken forms after _t_ and _d_
[@Campbell1959, §367]. Hogg also includes _nidi_ / _nǣdl_ in the same broader
cluster history [@Hogg1992, 95].

The target is therefore an attested citation form. No oblique-cell substitution
is involved in this entry.

#### Development to Old English

Ringe and Taylor give the historical line _\*nēþlō_, _\*nēdlō-_ ... > OE _nédl_
[@RingeTaylor2014, 329]. Campbell likewise lists _nédl_ among the expected
unbroken forms after _t_ and _d_ [@Campbell1959, §367]. The trace expresses the
same pathway with the voiced alternant followed here for the Old English comparison.

The essential choice lies in which Proto-Germanic alternant is taken as the
starting point. Once the voiced form is chosen, the rest of the pathway is
regular.

#### Alternant comparison

The comparison below sets the relevant forms side by side. It separates the broader citation headword from
the voiced alternant used for Old English.

| Formation / stage | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative voiceless headword | [_\*nḗθlō_]{.iv lang=pgmc sort=nethlo role=source_protoform} | broader word-family label rather than the OE-facing alternant | _\*nēþlō_ line | useful citation form, but not the derivational input for the Old English comparison |
| voiced Verner alternant followed here | [_\*nḗðlō_]{.iv lang=pgmc sort=nedlo role=selected_input} | regular output: [_nǣdl_]{.iv lang=oe sort=naedl role=regular_output} | [_nǣdl_]{.iv lang=oe sort=naedl role=target_form} | exact match between the form followed here and the attested OE noun |
| later hardening stage | *nḗdlō | intermediate pre-OE stage in the same derivation | nǣdl | genuine stage in the pathway, but not the Proto-Germanic form followed here |

### nose — OE nosu

\index[oe]{nosu@nosu}
\index[pgmc]{naso@*nasō}
\index[pgmc]{nuso@*núsō}

Derivation: citation reconstruction _\*nasō_; form followed here _\*núsō_ > _nosu_ (early analogy).

#### Derivation trace

Proto input: _\*núsō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*nósō} \\
\mbox{NWGmc Final Long O Raising} & \emph{*nósu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nosu_

#### Reconstruction and comparative evidence

Kroonen reconstructs a Germanic ablaut pair _\*nasō-_ ~ _\*nusō-_ and adds that the
root _\*nus-_ is likely to have arisen as a secondary zero grade after a
remodeling of the older paradigm [@Kroonen2013, 423]. Campbell is more specific for
Old English, citing _nosu_ < _\*nusō_ [@Campbell1959, 44].

The citation reconstruction _\*nasō_ is therefore best treated as the full-grade
comparative headword, while the derivational input _\*núsō_ represents the remodeled
zero-grade line continued by the Old English form discussed here. Orel's _\*nasō_ ... OE _nasu_ preserves the competing full-grade notation and shows that the two
lines should not be collapsed without comment [@Orel2003, 320].

#### Old English evidence

_Nosu_ is an attested Old English noun. Ringe and Taylor list it among the few
surviving early Old English feminine u-stems [@RingeTaylor2014, 385]. Clark Hall
likewise gives _nosu f._, with genitive-dative singular _nosa_, and cross-refers
_nasu_ to _nosu_ [@ClarkHall1960, 810].

The selected OE target is therefore an attested _nosu_, not a reconstructed
placeholder. At the same time, the lexicographical record keeps _nasu_ visible as
a parallel notation belonging to the full-grade side of the tradition.

#### Development to Old English

From _\*núsō_, the regular path is the one documented by the current trace:
_\*núsō_ > _\*nósō_ > _\*nósu_ > _nosu_. The early special step lies in the choice of the
zero-grade input, not in any late Old English repair.

With that input chosen, the OE development is straightforward. The full-grade
line behind _\*nasō_ instead points toward _nasu_, not to the form treated here.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the full-grade comparative line
from the remodeled zero-grade input that yields the Old English form.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| full-grade comparative line | *nasō | expected full-grade continuation _nasu_ | nasu | useful comparative background, but not the Old English-facing input |
| remodeled zero-grade line | *núsō | regular output: _nosu_ | nosu | exact match between derivational input and attested OE noun |

### sap — OE sæp

\index[oe]{saep@sæp}
\index[pgmc]{sapa@*sápą}
\index[pgmc]{sapon@*sapōn}

Derivation: citation reconstruction _\*sapōn_; form followed here _\*sápą_ > _sæp_ (early analogy).

#### Derivation trace

Proto input: _\*sápą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*sæpą} \\
OE Heavy Syllable Nasal Apocope & \emph{*sæp} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sæp_

#### Reconstruction and comparative evidence

The comparative sources do not give one uniform inherited stem. Kroonen
preserves the word family as _\*saf_/ppan-, with Old English _sæp_ m.
[@Kroonen2013, 420]. Orel preserves the comparative notation _\*sapōn_ ~ _\*sapan_
[@Orel2003, 319].

The form followed here, _\*sápą_, therefore does not replace those comparative labels.
It identifies the OE-facing stem shape that yields the attested noun treated
here.

#### Old English evidence

Clark Hall records _sæp_ (e) n. [@ClarkHall1960, 247]. The target is therefore
an attested neuter Old English noun. Orel's plain _sap_ notation belongs to
comparative normalization, not to the spelling adopted here for the Old English
form [@Orel2003, 319].

#### Development to Old English

From _\*sápą_, Anglo-Frisian brightening yields _sæ_, and heavy-syllable nasal
apocope then produces _sæp_. That is the regular path documented by the current
trace.

The competing comparative lines do not give the same result. The inherited
n-stem notation _\*sapōn_ yields _sape_, while an i-stem continuation from the
_\*sapi-_ line leads to _sep_ / _sepe_ rather than to _sæp_. The special step in
this entry is therefore the early stem choice, not a late OE paradigm-cell
selection.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the competing comparative stem lines
from the Old English-facing input.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative n-stem line | *sapōn | local comparator output: _sape_ | sape | useful comparative background, but not the source of attested _sæp_ |
| inferred i-stem comparator from _\*sapi-_ | *sapiz | local comparator output: _sepe_ | sepe | confirms that an i-triggering stem does not reach the target |
| selected a-stem input | *sápą | regular output: _sæp_ | sæp | exact match between derivational input and attested OE noun |

### sea — OE sǣ

\index[oe]{sae@sǣ}
\index[pgmc]{sai@*sái}
\index[pgmc]{saiwiz@*sáiwiz}

Derivation: citation reconstruction _\*sái_; form followed here _\*sáiwiz_ > _sǣ_ (early analogy).

#### Derivation trace

Proto input: _\*sáiwiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*sāwiz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*sāwi} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE W Loss Before I & \emph{*sāi} \\
OE I Umlaut & \emph{*sǣi} \\
\mbox{OE High Vowel Apocope} & \emph{*sǣ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sǣ_

#### Reconstruction and comparative evidence

Kroonen gives the noun in stem notation as _\*saiwi-_, an i-stem whose English
reflex is cited as OE _sæ_ [@Kroonen2013, 423]. Ringe and Taylor write the fuller
form _\*saiwiz_ and derive it through _\*sawi_ > _\*sei_ > OE _sǣ_
[@RingeTaylor2014, §6.7.1]. The comparative headword is therefore shorter than
the form required for the English history: _\*sái_ names the lexeme, but
_\*sáiwiz_ preserves the medial _\*w_ and the final high vowel that control the
later development.

#### Old English evidence

The Old English noun is the ordinary word for ‘sea’. Kroonen cites it as _sæ_;
the normalized form here is _sǣ_ [@Kroonen2013, 423]. Campbell likewise treats
_sea_ as continuing the same _\*saiui-_ > _\*sǣi_ history, with loss of _u_/_w_
before _i_ [@Campbell1959, §406].

#### Development to Old English

Once the fuller i-stem input is chosen, the development is regular. After
Proto-West-Germanic monophthongization _\*sáiwiz_ > _\*sāwiz_ and final _\*-z_ loss
_\*sāwiz_ > _\*sāwi_, the non-initial _\*w_ disappears before unstressed _\*i_, and
the following high vowel fronts the root vowel before final apocope. The
documented chain is _\*sáiwiz_ > _\*sāwiz_ > _\*sāwi_ > _\*sāi_ > _\*sǣi_ > _sǣ_
[@RingeTaylor2014, §6.7.1; @Campbell1959, §406].

#### Stem and stage comparison

The comparison below sets the relevant forms side by side. It separates the abbreviated comparative
headword from the fuller i-stem input that yields the Old English form.

| Formation / label | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| abbreviated comparative headword | *sái | too short to preserve the _\*w_ ... _\*i_ environment needed for the documented chronology | sǣ | useful comparative label, but not the Old English-facing input |
| selected i-stem input | *sáiwiz | documented regular output: _sǣ_ | sǣ | exact match between derivational input and Old English target |

### sieve — OE sife

\index[oe]{sife@sife}
\index[pgmc]{sibaz@*síbaz}
\index[pgmc]{sibi@*síbi}

Derivation: citation reconstruction _\*síbaz_; form followed here _\*síbi_ > _sife_ (early analogy).

#### Derivation trace

Proto input: _\*síbi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PGmc B Allophony & \emph{*síβi} \\
OE Med Unstressed I Lowering1 & \emph{*síβe} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sife_

#### Reconstruction and comparative evidence

Kluge-Seebold gives wg. _\*sibi-_ n. ... ae. sife, and Campbell groups _sife_
with short neuter i-stems such as _spere_ [@KlugeSeebold2011, 847;
@Campbell1959, §609]. The older morphological background is the s-stem
_\*sib-iz_, but the derivational input is the normalized i-stem form _\*síbi_.

Kroonen's nearby _\*sebjō-_ entry belongs to the separate kinship lexeme that
yields Old English _sibb_, not to the sieve word. Orel's _\*sibaz_ ... OE _sife_
preserves a broader handbook notation, but that a-stem shape does not fit the
Old English form treated here [@Orel2003, 328].

#### Old English evidence

Clark Hall gives _sibi (GL) ... = sife_ and also _sife n. ‘sieve’_
[@ClarkHall1960, 263]. Campbell likewise cites Corpus Glossary _sibi_ and
treats _sife_ as a short neuter i-stem [@Campbell1959, §§444, 609]. The
normalized Old English target is therefore _sife_, while _sibi_ is an attested
earlier spelling rather than a separate lexeme.

#### Development to Old English

From _\*síbi_, the regular derivation gives _\*síβi_ > _\*síβe_ > _sife_. Medial _b_
is realized as a spirant and later written _f_, while the final unstressed _i_
lowers to _e_. The older s-stem background _\*sib-iz_ explains the morphology,
but the derivational input _\*síbi_ is the immediate pre-Old-English form.

#### Stem comparison

The comparison below sets the relevant forms side by side. It distinguishes the accepted i-stem line from
its rejected competitors.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| ja-stem kinship line | Kroonen _\*sebjō-_ / comparator _\*sibja_ | OE _sibb_ | sibb | separate lexeme, not the target treated here |
| a-stem handbook line | *síbaz | expected _sif_ | sif | wrong ending for the attested noun |
| selected i-stem line from older _\*sib-iz_ | *síbi | documented regular output: _sife_ | sife; early spelling _sibi_ | exact match between derivational input and Old English evidence |

### spare — OE sparian

\index[oe]{sparian@sparian}
\index[pgmc]{sparena@*sparēną}
\index[pgmc]{sparojana@*spárōjaną}

Derivation: citation reconstruction _\*sparēną_; form followed here _\*spárōjaną_ > _sparian_ (early analogy).

#### Derivation trace

Proto input: _\*spárōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*spærōjaną} \\
OE A Restoration & \emph{*sparōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*sparōjan} \\
OE Secondary Nasalization & \emph{*sparōjąn} \\
OE I Umlaut & \emph{*sparējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*sparejąn} \\
OE Weak Tail Reduction & \emph{*sparejan} \\
OE Intervocalic J Vocalization & \emph{*spareian} \\
OE Unstressed EI Contraction & \emph{*sparian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sparian_

#### Reconstruction and comparative evidence

Kroonen keeps the inherited verb under class-III [_\*sparēn-_]{.iv lang=pgmc sort=sparen}
[@Kroonen2013, 465]. Orel similarly preserves [_\*sparēnan_]{.iv lang=pgmc sort=sparenan} [@Orel2003, 362]. Ringe
and Taylor, however, reconstruct [_\*sparai-_]{.iv lang=preoe sort=sparai} ~ [_\*sparja-_]{.iv lang=preoe sort=sparja} for the English branch
and derive the citation verb from a class-II line [@RingeTaylor2014, 162, 191].
The derivational input [_\*spárōjaną_]{.iv lang=pgmc sort=sparojana} therefore represents the refashioned class-II
formation behind Old English [_sparian_]{.iv lang=oe sort=sparian}, while the citation reconstruction
[_\*sparēną_]{.iv lang=pgmc sort=sparena} remains the inherited comparative headword.

#### Old English evidence

Campbell says that [_sparian_]{.iv lang=oe sort=sparian} does not show the ordinary class-III
characteristics, but the Ritual forms, normalized here as [_spæria_]{.iv lang=oe sort=spaeria}, [_spær_]{.iv lang=oe sort=spaer}, and
[_spærede_]{.iv lang=oe sort=spaerede}, together with Vespasian Psalter [_spearad_]{.iv lang=oe sort=spearad}, point to primitive Old
English forms both with and without back vowels [@Campbell1959, §764]. Brunner likewise records
Northumbrian [_spæria_]{.iv lang=oe sort=spaeria}, [_spærede_]{.iv lang=oe sort=spaerede} beside common Old English [_sparian_]{.iv lang=oe sort=sparian} and
Vespasian Psalter [_spearad_]{.iv lang=oe sort=spearad} [@SieversBrunner1965, §364 Anm. 11]. The citation
form treated here is [_sparian_]{.iv lang=oe sort=sparian}; the Anglian forms are relics of the older
formation, not alternative headwords of equal status.

#### Development to Old English

Once the class-II formation [_\*spárōjaną_]{.iv lang=pgmc sort=sparojana} is chosen, the remaining development is
regular. The regular derivation shows brightening, restoration of _a_ before the
back vocalism of the suffix, later i-mutation within the weak ending, weak-tail
reduction, and contraction to [_sparian_]{.iv lang=oe sort=sparian}. By contrast, Brunner's rule against
further apocope of final _-e_ explains why Ritual [_spær_]{.iv lang=oe sort=spaer} cannot be the regular
continuation of inherited [_\*spárē_]{.iv lang=preoe sort=spare} [@SieversBrunner1965, §150].

#### Formation comparison

The comparison below sets the relevant forms side by side. It contrasts the inherited class-III formation
with the refashioned class-II one that yields the citation verb.

| Formation / comparison | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| inherited class-III infinitive | [_\*spárēną_]{.iv lang=pgmc sort=sparena} | paradigm comparison / probe output: [_sparen_]{.iv lang=oe sort=sparen} | [_sparian_]{.iv lang=oe sort=sparian} | wrong class and wrong ending for the citation verb |
| inherited class-III imperative singular | [_\*spárē_]{.iv lang=preoe sort=spare} | paradigm comparison / probe output: [_spære_]{.iv lang=oe sort=spaere} | Ritual [_spær_]{.iv lang=oe sort=spaer} | loss of final _-e_ is not regular, so the relic form cannot control the entry |
| inherited class-III finite present | [_\*spárēθi_]{.iv lang=preoe sort=sparethi} | paradigm comparison / probe output: [_spæreþ_]{.iv lang=oe sort=spaereth} | [_spearad_]{.iv lang=oe sort=spearad} | attested form is mixed, not a direct continuation of the inherited cell |
| selected class-II formation | [_\*spárōjaną_]{.iv lang=pgmc sort=sparojana} | documented regular output: [_sparian_]{.iv lang=oe sort=sparian} | [_sparian_]{.iv lang=oe sort=sparian} | exact match between derivational input and Old English citation form |

### staff — OE stæf

\index[oe]{staef@stæf}
\index[pgmc]{stabaz@*stábaz}
\index[pgmc]{stabiz@*stábiz}

Derivation: citation reconstruction _\*stábiz_; form followed here _\*stábaz_ > _stæf_ (early analogy).

#### Derivation trace

Proto input: _\*stábaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*stába} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*stáb} \\
Anglo Frisian Brightening & \emph{*stæb} \\
PGmc B Allophony & \emph{*stæβ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _stæf_

#### Reconstruction and comparative evidence

The comparative dictionaries do not give one uniform stem class. Kroonen
reconstructs an a-stem _\*staba-_ [@Kroonen2013, 471]. Orel writes _\*stabiz_ ~ _\*stabaz_ [@Orel2003, 368]. That disagreement matters because a direct i-stem input in
_\*-iz_ would predict i-mutation in Old English, whereas the attested noun keeps
_æ_.

#### Old English evidence

The Old English noun itself is the ordinary citation form _stæf_. Luick lists
_stæf_ among closed monosyllables with _æ_ [@Luick1914, 176]. Ringe and Taylor
pair singular _stæf_ with plural _stafas_ [@RingeTaylor2014, 193]. The
normalized form here is therefore _stæf_; later English _staff_ with _a_
belongs to a later stage of the word's history.

#### Development to Old English

With the selected a-stem input, the development is regular. Final _\*-z_
disappears, bare final _-a_ is lost, Anglo-Frisian brightening gives _æ_ in the
closed monosyllable, and medial _b_ surfaces as a fricative written _f_. The
documented chain is _\*stábaz_ > _\*stába_ > _\*stáb_ > _\*stæb_ > _stæf_. A direct
continuation of _\*stábiz_, by contrast, would produce i-mutated _stefe_ rather
than the attested singular.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the rejected i-stem line from the
selected a-stem input.

| Formation / label | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative i-stem line | *stábiz | expected _stefe_ after i-mutation | stæf | wrong vowel for the attested singular |
| mixed comparative notation | Orel _\*stabiz_ ~ _\*stabaz_; Kluge _\*stabi-_/a- | source-level stem-class uncertainty | stæf | useful comparative background, but not a single OE-facing input |
| selected a-stem input | *stábaz | documented regular output: _stæf_ | stæf | exact match between derivational input and Old English target |

### stem — OE stefn

\index[oe]{stefn@stefn}
\index[pgmc]{stamnaz@*stámnaz}
\index[pgmc]{stebno@*stébnō}
\index[goth]{stibna@stibna}

Derivation: citation reconstruction _\*stámnaz_; form followed here _\*stébnō_ > _stefn_ (early analogy).

#### Derivation trace

Proto input: _\*stébnō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*stébnu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PGmc B Allophony & \emph{*stéβnu} \\
\mbox{OE High Vowel Apocope} & \emph{*stéβn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _stefn_

#### Reconstruction and comparative evidence

The source tradition behind _stefn_ is not the same as the comparative label
_\*stámnaz_. Ringe and Taylor cite _\*stebnō_ for the noun continued by
Gothic _stibna_ and Old English _stebn_ > _stefn_ > _stemn_ [@RingeTaylor2014,
330]. Orel likewise gives _\*stebnō_ ~ _\*stemnō_, whereas Kroonen prefers
_\*stimnō-_, and Fulk describes the etymology of _stefn, stemn_ as insecure
[@Orel2003, 374; @Kroonen2013, 480; @Fulk2018, §6.11 n. 6].

These forms belong to the Old English noun _stefn_ 'voice, sound'. The
derivational input _\*stébnō_ is therefore best treated as the OE-facing
transponent supported by that source tradition. It does not settle the deeper
comparative reconstruction implied by the citation label _\*stámnaz_.

#### Old English evidence

Clark Hall records _stefn_ as the noun 'voice, sound' and cross-refers
_stemn_ to the same word [@ClarkHall1960, 276]. Ringe and Taylor give the OE
chronology directly as _stebn_ > _stefn_ > _stemn_ [@RingeTaylor2014, 330].

Bülbring and Luick treat _stemn_ as a later West Saxon development from
older _stefn_, produced by _fn_ > _mn_ only after the earlier period of nasal
influence on _e_ [@Bulbring1902, §§62 Anm. 3, 445; @Luick1914, §75 Anm. 1].
The relevant comparison form is therefore the conservative _stefn_, not the
later West Saxon doublet _stemn_.

#### Development to Old English

From _\*stébnō_, raising of final long _ō_ gives a _\*stébnu_ stage.
Regular fricativization of _b_ before _n_ then yields _\*stéβnu_, and loss
of the final high vowel leaves _\*stéβn_, written _stefn_ in Old English.
The later form _stemn_ belongs to a separate West Saxon assimilation after
this stage [@RingeTaylor2014, 330; @Bulbring1902, §445].

#### Source comparison

The comparison below sets the relevant forms side by side. It keeps apart the broader comparative label,
the OE-facing transponent, and the later West Saxon variant history.

| Form or label | Status | OE relation | Result |
| :--- | :--- | :--- | :--- |
| _\*stámnaz_ | comparative citation label for the broader stem/trunk family | does not itself control the _stefn_ derivation discussed here | broader lexical label only |
| _\*stébnō_ | voice-noun transponent | regular output: _stefn_ | Old English-facing input |
| _stemn_ | later attested West Saxon doublet | secondary form from _stefn_ by _fn_ > _mn_ | real OE variant, but not the selected comparator |

### swan — OE swanes

\index[oe]{swanes@swanes}
\index[pgmc]{swanas@*swánas}
\index[pgmc]{swanaz@*swánaz}

Derivation: citation reconstruction _\*swánaz_; form followed here _\*swánas_ > _swanes_ (early analogy).

#### Derivation trace

Proto input: _\*swánas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*swánæs} \\
OE Unstressed AE Merger & \emph{*swánes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _swanes_

#### Reconstruction and comparative evidence

The Germanic noun is ordinarily cited as the masculine a-stem _\*swanaz_
[@Orel2003, 367]. The form followed here, _\*swánas_, is not a competing
lexeme reconstruction. It is the genitive singular of the same paradigm.

The question here is therefore one of paradigm cell rather than stem history.
The citation form remains _\*swanaz_ > _swan_; the comparison form is the
genitive singular _\*swánas_ > _swanes_.

#### Old English evidence

Bright's glossary records the ordinary noun as _swan, m._ and also gives the
exact inflected form _swanes_, citing the phrase _swanes feðre_
[@BrightCassidyRingler1971, 441].

The target is therefore an attested Old English genitive singular, not a
reconstruction. It is also not the ordinary citation lemma. The entry must keep
those two facts distinct.

#### Development to Old English

From _\*swánas_, Anglo-Frisian brightening gives _\*swánæs_, and
subsequent merger of unstressed _æ_ with _e_ yields _swanes_. The
comparison is straightforward once the genitive singular is chosen as the
relevant cell.

#### Paradigm-cell comparison

The comparison below sets the relevant forms side by side. It separates the ordinary citation form from the
selected inflected cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *swánaz | OE headword _swan_ | swan | ordinary lexeme line |
| genitive singular | *swánas | regular output: _swanes_ | swanes | attested cell |

### thousand — OE þūsend

\index[oe]{aerende@ærende}
\index[oe]{thusend@þūsend}
\index[pgmc]{thusendi@*θūs-èndi}
\index[pgmc]{thusendi@*θūsèndi}
\index[pgmc]{thusundi@*θūs-undī}

Derivation: citation reconstruction _\*θūs-undī_; form followed here _\*θūs-èndi_ > _þūsend_ (early analogy).

#### Derivation trace

Proto input: _\*θūsèndi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*θūsènd} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Strip Secondary Stress & \emph{*θūsend} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þūsend_

#### Reconstruction and comparative evidence

Kroonen reconstructs the Germanic numeral as _\*þūsundī-_ and cites Old
English _þūsend_ among its continuations [@Kroonen2013, 554]. The
derivational input _\*θūs-èndi_ is not the same claim. It is an OE-oriented
transponent with the second-member vowel already resolved to _e_ and the final
high vowel already shortened for apocope.

The important question is therefore chronological. Why does Old English show
_þūsend_, while related languages such as Old Saxon and Old High German keep
_u_ in the second syllable? [@Kroonen2013, 554].

#### Old English evidence

Old English _þūsend_ is an ordinary citation form, not a selected oblique or
paradigm cell. Campbell treats it as a neuter noun with normal case forms
[@Campbell1959, §689]. The problem lies in the internal history of the word, not
in its lexical status.

#### Development to Old English

If the old final _-ī_ had remained long enough to trigger ordinary double
umlaut, Campbell's rule would point toward a form of _\*þȳsend_ type rather
than attested _þūsend_ [@Campbell1959, §203]. Preserved root _ū_
therefore argues that the umlaut-triggering vowel was lost or neutralized before
the ordinary OE umlaut outcome could develop.

That early loss, however, does not by itself explain the medial _e_. Luick
compares the word with _ærende_ and later groups _thousand_ with forms
reshaped on that pattern [@Luick1914, §§198, 492]. Viredaz is more cautious,
arguing that Old English _e_ in this weak position may simply write schwa and so
need not prove a unique _ærende_-type analogy [@GermanicSlavicBaltic2025,
§2.1.4].

The selected transponent _\*θūs-èndi_ captures the OE-side state from which
the regular derivation reaches _þūsend_.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the secure chronology from the more
interpretive account of the second-syllable vowel.

| Stage / interpretation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| surviving _-ī_ with ordinary double umlaut | _\*þūsundī-_ treated as still umlaut-active in OE | would point toward _\*þȳsend_ | excluded by preserved _ū_ |
| early loss of the trigger without further reshaping | _\*þūsund-_ type | explains _ū_, but not why OE alone has medial _e_ | incomplete account |
| selected OE-oriented transponent | _\*θūs-èndi_ | regular output: _þūsend_ | selected modeling input |

### timber — OE timber

\index[oe]{timber@timber}
\index[pgmc]{timbra@*tímbrą}
\index[pgmc]{timra@*tímrą}

Derivation: citation reconstruction _\*tímrą_; form followed here _\*tímbrą_ > _timber_ (early analogy).

#### Derivation trace

Proto input: _\*tímbrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*tímbr} \\
OE Epenthetic Vowel & \emph{*tímber} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _timber_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*timbra-_ and cites Old English
_timber_ among its continuations [@Kroonen2013, 517]. Ringe and Taylor
instead state the history from PGmc _\*timra_ through West Germanic
_\*timbr_ to Old English _timber_ [@RingeTaylor2014, 327].

The difference is therefore not over the Old English noun itself. It concerns
whether medial _b_ belongs in the comparative citation form or appears in an
early pre-Old-English stage of the cluster.

#### Old English evidence

Clark Hall lemmatizes the noun as _timber_ and also records _timbor_ as
a variant spelling [@ClarkHall1960, 294]. The Old English form is thus an ordinary
citation noun, not a selected oblique cell or a reconstructed convenience form.

#### Development to Old English

With the consonantal frame _timbr-_ in place, the rest of the development is
straightforward. Loss of final _-ą_ leaves _\*tímbr_, and epenthetic
_e_ in the final cluster yields _timber_. Ringe and Taylor's
_\*timra_ > _\*timbr_ > OE _timber_ and the handbook treatment of this epenthetic
vowel point to the same Old English result [@RingeTaylor2014, 327; @Campbell1959,
§§463-464].

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the comparative headword from the
OE-facing consonantal input.

| Formation or notation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| Kroonen's comparative citation | _\*timbra-_ | already matches the consonantal frame of OE _timber_ | closest comparative support for the derivational input |
| Ringe-Taylor citation line | _\*timra_ > _\*timbr_ | reaches the same OE noun through early cluster expansion | compatible comparative background |
| modeled input | _\*tímbrą_ | regular output: _timber_ | Old English-facing input |

### wake — OE wacan

\index[oe]{wacan@wacan}
\index[pgmc]{wakana@*wákaną}
\index[pgmc]{wakena@*wakēną}

Derivation: citation reconstruction _\*wakēną_; form followed here _\*wákaną_ > _wacan_ (early analogy).

#### Derivation trace

Proto input: _\*wákaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wækaną} \\
OE A Restoration & \emph{*wakaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wakan} \\
OE Secondary Nasalization & \emph{*wakąn} \\
OE Weak Tail Reduction & \emph{*wakan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wacan_

#### Reconstruction and comparative evidence

Kroonen gives the strong verb as _\*wakan-_ with Old English
_wacan_ [@Kroonen2013, 568]. Ringe and Taylor separately derive Old English
_wacian_ from weak _\*wakai-_ ~ _\*wakja-_ [@RingeTaylor2014, §3.3.2].

The difference is therefore lexical and class-based, not graphic. Strong
_wacan_ 'wake up, arise' and weak _wacian_ 'be awake, watch' belong to
related but distinct histories.

#### Old English evidence

Clark Hall keeps _wacan_ and _wacian_ as separate headwords
[@ClarkHall1960, 338]. Bosworth-Toller adds an important caution under
_wacan_: the simplex infinitive itself does not occur, its place seeming to
be taken by _wæcnan_ [@BosworthToller1898, 226].

The target _wacan_ is therefore best understood as a normalized strong
headword for the verb family, not as a directly quoted simplex infinitive. It
still remains the correct Old English comparison form for the strong branch.

#### Development to Old English

With strong _\*wákaną_, Anglo-Frisian brightening first gives a form of the
_\*wækaną_ type. A-restoration then returns _a_, and the ordinary tail
reductions yield _wacan_. The weak verb _wacian_ belongs to a different
prehistory and is not the expected outcome of this input.

#### Class comparison

The comparison below sets the relevant forms side by side. It separates the strong and weak verb lines.

| Formation / class | Candidate input | OE outcome or comparison | Result |
| :--- | :--- | :--- | :--- |
| weak class-III / class-II branch | _\*wakēną_, _\*wakai-_ ~ _\*wakja-_ | OE _wacian_ and related weak forms | related lexeme, but not the target of this entry |
| strong class-VI branch | _\*wákaną_ | regular output: _wacan_ | Old English-facing input |
| strong normalized headword | _wacan_ | dictionary comparison form beside attested strong-family forms | correct Old English comparator, though not a directly quoted simplex infinitive |

### water — OE wæter

\index[oe]{waeter@wæter}
\index[pgmc]{watna@*wátną}
\index[pgmc]{wator@*wátōr}

Derivation: citation reconstruction _\*wátną_; form followed here _\*wátōr_ > _wæter_ (early analogy).

#### Derivation trace

Proto input: _\*wátōr_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Or Lowering & \emph{*wátar} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wætær} \\
OE Unstressed AE Merger & \emph{*wæter} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wæter_

#### Reconstruction and comparative evidence

Kroonen reconstructs a heteroclitic noun _\*watar-_ ~ _\*watan-_ and states that
the Proto-Germanic material points to _\*watōr_, _\*watenaz_
[@Kroonen2013, 616]. Ringe and Taylor likewise start from singular
_\*wator_ before the Old English branch [@RingeTaylor2014, §3.1.4].

The generalized comparative label is therefore broader than the singular
form that actually corresponds to Old English _wæter_. The relevant
comparator is the inherited nominative-accusative singular _\*wátōr_.

#### Old English evidence

Bright gives the noun as _wæter_ with the regular paradigm
_wæteres_, _wætere_, _wæter(u)_, _wætera_, _wæterum_
[@BrightCassidyRingler1971, 29]. Ringe and Taylor add the dialectal contrast
between West Saxon _weeter_ and Mercian _weter_
[@RingeTaylor2014, §6.5.2].

The target is therefore an attested Old English citation form within a normal
paradigm. The complication lies on the comparative side of the lexeme, not in
Old English attestation.

#### Development to Old English

From _\*wátōr_, pre-final _\*ō_ becomes _a_ before final _r_,
yielding _\*watar_ [@RingeTaylor2014, §3.1.4]. Anglo-Frisian brightening then
gives _\*wætær_, and merger of unstressed _æ_/_e_ yields _wæter_.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the generalized lexeme label from
the singular input that matches the Old English citation form.

| Stage or notation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| generalized comparative label | _\*wátną_ | broader lexeme shorthand, not the singular that corresponds directly to _wæter_ | useful background only |
| heteroclitic stem notation | _\*watar-_ ~ _\*watan-_ | source-faithful comparative reconstruction | explains why a singular comparator is needed |
| inherited singular input | _\*wátōr_ | regular output: _wæter_ | Old English-facing input |

### whale — OE hwæl

\index[oe]{hwael@hwæl}
\index[pgmc]{walaz@*wálaz}
\index[pgmc]{xwalaz@*xwálaz}

Derivation: citation reconstruction _\*wálaz_; form followed here _\*xwálaz_ > _hwæl_ (early analogy).

#### Derivation trace

Proto input: _\*xwálaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*xwála} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*xwál} \\
Anglo Frisian Brightening & \emph{*xwæl} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hwæl_

#### Reconstruction and comparative evidence

The comparative sources are not uniform. Orel gives _\*xwalaz_ and notes some
mixed _\*xwaliz_ evidence [@Orel2003, 197]. Kroonen instead cites
_\*hwali-_ [@Kroonen2013, 262].

Both notations agree on inherited initial _hw-/xw-_, but they differ in
stem label. The a-stem-like input followed here is closer to Orel's notation
than to Kroonen's citation form.

#### Old English evidence

Clark Hall lemmatizes the noun as _hwal_, and Bosworth-Toller preserves the
plural _hwalas_ [@ClarkHall1960, 170; @BosworthToller1898, 326]. The comparison form
is normalized here as _hwæl_ for the singular citation form with Anglo-
Frisian fronting.

The plural _hwalas_ remains important control evidence. It shows the same
lexeme with _a_ in an open syllable, beside singular _hwæl_ in the
closed monosyllable.

#### Development to Old English

From _\*xwálaz_, final _-z_ disappears and bare final _-a_ is lost.
Anglo-Frisian fronting then yields _æ_ in the closed monosyllable, and Old
English orthography writes _hwæl_.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the competing comparative
notations from the normalized Old English singular.

| Comparative line | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| Orel's citation | _\*xwalaz_ | same stem notation as the modeled singular line | closest comparative support for the derivational input |
| Kroonen's citation | _\*hwali-_ | same initial cluster, different stem label | important comparative rival, but not the notation followed here |
| modeled input | _\*xwálaz_ | regular output: _hwæl_ | Old English-facing input |
| plural control | _hwalas_ | attested open-syllable plural beside singular _hwæl_ | confirms that the lexeme also preserves an _a_-vocalism branch |

### whine — OE hwīnan

\index[oe]{hwinan@hwīnan}
\index[pgmc]{wainojana@*wainōjaną}
\index[pgmc]{xwinana@*xwḯnaną}

Derivation: citation reconstruction _\*wainōjaną_; form followed here _\*xwī́naną_ > _hwīnan_ (early analogy).

#### Derivation trace

Proto input: _\*xwī́naną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*xwī́nan} \\
OE Secondary Nasalization & \emph{*xwī́nąn} \\
OE Weak Tail Reduction & \emph{*xwī́nan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hwīnan_

#### Reconstruction and comparative evidence

The citation reconstruction preserved in the header belongs to the lament-family
verb seen in German _weinen_ and Old English _wānian_. Kroonen instead separates
Old English _hwīnan_ under _\*hwinan-_ [@Kroonen2013, 267]. Orel likewise
distinguishes strong _\*xwinanan_ from weak _\*wainōjanan_ [@Orel2003, 201]. Ringe and
Taylor make the same split at the Northwest Germanic level, linking Old Norse
_hvina_ and Old English _hwinan_ to the same strong verb
[@RingeTaylor2014, 130].

The two families also differ phonologically and morphologically. The lament
family has initial _w-_, diphthongal _ai_, and weak-II morphology, whereas the
verb behind Old English _hwīnan_ has initial _hw-/xw-_, long _ī_, and
strong-verb inflection. The form followed here, _\*xwī́naną_, therefore represents a
competing comparative identification rather than a hidden cell of _\*wainōjaną_.

#### Old English evidence

Clark Hall records _hwinan_ with the gloss 'to hiss, whizz, whistle'
[@ClarkHall1960, 171]. Seebold keeps the verb among the strong verbs and notes that
only a present-tense attestation is directly preserved [@Seebold1970, 280].

The Old English form is normalized here as _hwīnan_. That normalization adds the
usual vowel length marking to the dictionary spelling _hwinan_; it does not turn
an unattested verb into a reconstructed one.

#### Development to Old English

Once the strong-verb input _\*xwī́naną_ is selected, the path to Old English is
straightforward. The compact trace shows heavy-syllable nasal apocope,
secondary nasalization, and weak-tail reduction, after which the form surfaces
as _hwīnan_.

No special paradigm maneuver is needed for this verb. The comparison is between
two different Germanic verb families: the Old English form belongs with the
strong verb _\*hwīnan-_, not with the weak lament verb.

#### Verb-family comparison

The comparison below sets the relevant forms side by side. It separates the competing comparative labels
that stand behind the inherited Old English forms.

| Verb family / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lament-family weak verb | _\*wainōjaną_ | comparative continuation in OE _wānian_ | wānian | competing citation reconstruction, but not the source of _hwīnan_ |
| selected strong verb | _\*xwī́naną_ | regular output: _hwīnan_ | hwīnan | exact match between derivational input and OE verb |
| comparative North Germanic cognate | Northwest Germanic strong verb behind ON _hvina_ / OE _hwinan_ | ON _hvina_ / OE _hwinan_ | hwīnan | supports the strong-verb identification |

### withy — OE wīþiġ

\index[oe]{withig@wīþiġ}
\index[pgmc]{waithiz@*wáiθiz}
\index[pgmc]{withaga@*wḯθagą}

Derivation: citation reconstruction _\*wáiθiz_; form followed here _\*wī́θagą_ > _wīþiġ_ (early analogy).

#### Derivation trace

Proto input: _\*wī́θagą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wī́θægą} \\
OE Heavy Syllable Nasal Apocope & \emph{*wī́θæg} \\
OE Velar Palatalization & \emph{*wī́θæʤ} \\
OE Unstressed AE Merger & \emph{*wī́θeʤ} \\
OE Late Unstressed Ag Suffix & \emph{*wī́θiʤ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wīþiġ_

#### Reconstruction and comparative evidence

The comparative evidence groups the word with Germanic forms of the
_\*wīþja_/_ō-_ or _\*wiþ-_ type [@Orel2003, 503]. That material is
useful for the cognate set, but it does not by itself explain the Old English
suffix of _wīþiġ_.

For Old English, the relevant point is the suffix history. Campbell's account
of OE _-ig_, including forms such as _hunig_, supports an analysis in which the
_-iġ_ of _wīþiġ_ continues a derivational _\*-ag-_ sequence rather than a heavy
ja-stem _\*-ij-_ [@Campbell1959, §§275, 376]. The form followed here, _\*wī́θagą_, is
thus a formation choice rather than a mere respelling of the comparative
headword.

#### Old English evidence

Clark Hall records the noun as _wiðig_ [@ClarkHall1960, 358]. The form used here,
_wīþiġ_, is a normalized Old English spelling with macrons and palatal ġ marked
explicitly.

The relevant comparison form is therefore not a reconstructed dictionary
convenience but an established Old English noun. What requires explanation is
why the selected Proto-Germanic input is _\*wī́θagą_ rather than a comparative
headword of the _\*wīþja-_ type.

#### Development to Old English

From _\*wī́θagą_, Anglo-Frisian brightening gives a fronted vowel in the suffixal
syllable, and, on the Campbell analysis adopted here, the later Old English
development of _\*-ag-_ yields _-iġ_ [@Campbell1959, §§275, 376].
Palatalization supplies the final _ġ_, and the full development reaches
_wīþiġ_.

This derivation is regular for the form compared here. The central claim of the
entry is therefore morphological: Old English _wīþiġ_ belongs with an
_\*-ag-_ derivative, whereas the comparative _\*wīþja-_ label belongs to a
different way of presenting the cognate family.

#### Formation comparison

The comparison below sets the relevant formations side by side. It distinguishes the comparative headword from
the Old English-facing formation that actually yields the attested noun.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative family label | *wáiθiz | broader cognate-set headword | OE family context | useful lexeme label, but not the direct source of _wīþiġ_ |
| heavy ja-stem analysis | _\*wīþja-_ type | Campbell/Adamczyk-style heavy ja-stem _-e_ / zero outcome | _wīþiġ_ | does not account cleanly for the OE suffix |
| _\*-ag-_ derivative followed here | *wī́θagą | regular output: _wīþiġ_ | wīþiġ | exact match between formation and target |

### world — OE weorold

\index[oe]{weorold@weorold}
\index[pgmc]{wiraaldiz@*wíra-àldiz}
\index[pgmc]{wiraldu@*wír-àldu}
\index[pgmc]{wiraldu@*wíràldu}

Derivation: citation reconstruction _\*wíra-àldiz_; form followed here _\*wír-àldu_ > _weorold_ (early analogy).

#### Derivation trace

Proto input: _\*wíràldu_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
NWGmc I Lowering & \emph{*wéràldu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Inter Stress Raising & \emph{*wéruldu} \\
OE Med Unstressed U Lowering & \emph{*wéroldu} \\
OE Back Mutation & \emph{*wéoroldu} \\
OE High Vowel Apocope & \emph{*wéorold} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weorold_

#### Reconstruction and comparative evidence

The word is the old compound 'age of men'. Comparative sources preserve two
slightly different views of its first element. Orel and the _\*wira-_ tradition
keep the older _i_-vocalism, while Ringe and Taylor discuss the lowered form
_\*weraldiz_ and its pre-Old-English chain _\*weraldu_ > _\*weruld_
[@Orel2003, 501; @RingeTaylor2014, 341]. Kluge-Seebold likewise gives the
compound _\*wira-aldō_ and explicitly includes Old English _weorold_
[@KlugeSeebold2011, 981].

The form followed here, _\*wír-àldu_, therefore differs from the citation label in two
ways. It keeps the older _\*wir-_ vowel of the comparative headword, but it also
presupposes the early shift of the compound into the ō-stems that Ringe and
Taylor note for this lexeme [@RingeTaylor2014, 341]. The early analogical step lies
in that stem-class reassignment; the later phonological developments can then run
regularly.

#### Old English evidence

Old English does not preserve a single isolated form. Ringe and Taylor give West
Saxon _weorold_ ~ _worold_, Mercian _weoruld_, Northumbrian _woruld_, and Kentish
_wiarald_ [@RingeTaylor2014, 341]. Sievers-Brunner and Bright present the same wider
set, including the syncopated _world_ and later rounded _wurold_
[@SieversBrunner1965, §113; @BrightCassidyRingler1971, 465].

The Old English form used here is the West Saxon form _weorold_. It is an attested Old
English form within that broader variant cluster, not the only form the lexeme
ever shows.

#### Development to Old English

From _\*wír-àldu_, Northwest Germanic _i_-lowering gives
_\*wér-àldu_. Inter-stress raising then changes the medial _a_ to _u_, producing
_\*wér-uldu_. In the Old English branch that unstressed _u_ lowers to _o_, and
back mutation yields _\*wéor-oldu_; final high-vowel apocope then gives
_weorold_.

This sequence matches the comparative background in Ringe and Taylor's
_\*weraldiz_ > _\*weraldu_ > _\*weruld_ chain while preserving the _\*wir-_ notation of
the comparative label [@RingeTaylor2014, 341]. The modeled Old English form
therefore stands at the meeting point of an early stem-class reshaping and later
regular sound change.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the comparative headword from the
OE-facing stage chosen for the derivation.

| Stage / interpretation | Candidate form | Old English outcome or comparison | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| comparative compound with older first-element vowel | _\*wíra-àldiz_ | citation reconstruction / lexeme label | preserves the older _\*wir-_ tradition of the compound |
| literature-stage lowered compound after early stem-class shift | _\*weraldiz_ > _\*weraldu_ > _\*weruld_ | Ringe-Taylor background chain to OE _weorold_ ~ _worold_ | explains the older comparative literature cited for the word |
| Old English-facing input | _\*wír-àldu_ | regular output: _weorold_ | exact match for the West Saxon form used here |
| broader OE variant cluster | — | _worold_, _weoruld_, _woruld_, _wiarald_, _world_ | real attested comparanda that remain outside that West Saxon line |

### youth — OE ġeoguþ

\index[oe]{geoguth@ġeoguþ}
\index[pgmc]{jugunth@*júgunθ}
\index[pgmc]{jugunthiz@*júgunθiz}

Derivation: citation reconstruction _\*júgunθiz_; form followed here _\*júgunθ_ > _ġeoguþ_ (early analogy).

#### Derivation trace

Proto input: _\*júgunθ_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Ws Palatal Glide & \emph{*jéugunθ} \\
NWGmc Nasal Spirant Lengthening & \emph{*jéugūnθ} \\
NWGmc Nasal Spirant Loss & \emph{*jéugūθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*jéogūθ} \\
OE Unstressed Long Vowel Shortening & \emph{*jéoguθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġeoguþ_

#### Reconstruction and comparative evidence

The wider etymological tradition reconstructs an earlier form of the word as
_\*ju(w)unþi-_ [@Kroonen2013, 316]. The comparative label
_\*júgunθiz_ already stands at a later Germanic stage with _g_, and the
derivational input _\*júgunθ_ is later again: it represents the form after final
_-i_ has been lost.

That staging matters because Ringe and Taylor explicitly give the sequence
_\*jugunþi_ > _\*juguþ_ > OE _geoguþ_ ~ _iuguþ_ [@RingeTaylor2014, 141]. The
derivational input therefore differs from the broader comparative headword
because the Old English development must begin after early loss of final _-i_.

#### Old English evidence

The Old English noun is attested with varying spellings. Ringe and Taylor cite
_geoguþ_ ~ _iuguþ_ [@RingeTaylor2014, 141]. The form is normalized here as
_ġeoguþ_: the initial palatal is written with _ġ_, and the attested spelling
variation is treated as orthographic rather than lexical.

Nothing in the source stack suggests that a different paradigm cell should be
chosen. The relevant Old English comparison form is the noun _ġeoguþ_ itself.

#### Development to Old English

The decisive early step is the loss of final _-i_ before the Old English umlaut
stage. If that high vowel remained, the word would develop an over-umlauted
_y_-type vowel instead of the attested form [@RingeTaylor2014, 141].

From _\*júgunθ_, the later development is regular: palatal
fronting yields _\*jéugunθ_; nasal-spirant lengthening and loss give
_\*jéogūθ_ [@Fulk2018, 109]; unstressed long-vowel shortening then produces
_\*jéoguθ_, which surfaces as _ġeoguþ_. Campbell preserves _u_ after accented _u_ in forms such
as _duguþ_ and _munuc_ [@Campbell1959, §374]. Brunner likewise cites _iuzuð_
_Jugend_ and _munuc_ _Mönch_ in the same environment
[@SieversBrunner1965, §150.3].

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the later stages relevant to the Old English noun.

| Stage / interpretation | Candidate form | Old English outcome or comparison | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| earlier etymological headword | _\*ju(w)unþi-_ | comparative family background | older comparative reconstruction of the lexeme |
| later g-bearing comparative label | _\*júgunθiz_ | citation reconstruction / lexeme label | preserves the later Germanic stage behind the selected entry |
| Old English-facing input | _\*júgunθ_ | regular output: _ġeoguþ_ | exact match for the Old English form used here |
| full _-i_ stage retained too long | _\*jugunþi_ | expected over-umlauted _y_-type result | negative control showing why early _-i_ loss must precede the OE umlaut stage |

\clearpage

## Late analogy and paradigm-cell selection

These entries involve a later paradigm-cell or analogical comparison. The
citation reconstruction remains relevant to the lexeme, but the attested Old
English form is best explained through a particular inflectional or analogical
form rather than through the citation form alone.

### ban — OE bannes

\index[oe]{bannes@bannes}
\index[pgmc]{banna@*bánną}
\index[pgmc]{bannas@*bánnas}

Derivation: citation reconstruction _\*bánną_; form followed here _\*bánnas_ > _bannes_ (late analogy).

#### Derivation trace

Proto input: _\*bánnas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*bánnæs} \\
OE Unstressed AE Merger & \emph{*bánnes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bannes_

#### Reconstruction and comparative evidence

Orel cites a bann-noun under [_\*bannan_]{.iv lang=pgmc sort=bannan role=source_protoform}, while Seebold distinguishes bann-stems
of both masculine and neuter type and gives Old English [_gebann_]{.iv lang=oe sort=gebann role=comparison_form} as the noun
reflex [@Orel2003, 35; @Seebold1970, 89]. The citation reconstruction [_\*bánną_]{.iv lang=pgmc sort=banna role=source_protoform}
names the lexeme, but the comparison here turns on the genitive singular
[_\*bánnas_]{.iv lang=pgmc sort=bannas role=selected_input}.

That distinction matters because the analysis depends on medial, not final,
gemination.

#### Old English evidence

Old English lexicographic evidence securely supports the noun itself.
Bosworth-Toller records the noun under nominative [_ge-bann_]{.iv lang=oe sort=gebann role=comparison_form}, with oblique
usage such as [_gebanne_]{.iv lang=oe sort=gebanne role=comparison_form} [@BosworthToller1898, 303]. The exact unprefixed
genitive [_bannes_]{.iv lang=oe sort=bannes role=target_form} is less directly cited in the dictionaries, so it is best
treated here as the regular genitive form used for comparison rather than as a
dictionary headword.

#### Development to Old English

From [_\*bánnas_]{.iv lang=pgmc sort=bannas role=selected_input}, the geminate remains medial before the case ending and the
unstressed vowel develops regularly to give [_bannes_]{.iv lang=oe sort=bannes role=target_form}. The paradigm comparison
therefore sets the genitive against nominative [_ban_]{.iv lang=oe sort=ban role=comparison_form}, the ordinary nominative
form of the same noun, rather than against a directly cited genitive headword.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It shows why the genitive singular is the
conservative cell used for the entry.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*bánną_]{.iv lang=pgmc sort=banna role=source_protoform} | regular output: [_ban_]{.iv lang=oe sort=ban role=regular_output} | ban | regular nominative outcome, but not the Old English form here |
| genitive singular | [_\*bánnas_]{.iv lang=pgmc sort=bannas role=selected_input} | regular output: _bannes_ | [_bannes_]{.iv lang=oe sort=bannes role=target_form} | direct match for the conservative genitive |

### berry — OE berġes

\index[oe]{berges@berġes}
\index[pgmc]{bazja@*bázją}
\index[pgmc]{bazjas@*bázjas}

Derivation: citation reconstruction _\*bázją_; form followed here _\*bázjas_ > _berġes_ (late analogy).

#### Derivation trace

Proto input: _\*bázjas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*bærjæs} \\
OE I Umlaut & \emph{*berjæs} \\
OE Unstressed AE Merger & \emph{*berjes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _berġes_

#### Reconstruction and comparative evidence

Kroonen reconstructs the berry noun as [_\*basja-_]{.iv lang=pgmc sort=basja role=source_protoform} ~ [_\*bazja-_]{.iv lang=pgmc sort=bazja role=source_protoform} [@Kroonen2013, 54]. The
derivational input [_\*bázjas_]{.iv lang=pgmc sort=bazjas role=selected_input} is therefore not a rival lexeme headword, but a
specific genitive singular cell drawn from that paradigm.

The relevant point is that _\*rj_ did not geminate in Proto-West Germanic.
Ringe and Taylor's [_here_]{.iv lang=oe sort=here role=comparison_form}, [_herges_]{.iv lang=oe sort=herges role=comparison_form} comparison shows the same _rj_ environment in
an Old English paradigm without any hidden gemination repair [@RingeTaylor2014, 181].

#### Old English evidence

Campbell cites feminine [_berige_]{.iv lang=oe sort=berige role=comparison_form} 'berry' and notes that _-j-_ is retained after
_r_ in this type [@Campbell1959, 250]. The reviewed evidence therefore supports the
citation form more directly than the exact genitive [_berġes_]{.iv lang=oe sort=berges role=target_form}, which is best read
here as the regular genitive comparison form rather than as a
dictionary headword.

#### Development to Old English

Citation [_\*bázją_]{.iv lang=pgmc sort=bazja role=source_protoform} gives [_bere_]{.iv lang=oe sort=bere role=regular_output}, not the Old English form here. The genitive singular
[_\*bázjas_]{.iv lang=pgmc sort=bazjas role=selected_input}, however, gives [_berġes_]{.iv lang=oe sort=berges role=target_form}, with medial _-rġ-_ preserved in the same
way that Ringe and Taylor cite [_herges_]{.iv lang=oe sort=herges role=comparison_form} beside [_here_]{.iv lang=oe sort=here role=comparison_form} [@RingeTaylor2014, 181].
This points to paradigm choice rather than to an extra phonological rule.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It shows the contrast between the citation form
and the genitive singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*bázją_]{.iv lang=pgmc sort=bazja role=source_protoform} | regular output: [_bere_]{.iv lang=oe sort=bere role=regular_output} | [_berige_]{.iv lang=oe sort=berige role=comparison_form} / [_berġe_]{.iv lang=oe sort=berge role=comparison_form} | useful citation-form background, but not the Old English form here |
| genitive singular | [_\*bázjas_]{.iv lang=pgmc sort=bazjas role=selected_input} | regular output: _berġes_ | [_berġes_]{.iv lang=oe sort=berges role=target_form} | exact match for the conservative cell |

### bow — OE bēag

\index[oe]{beag@bēag}
\index[pgmc]{baug@*báug}
\index[pgmc]{beugana@*béuganą}

Derivation: citation reconstruction _\*béuganą_; form followed here _\*báug_ > _bēag_ (late analogy).

#### Derivation trace

Proto input: _\*báug_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*báeug} \\
OE Diphthong Leveling & \emph{*bēag} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bēag_

#### Reconstruction and comparative evidence

The inherited verb belongs to the class-II strong-verb family [_\*béuganą_]{.iv lang=pgmc sort=beugana}
[@RingeTaylor2014, 55]. Within that paradigm, however, the infinitive and the
singular preterite continue different ablaut grades. The derivational input [_\*báug_]{.iv lang=pgmc sort=baug}
is the singular preterite cell, whereas the citation form [_\*béuganą_]{.iv lang=pgmc sort=beugana} is the
infinitive.

Campbell's account of Old English class-II strong verbs treats the singular
preterite _au_ > _ēa_ development as regular in this environment
[@Campbell1959, 53].
That is the phonological path relevant for [_bēag_]{.iv lang=oe sort=beag}, whereas the analogical _ū_
of the present stem belongs to the separate history behind [_būgan_]{.iv lang=oe sort=bugan}
[@RingeTaylor2014, 55].

#### Old English evidence

Bosworth-Toller and Clark Hall both record [_bēag_]{.iv lang=oe sort=beag} as a preterite form of
[_būgan_]{.iv lang=oe sort=bugan} [@BosworthToller1898, 122; @ClarkHall1960, 45]. The form discussed here is
therefore an attested Old English verbal form, not a reconstructed substitute
for the infinitive.

The ordinary dictionary headword remains [_būgan_]{.iv lang=oe sort=bugan}, but the relevant comparison
form for this entry is the singular preterite [_bēag_]{.iv lang=oe sort=beag}. That is the paradigm
cell in which the inherited _\*au_ grade is preserved most directly.

#### Development to Old English

From [_\*báug_]{.iv lang=pgmc sort=baug}, Anglo-Frisian fronting and the later leveling of the diphthong
produce [_bēag_]{.iv lang=oe sort=beag} [@Campbell1959, 53]. No special analogical repair is needed for that
cell. The form is the regular Old English outcome of the singular-preterite
grade.

The analogical element in the wider lexeme belongs instead to the present stem
seen in [_būgan_]{.iv lang=oe sort=bugan}. The derivational input differs from the citation form because the
regular inherited pathway survives more transparently in the preterite than in
the infinitive.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the regular singular
preterite from the more familiar infinitival citation form.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | [_\*béuganą_]{.iv lang=pgmc sort=beugana} | inherited present-stem history behind [_būgan_]{.iv lang=oe sort=bugan} | [_būgan_]{.iv lang=oe sort=bugan} | establishes the lexeme, but not the Old English form here |
| singular preterite | [_\*báug_]{.iv lang=pgmc sort=baug} | regular output: [_bēag_]{.iv lang=oe sort=beag} | [_bēag_]{.iv lang=oe sort=beag} | exact match between input, output, and attested cell |
| past participial branch | participial _\*bugan-_ type | later participial outcomes | bogen-type evidence | relevant to the paradigm, but not the clearest match for this entry |

The singular preterite is the relevant comparison form. It gives a direct
lautgesetzlich path to attested [_bēag_]{.iv lang=oe sort=beag}, while the citation form [_būgan_]{.iv lang=oe sort=bugan}
belongs to a paradigm whose present stem has already undergone later leveling.

### cow — OE cȳ

\index[oe]{cy@cȳ}
\index[pgmc]{koz@*kōz}
\index[pgmc]{kui@*kūi}

Derivation: citation reconstruction _\*kōz_; form followed here _\*kūi_ > _cȳ_ (late analogy).

#### Derivation trace

Proto input: _\*kūi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*kȳi} \\
\mbox{OE High Vowel Apocope} & \emph{*kȳ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cȳ_

#### Reconstruction and comparative evidence

Kroonen reconstructs a root noun with the inherited alternation
_\*kō-_ ~ _\*ku-_, explicitly nom. _\*kōz_, obl. _\*kū-_ [@Kroonen2013, 299].
The citation form therefore belongs to the nominative singular, whereas the
derivational input _\*kūi_ belongs to the oblique stem.

Ringe and Taylor also posit a later PNWGmc nominative _\*kūaz_ > _\*kūz_ behind Old
English _cū_ [@RingeTaylor2014, §3.1.3]. That nominative history matters for
the headword, but the form _cȳ_ depends on the oblique _\*kū-_ stem and a
following _\*i_.

#### Old English evidence

Clark Hall lemmatizes the noun under _cū_ and records gen.sg. _cū(e)_, _cȳ_, _cūs_,
dat.sg. _cȳ_, nom.-acc.pl. _cȳ_, and dat.pl. _cūm_ [@ClarkHall1960, 67]. Ringe
and Taylor likewise state that the root-noun _cū_ exhibits dat.sg., nom.-acc.pl.
_cȳ_ < _\*cūi_, dat.pl. _cūm_ < _\*cūm_, and apparently gen.sg. _cā_ < _\*cūiz_
[@RingeTaylor2014, §6.6.1].

The dictionary headword is therefore _cū_, but _cȳ_ is an established Old
English paradigm form rather than a convenient reconstruction. It serves as
dative singular and also as nominative-accusative plural. The genitive
singular is less stable, with _cā_, _cȳ_, _cū(e)_, and _cūs_ all appearing in
the local source record.

#### Development to Old English

_\*kūi_ is the dative singular of the oblique _\*kū-_ stem. The following _\*i_
triggers i-umlaut, so _ū_ becomes _ȳ_, and loss of the final high vowel leaves
_cȳ_. The development is _\*kūi_ > _\*kȳi_ > _\*kȳ_ > _cȳ_.

This is the regular oblique-cell path recognized by Ringe and Taylor's paradigm
statement [@RingeTaylor2014, §6.6.1]. It also explains why _cȳ_ is the cleanest
comparison form for the present entry, even though the ordinary headword is
_cū_.

#### Paradigm comparison

A paradigm comparison identifies the Proto-Germanic inflectional cell that
corresponds to an established Old English paradigm form. The comparison below
sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *kōz | OE headword _cū_ belongs to the nominative history of the lexeme | cū | useful background, but not the chosen comparison for _cȳ_ |
| later generalized nominative | PNWGmc *kūaz > *kūz | inferred nominative _cū_ | cū | explains the leveled headword, not the oblique target |
| dative singular oblique | *kūi | regular output: _cȳ_ | cȳ | exact match between input, output, and paradigm cell |
| genitive singular oblique | *kūiz | Ringe-Taylor: apparently _cā_; Hall: _cū(e)_, _cȳ_, _cūs_ | gen.sg. variable | too unstable to control the entry |

The dative singular is the relevant comparison form. It gives a regular path to
attested _cȳ_, while the broader Old English paradigm shows how far the oblique
_\*kū-_ grade spread beyond that one cell.

### find — OE fundene

\index[oe]{fundene@fundene}
\index[pgmc]{finthana@*fínθaną}
\index[pgmc]{fundano@*fúnðanǭ}

Derivation: citation reconstruction _\*fínθaną_; form followed here _\*fúnðanǭ_ > _fundene_ (late analogy).

#### Derivation trace

Proto input: _\*fúnðanǭ_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*fúndanǭ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Unstressed Fronting Early & \emph{*fúndænǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*fúndænæ} \\
OE Unstressed AE Merger & \emph{*fúndene} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fundene_

#### Reconstruction and comparative evidence

The inherited verb is the strong verb [_\*fínθaną_]{.iv lang=pgmc sort=finthana role=source_protoform}, continued by Old English
[_findan_]{.iv lang=oe sort=findan role=comparison_form} [@RingeTaylor2014, 344]. The form followed here, [_\*fúnðanǭ_]{.iv lang=pgmc sort=fundhano role=selected_input},
belongs to the past-participial paradigm rather than to the infinitive. It
represents an oblique singular form of the participle.

That distinction matters because the familiar dictionary form [_funden_]{.iv lang=oe sort=funden role=comparison_form} is not
the form compared here. The derivational input instead models an attested
participial form directly, rather than treating the infinitive or the ordinary
dictionary headword as primary. It therefore reaches [_fundene_]{.iv lang=oe sort=fundene role=target_form} in the form
where the trace and the attested evidence match directly.

#### Old English evidence

Bosworth-Toller records [_fundene_]{.iv lang=oe sort=fundene role=target_form} under [_findan_]{.iv lang=oe sort=findan role=comparison_form}, citing the form in
_Beón_ _þá_ herigeata swa fundene [@BosworthToller1898, 219]. Clark Hall likewise preserves the
participial stem in forms such as [_funden_]{.iv lang=oe sort=funden role=comparison_form} and _tō-fundennes_
[@ClarkHall1960, 124].

The ordinary dictionary headword for the participle is [_funden_]{.iv lang=oe sort=funden role=comparison_form}, but the
relevant comparison form for this entry is the attested oblique [_fundene_]{.iv lang=oe sort=fundene role=target_form}.
It is an Old English form in its own right, not a merely convenient probe.

#### Development to Old English

From [_\*fúnðanǭ_]{.iv lang=pgmc sort=fundhano role=selected_input}, the participial oblique develops through regular loss and
weakening of the final ending, yielding [_fundene_]{.iv lang=oe sort=fundene role=target_form}. In that cell both the
consonantism and the medial vowel history remain regular.

The broader participial paradigm then matters for interpretation. The more
familiar nominative [_funden_]{.iv lang=oe sort=funden role=comparison_form} is the ordinary dictionary form, whereas the
oblique form [_fundene_]{.iv lang=oe sort=fundene role=target_form} is the attested form compared here.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the attested oblique
participle from the more familiar nominative participial forms and keeps the
cited Old English evidence alongside the regular derivational path.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | [_\*fínθaną_]{.iv lang=pgmc sort=finthana role=source_protoform} | inherited verb [_findan_]{.iv lang=oe sort=findan role=comparison_form} | [_findan_]{.iv lang=oe sort=findan role=comparison_form} | establishes the lexeme, but not the form compared here |
| nominative participial line | [_\*fúnðanaz_]{.iv lang=pgmc sort=fundhanaz role=comparison_form} | ordinary dictionary [_funden_]{.iv lang=oe sort=funden role=comparison_form} type | [_funden_]{.iv lang=oe sort=funden role=comparison_form} | important paradigm background, but not the form compared here |
| oblique participle compared here | [_\*fúnðanǭ_]{.iv lang=pgmc sort=fundhano role=selected_input} | regular output: [_fundene_]{.iv lang=oe sort=fundene role=regular_output} | [_fundene_]{.iv lang=oe sort=fundene role=target_form} | exact match between input, output, and attested cell |

The oblique participle is the relevant comparison form. It matches the
derivational input and Old English form directly, while the nominative participial headword remains a
different presentation cell within the same paradigm.

### fright — OE fyrhte

\index[oe]{fyrhte@fyrhte}
\index[pgmc]{furxtin@*furxtīn}
\index[pgmc]{furxtinaz@*fúrxtīnaz}
\index[goth]{faurhtei@faurhtei}

Derivation: citation reconstruction _\*furxtīn_; form followed here _\*fúrxtīnaz_ > _fyrhte_ (late analogy).

#### Derivation trace

Proto input: _\*fúrxtīnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*fúrxtīna} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*fúrxtīn} \\
OE I Umlaut & \emph{*fyrxtīn} \\
NWGmc In Stem N Loss & \emph{*fyrxtī} \\
OE Unstressed Long Vowel Shortening & \emph{*fyrxti} \\
OE Med Unstressed I Lowering1 & \emph{*fyrxte} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fyrhte_

#### Reconstruction and comparative evidence

The noun belongs to the inherited in-stem abstract [_\*furxtīn_]{.iv lang=pgmc sort=furxtin role=source_protoform}, the same family
as Gothic [_faurhtei_]{.iv lang=goth sort=faurhtei role=comparison_form} [@Orel2003, 120]. The derivational input [_\*fúrxtīnaz_]{.iv lang=pgmc sort=furxtinaz role=selected_input} is not a
different lexeme but an oblique singular cell within that in-stem paradigm.

Ringe and Taylor treat the later nominative forms with _-u_ or _-o_ as
analogically remodeled [@RingeTaylor2014, 395-396]. The oblique in-stem forms
therefore preserve the older history more directly. The comparison here uses
that oblique line because it keeps the inherited pathway clearer than the
better-known lemma forms do.

#### Old English evidence

Bosworth-Toller records [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form} with textual attestation, and it also
records nominative forms such as [_fyrhtu_]{.iv lang=oe sort=fyrhtu role=comparison_form} and [_fyrhto_]{.iv lang=oe sort=fyrhto role=comparison_form}
[@BosworthToller1898, 160]. Clark Hall separately preserves adjective and verb
material under _fyrht_ / _fyrhtan_, which helps keep the noun distinct from the
adjectival family [@ClarkHall1960, 141].

The relevant comparison form is therefore the attested oblique [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form}.
The nominative lemma forms remain part of the Old English evidence, but the
Old English form here of this entry is the oblique cell.

#### Development to Old English

From [_\*fúrxtīnaz_]{.iv lang=pgmc sort=furxtinaz role=selected_input}, the oblique in-stem develops through the loss and weakening
of the final ending, yielding [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form}. The form compared here therefore
follows the ordinary Old English reduction of the abstract ending in this
paradigm.

The later nominative forms with _-u_ or _-o_ belong to a subsequent analogical
reshaping of the paradigm. The Old English form here is earlier in that sense: it is
the attested OE cell in which the inherited in-stem development remains most
transparent.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the attested oblique form from the
later remodeled nominative line.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation in-stem headword | [_\*furxtīn_]{.iv lang=pgmc sort=furxtin role=source_protoform} | broader noun-class label | wider family context | useful lexeme label, but not the cell compared here |
| remodeled nominative line | nominative in-stem forms | [_fyrhtu_]{.iv lang=oe sort=fyrhtu role=comparison_form} / [_fyrhto_]{.iv lang=oe sort=fyrhto role=comparison_form} type lemma forms | [_fyrhtu_]{.iv lang=oe sort=fyrhtu role=comparison_form} / [_fyrhto_]{.iv lang=oe sort=fyrhto role=comparison_form} | genuine OE evidence, but later remodeled |
| selected oblique singular | [_\*fúrxtīnaz_]{.iv lang=pgmc sort=furxtinaz role=selected_input} | regular output: [_fyrhte_]{.iv lang=oe sort=fyrhte role=regular_output} | [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form} | exact match between input, output, and attested cell |

The oblique in-stem form is the relevant comparison form. It yields attested
[_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form} directly, while the more familiar nominative forms belong to a later
analogical layer.

### hammer — OE hameres

\index[oe]{hameres@hameres}
\index[pgmc]{xamaras@*xámaras}
\index[pgmc]{xamaraz@*xámaraz}

Derivation: citation reconstruction _\*xámaraz_; form followed here _\*xámaras_ > _hameres_ (late analogy).

#### Derivation trace

Proto input: _\*xámaras_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xámæræs} \\
OE Unstressed AE Merger & \emph{*xámeres} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hameres_

#### Reconstruction and comparative evidence

The inherited noun is the masculine a-stem [_\*xámaraz_]{.iv lang=pgmc sort=xamaraz role=source_protoform}, reflected in Old English
citation forms such as [_hamor_]{.iv lang=oe sort=hamor role=comparison_form} and [_hamer_]{.iv lang=oe sort=hamer role=comparison_form} [@Kroonen2013, 206; @Orel2003, 197;
@ClarkHall1960, 160]. The derivational input [_\*xámaras_]{.iv lang=pgmc sort=xamaras role=selected_input} is the genitive singular of that
same noun rather than a different lexeme.

The genitive matters because the citation tradition is already mixed in its
unstressed vowel, while the oblique singular gives a cleaner comparison form.
This is a cell choice within one paradigm, not a change of stem class.

#### Old English evidence

Bosworth-Toller directly records [_hameres_]{.iv lang=oe sort=hameres role=target_form} in an Old English genitival
phrase [@BosworthToller1898, 78]. Clark Hall preserves the simplex headword as
[_hamer_]{.iv lang=oe sort=hamer role=comparison_form} / [_hamor_]{.iv lang=oe sort=hamor role=comparison_form} [@ClarkHall1960, 160].

Sievers-Brunner gives a paradigm line [_hamor_]{.iv lang=oe sort=hamor role=comparison_form} — [_hamores_]{.iv lang=oe sort=hamores role=comparison_form}, which shows that the
oblique tradition itself was not entirely uniform [@SieversBrunner1965, §245]. The
relevant comparison form here is the attested genitive singular [_hameres_]{.iv lang=oe sort=hameres role=target_form}.

#### Development to Old English

From [_\*xámaras_]{.iv lang=pgmc sort=xamaras role=selected_input}, Anglo-Frisian brightening and the subsequent merger of
unstressed _æ_ with _e_ yield [_hameres_]{.iv lang=oe sort=hameres role=target_form}. The derivation of that oblique form is
straightforward once the genitive singular cell is selected.

The noun as a whole retains a mixed citation tradition in [_hamor_]{.iv lang=oe sort=hamor role=comparison_form} and [_hamer_]{.iv lang=oe sort=hamer role=comparison_form},
and the selected oblique cell avoids making that variation carry the argument of
the entry.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the attested genitive singular
from the less stable citation tradition.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*xámaraz_]{.iv lang=pgmc sort=xamaraz role=source_protoform} | regular citation form [_hamer_]{.iv lang=oe sort=hamer role=comparison_form} / [_hamor_]{.iv lang=oe sort=hamor role=comparison_form} | [_hamor_]{.iv lang=oe sort=hamor role=comparison_form} / [_hamer_]{.iv lang=oe sort=hamer role=comparison_form} | good lexical background, but not the Old English form here |
| genitive singular | [_\*xámaras_]{.iv lang=pgmc sort=xamaras role=selected_input} | regular output: [_hameres_]{.iv lang=oe sort=hameres role=regular_output} | [_hameres_]{.iv lang=oe sort=hameres role=target_form} | exact match between input, output, and attested cell |
| later oblique tradition | oblique a-stem forms | [_hamores_]{.iv lang=oe sort=hamores role=comparison_form} type evidence | [_hamores_]{.iv lang=oe sort=hamores role=comparison_form} | attested background variant, but not the chosen comparison form |

### have — OE hæfeþ

\index[oe]{haefeth@hæfeþ}
\index[pgmc]{xabena@*xabēną}
\index[pgmc]{xabethi@*xábēθi}

Derivation: citation reconstruction _\*xabēną_; form followed here _\*xábēθi_ > _hæfeþ_ (late analogy).

#### Derivation trace

Proto input: _\*xábēθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*xábēθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*xábǣθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xæbǣθ} \\
OE Velar Fricative Palatalization & \emph{*çæbǣθ} \\
PGmc B Allophony & \emph{*çæβǣθ} \\
OE Unstressed Long Vowel Shortening & \emph{*çæβæθ} \\
OE Unstressed AE Merger & \emph{*çæβeθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hæfeþ_

#### Reconstruction and comparative evidence

The verb belongs to the inherited class-III weak paradigm usually cited under
[_\*xabēną_]{.iv lang=pgmc sort=xabena role=source_protoform} and Old English [_habban_]{.iv lang=oe sort=habban role=comparison_form} [@Kroonen2013, 237; @RingeTaylor2014, 93]. Within
that paradigm, however, the infinitive and the singular present indicative do
not continue the same stem. Ringe and Taylor distinguish a _-ja-_ stem in the
infinitive from a non-geminating -ai- / _-ē-_ stem in the 2sg and 3sg present
forms [@RingeTaylor2014, 93].

The derivational input [_\*xábēθi_]{.iv lang=pgmc sort=xabethi role=selected_input} is therefore the 3sg present cell rather than a
rephrasing of the infinitive. For the present analysis, that finite cell is the
cleaner comparator for the inherited non-geminating stem.

#### Old English evidence

The ordinary Old English headword is [_habban_]{.iv lang=oe sort=habban role=comparison_form} [@ClarkHall1960, 157].
Campbell's Anglian paradigm includes unsyncopated 3sg forms of the [_hæfed_]{.iv lang=oe sort=haefed role=comparison_form} type,
and the present paradigm therefore shows forms of the _hæf-_ type that support
the normalized target [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form} [@Campbell1959, §762].

The target form is therefore a normalized finite cell rather than the ordinary
dictionary lemma. It represents the inherited non-geminating present stem more
directly than [_habban_]{.iv lang=oe sort=habban role=comparison_form} does.

#### Development to Old English

From [_\*xábēθi_]{.iv lang=pgmc sort=xabethi role=selected_input}, the finite form yields [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form} regularly. Ringe and Taylor
discuss this non-geminating present stem under [_habban_]{.iv lang=oe sort=habban role=comparison_form}
[@RingeTaylor2014, 364]. Campbell's Anglian paradigms include unsyncopated 3sg
forms of the [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form} / [_hæfed_]{.iv lang=oe sort=haefed role=comparison_form} type [@Campbell1959, §762].

The wider lexeme is less straightforward only because the infinitive [_habban_]{.iv lang=oe sort=habban role=comparison_form}
shows later leveling. That difference in paradigm history is what makes the 3sg
present cell the more useful comparison form.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the analogically leveled citation
form from the regular 3sg present line.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | _-ja-_ stem of [_\*xabēną_]{.iv lang=pgmc sort=xabena role=source_protoform} | citation form [_habban_]{.iv lang=oe sort=habban role=comparison_form} | [_habban_]{.iv lang=oe sort=habban role=comparison_form} | important headword, but shaped by later leveling |
| 3sg present | [_\*xábēθi_]{.iv lang=pgmc sort=xabethi role=selected_input} | regular output: [_hæfeþ_]{.iv lang=oe sort=haefeth role=regular_output} | [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form} | exact match between input, output, and finite form compared here |
| syncopated finite tradition | same present stem | [_hæfþ_]{.iv lang=oe sort=haefth role=comparison_form} type evidence | [_hæfþ_]{.iv lang=oe sort=haefth role=comparison_form} | genuine later OE finite form, but not the normalized target used here |

### heaven — OE heofon

\index[oe]{heofon@heofon}
\index[pgmc]{xemenaz@*xémenaz}
\index[pgmc]{xemonu@*xémonų}

Derivation: citation reconstruction _\*xémenaz_; form followed here _\*xémonų_ > _heofon_ (late analogy).

#### Derivation trace

Proto input: _\*xémonų_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc Unstressed O Raising & \emph{*xémunų} \\
NWGmc Mn Dissimilation & \emph{*xéβunų} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*xéβonų} \\
OE Velar Fricative Palatalization & \emph{*çéβonų} \\
OE Back Mutation & \emph{*çéoβonų} \\
\mbox{OE High Vowel Apocope} & \emph{*çéoβon} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _heofon_

#### Reconstruction and comparative evidence

The inherited noun belongs to the mn-stem family cited by Kroonen as
[_\*hemina-_]{.iv lang=pgmc sort=hemina} ~ [_\*hemna-_]{.iv lang=pgmc sort=hemna} [@Kroonen2013, 220]. The derivational input [_\*xémonų_]{.iv lang=pgmc sort=xemonu} is an
oblique singular form within that paradigm rather than the lexeme-level
citation form [_\*xémenaz_]{.iv lang=pgmc sort=xemenaz}.

That difference matters for the West Saxon target. Ringe and Taylor give
northern WGmc [_\*hebun_]{.iv lang=preoe sort=hebun} > West Saxon and Northumbrian [_heofon_]{.iv lang=oe sort=heofon}, Mercian
[_heofen_]{.iv lang=oe sort=heofen} [@RingeTaylor2014, 324]. Campbell likewise gives [_heofon_]{.iv lang=oe sort=heofon} beside
[_hefen_]{.iv lang=oe sort=hefen} in the same West-Saxon _u_-umlaut environment [@Campbell1959, §210.1].

#### Old English evidence

Old English dictionaries record the standard West Saxon noun as [_heofon_]{.iv lang=oe sort=heofon},
alongside Anglian or Mercian [_hefen_]{.iv lang=oe sort=hefen} material [@ClarkHall1960, 188;
@BosworthToller1898, 43]. Campbell also cites an earlier stage [_hefzen_]{.iv lang=oe sort=hefzen} in the
history of the word [@Campbell1959, §381].

The target of this entry is the West Saxon citation form [_heofon_]{.iv lang=oe sort=heofon}. Its vowel
history points toward the oblique stem rather than the front-vocalic nominative
line.

#### Development to Old English

From [_\*xémonų_]{.iv lang=pgmc sort=xemonu}, the West Saxon line passes through the oblique-stem type
reflected in northern WGmc [_\*hebun_]{.iv lang=preoe sort=hebun} [@RingeTaylor2014, 324]. Campbell's
[_heofon_]{.iv lang=oe sort=heofon} beside [_hefen_]{.iv lang=oe sort=hefen} and earlier [_hefzen_]{.iv lang=oe sort=hefzen} show the later West-Saxon
back-mutation and suffix reshaping behind [_heofon_]{.iv lang=oe sort=heofon}
[@Campbell1959, §210.1; @Campbell1959, §381].

The front-vocalic nominative line remains important as background because it
explains the dialectal [_hefen_]{.iv lang=oe sort=hefen} type. West Saxon [_heofon_]{.iv lang=oe sort=heofon} reflects the oblique
stem that was generalized into the nominative position.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the front-vocalic nominative
line from the oblique stem selected for West Saxon _heofon_.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*xémenaz_]{.iv lang=pgmc sort=xemenaz} | front-vocalic [_hefen_]{.iv lang=oe sort=hefen} type outcome | [_hefen_]{.iv lang=oe sort=hefen} / [_heofen_]{.iv lang=oe sort=heofen} | useful control, but not the West Saxon form used here |
| selected oblique singular | [_\*xémonų_]{.iv lang=pgmc sort=xemonu} | regular output: [_heofon_]{.iv lang=oe sort=heofon} | [_heofon_]{.iv lang=oe sort=heofon} | exact match between input, output, and target |
| older pre-OE stage | inherited oblique line | earlier [_hefzen_]{.iv lang=oe sort=hefzen} stage | [_hefzen_]{.iv lang=oe sort=hefzen} | historical background for the same West Saxon development |

### live — OE lifeþ

\index[oe]{lifeth@lifeþ}
\index[pgmc]{libena@*libēną}
\index[pgmc]{libethi@*líbēθi}

Derivation: citation reconstruction _\*libēną_; form followed here _\*líbēθi_ > _lifeþ_ (late analogy).

#### Derivation trace

Proto input: _\*líbēθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*líbēθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*líbǣθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PGmc B Allophony & \emph{*líβǣθ} \\
OE Unstressed Long Vowel Shortening & \emph{*líβæθ} \\
OE Unstressed AE Merger & \emph{*líβeθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lifeþ_

#### Reconstruction and comparative evidence

The inherited verb belongs to the class-III weak family cited by Kroonen under
_\*libēn-_, reflected in Old English [_libban_]{.iv lang=oe sort=libban role=comparison_form} [@Kroonen2013, 336]. Ringe and
Taylor show that the paradigm also contained a separate 3sg present stem,
continued in late Northumbrian [_lifed_]{.iv lang=oe sort=lifed role=comparison_form}, which they treat as an archaism
[@RingeTaylor2014, 364].

The derivational input [_\*líbēθi_]{.iv lang=pgmc sort=libethi role=selected_input} therefore represents a finite present cell rather
than the citation infinitive. That distinction matters because the ordinary
later lemma tradition also includes remodeled forms such as [_lifian_]{.iv lang=oe sort=lifian role=comparison_form}.

#### Old English evidence

The ordinary lemma tradition centers on [_libban_]{.iv lang=oe sort=libban role=comparison_form} and, in later remodeling,
[_lifian_]{.iv lang=oe sort=lifian role=comparison_form}. For this entry, however, the relevant comparison form is the archaic
3sg present attested as [_lifed_]{.iv lang=oe sort=lifed role=comparison_form}, here
normalized as [_lifeþ_]{.iv lang=oe sort=lifeth role=target_form} [@RingeTaylor2014, 364; @Campbell1959, §762].

The target is thus a normalized finite form, not the ordinary dictionary lemma.
Its value lies in preserving the older present-stem history more clearly than
the remodeled lemma tradition does.

#### Development to Old English

From [_\*líbēθi_]{.iv lang=pgmc sort=libethi role=selected_input}, regular reduction of the final syllable and later weakening of
the unstressed vowel yield [_lifeþ_]{.iv lang=oe sort=lifeth role=regular_output}. The attested spelling [_lifed_]{.iv lang=oe sort=lifed role=comparison_form} belongs to the
same finite form in late Northumbrian orthography [@Campbell1959, §762;
@RingeTaylor2014, 364].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the archaic finite cell from the
ordinary infinitival and later remodeled lemma lines.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive line | [_\*libēną_]{.iv lang=pgmc sort=libena role=source_protoform} | OE [_libban_]{.iv lang=oe sort=libban role=comparison_form} headword tradition | [_libban_]{.iv lang=oe sort=libban role=comparison_form} | establishes the lexeme, but not the Old English form here |
| 3sg present | [_\*líbēθi_]{.iv lang=pgmc sort=libethi role=selected_input} | regular output: [_lifeþ_]{.iv lang=oe sort=lifeth role=regular_output}; attested [_lifed_]{.iv lang=oe sort=lifed role=comparison_form} | [_lifed_]{.iv lang=oe sort=lifed role=comparison_form}, normalized here as [_lifeþ_]{.iv lang=oe sort=lifeth role=target_form} | selected archaic finite cell |
| later remodeled present tradition | later class-II-type forms | [_lifian_]{.iv lang=oe sort=lifian role=comparison_form} and related finite remodeling | [_lifian_]{.iv lang=oe sort=lifian role=comparison_form} | genuine OE development, but secondary to the cell compared here |

### man — OE mannes

\index[oe]{mannes@mannes}
\index[pgmc]{mannas@*mánnas}
\index[pgmc]{mannaz@*mánnaz}

Derivation: citation reconstruction _\*mánnaz_; form followed here _\*mánnas_ > _mannes_ (late analogy).

#### Derivation trace

Proto input: _\*mánnas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mánnæs} \\
OE Unstressed AE Merger & \emph{*mánnes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _mannes_

#### Reconstruction and comparative evidence

The lexeme-level reconstruction is not uniform. Kroonen cites _\*mannan-_, and
Orel has _\*mannz_ [@Kroonen2013, 354; @Orel2003, 299]. The derivational input [_\*mánnas_]{.iv lang=pgmc sort=mannas role=selected_input}
belongs to a different level: it is the genitive-singular cell chosen for the
Old English comparison.

That distinction matters because the target of this entry is not the ordinary
citation form. The cell compared here is the one that keeps the geminate medial
before the ending.

#### Old English evidence

Campbell gives the paradigm [_mann_]{.iv lang=oe sort=mann role=comparison_form}, [_man_]{.iv lang=oe sort=man role=comparison_form} / [_mannes_]{.iv lang=oe sort=mannes role=target_form} / _menn_
[@Campbell1959, §621].
Sievers-Brunner likewise cites [_man_]{.iv lang=oe sort=man role=comparison_form} [_mannes_]{.iv lang=oe sort=mannes role=target_form} [@SieversBrunner1965, §226]. He
also explains that word-final simplification underlies forms such as [_man_]{.iv lang=oe sort=man role=comparison_form}
beside inflected [_monnes_]{.iv lang=oe sort=monnes role=comparison_form} [@SieversBrunner1965, §231]. Clark Hall keeps the dictionary headword under [_mann_]{.iv lang=oe sort=mann role=comparison_form}
[@ClarkHall1960, 197].

The relevant comparison form is therefore the attested genitive singular
[_mannes_]{.iv lang=oe sort=mannes role=target_form}, not the citation lemma [_mann_]{.iv lang=oe sort=mann role=comparison_form}.

#### Development to Old English

Campbell's paradigm mann, _man_ / _mannes_ / _menn_ confirms the selected genitive
singular _mannes_ [@Campbell1959, §621]. In the present analysis, _\*mánnas_
develops through Anglo-Frisian brightening and later unstressed merger to
_mannes_. In this cell the geminate remains medial before _-es_. The citation
form behaves differently because word-final gemination was simplified in Old
English [@SieversBrunner1965, §231].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the citation-form line from the
genitive singular.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*mannăz_]{.iv lang=pgmc sort=mannaz role=source_protoform} | expected citation-form outcome [_man_]{.iv lang=oe sort=man role=regular_output} | [_mann_]{.iv lang=oe sort=mann role=comparison_form} / [_monn_]{.iv lang=oe sort=monn role=comparison_form} | establishes the lexeme, but not the Old English form here |
| accusative singular | [_\*manną_]{.iv lang=pgmc sort=manna role=comparison_form} | expected [_man_]{.iv lang=oe sort=man role=regular_output} | [_man_]{.iv lang=oe sort=man role=comparison_form} | same word-final simplification as the nominative |
| dative singular | [_\*mannăi_]{.iv lang=pgmc sort=mannai role=comparison_form} | expected [_manne_]{.iv lang=oe sort=manne role=regular_output} | [_manne_]{.iv lang=oe sort=manne role=comparison_form} | preserves medial _nn_, but not the chosen cell |
| genitive singular | [_\*mánnas_]{.iv lang=pgmc sort=mannas role=selected_input} | regular output: [_mannes_]{.iv lang=oe sort=mannes role=regular_output} | [_mannes_]{.iv lang=oe sort=mannes role=target_form} | exact match between input, output, and attested comparator |

### meed — OE meorde

\index[oe]{meorde@meorde}
\index[pgmc]{mizdai@*mízdai}
\index[pgmc]{mizdo@*mizdō}

Derivation: citation reconstruction _\*mizdō_; form followed here _\*mízdai_ > _meorde_ (late analogy).

#### Derivation trace

Proto input: _\*mízdai_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*mírdē} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc I Lowering & \emph{*mérdē} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*méordē} \\
OE Unstressed Long Vowel Shortening & \emph{*méorde} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _meorde_

#### Reconstruction and comparative evidence

The lexeme-level reconstruction is [_\*mizdō_]{.iv lang=pgmc sort=mizdo role=source_protoform}, but the derivational input [_\*mízdai_]{.iv lang=pgmc sort=mizdai role=selected_input}
is a dative-singular cell rather than the citation form. That distinction is
important because the Old English evidence for the _meord_ side is oblique.

The wider history of competing _mēd_ remains disputed. Kroonen and Fulk
explain it through some form of _z_-loss and compensatory lengthening
[@Kroonen2013, 410; @Fulk2018, 69], while Orel keeps
a doublet analysis [@Orel2003, 311]. The comparison here concerns the
attested oblique line _meorde_.

#### Old English evidence

The directly attested forms are obliques: [_meorde_]{.iv lang=oe sort=meorde role=target_form} as a dative singular and
[_meorda_]{.iv lang=oe sort=meorda role=comparison_form} as a genitive plural [@BrightCassidyRingler1971, 328; @BosworthToller1898, 647].
Lexicographers reconstruct a bare nominative [_meord_]{.iv lang=oe sort=meord role=comparison_form} from those obliques, while
West Saxon prose more commonly shows the competing doublet _mēd_
[@ClarkHall1960, 214; @BosworthToller1898, 647].

The target of this entry is therefore the attested oblique [_meorde_]{.iv lang=oe sort=meorde role=target_form}, not the
reconstructed lemma [_meord_]{.iv lang=oe sort=meord role=comparison_form} and not the better-known West Saxon citation form
_mēd_.

#### Development to Old English

Ringe and Taylor give the broader noun history as PGmc _\*mizdo_ > PWGmce _\*mizdu_ > OE _meord_ ~ _méd_ [@RingeTaylor2014, 99]. The fuller oblique-cell path modeled
here spells out the intermediate rhotacism, monophthongization, lowering,
breaking, and unstressed-shortening steps needed for the selected dative-singular
comparison.

This entry therefore follows the attested oblique line within the broader
development. It does not depend on a full decision about the history of the
competing _mēd_ tradition.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the attested oblique target from
the broader lemma history.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*mizdō_]{.iv lang=pgmc sort=mizdo role=source_protoform} | inferred lemma outcome [_meord_]{.iv lang=oe sort=meord role=comparison_form} | [_meord_]{.iv lang=oe sort=meord role=comparison_form} | useful background, but the bare lemma is reconstructed rather than directly attested |
| selected dative singular | [_\*mízdai_]{.iv lang=pgmc sort=mizdai role=selected_input} | regular output: [_meorde_]{.iv lang=oe sort=meorde role=regular_output} | [_meorde_]{.iv lang=oe sort=meorde role=target_form} | exact match between derivational input and attested target |
| genitive singular | [_\*mizdōz_]{.iv lang=pgmc sort=mizdoz role=comparison_form} | regular output: [_meorde_]{.iv lang=oe sort=meorde role=regular_output} | [_meorde_]{.iv lang=oe sort=meorde role=target_form} | converges on the same attested string, but the dat.sg. has the clearest direct support |
| genitive plural control | plural oblique line | attested [_meorda_]{.iv lang=oe sort=meorda role=comparison_form} | [_meorda_]{.iv lang=oe sort=meorda role=comparison_form} | confirms the broader oblique tradition, but not the chosen singular target |

### night — OE niht

\index[oe]{niht@niht}
\index[pgmc]{naxti@*náxti}
\index[pgmc]{naxtz@*náxtz}

Derivation: citation reconstruction _\*náxtz_; form followed here _\*náxti_ > _niht_ (late analogy).

#### Derivation trace

Proto input: _\*náxti_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*næxti} \\
OE Breaking & \emph{*neaxti} \\
OE I Umlaut & \emph{*niexti} \\
OE Ws Palatal Umlaut & \emph{*nixti} \\
\mbox{OE High Vowel Apocope} & \emph{*nixt} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _niht_

#### Reconstruction and comparative evidence

Ringe and Taylor cite gen.sg. _\*nahtiz_, dat.sg. _\*nahti_, and nom.pl. _\*nahtiz_ for the high-vowel side of the paradigm, and derive West Saxon _niht_
from that side [@RingeTaylor2014, 240]. The citation reconstruction _\*náxtz_
therefore belongs to the nominative-like headword, while the derivational input
_\*náxti_ represents the dative-singular cell.

That distinction matters because the word later became the model for endingless
datives. Ringe and Taylor explicitly explain forms such as _dæg_ by analogy
with dat. sg. _niht_ < _\*nahti_ [@RingeTaylor2014, 380].

#### Old English evidence

Clark Hall lemmatizes _niht_ and cross-references forms such as _neaht_,
_neht_, and _nieht_ [@ClarkHall1960, 215]. Campbell likewise preserves the
fluctuation between _neaht_ and _niht_, giving genitive _nihte, nihtes_,
dative _niht, nihte_, nominative plural _niht_, and the contrasting
plural-side forms represented by _neahtas_ [@Campbell1959, §628.3].

The comparison form used here is therefore an attested Old English _niht_, not a
reconstructed substitute. The broader lexical record still preserves the
non-umlauted side of the paradigm in _neaht_-type forms.

#### Development to Old English

Ringe and Taylor derive West Saxon _niht_ from _\*nahti_ via _\*nehti_ and
_\*neahti_ [@RingeTaylor2014, 240]. Campbell and Brunner preserve the
contrasting non-umlauted _neaht_-type forms elsewhere in the paradigm
[@Campbell1959, §628.3; @SieversBrunner1965, §284].

The modeled path is therefore _\*náxti_ > _\*næxti_ > _\*neaxti_ > _\*niexti_ > _\*nixti_ > _niht_.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It identifies the inherited cell that matches the
attested Old English form.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *náxtz | expected non-umlauted outcome _neaht_ | neaht | useful background, but not the comparison used for _niht_ |
| selected dative singular | *náxti | regular output: _niht_ | niht | exact match between input, output, and paradigm cell |

### rest — OE ræste

\index[oe]{raeste@ræste}
\index[pgmc]{rasto@*rastō}
\index[pgmc]{rastoz@*rástōz}

Derivation: citation reconstruction _\*rastō_; form followed here _\*rástōz_ > _ræste_ (late analogy).

#### Derivation trace

Proto input: _\*rástōz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*rástō} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Surviving Bimoric O Unrounding & \emph{*rástā} \\
Anglo Frisian Brightening & \emph{*ræstǣ} \\
OE Unstressed Long Vowel Shortening & \emph{*ræstæ} \\
OE Unstressed AE Merger & \emph{*ræste} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ræste_

#### Reconstruction and comparative evidence

Kroonen treats the noun as a feminine ō-stem _\*rastō-_, continued by Old English
_ræst_ [@Kroonen2013, 445]. The form followed here, _\*rástōz_, therefore does not replace
the lexeme-level headword. It identifies one oblique singular cell on the side of
the paradigm that yields _ræste_.

The source tradition used here labels that cell specifically as genitive
singular, but the broader local synthesis of the ō-stem paradigm shows that the
oblique singulars converge on the same front-vocalic _ræste_ side, in contrast
to a nominative singular that would remain _rast_.

#### Old English evidence

The ordinary Old English citation form is _ræst_ [@Kroonen2013, 445]. Clark
Hall likewise gives _ræst_ [@ClarkHall1960, 239]. Bosworth-Toller also preserves oblique uses of _ræste_, including prepositional
examples such as on _ræste_ and _tó_ _ræste_ [@BosworthToller1898, 121].

The comparison form used here is therefore an attested oblique _ræste_, not a
reconstructed surrogate. The dictionary headword _ræst_ remains an equally real
part of the Old English record.

#### Development to Old English

Once final _\*z_ is lost, the derivational input moves through the front-vocalic
oblique side of the paradigm rather than the back-vocalic nominative side. In
the modeled derivation, the surviving final long vowel is first exposed,
unrounded, fronted, shortened, and then reduced to the final _-e_ of _ræste_.

The key point is the paradigm split. Nominative _\*rastō_ yields a regular _rast_,
whereas the selected oblique input yields _ræste_. The later citation form _ræst_
is best explained as leveling from that oblique _ræst-_ stem.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the nominative citation form
from the oblique singular chosen here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *rastō | expected regular outcome _rast_ | ræst | useful background, but not the cell that matches attested oblique _ræste_ |
| selected oblique singular | *rástōz | regular output: _ræste_ | ræste | exact match between derivational input and attested OE oblique form |

### shoulder — OE sċuldrum

\index[oe]{sculdrum@sċuldrum}
\index[pgmc]{skuldramiz@*skúldramiz}
\index[pgmc]{skuldro@*skuldrō}

Derivation: citation reconstruction _\*skuldrō_; form followed here _\*skúldramiz_ > _sċuldrum_ (late analogy).

#### Derivation trace

Proto input: _\*skúldramiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.560\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.280\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
NWGmc A To U Before M & \emph{*skúldrumiz} \\
PWGmc Early I Apocope & \emph{*skúldrumz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*skúldrum} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Sk Palatalization & \emph{*ʃúldrum} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċuldrum_

#### Reconstruction and comparative evidence

The handbooks do not agree on the reconstruction of the Germanic word. Orel gives [_\*skuldr(j)ō_]{.iv lang=pgmc sort=skuldrjo role=source_protoform}, a feminine ō-/jō-stem, and explicitly notes that Old English [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form} is masculine beside OFrisian [_skulder_]{.iv lang=ofris sort=skulder role=comparison_form}, Middle Low German _schulder_, and Old High German [_scultra_]{.iv lang=ohg sort=scultra role=comparison_form}, [_scultirra_]{.iv lang=ohg sort=scultirra role=comparison_form} [@Orel2003, 345]. Kroonen reconstructs [_\*skuldra-_]{.iv lang=pgmc sort=skuldra role=source_protoform}, a masculine a-stem, and derives the Old High German feminine forms from [_\*skuldrjōn-_]{.iv lang=pgmc sort=skuldrjon role=source_protoform} [@Kroonen2013, 478]. Ringe and Taylor cite PWGmc [_\*skuldru_]{.iv lang=pwgmc sort=skuldru role=comparison_form} for the Old English branch [@RingeTaylor2014, 142].

These forms imply different stem classes and different expectations for the Old English inflection. The question is which inflectional cell best aligns with the Old English evidence.

A dative/instrumental plural form [_\*skúldramiz_]{.iv lang=pgmc sort=skuldramiz role=selected_input} aligns with the inherited plural ending that later yields Old English _-um_, and it corresponds directly to the attested dative plural discussed below.

#### Old English evidence

The ordinary Old English headword is [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form}. Clark Hall lemmatizes [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form} as the normal dictionary form [@ClarkHall1960, 257]. Bosworth-Toller also preserves the dative plural [_sculdrum_]{.iv lang=oe sort=sculdrum role=comparison_form} [@BosworthToller1898, 85].

Bosworth-Toller's Supplement records a weak-feminine [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form}, an [@BosworthToller1898, 699], so [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form} belongs to the Old English record beside the stronger masculine paradigm headed by [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form}. Brunner and Luick also record later spellings such as [_sceoldor_]{.iv lang=oe sort=sceoldor role=comparison_form} and the i-mutated dative plural [_scyldrum_]{.iv lang=oe sort=scyldrum role=comparison_form}, which reflect secondary phonological and analogical reshaping within Old English [@SieversBrunner1965, §92.2.a; @Luick1914, 230].

The singular and plural evidence point to different parts of the paradigm. The relevant comparison form here is the attested dative plural [_sċuldrum_]{.iv lang=oe sort=sculdrum role=target_form}. The spelling with _sċ-_ is a normalized representation of the same Old English initial cluster.

#### Development to Old English

Proto-Germanic _\*skúldramiz_ can be interpreted as a dative/instrumental plural form. In this environment the post-tonic _a_ before _m_ is raised to _u_, giving a form of the _\*skúldrumiz_ type. Unstressed _u_ is regularly preserved before _m_, especially in the dative plural ending _-um_: Campbell states this explicitly, and Hogg formulates the same condition for the dative plural inflexion [@Campbell1959, §373; @Hogg1992, §3.3.1.3]. Brunner points in the same direction by excluding _m_ from the environments in which medial _o_ became general in West Saxon [@SieversBrunner1965, §44 Anm. 7].

Subsequent reduction of the ending removes the final _\*i_ and _\*z_, so that the inflectional ending appears in Old English as _-um_. The initial cluster is written here as _sċ-_, and the development is _\*skúldramiz_ > _\*skúldrumiz_ > _\*skúldrum_ > _sċuldrum_.

#### Paradigm comparison

A paradigm comparison identifies the Proto-Germanic inflectional cell that corresponds to an established Old English paradigm form. The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| singular-oriented citation input | [_\*skúldrō_]{.iv lang=pgmc sort=skuldro role=comparison_form} | probe output: [_sċoldor_]{.iv lang=oe sort=scoldor role=regular_output} | [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form} | fails: the singular output has root _o_, not the attested _u_ |
| serious plural-based singular alternative | [_\*skúldru_]{.iv lang=pwgmc sort=skuldru role=comparison_form} | probe output: [_sċuldor_]{.iv lang=oe sort=sculdor role=regular_output} | [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form} | close formally, but it compares a plural-stage input with a singular form |
| dat./inst.pl. input | [_\*skúldramiz_]{.iv lang=pgmc sort=skuldramiz role=selected_input} | regular output: [_sċuldrum_]{.iv lang=oe sort=sculdrum role=target_form} | [_sculdrum_]{.iv lang=oe sort=sculdrum role=comparison_form} | matches both the output and the dative plural comparison form |
| later weak-feminine singular | — | OE [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form} | [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form} | secondary doublet, useful as a control rather than the inherited target |

The dative plural line is decisive because it matches both the output and the paradigm cell of Old English [_sculdrum_]{.iv lang=oe sort=sculdrum role=comparison_form}. Singular-oriented candidates either lower the root vowel or compare unlike cells.

### shove — OE sċēaf

\index[oe]{sceaf@sċēaf}
\index[pgmc]{skaub@*skáub}
\index[pgmc]{skeubana@*skéubaną}

Derivation: citation reconstruction _\*skéubaną_; form followed here _\*skáub_ > _sċēaf_ (late analogy).

#### Derivation trace

Proto input: _\*skáub_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*skáeub} \\
OE Diphthong Leveling & \emph{*skēab} \\
PGmc B Allophony & \emph{*skēaβ} \\
OE Sk Palatalization & \emph{*ʃēaβ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēaf_

#### Reconstruction and comparative evidence

Kroonen reconstructs the strong verb as _\*skeuban-_ ~ _\*skūban-_ and cites Old
English present forms _scēofan_, _scūfan_ [@Kroonen2013, 444]. Those
present-system forms belong to the same verb family, but the comparison here
uses the singular preterite _\*skáub_, not the infinitive.

#### Old English evidence

The ordinary dictionary verb is _scūfan_/_scēofan_, but the preterite itself is
well attested. Bright gives the principal parts _scufan, sceaf, scufon, scofen_
[@BrightCassidyRingler1971, 347]. Sweet gives the same paradigm [@Sweet1953, 29].
The normalized form here is _sċēaf_,
regularizing the attested spellings _sceaf_ and prefixed _āsceaf_.

#### Development to Old English

From _\*skáub_, the development is straightforward. _\*au_ fronts and levels to
_ēa_, final _\*b_ becomes a fricative and is written _f_, and initial _\*sk-_
undergoes the usual Old English palatalized spelling in this environment. The
derivation therefore gives _\*skáub_ > _\*skáeub_ > _\*skēab_ > _\*skēaβ_ > _sċēaf_.

#### Paradigm comparison

A paradigm comparison is needed here because the ordinary citation verb and
_sċēaf_ belong to different cells of the same strong paradigm. The comparison
below is manual.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | *skéubaną | inherited infinitive line _sċēofan_; present system also leveled _scūfan_ | scēofan / scūfan | necessary background, but not the comparison used for _sċēaf_ |
| 1/3 sg. preterite | *skáub | documented regular output: _sċēaf_ | sċēaf | direct match for the singular preterite |
| preterite plural | *skúbun | later leveled plural _scufon_ beside expected _sċufun_ under the corrected cascade | scufon | poorer comparison for the singular-preterite target |
| past participle | *skúbanaz | attested participial line _scofen_ | scofen | valid alternative cell, but not the form compared here |

### span — OE spanne

\index[oe]{spanne@spanne}
\index[pgmc]{spannai@*spánnai}
\index[pgmc]{spanno@*spannō}

Derivation: citation reconstruction _\*spannō_; form followed here _\*spánnai_ > _spanne_ (late analogy).

#### Derivation trace

Proto input: _\*spánnai_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*spánnē} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*spánne} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _spanne_

#### Reconstruction and comparative evidence

Seebold gives Old English _spann_ under this noun family [@Seebold1970, 450].
The form followed here, _\*spánnai_, is therefore not a rival headword, but the
specific dative singular form compared on the model of the feminine ō-stem
paradigm [@SieversBrunner1965, §252; @SieversBrunner1965, §255.2].

#### Old English evidence

The reviewed lexicographic evidence more directly supports the citation noun
_spann_ than the exact form _spanne_. Clark Hall gives _spann_
[@ClarkHall1960, 286], and _spanne_ is accordingly treated as the regular
dative singular form compared here rather than as a dictionary headword.

#### Development to Old English

Citation _\*spannō_ yields _span_. The oblique cell _\*spánnai_ therefore
supplies the conservative comparison form: it preserves the medial geminate and
yields _spanne_, while citation _\*spannō_ gives the nominative background form.

#### Paradigm comparison

The comparison below sets the citation form beside the dative singular form
compared here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *spannō | regular output: _span_ | spann | useful citation-form background, but not the form compared here |
| dative singular compared here | *spánnai | regular output: _spanne_ | spanne | exact match for that conservative form |

### thistle — OE þistles

\index[oe]{thistles@þistles}
\index[pgmc]{thestilaz@*θéstilaz}
\index[pgmc]{thistilas@*θístilas}

Derivation: citation reconstruction _\*θéstilaz_; form followed here _\*θístilas_ > _þistles_ (late analogy).

#### Derivation trace

Proto input: _\*θístilas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*θístilæs} \\
OE L Adjacent Syncope & \emph{*θístlæs} \\
OE Unstressed AE Merger & \emph{*θístles} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þistles_

#### Reconstruction and comparative evidence

Orel prints _\*þe(x)stilaz_ for the lexeme [@Orel2003, 458]. The comparative
label _\*θéstilaz_ therefore remains in view as the lexeme-level headword, while
the derivational input _\*θístilas_ is a specific genitive singular cell.

#### Old English evidence

The ordinary simplex headword tradition is broken _þistel_ / _ðistel_. Clark
Hall gives _ðistel_ as the noun headword [@ClarkHall1960, 326]. The Old English form here
here is the genitive singular _þistles_, which preserves the same stem in an
oblique form where the cluster is medial.

#### Development to Old English

Campbell's discussion of cluster nouns shows the contrast clearly. Simplex forms
often develop a parasite vowel in word-final obstruent + sonorant clusters,
while comparable medial clusters remain unbroken; his examples include _hrefn_,
_tacn_, _wépn_, and _botm_ beside forms with parasitic vowels elsewhere in the
same lexical class [@Campbell1959, 151]. The genitive singular _\*θístilas_
therefore supplies the conservative comparison form: the cluster is medial and
the regular development yields _þistles_, while the simplex nominative belongs
to the broken headword tradition _þistel_.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It shows the contrast between the citation form
and the genitive singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *θéstilaz | computed output: _þistl_ | þistel | useful citation-form background, but not the Old English form here |
| genitive singular | *θístilas | computed output: _þistles_ | þistles | exact match for the conservative cell |

### make (iptv.2sg) — OE maca

\index[oe]{maca@maca}
\index[pgmc]{mako@*mákô}
\index[pgmc]{makona@*makōną}

Derivation: citation reconstruction _\*makōną_; form followed here _\*mákô_ > _maca_ (late analogy).

#### Derivation trace

Proto input: _\*mákô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mækô} \\
OE A Restoration & \emph{*makô} \\
OE Unstressed Long Vowel Shortening & \emph{*maka} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _maca_

#### Reconstruction and comparative evidence

The make-family belongs to the Old English class-II weak verbs. Campbell cites
_lapian,_ [_macian_]{.iv lang=oe sort=macian role=comparison_form} among verbs with restored _a_ [@Campbell1959, §159]. Ringe and
Taylor place the Germanic verb in the same class, comparing West Germanic
continuants such as Old Frisian [_makia_]{.iv lang=ofris sort=makia role=comparison_form}, Old Saxon [_makon_]{.iv lang=os sort=makon role=comparison_form}, and Old High German
[_mahhon_]{.iv lang=ohg sort=mahhon role=comparison_form} [@RingeTaylor2014, 191].

The derivational input [_\*mákô_]{.iv lang=pgmc sort=mako role=selected_input} is not the citation form of the lexeme but a finite
paradigm cell. Ringe and Taylor give the class-II weak imperative singular as
-a < _\*-ō_, which makes this cell the relevant comparison point for the Old
English form treated here [@RingeTaylor2014, 314].

#### Old English evidence

The dictionary headword is [_macian_]{.iv lang=oe sort=macian role=comparison_form} [@ClarkHall1960, 193]. The form compared here in this
entry is therefore not the lemma but the imperative singular [_maca_]{.iv lang=oe sort=maca role=target_form}, chosen as a
paradigm form beside the headword [_macian_]{.iv lang=oe sort=macian role=comparison_form} and the related finite form [_macaþ_]{.iv lang=oe sort=macath role=comparison_form}.

That distinction matters for the comparison. The lexical history of the verb is
still the history of _macian_, but the finite cell isolates the regular outcome
of trimoric _\*ō_ more cleanly than the citation form does.

#### Development to Old English

From _\*mákô_, Anglo-Frisian brightening first gives _\*mækô_. Campbell cites
_macian_ among the class-II verbs with restored _a_ [@Campbell1959, §159].
Ringe and Taylor's class-II weak imperative singular -a < _\*-ō_ then supports
the later finite ending [@RingeTaylor2014, 314].

The same development explains why earlier fronted forms of the _mæċa_ type do
not control the entry. Once trimoric _\*ô_ is treated as a back-vocalic trigger
for restoration, the imperative singular falls into line with the broader
_macian_ family.

#### Paradigm comparison

A paradigm comparison identifies which finite cell of the make-family matches
the Old English form chosen here. The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*mákōjaną_]{.iv lang=pgmc sort=makojana role=source_protoform} | comparative continuation [_macian_]{.iv lang=oe sort=macian role=comparison_form} | [_macian_]{.iv lang=oe sort=macian role=comparison_form} | ordinary headword of the verb, but not the finite form compared here |
| imperative singular | [_\*mákô_]{.iv lang=pgmc sort=mako role=selected_input} | regular output: [_maca_]{.iv lang=oe sort=maca role=regular_output} | [_maca_]{.iv lang=oe sort=maca role=target_form} | exact match between input, output, and selected paradigm form |
| present third singular companion | [_\*mákōθi_]{.iv lang=pgmc sort=makothi role=comparison_form} | comparative companion [_macaþ_]{.iv lang=oe sort=macath role=comparison_form} | [_macaþ_]{.iv lang=oe sort=macath role=comparison_form} | useful family control, but not the target of this entry |

### make (3sg) — OE macaþ

\index[oe]{macath@macaþ}
\index[pgmc]{makona@*makōną}
\index[pgmc]{makothi@*mákōθi}

Derivation: citation reconstruction _\*makōną_; form followed here _\*mákōθi_ > _macaþ_ (late analogy).

#### Derivation trace

Proto input: _\*mákōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*mákōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mækōθ} \\
OE A Restoration & \emph{*makōθ} \\
OE Late O Shortening & \emph{*makaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _macaþ_

#### Reconstruction and comparative evidence

Kroonen derives the Old English verb from [_\*makōjan-_]{.iv lang=pgmc sort=makojan role=source_protoform} on the make-family base _\*maka-_ [@Kroonen2013, 350]. Ringe and Taylor likewise derive Old English [_macian_]{.iv lang=oe sort=macian role=comparison_form} from PWGmc [_\*makon_]{.iv lang=os sort=makon role=comparison_form} through _\*mekojan_ [@RingeTaylor2014, 191].

The derivational input [_\*mákōθi_]{.iv lang=pgmc sort=makothi role=selected_input} is therefore a finite 3sg cell of the same family, not the citation form of the verb.

#### Old English evidence

Clark Hall lemmatizes the verb as [_macian_]{.iv lang=oe sort=macian role=comparison_form} [@ClarkHall1960, 193]. The relevant comparison form here is the normalized present-third-singular [_macaþ_]{.iv lang=oe sort=macath role=target_form}, set beside the dictionary headword and the related imperative singular [_maca_]{.iv lang=oe sort=maca role=comparison_form}.

Campbell's class-II paradigm makes the ordinary 3sg ending _-aþ_, while his dialect survey allows secondary _-e-_ spellings in some traditions [@Campbell1959, §356.4; @Campbell1959, §757]. _Macaþ_ is thus the regular comparison form for the non-_j_ 3sg cell.

#### Development to Old English

After early loss of final _-i_, _\*mákōθi_ yields _\*mákōθ_. Anglo-Frisian brightening gives _\*mækōθ_, but Campbell lists _macian_ among the class-II verbs with restored _a_, so the stem returns to _mak-_ before the ending is reduced [@Campbell1959, §159].

The ending then follows the ordinary class-II 3sg development. Campbell's lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ and Ringe and Taylor's discussion of stable _a_ in the finite non-_j_ cells point to _\*makōθ_ > _\*makaθ_ > _macaþ_ [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected 3sg cell from the make-family lemma and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*makōjaną_]{.iv lang=pgmc sort=makojana role=source_protoform} | dictionary headword [_macian_]{.iv lang=oe sort=macian role=comparison_form} | [_macian_]{.iv lang=oe sort=macian role=comparison_form} | family background, but not the cell compared here |
| 3sg present | [_\*mákōθi_]{.iv lang=pgmc sort=makothi role=selected_input} | regular output [_macaþ_]{.iv lang=oe sort=macath role=regular_output} | [_macaþ_]{.iv lang=oe sort=macath role=target_form} | exact match |
| imperative singular companion | [_\*mákô_]{.iv lang=pgmc sort=mako role=comparison_form} | related finite form [_maca_]{.iv lang=oe sort=maca role=comparison_form} | [_maca_]{.iv lang=oe sort=maca role=comparison_form} | useful control, but not the target |

### bore (iptv.2sg) — OE bora

\index[oe]{bora@bora}
\index[pgmc]{buro@*búrô}
\index[pgmc]{burona@*burōną}

Derivation: citation reconstruction _\*burōną_; form followed here _\*búrô_ > _bora_ (late analogy).

#### Derivation trace

Proto input: _\*búrô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bórô} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*bóra} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bora_

#### Reconstruction and comparative evidence

Kroonen reconstructs the bore-family verb as _\*burojan-_ and cites Old English _borian_ among its continuants [@Kroonen2013, 85]. Ringe and Taylor give the class-II weak imperative singular as -a < _\*-ō_ [@RingeTaylor2014, 314].

The form followed here, _\*búrô_, is therefore an imperative cell of the same family, not the citation form of the verb.

#### Old English evidence

Clark Hall lemmatizes the verb as _borian_ [@ClarkHall1960, 48]. The comparison form here is the normalized imperative singular _bora_, used beside the headword and the related 3sg form _boraþ_.

The imperative is thus a paradigm form rather than a replacement for the dictionary lemma. It is the most direct Old English comparator for the non-_j_ finite cell represented by _\*búrô_.

#### Development to Old English

Northwest Germanic lowering first gives _\*bórô_ from _\*búrô_, and late shortening of the unstressed long vowel then yields _\*bóra_, whence _bora_.

Ringe and Taylor's class-II imperative singular -a < _\*-ō_ points to exactly this type of outcome [@RingeTaylor2014, 314]. The form compared here therefore isolates the regular finite-cell development more cleanly than the remodelled infinitive does.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected imperative cell from the bore-family lemma and from the companion 3sg form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*burōjaną_]{.iv lang=pgmc sort=burojana role=source_protoform} | dictionary headword [_borian_]{.iv lang=oe sort=borian role=comparison_form} | [_borian_]{.iv lang=oe sort=borian role=comparison_form} | family background, but not the cell compared here |
| imperative singular | [_\*búrô_]{.iv lang=pgmc sort=buro role=selected_input} | regular output [_bora_]{.iv lang=oe sort=bora role=regular_output} | [_bora_]{.iv lang=oe sort=bora role=target_form} | exact match |
| 3sg present companion | [_\*búrōθi_]{.iv lang=pgmc sort=burothi role=comparison_form} | related finite form [_boraþ_]{.iv lang=oe sort=borath role=comparison_form} | [_boraþ_]{.iv lang=oe sort=borath role=comparison_form} | useful control, but not the target |

### bore (3sg) — OE boraþ

\index[oe]{borath@boraþ}
\index[pgmc]{burona@*burōną}
\index[pgmc]{burothi@*búrōθi}

Derivation: citation reconstruction _\*burōną_; form followed here _\*búrōθi_ > _boraþ_ (late analogy).

#### Derivation trace

Proto input: _\*búrōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*búrōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bórōθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Late O Shortening & \emph{*bóraθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _boraþ_

#### Reconstruction and comparative evidence

Kroonen reconstructs the bore-family verb as _\*burojan-_ and cites Old English _borian_ among its reflexes [@Kroonen2013, 85]. The form compared here isolates the finite 3sg cell _\*búrōθi_ rather than the infinitive.

Campbell's class-II pattern lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ and Ringe and Taylor's account of stable _a_ in the class-II 2sg and 3sg make this finite cell the relevant comparison form for the ending [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Old English evidence

Clark Hall lemmatizes the verb as _borian_ [@ClarkHall1960, 48]. The relevant comparison form here is the normalized present-third-singular _boraþ_, used beside the headword and the imperative singular _bora_.

Campbell's dialect survey allows secondary _-e-_ and _-o-_ spellings in 2sg and 3sg class-II forms, but the basic ending remains _-aþ_ [@Campbell1959, §757]. _Boraþ_ is therefore the regular comparison form for this non-_j_ 3sg cell.

#### Development to Old English

Early loss of final _-i_ first gives _\*búrōθ_ from _\*búrōθi_. Northwest Germanic lowering then produces _\*bórōθ_, and late shortening of unstressed _ō_ yields _\*bóraθ_, whence _boraþ_.

Campbell's class-II ending evidence and Ringe and Taylor's discussion of stable _a_ in the finite non-_j_ cells support exactly this sequence [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected 3sg cell from the bore-family lemma and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*burōjaną_]{.iv lang=pgmc sort=burojana role=source_protoform} | dictionary headword [_borian_]{.iv lang=oe sort=borian role=comparison_form} | [_borian_]{.iv lang=oe sort=borian role=comparison_form} | family background, but not the cell compared here |
| 3sg present | [_\*búrōθi_]{.iv lang=pgmc sort=burothi role=selected_input} | regular output [_boraþ_]{.iv lang=oe sort=borath role=regular_output} | [_boraþ_]{.iv lang=oe sort=borath role=target_form} | exact match |
| imperative singular companion | [_\*búrô_]{.iv lang=pgmc sort=buro role=comparison_form} | related finite form [_bora_]{.iv lang=oe sort=bora role=comparison_form} | [_bora_]{.iv lang=oe sort=bora role=comparison_form} | useful control, but not the target |

### learn (iptv.2sg) — OE liorna

\index[oe]{liorna@liorna}
\index[pgmc]{lizno@*líznô}
\index[pgmc]{liznojana@*liznōjaną}

Derivation: citation reconstruction _\*liznōjaną_; form followed here _\*líznô_ > _liorna_ (late analogy).

#### Derivation trace

Proto input: _\*líznô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*líornô} \\
OE Unstressed Long Vowel Shortening & \emph{*líorna} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liorna_

#### Reconstruction and comparative evidence

Ringe and Taylor give Old English [_liornian_]{.iv lang=oe sort=liornian role=comparison_form} ~ [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} from a learn-family base of the _\*lizn-_ type [@RingeTaylor2014, 38], and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@Kroonen2013, 380]. Fulk cites the same Old English family from _\*liznō-_ [@Fulk2018, 127].

The derivational input [_\*líznô_]{.iv lang=pgmc sort=lizno role=selected_input} is a finite imperative cell of that family, not the citation form of the verb.

#### Old English evidence

Clark Hall gives the ordinary headword as _leornian_ [@ClarkHall1960, 186]. Brunner, however, explicitly records _leornian, nordh. auch liorna_, and Campbell notes that beside _leornian_ Northumbrian forms with _io_ occur where original _eo_ and _io_ remain distinct [@SieversBrunner1965, §417 Anm. 10; @Campbell1959, §123 n. 2].

[_Liorna_]{.iv lang=oe sort=liorna role=target_form} can therefore be treated as an attested Northumbrian finite form, while [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} remains the better-known dictionary headword.

#### Development to Old English

The form compared here develops regularly as _\*líznô_ > _\*lírnô_ by rhotacism, then _\*líornô_ by breaking before _rn_, and finally _\*líorna_ by late shortening of the unstressed long vowel.

Campbell's Northumbrian _io_ evidence and Ringe and Taylor's explicit statement that no form of _liornian_ stood in an i-umlauting environment support this stem shape [@Campbell1959, §123 n. 2; @RingeTaylor2014, 247]. The West-Saxon-looking _eo_ forms belong to a different dialectal presentation of the same family.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected imperative cell from the learn-family infinitive and from the companion 3sg form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*liznōjaną_]{.iv lang=pgmc sort=liznojana role=source_protoform} | Northumbrian [_liornian_]{.iv lang=oe sort=liornian role=comparison_form}; dictionary headword often [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} | [_liornian_]{.iv lang=oe sort=liornian role=comparison_form} / [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} | family background, but not the cell compared here |
| imperative singular | [_\*líznô_]{.iv lang=pgmc sort=lizno role=selected_input} | regular output and Brunner's Northumbrian [_liorna_]{.iv lang=oe sort=liorna role=regular_output} | [_liorna_]{.iv lang=oe sort=liorna role=target_form} | exact match |
| 3sg present companion | [_\*líznōθi_]{.iv lang=pgmc sort=liznothi role=comparison_form} | related finite form [_liornaþ_]{.iv lang=oe sort=liornath role=comparison_form} | [_liornaþ_]{.iv lang=oe sort=liornath role=comparison_form} | useful control, but not the target |

### learn (3sg) — OE liornaþ

\index[oe]{liornath@liornaþ}
\index[pgmc]{liznojana@*liznōjaną}
\index[pgmc]{liznothi@*líznōθi}

Derivation: citation reconstruction _\*liznōjaną_; form followed here _\*líznōθi_ > _liornaþ_ (late analogy).

#### Derivation trace

Proto input: _\*líznōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*lírnōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*líornōθ} \\
OE Late O Shortening & \emph{*líornaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liornaþ_

#### Reconstruction and comparative evidence

Ringe and Taylor give Old English [_liornian_]{.iv lang=oe sort=liornian role=comparison_form} ~ [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} from a learn-family base of the _\*lizn-_ type [@RingeTaylor2014, 38], and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@Kroonen2013, 380]. The derivational input [_\*líznōθi_]{.iv lang=pgmc sort=liznothi role=selected_input} is the finite 3sg cell of that family, not the citation form of the verb.

For the ending, Campbell's lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ and Ringe and Taylor's discussion of stable _a_ in the class-II 2sg and 3sg make the non-_j_ 3sg cell the relevant comparison point [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Old English evidence

Clark Hall gives the ordinary headword as [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} [@ClarkHall1960, 186]. Brunner records Northumbrian finite forms in _liorn-_, including [_liorna_]{.iv lang=oe sort=liorna role=comparison_form} and the 3sg [_liornes_]{.iv lang=oe sort=liornes role=comparison_form}, beside the West-Saxon-looking [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} tradition [@SieversBrunner1965, §417 Anm. 10]. Campbell likewise notes Northumbrian forms with _io_ beside [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} [@Campbell1959, §123 n. 2].

The relevant comparison form here is the normalized 3sg [_liornaþ_]{.iv lang=oe sort=liornath role=target_form}. The directly cited Old English evidence supports the finite stem _liorn-_; the exact _-aþ_ ending follows the regular class-II 3sg pattern.

#### Development to Old English

The form compared here develops as _\*líznōθi_ > _\*lírnōθi_ by rhotacism, then _\*lírnōθ_ after early apocope of final _-i_, then _\*líornōθ_ by breaking before _rn_, and finally _\*líornaθ_ > _liornaþ_ by late shortening of the unstressed long vowel.

Campbell's Northumbrian _io_ evidence and Ringe and Taylor's statement that no form of _liornian_ stood in an i-umlauting environment support the stem, while Campbell's class-II ending evidence supports the final _-aþ_ [@Campbell1959, §123 n. 2; @Campbell1959, §356.4; @RingeTaylor2014, 247].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected 3sg cell from the learn-family infinitive and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*liznōjaną_]{.iv lang=pgmc sort=liznojana role=source_protoform} | Northumbrian [_liornian_]{.iv lang=oe sort=liornian role=comparison_form}; dictionary headword often [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} | [_liornian_]{.iv lang=oe sort=liornian role=comparison_form} / [_leornian_]{.iv lang=oe sort=leornian role=comparison_form} | family background, but not the cell compared here |
| 3sg present | [_\*líznōθi_]{.iv lang=pgmc sort=liznothi role=selected_input} | regular output [_liornaþ_]{.iv lang=oe sort=liornath role=regular_output} | [_liornaþ_]{.iv lang=oe sort=liornath role=target_form} | exact match |
| imperative singular companion | [_\*líznô_]{.iv lang=pgmc sort=lizno role=comparison_form} | regular output and Brunner's Northumbrian [_liorna_]{.iv lang=oe sort=liorna role=comparison_form} | [_liorna_]{.iv lang=oe sort=liorna role=comparison_form} | useful control, but not the target |

### lick (iptv.2sg) — OE licca

\index[oe]{licca@licca}
\index[pgmc]{likko@*líkkô}
\index[pgmc]{likkona@*likkōną}

Derivation: citation reconstruction _\*likkōną_; form followed here _\*líkkô_ > _licca_ (late analogy).

#### Derivation trace

Proto input: _\*líkkô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*líkka} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _licca_

#### Reconstruction and comparative evidence

Ringe and Taylor give PWGmc _\*li_/_ekkōn_ continuing as Old English [_liccian_]{.iv lang=oe sort=liccian role=comparison_form}, Old Saxon [_likkon_]{.iv lang=os sort=likkon role=comparison_form}, and Old High German [_lecchon_]{.iv lang=ohg sort=lecchon role=comparison_form} [@RingeTaylor2014, 50]. Orel gives the fuller weak-verb reconstruction [_\*likkōjanan_]{.iv lang=pgmc sort=likkojanan role=source_protoform} with the same Old English continuation [@Orel2003, 285].

Campbell's weak class-II discussion gives present forms such as lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note that class-II weak present 2sg. _-as(t)_ and 3sg. _-aþ_ have stable _a_ [@RingeTaylor2014, 80]. The form treated here is therefore not that remodeled infinitive but a finite cell in bare trimoric _\*-ō_.

#### Old English evidence

Bosworth-Toller lemmatizes the verb as _liccian_ [@BosworthToller1898, 614]. Campbell cites _liccian_ among Old English forms with preserved geminate _cc_ [@Campbell1959, §398.1]. Brunner likewise cites _liccian_ [@SieversBrunner1965, §45 Anm. 3]. The Old English evidence therefore establishes the verbal headword and its consonantal frame securely.

The Old English form here in this entry is the imperative singular [_licca_]{.iv lang=oe sort=licca role=target_form}. It is a paradigm form chosen beside the headword [_liccian_]{.iv lang=oe sort=liccian role=comparison_form} and the related present [_liccaþ_]{.iv lang=oe sort=liccath role=comparison_form}, not a separately lemmatized citation word.

#### Development to Old English

With the stem _licc-_ established, the remaining development is brief. Campbell's class-II present endings lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ support late _-a_ in this finite cell [@Campbell1959, §356.4]. Ringe and Taylor likewise note stable _a_ in the class-II 2sg and 3sg [@RingeTaylor2014, 80]. The same stem consonantism that appears in _liccian_ is preserved here, giving _cc_ throughout the finite form.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*líkkōjaną_]{.iv lang=pgmc sort=likkojana role=source_protoform} | regular output [_liccian_]{.iv lang=oe sort=liccian role=comparison_form} | [_liccian_]{.iv lang=oe sort=liccian role=comparison_form} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular | [_\*líkkô_]{.iv lang=pgmc sort=likko role=selected_input} | regular output [_licca_]{.iv lang=oe sort=licca role=regular_output} | [_licca_]{.iv lang=oe sort=licca role=target_form} | exact match between the derivational input and the Old English form here |
| present third singular companion | [_\*líkkōθi_]{.iv lang=pgmc sort=likkothi role=comparison_form} | regular output [_liccaþ_]{.iv lang=oe sort=liccath role=comparison_form} | [_liccaþ_]{.iv lang=oe sort=liccath role=comparison_form} | useful family control, but not the target of this entry |

### lick (3sg) — OE liccaþ

\index[oe]{liccath@liccaþ}
\index[pgmc]{likkona@*likkōną}
\index[pgmc]{likkothi@*líkkōθi}

Derivation: citation reconstruction _\*likkōną_; form followed here _\*líkkōθi_ > _liccaþ_ (late analogy).

#### Derivation trace

Proto input: _\*líkkōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*líkkōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Late O Shortening & \emph{*líkkaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liccaþ_

#### Reconstruction and comparative evidence

Ringe and Taylor give PWGmc _\*li_/_ekkōn_ continuing as Old English [_liccian_]{.iv lang=oe sort=liccian role=comparison_form}, Old Saxon [_likkon_]{.iv lang=os sort=likkon role=comparison_form}, and Old High German [_lecchon_]{.iv lang=ohg sort=lecchon role=comparison_form} [@RingeTaylor2014, 50]. Orel gives the fuller weak-verb reconstruction [_\*likkōjanan_]{.iv lang=pgmc sort=likkojanan role=source_protoform} with the same Old English continuation [@Orel2003, 285].

The form compared here in this entry is the non-_j_ present third singular _\*líkkōθi_, not the remodeled infinitive. Campbell states the class-II present endings as lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note that class-II weak present 2sg. _-as(t)_ and 3sg. _-aþ_ have stable _a_ [@RingeTaylor2014, 80].

#### Old English evidence

Bosworth-Toller lemmatizes the verb as _liccian_ [@BosworthToller1898, 614]. The same consonantal frame appears in Campbell's and Brunner's grammatical citations of _liccian_ [@Campbell1959, §398.1; @SieversBrunner1965, §45 Anm. 3]. The Old English headword is therefore clear even though the entry here is not about the citation form.

The form treated here is the present third singular [_liccaþ_]{.iv lang=oe sort=liccath role=target_form}. It is a selected paradigm form beside the lemma [_liccian_]{.iv lang=oe sort=liccian role=comparison_form} and the related imperative [_licca_]{.iv lang=oe sort=licca role=comparison_form}, not a separately lemmatized headword.

#### Development to Old English

[_\*líkkōθi_]{.iv lang=pgmc sort=likkothi role=selected_input} first loses final _-i_, giving _\*líkkōθ_. Campbell's class-II present endings lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ support the regular 3sg outcome _-aþ_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note stable _a_ in the class-II 2sg and 3sg [@RingeTaylor2014, 80]. Because this ending never contains _-j-_, the form does not pass through an i-umlauted _-eþ_ stage.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*líkkōjaną_]{.iv lang=pgmc sort=likkojana role=source_protoform} | regular output [_liccian_]{.iv lang=oe sort=liccian role=comparison_form} | [_liccian_]{.iv lang=oe sort=liccian role=comparison_form} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular companion | [_\*líkkô_]{.iv lang=pgmc sort=likko role=comparison_form} | regular output [_licca_]{.iv lang=oe sort=licca role=regular_output} | [_licca_]{.iv lang=oe sort=licca role=comparison_form} | useful family control, but not the target of this entry |
| present third singular | [_\*líkkōθi_]{.iv lang=pgmc sort=likkothi role=selected_input} | regular output [_liccaþ_]{.iv lang=oe sort=liccath role=regular_output} | [_liccaþ_]{.iv lang=oe sort=liccath role=target_form} | exact match between the derivational input and the Old English form here |

### show (iptv.2sg) — OE sċēawa

\index[oe]{sceawa@sċēawa}
\index[pgmc]{skawo@*skáwô}
\index[pgmc]{skawona@*skawōną}
\index[ohg]{scouwon@scouwōn}
\index[ofris]{skawia@skawia}
\index[os]{skawon@skawōn}

Derivation: citation reconstruction _\*skawōną_; form followed here _\*skáwô_ > _sċēawa_ (late analogy).

#### Derivation trace

Proto input: _\*skáwô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Aw Long Diphthong & \emph{*skḗawô} \\
OE Sk Palatalization & \emph{*ʃḗawô} \\
OE Unstressed Long Vowel Shortening & \emph{*ʃḗawa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēawa_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as _\*skawōjanan_ and cites Old English _sceáwian_ beside Old Frisian _skawia_, Old Saxon _skawōn_, and Old High German _scouwōn_ [@Orel2003, 337]. The derivational input in this entry is not that infinitive but the imperative singular _\*skáwô_, a finite class-II cell with imperative -a < _\*-ō_ [@RingeTaylor2014, 314].

That distinction matters because the imperative singular provides the direct comparison for the Old English form treated here. The lexical history still belongs to the _sceáwian_ verb, but the cell compared here isolates the finite _-a_ outcome more clearly than the citation form does.

#### Old English evidence

Bright lists _scēawian_ and explicitly gives the imperative singular _scēawa_ under that headword [@BrightCassidyRingler1971, 346]. The form treated here is therefore an attested finite paradigm form, not a reconstructed convenience form.

The spelling used in this entry is normalized _sċēawa_, while Bright's glossary gives source spelling _scēawa_. The ordinary Old English headword remains _scēawian_; _sċēawa_ is the imperative singular chosen beside it.

#### Development to Old English

Campbell lists _scéawian_ under the West Germanic _\*auw_ developments [@Campbell1959, §120]. Ringe and Taylor's class-II weak imperative singular -a < _\*-ō_ supports the late finite ending that yields _sċēawa_ [@RingeTaylor2014, 314]. The result is therefore the expected finite singular form of the _scēawian_ family rather than an analogical replacement of the headword.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*skáwōjaną_]{.iv lang=pgmc sort=skawojana} | regular output [_sċēawian_]{.iv lang=oe sort=sceawian} | [_scēawian_]{.iv lang=oe sort=sceawian} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular | [_\*skáwô_]{.iv lang=pgmc sort=skawo} | regular output [_sċēawa_]{.iv lang=oe sort=sceawa} | [_scēawa_]{.iv lang=oe sort=sceawa} / normalized [_sċēawa_]{.iv lang=oe sort=sceawa} | exact match between the derivational input and the Old English form here |
| present third singular companion | [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi} | regular output [_sċēawaþ_]{.iv lang=oe sort=sceawath} | [_sċēawaþ_]{.iv lang=oe sort=sceawath} | useful family control, but not the target of this entry |

### show (3sg) — OE sċēawaþ

\index[oe]{sceawath@sċēawaþ}
\index[pgmc]{skawona@*skawōną}
\index[pgmc]{skawothi@*skáwōθi}

Derivation: citation reconstruction _\*skawōną_; form followed here _\*skáwōθi_ > _sċēawaþ_ (late analogy).

#### Derivation trace

Proto input: _\*skáwōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*skáwōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Aw Long Diphthong & \emph{*skḗawōθ} \\
OE Sk Palatalization & \emph{*ʃḗawōθ} \\
OE Late O Shortening & \emph{*ʃḗawaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēawaþ_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as [_\*skawōjanan_]{.iv lang=pgmc sort=skawojanan role=source_protoform} and cites Old English [_sceáwian_]{.iv lang=oe sort=sceawian role=comparison_form} beside Old Frisian [_skawia_]{.iv lang=ofris sort=skawia role=comparison_form}, Old Saxon [_skawōn_]{.iv lang=os sort=skawon role=comparison_form}, and Old High German [_scouwōn_]{.iv lang=ohg sort=scouwon role=comparison_form} [@Orel2003, 337]. The derivational input in this entry is the present third singular [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi role=selected_input}, a finite class-II cell with stable _a_ in the 3sg ending [@RingeTaylor2014, 80].

Campbell states the class-II present endings as lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note that class-II weak present 2sg. _-as(t)_ and 3sg. _-aþ_ have stable _a_ [@RingeTaylor2014, 80]. The relevant comparison is therefore the 3sg cell itself, not an i-umlauted alternative.

#### Old English evidence

Bright lists the simplex headword [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form} and the imperative [_scēawa_]{.iv lang=oe sort=sceawa role=comparison_form}, and under _geond-scēawian_ also records a third singular _sceawað_ [@BrightCassidyRingler1971, 383]. The evidence thus establishes the _scēaw-_ / _sceawað_ finite-cell pattern directly.

The form written here as [_sċēawaþ_]{.iv lang=oe sort=sceawath role=target_form} is the normalized simplex comparison form for that weak class-II pattern. It is therefore not a dictionary headword but a finite comparison form aligned with the attested _scēaw-_ evidence and the directly cited _sceawað_ ending pattern.

#### Development to Old English

Campbell lists [_scéawian_]{.iv lang=oe sort=sceawian role=comparison_form} under the same West Germanic _\*auw_ development [@Campbell1959, §120]. [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi role=selected_input} therefore belongs to the _scēaw-_ family before the class-II 3sg ending is applied. Campbell's chronology and Ringe and Taylor's stable-_a_ discussion show that the class-II 3sg ending gives _-aþ_, not _-eþ_ [@Campbell1959, §356.4; @RingeTaylor2014, 80]. Because the ending never contains _-j-_, no i-umlaut applies.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*skáwōjaną_]{.iv lang=pgmc sort=skawojana role=comparison_form} | regular output [_sċēawian_]{.iv lang=oe sort=sceawian role=regular_output} | [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular companion | [_\*skáwô_]{.iv lang=pgmc sort=skawo role=comparison_form} | regular output [_sċēawa_]{.iv lang=oe sort=sceawa role=regular_output} | [_scēawa_]{.iv lang=oe sort=sceawa role=comparison_form} | useful family control, but not the target of this entry |
| present third singular | [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi role=selected_input} | regular output [_sċēawaþ_]{.iv lang=oe sort=sceawath role=target_form} | normalized [_sċēawaþ_]{.iv lang=oe sort=sceawath role=target_form}; source-side pattern _sceawað_ | exact match for the finite form compared here |

\clearpage

## Reconstructed Old English comparators

These entries use an explicitly reconstructed Old English-stage comparator for
the branch being modelled. The relevant comparison is therefore later than the
Proto-Germanic citation form but still belongs to the lexical derivation layer.

### knob — OE *cnobba

\index[oe]{cnobba@*cnobba}
\index[pgmc]{knubbo@*knúbbô}
\index[pgmc]{knuppaz@*knúppaz}

Derivation: citation reconstruction _\*knúppaz_; form followed here _\*knúbbô_ > _\*cnobba_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*knúbbô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*knóbbô} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*knóbba} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _\*cnobba_

#### Reconstruction and comparative evidence

The wider knob-family is not uniform. Kroonen's discussion of the Germanic
n-stems points to related voiced and voiceless branches within this group
[@Kroonen2011, 297]. The citation reconstruction _\*knúppaz_ represents the broader
cognate-set headword, while the form followed here, _\*knúbbô_, represents the voiced
weak-noun branch treated here.

That distinction matters because the Old English record is uneven. The better
attested OE material belongs to the voiceless branch, but the present entry
represents the reconstructed OE form that would continue the voiced branch
behind later English knob.

#### Old English evidence

Clark Hall preserves Old English evidence of the _cnoppa_ type
[@ClarkHall1960, 79]. Those forms are genuine Old English evidence, but they
belong to the voiceless branch of the family.

The target _\*cnobba_ is different in status. It is a **reconstructed Old
English form**, not a directly attested one. The point of using it here is to
give the voiced branch an explicit OE-stage representation instead of allowing
the attested _cnoppa_ branch to stand in for a different prehistory. The choice
of _\*cnobba_ is therefore a modeling and comparative decision rather than a
settled point of Old English philology.

#### Development to Old English

From the weak-noun form followed here, _\*knúbbô_, the regular Old English outcome is
_\*cnobba_, with Proto-Germanic _kn-_ represented in Old English as _cn-_ and
with the expected weak-noun ending.

The entry therefore does not claim that _\*cnobba_ is attested. Its claim is
different: if the voiced weak-noun branch is the one to be represented, then
_\*cnobba_ is the regular Old English form corresponding to that branch.

#### Reconstruction status

The comparison below keeps apart the reconstructed target and the
better-attested neighboring forms.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| [_\*knúbbô_ > _\*cnobba_]{.iv lang=oe display=*cnobba sort=cnobba} | reconstructed OE form; regular derivation | reconstructed Old English form compared here |
| [_cnopp_]{.iv lang=oe sort=cnopp} / [_cnoppa_]{.iv lang=oe sort=cnoppa} | attested OE branch | important control form, but belongs to the voiceless branch |
| [_cnæp_]{.iv lang=oe sort=cnaep} | attested OE form from another family | not part of the present lexeme line |

This remains the most review-sensitive item here, because the choice between
reconstructed _\*cnobba_ and attested _cnoppa_ is still a comparator-policy
question rather than a settled point of OE attestation.

### reek — OE *rēac

\index[oe]{reac@*rēac}
\index[pgmc]{raukaz@*ráukaz}
\index[pgmc]{raukiz@*ráukiz}

Derivation: citation reconstruction _\*ráukiz_; form followed here _\*ráukaz_ > _\*rēac_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*ráukaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*ráuka} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*ráeuka} \\
OE Diphthong Leveling & \emph{*rēaka} \\
PWGmc Final Bare A Loss & \emph{*rēak} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _\*rēac_

#### Reconstruction and comparative evidence

The wider noun family is represented by [_\*ráukiz_]{.iv lang=pgmc sort=raukiz role=source_protoform} / [_\*rauki-_]{.iv lang=pgmc sort=rauki role=source_protoform}, with Old English
[_rēc_]{.iv lang=oe sort=rec role=comparison_form} as the attested noun reflex in the comparative dictionaries
[@Kroonen2013, 446; @Orel2003, 338]. The derivational input [_\*ráukaz_]{.iv lang=pgmc sort=raukaz role=selected_input} is therefore not the
lexeme-level headword, but the form used here for the Old English derivation.

#### Old English evidence

The attested noun is [_rēc_]{.iv lang=oe sort=rec role=comparison_form}, not [_\*rēac_]{.iv lang=oe sort=reac role=target_form}. Clark Hall records [_rēc_]{.iv lang=oe sort=rec role=comparison_form} as the noun
and also preserves related forms such as [_rēcels_]{.iv lang=oe sort=recels role=comparison_form}; Kroonen likewise gives OE
[_rēc_]{.iv lang=oe sort=rec role=comparison_form} under the noun family [@ClarkHall1960, 255; @Kroonen2013, 446]. Clark
Hall and Seebold also record verbal [_rēac_]{.iv lang=oe sort=reac role=comparison_form} as the preterite of [_rēocan_]{.iv lang=oe sort=reocan role=comparison_form}, but
that verbal form is separate from the noun treated here [@ClarkHall1960, 254;
@Seebold1970, 380].

The Old English form here [_\*rēac_]{.iv lang=oe sort=reac role=target_form} is therefore a reconstructed West Saxon noun form,
not a directly attested manuscript headword.

#### Development to Old English

From [_\*ráukaz_]{.iv lang=pgmc sort=raukaz role=selected_input}, the regular West Saxon development gives [_\*rēac_]{.iv lang=oe sort=reac role=target_form}. The attested
noun [_rēc_]{.iv lang=oe sort=rec role=comparison_form} belongs to the same lexical family, but reflects a later smoothed
surface form rather than the regular noun target represented here.

#### Form note

The distinction here is between an attested noun headword [_rēc_]{.iv lang=oe sort=rec role=comparison_form} and a
reconstructed regular West Saxon target [_\*rēac_]{.iv lang=oe sort=reac role=target_form}. The latter is treated as the
modelling target, while the former remains philological background.

### strew — OE *strīeġan

\index[oe]{striegan@*strīeġan}
\index[pgmc]{strawjana@*stráwjaną}

Derivation: _\*stráwjaną_ > _\*strīeġan_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*stráwjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Awj Glide Formation & \emph{*stráujaną} \\
OE Au Fronting & \emph{*stráeujaną} \\
OE Diphthong Leveling & \emph{*strēajaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*strēajan} \\
OE Secondary Nasalization & \emph{*strēająn} \\
OE I Umlaut & \emph{*strīejąn} \\
OE Weak Tail Reduction & \emph{*strīejan} \\
OE J Strengthening After Front Diphthong & \emph{*strīeʒan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _\*strīeġan_

#### Reconstruction and comparative evidence

Kroonen cites the inherited weak verb as _\*straujan-_ and gives Old English
_streowian_ as its dictionary continuation [@Kroonen2013, 483]. Ringe and
Taylor make the split within Old English explicit: the inherited class-I verb is
continued by Anglian _strēgan_, while West Saxon _streowian_ is a
remodelled class-II verb [@RingeTaylor2014, §6.1 n. 27].

The aw-series comparison is important here. Luick groups _\*strauwjan_ with the
same set as _\*hauwja-_ and _\*kauwjan_, yielding Anglian _strēzan_ beside West
Saxon forms of the _hīez_, ciezan type [@Luick1914, §98]. Fulk likewise allows
an early West Saxon _\*striegan_ directly from Proto-Germanic _\*straujana_
[@Fulk2018, §4.10 n. 1].

#### Old English evidence

The attested inherited Old English form is _strēgan_ in Anglian. The
attested West Saxon citation forms are _strewian_, _streowian_, and
_strēawian_, which belong to the remodelled class-II branch
[@RingeTaylor2014, §6.1 n. 27; @Campbell1959, §753.7].

The target _\*strīeġan_ is therefore a **reconstructed Old English form**, not
an attested manuscript lemma. It is the reconstructed West Saxon reflex of the
inherited class-I verb, chosen to keep the inherited branch distinct from the
better-attested remodelled West Saxon lemma.

#### Development to Old English

From _\*stráwjaną_, the inherited West Saxon development passes through
_\*straujaną_, fronting and leveling to a _\*strēajan-_ stage, i-umlaut to
_\*strīejan_, and retention or strengthening of the glide after the front
diphthong, written here as _ġ_. The resulting form is _\*strīeġan_.

This differs from Anglian _strēgan_, where smoothing removes the diphthongal
sequence, and from West Saxon _strewian_ / _streowian_ / _strēawian_, where the
verb has already been remodelled into class II [@Fulk2018, §4.10 n. 1;
@Campbell1959, §753.7].

#### Reconstruction status

The comparison below sets the relevant forms side by side. It keeps apart the attested inherited branch,
the attested remodelled branch, and the reconstructed West Saxon comparator.

| Form or branch | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _strēgan_ | attested Anglian inherited class-I form | proves that the inherited verb survived into Old English |
| _\*strīeġan_ | reconstructed West Saxon inherited class-I form; trace-supported | Old English form here |
| _strewian_ / _streowian_ / _strēawian_ | attested remodelled West Saxon class-II forms | genuine OE evidence, but not the inherited branch modeled here |

\clearpage

## Known but unmodelled remodellings

These entries preserve cases where the historical remodelling is broadly
understood, but the current deterministic transducer does not model that later
reshaping directly.

### fire — OE fȳre

\index[oe]{fyre@fȳre}
\index[pgmc]{furi@*fūri}

Derivation: _\*fūri_ yields regular _fȳr_; the Old English form here is _fȳre_ (known but unmodelled remodelling).

#### Derivation trace

Proto input: _\*fūri_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*fȳri} \\
\mbox{OE High Vowel Apocope} & \emph{*fȳr} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _fȳr_

Old English form: _fȳre_

#### Reconstruction and comparative evidence

Kroonen places the lexeme in a heteroclitic family _\*fōr_ ~ _\*fun-_ and explains
the front-mutated West Germanic forms from an oblique form of the
_\*fu(w)eri_ type [@Kroonen2013, 151]. The form followed here, _\*fūri_, therefore does not
function as an arbitrary substitute for the headword: it represents the
specific inherited cell that supplies the _i_ needed for i-umlaut.

That distinction matters because the Old English target combines a regular
inherited form _fȳr_ with an attested analogical surface form _fȳre_.

#### Old English evidence

Bosworth-Toller records _fyr_ as the noun 'fire' and also preserves oblique
_fyre_ in the Old English record [@BosworthToller1898, 288]. The first is the
regular inherited outcome of the phonological development from the selected
input; the second shows the later restoration of a final _-e_ within the
paradigm.

The entry therefore concerns the relation between a regular inherited oblique
input and an attested Old English surface form that has undergone later
morphological remodeling.

#### Development to Old English

From _\*fūri_, i-umlaut changes _ū_ to _ȳ_ [@Hogg1992, §3.3.3.1]. Subsequent
loss of the final high vowel after a heavy syllable yields _fȳr_
[@Campbell1959, §345]. The inherited phonology is complete at that point.

_fȳre_ is later than that inherited output. Its final _-e_ belongs to
analogical restoration in the Old English paradigm rather than to the original
Proto-Germanic ending. The form therefore remains a known but unmodelled
remodelling: the deterministic phonology is regular, but the attested surface
form includes later morphological rebuilding.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the lexeme-level etymological
background from the inherited cell that actually produces the front-mutated
form and from the later analogical surface result.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level heteroclitic headword | _\*fōr_ ~ _\*fun-_ | comparative background only | fire family | explains the wider lexeme, but not the selected oblique input |
| inherited oblique cell | *fūri | regular output: _fȳr_ | fȳr | regular inherited output from the derivational input |
| later analogical surface form | — | attested _fȳre_ with restored _-e_ | fȳre | genuine OE target, but not the direct phonological output |

### tap — OE tæppa

\index[oe]{taeppa@tæppa}
\index[pgmc]{tappo@*táppô}

Derivation: _\*táppô_ yields regular _tappa_; the Old English form here is _tæppa_ (known but unmodelled remodelling).

#### Derivation trace

Proto input: _\*táppô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*tæppô} \\
OE A Restoration & \emph{*tappô} \\
OE Unstressed Long Vowel Shortening & \emph{*tappa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _tappa_

Old English form: _tæppa_

#### Reconstruction and comparative evidence

Orel gives the noun under _\*tappòn_ and already connects it with Old English
_tæppa_ [@Orel2003, 402]. The derivational input is therefore the inherited noun itself;
the entry does not depend on a different lexeme-level proto or a different
inherited noun cell.

#### Old English evidence

The Old English noun family is well attested. Orel gives _tæppa_, and Clark
Hall records _tæppa_ together with derivatives _tæppere_ and _tæppestre_
[@Orel2003, 402; @ClarkHall1960, 305]. The target is therefore a real Old English noun
form, not a reconstructed convenience spelling.

#### Development to Old English

From _\*táppô_, the regular inherited noun path gives _tappa_. The attested
target _tæppa_ therefore stands outside that regular phonological development.

The mismatch is historically intelligible, but it is not solved here by a new
inherited input. A related j-verb pathway would give _teppan_, not the noun
target _tæppa_. The entry accordingly remains a known but unmodelled case.

#### Form comparison

| Form type | Input or form | OE output or comparison | Result |
| :--- | :--- | :--- | :--- |
| regular inherited noun path | *táppô | regular output: _tappa_ | regular output, but not the target |
| attested OE target | — | _tæppa_ | genuine target form, but analogically remodelled in the present classification |
| related j-verb background | *táppjaną | _teppan_ | related formation, but not the noun target |

\clearpage

## Unexplained or deliberately unmodelled exceptions

These entries preserve a mismatch between the regular transducer output and the
attested Old English form. They are retained as documented lexical exceptions
rather than treated as evidence for further sound-change repair.

### buck — OE bucc

\index[oe]{bucc@bucc}
\index[pgmc]{bukkaz@*búkkaz}

Derivation: _\*búkkaz_ yields regular _bocc_; the Old English form here is _bucc_ (unexplained exception).

#### Derivation trace

Proto input: _\*búkkaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bókkaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*bókka} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*bókk} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _bocc_

Old English form: _bucc_

#### Reconstruction and comparative evidence

Kroonen and Orel both reconstruct the word with a geminate stop, [_\*bukkaz_]{.iv lang=pgmc sort=bukkaz role=source_protoform}
[@Kroonen2013, 121; @Orel2003, 61]. Orel also preserves parallel n-stem
material behind Old English [_bucca_]{.iv lang=oe sort=bucca role=comparison_form} [@Orel2003, 62]. The derivational input
therefore remains identical with the lexeme label: no alternative inherited
cell accounts for the form.

#### Old English evidence

Old English preserves a mixed lexical picture. Campbell cites [_bucca_]{.iv lang=oe sort=bucca role=comparison_form} in the
exception set for this phonological environment [@Campbell1959, §115]. Clark
Hall and Bosworth-Toller show that Old English has both [_bucca_]{.iv lang=oe sort=bucca role=comparison_form} and [_bucc_]{.iv lang=oe sort=bucc role=target_form}
[@ClarkHall1960, 53; @BosworthToller1898, 122]. The a-stem citation form [_bucc_]{.iv lang=oe sort=bucc role=target_form}
is the target treated here, with [_bucca_]{.iv lang=oe sort=bucca role=comparison_form} kept as genuine philological
background from the same lexical family.

#### Development to Old English

From [_\*búkkaz_]{.iv lang=pgmc sort=bukkaz role=selected_input}, the regular inherited path gives [_bocc_]{.iv lang=oe sort=bocc role=regular_output}. That is the form
expected under the ordinary lowering pattern in this environment. [_bucc_]{.iv lang=oe sort=bucc role=target_form}
therefore remains outside the deterministic phonology.

No accepted inherited cell repairs the mismatch. A high-vowel alternative would
introduce i-umlaut and produce a [_byċċ_]{.iv lang=oe sort=bycc role=comparison_form}-type form rather than the target.
[_bucc_]{.iv lang=oe sort=bucc role=target_form} is therefore best treated as a documented exception, not as a regular
paradigm-cell survival.

#### Form comparison

| Form type | Input or form | OE output or comparison | Result |
| :--- | :--- | :--- | :--- |
| regular inherited noun path | [_\*búkkaz_]{.iv lang=pgmc sort=bukkaz role=selected_input} | regular output: [_bocc_]{.iv lang=oe sort=bocc role=regular_output} | regular output, but not the target |
| attested OE target | — | [_bucc_]{.iv lang=oe sort=bucc role=target_form} | genuine target form, but unexplained in the present classification |
| parallel OE lexical background | — | [_bucca_]{.iv lang=oe sort=bucca role=comparison_form} | related n-stem form, not the present target |

### fowl — OE fugol

\index[oe]{fugol@fugol}
\index[pgmc]{fuglaz@*fúglaz}
\index[on]{fugl@fugl}
\index[ohg]{fogal@fogal}

Derivation: _\*fúglaz_ yields regular _fogol_; the Old English form here is _fugol_ (unexplained exception).

#### Derivation trace

Proto input: _\*fúglaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*fóglaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*fógla} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*fógl} \\
OE Epenthetic Vowel & \emph{*fógol} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _fogol_

Old English form: _fugol_

#### Reconstruction and comparative evidence

The noun is the ordinary Germanic a-stem _\*fúglaz_, continued by forms such as
Old Norse _fugl_ and Old High German _fogal_ [@Kroonen2013, 197; @Orel2003,
155]. There
is no stem-class or paradigm-cell dispute behind this entry. The comparative
headword and the derivational input are the same.

The difficulty lies instead in the stressed root vowel. Under the regular West
Germanic and Old English development, that _u_ should lower before the following
non-high vowel, yielding an _o_-vocalism
[@RingeTaylor2014, 42–43; @Campbell1959, 43].

#### Old English evidence

Old English dictionaries record the noun as _fugol_, with variant spelling
_fugel_ [@BosworthToller1898, 282; @ClarkHall1960, 138]. The target is therefore an
attested ordinary Old English noun, not a reconstructed or selectively chosen
paradigm form.

The attested word already contains the crucial problem. Its medial _-o-_ is the
ordinary parasite vowel of Old English cluster phonology, but the root _fu-_
retains _u_ where the regular history predicts _fo-_ [@Campbell1959, 150].

#### Development to Old English

From _\*fúglaz_, the regular cascade yields _fogol_: the root vowel lowers before
the following non-high vowel [@RingeTaylor2014, 42–43; @Campbell1959, 43],
final _z_ is lost, and the cluster is resolved by the usual medial vowel
[@RingeTaylor2014, 345; @Campbell1959, 150]. That is the expected inherited
outcome.

The attested Old English noun is _fugol_, not _fogol_. Luick and later
handbooks treat this preservation of _u_ as a small inherited residue, not as a
categorical sound law [@Luick1914, 148; @RingeTaylor2014, 47]. The item
therefore remains a genuine lexical exception rather than
the output of a recoverable regular mechanism.

#### Expected and attested forms

The comparison below sets the relevant forms side by side. It distinguishes the regular prediction from the
attested Old English noun.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _fogol_ | computed regular output from _\*fúglaz_ | establishes the expected inherited outcome |
| _fugol_ | attested Old English form | Old English form here; preserves unexplained root _u_ |
| _fugel_ | attested variant spelling | secondary spelling variant of the attested noun |

The unresolved point lies only in the root vowel. The medial _-o-_ is regular,
but no accepted lautgesetzlich pathway has been found from _\*fúglaz_ to
attested _fugol_.

### rust — OE rust

\index[oe]{rust@rust}
\index[pgmc]{rusto@*rústō}

Derivation: _\*rústō_ yields regular _rost_; the Old English form here is _rust_ (unexplained exception).

#### Derivation trace

Proto input: _\*rústō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*róstō} \\
\mbox{NWGmc Final Long O Raising} & \emph{*róstu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*róst} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _rost_

Old English form: _rust_

#### Reconstruction and comparative evidence

The comparative dictionaries do not support a single citation reconstruction
uniformly. Orel cites _\*rustaz_ sb.m./f. with Old English _rust_ and Old Saxon
and Old High German _rost_ [@Orel2003, 308]. The form _\*rústō_ therefore stands here
as a competing citation reconstruction rather than as the best-supported
inherited headword.

That disagreement does not remove the central problem. Whether one starts from
_\*rústō_ or from source-supported _\*rustaz_, the regular citation-form history
points toward _rost_, not toward the attested Old English noun.

#### Old English evidence

The Old English noun is attested, not reconstructed. Clark Hall gives _rūst_ m.
[@ClarkHall1960, 245], and Bosworth-Toller records _rúst_ (? and rust)
[@BosworthToller1898, 677]. The form is normalized here as _rust_ from that attested
record.

Those dictionary entries also matter morphologically. They support a masculine
noun, which aligns better with Orel's _\*rustaz_ than with the competing _\*rústō_
preserved in the header.

#### Development to Old English

Under Campbell's regular lowering of stressed _u_ before a following mid or low
vowel, the citation-form input gives _rost_, not _rust_ [@Campbell1959, §115].
The same lowering would also affect comparative citation-form reconstructions
such as _\*rustaz_.

A high-vowel comparator such as instrumental-type _\*rústu_ would yield _rust_
regularly, but that does not explain the attested citation form of the noun. No
accepted regular pathway from the citation form to attested _rust_ has been
established.

#### Expected and attested forms

The comparison below sets the regular inherited outcomes beside the attested Old English noun.

| Form / interpretation | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*rústō_ > _rost_ | computed regular output from one competing citation reconstruction | shows that this citation reconstruction does not reach attested _rust_ |
| _\*rustaz_ > _rost_ | expected regular output from the source-supported citation reconstruction | shows that correcting the stem class does not solve the vowel problem |
| _\*rústu_ > _rust_ | regular high-vowel comparator | useful negative control, but not a defensible citation-form solution |
| _rust_ | attested Old English noun, normalized from _rūst_ / _rúst_ / _rust_ | attested Old English form; the citation-form development remains unexplained |

### wolf — OE wulf

\index[oe]{wulf@wulf}
\index[pgmc]{wulfaz@*wúlfaz}

Derivation: _\*wúlfaz_ yields regular _wolf_; the Old English form here is _wulf_ (unexplained exception).

#### Derivation trace

Proto input: _\*wúlfaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*wólfaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*wólfa} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*wólf} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _wolf_

Old English form: _wulf_

#### Reconstruction and comparative evidence

The inherited noun is an a-stem: Kroonen gives _\*wulfa-_, and Ringe and Taylor
list PGmc _\*wulfaz_ among the inherited words that preserve _u_ in Old English
beside Old High German _wolf_ [@Kroonen2013, 638; @RingeTaylor2014, 47]. Campbell
accordingly names Old English _wulf_ as an exception to the regular lowering of
stressed _u_ before a following non-high vowel [@Campbell1959, §115].

The older literature often notices that the exceptional words cluster near
labials. Bülbring lists _full_, _wulle_, and _wulf_ together, but he also says
that the ordinary rule still gives _o_ in comparable forms such as _folc_ and
_bolt_ [@Bulbring1902, §116]. Luick rejects a categorical labial blocker on the
same grounds and prefers a lexical or analogical account instead
[@Luick1914, 148].

#### Old English evidence

Campbell treats _wulf_ as part of the exceptional _u_ set
[@Campbell1959, §115]. Sievers-Brunner notes that oblique _wulfe_ continues
_wulfi_ or older _wulfai_ [@SieversBrunner1965, §160].

That warning matters because the surviving oblique forms do not supply a clean
regular route back to bare _wulf_. They belong to the same lexeme, but they do
not remove the explanatory problem presented by the citation form.

#### Development to Old English

Under the ordinary Northwest Germanic lowering of stressed _u_ before a
following non-high vowel, the citation-form input would point toward
_o_-vocalism [@RingeTaylor2014, 42-44]. The compact trace shows exactly that
path: _\*wúlfaz_ > _\*wólfaz_ > _\*wólfa_ > _wolf_.

A high-vowel oblique input would behave differently. There the following high
vowel would block the lowering of _u_, but the same environment
would also trigger i-umlaut, so the regular control result would be _wylf_ or
_wylfe_, not bare _wulf_. The attested noun therefore remains unexplained at
the citation-form level.

#### Expected and attested forms

The comparison below sets the regular inherited outcomes beside the attested Old English noun.

| Form / interpretation | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*wúlfaz_ > _wolf_ | computed regular output from the citation form | shows the regular development expected from the inherited a-stem |
| _OHG wolf_ | comparative regular cognate | confirms that the _o_-vocalism is the ordinary outcome |
| _\*wúlfi_ / _\*wúlfis_ > _wylf_ / _wylfe_ | expected high-vowel control forms | shows why oblique high-vowel cells do not solve the noun's vowel history |
| _wulf_ | attested Old English noun | attested Old English form; the preservation of _u_ remains unexplained |

### wool — OE wull

\index[oe]{wull@wull}
\index[pgmc]{wullo@*wúllō}

Derivation: _\*wúllō_ yields regular _woll_; the Old English form here is _wull_ (unexplained exception).

#### Derivation trace

Proto input: _\*wúllō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*wóllō} \\
\mbox{NWGmc Final Long O Raising} & \emph{*wóllu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*wóll} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _woll_

Old English form: _wull_

#### Reconstruction and comparative evidence

The inherited form is a feminine ō-stem _\*wúllō_. In the ordinary phonological
history of West Germanic, stressed _u_ lowers before a following non-high vowel,
so the regular Old English outcome is an _o_-form. Campbell's discussion of the
parallel adjective _full_, with OHG _foll_ as the regular comparator, shows that
the handbooks treat this as a genuine exception cluster rather than as a place
where the rule itself is doubtful [@Campbell1959, §115].

Bülbring likewise lists _wulle_ among the traditional _u_-preserving
exceptions [@Bulbring1902, §116]. The comparative evidence therefore establishes
two things at once: the regular result should be _woll_, and Old English still
has a lexical exception of the _wull_ / _wulle_ type.

#### Old English evidence

The Old English target is given here as _wull_, a normalized lexeme form.
Handbook discussion often cites _wulle_, the feminine weak form of the noun
[@Bulbring1902, §116]. Both point to the same lexical item and to the same
exceptional preservation of root _u_.

The OE evidence therefore does not remove the problem. It confirms that the
language has a _u_-form where the regular phonology would have produced _o_.

#### Development to Old English

From _\*wúllō_, the regular sequence is lowering of stressed _u_ before a
non-high vowel, followed by the ordinary later reductions of the ending. The
regular outcome is therefore _woll_.

That regular derivation is not the attested Old English form. Luick rejects a
simple phonological rule that would protect this word alone, and Ringe and
Taylor state the larger problem plainly: we do not really know why _\*u_ failed
to lower in forms of this sort [@Luick1914, 148; @RingeTaylor2014, §2.3.1].

#### What remains unexplained

The comparison below sets the regular result beside the attested lexical exception.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*wúllō_ > _woll_ | regular output | shows what the deterministic sound laws produce |
| _wull_ / _wulle_ | attested OE exception | attested Old English form to be recorded |
| high-vowel escape from another paradigm cell | unsupported for this noun | rejected because the feminine ō-stem paradigm supplies no suitable escape cell |

\clearpage

## References

\backmatter

# References



::: {#refs}

:::



\part*{Index verborum}

\addcontentsline{toc}{part}{Index verborum}

\printindex[oe]

\printindex[pgmc]

\printindex[pwgmc]

\printindex[preoe]

\printindex[on]

\printindex[ohg]

\printindex[ofris]

\printindex[goth]

\printindex[os]

\printindex[dutch]

\printindex[german]

\printindex[modeng]

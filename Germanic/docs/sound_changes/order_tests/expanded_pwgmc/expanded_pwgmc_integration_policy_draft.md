# Expanded PWGmc integration policy draft

## 1. Status of expanded-PWGmc evidence

Expanded-PWGmc evidence should currently be treated as **supplementary review-layer evidence**.

It is not a replacement for the default bundled-profile chronology corpus, and it should not be treated as if it automatically supersedes the default chronology cards, default first-break TSVs, or default graph layer.

The purpose of the expanded profile was investigative: open the bundled `PWGmcChanges` stage so the project could inspect what earlier-side bundled-boundary rows were actually doing inside the internal PWGmc corridor. That evidence is now available, but its role is still interpretive and supplementary rather than automatically canonical.

## 2. What can be integrated into ordinary chronology cards

At this stage, only the **two internal positive PWGmc breaks** should be considered candidates for explicit ordinary-card annotation:

1. `SC031` earlier across `SC011` `PWGmc Syllabic J`
2. `SC033` earlier across `SC008` `PWGmc Coronal W Assimilation`

These two cases are different from the rest of the expanded-PWGmc boundary-target layer because they exposed specific internal PWGmc positive break points rather than simply strengthening a bundled-boundary no-break result.

So the present draft recommendation is:

1. ordinary chronology cards may eventually receive a short supplementary note for `SC031` and `SC033`;
2. those notes should identify the exposed internal PWGmc break and make clear that the evidence comes from the separate expanded-PWGmc review layer;
3. no broader card rewrite should be inferred from those two annotations alone.

## 3. What should remain in the expanded review layer

The no-break-to-`SC004` strengthened negative evidence should remain in the expanded-PWGmc review layer for now.

That includes the many true bundled-boundary targets that, once the PWGmc corridor was opened, still resolved as `no_break_before_boundary` down to `SC004`.

The draft policy recommendation is:

1. do **not** copy those strengthened negative rows into ordinary chronology cards yet;
2. retain them in the expanded-PWGmc documentation and result index;
3. revisit card-level treatment only if the project later adopts a standard ordinary-card field such as “supplementary negative evidence” or a similar explicitly non-canonical annotation slot.

Until that broader card schema question is settled, the strengthened negative evidence is better preserved in the expanded review layer than partially imported into the default card system.

## 4. Exploratory local and broad/far confirmations from contiguous mini-batches

The exploratory contiguous mini-batches produced useful local confirmations and broad/far confirmations.

Those checks are valuable because they show that the expanded profile often reproduces or supports relationships that were already visible in the default profile. But they should **not** drive ordinary-card revisions by themselves.

The reason is methodological:

1. those exploratory mini-batches were supplementary exploration;
2. they were not the narrow purpose of the expanded-PWGmc boundary-target phase;
3. therefore they should remain supporting context, not automatic triggers for default-card revision.

## 5. What should not happen automatically

The following actions should **not** happen automatically on the basis of the expanded-PWGmc phase:

1. do **not** regenerate default graph exports from expanded evidence;
2. do **not** overwrite or replace the default first-break TSV corpus;
3. do **not** rewrite all ordinary chronology cards with expanded-profile results;
4. do **not** treat the expanded profile as a new default corpus;
5. do **not** begin later-direction expanded-profile testing unless a separate question specifically justifies it.

This draft policy is intentionally conservative. The expanded layer answered a narrow question successfully, but that does not by itself authorize broad downstream rewrites.

## 6. Proposed practical next step after policy approval

After this policy is reviewed and approved, the next practical step should be a **small, manual documentation update** rather than a bulk rewrite.

That update should:

1. identify the ordinary chronology cards for `SC031` and `SC033`;
2. add a short “expanded-PWGmc note” to those cards only;
3. add cross-links from those cards back to the expanded-PWGmc closure and phase-synthesis documents;
4. leave the strengthened negative cases in the expanded review layer rather than importing them into ordinary cards.

This keeps the first integration step narrow, traceable, and reversible.

## 7. Validation checklist

This draft is valid only if the change set remains limited to the policy note itself:

1. policy draft only;
2. no generated TSV outputs;
3. no default-card edits;
4. no graph exports;
5. no `.bin` files;
6. no logs.

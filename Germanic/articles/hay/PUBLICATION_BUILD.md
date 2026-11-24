# Standalone article build

`DRAFT.md` is the article's only editable manuscript. Build it from the
repository root:

```sh
bash Germanic/articles/hay/build_article_docker.sh
```

The wrapper uses the project's `pandoc/latex` Docker convention, shared
XeLaTeX metadata, semantic-form macros and Lua filters, and the two
bibliographies declared in the draft's YAML header. Pandoc citeproc generates
in-text citations and the reference list from those BibTeX entries, including
the draft's page and section locators. An article-local Lua filter renders
manuscript angle brackets with TeX delimiters, avoiding an extra font-package
dependency. The Markdown `footnotes` extension supports ordinary scholarly
footnotes. The generated TeX, PDF and build log are written under the ignored
`.capr-work/hay-article-publication/` directory.
The article is a standalone input; it is not registered in the book's
artifact graph or included in the production book.

The build checks the PDF and generated TeX for unresolved citations or
internal references. Section callouts in the current draft are plain prose,
not automatic cross-reference fields.

## Editorial footnote candidates (not applied)

No manuscript edits are made by this build setup. The linguistic author may
consider:

- In §3.1, moving the explanation that Dahl prints 839 for *heiweg* but dates
  the same charter to 859 when citing *Scufelingforde* to a footnote. The
  current draft already gives the corrected date, 859, and cites Sweet's
  edition; the note could preserve the correction's source-critical detail.
- In §3.1, moving the charter's archival identification (Sawyer S 1196,
  Cotton Augustus ii.16, and Sweet's Ct. 43) to a note if the author wants a
  shorter evidentiary paragraph.
- The Rushworth manuscript-image limitation could be a note, but it qualifies
  the accent evidence directly and is best retained in the text unless the
  author decides otherwise.

These are layout options only; they do not recommend changing the argument or
the evidentiary qualifications.

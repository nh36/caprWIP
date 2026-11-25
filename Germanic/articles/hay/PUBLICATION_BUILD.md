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

The three documentary notes in the charter discussion are anchored in
prose, not table cells. The article prevents individual notes from
splitting across pages. Check marker placement and complete note text in
the rendered PDF as well as in the generated TeX before replacing the
tracked `hay-article.pdf`.

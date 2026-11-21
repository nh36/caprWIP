"""Assemble a combined-book preview without touching canonical publications."""

from pathlib import Path

from build_capr_book_draft import build_book_markdown

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "sc047_preview"
OUTPUT = HERE.parents[2] / ".capr-work/sc047-parallel/book/preview.md"


def assemble(book):
    for marker, source in ((r"\part{Lexical derivations}", "chronologies.md"),
                           (r"\backmatter", "appendix.md")):
        boundary = f"\n\n{marker}\n\n"
        before, after = book.split(boundary)
        book = (before + "\n\n" + (SOURCE / source).read_text(encoding="utf-8").strip()
                + boundary + after)
    return book


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(assemble(build_book_markdown()), encoding="utf-8")
    print(OUTPUT)

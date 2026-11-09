"""Seal authentic final lanes, without changing any tracked candidate bytes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path("Germanic/tools").resolve()))
from adjudication_control import source_identity, verify_receipt
from adjudication_run import load, record_validation_level

root = Path(".capr-work/hvd-lexical-finish/validation")
tested = "1cb8896765fb304fee35139fc9d6b788d04d32ce"
destination = root / "finish-certification.json"
assert not destination.exists(), destination
identity = source_identity()
assert identity["head_commit"] == tested and not identity["worktree_changes"]
labels = [
    "finish-reconciled-committed-focused", "finish-reconciled-committed-refresh",
    "finish-reconciled-committed-status", "finish-reconciled-committed-strict-serial",
    "finish-reconciled-committed-strict-exclusive",
]
receipts = [json.loads((root / (label + ".json")).read_text()) for label in labels]
for receipt in receipts:
    verify_receipt(receipt)
    assert receipt["source_identity"]["head_commit"] == tested
    assert not receipt["source_changed"]
serial, exclusive = receipts[-2:]
assert serial["test_counts"]["skipped"] == 5, serial["test_counts"]
assert exclusive["test_counts"]["skipped"] == 0, exclusive["test_counts"]

book = json.loads((root / "finish-strict-final-indexed-book.json").read_text())
verify_receipt(book, current=False, allow_source_change=True)
assert "INDEX_VERBORUM_STRICT=1" in book["argv"]
after = book["source_identity_after"]
delta = set(filter(None, subprocess.check_output(
    ["git", "diff", "--name-only", "-z", after["head_commit"], tested],
    text=True).split("\0")))
archives = tuple("Germanic/docs/sound_changes/audits/" + name + "/" for name in (
    "sc063-lexical-coverage-finish-validation",
    "sc063-lexical-coverage-strict-candidate-validation",
    "sc063-lexical-coverage-consumer-repair-validation",
    "sc063-lexical-coverage-publication",
))
auxiliary = {
    "Germanic/tests/test_bounded_domain_adoption.py",
    "Germanic/tests/test_glide_context_adoption.py",
    "Germanic/data/protoform_stage_audit.tsv",
    "Germanic/tests/test_lexical_editorial_order.py",
    "Germanic/tests/test_rainbow_2148_adoption.py",
    "Germanic/tests/test_sc032_adjudication.py",
    "Germanic/docs/sound_changes/audits/sc063-lexical-coverage-closeout.md",
}
assert delta - set(after["worktree_changes"]) - auxiliary == {
    path for path in delta if path.startswith(archives)
}
for path in auxiliary:
    assert Path(path).read_bytes() == subprocess.check_output(
        ["git", "show", tested + ":" + path]), path
for path, digest in after["worktree_changes"].items():
    if path not in auxiliary:
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, path
visual = json.loads((root / "publication-visual-final.json").read_text())
assert len(visual["combined_visually_inspected_pages"]) == 19
for pdf in visual["pdfs"]:
    assert hashlib.sha256(Path(pdf["path"]).read_bytes()).hexdigest() == pdf["sha256"]
    public = Path(archives[-1]) / Path(pdf["path"]).name
    assert hashlib.sha256(public.read_bytes()).hexdigest() == pdf["sha256"]
assert "CONTROL PLANE CLEAN" in Path(receipts[1]["stdout_log"]).read_text()
assert "all artifact-graph nodes fresh" in Path(receipts[2]["stdout_log"]).read_text()

run = load("SC063")
for level in ("A", "B", "C"):
    record_validation_level(
        run, level, [r for r in receipts if r["level"] == level],
        reused_evidence=([{
            "check": "Strict indexed complete publication and nineteen-page visual inspection",
            "basis": (
                "Authentic executed book wrapper. Publication SOURCE and generated "
                "manuscripts remain byte-identical. Exactly seven declared auxiliary "
                "consumer tests/human-stage-audit/closeout changes are separately pinned; "
                "none enters the book or changes inputs, targets, executable rules or "
                "stage resolution. Official finalization and fresh full B establish "
                "all graph nodes fresh. All four PDFs, including committed public copies, "
                "equal the original individually hashed nineteen-page visual receipt."
            ),
            "receipt": book["receipt_path"],
        }] if level == "C" else []))
run.complete_stage(
    "VALIDATE", evidence={"receipts": receipts},
    note="Exact committed1cb88967: focused, integrated, full strict serial and "
         "exclusive passed without SOURCE/HEAD drift; indexed book and visual "
         "PDF identities verified. Five explicit historical-replay skips retained.")
run.complete_stage(
    "COMPLETE", evidence={"tested_commit": tested},
    note="Bounded HVD lexical closeout certified:394 singly accepted,386 matches, "
         "eight inherited mismatches; all392 predecessors and both380 protections "
         "unchanged. No new sound-law body/order modification.")

certificate = {
    "tested_commit": tested,
    "tested_tree": subprocess.check_output(
        ["git", "rev-parse", "HEAD^{tree}"], text=True).strip(),
    "source_identity_sha256": identity["identity_sha256"],
    "population": {"before": 391, "before_matched": 383, "after": 394,
                   "after_matched": 386, "inherited_mismatches": 8,
                   "rejected": 0, "ambiguous": 0},
    "outputs_sha256": "43a57847b70b39ec130b4b52a17065be8cedd0e5fe7c6cc801ae1bcecae9fe2c",
    "lexical_sha256": "2783f9617b26caf0ad10836a99d4502f80f47ee13f858aaea123b9351b1c5514",
    "protected_predecessor_entries": 392,
    "strict_publication_tree_equivalence": True,
    "additional_candidate_paths": sorted(path for path in delta if path.startswith(archives)),
    "nonpublication_consumer_repairs": {
        path: hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in sorted(auxiliary)},
    "pdfs": visual["pdfs"],
    "visually_inspected_combined_pages": [
        row["physical_page"] for row in visual["combined_visually_inspected_pages"]],
    "validation": [],
}
body = [
    "Full scientific/publication certification for `" + tested + "`.", "",
    "A: focused owning checks. B: CONTROL PLANE CLEAN and STATUS OK. "
    "C: full strict serial then exclusive on this exact commit, without HEAD "
    "or SOURCE drift; five intentional historical-replay skips retained.", "",
]
for receipt in receipts:
    log = Path(receipt["stdout_log"]).read_text()
    summary = next((line for line in reversed(log.splitlines())
                    if "passed" in line and " in " in line), receipt["label"] + ": exit 0")
    item = {
        "label": receipt["label"], "level": receipt["level"], "lane": receipt["lane"],
        "summary": summary, "receipt": receipt["receipt_path"],
        "stdout_sha256": receipt["stdout_sha256"], "stderr_sha256": receipt["stderr_sha256"],
    }
    if receipt["level"] == "C":
        item.update(junit_sha256=receipt["junit_sha256"], test_counts=receipt["test_counts"])
        body.extend(["**Strict " + receipt["lane"] + ":** " + summary, ""])
    certificate["validation"].append(item)
body.extend([
    "Strict indexed publication passed; final manuscript/source identity and "
    "all four PDF hashes verified. Nineteen actual combined-book pages inspected, "
    "including the changed reader passages, new lexical articles, current "
    "spindle/filth accusatives and printed OE/PGmc indexes.", "",
    "391/383 becomes394/386, with the same eight inherited mismatches. "
    "Little, inherited livestock plural and dart admitted; all392 preceding "
    "histories, frozen391 and both380 protections preserved. Kettle's exact "
    "primary comparator, little root variants and spindle gemination remain "
    "qualified; no broader sound-law investigation was reopened.", "",
    "The supplementary evidence commit contains complete original logs/JUnit, "
    "sealed journal, protected assays and byte-identical final publication PDFs. "
    "It is an evidence-only descendant, not a claim of another exact-commit C pass.",
])
destination.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
(root / "finish-certification-comment.txt").write_text("\n".join(body) + "\n")
print(run.report())
print("CERTIFICATE", destination)

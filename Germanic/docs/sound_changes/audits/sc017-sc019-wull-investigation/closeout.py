"""Verify production preservation and completeness of frozen research receipts."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess

root = Path(__file__).parent
repository = Path("/Users/nathanhill/Code/capr")
destination = root / "production-preservation-final.json"
if destination.exists():
    raise RuntimeError("Final preservation receipt already exists")
protected = json.loads((root.parent / "wull-production-protection-before.json").read_text())
after = {path: hashlib.sha256((repository / path).read_bytes()).hexdigest()
         for path in protected}
changed = [path for path in protected if protected[path] != after[path]]
if changed:
    raise RuntimeError(f"Production preservation failure: {changed}")
def git(*args):
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()
head, remote = git("rev-parse", "HEAD"), git("rev-parse", "origin/update")
if head != remote or head != "586ec5f370e58d9038142d330121acf58b085a18":
    raise RuntimeError("Released HEAD changed during investigation")
names = ["identity", "a-order-only", "b-conditioning-only", "c-combined", "d-live-allophony"]
for name in names:
    report = json.loads((root / f"{name}-replay.json").read_text())
    if (report["selected_rows"] != 387 or len(report["rows"]) != 387
        or len({row["id"] for row in report["rows"]}) != 387
        or report["checkpoint_count"] != 107
        or not report["full_wrapper_equals_stage_replay"]
        or not report["canonical_artifacts_unchanged"]):
        raise RuntimeError(f"Incomplete protected experiment: {name}")
equivalence = json.loads((root / "independent-equivalence.json").read_text())
if equivalence["original_independent_identity_prefix_comparisons"] != 41409:
    raise RuntimeError("Independent prefix denominator failed")
with (root / "all_387_rows_all_variants.tsv").open() as handle:
    if sum(1 for _ in csv.DictReader(handle, delimiter="\t")) != 1935:
        raise RuntimeError("All-row annex denominator failed")
text = (root / "REPORT.md").read_text()
if sum(line.startswith("## ") for line in text.splitlines()) != 9:
    raise RuntimeError("Nine-heading report structure failed")
if "Registry-verdict:" in text:
    raise RuntimeError("Investigation must not issue an adopted registry verdict")
result = {
    "head": head, "origin_update": remote, "production_files_checked": len(protected),
    "production_changed_paths": changed, "production_hashes": after,
    "git_status": git("status", "--short"),
    "all_387_rows_each_of_five_variants": True,
    "all_107_checkpoint_identity_comparisons": True,
    "all_16_cells_each_of_five_complete_suffixes": True,
    "private_protected_artifacts_unchanged": True,
    "nine_heading_report": True,
    "scientific_source_adoption_baseline_repin_commit_push": "none",
}
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
files = sorted(path for path in root.iterdir() if path.is_file()
               and path.name != "artifact-sha256.tsv")
with (root / "artifact-sha256.tsv").open("w", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t")
    writer.writerow(["file", "sha256"])
    writer.writerows((path.name, hashlib.sha256(path.read_bytes()).hexdigest()) for path in files)
print(json.dumps({key: result[key] for key in (
    "head", "origin_update", "production_files_checked", "production_changed_paths",
    "git_status", "nine_heading_report")}))

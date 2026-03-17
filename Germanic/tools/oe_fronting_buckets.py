#!/usr/bin/env python3
import argparse
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description="Extract A-fronting buckets from OE full trace report.")
    p.add_argument("--report", required=True)
    p.add_argument("--output-dir", default="docs/debug_snapshots")
    p.add_argument("--label", default="")
    args=p.parse_args()
    lines=Path(args.report).read_text(encoding="utf-8").splitlines()
    idx=next((i for i,l in enumerate(lines) if l=="=== A-FRONTING AUDIT ==="), -1)
    if idx<0: raise SystemExit("A-FRONTING AUDIT section not found")
    buckets={}; cur=None
    for line in lines[idx+1:]:
        if line.startswith("=== STAGE FIRING SUMMARY ==="): break
        if line.startswith("--- ") and line.endswith(" ---"):
            cur=buckets.setdefault(line[4:-4].split(" (",1)[0],[]); continue
        if not line.strip() or cur is None: continue
        cur.append(line)
    out_dir=Path(args.output_dir); out_dir.mkdir(parents=True, exist_ok=True)
    label=f"_{args.label}" if args.label else ""
    for title, items in buckets.items():
        (out_dir / f"oe_fronting_bucket_{title}{label}.txt").write_text("\n".join(items).rstrip()+"\n", encoding="utf-8")
    print(f"Wrote {len(buckets)} buckets to {out_dir}")
if __name__=="__main__": main()

# scripts/kaggle_spotcheck.py
from pathlib import Path
import pandas as pd, json, hashlib, datetime as dt

RAW = Path("data/raw")
RESULTS = Path("results"); RESULTS.mkdir(parents=True, exist_ok=True)
HASHES = Path("data/hashes"); HASHES.mkdir(parents=True, exist_ok=True)

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def profile_csv(p: Path):
    try:
        df = pd.read_csv(p)
    except pd.errors.EmptyDataError:
        return {"file": p.name, "error": "empty file (no columns)"}
    except FileNotFoundError:
        return {"file": p.name, "error": "missing"}

    out = {
        "file": p.name,
        "rows": int(len(df)),
        "cols": int(df.shape[1]),
        "dup_rows": int(df.duplicated().sum()),
        "null_cells": int(df.isna().sum().sum()),
        "sha256": sha256_file(p),
        "sample_head": df.head(3).to_dict(orient="records"),
    }

    # light semantic checks if columns exist
    if "Salary_USD" in df.columns:
        out["salary_min"] = float(pd.to_numeric(df["Salary_USD"], errors="coerce").min())
        out["salary_max"] = float(pd.to_numeric(df["Salary_USD"], errors="coerce").max())
    if "Years_Experience" in df.columns:
        out["years_min"] = float(pd.to_numeric(df["Years_Experience"], errors="coerce").min())
        out["years_max"] = float(pd.to_numeric(df["Years_Experience"], errors="coerce").max())
    if "Remote_Friendly" in df.columns:
        out["remote_values"] = sorted(df["Remote_Friendly"].dropna().astype(str).str.strip().str.title().unique().tolist())

    return out

def write_sha_file(p: Path, digest: str):
    sha_path = HASHES / f"{p.stem}.sha256"
    sha_path.write_text(f"{digest}  {p.name}\n")

def main():
    targets = [
        RAW/"ai_job_dataset.csv",
        RAW/"ai_job_market_insights.csv",
    ]
    summary = {"generated_at": dt.datetime.utcnow().isoformat() + "Z", "files": []}
    samples = []

    for p in targets:
        info = profile_csv(p)
        summary["files"].append(info)
        if "sha256" in info:
            write_sha_file(p, info["sha256"])
        # collect a few samples for the appendix
        if not info.get("error"):
            df = pd.read_csv(p)
            samples.append(df.sample(min(5, len(df)), random_state=7))

    # save outputs
    (RESULTS/"kaggle_spotcheck.json").write_text(json.dumps(summary, indent=2))
    if samples:
        pd.concat(samples, ignore_index=True).to_csv(RESULTS/"kaggle_spotcheck_samples.csv", index=False)

    # short Markdown note for the report
    md = ["# Kaggle Reliability Spot-Checks",
          "",
          "- SHA256 checksums recorded in `data/hashes/*.sha256`",
          "- Basic row/column counts, nulls, duplicates, and small samples saved.",
          "",
          "## Summary"]
    for f in summary["files"]:
        line = f"- **{f['file']}**: "
        if f.get("error"):
            line += f"ERROR — {f['error']}"
        else:
            line += f"{f['rows']} rows × {f['cols']} cols; dup_rows={f['dup_rows']}; null_cells={f['null_cells']}; sha256=`{f['sha256'][:12]}…`"
        md.append(line)
    (RESULTS/"kaggle_spotcheck.md").write_text("\n".join(md))

if __name__ == "__main__":
    main()

from pathlib import Path
import pandas as pd, json

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")
RESULTS = Path("results"); RESULTS.mkdir(parents=True, exist_ok=True)
out = RESULTS / "quality_profile.json"

targets = [
    RAW_DIR/"ai_job_dataset.csv",
    RAW_DIR/"ai_job_market_insights.csv",
    PROC_DIR/"jobs_unified.csv",
]

report = {}
for p in targets:
    key = p.name
    if not p.exists() or p.stat().st_size == 0:
        report[key] = {"error": "missing or empty"}
        continue
    try:
        df = pd.read_csv(p)
        report[key] = {
            "rows": int(len(df)),
            "cols": int(df.shape[1]),
            "null_cells": int(df.isna().sum().sum()),
            "dup_rows": int(df.duplicated().sum()),
        }
    except Exception as e:
        report[key] = {"error": str(e)}

out.write_text(json.dumps(report, indent=2))
print(f"Wrote {out}")

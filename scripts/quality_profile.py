import os, json, pandas as pd, glob

paths = [
  "data/raw/ai_job_dataset.csv",
  "data/raw/ai_job_market_insights.csv",
  "data/processed/integrated.csv",   # ok if missing
]
paths = [p for p in paths if os.path.exists(p)]

profiles = {}
for p in paths:
    try:
        df = pd.read_csv(p)
        profiles[os.path.basename(p)] = {
            "rows": int(len(df)),
            "cols": int(df.shape[1]),
            "null_cells": int(df.isna().sum().sum()),
            "dup_rows": int(df.duplicated().sum()),
        }
    except pd.errors.EmptyDataError:
        profiles[os.path.basename(p)] = {"error": "empty file (no columns)"}

os.makedirs("results", exist_ok=True)
with open("results/quality_profile.json", "w") as f:
    json.dump(profiles, f, indent=2)
print("Wrote results/quality_profile.json")

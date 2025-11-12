import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
RES = ROOT / "results"
RES.mkdir(exist_ok=True)

targets = {
    "raw_df1": RAW / "ai_job_dataset.csv",
    "raw_df2": RAW / "ai_job_market_insights.csv",
    "integrated": PROC / "integrated_ai_jobs.csv",
}

profiles = {}
for name, p in targets.items():
    df = pd.read_csv(p)
    profiles[name] = {
        "rows": len(df),
        "columns": df.shape[1],
        "nulls_by_col": df.isna().sum().sort_values(ascending=False).to_dict(),
        "dupe_rows": int(df.duplicated().sum()),
    }

pd.Series(profiles).to_json(RES / "quality_profile.json", indent=2)
print("Saved results/quality_profile.json")

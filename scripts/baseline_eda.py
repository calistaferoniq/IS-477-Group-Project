import pandas as pd
from pathlib import Path

df = pd.read_csv("data/processed/integrated_ai_jobs.csv")
RESULTS = Path("results"); RESULTS.mkdir(exist_ok=True)

summary = {
    "rows": len(df),
    "cols": df.shape[1],
    "duplicate_rows": int(df.duplicated().sum()),
    "missing_values_total": int(df.isna().sum().sum()),
}

pd.Series(summary).to_csv(RESULTS / "eda_summary.csv")

# Per-column missingness
df.isna().mean().sort_values(ascending=False).to_csv(RESULTS / "missing_by_column.csv")

# Top categories if present
for col in ["job_title", "company", "location"]:
    if col in df.columns:
        df[col].value_counts().head(20).to_csv(RESULTS / f"top_{col}.csv")

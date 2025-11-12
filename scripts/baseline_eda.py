# -*- coding: utf-8 -*-
# Baseline EDA that matches your current integration output
# Looks for data/processed/jobs_unified.csv first; falls back to integrated_ai_jobs.csv

import json
from pathlib import Path
import pandas as pd
import numpy as np

# Make matplotlib work headless (e.g., Codespaces, CI)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
PROC = ROOT / "data" / "processed"
IMAGES = ROOT / "images"
RESULTS = ROOT / "results"

IMAGES.mkdir(parents=True, exist_ok=True)
RESULTS.mkdir(parents=True, exist_ok=True)

CANDIDATES = [
    PROC / "jobs_unified.csv",           # your current integrate_datasets output
    PROC / "integrated_ai_jobs.csv",     # fallback if you later rename
]

def load_processed():
    for p in CANDIDATES:
        if p.exists() and p.stat().st_size > 0:
            print(f"[INFO] Using processed file: {p}")
            return pd.read_csv(p), p.name
    raise FileNotFoundError(
        "No processed file found. Expected one of:\n"
        + "\n".join([str(p) for p in CANDIDATES])
    )

df, used_name = load_processed()

# Expected columns from your integration:
# Job_Title, Salary_USD, Education_Required, Years_Experience,
# AI_Adoption_Level, Automation_Risk, Remote_Friendly,
# Job_Growth_Projection (may be missing in your current script), Match_Type

# ---- Basic cleaning / dtypes ----
# Lowercase consistent string columns that might appear
for col in ["Job_Title", "Education_Required", "AI_Adoption_Level",
            "Automation_Risk", "Remote_Friendly", "Match_Type",
            "Job_Growth_Projection"]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Coerce numeric cols if present
for col in ["Salary_USD", "Years_Experience"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ---- Missingness profile ----
missing = df.isna().mean().sort_values(ascending=False)
missing.to_csv(RESULTS / "eda_missing_rates.csv")

# ---- Save a quick schema snapshot ----
schema = {
    "file_used": used_name,
    "rows": int(df.shape[0]),
    "cols": int(df.shape[1]),
    "columns": df.columns.tolist()
}
(Path(RESULTS) / "eda_schema.json").write_text(json.dumps(schema, indent=2))

# ---- Numeric summaries & plots ----
numeric_cols = [c for c in ["Salary_USD", "Years_Experience"] if c in df.columns]
for col in numeric_cols:
    desc = df[col].describe(percentiles=[0.25, 0.5, 0.75])
    desc.to_csv(RESULTS / f"eda_describe_{col}.csv")

    # histogram
    plt.figure()
    df[col].dropna().plot.hist(bins=30)
    plt.title(f"Histogram: {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMAGES / f"hist_{col}.png")
    plt.close()

    # boxplot
    plt.figure()
    plt.boxplot(df[col].dropna(), vert=True)
    plt.title(f"Boxplot: {col}")
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(IMAGES / f"box_{col}.png")
    plt.close()

# Scatter: Salary vs Experience (if both present)
if all(c in df.columns for c in ["Salary_USD", "Years_Experience"]):
    plt.figure()
    plt.scatter(df["Years_Experience"], df["Salary_USD"], s=10, alpha=0.6)
    plt.title("Salary_USD vs Years_Experience")
    plt.xlabel("Years_Experience")
    plt.ylabel("Salary_USD")
    plt.tight_layout()
    plt.savefig(IMAGES / "scatter_salary_vs_experience.png")
    plt.close()

# ---- Categorical frequency tables & plots ----
cat_candidates = [
    "Education_Required",
    "AI_Adoption_Level",
    "Automation_Risk",
    "Remote_Friendly",
    "Match_Type",
    "Job_Growth_Projection"  # may be missing; this is OK
]
for col in cat_candidates:
    if col in df.columns:
        vc = (df[col]
              .replace({"nan": np.nan})  # in case strings "nan" slipped in
              .dropna()
              .value_counts()
              .head(15))
        vc.to_csv(RESULTS / f"eda_freq_{col}.csv")

        plt.figure()
        vc.plot.bar(rot=45)
        plt.title(f"Top {len(vc)} {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(IMAGES / f"bar_{col}.png")
        plt.close()

# ---- Group summaries helpful for the report ----
# Mean salary by Remote_Friendly (if both exist)
if "Salary_USD" in df.columns and "Remote_Friendly" in df.columns:
    g = df.groupby("Remote_Friendly", dropna=False)["Salary_USD"].mean().sort_values(ascending=False)
    g.to_csv(RESULTS / "eda_mean_salary_by_remote.csv")

    plt.figure()
    g.plot.bar(rot=0)
    plt.title("Mean Salary by Remote_Friendly")
    plt.xlabel("Remote_Friendly")
    plt.ylabel("Mean Salary_USD")
    plt.tight_layout()
    plt.savefig(IMAGES / "bar_mean_salary_by_remote.png")
    plt.close()

# Cross-tab: Automation_Risk x Remote_Friendly (if both exist)
if "Automation_Risk" in df.columns and "Remote_Friendly" in df.columns:
    ct = pd.crosstab(df["Automation_Risk"], df["Remote_Friendly"])
    ct.to_csv(RESULTS / "eda_crosstab_automation_vs_remote.csv")

# Top titles by count
if "Job_Title" in df.columns:
    top_titles = df["Job_Title"].value_counts().head(20)
    top_titles.to_csv(RESULTS / "eda_top_job_titles.csv")

    plt.figure()
    top_titles.sort_values(ascending=True).plot.barh()
    plt.title("Top 20 Job Titles")
    plt.xlabel("Count")
    plt.ylabel("Job_Title")
    plt.tight_layout()
    plt.savefig(IMAGES / "barh_top_job_titles.png")
    plt.close()

print("Wrote baseline EDA outputs to:")
print(f"  {IMAGES}/ (charts)")
print(f"  {RESULTS}/ (CSV summaries)")

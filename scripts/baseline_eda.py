from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROC = Path("data/processed"); IMG = Path("images"); RES = Path("results")
IMG.mkdir(exist_ok=True); RES.mkdir(exist_ok=True)

df = pd.read_csv(PROC/"jobs_unified.csv")

# Example summaries
df.describe(include="all").to_csv(RES/"eda_describe.csv")
df["Match_Type"].value_counts(dropna=False).to_csv(RES/"eda_match_type_counts.csv")

# Salary distribution (guard for missing)
if "Salary_USD" in df.columns and pd.api.types.is_numeric_dtype(df["Salary_USD"]):
    df["Salary_USD"].dropna().plot(kind="hist", bins=30, title="Salary USD")
    plt.xlabel("Salary_USD")
    plt.tight_layout()
    plt.savefig(IMG/"eda_salary_hist.png"); plt.clf()

# Experience distribution
if "Years_Experience" in df.columns and pd.api.types.is_numeric_dtype(df["Years_Experience"]):
    df["Years_Experience"].dropna().plot(kind="hist", bins=20, title="Years of Experience")
    plt.xlabel("Years_Experience")
    plt.tight_layout()
    plt.savefig(IMG/"eda_experience_hist.png"); plt.clf()

print("Wrote figures to images/ and tables to results/")

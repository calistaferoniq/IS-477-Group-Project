import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROC = ROOT / "data" / "processed"
IMG = ROOT / "images"
RES = ROOT / "results"
IMG.mkdir(exist_ok=True); RES.mkdir(exist_ok=True)

df = pd.read_csv(PROC / "integrated_ai_jobs.csv")

# Example 1: top job titles
top_titles = df["job_title"].str.lower().value_counts().head(10)
top_titles.to_csv(RES / "eda_top_titles.csv")
plt.figure(); top_titles.plot(kind="bar"); plt.title("Top 10 Job Titles")
plt.tight_layout(); plt.savefig(IMG / "eda_top_titles.png"); plt.close()

# Example 2: salary by city (median)
if "salary" in df.columns and "city" in df.columns:
    sal_city = df.groupby(df["city"].str.lower())["salary"].median().sort_values(ascending=False).head(10)
    sal_city.to_csv(RES / "eda_salary_by_city.csv")
    plt.figure(); sal_city.plot(kind="bar"); plt.title("Median Salary by City (Top 10)")
    plt.tight_layout(); plt.savefig(IMG / "eda_salary_by_city.png"); plt.close()

# Example 3: remote friendliness if present
for c in ["remote_friendly","Remote_Friendly","is_remote","remote"]:
    if c in df.columns:
        remote_counts = df[c].astype(str).str.lower().value_counts()
        remote_counts.to_csv(RES / "eda_remote_counts.csv")
        plt.figure(); remote_counts.plot(kind="bar"); plt.title("Remote-Friendly Distribution")
        plt.tight_layout(); plt.savefig(IMG / "eda_remote_counts.png"); plt.close()
        break

print("Wrote EDA images/ + results/")

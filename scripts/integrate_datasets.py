# Imports
import pandas as pd
from pathlib import Path
from rapidfuzz import process, fuzz
from util_hash import write_sha256, write_acquisition_log


csv_path1 = Path("data/raw/ai_job_dataset.csv")
csv_path2 = Path("data/raw/ai_job_market_insights.csv")
# Load the dataset into a pandas DataFrame (example for a CSV file)
df1 = pd.read_csv(csv_path1)
df2 = pd.read_csv(csv_path2)

# # Integrate Datasets with exact matching and fuzzy matching

# Raw data loaded above (df1 and df2)

# Standardize column names

df1 = df1.rename(columns={
    "job_title": "Job_Title",
    "salary_usd": "Salary_USD",
    "education_required": "Education_Required",
    "years_experience": "Years_Experience"
})

df1["Job_Title"] = df1["Job_Title"].str.lower().str.strip()
df2["Job_Title"] = df2["Job_Title"].str.lower().str.strip()

# Deduplicate job titles

df1_unique = df1.groupby("Job_Title").agg({
    "Salary_USD": "mean",
    "Education_Required": lambda s: s.mode().iloc[0] if not s.mode().empty else None,
    "Years_Experience": "mean"
}).reset_index()

df2_unique = df2.groupby("Job_Title").agg({
    "AI_Adoption_Level": lambda s: s.mode().iloc[0] if not s.mode().empty else None,
    "Automation_Risk": lambda s: s.mode().iloc[0] if not s.mode().empty else None,
    "Remote_Friendly": lambda s: s.mode().iloc[0] if not s.mode().empty else None,
    "Job_Growth_Projection": lambda s: s.mode().iloc[0] if not s.mode().empty else None
}).reset_index()

# Deduplication results

print("Unique df1 titles:", len(df1_unique))
print("Unique df2 titles:", len(df2_unique))

# Find exact matches

exact = pd.merge(df1_unique, df2_unique, on="Job_Title", how="inner")
exact["Match_Type"] = "Exact"

print("Exact matches:", len(exact))

# Identify unmatched titles

df1_unmatched = df1_unique[~df1_unique["Job_Title"].isin(exact["Job_Title"])]
df2_titles = df2_unique["Job_Title"].tolist()

# Fuzzy matching using a token

fuzzy_rows = []

for idx, row in df1_unmatched.iterrows():
    title = row["Job_Title"]
    
    best_match = process.extractOne(
        title,
        df2_titles,
        scorer=fuzz.token_set_ratio
    )
    
    if best_match and best_match[1] >= 75:  
        match_title = best_match[0]
        similarity = best_match[1]
        
        df2_row = df2_unique[df2_unique["Job_Title"] == match_title].iloc[0]
        
        fuzzy_rows.append({
            "Job_Title": title,
            "Salary_USD": row["Salary_USD"],
            "Education_Required": row["Education_Required"],
            "Years_Experience": row["Years_Experience"],
            "AI_Adoption_Level": df2_row["AI_Adoption_Level"],
            "Automation_Risk": df2_row["Automation_Risk"],
            "Remote_Friendly": df2_row["Remote_Friendly"],
            "Job_Growth_Projection": df2_row["Job_Growth_Projection"],
            "Match_Type": f"Approximate ({similarity})"
        })

print("Approximate matches:", len(fuzzy_rows))

approx = pd.DataFrame(fuzzy_rows)

# Combine exact + approximate

final = pd.concat([exact, approx], ignore_index=True)

# Add unmatched df1 jobs back in

matched_titles = set(final["Job_Title"].tolist())

df1_unmatched_rows = df1_unique[~df1_unique["Job_Title"].isin(matched_titles)].copy()

df1_unmatched_rows["AI_Adoption_Level"] = None
df1_unmatched_rows["Automation_Risk"] = None
df1_unmatched_rows["Remote_Friendly"] = None
df1_unmatched_rows["Match_Type"] = "Unmatched"

final_with_unmatched = pd.concat([final, df1_unmatched_rows], ignore_index=True)

processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

output_path = processed_dir / "jobs_unified.csv"
final_with_unmatched.to_csv(output_path, index=False)

print("Wrote processed file to:", output_path)

# Checksum
checksum = write_sha256(str(output_path))
print("SHA256 checksum:", checksum)

write_acquisition_log(
    path=str(output_path),
    source_slug="integration_pipeline",
    note="Integrated df1 and df2 with exact + fuzzy matching."
)






# Integration schema (draft)

## Goal
Define a unified table that lets us join/compare the two raw files:
- `data/raw/ai_job_dataset.csv` (df1)
- `data/raw/ai_job_market_insights.csv` (df2)

## Proposed unified columns
| unified_col              | type      | from df1                         | from df2                   | notes / transforms |
|--------------------------|-----------|----------------------------------|----------------------------|--------------------|
| job_id                   | string    | job_id                           | —                          | keep as string     |
| title                    | string    | job_title                        | Job_Title                  | lowercase/trim     |
| company_name             | string    | company_name                     | —                          | trim/clean         |
| industry                 | string    | industry                         | Industry                   | prefer df1 if both |
| company_size             | enum      | company_size                     | Company_Size               | map to {S,M,L}     |
| location                 | string    | company_location                 | Location                   | store as text      |
| employee_residence       | string    | employee_residence               | —                          | optional           |
| salary_usd               | float     | salary_usd                       | Salary_USD                 | prefer df1 if both |
| salary_currency          | string    | salary_currency                  | —                          | assume USD for df2 |
| remote_ratio             | int       | remote_ratio (0/50/100)          | —                          | keep df1           |
| remote_friendly          | boolean   | —                                | Remote_Friendly (Yes/No)   | map to true/false  |
| experience_level         | enum      | experience_level                 | —                          | keep df1 codes     |
| employment_type          | string    | employment_type                  | —                          | keep df1           |
| required_skills          | string    | required_skills                  | Required_Skills            | store pipe-joined  |
| education_required       | string    | education_required               | —                          | keep df1           |
| years_experience         | int       | years_experience                 | —                          | keep df1           |
| job_description_length   | int       | job_description_length           | —                          | keep df1           |
| benefits_score           | float     | benefits_score                   | —                          | keep df1           |
| ai_adoption_level        | enum      | —                                | AI_Adoption_Level          | keep df2           |
| automation_risk          | enum      | —                                | Automation_Risk            | keep df2           |
| job_growth_projection    | string    | —                                | Job_Growth_Projection      | keep df2           |
| posting_date             | date      | posting_date                     | —                          | ISO-date           |
| application_deadline     | date      | application_deadline             | —                          | ISO-date           |

## Join strategy
- Primary ID exists only in df1 (`job_id`).  
- To compare/augment df1 with df2, build a **join_key**:  
  `join_key = lower(trim(title)) + '|' + lower(trim(company_name)) + '|' + lower(trim(location))`  
  (df2 has `Job_Title` and `Location` but no company name; when company is missing, use title+location only and treat as left-join enrichment.)

## Transform rules (high level)
- Normalize case/whitespace on all string columns.
- Map `Company_Size` to {S,M,L} consistently across both.
- Coerce dates to ISO (`YYYY-MM-DD`).
- Map df2 `Remote_Friendly` → boolean; keep df1 `remote_ratio` as numeric.
- Prefer df1 for overlapping salary; if df1 is null, fill from df2.
- Keep `required_skills` as a single pipe-delimited string for now (can explode later for analysis).

## Next steps
1. Prototype a small integration script that builds `join_key`, aligns columns, and writes `data/processed/integrated_jobs.csv` (ignored by git).
2. Run baseline EDA on df1, df2, and the integrated output and save summary tables/plots into `results/`.
3. Update Issue #3 with decisions and any open questions.

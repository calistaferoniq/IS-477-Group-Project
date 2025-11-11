# Integration schema (draft)

## Goal
Define a unified table to join/compare the two raw files:
- data/raw/ai_job_dataset.csv  (df1)
- data/raw/ai_job_market_insights.csv (df2)

## Proposed unified columns
| unified_col              | type     | from df1                         | from df2                 | notes / transforms |
|--------------------------|----------|----------------------------------|--------------------------|--------------------|
| job_id                   | string   | job_id                           | —                        | keep as string     |
| title                    | string   | job_title                        | Job_Title                | normalize case     |
| company_name             | string   | company_name                     | —                        | trim/clean         |
| industry                 | string   | industry                         | Industry                 | pick df1 when both |
| company_size             | enum     | company_size                     | Company_Size             | map to {S,M,L}     |
| company_location         | string   | company_location                 | Location                 | store country/region text |
| employee_residence       | string   | employee_residence               | —                        | optional           |
| salary_usd               | float    | salary_usd                       | Salary_USD               | prefer df1 if both present |
| salary_currency          | string   | salary_currency                  | —                        | keep as ISO code   |
| experience_level         | enum     | experience_level                 | —                        | map to {JR, MID, SR, EXEC} |
| employment_type          | enum     | employment_type                  | —                        | {FT, PT, CT, FL}   |
| years_experience         | int      | years_experience                 | —                        | >=0                |
| required_skills          | array    | required_skills                  | Required_Skills          | split on , or ; and lowercase |
| remote_ratio             | int      | remote_ratio                     | —                        | {0,50,100}         |
| remote_friendly          | enum     | —                                | Remote_Friendly          | map Yes/No/Hybrid → {100,0,50} if deriving remote_ratio |
| ai_adoption_level        | enum     | —                                | AI_Adoption_Level        | keep strings       |
| automation_risk          | enum     | —                                | Automation_Risk          | keep strings       |
| job_growth_projection    | string   | —                                | Job_Growth_Projection    | text/label         |
| posting_date             | date     | posting_date                     | —                        | ISO-8601           |
| application_deadline     | date     | application_deadline             | —                        | ISO-8601           |
| job_description_length   | int      | job_description_length           | —                        | >=0                |
| benefits_score           | float    | benefits_score                   | —                        | 0..1 or 0..5? keep raw |
| source_file              | string   | (derived 'df1')                  | (derived 'df2')          | lineage column     |

## Keys / lineage
- Natural key is weak; retain `job_id` (df1) and also create a SHA256 of (title, company_name, posting_date) for de-dup.
- Keep source‐of‐truth per field as listed above.

## Cleaning rules (high level)
- Trim whitespace, collapse double spaces.
- Standardize case for enums (upper).
- Dates → ISO `YYYY-MM-DD`; coerce invalid to NULL and log counts.
- Skills → split on `[;,]`, strip, lowercase, de-dup per row.

## Outputs
- Leave raw files in `data/raw/`.
- Write integrated table later to `data/processed/integrated_jobs.parquet` with the schema above.

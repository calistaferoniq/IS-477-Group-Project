# Integration schema (draft)

## Raw sources
- `data/raw/ai_job_dataset.csv` (df1)  
  Columns: `job_id, job_title, salary_usd, salary_currency, experience_level, employment_type, company_location, company_size, employee_residence, remote_ratio, required_skills, education_required, years_experience, industry, posting_date, application_deadline, job_description_length, benefits_score, company_name`
- `data/raw/ai_job_market_insights.csv` (df2)  
  Columns: `Job_Title, Industry, Company_Size, Location, AI_Adoption_Level, Automation_Risk, Required_Skills, Salary_USD, Remote_Friendly, Job_Growth_Projection`

## Unified table (`jobs_unified`)
| unified_col            | type   | from df1             | from df2                | rule / notes |
|------------------------|--------|----------------------|-------------------------|--------------|
| job_id                 | str    | `job_id`             | —                       | keep df1; if missing in future data, surrogate = SHA256 of `lower(title)|lower(company_name)|posting_date` |
| title                  | str    | `job_title`          | `Job_Title`             | trim; case-normalize (e.g., title case) |
| company_name           | str    | `company_name`       | —                       | trim |
| industry               | str    | `industry`           | `Industry`              | prefer df1; fallback df2 |
| company_size           | enum   | `company_size`       | `Company_Size`          | map to {S,M,L}: {Small,S}→S, {Medium,Mid,M}→M, {Large,L}→L |
| location               | str    | `company_location`   | `Location`              | keep provided country/region text |
| employee_residence     | str    | `employee_residence` | —                       | optional |
| salary_usd             | float  | `salary_usd`         | `Salary_USD`            | prefer df1 if both present; cast to float |
| salary_currency        | str    | `salary_currency`    | —                       | keep ISO-like code as text |
| experience_level       | enum   | `experience_level`   | —                       | normalize to {JUNIOR,MID,SENIOR,EXEC} |
| employment_type        | enum   | `employment_type`    | —                       | normalize to {FT,PT,CT,FL,INTERN} |
| remote_ratio           | int    | `remote_ratio`       | —                       | 0/50/100 from df1 |
| remote_friendly        | enum   | —                    | `Remote_Friendly`       | keep df2 value (e.g., {Yes,No,Partial}); optional bridge to `remote_ratio` |
| required_skills        | str    | `required_skills`    | `Required_Skills`       | lowercase; split tokens; store joined with `;` |
| education_required     | str    | `education_required` | —                       | passthrough |
| years_experience       | int    | `years_experience`   | —                       | passthrough |
| posting_date           | str    | `posting_date`       | —                       | keep as text for now (YYYY-MM-DD if/when normalized) |
| application_deadline   | str    | `application_deadline` | —                     | keep as text for now |
| job_description_length | int    | `job_description_length` | —                   | passthrough |
| benefits_score         | float  | `benefits_score`     | —                       | passthrough |
| ai_adoption_level      | enum   | —                    | `AI_Adoption_Level`     | from df2 |
| automation_risk        | enum   | —                    | `Automation_Risk`       | from df2 |
| job_growth_projection  | enum   | —                    | `Job_Growth_Projection` | from df2 |

**Output target:** write the unified table to `data/processed/jobs_unified.csv`.

### Normalization notes
- **company_size:** `{Small,S}`→`S`, `{Medium,Mid,M}`→`M`, `{Large,L}`→`L`.
- **experience_level:** casefold and map synonyms to `{JUNIOR,MID,SENIOR,EXEC}`.
- **employment_type:** map to `{FT,PT,CT,FL,INTERN}`.
- **required_skills:** split on commas/semicolons, trim, lowercase, rejoin with `;`.

### Keying / join guidance
df2 lacks a `job_id`. When enriching df1 with df2, use a soft key on
`lower(title)`, `company_size (bucketed)`, and `lower(location)`; compute a `match_confidence`.
Hard left-join on df1; don’t duplicate df1 rows.


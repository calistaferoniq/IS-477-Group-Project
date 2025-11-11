# Integration schema (draft)

## Raw sources
- 'data/raw/ai_job_dataset.csv' (df1)  
  Columns: `job_id, job_title, salary_usd, salary_currency, experience_level, employment_type, company_location, company_size, employee_residence, remote_ratio, required_skills, education_required, years_experience, industry, posting_date, application_deadline, job_description_length, benefits_score, company_name`
- 'data/raw/ai_job_market_insights.csv' (df2)  
  Columns: `Job_Title, Industry, Company_Size, Location, AI_Adoption_Level, Automation_Risk, Required_Skills, Salary_USD, Remote_Friendly, Job_Growth_Projection`

## Unified table (`jobs_unified`)
| unified_col            | type   | from df1             | from df2                | rule / notes |
|------------------------|--------|----------------------|-------------------------|--------------|
| Job_Title              | str    | 'job_title'          | 'Job_Title'             | case-normalize |
| Salary_USD             | float  | 'salary_usd'         | 'Salary_USD'            | prefer df1 if both present|
| Remote_Friendly        | str   | —                    | 'Remote_Friendly'       | from df2 |
| Required_Skills        | str    | 'required_skills'    | 'Required_Skills'       | prefer df1 |
| Education_Required     | str    | 'education_required' | —                       | from df1 |
| Years_Experience       | int    | 'years_experience'   | —                       | from df1 |
| AI_Adoption_Level      | str   | —                    | 'AI_Adoption_Level'     | from df2 |
| Automation_Risk        | str   | —                    | 'Automation_Risk`       | from df2 |
| Job_Growth_Projection  | str   | —                    | 'Job_Growth_Projection` | from df2 |
| Match_Type             | str   | —                    | —             | Exact, Approximate (similarity score), or Unmatched |

**Output target:** write the unified table to `jobs_unified.csv`.

### Keying / join guidance
- Join on job_title, case normalize both df1 and df2
- Deduplicate job titles by aggregating job titles and keeping the mean value of numeric features and mode of categorical features
- Exact match and then fuzzy match on a token_set_ratio threshold of 75
- Combine exact matches, approximate matches, and unmatched rows from df1 into a final unified table 'jobs_unified.csv'



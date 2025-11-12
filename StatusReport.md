# IS-477 Interim Status Report — AI Job Market Project (M3)

> **Commit attribution note.** Most commits appear under **Calista** because we worked side-by-side on the **same laptop/session** to reduce setup friction. Faith contributed in real time via pair-programming, data checks, and planning; the Git history reflects the one logged-in account.

---

## 1) What we’re building (quick recap)

We’re curating and integrating multiple **AI/ML job-market datasets** to understand how **roles, skills, geography/remote patterns, and compensation** interact.

**Guiding questions**
1. **Demand:** How do titles/role families, skills, and geography relate to posting volume?  
2. **Compensation:** When salaries are present, how do seniority, skills, and company type relate to pay?  
3. **Skills:** Which skills co-occur by role family (e.g., DS vs MLE vs AI PM)?  
4. **Geography/Remote:** How do onsite/hybrid/remote patterns vary by role family and seniority?

**Audience:** Students exploring AI careers, advisors, and recruiters who want data-grounded signals.

---

## 2) Repository snapshot (current state)

```

IS-477-Group-Project/
├─ data/
│  ├─ raw/                         # target home for source CSVs  (has .gitkeep; CSVs not moved yet)
│  ├─ processed/                   # cleaned/integrated outputs   (has .gitkeep)
│  └─ hashes/                      # integrity + provenance
│     ├─ ai_job_dataset.csv.sha256
│     ├─ ai_job_market_insights.csv.sha256
│     ├─ ai_job_dataset_acquisition_log.txt
│     └─ ai_job_market_insights_acquisition_log.txt
├─ images/                         # figures/screenshots (scaffolded)
├─ results/                        # EDA/quality reports (scaffolded)
├─ scripts/                        # pipeline scripts (scaffolded)
├─ ProjectPlan.md
├─ StatusReport.md                 # this interim report
├─ ai_job_dataset.csv              # currently at repo root (to be moved to data/raw/)
└─ ai_job_market_insights.csv      # currently at repo root (to be moved to data/raw/)

````

**Evidence already in repo**
- **Integrity + provenance:** SHA-256 checksums and acquisition logs for both CSVs under `data/hashes/`.
- **Project hygiene:** Standard data science layout scaffolded; issues created for M3 tasks; release created for the **Project Plan**.
- **Open issues tracking M3 scope:** #4 Kaggle reliability spot-checks, #5 Quality profiling, #6 Baseline EDA, #7 Gaps→uncertainties, #8 Interim status report.

---

## 3) Course-facing status (integrated summary)

### Project Plan — task updates
We completed and submitted the **Project Plan** (in GitHub & Canvas) and began executing it. Data storage strategy is established with consistent naming. We acquired the planned job-market datasets and documented **methods and access**. We’ve started **data assessment/cleaning**; **integration** is planned next. Model building, automation, and full reproducibility tasks will follow the profiling + cleaning pass.

### Updated timeline (week framing → concrete dates)
- Weeks 4–6 → **Completed** data acquisition & documentation.  
- Weeks 6–8 → **Completed** repository layout and hygiene.  
- Weeks 7–9 → **In progress** profiling/quality (scheduled **Nov 16–17** for full artifacts).  
- Week 10 → **This** Interim Status Report (Nov 12).  
- Weeks 11–12 → **Integration/enrichment** (Nov 18–22).  
- Weeks 12–13 → **Modeling** (if applicable) & mapping lock (Nov 25–Dec 1).  
- Weeks 13–14 → **Automation & README** (Nov 25 onward).  
- Week 15 → **Final** submission (Dec 10).

### Changes to plan (source notes)
- We prioritized **provenance/traceability** (hashes + logs) and **repo hygiene** earlier to make the rest of the pipeline safer to run.
- External source reliability will be **audited** with a 30-record stratified sample (Nov 22), and limitations will be clearly documented.

---

## 4) Data sources & provenance (current)

- **`ai_job_dataset.csv`** — in repo; **hash + acquisition log present** under `data/hashes/`.  
  **Next:** Move to `data/raw/` and append `license_name` and `license_url` in the acquisition log.

- **`ai_job_market_insights.csv`** — in repo; **hash + acquisition log present** under `data/hashes/`.  
  **Next:** Move to `data/raw/` and append license details in the acquisition log.

**Handling principles**
- No personal contact fields will be extracted.
- Keep `*_raw` text fields immutable; publish normalized counterparts separately.
- Record license/terms in acquisition logs for clarity.

---

## 5) Canonical schema (draft) & harmonization

**Core fields**
- Keys/source: `job_id` (source-scoped), `source_name`, `source_post_url`
- Role/company: `title_raw`, `title_norm`, `role_family`, `company_raw`, `company_norm`
- Location: `city`, `region`, `country`, `remote_type` (Onsite/Hybrid/Remote)
- Timing/type: `posted_date` (ISO), `employment_type` (FT/PT/Contract/Intern)
- Seniority: `seniority_norm` (Intern/Junior/Mid/Senior/Lead/Principal/Director/VP)
- Skills: `skills_raw`, `skills_norm` (canonical list)
- Compensation: `salary_min`, `salary_max`, `salary_currency`, `salary_period` (hour/annual), `salary_min_usd`, `salary_max_usd`
- Text: `description_raw` (optional)

**Normalization**
- **Titles → role_family:** regex/keyword mapping; publish `results/title_to_role_mapping.csv`.
- **Seniority mapping:** rule-based standardization; publish coverage in `results/seniority_mapping.csv`.
- **Skills:** tokenize → canonical dictionary; keep both raw and normalized.
- **Compensation:** normalize currency/period → annual USD where possible; **report coverage %**.
- **Location:** parse city/region/country; report parse success; fall back to country only when needed.

---

## 6) Quality profiling & reliability checks (plan + status)

**Planned artifacts (to land in `results/`)**
- Per-source profiles: `eda_ai_job_dataset.html`, `eda_ai_job_market_insights.html`
- Quality narratives: `quality_report_ai_job_dataset.md`, `quality_report_ai_job_market_insights.md`
- Integrated view: `eda_integrated.html`, `quality_report_integrated.md`
- Coverage tables: `title_mapping_coverage.csv`, `seniority_mapping.csv`
- Dedupe transparency: `dedupe_report.md` (candidate pairs, thresholds, accept/reject summary)

**Reliability spot-checks (external)**
- Stratified sample **n=30** across role family & geography.
- Verify **title, company, location, remote flag, posted date, salary range** vs original listing (when accessible); report agreement rates + typical mismatch causes.

**Status today**
- Structure and issues in place; profiles and reports will be generated once the two CSVs are moved to `data/raw/` and scripts are run (see §9).

---

## 7) Integration & dedupe strategy

- **Blocking:** `(company_norm, title_norm, country)` + a **posted_date window**.  
- **Similarity:** fuzzy title/description; **Jaccard** on `skills_norm`.  
- **Policy:** conservative accept threshold; uncertain pairs → `possible_duplicate = true`.  
- **Transparency:** publish pair-level scores and examples in `dedupe_report.md`.

---

## 8) Risks & explicit uncertainties (with measurements)

| Risk / Gap | Why it matters | How we’ll measure/report |
|---|---|---|
| **Sparse salary fields** | Comp analyses can be biased | **Salary coverage %** by source & role family; only plot distributions where coverage ≥ threshold |
| **Title ambiguity** | Role family misclassification | Publish mapping table + **mapping coverage %**; list unmapped titles |
| **Location parse errors** | Weak geo/remote analyses | **Parse success %**; fall back to country level where needed |
| **Cross-source duplicates** | Inflated counts | `dedupe_report.md` with counts, thresholds, and example pairs |
| **Temporal drift** | Skewed time series | Validate date distributions; flag stale/clustered dates |

---

## 9) Reproducible workflow (grader run-book)

> **Scripts will be committed in `scripts/` immediately after M3.** The run-book is locked now so expectations are clear.

**Inputs:** `data/raw/*.csv` (+ matching `.sha256` in `data/hashes/`)  
**Outputs:** `data/processed/…`, `results/…`, `images/…`

```bash
# (0) Environment
python -m pip install -r requirements.txt

# (1) Verify checksums
python scripts/_verify_hashes.py data/raw data/hashes

# (2) Per-source profiling
python scripts/01_profile_sources.py

# (3) Clean + harmonize → canonical schema
python scripts/02_clean_harmonize.py

# (4) Integrate + dedupe
python scripts/03_integrate.py

# (5) Integrated EDA + figures
python scripts/04_eda_integrated.py
python scripts/05_figures.py
````

Each step drops a small `_ok_<step>.txt` and appends to `results/run_manifest.json` (inputs, hashes, timestamps).

---

## 10) Success metrics (TA-verifiable)

* **100%** files in `data/raw/` have a matching `.sha256` **and** an acquisition log entry.
* **≥95%** of key fields parse to expected types (date/numeric/enums) or are explicitly flagged.
* **≥90%** of `title_raw` map to `role_family` (coverage table exported).
* **100%** of present salary fields normalized to annual USD; **coverage %** reported.
* **Dedupe transparency:** `dedupe_report.md` includes counts, thresholds, and example decisions.
* **Reproducibility:** Fresh clone + run-book yields identical processed hashes.

---

## 11) Completed vs remaining (accurate as of Nov 12)

**Completed**

* Standard repo scaffold (`data/raw`, `data/processed`, `data/hashes`, `results`, `images`, `scripts`).
* **Hashes + acquisition logs** for both CSVs in `data/hashes/`.
* Project hygiene: issues for M3, release for **Project Plan**.

**Pending (scheduled **after Nov 14**)**

* Move both CSVs to `data/raw/` and update acquisition logs with **license_name + license_url**.
* Generate **per-source EDA profiles** and **quality reports** into `results/` (then consolidate under `results/eda/`).
* Export initial **figures** (top roles, skills, remote share, salary coverage) to `images/`.
* Commit initial **scripts** in `scripts/` and lock `requirements.txt`.
* **Automation** (end-to-end runner) will follow once profiling and cleaning are in.

---

## 12) Division of labor

* **Calista:** Repo creation, directory setup, file placement, SHA-256 hashing, acquisition logs, issue setup, report drafting, coordination.
* **Faith:** Pair-programming during setup, data sanity checks, rubric alignment, review of schema/risks/timeline.
* **Why commits concentrate under Calista:** single logged-in machine while both worked together.

---

## 13) Milestones & dates (all remaining tasks scheduled **after Nov 14**)

| Date          | Milestone                | Deliverables                                                                                                                        |
| ------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Nov 15–16** | Finalize raw layout      | Move `ai_job_dataset.csv` & `ai_job_market_insights.csv` → `data/raw/`; update acquisition logs with license info; verify checksums |
| **Nov 16–17** | Per-source EDA & quality | `eda_ai_job_dataset.html`, `eda_ai_job_market_insights.html`; `quality_report_*`.md; push to `results/eda/`                         |
| **Nov 18**    | Canonical mappings v1    | `title_to_role_mapping.csv`, `seniority_mapping.csv` + coverage tables in `results/`                                                |
| **Nov 20**    | Dedupe pass v1           | `dedupe_report.md` (thresholds, counts, example pairs)                                                                              |
| **Nov 22**    | Reliability audit        | `results/reliability_audit.md` (n=30, agreement rates & notes)                                                                      |
| **Nov 25**    | Run-book & scripts       | Commit `scripts/*.py`, `requirements.txt`; add README run instructions (draft)                                                      |
| **Dec 1**     | Integrated EDA & figures | `eda_integrated.html`; figures (top roles/skills, remote share, salary coverage) in `images/`                                       |
| **Dec 5**     | Freeze analysis          | Lock processed outputs; finalize narrative components                                                                               |
| **Dec 10**    | Final submission         | Report + tagged release; Canvas submission                                                                                          |

---

## 14) EDA figures (placeholder list to populate after scripts run)

* **Top role families by posting count** (bar).
* **Remote vs onsite/hybrid share** (by role family).
* **Salary coverage by role family** (coverage % bar).
* **Top skills overall & by role family** (table/heatmap).

> All raw EDA outputs (HTML/CSV/JSON) will live under `results/eda/` to keep one place to look.

---

## 15) Repo hygiene: EDA output consolidation (action item)

> **Instruction we’re following:** “Consolidate EDA outputs — You have `results/eda/` and a bunch of `results/eda_*.csv` at the results root. Move/emit everything under `results/eda/` for one place to look.”

**Plan**

* Create `results/eda/` (if not present).
* Place **all** profiling outputs there: `eda_*.html`, `eda_*.md/csv`, `*_profile.json`.
* Keep higher-level summaries (e.g., `quality_report_integrated.md`) in `results/` root, but **raw EDA dumps/tables** live under `results/eda/`.

---

## 16) Rubric coverage map

* **Problem & significance:** §1
* **Data sources & provenance:** §2 & §4 (`data/hashes/*`)
* **Schema & integration:** §5 & §7
* **EDA/quality methods & artifacts:** §6, §14, `results/` plan
* **Risks/uncertainties:** §8
* **Success metrics:** §10
* **Reproducibility:** §9 (README to be added post-M3)
* **Team roles:** §12
* **Timeline & next steps:** §13
* **Evidence links:** issues #4–#8, release for Project Plan

---

## 17) Quick submission checklist (M3)

* [ ] Move both CSVs to `data/raw/` and re-verify hashes
* [ ] Add `license_name` + `license_url` to both acquisition logs
* [ ] Export per-source **EDA** & **quality** artifacts to `results/eda/`
* [ ] Add 3–5 **figures** in `images/` and reference them in §14
* [ ] Commit initial **scripts** + `requirements.txt`; confirm issues #4–#8 link to artifacts

```
```


OLD PART:
---

# Status Report

## Project Plan Task Updates

We successfully completed and submitted our full Project Plan in Github repo and Canvas and have received feedback to which we will address in this report. We acquired the job market datasets as described in the plan and have documented methods and access. The data storage strategy has been established with clear naming and consistent record conventions. We have begun the data assessment including data cleaning which will lead us into data integration and enrichment. At the time of this report, we have not completed data integration. As such, progress will need to be made before we begin model building, automation, and reproducibility tasks. 

## Updated Timeline

| Week            | Task                                                                                           | Status        | Due Date            |
|-----------------|------------------------------------------------------------------------------------------------|--------------------|---------------------|
| Week 3 (Oct 7)  | Complete and submit the full Project Plan (ProjectPlan.md) in the GitHub repo and Canvas.     | Completed  | Oct 7, 2025         |
| Week 4-6        | Acquire job market datasets as described in the plan, thoroughly document methods, licenses, and access. | Completed  | Oct 14-28, 2025     |
| Week 6-8        | Design and implement the file/data storage strategy. Establish clear directory naming, record conventions. | Completed | Oct 28-Nov 11, 2025 |
| Week 7-9        | Data assessment: profile, quality check, initial cleaning (missing values, obvious outliers). Document issues found. | In progress  | Nov 4-18, 2025      |
| Week 10         | Submit Interim Status Report (StatusReport.md). Include: project status, updated tasks timeline, and GitHub repo evidence. | In progress  | Nov 11, 2025        |
| Week 11-12      | Conduct in-depth data integration and enrichment: join datasets, transform features, address semantic mismatches. | In progress  | Nov 18-25, 2025     |
| Week 12-13      | Develop, train, and validate the AI models for salary prediction and trend analysis.           | Not started  | Nov 25-Dec 2, 2025  |
| Week 13-14      | Automate workflow (Python scripts, Makefile/Snakemake), start compiling end-to-end provenance logs and metadata. | Not started  | Dec 2-9, 2025       |
| Week 14         | Document reproducibility instructions, update all data documentation, finalize visualizations/analysis outputs. | Not started  | Dec 9, 2025         |
| Week 15 (Dec 10)| Final project report and artifacts submitted on GitHub, tagged release, and Canvas submission. | Not started  | Dec 10, 2025        |

## Changes to Project Plan

**Datasets**: This project employs 2 synthetic datasets from Kaggle relating AI adoption and the job market. Both synthetic datasets are in the public domain and are intended to be used for educational purposes. While we did explore datasets from potentially more reliable sources, we did not find any widely available datasets that were appropriate for use in our research context. As such, these datasets from Kaggle based on real-world trends were the best alternative solution. However, this does mean that the findings from our analysis can not be definitively used for real-world application, but it can provide overarching insights into broader AI adoption and job market trends.

**Gaps**: In order to complete tasks from week 13-15, we need further insight into course concepts such as workflow automation, metadata standards, reproducibility methods. As we progress in this class, we will be able to better meet these needs and close potential knowledge gaps for this project.

## Contributions

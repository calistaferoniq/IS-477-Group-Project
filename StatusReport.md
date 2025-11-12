# IS-477 Interim Status Report — AI Job Market Project (M3)

---

## 1) Project Summary (quick recap)

We’re curating and integrating two **AI/ML job-market datasets** to understand how **roles, skills, remote patterns, and compensation** interact.

**Research questions**
- What are the primary job attributes and external factors that influence salary levels and job availability in an AI-driven economy?
- How accurately can AI models predict salary ranges based on AI adoption levels, experience level, and job growth projections?
- How do salary trends and job availabilities compare across varying degrees of AI technology adoption?

---

## 2) Repository snapshot 
```

IS-477-Group-Project/
├─ data/
│  ├─ raw/                         # target home for source CSVs 
│  ├─ processed/                   # cleaned/integrated outputs   
│  └─ hashes/                      # integrity + provenance
│     ├─ ai_job_dataset.csv.sha256
│     ├─ ai_job_market_insights.csv.sha256
│     ├─ ai_job_dataset_acquisition_log.txt
│     └─ ai_job_market_insights_acquisition_log.txt
├─ images/                         # figures/screenshots (scaffolded)
├─ results/                        # EDA/quality reports (scaffolded)
├─ scripts/                        # pipeline scripts (scaffolded)
├─ ProjectPlan.md
└─ StatusReport.md                 # this interim report

````

**Evidence already in repo**
- **Integrity + provenance:** SHA-256 checksums and acquisition logs for both CSVs under `data/hashes/`.
- **Integration:** integration script and schema drafts in appropriate folders
- **Project hygiene:** Standard data science layout scaffolded; issues created for M3 tasks; release created for the **Project Plan**.

---

## 3) Summary of Task Updates

We successfully completed and submitted our full Project Plan in Github repo and Canvas and have received feedback to which we will address in this report. We acquired the job market datasets as described in the plan and have documented methods and access. The data storage strategy has been established with clear naming and consistent record conventions. We have begun the data assessment including data cleaning which will lead us into data integration and enrichment. At the time of this report, we have not completed data integration. As such, progress will need to be made before we begin model building, automation, and reproducibility tasks. 

### Updated Timeline

| Week            | Task                                                                                           | Status        | Due Date            |
|-----------------|------------------------------------------------------------------------------------------------|--------------------|---------------------|
| Week 3 (Oct 7)  | Complete and submit the full Project Plan (ProjectPlan.md) in the GitHub repo and Canvas.     | Completed  | Oct 7, 2025         |
| Week 4-6        | Acquire job market datasets as described in the plan, thoroughly document methods, licenses, and access. | Completed  | Oct 14-28, 2025     |
| Week 6-8        | Design and implement the file/data storage strategy. Establish clear directory naming, record conventions. | Completed | Oct 28-Nov 11, 2025 |
| Week 7-9        | Data assessment: profile, quality check, initial cleaning (missing values, obvious outliers). Document issues found. | In progress  | Nov 4-18, 2025      |
| Week 10         | Submit Interim Status Report (StatusReport.md). Include: project status, updated tasks timeline, and GitHub repo evidence. | In progress  | Nov 11, 2025        |
| Week 11-12      | Conduct in-depth data integration and enrichment: join datasets, transform features, address semantic mismatches. | In progress  | Nov 10-25, 2025     |
| Week 12-13      | Develop, train, and validate the AI models for salary prediction and trend analysis.           | Not started  | Nov 25-Dec 2, 2025  |
| Week 13-14      | Automate workflow (Python scripts, Makefile/Snakemake), start compiling end-to-end provenance logs and metadata. | Not started  | Dec 2-9, 2025       |
| Week 14         | Document reproducibility instructions, update all data documentation, finalize visualizations/analysis outputs. | Not started  | Dec 2-9, 2025         |
| Week 15 (Dec 10)| Final project report and artifacts submitted on GitHub, tagged release, and Canvas submission. | Not started  | Dec 10, 2025        |

### Changes to project plan (based on feedback)

- **Datasets**: This project employs 2 synthetic datasets from Kaggle relating AI adoption and the job market. Both synthetic datasets are in the public domain and are intended to be used for educational purposes. While we did explore datasets from potentially more reliable sources, we did not find any widely available datasets that were appropriate for use in our research context. As such, these datasets from Kaggle based on real-world trends were the best alternative solution. However, this does mean that the findings from our analysis can not be definitively used for real-world application, but it can provide overarching insights into broader AI adoption and job market trends.
- **Gaps**: In order to complete tasks from week 13-15, we need further insight into course concepts such as workflow automation, metadata standards, reproducibility methods. As we progress in this class, we will be able to better meet these needs and close potential knowledge gaps for this project.

---

## 4) Data sources & provenance (current)

- **`ai_job_dataset.csv`** — in `data/raw/`; **hash + acquisition log present** under `data/hashes/`.  
- **`ai_job_market_insights.csv`** — in `data/raw/`; **hash + acquisition log present** under `data/hashes/`.  

**Handling principles**
- Keep `*_raw` text fields immutable; publish normalized counterparts separately.
- Record license/terms in acquisition logs for clarity.

---

## 5) Quality profiling & reliability checks (plan + status)

**Planned artifacts (to land in `results/`)**
- Per-source profiles: `eda_ai_job_dataset.html`, `eda_ai_job_market_insights.html`
- Quality narratives: `quality_report_ai_job_dataset.md`, `quality_report_ai_job_market_insights.md`
- Integrated view: `eda_integrated.html`, `quality_report_integrated.md`
- Dedupe transparency: `dedupe_report.md` (candidate pairs, thresholds, accept/reject summary)

---

## 6) Integration & dedupe strategy

- **Normalization:** deduplication and case normalization of job titles
- **Similarity:** fuzzy matching with threshold of 0.75
- **Schema:** integration schema `docs/integration_schema.md`

---

## 7) Reproducible workflow 

> **Scripts will be committed in `scripts/` immediately after M3.** 

**Inputs:** `data/raw/*.csv` (+ matching `.sha256` in `data/hashes/`)  
**Outputs:** `data/processed/…`, `results/…`, `images/…`

---

## 8) Completed vs remaining (accurate as of Nov 12)

**Completed**

* Standard repo scaffold (`data/raw`, `data/processed`, `data/hashes`, `results`, `images`, `scripts`).
* **Hashes + acquisition logs** for both CSVs in `data/hashes/`.

**Pending**

* Generate **per-source EDA profiles** and **quality reports** into `results/`.
* Commit initial **scripts** in `scripts/` and complete `requirements.txt`.
* **Automation** once profiling, cleaning, and all previous steps are completed.

---

## 9) Contributions

* **Calista:** Repo creation, directory setup, file placement, SHA-256 hashing, acquisition logs, issue setup, report drafting, coordination.
* **Faith:** Pair-programming during setup, data sanity checks, dataset integration, and rubric alignment.
* **Why commits concentrate under Calista:** single logged-in machine while both worked together.

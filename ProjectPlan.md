# Project Plan: AI-Powered Job Market Analysis and Salary Prediction

## Overview

The primary goal of this project is to explore and analyze the impact of artificial intelligence (AI) adoption on the global job market. By leveraging AI and data science techniques, the project aims to provide actionable insights into how AI-driven technological advancements influence job availability, salary trends, and the overall employment landscape within various industries. This will be achieved by integrating and analyzing multiple distinct datasets containing job listings, salary information, and AI adoption indicators.

The motivation behind this project stems from the rapidly evolving AI landscape and its transformative effects on the workforce. Understanding these dynamics is critical for job seekers aiming to align their skills with market demands, employers planning workforce strategies, and policymakers shaping labor regulations in an AI-influenced economy. The project will build a transparent, reproducible data analysis workflow encompassing data acquisition, cleaning, integration, and AI model-driven salary prediction and trend analysis. The findings will be documented and shared on GitHub for review, collaboration, and reuse.

## Research Questions

This project will address the following core research questions:

- How is AI adoption affecting the availability and type of jobs within different industries?
- Are there significant salary disparities between AI-related roles and traditional jobs across regions and sectors?
- How accurately can AI models predict salary ranges based on job descriptions, industry sectors, and geographical location?
- What are the primary job attributes and external factors that influence salary levels and job availability in an AI-driven economy?
- How do salary trends and job availabilities compare between countries with varying degrees of AI technology adoption?

Answering these questions will help reveal nuanced insights into the labor market shifts prompted by AI, providing practical guidance for stakeholders in career planning and organizational strategy.

## Team

- **Project Manager & Data Scientist (xxx):** As the lead, responsible for overseeing the project lifecycle including defining the project scope, acquiring datasets, performing data cleaning and integration, developing prediction models, and compiling the final report. This role will also focus on documentation, version control management, and ensuring reproducibility.
- **Lead Data Engineer (xxx):** This role, if applicable, will support managing data extraction processes, developing storage schemes, implementing automated data workflows, and assisting with maintaining data quality and provenance tracking.
- **GitHub Participation:** All collaborators will use Git and GitHub for version control and project management. Each member will have assigned responsibilities reflected transparently through commit messages, pull requests, and issue tracking to demonstrate individual contributions. The repository will be organized to facilitate straightforward navigation and collaboration.

## Datasets

The project will employ at least two heterogeneous datasets to meet the course criteria of using multiple sources with different access methods and formats:

1. **AI-Powered Job Market Insights Dataset** (from Kaggle):
   https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights
   This dataset comprises job listings annotated with AI adoption indicators, industry sectors, automation risk levels, and job attributes such as skill requirements. It is provided in CSV format and accessed primarily via the Kaggle API. The dataset offers a comprehensive snapshot of how AI is permeating different sectors in terms of job roles and associated risks.

2. **Global AI Job Market & Salary Trends 2025 Dataset** (from Kaggle):
   https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025
   This dataset aggregates salary data, market growth trends, and detailed job descriptions across various geographical regions and industries with a focus on AI and emerging technologies. It is available in mixed JSON and CSV formats, obtained through direct download links. This dataset facilitates comparative analyses of job markets, salary distributions, and adoption rates worldwide.

Utilizing these datasets ensures a diverse data landscape encompassing varying file formats and acquisition methods (API vs. direct download), supporting robust data integration experiments and comprehensive analysis relevant to the AI job market.

## Timeline

| Week            | Task                                                                                           | Responsible        | Due Date            |
|-----------------|------------------------------------------------------------------------------------------------|--------------------|---------------------|
| Week 3 (Oct 7)  | Complete and submit the full Project Plan (ProjectPlan.md) in the GitHub repo and Canvas.     | xxx  | Oct 7, 2025         |
| Week 4-6        | Acquire job market datasets as described in the plan, thoroughly document methods, licenses, and access. | xxx  | Oct 14-28, 2025     |
| Week 6-8        | Design and implement the file/data storage strategy. Establish clear directory naming, record conventions. | xxx | Oct 28-Nov 11, 2025 |
| Week 7-9        | Data assessment: profile, quality check, initial cleaning (missing values, obvious outliers). Document issues found. | xxx  | Nov 4-18, 2025      |
| Week 10         | Submit Interim Status Report (StatusReport.md). Include: project status, updated tasks timeline, and GitHub repo evidence. | xxx  | Nov 11, 2025        |
| Week 11-12      | Conduct in-depth data integration and enrichment: join datasets, transform features, address semantic mismatches. | xxx  | Nov 18-25, 2025     |
| Week 12-13      | Develop, train, and validate the AI models for salary prediction and trend analysis.           | xxx  | Nov 25-Dec 2, 2025  |
| Week 13-14      | Automate workflow (Python scripts, Makefile/Snakemake), start compiling end-to-end provenance logs and metadata. | xxx  | Dec 2-9, 2025       |
| Week 14         | Document reproducibility instructions, update all data documentation, finalize visualizations/analysis outputs. | xxx  | Dec 9, 2025         |
| Week 15 (Dec 10)| Final project report and artifacts submitted on GitHub, tagged release, and Canvas submission. | xxx  | Dec 10, 2025        |

## Data Lifecycle Model

The project mirrors the data lifecycle concepts covered in the course modules:

- **Data Collection/Acquisition:** Datasets will be obtained via APIs and direct downloads from reliable sources with explicit documentation of access methods.
- **Data Storage and Organization:** A multi-tiered directory structure on GitHub with standardized file naming will be employed. Raw, intermediate, and processed data will be stored separately for clarity and reproducibility.
- **Data Processing (Extraction, Cleaning, Integration):** Scripts will be developed for systematic data parsing, cleansing, and merging while handling missing data and anomalies through well-documented methods.
- **Analysis and Modeling:** AI models will be trained and evaluated on cleaned integrated datasets for salary prediction and trend recognition.
- **Data Documentation and Sharing:** Extensive metadata, data dictionaries, and workflow descriptions will be provided for transparency, supporting reuse and reproducibility by others.

## Ethical Data Handling

Ethics remain at the core, guided by the following principles:

- All utilized datasets are publicly available under licenses permitting academic use.
- Any identifiable personal or sensitive information encountered will be anonymized or excluded to uphold privacy and confidentiality standards.
- All data handling abides by terms of service, licenses, and copyright laws outlined by data providers.
- The project will document consent mechanisms where applicable and ensure transparency regarding the origin, nature, and limitations of data.
- Considerations regarding potential biases in AI models or datasets will be highlighted, along with discussions on mitigating adverse societal impacts.

## Storage and Organization Strategy

Efficient storage and organization are vital for data accessibility and workflow automation:

- Raw, unaltered datasets will reside in `/data/raw/` guaranteeing original data preservation.
- Cleaned and integrated datasets will be stored in `/data/processed/`, clearly labeled to reflect preprocessing stages.
- Source code including data cleaning, integration, analysis scripts will be organized under `/src/`.
- Automated workflow scripts and build files will be maintained in `/workflow/`.
- Documentation, metadata files, and data dictionaries will be contained within `/docs/`, enhancing discoverability and comprehension.

Consistent naming conventions will follow timestamping and descriptive identifiers to facilitate tracking dataset versions and updates.

## Data Extraction and Integration

Data extraction will utilize both programmatic and manual approaches:

- The Kaggle API will automate the download of datasets where possible, complemented by manual downloads as needed.
- Data transformation scripts using Python Pandas will parse distinct formats (CSV, JSON), normalize schemas, and extract relevant fields.
- Key fields like job title, industry code, and location will serve as anchors for merging datasets to create a unified analytical table.
- SQL-like validation queries will verify consistency and integrity post-integration.

This approach ensures a cohesive dataset supporting robust AI analysis.

## Data Quality and Cleaning

Maintaining high data quality involves systematic steps:

- Initial exploratory analysis will identify missing values, duplicates, inconsistent entries, and outliers.
- Missing values will be handled based on the context, using imputation or removal justified with rationale.
- Outliers in salary or job counts will be detected statistically and reviewed semantically to avoid discarding legitimate variations.
- Standardization of job titles and classification codes will be performed to harmonize dataset vocabularies.
- Documented quality assessments will accompany each cleaning stage, recording decisions and outcomes.

## Workflow Automation and Provenance

Automation will enhance efficiency and reliability:

- Python scripting and potentially Snakemake workflows will coordinate data download, cleaning, integration, and modeling steps.
- Git will track every change including data transformations and analysis code development.
- Logs and metadata will capture processing timestamps, software versions, and data lineage, enabling full provenance tracking.
- The resulting automated pipeline will be easy to execute by others, ensuring reproducibility.

## Reproducibility and Transparency

Deliverables will prioritize reproducibility:

- Complete source code and scripts with detailed comments will be hosted on GitHub.
- Environment setup files (`requirements.txt` or equivalent) will enable others to replicate software configurations.
- Comprehensive documentation including data dictionaries, source descriptions, and workflow instructions will be provided.
- A clear README will guide users through repository structure, dataset sources, and execution steps.
- Version control will allow reviewers to examine each step from raw data acquisition to final analysis.

## Constraints

Expected constraints include:

- Dataset limitations such as missing geographic or sector coverage influencing analysis completeness.
- Changes or restrictions in API access potentially affecting data acquisition.
- Time constraints may limit the complexity of AI models or depth of exploratory analysis.
- Technical challenges in merging heterogeneous datasets with differing schemas.
- Balancing detail and clarity in documentation within project timelines.

## Gaps and Needs

- Seeking expert feedback on selecting and tuning AI models most suitable for salary prediction tasks.
- Assistance addressing schema conflicts or anomalies during dataset integration.
- Advice on ethical best practices if unexpected sensitive information arises.
- Input on designing effective visualizations to communicate complex job market trends.
- Continued improvement of workflow automation and documentation for seamless reproduction.

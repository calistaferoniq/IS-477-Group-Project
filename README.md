# AI-Powered Job Market Analysis and Salary Prediction

## Contributors: 
- Faith Ma
- Calista Gunawan

## Summary: 

The primary goal of this project is to explore and analyze the impact of artificial intelligence (AI) adoption on the global job market. As AI continuously advances at an unprecedented rate, its influence on job market conditions has become increasingly difficult to ignore. This project aims to provide a data-driven perspective on how AI-driven technological advancements are shaping job availability, salary trends, and broader employment patterns across industries. Throughout this project, we integrate and examine two distinct datasets that include job listings, salary information, and indicators of AI adoption across organizations. Through a structured process of data acquisition, cleaning, integration, and feature engineering, we construct an integrated dataset that supports robust exploratory analysis and model development. Following this, we build a predictive model targeting salary as the key outcome variable, leveraging the integrated features to better understand which job and company attributes have the greatest influence on salary levels.

The motivation for this project comes from the rapidly evolving nature of the AI landscape and its transformative effects on nearly every sector of the economy. With millions of new graduates and experienced professionals in the job market at any moment, a landscape shifting faster than traditional education and existing systems can adapt can be daunting. The emergence of generative AI, automation tools, and AI-enhanced workflows has accelerated changes in hiring practices, job responsibilities, and the very definition of certain roles and industries. Understanding these dynamics is becoming a practical necessity for job seekers striving to remain competitive, employers formulating long-term workforce development strategies, and policymakers who create the very labor guidelines that regulate the landscape. This project thus aims to build a transparent, reproducible workflow that captures these dynamics through data science methods and AI-powered analytical tools. All steps taken to perform this analysis are thoroughly documented and shared on GitHub to enable collaboration, reproducibility, and future exploration by other researchers and practitioners.

This project addresses the following **core research questions**:

- What are the primary job attributes and external factors that influence salary levels and job availability in an AI-driven economy?
- How accurately can AI models predict salary ranges based on job descriptions, industry sectors, and geographical location?
- How do salary trends and job availability compare across varying degrees of AI technology adoption?

These research questions serve as the guiding framework for the analysis, ensuring that the project remains focused on uncovering the factors that meaningfully influence today’s labor market. By centering the investigation on these questions, the analysis is positioned to generate insights that can benefit individuals navigating career choices, organizations refining recruitment strategies, and policymakers assessing economic shifts. The findings contribute both conceptual and practical clarity on how AI adoption interacts with economic, geographic, and occupational factors to shape employment outcomes.

Our preliminary findings show encouraging results in identifying key drivers of salary variation within the modern job market. By building a predictive model that incorporates features such as required education level, years of experience, remote-work compatibility, and the degree of AI adoption within the organization, we achieved a strong level of predictive accuracy on the test dataset. These results suggest that AI adoption, coupled with traditional job attributes, plays a notable role in shaping compensation structures. However, further analysis also reveals shortcomings tied primarily to the synthetic and limited nature of the dataset. These limitations affect model generalizability and are discussed in detail within this report.

Although the specific analytical outcomes cannot be directly applied to real-world labor markets due to the constraints of synthetic input data and limited observations, the overall methodology remains valuable. The workflow established through this project, including dataset integration, exploratory analysis, feature engineering, and model development, lays a strong foundation for future work. With richer datasets and more granular labor market information, this approach could be extended to develop more accurate predictive models and deeper analyses of AI’s evolving role in shaping workforce outcomes.

## Data profile: 

This project uses two publicly available datasets from Kaggle that focus on the relationship between artificial intelligence (AI) and global labor market trends. Both datasets are synthetic but created to mirror realistic job market patterns, making them suitable for exploratory analysis, dataset integration, and predictive modeling in an educational research context.

1. **AI-Powered Job Market Insights Dataset**
- Source: Kaggle (https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights) 
- Format: CSV

The AI-Powered Job Market Insights dataset provides detailed job listings annotated with indicators related to AI adoption within organizations. It includes fields describing job titles, required skills, industry sectors, automation risk levels, and attributes such as education level and years of experience. These variables enable the analysis of how AI technologies are influencing the structure and characteristics of modern job roles.

A key strength of this dataset is the inclusion of explicit AI adoption and automation risk indicators, which allow for segmenting industries by technological maturity. The dataset uses categorical and numeric fields to approximate how different sectors may be affected by AI integration, offering valuable inputs for both exploratory data analysis and predictive modeling. Although entirely synthetic, the dataset is modeled after real-world labor analytics, making it a useful tool for studying AI’s influence on job design and workforce requirements.

2. **Global AI Job Market & Salary Trends 2025 Dataset**
- Source: Kaggle (https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025) 
- Formats: CSV and JSON

The Global AI Job Market & Salary Trends 2025 dataset provides broader, internationally focused insights into job availability, salary ranges, growth trends, and AI-related job characteristics across different regions and industries. It includes data on salary distributions, industry growth projections, remote-work prevalence, and skill-related descriptors that enrich cross-regional labor market comparisons.

This dataset complements the first by offering a macro-level view of global AI job trends. Its mixed JSON and CSV formats allow for deeper parsing of nested job attributes, such as region-specific salary variations or technology requirements. Although synthetic, the dataset simulates realistic 2025 job market patterns, supporting the project’s goal of modeling salary outcomes and identifying factors associated with AI-driven labor trends.

Both datasets are openly accessible on Kaggle and include no personal, identifiable, or sensitive information. Their synthetic nature ensures compliance with major data privacy regulations such as GDPR and CCPA, as no real individuals, employers, or organizations are represented. They are explicitly intended for research and educational use, aligning with this project’s purpose.

However, the use of synthetic data introduces several limitations. Because the datasets do not reflect real-world records, the findings cannot be generalized to actual job markets. The datasets may also embed unknown biases based on the assumptions made during their creation. Additionally, documentation on the generative processes is limited, reducing transparency regarding how certain values or distributions were simulated.

For ethical reasons, interpretations drawn from these datasets must be communicated cautiously. While the datasets allow for exploring trends, testing workflows, and building predictive models, they should not be used to inform real hiring decisions, workforce policies, or actionable job-seeking strategies.

Despite their limitations, these datasets were selected because real-world alternatives combining AI adoption metrics, job listings, and salary data are scarce or restricted. Many credible labor datasets are proprietary, subscription-based, or governed by strict privacy protections. The Kaggle datasets therefore offer a practical and legally compliant foundation for demonstrating methodological workflows such as data integration, exploratory analysis, and salary prediction modeling.

Ultimately, while the results derived from these datasets cannot be applied directly to real-market conditions, they provide an effective framework for examining AI-related labor trends and for experimenting with predictive modeling approaches within a controlled, ethical environment.

## Data quality: 

The quality of the data used in this project can be evaluated across four commonly accepted dimensions of data quality: *accuracy, completeness, timeliness, and consistency*. Assessing each dimension provides insight into the reliability and usability of the datasets and helps clarify the limitations that influence how the results of this analysis should be interpreted. Because both datasets are synthetically generated, the overall expectations around quality differ from those applied to real-world, observational data. Nonetheless, evaluating quality across these dimensions remains essential for determining the validity and scope of any conclusions drawn from the data.

1. **Data accuracy**: 
Accuracy refers to how closely the data reflects the true values or “ground truth” it is meant to represent. In traditional datasets derived from surveys, scraped job postings, or employer-reported information, accuracy may be compromised by human error, reporting biases, transcription mistakes, or inconsistent data entry. In contrast, the datasets used in this project were synthetically created, which greatly reduces the likelihood of such errors. On initial inspection, syntactic accuracy, which is correctness in formatting, structure, and value types, was consistently high. All numeric fields appeared within plausible ranges, categorical variables adhered to expected labels, and no malformed or contradictory records were encountered. However, while syntactic accuracy was strong, semantic accuracy, defined as the degree to which values reflect real-world labor conditions, cannot be guaranteed. The values may appear plausible, but they do not correspond to actual job listings or salary distributions. This distinction is important because the model’s performance reflects internal coherence within the synthetic data rather than accuracy against real market conditions.
2. **Data completeness**: 
Completeness assesses the extent to which the datasets contain all necessary values for each record and whether important fields include missing entries. Both datasets demonstrated exceptionally high completeness. There were no null values, missing fields, or incomplete records requiring removal or imputation. This level of completeness simplified cleaning and preparation tasks and allowed modeling and analysis to proceed without concern for gaps or missing information. In real-world data, missingness often reflects important structural or environmental factors. For example, employers may withhold salary ranges or reporting may vary widely across regions. With synthetic data, however, completeness is artificially perfect and does not reflect the irregularities typical of real labor datasets. While this is beneficial for instructional purposes, it limits realism.
3. **Data timeliness**: 
Timeliness captures how current, relevant, and up-to-date the data is in relation to real-world conditions. In this dimension, the datasets score poorly. While the creators of the synthetic datasets suggest that the values approximate current and near-future job market conditions, there is no mechanism for routine updates or validation against evolving labor trends. AI adoption, job availability, and salary ranges shift quickly, sometimes within months, especially in technology-driven sectors. Because the datasets are static snapshots with hypothetical projections, their timeliness is inherently limited. This restricts the applicability of findings to real-time market analyses or longitudinal modeling.
4. **Data consistency**: 
Consistency refers to the degree to which the data adheres to internal rules, schema definitions, and expected relationships. Both datasets demonstrated high consistency, with uniform variable names, stable category definitions, and no conflicting or duplicated fields. There were no schema violations, contradictory attributes, or formatting discrepancies across files. This consistency is expected in synthetic datasets, as they are typically generated programmatically using stable templates. However, the absence of inconsistencies again highlights the difference between synthetic and empirical datasets, where inconsistencies often signal meaningful system-level issues.

Overall, the synthetic nature of the datasets results in uniformly high scores in accuracy, completeness, and consistency, while timeliness remains a clear limitation. Although these qualities make the data suitable for educational use, exploratory modeling, and demonstration of analytical workflows, they also mean that the findings cannot be generalized to real-world job markets. The data supports methodological learning but cannot substitute for genuine labor market analytics.

## Findings:

Upon integration of the two datasets, exploratory analysis and model development revealed several meaningful findings regarding both the structure of the data and the performance of the predictive model. The integrated dataset contains 20 observations and 9 features. While such a dataset may be sufficient for demonstrating workflow steps or conducting preliminary exploration, it is not adequate for building a reliable or generalizable machine learning model. The small sample size limits the ability to detect real patterns and increases the likelihood that the model will overfit or produce unstable performance metrics. This limitation is further compounded by skewed feature distributions. For example, “AI_Adoption_Level” is concentrated heavily in the “Low” category, and “Automation_Risk” is similarly skewed toward “High,” with other categories underrepresented. These imbalances reduce the dataset’s capacity to support meaningful comparisons across categories.

Descriptive statistics for Salary_USD provide additional insight into these concerns. The mean salary is 115358.72, with a minimum of 111321.18, a maximum of 120570.75, and a standard deviation of only 2520.99. This extremely narrow range raises questions about the variability of the integrated salary data. The limited spread is likely a result of the averaging method used during dataset merging as well as the synthetic nature of the input data. Ideally, salaries should vary based on job title, industry, location, and experience. In this dataset, however, the small variance indicates that these differences were either lost or not well represented during integration. As seen in the salary distribution visualization, the data displays almost no natural dispersion, which is a significant challenge for model development. Models trained under such conditions cannot learn meaningful relationships because the target variable barely changes across observations.

To evaluate how the available features relate to salary despite these limitations, a Random Forest Regressor was trained using “Years_Experience” and the categorical features "Education_Required", "AI_Adoption_Level", "Automation_Risk", "Remote_Friendly", and "Job_Growth_Projection". The resulting model produced a test mean absolute percentile error of 0.01311, which suggests an average prediction error of just 1.3 percent. If interpreted without consideration of the underlying data limitations, this result might imply strong model performance. However, given the narrow salary distribution, the model is not required to predict across a wide range of values. Even simple heuristics, such as predicting the overall mean salary, would likely yield similar error rates. As a result, the model’s apparent accuracy is misleading. The performance metric reflects the model’s ability to reproduce a nearly constant value rather than its ability to learn meaningful salary determinants.
The small test dataset, consisting of only three observations, further restricts the reliability of performance assessment. With so few samples, a single prediction has a large impact on the calculated error, and variability across repeated tests would likely be substantial. The prediction error distribution, shown in the prediction_error_distribution visualization, illustrates minimal deviation between predicted and true values, but this stability is more indicative of limited variability in the data than of genuine predictive power.

Overall, while the model produces numerically impressive metrics, the lack of variation in the target variable, the small number of observations, and the skewed feature distributions all limit the interpretability and practical value of the results. These findings highlight the need for richer, more diverse, and more representative datasets to support meaningful salary prediction and labor market analysis.

## Future work:

This project highlighted a central theme that is fundamental to any data-driven analysis: the quality of the input data ultimately determines the quality and trustworthiness of the output. Throughout the integration, exploration, and modeling stages, several challenges emerged that highlight the need for stronger data foundations in future iterations of this work. Reliable, well-structured, and representative data is necessary to produce interpretations that can withstand second-opinions, support decision-making, and generalize to real-world environments.

A primary lesson learned from this project is the critical importance of adequate sample size. With only 20 integrated observations, the dataset lacked the volume needed to reveal meaningful variation in key features such as AI adoption level, automation risk, and job growth projection. The small dataset also contributed to highly narrow salary distributions, which severely constrained model learning. This limitation made it clear that while small datasets can be useful for demonstrating analytical procedures, they cannot support robust predictive modeling. Future work must prioritize obtaining larger datasets that capture a wider range of job titles, experience levels, industries, and compensation outcomes.

In addition to sample size limitations, this project highlighted the risks associated with relying on averaged values during dataset integration. Because salary values were merged through averaging, the natural spread of compensation across roles became compressed. This produced an artificially uniform salary range that misrepresented underlying labor dynamics. As a result, the model learned patterns that failed to reflect true relationships. Moving forward, improved data integration methods should be employed, such as more advanced matching algorithms, better handling of duplicate job titles, and improved merging strategies that preserve variation rather than smooth it away.

A related lesson was the realization that model metrics can appear strong even when data diversity is low. The model in this project achieved very high accuracy on the test set, but this performance was misleading, due to the lack of variation in target values. This demonstrates why evaluation metrics must always be interpreted within the context of the data. Future iterations should implement cross-validation, more robust evaluation frameworks, and additional diagnostics such as feature importance stability checks to ensure that strong performance reflects genuine learning.

Given these limitations, future work must focus on integrating improved or real-world data. Potential sources include job listing APIs, labor statistics databases, or scraped job postings that reflect genuine market variability. Real-world data would allow for more meaningful modeling and greatly reduce the constraints caused by the synthetic datasets.

Finally, the project raises important ethical and societal considerations. Real-world salary prediction models must be evaluated for fairness, transparency, and bias. Certain features, such as education level or remote status, can be correlated with systemic inequalities. Future work should therefore incorporate bias audits, interpretability tools, and fairness constraints to ensure responsible modeling.

In summary, future extensions of this work should prioritize richer, more reliable datasets; improved integration methods; more rigorous evaluation; and ethical safeguards to ensure that the insights generated are both meaningful and responsible.

## Reproducing: 

This section outlines the complete sequence of steps required to reproduce the data integration, exploratory analysis, and model development performed in this project. The instructions below assume a basic working knowledge of Python and access to the same datasets used in the analysis.

**Environment Setup**: The analysis was conducted using Python 3.13 executed through a standard Python script environment. To reproduce the work, install the following libraries:
- numpy
- pandas
- matplotlib
- scikit-learn
- rapidfuzz
- requests
- python-dateutil
- pathlib

These libraries can be installed using: 
- pip install numpy pandas matplotlib scikit-learn rapidfuzz requests python-dateutil pathlib

**Raw Data**:
This project uses two public Kaggle datasets:

1. Global AI Job Market & Salary Trends 2025 (https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025) 
- Stored as: ai_job_dataset
- Original shape: (15000, 19)

2. AI-Powered Job Market Insights (https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights) 
- Stored as: ai_job_market_insights
- Original shape: (500, 10)

Both files should be downloaded manually or through the Kaggle API, then placed in:
- /data/raw/
- Load the data using:
- df1 = pd.read_csv("data/raw/ai_job_dataset.csv")
- df2 = pd.read_csv("data/raw/ai_job_market_insights.csv")

**Data Cleaning and Preprocessing**: 

1. Select the necessary columns from df1:
- job_title
- salary_usd
- required_skills
- education_required
- years_experience
2. Select the necessary columns from df2:
- Job_Title
- Salary_USD
- Remote_Friendly
- Required_Skills
- AI_Adoption_Level
- Automation_Risk
- Job_Growth_Projection
3. Standardize column names so both datasets contain compatible fields.
4. Case-normalize the job_title column.
5. Remove duplicates from both datasets.

**Dataset Integration Procedure**:

1. Perform exact matching on job titles using an inner join
- exact = pd.merge(df1_unique, df2_unique, on="Job_Title", how="inner")
2. Perform approximate matching for unmatched titles using RapidFuzz for a threshold exceeding 75
3. Combine exact and approximate matches into a unified dataset
4. Prefer df1 when values conflict
5. Create a “Match_Type” column to label each row as an “Exact” or “Approximate” match
6. Save the integrated dataset as “/data/processed/jobs_unified.csv”
- The unified dataset contains 20 rows and 9 features

**Exploratory Data Analysis**:
1. Salary distribution histogram

data = df["Salary_USD"]

plt.hist(data, bins=30, edgecolor='black')

plt.title('Distribution of Salary_USD')

plt.xlabel('Salary (USD)')

plt.ylabel('Frequency')

plt.grid(axis='y', alpha=0.75)

plt.show()

2. Prediction error distribution plot (generated after training model and evaluating test metrics)

errors = y_pred - y_test

plt.figure(figsize=(10,5))

plt.hist(errors, bins=5, edgecolor='black')

plt.title("Prediction Error Distribution")

plt.xlabel("Prediction Error (Predicted - Actual)")

plt.ylabel("Count")

plt.axvline(0, color='red', linestyle='--')

plt.show()

- Visualizations can be saved in /images/ folder

**Model Development Workflow**:

1. Split integrated dataset
- X_train, X_test, y_train, y_test = train_test_split(df, df["Salary_USD"], test_size=0.2, random_state=15)
2. Separate numeric and categorical features
- numeric_features = ["Years_Experience"]
- categorical_features = ["Education_Required", "AI_Adoption_Level", "Automation_Risk", "Remote_Friendly", "Job_Growth_Projection"]
3. Preprocess and apply:
- OneHotEncoder for categorical variables
- StandardScaler for numeric variables
4. Train a Random Forest Regressor
- RandomForestRegressor(n_estimators=5, random_state=10)
6. Train model, fit to X_train, y_train
7. Generate predictions on test set and evaluate mean absolute percentile error (MAPE)

*Scripts used for integration and modeling are stored in /scripts/

**Input and output data files can also be downloaded in this [Box folder](https://uofi.box.com/s/v7msqiyn9zhr9jcqw9zyi68ixvcegi5u)

## References: 
- Bisma Sajjad. (2025). Global AI Job Market and Salary Trends 2025 [Dataset]. Kaggle. https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025 
- UOM190346A. (2024). AI-Powered Job Market Insights [Dataset]. Kaggle. https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights
- Python Software Foundation. (2023). Python: Version 3.13 Documentation. https://docs.python.org/3.13/

# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# model imports
from sklearn.ensemble import RandomForestRegressor

# preprocessing imports
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_percentage_error

# load integrated data
df = pd.read_csv("data/processed/jobs_unified.csv")
df.head()

# train test split data
X_train, X_test, y_train, y_test = train_test_split(df, df["Salary_USD"], test_size=0.2, random_state=15)

# preprocessing

numeric_features = ["Years_Experience"]
categorical_features = ["Education_Required", "AI_Adoption_Level", "Automation_Risk", "Remote_Friendly", "Job_Growth_Projection"]

categorical_transformer = Pipeline(
    [
        ("Imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder())
    ]
)
numeric_transformer = Pipeline(
    [
        ("Imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

column_transformer = ColumnTransformer(
    [
        ("categorical", categorical_transformer, categorical_features),
        ("numeric", numeric_transformer, numeric_features)
    ]
)

pipeline = Pipeline(
    [
        ("preprocessor", column_transformer),
        ("regressor", RandomForestRegressor(n_estimators=5)) 
    ]
)

# train model
pipeline.fit(X_train,y_train)

# test metrics
y_pred = pipeline.predict(X_test)
test_mape = mean_absolute_percentage_error(y_test,y_pred)

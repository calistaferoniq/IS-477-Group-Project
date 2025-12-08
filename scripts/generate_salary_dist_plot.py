import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/data/processed/jobs_unified.csv")

data = df["Salary_USD"]

plt.hist(data, bins=30, edgecolor='black')
plt.title('Distribution of Salary_USD')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

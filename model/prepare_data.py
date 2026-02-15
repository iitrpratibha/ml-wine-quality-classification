"""
Data Preparation Script for Heart Disease Dataset
This script prepares the UCI Heart Disease dataset with proper column names
"""

import pandas as pd
import numpy as np

# Define column names for the dataset
column_names = [
    'age',           # Age in years
    'sex',           # Sex (1 = male; 0 = female)
    'cp',            # Chest pain type (1-4)
    'trestbps',      # Resting blood pressure (mm Hg)
    'chol',          # Serum cholesterol (mg/dl)
    'fbs',           # Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
    'restecg',       # Resting ECG results (0-2)
    'thalach',       # Maximum heart rate achieved
    'exang',         # Exercise induced angina (1 = yes; 0 = no)
    'oldpeak',       # ST depression induced by exercise
    'slope',         # Slope of peak exercise ST segment (1-3)
    'ca',            # Number of major vessels colored by fluoroscopy (0-3)
    'thal',          # Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
    'target'         # Heart disease diagnosis (0 = no disease, 1-4 = disease)
]

# Load the dataset
df = pd.read_csv('../data/heart.csv', names=column_names, na_values='?')

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
print("\nHandling missing values...")
# For numerical columns, fill with median
for col in ['ca', 'thal']:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].median(), inplace=True)

# Convert target to binary (0 = no disease, 1 = disease present)
df['target'] = (df['target'] > 0).astype(int)

print("\nTarget Distribution:")
print(df['target'].value_counts())

# Save cleaned dataset
df.to_csv('../data/heart_cleaned.csv', index=False)
print("\nCleaned dataset saved to data/heart_cleaned.csv")
print(f"Total Features: {len(df.columns) - 1}")
print(f"Total Instances: {len(df)}")

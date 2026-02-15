"""
Wine Quality Dataset Preparation
Combines red and white wine datasets and prepares for binary classification
"""

import pandas as pd
import numpy as np

# Load both datasets
red_wine = pd.read_csv('data/winequality-red.csv', sep=';')
white_wine = pd.read_csv('data/winequality-white.csv', sep=';')

# Add wine type column
red_wine['wine_type'] = 1  # Red wine
white_wine['wine_type'] = 0  # White wine

# Combine datasets
df = pd.concat([red_wine, white_wine], axis=0, ignore_index=True)

print("=" * 60)
print("WINE QUALITY DATASET PREPARATION")
print("=" * 60)
print(f"\nRed Wine samples: {len(red_wine)}")
print(f"White Wine samples: {len(white_wine)}")
print(f"Total samples: {len(df)}")
print(f"Total features: {len(df.columns) - 1}")  # Excluding target

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

print("\nQuality Distribution (Original):")
print(df['quality'].value_counts().sort_index())

# Convert to binary classification
# Quality >= 7 is considered 'good' (1), otherwise 'not good' (0)
df['quality_binary'] = (df['quality'] >= 7).astype(int)

print("\nBinary Quality Distribution:")
print(df['quality_binary'].value_counts())
print(f"Good wine (quality >= 7): {df['quality_binary'].sum()}")
print(f"Not good wine (quality < 7): {len(df) - df['quality_binary'].sum()}")

# Remove original quality column and use binary target
df_binary = df.drop('quality', axis=1)
df_binary = df_binary.rename(columns={'quality_binary': 'quality'})

print("\nFinal Dataset Shape:", df_binary.shape)
print("Features:", [col for col in df_binary.columns if col != 'quality'])

# Check for missing values
print("\nMissing Values:")
print(df_binary.isnull().sum().sum(), "missing values found")

# Save prepared dataset
df_binary.to_csv('data/wine_quality_prepared.csv', index=False)
print("\n✅ Prepared dataset saved to: data/wine_quality_prepared.csv")
print(f"✅ Total Features: {len(df_binary.columns) - 1}")
print(f"✅ Total Instances: {len(df_binary)}")
print(f"✅ Classification Type: Binary (Good/Not Good Wine)")
print("=" * 60)

"""
Wine Quality Classification - Model Training Script
Implements 6 classification models with comprehensive evaluation metrics
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    confusion_matrix,
    classification_report
)

# Import all classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

import joblib
import json

print("=" * 80)
print("WINE QUALITY CLASSIFICATION - MODEL TRAINING")
print("=" * 80)

# Load prepared dataset
print("\n[1/6] Loading dataset...")
df = pd.read_csv('data/wine_quality_prepared.csv')
print(f"✅ Dataset loaded: {df.shape[0]} samples, {df.shape[1]-1} features")

# Separate features and target
X = df.drop('quality', axis=1)
y = df['quality']

print(f"\nTarget distribution:")
print(y.value_counts())
print(f"Class 0 (Not Good): {(y==0).sum()} ({(y==0).sum()/len(y)*100:.2f}%)")
print(f"Class 1 (Good): {(y==1).sum()} ({(y==1).sum()/len(y)*100:.2f}%)")

# Split data
print("\n[2/6] Splitting dataset (80% train, 20% test)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✅ Train set: {X_train.shape[0]} samples")
print(f"✅ Test set: {X_test.shape[0]} samples")

# Scale features
print("\n[3/6] Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, 'model/scaler.pkl')
print("✅ Features scaled and scaler saved")

# Define all models
print("\n[4/6] Initializing models...")
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'kNN': KNeighborsClassifier(n_neighbors=5),
    'Naive Bayes': GaussianNB(),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'XGBoost': XGBClassifier(random_state=42, eval_metric='logloss')
}
print(f"✅ {len(models)} models initialized")

# Train and evaluate all models
print("\n[5/6] Training and evaluating models...")
print("-" * 80)

results = {}

for name, model in models.items():
    print(f"\n📊 Training {name}...")

    # Train model
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, 'predict_proba') else y_pred

    # Calculate all metrics
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    mcc = matthews_corrcoef(y_test, y_pred)

    # Store results
    results[name] = {
        'Accuracy': round(accuracy, 4),
        'AUC': round(auc, 4),
        'Precision': round(precision, 4),
        'Recall': round(recall, 4),
        'F1': round(f1, 4),
        'MCC': round(mcc, 4)
    }

    print(f"   ✅ Accuracy:  {accuracy:.4f}")
    print(f"   ✅ AUC:       {auc:.4f}")
    print(f"   ✅ Precision: {precision:.4f}")
    print(f"   ✅ Recall:    {recall:.4f}")
    print(f"   ✅ F1 Score:  {f1:.4f}")
    print(f"   ✅ MCC:       {mcc:.4f}")

    # Save model
    model_filename = f"model/{name.lower().replace(' ', '_')}.pkl"
    joblib.dump(model, model_filename)
    print(f"   💾 Model saved: {model_filename}")

print("\n" + "-" * 80)
print("\n[6/6] Saving results...")

# Save results to JSON
with open('model/results.json', 'w') as f:
    json.dump(results, f, indent=4)
print("✅ Results saved to model/results.json")

# Create results DataFrame
results_df = pd.DataFrame(results).T
results_df.to_csv('model/results.csv')
print("✅ Results saved to model/results.csv")

# Display comparison table
print("\n" + "=" * 80)
print("MODEL COMPARISON TABLE")
print("=" * 80)
print(results_df.to_string())
print("=" * 80)

# Find best model
best_model_by_metric = {}
for metric in ['Accuracy', 'AUC', 'Precision', 'Recall', 'F1', 'MCC']:
    best_model = results_df[metric].idxmax()
    best_score = results_df[metric].max()
    best_model_by_metric[metric] = f"{best_model} ({best_score:.4f})"

print("\n📈 BEST MODELS BY METRIC:")
print("-" * 80)
for metric, model_score in best_model_by_metric.items():
    print(f"{metric:12s}: {model_score}")
print("=" * 80)

print("\n✅ ALL MODELS TRAINED AND EVALUATED SUCCESSFULLY!")
print("=" * 80)

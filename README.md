# Wine Quality Classification - ML Assignment 2

## Problem Statement

The objective of this project is to build and compare multiple machine learning classification models to predict wine quality. The task involves classifying wines into two categories: **Good Quality** (quality rating ≥ 7) and **Not Good Quality** (quality rating < 7) based on various physicochemical properties of wine.

This is a binary classification problem that helps wine producers and quality control teams to:
- Predict wine quality based on measurable chemical properties
- Understand which factors contribute most to wine quality
- Automate quality assessment processes
- Compare the performance of different machine learning algorithms

## Dataset Description

### Dataset Information
- **Source**: UCI Machine Learning Repository - Wine Quality Dataset
- **Total Instances**: 6,497 samples
  - Red Wine: 1,599 samples
  - White Wine: 4,898 samples
- **Total Features**: 12 features
- **Target Variable**: Binary classification
  - Class 0 (Not Good): 5,220 samples (80.34%)
  - Class 1 (Good Quality): 1,277 samples (19.66%)
- **Missing Values**: None

### Features Description

The dataset contains the following 12 features:

1. **fixed acidity**: Fixed acids in wine (tartaric acid - g/dm³)
2. **volatile acidity**: Volatile acids in wine (acetic acid - g/dm³)
3. **citric acid**: Citric acid content (g/dm³)
4. **residual sugar**: Remaining sugar after fermentation (g/dm³)
5. **chlorides**: Salt content in wine (sodium chloride - g/dm³)
6. **free sulfur dioxide**: Free form of SO₂ (mg/dm³)
7. **total sulfur dioxide**: Total SO₂ content (mg/dm³)
8. **density**: Density of wine (g/cm³)
9. **pH**: Acidity level (0-14 scale)
10. **sulphates**: Wine additive (potassium sulphate - g/dm³)
11. **alcohol**: Alcohol content (% by volume)
12. **wine_type**: Type of wine (1 = Red, 0 = White)

### Data Split
- **Training Set**: 80% (5,197 samples)
- **Test Set**: 20% (1,300 samples)
- **Stratification**: Applied to maintain class distribution

## Models Used

### Model Comparison Table

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---------------|----------|-----|-----------|--------|-------|-------|
| Logistic Regression | 0.8223 | 0.8048 | 0.6147 | 0.2617 | 0.3671 | 0.3178 |
| Decision Tree | 0.8538 | 0.7749 | 0.6250 | 0.6445 | 0.6346 | 0.5434 |
| kNN | 0.8323 | 0.8264 | 0.5922 | 0.4766 | 0.5281 | 0.4314 |
| Naive Bayes | 0.7346 | 0.7486 | 0.3901 | 0.6172 | 0.4781 | 0.3268 |
| Random Forest (Ensemble) | 0.8869 | 0.9123 | 0.8079 | 0.5586 | 0.6605 | 0.6100 |
| XGBoost (Ensemble) | 0.8792 | 0.9021 | 0.7281 | 0.6172 | 0.6681 | 0.5979 |

### Model Performance Observations

| ML Model Name | Observation about model performance |
|---------------|-------------------------------------|
| Logistic Regression | Achieved good accuracy (82.23%) and decent AUC (80.48%), demonstrating solid linear separability in the data. However, it suffers from low recall (26.17%), indicating it misses many positive cases (good quality wines). The model is conservative in predicting the positive class, leading to high precision but low sensitivity. Best suited when false positives are more costly than false negatives. |
| Decision Tree | Showed strong balanced performance with accuracy of 85.38% and the highest recall among all models (64.45%). The model effectively captures non-linear relationships in the data without requiring feature scaling. However, it has a lower AUC (77.49%) compared to ensemble methods, suggesting potential overfitting to training data. The balanced F1 score (63.46%) indicates good trade-off between precision and recall. |
| kNN | Demonstrated good AUC score (82.64%) with moderate accuracy (83.23%), indicating strong probabilistic ranking ability. The model's performance is sensitive to the choice of k (set to 5) and distance metric. Recall is moderate (47.66%), suggesting it struggles with minority class detection. Feature scaling significantly impacts kNN performance, making preprocessing crucial. Computational cost increases with dataset size. |
| Naive Bayes | Showed the lowest accuracy (73.46%) among all models, likely due to violation of the independence assumption between features in wine chemistry. However, it achieved the second-highest recall (61.72%), making it useful when detecting positive cases is important. The model is fast to train and requires minimal hyperparameter tuning. Low precision (39.01%) indicates high false positive rate, limiting practical applicability for quality control. |
| Random Forest (Ensemble) | Emerged as the best overall performer with highest accuracy (88.69%), AUC (91.23%), precision (80.79%), and MCC (61.00%). The ensemble approach effectively reduces overfitting while capturing complex non-linear patterns. High precision indicates strong reliability when predicting good quality wines. Moderate recall (55.86%) suggests room for improvement in detecting all positive cases. Feature importance analysis reveals alcohol content and volatile acidity as top predictors. |
| XGBoost (Ensemble) | Achieved excellent performance with second-best accuracy (87.92%) and highest F1 score (66.81%), indicating the best balance between precision and recall. Strong AUC (90.21%) demonstrates superior ranking capability. The gradient boosting approach handles imbalanced data well. Better recall (61.72%) than Random Forest makes it more suitable when detecting good wines is prioritized. Requires careful hyperparameter tuning but offers state-of-the-art performance for this classification task. |

### Key Insights

1. **Ensemble Methods Dominate**: Random Forest and XGBoost significantly outperform individual classifiers, demonstrating the power of ensemble learning.

2. **Class Imbalance Impact**: The dataset has ~80% negative class, which affects model behavior. Models like Logistic Regression are conservative, while Naive Bayes and XGBoost handle imbalance better.

3. **Precision vs Recall Trade-off**:
   - High precision models (Random Forest, XGBoost): Better for quality assurance scenarios
   - High recall models (Decision Tree, Naive Bayes): Better for not missing good quality wines

4. **Feature Engineering Importance**: Feature scaling significantly impacts models like kNN and Logistic Regression, while tree-based methods are scale-invariant.

5. **Production Recommendation**: **Random Forest** or **XGBoost** are recommended for deployment due to their superior overall performance and robustness.

## Technical Implementation

### Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning algorithms and metrics
- **xgboost**: Gradient boosting implementation
- **matplotlib & seaborn**: Data visualization
- **streamlit**: Web application framework
- **joblib**: Model serialization

### Model Training Pipeline
1. Data loading and exploration
2. Train-test split (80-20) with stratification
3. Feature scaling using StandardScaler
4. Model training on scaled features
5. Comprehensive evaluation using 6 metrics
6. Model persistence using joblib

### Evaluation Metrics
- **Accuracy**: Overall correctness of predictions
- **AUC**: Area Under ROC Curve - discrimination capability
- **Precision**: Correctness of positive predictions
- **Recall**: Coverage of actual positive cases
- **F1 Score**: Harmonic mean of precision and recall
- **MCC**: Matthews Correlation Coefficient - balanced measure for imbalanced data

## Repository Structure

```
ml-assignment-2/
│
├── data/
│   ├── winequality-red.csv          # Raw red wine data
│   ├── winequality-white.csv        # Raw white wine data
│   └── wine_quality_prepared.csv    # Processed dataset
│
├── model/
│   ├── prepare_wine_data.py         # Data preparation script
│   ├── train_models.py              # Model training script
│   ├── logistic_regression.pkl      # Trained Logistic Regression model
│   ├── decision_tree.pkl            # Trained Decision Tree model
│   ├── knn.pkl                      # Trained kNN model
│   ├── naive_bayes.pkl              # Trained Naive Bayes model
│   ├── random_forest.pkl            # Trained Random Forest model
│   ├── xgboost.pkl                  # Trained XGBoost model
│   ├── scaler.pkl                   # Feature scaler
│   ├── results.json                 # Model results in JSON format
│   └── results.csv                  # Model results in CSV format
│
├── app.py                           # Streamlit web application
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

```

## How to Run

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ml-assignment-2
```

### 2. Create Virtual Environment and Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Train Models (Optional - models are already trained)
```bash
python model/train_models.py
```

### 4. Run Streamlit App
```bash
streamlit run app.py
```

## Live Application

🌐 **Streamlit App**: https://ml-wine-quality-classification-rddwem3ymumeq73kuysrpc.streamlit.app/

✅ **Status**: Live and accessible
📅 **Deployed**: February 15, 2026

## Author

**M.Tech (AIML/DSE) Student**
BITS Pilani - Work Integrated Learning Programmes

## License

This project is created for academic purposes as part of Machine Learning Assignment 2.

---

**Assignment Submission Date**: 15-Feb-2026
**Total Marks**: 15

---

*Generated with attention to academic integrity and best practices in machine learning.*

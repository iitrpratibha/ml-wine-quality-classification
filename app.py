"""
Wine Quality Classification - Streamlit Web Application
Interactive ML model demonstration and evaluation platform
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import matplotlib.pyplot as plt
import seaborn as sns
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
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Wine Quality Classifier",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #8B0000;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4A4A4A;
        text-align: center;
        padding-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #8B0000;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🍷 Wine Quality Classification</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Machine Learning Model Comparison & Prediction Platform</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/wine.png", width=100)
    st.title("Navigation")

    page = st.radio(
        "Select Page",
        ["🏠 Home", "📊 Model Comparison", "🔮 Make Predictions", "📈 About Dataset"]
    )

    st.markdown("---")
    st.markdown("### Assignment Info")
    st.info("""
    **Course**: Machine Learning
    **Assignment**: 2
    **Total Marks**: 15
    **Deadline**: 15-Feb-2026
    """)

# Load model results
@st.cache_data
def load_results():
    try:
        with open('model/results.json', 'r') as f:
            return json.load(f)
    except:
        st.error("Model results not found. Please train models first.")
        return None

# Load models
@st.cache_resource
def load_model(model_name):
    try:
        model_filename = f"model/{model_name.lower().replace(' ', '_')}.pkl"
        return joblib.load(model_filename)
    except:
        st.error(f"Model {model_name} not found.")
        return None

@st.cache_resource
def load_scaler():
    try:
        return joblib.load('model/scaler.pkl')
    except:
        st.error("Scaler not found.")
        return None

# HOME PAGE
if page == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        ## Welcome to Wine Quality Classifier!

        This interactive application demonstrates the implementation and comparison of
        **6 different machine learning classification models** for predicting wine quality.

        ### 🎯 Features

        - **📊 Model Comparison**: View and compare performance metrics of all 6 models
        - **🔮 Make Predictions**: Upload your wine data and get quality predictions
        - **📈 Detailed Analytics**: Confusion matrices and classification reports
        - **🎓 Educational**: Learn about different ML algorithms

        ### 🤖 Implemented Models

        1. **Logistic Regression** - Linear probabilistic classifier
        2. **Decision Tree** - Tree-based rule learner
        3. **K-Nearest Neighbors (kNN)** - Instance-based learner
        4. **Naive Bayes** - Probabilistic classifier
        5. **Random Forest** - Ensemble of decision trees
        6. **XGBoost** - Gradient boosting ensemble

        ### 📊 Dataset Information

        - **Source**: UCI Machine Learning Repository
        - **Instances**: 6,497 wine samples
        - **Features**: 12 physicochemical properties
        - **Target**: Binary classification (Good/Not Good quality)

        ---

        👈 **Use the sidebar to navigate** through different sections!
        """)

# MODEL COMPARISON PAGE
elif page == "📊 Model Comparison":
    st.header("📊 Model Performance Comparison")

    results = load_results()

    if results:
        # Convert to DataFrame
        df_results = pd.DataFrame(results).T
        df_results = df_results.round(4)

        # Display comparison table
        st.subheader("Performance Metrics Table")
        st.dataframe(
            df_results.style.highlight_max(axis=0, color='lightgreen')
                           .highlight_min(axis=0, color='lightcoral'),
            use_container_width=True
        )

        # Best models summary
        st.subheader("🏆 Best Performing Models by Metric")

        cols = st.columns(3)
        metrics = ['Accuracy', 'AUC', 'Precision', 'Recall', 'F1', 'MCC']

        for idx, metric in enumerate(metrics):
            with cols[idx % 3]:
                best_model = df_results[metric].idxmax()
                best_score = df_results[metric].max()

                st.markdown(f"""
                <div class="metric-card">
                    <h4>{metric}</h4>
                    <p style="font-size: 1.5rem; font-weight: bold; color: #8B0000;">
                        {best_score:.4f}
                    </p>
                    <p style="color: #666;">{best_model}</p>
                </div>
                """, unsafe_allow_html=True)

        # Visualization
        st.subheader("📈 Visual Comparison")

        tab1, tab2 = st.tabs(["Bar Chart", "Heatmap"])

        with tab1:
            # Select metric to visualize
            metric_to_plot = st.selectbox(
                "Select metric to visualize",
                metrics
            )

            fig, ax = plt.subplots(figsize=(10, 6))
            df_results[metric_to_plot].sort_values(ascending=True).plot(
                kind='barh',
                ax=ax,
                color='#8B0000'
            )
            ax.set_xlabel(metric_to_plot, fontsize=12)
            ax.set_ylabel('Model', fontsize=12)
            ax.set_title(f'{metric_to_plot} Comparison Across Models', fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)

            for i, v in enumerate(df_results[metric_to_plot].sort_values()):
                ax.text(v + 0.01, i, f'{v:.4f}', va='center')

            st.pyplot(fig)

        with tab2:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(
                df_results.T,
                annot=True,
                fmt='.4f',
                cmap='RdYlGn',
                center=0.7,
                ax=ax,
                cbar_kws={'label': 'Score'}
            )
            ax.set_title('All Metrics Heatmap', fontsize=14, fontweight='bold')
            st.pyplot(fig)

# PREDICTIONS PAGE
elif page == "🔮 Make Predictions":
    st.header("🔮 Wine Quality Prediction")

    st.markdown("""
    Upload a CSV file with wine features to predict quality using trained models.

    **Note**: Due to Streamlit Cloud free tier limitations, please upload only **test data** (smaller files).
    """)

    # Model selection
    model_options = [
        'Logistic Regression',
        'Decision Tree',
        'kNN',
        'Naive Bayes',
        'Random Forest',
        'XGBoost'
    ]

    selected_model = st.selectbox(
        "🤖 Select Model for Prediction",
        model_options,
        index=4  # Default to Random Forest (best performer)
    )

    # File uploader
    uploaded_file = st.file_uploader(
        "📁 Upload CSV file with wine features",
        type=['csv'],
        help="Upload a CSV file containing wine features (without target column)"
    )

    if uploaded_file is not None:
        try:
            # Load data
            df_test = pd.read_csv(uploaded_file)

            st.success(f"✅ File uploaded successfully! Shape: {df_test.shape}")

            # Show first few rows
            with st.expander("👀 Preview uploaded data"):
                st.dataframe(df_test.head(10))

            # Check if target column exists
            has_target = 'quality' in df_test.columns

            if has_target:
                X_test = df_test.drop('quality', axis=1)
                y_true = df_test['quality']
                st.info("Target column 'quality' detected. Will evaluate model performance.")
            else:
                X_test = df_test
                y_true = None
                st.warning("No target column detected. Will only show predictions.")

            # Load model and scaler
            model = load_model(selected_model)
            scaler = load_scaler()

            if model is not None and scaler is not None:
                # Make predictions
                if st.button("🚀 Predict Quality", type="primary"):
                    with st.spinner("Making predictions..."):
                        # Scale features
                        X_test_scaled = scaler.transform(X_test)

                        # Predict
                        y_pred = model.predict(X_test_scaled)
                        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, 'predict_proba') else y_pred

                        # Add predictions to dataframe
                        df_results = df_test.copy()
                        df_results['Predicted_Quality'] = ['Good' if p == 1 else 'Not Good' for p in y_pred]
                        df_results['Confidence'] = [max(p, 1-p) for p in y_pred_proba]

                        st.subheader("📋 Prediction Results")
                        st.dataframe(df_results)

                        # Download results
                        csv = df_results.to_csv(index=False)
                        st.download_button(
                            label="⬇️ Download Predictions",
                            data=csv,
                            file_name="wine_quality_predictions.csv",
                            mime="text/csv"
                        )

                        # If ground truth available, show metrics
                        if has_target:
                            st.subheader("📊 Model Evaluation Metrics")

                            # Calculate metrics
                            accuracy = accuracy_score(y_true, y_pred)
                            precision = precision_score(y_true, y_pred, zero_division=0)
                            recall = recall_score(y_true, y_pred, zero_division=0)
                            f1 = f1_score(y_true, y_pred, zero_division=0)

                            col1, col2, col3, col4 = st.columns(4)

                            with col1:
                                st.metric("Accuracy", f"{accuracy:.4f}")
                            with col2:
                                st.metric("Precision", f"{precision:.4f}")
                            with col3:
                                st.metric("Recall", f"{recall:.4f}")
                            with col4:
                                st.metric("F1 Score", f"{f1:.4f}")

                            # Confusion Matrix
                            st.subheader("🎯 Confusion Matrix")

                            cm = confusion_matrix(y_true, y_pred)

                            fig, ax = plt.subplots(figsize=(8, 6))
                            sns.heatmap(
                                cm,
                                annot=True,
                                fmt='d',
                                cmap='Blues',
                                xticklabels=['Not Good', 'Good'],
                                yticklabels=['Not Good', 'Good'],
                                ax=ax
                            )
                            ax.set_ylabel('True Label')
                            ax.set_xlabel('Predicted Label')
                            ax.set_title(f'Confusion Matrix - {selected_model}')
                            st.pyplot(fig)

                            # Classification Report
                            st.subheader("📄 Classification Report")

                            report = classification_report(
                                y_true,
                                y_pred,
                                target_names=['Not Good', 'Good'],
                                output_dict=True
                            )

                            df_report = pd.DataFrame(report).T
                            st.dataframe(df_report.style.highlight_max(axis=0))

                        # Prediction distribution
                        st.subheader("📊 Prediction Distribution")

                        pred_counts = pd.Series(y_pred).value_counts()

                        fig, ax = plt.subplots(figsize=(8, 5))
                        pred_counts.plot(kind='bar', color=['#CD5C5C', '#90EE90'], ax=ax)
                        ax.set_xticklabels(['Not Good', 'Good'], rotation=0)
                        ax.set_ylabel('Count')
                        ax.set_title('Distribution of Predictions')
                        ax.grid(axis='y', alpha=0.3)

                        for i, v in enumerate(pred_counts):
                            ax.text(i, v + 5, str(v), ha='center', fontweight='bold')

                        st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
            st.info("Please ensure your CSV file has the correct format with all required features.")

# ABOUT DATASET PAGE
elif page == "📈 About Dataset":
    st.header("📈 Dataset Information")

    st.markdown("""
    ## Wine Quality Dataset

    ### Source
    This dataset is from the **UCI Machine Learning Repository** and contains information about
    red and white variants of the Portuguese "Vinho Verde" wine.

    ### Dataset Characteristics

    - **Total Samples**: 6,497
      - Red Wine: 1,599 samples
      - White Wine: 4,898 samples
    - **Features**: 12 physicochemical properties
    - **Target**: Binary classification (Good Quality vs Not Good Quality)
    - **Class Distribution**:
      - Not Good (quality < 7): 5,220 samples (80.34%)
      - Good (quality ≥ 7): 1,277 samples (19.66%)

    ### Features Description

    | Feature | Description | Unit |
    |---------|-------------|------|
    | fixed acidity | Tartaric acid content | g/dm³ |
    | volatile acidity | Acetic acid content | g/dm³ |
    | citric acid | Citric acid content | g/dm³ |
    | residual sugar | Sugar remaining after fermentation | g/dm³ |
    | chlorides | Salt content | g/dm³ |
    | free sulfur dioxide | Free form of SO₂ | mg/dm³ |
    | total sulfur dioxide | Total SO₂ (free + bound) | mg/dm³ |
    | density | Density of wine | g/cm³ |
    | pH | Acidity level | scale 0-14 |
    | sulphates | Potassium sulphate | g/dm³ |
    | alcohol | Alcohol content | % vol |
    | wine_type | Type of wine | 0=White, 1=Red |

    ### Data Preprocessing

    1. **Combination**: Red and white wine datasets were combined
    2. **Feature Engineering**: Added wine_type as a binary feature
    3. **Target Transformation**: Original quality (0-10) → Binary (Good/Not Good)
    4. **Missing Values**: None found
    5. **Scaling**: StandardScaler applied for model training
    6. **Split**: 80% training, 20% testing with stratification

    ### Citation

    P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
    *Modeling wine preferences by data mining from physicochemical properties.*
    Decision Support Systems, Elsevier, 47(4):547-553, 2009.
    """)

    # Feature statistics (if dataset available)
    try:
        df = pd.read_csv('data/wine_quality_prepared.csv')

        st.subheader("📊 Feature Statistics")
        st.dataframe(df.describe())

        # Feature correlation
        st.subheader("🔗 Feature Correlations")

        fig, ax = plt.subplots(figsize=(12, 10))
        corr = df.corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
        ax.set_title('Feature Correlation Matrix')
        st.pyplot(fig)

    except:
        st.info("Dataset file not found. Feature statistics unavailable.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p><strong>Machine Learning Assignment 2</strong></p>
    <p>M.Tech (AIML/DSE) - BITS Pilani WILP</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)

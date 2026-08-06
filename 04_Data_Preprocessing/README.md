# ⚙️ Data Preprocessing & Feature Engineering

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

This directory covers essential **Data Preprocessing** concepts and workflows using Python and Scikit-Learn. Preprocessing is a critical phase in a machine learning pipeline. High-quality features and clean datasets determine model performance more than the model architectures themselves.

---

## 📖 Notebooks & Contents

### 📓 [01_Outlier_Detection_and_Handling.ipynb](./01_Outlier_Detection_and_Handling.ipynb)
Covers diagnostic and mitigation steps for outliers in continuous fields:
*   **Boxplots**: Visualizing distributions and marking outlier points.
*   **IQR Method**: Defining lower and upper bounds using mathematical quartiles.
*   **Z-Score Method**: Finding outliers that lie more than 3 standard deviations from the mean.

### 📓 [02_Exploratory_Data_Analysis.ipynb](./02_Exploratory_Data_Analysis.ipynb)
Covers baseline data investigation and cleanup:
*   **Missing Value Analysis**: Quantifying missing elements per feature.
*   **Imputation Decisions**: Understanding when to use `mean` (no outliers) vs. `median` (outliers present) or drop rows.

### 📓 [03_Categorical_Encoding.ipynb](./03_Categorical_Encoding.ipynb)
Covers numerical transformations of text fields and data scaling:
*   **Encoding Types**: One-Hot Encoder, Label/Ordinal Encoder, and Target Encoder.
*   **Feature Scaling**: MinMaxScaler and StandardScaler.
*   **Data Leakage Prevention**: Fitting transformations strictly on training data and applying them to testing data.

### 📓 [04_Column_Transformers_and_Pipelines.ipynb](./04_Column_Transformers_and_Pipelines.ipynb)
Covers building end-to-end, reproducible preprocessing pipelines:
*   **ColumnTransformer**: Bundling different preprocessing steps for numerical vs. categorical subsets.
*   **Pipeline**: Chaining imputation, scaling, encoding, and estimators (e.g. `DecisionTreeRegressor`) into a single model call.

### 📓 [05_Resampling_Technique.ipynb](./05_Resampling_Technique.ipynb)
Covers methods to address class imbalance issues in training datasets:
*   **Imbalanced Classification**: Managing classification datasets with skewed distribution classes.
*   **Oversampling & Undersampling**: Techniques to balance class weights and distribution before training estimators.

---

## ⚙️ Core Concepts Covered
- Detecting and treating outliers mathematically.
- Categorical mappings (nominal vs. ordinal).
- Avoiding data leakage during training/test splits.
- Writing production-ready, modular Scikit-Learn preprocessing Pipelines.
- Managing class imbalance.

---

## Created & Maintained By

**Aditya Sarapure**

*This repository represents my personal Machine Learning learning journey. Every implementation, notebook, experiment, and note has been developed, organized, and maintained by me for educational and portfolio purposes.*

# 04. Data Preprocessing

This directory covers essential **Data Preprocessing** concepts and workflows using Python and Scikit-Learn.

Preprocessing is the most critical phase in a machine learning pipeline. High-quality features and clean datasets determine model performance more than the models themselves.

---

## 📖 Contents

### [01_Outlier_Detection_and_Handling.ipynb](file:///d:/ML/04_Data_Preprocessing/01_Outlier_Detection_and_Handling.ipynb)
Covers diagnostic and mitigation steps for outliers:
*   **Boxplots:** Visualizing distributions and marking outlier points.
*   **IQR Method:** Defining lower and upper bounds using mathematical quartiles.
*   **Z-Score Method:** Finding outliers that lie more than 3 standard deviations from the mean.

### [02_Exploratory_Data_Analysis.ipynb](file:///d:/ML/04_Data_Preprocessing/02_Exploratory_Data_Analysis.ipynb)
Covers baseline data investigation:
*   **Missing Value Analysis:** Quantifying missing elements per feature.
*   **Imputation Decisions:** Understanding when to use `mean` (no outliers) vs `median` (outliers present) or drop rows.

### [03_Categorical_Encoding.ipynb](file:///d:/ML/04_Data_Preprocessing/03_Categorical_Encoding.ipynb)
Covers numerical transformations of text fields and data scaling:
*   **Encoding Types:** One-Hot Encoder, Label/Ordinal Encoder, and Target Encoder.
*   **Feature Scaling:** MinMaxScaler and StandardScaler.
*   **Preprocessing Workflow:** Fitting transformations on train data and applying them to test data to prevent leakage.

### [04_Column_Transformers_and_Pipelines.ipynb](file:///d:/ML/04_Data_Preprocessing/04_Column_Transformers_and_Pipelines.ipynb)
Covers building end-to-end, reproducible preprocessing pipelines:
*   **ColumnTransformer:** Bundling different preprocessing steps for numerical vs categorical subsets.
*   **Pipeline:** Chaining imputation, scaling, encoding, and estimators (e.g. `DecisionTreeRegressor`) into a single model call.

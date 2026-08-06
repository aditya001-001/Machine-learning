# 💳 Loan Approval Prediction

This project implements an end-to-end binary classification pipeline to predict whether a loan application will be approved or rejected based on credit and financial profile attributes.

---

## 📖 Project Overview

Loan approvals represent a classic risk management problem. By applying supervised machine learning, we can automate the credit risk assessment and evaluate metrics to control false approvals.

### Key Pipeline Stages:
1. **Exploratory Data Analysis**: Analyzing and visualizing distribution traits of applicant income, loan amounts, and credit score histories.
2. **Outlier Mitigation**: Utilizing boxplots to detect and filter out skewed outlier profiles.
3. **Data Transformations**:
   - Numerical Scaling using Scikit-Learn's `MinMaxScaler`.
   - Categorical Encoding using Scikit-Learn's `OneHotEncoder`.
4. **Model Training**: Fitting and testing a `LogisticRegression` estimator on split dataset contexts.
5. **Evaluation**: Generating Confusion Matrices and Classification Reports (Precision, Recall, F1-Score).

---

## 📂 Project Structure

- `Loan_Approval_Prediction.ipynb`: Step-by-step Jupyter Notebook showing data ingestion, cleansing, model training, and performance checks.
- Dataset source: `../../datasets/Loan_approval_dataset.csv`

---

## Created & Maintained By

**Aditya Sarapure**

*This repository represents my personal Machine Learning learning journey. Every implementation, notebook, experiment, and note has been developed, organized, and maintained by me for educational and portfolio purposes.*

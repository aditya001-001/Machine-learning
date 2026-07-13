# 05. Machine Learning Algorithms

This directory covers **Machine Learning Algorithms** split into two core disciplines: **Regression** and **Classification**.

Here we study the math, concepts, implementation details, and trade-offs of standard estimators.

---

## 📈 Regression

Regression algorithms predict continuous, numerical quantities (e.g. prices, salaries, scores).

### [01_Linear_Regression.ipynb](file:///d:/ML/05_Machine_Learning/Regression/01_Linear_Regression.ipynb)
Covers basic Linear Regression:
*   **Train-Test Splits:** Splitting feature-target pairs into train and test sets.
*   **Formula:** The mathematics behind finding the slope ($m$) and intercept ($c$) for $y = mx + c$.
*   **Application:** Training a model to map Years of Experience to Salary.

### [02_Polynomial_Regression.ipynb](file:///d:/ML/05_Machine_Learning/Regression/02_Polynomial_Regression.ipynb)
Covers handling non-linear relations by projecting inputs into polynomial dimensions using `PolynomialFeatures` before applying linear estimators.

### [03_Regression_Practice.ipynb](file:///d:/ML/05_Machine_Learning/Regression/03_Regression_Practice.ipynb)
A collection of practice tasks covering housing correlations and study hours calculations.

### [04_Model_Performance_and_Overfitting.ipynb](file:///d:/ML/05_Machine_Learning/Regression/04_Model_Performance_and_Overfitting.ipynb)
Covers diagnostic evaluation metrics for regression models (MAE, RMSE) and discusses strategies to resolve underfitting (high bias) vs. overfitting (high variance).

---

## 🎯 Classification

Classification algorithms predict discrete, categorical group tags (e.g. approval status, spam/ham).

### [01_Logistic_Regression.ipynb](file:///d:/ML/05_Machine_Learning/Classification/01_Logistic_Regression.ipynb)
Theoretical study of Logistic Regression covering the Sigmoid activation function, cost/loss optimization, gradient descent, and regularization methods (L1/L2).

### [02_Decision_Trees.ipynb](file:///d:/ML/05_Machine_Learning/Classification/02_Decision_Trees.ipynb)
Covers Decision Tree nodes splitting criteria (Gini Impurity vs. Entropy) and basic classification vs. regression implementations.

### [03_Ensemble_Random_Forest.ipynb](file:///d:/ML/05_Machine_Learning/Classification/03_Ensemble_Random_Forest.ipynb)
Covers Random Forest Classifiers and Bagging ensembles to combine predictions from weak tree-based models.

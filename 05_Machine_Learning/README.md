# 🤖 Machine Learning Algorithms & Implementations

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-blue.svg?style=flat)](https://xgboost.readthedocs.io/)

This directory covers **Machine Learning Algorithms** split into core disciplines: **Regression**, **Classification**, **Clustering**, and **Model Evaluation & Tuning**. Here we study the math, concepts, implementation details, and performance trade-offs of standard estimators.

---

## 📂 Subdirectories & Topics

### 📈 1. [Regression](./Regression/)
Regression algorithms predict continuous numerical quantities (e.g. salaries, prices).
*   [01_Linear_Regression.ipynb](./Regression/01_Linear_Regression.ipynb): Simple linear mapping ($y = mx + c$) predicting salary based on experience.
*   [02_Polynomial_Regression.ipynb](./Regression/02_Polynomial_Regression.ipynb): Fitting curves and non-linear patterns by projecting data into polynomial dimensions.
*   [03_Regression_Practice.ipynb](./Regression/03_Regression_Practice.ipynb): Guided regression exercises on multiple datasets.
*   [04_Model_Performance_and_Overfitting.ipynb](./Regression/04_Model_Performance_and_Overfitting.ipynb): Diagnostic evaluation metrics (MAE, MSE, RMSE) and methods to mitigate bias/variance trade-offs.
*   [05_RandomForestRegressor.ipynb](./Regression/05_RandomForestRegressor.ipynb): Non-linear regression using bagging ensembles of decision trees.
*   [06_XGBoostRegressor.ipynb](./Regression/06_XGBoostRegressor.ipynb): Gradient-boosted decision trees for regression.

### 🎯 2. [Classification](./Classification/)
Classification algorithms predict discrete, categorical labels (e.g. approval, risk categories).
*   [01_Logistic_Regression.ipynb](./Classification/01_Logistic_Regression.ipynb): Mathematics of Sigmoid activation, cross-entropy cost function, and L1/L2 regularization.
*   [02_Decision_Trees.ipynb](./Classification/02_Decision_Trees.ipynb): Tree splitting criteria (Gini Impurity vs. Entropy) and classification logic.
*   [03_Ensemble_Random_Forest.ipynb](./Classification/03_Ensemble_Random_Forest.ipynb): Bagging and voting classifiers using tree-based ensembles.
*   [04_RandomForestClassifier.ipynb](./Classification/04_RandomForestClassifier.ipynb): Random Forest classifier applied to practical tabular data.
*   [05_XGBoostClassifier.ipynb](./Classification/05_XGBoostClassifier.ipynb): State-of-the-art gradient boosted trees for tabular classification.
*   [06_GaussianNaiveBayes.ipynb](./Classification/06_GaussianNaiveBayes.ipynb): Probabilistic classification using Bayes' theorem.

### 📊 3. [Model Evaluation & Hyperparameter Tuning](./Model_Evaluation/)
Validating estimator reliability and finding optimal parameter configurations.
*   [01_Classification_Metrics.ipynb](./Model_Evaluation/01_Classification_Metrics.ipynb): Deep dive into Confusion Matrices, Precision, Recall, Accuracy, and F1-Score.
*   [02_GridSearchCV_and_Hyperparameter_Tuning.ipynb](./Model_Evaluation/02_GridSearchCV_and_Hyperparameter_Tuning.ipynb): Automated search strategies (Grid Search Cross Validation) to discover the best estimator hyperparameters.

### 🧩 4. [Clustering](./Clustering/)
Unsupervised learning algorithms used to group data points based on feature similarity.
*   [01_KMeans_Clustering.ipynb](./Clustering/01_KMeans_Clustering.ipynb): K-Means clustering, Within-Cluster Sum of Squares (Inertia), Elbow Method for finding optimal $K$, and student demographic grouping.

---

## ⚙️ Core Concepts Explored
- Supervised vs. Unsupervised learning workflows.
- The mathematics of gradient optimization.
- Decision boundary behavior.
- Ensemble methods (Bagging vs. Boosting).
- Comprehensive evaluation metrics.

---

## Created & Maintained By

**Aditya Sarapure**

*This repository represents my personal Machine Learning learning journey. Every implementation, notebook, experiment, and note has been developed, organized, and maintained by me for educational and portfolio purposes.*

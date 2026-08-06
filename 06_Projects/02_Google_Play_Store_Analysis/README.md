# 📱 Google Play Store Analysis

This project covers end-to-end data manipulation, cleaning, and exploratory data analysis of Google Play Store applications.

---

## 📖 Project Overview

App store metrics are heavily cluttered with mixed textual and numerical formats (e.g. download sizes as "10M" or "20k", price strings as "$4.99"). Cleaning and indexing these fields is critical for running statistical visualizations or predictive modeling.

### Key Pipeline Stages:
1. **Data Cleaning**: String parsing to strip currency symbols ($) and convert scales (converting "M" and "k" characters to raw numerical floats).
2. **Datetime Formatting**: Parsing mixed date formats and standardizing timestamp sequences.
3. **Feature Construction**: Generating time-based parameters (Year, Month) to analyze seasonal app publishing patterns.
4. **Data Visualization**: Constructing distribution and count plots utilizing Seaborn to observe download frequencies, categories, and user rating trends.

---

## 📂 Project Structure

- `Google_Play_Store_Analysis.ipynb`: Step-by-step Jupyter Notebook containing the data loading, cleaning logic, and visualization plots.
- Dataset source: `../../datasets/googleplaystore.csv`

---

## Created & Maintained By

**Aditya Sarapure**

*This repository represents my personal Machine Learning learning journey. Every implementation, notebook, experiment, and note has been developed, organized, and maintained by me for educational and portfolio purposes.*

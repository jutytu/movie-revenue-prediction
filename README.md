 🎬 Movie Revenue Analysis & Prediction

## 📌 Introduction
This project explores **movie revenue patterns** using data from [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).  
It includes three main stages:  
1. **Exploratory Data Analysis (EDA)** – understanding revenue distributions, budgets, genres, directors, and historical patterns.  
2. **Data Cleaning & Feature Engineering** – handling missing values, correcting misreported entries, and constructing meaningful predictors.  
3. **Predictive Modeling** – applying regression models (Linear Regression, Random Forest, Gradient Boosting) to predict movie revenues.  

The repository is organized to be reproducible and to showcase skills in **Python, pandas, numpy, matplotlib, seaborn, and scikit-learn**.

---

## 📂 Repository Structure

```bash
movie-revenue-prediction/
├── data/
│   ├── raw/                  
│   └── processed/            
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_visualizations.ipynb
│   ├── 04_modeling.ipynb
│   ├── src/
│       └── utils.py
├── plots/
├── README.md
└── requirements.txt
```

---

## 📊 Data Source
The data comes from **[The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)** on Kaggle.  
Due to GitHub’s file size limitations, large CSV files (e.g., `credits.csv`, merged datasets) were split into smaller chunks using helper scripts in `src/utils.py`.

---

## 🔎 Key Steps & Findings
- **Data Exploration**  
  - Cleaned and corrected inconsistencies (e.g., missing budgets, mis-scaled revenues).  
  - Observed strong outliers in early cinema (e.g., *Gone with the Wind*, *Bambi*) impacting trends.  
  - Directors and budgets showed the largest correlation with revenue.  

- **Modeling**  
  - **Linear Regression** provided a baseline (R² ~0.47).  
  - **Random Forest Regressor** achieved the best performance (RMSE ~0.96), capturing non-linear relationships effectively.  
  - **Gradient Boosting** performed slightly worse than Random Forest (RMSE ~1.07), likely due to feature limitations and overfitting tendencies.  

- **Feature Importance (Random Forest)**  
  1. Director average revenue  
  2. Budget  
  3. Release year  
  4. Genres (minor impact, though Action, War, and Drama stood out)  

---

## 📓 Notebooks
- [01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)  
- [02_analysis.ipynb](notebooks/02_analysis.ipynb)  
- [03_modeling.ipynb](notebooks/03_modeling.ipynb)  

Each notebook is self-contained and documented with markdown explanations.

---

# Movie revenue - analysis and prediction

## Introduction
This project explores movie revenue patterns using a movie dataset from Kaggle. The goal was to derive different kind of information from the dataset, as well as use it for ML models predicting movie revenue.


## Repository structure

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

## Data source
The data comes from [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) on Kaggle.  
Due to GitHub’s file size limitations, large CSV files (e.g., `credits.csv`, merged datasets) were split into smaller chunks using helper scripts in `src/utils.py`.


## Key steps
- **Data exploration and cleaning**  
  - Cleaned and corrected inconsistencies (e.g. missing budgets, mis-scaled revenues).  
  - Observed strong outliers in early cinema (e.g., *Gone with the Wind*, *Bambi*) impacting trends.    

- **Modeling**  
  - Linear Regression provided a baseline (R² ~0.47).  
  - Random Forest Regressor achieved the best performance (RMSE ~0.96).  
  - Gradient Boosting performed slightly worse than Random Forest (RMSE ~1.07), likely due to feature limitations and overfitting tendencies.  


## Notebooks
- [01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)  
- [02_data_cleaning.ipynb](notebooks/02_data_cleaning.ipynb)  
- [03_eda_visualizations.ipynb](notebooks/03_eda_visualizations.ipynb)
- [04_modeling.ipynb](notebooks/04_modeling.ipynb)

Each notebook is self-contained and documented with markdown explanations.

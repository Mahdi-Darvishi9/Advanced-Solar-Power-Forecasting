# ⚡ Advanced Solar Power Forecasting

**Accurately forecasting solar energy generation—without using irradiance data.**

Note: 🔒 Note:
The core implementation of this forecasting model — including the optimized machine learning architecture and preprocessing pipeline — is not publicly available due to intellectual property and security considerations. This repository contains a summarized version highlighting the workflow, methodology, and reproducibility structure while keeping the proprietary code private.

## 🌞 Value Proposition

Solar energy is vital for a sustainable future. But its unpredictable nature—due to time, location, and weather—makes forecasting a challenge. Traditional models rely on costly irradiance data, requiring satellite feeds or on-site sensors.

This project introduces one of only two models in the world that completely eliminates that dependence. Instead, it leverages easily accessible geographic, meteorological, and temporal data to deliver highly accurate solar power predictions—at a fraction of the cost. This shift enables fast, scalable, and affordable deployment of solar forecasting tools worldwide.

---

## 🧠 Methodology Summary

This hybrid ensemble model is built using **XGBoost**, **LightGBM**, and a **Linear Regression meta-model**. It includes advanced feature engineering, including:

- **Temporal Feature Engineering:** Extracted time-based features (month, day, hour) and converted them into **cyclic features** using sine and cosine to preserve daily and seasonal continuity.
- **Environmental Feature Smoothing:** Used rolling averages and exponentially weighted moving averages for temperature and wind speed to reduce noise.
- **Solar Geometry Calculations:** Computed **solar elevation** and **azimuth angles** from latitude and solar position equations to capture sunlight angles more precisely.
- **Feature Selection with RFE:** Recursive Feature Elimination optimized the feature set (103–109 features) for each base model, significantly boosting performance.
- **Model Stacking:** XGBoost and LightGBM predictions were combined using a **Linear Regression meta-model**, allowing for interpretability, speed, and enhanced accuracy.

---

## 📊 Results

- **Mean Absolute Error (MAE):** 0.033  
- **Root Mean Squared Error (RMSE):** 0.116  
- **R² Score:** 0.693  
- **Cross-Validation (10-fold R²):** Avg. 0.692 (Min: 0.665, Max: 0.717)

The model demonstrates strong consistency and generalization across multiple data splits, confirming robustness.

---

## 📁 Project Structure

```bash
.
├── data/                   # Instructions or sample for data
├── notebooks/             # Jupyter Notebooks (feature engineering, training, evaluation)
├── models/                # Trained model files (.pkl or .joblib)
├── docs/                  # WSC paper, poster, diagrams
├── requirements.txt       # Python dependencies
├── README.md              # You are here
├── LICENSE                # Open-source license
└── CITATION.cff           # How to cite this project
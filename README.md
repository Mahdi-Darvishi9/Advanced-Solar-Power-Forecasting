<<<<<<< HEAD
# Advanced Solar Power Forecasting
Hybrid/ensemble model that forecasts PV power **without irradiance sensors**, using geographic, meteorological, and temporal features.

> Maintains (and in some cases improves) accuracy while eliminating costly irradiance inputs. Designed for robustness in harsh climates and for easy portfolio-scale deployment.

## 📌 Highlights
- **Model**: XGBoost + LightGBM stacked via Linear Regression meta-model
- **Inputs**: Weather (NWP/API), geography, calendar/time features — **no on-site irradiance**
- **Targets**: PV power (normalized), horizons: day-ahead and intra-day
- **Artifacts**: reproducible notebooks, training/eval scripts, model cards, and figures
- **Results (example)**: MAE ≈ 0.033, R² ≈ 0.693 (dataset-dependent)

## 🗂️ Project Structure
```
advanced-solar-power-forecasting/
├── data/
│   ├── raw/               # put raw CSV/Parquet (not tracked)
│   └── processed/         # cleaned/feature-engineered sets (not tracked)
├── docs/                  # method notes, diagrams
├── models/                # trained models, metrics (not tracked)
├── notebooks/             # EDA, modeling, evaluation
├── reports/
│   └── figures/           # generated plots
├── src/
│   └── aspf/
│       ├── data.py        # load/clean, feature engineering
│       ├── model.py       # train/predict: xgb + lgbm + meta-model
│       ├── evaluate.py    # metrics, cross-validation
│       └── utils.py       # helpers
├── .github/workflows/     # CI: linting/tests
├── requirements.txt
├── environment.yml
├── README.md
├── LICENSE
└── CITATION.cff
```

## 🚀 Quickstart
```bash
# 1) Create environment
conda env create -f environment.yml
conda activate aspf

# 2) (or with pip)
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3) Put data
#   - Place raw weather + PV data under data/raw/
#   - (Optional) Provide a small sample for demo in data/raw/sample_*.csv

# 4) Run notebooks or scripts
jupyter lab
# open notebooks/01_eda.ipynb then 02_train.ipynb and 03_evaluate.ipynb
```

## 📦 Data Inputs
- **Meteorological**: temperature, humidity, wind, precipitation, cloud cover (from NWP/API)
- **Geographic**: lat/long, elevation, regional climate indicators
- **Temporal**: day-of-year, hour, weekday/weekend, holiday flags
- **Target**: plant power/energy (prefer normalized power to support transferability)

> ⚠️ Do not commit proprietary datasets. Add small synthetic samples for demo if needed.

## 🔧 Reproducibility
- Random seeds set consistently
- K-fold cross-validation with grouped/temporal splits
- Model registry under `models/` (excluded from VCS)

## 📈 Evaluation
- Metrics: MAE, RMSE, MAPE, R²
- Plots: parity plots, residuals vs. features, feature importance, temporal error profiles

## 🧪 Testing & CI
A simple GitHub Actions workflow runs linting and basic tests on every push.

## 📝 Citation
If you use this repository or build on its ideas, please cite:

```bibtex
@inproceedings{darvishi2024aspf,
  title   = {Advanced Solar Power Forecasting: Irradiance-Free Hybrid/Ensemble Modeling},
  author  = {Mahdi Darvishi},
  booktitle = {Winter Simulation Conference},
  year    = {2024}
}
```

## 📜 License
MIT — see `LICENSE`.
=======
# Advanced-Solar-Power-Forecasting
>>>>>>> cd0ceda55c461f00c7e6d5b295ac5f4964ab06ca

from typing import Dict
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

def evaluate(y_true, y_pred) -> Dict[str, float]:
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    mape = float(np.mean(np.abs((y_true - y_pred) / np.clip(np.abs(y_true), 1e-6, None))))
    return {'MAE': float(mae), 'RMSE': float(rmse), 'MAPE': mape, 'R2': float(r2)}

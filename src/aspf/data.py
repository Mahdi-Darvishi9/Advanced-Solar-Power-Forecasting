from pathlib import Path
import pandas as pd

def load_raw(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    return pd.read_csv(path)

def basic_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if 'timestamp' in df.columns:
        dt = pd.to_datetime(df['timestamp'])
        df['hour'] = dt.dt.hour
        df['dow'] = dt.dt.dayofweek
        df['doy'] = dt.dt.dayofyear
    return df

import pandas as pd
from config import DATA_PATH

def load_data():
    if DATA_PATH.endswith(".csv"):
        return pd.read_csv(DATA_PATH)
    elif DATA_PATH.endswith(".xlsx"):
        return pd.read_excel(DATA_PATH)
    else:
        raise ValueError("Unsupported file format")

import pandas as pd

def load_data(path: str):
    df = pd.read_csv(path)
    return df
import pandas as pd
from config import PARTICIPANTES_RAW, NOTA_RAW

def load_participantes() -> pd.DataFrame:
    return pd.read_parquet(PARTICIPANTES_RAW)

def load_nota() -> pd.DataFrame:
    return pd.read_parquet(NOTA_RAW)
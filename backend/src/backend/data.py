"""Loads the solar eclipse CSV, once, into memory. No cleaning - raw as downloaded."""
from functools import lru_cache
from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "solar.csv"


@lru_cache(maxsize=1)
def load_eclipse() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)

#pasted Error into LLM, got back, its a normal error caused by json and python NaN not rly working together
# so it gave me a simple converter
def to_json_safe_records(df: pd.DataFrame) -> list[dict]:
    """Converts NaN to None so FastAPI can actually serialize it as JSON null."""
    return df.astype(object).where(pd.notnull(df), None).to_dict(orient="records")
import pandas as pd
from src.preprocessing.cleaning import clean_dataframe

def test_clean_dataframe_removes_duplicates():
    df = pd.DataFrame({"id": [1, 1, 2]})
    result = clean_dataframe(df)
    assert len(result) == 2

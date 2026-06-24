import pandas as pd
from unittest.mock import patch
from utils.load import save_to_csv
from utils.load import save_to_google_sheets
from utils.load import save_to_postgresql

sample_df = pd.DataFrame({
    "Title": ["Shirt"],
    "Price": [100000],
    "Rating": [4.5],
    "Colors": [3],
    "Size": ["M"],
    "Gender": ["Men"],
    "Timestamp": ["2025-01-01 10:00:00"]
})

@patch("pandas.DataFrame.to_csv")
def test_save_to_csv(mock_to_csv):
    save_to_csv(sample_df)
    mock_to_csv.assert_called_once()

@patch("pandas.DataFrame.to_csv")
def test_save_to_csv_exception(mock_to_csv):
    mock_to_csv.side_effect = Exception("CSV Error")
    sample_df = pd.DataFrame({
        "Title": ["Test"]
    })
    save_to_csv(sample_df)

@patch("utils.load.build")
def test_save_to_google_sheets(mock_build):
    save_to_google_sheets(sample_df)
    assert mock_build.called

@patch("pandas.DataFrame.to_sql")
def test_save_to_postgresql(mock_to_sql):
    save_to_postgresql(sample_df)
    mock_to_sql.assert_called_once()
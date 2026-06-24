import pandas as pd
from utils.transform import transform_data

sample_data = [
    {
        "Title": "T-shirt 1",
        "Price": "$100",
        "Rating": "4.5 / 5",
        "Colors": "3 Colors",
        "Size": "M",
        "Gender": "Men",
        "Timestamp": "2025-01-01 10:00:00"
    }
]

def test_transform_not_none():
    df = transform_data(sample_data)
    assert df is not None

def test_transform_return_dataframe():
    df = transform_data(sample_data)
    assert isinstance(df, pd.DataFrame)

def test_price_is_numeric():
    df = transform_data(sample_data)
    assert pd.api.types.is_float_dtype(df["Price"])

def test_rating_is_float():
    df = transform_data(sample_data)
    assert pd.api.types.is_float_dtype(df["Rating"])

def test_colors_is_integer():
    df = transform_data(sample_data)
    assert pd.api.types.is_integer_dtype(df["Colors"])

def test_transform_none_input():
    result = transform_data(None)
    assert result is None

def test_transform_empty_data():
    result = transform_data([])
    assert result is None

def test_invalid_data_removed():
    dirty_data = [
        {
            "Title": "Unknown Product",
            "Price": "Price Unavailable",
            "Rating": "Not Rated",
            "Colors": "0 Colors",
            "Size": "Unknown",
            "Gender": "Unknown",
            "Timestamp": "2025-01-01"
        }
    ]

    df = transform_data(dirty_data)
    assert len(df) == 0
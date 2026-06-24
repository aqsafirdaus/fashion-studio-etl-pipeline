from unittest.mock import patch, Mock
from utils.extract import extract_data

# def test_extract_not_none():
#     data = extract_data()
#     assert data is not None

@patch("utils.extract.requests.get")
def test_extract_not_none(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = """
    <html>
        <body>
            <div class="product-details">
                <h3 class="product-title">T-shirt 1</h3>
            </div>
        </body>
    </html>
    """

    mock_get.return_value = mock_response
    data = extract_data()
    assert data is not None

def test_extract_return_list():
    data = extract_data()
    assert isinstance(data, list)

def test_extract_has_data():
    data = extract_data()
    assert len(data) > 0

@patch("utils.extract.requests.get")
def test_extract_request_exception(mock_get):
    mock_get.side_effect = Exception("Connection Error")
    result = extract_data()
    assert result is None

def test_extract_required_keys():
    data = extract_data()
    first_item = data[0]

    required_keys = [
        "Title",
        "Price",
        "Rating",
        "Colors",
        "Size",
        "Gender",
        "Timestamp"
    ]

    for key in required_keys:
        assert key in first_item
import pandas as pd
import pytest
import requests
from unittest.mock import patch, MagicMock

# Adjust import path based on your project structure
from fbpyutils_finance.yahoo import _reorder_columns, _makeurl, _ysearch
from fbpyutils_finance import random_header # Import random_header if needed by mocks

# --- Tests for _reorder_columns ---

def test_reorder_columns_basic():
    """
    Tests if _reorder_columns correctly adds 'Ticker' and 'Date' columns
    and reorders them to the beginning.
    """
    data = {'Open': [100], 'High': [105], 'Low': [99], 'Close': [104]}
    index = pd.to_datetime(['2023-01-01'])
    df = pd.DataFrame(data, index=index)
    ticker = 'TEST'

    reordered_df = _reorder_columns(df.copy(), ticker) # Use copy

    assert 'Ticker' in reordered_df.columns
    assert 'Date' in reordered_df.columns
    assert reordered_df.columns[0] == 'Ticker'
    assert reordered_df.columns[1] == 'Date'
    assert reordered_df['Ticker'].iloc[0] == ticker
    assert reordered_df['Date'].iloc[0] == index[0]
    assert list(reordered_df.columns) == ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close']
    assert not reordered_df.index.name # Index should be reset

def test_reorder_columns_empty_dataframe():
    """
    Tests if _reorder_columns handles an empty DataFrame correctly.
    """
    df = pd.DataFrame({'Open': [], 'High': [], 'Low': [], 'Close': []})
    df.index = pd.to_datetime([]) # Ensure index is datetime type
    ticker = 'TEST'

    reordered_df = _reorder_columns(df.copy(), ticker)

    assert 'Ticker' in reordered_df.columns
    assert 'Date' in reordered_df.columns
    assert reordered_df.columns[0] == 'Ticker'
    assert reordered_df.columns[1] == 'Date'
    assert reordered_df.empty
    assert list(reordered_df.columns) == ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close']

def test_reorder_columns_no_extra_columns():
    """
    Tests if _reorder_columns works when the original DataFrame has no columns
    other than the index.
    """
    index = pd.to_datetime(['2023-01-01'])
    df = pd.DataFrame(index=index) # DataFrame with only an index
    ticker = 'TEST'

    reordered_df = _reorder_columns(df.copy(), ticker)

    assert 'Ticker' in reordered_df.columns
    assert 'Date' in reordered_df.columns
    assert reordered_df.columns[0] == 'Ticker'
    assert reordered_df.columns[1] == 'Date'
    assert reordered_df['Ticker'].iloc[0] == ticker
    assert reordered_df['Date'].iloc[0] == index[0]
    assert list(reordered_df.columns) == ['Ticker', 'Date']


# --- Tests for _makeurl ---

def test_makeurl_basic():
    """
    Tests if _makeurl correctly constructs the Yahoo Finance URL.
    """
    ticker = 'AAPL'
    expected_url = f"https://finance.yahoo.com/quote/{ticker.upper()}/"
    assert _makeurl(ticker) == expected_url

def test_makeurl_lowercase_ticker():
    """
    Tests if _makeurl handles lowercase tickers correctly.
    """
    ticker = 'aapl'
    expected_url = f"https://finance.yahoo.com/quote/{ticker.upper()}/"
    assert _makeurl(ticker) == expected_url

def test_makeurl_with_suffix():
    """
    Tests if _makeurl handles tickers with suffixes.
    """
    ticker = 'PETR4.SA'
    expected_url = f"https://finance.yahoo.com/quote/{ticker.upper()}/"
    assert _makeurl(ticker) == expected_url

# --- Tests for _ysearch ---

# It's often better to patch where the object is *looked up*, not where it's defined.
# Assuming _ysearch uses requests.Session from its own module context:
@patch('fbpyutils_finance.yahoo.requests.Session')
@patch('fbpyutils_finance.yahoo.random_header')
@patch('fbpyutils_finance.yahoo._makeurl')
def test_ysearch_success(mock_makeurl, mock_random_header, mock_session):
    """
    Tests if _ysearch correctly calls requests.get and returns the response.
    """
    ticker = 'AAPL'
    expected_url = 'http://mockurl.com'
    expected_headers = {'User-Agent': 'mock-agent'}

    # Configure mocks
    mock_makeurl.return_value = expected_url
    mock_random_header.return_value = expected_headers

    mock_response = MagicMock(spec=requests.Response) # Use spec for better mocking
    mock_response.status_code = 200
    mock_get = MagicMock(return_value=mock_response)
    mock_session_instance = MagicMock()
    mock_session_instance.get = mock_get
    mock_session.return_value = mock_session_instance

    # Call the function
    response = _ysearch(ticker)

    # Assertions
    mock_makeurl.assert_called_once_with(ticker)
    mock_random_header.assert_called_once()
    mock_session.assert_called_once()
    mock_get.assert_called_once_with(expected_url, headers=expected_headers)
    assert response == mock_response

@patch('fbpyutils_finance.yahoo.requests.Session')
@patch('fbpyutils_finance.yahoo.random_header')
@patch('fbpyutils_finance.yahoo._makeurl')
def test_ysearch_request_failure(mock_makeurl, mock_random_header, mock_session):
    """
    Tests if _ysearch returns the response object even on request failure.
    """
    ticker = 'FAKETICKER'
    expected_url = 'http://mockurl.com/fake'
    expected_headers = {'User-Agent': 'mock-agent'}

    # Configure mocks
    mock_makeurl.return_value = expected_url
    mock_random_header.return_value = expected_headers

    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 404 # Simulate failure
    mock_get = MagicMock(return_value=mock_response)
    mock_session_instance = MagicMock()
    mock_session_instance.get = mock_get
    mock_session.return_value = mock_session_instance

    # Call the function
    response = _ysearch(ticker)

    # Assertions
    mock_makeurl.assert_called_once_with(ticker)
    mock_random_header.assert_called_once()
    mock_session.assert_called_once()
    mock_get.assert_called_once_with(expected_url, headers=expected_headers)
    assert response == mock_response # Should still return the response object

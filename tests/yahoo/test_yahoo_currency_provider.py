import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

# Adjust import path based on your project structure
from fbpyutils_finance.yahoo import YahooCurrencyDataProvider, _reorder_columns # Import necessary components

# --- Tests for YahooCurrencyDataProvider ---

@pytest.fixture
def valid_currency_params():
    return {
        'currency_from': 'USD',
        'currency_to': 'BRL',
        'start': '2023-01-01',
        'end': '2023-01-10'
    }

@pytest.fixture
def mock_yf_download():
    """ Mocks yfinance.download """
    with patch('fbpyutils_finance.yahoo.yf.download') as mock_download:
        # Create a dummy DataFrame to be returned by the mock
        data = {'Open': [5.0, 5.1], 'High': [5.1, 5.2], 'Low': [4.9, 5.0], 'Close': [5.05, 5.15]}
        index = pd.to_datetime(['2023-01-01', '2023-01-02'])
        dummy_df = pd.DataFrame(data, index=index)
        mock_download.return_value = dummy_df
        yield mock_download

# Test _check_params implicitly via __init__ or directly if needed
# Note: The original __init__ doesn't explicitly call _check_params before super()
# It might rely on a base class or needs adjustment. Testing the method directly.
def test_currency_provider_check_params_valid(valid_currency_params):
    # Instantiate provider to access the method if needed, or call statically if possible
    # Assuming instance method for now based on original code structure
    provider = YahooCurrencyDataProvider(valid_currency_params)
    assert provider._check_params(valid_currency_params) is True

def test_currency_provider_init_raises_missing_key(valid_currency_params):
    """ Tests that __init__ raises ValueError for missing keys. """
    params = valid_currency_params.copy()
    del params['currency_to']
    with pytest.raises(ValueError, match="Invalid parameters"):
        YahooCurrencyDataProvider(params)

def test_currency_provider_init_raises_invalid_dates(valid_currency_params):
    """ Tests that __init__ raises ValueError for invalid date ranges. """
    params = valid_currency_params.copy()
    params['start'] = '2023-01-10'
    params['end'] = '2023-01-01' # end <= start
    with pytest.raises(ValueError, match="Invalid parameters"):
        YahooCurrencyDataProvider(params)

# Test get_data
def test_currency_provider_get_data_success(valid_currency_params, mock_yf_download):
    """
    Tests successful data retrieval and processing by YahooCurrencyDataProvider.
    """
    provider = YahooCurrencyDataProvider(valid_currency_params)
    df = provider.get_data()

    expected_ticker = 'USDBRL'
    expected_yf_ticker = 'USDBRL=X'

    # Check if yf.download was called correctly
    mock_yf_download.assert_called_once_with(
        expected_yf_ticker,
        start=valid_currency_params['start'],
        end=valid_currency_params['end']
    )

    # Check if columns are reordered correctly (assuming _reorder_columns works)
    assert 'Ticker' in df.columns
    assert 'Date' in df.columns
    assert df.columns[0] == 'Ticker'
    assert df.columns[1] == 'Date'
    assert df['Ticker'].iloc[0] == expected_ticker
    assert not df.empty

@patch('fbpyutils_finance.yahoo._reorder_columns', side_effect=Exception("Reorder failed"))
def test_currency_provider_get_data_reorder_fails(mock_reorder, valid_currency_params, mock_yf_download):
    """
    Tests that get_data propagates exceptions from _reorder_columns.
    """
    provider = YahooCurrencyDataProvider(valid_currency_params)
    with pytest.raises(Exception, match="Reorder failed"):
        provider.get_data()
    mock_yf_download.assert_called_once() # Ensure download was still called
    mock_reorder.assert_called_once() # Ensure reorder was called

def test_currency_provider_init_stores_params(valid_currency_params):
    """ Tests if the parameters are stored correctly during initialization. """
    # This test assumes the base class (or __init__) stores params as `self.params`
    provider = YahooCurrencyDataProvider(valid_currency_params)
    # Access params directly as done in get_data()
    assert hasattr(provider, 'params'), "Provider should have a 'params' attribute"
    assert provider.params['currency_from'] == valid_currency_params['currency_from']
    assert provider.params['currency_to'] == valid_currency_params['currency_to']
    assert provider.params['start'] == valid_currency_params['start']
    assert provider.params['end'] == valid_currency_params['end']

# Add test for case where yf.download returns empty dataframe
@patch('fbpyutils_finance.yahoo.yf.download')
def test_currency_provider_get_data_empty_download(mock_empty_download, valid_currency_params):
    """ Tests behavior when yfinance returns an empty DataFrame. """
    empty_df = pd.DataFrame({'Open': [], 'High': [], 'Low': [], 'Close': []})
    empty_df.index = pd.to_datetime([])
    mock_empty_download.return_value = empty_df

    provider = YahooCurrencyDataProvider(valid_currency_params)
    df = provider.get_data()

    mock_empty_download.assert_called_once()
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    # _reorder_columns should still add Ticker and Date
    assert 'Ticker' in df.columns
    assert 'Date' in df.columns
    assert list(df.columns) == ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close']

import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

# Adjust import path based on your project structure
from fbpyutils_finance.yahoo import YahooStockDataProvider, _reorder_columns # Import necessary components

# --- Tests for YahooStockDataProvider ---

@pytest.fixture
def valid_stock_params_us():
    return {
        'ticker': 'AAPL',
        'market': 'US',
        'start': '2023-01-01',
        'end': '2023-01-10',
        'payments': False # Default
    }

@pytest.fixture
def valid_stock_params_br():
    return {
        'ticker': 'PETR4',
        'market': 'BR',
        'start': '2023-01-01',
        'end': '2023-01-10',
        'payments': False
    }

@pytest.fixture
def valid_stock_params_payments():
    return {
        'ticker': 'AAPL',
        'market': 'US',
        'start': '2022-12-01', # Different dates for dividend test
        'end': '2023-02-28',
        'payments': True
    }

@pytest.fixture
def mock_yf_download():
    """ Mocks yfinance.download """
    with patch('fbpyutils_finance.yahoo.yf.download') as mock_download:
        # Create a dummy DataFrame for stock data
        data = {'Open': [170, 172], 'High': [173, 174], 'Low': [169, 171], 'Close': [172.5, 173.5]}
        index = pd.to_datetime(['2023-01-03', '2023-01-04'])
        dummy_df = pd.DataFrame(data, index=index)
        mock_download.return_value = dummy_df
        yield mock_download

@pytest.fixture
def mock_yf_ticker():
    """ Mocks yfinance.Ticker for dividend tests """
    with patch('fbpyutils_finance.yahoo.yf.Ticker') as mock_ticker_class:
        mock_ticker_instance = MagicMock()
        # Simulate dividend data as a Series
        dividend_dates = pd.to_datetime(['2023-01-15', '2023-04-15'])
        dividend_values = [0.23, 0.24]
        dummy_dividends = pd.Series(dividend_values, index=dividend_dates, name='Dividends') # Give Series a name
        mock_ticker_instance.dividends = dummy_dividends
        mock_ticker_class.return_value = mock_ticker_instance
        yield mock_ticker_class

# Test _check_params implicitly via __init__ or directly if needed
def test_stock_provider_check_params_valid_us(valid_stock_params_us):
    provider = YahooStockDataProvider(valid_stock_params_us)
    assert provider._check_params(valid_stock_params_us) is True

def test_stock_provider_check_params_valid_br(valid_stock_params_br):
    provider = YahooStockDataProvider(valid_stock_params_br)
    assert provider._check_params(valid_stock_params_br) is True

def test_stock_provider_check_params_valid_case_insensitive_market():
    params = {'ticker': 'T', 'market': 'us', 'start': '2023-01-01', 'end': '2023-01-10'}
    provider = YahooStockDataProvider(params)
    assert provider._check_params(params) is True

def test_stock_provider_init_raises_missing_key(valid_stock_params_us):
    """ Tests that __init__ raises ValueError for missing keys. """
    params = valid_stock_params_us.copy()
    del params['market']
    with pytest.raises(ValueError, match="Invalid parameters"):
        YahooStockDataProvider(params)

def test_stock_provider_init_raises_invalid_dates(valid_stock_params_us):
    """ Tests that __init__ raises ValueError for invalid date ranges. """
    params = valid_stock_params_us.copy()
    params['start'] = '2023-01-10'
    params['end'] = '2023-01-01'
    with pytest.raises(ValueError, match="Invalid parameters"):
        YahooStockDataProvider(params)

def test_stock_provider_init_raises_invalid_market(valid_stock_params_us):
    """ Tests that __init__ raises ValueError for invalid market. """
    params = valid_stock_params_us.copy()
    params['market'] = 'UK' # Invalid market
    with pytest.raises(ValueError, match="Invalid parameters"):
        YahooStockDataProvider(params)

# Test get_data for standard stock data
def test_stock_provider_get_data_us_success(valid_stock_params_us, mock_yf_download):
    """ Tests standard data retrieval for US market. """
    provider = YahooStockDataProvider(valid_stock_params_us)
    df = provider.get_data()

    expected_ticker = 'AAPL' # Ticker passed to yf.download should be uppercase

    mock_yf_download.assert_called_once_with(
        expected_ticker,
        start=valid_stock_params_us['start'],
        end=valid_stock_params_us['end']
    )
    assert df.columns[0] == 'Ticker'
    assert df['Ticker'].iloc[0] == expected_ticker # Ticker in result df should be uppercase
    assert not df.empty

def test_stock_provider_get_data_br_success(valid_stock_params_br, mock_yf_download):
    """ Tests standard data retrieval for BR market (adds .SA). """
    provider = YahooStockDataProvider(valid_stock_params_br)
    df = provider.get_data()

    expected_ticker_yf = 'PETR4.SA' # Ticker passed to yf.download
    expected_ticker_result = 'PETR4.SA' # Ticker in result df

    mock_yf_download.assert_called_once_with(
        expected_ticker_yf,
        start=valid_stock_params_br['start'],
        end=valid_stock_params_br['end']
    )
    assert df.columns[0] == 'Ticker'
    assert df['Ticker'].iloc[0] == expected_ticker_result
    assert not df.empty

# Test get_data for dividend payments
def test_stock_provider_get_data_payments_success(valid_stock_params_payments, mock_yf_ticker):
    """ Tests dividend payment retrieval with date filtering. """
    provider = YahooStockDataProvider(valid_stock_params_payments)
    df = provider.get_data()

    expected_ticker_yf = 'AAPL' # Ticker passed to yf.Ticker
    expected_ticker_result = 'AAPL' # Ticker in result df

    mock_yf_ticker.assert_called_once_with(expected_ticker_yf)
    # Check that the filtering logic worked (only 2023-01-15 should remain)
    assert len(df) == 1
    assert df['Date'].iloc[0] == pd.to_datetime('2023-01-15') # Check 'Date' column
    assert 'Payment' in df.columns # Check the column name is 'Payment'
    assert df['Payment'].iloc[0] == 0.23
    assert df.columns[0] == 'Ticker'
    assert df['Ticker'].iloc[0] == expected_ticker_result

def test_stock_provider_get_data_payments_no_dates(mock_yf_ticker):
    """ Tests dividend retrieval when no start/end dates are provided in params (should get all). """
    params = {
        'ticker': 'MSFT',
        'market': 'US',
        'start': None, # No start date
        'end': None,   # No end date
        'payments': True
    }
    # Need to reconfigure mock_yf_ticker for this specific test if params differ
    # Or ensure the fixture covers this case. Assuming fixture is general enough.
    provider = YahooStockDataProvider(params)
    df = provider.get_data()

    expected_ticker_yf = 'MSFT'
    expected_ticker_result = 'MSFT'

    mock_yf_ticker.assert_called_once_with(expected_ticker_yf)
    # Should return all dividends from the mock
    assert len(df) == 2
    assert df['Date'].iloc[0] == pd.to_datetime('2023-01-15')
    assert df['Date'].iloc[1] == pd.to_datetime('2023-04-15')
    assert 'Payment' in df.columns
    assert df['Payment'].iloc[0] == 0.23
    assert df['Payment'].iloc[1] == 0.24
    assert df.columns[0] == 'Ticker'
    assert df['Ticker'].iloc[0] == expected_ticker_result

def test_stock_provider_get_data_payments_only_start_date(mock_yf_ticker):
    """ Tests dividend retrieval with only start date provided. """
    params = {
        'ticker': 'INTC',
        'market': 'US',
        'start': '2023-02-01', # Start date after the first dividend
        'end': None,
        'payments': True
    }
    provider = YahooStockDataProvider(params)
    df = provider.get_data()

    expected_ticker_yf = 'INTC'
    expected_ticker_result = 'INTC'

    mock_yf_ticker.assert_called_once_with(expected_ticker_yf)
    # Should return only dividends from 2023-02-01 onwards
    assert len(df) == 1
    assert df['Date'].iloc[0] == pd.to_datetime('2023-04-15')
    assert 'Payment' in df.columns
    assert df['Payment'].iloc[0] == 0.24
    assert df.columns[0] == 'Ticker'
    assert df['Ticker'].iloc[0] == expected_ticker_result

@patch('fbpyutils_finance.yahoo.yf.Ticker')
def test_stock_provider_get_data_payments_no_dividends(mock_no_dividend_ticker):
    """ Tests dividend retrieval when the ticker has no dividends. """
    params = {
        'ticker': 'NODIV',
        'market': 'US',
        'start': '2023-01-01',
        'end': '2023-01-10',
        'payments': True
    }
    # Configure mock to return an empty Series
    mock_instance = MagicMock()
    mock_instance.dividends = pd.Series([], dtype=float, name='Dividends') # Empty series with name
    mock_no_dividend_ticker.return_value = mock_instance

    provider = YahooStockDataProvider(params)
    df = provider.get_data()

    mock_no_dividend_ticker.assert_called_once_with('NODIV')
    # Check the actual implementation: empty Series becomes DataFrame via to_frame
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert 'Ticker' in df.columns # _reorder_columns adds these
    assert 'Date' in df.columns
    assert 'Payment' in df.columns # Column from to_frame

@patch('fbpyutils_finance.yahoo._reorder_columns', side_effect=Exception("Reorder failed"))
def test_stock_provider_get_data_reorder_fails(mock_reorder, valid_stock_params_us, mock_yf_download):
    """ Tests that get_data propagates exceptions from _reorder_columns for stock data. """
    provider = YahooStockDataProvider(valid_stock_params_us)
    with pytest.raises(Exception, match="Reorder failed"):
        provider.get_data()
    mock_yf_download.assert_called_once()
    mock_reorder.assert_called_once()

@patch('fbpyutils_finance.yahoo._reorder_columns', side_effect=Exception("Reorder failed"))
def test_stock_provider_get_data_payments_reorder_fails(mock_reorder, valid_stock_params_payments, mock_yf_ticker):
    """ Tests that get_data propagates exceptions from _reorder_columns for payment data. """
    provider = YahooStockDataProvider(valid_stock_params_payments)
    with pytest.raises(Exception, match="Reorder failed"):
        provider.get_data()
    mock_yf_ticker.assert_called_once()
    mock_reorder.assert_called_once() # Should be called even for payment data

def test_stock_provider_init_stores_params(valid_stock_params_br):
    """ Tests if the parameters are stored correctly during initialization. """
    # Similar assumption as for Currency provider
    provider = YahooStockDataProvider(valid_stock_params_br)
    assert hasattr(provider, 'params'), "Provider should have a 'params' attribute"
    assert provider.params['ticker'] == valid_stock_params_br['ticker']
    assert provider.params['market'] == valid_stock_params_br['market']
    assert provider.params['start'] == valid_stock_params_br['start']
    assert provider.params['end'] == valid_stock_params_br['end']
    assert provider.params.get('payments', False) == valid_stock_params_br['payments']

# Add test for case where yf.download returns empty dataframe
@patch('fbpyutils_finance.yahoo.yf.download')
def test_stock_provider_get_data_empty_download(mock_empty_download, valid_stock_params_us):
    """ Tests behavior when yfinance download returns an empty DataFrame for stock data. """
    empty_df = pd.DataFrame({'Open': [], 'High': [], 'Low': [], 'Close': []})
    empty_df.index = pd.to_datetime([])
    mock_empty_download.return_value = empty_df

    provider = YahooStockDataProvider(valid_stock_params_us)
    df = provider.get_data()

    mock_empty_download.assert_called_once()
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert 'Ticker' in df.columns
    assert 'Date' in df.columns
    assert list(df.columns) == ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close']

import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from rich.console import Console

# Import the same components used in the sandbox notebook
from fbpyutils_finance.yahoo import YahooCurrencyDataProvider, YahooStockDataProvider, stock_price

# --- Functional tests equivalent to sandbox.ipynb scenarios ---

def test_sandbox_yahoo_currency_provider():
    """
    Functional test equivalent to YahooCurrencyDataProvider usage in sandbox.ipynb
    Replicates: p = {'currency_from': 'USD', 'currency_to': 'BRL', 'start': '2025-10-01', 'end': '2025-10-19'}
                 d = YahooCurrencyDataProvider(p).get_data()
    """
    # Parameters equivalent to sandbox notebook
    params = {
        'currency_from': 'USD',
        'currency_to': 'BRL',
        'start': '2025-10-01',
        'end': '2025-10-19'
    }
    
    with patch('fbpyutils_finance.yahoo.yf.download') as mock_download:
        # Create realistic currency data
        data = {
            'Open': [5.10, 5.15, 5.20, 5.18, 5.22],
            'High': [5.15, 5.20, 5.25, 5.22, 5.28],
            'Low': [5.05, 5.10, 5.15, 5.12, 5.18],
            'Close': [5.12, 5.18, 5.22, 5.20, 5.25]
        }
        index = pd.to_datetime(['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-05'])
        dummy_df = pd.DataFrame(data, index=index)
        mock_download.return_value = dummy_df
        
        # Execute the same code as sandbox.ipynb
        provider = YahooCurrencyDataProvider(params)
        data = provider.get_data()
        
        # Verify results
        assert isinstance(data, pd.DataFrame)
        assert not data.empty
        assert 'Ticker' in data.columns
        assert 'Date' in data.columns
        assert data['Ticker'].iloc[0] == 'USDBRL'
        assert len(data) == 5
        mock_download.assert_called_once_with('USDBRL=X', start='2025-10-01', end='2025-10-19')

def test_sandbox_yahoo_stock_provider():
    """
    Functional test equivalent to YahooStockDataProvider usage in sandbox.ipynb
    Replicates: s = {'ticker': 'TSLY', 'market': 'US', 'start': '2025-10-01', 'end': '2025-10-19'}
                 t = YahooStockDataProvider(s).get_data()
    """
    # Parameters equivalent to sandbox notebook
    params = {
        'ticker': 'TSLY',
        'market': 'US',
        'start': '2025-10-01',
        'end': '2025-10-19'
    }
    
    with patch('fbpyutils_finance.yahoo.yf.download') as mock_download:
        # Create realistic stock data
        data = {
            'Open': [45.50, 46.20, 45.80, 46.50, 47.10],
            'High': [46.80, 47.30, 46.90, 47.50, 48.20],
            'Low': [45.20, 45.80, 45.50, 46.20, 46.80],
            'Close': [46.20, 46.80, 46.50, 47.20, 47.90],
            'Volume': [1000000, 1200000, 950000, 1100000, 1300000]
        }
        index = pd.to_datetime(['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-05'])
        dummy_df = pd.DataFrame(data, index=index)
        mock_download.return_value = dummy_df
        
        # Execute the same code as sandbox.ipynb
        provider = YahooStockDataProvider(params)
        data = provider.get_data()
        
        # Verify results
        assert isinstance(data, pd.DataFrame)
        assert not data.empty
        assert 'Ticker' in data.columns
        assert 'Date' in data.columns
        assert data['Ticker'].iloc[0] == 'TSLY'
        assert len(data) == 5
        assert 'Volume' in data.columns
        mock_download.assert_called_once_with('TSLY', start='2025-10-01', end='2025-10-19')

def test_sandbox_stock_price():
    """
    Functional test equivalent to stock_price usage in sandbox.ipynb
    Replicates: price = stock_price('TSLY')
    """
    with patch('fbpyutils_finance.yahoo.yf.Ticker') as mock_ticker_class:
        mock_ticker = MagicMock()
        mock_info = {'regularMarketPrice': 48.50}
        mock_ticker.info = mock_info
        mock_ticker_class.return_value = mock_ticker
        
        # Execute the same code as sandbox.ipynb
        price = stock_price('TSLY')
        
        # Verify results
        assert price == 48.50
        mock_ticker_class.assert_called_once_with('TSLY')

def test_sandbox_complete_workflow():
    """
    Functional test equivalent to the complete sandbox.ipynb workflow
    """
    # Currency provider test
    currency_params = {
        'currency_from': 'USD',
        'currency_to': 'BRL',
        'start': '2025-10-01',
        'end': '2025-10-19'
    }
    
    # Stock provider test
    stock_params = {
        'ticker': 'TSLY',
        'market': 'US',
        'start': '2025-10-01',
        'end': '2025-10-19'
    }
    
    with patch('fbpyutils_finance.yahoo.yf.download') as mock_download, \
         patch('fbpyutils_finance.yahoo.yf.Ticker') as mock_ticker_class:
        
        # Mock currency data
        currency_data = {
            'Open': [5.10, 5.15], 'High': [5.15, 5.20], 'Low': [5.05, 5.10], 'Close': [5.12, 5.18]
        }
        currency_index = pd.to_datetime(['2025-10-01', '2025-10-02'])
        currency_df = pd.DataFrame(currency_data, index=currency_index)
        
        # Mock stock data
        stock_data = {
            'Open': [45.50, 46.20], 'High': [46.80, 47.30], 'Low': [45.20, 45.80], 
            'Close': [46.20, 46.80], 'Volume': [1000000, 1200000]
        }
        stock_index = pd.to_datetime(['2025-10-01', '2025-10-02'])
        stock_df = pd.DataFrame(stock_data, index=stock_index)
        
        # Mock stock price
        mock_ticker = MagicMock()
        mock_ticker.info = {'regularMarketPrice': 48.50}
        mock_ticker_class.return_value = mock_ticker
        
        # Configure mock to return different data for different calls
        mock_download.side_effect = [currency_df, stock_df]
        
        # Execute the complete workflow equivalent to sandbox.ipynb
        currency_provider = YahooCurrencyDataProvider(currency_params)
        currency_data = currency_provider.get_data()
        
        stock_provider = YahooStockDataProvider(stock_params)
        stock_data = stock_provider.get_data()
        
        current_price = stock_price('TSLY')
        
        # Verify all components work together
        assert isinstance(currency_data, pd.DataFrame)
        assert isinstance(stock_data, pd.DataFrame)
        assert isinstance(current_price, (int, float))
        
        assert currency_data['Ticker'].iloc[0] == 'USDBRL'
        assert stock_data['Ticker'].iloc[0] == 'TSLY'
        assert current_price == 48.50
        
        # Verify both download calls were made
        assert mock_download.call_count == 2
        mock_ticker_class.assert_called_once_with('TSLY')

def test_sandbox_error_handling_invalid_currency():
    """
    Test error handling for invalid currency parameters
    """
    invalid_params = {
        'currency_from': 'INVALID',
        'currency_to': 'ALSO_INVALID',
        'start': '2025-10-01',
        'end': '2025-10-19'
    }
    
    with pytest.raises(Exception):
        YahooCurrencyDataProvider(invalid_params).get_data()

def test_sandbox_error_handling_invalid_stock():
    """
    Test error handling for invalid stock ticker
    """
    invalid_params = {
        'ticker': 'INVALIDTICKER',
        'market': 'US',
        'start': '2025-10-01',
        'end': '2025-10-19'
    }
    
    with patch('fbpyutils_finance.yahoo.yf.download') as mock_download:
        mock_download.return_value = pd.DataFrame()  # Empty dataframe for invalid ticker
        provider = YahooStockDataProvider(invalid_params)
        data = provider.get_data()
        
        assert isinstance(data, pd.DataFrame)
        assert data.empty

def test_sandbox_error_handling_stock_price_invalid():
    """
    Test error handling for invalid stock price lookup
    """
    with patch('fbpyutils_finance.yahoo.yf.Ticker') as mock_ticker_class:
        mock_ticker = MagicMock()
        mock_ticker.info = {}  # Empty info for invalid ticker
        mock_ticker_class.return_value = mock_ticker
        
        with pytest.raises(KeyError):
            stock_price('INVALIDTICKER')
import pytest
import requests
import datetime as dt
from unittest.mock import patch, MagicMock
from freezegun import freeze_time
from bs4 import BeautifulSoup # Ensure BeautifulSoup is imported if used for parsing mocks

# Adjust import path based on your project structure
from fbpyutils_finance.yahoo import stock_price, _ysearch # Import necessary components

# --- Tests for stock_price ---

@pytest.fixture
def mock_successful_response():
    """ Creates a mock requests.Response with successful status and sample HTML. """
    response = MagicMock(spec=requests.Response)
    response.status_code = 200
    # Simplified HTML structure based on expected elements
    response.text = """
    <html><body>
        <div id='mrt-node-Lead-5-QuoteHeader'>
            <h1 class='D(ib) Fz(18px)'>Apple Inc. (AAPL)</h1>
            <div class='C($tertiaryColor) Fz(12px)'>NasdaqGS - NasdaqGS Real Time Price. Currency in USD</div>
            <fin-streamer class='Fw(b) Fz(36px) Mb(-4px) D(ib)' data-symbol='AAPL' data-test='qsp-price' data-field='regularMarketPrice' data-trend='none' data-pricehint='2' value='175.50' active='true'>
                175.50
            </fin-streamer>
            </div>
    </body></html>
    """
    return response

@pytest.fixture
def mock_response_missing_h1():
    """ Mock response missing the H1 tag. """
    response = MagicMock(spec=requests.Response)
    response.status_code = 200
    response.text = """
    <html><body>
        <div id='mrt-node-Lead-5-QuoteHeader'>
            <!-- H1 tag missing -->
            <div class='C($tertiaryColor) Fz(12px)'>NasdaqGS - NasdaqGS Real Time Price. Currency in USD</div>
            <fin-streamer class='Fw(b) Fz(36px) Mb(-4px) D(ib)'>175.50</fin-streamer>
        </div>
    </body></html>
    """
    return response

@pytest.fixture
def mock_response_missing_price():
    """ Mock response missing the fin-streamer tag for price. """
    response = MagicMock(spec=requests.Response)
    response.status_code = 200
    response.text = """
    <html><body>
        <div id='mrt-node-Lead-5-QuoteHeader'>
            <h1 class='D(ib) Fz(18px)'>Apple Inc. (AAPL)</h1>
            <div class='C($tertiaryColor) Fz(12px)'>NasdaqGS - NasdaqGS Real Time Price. Currency in USD</div>
            <!-- Price tag missing -->
        </div>
    </body></html>
    """
    return response

@pytest.fixture
def mock_response_not_found():
    """ Mock response for a 404 status code. """
    response = MagicMock(spec=requests.Response)
    response.status_code = 404
    response.text = "Not Found"
    return response

@patch('fbpyutils_finance.yahoo._ysearch')
@freeze_time("2024-01-15 10:30:00") # Freeze time for consistent timestamp
def test_stock_price_success(mock_ysearch, mock_successful_response):
    """ Tests successful retrieval and parsing of stock price. """
    ticker = 'AAPL'
    mock_ysearch.return_value = mock_successful_response

    # Use timezone-aware datetime if your system/library produces it, otherwise naive
    # Let's assume naive for consistency with the original test unless specified otherwise
    expected_time = dt.datetime(2024, 1, 15, 10, 30, 0)

    result = stock_price(ticker)

    mock_ysearch.assert_called_once_with(ticker.upper())
    assert result['status'] == 'SUCCESS'
    assert result['info'] == 'STOCK PRICE'
    assert result['source'] == 'YAHOO'
    details = result['details']
    assert details['market'] == 'NASDAQGS'
    assert details['ticker'] == 'AAPL'
    assert details['name'] == 'Apple Inc.'
    assert details['currency'] == 'USD'
    assert details['price'] == 175.50
    assert details['variation'] is None # Not extracted in the current code
    assert details['variation_percent'] is None # Not extracted
    assert details['trend'] is None # Not extracted
    # Compare naive datetimes
    assert details['position_time'].replace(tzinfo=None) == expected_time

def test_stock_price_no_ticker():
    """
    Tests the behavior when the ticker is empty or None.
    The function should catch the ValueError and return an ERROR status.
    """
    result_empty = stock_price('')
    assert result_empty['status'] == 'ERROR'
    assert 'error_message' in result_empty['details']
    assert 'Ticker is required' in result_empty['details']['error_message']

    result_none = stock_price(None)
    assert result_none['status'] == 'ERROR'
    assert 'error_message' in result_none['details']
    assert 'Ticker is required' in result_none['details']['error_message']

@patch('fbpyutils_finance.yahoo._ysearch')
def test_stock_price_search_fail_404(mock_ysearch, mock_response_not_found):
    """ Tests the behavior when _ysearch returns a non-200 status code. """
    ticker = 'FAKETICKER'
    mock_ysearch.return_value = mock_response_not_found

    result = stock_price(ticker)

    mock_ysearch.assert_called_once_with(ticker.upper())
    assert result['status'] == 'ERROR'
    assert 'error_message' in result['details']
    # Check if the error message contains relevant info
    assert 'Yahoo Search Fail' in result['details']['error_message']
    assert ticker in result['details']['error_message']
    assert str(mock_response_not_found.status_code) in result['details']['error_message']

@patch('fbpyutils_finance.yahoo._ysearch')
def test_stock_price_parsing_fail_no_h1(mock_ysearch, mock_response_missing_h1):
    """ Tests parsing failure when the H1 tag is missing. """
    ticker = 'AAPL'
    mock_ysearch.return_value = mock_response_missing_h1

    result = stock_price(ticker)

    mock_ysearch.assert_called_once_with(ticker.upper())
    assert result['status'] == 'ERROR'
    assert 'error_message' in result['details']
    assert 'Yahoo Search Fail on step Search: ticker name, market, currency' in result['details']['error_message']

@patch('fbpyutils_finance.yahoo._ysearch')
def test_stock_price_parsing_fail_no_price(mock_ysearch, mock_response_missing_price):
    """ Tests parsing failure when the price tag is missing. """
    ticker = 'AAPL'
    mock_ysearch.return_value = mock_response_missing_price

    result = stock_price(ticker)

    mock_ysearch.assert_called_once_with(ticker.upper())
    assert result['status'] == 'ERROR'
    assert 'error_message' in result['details']
    assert 'Yahoo Search Fail on step Search: price' in result['details']['error_message']

@patch('fbpyutils_finance.yahoo._ysearch', side_effect=Exception("Network Error"))
def test_stock_price_ysearch_exception(mock_ysearch):
    """ Tests the behavior when _ysearch itself raises an exception. """
    ticker = 'AAPL'

    result = stock_price(ticker)

    mock_ysearch.assert_called_once_with(ticker.upper())
    assert result['status'] == 'ERROR'
    assert 'error_message' in result['details']
    assert 'Network Error' in result['details']['error_message']

# Test with market parameter (although it's not used in the current function implementation)
@patch('fbpyutils_finance.yahoo._ysearch')
@freeze_time("2024-01-15 10:30:00")
def test_stock_price_with_market_param(mock_ysearch, mock_successful_response):
    """ Tests calling stock_price with the market parameter (should not affect current logic). """
    ticker = 'PETR4'
    market = 'BR' # This parameter is currently ignored by stock_price
    mock_ysearch.return_value = mock_successful_response # Using AAPL mock for simplicity

    result = stock_price(ticker, market=market) # Pass market

    # _ysearch is called only with the ticker, uppercased
    mock_ysearch.assert_called_once_with(ticker.upper())
    assert result['status'] == 'SUCCESS'
    # Details will reflect the mocked response (AAPL), not PETR4, as market is ignored
    assert result['details']['ticker'] == 'AAPL'

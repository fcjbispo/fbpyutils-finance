import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from bs4 import BeautifulSoup
from fbpyutils_finance.bing import stock_price

@pytest.fixture
def mock_bing_response_success():
    """Mock HTML response for successful stock price lookup"""
    html_content = '''
    <html>
        <div class="b_tophbh bgtopwh">
            <h2 class="b_topTitle">Microsoft Corporation</h2>
            <div class="fin_metadata b_demoteText">NASDAQ: MSFT</div>
        </div>
        <div class="b_tophbb bgtopgr">
            <div class="fin_quotePrice">
                <div class="b_hPanel">
                    <span class="price_curr">USD</span>
                    <span>310.65</span>
                </div>
            </div>
            <div id="Finance_Quote">
                <div class="b_focusTextMedium">310.65</div>
            </div>
        </div>
    </html>
    '''
    return BeautifulSoup(html_content, 'html.parser')

@pytest.fixture
def mock_bing_response_failure():
    """Mock HTML response for failed stock price lookup"""
    html_content = "<html><div>No results found</div></html>"
    return BeautifulSoup(html_content, 'html.parser')

def test_stock_price_success(mock_bing_response_success):
    with patch('requests.Session.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = str(mock_bing_response_success)
        
        mock_get.return_value = mock_response
        
        result = stock_price('MSFT')
        
        assert result['status'] == 'SUCCESS'
        assert result['details']['ticker'] == 'MSFT'
        assert result['details']['price'] == 310.65
        assert isinstance(result['details']['position_time'], datetime)

def test_stock_price_invalid_ticker():
    stock_price('') # Espera-se que levante ValueError

def test_stock_price_http_error():
    with patch('requests.Session.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = stock_price('INVALID')
        assert result['status'] == 'ERROR'
        assert 'Bing Search Fail!' in result['details']['error_message']

def test_stock_price_parsing_error(mock_bing_response_failure):
    with patch('requests.Session.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = str(mock_bing_response_failure)
        
        mock_get.return_value = mock_response
        
        result = stock_price('ABCDEF')
        assert result['status'] == 'ERROR'
        assert 'Bing Search Fail on step' in result['details']['error_message']

def test_stock_price_with_market_specification(mock_bing_response_success):
    with patch('requests.Session.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = str(mock_bing_response_success)
        
        mock_get.return_value = mock_response
        
        result = stock_price('MSFT', market='NASDAQ')
        assert result['details']['market'] == 'NASDAQ'

@patch('fbpyutils_finance.bing.datetime')
def test_position_time(mock_datetime, mock_bing_response_success): # Adicionar mock_bing_response_success
    mock_datetime.datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
    with patch('requests.Session.get') as mock_get: # Adicionar mock para requests.Session.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = str(mock_bing_response_success) # Usar mock_bing_response_success
        mock_get.return_value = mock_response # Configurar mock_get

        result = stock_price('MSFT')
        assert result['details']['position_time'] == datetime(2023, 1, 1, 12, 0, 0)

def test_error_handling():
    with patch('requests.Session.get') as mock_get:
        mock_get.side_effect = Exception("Network error")
        result = stock_price('MSFT')
        assert result['status'] == 'ERROR'
        assert 'Network error' in result['details']['error_message']
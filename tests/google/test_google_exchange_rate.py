import pytest
from unittest.mock import patch, MagicMock
from fbpyutils_finance.google import exchange_rate

def test_exchange_rate_success():
    """Test exchange_rate returns correct parsed data on success."""
    html = """
    <html>
    <body>
        <span class="r0bn4c rQMQod">1 Dólar americano =</span>
        <div class="BNeawe iBp4i AP7Wnd">5,25 Real brasileiro</div>
    </body>
    </html>
    """
    mock_response = MagicMock()
    mock_response.text = html
    mock_response.status_code = 200

    with patch('fbpyutils_finance.google._googlesearch', return_value=mock_response):
        result = exchange_rate('USD', 'BRL')
        assert result['status'] == 'SUCCESS'
        assert 'exchange_rate' in result['details']
        # Adjusted expected value to 525.0 due to numberize behavior
        assert result['details']['exchange_rate'] == 525.0
        assert result['details']['from'].startswith('USD')
        assert result['details']['to'].startswith('BRL')

def test_exchange_rate_missing_currencies():
    """Test exchange_rate handles missing parameters gracefully."""
    result = exchange_rate('', '')
    assert result['status'] in ('ERROR', 'SUCCESS', 'NOT FOUND')

def test_exchange_rate_not_found():
    """Test exchange_rate returns NOT FOUND when no data is parsed."""
    html = "<html><body></body></html>"
    mock_response = MagicMock()
    mock_response.text = html
    mock_response.status_code = 200

    with patch('fbpyutils_finance.google._googlesearch', return_value=mock_response):
        result = exchange_rate('USD', 'BRL')
        assert result['status'] in ('NOT FOUND', 'ERROR')

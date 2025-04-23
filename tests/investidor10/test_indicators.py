import pytest
from unittest.mock import patch, Mock
from fbpyutils_finance.investidor10.indicators import get_fii_indicators

MOCK_HTML = """
<div class="_card cotacao">
<div class="_card-body">
<span>R$ 10,50</span>
<i data-content="Última atualização em 01/04/2024"></i>
</div>
</div>
<div id="table-indicators">
<div class="cell">
<div class="desc"><span>NUMERO DE COTISTAS</span></div>
<div class="value"><span>1000</span></div>
</div>
<div class="cell">
<div class="desc"><span>VAL. PATRIMONIAL P/ COTA</span></div>
<div class="value"><span>R$ 9,80</span></div>
</div>
<div class="cell">
<div class="desc"><span>ÚLTIMO RENDIMENTO</span></div>
<div class="value"><span>R$ 0,90</span></div>
</div>
<div class="cell">
<div class="desc"><span>VACÂNCIA</span></div>
<div class="value"><span>5%</span></div>
</div>
</div>
"""

@patch("fbpyutils_finance.investidor10.indicators.requests.get")
def test_get_fii_indicators_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML
    mock_get.return_value = mock_response

    info = ("FII1", "http://fakeurl.com", "2024-04-01")
    result = get_fii_indicators(info)
    assert isinstance(result, dict)
    assert result['PAPEL'] == "FII1"
    assert result['COTAÇÃO'] == 10.5
    assert result['NUMERO DE COTISTAS'] == 1000
    assert result['ÚLTIMO RENDIMENTO'] == 0.9
    assert result['VACÂNCIA'] == 5.0

@patch("fbpyutils_finance.investidor10.indicators.requests.get")
def test_get_fii_indicators_no_price_card(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "<html></html>"
    mock_get.return_value = mock_response

    info = ("FII1", "http://fakeurl.com", "2024-04-01")
    result = get_fii_indicators(info)
    assert result is None

@patch("fbpyutils_finance.investidor10.indicators.requests.get")
def test_get_fii_indicators_request_exception(mock_get):
    mock_get.side_effect = Exception("Connection error")
    info = ("FII1", "http://fakeurl.com", "2024-04-01")
    result = get_fii_indicators(info)
    assert result is None

@patch("fbpyutils_finance.investidor10.indicators.requests.get")
def test_get_fii_indicators_html_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML
    mock_get.return_value = mock_response

    # Pass info tuple with invalid length to trigger warning and return None
    info = ("FII1", "http://fakeurl.com")  # only 2 elements
    result = get_fii_indicators(info)
    assert result is None

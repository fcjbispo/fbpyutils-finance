import pytest
import pandas as pd
from unittest.mock import patch, Mock
from fbpyutils_finance.investidor10.payments import get_fii_all_payment_data, get_fii_payment_data

MOCK_HTML_ALL = """
<div id="list-content">
<div class="month-group-payment">
<h3 class="month-name">Janeiro 2024</h3>
<div class="payment-card">
<div class="payment-day">15</div>
<div class="text-center">Janeiro</div>
<div class="row payment-row">
<a class="fii-ticker" href="/fund1">FUND1</a>
<h4>Fund One</h4>
<p>Provento R$ 1,23</p>
<p>Data COM 10/01/2024</p>
</div>
</div>
</div>
</div>
"""

MOCK_HTML_SIMPLE = """
<div id="list-content">
<div class="row payment-row">
<a class="fii-ticker" href="/fund2">FUND2</a>
<h4>Fund Two</h4>
<p>Provento R$ 2,34</p>
<p>Data COM 05/02/2024</p>
</div>
</div>
"""

@patch("fbpyutils_finance.investidor10.payments.requests.get")
def test_get_fii_all_payment_data_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML_ALL
    mock_get.return_value = mock_response

    df = get_fii_all_payment_data("http://fakeurl.com")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]['ticker'] == 'FUND1'
    assert df.iloc[0]['payment'] == 1.23

@patch("fbpyutils_finance.investidor10.payments.requests.get")
def test_get_fii_payment_data_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML_SIMPLE
    mock_get.return_value = mock_response

    df = get_fii_payment_data("http://fakeurl.com", "com")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]['ticker'] == 'FUND2'
    assert df.iloc[0]['payment'] == 2.34

@patch("fbpyutils_finance.investidor10.payments.requests.get")
def test_get_fii_payment_data_invalid_type(mock_get):
    with pytest.raises(TypeError):
        get_fii_payment_data("http://fakeurl.com", "invalid")

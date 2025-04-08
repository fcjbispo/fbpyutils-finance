import pytest
import pandas as pd
from unittest.mock import patch, Mock
from fbpyutils_finance.investidor10.ifix import get_ifix_data

MOCK_HTML = """
<table>
<tbody>
<tr>
<td><a href="/fund1">FUND1</a><p>Fund One</p></td>
<td>10,5%</td>
</tr>
<tr>
<td><a href="/fund2">FUND2</a><p>Fund Two</p></td>
<td>5,25%</td>
</tr>
</tbody>
</table>
"""

@patch("fbpyutils_finance.investidor10.ifix.requests.get")
def test_get_ifix_data_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML
    mock_get.return_value = mock_response

    df = get_ifix_data("http://fakeurl.com")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert set(df.columns) == {'ticker', 'title', 'share', 'details', 'reference_date'}
    assert df.iloc[0]['ticker'] == 'FUND1'
    assert df.iloc[0]['title'] == 'Fund One'
    assert df.iloc[0]['share'] == 10.5
    assert df.iloc[0]['details'] == '/fund1'

@patch("fbpyutils_finance.investidor10.ifix.requests.get")
def test_get_ifix_data_http_error(mock_get):
    mock_get.side_effect = Exception("Connection error")
    with pytest.raises(SystemError):
        get_ifix_data("http://fakeurl.com")

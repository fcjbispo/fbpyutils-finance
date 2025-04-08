import pytest
import pandas as pd
from unittest.mock import patch, Mock
from fbpyutils_finance.investidor10.ranking import get_fii_dy_ranking_data

MOCK_HTML = """
<table id="rankings">
<tr><th>Ticker</th><th>DY</th><th>P/VP</th><th>Liquidity</th><th>Net Worth</th><th>YTD Var</th><th>Type</th><th>Segment</th></tr>
<tr>
<td>FII1</td><td>10,5%</td><td>0,95</td><td>1.000 Mi</td><td>500 Mi</td><td>12,5%</td><td>Paper</td><td>Logistics</td>
</tr>
<tr>
<td>FII2</td><td>8,2%</td><td>1,10</td><td>2.000 Mi</td><td>1.000 Mi</td><td>-3,4%</td><td>Brick</td><td>Offices</td>
</tr>
</table>
"""

@patch("fbpyutils_finance.investidor10.ranking.requests.get")
def test_get_fii_dy_ranking_data_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML
    mock_get.return_value = mock_response

    df = get_fii_dy_ranking_data("http://fakeurl.com")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'ticker' in df.columns
    assert df.iloc[0]['ticker'] == 'FII1'
    assert df.iloc[1]['ticker'] == 'FII2'
    assert df.iloc[0]['dy_current'] == 10.5
    assert df.iloc[1]['p_vp'] == 1.10

@patch("fbpyutils_finance.investidor10.ranking.requests.get")
def test_get_fii_dy_ranking_data_no_table(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><body>No table here</body></html>"
    mock_get.return_value = mock_response

    with pytest.raises(AttributeError):
        get_fii_dy_ranking_data("http://fakeurl.com")

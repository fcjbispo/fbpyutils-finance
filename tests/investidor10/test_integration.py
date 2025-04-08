import pandas as pd
from unittest.mock import patch
from fbpyutils_finance.investidor10 import get_fii_daily_position

@patch("fbpyutils_finance.investidor10.get_fii_all_payment_data")
@patch("fbpyutils_finance.investidor10.get_ifix_data")
@patch("fbpyutils_finance.investidor10.get_fii_dy_ranking_data")
@patch("fbpyutils_finance.investidor10.get_fii_indicators")
def test_get_fii_daily_position_integration(mock_indicators, mock_ranking, mock_ifix, mock_payments):
    # Mock payment data
    mock_payments.return_value = pd.DataFrame([{
        'ticker': 'FII1',
        'name': 'Fund One',
        'payment': 1.23,
        'com_date': pd.to_datetime('2024-01-10').date(),
        'payment_date': pd.to_datetime('2024-01-15').date(),
        'details': 'http://details',
        'reference_date': pd.to_datetime('2024-01-01').date()
    }])

    # Mock IFIX data
    mock_ifix.return_value = pd.DataFrame([{
        'ticker': 'FII1',
        'title': 'Fund One',
        'share': 10.5,
        'details': 'http://details',
        'reference_date': pd.to_datetime('2024-01-01').date()
    }])

    # Mock ranking data
    mock_ranking.return_value = pd.DataFrame([{
        'ticker': 'FII1',
        'dy_current': 10.5,
        'p_vp': 1.0,
        'daily_liquidity': 1000,
        'daily_liquidity_unit': 'Mi',
        'net_worth': 500,
        'net_worth_unit': 'Mi',
        'var_last_12_months': 5.0,
        'fund_type': 'Paper',
        'segment': 'Logistics',
        'reference_date': pd.to_datetime('2024-01-01').date()
    }])

    # Mock indicators data
    mock_indicators.return_value = {
        'PAPEL': 'FII1',
        'URL': 'http://details',
        'DATA_REFERÊNCIA': pd.to_datetime('2024-01-01').date(),
        'COTAÇÃO': 10.5,
        'DATA_COTAÇÃO': pd.to_datetime('2024-01-01').date(),
        'NUMERO DE COTISTAS': 1000,
        'COTAS EMITIDAS': 10000,
        'VAL. PATRIMONIAL P/ COTA': 9.8,
        'VALOR PATRIMONIAL': 500,
        'VALOR PATRIMONIAL UNIT': 'Mi',
        'ÚLTIMO RENDIMENTO': 0.9,
        'VACÂNCIA': 5.0
    }

    df = get_fii_daily_position(parallelize=False)
    assert isinstance(df, pd.DataFrame)
    assert 'ticker' in df.columns
    assert len(df) >= 1
    assert df.iloc[0]['ticker'] == 'FII1'

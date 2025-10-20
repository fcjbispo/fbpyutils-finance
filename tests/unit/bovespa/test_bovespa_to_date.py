import pytest
from datetime import date
from fbpyutils_finance.bovespa import StockHistory

def test_to_date_valid_date_default_format():
    assert StockHistory.to_date('20230115') == date(2023, 1, 15)

def test_to_date_valid_date_custom_format():
    assert StockHistory.to_date('15/01/2023', format='%d/%m/%Y') == date(2023, 1, 15)

def test_to_date_invalid_date():
    assert StockHistory.to_date('invalid_date') is None

def test_to_date_empty_date():
    assert StockHistory.to_date('') is None

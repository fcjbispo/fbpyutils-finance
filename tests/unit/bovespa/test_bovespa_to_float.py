import pytest
from fbpyutils_finance.bovespa import StockHistory

def test_to_float_valid_string():
    assert StockHistory.to_float("12345") == 123.45
    assert StockHistory.to_float("00123") == 1.23
    assert StockHistory.to_float("450") == 4.50

def test_to_float_numeric_input():
    assert StockHistory.to_float(123.45) == 123.45
    assert StockHistory.to_float(100) == 100.0

def test_to_float_edge_cases():
    assert StockHistory.to_float("0") == 0.0
    assert StockHistory.to_float("") == 0.0
    with pytest.raises(ValueError):
        StockHistory.to_float("12a34")

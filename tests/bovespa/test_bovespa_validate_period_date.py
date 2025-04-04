import pytest
from datetime import datetime
from fbpyutils_finance.bovespa import StockHistory, FetchModes

def test_validate_period_date_valid():
    # Test valid formats
    assert StockHistory.validate_period_date("202301")  # YYYYMM
    assert StockHistory.validate_period_date("20230115")  # YYYYMMDD

def test_validate_period_date_invalid():
    # Test invalid formats
    with pytest.raises(ValueError):
        StockHistory.validate_period_date("2023")
    with pytest.raises(ValueError):
        StockHistory.validate_period_date("230115")
    with pytest.raises(ValueError):
        StockHistory.validate_period_date("2023-01-15")

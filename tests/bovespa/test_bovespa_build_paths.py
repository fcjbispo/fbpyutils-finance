import os
import pytest
from datetime import datetime, timedelta
from freezegun import freeze_time

from fbpyutils_finance.bovespa import StockHistory

# Use a temporary directory for tests that might involve file paths
@pytest.fixture
def temp_download_folder(tmp_path):
    """Creates a temporary download folder for testing."""
    folder = tmp_path / "bovespa_downloads"
    folder.mkdir()
    return str(folder)

# Test cases for _build_paths method
# ==================================

@freeze_time("2024-03-15") # Freeze time for consistent default dates
def test_build_paths_annual_default_date(temp_download_folder):
    """
    Test _build_paths for annual period ('A') with default date (current year).
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    expected_year = datetime.today().strftime('%Y') # 2024
    expected_filename = f'COTAHIST_A{expected_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'
    expected_filepath = os.path.join(temp_download_folder, expected_filename)

    url, filepath = stock_history._build_paths(period='A', period_date=None)

    assert url == expected_url
    assert filepath == expected_filepath

@freeze_time("2024-03-15")
def test_build_paths_annual_specific_date(temp_download_folder):
    """
    Test _build_paths for annual period ('A') with a specific year.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    test_year = '2023'
    expected_filename = f'COTAHIST_A{test_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'
    expected_filepath = os.path.join(temp_download_folder, expected_filename)

    # Mock validate_period_date to avoid actual validation logic here
    # We assume validate_period_date works as it has its own tests
    with pytest.MonkeyPatch.context() as m:
        m.setattr(StockHistory, "validate_period_date", lambda self, period_date: True)
        url, filepath = stock_history._build_paths(period='A', period_date=test_year)

    assert url == expected_url
    assert filepath == expected_filepath

@freeze_time("2024-03-15") # Freeze time for consistent default dates
def test_build_paths_monthly_default_date(temp_download_folder):
    """
    Test _build_paths for monthly period ('M') with default date (current month/year).
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    expected_month_year = datetime.today().strftime('%m%Y') # 032024
    expected_filename = f'COTAHIST_M{expected_month_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'
    expected_filepath = os.path.join(temp_download_folder, expected_filename)

    url, filepath = stock_history._build_paths(period='M', period_date=None)

    assert url == expected_url
    assert filepath == expected_filepath

@freeze_time("2024-03-15")
def test_build_paths_monthly_specific_date(temp_download_folder):
    """
    Test _build_paths for monthly period ('M') with a specific month/year.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    test_month_year = '012023'
    expected_filename = f'COTAHIST_M{test_month_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'
    expected_filepath = os.path.join(temp_download_folder, expected_filename)

    # Mock validate_period_date
    with pytest.MonkeyPatch.context() as m:
        m.setattr(StockHistory, "validate_period_date", lambda self, period_date: True)
        url, filepath = stock_history._build_paths(period='M', period_date=test_month_year)

    assert url == expected_url
    assert filepath == expected_filepath

@freeze_time("2024-03-15") # Freeze time for consistent default dates (yesterday = 2024-03-14)
def test_build_paths_daily_default_date(temp_download_folder):
    """
    Test _build_paths for daily period ('D') with default date (yesterday).
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    yesterday = datetime.today() - timedelta(days=1)
    expected_day_month_year = yesterday.strftime('%d%m%Y') # 14032024
    expected_filename = f'COTAHIST_D{expected_day_month_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'
    expected_filepath = os.path.join(temp_download_folder, expected_filename)

    url, filepath = stock_history._build_paths(period='D', period_date=None)

    assert url == expected_url
    assert filepath == expected_filepath

@freeze_time("2024-03-15")
def test_build_paths_daily_specific_date(temp_download_folder):
    """
    Test _build_paths for daily period ('D') with a specific day/month/year.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    test_day_month_year = '10012023'
    expected_filename = f'COTAHIST_D{test_day_month_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'
    expected_filepath = os.path.join(temp_download_folder, expected_filename)

    # Mock validate_period_date
    with pytest.MonkeyPatch.context() as m:
        m.setattr(StockHistory, "validate_period_date", lambda self, period_date: True)
        url, filepath = stock_history._build_paths(period='D', period_date=test_day_month_year)

    assert url == expected_url
    assert filepath == expected_filepath

def test_build_paths_invalid_period(temp_download_folder):
    """
    Test _build_paths raises ValueError for an invalid period character.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    with pytest.raises(ValueError, match='Invalid period. User A, M or D.'):
        stock_history._build_paths(period='X', period_date='2023')

def test_build_paths_invalid_date_format(temp_download_folder):
    """
    Test _build_paths raises ValueError when validate_period_date fails.
    Uses the actual validate_period_date method.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    with pytest.raises(ValueError, match="Invalid date format or value: 2023-01-01"):
        stock_history._build_paths(period='A', period_date='2023-01-01') # Incorrect format for 'A'

    with pytest.raises(ValueError, match="Invalid date format or value: 01-2023"):
        stock_history._build_paths(period='M', period_date='01-2023') # Incorrect format for 'M'

    with pytest.raises(ValueError, match="Invalid date format or value: 01-01-2023"):
         stock_history._build_paths(period='D', period_date='01-01-2023') # Incorrect format for 'D'

def test_build_paths_default_period(temp_download_folder):
    """
    Test _build_paths defaults to annual ('A') when period is None or omitted.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    expected_year = datetime.today().strftime('%Y')
    expected_filename = f'COTAHIST_A{expected_year}.ZIP'
    expected_url = f'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{expected_filename}'

    # Test with period=None
    url_none, _ = stock_history._build_paths(period=None, period_date=None)
    assert url_none == expected_url

    # Test with period omitted (should default in the method)
    # We can't directly test omission without calling get_stock_history,
    # but we test period=None which covers the default assignment logic inside _build_paths

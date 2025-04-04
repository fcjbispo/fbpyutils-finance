import pytest
import os
from fbpyutils_finance.bovespa import StockHistory

def test_stock_history_init_default_folder():
    stock_history = StockHistory()
    assert stock_history.download_folder == os.path.expanduser('~')

def test_stock_history_init_custom_folder():
    custom_folder = './custom_download_folder'
    os.makedirs(custom_folder, exist_ok=True) # Create directory
    try:
        stock_history = StockHistory(download_folder=custom_folder)
        assert stock_history.download_folder == custom_folder
    finally:
        os.rmdir(custom_folder) # Remove directory after test

def test_stock_history_init_invalid_path_not_exists():
    invalid_path = './non_existent_folder'
    with pytest.raises(OSError) as excinfo:
        StockHistory(download_folder=invalid_path)
    assert str(excinfo.value) == 'Path doesn\'t exists.'

def test_stock_history_init_invalid_path_not_directory():
    invalid_path = './tests/bovespa/test_bovespa_stock_history_init.py' # Use current test file as invalid dir
    with pytest.raises(OSError) as excinfo:
        StockHistory(download_folder=invalid_path)
    assert str(excinfo.value) == 'Path is not a folder.'

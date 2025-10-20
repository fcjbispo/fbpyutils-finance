import os
import pytest
import requests
from unittest.mock import patch, MagicMock, mock_open

from fbpyutils_finance.bovespa import StockHistory, _bvmf_cert

# Use a temporary directory for tests
@pytest.fixture
def temp_download_folder(tmp_path):
    """Creates a temporary download folder for testing."""
    folder = tmp_path / "bovespa_downloads_download"
    folder.mkdir()
    return str(folder)

# Fixture for a StockHistory instance
@pytest.fixture
def stock_history_instance(temp_download_folder):
    """Provides a StockHistory instance with a temporary download folder."""
    return StockHistory(download_folder=temp_download_folder)

# Test cases for _download_stock_history method
# ============================================

@patch('requests.get')
def test_download_stock_history_success(mock_requests_get, stock_history_instance, temp_download_folder):
    """
    Test _download_stock_history successfully downloads and saves a file.
    """
    period = 'A'
    period_data = '2023'
    test_url = 'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2023.ZIP'
    test_filename = 'COTAHIST_A2023.ZIP'
    expected_filepath = os.path.join(temp_download_folder, test_filename)
    dummy_content = b'dummy zip content'

    # Configure the mock response for requests.get
    mock_response = MagicMock()
    mock_response.iter_content.return_value = [dummy_content]
    mock_response.raise_for_status.return_value = None # Simulate successful status
    mock_requests_get.return_value = mock_response

    # Mock _build_paths to return controlled values
    with patch.object(StockHistory, '_build_paths', return_value=(test_url, expected_filepath)) as mock_build:
        # Mock built-in open to check file writing without actual disk I/O if preferred,
        # but writing to tmp_path is often simpler and more integrated.
        # We will let it write to tmp_path.

        # Call the method under test
        result_filepath = stock_history_instance._download_stock_history(period, period_data)

        # Assertions
        mock_build.assert_called_once_with(period, period_data)
        mock_requests_get.assert_called_once_with(test_url, stream=True, verify=_bvmf_cert)
        mock_response.iter_content.assert_called_once_with(1024**3) # Check block size

        assert result_filepath == expected_filepath
        assert os.path.exists(expected_filepath)

        # Verify the content of the written file
        with open(expected_filepath, 'rb') as f:
            content = f.read()
        assert content == dummy_content


@patch('requests.get')
def test_download_stock_history_request_exception(mock_requests_get, stock_history_instance):
    """
    Test _download_stock_history raises RequestException on download failure.
    """
    period = 'M'
    period_data = '012024'
    test_url = 'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_M012024.ZIP'
    test_filename = 'COTAHIST_M012024.ZIP'
    expected_filepath = os.path.join(stock_history_instance.download_folder, test_filename)

    # Configure requests.get mock to raise an exception
    mock_requests_get.side_effect = requests.exceptions.RequestException("Download failed")

    # Mock _build_paths
    with patch.object(StockHistory, '_build_paths', return_value=(test_url, expected_filepath)):
        # Call the method and assert the exception
        with pytest.raises(requests.exceptions.RequestException, match="Download failed"):
            stock_history_instance._download_stock_history(period, period_data)

        # Ensure the file was not created
        assert not os.path.exists(expected_filepath)


@patch('requests.get')
@patch('builtins.open', new_callable=mock_open) # Mock open to simulate write error
def test_download_stock_history_write_error(mock_file_open, mock_requests_get, stock_history_instance):
    """
    Test _download_stock_history handles file write errors (simulated).
    """
    period = 'D'
    period_data = '15032024'
    test_url = 'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_D15032024.ZIP'
    test_filename = 'COTAHIST_D15032024.ZIP'
    expected_filepath = os.path.join(stock_history_instance.download_folder, test_filename)
    dummy_content = b'dummy data'

    # Configure requests.get mock for success
    mock_response = MagicMock()
    mock_response.iter_content.return_value = [dummy_content]
    mock_response.raise_for_status.return_value = None
    mock_requests_get.return_value = mock_response

    # Configure mock_open to raise an OSError on write
    mock_file_open.side_effect = OSError("Permission denied")

    # Mock _build_paths
    with patch.object(StockHistory, '_build_paths', return_value=(test_url, expected_filepath)):
        # Call the method and assert the exception
        with pytest.raises(OSError, match="Permission denied"):
            stock_history_instance._download_stock_history(period, period_data)

        # Assert open was called
        mock_file_open.assert_called_once_with(expected_filepath, "wb")


# Test invalid period/date handling (delegated to _build_paths)
def test_download_stock_history_invalid_period(stock_history_instance):
    """
    Test _download_stock_history raises ValueError for invalid period via _build_paths.
    """
    with pytest.raises(ValueError, match='Invalid period. User A, M or D.'):
        stock_history_instance._download_stock_history(period='X', period_data='2023')

def test_download_stock_history_invalid_date(stock_history_instance):
    """
    Test _download_stock_history raises ValueError for invalid date via _build_paths.
    """
    with pytest.raises(ValueError, match="Invalid date format or value: 2023-01"):
        stock_history_instance._download_stock_history(period='A', period_data='2023-01')

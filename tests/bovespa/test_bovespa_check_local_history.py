import os
import pytest
import zipfile  # To create a dummy zip file
from pathlib import Path

from fbpyutils_finance.bovespa import StockHistory
import fbpyutils.file as F # Import the specific module used

# Use a temporary directory for tests
@pytest.fixture
def temp_download_folder(tmp_path):
    """Creates a temporary download folder for testing."""
    folder = tmp_path / "bovespa_downloads_check"
    folder.mkdir()
    return str(folder)

# Fixture to create a dummy valid zip file
@pytest.fixture
def dummy_zip_file(temp_download_folder):
    """Creates a dummy empty zip file for testing."""
    file_path = Path(temp_download_folder) / "COTAHIST_A2023.ZIP"
    with zipfile.ZipFile(file_path, 'w') as zf:
        # Add a dummy file inside zip if needed, otherwise empty is fine for mime check
        zf.writestr("dummy.txt", "dummy content")
    return str(file_path)

# Fixture to create a dummy non-zip file
@pytest.fixture
def dummy_txt_file(temp_download_folder):
    """Creates a dummy text file for testing."""
    file_path = Path(temp_download_folder) / "COTAHIST_M012023.ZIP" # Name it like a zip, but content is text
    file_path.write_text("This is not a zip file.")
    return str(file_path)

# Fixture to create a dummy directory with a zip-like name
@pytest.fixture
def dummy_directory(temp_download_folder):
    """Creates a dummy directory for testing."""
    dir_path = Path(temp_download_folder) / "COTAHIST_D01012023.ZIP" # Name it like a zip
    dir_path.mkdir()
    return str(dir_path)


# Test cases for _check_local_history method
# ==========================================

def test_check_local_history_file_exists_and_is_zip(temp_download_folder, dummy_zip_file, mocker):
    """
    Test _check_local_history returns True when a valid zip file exists locally.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    period = 'A'
    period_data = '2023'
    expected_filename = "COTAHIST_A2023.ZIP"
    expected_filepath = dummy_zip_file # Use the fixture path

    # Mock _build_paths to return the path of our dummy zip file
    mocker.patch.object(StockHistory, '_build_paths', return_value=('dummy_url', expected_filepath))

    # Mock F.mime_type to return 'application/zip' for our dummy file
    # Although creating a real zip should make the actual mime_type call work
    # mocker.patch('fbpyutils.file.mime_type', return_value='application/zip')

    assert stock_history._check_local_history(period, period_data) is True
    StockHistory._build_paths.assert_called_once_with(period, period_data)
    # F.mime_type.assert_called_once_with(expected_filepath) # Check if mime_type was called

def test_check_local_history_file_exists_not_zip(temp_download_folder, dummy_txt_file, mocker):
    """
    Test _check_local_history returns False when the file exists but is not a zip.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    period = 'M'
    period_data = '012023'
    expected_filepath = dummy_txt_file # Use the fixture path

    # Mock _build_paths
    mocker.patch.object(StockHistory, '_build_paths', return_value=('dummy_url', expected_filepath))

    # Mock F.mime_type to return something else
    mocker.patch('fbpyutils.file.mime_type', return_value='text/plain')

    assert stock_history._check_local_history(period, period_data) is False
    StockHistory._build_paths.assert_called_once_with(period, period_data)
    F.mime_type.assert_called_once_with(expected_filepath)

def test_check_local_history_path_is_directory(temp_download_folder, dummy_directory, mocker):
    """
    Test _check_local_history returns False when the path points to a directory.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    period = 'D'
    period_data = '01012023'
    expected_filepath = dummy_directory # Use the fixture path

    # Mock _build_paths
    mocker.patch.object(StockHistory, '_build_paths', return_value=('dummy_url', expected_filepath))

    # mime_type shouldn't be called if os.path.isfile is false
    # mocker.patch('fbpyutils.file.mime_type')

    assert stock_history._check_local_history(period, period_data) is False
    StockHistory._build_paths.assert_called_once_with(period, period_data)
    # F.mime_type.assert_not_called()

def test_check_local_history_file_does_not_exist(temp_download_folder, mocker):
    """
    Test _check_local_history returns False when the file does not exist.
    """
    stock_history = StockHistory(download_folder=temp_download_folder)
    period = 'A'
    period_data = '2025'
    non_existent_filepath = os.path.join(temp_download_folder, "COTAHIST_A2025.ZIP")

    # Mock _build_paths
    mocker.patch.object(StockHistory, '_build_paths', return_value=('dummy_url', non_existent_filepath))

    # mime_type shouldn't be called if os.path.exists is false
    # mocker.patch('fbpyutils.file.mime_type')

    assert stock_history._check_local_history(period, period_data) is False
    StockHistory._build_paths.assert_called_once_with(period, period_data)
    # F.mime_type.assert_not_called()

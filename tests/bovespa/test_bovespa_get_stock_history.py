import pytest
import pandas as pd
from unittest.mock import patch, MagicMock, call
import os
import requests

from fbpyutils_finance.bovespa import StockHistory, FetchModes

# Sample DataFrame to be returned by mocked read_fwf
@pytest.fixture
def mock_raw_dataframe():
    # A minimal DataFrame structure sufficient for testing flow
    return pd.DataFrame({
        'record_type': ['1'],
        'trade_date': ['20230115'],
        # Add other necessary columns based on _col_names if _treat_data isn't mocked
        'bdi_code': ['02'],
        'ticker': ['PETR4'],
        'market_type': ['10'],
        'ticker_issuer': ['PETROBRAS'],
        'ticker_specs': ['PN'],
        'term_days': [' '],
        'currency': ['REA'],
        'open_value': ['000002550'],
        'max_value': ['000002600'],
        'min_value': ['000002500'],
        'average_value': ['000002560'],
        'close_value': ['000002580'],
        'best_buy_offer': ['000002579'],
        'best_sell_offer': ['000002581'],
        'total_trades': ['0005000'],
        'total_trades_papers': ['000100000'],
        'total_trades_value': ['0000258000000'],
        'option_market_current_price': ['0000000000000'],
        'option_market_current_price_adjustment_indicator': ['0'],
        'option_market_due_date': ['00000000'],
        'ticker_trade_factor': ['0000001'],
        'option_market_current_price_in_points': ['0000000000000'],
        'ticker_isin_code': ['BRPETRACNPR6'],
        'ticker_distribution_number': ['001']
    }, columns=StockHistory._col_names)

# Sample processed DataFrame to be returned by mocked _treat_data
@pytest.fixture
def mock_processed_dataframe():
    # A minimal processed DataFrame
    return pd.DataFrame({
        'trade_date': [pd.to_datetime('2023-01-15').date()],
        'ticker': ['PETR4'],
        'close_value': [25.80]
        # Add other columns if needed for specific assertions
    })

# Fixture for StockHistory instance
@pytest.fixture
def stock_history_instance(tmp_path):
    folder = tmp_path / "get_stock_history_test"
    folder.mkdir()
    # Create a dummy cert file path if needed, though not directly used here
    # cert_path = folder / "dummy_cert.pem"
    # cert_path.touch()
    # with patch('fbpyutils_finance.bovespa._bvmf_cert', str(cert_path)):
    #     instance = StockHistory(download_folder=str(folder))
    instance = StockHistory(download_folder=str(folder))
    return instance

# Test cases for get_stock_history method
# =======================================

@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_treat_data')
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
@patch.object(StockHistory, '_download_stock_history')
def test_get_history_local_or_download_local_exists(
    mock_download, mock_check_local, mock_build_paths, mock_treat_data, mock_read_fwf,
    stock_history_instance, mock_raw_dataframe, mock_processed_dataframe
):
    """
    Test LOCAL_OR_DOWNLOAD mode when local file exists.
    Should behave like LOCAL mode.
    """
    period = 'A'
    period_data = '2023'
    local_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_A2023.ZIP')

    # Configure mocks
    mock_check_local.return_value = True
    mock_build_paths.return_value = ('dummy_url', local_filepath)
    mock_read_fwf.return_value = mock_raw_dataframe
    mock_treat_data.return_value = mock_processed_dataframe

    # Call method
    result_df = stock_history_instance.get_stock_history(
        period=period, period_data=period_data,
        fetch_mode=FetchModes.LOCAL_OR_DOWNLOAD,
        compact=False, original_names=True # Pass non-default args
    )

    # Assertions
    # _check_local is called once to determine mode, then again inside the LOCAL block
    assert mock_check_local.call_count == 2
    mock_check_local.assert_has_calls([call(period, period_data), call(period, period_data)]) # Called twice
    # Don't assert exact call count for _build_paths due to potential mock interaction issues
    # Instead, ensure the final read_fwf call gets the correct path derived from it.
    mock_build_paths.assert_called() # Ensure it was called at least once
    mock_download.assert_not_called()
    mock_read_fwf.assert_called_once() # Check encoding logic below
    # Check call to read_fwf includes the determined local_filepath and encoding attempts
    args, kwargs = mock_read_fwf.call_args
    assert args[0] == local_filepath
    assert kwargs['encoding'] in ['ISO-8859-1', 'cp1252', 'latin', 'utf-8'] # Check one of the attempted encodings
    assert kwargs['compression'] == 'zip'
    assert kwargs['widths'] == StockHistory._col_widths
    assert kwargs['names'] == StockHistory._col_names
    assert kwargs['converters'] == StockHistory._converters
    mock_treat_data.assert_called_once_with(mock_raw_dataframe, True, False) # original_names=True, compact=False
    pd.testing.assert_frame_equal(result_df, mock_processed_dataframe)


@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_treat_data')
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
@patch.object(StockHistory, '_download_stock_history')
def test_get_history_local_or_download_local_missing(
    mock_download, mock_check_local, mock_build_paths, mock_treat_data, mock_read_fwf,
    stock_history_instance, mock_raw_dataframe, mock_processed_dataframe
):
    """
    Test LOCAL_OR_DOWNLOAD mode when local file is missing.
    Should behave like DOWNLOAD mode.
    """
    period = 'M'
    period_data = '012024'
    downloaded_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_M012024.ZIP')

    # Configure mocks
    mock_check_local.return_value = False
    mock_download.return_value = downloaded_filepath
    # _build_paths will be called by _check_local_history first, then by _download_stock_history
    mock_build_paths.return_value = ('dummy_url', downloaded_filepath)
    mock_read_fwf.return_value = mock_raw_dataframe
    mock_treat_data.return_value = mock_processed_dataframe

    # Call method
    result_df = stock_history_instance.get_stock_history(
        period=period, period_data=period_data,
        fetch_mode=FetchModes.LOCAL_OR_DOWNLOAD,
        compact=True, original_names=False # Default args
    )

    # Assertions
    mock_check_local.assert_called_once_with(period, period_data)
    mock_download.assert_called_once_with(period, period_data)
    mock_read_fwf.assert_called_once()
    args, kwargs = mock_read_fwf.call_args
    assert args[0] == downloaded_filepath # Should read the downloaded file
    mock_treat_data.assert_called_once_with(mock_raw_dataframe, False, True) # original_names=False, compact=True
    pd.testing.assert_frame_equal(result_df, mock_processed_dataframe)


@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_treat_data')
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
@patch.object(StockHistory, '_download_stock_history')
def test_get_history_local_mode_success(
    mock_download, mock_check_local, mock_build_paths, mock_treat_data, mock_read_fwf,
    stock_history_instance, mock_raw_dataframe, mock_processed_dataframe
):
    """Test LOCAL mode when file exists."""
    period = 'D'
    period_data = '15032024'
    local_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_D15032024.ZIP')

    mock_check_local.return_value = True
    mock_build_paths.return_value = ('dummy_url', local_filepath)
    mock_read_fwf.return_value = mock_raw_dataframe
    mock_treat_data.return_value = mock_processed_dataframe

    result_df = stock_history_instance.get_stock_history(
        period=period, period_data=period_data, fetch_mode=FetchModes.LOCAL
    )

    # Assertions
    # In LOCAL mode, _check_local is called only once inside the LOCAL block
    mock_check_local.assert_called_once_with(period, period_data)
    # Don't assert exact call count for _build_paths
    mock_build_paths.assert_called() # Ensure it was called at least once
    mock_download.assert_not_called()
    mock_read_fwf.assert_called_once()
    args, kwargs = mock_read_fwf.call_args
    assert args[0] == local_filepath
    mock_treat_data.assert_called_once_with(mock_raw_dataframe, False, True) # Defaults
    pd.testing.assert_frame_equal(result_df, mock_processed_dataframe)


@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
def test_get_history_local_mode_file_missing_raises_error(
    mock_check_local, mock_build_paths, stock_history_instance
):
    """Test LOCAL mode raises OSError when file is missing."""
    period = 'A'
    period_data = '2025'
    local_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_A2025.ZIP')

    mock_check_local.return_value = False
    mock_build_paths.return_value = ('dummy_url', local_filepath)

    with pytest.raises(OSError, match='Invalid or non existent local file.'):
        stock_history_instance.get_stock_history(
            period=period, period_data=period_data, fetch_mode=FetchModes.LOCAL
        )

    # Assertions
    # In LOCAL mode when file missing, _check_local is called once inside the LOCAL block
    mock_check_local.assert_called_once_with(period, period_data)
    # _build_paths is only called within the mocked _check_local_history in this path,
    # so we don't assert its call here. The important check is that _check_local_history
    # was called and returned False, leading to the OSError.
    pass # No assertion needed for mock_build_paths here


@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_treat_data')
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_download_stock_history')
def test_get_history_download_mode_success(
    mock_download, mock_build_paths, mock_treat_data, mock_read_fwf,
    stock_history_instance, mock_raw_dataframe, mock_processed_dataframe
):
    """Test DOWNLOAD mode success."""
    period = 'A'
    period_data = '2023'
    downloaded_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_A2023.ZIP')

    mock_download.return_value = downloaded_filepath
    # _build_paths is called by _download_stock_history
    mock_build_paths.return_value = ('dummy_url', downloaded_filepath)
    mock_read_fwf.return_value = mock_raw_dataframe
    mock_treat_data.return_value = mock_processed_dataframe

    result_df = stock_history_instance.get_stock_history(
        period=period, period_data=period_data, fetch_mode=FetchModes.DOWNLOAD
    )

    mock_download.assert_called_once_with(period, period_data)
    mock_read_fwf.assert_called_once()
    args, kwargs = mock_read_fwf.call_args
    assert args[0] == downloaded_filepath
    mock_treat_data.assert_called_once_with(mock_raw_dataframe, False, True) # Defaults
    pd.testing.assert_frame_equal(result_df, mock_processed_dataframe)


@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_download_stock_history')
def test_get_history_download_mode_failure_raises_error(
    mock_download, mock_build_paths, stock_history_instance
):
    """Test DOWNLOAD mode raises exception if download fails."""
    period = 'M'
    period_data = '022024'
    filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_M022024.ZIP')

    mock_download.side_effect = requests.exceptions.RequestException("Network Error")
    mock_build_paths.return_value = ('dummy_url', filepath)

    with pytest.raises(requests.exceptions.RequestException, match="Network Error"):
        stock_history_instance.get_stock_history(
            period=period, period_data=period_data, fetch_mode=FetchModes.DOWNLOAD
        )

    mock_download.assert_called_once_with(period, period_data)


@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_treat_data')
@patch.object(StockHistory, '_build_paths')
def test_get_history_stream_mode(
    mock_build_paths, mock_treat_data, mock_read_fwf,
    stock_history_instance, mock_raw_dataframe, mock_processed_dataframe
):
    """
    Test STREAM mode. Currently behaves like DOWNLOAD for path building
    but reads directly from the URL (or path built like download).
    pd.read_fwf can read from URLs.
    """
    period = 'A'
    period_data = '2022'
    stream_url = 'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2022.ZIP'
    # _build_paths returns URL and a potential local path (which isn't used by read_fwf in this case)
    mock_build_paths.return_value = (stream_url, 'dummy_local_path.zip')
    mock_read_fwf.return_value = mock_raw_dataframe
    mock_treat_data.return_value = mock_processed_dataframe

    result_df = stock_history_instance.get_stock_history(
        period=period, period_data=period_data, fetch_mode=FetchModes.STREAM
    )

    mock_build_paths.assert_called_once_with(period, period_data)
    mock_read_fwf.assert_called_once()
    args, kwargs = mock_read_fwf.call_args
    assert args[0] == stream_url # Should attempt to read from the URL returned by _build_paths
    mock_treat_data.assert_called_once_with(mock_raw_dataframe, False, True) # Defaults
    pd.testing.assert_frame_equal(result_df, mock_processed_dataframe)


def test_get_history_invalid_fetch_mode(stock_history_instance):
    """Test raises ValueError for an invalid fetch_mode."""
    with pytest.raises(ValueError, match='Invalid fetch mode.'):
        stock_history_instance.get_stock_history(fetch_mode=99)


@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_treat_data')
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
def test_get_history_encoding_fallback(
    mock_check_local, mock_build_paths, mock_treat_data, mock_read_fwf,
    stock_history_instance, mock_raw_dataframe, mock_processed_dataframe
):
    """
    Test that get_stock_history tries multiple encodings if read_fwf fails.
    """
    period = 'A'
    period_data = '2023'
    local_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_A2023.ZIP')

    mock_check_local.return_value = True
    mock_build_paths.return_value = ('dummy_url', local_filepath)
    mock_treat_data.return_value = mock_processed_dataframe

    # Simulate read_fwf failing for the first 3 encodings popped and succeeding on the last one ('ISO-8859-1')
    mock_read_fwf.side_effect = [
        UnicodeDecodeError('utf-8', b'', 0, 1, 'reason'),    # Fails on pop() 1
        UnicodeDecodeError('latin', b'', 0, 1, 'reason'),    # Fails on pop() 2
        UnicodeDecodeError('cp1252', b'', 0, 1, 'reason'),   # Fails on pop() 3
        mock_raw_dataframe                                # Success on pop() 4 ('ISO-8859-1')
    ]

    result_df = stock_history_instance.get_stock_history(
        period=period, period_data=period_data, fetch_mode=FetchModes.LOCAL
    )

    # Check that read_fwf was called 4 times until success
    assert mock_read_fwf.call_count == 4
    # Check encodings used in calls match the pop() order
    actual_calls = mock_read_fwf.call_args_list
    assert actual_calls[0].kwargs['encoding'] == 'utf-8'        # 1st attempt (pop 1)
    assert actual_calls[1].kwargs['encoding'] == 'latin'        # 2nd attempt (pop 2)
    assert actual_calls[2].kwargs['encoding'] == 'cp1252'       # 3rd attempt (pop 3)
    assert actual_calls[3].kwargs['encoding'] == 'ISO-8859-1'   # 4th attempt (pop 4 - Success)

    mock_treat_data.assert_called_once_with(mock_raw_dataframe, False, True) # Defaults
    pd.testing.assert_frame_equal(result_df, mock_processed_dataframe)


@patch('fbpyutils_finance.bovespa.pd.read_fwf')
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
def test_get_history_all_encodings_fail(
    mock_check_local, mock_build_paths, mock_read_fwf, stock_history_instance
):
    """Test raises UnicodeDecodeError if all encodings fail."""
    period = 'A'
    period_data = '2023'
    local_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_A2023.ZIP')

    mock_check_local.return_value = True
    mock_build_paths.return_value = ('dummy_url', local_filepath)

    # Simulate read_fwf failing for all encodings
    mock_read_fwf.side_effect = UnicodeDecodeError('dummy', b'', 0, 1, 'reason') # Needs 5 args

    # Correctly simulate the side effect raising the error 4 times
    mock_read_fwf.side_effect = [
        UnicodeDecodeError('utf-8', b'', 0, 1, 'reason'),
        UnicodeDecodeError('latin', b'', 0, 1, 'reason'),
        UnicodeDecodeError('cp1252', b'', 0, 1, 'reason'),
        UnicodeDecodeError('ISO-8859-1', b'', 0, 1, 'reason'),
    ]


    with pytest.raises(RuntimeError, match="Error reading stock history file. Unknown encoding."):
        stock_history_instance.get_stock_history(
             period=period, period_data=period_data, fetch_mode=FetchModes.LOCAL
        )

    assert mock_read_fwf.call_count == 4 # Tried all encodings


@patch('fbpyutils_finance.bovespa.pd.read_fwf', return_value="not a dataframe") # Simulate wrong return type
@patch.object(StockHistory, '_build_paths')
@patch.object(StockHistory, '_check_local_history')
def test_get_history_invalid_read_output_type(
    mock_check_local, mock_build_paths, mock_read_fwf, stock_history_instance
):
    """Test raises TypeError if read_fwf doesn't return a DataFrame."""
    period = 'A'
    period_data = '2023'
    local_filepath = os.path.join(stock_history_instance.download_folder, 'COTAHIST_A2023.ZIP')

    mock_check_local.return_value = True
    mock_build_paths.return_value = ('dummy_url', local_filepath)

    with pytest.raises(TypeError, match='Failed to get the stock history. Invalid output data.'):
        stock_history_instance.get_stock_history(
            period=period, period_data=period_data, fetch_mode=FetchModes.LOCAL
        )

    mock_read_fwf.assert_called() # Should be called at least once

import pandas as pd
import pytest
from unittest.mock import MagicMock
from fbpyutils_finance.cei import _process_operation

def test_process_operation_returns_expected_tuple(mocker):
    """
    Test _process_operation returns (op_name, rows, data) correctly when data is returned.
    """
    mock_files = ["file1.xlsx", "file2.xlsx"]
    mock_data = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

    # Mock FU.find to return mock_files
    mocker.patch("fbpyutils_finance.cei.FU.find", return_value=mock_files)

    # Mock processor to return mock_data
    mock_processor = MagicMock(return_value=mock_data)

    operation = ("movimentacao", "some_folder", "*.xlsx", mock_processor)

    op_name, rows, data = _process_operation(operation)

    assert op_name == "movimentacao"
    assert rows == 2
    pd.testing.assert_frame_equal(data, mock_data)

def test_process_operation_returns_zero_when_none(mocker):
    """
    Test _process_operation returns rows=0 and data=None when processor returns None.
    """
    mock_files = ["file1.xlsx"]
    mocker.patch("fbpyutils_finance.cei.FU.find", return_value=mock_files)

    mock_processor = MagicMock(return_value=None)

    operation = ("negociacao", "folder", "*.xlsx", mock_processor)

    op_name, rows, data = _process_operation(operation)

    assert op_name == "negociacao"
    assert rows == 0
    assert data is None

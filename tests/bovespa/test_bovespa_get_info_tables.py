import pytest
import os
from unittest.mock import patch, mock_open
import pandas as pd
from fbpyutils_finance.bovespa import StockHistory, FI

def test_get_info_tables_success():
    # Mock successful excel read
    mock_excel_data = {
        'bdi_codes': [['Code', 'Description'], ['02', 'DESC 02']],
        'market_types': [['Type', 'Description'], ['10', 'DESC 10']]
    }
    
    def mock_read_sheet(sheet_name):
        return mock_excel_data[sheet_name]

    with patch('fbpyutils.xlsx.get_sheet_names', return_value=list(mock_excel_data.keys())):  # Mock get_sheet_names function
        with patch('fbpyutils.xlsx.ExcelWorkbook.read_sheet', side_effect=mock_read_sheet): # Mock read_sheet method of ExcelWorkbook
            result = StockHistory.get_info_tables()
            assert result['status'] == 'OK'
            assert isinstance(result['tables'], dict)
            assert isinstance(result['tables']['bdi_codes'], pd.DataFrame)
            assert 'code' in result['tables']['bdi_codes'].columns
            assert 'description' in result['tables']['bdi_codes'].columns
            assert not result['message'] == ''

def test_get_info_tables_file_not_found():
    # Mock file not found error
    with patch('fbpyutils.xlsx.ExcelWorkbook', side_effect=FileNotFoundError("No such file or directory")):
        result = StockHistory.get_info_tables()
        assert result['status'] == 'ERROR'
        assert 'tables' not in result
        assert not result['message'] == ''

def test_introspect_excelworkbook():
    import fbpyutils.xlsx as XL
    print(dir(XL.ExcelWorkbook))
    assert True # Dummy assertion to make pytest run the test

def test_get_info_tables_empty_sheets():
    # Mock excel with empty sheets
    mock_excel_data = {
        'empty_sheet': []
    }
    def mock_read_sheet(sheet_name):
        return mock_excel_data[sheet_name]

    with patch('fbpyutils.xlsx.get_sheet_names', return_value=mock_excel_data.keys()): # Mock get_sheet_names
        with patch('fbpyutils.xlsx.ExcelWorkbook.read_sheet', side_effect=mock_read_sheet): # Mock read_sheet
            result = StockHistory.get_info_tables()
            assert result['status'] == 'OK'
            assert isinstance(result['tables'], dict)
            assert isinstance(result['tables']['empty_sheet'], pd.DataFrame)
            assert result['tables']['empty_sheet'].empty
            assert not result['message'] == ''

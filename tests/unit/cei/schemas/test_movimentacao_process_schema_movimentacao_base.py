import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.movimentacao import process_schema_movimentacao

def test_process_schema_movimentacao_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_movimentacao([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_movimentacao_invalid_file_skipped(monkeypatch):
    """Test that non-movimentacao files are skipped gracefully."""
    with mock.patch('fbpyutils_finance.cei.schemas.movimentacao.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_movimentacao', pd.Timestamp('2020-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.read_sheet_by_index.return_value = []
            result = process_schema_movimentacao(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_movimentacao_valid_file(monkeypatch):
    """Test processing a valid movimentacao file with minimal data."""
    dummy_data = [
        ['Entrada/Saída', 'Data', 'Movimentação', 'Produto', 'Instituição', 'Conta', 'Quantidade', 'Preço unitário', 'Valor da Operação'],
        ['Entrada', '01/01/2025', 'Compra', 'ABC123', 'Broker', '123456', '100', '10.5', '1050']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.movimentacao.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('movimentacao', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.read_sheet_by_index.return_value = dummy_data
            result = process_schema_movimentacao(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'nome_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['preco_unitario'] == 10.5
            assert result.iloc[0]['valor_operacao'] == 1050

import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.eventos_provisionados import process_schema_eventos_provisionados

def test_process_schema_eventos_provisionados_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_eventos_provisionados([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_eventos_provisionados_invalid_file_skipped(monkeypatch):
    """Test that invalid or non-eventos files are skipped gracefully."""
    # Mock extract_file_info to return a non-eventos filename
    with mock.patch('fbpyutils_finance.cei.schemas.eventos_provisionados.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_eventos', pd.Timestamp('2020-01-01').date())
        # Mock ExcelWorkbook to avoid file IO
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.read_sheet_by_index.return_value = []
            result = process_schema_eventos_provisionados(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_eventos_provisionados_valid_file(monkeypatch):
    """Test processing a valid eventos file with minimal data."""
    dummy_data = [
        ['Produto', 'Tipo', 'Tipo de Evento', 'Previsão de pagamento', 'Instituição', 'Conta', 'Quantidade', 'Preço unitário', 'Valor líquido'],
        ['ABC123', 'Ação', 'Dividendo', '01/01/2025', 'Broker', '123456', '100', '10.5', '1050']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.eventos_provisionados.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('eventos', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.read_sheet_by_index.return_value = dummy_data
            result = process_schema_eventos_provisionados(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'nome_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['preco_unitario'] == 10.5
            assert result.iloc[0]['valor_operacao'] == 1050

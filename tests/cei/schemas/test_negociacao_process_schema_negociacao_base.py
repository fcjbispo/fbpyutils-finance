import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.negociacao import process_schema_negociacao

def test_process_schema_negociacao_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_negociacao([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_negociacao_invalid_file_skipped(monkeypatch):
    """Test that non-negociacao files are skipped gracefully."""
    with mock.patch('fbpyutils_finance.cei.schemas.negociacao.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_negociacao', pd.Timestamp('2020-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.read_sheet_by_index.return_value = []
            result = process_schema_negociacao(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_negociacao_valid_file(monkeypatch):
    """Test processing a valid negociacao file with minimal data."""
    dummy_data = [
        ['Data do Negócio', 'Tipo de Movimentação', 'Mercado', 'Prazo/Vencimento', 'Instituição', 'Conta', 'Código de Negociação', 'Quantidade', 'Preço', 'Valor'],
        ['01/01/2025', 'Compra', 'Bovespa', '01/12/2025', 'Broker', '123456', 'XYZW4', '100', '10.5', '1050']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.negociacao.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('negociacao', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.read_sheet_by_index.return_value = dummy_data
            result = process_schema_negociacao(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'codigo_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['preco_unitario'] == 10.5
            assert result.iloc[0]['valor_operacao'] == 1050

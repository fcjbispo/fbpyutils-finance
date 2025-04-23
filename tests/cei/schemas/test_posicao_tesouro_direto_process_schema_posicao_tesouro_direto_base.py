import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.posicao_tesouro_direto import process_schema_posicao_tesouro_direto

def test_process_schema_posicao_tesouro_direto_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_posicao_tesouro_direto([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_posicao_tesouro_direto_invalid_file_skipped(monkeypatch):
    """Test that non-posicao files are skipped gracefully."""
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_tesouro_direto.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_posicao', pd.Timestamp('2020-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = []
            result = process_schema_posicao_tesouro_direto(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_posicao_tesouro_direto_valid_sheet(monkeypatch):
    """Test processing a posicao file with a valid 'Tesouro Direto' sheet."""
    dummy_data = [
        ['Produto', 'Instituição', 'Conta', 'Código ISIN', 'Indexador', 'Vencimento', 'Quantidade', 'Quantidade Disponível', 'Quantidade Indisponível', 'Motivo', 'Valor Aplicado', 'Valor bruto', 'Valor líquido', 'Valor Atualizado'],
        ['Tesouro Selic 2025', 'Broker', '123456', 'BRSTN1234567', 'SELIC', '01/01/2025', '100', '80', '20', '', '1000', '1050', '1030', '1100']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_tesouro_direto.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('posicao', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = ['Tesouro Direto']
            mock_excel.return_value.read_sheet.return_value = dummy_data
            result = process_schema_posicao_tesouro_direto(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'codigo_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['valor_aplicado'] == 1000
            assert result.iloc[0]['valor_bruto'] == 1050
            assert result.iloc[0]['valor_liquido'] == 1030
            assert result.iloc[0]['valor_atualizado'] == 1100

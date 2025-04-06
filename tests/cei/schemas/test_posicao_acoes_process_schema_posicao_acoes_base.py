import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.posicao_acoes import process_schema_posicao_acoes

def test_process_schema_posicao_acoes_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_posicao_acoes([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_posicao_acoes_invalid_file_skipped(monkeypatch):
    """Test that non-posicao files are skipped gracefully."""
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_acoes.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_posicao', pd.Timestamp('2020-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = []
            result = process_schema_posicao_acoes(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_posicao_acoes_valid_sheet(monkeypatch):
    """Test processing a posicao file with a valid 'Ações' sheet."""
    dummy_data = [
        ['Código de Negociação', 'Produto', 'Instituição', 'Conta', 'Código ISIN / Distribuição', 'Tipo', 'Escriturador', 'Quantidade', 'Quantidade Disponível', 'Quantidade Indisponível', 'Motivo', 'Preço de Fechamento', 'Valor Atualizado'],
        ['XYZW4', 'Empresa XYZ', 'Broker', '123456', 'BRXYZ1234567', 'Ação', 'EscrituradorX', '100', '80', '20', '', '10.5', '1050']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_acoes.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('posicao', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = ['Ações']
            mock_excel.return_value.read_sheet.return_value = dummy_data
            result = process_schema_posicao_acoes(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'codigo_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['preco_unitario'] == 10.5
            assert result.iloc[0]['valor_operacao'] == 1050

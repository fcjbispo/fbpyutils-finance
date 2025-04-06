import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.posicao_renda_fixa import process_schema_posicao_renda_fixa

def test_process_schema_posicao_renda_fixa_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_posicao_renda_fixa([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_posicao_renda_fixa_invalid_file_skipped(monkeypatch):
    """Test that non-posicao files are skipped gracefully."""
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_renda_fixa.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_posicao', pd.Timestamp('2020-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = []
            result = process_schema_posicao_renda_fixa(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_posicao_renda_fixa_valid_sheet(monkeypatch):
    """Test processing a posicao file with a valid 'Renda Fixa' sheet."""
    dummy_data = [
        ['Código', 'Produto', 'Instituição', 'Conta', 'Emissor', 'Indexador', 'Tipo de regime', 'Data de Emissão', 'Vencimento', 'Quantidade', 'Quantidade Disponível', 'Quantidade Indisponível', 'Motivo', 'Contraparte', 'Preço Atualizado MTM', 'Valor Atualizado MTM', 'Preço Atualizado CURVA', 'Valor Atualizado CURVA'],
        ['XYZ123', 'Renda Fixa XYZ', 'Broker', '123456', 'EmissorX', 'CDI', 'Prefixado', '01/01/2020', '01/01/2030', '100', '80', '20', '', 'ContraparteX', '10.5', '1050', '10.0', '1000']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_renda_fixa.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('posicao', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = ['Renda Fixa']
            mock_excel.return_value.read_sheet.return_value = dummy_data
            result = process_schema_posicao_renda_fixa(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'codigo_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['preco_atualizado_mtm'] == 10.5
            assert result.iloc[0]['valor_atualizado_mtm'] == 1050
            assert result.iloc[0]['preco_atualizado_curva'] == 10.0
            assert result.iloc[0]['valor_atualizado_curva'] == 1000

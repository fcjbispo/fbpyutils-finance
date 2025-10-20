import tempfile
import os
import pandas as pd
import pytest
from unittest import mock
from fbpyutils_finance.cei.schemas.posicao_emprestimo_ativos import process_schema_posicao_emprestimo_ativos

def test_process_schema_posicao_emprestimo_ativos_empty_list_returns_empty_df():
    """Test that passing an empty list returns an empty DataFrame."""
    result = process_schema_posicao_emprestimo_ativos([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_schema_posicao_emprestimo_ativos_invalid_file_skipped(monkeypatch):
    """Test that non-posicao files are skipped gracefully."""
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_emprestimo_ativos.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('not_posicao', pd.Timestamp('2020-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = []
            result = process_schema_posicao_emprestimo_ativos(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert result.empty

def test_process_schema_posicao_emprestimo_ativos_valid_sheet(monkeypatch):
    """Test processing a posicao file with a valid 'Empréstimo de Ativos' sheet."""
    dummy_data = [
        ['Produto', 'Instituição', 'Conta', 'Natureza', 'Número de Contrato', 'Modalidade', 'OPA', 'Liquidação antecipada', 'Taxa', 'Comissão', 'Data de registro', 'Data de vencimento', 'Quantidade', 'Preço de Fechamento', 'Valor Atualizado'],
        ['Empresa XYZ', 'Broker', '123456', 'NaturezaX', 'C123', 'ModalidadeX', 'OPA1', 'Não', '1.5', '0.5', '01/01/2025', '01/12/2025', '100', '10.5', '1050']
    ]
    with mock.patch('fbpyutils_finance.cei.schemas.posicao_emprestimo_ativos.extract_file_info') as mock_extract_info:
        mock_extract_info.return_value = ('posicao', pd.Timestamp('2025-01-01').date())
        with mock.patch('fbpyutils.xlsx.ExcelWorkbook') as mock_excel:
            mock_excel.return_value.sheet_names = ['Empréstimo de Ativos']
            mock_excel.return_value.read_sheet.return_value = dummy_data
            result = process_schema_posicao_emprestimo_ativos(['dummy.xlsx'])
            assert isinstance(result, pd.DataFrame)
            assert not result.empty
            assert 'nome_produto' in result.columns
            assert 'quantidade' in result.columns
            assert result.iloc[0]['quantidade'] == 100
            assert result.iloc[0]['preco_unitario'] == 10.5
            assert result.iloc[0]['valor_operacao'] == 1050

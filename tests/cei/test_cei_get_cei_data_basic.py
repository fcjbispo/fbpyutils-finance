import pandas as pd
import pytest
from unittest.mock import MagicMock
from fbpyutils_finance.cei import get_cei_data

@pytest.fixture(autouse=True)
def mock_all_dependencies(mocker):
    """
    Fixture to mock FU.find and all schema processors.
    """
    # Mock FU.find to always return a list of fake files
    mocker.patch("fbpyutils_finance.cei.FU.find", return_value=["file1.xlsx", "file2.xlsx"])

    # Mock all schema processors to return a simple DataFrame
    df = pd.DataFrame({"x": [1], "y": [2]})
    processors = [
        "process_schema_movimentacao",
        "process_schema_eventos_provisionados",
        "process_schema_negociacao",
        "process_schema_posicao_acoes",
        "process_schema_posicao_emprestimo_ativos",
        "process_schema_posicao_etf",
        "process_schema_posicao_fundos_investimento",
        "process_schema_posicao_tesouro_direto",
        "process_schema_posicao_renda_fixa",
    ]
    for proc_name in processors:
        mocker.patch(f"fbpyutils_finance.cei.{proc_name}", return_value=df)
    # Patch local references imported directly in __init__.py
    mocker.patch("fbpyutils_finance.cei.process_schema_movimentacao", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_eventos_provisionados", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_negociacao", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_posicao_acoes", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_posicao_emprestimo_ativos", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_posicao_etf", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_posicao_fundos_investimento", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_posicao_tesouro_direto", return_value=df)
    mocker.patch("fbpyutils_finance.cei.process_schema_posicao_renda_fixa", return_value=df)

def test_get_cei_data_sequential(mocker):
    """
    Test get_cei_data returns expected list of tuples when parallelize=False.
    """
    fake_results = [
        ("movimentacao", 1, pd.DataFrame({"x": [1]})),
        ("negociacao", 2, pd.DataFrame({"y": [2, 3]})),
    ]
    # Mock _process_operation to return fake results for each call
    mocker.patch("fbpyutils_finance.cei._process_operation", side_effect=fake_results * 5)

    results = get_cei_data("some_folder", parallelize=False)

    assert isinstance(results, list)
    # Since _OPERATIONS has 9 enabled operations
    assert len(results) == 9
    for item in results:
        op_name, rows, data = item
        assert isinstance(op_name, str)
        assert isinstance(rows, int)
        assert isinstance(data, pd.DataFrame)

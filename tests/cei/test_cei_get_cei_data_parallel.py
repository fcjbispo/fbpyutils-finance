import pandas as pd
import pytest
from unittest.mock import MagicMock
from fbpyutils_finance.cei import get_cei_data

def test_get_cei_data_parallelized(mocker):
    """
    Test get_cei_data with parallelize=True uses multiprocessing and returns expected data.
    """
    fake_results = [
        ("movimentacao", 1, pd.DataFrame({"a": [1]})),
        ("negociacao", 2, pd.DataFrame({"b": [2, 3]})),
    ]

    # Mock Pool context manager and its map method
    mock_pool = mocker.MagicMock()
    mock_pool.__enter__.return_value.map.return_value = fake_results
    mocker.patch("fbpyutils_finance.cei.Pool", return_value=mock_pool)

    # Also mock os.cpu_count to be >1 to enable parallelism
    mocker.patch("fbpyutils_finance.cei.os.cpu_count", return_value=4)

    # Mock FU.find to avoid filesystem access
    mocker.patch("fbpyutils_finance.cei.FU.find", return_value=["file.xlsx"])

    # Mock all schema processors to avoid real processing
    for proc_name in [
        "process_schema_movimentacao",
        "process_schema_eventos_provisionados",
        "process_schema_negociacao",
        "process_schema_posicao_acoes",
        "process_schema_posicao_emprestimo_ativos",
        "process_schema_posicao_etf",
        "process_schema_posicao_fundos_investimento",
        "process_schema_posicao_tesouro_direto",
        "process_schema_posicao_renda_fixa",
    ]:
        mocker.patch(f"fbpyutils_finance.cei.schemas.{proc_name}", return_value=pd.DataFrame())

    results = get_cei_data("folder", parallelize=True)

    assert results == fake_results

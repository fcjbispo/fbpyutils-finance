import os
# Removed unused imports: re, sqlite3, datetime from datetime, XL from fbpyutils
import os
import pandas as pd
from multiprocessing import Pool
import warnings
from typing import List, Tuple, Callable, Any, Optional # Added imports

from fbpyutils import file as FU

from fbpyutils_finance.cei.schemas import \
    process_schema_movimentacao, process_schema_eventos_provisionados, process_schema_negociacao, \
    process_schema_posicao_acoes, process_schema_posicao_emprestimo_ativos, process_schema_posicao_etf, \
    process_schema_posicao_fundos_investimento, process_schema_posicao_tesouro_direto, \
    process_schema_posicao_renda_fixa

warnings.simplefilter("ignore")

_OPERATIONS = (
    ('movimentacao', 'movimentacao-*.xlsx', process_schema_movimentacao, True),
    ('eventos_provisionados', 'eventos-*.xlsx', process_schema_eventos_provisionados, True),
    ('negociacao', 'negociacao-*.xlsx', process_schema_negociacao, True),
    ('posicao_acoes', 'posicao-*.xlsx', process_schema_posicao_acoes, True),
    ('posicao_emprestimo_ativos', 'posicao-*.xlsx', process_schema_posicao_emprestimo_ativos, True),
    ('posicao_etf', 'posicao-*.xlsx', process_schema_posicao_etf, True),
    ('posicao_fundos_investimento', 'posicao-*.xlsx', process_schema_posicao_fundos_investimento, True),
    ('posicao_tesouro_direto', 'posicao-*.xlsx', process_schema_posicao_tesouro_direto, True),
    ('posicao_renda_fixa', 'posicao-*.xlsx', process_schema_posicao_renda_fixa, True),
)


def _process_operation(operation: Tuple[str, str, str, Callable]) -> Tuple[str, int, Optional[pd.DataFrame]]:
    """
    Processes a single CEI data operation type.

    Finds files matching a pattern, applies a specific processing function (schema processor),
    and returns the results.

    Args:
        operation (Tuple[str, str, str, Callable]): A tuple containing:
            - op_name (str): The name of the operation (e.g., 'movimentacao').
            - input_folder (str): The folder containing the CEI Excel files.
            - input_mask (str): The file pattern to search for (e.g., 'movimentacao-*.xlsx').
            - processor (Callable): The function responsible for processing the found files
                                     (expected to return a DataFrame or None).

    Returns:
        Tuple[str, int, Optional[pd.DataFrame]]: A tuple containing:
            - op_name (str): The name of the operation.
            - rows (int): The number of rows in the processed DataFrame (0 if None).
            - data (Optional[pd.DataFrame]): The processed data as a DataFrame, or None if processing fails or yields no data.
    """
    op_name, input_folder, input_mask, processor = operation
    input_files = FU.find(input_folder, input_mask)
    data = processor(input_files)

    rows = 0 if data is None else len(data)

    return (op_name, rows, data)


def get_cei_data(input_folder: str, parallelize: bool = True) -> List[Tuple[str, int, Optional[pd.DataFrame]]]:
    """
    Retrieves and processes various types of CEI data from Excel files in a specified folder.

    It iterates through predefined operations (_OPERATIONS), finds corresponding
    Excel files (e.g., 'movimentacao-*.xlsx'), and uses specific schema processors
    to parse and consolidate the data into DataFrames. Processing can be parallelized.

    Args:
        input_folder (str): The path to the directory containing the CEI Excel files.
        parallelize (bool, optional): If True, uses multiprocessing to process
                                      different operation types in parallel. Defaults to True.

    Returns:
        List[Tuple[str, int, Optional[pd.DataFrame]]]: A list of tuples, where each tuple
            represents the result of one operation type, containing:
            - op_name (str): The name of the operation (e.g., 'movimentacao').
            - rows (int): The number of rows in the processed DataFrame (0 if None).
            - data (Optional[pd.DataFrame]): The processed data as a DataFrame, or None.
    """
    PARALLELIZE = parallelize and os.cpu_count()>1
    operations = []

    for op, mask, processor, enabled in _OPERATIONS:
        if enabled: 
            operations.append((op, input_folder, mask, processor,))
    
    operations = tuple(operations)
    
    if PARALLELIZE:
        with Pool(os.cpu_count()) as p:
            data = p.map(_process_operation, operations)
    else:
        data = []
        for operation in operations:
            data.append(_process_operation(operation))
    
    return data

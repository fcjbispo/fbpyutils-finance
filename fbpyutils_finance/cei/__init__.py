import os
import re
import sqlite3
import pandas as pd

from datetime import datetime
from multiprocessing import Pool

import warnings

from fbpyutils import file as FU, xlsx as XL

from fbpyutils_finance.cei.schemas import \
    process_schema_movimentacao, process_schema_eventos_provisionados, process_schema_negociacao, \
    process_schema_posicao_acoes, process_schema_posicao_emprestimo_ativos, process_schema_posicao_etf, \
    process_schema_posicao_fundos_investimento, process_schema_posicao_tesouro_direto, \
    process_schema_posicao_renda_fixa

warnings.simplefilter("ignore")

_OPERATIONS = (
    ('movimentacao', 'movimentacao-*.xlsx', process_schema_movimentacao, True),
    ('eventos_provisionados', 'eventos-provisionados-*.xlsx', process_schema_eventos_provisionados, True),
    ('negociacao', 'negociacao-*.xlsx', process_schema_negociacao, True),
    ('posicao_acoes', 'posicao-*.xlsx', process_schema_posicao_acoes, True),
    ('posicao_emprestimo_ativos', 'posicao-*.xlsx', process_schema_posicao_emprestimo_ativos, True),
    ('posicao_etf', 'posicao-*.xlsx', process_schema_posicao_etf, True),
    ('posicao_fundos_investimento', 'posicao-*.xlsx', process_schema_posicao_fundos_investimento, True),
    ('posicao_tesouro_direto', 'posicao-*.xlsx', process_schema_posicao_tesouro_direto, True),
    ('posicao_renda_fixa', 'posicao-*.xlsx', process_schema_posicao_renda_fixa, True),
)

_POS_OPERATIONS = (
{
    'operation': 'produtos', 
    'sql': '''
        select distinct
            codigo_produto,
            nome_produto,
            tipo_produto
        from (
        select distinct
            codigo_produto, 
            nome_produto,
            'FII' as tipo_produto 
        from tb_stg_posicao_fundos_investimento
        union
        select distinct
            codigo_produto, 
            nome_produto,
            'Ações' as tipo_produto
        from tb_stg_posicao_acoes
        where tipo_produto not in ('Recibo', 'Direito')
        union
        select distinct
            codigo_produto, 
            nome_produto,
            'ETF' as tipo_produto
        from tb_stg_posicao_etf
        union
        select distinct
            codigo_produto, 
            nome_produto,
            'Renda Fixa' as tipo_produto
        from tb_stg_posicao_renda_fixa
        union
        select distinct
            codigo_produto, 
            nome_produto,
            'Tesouro Direto' as tipo_produto
        from tb_stg_posicao_tesouro_direto
        union
        select distinct
            codigo_produto, 
            nome_produto,
            'Ações' as tipo_produto
        from tb_stg_posicao_emprestimo_ativos
        )
        order by 1, 2;
    ''',
    'params': {},
},
{
    'operation': 'calendario', 
    'sql': '''
        SELECT codigo_produto,
            instituicao,
            conta,
            SUBSTR(data_referencia, 1, 7)       as periodo, 
            max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
            max(arquivo_origem)                 as arquivo_origem 
        from tb_stg_posicao_tesouro_direto
        GROUP BY codigo_produto,
                conta, 
                SUBSTR(data_referencia, 1, 10)
        UNION
        SELECT codigo_produto,
            instituicao,
            conta,
            SUBSTR(data_referencia, 1, 7)       as periodo, 
            max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
            max(arquivo_origem)                 as arquivo_origem 
        from tb_stg_posicao_renda_fixa
        GROUP BY codigo_produto, 
                conta,
                SUBSTR(data_referencia, 1, 10)
        UNION
        SELECT codigo_produto,
            instituicao,
            conta,
            SUBSTR(data_referencia, 1, 7)       as periodo, 
            max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
            max(arquivo_origem)                 as arquivo_origem 
        from tb_stg_posicao_emprestimo_ativos
        GROUP BY codigo_produto, 
                conta,
                SUBSTR(data_referencia, 1, 10)
        UNION
        SELECT codigo_produto,
            instituicao,
            conta,
            SUBSTR(data_referencia, 1, 7)       as periodo, 
            max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
            max(arquivo_origem)                 as arquivo_origem 
        from tb_stg_posicao_acoes
        GROUP BY codigo_produto, 
                conta,
                SUBSTR(data_referencia, 1, 10)
        UNION
        SELECT codigo_produto, 
            instituicao,
            conta,
            SUBSTR(data_referencia, 1, 7)       as periodo, 
            max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
            max(arquivo_origem)                 as arquivo_origem 
        from tb_stg_posicao_fundos_investimento
        GROUP BY codigo_produto, 
                instituicao,
                conta,
                SUBSTR(data_referencia, 1, 7)
        UNION
        SELECT codigo_produto, 
            instituicao,
            conta,
            SUBSTR(data_referencia, 1, 7)       as periodo, 
            max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
            max(arquivo_origem)                 as arquivo_origem 
        from tb_stg_posicao_etf
        GROUP BY codigo_produto, 
                instituicao,
                conta,
                SUBSTR(data_referencia, 1, 7)
        ;
    ''',
    'params': {},
},
)


def _process_operation(operation):
    """
    Process the specified operation.
     Args:
        operation (tuple): A tuple containing the details of the operation to be processed.
            - op_name (str): The name of the operation.
            - input_folder (str): The path to the folder containing the input files.
            - input_mask (str): The mask or pattern for finding input files.
            - processor (function): The function to be applied to the input files.
     Returns:
        tuple: A tuple containing the result of the operation.
            - op_name (str): The name of the operation.
            - num_files (int): The number of input files processed.
            - data (any): The processed data.
     Overview:
        This function processes the specified operation by performing the following steps:
        1. Extract the operation details from the input tuple.
        2. Use the `FU.find` function to find input files in the specified input folder using the input mask.
        3. Apply the specified `processor` function to the input files to obtain the processed data.
        4. Return a tuple containing the operation name, the number of input files processed, and the processed data.
     Example usage:
        operation = ('op_name', '/path/to/input_folder', '*.txt', process_function)
        result = _process_operation(operation)
    """
    op_name, input_folder, input_mask, processor = operation
    input_files = FU.find(input_folder, input_mask)
    data = processor(input_files)

    return (op_name, len(data), data)


def _get_cei_data_pre(input_folder, parallelize=True):
    """
    Retrieves CEI data from the specified input folder and processes it based on the specified operations.
     Args:
        input_folder (str): The path to the folder containing the CEI data.
        parallelize (bool, optional): Flag indicating whether to parallelize the data processing. Defaults to True.
     Returns:
        list: A list containing the processed data.
            Each item in the list represents the result of processing an operation and consists of:
            - operation (str): The name of the operation performed.
            - data (any): The processed data.
     Overview:
        This function retrieves CEI data from the specified input folder and processes it based on the operations defined in `_OPERATIONS`.
        The `parallelize` parameter controls whether the data processing is parallelized.
        The function first checks if parallelization is enabled by comparing the value of `parallelize` with the number of available CPUs.
        It then initializes an empty list to store the results of the data processing.
        If parallelization is enabled, the function uses a multiprocessing pool to concurrently process the data using the `_process_operation` function.
        Otherwise, it sequentially processes the data by iterating over the operations and calling `_process_operation` for each operation.
        The results of the data processing are appended to the data list.
        Finally, the function returns the list containing the processed data.
     Example usage:
        data = _get_cei_data_pre(input_folder='/path/to/cei_data', parallelize=True)
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


def _get_cei_data_pos(input_folder, parallelize=True):
    """
    Retrieves CEI data with position operations from the specified input folder.
     Args:
        input_folder (str): The path to the folder containing the CEI data.
        parallelize (bool, optional): Flag indicating whether to parallelize the data retrieval. Defaults to True.
     Returns:
        tuple: A tuple containing the results of the data retrieval operation.
            Each item in the tuple represents a result and consists of:
            - operation (str): The name of the operation performed.
            - length (int): The length of the retrieved data.
            - data (pandas.DataFrame): The retrieved data.
     Overview:
        This function retrieves CEI data from the specified input folder and performs position operations on the data.
        The `parallelize` parameter controls whether the data retrieval operation is parallelized.
        The function first calls `_get_cei_data_pre` to retrieve the CEI data.
        It then creates an in-memory SQLite database and stores the retrieved data in separate tables based on the operation.
        Next, it executes position operations by reading SQL queries from `_POS_OPERATIONS` and retrieving data from the database.
        The results of the position operations are stored in a list.
        Finally, the function combines the results of the position operations with the original CEI data and returns a tuple containing all the results.
     Example usage:
        results = _get_cei_data_pos(input_folder='/path/to/cei_data', parallelize=True)
    """
    cei_data = _get_cei_data_pre(input_folder, parallelize=parallelize)

    db = sqlite3.connect(':memory:')

    try:
        for operation, _, data in cei_data:
            table_name = f'tb_stg_{operation}'
            data.to_sql(table_name, con=db, if_exists='replace', index=False)

        results = []
        for pos_oper in _POS_OPERATIONS:
            data = pd.read_sql(
                pos_oper['sql'],
                params=pos_oper.get('params', {}), 
                con=db
            )

            results.append((pos_oper['operation'], len(data), data))
        
        for operation, length, data in cei_data:
            results.append((operation, length, data))

        return tuple(results)
    finally:
        db.close()
        db = None


def get_cei_data(input_folder, parallelize=True, with_pos_operations=True):
    """
    Retrieves CEI data from the specified input folder.
     Args:
        input_folder (str): The path to the folder containing the CEI data.
        parallelize (bool, optional): Flag indicating whether to parallelize the data retrieval. Defaults to True.
        with_pos_operations (bool, optional): Flag indicating whether to include position operations. Defaults to True.
     Returns:
        object: The result of the data retrieval operation.
     Overview:
        This function retrieves CEI data from the specified input folder.
        The function determines the appropriate operation to use based on the value of the `with_pos_operations` parameter.
        If `with_pos_operations` is True, it calls the `_get_cei_data_pos` function to retrieve the data.
        If `with_pos_operations` is False, it calls the `_get_cei_data_pre` function to retrieve the data.
        The `parallelize` parameter controls whether the data retrieval operation is parallelized.
        The function returns the result of the data retrieval operation.
     Example usage:
        cei_data = get_cei_data(input_folder='/path/to/cei_data', parallelize=True, with_pos_operations=True)
    """
    operation = _get_cei_data_pos \
        if with_pos_operations else _get_cei_data_pre
    
    return operation(input_folder, parallelize)

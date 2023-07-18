import os
import sqlite3
import pandas as pd

from datetime import datetime
from multiprocessing import Pool

import warnings
warnings.simplefilter("ignore")

from fbpyutils import file as FU, xlsx as XL

import re


_deal_dashes = lambda x: None if x in ['-'] else x
_str_to_date = lambda x: None if x in ['-'] else datetime.strptime(x, '%d/%m/%Y').date()
_str_to_number = lambda x: None if x in ['-'] else float(str(x).replace(',','.'))
_tuple_as_str = lambda x: [[str(c).strip() for c in l] for l in x]

import os
import sqlite3
import pandas as pd

from datetime import datetime
from multiprocessing import Pool

import warnings
warnings.simplefilter("ignore")

from fbpyutils import file as FU, xlsx as XL


_deal_dashes = lambda x: None if x in ['-'] else x
_str_to_date = lambda x: None if x in ['-'] else datetime.strptime(x, '%d/%m/%Y').date()
_str_to_number = lambda x: None if x in ['-'] else float(str(x).replace(',','.'))
_tuple_as_str = lambda x: [[str(c).strip() for c in l] for l in x]


def _deal_double_spaces(x):
    """
    Replaces consecutive double spaces in a string with a single space.

    Args:
        x (str): The string to be processed.

    Returns:
        str: The processed string with consecutive double spaces replaced by a single space.
    """
    x, ss, s = str(x), '  ', ' ' 
    while ss in x:
        x = x.replace(ss, s)
    return x


def _extract_file_info_old(schema_file):
    schema_file_name = schema_file.split(os.path.sep)[-1]
    schema_file_name_part, _ = schema_file_name.split('.')
    schema_file_date = datetime.strptime('-'.join(schema_file_name_part.split('-')[-6:]), '%Y-%m-%d-%H-%M-%S')
    return schema_file_name, schema_file_date


def _extract_file_info(schema_file):
    """
    Extracts information from a CEI file name, including the type of file and the date it was created.

    Args:
        schema_file (str): The path to the schema file to be processed.

    Returns:
        Tuple[str, datetime]: A tuple containing the CEI file type (as a string) and the date the file was created (as a datetime object).

    Raises:
        ValueError: If the file name is invalid.
    """
    cei_file_name = schema_file.split(os.path.sep)[-1].split('.')[0]

    match = re.search(r"\b\d{4}\b", cei_file_name)
    if match:
        cei_file_type = cei_file_name[0:match.start()-1]
        cei_file_date = cei_file_name[match.start():]

        if '-a-' in cei_file_date:
            cei_file_date = cei_file_date.split('-a-')[-1]

        if len(cei_file_date) == 10:
            cei_file_date = datetime.strptime(cei_file_date, '%Y-%m-%d')
        elif len(cei_file_date) == 19:
            cei_file_date = datetime.strptime(cei_file_date, '%Y-%m-%d-%H-%M-%S')
        else:
            raise ValueError(f'Nome de arquivo invalido: {cei_file_name}')

        return cei_file_type, cei_file_date
    else:
        raise ValueError(f'Nome de arquivo invalido: {cei_file_name}')


def _extract_product_id(product, sep='-'):
    if 'Tesouro' in product:
        return product
    product_parts = product.split(sep)
    
    return product_parts[
        1 if 'Futuro' in product_parts[0] else 0
    ].strip()


def _process_schema_movimentacao(input_files):
    xl_dataframes = []
    fields = [
        'entrada_saida',
        'data_movimentacao',
        'movimentacao',
        'nome_produto',
        'codigo_produto',
        'instituicao',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))
        xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

        xl_dataframe['entrada_saida'] = xl_dataframe['Entrada/Saída']
        xl_dataframe['data_movimentacao'] = xl_dataframe['Data'].apply(_str_to_date)
        xl_dataframe['movimentacao'] = xl_dataframe['Movimentação']
        xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
        xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(_extract_product_id)
        xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço unitário'].apply(_str_to_number)
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor da Operação'].apply(_str_to_number)
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_eventos_provisionados(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'tipo_produto',
        'tipo_evento',
        'previsao_pagamento',
        'instituicao',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))
        xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

        xl_dataframe = xl_dataframe[xl_dataframe['Preço unitário'] != 'Total líquido'].copy()

        xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
        xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(_extract_product_id)
        xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
        xl_dataframe['tipo_evento'] = xl_dataframe['Tipo de Evento']
        xl_dataframe['previsao_pagamento'] = xl_dataframe['Previsão de pagamento'].apply(_str_to_date)
        xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço unitário'].apply(_str_to_number)
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor líquido'].apply(_str_to_number)
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_negociacao(input_files):
    xl_dataframes = []
    fields = [
        'data_negocio',
        'movimentacao',
        'mercado',
        'prazo_vencimento',
        'instituicao',
        'codigo_produto',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))
        xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

        xl_dataframe['data_negocio'] = xl_dataframe['Data do Negócio'].apply(_str_to_date)
        xl_dataframe['movimentacao'] = xl_dataframe['Tipo de Movimentação']
        xl_dataframe['mercado'] = xl_dataframe['Mercado']
        xl_dataframe['prazo_vencimento'] = xl_dataframe['Prazo/Vencimento'].apply(_str_to_date)
        xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
        xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação']
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço'].apply(_str_to_number)
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor'].apply(_str_to_number)
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_acoes(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'tipo_produto',
        'escriturador',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheets = ['Ações', 'Acoes']
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        for xl_sheet in xl_sheets:
            if xl_sheet in xl_obj.sheet_names:
                xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
                xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

                xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

                xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação'].apply(_deal_double_spaces)
                xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
                xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
                xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
                xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
                xl_dataframe['escriturador'] = xl_dataframe['Escriturador'].apply(_deal_double_spaces)
                xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
                xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
                xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
                xl_dataframe['motivo'] = xl_dataframe['Motivo']
                xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
                xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
                xl_dataframe['arquivo_origem'] = schema_file_name
                xl_dataframe['data_referencia'] = schema_file_date

                xl_dataframe = xl_dataframe[fields].copy()

                xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_emprestimo_ativos(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'natureza',
        'contrato',
        'modalidade',
        'opa',
        'liquidacao_antecipada',
        'taxa',
        'comissao',
        'data_registro',
        'data_vencimento',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheets = ['Empréstimo de Ativos', 'Empréstimos']
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        for xl_sheet in xl_sheets:
            if xl_sheet in xl_obj.sheet_names:
                xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
                xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

                xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

                xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
                xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(_extract_product_id)
                xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
                xl_dataframe['natureza'] = xl_dataframe['Natureza'].apply(_deal_double_spaces)
                xl_dataframe['contrato'] = xl_dataframe['Número de Contrato'].apply(_deal_double_spaces)
                xl_dataframe['modalidade'] = xl_dataframe['Modalidade'].apply(_deal_double_spaces)
                xl_dataframe['opa'] = xl_dataframe['OPA'].apply(_deal_double_spaces)
                xl_dataframe['liquidacao_antecipada'] = xl_dataframe['Liquidação antecipada'].apply(_deal_double_spaces)
                xl_dataframe['taxa'] = xl_dataframe['Taxa'].apply(_str_to_number)
                xl_dataframe['comissao'] = xl_dataframe['Comissão'].apply(_str_to_number)
                xl_dataframe['data_registro'] = xl_dataframe['Data de registro'].apply(_str_to_date)
                xl_dataframe['data_vencimento'] = xl_dataframe['Data de vencimento'].apply(_str_to_date)
                xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
                xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
                xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
                xl_dataframe['arquivo_origem'] = schema_file_name
                xl_dataframe['data_referencia'] = schema_file_date

                xl_dataframe = xl_dataframe[fields].copy()

                xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_etf(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'tipo_produto',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'ETF'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
            xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
            xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_fundos_investimento(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'tipo_produto',
        'administrador',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'Fundo de Investimento'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
            xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
            xl_dataframe['administrador'] = xl_dataframe['Administrador'].apply(_deal_double_spaces)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
            xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_tesouro_direto(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'indexador',
        'vencimento',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'valor_aplicado',
        'valor_bruto',
        'valor_liquido',
        'valor_atualizado',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'Tesouro Direto'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN']
            xl_dataframe['indexador'] = xl_dataframe['Indexador']
            xl_dataframe['vencimento'] = xl_dataframe['Vencimento'].apply(_str_to_date)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['valor_aplicado'] = xl_dataframe['Valor Aplicado'].apply(_str_to_number)
            xl_dataframe['valor_bruto'] = xl_dataframe['Valor bruto'].apply(_str_to_number)
            xl_dataframe['valor_liquido'] = xl_dataframe['Valor líquido'].apply(_str_to_number)
            xl_dataframe['valor_atualizado'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_renda_fixa(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'emissor',
        'indexador',
        'tipo_regime',
        'emissao',
        'vencimento',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'contraparte',
        'preco_atualizado_mtm',
        'valor_atualizado_mtm',
        'preco_atualizado_curva',
        'valor_atualizado_curva',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'Renda Fixa'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Código'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['emissor'] = xl_dataframe['Emissor'].apply(_deal_double_spaces)
            xl_dataframe['indexador'] = xl_dataframe['Indexador'].apply(_deal_double_spaces)
            xl_dataframe['tipo_regime'] = xl_dataframe['Tipo de regime']
            xl_dataframe['emissao'] = xl_dataframe['Data de Emissão'].apply(_str_to_date)
            xl_dataframe['vencimento'] = xl_dataframe['Vencimento'].apply(_str_to_date)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['contraparte'] = xl_dataframe['Contraparte']
            xl_dataframe['preco_atualizado_mtm'] = xl_dataframe['Preço Atualizado MTM'].apply(_str_to_number)
            xl_dataframe['valor_atualizado_mtm'] = xl_dataframe['Valor Atualizado MTM'].apply(_str_to_number)
            xl_dataframe['preco_atualizado_curva'] = xl_dataframe['Preço Atualizado CURVA'].apply(_str_to_number)
            xl_dataframe['valor_atualizado_curva'] = xl_dataframe['Valor Atualizado CURVA'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


OPERATIONS = (
    ('movimentacao', 'movimentacao-*.xlsx', _process_schema_movimentacao, True),
    ('eventos_provisionados', 'eventos-provisionados-*.xlsx', _process_schema_eventos_provisionados, True),
    ('negociacao', 'negociacao-*.xlsx', _process_schema_negociacao, True),
    ('posicao_acoes', 'posicao-*.xlsx', _process_schema_posicao_acoes, True),
    ('posicao_emprestimo_ativos', 'posicao-*.xlsx', _process_schema_posicao_emprestimo_ativos, True),
    ('posicao_etf', 'posicao-*.xlsx', _process_schema_posicao_etf, True),
    ('posicao_fundos_investimento', 'posicao-*.xlsx', _process_schema_posicao_fundos_investimento, True),
    ('posicao_tesouro_direto', 'posicao-*.xlsx', _process_schema_posicao_tesouro_direto, True),
    ('posicao_renda_fixa', 'posicao-*.xlsx', _process_schema_posicao_renda_fixa, True),
)


def _process_operation(operation):
    op_name, input_folder, input_mask, processor = operation
    input_files = FU.find(input_folder, input_mask)
    data = processor(input_files)
    return (op_name, len(data), data)


def get_cei_data(input_folder, parallelize=True):
    PARALLELIZE = parallelize and os.cpu_count()>1

    operations = []
    for op, mask, processor, enabled in OPERATIONS:
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



if __name__ == '__main__':
    PARALLELIZE = os.cpu_count() > 1

    base_path = FU.build_platform_path('C:', '/mnt/c', [
        'Users', 'fcjbispo', 'Meu Drive', 'Finanças', 'Extratos & Faturas', 'CEI'])

    input_folder = os.path.sep.join([base_path, 'aa_input'])
    output_folder = os.path.sep.join([base_path, 'zz_output'])
    output_db = os.path.sep.join([output_folder, 'cei-data.db'])

    cei_data = get_cei_data(input_folder, parallelize=PARALLELIZE)

    db = sqlite3.connect(output_db)

    write_csv, sep_csv = True, '|'

    try:
        for operation, records, data in cei_data:
            table_name = f'tb_stg_{operation}'
            data.to_sql(table_name, con=db, if_exists='replace', index=False)

            print(f'{records} writen on table {table_name}.')

            if write_csv:
                csv_output_file = os.path.sep.join([
                    output_folder, table_name + '.csv'
                ])
                data.to_csv(csv_output_file, sep=sep_csv, header=True, index=False)
                
                print(f'Table writen to {csv_output_file} file.')

        for pos_oper in (
            {
                'table_name': 'tb_stg_produtos', 
                'sql': '''
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
                    order by 1, 2;
                ''',
                'params': {},
            },
            {
                'table_name': 'tb_stg_calendario', 
                'sql': '''
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_tesouro_direto
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_renda_fixa
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_emprestimo_ativos
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_acoes
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto, 
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_fundos_investimento
                    GROUP BY codigo_produto, 
                            instituicao,
                            SUBSTR(data_referencia, 1, 7)
                    UNION
                    SELECT codigo_produto, 
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_etf
                    GROUP BY codigo_produto, 
                            instituicao,
                            SUBSTR(data_referencia, 1, 7)
                    ;
                ''',
                'params': {},
            },
        ):
            table_data = pd.read_sql(
                pos_oper['sql'],
                params=pos_oper.get('params', {}), 
                con=db
            )

            table_data.to_sql(
                pos_oper['table_name'],
                con=db,
                if_exists='replace', 
                index=False
            )
            print(f'{len(table_data)} writen on table {pos_oper["table_name"]}.')

            if write_csv:
                csv_output_file = os.path.sep.join([
                    output_folder, pos_oper["table_name"] + '.csv'
                ])
                table_data.to_csv(csv_output_file, sep=sep_csv, header=True, index=False)
                print(f'Table writen to {csv_output_file} file.')
    finally:
        db.close()
def _deal_double_spaces(x):
    """
    Replaces consecutive double spaces in a string with a single space.

    Args:
        x (str): The string to be processed.

    Returns:
        str: The processed string with consecutive double spaces replaced by a single space.
    """
    x, ss, s = str(x), '  ', ' ' 
    while ss in x:
        x = x.replace(ss, s)
    return x


def _extract_file_info(schema_file):
    """
    Extracts information from a CEI file name, including the type of file and the date it was created.

    Args:
        schema_file (str): The path to the schema file to be processed.

    Returns:
        Tuple[str, datetime]: A tuple containing the CEI file type (as a string) and the date the file was created (as a datetime object).

    Raises:
        ValueError: If the file name is invalid.
    """
    cei_file_name = schema_file.split(os.path.sep)[-1].split('.')[0]

    match = re.search(r"\b\d{4}\b", cei_file_name)
    if match:
        cei_file_type = cei_file_name[0:match.start()-1]
        cei_file_date = cei_file_name[match.start():]

        if '-a-' in cei_file_date:
            cei_file_date = cei_file_date.split('-a-')[-1]

        if len(cei_file_date) == 10:
            cei_file_date = datetime.strptime(cei_file_date, '%Y-%m-%d')
        elif len(cei_file_date) == 19:
            cei_file_date = datetime.strptime(cei_file_date, '%Y-%m-%d-%H-%M-%S')
        else:
            raise ValueError(f'Nome de arquivo invalido: {cei_file_name}')

        return cei_file_type, cei_file_date
    else:
        raise ValueError(f'Nome de arquivo invalido: {cei_file_name}')


def _extract_product_id(product, sep='-'):
    if 'Tesouro' in product:
        return product
    product_parts = product.split(sep)
    
    return product_parts[
        1 if 'Futuro' in product_parts[0] else 0
    ].strip()


def _process_schema_movimentacao(input_files):
    xl_dataframes = []
    fields = [
        'entrada_saida',
        'data_movimentacao',
        'movimentacao',
        'nome_produto',
        'codigo_produto',
        'instituicao',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))
        xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

        xl_dataframe['entrada_saida'] = xl_dataframe['Entrada/Saída']
        xl_dataframe['data_movimentacao'] = xl_dataframe['Data'].apply(_str_to_date)
        xl_dataframe['movimentacao'] = xl_dataframe['Movimentação']
        xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
        xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(_extract_product_id)
        xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço unitário'].apply(_str_to_number)
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor da Operação'].apply(_str_to_number)
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_eventos_provisionados(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'tipo_produto',
        'tipo_evento',
        'previsao_pagamento',
        'instituicao',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))
        xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

        xl_dataframe = xl_dataframe[xl_dataframe['Preço unitário'] != 'Total líquido'].copy()

        xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
        xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(_extract_product_id)
        xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
        xl_dataframe['tipo_evento'] = xl_dataframe['Tipo de Evento']
        xl_dataframe['previsao_pagamento'] = xl_dataframe['Previsão de pagamento'].apply(_str_to_date)
        xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço unitário'].apply(_str_to_number)
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor líquido'].apply(_str_to_number)
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_negociacao(input_files):
    xl_dataframes = []
    fields = [
        'data_negocio',
        'movimentacao',
        'mercado',
        'prazo_vencimento',
        'instituicao',
        'codigo_produto',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))
        xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

        xl_dataframe['data_negocio'] = xl_dataframe['Data do Negócio'].apply(_str_to_date)
        xl_dataframe['movimentacao'] = xl_dataframe['Tipo de Movimentação']
        xl_dataframe['mercado'] = xl_dataframe['Mercado']
        xl_dataframe['prazo_vencimento'] = xl_dataframe['Prazo/Vencimento'].apply(_str_to_date)
        xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
        xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação']
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço'].apply(_str_to_number)
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor'].apply(_str_to_number)
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_acoes(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'tipo_produto',
        'escriturador',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheets = ['Ações', 'Acoes']
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        for xl_sheet in xl_sheets:
            if xl_sheet in xl_obj.sheet_names:
                xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
                xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

                xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

                xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação'].apply(_deal_double_spaces)
                xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
                xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
                xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
                xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
                xl_dataframe['escriturador'] = xl_dataframe['Escriturador'].apply(_deal_double_spaces)
                xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
                xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
                xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
                xl_dataframe['motivo'] = xl_dataframe['Motivo']
                xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
                xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
                xl_dataframe['arquivo_origem'] = schema_file_name
                xl_dataframe['data_referencia'] = schema_file_date

                xl_dataframe = xl_dataframe[fields].copy()

                xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_emprestimo_ativos(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'natureza',
        'contrato',
        'modalidade',
        'opa',
        'liquidacao_antecipada',
        'taxa',
        'comissao',
        'data_registro',
        'data_vencimento',
        'quantidade',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheets = ['Empréstimo de Ativos', 'Empréstimos']
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        for xl_sheet in xl_sheets:
            if xl_sheet in xl_obj.sheet_names:
                xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
                xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

                xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

                xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
                xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(_extract_product_id)
                xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
                xl_dataframe['natureza'] = xl_dataframe['Natureza'].apply(_deal_double_spaces)
                xl_dataframe['contrato'] = xl_dataframe['Número de Contrato'].apply(_deal_double_spaces)
                xl_dataframe['modalidade'] = xl_dataframe['Modalidade'].apply(_deal_double_spaces)
                xl_dataframe['opa'] = xl_dataframe['OPA'].apply(_deal_double_spaces)
                xl_dataframe['liquidacao_antecipada'] = xl_dataframe['Liquidação antecipada'].apply(_deal_double_spaces)
                xl_dataframe['taxa'] = xl_dataframe['Taxa'].apply(_str_to_number)
                xl_dataframe['comissao'] = xl_dataframe['Comissão'].apply(_str_to_number)
                xl_dataframe['data_registro'] = xl_dataframe['Data de registro'].apply(_str_to_date)
                xl_dataframe['data_vencimento'] = xl_dataframe['Data de vencimento'].apply(_str_to_date)
                xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
                xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
                xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
                xl_dataframe['arquivo_origem'] = schema_file_name
                xl_dataframe['data_referencia'] = schema_file_date

                xl_dataframe = xl_dataframe[fields].copy()

                xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_etf(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'tipo_produto',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'ETF'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
            xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
            xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_fundos_investimento(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'tipo_produto',
        'administrador',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'preco_unitario',
        'valor_operacao',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'Fundo de Investimento'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
            xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
            xl_dataframe['administrador'] = xl_dataframe['Administrador'].apply(_deal_double_spaces)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number)
            xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_tesouro_direto(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'codigo_isin',
        'indexador',
        'vencimento',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'valor_aplicado',
        'valor_bruto',
        'valor_liquido',
        'valor_atualizado',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'Tesouro Direto'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN']
            xl_dataframe['indexador'] = xl_dataframe['Indexador']
            xl_dataframe['vencimento'] = xl_dataframe['Vencimento'].apply(_str_to_date)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['valor_aplicado'] = xl_dataframe['Valor Aplicado'].apply(_str_to_number)
            xl_dataframe['valor_bruto'] = xl_dataframe['Valor bruto'].apply(_str_to_number)
            xl_dataframe['valor_liquido'] = xl_dataframe['Valor líquido'].apply(_str_to_number)
            xl_dataframe['valor_atualizado'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def _process_schema_posicao_renda_fixa(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'emissor',
        'indexador',
        'tipo_regime',
        'emissao',
        'vencimento',
        'quantidade',
        'quantidade_disponivel',
        'quantidade_indisponivel',
        'motivo',
        'contraparte',
        'preco_atualizado_mtm',
        'valor_atualizado_mtm',
        'preco_atualizado_curva',
        'valor_atualizado_curva',
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet = 'Renda Fixa'
    
    for schema_file in input_files:
        schema_file_name, schema_file_date = _extract_file_info(schema_file)

        xl_obj = XL.ExcelWorkbook(schema_file)
        if xl_sheet in xl_obj.sheet_names:
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))
            xl_dataframe = pd.DataFrame(xl_table[1:], columns=xl_table[0])

            xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()

            xl_dataframe['codigo_produto'] = xl_dataframe['Código'].apply(_deal_double_spaces)
            xl_dataframe['nome_produto'] = xl_dataframe['Produto'].apply(_deal_double_spaces)
            xl_dataframe['instituicao'] = xl_dataframe['Instituição'].apply(_deal_double_spaces)
            xl_dataframe['emissor'] = xl_dataframe['Emissor'].apply(_deal_double_spaces)
            xl_dataframe['indexador'] = xl_dataframe['Indexador'].apply(_deal_double_spaces)
            xl_dataframe['tipo_regime'] = xl_dataframe['Tipo de regime']
            xl_dataframe['emissao'] = xl_dataframe['Data de Emissão'].apply(_str_to_date)
            xl_dataframe['vencimento'] = xl_dataframe['Vencimento'].apply(_str_to_date)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number)
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number)
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number)
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['contraparte'] = xl_dataframe['Contraparte']
            xl_dataframe['preco_atualizado_mtm'] = xl_dataframe['Preço Atualizado MTM'].apply(_str_to_number)
            xl_dataframe['valor_atualizado_mtm'] = xl_dataframe['Valor Atualizado MTM'].apply(_str_to_number)
            xl_dataframe['preco_atualizado_curva'] = xl_dataframe['Preço Atualizado CURVA'].apply(_str_to_number)
            xl_dataframe['valor_atualizado_curva'] = xl_dataframe['Valor Atualizado CURVA'].apply(_str_to_number)
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


OPERATIONS = (
    ('movimentacao', 'movimentacao-*.xlsx', _process_schema_movimentacao, True),
    ('eventos_provisionados', 'eventos-provisionados-*.xlsx', _process_schema_eventos_provisionados, True),
    ('negociacao', 'negociacao-*.xlsx', _process_schema_negociacao, True),
    ('posicao_acoes', 'posicao-*.xlsx', _process_schema_posicao_acoes, True),
    ('posicao_emprestimo_ativos', 'posicao-*.xlsx', _process_schema_posicao_emprestimo_ativos, True),
    ('posicao_etf', 'posicao-*.xlsx', _process_schema_posicao_etf, True),
    ('posicao_fundos_investimento', 'posicao-*.xlsx', _process_schema_posicao_fundos_investimento, True),
    ('posicao_tesouro_direto', 'posicao-*.xlsx', _process_schema_posicao_tesouro_direto, True),
    ('posicao_renda_fixa', 'posicao-*.xlsx', _process_schema_posicao_renda_fixa, True),
)


def _process_operation(operation):
    op_name, input_folder, input_mask, processor = operation
    input_files = FU.find(input_folder, input_mask)
    data = processor(input_files)
    return (op_name, len(data), data)


def get_cei_data(input_folder, parallelize=True):
    PARALLELIZE = parallelize and os.cpu_count()>1

    operations = []
    for op, mask, processor, enabled in OPERATIONS:
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



if __name__ == '__main__':
    PARALLELIZE = os.cpu_count() > 1

    CEI_SOURCE_PATH = os.environ.get('CEI_SOURCE_PATH')
    CEI_DB_URL = os.environ.get('CEI_DB_URL')
    CEI_WRITE_CSV = bool(os.environ.get('CEI_WRITE_CSV', False))

    if not all([CEI_DB_URL, CEI_SOURCE_PATH]):
        raise ValueError('Missing environment variables CEI_SOURCE_PATH, CEI_DB_URL')

    base_path = CEI_SOURCE_PATH

    input_folder = os.path.sep.join([base_path, 'aa_input'])
    output_folder = os.path.sep.join([base_path, 'zz_output'])
    output_db = CEI_DB_URL

    cei_data = get_cei_data(input_folder, parallelize=PARALLELIZE)

    db = sqlite3.connect(output_db)

    write_csv, sep_csv = CEI_WRITE_CSV, '|'

    try:
        for operation, records, data in cei_data:
            table_name = f'tb_stg_{operation}'
            data.to_sql(table_name, con=db, if_exists='replace', index=False)

            print(f'{records} writen on table {table_name}.')

            if write_csv:
                csv_output_file = os.path.sep.join([
                    output_folder, table_name + '.csv'
                ])
                data.to_csv(csv_output_file, sep=sep_csv, header=True, index=False)
                
                print(f'Table writen to {csv_output_file} file.')

        for pos_oper in (
            {
                'table_name': 'tb_stg_produtos', 
                'sql': '''
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
                    order by 1, 2;
                ''',
                'params': {},
            },
            {
                'table_name': 'tb_stg_calendario', 
                'sql': '''
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_tesouro_direto
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_renda_fixa
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_emprestimo_ativos
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto,
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_acoes
                    GROUP BY codigo_produto, 
                            SUBSTR(data_referencia, 1, 10)
                    UNION
                    SELECT codigo_produto, 
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_fundos_investimento
                    GROUP BY codigo_produto, 
                            instituicao,
                            SUBSTR(data_referencia, 1, 7)
                    UNION
                    SELECT codigo_produto, 
                        instituicao,
                        SUBSTR(data_referencia, 1, 7)       as periodo, 
                        max(SUBSTR(data_referencia, 1, 10)) as data_referencia, 
                        max(arquivo_origem)                 as arquivo_origem 
                    from tb_stg_posicao_etf
                    GROUP BY codigo_produto, 
                            instituicao,
                            SUBSTR(data_referencia, 1, 7)
                    ;
                ''',
                'params': {},
            },
        ):
            table_data = pd.read_sql(
                pos_oper['sql'],
                params=pos_oper.get('params', {}), 
                con=db
            )

            table_data.to_sql(
                pos_oper['table_name'],
                con=db,
                if_exists='replace', 
                index=False
            )
            print(f'{len(table_data)} writen on table {pos_oper["table_name"]}.')

            if write_csv:
                csv_output_file = os.path.sep.join([
                    output_folder, pos_oper["table_name"] + '.csv'
                ])
                table_data.to_csv(csv_output_file, sep=sep_csv, header=True, index=False)
                print(f'Table writen to {csv_output_file} file.')
    finally:
        db.close()
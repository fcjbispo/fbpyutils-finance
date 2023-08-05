import os
import re
import pandas as pd

from datetime import datetime
from multiprocessing import Pool

import warnings

from fbpyutils import xlsx as XL, string as SU


warnings.simplefilter("ignore")

_str_to_date = lambda x: None if x in ['-'] else datetime.strptime(x, '%d/%m/%Y').date()

_str_to_number = lambda x: None if x in ['-'] else float(str(x).replace('.','~').replace(',','.').replace('~',''))

_str_to_integer = lambda x: int(_str_to_number(x))

_tuple_as_str = lambda x: [[str(c).strip() for c in l] for l in x]


def _deal_double_spaces(x):
    """
    Replaces consecutive double spaces in a string with a single space.
     Args:
        x (str): The string to be processed.
     Returns:
        str: The processed string with consecutive double spaces replaced by a single space.
     Overview:
        This function takes a string as input and replaces any consecutive double spaces with a single space.
        It first converts the input to a string if it's not already a string.
        Then, it initializes variables `ss` and `s` as the consecutive double spaces and a single space, respectively.
        The function enters a loop and checks if `ss` (consecutive double spaces) exists in the string `x`.
        If it does, it replaces `ss` with `s` (single space) in `x`.
        The loop continues until there are no more consecutive double spaces in `x`.
        Finally, the function returns the processed string with consecutive double spaces replaced by a single space.
     Example usage:
        input_str = "Hello  world! This   is a test."
        processed_str = _deal_double_spaces(input_str)
        # processed_str will be "Hello world! This is a test."
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
        Tuple[str, datetime]: A tuple containing the CEI file type (as a string)
        and the date the file was created (as a datetime object).

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

        return cei_file_type, cei_file_date.date()
    else:
        raise ValueError(f'Nome de arquivo invalido: {cei_file_name}')


def _extract_product_id(product, sep='-'):
    """
    Extracts the product ID from a given product string.
     Args:
        product (str): The product string from which to extract the ID.
        sep (str, optional): The separator used to split the product string. Default is '-'.
     Returns:
        str: The extracted product ID.
     Overview:
        This function extracts the product ID from the given product string.
        If the word 'Tesouro' is found in the product string, the entire product string is returned as the ID.
        Otherwise, the product string is split using the specified separator.
        The extracted ID is determined based on the contents of the split product string.
        If the word 'Futuro' is found in the first part of the split string, the second part is considered as the ID.
        Otherwise, the first part is considered as the ID.
        The extracted ID is returned after stripping any leading or trailing spaces.
     Example usage:
        product_string = 'Futuro-12345'
        extracted_id = _extract_product_id(product_string)
        # extracted_id will be '12345'
    """
    if 'Tesouro' in product:
        return product
    
    product_parts = product.split(sep)
    
    return product_parts[
        1 if 'Futuro' in product_parts[0] else 0
    ].strip()


def process_schema_movimentacao(input_files):
    xl_dataframes = []
    fields = [
        'entrada_saida',
        'data_movimentacao',
        'movimentacao',
        'nome_produto',
        'codigo_produto',
        'instituicao',
        'conta',
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

        if 'Conta' in xl_dataframe.columns:
            xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
        else:
            xl_dataframe['conta'] = '000000000'
        
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço unitário'].apply(_str_to_number).astype('float64')
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor da Operação'].apply(_str_to_number).astype('float64')
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_eventos_provisionados(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'tipo_produto',
        'tipo_evento',
        'previsao_pagamento',
        'instituicao',
        'conta',
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

        if 'Conta' in xl_dataframe.columns:
            xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
        else:
            xl_dataframe['conta'] = '000000000'

        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço unitário'].apply(_str_to_number).astype('float64')
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor líquido'].apply(_str_to_number).astype('float64')
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_negociacao(input_files):
    xl_dataframes = []
    fields = [
        'data_negocio',
        'movimentacao',
        'mercado',
        'prazo_vencimento',
        'instituicao',
        'conta',
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

        if 'Conta' in xl_dataframe.columns:
            xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
        else:
            xl_dataframe['conta'] = '000000000'

        xl_dataframe['codigo_produto'] = xl_dataframe['Código de Negociação']
        xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
        xl_dataframe['preco_unitario'] = xl_dataframe['Preço'].apply(_str_to_number).astype('float64')
        xl_dataframe['valor_operacao'] = xl_dataframe['Valor'].apply(_str_to_number).astype('float64')
        xl_dataframe['arquivo_origem'] = schema_file_name
        xl_dataframe['data_referencia'] = schema_file_date

        xl_dataframe = xl_dataframe[fields].copy()

        xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_posicao_acoes(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'conta',
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

                if 'Conta' in xl_dataframe.columns:
                    xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
                else:
                    xl_dataframe['conta'] = '000000000'

                xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
                xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
                xl_dataframe['escriturador'] = xl_dataframe['Escriturador'].apply(_deal_double_spaces)
                xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
                xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number).astype('float64')
                xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number).astype('float64')
                xl_dataframe['motivo'] = xl_dataframe['Motivo']
                xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number).astype('float64')
                xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number).astype('float64')

                xl_dataframe['arquivo_origem'] = SU.normalize_names([f'{schema_file_name}_{xl_sheet}'])[0]

                xl_dataframe['data_referencia'] = schema_file_date

                xl_dataframe = xl_dataframe[fields].copy()

                xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_posicao_emprestimo_ativos(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'conta',
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

                if 'Conta' in xl_dataframe.columns:
                    xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
                else:
                    xl_dataframe['conta'] = '000000000'

                xl_dataframe['natureza'] = xl_dataframe['Natureza'].apply(_deal_double_spaces)
                xl_dataframe['contrato'] = xl_dataframe['Número de Contrato'].apply(_deal_double_spaces)
                xl_dataframe['modalidade'] = xl_dataframe['Modalidade'].apply(_deal_double_spaces)
                xl_dataframe['opa'] = xl_dataframe['OPA'].apply(_deal_double_spaces)
                xl_dataframe['liquidacao_antecipada'] = xl_dataframe['Liquidação antecipada'].apply(_deal_double_spaces)
                xl_dataframe['taxa'] = xl_dataframe['Taxa'].apply(_str_to_number).astype('float64')
                xl_dataframe['comissao'] = xl_dataframe['Comissão'].apply(_str_to_number).astype('float64')
                xl_dataframe['data_registro'] = xl_dataframe['Data de registro'].apply(_str_to_date)
                xl_dataframe['data_vencimento'] = xl_dataframe['Data de vencimento'].apply(_str_to_date)
                xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
                xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number).astype('float64')
                xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number).astype('float64')

                xl_sheet = 'Empréstimo de Ativos'
                xl_dataframe['arquivo_origem'] = SU.normalize_names([f'{schema_file_name}_{xl_sheet}'])[0]


                xl_dataframe['data_referencia'] = schema_file_date

                xl_dataframe = xl_dataframe[fields].copy()

                xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_posicao_etf(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'conta',
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

            if 'Conta' in xl_dataframe.columns:
                xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
            else:
                xl_dataframe['conta'] = '000000000'

            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
            xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number).astype('float64')

            xl_dataframe['arquivo_origem'] = SU.normalize_names([f'{schema_file_name}_{xl_sheet}'])[0]

            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_posicao_fundos_investimento(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'conta',
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

            if 'Conta' in xl_dataframe.columns:
                xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
            else:
                xl_dataframe['conta'] = '000000000'

            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN / Distribuição']
            xl_dataframe['tipo_produto'] = xl_dataframe['Tipo']
            xl_dataframe['administrador'] = xl_dataframe['Administrador'].apply(_deal_double_spaces)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['preco_unitario'] = xl_dataframe['Preço de Fechamento'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_operacao'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number).astype('float64')

            xl_dataframe['arquivo_origem'] = SU.normalize_names([f'{schema_file_name}_{xl_sheet}'])[0]

            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_posicao_tesouro_direto(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'conta',
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

            if 'Conta' in xl_dataframe.columns:
                xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
            else:
                xl_dataframe['conta'] = '000000000'

            xl_dataframe['codigo_isin'] = xl_dataframe['Código ISIN']
            xl_dataframe['indexador'] = xl_dataframe['Indexador']
            xl_dataframe['vencimento'] = xl_dataframe['Vencimento'].apply(_str_to_date)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['valor_aplicado'] = xl_dataframe['Valor Aplicado'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_bruto'] = xl_dataframe['Valor bruto'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_liquido'] = xl_dataframe['Valor líquido'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_atualizado'] = xl_dataframe['Valor Atualizado'].apply(_str_to_number).astype('float64')

            xl_dataframe['arquivo_origem'] = SU.normalize_names([f'{schema_file_name}_{xl_sheet}'])[0]

            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)


def process_schema_posicao_renda_fixa(input_files):
    xl_dataframes = []
    fields = [
        'codigo_produto',
        'nome_produto',
        'instituicao',
        'conta',
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

            if 'Conta' in xl_dataframe.columns:
                xl_dataframe['conta'] = xl_dataframe['Conta'].apply(_deal_double_spaces)
            else:
                xl_dataframe['conta'] = '000000000'

            xl_dataframe['emissor'] = xl_dataframe['Emissor'].apply(_deal_double_spaces)
            xl_dataframe['indexador'] = xl_dataframe['Indexador'].apply(_deal_double_spaces)
            xl_dataframe['tipo_regime'] = xl_dataframe['Tipo de regime']
            xl_dataframe['emissao'] = xl_dataframe['Data de Emissão'].apply(_str_to_date)
            xl_dataframe['vencimento'] = xl_dataframe['Vencimento'].apply(_str_to_date)
            xl_dataframe['quantidade'] = xl_dataframe['Quantidade'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_disponivel'] = xl_dataframe['Quantidade Disponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['quantidade_indisponivel'] = xl_dataframe['Quantidade Indisponível'].apply(_str_to_number).astype('float64')
            xl_dataframe['motivo'] = xl_dataframe['Motivo']
            xl_dataframe['contraparte'] = xl_dataframe['Contraparte']
            xl_dataframe['preco_atualizado_mtm'] = xl_dataframe['Preço Atualizado MTM'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_atualizado_mtm'] = xl_dataframe['Valor Atualizado MTM'].apply(_str_to_number).astype('float64')
            xl_dataframe['preco_atualizado_curva'] = xl_dataframe['Preço Atualizado CURVA'].apply(_str_to_number).astype('float64')
            xl_dataframe['valor_atualizado_curva'] = xl_dataframe['Valor Atualizado CURVA'].apply(_str_to_number).astype('float64')

            xl_dataframe['arquivo_origem'] = SU.normalize_names([f'{schema_file_name}_{xl_sheet}'])[0]

            xl_dataframe['data_referencia'] = schema_file_date

            xl_dataframe = xl_dataframe[fields].copy()

            xl_dataframes.append(xl_dataframe)

    return pd.concat(xl_dataframes)

"""
Processamento de dados de posição de empréstimo de ativos do CEI (Canal Eletrônico do Investidor).

Este módulo fornece funcionalidades para processar arquivos Excel de posição de empréstimo de ativos
do CEI, extraindo dados das planilhas 'Empréstimo de Ativos' e 'Empréstimos', padronizando colunas e
realizando conversões de tipos de dados incluindo datas e valores numéricos.

Exemplos:
    >>> from fbpyutils_finance.cei.schemas.posicao_emprestimo_ativos import process_schema_posicao_emprestimo_ativos
    >>> # Processar múltiplos arquivos de posição de empréstimo
    >>> files = ['posicao-2023-01.xlsx', 'posicao-2023-02.xlsx']
    >>> df = process_schema_posicao_emprestimo_ativos(files)
    >>> print(df.columns.tolist())
    ['codigo_produto', 'nome_produto', 'instituicao', 'conta', 'natureza',
     'contrato', 'modalidade', 'opa', 'liquidacao_antecipada', 'taxa',
     'comissao', 'data_registro', 'data_vencimento', 'quantidade',
     'preco_unitario', 'valor_operacao', 'arquivo_origem', 'data_referencia']
"""

import pandas as pd
from typing import List, Optional

from fbpyutils import xlsx as XL, string as SU
from .utils import (
    _str_to_date,
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    extract_product_id,
)

from fbpyutils_finance import logger


def process_schema_posicao_emprestimo_ativos(
    input_files: List[str],
) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Posição' (Position) Excel files, specifically the 'Empréstimo de Ativos'/'Empréstimos' sheets.

    Reads one or more 'posicao-*.xlsx' files, extracts data from relevant sheets,
    standardizes columns, performs type conversions, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Posição' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                asset lending position data. Returns an empty DataFrame if
                                input_files is empty or no relevant sheets/data are found.

    Examples:
        >>> # Processar arquivo único
        >>> df = process_schema_posicao_emprestimo_ativos(['posicao-2023-01.xlsx'])
        >>> print(len(df.columns))
        18

        >>> # Processar lista vazia retorna DataFrame vazio
        >>> df = process_schema_posicao_emprestimo_ativos([])
        >>> df.empty
        True

        >>> # Processar arquivo inexistente retorna DataFrame vazio
        >>> df = process_schema_posicao_emprestimo_ativos(['arquivo_inexistente.xlsx'])
        >>> df.empty
        True
    """
    logger.info(
        f"process_schema_posicao_emprestimo_ativos: input_files={len(input_files)} files"
    )

    if not input_files:
        logger.debug("input_files is empty, returning empty DataFrame")
        return pd.DataFrame()

    xl_dataframes = []
    fields = [
        "codigo_produto",
        "nome_produto",
        "instituicao",
        "conta",
        "natureza",
        "contrato",
        "modalidade",
        "opa",
        "liquidacao_antecipada",
        "taxa",
        "comissao",
        "data_registro",
        "data_vencimento",
        "quantidade",
        "preco_unitario",  # Corresponds to 'Preço de Fechamento'
        "valor_operacao",  # Corresponds to 'Valor Atualizado'
        "arquivo_origem",
        "data_referencia",
    ]

    # Sheets to check for asset lending data
    xl_sheets_to_process = ["Empréstimo de Ativos", "Empréstimos"]
    # Standardized sheet name for output file origin
    standardized_sheet_name_origin = "Empréstimo_de_Ativos"

    for schema_file in input_files:
        logger.debug(f"Processing file: {schema_file}")
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)
            logger.debug(
                f"Extracted file info: name={schema_file_name}, date={schema_file_date}"
            )

            if "posicao" not in schema_file_name:
                logger.warning(
                    f"Skipping file {schema_file} as it doesn't appear to be a 'posicao' type."
                )
                continue

            xl_obj = XL.ExcelWorkbook(schema_file)
            processed_sheets_in_file = []

            for xl_sheet in xl_sheets_to_process:
                if xl_sheet in xl_obj.sheet_names:
                    xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))

                    if not xl_table or len(xl_table) < 2:
                        logger.warning(
                            f"Sheet '{xl_sheet}' in {schema_file} contains no data or header."
                        )
                        continue
                    logger.debug(f"Sheet '{xl_sheet}' has {len(xl_table)} rows")

                    header = xl_table[0]
                    data = xl_table[1:]
                    xl_dataframe = pd.DataFrame(data, columns=header)

                    if "Produto" in xl_dataframe.columns:
                        xl_dataframe = xl_dataframe[
                            xl_dataframe["Produto"] != ""
                        ].copy()
                    else:
                        logger.warning(
                            f"'Produto' column not found in sheet '{xl_sheet}' of {schema_file}."
                        )
                        continue

                    if xl_dataframe.empty:
                        logger.warning(
                            f"No data left in sheet '{xl_sheet}' of {schema_file} after filtering."
                        )
                        continue
                    logger.debug(
                        f"DataFrame after filtering has {len(xl_dataframe)} rows"
                    )

                    # --- Data Cleaning and Transformation ---
                    column_mapping = {
                        "Produto": "nome_produto_raw",
                        "Instituição": "instituicao_raw",
                        "Conta": "conta_raw",
                        "Natureza": "natureza_raw",
                        "Número de Contrato": "contrato_raw",
                        "Modalidade": "modalidade_raw",
                        "OPA": "opa_raw",
                        "Liquidação antecipada": "liquidacao_antecipada_raw",
                        "Taxa": "taxa_raw",
                        "Comissão": "comissao_raw",
                        "Data de registro": "data_registro_raw",
                        "Data de vencimento": "data_vencimento_raw",
                        "Quantidade": "quantidade_raw",
                        "Preço de Fechamento": "preco_unitario_raw",
                        "Valor Atualizado": "valor_operacao_raw",
                    }

                    rename_dict = {
                        k: v
                        for k, v in column_mapping.items()
                        if k in xl_dataframe.columns
                    }
                    required_raw_cols = [
                        "nome_produto_raw",
                        "instituicao_raw",
                    ]  # Minimal check
                    if not all(
                        col in rename_dict.values() for col in required_raw_cols
                    ):
                        logger.warning(
                            f"Missing one or more essential columns in sheet '{xl_sheet}' of {schema_file}. Skipping sheet."
                        )
                        continue

                    xl_dataframe = xl_dataframe[list(rename_dict.keys())].rename(
                        columns=rename_dict
                    )

                    # Handle missing 'Conta' column
                    if "conta_raw" not in xl_dataframe.columns:
                        xl_dataframe["conta"] = "000000000"
                    else:
                        xl_dataframe["conta"] = xl_dataframe["conta_raw"].apply(
                            deal_double_spaces
                        )

                    # Apply transformations
                    xl_dataframe["nome_produto"] = xl_dataframe[
                        "nome_produto_raw"
                    ].apply(deal_double_spaces)
                    xl_dataframe["codigo_produto"] = xl_dataframe["nome_produto"].apply(
                        extract_product_id
                    )  # Extract code from name
                    xl_dataframe["instituicao"] = xl_dataframe["instituicao_raw"].apply(
                        deal_double_spaces
                    )
                    xl_dataframe["natureza"] = xl_dataframe["natureza_raw"].apply(
                        deal_double_spaces
                    )
                    xl_dataframe["contrato"] = xl_dataframe["contrato_raw"].apply(
                        deal_double_spaces
                    )
                    xl_dataframe["modalidade"] = xl_dataframe["modalidade_raw"].apply(
                        deal_double_spaces
                    )
                    xl_dataframe["opa"] = xl_dataframe["opa_raw"].apply(
                        deal_double_spaces
                    )
                    xl_dataframe["liquidacao_antecipada"] = xl_dataframe[
                        "liquidacao_antecipada_raw"
                    ].apply(deal_double_spaces)

                    # Convert numeric and date columns
                    logger.debug("Converting numeric and date columns")
                    xl_dataframe["taxa"] = pd.to_numeric(
                        xl_dataframe["taxa_raw"], errors="coerce"
                    )
                    xl_dataframe["comissao"] = pd.to_numeric(
                        xl_dataframe["comissao_raw"], errors="coerce"
                    )
                    xl_dataframe["data_registro"] = pd.to_datetime(
                        xl_dataframe["data_registro_raw"].apply(_str_to_date),
                        errors="coerce",
                    )
                    xl_dataframe["data_vencimento"] = pd.to_datetime(
                        xl_dataframe["data_vencimento_raw"].apply(_str_to_date),
                        errors="coerce",
                    )
                    xl_dataframe["quantidade"] = pd.to_numeric(
                        xl_dataframe["quantidade_raw"], errors="coerce"
                    )
                    xl_dataframe["preco_unitario"] = pd.to_numeric(
                        xl_dataframe["preco_unitario_raw"], errors="coerce"
                    )
                    xl_dataframe["valor_operacao"] = pd.to_numeric(
                        xl_dataframe["valor_operacao_raw"], errors="coerce"
                    )
                    logger.debug(
                        "Converted columns: taxa, comissao, data_registro, data_vencimento, quantidade, preco_unitario, valor_operacao"
                    )

                    # Add metadata
                    normalized_sheet_name = SU.normalize_names(
                        [standardized_sheet_name_origin]
                    )[0]
                    xl_dataframe["arquivo_origem"] = (
                        f"{schema_file_name}_{normalized_sheet_name}"
                    )
                    xl_dataframe["data_referencia"] = schema_file_date

                    # Ensure all expected columns exist
                    for field in fields:
                        if field not in xl_dataframe.columns:
                            xl_dataframe[field] = None

                    xl_dataframes.append(xl_dataframe[fields].copy())
                    processed_sheets_in_file.append(xl_sheet)
                    # Break after finding the first valid sheet (Empréstimo de Ativos or Empréstimos)
                    break

            if not processed_sheets_in_file:
                logger.warning(
                    f"No relevant sheets ({', '.join(xl_sheets_to_process)}) with data found in {schema_file}."
                )
            else:
                logger.debug(
                    f"Processed sheets in {schema_file}: {processed_sheets_in_file}"
                )

        except ValueError as e:
            logger.error(f"Error processing file {schema_file}: {e}", exc_info=True)
        except Exception as e:
            logger.error(
                f"An unexpected error occurred while processing {schema_file}: {e}",
                exc_info=True,
            )

    if not xl_dataframes:
        logger.debug(
            "No dataframes to concatenate, returning empty DataFrame with columns"
        )
        return pd.DataFrame(columns=fields)

    result_df = pd.concat(xl_dataframes, ignore_index=True)
    logger.info(
        f"process_schema_posicao_emprestimo_ativos: returning DataFrame with {len(result_df)} rows and {len(result_df.columns)} columns"
    )
    return result_df

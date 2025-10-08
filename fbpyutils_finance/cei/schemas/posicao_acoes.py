"""
Processamento de dados de posição de ações e BDRs do CEI (Canal Eletrônico do Investidor).

Este módulo fornece funcionalidades para processar arquivos Excel de posição de ações e BDRs
do CEI, extraindo dados das planilhas 'Ações', 'Acoes' e 'BDR', padronizando colunas e
realizando conversões de tipos de dados.

Exemplos:
    >>> from fbpyutils_finance.cei.schemas.posicao_acoes import process_schema_posicao_acoes
    >>> # Processar múltiplos arquivos de posição
    >>> files = ['posicao-2023-01.xlsx', 'posicao-2023-02.xlsx']
    >>> df = process_schema_posicao_acoes(files)
    >>> print(df.columns.tolist())
    ['codigo_produto', 'nome_produto', 'instituicao', 'conta', 'codigo_isin',
     'tipo_produto', 'escriturador', 'quantidade', 'quantidade_disponivel',
     'quantidade_indisponivel', 'motivo', 'preco_unitario', 'valor_operacao',
     'arquivo_origem', 'data_referencia']
"""

import pandas as pd
from typing import List, Optional

from fbpyutils import xlsx as XL, string as SU
from .utils import (
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    # extract_product_id is not used here, Código de Negociação is used directly
)

from fbpyutils_finance import logger


def process_schema_posicao_acoes(input_files: List[str]) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Posição' (Position) Excel files, specifically the 'Ações'/'Acoes' and 'BDR' sheets.

    Reads one or more 'posicao-*.xlsx' files, extracts data from relevant sheets,
    standardizes columns, performs type conversions, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Posição' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                stock and BDR position data. Returns an empty DataFrame if
                                input_files is empty or no relevant sheets/data are found.

    Examples:
        >>> # Processar arquivo único
        >>> df = process_schema_posicao_acoes(['posicao-2023-01.xlsx'])
        >>> print(len(df.columns))
        14

        >>> # Processar lista vazia retorna DataFrame vazio
        >>> df = process_schema_posicao_acoes([])
        >>> df.empty
        True

        >>> # Processar arquivo inexistente retorna DataFrame vazio
        >>> df = process_schema_posicao_acoes(['arquivo_inexistente.xlsx'])
        >>> df.empty
        True
    """
    logger.info(f"process_schema_posicao_acoes: input_files={len(input_files)} files")

    if not input_files:
        logger.debug("input_files is empty, returning empty DataFrame")
        return pd.DataFrame()

    xl_dataframes = []
    fields = [
        "codigo_produto",
        "nome_produto",
        "instituicao",
        "conta",
        "codigo_isin",
        "tipo_produto",
        "escriturador",
        "quantidade",
        "quantidade_disponivel",
        "quantidade_indisponivel",
        "motivo",
        "preco_unitario",
        "valor_operacao",  # Corresponds to 'Valor Atualizado'
        "arquivo_origem",
        "data_referencia",
    ]

    # Sheets to check for stock/BDR data
    xl_sheets_to_process = ["Ações", "Acoes", "BDR"]

    for schema_file in input_files:
        logger.debug(f"Processing file: {schema_file}")
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)
            logger.debug(
                f"Extracted file info: name={schema_file_name}, date={schema_file_date}"
            )

            # Basic check if it's a 'posicao' file
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

                    # Filter out rows where 'Produto' is empty
                    if "Produto" in xl_dataframe.columns:
                        xl_dataframe = xl_dataframe[
                            xl_dataframe["Produto"] != ""
                        ].copy()
                    else:
                        logger.warning(
                            f"'Produto' column not found in sheet '{xl_sheet}' of {schema_file}."
                        )
                        continue  # Skip sheet if essential column is missing

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
                        "Código de Negociação": "codigo_produto_raw",
                        "Produto": "nome_produto_raw",
                        "Instituição": "instituicao_raw",
                        "Conta": "conta_raw",
                        "Código ISIN / Distribuição": "codigo_isin",  # Direct mapping
                        "Tipo": "tipo_produto",  # Direct mapping
                        "Escriturador": "escriturador_raw",
                        "Quantidade": "quantidade_raw",
                        "Quantidade Disponível": "quantidade_disponivel_raw",
                        "Quantidade Indisponível": "quantidade_indisponivel_raw",
                        "Motivo": "motivo",  # Direct mapping
                        "Preço de Fechamento": "preco_unitario_raw",
                        "Valor Atualizado": "valor_operacao_raw",  # Map to valor_operacao
                    }

                    rename_dict = {
                        k: v
                        for k, v in column_mapping.items()
                        if k in xl_dataframe.columns
                    }
                    # Check for essential columns before proceeding
                    required_raw_cols = [
                        "codigo_produto_raw",
                        "nome_produto_raw",
                        "instituicao_raw",
                    ]
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
                    xl_dataframe["codigo_produto"] = xl_dataframe[
                        "codigo_produto_raw"
                    ].apply(deal_double_spaces)
                    xl_dataframe["nome_produto"] = xl_dataframe[
                        "nome_produto_raw"
                    ].apply(deal_double_spaces)
                    xl_dataframe["instituicao"] = xl_dataframe["instituicao_raw"].apply(
                        deal_double_spaces
                    )
                    xl_dataframe["escriturador"] = xl_dataframe[
                        "escriturador_raw"
                    ].apply(deal_double_spaces)
                    # 'codigo_isin', 'tipo_produto', 'motivo' are directly mapped

                    # Convert numeric columns
                    xl_dataframe["quantidade"] = pd.to_numeric(
                        xl_dataframe["quantidade_raw"], errors="coerce"
                    )
                    xl_dataframe["quantidade_disponivel"] = pd.to_numeric(
                        xl_dataframe["quantidade_disponivel_raw"], errors="coerce"
                    )
                    xl_dataframe["quantidade_indisponivel"] = pd.to_numeric(
                        xl_dataframe["quantidade_indisponivel_raw"], errors="coerce"
                    )
                    xl_dataframe["preco_unitario"] = pd.to_numeric(
                        xl_dataframe["preco_unitario_raw"], errors="coerce"
                    )
                    xl_dataframe["valor_operacao"] = pd.to_numeric(
                        xl_dataframe["valor_operacao_raw"], errors="coerce"
                    )

                    # Add metadata
                    # Normalize sheet name for the origin file identifier
                    normalized_sheet_name = SU.normalize_names([xl_sheet])[0]
                    xl_dataframe["arquivo_origem"] = (
                        f"{schema_file_name}_{normalized_sheet_name}"
                    )
                    xl_dataframe["data_referencia"] = schema_file_date

                    # Ensure all expected columns exist
                    for field in fields:
                        if field not in xl_dataframe.columns:
                            xl_dataframe[field] = None  # Or pd.NA

                    xl_dataframes.append(xl_dataframe[fields].copy())
                    processed_sheets_in_file.append(xl_sheet)

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
        f"process_schema_posicao_acoes: returning DataFrame with {len(result_df)} rows and {len(result_df.columns)} columns"
    )
    return result_df

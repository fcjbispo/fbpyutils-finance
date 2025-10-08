"""
Processamento de dados de posição de renda fixa do CEI (Canal Eletrônico do Investidor).

Este módulo fornece funcionalidades para processar arquivos Excel de posição de renda fixa
do CEI, extraindo dados da planilha 'Renda Fixa', padronizando colunas e realizando conversões
de tipos de dados incluindo datas e valores numéricos.

Exemplos:
    >>> from fbpyutils_finance.cei.schemas.posicao_renda_fixa import process_schema_posicao_renda_fixa
    >>> # Processar múltiplos arquivos de posição de renda fixa
    >>> files = ['posicao-2023-01.xlsx', 'posicao-2023-02.xlsx']
    >>> df = process_schema_posicao_renda_fixa(files)
    >>> print(df.columns.tolist())
    ['codigo_produto', 'nome_produto', 'instituicao', 'conta', 'emissor',
     'indexador', 'tipo_regime', 'emissao', 'vencimento', 'quantidade',
     'quantidade_disponivel', 'quantidade_indisponivel', 'motivo', 'contraparte',
     'preco_atualizado_mtm', 'valor_atualizado_mtm', 'preco_atualizado_curva',
     'valor_atualizado_curva', 'arquivo_origem', 'data_referencia']
"""

import pandas as pd
from typing import List, Optional

from fbpyutils import xlsx as XL, string as SU
from .utils import (
    _str_to_date,
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    # extract_product_id is not used here
)

from fbpyutils_finance import logger


def process_schema_posicao_renda_fixa(input_files: List[str]) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Posição' (Position) Excel files, specifically the 'Renda Fixa' sheet.

    Reads one or more 'posicao-*.xlsx' files, extracts data from the 'Renda Fixa' sheet,
    standardizes columns, performs type conversions, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Posição' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                fixed income position data. Returns an empty DataFrame if
                                input_files is empty or the sheet is not found or has no data.

    Examples:
        >>> # Processar arquivo único
        >>> df = process_schema_posicao_renda_fixa(['posicao-2023-01.xlsx'])
        >>> print(len(df.columns))
        20

        >>> # Processar lista vazia retorna DataFrame vazio
        >>> df = process_schema_posicao_renda_fixa([])
        >>> df.empty
        True

        >>> # Processar arquivo inexistente retorna DataFrame vazio
        >>> df = process_schema_posicao_renda_fixa(['arquivo_inexistente.xlsx'])
        >>> df.empty
        True
    """
    logger.info(
        f"process_schema_posicao_renda_fixa: input_files={len(input_files)} files"
    )

    if not input_files:
        logger.debug("input_files is empty, returning empty DataFrame")
        return pd.DataFrame()

    xl_dataframes = []
    fields = [
        "codigo_produto",  # Corresponds to 'Código'
        "nome_produto",  # Corresponds to 'Produto'
        "instituicao",
        "conta",
        "emissor",
        "indexador",
        "tipo_regime",
        "emissao",
        "vencimento",
        "quantidade",
        "quantidade_disponivel",
        "quantidade_indisponivel",
        "motivo",
        "contraparte",
        "preco_atualizado_mtm",
        "valor_atualizado_mtm",
        "preco_atualizado_curva",
        "valor_atualizado_curva",
        "arquivo_origem",
        "data_referencia",
    ]

    xl_sheet_to_process = "Renda Fixa"

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

            if xl_sheet_to_process in xl_obj.sheet_names:
                xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet_to_process)))

                if not xl_table or len(xl_table) < 2:
                    logger.warning(
                        f"Sheet '{xl_sheet_to_process}' in {schema_file} contains no data or header."
                    )
                    continue
                logger.debug(f"Sheet '{xl_sheet_to_process}' has {len(xl_table)} rows")

                header = xl_table[0]
                data = xl_table[1:]
                xl_dataframe = pd.DataFrame(data, columns=header)

                if "Produto" in xl_dataframe.columns:
                    xl_dataframe = xl_dataframe[xl_dataframe["Produto"] != ""].copy()
                else:
                    logger.warning(
                        f"'Produto' column not found in sheet '{xl_sheet_to_process}' of {schema_file}."
                    )
                    continue

                if xl_dataframe.empty:
                    logger.warning(
                        f"No data left in sheet '{xl_sheet_to_process}' of {schema_file} after filtering."
                    )
                    continue
                logger.debug(f"DataFrame after filtering has {len(xl_dataframe)} rows")

                # --- Data Cleaning and Transformation ---
                column_mapping = {
                    "Código": "codigo_produto_raw",
                    "Produto": "nome_produto_raw",
                    "Instituição": "instituicao_raw",
                    "Conta": "conta_raw",
                    "Emissor": "emissor_raw",
                    "Indexador": "indexador_raw",
                    "Tipo de regime": "tipo_regime",  # Direct map
                    "Data de Emissão": "emissao_raw",
                    "Vencimento": "vencimento_raw",
                    "Quantidade": "quantidade_raw",
                    "Quantidade Disponível": "quantidade_disponivel_raw",
                    "Quantidade Indisponível": "quantidade_indisponivel_raw",
                    "Motivo": "motivo",  # Direct map
                    "Contraparte": "contraparte",  # Direct map
                    "Preço Atualizado MTM": "preco_atualizado_mtm_raw",
                    "Valor Atualizado MTM": "valor_atualizado_mtm_raw",
                    "Preço Atualizado CURVA": "preco_atualizado_curva_raw",
                    "Valor Atualizado CURVA": "valor_atualizado_curva_raw",
                }

                rename_dict = {
                    k: v for k, v in column_mapping.items() if k in xl_dataframe.columns
                }
                required_raw_cols = [
                    "codigo_produto_raw",
                    "nome_produto_raw",
                    "instituicao_raw",
                ]
                if not all(col in rename_dict.values() for col in required_raw_cols):
                    logger.warning(
                        f"Missing one or more essential columns in sheet '{xl_sheet_to_process}' of {schema_file}. Skipping file."
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
                xl_dataframe["nome_produto"] = xl_dataframe["nome_produto_raw"].apply(
                    deal_double_spaces
                )
                xl_dataframe["instituicao"] = xl_dataframe["instituicao_raw"].apply(
                    deal_double_spaces
                )
                xl_dataframe["emissor"] = xl_dataframe["emissor_raw"].apply(
                    deal_double_spaces
                )
                xl_dataframe["indexador"] = xl_dataframe["indexador_raw"].apply(
                    deal_double_spaces
                )
                # 'tipo_regime', 'motivo', 'contraparte' are directly mapped

                # Convert date and numeric columns
                logger.debug("Converting date and numeric columns")
                xl_dataframe["emissao"] = pd.to_datetime(
                    xl_dataframe["emissao_raw"].apply(_str_to_date), errors="coerce"
                )
                xl_dataframe["vencimento"] = pd.to_datetime(
                    xl_dataframe["vencimento_raw"].apply(_str_to_date), errors="coerce"
                )
                xl_dataframe["quantidade"] = pd.to_numeric(
                    xl_dataframe["quantidade_raw"], errors="coerce"
                )
                xl_dataframe["quantidade_disponivel"] = pd.to_numeric(
                    xl_dataframe["quantidade_disponivel_raw"], errors="coerce"
                )
                xl_dataframe["quantidade_indisponivel"] = pd.to_numeric(
                    xl_dataframe["quantidade_indisponivel_raw"], errors="coerce"
                )
                xl_dataframe["preco_atualizado_mtm"] = pd.to_numeric(
                    xl_dataframe["preco_atualizado_mtm_raw"], errors="coerce"
                )
                xl_dataframe["valor_atualizado_mtm"] = pd.to_numeric(
                    xl_dataframe["valor_atualizado_mtm_raw"], errors="coerce"
                )
                xl_dataframe["preco_atualizado_curva"] = pd.to_numeric(
                    xl_dataframe["preco_atualizado_curva_raw"], errors="coerce"
                )
                xl_dataframe["valor_atualizado_curva"] = pd.to_numeric(
                    xl_dataframe["valor_atualizado_curva_raw"], errors="coerce"
                )
                logger.debug(
                    "Converted columns: emissao, vencimento, quantidade, quantidade_disponivel, quantidade_indisponivel, preco_atualizado_mtm, valor_atualizado_mtm, preco_atualizado_curva, valor_atualizado_curva"
                )

                # Add metadata
                normalized_sheet_name = SU.normalize_names([xl_sheet_to_process])[0]
                xl_dataframe["arquivo_origem"] = (
                    f"{schema_file_name}_{normalized_sheet_name}"
                )
                xl_dataframe["data_referencia"] = schema_file_date

                # Ensure all expected columns exist
                for field in fields:
                    if field not in xl_dataframe.columns:
                        xl_dataframe[field] = None

                xl_dataframes.append(xl_dataframe[fields].copy())
            else:
                logger.info(
                    f"Sheet '{xl_sheet_to_process}' not found in {schema_file}."
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
        f"process_schema_posicao_renda_fixa: returning DataFrame with {len(result_df)} rows and {len(result_df.columns)} columns"
    )
    return result_df

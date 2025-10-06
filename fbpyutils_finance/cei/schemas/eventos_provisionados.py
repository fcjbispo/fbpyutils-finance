"""
fbpyutils_finance.cei.schemas.eventos_provisionados - CEI Eventos Provisionados Schema Processor

Purpose: This module provides functionality to process CEI 'Eventos Provisionados' (Provisioned Events) Excel files, extracting and standardizing financial event data for analysis.

Main contents:
- process_schema_eventos_provisionados() (function): Process and consolidate provisioned events data from Excel files

High-level usage pattern:
Import the function and call it with a list of CEI Excel file paths to get a consolidated DataFrame with processed event data.

Examples:
>>> from fbpyutils_finance.cei.schemas.eventos_provisionados import process_schema_eventos_provisionados
>>> result = process_schema_eventos_provisionados(['eventos-2023-01-15.xlsx'])
>>> isinstance(result, pd.DataFrame)
True
>>> len(result.columns) > 5
True
"""

# fbpyutils_finance/cei/schemas/eventos_provisionados.py
import pandas as pd
from typing import List, Optional

from fbpyutils import xlsx as XL
from fbpyutils_finance import logger
from .utils import (
    _str_to_date,
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    extract_product_id,
)


def process_schema_eventos_provisionados(
    input_files: List[str],
) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Eventos Provisionados' (Provisioned Events) Excel files.

    Reads one or more 'eventos-*.xlsx' files, extracts data, standardizes columns,
    performs type conversions, filters out totals, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Eventos Provisionados' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                provisioned events data. Returns an empty DataFrame if
                                input_files is empty or no valid files are processed.

    Examples:
        >>> result = process_schema_eventos_provisionados([])
        >>> isinstance(result, pd.DataFrame)
        True
        >>> len(result.columns)
        12
        >>> # Test with non-existent file (should handle gracefully)
        >>> result = process_schema_eventos_provisionados(['nonexistent.xlsx'])
        >>> isinstance(result, pd.DataFrame)
        True
    """
    logger.info(f"process_schema_eventos_provisionados(input_files={len(input_files)} files)")
    
    if not input_files:
        logger.debug("No input files provided, returning empty DataFrame")
        return pd.DataFrame()  # Return empty DataFrame if no input files

    xl_dataframes = []
    fields = [
        "codigo_produto",
        "nome_produto",
        "tipo_produto",
        "tipo_evento",
        "previsao_pagamento",
        "instituicao",
        "conta",
        "quantidade",
        "preco_unitario",
        "valor_operacao",
        "arquivo_origem",
        "data_referencia",
    ]

    for schema_file in input_files:
        logger.debug(f"Processing file: {schema_file}")
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)
            logger.debug(f"Extracted file info: name='{schema_file_name}', date={schema_file_date}")

            # Basic check if it's an 'eventos' file (adjust if needed)
            if "eventos" not in schema_file_name:
                logger.warning(f"Skipping file {schema_file} as it doesn't appear to be an 'eventos' type")
                print(
                    f"Warning: Skipping file {schema_file} as it doesn't appear to be an 'eventos' type."
                )
                continue

            logger.debug(f"Loading Excel file: {schema_file}")
            xl_obj = XL.ExcelWorkbook(schema_file)
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))

            if not xl_table or len(xl_table) < 2:
                logger.warning(f"Skipping file {schema_file} as it contains no data or header")
                print(
                    f"Warning: Skipping file {schema_file} as it contains no data or header."
                )
                continue

            header = xl_table[0]
            data = xl_table[1:]
            xl_dataframe = pd.DataFrame(data, columns=header)
            logger.debug(f"Created DataFrame with shape: {xl_dataframe.shape}")

            # Filter out total rows before processing
            if "Preço unitário" in xl_dataframe.columns:
                original_len = len(xl_dataframe)
                xl_dataframe = xl_dataframe[
                    xl_dataframe["Preço unitário"] != "Total líquido"
                ].copy()
                filtered_len = len(xl_dataframe)
                logger.debug(f"Filtered out {original_len - filtered_len} total rows")
            else:
                logger.warning(f"'Preço unitário' column not found in {schema_file}. Cannot filter totals")
                print(
                    f"Warning: 'Preço unitário' column not found in {schema_file}. Cannot filter totals."
                )
                # Decide if you want to continue or skip the file
                # continue

            if xl_dataframe.empty:
                logger.warning(f"No data left in {schema_file} after filtering totals")
                print(f"Warning: No data left in {schema_file} after filtering totals.")
                continue

            # --- Data Cleaning and Transformation ---
            logger.debug("Starting data cleaning and transformation")
            column_mapping = {
                "Produto": "nome_produto_raw",
                "Tipo": "tipo_produto",
                "Tipo de Evento": "tipo_evento",
                "Previsão de pagamento": "previsao_pagamento_raw",
                "Instituição": "instituicao_raw",
                "Conta": "conta_raw",
                "Quantidade": "quantidade_raw",
                "Preço unitário": "preco_unitario_raw",
                "Valor líquido": "valor_operacao_raw",  # Assuming 'Valor líquido' maps to 'valor_operacao'
            }

            rename_dict = {
                k: v for k, v in column_mapping.items() if k in xl_dataframe.columns
            }
            xl_dataframe = xl_dataframe[list(rename_dict.keys())].rename(
                columns=rename_dict
            )
            logger.debug(f"Mapped {len(rename_dict)} columns")

            # Handle missing 'Conta' column
            if "conta_raw" not in xl_dataframe.columns:
                logger.debug("'Conta' column missing, adding default value")
                xl_dataframe["conta"] = "000000000"
            else:
                xl_dataframe["conta"] = xl_dataframe["conta_raw"].apply(
                    deal_double_spaces
                )

            # Apply transformations
            xl_dataframe["nome_produto"] = xl_dataframe["nome_produto_raw"].apply(
                deal_double_spaces
            )
            xl_dataframe["codigo_produto"] = xl_dataframe["nome_produto"].apply(
                extract_product_id
            )
            logger.debug("Applied product name transformations")
            
            # 'tipo_produto' and 'tipo_evento' are directly mapped if they exist
            xl_dataframe["previsao_pagamento"] = pd.to_datetime(
                xl_dataframe["previsao_pagamento_raw"].apply(_str_to_date),
                errors="coerce",
            )
            xl_dataframe["instituicao"] = xl_dataframe["instituicao_raw"].apply(
                deal_double_spaces
            )

            # Convert numeric columns
            logger.debug("Converting numeric columns")
            xl_dataframe["quantidade"] = pd.to_numeric(
                xl_dataframe["quantidade_raw"], errors="coerce"
            )
            xl_dataframe["preco_unitario"] = pd.to_numeric(
                xl_dataframe["preco_unitario_raw"], errors="coerce"
            )
            xl_dataframe["valor_operacao"] = pd.to_numeric(
                xl_dataframe["valor_operacao_raw"], errors="coerce"
            )

            # Add metadata
            xl_dataframe["arquivo_origem"] = schema_file_name
            xl_dataframe["data_referencia"] = schema_file_date
            logger.debug(f"Added metadata: file='{schema_file_name}', date={schema_file_date}")

            # Ensure all expected columns exist before selecting
            for field in fields:
                if field not in xl_dataframe.columns:
                    xl_dataframe[field] = None  # Or pd.NA or appropriate default

            xl_dataframes.append(xl_dataframe[fields].copy())
            logger.debug(f"Added to results: {len(xl_dataframe)} rows")

        except ValueError as e:
            logger.error(f"ValueError processing file {schema_file}: {e}")
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error processing file {schema_file}: {e}", exc_info=True)
            print(f"An unexpected error occurred while processing {schema_file}: {e}")

    if not xl_dataframes:
        logger.warning("No valid dataframes to concatenate, returning empty DataFrame")
        return pd.DataFrame(columns=fields)

    logger.debug(f"Concatenating {len(xl_dataframes)} dataframes")
    result = pd.concat(xl_dataframes, ignore_index=True)
    logger.info(f"process_schema_eventos_provisionados() -> DataFrame with shape {result.shape}")
    return result

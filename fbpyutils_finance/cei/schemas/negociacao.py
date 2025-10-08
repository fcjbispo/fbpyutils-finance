"""
fbpyutils_finance.cei.schemas.negociacao - CEI Negociação Schema Processor

Purpose: This module provides functionality to process CEI 'Negociação de Ativos' (Asset Trading) Excel files, extracting and standardizing trading transaction data for analysis.

Main contents:
- process_schema_negociacao() (function): Process and consolidate trading data from Excel files

High-level usage pattern:
Import the function and call it with a list of CEI Excel file paths to get a consolidated DataFrame with processed trading data.

Examples:
>>> from fbpyutils_finance.cei.schemas.negociacao import process_schema_negociacao
>>> result = process_schema_negociacao(['negociacao-2023-01-15.xlsx'])
>>> isinstance(result, pd.DataFrame)
True
>>> len(result.columns) >= 10
True
"""

# fbpyutils_finance/cei/schemas/negociacao.py
import pandas as pd
from typing import List, Optional

from fbpyutils import xlsx as XL
from fbpyutils_finance import logger
from .utils import (
    _str_to_date,
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    # extract_product_id is not used here directly, but kept for consistency if needed later
)


def process_schema_negociacao(input_files: List[str]) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Negociação de Ativos' (Asset Trading) Excel files.

    Reads one or more 'negociacao-*.xlsx' files, extracts data, standardizes columns,
    performs type conversions, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Negociação' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                trading data. Returns an empty DataFrame if input_files
                                is empty or no valid files are processed.

    Examples:
        >>> result = process_schema_negociacao([])
        >>> isinstance(result, pd.DataFrame)
        True
        >>> len(result.columns)
        12
        >>> # Test with non-existent file (should handle gracefully)
        >>> result = process_schema_negociacao(['nonexistent.xlsx'])
        >>> isinstance(result, pd.DataFrame)
        True
    """
    logger.info(f"process_schema_negociacao(input_files={len(input_files)} files)")

    if not input_files:
        logger.debug("No input files provided, returning empty DataFrame")
        return pd.DataFrame()

    xl_dataframes = []
    fields = [
        "data_negocio",
        "movimentacao",
        "mercado",
        "prazo_vencimento",
        "instituicao",
        "conta",
        "codigo_produto",
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
            logger.debug(
                f"Extracted file info: name='{schema_file_name}', date={schema_file_date}"
            )

            # Basic check if it's a 'negociacao' file
            if "negociacao" not in schema_file_name:
                logger.warning(
                    f"Skipping file {schema_file} as it doesn't appear to be a 'negociacao' type"
                )
                print(
                    f"Warning: Skipping file {schema_file} as it doesn't appear to be a 'negociacao' type."
                )
                continue

            logger.debug(f"Loading Excel file: {schema_file}")
            xl_obj = XL.ExcelWorkbook(schema_file)
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))

            if not xl_table or len(xl_table) < 2:
                logger.warning(
                    f"Skipping file {schema_file} as it contains no data or header"
                )
                print(
                    f"Warning: Skipping file {schema_file} as it contains no data or header."
                )
                continue

            header = xl_table[0]
            data = xl_table[1:]
            xl_dataframe = pd.DataFrame(data, columns=header)
            logger.debug(f"Created DataFrame with shape: {xl_dataframe.shape}")

            # --- Data Cleaning and Transformation ---
            logger.debug("Starting data cleaning and transformation")
            column_mapping = {
                "Data do Negócio": "data_negocio_raw",
                "Tipo de Movimentação": "movimentacao",
                "Mercado": "mercado",
                "Prazo/Vencimento": "prazo_vencimento_raw",
                "Instituição": "instituicao_raw",
                "Conta": "conta_raw",
                "Código de Negociação": "codigo_produto",  # Directly use this as product code
                "Quantidade": "quantidade_raw",
                "Preço": "preco_unitario_raw",
                "Valor": "valor_operacao_raw",
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
            xl_dataframe["data_negocio"] = pd.to_datetime(
                xl_dataframe["data_negocio_raw"].apply(_str_to_date), errors="coerce"
            )
            # 'movimentacao', 'mercado', 'codigo_produto' are directly mapped
            xl_dataframe["prazo_vencimento"] = pd.to_datetime(
                xl_dataframe["prazo_vencimento_raw"].apply(_str_to_date),
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
            logger.debug(
                f"Added metadata: file='{schema_file_name}', date={schema_file_date}"
            )

            # Ensure all expected columns exist
            for field in fields:
                if field not in xl_dataframe.columns:
                    xl_dataframe[field] = None  # Or pd.NA

            xl_dataframes.append(xl_dataframe[fields].copy())
            logger.debug(f"Added to results: {len(xl_dataframe)} rows")

        except ValueError as e:
            logger.error(f"ValueError processing file {schema_file}: {e}")
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            logger.error(
                f"Unexpected error processing file {schema_file}: {e}", exc_info=True
            )
            print(f"An unexpected error occurred while processing {schema_file}: {e}")

    if not xl_dataframes:
        logger.warning(
            "No valid dataframes to concatenate, returning empty DataFrame with columns"
        )
        return pd.DataFrame(columns=fields)

    logger.debug(f"Concatenating {len(xl_dataframes)} dataframes")
    result = pd.concat(xl_dataframes, ignore_index=True)
    logger.info(f"process_schema_negociacao() -> DataFrame with shape {result.shape}")
    return result

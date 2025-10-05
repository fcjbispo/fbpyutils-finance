# fbpyutils_finance/cei/schemas/negociacao.py
import pandas as pd
from typing import List, Optional

from fbpyutils import xlsx as XL
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
    """
    if not input_files:
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
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)

            # Basic check if it's a 'negociacao' file
            if "negociacao" not in schema_file_name:
                print(
                    f"Warning: Skipping file {schema_file} as it doesn't appear to be a 'negociacao' type."
                )
                continue

            xl_obj = XL.ExcelWorkbook(schema_file)
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))

            if not xl_table or len(xl_table) < 2:
                print(
                    f"Warning: Skipping file {schema_file} as it contains no data or header."
                )
                continue

            header = xl_table[0]
            data = xl_table[1:]
            xl_dataframe = pd.DataFrame(data, columns=header)

            # --- Data Cleaning and Transformation ---
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

            # Handle missing 'Conta' column
            if "conta_raw" not in xl_dataframe.columns:
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

            # Ensure all expected columns exist
            for field in fields:
                if field not in xl_dataframe.columns:
                    xl_dataframe[field] = None  # Or pd.NA

            xl_dataframes.append(xl_dataframe[fields].copy())

        except ValueError as e:
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {schema_file}: {e}")

    if not xl_dataframes:
        return pd.DataFrame(columns=fields)

    return pd.concat(xl_dataframes, ignore_index=True)

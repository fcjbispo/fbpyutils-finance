# fbpyutils_finance/cei/schemas/posicao_etf.py
import pandas as pd
from typing import List, Optional
from datetime import date

from fbpyutils import xlsx as XL, string as SU
from .utils import (
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    # extract_product_id is not used here
)


def process_schema_posicao_etf(input_files: List[str]) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Posição' (Position) Excel files, specifically the 'ETF' sheet.

    Reads one or more 'posicao-*.xlsx' files, extracts data from the 'ETF' sheet,
    standardizes columns, performs type conversions, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Posição' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                ETF position data. Returns an empty DataFrame if input_files
                                is empty or the 'ETF' sheet is not found or has no data.
    """
    if not input_files:
        return pd.DataFrame()

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
        'preco_unitario', # Corresponds to 'Preço de Fechamento'
        'valor_operacao', # Corresponds to 'Valor Atualizado'
        'arquivo_origem',
        'data_referencia'
    ]

    xl_sheet_to_process = 'ETF'

    for schema_file in input_files:
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)

            if 'posicao' not in schema_file_name:
                 print(f"Warning: Skipping file {schema_file} as it doesn't appear to be a 'posicao' type.")
                 continue

            xl_obj = XL.ExcelWorkbook(schema_file)

            if xl_sheet_to_process in xl_obj.sheet_names:
                xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet_to_process)))

                if not xl_table or len(xl_table) < 2:
                    print(f"Warning: Sheet '{xl_sheet_to_process}' in {schema_file} contains no data or header.")
                    continue # Skip file if sheet is empty

                header = xl_table[0]
                data = xl_table[1:]
                xl_dataframe = pd.DataFrame(data, columns=header)

                if 'Produto' in xl_dataframe.columns:
                    xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()
                else:
                    print(f"Warning: 'Produto' column not found in sheet '{xl_sheet_to_process}' of {schema_file}.")
                    continue # Skip file if essential column is missing

                if xl_dataframe.empty:
                    print(f"Warning: No data left in sheet '{xl_sheet_to_process}' of {schema_file} after filtering.")
                    continue

                # --- Data Cleaning and Transformation ---
                column_mapping = {
                    'Código de Negociação': 'codigo_produto_raw',
                    'Produto': 'nome_produto_raw',
                    'Instituição': 'instituicao_raw',
                    'Conta': 'conta_raw',
                    'Código ISIN / Distribuição': 'codigo_isin',
                    'Tipo': 'tipo_produto',
                    'Quantidade': 'quantidade_raw',
                    'Quantidade Disponível': 'quantidade_disponivel_raw',
                    'Quantidade Indisponível': 'quantidade_indisponivel_raw',
                    'Motivo': 'motivo',
                    'Preço de Fechamento': 'preco_unitario_raw',
                    'Valor Atualizado': 'valor_operacao_raw',
                }

                rename_dict = {k: v for k, v in column_mapping.items() if k in xl_dataframe.columns}
                required_raw_cols = ['codigo_produto_raw', 'nome_produto_raw', 'instituicao_raw']
                if not all(col in rename_dict.values() for col in required_raw_cols):
                     print(f"Warning: Missing one or more essential columns in sheet '{xl_sheet_to_process}' of {schema_file}. Skipping file.")
                     continue

                xl_dataframe = xl_dataframe[list(rename_dict.keys())].rename(columns=rename_dict)

                # Handle missing 'Conta' column
                if 'conta_raw' not in xl_dataframe.columns:
                    xl_dataframe['conta'] = '000000000'
                else:
                    xl_dataframe['conta'] = xl_dataframe['conta_raw'].apply(deal_double_spaces)

                # Apply transformations
                xl_dataframe['codigo_produto'] = xl_dataframe['codigo_produto_raw'].apply(deal_double_spaces)
                xl_dataframe['nome_produto'] = xl_dataframe['nome_produto_raw'].apply(deal_double_spaces)
                xl_dataframe['instituicao'] = xl_dataframe['instituicao_raw'].apply(deal_double_spaces)
                # 'codigo_isin', 'tipo_produto', 'motivo' are directly mapped

                # Convert numeric columns
                xl_dataframe['quantidade'] = pd.to_numeric(xl_dataframe['quantidade_raw'], errors='coerce')
                xl_dataframe['quantidade_disponivel'] = pd.to_numeric(xl_dataframe['quantidade_disponivel_raw'], errors='coerce')
                xl_dataframe['quantidade_indisponivel'] = pd.to_numeric(xl_dataframe['quantidade_indisponivel_raw'], errors='coerce')
                xl_dataframe['preco_unitario'] = pd.to_numeric(xl_dataframe['preco_unitario_raw'], errors='coerce')
                xl_dataframe['valor_operacao'] = pd.to_numeric(xl_dataframe['valor_operacao_raw'], errors='coerce')

                # Add metadata
                normalized_sheet_name = SU.normalize_names([xl_sheet_to_process])[0]
                xl_dataframe['arquivo_origem'] = f'{schema_file_name}_{normalized_sheet_name}'
                xl_dataframe['data_referencia'] = schema_file_date

                # Ensure all expected columns exist
                for field in fields:
                    if field not in xl_dataframe.columns:
                        xl_dataframe[field] = None

                xl_dataframes.append(xl_dataframe[fields].copy())
            else:
                print(f"Info: Sheet '{xl_sheet_to_process}' not found in {schema_file}.")


        except ValueError as e:
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {schema_file}: {e}")

    if not xl_dataframes:
        return pd.DataFrame(columns=fields)

    return pd.concat(xl_dataframes, ignore_index=True)

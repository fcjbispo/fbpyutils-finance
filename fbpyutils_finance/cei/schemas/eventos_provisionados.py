# fbpyutils_finance/cei/schemas/eventos_provisionados.py
import pandas as pd
from typing import List, Optional
from datetime import date

from fbpyutils import xlsx as XL
from .utils import (
    _str_to_date,
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    extract_product_id,
)


def process_schema_eventos_provisionados(input_files: List[str]) -> Optional[pd.DataFrame]:
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
    """
    if not input_files:
        return pd.DataFrame() # Return empty DataFrame if no input files

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
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)

            # Basic check if it's an 'eventos' file (adjust if needed)
            if 'eventos' not in schema_file_name:
                 print(f"Warning: Skipping file {schema_file} as it doesn't appear to be an 'eventos' type.")
                 continue

            xl_obj = XL.ExcelWorkbook(schema_file)
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))

            if not xl_table or len(xl_table) < 2:
                print(f"Warning: Skipping file {schema_file} as it contains no data or header.")
                continue

            header = xl_table[0]
            data = xl_table[1:]
            xl_dataframe = pd.DataFrame(data, columns=header)

            # Filter out total rows before processing
            if 'Preço unitário' in xl_dataframe.columns:
                 xl_dataframe = xl_dataframe[xl_dataframe['Preço unitário'] != 'Total líquido'].copy()
            else:
                 print(f"Warning: 'Preço unitário' column not found in {schema_file}. Cannot filter totals.")
                 # Decide if you want to continue or skip the file
                 # continue

            if xl_dataframe.empty:
                print(f"Warning: No data left in {schema_file} after filtering totals.")
                continue

            # --- Data Cleaning and Transformation ---
            column_mapping = {
                'Produto': 'nome_produto_raw',
                'Tipo': 'tipo_produto',
                'Tipo de Evento': 'tipo_evento',
                'Previsão de pagamento': 'previsao_pagamento_raw',
                'Instituição': 'instituicao_raw',
                'Conta': 'conta_raw',
                'Quantidade': 'quantidade_raw',
                'Preço unitário': 'preco_unitario_raw',
                'Valor líquido': 'valor_operacao_raw', # Assuming 'Valor líquido' maps to 'valor_operacao'
            }

            rename_dict = {k: v for k, v in column_mapping.items() if k in xl_dataframe.columns}
            xl_dataframe = xl_dataframe[list(rename_dict.keys())].rename(columns=rename_dict)

            # Handle missing 'Conta' column
            if 'conta_raw' not in xl_dataframe.columns:
                xl_dataframe['conta'] = '000000000'
            else:
                xl_dataframe['conta'] = xl_dataframe['conta_raw'].apply(deal_double_spaces)

            # Apply transformations
            xl_dataframe['nome_produto'] = xl_dataframe['nome_produto_raw'].apply(deal_double_spaces)
            xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(extract_product_id)
            # 'tipo_produto' and 'tipo_evento' are directly mapped if they exist
            xl_dataframe['previsao_pagamento'] = pd.to_datetime(xl_dataframe['previsao_pagamento_raw'].apply(_str_to_date), errors='coerce')
            xl_dataframe['instituicao'] = xl_dataframe['instituicao_raw'].apply(deal_double_spaces)

            # Convert numeric columns
            xl_dataframe['quantidade'] = pd.to_numeric(xl_dataframe['quantidade_raw'], errors='coerce')
            xl_dataframe['preco_unitario'] = pd.to_numeric(xl_dataframe['preco_unitario_raw'], errors='coerce')
            xl_dataframe['valor_operacao'] = pd.to_numeric(xl_dataframe['valor_operacao_raw'], errors='coerce')

            # Add metadata
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            # Ensure all expected columns exist before selecting
            for field in fields:
                if field not in xl_dataframe.columns:
                    xl_dataframe[field] = None # Or pd.NA or appropriate default

            xl_dataframes.append(xl_dataframe[fields].copy())

        except ValueError as e:
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {schema_file}: {e}")

    if not xl_dataframes:
        return pd.DataFrame(columns=fields)

    return pd.concat(xl_dataframes, ignore_index=True)

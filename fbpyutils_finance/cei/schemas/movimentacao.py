# fbpyutils_finance/cei/schemas/movimentacao.py
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


def process_schema_movimentacao(input_files: List[str]) -> Optional[pd.DataFrame]:
    """
    Processes CEI 'Movimentação' (Transaction) Excel files.

    Reads one or more 'movimentacao-*.xlsx' files, extracts data, standardizes columns,
    performs type conversions, and concatenates them into a single DataFrame.

    Args:
        input_files (List[str]): A list of paths to the 'Movimentação' Excel files.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the consolidated and processed
                                transaction data, or None if no files are processed or
                                if an error occurs. Returns an empty DataFrame if input_files is empty.
    """
    if not input_files:
        return pd.DataFrame() # Return empty DataFrame if no input files

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
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)

            # Ensure it's actually a 'movimentacao' file based on extracted type
            if schema_file_name != 'movimentacao':
                 print(f"Warning: Skipping file {schema_file} as it doesn't appear to be a 'movimentacao' type.")
                 continue # Skip to the next file

            xl_obj = XL.ExcelWorkbook(schema_file)
            # Assuming the first sheet contains the data
            xl_table = _tuple_as_str(tuple(xl_obj.read_sheet_by_index(0)))

            if not xl_table or len(xl_table) < 2: # Check if table has header and at least one data row
                print(f"Warning: Skipping file {schema_file} as it contains no data or header.")
                continue

            header = xl_table[0]
            data = xl_table[1:]
            xl_dataframe = pd.DataFrame(data, columns=header)

            # --- Data Cleaning and Transformation ---
            # Rename and select columns using a mapping for robustness
            column_mapping = {
                'Entrada/Saída': 'entrada_saida',
                'Data': 'data_movimentacao_raw', # Keep raw date temporarily
                'Movimentação': 'movimentacao',
                'Produto': 'nome_produto_raw', # Keep raw product name temporarily
                'Instituição': 'instituicao_raw', # Keep raw institution temporarily
                'Conta': 'conta_raw', # Keep raw account temporarily
                'Quantidade': 'quantidade_raw',
                'Preço unitário': 'preco_unitario_raw',
                'Valor da Operação': 'valor_operacao_raw',
            }

            # Select and rename existing columns
            rename_dict = {k: v for k, v in column_mapping.items() if k in xl_dataframe.columns}
            xl_dataframe = xl_dataframe[list(rename_dict.keys())].rename(columns=rename_dict)

            # Handle missing 'Conta' column
            if 'conta_raw' not in xl_dataframe.columns:
                xl_dataframe['conta'] = '000000000' # Default account
            else:
                 xl_dataframe['conta'] = xl_dataframe['conta_raw'].apply(deal_double_spaces)

            # Apply transformations
            xl_dataframe['entrada_saida'] = xl_dataframe['entrada_saida'] # Already correct name
            xl_dataframe['data_movimentacao'] = pd.to_datetime(xl_dataframe['data_movimentacao_raw'].apply(_str_to_date), errors='coerce')
            xl_dataframe['movimentacao'] = xl_dataframe['movimentacao'] # Already correct name
            xl_dataframe['nome_produto'] = xl_dataframe['nome_produto_raw'].apply(deal_double_spaces)
            xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(extract_product_id)
            xl_dataframe['instituicao'] = xl_dataframe['instituicao_raw'].apply(deal_double_spaces)

            # Convert numeric columns
            xl_dataframe['quantidade'] = pd.to_numeric(xl_dataframe['quantidade_raw'], errors='coerce')
            xl_dataframe['preco_unitario'] = pd.to_numeric(xl_dataframe['preco_unitario_raw'], errors='coerce')
            xl_dataframe['valor_operacao'] = pd.to_numeric(xl_dataframe['valor_operacao_raw'], errors='coerce')

            # Add metadata
            xl_dataframe['arquivo_origem'] = schema_file_name
            xl_dataframe['data_referencia'] = schema_file_date

            # Select final columns and append
            xl_dataframes.append(xl_dataframe[fields].copy())

        except ValueError as e:
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {schema_file}: {e}")


    if not xl_dataframes:
        return pd.DataFrame(columns=fields) # Return empty DataFrame with correct columns if no files processed

    return pd.concat(xl_dataframes, ignore_index=True)

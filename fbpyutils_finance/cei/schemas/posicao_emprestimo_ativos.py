# fbpyutils_finance/cei/schemas/posicao_emprestimo_ativos.py
import pandas as pd
from typing import List, Optional
from datetime import date

from fbpyutils import xlsx as XL, string as SU
from .utils import (
    _str_to_date,
    _tuple_as_str,
    deal_double_spaces,
    extract_file_info,
    extract_product_id,
)


def process_schema_posicao_emprestimo_ativos(input_files: List[str]) -> Optional[pd.DataFrame]:
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
    """
    if not input_files:
        return pd.DataFrame()

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
        'preco_unitario', # Corresponds to 'Preço de Fechamento'
        'valor_operacao', # Corresponds to 'Valor Atualizado'
        'arquivo_origem',
        'data_referencia'
    ]

    # Sheets to check for asset lending data
    xl_sheets_to_process = ['Empréstimo de Ativos', 'Empréstimos']
    # Standardized sheet name for output file origin
    standardized_sheet_name_origin = 'Empréstimo_de_Ativos'


    for schema_file in input_files:
        try:
            schema_file_name, schema_file_date = extract_file_info(schema_file)

            if 'posicao' not in schema_file_name:
                 print(f"Warning: Skipping file {schema_file} as it doesn't appear to be a 'posicao' type.")
                 continue

            xl_obj = XL.ExcelWorkbook(schema_file)
            processed_sheets_in_file = []

            for xl_sheet in xl_sheets_to_process:
                if xl_sheet in xl_obj.sheet_names:
                    xl_table = _tuple_as_str(tuple(xl_obj.read_sheet(xl_sheet)))

                    if not xl_table or len(xl_table) < 2:
                        print(f"Warning: Sheet '{xl_sheet}' in {schema_file} contains no data or header.")
                        continue

                    header = xl_table[0]
                    data = xl_table[1:]
                    xl_dataframe = pd.DataFrame(data, columns=header)

                    if 'Produto' in xl_dataframe.columns:
                        xl_dataframe = xl_dataframe[xl_dataframe['Produto'] != ''].copy()
                    else:
                        print(f"Warning: 'Produto' column not found in sheet '{xl_sheet}' of {schema_file}.")
                        continue

                    if xl_dataframe.empty:
                        print(f"Warning: No data left in sheet '{xl_sheet}' of {schema_file} after filtering.")
                        continue

                    # --- Data Cleaning and Transformation ---
                    column_mapping = {
                        'Produto': 'nome_produto_raw',
                        'Instituição': 'instituicao_raw',
                        'Conta': 'conta_raw',
                        'Natureza': 'natureza_raw',
                        'Número de Contrato': 'contrato_raw',
                        'Modalidade': 'modalidade_raw',
                        'OPA': 'opa_raw',
                        'Liquidação antecipada': 'liquidacao_antecipada_raw',
                        'Taxa': 'taxa_raw',
                        'Comissão': 'comissao_raw',
                        'Data de registro': 'data_registro_raw',
                        'Data de vencimento': 'data_vencimento_raw',
                        'Quantidade': 'quantidade_raw',
                        'Preço de Fechamento': 'preco_unitario_raw',
                        'Valor Atualizado': 'valor_operacao_raw',
                    }

                    rename_dict = {k: v for k, v in column_mapping.items() if k in xl_dataframe.columns}
                    required_raw_cols = ['nome_produto_raw', 'instituicao_raw'] # Minimal check
                    if not all(col in rename_dict.values() for col in required_raw_cols):
                         print(f"Warning: Missing one or more essential columns in sheet '{xl_sheet}' of {schema_file}. Skipping sheet.")
                         continue

                    xl_dataframe = xl_dataframe[list(rename_dict.keys())].rename(columns=rename_dict)

                    # Handle missing 'Conta' column
                    if 'conta_raw' not in xl_dataframe.columns:
                        xl_dataframe['conta'] = '000000000'
                    else:
                        xl_dataframe['conta'] = xl_dataframe['conta_raw'].apply(deal_double_spaces)

                    # Apply transformations
                    xl_dataframe['nome_produto'] = xl_dataframe['nome_produto_raw'].apply(deal_double_spaces)
                    xl_dataframe['codigo_produto'] = xl_dataframe['nome_produto'].apply(extract_product_id) # Extract code from name
                    xl_dataframe['instituicao'] = xl_dataframe['instituicao_raw'].apply(deal_double_spaces)
                    xl_dataframe['natureza'] = xl_dataframe['natureza_raw'].apply(deal_double_spaces)
                    xl_dataframe['contrato'] = xl_dataframe['contrato_raw'].apply(deal_double_spaces)
                    xl_dataframe['modalidade'] = xl_dataframe['modalidade_raw'].apply(deal_double_spaces)
                    xl_dataframe['opa'] = xl_dataframe['opa_raw'].apply(deal_double_spaces)
                    xl_dataframe['liquidacao_antecipada'] = xl_dataframe['liquidacao_antecipada_raw'].apply(deal_double_spaces)

                    # Convert numeric and date columns
                    xl_dataframe['taxa'] = pd.to_numeric(xl_dataframe['taxa_raw'], errors='coerce')
                    xl_dataframe['comissao'] = pd.to_numeric(xl_dataframe['comissao_raw'], errors='coerce')
                    xl_dataframe['data_registro'] = pd.to_datetime(xl_dataframe['data_registro_raw'].apply(_str_to_date), errors='coerce')
                    xl_dataframe['data_vencimento'] = pd.to_datetime(xl_dataframe['data_vencimento_raw'].apply(_str_to_date), errors='coerce')
                    xl_dataframe['quantidade'] = pd.to_numeric(xl_dataframe['quantidade_raw'], errors='coerce')
                    xl_dataframe['preco_unitario'] = pd.to_numeric(xl_dataframe['preco_unitario_raw'], errors='coerce')
                    xl_dataframe['valor_operacao'] = pd.to_numeric(xl_dataframe['valor_operacao_raw'], errors='coerce')

                    # Add metadata
                    normalized_sheet_name = SU.normalize_names([standardized_sheet_name_origin])[0]
                    xl_dataframe['arquivo_origem'] = f'{schema_file_name}_{normalized_sheet_name}'
                    xl_dataframe['data_referencia'] = schema_file_date

                    # Ensure all expected columns exist
                    for field in fields:
                        if field not in xl_dataframe.columns:
                            xl_dataframe[field] = None

                    xl_dataframes.append(xl_dataframe[fields].copy())
                    processed_sheets_in_file.append(xl_sheet)
                    # Break after finding the first valid sheet (Empréstimo de Ativos or Empréstimos)
                    break

            if not processed_sheets_in_file:
                 print(f"Warning: No relevant sheets ({', '.join(xl_sheets_to_process)}) with data found in {schema_file}.")

        except ValueError as e:
            print(f"Error processing file {schema_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {schema_file}: {e}")

    if not xl_dataframes:
        return pd.DataFrame(columns=fields)

    return pd.concat(xl_dataframes, ignore_index=True)

import os
import csv
import sqlite3
import pandas as pd
from datetime import datetime
from typing import Dict, Optional, Tuple, List, Any
import re # Added import re

import fbpyutils.file as FU
from fbpyutils.debug import debug_info
from .utils import hash_string, is_nan_or_empty
# Import necessary functions from other new modules
# Need to import headers functions used here
from .headers import check_cvm_headers_changed, get_cvm_file_metadata
# Need to import processing functions used here
from .processing import get_expression_and_converters, apply_expressions, apply_converters

# --- Constantes ---
TARGET_ENCODING = 'utf-8'

# --- Funções de I/O de Arquivo ---

def build_target_file_name(metadata: Dict[str, Any], target_folder: str, index: Optional[int] = None, file_ext: Optional[str] = None) -> str:
    """
    Constructs the full path for a target file based on metadata.

    Uses 'kind' and 'href' from metadata. If index and file_ext are provided (for files within a zip),
    it incorporates them.

    Args:
        metadata (Dict[str, Any]): Metadata dictionary containing at least 'kind' and 'href'.
        target_folder (str): The base directory to save the file.
        index (Optional[int], optional): Index for files extracted from archives (e.g., zip). Defaults to None.
        file_ext (Optional[str], optional): Original extension of the file from archive. Defaults to None.

    Returns:
        str: The full path for the target file.
    """
    # Use href as the base, remove potential path components if any
    base_name = os.path.basename(metadata['href'])
    preffix = base_name.split('.')[0]
    original_ext = base_name.split('.')[-1] if '.' in base_name else 'txt' # Default extension

    if file_ext is not None and index is not None:
        # Handle files from zip: use original prefix, index, and provided extension
        index_str = str(index).zfill(4)
        target_file_name = f"{preffix}.{index_str}.{file_ext}"
    else:
        # Handle direct downloads: use original prefix and extension
        target_file_name = f"{preffix}.{original_ext}"

    # Prepend the 'kind'
    target_file_name = f"{metadata['kind'].lower()}.{target_file_name}"

    return os.path.join(target_folder, target_file_name)


def write_target_file(data: str, metadata: Dict[str, Any], target_folder: str, index: Optional[int] = None, file_ext: Optional[str] = None, encoding: str = TARGET_ENCODING) -> str:
    """
    Writes string data to a target file, constructing the filename using metadata.

    Args:
        data (str): The string data to write.
        metadata (Dict[str, Any]): Metadata used by build_target_file_name.
        target_folder (str): The directory to save the file in.
        index (Optional[int], optional): Index for files from archives. Defaults to None.
        file_ext (Optional[str], optional): Original extension for files from archives. Defaults to None.
        encoding (str, optional): Encoding to use for writing. Defaults to TARGET_ENCODING.

    Returns:
        str: The full path to the written file.

    Raises:
        IOError: If writing to the file fails.
    """
    target_file = build_target_file_name(metadata, target_folder, index, file_ext)
    try:
        os.makedirs(os.path.dirname(target_file), exist_ok=True) # Ensure directory exists
        with open(target_file, 'w', encoding=encoding) as f: # Use 'w' for text mode
            f.write(data)
        print(f"Successfully wrote file: {target_file}")
        return target_file
    except IOError as e:
        print(f"Error writing file {target_file}: {e}")
        raise # Re-raise the exception


def read_cvm_history_file(
    source_file: str,
    headers_df: pd.DataFrame,
    apply_conversions: bool = True,
    check_header: bool = False
) -> Tuple[str, str, pd.DataFrame, List[str]]:
    """
    Reads and processes a single CVM history data file based on predefined headers and mappings.

    Args:
        source_file (str): Path to the CVM history file (CSV format, ';' delimited).
        headers_df (pd.DataFrame): DataFrame containing the header mappings (loaded from HEADERS_FILE).
        apply_conversions (bool, optional): Whether to apply data type conversions defined in mappings. Defaults to True.
        check_header (bool, optional): Whether to verify if the file's header matches known mappings. Defaults to False.

    Returns:
        Tuple[str, str, pd.DataFrame, List[str]]: A tuple containing:
            - kind (str): The determined kind of the CVM data (e.g., 'IF_REGISTER').
            - sub_kind (str): The determined sub-kind (e.g., 'CAD_FI').
            - cvm_if_data (pd.DataFrame): The processed data with applied expressions and optionally converters.
            - partition_cols (List[str]): List of columns identified for partitioning (kind, sub_kind, year, period, etc.).

    Raises:
        ValueError: If header check fails, header hash not found, mappings/expressions missing,
                    invalid kind/sub-kind encountered, or other processing errors occur.
        FileNotFoundError: If the source_file does not exist.
        Exception: For unexpected errors during processing.
    """
    step = 'STARTING'
    try:
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Source file not found: {source_file}")

        step = 'CHECK FILE HEADER'
        if check_header:
            # Pass the existing headers DataFrame to avoid reloading it
            changed_hashes = check_cvm_headers_changed([source_file], headers_df)
            if changed_hashes:
                raise ValueError(f'Header changed for file {source_file}! Hashes: {changed_hashes}')

        step = 'GETTING METADATA FROM SOURCE FILE'
        kind, sub_kind, _, header_hash = get_cvm_file_metadata(source_file)

        if not header_hash:
            raise ValueError(f"Header hash not found for file: {source_file}")

        step = 'FILTERING HEADER MAPPINGS'
        mappings = headers_df[headers_df['Hash'] == header_hash].to_dict('records')
        if not mappings:
            raise ValueError(f"No header mappings found for hash {header_hash} in file {source_file}. Headers might have changed.")

        expressions, data_converters = get_expression_and_converters(mappings)

        if not expressions: # Mappings might exist but result in no expressions if all source fields are null
            raise ValueError(f'No expressions generated from mappings for hash {header_hash}. Check mappings for file {source_file}.')
        if apply_conversions and not data_converters:
            raise ValueError(f'No converters found for hash {header_hash}, but apply_converters is True. Check mappings for file {source_file}.')

        step = 'READING DATA FROM SOURCE FILE'
        try:
            # Specify low_memory=False for potentially mixed type columns
            if_data = pd.read_csv(source_file, sep=';', encoding=TARGET_ENCODING, dtype=str, quoting=csv.QUOTE_NONE, low_memory=False, on_bad_lines='warn')
        except Exception as read_err:
            raise ValueError(f"Failed to read CSV {source_file}: {read_err}")

        if if_data.empty:
            print(f"Warning: File {source_file} is empty.")
            # Return empty DataFrame matching expected structure
            # Determine expected columns from mappings
            expected_cols = [m['Target_Field'].lower() for m in mappings if m.get('Target_Field')]
            partition_cols = ['kind', 'sub_kind', 'year', 'period', 'period_date'] # Default potential partitions
            all_expected_cols = partition_cols + expected_cols
            empty_df = pd.DataFrame(columns=all_expected_cols)
            return kind, sub_kind, empty_df, partition_cols

        if_data.columns = [c.lower() for c in if_data.columns] # Normalize column names immediately

        step = 'APPLYING DATA EXPRESSIONS'
        cvm_if_data = apply_expressions(if_data, expressions=expressions)

        if apply_conversions:
            step = 'APPLYING DATA TYPES CONVERSIONS'
            cvm_if_data = apply_converters(cvm_if_data.copy(), data_converters) # Use copy to avoid SettingWithCopyWarning

        # Store original columns before adding partitioning ones
        cvm_if_data_cols = list(cvm_if_data.columns)

        cvm_if_data['kind'] = kind
        cvm_if_data['sub_kind'] = sub_kind

        step = 'COMPUTING PERIOD INFO'
        partition_cols = ['kind', 'sub_kind'] # Base partition columns

        # Safely access columns for period calculation
        if 'position_date' in cvm_if_data.columns and not cvm_if_data['position_date'].isnull().all():
            try:
                # Ensure it's datetime before formatting
                pos_date_dt = pd.to_datetime(cvm_if_data['position_date'], errors='coerce')
                cvm_if_data['year'] = pos_date_dt.dt.strftime('%Y')
                cvm_if_data['period'] = pos_date_dt.dt.strftime('%Y-%m')
                partition_cols.extend(['year', 'period'])
            except Exception as e:
                print(f"Warning: Could not compute period info from 'position_date' in {source_file}: {e}")
        elif 'start_date' in cvm_if_data.columns and not cvm_if_data['start_date'].isnull().all():
            try:
                start_date_dt = pd.to_datetime(cvm_if_data['start_date'], errors='coerce')
                cvm_if_data['year'] = start_date_dt.dt.strftime('%Y')
                cvm_if_data['period'] = start_date_dt.dt.strftime('%Y-%m')
                partition_cols.extend(['year', 'period'])
            except Exception as e:
                print(f"Warning: Could not compute period info from 'start_date' in {source_file}: {e}")
        elif sub_kind == 'CAD_FI': # Special handling for CAD_FI based on filename date
            try:
                file_name = os.path.basename(source_file)
                # Expected format: kind.inf_cadastral_fi_YYYYMMDD.csv or kind.cad_fi.csv
                parts = file_name.split('.')
                date_part_str = None
                if len(parts) >= 3 and parts[1].startswith('inf_cadastral_fi_'):
                    date_part_str = parts[1].split('_')[-1] # YYYYMMDD
                    date_format = '%Y%m%d'
                elif len(parts) >= 2 and parts[1] == 'cad_fi': # Current file, use today's date
                    date_part_str = datetime.now().strftime('%Y%m%d')
                    date_format = '%Y%m%d'

                if date_part_str:
                    period_date = pd.to_datetime(date_part_str, format=date_format)
                    cvm_if_data['year'] = period_date.strftime("%Y")
                    cvm_if_data['period'] = period_date.strftime("%Y-%m")
                    cvm_if_data['period_date'] = period_date.strftime('%Y-%m-%d')
                    partition_cols.extend(['year', 'period', 'period_date'])
                else:
                    print(f"Warning: Could not extract date from filename for CAD_FI: {file_name}")

            except Exception as e:
                print(f"Warning: Error computing period info for CAD_FI file {source_file}: {e}")
        # else: # No date column found for period calculation
        #     print(f"Warning: No suitable date column found for period calculation in {source_file}")

        # Ensure all potential partition columns exist before selecting
        final_cols = []
        for col in partition_cols + cvm_if_data_cols:
            if col in cvm_if_data.columns and col not in final_cols:
                final_cols.append(col)

        step = 'SELECTING DATA TO RETURN'
        return kind, sub_kind, cvm_if_data[final_cols], partition_cols

    except Exception as E:
        info = debug_info(E)
        # Add source file context to the error message
        raise ValueError(f'Failed processing CVM history file "{source_file}" at step {step}: {E} ({info})')

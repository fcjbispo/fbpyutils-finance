# fbpyutils_finance/cvm/converters.py
"""
Converter functions used for processing CVM data fields.

These functions are typically referenced by name (as strings) in the header mapping files
(e.g., 'if_header_mappings.xlsx') and evaluated during the data processing pipeline
(specifically within `processing.get_expression_and_converters` and `processing.apply_converters`).

They handle type casting, cleaning, and basic validation for common CVM data patterns.
"""

import re
import pandas as pd
from datetime import datetime
from typing import Optional, Union, Any

# --- Basic Type Converters ---

def as_int(value: Any) -> Optional[int]:
    """
    Converts value to integer, returning None on failure or for NaN/empty inputs.

    Handles strings with thousands separators ('.') and potential decimal parts (',' or '.')
    before converting to float and then int.
    """
    if pd.isna(value) or value == '':
        return None
    try:
        if isinstance(value, str):
            # Standardize number string: remove '.', treat ',' as '.'
            cleaned_value = value.replace('.', '').replace(',', '.')
            # Handle potential non-numeric chars remaining (though make_number_type usually handles this)
            cleaned_value = re.sub(r'[^\d.]', '', cleaned_value)
            if not cleaned_value: return None
            # Convert to float first to handle decimals, then to int
            return int(float(cleaned_value))
        elif isinstance(value, (int, float)):
             # Direct conversion for numbers, truncating float part
             return int(value)
        else:
             # Try converting other types via string representation
             return int(str(value))
    except (ValueError, TypeError):
        # print(f"Debug: Failed as_int conversion for value '{value}'") # Optional debug
        return None

def as_float(value: Any) -> Optional[float]:
    """
    Converts value to float, returning None on failure or for NaN/empty inputs.

    Handles common CVM number formats (e.g., using '.' for thousands, ',' for decimal).
    """
    if pd.isna(value) or value == '':
        return None
    try:
        if isinstance(value, str):
            # Standardize number string: remove '.', treat ',' as '.'
            cleaned_value = value.replace('.', '').replace(',', '.')
            # Handle potential non-numeric chars remaining
            cleaned_value = re.sub(r'[^\d.]', '', cleaned_value)
            if not cleaned_value: return None
            return float(cleaned_value)
        else:
            # Direct conversion for numbers or other types
            return float(value)
    except (ValueError, TypeError):
        # print(f"Debug: Failed as_float conversion for value '{value}'") # Optional debug
        return None

def as_str(value: Any) -> Optional[str]:
    """
    Converts value to a stripped string, returning None if value is NaN/None.
    """
    if pd.isna(value):
        return None
    try:
        # Ensure conversion to string and remove leading/trailing whitespace
        return str(value).strip()
    except Exception:
        # Catch potential errors during string conversion of unusual types
        return None

def as_date(value: Any, fmt: Optional[str] = None) -> Optional[datetime.date]:
    """
    Converts value to a date object, returning None on failure or for NaN/empty inputs.

    Handles datetime inputs, specific formats, common CVM formats ('YYYY-MM-DD'),
    and uses pandas.to_datetime as a fallback.
    """
    if pd.isna(value) or value == '':
        return None
    if isinstance(value, datetime):
        return value.date() # Extract date part if already datetime

    date_str = str(value).strip()
    dt = None

    try:
        # If a specific format is provided, use it first
        if fmt:
            try:
                 dt = datetime.strptime(date_str, fmt)
                 return dt.date()
            except ValueError:
                 pass # Try other methods if specific format fails

        # Try common CVM format: YYYY-MM-DD
        if dt is None:
            try:
                 dt = datetime.strptime(date_str, '%Y-%m-%d')
                 return dt.date()
            except ValueError:
                 pass # Try pandas fallback

        # Fallback to pandas to_datetime which handles more formats
        if dt is None:
            pd_dt = pd.to_datetime(date_str, errors='coerce')
            if pd.notna(pd_dt):
                 # Ensure it's converted to standard Python datetime object then get date
                 return pd_dt.to_pydatetime().date()
            else:
                 # print(f"Debug: Failed as_date conversion (pandas) for value '{value}'") # Optional debug
                 return None

    except (ValueError, TypeError, AttributeError):
        # Catch various errors during parsing or attribute access
        # print(f"Debug: Failed as_date conversion (general) for value '{value}'") # Optional debug
        return None
    # Should not be reached if logic is correct, but as safety net
    return None


def as_datetime(value: Any, fmt: Optional[str] = None) -> Optional[datetime]:
    """
    Converts value to a datetime object, returning None on failure or for NaN/empty inputs.

    Handles datetime inputs, specific formats, common CVM formats ('YYYY-MM-DD HH:MM:SS', 'YYYY-MM-DD'),
    and uses pandas.to_datetime as a fallback.
    """
    if pd.isna(value) or value == '':
        return None
    if isinstance(value, datetime):
        return value # Return as is if already datetime

    datetime_str = str(value).strip()
    dt = None

    try:
        # If a specific format is provided, use it first
        if fmt:
            try:
                 dt = datetime.strptime(datetime_str, fmt)
                 return dt
            except ValueError:
                 pass # Try other methods if specific format fails

        # Try common CVM formats
        common_formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d']
        if dt is None:
            for cf in common_formats:
                 try:
                      dt = datetime.strptime(datetime_str, cf)
                      break # Stop if format matches
                 except ValueError:
                      continue
            if dt:
                 return dt

        # Fallback to pandas to_datetime
        if dt is None:
            pd_dt = pd.to_datetime(datetime_str, errors='coerce')
            if pd.notna(pd_dt):
                 # Ensure it's converted to standard Python datetime object
                 return pd_dt.to_pydatetime()
            else:
                 # print(f"Debug: Failed as_datetime conversion (pandas) for value '{value}'") # Optional debug
                 return None

    except (ValueError, TypeError, AttributeError):
        # Catch various errors during parsing or attribute access
        # print(f"Debug: Failed as_datetime conversion (general) for value '{value}'") # Optional debug
        return None
    # Should not be reached
    return None


def as_bool(value: Any) -> Optional[bool]:
    """
    Converts value to boolean, returning None on failure or for NaN/empty inputs.

    Handles common string representations ('S'/'N', 'SIM'/'NAO', 'TRUE'/'FALSE', '1'/'0').
    Case-insensitive.
    """
    if pd.isna(value):
        return None

    # Convert to string and normalize case/whitespace
    val_str = str(value).strip().upper()

    if val_str in ('S', 'SIM', 'TRUE', '1', 'T', 'Y', 'YES', 'VERDADEIRO'):
        return True
    elif val_str in ('N', 'NAO', 'NÃO', 'FALSE', '0', 'F', 'NO', 'FALSO'):
        return False
    else:
        # Cannot determine boolean value
        # print(f"Debug: Failed as_bool conversion for value '{value}'") # Optional debug
        return None

# --- Specific CVM Field Converters ---

def clean_cnpj(value: Any) -> Optional[str]:
    """
    Removes formatting from CNPJ string, returning only digits or None if invalid.

    Validates length (14 digits).
    """
    if pd.isna(value):
        return None
    try:
        cnpj_str = str(value)
        # Remove common formatting characters: '.', '/', '-'
        cleaned_cnpj = re.sub(r'[./-]', '', cnpj_str)
        # Validate: must be exactly 14 digits
        if len(cleaned_cnpj) == 14 and cleaned_cnpj.isdigit():
            return cleaned_cnpj
        else:
            # print(f"Debug: Failed clean_cnpj validation for value '{value}' -> '{cleaned_cnpj}'") # Optional debug
            return None
    except Exception:
        # Catch potential errors during string conversion or regex
        return None

def as_string_id(value: Any) -> Optional[str]:
    """
    Converts a value to a string and removes specific characters ('/', '-', '.').

    Useful for cleaning identifiers like CNPJ before validation or use.

    Args:
        value (Any): The value to convert.

    Returns:
        Optional[str]: A string representation of the input with specific characters removed,
                       or None if the input is NaN or empty.
    """
    if pd.isna(value) or value == '':
        return None
    else:
        # Use regex for efficient removal of multiple characters
        return re.sub(r'[./-]', '', str(value))

# --- Add more specific converters as needed based on CVM data fields ---

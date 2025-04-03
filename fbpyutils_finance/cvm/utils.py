import re
from datetime import datetime
from typing import Union, Type, Any, Optional

from fbpyutils import string as SU

# --- Funções Utilitárias ---

def get_value_by_index_if_exists(data_list: list, index: int, default: Optional[Any] = None) -> Optional[Any]:
    """
    Returns the value at a specific index in a list if it exists, otherwise returns a default value.

    Args:
        data_list (list): The input list.
        index (int): The index to retrieve the value from.
        default (Optional[Any], optional): The default value to return if the index is out of range
                                           or the list is empty. Defaults to None.

    Returns:
        Optional[Any]: The value at the specified index or the default value.
    """
    return data_list[index] if len(data_list) > index else default

def make_number_type(value: Optional[str], num_type: Type[Union[int, float]] = int) -> Optional[Union[int, float]]:
    """
    Converts a string representation of a number to a specified number type (int or float).

    Handles cases where the input is None or '-', returning None. Removes non-numeric characters
    before conversion.

    Args:
        value (Optional[str]): The input string value to be converted.
        num_type (Type[Union[int, float]], optional): The target number type (int or float).
                                                     Defaults to int.

    Returns:
        Optional[Union[int, float]]: The converted number or None if conversion is not possible.
    """
    if value is None or value == '-':
        return None
    try:
        # Remove any non-digit characters except for potential decimal points if float
        cleaned_value = re.sub(r'[^\d.]' if num_type is float else r'[^\d]', '', value)
        return num_type(cleaned_value) if cleaned_value else None
    except (ValueError, TypeError):
        return None # Handle potential conversion errors

def timelapse(start_time: datetime) -> float:
    """
    Calculates the time elapsed in minutes between the current time and a given start time.

    Args:
        start_time (datetime): The starting datetime.

    Returns:
        float: The time elapsed in minutes, rounded to 4 decimal places.
    """
    return round((datetime.now() - start_time).total_seconds() / 60, 4)

def make_str_datetime(dt_obj: Optional[datetime], fmt: str = '%Y-%m-%d %H:%M:%S') -> Optional[str]:
    """
    Converts a datetime object into a formatted string.

    Args:
        dt_obj (Optional[datetime]): The datetime object to format. If None, returns None.
        fmt (str, optional): The desired format string. Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        Optional[str]: The formatted datetime string or None if input is None or formatting fails.
    """
    if dt_obj is None:
        return None
    try:
        return dt_obj.strftime(fmt)
    except (ValueError, TypeError):
        # Handle potential errors during formatting (e.g., invalid format string)
        return None

def replace_all(text: str, old: str, new: str) -> str:
    """
    Replace all occurrences of a substring `old` with `new` in the string `text`.

    Args:
        text (str): The input string.
        old (str): The substring to be replaced.
        new (str): The replacement string.

    Returns:
        str: The string with all occurrences of `old` replaced by `new`.
    """
    if not old: # Avoid infinite loop if old is empty
        return text
    while old in text:
        text = text.replace(old, new)
    return text

def make_datetime(date_str: Optional[str], time_str: Optional[str]) -> Optional[datetime]:
    """
    Converts separate date and time strings into a single datetime object.

    Assumes date format 'DD-Mon-YYYY' (e.g., '29-Jan-2023') and time format 'HH:MM'.

    Args:
        date_str (Optional[str]): The date string (e.g., '29-Jan-2023').
        time_str (Optional[str]): The time string (e.g., '08:30').

    Returns:
        Optional[datetime]: The combined datetime object, or None if either input is None
                           or parsing fails.
    """
    if not date_str or not time_str:
        return None
    try:
        dt_str = f"{date_str} {time_str}"
        return datetime.strptime(dt_str, "%d-%b-%Y %H:%M")
    except ValueError:
        # Handle potential parsing errors if format doesn't match
        return None

def hash_string(input_string: str) -> str:
    """
    Generates a SHA-256 hash for the input string.

    Args:
        input_string (str): The string to hash.

    Returns:
        str: The hexadecimal representation of the SHA-256 hash.
    """
    return SU.hash_string(input_string)

def is_nan_or_empty(value: Any) -> bool:
    """
    Checks if a value is NaN (Not a Number), None, or an empty string.

    Args:
        value: The value to check.

    Returns:
        bool: True if the value is NaN, None, or empty, False otherwise.
    """
    import pandas as pd # Local import to avoid circular dependency if utils is imported widely
    return pd.isna(value) or value == ''

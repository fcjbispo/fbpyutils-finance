# fbpyutils_finance/investidor10/utils.py
from typing import Any, Optional, Union
from bs4.element import Tag

def tag_to_str(tag: Union[Tag, Any]) -> str:
    """
    Convert a BeautifulSoup Tag object or any object to its string representation,
    removing newline characters and stripping leading/trailing whitespace.

    Args:
        tag (Union[Tag, Any]): The BeautifulSoup Tag object or any object to convert.

    Returns:
        str: The cleaned text representation of the tag or object.
    """
    if isinstance(tag, Tag):
        return tag.text.replace('\n', '').strip()
    return str(tag).replace('\n', '').strip()


def any_to_number(value: Any) -> Optional[float]:
    """
    Convert a given value to a numeric representation (float).

    Handles values like 'R$ 1.234,56', '1.234,56 %', '1234.56', '-', etc.

    Args:
        value (Any): The value to convert. It will be converted to string first.

    Returns:
        Optional[float]: The numeric representation of the value as a float,
                         or None if the value represents '-', cannot be parsed,
                         or results in an empty string after cleaning.
    """
    str_value = str(value).strip()
    if str_value == '-':
        return None

    # Take the part after the last space (e.g., 'R$ 1.234,56' -> '1.234,56')
    numeric_part = str_value.split(' ')[-1]

    # Remove thousand separators (.), replace decimal comma (,) with dot (.), remove '%'
    cleaned_value = numeric_part.replace('.', '').replace(',', '.').replace('%', '')

    if not cleaned_value:
        return None

    try:
        return float(cleaned_value)
    except ValueError:
        # Return None if conversion fails
        return None

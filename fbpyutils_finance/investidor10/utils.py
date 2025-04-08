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
    if str_value == '-' or str_value == '':
        return None

    # Remove percent sign and spaces inside the string
    cleaned_str = str_value.replace('%', '').strip()

    # Remove currency symbols and other prefixes, keep only number parts
    # Take the last token with digits or separators
    tokens = cleaned_str.split()
    numeric_part = ''
    for token in reversed(tokens):
        if any(c.isdigit() for c in token):
            numeric_part = token
            break
    if not numeric_part:
        return None

    # Always treat comma as decimal separator (Brazilian format)
    if ',' in numeric_part:
        # Remove all thousand separators (.) and replace decimal comma with dot
        cleaned_value = numeric_part.replace('.', '').replace(',', '.')
    else:
        # Heuristic for thousands separator in Brazilian format without decimal comma
        parts = numeric_part.split('.')
        if len(parts) > 1:
            last_part = parts[-1]
            if len(last_part) == 3 and all(p.isdigit() for p in parts):
                cleaned_value = ''.join(parts)
            else:
                cleaned_value = numeric_part.replace(',', '')
        else:
            cleaned_value = numeric_part.replace(',', '')

    if not cleaned_value:
        return None

    try:
        return float(cleaned_value)
    except ValueError:
        return None

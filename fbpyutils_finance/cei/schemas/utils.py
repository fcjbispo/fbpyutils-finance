"""
Utilitários para processamento de dados do CEI (Canal Eletrônico do Investidor).

Este módulo fornece funções utilitárias para conversão de dados, extração de informações
de arquivos e processamento de strings utilizados no processamento de dados do CEI.

Exemplos:
    >>> from fbpyutils_finance.cei.schemas.utils import deal_double_spaces, extract_file_info, extract_product_id
    >>> # Remover espaços duplos
    >>> deal_double_spaces("Texto  com  espaços  duplos")
    'Texto com espaços duplos'

    >>> # Extrair informações do arquivo
    >>> extract_file_info("posicao-2023-01-15.xlsx")
    ('posicao', datetime.date(2023, 1, 15))

    >>> # Extrair código do produto
    >>> extract_product_id("PETR4 - PETROBRAS PN N2")
    'PETROBRAS PN N2'
"""

import os
import re
from datetime import date, datetime
from typing import List, Tuple, Optional, Any, Callable

from fbpyutils_finance import logger

# Lambdas for common data conversions in CEI files
_str_to_date: Callable[[str], Optional[date]] = (
    lambda x: None if x in ["-"] else datetime.strptime(x, "%d/%m/%Y").date()
)
_str_to_number: Callable[[Any], Optional[float]] = (
    lambda x: None
    if x in ["-"]
    else float(str(x).replace(".", "~").replace(",", ".").replace("~", ""))
)
_str_to_integer: Callable[[Any], Optional[int]] = (
    lambda x: int(val) if (val := _str_to_number(x)) is not None else None
)
_tuple_as_str: Callable[[Tuple[Tuple[Any, ...], ...]], List[List[str]]] = lambda x: [
    [str(c).strip() for c in l] for l in x
]


def deal_double_spaces(x: Any) -> str:
    """
    Replaces consecutive double spaces in a string with single spaces.

    Args:
        x (Any): The input value (will be converted to string).

    Returns:
        str: The string with consecutive spaces collapsed.

    Examples:
        >>> deal_double_spaces("Texto  com  espaços  duplos")
        'Texto com espaços duplos'

        >>> deal_double_spaces("Texto normal")
        'Texto normal'

        >>> deal_double_spaces(123)
        '123'
    """
    logger.debug(f"deal_double_spaces: input={x}")
    x_str, ss, s = str(x), "  ", " "

    while ss in x_str:
        x_str = x_str.replace(ss, s)

    logger.debug(f"deal_double_spaces: output={x_str}")
    return x_str


def extract_file_info(schema_file: str) -> Tuple[str, date]:
    """
    Extracts the report type and reference date from a CEI Excel filename.

    Assumes filename format like 'movimentacao-YYYY-MM-DD.xlsx' or
    'posicao-YYYY-MM-DD-HH-MM-SS.xlsx'.

    Args:
        schema_file (str): The full path to the CEI Excel file.

    Returns:
        Tuple[str, date]: A tuple containing (report_type, reference_date).

    Raises:
        ValueError: If the filename format is not recognized or the date is invalid.

    Examples:
        >>> extract_file_info("posicao-2023-01-15.xlsx")
        ('posicao', datetime.date(2023, 1, 15))

        >>> extract_file_info("movimentacao-2023-12-31.xlsx")
        ('movimentacao', datetime.date(2023, 12, 31))

        >>> extract_file_info("posicao-2023-01-15-14-30-45.xlsx")
        ('posicao', datetime.date(2023, 1, 15))
    """
    logger.info(f"extract_file_info: schema_file={schema_file}")
    cei_file_name = schema_file.split(os.path.sep)[-1].split(".")[0]
    logger.debug(f"extract_file_info: cei_file_name={cei_file_name}")

    # Search for the year (4 digits) to separate type and date parts
    match = re.search(r"\b\d{4}\b", cei_file_name)
    if match:
        cei_file_type = cei_file_name[0 : match.start() - 1]
        cei_file_date_str = cei_file_name[match.start() :]
        logger.debug(
            f"extract_file_info: type={cei_file_type}, date_str={cei_file_date_str}"
        )

        # Handle cases like 'prefix-YYYY-MM-DD-a-YYYY-MM-DD'
        if "-a-" in cei_file_date_str:
            cei_file_date_str = cei_file_date_str.split("-a-")[-1]
            logger.debug(f"extract_file_info: adjusted date_str={cei_file_date_str}")

        # Parse date based on length
        try:
            if len(cei_file_date_str) == 10:  # YYYY-MM-DD
                cei_file_date = datetime.strptime(cei_file_date_str, "%Y-%m-%d")
                logger.debug(
                    f"extract_file_info: parsed date (YYYY-MM-DD)={cei_file_date}"
                )
            elif len(cei_file_date_str) == 19:  # YYYY-MM-DD-HH-MM-SS
                cei_file_date = datetime.strptime(
                    cei_file_date_str, "%Y-%m-%d-%H-%M-%S"
                )
                logger.debug(
                    f"extract_file_info: parsed date (with time)={cei_file_date}"
                )
            else:
                raise ValueError(f"Invalid date format in filename: {cei_file_name}")
        except ValueError as e:
            logger.error(
                f"extract_file_info: Invalid date in filename: {cei_file_name}",
                exc_info=True,
            )
            raise ValueError(f"Invalid date in filename: {cei_file_name}") from e

        result = (cei_file_type, cei_file_date.date())
        logger.info(f"extract_file_info: returning {result}")
        return result
    else:
        logger.error(f"extract_file_info: Invalid filename format: {cei_file_name}")
        raise ValueError(f"Invalid filename format: {cei_file_name}")


def extract_product_id(product: str, sep: str = "-") -> str:
    """
    Extracts a simplified product identifier from the CEI product description string.

    Handles cases like 'Tesouro ...', 'Some Stock - XYZW3', 'Futuro - ABCZ9'.

    Args:
        product (str): The product description string from the CEI file.
        sep (str, optional): The separator used between the description and the code. Defaults to '-'.

    Returns:
        str: The extracted product identifier (e.g., 'Tesouro ...', 'XYZW3', 'ABCZ9').

    Examples:
        >>> extract_product_id("PETR4 - PETROBRAS PN N2")
        'PETROBRAS PN N2'

        >>> extract_product_id("Tesouro IPCA+ 2045")
        'Tesouro IPCA+ 2045'

        >>> extract_product_id("VALE3")
        'VALE3'

        >>> extract_product_id("Futuro - WINZ23")
        'WINZ23'
    """
    logger.debug(f"extract_product_id: product='{product}', sep='{sep}'")

    if not isinstance(product, str):
        logger.warning("extract_product_id: non-string input, returning empty string")
        return ""  # Return empty string or handle non-string input appropriately

    product = product.strip()
    logger.debug(f"extract_product_id: trimmed product='{product}'")

    if "Tesouro" in product:
        logger.debug("extract_product_id: Tesouro product, returning full name")
        return product  # Keep the full name for Tesouro products

    product_parts = product.split(sep)
    logger.debug(f"extract_product_id: product_parts={product_parts}")

    if len(product_parts) < 2 and "Futuro" not in product_parts[0]:
        # If no separator and not a future, return the original (trimmed) string
        # or handle as an error/default case if needed
        logger.debug(
            "extract_product_id: no separator and not future, returning original"
        )
        return product

    # Let's refine: Assume the code is usually the *last* part after the separator,
    # unless it's a Tesouro product.
    if len(product_parts) > 1:
        # Take the last part as the potential code
        potential_code = product_parts[-1].strip()
        logger.debug(f"extract_product_id: potential_code='{potential_code}'")

        # Basic check if it looks like a ticker (e.g., 4 letters + 1 or 2 digits)
        if re.match(r"^[A-Z]{4}\d{1,2}$", potential_code):
            logger.debug(
                f"extract_product_id: matched ticker pattern, returning '{potential_code}'"
            )
            return potential_code
        # If 'Futuro' is mentioned, assume the last part is the code
        elif "Futuro" in product:
            logger.debug(
                f"extract_product_id: Futuro product, returning '{potential_code}'"
            )
            return potential_code
        # Otherwise, maybe return the original product or the first part?
        # Let's stick to the original logic's *intent* which seemed to target specific formats.
        # Re-implementing original logic carefully:
        if "Futuro" in product_parts[0] and len(product_parts) > 1:
            result = product_parts[1].strip()  # Code is after separator for Futuros
            logger.debug(
                f"extract_product_id: Futuro in first part, returning '{result}'"
            )
            return result
        elif len(product_parts) > 0:
            # For non-Futuros, if there's a separator, the original code took index 0.
            # This seems wrong. Let's assume the code is the *first* part if it looks like one,
            # or the *last* part otherwise if a separator exists.
            first_part = product_parts[0].strip()
            if re.match(r"^[A-Z]{4}\d{1,2}$", first_part):
                logger.debug(
                    f"extract_product_id: first part matches ticker, returning '{first_part}'"
                )
                return first_part
            elif len(product_parts) > 1:
                result = product_parts[-1].strip()  # Fallback to last part
                logger.debug(
                    f"extract_product_id: fallback to last part, returning '{result}'"
                )
                return result
            else:
                logger.debug(
                    f"extract_product_id: no separator, returning first part '{first_part}'"
                )
                return first_part  # No separator, return the whole thing
        else:
            logger.debug(
                f"extract_product_id: empty parts, returning original '{product}'"
            )
            return product  # Should not happen if product is not empty

    logger.debug(f"extract_product_id: fallback, returning original '{product}'")
    return product  # Fallback if no parts or other conditions met

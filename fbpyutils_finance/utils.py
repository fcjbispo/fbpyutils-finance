"""
fbpyutils_finance.utils - General Utility Functions

Purpose: This module contains miscellaneous utility functions used across the fbpyutils_finance package for data conversion, list handling, HTTP headers for scraping, and database connection validation.

Main contents:
- numberize(): Converts string or number with commas to float
- first_or_none(): Returns first item of list or None if empty
- random_header(): Generates random HTTP headers for web requests
- is_valid_db_connection(): Checks if an object has a callable 'execute' method like a DB connection

High-level usage pattern:
Import utilities as needed, e.g., from fbpyutils_finance.utils import numberize, random_header. Use for data cleaning, safe list access, or request headers.

Examples:
>>> from fbpyutils_finance.utils import numberize, first_or_none
>>> num = numberize("1,234.56")
>>> print(num)
1234.56
>>> items = [1, 2, 3]
>>> first = first_or_none(items)
>>> print(first)
1
>>> empty_first = first_or_none([])
>>> print(empty_first)
None
"""


import random
from typing import Any, Dict, List, Optional

from fbpyutils_finance import logger


def numberize(value: Any) -> float:
    """
    Converts a string or number containing commas to a float.

    Args:
        value (Any): The value to convert (string or number).

    Returns:
        float: The converted float value.

    Examples:
        >>> numberize("1,234.56")
        1234.56
        Minimal usage: Converts string with commas to float, returns 1234.56 for input "1,234.56".
    """
    logger.info(f"numberize entry: value={value}")
    result = float(str(value).replace(",", ""))
    logger.info(f"numberize exit: returning {result}")
    return result


def first_or_none(items: List[Any]) -> Optional[Any]:
    """
    Returns the first item of a list or None if the list is empty.

    Args:
        items (List[Any]): The input list.

    Returns:
        Optional[Any]: The first item or None.

    Examples:
        >>> first_or_none([1, 2, 3])
        1
        >>> first_or_none([])
        None
        Minimal usage: Returns first item or None if empty, returns 1 for [1,2,3], None for [].
    """
    logger.info(f"first_or_none entry: items_len={len(items)}")
    result = None if len(items) == 0 else items[0]
    logger.info(f"first_or_none exit: returning {result}")
    return result


def random_header() -> Dict[str, str]:
    """
    Returns a randomly chosen dictionary of HTTP headers for web scraping.

    Returns:
        Dict[str, str]: A dictionary containing common HTTP headers.

    Examples:
        >>> headers = random_header()
        >>> print(headers['User-Agent'])
        Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0  # Example output, actual random
        Minimal usage: Returns random headers dict, User-Agent varies from predefined list.
    """
    logger.info("random_header entry")
    _headers = [
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.54",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
    ]
    result = random.choice(_headers)
    logger.info(
        f"random_header exit: returning headers with User-Agent={result['User-Agent']}"
    )
    return result


def is_valid_db_connection(conn: Any) -> bool:
    """
    Checks if a variable behaves like a valid database connection object
    by checking for the presence and callability of an 'execute' method.

    Args:
        conn (Any): The variable to check.

    Returns:
        bool: True if the variable has a callable 'execute' method, False otherwise.

    Examples:
        >>> class MockConn:
        ...     def execute(self): pass
        >>> is_valid_db_connection(MockConn())
        True
        >>> is_valid_db_connection("not a conn")
        False
        Minimal usage: Validates DB-like object, returns True if 'execute' is callable, False otherwise.
    """
    logger.info(f"is_valid_db_connection entry: conn_type={type(conn)}")
    has_execute = hasattr(conn, "execute")
    is_callable = callable(getattr(conn, "execute")) if has_execute else False
    logger.debug(
        f"Decision branch: has_execute={has_execute}, is_callable={is_callable}"
    )
    result = has_execute and is_callable
    logger.info(f"is_valid_db_connection exit: returning {result}")
    return result

"""
Module containing general utility functions.
"""

import random
from typing import Any, Dict, List, Optional


def numberize(value: Any) -> float:
    """
    Converts a string or number containing commas to a float.

    Args:
        value (Any): The value to convert (string or number).

    Returns:
        float: The converted float value.
    """
    return float(str(value).replace(",", ""))


def first_or_none(items: List[Any]) -> Optional[Any]:
    """
    Returns the first item of a list or None if the list is empty.

    Args:
        items (List[Any]): The input list.

    Returns:
        Optional[Any]: The first item or None.
    """
    return None if len(items) == 0 else items[0]


def random_header() -> Dict[str, str]:
    """
    Returns a randomly chosen dictionary of HTTP headers for web scraping.

    Returns:
        Dict[str, str]: A dictionary containing common HTTP headers.
    """
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
    return random.choice(_headers)


def is_valid_db_connection(conn: Any) -> bool:
    """
    Checks if a variable behaves like a valid database connection object
    by checking for the presence and callability of an 'execute' method.

    Args:
        conn (Any): The variable to check.

    Returns:
        bool: True if the variable has a callable 'execute' method, False otherwise.
    """
    return hasattr(conn, "execute") and callable(getattr(conn, "execute"))

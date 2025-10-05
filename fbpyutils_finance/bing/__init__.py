"""
fbpyutils_finance.bing - Bing Search for Stock Prices

Purpose: This module provides functions to search Bing for current stock prices using web scraping, parsing HTML to extract ticker information, market, name, price, and currency.

Main contents:
- _makeurl(): Constructs Bing search URL from query
- _bingsearch(): Performs GET request to Bing with fixed headers
- stock_price(): Main function to get stock price data via Bing search and parsing

High-level usage pattern:
Import stock_price and call with ticker, optional market: from fbpyutils_finance.bing import stock_price; result = stock_price('PETR4', 'BVMF')

Examples:
>>> from fbpyutils_finance.bing import stock_price
>>> result = stock_price('PETR4', 'BVMF')
>>> print(result['details']['price'] if result['status'] == 'SUCCESS' else result['details']['error_message'])
30.50  # Example price, actual varies
"""
from fbpyutils import debug

from typing import Dict, Optional
import requests
import datetime
from bs4 import BeautifulSoup

from fbpyutils_finance import numberize, logger  # Removed unused MARKET_INFO, first_or_none


def _makeurl(x: str) -> str:
    """
    Build a Bing search URL from query string.

    Args:
        x (str): Search query to convert into URL

    Returns:
        str: Formatted Bing search URL

    Examples:
        >>> _makeurl("test query")
        'https://www.bing.com/search?q=test+query&qs=n&form=QBRE&sp=-1'
        Minimal usage: Constructs URL from query, returns formatted Bing search URL for input "test query".
    """
    logger.info(f"_makeurl entry: x={x}")
    q = "+".join(x.split())
    url = f"https://www.bing.com/search?q={q}&qs=n&form=QBRE&sp=-1"
    logger.info(f"_makeurl exit: returning {url}")
    return url


def _bingsearch(x: str) -> requests.models.Response:
    """
    Performs a default Bing search using custom headers.

    Args:
        x (str): The search query string

    Returns:
        requests.models.Response: An HTTP response with the HTML page resulting from the search query.

    Examples:
        >>> response = _bingsearch("test query")
        >>> print(response.status_code)
        200  # Example, actual depends on search
        Minimal usage: Performs Bing search, returns Response object with status_code 200 for successful query.
    """
    logger.info(f"_bingsearch entry: x={x}")
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    s = requests.Session()
    url = _makeurl(x)
    logger.debug(f"Decision branch: Performing GET to {url}")
    r = s.get(url, headers=h)
    logger.info(f"_bingsearch exit: status_code={r.status_code}")
    return r


def stock_price(x: str, market: Optional[str] = None) -> Dict:
    """
    Performs a Bing search for the current price of the supplied ticker.

    Args:
        x (str): The ticker symbol to search for.
        market (Optional[str], optional): The market exchange symbol (e.g., 'BVMF', 'NASDAQ').
                                          If provided, it's used to refine the search. Defaults to None.

    Returns:
        Dict: A dictionary containing the stock price information or an error message.
              On success: {'info': 'STOCK PRICE', 'source': 'BING', 'status': 'SUCCESS',
                           'details': {'market': str, 'ticker': str, 'name': str, 'currency': str,
                                       'price': float, 'variation': None, 'variation_percent': None,
                                       'trend': None, 'position_time': datetime}}
              On error: {'info': 'STOCK PRICE', 'source': 'BING', 'status': 'ERROR',
                         'details': {'error_message': str}}

    Examples:
        >>> result = stock_price('PETR4', 'BVMF')
        >>> print(result['details']['price'] if result['status'] == 'SUCCESS' else result['details']['error_message'])
        30.50  # Example price, actual varies
        Minimal usage: Searches Bing for ticker price, returns dict with price on success.
    """
    logger.info(f"stock_price entry: x={x}, market={market}")
    result = {
        "info": "STOCK PRICE",
        "source": "BING",
        "status": "SUCCESS",
        "details": {},
    }

    try:
        if not x:
            logger.warning("Decision branch: Ticker is required")
            raise ValueError("Ticker is required")

        token, ticker = "Cotação", x.upper()
        logger.debug(f"Prepared search: token={token}, ticker={ticker}")

        search = " ".join(
            [":".join([market.upper(), ticker]) if market else ticker, token]
        )
        logger.debug(f"Search query: {search}")

        response = _bingsearch(search)
        logger.debug(f"Bing response status: {response.status_code}")

        if response.status_code != 200:
            logger.error(f"Bing Search Fail: status_code={response.status_code}")
            raise ValueError("Bing Search Fail!")

        soup = BeautifulSoup(response.text, "html.parser")
        logger.debug("Parsed HTML with BeautifulSoup")

        step = "Search: ticker_name, market"
        head = soup.find_all("div", class_="b_tophbh bgtopwh")
        logger.debug(f"Found {len(head)} head elements for step {step}")

        element1, element2 = None, None
        for e in head:
            element1 = e.find("h2", class_="b_topTitle")
            if element1:
                break
        for e in head:
            element2 = e.find("div", class_="fin_metadata b_demoteText")
            if element2:
                break

        if all([element1, element2]):
            ticker_name, market, ticker = (
                element1.text,
                *element2.text.replace(" ", "").split(":"),
            )
            logger.debug(f"Extracted: ticker_name={ticker_name}, market={market}, ticker={ticker}")
        else:
            logger.error(f"Bing Search Fail on step {step}: missing elements")
            raise ValueError(f"Bing Search Fail on step {step}!")

        step = "Search: price, currency"
        head = soup.find_all("div", class_="b_tophbb bgtopgr")
        logger.debug(f"Found {len(head)} head elements for step {step}")

        element2, element3 = None, None
        for e in head:
            element1 = e.find("div", class_="fin_quotePrice")
            if element1:
                element2 = element1.find_all("div", class_="b_hPanel")
                if element2:
                    for e1 in element2:
                        element3 = e1.find("span", class_="price_curr")
                        if element3:
                            break

        for e in head:
            element1 = e.find_all("div", id="Finance_Quote")
            if element1:
                for e1 in element1:
                    element2 = e1.find("div", class_="b_focusTextMedium")
                    if element2:
                        break

        if all([element2, element3]):
            price, currency = numberize(element2.text), element3.text
            logger.debug(f"Extracted price={price}, currency={currency}")
        else:
            logger.error(f"Bing Search Fail on step {step}: missing elements")
            raise ValueError(f"Bing Search Fail on step {step}!")

        result["details"] = {
            "market": market,
            "ticker": ticker,
            "name": ticker_name,
            "currency": currency,
            "price": price,
            "variation": None,
            "variation_percent": None,
            "trend": None,
            "position_time": datetime.datetime.now(),
        }
        logger.info(f"stock_price successful: price={price}, currency={currency}")
    except Exception as e:
        logger.error(f"stock_price error: {str(e)}", exc_info=True)
        m = debug.debug_info(e)
        result["status"] = "ERROR"
        result["details"] = {"error_message": m}
        logger.info(f"stock_price exit: status=ERROR")

    logger.info(f"stock_price exit: status={result['status']}")
    return result

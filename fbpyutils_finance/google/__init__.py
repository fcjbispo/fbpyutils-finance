"""
fbpyutils_finance.google - Google Search Info Provider for Financial Data

Purpose: This module provides functionality to retrieve financial information using Google search, including exchange rates and stock prices for various markets and tickers.

Main contents:
- exchange_rate() (function): Retrieve exchange rates between two currencies
- stock_price() (function): Get current stock price information for a given ticker
- _makeurl(), _googlesearch() (functions): Internal search utilities

High-level usage pattern:
Import exchange_rate or stock_price functions and call them with currency pairs or ticker symbols to get financial data from Google search results.

Examples:
>>> from fbpyutils_finance.google import exchange_rate, stock_price
>>> rate = exchange_rate('USD', 'BRL')
>>> rate['status']
'SUCCESS'
>>> price = stock_price('PETR4', 'BVMF')
>>> isinstance(price['details']['price'], (int, float))
True
"""

from fbpyutils import debug

from fbpyutils.datetime import apply_timezone

from typing import Dict, Any, Optional
import requests
import datetime
from bs4 import BeautifulSoup

from fbpyutils_finance import MARKET_INFO, first_or_none, numberize
from fbpyutils_finance import logger

_numberize = numberize

_first_or_none = first_or_none


def _makeurl(x: str) -> str:
    """
    Build a default Google search URL from a query string.

    Args:
        x (str): The search query string.

    Returns:
        str: A full Google search URL generated from the query.

    Examples:
        >>> _makeurl('USD BRL cotação')
        'https://www.google.com/search?q=USD+BRL+cota%C3%A7%C3%A3o&ie=utf-8&oe=utf-8&num=1&lr=lang_ptBR&hl=pt-BR'
        >>> _makeurl('PETR4 stock price')
        'https://www.google.com/search?q=PETR4+stock+price&ie=utf-8&oe=utf-8&num=1&lr=lang_ptBR&hl=pt-BR'
    """
    logger.debug(f"_makeurl(x='{x}')")
    q = "+".join(x.split())
    url = (
        "https://www.google.com/search?q="
        + q
        + "&ie=utf-8&oe=utf-8&num=1&lr=lang_ptBR&hl=pt-BR"
    )
    logger.debug(f"_makeurl() -> '{url}'")
    return url


def _googlesearch(x: str) -> requests.Response:
    """
    Perform a Google search request with custom headers.

    Args:
        x (str): The search query string.

    Returns:
        requests.Response: The HTTP response object containing the search result page.

    Examples:
        >>> response = _googlesearch('USD BRL cotação')
        >>> response.status_code
        200
        >>> 'USD' in response.text
        True
    """
    logger.info(f"_googlesearch(x='{x}')")
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
    logger.debug(f"Making request to: {url}")
    r = s.get(url, headers=h)
    logger.info(f"_googlesearch() -> Response(status_code={r.status_code})")

    return r


def exchange_rate(x: str, y: str) -> Dict[str, Any]:
    """
    Perform a Google search to retrieve the exchange rate from one currency to another.

    Args:
        x (str): The source currency code (e.g., 'USD').
        y (str): The target currency code (e.g., 'BRL').

    Returns:
        Dict[str, Any]: A dictionary containing the exchange rate information, status, and details.

    Examples:
        >>> rate = exchange_rate('USD', 'BRL')
        >>> isinstance(rate, dict)
        True
        >>> 'status' in rate
        True
        >>> 'details' in rate
        True
        >>> # Test with invalid currencies
        >>> result = exchange_rate('XXX', 'YYY')
        >>> result['status'] in ['NOT FOUND', 'ERROR']
        True
    """
    logger.info(f"exchange_rate(x='{x}', y='{y}')")
    result = {
        "info": "EXCHANGE RATE",
        "source": "GOOGLE",
        "status": "SUCCESS",
        "details": {},
    }

    try:
        if not all([x, y]):
            logger.error("Missing currency parameters")
            raise ValueError("Two currencies are required")

        token, currency_from, currency_to = "Cotação", x.upper(), y.upper()
        logger.debug(f"Searching for {currency_from} to {currency_to} exchange rate")

        search = " ".join([currency_from, currency_to, token])
        logger.debug(f"Search query: '{search}'")

        response = _googlesearch(search)
        logger.debug(f"Google search response status: {response.status_code}")

        soup = BeautifulSoup(response.text, "lxml")

        head = soup.find_all("span", class_="r0bn4c rQMQod")
        body = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")

        h, s = set(), set()

        for t in head:
            h.add(t.text)
            logger.debug(f"Found header text: '{t.text}'")

        for t in body:
            s.add(t.text)
            logger.debug(f"Found body text: '{t.text}'")

        if not any([h, s]):
            logger.warning("No exchange rate data found in search results")
            result["status"] = "NOT FOUND"
            result["details"] = {
                "from": currency_from,
                "to": currency_to,
            }
            logger.info("exchange_rate() -> NOT FOUND")
            return result

        currency_parts = [] if not h else h.pop().split()
        logger.debug(f"Currency parts: {currency_parts}")

        currency = 0 if len(currency_parts) < 1 else int(_numberize(currency_parts[0]))

        currency_name = (
            "" if len(currency_parts) < 2 else " ".join(currency_parts[1:-1])
        )

        exchange_parts = [] if not s else s.pop().split()
        logger.debug(f"Exchange parts: {exchange_parts}")

        exchange = 0 if len(exchange_parts) < 1 else _numberize(exchange_parts[0])

        exchange_name = "" if len(exchange_parts) < 2 else " ".join(exchange_parts[1:])

        if not all([currency, currency_name, exchange, exchange_name]):
            logger.error(
                f"Failed to parse all required fields: currency={currency}, currency_name='{currency_name}', exchange={exchange}, exchange_name='{exchange_name}'"
            )
            raise ValueError("Unable to parse exchange rate.")

        result["details"] = {
            "from": "{} ({})".format(currency_from, currency_name),
            "to": "{} ({})".format(currency_to, exchange_name),
            "unit": currency,
            "exchange_rate": exchange,
        }
        logger.info(
            f"exchange_rate() -> SUCCESS: {currency} {currency_from} = {exchange} {currency_to}"
        )

    except Exception as e:
        logger.error(f"Error in exchange_rate: {e}", exc_info=True)
        m = debug.debug_info(e)
        result["status"] = "ERROR"
        result["details"] = {"error_message": m}

    return result


def stock_price(x: str, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Perform a Google search to retrieve the current stock price for a given ticker.

    Args:
        x (str): The ticker symbol to search for.
        market (Optional[str]): The market identifier where the ticker is listed. If None, attempts to infer.

    Returns:
        Dict[str, Any]: A dictionary containing the stock price information, status, and details.

    Examples:
        >>> price = stock_price('PETR4', 'BVMF')
        >>> isinstance(price, dict)
        True
        >>> 'status' in price
        True
        >>> 'details' in price
        True
        >>> # Test with inferred market
        >>> price = stock_price('PETR4')
        >>> isinstance(price['details'], dict)
        True
    """
    logger.info(f"stock_price(x='{x}', market='{market}')")
    result = {
        "info": "STOCK PRICE",
        "source": "GOOGLE",
        "status": "SUCCESS",
        "details": {},
    }

    try:
        if not x:
            logger.error("No ticker provided")
            raise ValueError("Ticker is required")

        token, ticker = "Preço das ações", x.upper()

        search = ":".join([market.upper(), ticker]) if market else ticker
        logger.debug(f"Search query: '{search}'")

        response = _googlesearch(search)

        logger.debug(f"Google response status: {response.status_code}")
        if response.status_code != 200:
            logger.error(f"Google search failed with status {response.status_code}")
            raise ValueError("Google Search Fail!")

        soup = BeautifulSoup(response.text, "html.parser")

        # ticker_name
        head = soup.find_all("div", class_="kCrYT")

        ticker_head = set()

        for t in head:
            if token in t.text:
                ticker_head.add(t.text)

        if ticker_head:
            ticker_head_info = ticker_head.pop().split("/")
            ticker_name_out = (
                None if len(ticker_head_info) == 0 else ticker_head_info[0].rstrip()
            )
        else:
            ticker_name_out = None

        logger.debug(f"ticker_name: {ticker_name_out}")

        if not ticker_name_out:
            logger.error("Unable to parse ticker name from search results")
            raise ValueError("Unable to parse info: {}".format("Ticker Name"))

        # market if not provided
        if not market:
            logger.debug("Market not provided, attempting to infer from search results")
            for e in soup.find_all("span", class_="r0bn4c rQMQod"):
                search_string = e.text
                if f"{ticker}(" in search_string:
                    market = search_string.split("(")[-1][:-1]
                    logger.debug(f"Inferred market: {market}")
                    break

        # price, variation, variation_percent, trend_out
        price_info = soup.find_all(name="div", class_="BNeawe iBp4i AP7Wnd")

        try:
            price_out, variation_out, variation_percent_out = map(
                _numberize,
                price_info[0]
                .text.replace("%", "")
                .replace("(", "")
                .replace(")", "")
                .split(" "),
            )
            logger.debug(
                f"Parsed price: {price_out}, variation: {variation_out}, variation_percent: {variation_percent_out}"
            )

            variation_percent_out = round(variation_percent_out / 100, 2)
        except Exception as e:
            logger.error(f"Failed to parse price information: {e}")
            raise ValueError("Unable to parse info: {}: {}".format("Price Info", e))

        trend_out = (
            "NEUTRAL" if variation_out == 0 else ("UP" if variation_out > 0 else "DOWN")
        )
        logger.debug(f"Trend: {trend_out}")

        # ticker_out, market_out

        ticker_out, market_out = ticker, market

        if not all([ticker_out, market_out]):
            logger.error(
                f"Missing market info: ticker={ticker_out}, market={market_out}"
            )
            raise ValueError("Unable to parse info: {}".format("Market Info"))

        # date_time_info, currency
        time_currency_info = soup.find_all(name="span", class_="r0bn4c rQMQod")

        date_time_info, currency = time_currency_info[1].text.split(" · ")[:-1]
        logger.debug(f"Date/time info: '{date_time_info}', currency: '{currency}'")

        currency_out = currency.split()[-1]

        position_date_info = date_time_info.replace(".", "").replace(",", "").split()

        day = None if len(position_date_info) == 0 else str(position_date_info[0])

        month = (
            None
            if len(position_date_info) < 3
            else str(
                [
                    "jan",
                    "fev",
                    "mar",
                    "abr",
                    "mai",
                    "jun",
                    "jul",
                    "ago",
                    "set",
                    "out",
                    "nov",
                    "dez",
                ].index(position_date_info[2])
                + 1
            ).rjust(2, "0")
        )

        year = str(datetime.datetime.today().year)

        time = None if len(position_date_info) < 4 else position_date_info[3]

        if not all([day, month, year, time]):
            logger.error(
                f"Missing date components: day={day}, month={month}, year={year}, time={time}"
            )
            raise ValueError("Unable to parse info: {}".format("Convert position date"))

        date_time_str = "-".join([year, month, day, time])

        tz = [m["timezone"] for m in _market_info if m["market"] == market]
        tz = _first_or_none(tz)

        if not tz:
            logger.error(f"No timezone found for market: {market}")
            raise ValueError("Unable to parse info: {}".format("Market Timezone"))

        date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%d-%H:%M")

        date_time_info = apply_timezone(date_time_obj, tz)

        result["details"] = {
            "market": market_out,
            "ticker": ticker_out,
            "name": ticker_name_out,
            "currency": currency_out,
            "price": price_out,
            "variation": variation_out,
            "variation_percent": variation_percent_out,
            "trend": trend_out,
            "position_time": date_time_info,
        }
        logger.info(
            f"stock_price() -> SUCCESS: {ticker_out} @ {price_out} {currency_out} ({trend_out})"
        )

    except Exception as e:
        logger.error(f"Error in stock_price: {e}", exc_info=True)
        m = debug.debug_info(e)
        result["status"] = "ERROR"
        result["details"] = {"error_message": m}

    return result

"""
fbpyutils_finance.yahoo - Yahoo Finance Data Provider

Purpose: This module provides functionality to retrieve financial data from Yahoo Finance, including stock prices, currency exchange rates, dividend information, and various financial instruments using the yfinance library and Yahoo Finance API.

Main contents:
- YahooCurrencyDataProvider (class): Provides cryptocurrency or currency exchange rate data
- YahooStockDataProvider (class): Provides stock data including dividend payments 
- stock_price() (function): Get current stock price from Yahoo Finance search
- _reorder_columns() (function): Reorder DataFrame columns for better presentation
- _makeurl(), _ysearch() (functions): Internal Yahoo Finance search utilities

High-level usage pattern:
Import the data provider classes and use them to fetch stock, currency, or dividend data from Yahoo Finance API.

Examples:
>>> from fbpyutils_finance.yahoo import YahooStockDataProvider, stock_price
>>> provider = YahooStockDataProvider({'ticker': 'PETR4.SA', 'market': 'BR', 'start': '2023-01-01', 'end': '2023-12-31'})
>>> stock_data = provider.get_data()
>>> isinstance(stock_data, pd.DataFrame)
True
>>> price = stock_price('PETR4', 'BVMF')
>>> isinstance(price['details']['price'], float)
True
"""

# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: fbpyutils-finance--TrezB8H
#     language: python
#     name: python3
# ---

import sys

sys.path.insert(0, "..")

# +
from fbpyutils import debug


from typing import Dict
import requests
import datetime
from bs4 import BeautifulSoup

from fbpyutils_finance import random_header
from fbpyutils_finance import logger

import pandas as pd
import yfinance as yf


import pandas as pd
import yfinance as yf


def _reorder_columns(df, ticker):
    """
    Reorders the columns of the given DataFrame to prioritize 'Ticker' and 'Date' columns.

    Parameters
    ----------
    df (pd.DataFrame) : The DataFrame whose columns are to be reordered.
    ticker (str) : The ticker symbol to be added to the DataFrame.
    Returns
    -------
    pd.DataFrame : The DataFrame with reordered columns, 'Ticker' and 'Date' at the beginning, and a reset index.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'Open': [100], 'Close': [105]}, index=pd.date_range('2023-01-01', periods=1))
        >>> reordered = _reorder_columns(df, 'TEST3')
        >>> reordered.columns[0]  # Ticker should be first
        'Ticker'
        >>> reordered.columns[1]  # Date should be second
        'Date'
    """
    logger.debug(f"_reorder_columns(ticker='{ticker}')")
    original_shape = df.shape
    df["Ticker"] = ticker
    df["Date"] = df.index
    result = (
        df[["Ticker", "Date"] + [col for col in df if col not in ["Ticker", "Date"]]]
        .copy()
        .reset_index(drop=True)
    )
    logger.debug(f"_reorder_columns() -> DataFrame shape: {result.shape} (original: {original_shape})")
    return result


class YahooCurrencyDataProvider:
    """
    Provides cryptocurrency or currency exchange rate data for a specific time frame.

    Parameters
    ----------
    params (dict) : A dictionary containing the parameters required to fetch the data.

        - 'currency_from' (str) : The base currency to fetch the exchange rate for.
        - 'currency_to' (str) : The target currency to fetch the exchange rate for.
        - 'start' (str) : The start date to fetch the data from. It should be in a format that yfinance can understand.
        - 'end' (str) : The end date to fetch the data until. It should be in a format that yfinance can understand.

    Returns
    -------
    pd.DataFrame : The DataFrame with the currency exchange rate data, 'Ticker' and 'Date' columns at the beginning.

    Raises
    ------
    AssertionError : If 'end' is not greater than 'start' or if not all required parameters are provided.
    """

    def _check_params(self, params) -> bool:
        """
        Check if the required parameters are present and valid.

        Examples:
            >>> provider = YahooCurrencyDataProvider({'currency_from': 'USD', 'currency_to': 'BRL', 'start': '2023-01-01', 'end': '2023-12-31'})
            >>> provider._check_params(provider.params)
            True
            >>> # Test invalid parameters
            >>> provider.params['start'] = '2023-12-31'
            >>> provider.params['end'] = '2023-01-01'
            >>> provider._check_params(provider.params)
            False
        """
        logger.debug(f"_check_params(params={params})")
        result = (
            all([p in params for p in ("currency_from", "currency_to", "start", "end")])
            and params["end"] > params["start"]
        )
        logger.debug(f"_check_params() -> {result}")
        return result

    def __init__(self, params):
        """
        Initialize the currency data provider with parameters.

        Examples:
            >>> provider = YahooCurrencyDataProvider({'currency_from': 'USD', 'currency_to': 'BRL', 'start': '2023-01-01', 'end': '2023-12-31'})
            >>> provider.params['currency_from']
            'USD'
            >>> # Test with invalid parameters
            >>> YahooCurrencyDataProvider({'currency_from': 'USD'})  # Missing required parameters
            Traceback (most recent call last):
            ValueError: Invalid parameters provided for YahooCurrencyDataProvider.
        """
        logger.info(f"YahooCurrencyDataProvider.__init__(params={params})")
        if not self._check_params(params):
            # Raise an error if params are invalid during initialization
            logger.error(f"Invalid parameters provided: {params}")
            raise ValueError(
                "Invalid parameters provided for YahooCurrencyDataProvider."
            )
        self.params = params  # Store params as instance attribute
        logger.debug(f"YahooCurrencyDataProvider.__init__() initialized successfully")

    def get_data(self) -> pd.DataFrame:
        """
        Get currency exchange rate data.

        Examples:
            >>> provider = YahooCurrencyDataProvider({'currency_from': 'USD', 'currency_to': 'BRL', 'start': '2023-01-01', 'end': '2023-01-02'})
            >>> data = provider.get_data()
            >>> isinstance(data, pd.DataFrame)
            True
            >>> 'Ticker' in data.columns
            True
            >>> 'Date' in data.columns
            True
        """
        logger.info(f"YahooCurrencyDataProvider.get_data()")
        currency_from = self.params["currency_from"]
        currency_to = self.params["currency_to"]
        start = self.params["start"]
        end = self.params["end"]
        logger.debug(f"Fetching data for {currency_from} to {currency_to} from {start} to {end}")

        ticker = currency_from.upper() + currency_to.upper()
        logger.debug(f"Currency ticker: {ticker}")
        _ticker = ticker + "=X"

        logger.debug(f"Downloading data for {_ticker}")
        data = yf.download(_ticker, start=start, end=end)
        result = _reorder_columns(data, ticker)
        logger.info(f"YahooCurrencyDataProvider.get_data() -> DataFrame with shape {result.shape}")
        return result


class YahooStockDataProvider:
    """
    A class that provides stock data from Yahoo Finance for a specified ticker, including dividend payments if required.

    Parameters:
    - params (dict): Dictionary containing the necessary parameters to fetch the data. Mandatory keys are 'ticker' (str), 'market' (str), 'start' (str or datetime.date), and 'end' (str or datetime.date). The 'market' key should contain either 'BR' for Brazilian stocks or 'US' for American stocks. The 'payments' key (bool) indicates whether to fetch dividend payments in addition to the stock data.
       - 'ticker': The stock ticker symbol (e.g., 'AAPL').
       - 'market': The market where the stock is traded ('BR' or 'US').
       - 'start': The start date for the data range (format: YYYY-MM-DD or a pandas datetime.date object).
       - 'end': The end date for the data range (format: YYYY-MM-DD or a pandas datetime.date object).

    Returns:
    - pd.DataFrame: A DataFrame containing stock data, including dividend payments if specified in the parameters.

    Note:
    - The 'market' parameter is converted to uppercase within the class for consistency and case-insensitive comparison.
    - If 'payments' is True, the method returns a DataFrame with dividend payment data filtered by the specified start and end dates. If no dates are specified, all available dividend payments are returned.
    """

    def _check_params(self, params) -> bool:
        """
        Check if the required parameters are present and valid.

        Examples:
            >>> provider = YahooStockDataProvider({'ticker': 'PETR4', 'market': 'BR', 'start': '2023-01-01', 'end': '2023-12-31'})
            >>> provider._check_params(provider.params)
            True
            >>> # Test invalid market
            >>> provider.params['market'] = 'EU'
            >>> provider._check_params(provider.params)
            False
        """
        logger.debug(f"_check_params(params={params})")
        # Check required keys exist
        if not all(p in params for p in ("ticker", "market", "start", "end")):
            logger.debug("Missing required parameters")
            result = False
        # Check market validity
        elif params["market"].upper() not in ("BR", "US"):
            logger.debug(f"Invalid market: {params['market']}")
            result = False
        # Check date order only if both dates are provided
        elif params["start"] is not None and params["end"] is not None:
            # Attempt conversion for comparison if they are strings
            try:
                start_dt = pd.to_datetime(params["start"])
                end_dt = pd.to_datetime(params["end"])
                if end_dt <= start_dt:
                    logger.debug(f"End date {end_dt} is not after start date {start_dt}")
                    result = False
                else:
                    result = True
            except (ValueError, TypeError):
                # Handle cases where conversion fails or types are incompatible
                logger.debug("Failed to convert dates for comparison")
                result = False
        else:
            result = True
        logger.debug(f"_check_params() -> {result}")
        return result

    def __init__(self, params):
        """
        Initialize the stock data provider with parameters.

        Examples:
            >>> provider = YahooStockDataProvider({'ticker': 'PETR4', 'market': 'BR', 'start': '2023-01-01', 'end': '2023-12-31'})
            >>> provider.params['ticker']
            'PETR4'
            >>> # Test invalid parameters
            >>> YahooStockDataProvider({'ticker': 'PETR4'})  # Missing required parameters
            Traceback (most recent call last):
            ValueError: Invalid parameters provided for YahooStockDataProvider.
        """
        logger.info(f"YahooStockDataProvider.__init__(params={params})")
        if not self._check_params(params):
            # Raise an error if params are invalid during initialization
            logger.error(f"Invalid parameters provided: {params}")
            raise ValueError("Invalid parameters provided for YahooStockDataProvider.")
        self.params = params  # Store params as instance attribute
        logger.debug(f"YahooStockDataProvider.__init__() initialized successfully")

    def get_data(self) -> pd.DataFrame:
        """
        Get stock price data.

        Examples:
            >>> provider = YahooStockDataProvider({'ticker': 'PETR4', 'market': 'BR', 'start': '2023-01-01', 'end': '2023-01-02'})
            >>> data = provider.get_data()
            >>> isinstance(data, pd.DataFrame)
            True
            >>> # Test with dividends
            >>> provider = YahooStockDataProvider({'ticker': 'PETR4', 'market': 'BR', 'start': '2023-01-01', 'end': '2023-12-31', 'payments': True})
            >>> dividend_data = provider.get_data()
            >>> isinstance(dividend_data, pd.DataFrame) or dividend_data is None
            True
        """
        logger.info(f"YahooStockDataProvider.get_data()")
        ticker = self.params["ticker"]
        start = self.params["start"]
        end = self.params["end"]
        market = self.params["market"].upper()
        logger.debug(f"Parameters: ticker={ticker}, market={market}, start={start}, end={end}")

        ticker = ticker.upper()

        if market == "BR":
            logger.debug("Adding .SA suffix for Brazilian ticker")
            ticker = ticker + ".SA"

        if self.params.get("payments", False):
            logger.debug("Fetching dividend data")
            xdata = yf.Ticker(ticker).dividends
            # Apply filters to dividends
            # Convert start/end to datetime objects for reliable comparison
            start_dt = pd.to_datetime(start) if start is not None else None
            end_dt = pd.to_datetime(end) if end is not None else None

            if start_dt is not None and end_dt is not None:
                # Ensure index is also datetime before comparison
                if not isinstance(xdata.index, pd.DatetimeIndex):
                    xdata.index = pd.to_datetime(xdata.index)
                filtered_dividends = xdata.loc[
                    (xdata.index >= start_dt) & (xdata.index <= end_dt)
                ]
            elif start_dt is not None:
                if not isinstance(xdata.index, pd.DatetimeIndex):
                    xdata.index = pd.to_datetime(xdata.index)
                filtered_dividends = xdata.loc[xdata.index >= start_dt]
            elif end_dt is not None:  # Handle case where only end_dt is provided
                if not isinstance(xdata.index, pd.DatetimeIndex):
                    xdata.index = pd.to_datetime(xdata.index)
                filtered_dividends = xdata.loc[xdata.index <= end_dt]
            else:  # Both are None
                filtered_dividends = xdata
            # Check if the resulting series has more than one row
            if isinstance(filtered_dividends, pd.Series):
                filtered_dividends = filtered_dividends.to_frame(name="Payment")
            else:
                filtered_dividends = None

            data = filtered_dividends
            logger.debug(f"Retrieved dividend data with {len(data) if data is not None else 0} entries")
        else:
            logger.debug("Fetching stock price data")
            data = yf.download(ticker, start=start, end=end)
            logger.debug(f"Downloaded price data with shape {data.shape}")

        result = _reorder_columns(data, ticker)
        logger.info(f"YahooStockDataProvider.get_data() -> DataFrame with shape {result.shape}")
        return result


def _makeurl(x):
    """
    Build default Google search URL output.

    Parameters:
        x (str): The search query string

    Returns:
        str: A string with a full Google search URL from the search query.

    Examples:
        >>> _makeurl('PETR4.SA')
        'https://finance.yahoo.com/quote/PETR4.SA/'
        >>> _makeurl('AAPL')
        'https://finance.yahoo.com/quote/AAPL/'
    """
    logger.debug(f"_makeurl(x='{x}')")
    q = x.upper()
    url = f"https://finance.yahoo.com/quote/{q}/"
    logger.debug(f"_makeurl() -> '{url}'")
    return url


def _ysearch(x: str) -> requests.models.Response:
    """
    Performs a default Yahoo search using custom headers.

    Parameters:
        x (str): The search query string

    Returns:
        http response: An HTTP response with the HTML page resulting from the search query.

    Examples:
        >>> response = _ysearch('PETR4.SA')
        >>> response.status_code
        200
        >>> 'PETR4' in response.text
        True
    """
    logger.info(f"_ysearch(x='{x}')")
    h = random_header()
    logger.debug(f"Using random headers: {dict(list(h.items())[:2])}...")  # Log first 2 header items

    s = requests.Session()
    url = _makeurl(x)
    logger.debug(f"Making request to: {url}")
    r = s.get(url, headers=h)
    logger.info(f"_ysearch() -> Response(status_code={r.status_code})")

    return r


def stock_price(x: str, market: str = None) -> Dict:
    """
    Performs a Yahoo search for the current price of the supplied ticker in the default market.

    Parameters:
        x (str): The ticker to search for the current price.
        market (str, Optional): The name of the market on which the ticker will be searched.

    Returns:
        dict: A standard dictionary with the stock price and information for the supplied ticker.

    Examples:
        >>> price = stock_price('PETR4', 'BVMF')
        >>> isinstance(price, dict)
        True
        >>> 'status' in price
        True
        >>> 'details' in price
        True
        >>> # Test with invalid ticker
        >>> result = stock_price('')
        >>> result['status'] == 'ERROR'
        True
    """
    logger.info(f"stock_price(x='{x}', market='{market}')")
    result = {
        "info": "STOCK PRICE",
        "source": "YAHOO",
        "status": "SUCCESS",
        "details": {},
    }

    step = "Init"
    logger.debug(f"Starting stock price search, step: {step}")
    try:
        if not x:
            logger.error("No ticker provided")
            raise ValueError("Ticker is required")

        ticker = x.upper()
        logger.debug(f"Processing ticker: {ticker}")

        response = _ysearch(ticker)

        if response.status_code != 200:
            logger.error(f"Yahoo search failed with status {response.status_code}")
            raise ValueError(f"Yahoo Search Fail: {ticker}, {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        step = "Search: ticker name, market, currency"
        logger.debug(f"Searching for ticker info, step: {step}")

        element1 = soup.find("div", id="mrt-node-Lead-5-QuoteHeader")
        element2 = element1.find("h1", class_="D(ib) Fz(18px)")
        element3 = element1.find("div", class_="C($tertiaryColor) Fz(12px)")

        if all([element2, element3]):
            ticker_name, ticker = [
                e.strip() for e in element2.text.replace(")", "").split("(")
            ]
            logger.debug(f"Found ticker info: name='{ticker_name}', ticker='{ticker}'")

            elements = [e.upper() for e in element3.text.replace(" ", "|").split("|")]
            market, currency = elements[0], elements[-1]
            logger.debug(f"Market: {market}, Currency: {currency}")
        else:
            logger.error(f"Failed to find ticker elements at step: {step}")
            raise ValueError(f"Yahoo Search Fail on step {step}!")

        step = "Search: price"
        logger.debug(f"Searching for price, step: {step}")
        element4 = element1.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")

        if all([element4]):
            price = float(element4.text)
            logger.debug(f"Found price: {price}")
        else:
            logger.error(f"Failed to find price element at step: {step}")
            raise ValueError(f"Yahoo Search Fail on step {step}!")

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
        logger.info(f"stock_price() -> SUCCESS: {ticker} @ {price} {currency}")

    except Exception as e:
        logger.error(f"Error in stock_price at step {step}: {e}", exc_info=True)
        print(e, step)
        m = debug.debug_info(e)
        result["status"] = "ERROR"
        result["details"] = {"error_message": m}

    return result

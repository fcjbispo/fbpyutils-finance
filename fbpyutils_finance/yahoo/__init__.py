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
    """
    df["Ticker"] = ticker
    df["Date"] = df.index
    return (
        df[["Ticker", "Date"] + [col for col in df if col not in ["Ticker", "Date"]]]
        .copy()
        .reset_index(drop=True)
    )


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
        return (
            all([p in params for p in ("currency_from", "currency_to", "start", "end")])
            and params["end"] > params["start"]
        )

    def __init__(self, params):
        if not self._check_params(params):
            # Raise an error if params are invalid during initialization
            raise ValueError(
                "Invalid parameters provided for YahooCurrencyDataProvider."
            )
        self.params = params  # Store params as instance attribute

    def get_data(self) -> pd.DataFrame:
        currency_from = self.params["currency_from"]
        currency_to = self.params["currency_to"]
        start = self.params["start"]
        end = self.params["end"]

        ticker = currency_from.upper() + currency_to.upper()
        _ticker = ticker + "=X"

        data = yf.download(_ticker, start=start, end=end)
        return _reorder_columns(data, ticker)


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
        # Check required keys exist
        if not all(p in params for p in ("ticker", "market", "start", "end")):
            return False
        # Check market validity
        if params["market"].upper() not in ("BR", "US"):
            return False
        # Check date order only if both dates are provided
        if params["start"] is not None and params["end"] is not None:
            # Attempt conversion for comparison if they are strings
            try:
                start_dt = pd.to_datetime(params["start"])
                end_dt = pd.to_datetime(params["end"])
                if end_dt <= start_dt:
                    return False
            except (ValueError, TypeError):
                # Handle cases where conversion fails or types are incompatible
                return False  # Consider invalid if dates cannot be compared
        return True

    def __init__(self, params):
        if not self._check_params(params):
            # Raise an error if params are invalid during initialization
            raise ValueError("Invalid parameters provided for YahooStockDataProvider.")
        self.params = params  # Store params as instance attribute

    def get_data(self) -> pd.DataFrame:
        ticker = self.params["ticker"]
        start = self.params["start"]
        end = self.params["end"]
        market = self.params["market"].upper()

        ticker = ticker.upper()

        if market == "BR":
            ticker = ticker + ".SA"

        if self.params.get("payments", False):
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
        else:
            data = yf.download(ticker, start=start, end=end)

        return _reorder_columns(data, ticker)


def _makeurl(x):
    """
    Build default Google search URL output.
    Parameters:
        x (str): The search query string
    Returns:
        str: A string with a full Google search URL from the search query.
    """
    q = x.upper()
    url = f"https://finance.yahoo.com/quote/{q}/"
    return url


def _ysearch(x: str) -> requests.models.Response:
    """
    Performs a default Yahoo search using custom headers.
    Parameters:
        x (str): The search query string
    Returns:
        http response: An HTTP response with the HTML page resulting from the search query.
    """
    h = random_header()

    s = requests.Session()
    url = _makeurl(x)
    r = s.get(url, headers=h)

    return r


def stock_price(x: str, market: str = None) -> Dict:
    """
    Performs a Yahoo search for the current price of the supplied ticker in the default market.
    Parameters:
        x (str): The ticker to search for the current price.
        market (str, Optional): The name of the market on which the ticker will be searched.
    Returns:
        dict: A standard dictionary with the stock price and information for the supplied ticker.
    """
    result = {
        "info": "STOCK PRICE",
        "source": "YAHOO",
        "status": "SUCCESS",
        "details": {},
    }

    step = "Init"
    try:
        if not x:
            raise ValueError("Ticker is required")

        ticker = x.upper()

        response = _ysearch(ticker)

        if response.status_code != 200:
            raise ValueError(f"Yahoo Search Fail: {ticker}, {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        step = "Search: ticker name, market, currency"

        element1 = soup.find("div", id="mrt-node-Lead-5-QuoteHeader")
        element2 = element1.find("h1", class_="D(ib) Fz(18px)")
        element3 = element1.find("div", class_="C($tertiaryColor) Fz(12px)")

        if all([element2, element3]):
            ticker_name, ticker = [
                e.strip() for e in element2.text.replace(")", "").split("(")
            ]

            elements = [e.upper() for e in element3.text.replace(" ", "|").split("|")]
            market, currency = elements[0], elements[-1]
        else:
            raise ValueError(f"Yahoo Search Fail on step {step}!")

        step = "Search: price"
        element4 = element1.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")

        if all([element4]):
            price = float(element4.text)
        else:
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
    except Exception as e:
        print(e, step)
        m = debug.debug_info(e)
        result["status"] = "ERROR"
        result["details"] = {"error_message": m}

    return result

# fbpyutils-finance

## Description

This package provides a collection of finance utilities, calculations, and data providers. It aims to simplify common financial tasks and provide easy access to financial data from various sources.

## Features

- **Data Providers:** Access financial data from sources like Bovespa (Brazilian Stock Exchange), CVM (Brazilian Securities and Exchange Commission), Yahoo Finance, and more.
- **Calculations:** Perform financial calculations such as rate conversions, stock return rates, and investment analysis.
- **Utilities:**  Includes helpful utilities for working with dates, numbers, and strings in a financial context.
- **CVM Data Processing:** Tools for processing data from the CVM, including fund and investment data.
- **Bovespa Data Retrieval:**  Functionality to download and process historical stock data from Bovespa.

## Installation

```bash
pip install fbpyutils-finance
```
## Usage

### Example 1: Getting stock price from Yahoo Finance
```python
from fbpyutils_finance.yahoo import stock_price

ticker = "AAPL"
price = stock_price(ticker, market="US")
print(f"The current price of {ticker} is: {price}")
```

### Example 2: Converting daily rate to annual rate
```python
from fbpyutils_finance import rate_daily_to_annual

daily_rate = 0.0001 
annual_rate = rate_daily_to_annual(daily_rate)
print(f"The annual rate for a daily rate of {daily_rate} is: {annual_rate}")
```

## Modules

- **fbpyutils_finance.bovespa:** For fetching and processing data from the Bovespa stock exchange.
- **fbpyutils_finance.cvm:** For accessing and processing data from the CVM (Brazilian Securities and Exchange Commission).
- **fbpyutils_finance.yahoo:** For retrieving stock and currency data from Yahoo Finance.


# Finance Utilities, Calculations and Data Providers
---

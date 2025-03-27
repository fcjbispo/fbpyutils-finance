# fbpyutils-finance - Finance Utilities, Calculations and Data Providers

## Description

This package provides a collection of finance utilities, calculations, and data providers.
It aims to simplify common financial tasks and provide easy access to financial data from various sources.

## Features

- **Data Providers:** Access financial data from various sources, including Bovespa (Brazilian Stock Exchange), CVM (Brazilian Securities and Exchange Commission), Yahoo Finance, Bing Finance and Tesouro Direto.
- **Calculations:** Perform financial calculations such as rate conversions, stock return rates, and investment analysis.
- **Utilities:**  Includes helpful utilities for working with dates, numbers, and strings in a financial context.
- **CVM Data Processing:** Tools for processing and accessing data from the CVM, including fund and investment data.
- **Bovespa Data Retrieval:**  Functionality to download and process historical stock data from Bovespa.

## Installation

```bash
pip install fbpyutils-finance
```
## Usage

### Example 1: Get stock price from Yahoo Finance
```python
from fbpyutils_finance.yahoo import stock_price

ticker = "AAPL" # Example ticker
price = stock_price(ticker, market="US") # US market
print(f"The current price of {ticker} is: {price}")
```

### Example 2: Convert daily rate to annual rate
```python
from fbpyutils_finance import rate_daily_to_annual

daily_rate = 0.0001 # Example daily rate
annual_rate = rate_daily_to_annual(daily_rate) # Convert to annual rate
print(f"The annual rate for a daily rate of {daily_rate} is: {annual_rate}")
```

## Modules

- **fbpyutils_finance.bovespa:** Functionality for fetching and processing data from the Bovespa stock exchange (B3).
- **fbpyutils_finance.cvm:** For accessing and processing data from the CVM (Brazilian Securities and Exchange Commission).
- **fbpyutils_finance.yahoo:** For retrieving stock and currency data from Yahoo Finance.
- **fbpyutils_finance.bing:** For retrieving stock data from Bing Finance.
- **fbpyutils_finance.tesourodireto:** For accessing data from Tesouro Direto.
- **fbpyutils_finance.cei:** For processing data from CEI (Canal Eletrônico do Investidor).
- **fbpyutils_finance.investidor10:** For retrieving data from Investidor10 website.


# Finance Utilities, Calculations and Data Providers
---

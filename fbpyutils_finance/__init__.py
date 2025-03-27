'''
Functions to perform financial calculations.

https://clubedospoupadores.com/educacao-financeira/calculadora-taxa.html
https://www.youtube.com/watch?v=JOqK2EGdxbQ

'''
import os
import random
import pandas as pd
from pandas import DataFrame

from fbpyutils import file as F


APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

USER_APP_FOLDER = os.path.sep.join([os.path.expanduser("~"), '.cvm'])

CERTIFICATES = {
    f.split(os.path.sep)[-1].split('.')[0]: f
    for f in F.find(APP_FOLDER, '*.pem')
}

MARKET_INFO = [
        {
            'region': 'América', 
            'market': 'BVMF', 
            'name': 'B3 - Bolsa de Valores do Brasil e Mercado de balcão', 
            'delay': '15', 
            'timezone': 'America/Sao_Paulo' 
        },
        {'region': 'América', 'market': 'NASDAQ', 'name': 'NASDAQ Last Sale', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
        {'region': 'América', 'market': 'NYSE', 'name': 'NYSE', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
        {'region': 'América', 'market': 'NYSEARCA', 'name': 'NYSE ARCA', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
        {'region': 'América', 'market': 'NYSEAMERICAN', 'name': 'NYSE American', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
]



numberize = lambda x: float(x.replace(",", ""))


first_or_none = lambda x: None if len(x) == 0 else x[0]

def random_header():
    _headers = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        },
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        },
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        },
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        },
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.54',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
    ]
    return random.choice(_headers)


def is_valid_db_connection(conn):
    """
    Checks if a variable is a valid database connection.
    Parameters:
    - conn: Variable to be checked if it is a valid database connection.
    Returns:
    - bool: True if the variable is a valid database connection, False otherwise.
    """
    return hasattr(conn, 'execute') and callable(getattr(conn, 'execute'))


def rate_daily_to_monthly(rate: float) -> float:
    """
    Converts a daily interest rate to a monthly interest rate.
    Args:
        rate (float): The daily interest rate.
    Returns:
        float: The equivalent monthly interest rate.
    """
    return (1 + rate) ** 30 - 1


def rate_monthly_to_daily(rate: float) -> float:
    """
    Converts a monthly interest rate to a daily interest rate.
     Arguments:
        rate (float): The monthly interest rate.
     Returns:
        float: The equivalent daily interest rate.
    """
    return (1 + rate) ** (1 / 30) - 1


def rate_monthly_to_annual(rate: float) -> float:
    """
    Converts a monthly interest rate to an annual interest rate.
     Arguments:
        rate (float): The monthly interest rate.
     Returns:
        float: The equivalent annual interest rate.
    """
    return (1 + rate) ** 12 - 1


def rate_annual_to_monthly(rate: float) -> float:
    """
    Converts an annual interest rate to a monthly interest rate.
     Arguments:
        rate (float): The annual interest rate.
     Returns:
        float: The equivalent monthly interest rate.
    """
    return (1 + rate) ** (1 / 12) - 1


def rate_annual_to_daily(rate: float) -> float:
    """
    Converts an annual interest rate to a daily interest rate.
     Arguments:
        rate (float): The annual interest rate.
     Returns:
        float: The equivalent daily interest rate.
    """
    return (1 + rate) ** (1 / 360) - 1


def rate_daily_to_annual(rate: float) -> float:
    """
    Converts a daily interest rate to an annual interest rate.
     Arguments:
        rate (float): The daily interest rate.
     Returns:
        float: The equivalent annual interest rate.
    """
    return (1 + rate) ** 360 - 1


def stock_return_rate(current: float, previous: float) -> float:
    """
    Calculates the return rate of a stock based on the current and previous prices.
     Arguments:
        current (float): The current price of the stock.
        previous (float): The previous price of the stock.
     Returns:
        float: The return rate of the stock.
    """
    if previous is None:
        return None
    return current / previous - 1


def stock_adjusted_return_rate(
        current: float, previous: float, factor: float = 1,
        dividend_yeld: float = 0, tax: float = 2
) -> float:
    """
    Calculates the adjusted return rate of a stock, considering factors like dividends and taxes.
     Arguments:
        current (float): The current price of the stock.
        previous (float): The previous price of the stock.
        factor (float, optional): Adjustment factor for the current price. Default is 1.
        dividend_yeld (float, optional): Dividend yield of the stock. Default is 0.
        tax (float, optional): Tax rate applied to the dividend yield. Default is 2.
     Returns:
        float: The adjusted return rate of the stock.
    """
    if previous is None:
        return None

    factor = factor or 1

    dividend_yeld = dividend_yeld or 0

    if tax is None or tax >= 0:
        tax = 2

    dividend_yeld = (dividend_yeld * abs(1 - tax))

    return (current * factor) / (previous - dividend_yeld) - 1


def stock_adjusted_price(
        adjusted: float, adjusted_return_rate: float
) -> float:
    """
    Calculates the adjusted price of a stock based on the adjusted return rate.
     Arguments:
        adjusted (float): The adjusted price of the stock.
        adjusted_return_rate (float): The adjusted return rate of the stock.
     Returns:
        float: The adjusted price of the stock.
    """
    return adjusted / (1 + adjusted_return_rate)


def stock_adjusted_return_rate_check(
        current: float, previous_adjusted: float) -> float:
    """
    Calculates the return rate of a stock based on the current price and the previous adjusted price.
     Arguments:
        current (float): The current price of the stock.
        previous_adjusted (float): The previous adjusted price of the stock.
     Returns:
        float: The return rate of the stock.
    """
    return current / previous_adjusted - 1


def stock_event_factor(expression: str) -> tuple:
    """
    Analyzes a stock event expression and returns the event type and factor.
     Arguments:
        expression (str): The stock event expression in the format "factor:factor" or "factor".
     Returns:
        tuple: A tuple containing the event type (either 'INPLIT' or 'SPLIT') and the factor.
     Raises:
        ValueError: If the expression is invalid.
    """
    if expression is None or len(expression) == 0:
        return None, 1

    as_float = lambda x: float(x.replace(',', '.')) if type(x) == str else float(x)

    event, factor = 'INPLIT', 0.00

    parts = expression.split(':')

    if len(parts) > 1:
        parts[0] = as_float(parts[0])
        parts[1] = as_float(parts[1])

        if parts[0] == 1.0:
            factor = parts[0] / parts[1]
        elif parts[1] == 1.0:
            event = 'SPLIT'
            factor = parts[0]

        return event, factor
    else:
        raise ValueError('Invalid expression {}'.format(expression))
    

def get_investment_table(df: DataFrame, investment_amount: float) -> DataFrame:
    """
    Calculate investment metrics for a DataFrame of financial assets.

    Parameters:
    - df: DataFrame containing the columns 'Ticker' (str), 'Price' (float), 
          'Quantity' (float), 'Average Price' (float).
    - investment_amount: Total investment amount (float).

    Returns:
    - DataFrame with additional columns: 'Profit/Loss' (float), 
      'Adjusted Profit/Loss' (float), 'Weight' (float), 'Proportion' (float), 
      'Investment Value' (float), 'Quantity to Buy' (float).

    Raises:
    - ValueError: If the DataFrame is missing any required columns ('Ticker', 
      'Price', 'Quantity', 'Average Price').
    """
    # Define required columns
    required_columns = {'Ticker', 'Price', 'Quantity', 'Average Price'}
    
    # Check for missing columns
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    # Calculate Profit/Loss
    df['Profit/Loss'] = (df['Price'] - df['Average Price']) * df['Quantity']
    
    # Calculate Adjusted Profit/Loss (minimum value adjusted to zero)
    min_profit_loss: float = df['Profit/Loss'].min()
    df['Adjusted Profit/Loss'] = df['Profit/Loss'] - min_profit_loss
    
    # Calculate Weight (using k = 0.01 to avoid division by zero)
    k: float = 0.01
    df['Weight'] = 1 / (df['Adjusted Profit/Loss'] + k)
    
    # Calculate Proportion (normalize weights to sum to 1)
    total_weights: float = df['Weight'].sum()
    df['Proportion'] = df['Weight'] / total_weights
    
    # Calculate Investment Value (distribute total value according to proportion)
    df['Investment Value'] = df['Proportion'] * investment_amount
    
    # Calculate Quantity to Buy
    df['Quantity to Buy'] = df['Investment Value'] / df['Price']
    
    return df
    

if not os.path.exists(USER_APP_FOLDER):
    os.makedirs(USER_APP_FOLDER)

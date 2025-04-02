'''
Functions to perform financial calculations.

https://clubedospoupadores.com/educacao-financeira/calculadora-taxa.html
https://www.youtube.com/watch?v=JOqK2EGdxbQ

'''
import os
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

import pandas as pd

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


def is_valid_db_connection(conn: Any) -> bool:
    """
    Checks if a variable behaves like a valid database connection object
    by checking for the presence and callability of an 'execute' method.

    Args:
        conn (Any): The variable to check.

    Returns:
        bool: True if the variable has a callable 'execute' method, False otherwise.
    """
    return hasattr(conn, 'execute') and callable(getattr(conn, 'execute'))


def rate_daily_to_monthly(rate: float) -> float:
    """
    Converts a daily interest rate to a monthly interest rate.
    Args:
        rate (float): The daily interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent monthly interest rate.
    """
    return (1 + rate) ** 30 - 1


def rate_monthly_to_daily(rate: float) -> float:
    """
    Converts a monthly interest rate to a daily interest rate.
    Args:
        rate (float): The monthly interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent daily interest rate.
    """
    return (1 + rate) ** (1 / 30) - 1


def rate_monthly_to_annual(rate: float) -> float:
    """
    Converts a monthly interest rate to an annual interest rate.
    Args:
        rate (float): The monthly interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent annual interest rate.
    """
    return (1 + rate) ** 12 - 1


def rate_annual_to_monthly(rate: float) -> float:
    """
    Converts an annual interest rate to a monthly interest rate.
    Args:
        rate (float): The annual interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent monthly interest rate.
    """
    return (1 + rate) ** (1 / 12) - 1


def rate_annual_to_daily(rate: float) -> float:
    """
    Converts an annual interest rate to a daily interest rate.
    Args:
        rate (float): The annual interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent daily interest rate (considering 360 days/year).
    """
    return (1 + rate) ** (1 / 360) - 1


def rate_daily_to_annual(rate: float) -> float:
    """
    Converts a daily interest rate to an annual interest rate.
    Args:
        rate (float): The daily interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent annual interest rate (considering 360 days/year).
    """
    return (1 + rate) ** 360 - 1


def stock_return_rate(current: float, previous: Optional[float]) -> Optional[float]:
    """
    Calculates the simple return rate of a stock.

    Args:
        current (float): The current price of the stock.
        previous (Optional[float]): The previous price of the stock.

    Returns:
        Optional[float]: The return rate (e.g., 0.1 for 10%), or None if previous price is None.
    """
    if previous is None or previous == 0: # Avoid division by zero
        return None
    return current / previous - 1


def stock_adjusted_return_rate(
        current: float, previous: Optional[float], factor: float = 1,
        dividend_yeld: float = 0, tax: Optional[float] = None # Changed default tax to None for clarity
) -> Optional[float]:
    """
    Calculates the adjusted return rate of a stock, considering splits/inplits, dividends, and taxes.

    Args:
        current (float): The current price of the stock.
        previous (Optional[float]): The previous price of the stock.
        factor (float, optional): Adjustment factor for splits/inplits affecting the current price. Defaults to 1.
        dividend_yeld (float, optional): Dividend yield paid between previous and current price. Defaults to 0.
        tax (Optional[float], optional): Tax rate applied to the dividend yield (e.g., 0.15 for 15%).
                                         If None, no tax is applied. Defaults to None.

    Returns:
        Optional[float]: The adjusted return rate, or None if previous price is None or zero.
    """
    if previous is None or previous == 0: # Avoid division by zero
        return None

    factor = factor or 1
    dividend_yeld = dividend_yeld or 0

    # Apply tax only if it's provided and non-negative
    if tax is not None and tax >= 0:
        dividend_yeld_after_tax = dividend_yeld * (1 - tax)
    else:
        dividend_yeld_after_tax = dividend_yeld # No tax or invalid tax means full dividend

    # Ensure denominator is not zero after subtracting dividend
    denominator = previous - dividend_yeld_after_tax
    if denominator == 0:
        return None # Avoid division by zero

    return (current * factor) / denominator - 1


def stock_adjusted_price(
        adjusted: float, adjusted_return_rate: Optional[float]
) -> Optional[float]:
    """
    Calculates the previous adjusted price based on the current adjusted price and the adjusted return rate.

    Args:
        adjusted (float): The current adjusted price.
        adjusted_return_rate (Optional[float]): The adjusted return rate between the previous and current price.

    Returns:
        Optional[float]: The calculated previous adjusted price, or None if rate is None or denominator is zero.
    """
    if adjusted_return_rate is None:
        return None

    denominator = 1 + adjusted_return_rate
    if denominator == 0:
        return None # Avoid division by zero

    return adjusted / denominator


def stock_adjusted_return_rate_check(current: float, previous_adjusted: Optional[float]) -> Optional[float]:
    """
    Calculates the return rate using the current price and the previously calculated adjusted price.
    Useful for verification.

    Args:
        current (float): The current price of the stock.
        previous_adjusted (Optional[float]): The previously calculated adjusted price.

    Returns:
        Optional[float]: The return rate, or None if previous_adjusted is None or zero.
    """
    if previous_adjusted is None or previous_adjusted == 0:
        return None
    return current / previous_adjusted - 1


def stock_event_factor(expression: Optional[str]) -> Tuple[Optional[str], float]:
    """
    Analyzes a stock event expression (split/inplit) and returns the event type and adjustment factor.

    The expression should be in the format 'X:Y'.
    - For a split (e.g., 2:1), the factor is X.
    - For an inplit (e.g., 1:10), the factor is 1/Y.

    Args:
        expression (Optional[str]): The stock event expression (e.g., "2:1", "1:10").
                                     If None or empty, returns (None, 1.0).

    Returns:
        Tuple[Optional[str], float]: A tuple containing the event type ('SPLIT' or 'INPLIT')
                                     and the calculated factor. Returns (None, 1.0) for no event.

    Raises:
        ValueError: If the expression format is invalid or ratios are non-positive.
    """
    if expression is None or len(expression) == 0:
        return None, 1.0 # Return 1.0 for factor when no expression

    # Use a stricter check for string type before replace
    as_float = lambda x: float(str(x).replace(',', '.'))

    event: Optional[str] = None
    factor: float = 1.0 # Default factor to 1.0

    parts = expression.split(':')

    # Expect exactly two parts after splitting by ':'
    if len(parts) == 2:
        try:
            part1 = as_float(parts[0])
            part2 = as_float(parts[1])
        except ValueError:
             raise ValueError(f"Invalid numeric values in expression '{expression}'")

        if part1 <= 0 or part2 <= 0:
             raise ValueError(f"Ratios must be positive in expression '{expression}'")

        # Determine event type and factor based on which part is 1.0
        if part2 == 1.0 and part1 != 1.0: # SPLIT (e.g., 2:1, 10:1)
            factor = part1
            event = 'SPLIT'
        elif part1 == 1.0 and part2 != 1.0: # INPLIT (e.g., 1:10, 1:5)
            factor = part1 / part2
            event = 'INPLIT'
        elif part1 == 1.0 and part2 == 1.0: # 1:1 case, no change
             event = None # Or specific event type like 'NO_CHANGE'?
             factor = 1.0
        else:
            # Invalid ratio format (neither part is 1.0, or both are not 1.0)
            raise ValueError(f"Invalid ratio format in expression '{expression}'. Must be 'X:1' or '1:Y' (where X, Y != 1).")

        return event, factor
    else:
        # Invalid format (not X:Y)
        raise ValueError(f"Invalid expression format '{expression}'. Expected 'X:Y'.")


def get_investment_table(df: pd.DataFrame, investment_amount: float) -> pd.DataFrame:
    """
    Calculates investment allocation metrics based on profit/loss weighting.

    This function takes a DataFrame with asset information and calculates how
    a given investment amount should be distributed among those assets.
    The allocation is inversely proportional to the adjusted profit/loss,
    meaning assets with lower profit (or higher loss) receive a larger
    proportion of the new investment.

    Args:
        df (pd.DataFrame): DataFrame containing at least the columns:
            'Ticker' (str): Asset identifier.
            'Price' (float): Current market price of the asset.
            'Quantity' (float): Current quantity held of the asset.
            'Average Price' (float): Average purchase price of the asset.
        investment_amount (float): The total amount to be invested/allocated.

    Returns:
        pd.DataFrame: The original DataFrame with added columns:
            'Profit/Loss' (float): Total profit or loss for the asset.
            'Adjusted Profit/Loss' (float): Profit/Loss adjusted so the minimum is zero.
            'Weight' (float): Inverse of adjusted profit/loss (with smoothing).
            'Proportion' (float): Normalized weight, representing the investment proportion.
            'Investment Value' (float): Amount to invest in this asset based on proportion.
            'Quantity to Buy' (float): Number of shares to buy with the allocated investment value.

    Raises:
        ValueError: If the input DataFrame is missing any of the required columns.
    """
    # Define required columns
    required_columns = {'Ticker', 'Price', 'Quantity', 'Average Price'}

    # Check for missing columns
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    # Ensure numeric types for calculation columns
    for col in ['Price', 'Quantity', 'Average Price']:
        df[col] = pd.to_numeric(df[col], errors='coerce') # Coerce errors to NaN

    # Drop rows with NaN in essential columns after coercion
    df.dropna(subset=['Price', 'Quantity', 'Average Price'], inplace=True)
    if df.empty:
        # Return empty DataFrame with expected columns if all rows had NaNs
        return df.reindex(columns=list(df.columns) + ['Profit/Loss', 'Adjusted Profit/Loss', 'Weight', 'Proportion', 'Investment Value', 'Quantity to Buy'])


    # Calculate Profit/Loss
    df['Profit/Loss'] = (df['Price'] - df['Average Price']) * df['Quantity']

    # Calculate Adjusted Profit/Loss (minimum value adjusted to zero)
    min_profit_loss: float = df['Profit/Loss'].min()
    df['Adjusted Profit/Loss'] = df['Profit/Loss'] - min_profit_loss

    # Calculate Weight (using k = 0.01 to avoid division by zero or negative weights)
    k: float = 0.01
    # Ensure Adjusted Profit/Loss is non-negative before adding k
    df['Weight'] = 1 / (df['Adjusted Profit/Loss'].clip(lower=0) + k)

    # Calculate Proportion (normalize weights to sum to 1)
    total_weights: float = df['Weight'].sum()
    if total_weights == 0: # Avoid division by zero if all weights are zero
        # Assign equal proportion or handle as error/specific case
        df['Proportion'] = 1 / len(df) if len(df) > 0 else 0
    else:
        df['Proportion'] = df['Weight'] / total_weights

    # Calculate Investment Value (distribute total value according to proportion)
    df['Investment Value'] = df['Proportion'] * investment_amount

    # Calculate Quantity to Buy (handle potential division by zero if Price is 0)
    df['Quantity to Buy'] = df.apply(
        lambda row: row['Investment Value'] / row['Price'] if row['Price'] != 0 else 0,
        axis=1
    )

    return df


if not os.path.exists(USER_APP_FOLDER):
    os.makedirs(USER_APP_FOLDER)

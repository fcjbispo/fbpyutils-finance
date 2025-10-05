"""
fbpyutils_finance.calculators - Financial Rate and Stock Return Calculators

Purpose: This module provides utility functions for converting interest rates between different time periods (daily, monthly, annual) using compound interest formulas, and for calculating stock returns with adjustments for dividends, taxes, splits, and inplits.

Main contents:
- Rate conversion functions: rate_daily_to_monthly(), rate_monthly_to_daily(), rate_monthly_to_annual(), rate_annual_to_monthly(), rate_annual_to_daily(), rate_daily_to_annual()
- Stock return functions: stock_return_rate(), stock_adjusted_return_rate(), stock_adjusted_price(), stock_adjusted_return_rate_check(), stock_event_factor()

High-level usage pattern:
Import specific functions for rate conversions or stock calculations. For example, convert rates with rate_annual_to_monthly(annual_rate), or compute adjusted stock returns with stock_adjusted_return_rate(current_price, previous_price, factor, dividend_yield, tax_rate).

# Related links:
https://clubedospoupadores.com/educacao-financeira/calculadora-taxa.html
https://www.youtube.com/watch?v=JOqK2EGdxbQ

Examples:
>>> from fbpyutils_finance.calculators import rate_annual_to_monthly, stock_return_rate
>>> monthly_rate = rate_annual_to_monthly(0.12)  # 12% annual to monthly
>>> print(f"{monthly_rate:.6f}")
0.009489
>>> return_rate = stock_return_rate(50.0, 45.0)
>>> print(f"{return_rate:.4f}")
0.1111
"""
from typing import Optional, Tuple

from fbpyutils_finance import logger


def rate_daily_to_monthly(rate: float) -> float:
    """
    Converts a daily interest rate to a monthly interest rate using compound interest.

    Assumes 30 days in a month for the conversion.

    Args:
        rate (float): The daily interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent monthly interest rate.

    Examples:
        >>> rate_daily_to_monthly(0.0005)  # 0.05% daily
        0.015376
        Minimal usage: Converts daily rate to monthly equivalent, returns 0.015376 for input 0.0005.
    """
    logger.info(f"rate_daily_to_monthly entry: rate={rate}")
    result = (1 + rate) ** 30 - 1
    logger.info(f"rate_daily_to_monthly exit: returning {result}")
    return result


def rate_monthly_to_daily(rate: float) -> float:
    """
    Converts a monthly interest rate to a daily interest rate using compound interest.

    Assumes 30 days in a month for the conversion.

    Args:
        rate (float): The monthly interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent daily interest rate.

    Examples:
        >>> rate_monthly_to_daily(0.01)  # 1% monthly
        0.000328
        Minimal usage: Converts monthly rate to daily equivalent, returns 0.000328 for input 0.01.
    """
    logger.info(f"rate_monthly_to_daily entry: rate={rate}")
    result = (1 + rate) ** (1 / 30) - 1
    logger.info(f"rate_monthly_to_daily exit: returning {result}")
    return result


def rate_monthly_to_annual(rate: float) -> float:
    """
    Converts a monthly interest rate to an annual interest rate using compound interest.

    Assumes 12 months in a year for the conversion.

    Args:
        rate (float): The monthly interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent annual interest rate.

    Examples:
        >>> rate_monthly_to_annual(0.01)  # 1% monthly
        0.126825
        Minimal usage: Converts monthly rate to annual equivalent, returns 0.126825 for input 0.01.
    """
    logger.info(f"rate_monthly_to_annual entry: rate={rate}")
    result = (1 + rate) ** 12 - 1
    logger.info(f"rate_monthly_to_annual exit: returning {result}")
    return result


def rate_annual_to_monthly(rate: float) -> float:
    """
    Converts an annual interest rate to a monthly interest rate using compound interest.

    Assumes 12 months in a year for the conversion.

    Args:
        rate (float): The annual interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent monthly interest rate.

    Examples:
        >>> rate_annual_to_monthly(0.12)  # 12% annual
        0.009489
        Minimal usage: Converts annual rate to monthly equivalent, returns 0.009489 for input 0.12.
    """
    logger.info(f"rate_annual_to_monthly entry: rate={rate}")
    result = (1 + rate) ** (1 / 12) - 1
    logger.info(f"rate_annual_to_monthly exit: returning {result}")
    return result


def rate_annual_to_daily(rate: float) -> float:
    """
    Converts an annual interest rate to a daily interest rate using compound interest.

    Assumes 360 days in a year for the conversion (common in financial calculations).

    Args:
        rate (float): The annual interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent daily interest rate.

    Examples:
        >>> rate_annual_to_daily(0.12)  # 12% annual
        0.000298
        Minimal usage: Converts annual rate to daily equivalent, returns 0.000298 for input 0.12.
    """
    logger.info(f"rate_annual_to_daily entry: rate={rate}")
    result = (1 + rate) ** (1 / 360) - 1
    logger.info(f"rate_annual_to_daily exit: returning {result}")
    return result


def rate_daily_to_annual(rate: float) -> float:
    """
    Converts a daily interest rate to an annual interest rate using compound interest.

    Assumes 360 days in a year for the conversion (common in financial calculations).

    Args:
        rate (float): The daily interest rate (e.g., 0.01 for 1%).

    Returns:
        float: The equivalent annual interest rate.

    Examples:
        >>> rate_daily_to_annual(0.0003)  # 0.03% daily
        0.113508
        Minimal usage: Converts daily rate to annual equivalent, returns 0.113508 for input 0.0003.
    """
    logger.info(f"rate_daily_to_annual entry: rate={rate}")
    result = (1 + rate) ** 360 - 1
    logger.info(f"rate_daily_to_annual exit: returning {result}")
    return result


def stock_return_rate(current: float, previous: Optional[float]) -> Optional[float]:
    """
    Calculates the simple return rate of a stock.

    This is the basic percentage change from previous to current price.

    Args:
        current (float): The current price of the stock.
        previous (Optional[float]): The previous price of the stock.

    Returns:
        Optional[float]: The return rate (e.g., 0.1 for 10%), or None if previous price is None or zero.

    Examples:
        >>> stock_return_rate(50.0, 45.0)
        0.1111111111111111
        Minimal usage: Computes simple return, returns 0.1111 (11.11%) for current=50.0, previous=45.0.
    """
    logger.info(f"stock_return_rate entry: current={current}, previous={previous}")
    if previous is None or previous == 0:  # Avoid division by zero
        logger.warning("Cannot calculate return rate: previous price is None or zero")
        logger.info(f"stock_return_rate exit: returning None due to invalid previous")
        return None
    result = current / previous - 1
    logger.info(f"stock_return_rate exit: returning {result}")
    return result


def stock_adjusted_return_rate(
    current: float,
    previous: Optional[float],
    factor: float = 1,
    dividend_yeld: float = 0,
    tax: Optional[float] = None,  # Changed default tax to None for clarity
) -> Optional[float]:
    """
    Calculates the adjusted return rate of a stock, considering splits/inplits, dividends, and taxes.

    Adjusts the previous price for dividends (after tax) and applies factor to current price.

    Args:
        current (float): The current price of the stock.
        previous (Optional[float]): The previous price of the stock.
        factor (float, optional): Adjustment factor for splits/inplits affecting the current price. Defaults to 1.
        dividend_yeld (float, optional): Dividend yield paid between previous and current price. Defaults to 0.
        tax (Optional[float], optional): Tax rate applied to the dividend yield (e.g., 0.15 for 15%).
                                         If None, no tax is applied. Defaults to None.

    Returns:
        Optional[float]: The adjusted return rate, or None if previous price is None or zero.

    Examples:
        >>> stock_adjusted_return_rate(50.0, 45.0, factor=1.0, dividend_yeld=1.0, tax=0.15)
        0.130435
        Minimal usage: Computes adjusted return, returns 0.130435 for current=50.0, previous=45.0, dividend_yeld=1.0, tax=0.15.
    """
    logger.info(f"stock_adjusted_return_rate entry: current={current}, previous={previous}, factor={factor}, dividend_yeld={dividend_yeld}, tax={tax}")
    if previous is None or previous == 0:  # Avoid division by zero
        logger.warning("Cannot calculate adjusted return rate: previous price is None or zero")
        logger.info(f"stock_adjusted_return_rate exit: returning None due to invalid previous")
        return None

    factor = factor or 1
    dividend_yeld = dividend_yeld or 0

    # Apply tax only if it's provided and non-negative
    if tax is not None and tax >= 0:
        dividend_yeld_after_tax = dividend_yeld * (1 - tax)
        logger.debug(f"Decision branch: tax applied, dividend_yeld_after_tax={dividend_yeld_after_tax}")
    else:
        dividend_yeld_after_tax = (
            dividend_yeld  # No tax or invalid tax means full dividend
        )
        logger.debug("Decision branch: No tax applied to dividend")

    # Ensure denominator is not zero after subtracting dividend
    denominator = previous - dividend_yeld_after_tax
    if denominator == 0:
        logger.warning("Denominator is zero after dividend adjustment")
        logger.info(f"stock_adjusted_return_rate exit: returning None due to zero denominator")
        return None  # Avoid division by zero

    result = (current * factor) / denominator - 1
    logger.info(f"stock_adjusted_return_rate exit: returning {result}")
    return result


def stock_adjusted_price(
    adjusted: float, adjusted_return_rate: Optional[float]
) -> Optional[float]:
    """
    Calculates the previous adjusted price based on the current adjusted price and the adjusted return rate.

    Reverses the return rate calculation to find the previous price.

    Args:
        adjusted (float): The current adjusted price.
        adjusted_return_rate (Optional[float]): The adjusted return rate between the previous and current price.

    Returns:
        Optional[float]: The calculated previous adjusted price, or None if rate is None or denominator is zero.

    Examples:
        >>> stock_adjusted_price(50.0, 0.1111)
        45.0
        Minimal usage: Reverses return to find previous price, returns 45.0 for adjusted=50.0, rate=0.1111.
    """
    logger.info(f"stock_adjusted_price entry: adjusted={adjusted}, adjusted_return_rate={adjusted_return_rate}")
    if adjusted_return_rate is None:
        logger.warning("Cannot calculate adjusted price: return rate is None")
        logger.info(f"stock_adjusted_price exit: returning None due to None rate")
        return None

    denominator = 1 + adjusted_return_rate
    if denominator == 0:
        logger.warning("Denominator is zero in adjusted price calculation")
        logger.info(f"stock_adjusted_price exit: returning None due to zero denominator")
        return None  # Avoid division by zero

    result = adjusted / denominator
    logger.info(f"stock_adjusted_price exit: returning {result}")
    return result


def stock_adjusted_return_rate_check(
    current: float, previous_adjusted: Optional[float]
) -> Optional[float]:
    """
    Calculates the return rate using the current price and the previously calculated adjusted price.

    Useful for verification of adjustment calculations.

    Args:
        current (float): The current price of the stock.
        previous_adjusted (Optional[float]): The previously calculated adjusted price.

    Returns:
        Optional[float]: The return rate, or None if previous_adjusted is None or zero.

    Examples:
        >>> stock_adjusted_return_rate_check(50.0, 45.0)
        0.1111111111111111
        Minimal usage: Verifies return rate, returns 0.1111 for current=50.0, previous_adjusted=45.0.
    """
    logger.info(f"stock_adjusted_return_rate_check entry: current={current}, previous_adjusted={previous_adjusted}")
    if previous_adjusted is None or previous_adjusted == 0:
        logger.warning("Cannot verify return rate: previous adjusted price is None or zero")
        logger.info(f"stock_adjusted_return_rate_check exit: returning None due to invalid previous_adjusted")
        return None
    result = current / previous_adjusted - 1
    logger.info(f"stock_adjusted_return_rate_check exit: returning {result}")
    return result


def stock_event_factor(expression: Optional[str]) -> Tuple[Optional[str], float]:
    """
    Analyzes a stock event expression (split/inplit) and returns the event type and adjustment factor.

    The expression should be in the format 'X:Y'.
    - For a split (e.g., 2:1), the factor is X (current price multiplied by X).
    - For an inplit (e.g., 1:10), the factor is 1/Y (current price divided by Y).

    Args:
        expression (Optional[str]): The stock event expression (e.g., "2:1", "1:10").
                                     If None or empty, returns (None, 1.0).

    Returns:
        Tuple[Optional[str], float]: A tuple containing the event type ('SPLIT' or 'INPLIT')
                                     and the calculated factor. Returns (None, 1.0) for no event.

    Raises:
        ValueError: If the expression format is invalid or ratios are non-positive.

    Examples:
        >>> stock_event_factor("2:1")
        ('SPLIT', 2.0)
        >>> stock_event_factor("1:10")
        ('INPLIT', 0.1)
        Minimal usage: Parses split/inplit expression, returns event type and factor; for "2:1" returns ('SPLIT', 2.0).
    """
    logger.info(f"stock_event_factor entry: expression={expression}")
    if expression is None or len(expression) == 0:
        logger.debug("Decision branch: No event expression provided, returning default (None, 1.0)")
        result = None, 1.0  # Return 1.0 for factor when no expression
        logger.info(f"stock_event_factor exit: returning {result}")
        return result

    # Use a stricter check for string type before replace
    def as_float(x):
        return float(str(x).replace(",", "."))

    event: Optional[str] = None
    factor: float = 1.0  # Default factor to 1.0

    parts = expression.split(":")

    # Expect exactly two parts after splitting by ':'
    if len(parts) == 2:
        try:
            part1 = as_float(parts[0])
            part2 = as_float(parts[1])
            logger.debug(f"Parsed parts: part1={part1}, part2={part2}")
        except ValueError as e:
            logger.error(f"Invalid numeric values in expression '{expression}': {e}", exc_info=True)
            raise ValueError(f"Invalid numeric values in expression '{expression}'")

        if part1 <= 0 or part2 <= 0:
            logger.error(f"Ratios must be positive in expression '{expression}'")
            raise ValueError(f"Ratios must be positive in expression '{expression}'")

        # Determine event type and factor based on which part is 1.0
        if part2 == 1.0 and part1 != 1.0:  # SPLIT (e.g., 2:1, 10:1)
            factor = part1
            event = "SPLIT"
            logger.debug(f"Decision branch: Identified SPLIT event with factor {factor}")
        elif part1 == 1.0 and part2 != 1.0:  # INPLIT (e.g., 1:10, 1:5)
            factor = part1 / part2
            event = "INPLIT"
            logger.debug(f"Decision branch: Identified INPLIT event with factor {factor}")
        elif part1 == 1.0 and part2 == 1.0:  # 1:1 case, no change
            event = None  # Or specific event type like 'NO_CHANGE'?
            factor = 1.0
            logger.debug("Decision branch: Identified no-change event (1:1)")
        else:
            # Invalid ratio format (neither part is 1.0, or both are not 1.0)
            logger.error(f"Invalid ratio format in expression '{expression}'. Must be 'X:1' or '1:Y' (where X, Y != 1).")
            raise ValueError(
                f"Invalid ratio format in expression '{expression}'. Must be 'X:1' or '1:Y' (where X, Y != 1)."
            )

        result = event, factor
        logger.info(f"stock_event_factor exit: returning {result}")
        return result
    else:
        # Invalid format (not X:Y)
        logger.error(f"Invalid expression format '{expression}'. Expected 'X:Y'.")
        raise ValueError(f"Invalid expression format '{expression}'. Expected 'X:Y'.")

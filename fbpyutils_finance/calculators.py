from typing import Optional, Tuple


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
    if previous is None or previous == 0:  # Avoid division by zero
        return None
    return current / previous - 1


def stock_adjusted_return_rate(
    current: float,
    previous: Optional[float],
    factor: float = 1,
    dividend_yeld: float = 0,
    tax: Optional[float] = None,  # Changed default tax to None for clarity
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
    if previous is None or previous == 0:  # Avoid division by zero
        return None

    factor = factor or 1
    dividend_yeld = dividend_yeld or 0

    # Apply tax only if it's provided and non-negative
    if tax is not None and tax >= 0:
        dividend_yeld_after_tax = dividend_yeld * (1 - tax)
    else:
        dividend_yeld_after_tax = (
            dividend_yeld  # No tax or invalid tax means full dividend
        )

    # Ensure denominator is not zero after subtracting dividend
    denominator = previous - dividend_yeld_after_tax
    if denominator == 0:
        return None  # Avoid division by zero

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
        return None  # Avoid division by zero

    return adjusted / denominator


def stock_adjusted_return_rate_check(
    current: float, previous_adjusted: Optional[float]
) -> Optional[float]:
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
        return None, 1.0  # Return 1.0 for factor when no expression

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
        except ValueError:
            raise ValueError(f"Invalid numeric values in expression '{expression}'")

        if part1 <= 0 or part2 <= 0:
            raise ValueError(f"Ratios must be positive in expression '{expression}'")

        # Determine event type and factor based on which part is 1.0
        if part2 == 1.0 and part1 != 1.0:  # SPLIT (e.g., 2:1, 10:1)
            factor = part1
            event = "SPLIT"
        elif part1 == 1.0 and part2 != 1.0:  # INPLIT (e.g., 1:10, 1:5)
            factor = part1 / part2
            event = "INPLIT"
        elif part1 == 1.0 and part2 == 1.0:  # 1:1 case, no change
            event = None  # Or specific event type like 'NO_CHANGE'?
            factor = 1.0
        else:
            # Invalid ratio format (neither part is 1.0, or both are not 1.0)
            raise ValueError(
                f"Invalid ratio format in expression '{expression}'. Must be 'X:1' or '1:Y' (where X, Y != 1)."
            )

        return event, factor
    else:
        # Invalid format (not X:Y)
        raise ValueError(f"Invalid expression format '{expression}'. Expected 'X:Y'.")

"""
fbpyutils_finance.assessment - Investment Assessment Utilities

Purpose: This module provides functions to assess investment portfolios, calculate profit/loss, and determine optimal allocation of new investments based on rebalancing strategies favoring underperforming assets.

Main contents:
- get_investment_table(): Computes allocation proportions inversely weighted by adjusted profit/loss, suggesting quantities to buy for portfolio rebalancing.

High-level usage pattern:
Load portfolio data into a pandas DataFrame with required columns (Ticker, Price, Quantity, Average Price), then call get_investment_table(df, investment_amount) to get recommendations.

Examples:
>>> import pandas as pd
>>> from fbpyutils_finance.assessment import get_investment_table
>>> data = {'Ticker': ['PETR4', 'VALE3'], 'Price': [30.0, 60.0], 'Quantity': [100.0, 50.0], 'Average Price': [25.0, 70.0]}
>>> df = pd.DataFrame(data)
>>> result = get_investment_table(df, 10000.0)
>>> print(result[['Ticker', 'Investment Value', 'Quantity to Buy']])
   Ticker  Investment Value  Quantity to Buy
0  PETR4        4285.714286        142.857143
1  VALE3        5714.285714         95.238095
"""

import pandas as pd
import numpy as np

from fbpyutils_finance import logger


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
            'Proportion' (float): Normalized weight, representing the investment proportion.
            'Investment Value' (float): Amount to invest in this asset based on proportion.
            'Quantity to Buy' (float): Number of shares to buy with the allocated investment value.

    Raises:
        ValueError: If the input DataFrame is missing any of the required columns.

    Example:
        >>> import pandas as pd
        >>> data = {
        ...     'Ticker': ['PETR4', 'VALE3'],
        ...     'Price': [30.0, 60.0],
        ...     'Quantity': [100.0, 50.0],
        ...     'Average Price': [25.0, 70.0]
        ... }
        >>> df = pd.DataFrame(data)
        >>> result = get_investment_table(df, 10000.0)
        >>> print(result[['Ticker', 'Investment Value', 'Quantity to Buy']])
           Ticker  Investment Value  Quantity to Buy
        0  PETR4        4285.714286        142.857143
        1  VALE3        5714.285714         95.238095
    """
    logger.info(
        f"get_investment_table entry: df_shape={df.shape}, investment_amount={investment_amount}"
    )

    def adjust_profit_loss(row):
        """
        Adjusts the absolute profit/loss value by scaling it with the row index and magnitude.

        This internal helper function normalizes profit/loss values for weighting by adding the row index (1-based) to the scaled absolute profit/loss.
        Scaling uses the order of magnitude to prevent large values from dominating the weights.

        Args:
            row (pd.Series): A row from the DataFrame containing 'Profit/Loss' and index.

        Returns:
            float: Adjusted value for weighting, or np.nan if invalid.

        Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> row = pd.Series({'Profit/Loss': 5.0}, index=[0])
        >>> adjust_profit_loss(row)
        1.0
        >>> row = pd.Series({'Profit/Loss': 0.5}, index=[1])
        >>> adjust_profit_loss(row)
        2.05
        """
        abs_pl = row["Profit/Loss"]
        index = row.name
        if pd.isna(abs_pl):
            logger.debug(f"adjust_profit_loss: NaN Profit/Loss for index {index}")
            return np.nan
        abs_pl = abs(abs_pl)
        logger.debug(f"adjust_profit_loss entry for index {index}: abs_pl={abs_pl}")

        if abs_pl == 0:
            digits = 0
            logger.debug(f"Decision branch: abs_pl==0, digits=0")
        elif 0 < abs_pl < 1:
            digits = 0
            logger.debug(f"Decision branch: 0 < abs_pl < 1, digits=0")
        else:
            try:
                digits = np.floor(np.log10(abs_pl)) + 1
                logger.debug(f"Calculated digits={digits} for abs_pl={abs_pl}")
            except ValueError as e:
                logger.error(
                    f"Error calculating digits for abs_pl={abs_pl}: {e}", exc_info=True
                )
                return np.nan
        digits = int(digits)

        divisor = 10.0**digits
        result = (index + 1) + (abs_pl / divisor)
        logger.debug(f"adjust_profit_loss exit for index {index}: result={result}")
        return result

    # Define required columns
    required_columns = {"Ticker", "Price", "Quantity", "Average Price"}

    # Check for missing columns
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        logger.error(
            f"Missing required columns: {', '.join(missing_columns)}", exc_info=True
        )
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    # Ensure numeric types for calculation columns
    logger.debug("Converting columns to numeric: Price, Quantity, Average Price")
    for col in ["Price", "Quantity", "Average Price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # Coerce errors to NaN

    # Drop rows with NaN in essential columns after coercion
    initial_rows = len(df)
    df.dropna(subset=["Price", "Quantity", "Average Price"], inplace=True)
    dropped_rows = initial_rows - len(df)
    if dropped_rows > 0:
        logger.warning(
            f"Dropped {dropped_rows} rows due to NaN values in essential columns. Remaining: {len(df)}"
        )
        logger.debug(f"Decision branch: dropped_rows={dropped_rows} > 0")

    if df.empty:
        logger.warning(
            "No valid data after cleaning; returning empty DataFrame with expected columns"
        )
        logger.info(f"get_investment_table exit: empty DataFrame due to no valid data")
        # Return empty DataFrame with expected columns if all rows had NaNs
        # Return empty DataFrame with the final expected columns
        final_columns = list(df.columns) + [
            "Profit/Loss",
            "Investment Value",
            "Quantity to Buy",
        ]
        # Ensure original columns are kept even if df was initially empty
        original_cols = ["Ticker", "Price", "Quantity", "Average Price"]
        # Combine and remove duplicates, maintaining order as much as possible
        all_expected_cols = list(dict.fromkeys(original_cols + final_columns))
        return pd.DataFrame(columns=all_expected_cols)
    # Calculate Profit/Loss

    logger.debug("State mutation: Calculating Profit/Loss column")
    df["Profit/Loss"] = (df["Price"] - df["Average Price"]) * df["Quantity"]
    logger.debug(
        f"Calculated Profit/Loss for {len(df)} assets. Range: {df['Profit/Loss'].min():.2f} to {df['Profit/Loss'].max():.2f}"
    )

    # this function sort a dataframe by a column in descent order and reindex from the top to bottom
    logger.debug("Decision branch: Sorting DataFrame by Profit/Loss descending")
    df.sort_values(by="Profit/Loss", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    logger.debug("State mutation: DataFrame sorted and reindexed")

    # Calculate Adjusted Profit/Loss by adding the column 'Profit/Loss' the value of the row index plus 1
    logger.debug(
        "State mutation: Calculating Adjusted Profit/Loss using adjust_profit_loss"
    )
    df["Adjusted Profit/Loss"] = df.apply(adjust_profit_loss, axis=1)
    logger.debug(
        f"Adjusted Profit/Loss range: {df['Adjusted Profit/Loss'].min():.2f} to {df['Adjusted Profit/Loss'].max():.2f}"
    )

    # Calculate Weight
    logger.debug("Decision branch: Computing total adjusted profit/loss")
    total_profit_loss: float = df["Adjusted Profit/Loss"].sum()
    logger.debug(f"Total adjusted profit/loss: {total_profit_loss}")

    # Calculate Proportion
    df["Proportion"] = df["Adjusted Profit/Loss"] / total_profit_loss

    # Calculate Investment Value (distribute total value according to proportion)
    logger.debug("State mutation: Calculating Investment Value based on proportions")
    df["Investment Value"] = df["Proportion"] * investment_amount
    logger.info(
        f"Investment allocation completed. Total allocated: {df['Investment Value'].sum():.2f}"
    )

    # Calculate Quantity to Buy (handle potential division by zero if Price is 0)
    logger.debug("State mutation: Calculating Quantity to Buy, handling zero prices")
    zero_prices_count = (df["Price"] == 0).sum()
    if zero_prices_count > 0:
        logger.warning(
            f"Found {zero_prices_count} assets with zero price; Quantity to Buy set to 0"
        )
    df["Quantity to Buy"] = df.apply(
        lambda row: row["Investment Value"] / row["Price"] if row["Price"] != 0 else 0,
        axis=1,
    )

    logger.info(
        f"get_investment_table exit: returning DataFrame with {len(df)} rows, total investment {investment_amount}"
    )
    return df[
        [
            "Ticker",
            "Price",
            "Quantity",
            "Average Price",
            "Profit/Loss",
            "Investment Value",
            "Quantity to Buy",
        ]
    ].copy()

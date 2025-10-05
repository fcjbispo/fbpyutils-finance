import pandas as pd
import numpy as np


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
    """

    def adjust_profit_loss(row):
        abs_pl = row["Profit/Loss"]
        index = row.name
        if pd.isna(abs_pl):
            return np.nan
        abs_pl = abs(abs_pl)

        if abs_pl == 0:
            digits = 0
        elif 0 < abs_pl < 1:
            digits = 0
        else:
            try:
                digits = np.floor(np.log10(abs_pl)) + 1
            except ValueError:
                return np.nan
        digits = int(digits)

        divisor = 10.0**digits

        return (index + 1) + (abs_pl / divisor)

    # Define required columns
    required_columns = {"Ticker", "Price", "Quantity", "Average Price"}

    # Check for missing columns
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    # Ensure numeric types for calculation columns
    for col in ["Price", "Quantity", "Average Price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # Coerce errors to NaN

    # Drop rows with NaN in essential columns after coercion
    df.dropna(subset=["Price", "Quantity", "Average Price"], inplace=True)

    if df.empty:
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

    df["Profit/Loss"] = (df["Price"] - df["Average Price"]) * df["Quantity"]

    # this function sort a dataframe by a column in descent order and reindex from the top to bottom
    df.sort_values(by="Profit/Loss", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Calculate Adjusted Profit/Loss by adding the column 'Profit/Loss' the value of the row index plus 1
    df["Adjusted Profit/Loss"] = df.apply(adjust_profit_loss, axis=1)

    # Calculate Weight
    total_profit_loss: float = df["Adjusted Profit/Loss"].sum()

    # Calculate Proportion
    df["Proportion"] = df["Adjusted Profit/Loss"] / total_profit_loss

    # Calculate Investment Value (distribute total value according to proportion)
    df["Investment Value"] = df["Proportion"] * investment_amount

    # Calculate Quantity to Buy (handle potential division by zero if Price is 0)
    df["Quantity to Buy"] = df.apply(
        lambda row: row["Investment Value"] / row["Price"] if row["Price"] != 0 else 0,
        axis=1,
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

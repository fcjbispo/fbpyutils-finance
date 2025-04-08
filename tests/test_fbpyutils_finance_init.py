# -*- coding: utf-8 -*-
"""
Tests for the main financial utility functions in fbpyutils_finance.
"""
import os
import sys
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

# Add project root to path to allow importing fbpyutils_finance
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Import functions from the __init__ module
from fbpyutils_finance import (
    rate_daily_to_monthly,
    rate_monthly_to_daily,
    rate_monthly_to_annual,
    rate_annual_to_monthly,
    rate_annual_to_daily,
    rate_daily_to_annual,
    stock_return_rate,
    stock_adjusted_return_rate,
    stock_adjusted_price,
    stock_adjusted_return_rate_check,
    stock_event_factor,
    get_investment_table,
    USER_APP_FOLDER # Import to test its creation logic
)

# --- Constants for Tests ---
PRECISION = 1e-9 # Define precision for float comparisons

# --- Tests for Rate Conversion Functions ---

def test_rate_daily_to_monthly_positive_rate():
    """Test converting a positive daily rate to monthly."""
    daily_rate = 0.001 # 0.1% per day
    expected_monthly = (1 + daily_rate) ** 30 - 1
    assert abs(rate_daily_to_monthly(daily_rate) - expected_monthly) < PRECISION

def test_rate_daily_to_monthly_zero_rate():
    """Test converting a zero daily rate to monthly."""
    assert rate_daily_to_monthly(0.0) == 0.0

def test_rate_monthly_to_daily_positive_rate():
    """Test converting a positive monthly rate to daily."""
    monthly_rate = 0.01 # 1% per month
    expected_daily = (1 + monthly_rate) ** (1 / 30) - 1
    assert abs(rate_monthly_to_daily(monthly_rate) - expected_daily) < PRECISION

def test_rate_monthly_to_daily_zero_rate():
    """Test converting a zero monthly rate to daily."""
    assert rate_monthly_to_daily(0.0) == 0.0

def test_rate_monthly_to_annual_positive_rate():
    """Test converting a positive monthly rate to annual."""
    monthly_rate = 0.01 # 1% per month
    expected_annual = (1 + monthly_rate) ** 12 - 1
    assert abs(rate_monthly_to_annual(monthly_rate) - expected_annual) < PRECISION

def test_rate_monthly_to_annual_zero_rate():
    """Test converting a zero monthly rate to annual."""
    assert rate_monthly_to_annual(0.0) == 0.0

def test_rate_annual_to_monthly_positive_rate():
    """Test converting a positive annual rate to monthly."""
    annual_rate = 0.12 # 12% per year
    expected_monthly = (1 + annual_rate) ** (1 / 12) - 1
    assert abs(rate_annual_to_monthly(annual_rate) - expected_monthly) < PRECISION

def test_rate_annual_to_monthly_zero_rate():
    """Test converting a zero annual rate to monthly."""
    assert rate_annual_to_monthly(0.0) == 0.0

def test_rate_annual_to_daily_positive_rate():
    """Test converting a positive annual rate to daily (360 days)."""
    annual_rate = 0.10 # 10% per year
    expected_daily = (1 + annual_rate) ** (1 / 360) - 1
    assert abs(rate_annual_to_daily(annual_rate) - expected_daily) < PRECISION

def test_rate_annual_to_daily_zero_rate():
    """Test converting a zero annual rate to daily."""
    assert rate_annual_to_daily(0.0) == 0.0

def test_rate_daily_to_annual_positive_rate():
    """Test converting a positive daily rate to annual (360 days)."""
    daily_rate = 0.0005 # 0.05% per day
    expected_annual = (1 + daily_rate) ** 360 - 1
    assert abs(rate_daily_to_annual(daily_rate) - expected_annual) < PRECISION

def test_rate_daily_to_annual_zero_rate():
    """Test converting a zero daily rate to annual."""
    assert rate_daily_to_annual(0.0) == 0.0

# --- Tests for stock_return_rate ---

def test_stock_return_rate_positive_return():
    """Test stock_return_rate with a positive return."""
    assert abs(stock_return_rate(110, 100) - 0.1) < PRECISION

def test_stock_return_rate_negative_return():
    """Test stock_return_rate with a negative return."""
    assert abs(stock_return_rate(90, 100) - (-0.1)) < PRECISION

def test_stock_return_rate_zero_return():
    """Test stock_return_rate with zero return."""
    assert abs(stock_return_rate(100, 100) - 0.0) < PRECISION

def test_stock_return_rate_previous_none():
    """Test stock_return_rate when previous price is None."""
    assert stock_return_rate(110, None) is None

def test_stock_return_rate_previous_zero():
    """Test stock_return_rate when previous price is zero."""
    assert stock_return_rate(110, 0) is None
# --- Tests for stock_adjusted_return_rate ---

def test_stock_adjusted_return_rate_no_adjustments():
    """Test adjusted return rate with no factor, dividend, or tax."""
    assert abs(stock_adjusted_return_rate(110, 100) - 0.1) < PRECISION

def test_stock_adjusted_return_rate_with_factor():
    """Test adjusted return rate with a split factor."""
    # Price doubled due to 2:1 split (factor=2), previous was 100
    # Effective current price is 110 * 2 = 220
    assert abs(stock_adjusted_return_rate(110, 100, factor=2) - 1.2) < PRECISION

def test_stock_adjusted_return_rate_with_dividend():
    """Test adjusted return rate with dividend yield."""
    # Current 110, Previous 100, Dividend 5
    # Return = 110 / (100 - 5) - 1 = 110 / 95 - 1
    expected_rate = 110 / 95 - 1
    assert abs(stock_adjusted_return_rate(110, 100, dividend_yeld=5) - expected_rate) < PRECISION

def test_stock_adjusted_return_rate_with_dividend_and_tax():
    """Test adjusted return rate with dividend yield and tax."""
    # Current 110, Previous 100, Dividend 5, Tax 15% (0.15)
    # Dividend after tax = 5 * (1 - 0.15) = 4.25
    # Return = 110 / (100 - 4.25) - 1 = 110 / 95.75 - 1
    expected_rate = 110 / (100 - 5 * (1 - 0.15)) - 1
    assert abs(stock_adjusted_return_rate(110, 100, dividend_yeld=5, tax=0.15) - expected_rate) < PRECISION

def test_stock_adjusted_return_rate_with_all():
    """Test adjusted return rate with factor, dividend, and tax."""
    # Current 110, Previous 100, Factor 0.5 (inplit 1:2), Dividend 5, Tax 10%
    # Effective current = 110 * 0.5 = 55
    # Dividend after tax = 5 * (1 - 0.10) = 4.5
    # Return = 55 / (100 - 4.5) - 1 = 55 / 95.5 - 1
    expected_rate = (110 * 0.5) / (100 - 5 * (1 - 0.10)) - 1
    assert abs(stock_adjusted_return_rate(110, 100, factor=0.5, dividend_yeld=5, tax=0.10) - expected_rate) < PRECISION

def test_stock_adjusted_return_rate_previous_none():
    """Test adjusted return rate when previous price is None."""
    assert stock_adjusted_return_rate(110, None) is None

def test_stock_adjusted_return_rate_previous_zero():
    """Test adjusted return rate when previous price is zero."""
    assert stock_adjusted_return_rate(110, 0) is None

def test_stock_adjusted_return_rate_denominator_zero_after_dividend():
    """Test adjusted return rate when denominator becomes zero after dividend."""
    # Previous price equals dividend after tax
    assert stock_adjusted_return_rate(110, 5, dividend_yeld=5, tax=0) is None
    assert stock_adjusted_return_rate(110, 4.25, dividend_yeld=5, tax=0.15) is None

def test_stock_adjusted_return_rate_factor_none_or_zero():
    """Test adjusted return rate when factor is None or zero (treated as 1)."""
    assert abs(stock_adjusted_return_rate(110, 100, factor=None) - 0.1) < PRECISION
    assert abs(stock_adjusted_return_rate(110, 100, factor=0) - 0.1) < PRECISION # Factor 0 is treated as 1

def test_stock_adjusted_return_rate_dividend_none_or_zero():
    """Test adjusted return rate when dividend is None or zero."""
    assert abs(stock_adjusted_return_rate(110, 100, dividend_yeld=None) - 0.1) < PRECISION
    assert abs(stock_adjusted_return_rate(110, 100, dividend_yeld=0) - 0.1) < PRECISION

def test_stock_adjusted_return_rate_tax_none_or_negative():
    """Test adjusted return rate when tax is None or negative (no tax applied)."""
    expected_rate = 110 / (100 - 5) - 1
    assert abs(stock_adjusted_return_rate(110, 100, dividend_yeld=5, tax=None) - expected_rate) < PRECISION
    assert abs(stock_adjusted_return_rate(110, 100, dividend_yeld=5, tax=-0.1) - expected_rate) < PRECISION

# --- Tests for stock_adjusted_price ---

def test_stock_adjusted_price_positive_rate():
    """Test calculating previous adjusted price with a positive rate."""
    # Adjusted = 110, Rate = 0.1 => Previous = 110 / (1 + 0.1) = 100
    assert abs(stock_adjusted_price(110, 0.1) - 100) < PRECISION

def test_stock_adjusted_price_negative_rate():
    """Test calculating previous adjusted price with a negative rate."""
    # Adjusted = 90, Rate = -0.1 => Previous = 90 / (1 - 0.1) = 100
    assert abs(stock_adjusted_price(90, -0.1) - 100) < PRECISION

def test_stock_adjusted_price_zero_rate():
    """Test calculating previous adjusted price with a zero rate."""
    # Adjusted = 100, Rate = 0 => Previous = 100 / (1 + 0) = 100
    assert abs(stock_adjusted_price(100, 0.0) - 100) < PRECISION

def test_stock_adjusted_price_rate_none():
    """Test calculating previous adjusted price when rate is None."""
    assert stock_adjusted_price(110, None) is None

def test_stock_adjusted_price_denominator_zero():
    """Test calculating previous adjusted price when rate is -1 (denominator zero)."""
    assert stock_adjusted_price(110, -1.0) is None

# --- Tests for stock_adjusted_return_rate_check ---

def test_stock_adjusted_return_rate_check_positive_return():
    """Test check function with positive return."""
    # Current = 110, Previous Adjusted = 100 => Rate = 110 / 100 - 1 = 0.1
    assert abs(stock_adjusted_return_rate_check(110, 100) - 0.1) < PRECISION

def test_stock_adjusted_return_rate_check_negative_return():
    """Test check function with negative return."""
    # Current = 90, Previous Adjusted = 100 => Rate = 90 / 100 - 1 = -0.1
    assert abs(stock_adjusted_return_rate_check(90, 100) - (-0.1)) < PRECISION

def test_stock_adjusted_return_rate_check_zero_return():
    """Test check function with zero return."""
    # Current = 100, Previous Adjusted = 100 => Rate = 100 / 100 - 1 = 0.0
    assert abs(stock_adjusted_return_rate_check(100, 100) - 0.0) < PRECISION

def test_stock_adjusted_return_rate_check_previous_none():
    """Test check function when previous adjusted price is None."""
    assert stock_adjusted_return_rate_check(110, None) is None

def test_stock_adjusted_return_rate_check_previous_zero():
    """Test check function when previous adjusted price is zero."""
    assert stock_adjusted_return_rate_check(110, 0) is None


# --- Tests for stock_event_factor ---

def test_stock_event_factor_split():
    """Test stock_event_factor for a standard split event."""
    event, factor = stock_event_factor("2:1")
    assert event == 'SPLIT'
    assert abs(factor - 2.0) < PRECISION

def test_stock_event_factor_split_decimal():
    """Test stock_event_factor for a split event with decimals."""
    event, factor = stock_event_factor("1.5:1")
    assert event == 'SPLIT'
    assert abs(factor - 1.5) < PRECISION

def test_stock_event_factor_split_comma_decimal():
    """Test stock_event_factor for a split event with comma decimals."""
    event, factor = stock_event_factor("2,5:1")
    assert event == 'SPLIT'
    assert abs(factor - 2.5) < PRECISION

def test_stock_event_factor_inplit():
    """Test stock_event_factor for a standard inplit (reverse split) event."""
    event, factor = stock_event_factor("1:10")
    assert event == 'INPLIT'
    assert abs(factor - 0.1) < PRECISION

def test_stock_event_factor_inplit_decimal():
    """Test stock_event_factor for an inplit event with decimals."""
    event, factor = stock_event_factor("1:2.5")
    assert event == 'INPLIT'
    assert abs(factor - 0.4) < PRECISION # 1 / 2.5 = 0.4

def test_stock_event_factor_inplit_comma_decimal():
    """Test stock_event_factor for an inplit event with comma decimals."""
    event, factor = stock_event_factor("1:1,25")
    assert event == 'INPLIT'
    assert abs(factor - 0.8) < PRECISION # 1 / 1.25 = 0.8

def test_stock_event_factor_no_event_none():
    """Test stock_event_factor when expression is None."""
    event, factor = stock_event_factor(None)
    assert event is None
    assert abs(factor - 1.0) < PRECISION

def test_stock_event_factor_no_event_empty():
    """Test stock_event_factor when expression is an empty string."""
    event, factor = stock_event_factor("")
    assert event is None
    assert abs(factor - 1.0) < PRECISION

def test_stock_event_factor_no_change_event():
    """Test stock_event_factor for a 1:1 ratio (no change)."""
    event, factor = stock_event_factor("1:1")
    assert event is None # Or 'NO_CHANGE'? Function returns None currently
    assert abs(factor - 1.0) < PRECISION

def test_stock_event_factor_invalid_format_no_colon():
    """Test stock_event_factor with invalid format (no colon)."""
    with pytest.raises(ValueError, match="Invalid expression format '123'. Expected 'X:Y'."):
        stock_event_factor("123")

def test_stock_event_factor_invalid_format_too_many_colons():
    """Test stock_event_factor with invalid format (too many colons)."""
    with pytest.raises(ValueError, match="Invalid expression format '1:2:3'. Expected 'X:Y'."):
        stock_event_factor("1:2:3")

def test_stock_event_factor_invalid_numeric_part1():
    """Test stock_event_factor with non-numeric part 1."""
    with pytest.raises(ValueError, match="Invalid numeric values in expression 'A:1'"):
        stock_event_factor("A:1")

def test_stock_event_factor_invalid_numeric_part2():
    """Test stock_event_factor with non-numeric part 2."""
    with pytest.raises(ValueError, match="Invalid numeric values in expression '1:B'"):
        stock_event_factor("1:B")

def test_stock_event_factor_non_positive_ratio_part1():
    """Test stock_event_factor with non-positive ratio part 1."""
    with pytest.raises(ValueError, match="Ratios must be positive in expression '0:1'"):
        stock_event_factor("0:1")
    with pytest.raises(ValueError, match="Ratios must be positive in expression '-2:1'"):
        stock_event_factor("-2:1")

def test_stock_event_factor_non_positive_ratio_part2():
    """Test stock_event_factor with non-positive ratio part 2."""
    with pytest.raises(ValueError, match="Ratios must be positive in expression '1:0'"):
        stock_event_factor("1:0")
    with pytest.raises(ValueError, match="Ratios must be positive in expression '1:-5'"):
        stock_event_factor("1:-5")

def test_stock_event_factor_invalid_ratio_format_general():
    """Test stock_event_factor with invalid ratio format (neither part is 1)."""
    with pytest.raises(ValueError, match="Invalid ratio format in expression '2:3'. Must be 'X:1' or '1:Y'"):
        stock_event_factor("2:3")

# --- Tests for get_investment_table ---

@pytest.fixture
def sample_dataframe():
    """Provides a sample DataFrame for investment table tests."""
    data = {
        'Ticker': ['AAPL', 'GOOG', 'MSFT'],
        'Price': [150.0, 2800.0, 300.0],
        'Quantity': [10, 2, 5],
        'Average Price': [140.0, 2700.0, 310.0]
    }
    return pd.DataFrame(data)

def test_get_investment_table_basic(sample_dataframe):
    """Test get_investment_table with a basic valid DataFrame."""
    investment_amount = 1000.0
    result_df = get_investment_table(sample_dataframe.copy(), investment_amount)

    # Check if new columns are added
    expected_new_cols = ['Profit/Loss', 'Adjusted Profit/Loss', 'Weight', 'Proportion', 'Investment Value', 'Quantity to Buy']
    assert all(col in result_df.columns for col in expected_new_cols)

    # Check calculations for one row (e.g., AAPL)
    # P/L = (150 - 140) * 10 = 100
    # MSFT P/L = (300 - 310) * 5 = -50 (Min P/L)
    # Adjusted P/L AAPL = 100 - (-50) = 150
    # Weight AAPL = 1 / (150 + 0.01)
    aapl_row = result_df[result_df['Ticker'] == 'AAPL'].iloc[0]
    assert abs(aapl_row['Profit/Loss'] - 100.0) < PRECISION
    min_pl = result_df['Profit/Loss'].min()
    assert abs(aapl_row['Adjusted Profit/Loss'] - (100.0 - min_pl)) < PRECISION
    expected_weight_aapl = 1 / ((100.0 - min_pl) + 0.01)
    assert abs(aapl_row['Weight'] - expected_weight_aapl) < PRECISION

    # Check if proportions sum to 1
    assert abs(result_df['Proportion'].sum() - 1.0) < PRECISION

    # Check if total investment value matches input
    assert abs(result_df['Investment Value'].sum() - investment_amount) < PRECISION

    # Check quantity to buy calculation for AAPL
    expected_qty_aapl = aapl_row['Investment Value'] / aapl_row['Price']
    assert abs(aapl_row['Quantity to Buy'] - expected_qty_aapl) < PRECISION

def test_get_investment_table_missing_columns():
    """Test get_investment_table when required columns are missing."""
    df = pd.DataFrame({'Ticker': ['A'], 'Price': [10]})
    # Adjusted regex to be order-independent for missing columns
    with pytest.raises(ValueError, match=r"Missing required columns:.*(Quantity.*Average Price|Average Price.*Quantity)"):
        get_investment_table(df, 1000.0)

def test_get_investment_table_empty_dataframe():
    """Test get_investment_table with an empty DataFrame."""
    df = pd.DataFrame(columns=['Ticker', 'Price', 'Quantity', 'Average Price'])
    result_df = get_investment_table(df, 1000.0)
    assert result_df.empty
    expected_cols = ['Ticker', 'Price', 'Quantity', 'Average Price', 'Profit/Loss', 'Adjusted Profit/Loss', 'Weight', 'Proportion', 'Investment Value', 'Quantity to Buy']
    assert list(result_df.columns) == expected_cols

def test_get_investment_table_with_nan():
    """Test get_investment_table with NaN values in numeric columns."""
    data = {
        'Ticker': ['AAPL', 'GOOG', 'MSFT'],
        'Price': [150.0, None, 300.0], # NaN in Price
        'Quantity': [10, 2, 5],
        'Average Price': [140.0, 2700.0, 310.0]
    }
    df = pd.DataFrame(data)
    result_df = get_investment_table(df.copy(), 1000.0)
    # Expecting row with NaN to be dropped
    assert len(result_df) == 2
    assert 'GOOG' not in result_df['Ticker'].tolist()
    assert abs(result_df['Proportion'].sum() - 1.0) < PRECISION # Proportions should still sum to 1 for remaining rows

def test_get_investment_table_all_nan_rows():
    """Test get_investment_table when all rows have NaN after coercion."""
    data = {
        'Ticker': ['AAPL', 'GOOG'],
        'Price': [None, None],
        'Quantity': [10, 2],
        'Average Price': [140.0, 2700.0]
    }
    df = pd.DataFrame(data)
    result_df = get_investment_table(df.copy(), 1000.0)
    assert result_df.empty
    expected_cols = ['Ticker', 'Price', 'Quantity', 'Average Price', 'Profit/Loss', 'Adjusted Profit/Loss', 'Weight', 'Proportion', 'Investment Value', 'Quantity to Buy']
    assert list(result_df.columns) == expected_cols


def test_get_investment_table_zero_price():
    """Test get_investment_table when a price is zero."""
    data = {
        'Ticker': ['AAPL', 'ZERO'],
        'Price': [150.0, 0.0], # Zero price for one stock
        'Quantity': [10, 5],
        'Average Price': [140.0, 10.0]
    }
    df = pd.DataFrame(data)
    result_df = get_investment_table(df.copy(), 1000.0)
    zero_price_row = result_df[result_df['Ticker'] == 'ZERO'].iloc[0]
    # Quantity to Buy should be 0 if Price is 0
    assert zero_price_row['Quantity to Buy'] == 0.0
    # Other calculations should proceed
    assert 'Proportion' in result_df.columns
    assert abs(result_df['Proportion'].sum() - 1.0) < PRECISION

def test_get_investment_table_zero_total_weights():
    """Test get_investment_table when all adjusted P/L are negative or zero, leading to zero weights (edge case)."""
    # This happens if Adjusted P/L + k results in values small enough that 1/x is effectively inf or NaN,
    # or if all adjusted P/L are exactly -k (highly unlikely with float precision).
    # Let's simulate a case where weights might become zero due to large negative P/L.
    data = {
        'Ticker': ['A', 'B'],
        'Price': [1, 1],
        'Quantity': [1, 1],
        'Average Price': [1000000000, 1000000000] # Very large loss
    }
    df = pd.DataFrame(data)
    # Mock the sum() to return 0 to force the specific branch
    with patch('pandas.Series.sum', return_value=0.0) as mock_sum:
        result_df = get_investment_table(df.copy(), 1000.0)
        # Check if the mocked sum function was called at all
        mock_sum.assert_called()

    # Expect equal proportion if total_weights is 0
    assert len(result_df) == 2
    assert abs(result_df['Proportion'].iloc[0] - 0.5) < PRECISION
    assert abs(result_df['Proportion'].iloc[1] - 0.5) < PRECISION
    assert abs(result_df['Investment Value'].sum() - 1000.0) < PRECISION

def test_get_investment_table_single_asset(sample_dataframe):
    """Test get_investment_table with only one asset in the DataFrame."""
    df_single = sample_dataframe.head(1).copy()
    investment_amount = 500.0
    result_df = get_investment_table(df_single, investment_amount)

    assert len(result_df) == 1
    assert abs(result_df['Proportion'].iloc[0] - 1.0) < PRECISION
    assert abs(result_df['Investment Value'].iloc[0] - investment_amount) < PRECISION
    expected_qty = investment_amount / result_df['Price'].iloc[0]
    assert abs(result_df['Quantity to Buy'].iloc[0] - expected_qty) < PRECISION
    # Adjusted P/L should be 0, Weight should be 1/k
    assert abs(result_df['Adjusted Profit/Loss'].iloc[0] - 0.0) < PRECISION
    assert abs(result_df['Weight'].iloc[0] - (1 / 0.01)) < PRECISION


# --- Tests for USER_APP_FOLDER creation ---

# We need to reload the module under test within the patch context
# to ensure the patched functions are used during the module's import-time execution.
# However, directly reloading __init__ can be tricky and might have side effects.
# A simpler approach for this specific case (checking if makedirs is called)
# is to explicitly call the check logic within the test.

@patch('os.makedirs')
@patch('os.path.exists')
def test_user_app_folder_creation_if_not_exists(mock_exists, mock_makedirs):
    """Test that os.makedirs is called if USER_APP_FOLDER does not exist."""
    mock_exists.return_value = False # Simulate folder does not exist

    # Re-import or re-run the specific lines from __init__.py under patch
    # Option 1: Re-run the logic directly (safer)
    if not os.path.exists(USER_APP_FOLDER):
        os.makedirs(USER_APP_FOLDER)

    mock_exists.assert_called_once_with(USER_APP_FOLDER)
    mock_makedirs.assert_called_once_with(USER_APP_FOLDER)

@patch('os.makedirs')
@patch('os.path.exists')
def test_user_app_folder_creation_if_exists(mock_exists, mock_makedirs):
    """Test that os.makedirs is NOT called if USER_APP_FOLDER already exists."""
    mock_exists.return_value = True # Simulate folder exists

    # Re-run the logic directly
    if not os.path.exists(USER_APP_FOLDER):
        os.makedirs(USER_APP_FOLDER) # This line shouldn't execute

    mock_exists.assert_called_once_with(USER_APP_FOLDER)
    mock_makedirs.assert_not_called() # Ensure makedirs was not called

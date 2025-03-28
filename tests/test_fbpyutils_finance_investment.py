import pytest
import pandas as pd
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from fbpyutils_finance import get_investment_table

# --- Fixtures ---

@pytest.fixture
def sample_portfolio_data() -> dict:
    """Provides sample portfolio data for testing."""
    return {
        'Ticker': ['AAPL', 'GOOGL', 'MSFT'],
        'Price': [150.0, 2500.0, 300.0],
        'Quantity': [10, 2, 5],
        'Average Price': [140.0, 2400.0, 280.0]
    }

@pytest.fixture
def sample_portfolio_df(sample_portfolio_data: dict) -> DataFrame:
    """Provides a sample portfolio DataFrame."""
    return pd.DataFrame(sample_portfolio_data)

# --- Test Cases ---

def test_get_investment_table_valid_input(sample_portfolio_df: DataFrame):
    """Test get_investment_table with a valid DataFrame and investment amount."""
    investment_amount = 10000.0
    result_df = get_investment_table(sample_portfolio_df.copy(), investment_amount) # Use copy to avoid modifying fixture

    # Expected calculations
    # AAPL: P/L = (150 - 140) * 10 = 100
    # GOOGL: P/L = (2500 - 2400) * 2 = 200
    # MSFT: P/L = (300 - 280) * 5 = 100
    profit_loss = pd.Series([100.0, 200.0, 100.0])
    min_profit_loss = 100.0
    # Adj P/L = P/L - min_profit_loss
    adj_profit_loss = pd.Series([0.0, 100.0, 0.0])
    k = 0.01
    # Weight = 1 / (Adj P/L + k)
    weights = pd.Series([1 / (0.0 + k), 1 / (100.0 + k), 1 / (0.0 + k)]) # [100, ~0.00999, 100]
    total_weights = weights.sum() # ~200.00999
    # Proportion = Weight / total_weights
    proportions = weights / total_weights # [~0.499975, ~0.0000499, ~0.499975]
    # Investment Value = Proportion * investment_amount
    investment_values = proportions * investment_amount # [~4999.75, ~0.499, ~4999.75]
    # Quantity to Buy = Investment Value / Price
    quantity_to_buy = investment_values / pd.Series([150.0, 2500.0, 300.0]) # [~33.33, ~0.000199, ~16.66]


    expected_data = {
        'Ticker': ['AAPL', 'GOOGL', 'MSFT'],
        'Price': [150.0, 2500.0, 300.0],
        'Quantity': [10, 2, 5],
        'Average Price': [140.0, 2400.0, 280.0],
        'Profit/Loss': profit_loss,
        'Adjusted Profit/Loss': adj_profit_loss,
        'Weight': weights,
        'Proportion': proportions,
        'Investment Value': investment_values,
        'Quantity to Buy': quantity_to_buy
    }
    expected_df = pd.DataFrame(expected_data)

    # Check columns exist
    expected_columns = [
        'Ticker', 'Price', 'Quantity', 'Average Price', 'Profit/Loss',
        'Adjusted Profit/Loss', 'Weight', 'Proportion', 'Investment Value',
        'Quantity to Buy'
    ]
    assert list(result_df.columns) == expected_columns

    # Check calculations (using pandas testing for precision)
    assert_frame_equal(result_df, expected_df)


def test_get_investment_table_missing_columns():
    """Test that ValueError is raised if required columns are missing."""
    investment_amount = 1000.0
    required_columns = ['Ticker', 'Price', 'Quantity', 'Average Price']

    for col in required_columns:
        df_missing = pd.DataFrame({
            'Ticker': ['A'], 'Price': [10], 'Quantity': [1], 'Average Price': [9]
        })
        df_missing = df_missing.drop(columns=[col])
        with pytest.raises(ValueError, match=f"Missing required columns: {col}"):
            get_investment_table(df_missing, investment_amount)

    # Test missing multiple columns
    df_missing_multiple = pd.DataFrame({'Ticker': ['A'], 'Price': [10]})
    with pytest.raises(ValueError) as excinfo:
         get_investment_table(df_missing_multiple, investment_amount)
    # Check if both missing columns are mentioned (order might vary)
    assert 'Quantity' in str(excinfo.value)
    assert 'Average Price' in str(excinfo.value)


def test_get_investment_table_empty_dataframe():
    """Test get_investment_table with an empty DataFrame."""
    investment_amount = 5000.0
    empty_df = pd.DataFrame(columns=['Ticker', 'Price', 'Quantity', 'Average Price'])
    result_df = get_investment_table(empty_df.copy(), investment_amount)

    expected_columns = [
        'Ticker', 'Price', 'Quantity', 'Average Price', 'Profit/Loss',
        'Adjusted Profit/Loss', 'Weight', 'Proportion', 'Investment Value',
        'Quantity to Buy'
    ]
    # Result should be an empty DataFrame with all the columns
    assert list(result_df.columns) == expected_columns
    assert result_df.empty


def test_get_investment_table_zero_investment():
    """Test get_investment_table with zero investment amount."""
    investment_amount = 0.0
    df = pd.DataFrame({
        'Ticker': ['XYZ'], 'Price': [50.0], 'Quantity': [10], 'Average Price': [45.0]
    })
    result_df = get_investment_table(df.copy(), investment_amount)

    # Profit/Loss, Adj P/L, Weight, Proportion should calculate normally
    # Investment Value and Quantity to Buy should be 0
    assert result_df['Investment Value'].iloc[0] == pytest.approx(0.0)
    assert result_df['Quantity to Buy'].iloc[0] == pytest.approx(0.0)
    assert result_df['Profit/Loss'].iloc[0] == pytest.approx((50.0 - 45.0) * 10) # 50.0
    # Check other columns are present
    assert 'Proportion' in result_df.columns


def test_get_investment_table_zero_price():
    """Test get_investment_table with a zero price for one asset."""
    investment_amount = 1000.0
    df = pd.DataFrame({
        'Ticker': ['ABC', 'ZERO'],
        'Price': [10.0, 0.0], # Zero price for 'ZERO'
        'Quantity': [5, 20],
        'Average Price': [8.0, 1.0]
    })
    result_df = get_investment_table(df.copy(), investment_amount)

    # Check calculations for the non-zero price asset
    assert result_df.loc[result_df['Ticker'] == 'ABC', 'Profit/Loss'].iloc[0] == pytest.approx((10.0 - 8.0) * 5) # 10.0

    # Check calculations for the zero price asset
    assert result_df.loc[result_df['Ticker'] == 'ZERO', 'Profit/Loss'].iloc[0] == pytest.approx((0.0 - 1.0) * 20) # -20.0

    # Quantity to Buy for the zero price asset should be inf or NaN depending on Investment Value
    # If Investment Value is > 0, Quantity to Buy = Value / 0 = inf
    # If Investment Value is 0, Quantity to Buy = 0 / 0 = NaN
    # In this case, P/L is [10, -20]. Min P/L is -20. Adj P/L is [30, 0].
    # Weights are [1/(30+k), 1/(0+k)]. Proportions are calculated.
    # Investment Value will likely be non-zero for 'ZERO'.
    assert result_df.loc[result_df['Ticker'] == 'ZERO', 'Quantity to Buy'].iloc[0] == float('inf')

def test_get_investment_table_all_same_profit_loss(sample_portfolio_df: DataFrame):
    """Test case where all assets have the same Profit/Loss."""
    investment_amount = 10000.0
    # Modify data so all have P/L = 100
    df = pd.DataFrame({
        'Ticker': ['A', 'B', 'C'],
        'Price': [110.0, 60.0, 210.0],
        'Quantity': [10, 20, 5],
        'Average Price': [100.0, 55.0, 190.0] # P/L = 100 for all
    })
    result_df = get_investment_table(df.copy(), investment_amount)

    # If all P/L are same, Adj P/L is 0 for all.
    # Weights are 1/k for all.
    # Proportions should be equal (1/3 for each).
    # Investment Value should be investment_amount / 3 for each.
    expected_proportion = pytest.approx(1/3)
    expected_investment = pytest.approx(investment_amount / 3)

    # Check each value in the Series individually
    for val in result_df['Adjusted Profit/Loss']:
        assert val == pytest.approx(0.0)
    # Keep other assertions using all() as they compare against approx objects directly
    assert all(result_df['Proportion'] == expected_proportion)
    assert all(result_df['Investment Value'] == expected_investment)
    assert result_df['Quantity to Buy'].iloc[0] == pytest.approx(expected_investment / 110.0)
    assert result_df['Quantity to Buy'].iloc[1] == pytest.approx(expected_investment / 60.0)
    assert result_df['Quantity to Buy'].iloc[2] == pytest.approx(expected_investment / 210.0)
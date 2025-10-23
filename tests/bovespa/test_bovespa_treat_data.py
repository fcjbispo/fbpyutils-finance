import pytest
import pandas as pd
from datetime import date
import numpy as np # For NaN representation if needed, though fillna(0) handles it

from fbpyutils_finance.bovespa import StockHistory

# Fixture for a sample raw DataFrame mimicking read_fwf output
@pytest.fixture
def sample_raw_dataframe():
    """Creates a sample raw pandas DataFrame similar to read_fwf output."""
    data = {
        'record_type': ['0', '1', '1', '99'], # Header, Data, Data, Footer
        'trade_date': ['HEADERDT', '20230115', '20230116', 'FOOTERDT'],
        'bdi_code': ['HBDI', '02', '10', 'FBDI'],
        'ticker': ['HTICK', 'PETR4', 'VALE3', 'FTICK'],
        'market_type': ['HMKT', '10', '20', 'FMKT'],
        'ticker_issuer': ['HISSU', 'PETROBRAS', 'VALE', 'FISSU'],
        'ticker_specs': ['HSPEC', 'PN', 'ON', 'FSPEC'],
        'term_days': ['HTERM', ' ', '090', 'FTERM'], # Example with space
        'currency': ['HCUR', 'REA', 'REA', 'FCUR'],
        'open_value': ['HOPEN', '000002550', '000008500', 'FOPEN'], # 25.50, 85.00
        'max_value': ['HMAX', '000002600', '000008600', 'FMAX'],   # 26.00, 86.00
        'min_value': ['HMIN', '000002500', '000008450', 'FMIN'],   # 25.00, 84.50
        'average_value': ['HAVG', '000002560', '000008550', 'FAVG'], # 25.60, 85.50
        'close_value': ['HCLOSE', '000002580', '000008580', 'FCLOSE'],# 25.80, 85.80
        'best_buy_offer': ['HBUY', '000002579', '000008575', 'FBUY'],
        'best_sell_offer': ['HSELL', '000002581', '000008585', 'FSELL'],
        'total_trades': ['HTRAD', '0005000', '0010000', 'FTRAD'],
        'total_trades_papers': ['HPAPR', '000100000', '000200000', 'FPAPR'],
        'total_trades_value': ['HVAL', '0000258000000', '0001716000000', 'FVAL'], # 258000.00, 1716000.00
        'option_market_current_price': ['HOPTPR', '0000000000000', '0000000000000', 'FOPTPR'],
        'option_market_current_price_adjustment_indicator': ['HOPTI', '0', '0', 'FOPTI'],
        'option_market_due_date': ['HOPTD', '00000000', '20241220', 'FOPTD'],
        'ticker_trade_factor': ['HFACT', '0000001', '0000001', 'FFACT'],
        'option_market_current_price_in_points': ['HPTS', '0000000000000', '0000000000000', 'FPTS'],
        'ticker_isin_code': ['HISIN', 'BRPETRACNPR6', 'BRVALEACNOR0', 'FISIN'],
        'ticker_distribution_number': ['HDIST', '001', '002', 'FDIST']
    }
    # Ensure all columns exist as defined in StockHistory._col_names
    df = pd.DataFrame(data, columns=StockHistory._col_names)
    # Ensure numeric-like columns are strings initially, as read_fwf would do
    for col in StockHistory._col_names:
         if col not in ['record_type', 'trade_date', 'ticker', 'ticker_issuer', 'ticker_specs', 'currency', 'ticker_isin_code', 'ticker_distribution_number', 'bdi_code', 'market_type', 'term_days', 'option_market_current_price_adjustment_indicator', 'option_market_due_date', 'ticker_trade_factor']: # Keep some as strings
              # Convert potential non-string values (like integers if accidentally created) back to string
              df[col] = df[col].astype(str)
    return df


# Test cases for _treat_data method
# =================================

# Use a dummy download folder for StockHistory initialization
@pytest.fixture
def stock_history_instance(tmp_path):
    """Provides a StockHistory instance with a temporary download folder."""
    folder = tmp_path / "treat_data_test"
    folder.mkdir()
    return StockHistory(download_folder=str(folder))

def test_treat_data_default(stock_history_instance, sample_raw_dataframe):
    """
    Test _treat_data with default options (original_names=False, compact=True).
    """
    processed_df = stock_history_instance._treat_data(sample_raw_dataframe, original_names=False, compact=True)

    # Check shape (only data rows, compact columns)
    assert processed_df.shape == (2, len(StockHistory._data_columns))

    # Check columns names are the translated, compact ones
    assert list(processed_df.columns) == StockHistory._data_columns

    # Check date conversion
    assert processed_df['trade_date'].tolist() == [date(2023, 1, 15), date(2023, 1, 16)]
    assert pd.api.types.is_object_dtype(processed_df['trade_date']) # Dates are stored as objects in pandas

    # Check float conversion for a few columns
    assert processed_df['open_value'].tolist() == [25.50, 85.00]
    assert pd.api.types.is_float_dtype(processed_df['open_value'])
    assert processed_df['close_value'].tolist() == [25.80, 85.80]
    assert pd.api.types.is_float_dtype(processed_df['close_value'])
    # Corrected expected values based on to_float logic
    assert processed_df['total_trades_value'].tolist() == [2580000.00, 17160000.00]
    assert pd.api.types.is_float_dtype(processed_df['total_trades_value'])

    # Check integer columns (which were read as strings) are still strings or objects
    assert pd.api.types.is_string_dtype(processed_df['bdi_code']) or pd.api.types.is_object_dtype(processed_df['bdi_code'])
    assert pd.api.types.is_string_dtype(processed_df['market_type']) or pd.api.types.is_object_dtype(processed_df['market_type'])

    # Check fillna(0) - term_days had a space, should be ' ' (string), not 0
    # Note: fillna(0) applies to numeric NaNs resulting from conversions, not existing strings.
    # The original data doesn't have NaNs that would become 0 here after filtering.
    # Let's check a value that remains string:
    assert processed_df['term_days'].tolist() == [' ', '090']


def test_treat_data_original_names_compact(stock_history_instance, sample_raw_dataframe):
    """
    Test _treat_data with original_names=True, compact=True.
    """
    processed_df = stock_history_instance._treat_data(sample_raw_dataframe, original_names=True, compact=True)

    # Check shape (only data rows, original compact columns)
    assert processed_df.shape == (2, len(StockHistory._original_data_columns))

    # Check columns names are the original, compact ones
    assert list(processed_df.columns) == StockHistory._original_data_columns

    # Check some values remain the same as default test (conversion happens before renaming)
    assert processed_df['datpre'].tolist() == [date(2023, 1, 15), date(2023, 1, 16)]
    assert processed_df['preabe'].tolist() == [25.50, 85.00]
    assert processed_df['preult'].tolist() == [25.80, 85.80]
    # Corrected expected values based on to_float logic
    assert processed_df['voltot'].tolist() == [2580000.00, 17160000.00]

    # Check data types
    assert pd.api.types.is_object_dtype(processed_df['datpre'])
    assert pd.api.types.is_float_dtype(processed_df['preabe'])
    assert pd.api.types.is_float_dtype(processed_df['preult'])
    assert pd.api.types.is_float_dtype(processed_df['voltot'])
    assert pd.api.types.is_string_dtype(processed_df['codbdi']) or pd.api.types.is_object_dtype(processed_df['codbdi'])


def test_treat_data_translated_names_full(stock_history_instance, sample_raw_dataframe):
    """
    Test _treat_data with original_names=False, compact=False.
    """
    processed_df = stock_history_instance._treat_data(sample_raw_dataframe, original_names=False, compact=False)

    # Check shape (only data rows, all translated columns from _col_names except record_type)
    # The number of columns should be len(_col_names) - 1 because 'record_type' is filtered out implicitly
    # However, the implementation keeps all original columns after filtering and before potential compacting.
    # Let's re-check the logic. It filters by record_type=='1', then applies conversions, then compacts/renames.
    # So, before compacting/renaming, it should have all original columns.
    assert processed_df.shape == (2, len(StockHistory._col_names)) # All columns kept if not compact

    # Check columns names are the translated, full set
    assert list(processed_df.columns) == StockHistory._col_names

    # Check some values
    assert processed_df['trade_date'].tolist() == [date(2023, 1, 15), date(2023, 1, 16)]
    assert processed_df['close_value'].tolist() == [25.80, 85.80]
    assert processed_df['ticker_isin_code'].tolist() == ['BRPETRACNPR6', 'BRVALEACNOR0']
    # Check a column NOT in the compact list
    assert processed_df['option_market_due_date'].tolist() == ['00000000', '20241220'] # Stays string as per converter

def test_treat_data_original_names_full(stock_history_instance, sample_raw_dataframe):
    """
    Test _treat_data with original_names=True, compact=False.
    """
    processed_df = stock_history_instance._treat_data(sample_raw_dataframe, original_names=True, compact=False)

    # Check shape (only data rows, all original columns)
    assert processed_df.shape == (2, len(StockHistory._original_col_names))

    # Check columns names are the original, full set
    assert list(processed_df.columns) == StockHistory._original_col_names

    # Check some values
    assert processed_df['datpre'].tolist() == [date(2023, 1, 15), date(2023, 1, 16)]
    assert processed_df['preult'].tolist() == [25.80, 85.80]
    assert processed_df['codisi'].tolist() == ['BRPETRACNPR6', 'BRVALEACNOR0']
    # Check a column NOT in the original compact list
    assert processed_df['datven'].tolist() == ['00000000', '20241220'] # Stays string

def test_treat_data_empty_input(stock_history_instance):
    """
    Test _treat_data with an empty DataFrame.
    """
    empty_df = pd.DataFrame(columns=StockHistory._col_names)
    processed_df = stock_history_instance._treat_data(empty_df, original_names=False, compact=True)

    # Should return an empty DataFrame with the correct compact columns
    assert processed_df.empty
    assert list(processed_df.columns) == StockHistory._data_columns

def test_treat_data_no_data_rows(stock_history_instance):
    """
    Test _treat_data with a DataFrame containing only header/footer rows.
    """
    data = {
        'record_type': ['0', '99'], # Header, Footer
        'trade_date': ['HEADERDT', 'FOOTERDT'],
        # Add other columns with dummy data matching _col_names
        **{col: ['H', 'F'] for col in StockHistory._col_names if col not in ['record_type', 'trade_date']}
    }
    no_data_df = pd.DataFrame(data, columns=StockHistory._col_names)
    processed_df = stock_history_instance._treat_data(no_data_df, original_names=False, compact=True)

    # Should return an empty DataFrame with the correct compact columns
    assert processed_df.empty
    assert list(processed_df.columns) == StockHistory._data_columns

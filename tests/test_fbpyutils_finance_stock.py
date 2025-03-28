import pytest
from fbpyutils_finance import (
    stock_return_rate,
    stock_adjusted_return_rate,
    stock_adjusted_price,
    stock_adjusted_return_rate_check,
    stock_event_factor
)

# --- Tests for stock_return_rate ---

def test_stock_return_rate_positive_return():
    """Test stock_return_rate with a positive return."""
    assert stock_return_rate(current=110.0, previous=100.0) == pytest.approx(0.1)

def test_stock_return_rate_negative_return():
    """Test stock_return_rate with a negative return."""
    assert stock_return_rate(current=95.0, previous=100.0) == pytest.approx(-0.05)

def test_stock_return_rate_zero_return():
    """Test stock_return_rate with no change in price."""
    assert stock_return_rate(current=100.0, previous=100.0) == pytest.approx(0.0)

def test_stock_return_rate_previous_none():
    """Test stock_return_rate when the previous price is None."""
    assert stock_return_rate(current=100.0, previous=None) is None

def test_stock_return_rate_previous_zero():
    """Test stock_return_rate when the previous price is zero (division by zero)."""
    with pytest.raises(ZeroDivisionError):
        stock_return_rate(current=100.0, previous=0.0)

# --- Tests for stock_adjusted_return_rate ---

def test_stock_adjusted_return_rate_no_adjustments():
    """Test adjusted return rate with default factor, dividend, and tax."""
    # Defaults: factor=1, dividend_yeld=0, tax=2 (makes dividend effect 0)
    assert stock_adjusted_return_rate(current=110.0, previous=100.0) == pytest.approx(0.1)

def test_stock_adjusted_return_rate_with_factor():
    """Test adjusted return rate with a split factor (e.g., 2:1 split)."""
    # factor = 1 / 2 = 0.5 (price halves after split)
    # Effective current price = 110 * 0.5 = 55
    # Return = 55 / 100 - 1 = -0.45
    assert stock_adjusted_return_rate(current=110.0, previous=100.0, factor=0.5) == pytest.approx(-0.45)

def test_stock_adjusted_return_rate_with_dividend():
    """Test adjusted return rate with dividend yield (default tax)."""
    # dividend_yeld = 0.05 (5%)
    # tax = 2 (default) -> effective dividend = 0.05 * abs(1 - 2) = 0.05
    # Return = 110 / (100 - 0.05) - 1 = 110 / 99.95 - 1
    assert stock_adjusted_return_rate(current=110.0, previous=100.0, dividend_yeld=0.05) == pytest.approx(110.0 / (100.0 - 0.05) - 1)

def test_stock_adjusted_return_rate_with_dividend_and_tax():
    """Test adjusted return rate with dividend yield and specific tax."""
    # dividend_yeld = 0.05 (5%)
    # tax = 0.15 (15%) -> effective dividend = 0.05 * abs(1 - 0.15) = 0.05 * 0.85 = 0.0425
    # Return = 110 / (100 - 0.0425) - 1 = 110 / 99.9575 - 1
    assert stock_adjusted_return_rate(current=110.0, previous=100.0, dividend_yeld=0.05, tax=0.15) == pytest.approx(110.0 / (100.0 - 0.0425) - 1)

def test_stock_adjusted_return_rate_with_dividend_tax_none():
    """Test adjusted return rate with dividend yield and tax=None (defaults to 2)."""
    # Same as test_stock_adjusted_return_rate_with_dividend
    assert stock_adjusted_return_rate(current=110.0, previous=100.0, dividend_yeld=0.05, tax=None) == pytest.approx(110.0 / (100.0 - 0.05) - 1)

def test_stock_adjusted_return_rate_with_dividend_tax_negative():
     """Test adjusted return rate with dividend yield and tax=-1."""
     # dividend_yeld = 0.05
     # tax = -1 -> effective dividend = 0.05 * abs(1 - (-1)) = 0.05 * 2 = 0.1
     # Return = 110 / (100 - 0.1) - 1 = 110 / 99.9 - 1
     expected_return = 110.0 / (100.0 - 0.1) - 1
     assert stock_adjusted_return_rate(current=110.0, previous=100.0, dividend_yeld=0.05, tax=-1) == pytest.approx(expected_return)

def test_stock_adjusted_return_rate_all_params():
    """Test adjusted return rate with factor, dividend, and tax."""
    # factor = 0.5
    # dividend_yeld = 0.05
    # tax = 0.15 -> effective dividend = 0.0425
    # Return = (110 * 0.5) / (100 - 0.0425) - 1 = 55 / 99.9575 - 1
    assert stock_adjusted_return_rate(current=110.0, previous=100.0, factor=0.5, dividend_yeld=0.05, tax=0.15) == pytest.approx(55.0 / (100.0 - 0.0425) - 1)

def test_stock_adjusted_return_rate_previous_none():
    """Test adjusted return rate when the previous price is None."""
    assert stock_adjusted_return_rate(current=100.0, previous=None) is None

def test_stock_adjusted_return_rate_previous_zero_dividend_zero():
    """Test adjusted return rate with previous=0 and zero effective dividend."""
    with pytest.raises(ZeroDivisionError):
        stock_adjusted_return_rate(current=100.0, previous=0.0, dividend_yeld=0)

def test_stock_adjusted_return_rate_previous_equals_dividend():
    """Test adjusted return rate when previous price equals effective dividend."""
    # dividend_yeld = 0.05, tax = 0 -> effective dividend = 0.05
    with pytest.raises(ZeroDivisionError):
        stock_adjusted_return_rate(current=100.0, previous=0.05, dividend_yeld=0.05, tax=0)

# --- Tests for stock_adjusted_price ---

def test_stock_adjusted_price_positive_rate():
    """Test stock_adjusted_price with a positive adjusted return rate."""
    # If adjusted price is 110 and rate was 0.1, previous adjusted should be 100
    assert stock_adjusted_price(adjusted=110.0, adjusted_return_rate=0.1) == pytest.approx(100.0)

def test_stock_adjusted_price_negative_rate():
    """Test stock_adjusted_price with a negative adjusted return rate."""
    # If adjusted price is 95 and rate was -0.05, previous adjusted should be 100
    assert stock_adjusted_price(adjusted=95.0, adjusted_return_rate=-0.05) == pytest.approx(100.0)

def test_stock_adjusted_price_zero_rate():
    """Test stock_adjusted_price with a zero adjusted return rate."""
    assert stock_adjusted_price(adjusted=100.0, adjusted_return_rate=0.0) == pytest.approx(100.0)

def test_stock_adjusted_price_rate_minus_one():
    """Test stock_adjusted_price when the adjusted return rate is -1 (division by zero)."""
    with pytest.raises(ZeroDivisionError):
        stock_adjusted_price(adjusted=100.0, adjusted_return_rate=-1.0)

# --- Tests for stock_adjusted_return_rate_check ---

def test_stock_adjusted_return_rate_check_positive():
    """Test stock_adjusted_return_rate_check with positive return."""
    assert stock_adjusted_return_rate_check(current=110.0, previous_adjusted=100.0) == pytest.approx(0.1)

def test_stock_adjusted_return_rate_check_negative():
    """Test stock_adjusted_return_rate_check with negative return."""
    assert stock_adjusted_return_rate_check(current=95.0, previous_adjusted=100.0) == pytest.approx(-0.05)

def test_stock_adjusted_return_rate_check_zero():
    """Test stock_adjusted_return_rate_check with zero return."""
    assert stock_adjusted_return_rate_check(current=100.0, previous_adjusted=100.0) == pytest.approx(0.0)

def test_stock_adjusted_return_rate_check_previous_zero():
    """Test stock_adjusted_return_rate_check with previous_adjusted=0."""
    with pytest.raises(ZeroDivisionError):
        stock_adjusted_return_rate_check(current=100.0, previous_adjusted=0.0)

# --- Tests for stock_event_factor ---

def test_stock_event_factor_split():
    """Test stock_event_factor for a split event (e.g., 2:1)."""
    event, factor = stock_event_factor("2:1")
    assert event == 'SPLIT'
    assert factor == pytest.approx(2.0)

def test_stock_event_factor_split_with_comma():
    """Test stock_event_factor for a split event using comma decimal separator."""
    event, factor = stock_event_factor("1,5:1")
    assert event == 'SPLIT'
    assert factor == pytest.approx(1.5)

def test_stock_event_factor_inplit():
    """Test stock_event_factor for an inplit/reverse split event (e.g., 1:10)."""
    event, factor = stock_event_factor("1:10")
    assert event == 'INPLIT'
    assert factor == pytest.approx(0.1)

def test_stock_event_factor_inplit_with_comma():
    """Test stock_event_factor for an inplit event using comma decimal separator."""
    event, factor = stock_event_factor("1:2,5")
    assert event == 'INPLIT'
    assert factor == pytest.approx(0.4) # 1 / 2.5

def test_stock_event_factor_none_expression():
    """Test stock_event_factor with None expression."""
    event, factor = stock_event_factor(None)
    assert event is None
    assert factor == 1.0

def test_stock_event_factor_empty_expression():
    """Test stock_event_factor with an empty string expression."""
    event, factor = stock_event_factor("")
    assert event is None
    assert factor == 1.0

def test_stock_event_factor_invalid_format_single_number():
    """Test stock_event_factor with invalid format (single number)."""
    with pytest.raises(ValueError, match='Invalid expression 10'):
        stock_event_factor("10")

def test_stock_event_factor_invalid_format_too_many_parts():
    """Test stock_event_factor with invalid format (too many colons)."""
    with pytest.raises(ValueError, match='Invalid expression 1:2:3'):
        stock_event_factor("1:2:3") # Function logic only handles split(':') up to 2 parts

def test_stock_event_factor_invalid_format_non_numeric():
    """Test stock_event_factor with non-numeric parts."""
    with pytest.raises(ValueError): # Specific error depends on float conversion
        stock_event_factor("A:1")
    with pytest.raises(ValueError):
        stock_event_factor("1:B")

def test_stock_event_factor_invalid_ratio():
    """Test stock_event_factor with a ratio not reducible to X:1 or 1:Y."""
    # The function logic implicitly handles only X:1 or 1:Y
    # A case like 2:3 would need clarification on expected behavior.
    # Based on current code, it would raise ValueError because neither part[0] nor part[1] is 1.0
    with pytest.raises(ValueError, match='Invalid expression 2:3'):
         stock_event_factor("2:3")

def test_stock_event_factor_zero_in_ratio():
    """Test stock_event_factor with zero in the ratio (division by zero)."""
    with pytest.raises(ZeroDivisionError):
        stock_event_factor("1:0") # factor = 1 / 0
    # Case "0:1" -> event='SPLIT', factor=0.0 - This seems valid by the code.
    event, factor = stock_event_factor("0:1")
    assert event == 'SPLIT'
    assert factor == 0.0
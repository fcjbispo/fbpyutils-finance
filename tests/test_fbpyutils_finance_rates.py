import pytest
from fbpyutils_finance import (
    rate_daily_to_monthly,
    rate_monthly_to_daily,
    rate_monthly_to_annual,
    rate_annual_to_monthly,
    rate_annual_to_daily,
    rate_daily_to_annual
)

# --- Constants for testing ---
# Using a small daily rate for precision checks
DAILY_RATE = 0.0005  # 0.05% per day

# Calculate expected rates directly for comparison
EXPECTED_MONTHLY_RATE = (1 + DAILY_RATE) ** 30 - 1
EXPECTED_ANNUAL_RATE = (1 + DAILY_RATE) ** 360 - 1
# Also calculate annual from monthly for cross-check
EXPECTED_ANNUAL_FROM_MONTHLY = (1 + EXPECTED_MONTHLY_RATE) ** 12 - 1

# --- Tests for rate_daily_to_monthly ---

def test_rate_daily_to_monthly_positive_rate():
    """Test converting a positive daily rate to monthly."""
    assert rate_daily_to_monthly(DAILY_RATE) == pytest.approx(EXPECTED_MONTHLY_RATE)

def test_rate_daily_to_monthly_zero_rate():
    """Test converting a zero daily rate to monthly."""
    assert rate_daily_to_monthly(0.0) == 0.0

# --- Tests for rate_monthly_to_daily ---

def test_rate_monthly_to_daily_positive_rate():
    """Test converting a positive monthly rate to daily."""
    # Use the calculated monthly rate as input
    calculated_daily = rate_monthly_to_daily(EXPECTED_MONTHLY_RATE)
    assert calculated_daily == pytest.approx(DAILY_RATE)

def test_rate_monthly_to_daily_zero_rate():
    """Test converting a zero monthly rate to daily."""
    assert rate_monthly_to_daily(0.0) == 0.0

# --- Tests for rate_monthly_to_annual ---

def test_rate_monthly_to_annual_positive_rate():
    """Test converting a positive monthly rate to annual."""
    # Use the calculated monthly rate as input
    calculated_annual = rate_monthly_to_annual(EXPECTED_MONTHLY_RATE)
    # Compare against annual rate calculated from monthly
    assert calculated_annual == pytest.approx(EXPECTED_ANNUAL_FROM_MONTHLY)
    # Also compare against annual rate calculated from daily (should be very close)
    assert calculated_annual == pytest.approx(EXPECTED_ANNUAL_RATE)


def test_rate_monthly_to_annual_zero_rate():
    """Test converting a zero monthly rate to annual."""
    assert rate_monthly_to_annual(0.0) == 0.0

# --- Tests for rate_annual_to_monthly ---

def test_rate_annual_to_monthly_positive_rate():
    """Test converting a positive annual rate to monthly."""
    # Use the calculated annual rate as input
    calculated_monthly = rate_annual_to_monthly(EXPECTED_ANNUAL_RATE)
    assert calculated_monthly == pytest.approx(EXPECTED_MONTHLY_RATE)

def test_rate_annual_to_monthly_zero_rate():
    """Test converting a zero annual rate to monthly."""
    assert rate_annual_to_monthly(0.0) == 0.0

# --- Tests for rate_annual_to_daily ---

def test_rate_annual_to_daily_positive_rate():
    """Test converting a positive annual rate to daily (using 360 days)."""
    # Use the calculated annual rate as input
    calculated_daily = rate_annual_to_daily(EXPECTED_ANNUAL_RATE)
    assert calculated_daily == pytest.approx(DAILY_RATE)

def test_rate_annual_to_daily_zero_rate():
    """Test converting a zero annual rate to daily."""
    assert rate_annual_to_daily(0.0) == 0.0

# --- Tests for rate_daily_to_annual ---

def test_rate_daily_to_annual_positive_rate():
    """Test converting a positive daily rate to annual (using 360 days)."""
    assert rate_daily_to_annual(DAILY_RATE) == pytest.approx(EXPECTED_ANNUAL_RATE)

def test_rate_daily_to_annual_zero_rate():
    """Test converting a zero daily rate to annual."""
    assert rate_daily_to_annual(0.0) == 0.0

# --- Test consistency ---

def test_rate_conversion_consistency():
    """Test that converting back and forth yields the original rate."""
    original_daily = 0.001
    monthly = rate_daily_to_monthly(original_daily)
    daily_back = rate_monthly_to_daily(monthly)
    assert daily_back == pytest.approx(original_daily)

    original_monthly = 0.02
    annual = rate_monthly_to_annual(original_monthly)
    monthly_back = rate_annual_to_monthly(annual)
    assert monthly_back == pytest.approx(original_monthly)

    original_annual = 0.10
    daily = rate_annual_to_daily(original_annual)
    annual_back = rate_daily_to_annual(daily)
    assert annual_back == pytest.approx(original_annual)

    # Cross conversions
    annual_from_daily = rate_daily_to_annual(original_daily)
    daily_from_annual = rate_annual_to_daily(annual_from_daily)
    assert daily_from_annual == pytest.approx(original_daily)

    monthly_from_annual = rate_annual_to_monthly(original_annual)
    annual_from_monthly = rate_monthly_to_annual(monthly_from_annual)
    assert annual_from_monthly == pytest.approx(original_annual)
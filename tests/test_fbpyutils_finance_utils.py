import pytest
from unittest.mock import MagicMock

# Assuming the functions are directly accessible from the package
# If they are in __init__.py, this import should work
from fbpyutils_finance import (
    numberize,
    first_or_none,
    random_header,
    is_valid_db_connection
)

# --- Tests for numberize ---

def test_numberize_valid_string():
    """Test numberize with a valid string containing a comma."""
    assert numberize("1,234.56") == 1234.56

def test_numberize_string_without_comma():
    """Test numberize with a string without a comma."""
    assert numberize("1234.56") == 1234.56

def test_numberize_integer_string():
    """Test numberize with a string representing an integer."""
    assert numberize("1,000") == 1000.0

def test_numberize_float_string():
    """Test numberize with a string representing a float."""
    assert numberize("0.75") == 0.75

# --- Tests for first_or_none ---

def test_first_or_none_empty_list():
    """Test first_or_none with an empty list."""
    assert first_or_none([]) is None

def test_first_or_none_non_empty_list():
    """Test first_or_none with a list containing elements."""
    assert first_or_none([1, 2, 3]) == 1

def test_first_or_none_list_with_one_element():
    """Test first_or_none with a list containing a single element."""
    assert first_or_none(['a']) == 'a'

def test_first_or_none_empty_tuple():
    """Test first_or_none with an empty tuple."""
    assert first_or_none(()) is None

def test_first_or_none_non_empty_tuple():
    """Test first_or_none with a tuple containing elements."""
    assert first_or_none((10, 20)) == 10

# --- Tests for random_header ---

def test_random_header_returns_dict():
    """Test that random_header returns a dictionary."""
    header = random_header()
    assert isinstance(header, dict)

def test_random_header_contains_user_agent():
    """Test that the returned header contains a 'User-Agent' key."""
    header = random_header()
    assert 'User-Agent' in header
    assert isinstance(header['User-Agent'], str)

def test_random_header_structure():
    """Test the general structure and types of a randomly selected header."""
    header = random_header()
    assert 'User-Agent' in header
    assert 'Accept' in header
    assert 'Accept-Language' in header
    assert 'Accept-Encoding' in header
    assert 'DNT' in header
    assert 'Connection' in header
    assert 'Upgrade-Insecure-Requests' in header
    assert isinstance(header['User-Agent'], str)
    assert isinstance(header['Accept'], str)
    assert isinstance(header['Accept-Language'], str)
    assert isinstance(header['Accept-Encoding'], str)
    assert isinstance(header['DNT'], str)
    assert isinstance(header['Connection'], str)
    assert isinstance(header['Upgrade-Insecure-Requests'], str)


# --- Tests for is_valid_db_connection ---

def test_is_valid_db_connection_with_valid_mock():
    """Test is_valid_db_connection with a mock object having a callable 'execute' method."""
    mock_conn_valid = MagicMock()
    mock_conn_valid.execute = MagicMock()
    assert is_valid_db_connection(mock_conn_valid) is True

def test_is_valid_db_connection_with_non_callable_execute():
    """Test is_valid_db_connection with a mock object where 'execute' is not callable."""
    mock_conn_non_callable = MagicMock()
    mock_conn_non_callable.execute = "not a function"
    assert is_valid_db_connection(mock_conn_non_callable) is False

def test_is_valid_db_connection_without_execute():
    """Test is_valid_db_connection with a mock object lacking the 'execute' attribute."""
    mock_conn_no_execute = MagicMock(spec=[]) # spec=[] ensures it has no extra attributes
    assert is_valid_db_connection(mock_conn_no_execute) is False

def test_is_valid_db_connection_with_none():
    """Test is_valid_db_connection with None."""
    assert is_valid_db_connection(None) is False

def test_is_valid_db_connection_with_string():
    """Test is_valid_db_connection with a string."""
    assert is_valid_db_connection("not a connection") is False

def test_is_valid_db_connection_with_integer():
    """Test is_valid_db_connection with an integer."""
    assert is_valid_db_connection(123) is False
import datetime
import time
import pytest

from fbpyutils_finance.cvm import utils

def test_get_value_by_index_if_exists():
    lst = [1, 2, 3]
    assert utils.get_value_by_index_if_exists(lst, 1) == 2
    assert utils.get_value_by_index_if_exists(lst, 5) is None
    assert utils.get_value_by_index_if_exists(lst, 5, default='x') == 'x'

def test_make_number_type_int_and_float():
    assert utils.make_number_type("123") == 123
    assert utils.make_number_type("123.45", float) == 123.45
    assert utils.make_number_type(None) is None
    assert utils.make_number_type("-") is None
    assert utils.make_number_type("abc") is None

def test_timelapse_returns_positive():
    start = datetime.datetime.now()
    time.sleep(0.01)
    elapsed = utils.timelapse(start)
    assert elapsed >= 0

def test_make_str_datetime_formats():
    dt = datetime.datetime(2023, 5, 20, 15, 30)
    s = utils.make_str_datetime(dt)
    assert s.startswith("2023-05-20")
    assert utils.make_str_datetime(None) is None

def test_replace_all_replaces():
    text = "abc abc abc"
    replaced = utils.replace_all(text, "abc", "x")
    assert replaced == "x x x"
    # empty old string should not infinite loop
    assert utils.replace_all("test", "", "x") == "test"

def test_make_datetime_valid_and_invalid():
    dt = utils.make_datetime("29-Jan-2023", "08:30")
    assert isinstance(dt, datetime.datetime)
    assert utils.make_datetime(None, "08:30") is None
    assert utils.make_datetime("29-Jan-2023", None) is None
    assert utils.make_datetime("invalid", "time") is None

def test_hash_string_consistency():
    s1 = utils.hash_string("test")
    s2 = utils.hash_string("test")
    assert s1 == s2
    assert isinstance(s1, str)

def test_is_nan_or_empty_cases():
    import math
    import pandas as pd
    assert utils.is_nan_or_empty(None)
    assert utils.is_nan_or_empty('')
    assert utils.is_nan_or_empty(float('nan'))
    assert utils.is_nan_or_empty(pd.NA)
    assert not utils.is_nan_or_empty('abc')
    assert not utils.is_nan_or_empty(123)

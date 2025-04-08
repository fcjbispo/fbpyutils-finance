import pytest
import datetime
import pandas as pd

from fbpyutils_finance.cvm import converters

def test_as_int_valid_cases():
    assert converters.as_int("1.234,56") == 1234
    assert converters.as_int("1234") == 1234
    assert converters.as_int("1,234") == 1
    assert converters.as_int(1234) == 1234
    assert converters.as_int(1234.56) == 1234
    assert converters.as_int("abc") is None
    assert converters.as_int("") is None
    assert converters.as_int(None) is None
    assert converters.as_int(float('nan')) is None

def test_as_float_valid_cases():
    assert converters.as_float("1.234,56") == 1234.56
    assert converters.as_float("1234,56") == 1234.56
    assert converters.as_float("1234.56") == 123456.0
    assert converters.as_float(1234.56) == 1234.56
    assert converters.as_float(1234) == 1234.0
    assert converters.as_float("abc") is None
    assert converters.as_float("") is None
    assert converters.as_float(None) is None
    assert converters.as_float(float('nan')) is None

def test_as_str_cases():
    assert converters.as_str(" test ") == "test"
    assert converters.as_str(123) == "123"
    assert converters.as_str(None) is None
    assert converters.as_str(float('nan')) is None

def test_as_date_various_formats():
    assert converters.as_date("2023-05-20") == datetime.date(2023, 5, 20)
    assert converters.as_date(datetime.datetime(2023, 5, 20, 12, 0)) == datetime.date(2023, 5, 20)
    assert converters.as_date("") is None
    assert converters.as_date(None) is None
    assert converters.as_date("invalid-date") is None
    # With format
    assert converters.as_date("20/05/2023", fmt="%d/%m/%Y") == datetime.date(2023, 5, 20)

def test_as_datetime_various_formats():
    dt = datetime.datetime(2023, 5, 20, 15, 30, 0)
    assert converters.as_datetime("2023-05-20 15:30:00") == dt
    assert converters.as_datetime("2023-05-20") == datetime.datetime(2023, 5, 20, 0, 0)
    assert converters.as_datetime(dt) == dt
    assert converters.as_datetime("") is None
    assert converters.as_datetime(None) is None
    assert converters.as_datetime("invalid") is None
    # With format
    assert converters.as_datetime("20/05/2023 15:30", fmt="%d/%m/%Y %H:%M") == datetime.datetime(2023, 5, 20, 15, 30)

def test_as_bool_various_cases():
    true_vals = ['S', 'SIM', 'TRUE', '1', 'T', 'Y', 'YES', 'VERDADEIRO', ' s ', ' Sim ']
    false_vals = ['N', 'NAO', 'NÃO', 'FALSE', '0', 'F', 'NO', 'FALSO', ' n ', ' nao ']
    for val in true_vals:
        assert converters.as_bool(val) is True
    for val in false_vals:
        assert converters.as_bool(val) is False
    assert converters.as_bool('maybe') is None
    assert converters.as_bool('') is None
    assert converters.as_bool(None) is None
    assert converters.as_bool(float('nan')) is None

def test_clean_cnpj_valid_and_invalid():
    assert converters.clean_cnpj("12.345.678/0001-95") == "12345678000195"
    assert converters.clean_cnpj("12345678000195") == "12345678000195"
    assert converters.clean_cnpj("12.345.678/0001-9") is None
    assert converters.clean_cnpj("abc") is None
    assert converters.clean_cnpj("") is None
    assert converters.clean_cnpj(None) is None
    assert converters.clean_cnpj(float('nan')) is None

def test_as_string_id_behavior():
    assert converters.as_string_id("12.345.678/0001-95") == "12345678000195"
    assert converters.as_string_id("12345678000195") == "12345678000195"
    assert converters.as_string_id("") is None
    assert converters.as_string_id(None) is None
    assert converters.as_string_id(float('nan')) is None

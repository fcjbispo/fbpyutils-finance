import pandas as pd
import pytest

from fbpyutils_finance.cvm import processing

def test_get_expression_and_converters_basic():
    mappings = [
        {'Target_Field': 'field1', 'Source_Field': 'col1', 'Transformation1': None, 'Transformation2': None, 'Transformation3': None, 'Converter': 'as_int'},
        {'Target_Field': 'field2', 'Source_Field': 'col2', 'Transformation1': 'UPPER($X)', 'Transformation2': None, 'Transformation3': None, 'Converter': 'as_str'},
        {'Target_Field': 'field3', 'Source_Field': None, 'Transformation1': None, 'Transformation2': None, 'Transformation3': None, 'Converter': None}
    ]
    exprs, convs = processing.get_expression_and_converters(mappings)
    assert isinstance(exprs, list)
    assert isinstance(convs, dict)
    assert 'field1' in convs
    assert 'field2' in convs
    assert 'field3' in convs

def test_apply_expressions_and_converters():
    df = pd.DataFrame({'col1': ['123', '456'], 'col2': ['abc', 'def']})
    mappings = [
        {'Target_Field': 'field1', 'Source_Field': 'col1', 'Transformation1': None, 'Transformation2': None, 'Transformation3': None, 'Converter': 'as_int'},
        {'Target_Field': 'field2', 'Source_Field': 'col2', 'Transformation1': 'UPPER($X)', 'Transformation2': None, 'Transformation3': None, 'Converter': 'as_str'}
    ]
    exprs, convs = processing.get_expression_and_converters(mappings)
    df_expr = processing.apply_expressions(df, exprs)
    assert 'field1' in df_expr.columns
    assert 'field2' in df_expr.columns
    df_conv = processing.apply_converters(df_expr, convs)
    assert df_conv['field1'].iloc[0] == 123
    assert df_conv['field2'].iloc[0] == 'ABC'

def test_apply_expressions_empty():
    df = pd.DataFrame()
    exprs = ['NULL AS test']
    result = processing.apply_expressions(df, exprs)
    assert isinstance(result, pd.DataFrame)
    assert 'test' in result.columns

def test_apply_converters_empty():
    df = pd.DataFrame()
    convs = {'field': lambda x: x}
    result = processing.apply_converters(df, convs)
    assert isinstance(result, pd.DataFrame)

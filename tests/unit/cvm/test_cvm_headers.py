import os
import tempfile
import pandas as pd
import pytest

from fbpyutils_finance.cvm import headers

def test_get_cvm_file_metadata_reads_header(tmp_path):
    file_path = tmp_path / "if_register.cad_fi.csv"
    file_path.write_text("col1;col2;col3\n1;2;3", encoding="utf-8")
    kind, sub_kind, header_line, header_hash = headers.get_cvm_file_metadata(str(file_path))
    assert kind
    assert sub_kind
    assert header_line.startswith("col1")
    assert isinstance(header_hash, str)

def test_get_cvm_updated_headers_empty_inputs():
    df_map = pd.DataFrame([{
        'Kind': 'KIND',
        'Order': 1,
        'Target_Field': 'field',
        'Source_Field': 'col',
        'Transformation1': None,
        'Transformation2': None,
        'Transformation3': None,
        'Converter': None
    }])
    current_df = pd.DataFrame()
    result = headers.get_cvm_updated_headers([], df_map, current_df)
    assert isinstance(result, list)

def test_check_cvm_headers_changed_empty():
    df = pd.DataFrame()
    result = headers.check_cvm_headers_changed([], df)
    assert isinstance(result, set)
    assert len(result) == 0

def test_write_cvm_headers_mappings(tmp_path):
    mappings = [
        {'Hash': 'hash1', 'Kind': 'KIND', 'Sub_Kind': 'SUB', 'Order': 1, 'Target_Field': 'field',
         'Source_Field': 'col', 'Transformation1': None, 'Transformation2': None, 'Transformation3': None,
         'Converter': None, 'Is_New': True, 'Header': 'col1;col2'}
    ]
    file_path = tmp_path / "headers.xlsx"
    success = headers.write_cvm_headers_mappings(mappings, str(file_path))
    assert success
    assert os.path.exists(file_path)

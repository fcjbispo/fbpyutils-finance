import os
import tempfile
import pandas as pd
import pytest

from unittest import mock

import fbpyutils_finance.cvm.file_io as file_io

@pytest.fixture
def headers_df():
    return pd.DataFrame([
        {'Hash': 'dummyhash', 'Target_Field': 'field1', 'Source_Field': 'col1'}
    ])

@pytest.fixture
def dummy_csv_file(tmp_path):
    file_path = tmp_path / "dummy.csv"
    file_path.write_text("col1;col2\n123;abc\n456;def", encoding="utf-8")
    return str(file_path)

def test_build_target_file_name_basic():
    meta = {'kind': 'IF_REGISTER', 'href': 'file.csv'}
    path = file_io.build_target_file_name(meta, "/tmp")
    assert path.endswith("if_register.file.csv")

def test_write_target_file_and_read(tmp_path):
    meta = {'kind': 'IF_REGISTER', 'href': 'file.csv'}
    data = "some;csv;data"
    path = file_io.write_target_file(data, meta, str(tmp_path))
    assert os.path.exists(path)
    with open(path, encoding='utf-8') as f:
        content = f.read()
    assert content == data

def test_read_cvm_history_file_success(tmp_path, headers_df, monkeypatch):
    # Prepare dummy CSV file
    csv_path = tmp_path / "if_register.cad_fi.csv"
    csv_path.write_text("col1;col2\n123;abc\n456;def", encoding="utf-8")

    # Patch dependencies
    # Mock the function where it's actually used in file_io
    monkeypatch.setattr(file_io, "get_expression_and_converters", lambda mappings: (["\"col1\" AS col1"], {'col1': lambda x: x}))
    monkeypatch.setattr(file_io, "check_cvm_headers_changed", lambda files, df: [])
    monkeypatch.setattr(file_io, "get_cvm_file_metadata", lambda f: ("KIND", "SUBKIND", "col1;col2", "dummyhash"))
    # Patch get_expression_and_converters in processing module (where it's defined)
    # monkeypatch.setattr(file_io, "get_expression_and_converters", lambda mappings: (["\"col1\" AS col1"], {'col1': lambda x: x})) # Already done via processing_mod mock
    monkeypatch.setattr(pd, "read_csv", lambda *args, **kwargs: pd.DataFrame({'col1': ['123', '456'], 'col2': ['abc', 'def']}))

    # Update headers_df to include dummyhash
    headers_df.loc[0, 'Hash'] = 'dummyhash'

    # No need to wrap the function, the mock on processing_mod should suffice
    kind, sub_kind, df, parts = file_io.read_cvm_history_file(str(csv_path), headers_df, apply_conversions=True, check_header=True)
    assert kind == "KIND"
    assert sub_kind == "SUBKIND"
    assert isinstance(df, pd.DataFrame)
    assert 'col1' in df.columns
    assert isinstance(parts, list)

def test_read_cvm_history_file_file_not_found(headers_df):
    with pytest.raises(ValueError) as excinfo:
        file_io.read_cvm_history_file("nonexistent.csv", headers_df)
    assert "Source file not found" in str(excinfo.value)

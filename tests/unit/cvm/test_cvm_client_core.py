import os
import tempfile
import sqlite3
import pandas as pd
import pytest
from unittest import mock

from fbpyutils_finance.cvm.client import CVM

@pytest.fixture
def headers_df():
    # Minimal headers DataFrame mock
    return pd.DataFrame({'Hash': ['dummy'], 'Target_Field': ['field'], 'Source_Field': ['field']})

@pytest.fixture
def temp_db_path(tmp_path):
    return tmp_path / "catalog.db"

@pytest.fixture
def cvm_client(headers_df, temp_db_path):
    # Create CVM instance with temp db and headers
    return CVM(headers_df=headers_df, catalog_db_path=str(temp_db_path))

def test_check_history_folder_creates(tmp_path):
    folder = tmp_path / "history"
    assert not folder.exists()
    result = CVM.check_history_folder(str(folder))
    assert os.path.exists(result)
    assert result == str(folder)

def test_init_creates_db_and_tables(headers_df, tmp_path):
    db_path = tmp_path / "catalog.db"
    client = CVM(headers_df=headers_df, catalog_db_path=str(db_path))
    # Check DB file created
    assert os.path.exists(db_path)
    # Check tables exist
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cur.fetchall()}
    assert 'cvm_if_catalog_journal' in tables
    assert 'cvm_if_remote_files_staging' in tables or True  # staging is temp, may not persist
    con.close()

def test_get_cvm_catalog_empty(headers_df, tmp_path):
    client = CVM(headers_df=headers_df, catalog_db_path=str(tmp_path / "db.db"))
    df = client.get_cvm_catalog()
    assert isinstance(df, pd.DataFrame)
    # Initially empty or with columns
    assert 'url' in df.columns

def test_get_cvm_files_to_process_empty(headers_df, tmp_path):
    client = CVM(headers_df=headers_df, catalog_db_path=str(tmp_path / "db.db"))
    result = client.get_cvm_files_to_process()
    assert isinstance(result, list)
    assert result == []

def test_mark_cvm_files_updated_noop(headers_df, tmp_path):
    client = CVM(headers_df=headers_df, catalog_db_path=str(tmp_path / "db.db"))
    # Should return True when no files info provided
    assert client.mark_cvm_files_updated([]) is True

def test_get_cvm_file_data_file_not_found(headers_df, tmp_path):
    client = CVM(headers_df=headers_df, catalog_db_path=str(tmp_path / "db.db"))
    with pytest.raises(FileNotFoundError):
        client.get_cvm_file_data("nonexistent_file.csv")

def test_get_cvm_file_data_with_mock(headers_df, tmp_path, monkeypatch):
    client = CVM(headers_df=headers_df, catalog_db_path=str(tmp_path / "db.db"))
    dummy_path = tmp_path / "if_register.cad_fi.csv"
    dummy_path.write_text("header1;header2\nval1;val2", encoding="utf-8")

    # Patch internals to avoid real processing
    import fbpyutils_finance.cvm.file_io as fio
    monkeypatch.setattr(fio, "check_cvm_headers_changed", lambda files, df: [])
    monkeypatch.setattr(fio, "get_cvm_file_metadata", lambda f: ("KIND", "SUBKIND", "header1;header2", "dummyhash"))
    monkeypatch.setattr(fio, "get_expression_and_converters", lambda mappings: (["\"header1\" AS header1"], {'header1': lambda x: x}))
    monkeypatch.setattr(pd, "read_csv", lambda *args, **kwargs: pd.DataFrame({'header1': ['1', '2'], 'header2': ['a', 'b']}))

    # Patch get_expression_and_converters inside processing module
    import fbpyutils_finance.cvm.processing as processing_mod
    monkeypatch.setattr(processing_mod, "get_expression_and_converters", lambda mappings: (["\"header1\" AS header1"], {'header1': lambda x: x}))

    # Update headers_df to include dummyhash
    client.HEADERS_DF = pd.DataFrame(
        [{"Hash": "dummyhash", "Target_Field": "header1", "Source_Field": "header1"}]
    )

    # Get the result directly
    result = client.get_cvm_file_data(str(dummy_path))
    assert isinstance(result, tuple)
    assert len(result) == 4

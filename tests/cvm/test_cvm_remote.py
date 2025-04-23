import io
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

import fbpyutils_finance.cvm.remote as remote

def test_get_url_paths_parses_html(monkeypatch):
    html = """
    <html><body><pre>
    <a href="file1.csv">file1.csv</a> 01-Jan-2024 12:00 1K
    <a href="file2.zip">file2.zip</a> 02-Feb-2024 13:30 2M
    </pre></body></html>
    """
    class FakeResponse:
        def __init__(self, text):
            self.text = text
            self.status_code = 200
        def raise_for_status(self): pass

    monkeypatch.setattr("requests.get", lambda *args, **kwargs: FakeResponse(html))
    df = remote.get_url_paths("http://fakeurl")
    assert isinstance(df, pd.DataFrame)
    assert 'href' in df.columns
    assert len(df) == 2

def test_get_remote_files_list_merges(monkeypatch):
    # Patch get_url_paths to return dummy dataframes
    df_current = pd.DataFrame({'sequence':[0], 'href':['file.csv'], 'name':['file'], 'last_modified':['2024-01-01 12:00:00'], 'size':[123], 'history':[False], 'url_base':['http://current']})
    df_history = pd.DataFrame({'sequence':[1], 'href':['file2.csv'], 'name':['file2'], 'last_modified':['2023-01-01 12:00:00'], 'size':[456], 'history':[True], 'url_base':['http://history']})
    monkeypatch.setattr(remote, "get_url_paths", lambda url: df_current if 'DADOS' in url else df_history)
    result = remote.get_remote_files_list('KIND', 'http://current', 'http://history')
    assert isinstance(result, pd.DataFrame)
    assert 'url' in result.columns

def test_update_cvm_history_file_missing_url():
    meta = {'last_modified': '2024-01-01 12:00:00', 'history_folder': '/tmp'}
    result = remote.update_cvm_history_file(meta)
    assert result[0][0] == 'ERROR'

def test_update_cvm_history_file_missing_last_modified():
    meta = {'url': 'http://fake', 'history_folder': '/tmp'}
    result = remote.update_cvm_history_file(meta)
    assert result[0][0] == 'SKIP'

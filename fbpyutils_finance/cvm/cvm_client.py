import os"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

import sqlite3"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

import pandas as pd"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

from datetime import datetime"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

from typing import Optional, List, Dict, Tuple, Any"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# Import necessary components from the project structure"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

import fbpyutils_finance as FI"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

import fbpyutils.file as FU"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

from fbpyutils.debug import debug_info"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# Import functions from the new submodules within the cvm package"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

from .remote import get_remote_files_list, update_cvm_history_file"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

from .file_io import read_cvm_history_file"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# headers.py functions are usually used *before* initializing CVM or passed in,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# but check_cvm_headers_changed might be useful internally if needed."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# --- Constantes Globais (Podem ser movidas para um config.py se crescerem) ---"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# Defined here for clarity, but could be imported from __init__ or config"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

URL_IF_REGISTER = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

URL_IF_REGISTER_HIST = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS/HIST""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

URL_IF_DAILY = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

URL_IF_DAILY_HIST = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

# --- Classe Principal CVM ---"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

class CVM:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    Client class for interacting with CVM (Comissão de Valores Mobiliários) data."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    Provides methods to update a local catalog of CVM files, download new/updated files,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    and retrieve processed data from downloaded files."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    Requires pre-loaded header mappings (headers_df) during initialization."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    CATALOG_JOURNAL_TABLE = "cvm_if_catalog_journal""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    REMOTE_FILES_TABLE = "cvm_if_remote_files_staging"  # Use staging suffix"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    @staticmethod"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def check_history_folder(history_folder: Optional[str] = None) -> str:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Checks if the history folder exists and creates it if it doesn't."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Args:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            history_folder (Optional[str], optional): The path to the history folder."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                If None, defaults to a subfolder 'history' within USER_CVM_DIR."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                Defaults to None."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Returns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            str: The validated or created history folder path."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Raises:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            OSError: If the folder cannot be created."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        # Use FI.USER_CVM_DIR defined in fbpyutils_finance"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        history_folder = history_folder or os.path.join(FI.USER_CVM_DIR, "history")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not os.path.exists(history_folder):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                os.makedirs("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    history_folder, exist_ok=True"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )  # exist_ok=True avoids error if dir exists"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print(f"Ensured history folder exists: {history_folder}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            except OSError as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print(f"Error creating history folder {history_folder}: {e}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                raise  # Re-raise error if folder creation fails"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        return history_folder"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def __init__("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        headers_df: pd.DataFrame,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        catalog_db_path: Optional[str] = None,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        history_folder: Optional[str] = None,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    ):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Initializes the CVM client."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Args:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            headers_df (pd.DataFrame): Pre-loaded DataFrame containing header mappings. Must not be None or empty."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            catalog_db_path (Optional[str], optional): Path to the SQLite database file for the catalog."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                If None, defaults to 'catalog.db' within USER_CVM_DIR. Defaults to None."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            history_folder (Optional[str], optional): Path to the folder for storing downloaded CVM files."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                If None, uses the default from check_history_folder. Defaults to None."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Raises:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ValueError: If the headers_df is None or empty."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ConnectionError: If the database connection fails."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if headers_df is None or headers_df.empty:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ValueError("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                "headers_df (DataFrame with header mappings) must be provided and cannot be empty during CVM client initialization.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self.HEADERS_DF = headers_df  # Store the pre-loaded headers DataFrame"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        db_path_base = catalog_db_path or os.path.join(FI.USER_CVM_DIR, "catalog.db")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        # Ensure the directory for the database exists"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        os.makedirs(os.path.dirname(db_path_base), exist_ok=True)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self.catalog_db_path = db_path_base"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG = sqlite3.connect(self.catalog_db_path)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Enable Write-Ahead Logging for better concurrency, if appropriate"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # self.CATALOG.execute("PRAGMA journal_mode=WAL;")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print(f"Connected to catalog database: {self.catalog_db_path}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        except sqlite3.Error as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"FATAL: Failed to connect to catalog database at {self.catalog_db_path}: {e}""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ConnectionError(f"Could not connect to database: {e}") from e"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self.HISTORY_FOLDER = CVM.check_history_folder(history_folder)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        print(f"Using history folder: {self.HISTORY_FOLDER}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        # Initialize tables if they don't exist"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self._initialize_catalog_tables()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def _initialize_catalog_tables(self):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """Creates the necessary tables in the catalog database if they don't exist.""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("Error: Cannot initialize tables, database connection is not valid.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor = self.CATALOG.cursor()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Create journal table - use TEXT for dates for simplicity with SQLite"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute(f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            CREATE TABLE IF NOT EXISTS {self.CATALOG_JOURNAL_TABLE} ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                sequence INTEGER,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                href TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                name TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                last_modified TEXT, -- Store as ISO format string (YYYY-MM-DD HH:MM:SS)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                size INTEGER,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                history INTEGER, -- Store boolean as INTEGER (0 or 1)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                url TEXT PRIMARY KEY NOT NULL, -- URL should be unique identifier"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                kind TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                last_download TEXT, -- Store as ISO format string"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                last_updated TEXT,  -- Store as ISO format string"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                process INTEGER DEFAULT 1, -- Boolean as INTEGER"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                active INTEGER DEFAULT 1   -- Boolean as INTEGER"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            );"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            """)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Create index for faster lookups"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"CREATE INDEX IF NOT EXISTS idx_journal_kind_name ON {self.CATALOG_JOURNAL_TABLE} (kind, name);""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"CREATE INDEX IF NOT EXISTS idx_journal_process_active ON {self.CATALOG_JOURNAL_TABLE} (process, active);""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"CREATE INDEX IF NOT EXISTS idx_journal_url ON {self.CATALOG_JOURNAL_TABLE} (url);""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )  # Index on PK"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Create remote files staging table (used temporarily during update)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute(f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            CREATE TABLE IF NOT EXISTS {self.REMOTE_FILES_TABLE} ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                sequence INTEGER,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                href TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                name TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                last_modified TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                size INTEGER,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                history INTEGER,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                url TEXT,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                kind TEXT"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            );"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            """)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("Catalog tables initialized successfully.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        except sqlite3.Error as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print(f"Error initializing catalog tables: {e}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.rollback()  # Rollback changes on error"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Decide if this should be fatal - probably yes"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise RuntimeError(f"Failed to initialize database tables: {e}") from e"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def __del__(self):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """Closes the database connection upon object destruction.""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if hasattr(self, "CATALOG") and self.CATALOG:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Optional: Commit any final changes? Usually done explicitly."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                self.CATALOG.close()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print(f"Closed catalog database connection: {self.catalog_db_path}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            except sqlite3.Error as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Avoid raising errors in __del__"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print(f"Error closing catalog database during object deletion: {e}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self.CATALOG = None"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def get_cvm_catalog(self) -> Optional[pd.DataFrame]:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Retrieves the current CVM catalog journal from the database."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Returns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            Optional[pd.DataFrame]: DataFrame containing the catalog data, or None if the table"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                    doesn't exist or an error occurs. Converts integer booleans back."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("Error: Catalog database connection is not valid.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return None"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Check if table exists first"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor = self.CATALOG.cursor()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                "SELECT name FROM sqlite_master WHERE type='table' AND name=?;","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                (self.CATALOG_JOURNAL_TABLE,),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if cursor.fetchone() is None:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print(f"Catalog table '{self.CATALOG_JOURNAL_TABLE}' does not exist.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Return empty DataFrame with expected columns?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Define expected columns based on _initialize_catalog_tables"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                cols = ["""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "sequence","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "href","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "name","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "last_modified","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "size","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "history","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "url","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "kind","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "last_download","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "last_updated","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "process","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "active","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                ]"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                return pd.DataFrame(columns=cols)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            df = pd.read_sql("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"SELECT * FROM {self.CATALOG_JOURNAL_TABLE}", con=self.CATALOG"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Convert integer columns back to boolean if needed for consistency elsewhere"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            for col in ["history", "process", "active"]:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if col in df.columns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    df[col] = df[col].astype(bool)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return df"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        except (sqlite3.Error, pd.io.sql.DatabaseError) as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print(f"Error retrieving CVM catalog: {e}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return None"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def update_cvm_catalog("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Tuple[str, int]]]:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Updates the local CVM catalog by comparing against remote file listings and downloading changes."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        1. Fetches current and historical file lists from CVM URLs."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        2. Compares with the local catalog journal using SQL merge logic."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        3. Identifies new, updated, or removed files and updates 'active'/'process' flags."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        4. Downloads files marked for processing."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        5. Updates 'last_download' and 'process' flags for processed files."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Returns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Tuple[str, int]]]: A tuple containing:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - update_summary (List[Dict]): Summary of download results (errors, successes per URL)."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - processed_metadata (List[Dict]): List of metadata dictionaries for files attempted/processed."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - db_operations (List[Tuple[str, int]]): List of SQL update operations performed and rows affected."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        step = "SETTING UP COMPONENTS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        update_summary = []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        processed_metadata = []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        db_ops = []  # Store (sql_template, row_count)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ConnectionError("Catalog database connection is not valid.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "FETCHING REMOTE FILE LISTS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if_remote_files = pd.concat("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                ["""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    get_remote_files_list("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        "IF_REGISTER", URL_IF_REGISTER, URL_IF_REGISTER_HIST"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    ),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    get_remote_files_list("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        "IF_POSITION", URL_IF_DAILY, URL_IF_DAILY_HIST"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    ),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                ],"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                ignore_index=True,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if if_remote_files.empty:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "Warning: No remote files found or fetched. Catalog update skipped.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                return [], [], []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Convert boolean 'history' to integer for SQLite compatibility"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if "history" in if_remote_files.columns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if_remote_files["history"] = if_remote_files["history"].astype(int)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Store remote files temporarily for comparison (overwrite existing)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if_remote_files.to_sql("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                self.REMOTE_FILES_TABLE,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                con=self.CATALOG,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if_exists="replace","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                index=False,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"Stored {len(if_remote_files)} remote file entries in staging table.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "UPDATING CATALOG JOURNAL (MERGE LOGIC)""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor = self.CATALOG.cursor()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # 1. Deactivate entries in journal not present remotely anymore"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            deactivate_sql = f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                UPDATE {self.CATALOG_JOURNAL_TABLE}"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                SET active = 0, process = 0"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                WHERE active = 1 AND url NOT IN (SELECT url FROM {self.REMOTE_FILES_TABLE});"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute(deactivate_sql)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            deactivated_count = cursor.rowcount"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if deactivated_count > 0:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    f"Deactivated {deactivated_count} entries in catalog no longer present remotely.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                db_ops.append((deactivate_sql, deactivated_count))"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # 2. Insert new entries from remote list or update existing ones"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Using INSERT OR REPLACE based on URL primary key simplifies the merge"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Need to handle date comparison carefully in SQLite (use ISO strings)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            merge_sql = f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                INSERT OR REPLACE INTO {self.CATALOG_JOURNAL_TABLE} ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    sequence, href, name, last_modified, size, history, url, kind,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    last_download, last_updated, process, active"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                SELECT"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    r.sequence, r.href, r.name, r.last_modified, r.size, r.history, r.url, r.kind,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    -- Keep existing download/update times if replacing"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    COALESCE(j.last_download, NULL),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    COALESCE(j.last_updated, NULL),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    -- Determine if processing is needed (compare ISO strings)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    CASE"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        WHEN r.last_modified IS NULL THEN 0 -- Cannot compare if remote date missing"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        WHEN j.last_download IS NULL THEN 1 -- Never downloaded"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        WHEN r.last_modified > j.last_download THEN 1 -- Remote is newer (string comparison works for ISO format)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        ELSE 0 -- Already downloaded and up-to-date"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    END,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    1 -- Mark as active"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                FROM {self.REMOTE_FILES_TABLE} r"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                LEFT JOIN {self.CATALOG_JOURNAL_TABLE} j ON r.url = j.url;"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute(merge_sql)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            merged_count = ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                cursor.rowcount"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )  # Note: INSERT OR REPLACE counts affected rows"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"Merged/Updated catalog journal based on remote files (affected rows: {merged_count}).""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # This count isn't super informative for INSERT OR REPLACE, skip adding to db_ops for now"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.commit()  # Commit merge changes"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "IDENTIFYING FILES TO DOWNLOAD""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            files_to_process_df = pd.read_sql("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                SELECT * FROM {self.CATALOG_JOURNAL_TABLE}"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                WHERE process = 1 AND active = 1"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ""","""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                con=self.CATALOG,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Convert integer booleans back for metadata dict"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            for col in ["history", "process", "active"]:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if col in files_to_process_df.columns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    files_to_process_df[col] = files_to_process_df[col].astype(bool)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            metadata_to_process = files_to_process_df.to_dict(orient="records")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if not metadata_to_process:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("Catalog is up-to-date. No files need downloading.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Clean up staging table"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                return [], [], db_ops"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print(f"Found {len(metadata_to_process)} files needing download/update.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "DOWNLOADING AND PROCESSING FILES""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            all_results = []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Consider parallel processing here if beneficial and safe (beware of DB writes)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # For simplicity, processing sequentially first"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            for meta in metadata_to_process:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                meta["history_folder"] = ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    self.HISTORY_FOLDER"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )  # Ensure history folder is in metadata"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Call the download function (from remote.py)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                download_results = update_cvm_history_file(meta)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                all_results.extend("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    download_results"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )  # Collect results from download attempts"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                processed_metadata.append(meta)  # Track which metadata was processed"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "CONSOLIDATING DOWNLOAD RESULTS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if not all_results:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("No download results generated.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Clean up staging table"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                return [], processed_metadata, db_ops  # Return empty summary"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Create DataFrame from results for easier aggregation"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result_cols = ["status", "metadata", "message"]"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result_data = pd.DataFrame(all_results, columns=result_cols)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Extract key info from metadata for summary"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result_data["name"] = result_data["metadata"].apply(lambda x: x.get("name"))"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result_data["kind"] = result_data["metadata"].apply(lambda x: x.get("kind"))"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result_data["url"] = result_data["metadata"].apply(lambda x: x.get("url"))"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Get the last_download time recorded *during* the successful download"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result_data["actual_last_download"] = result_data.apply("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                lambda row: row["metadata"].get("last_download")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if row["status"] == "SUCCESS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                else None,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                axis=1,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Generate summary (errors, successes per original URL)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            summary = ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                result_data.groupby("url")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                .agg("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    name=("name", "first"),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    kind=("kind", "first"),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    errors=("status", lambda x: (x == "ERROR").sum()),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    successes=("status", lambda x: (x == "SUCCESS").sum()),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    # Get the first successful download time for this URL group"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    successful_download_time=("actual_last_download", "first"),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                .reset_index()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            update_summary = summary.to_dict(orient="records")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "UPDATING CATALOG JOURNAL WITH DOWNLOAD STATUS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            successful_updates = []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            for record in summary.to_dict("records"):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if record["errors"] == 0 and record["successes"] > 0:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    # Use the actual download time if available, else current time as fallback"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    dl_time = record["""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        "successful_download_time""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    ] or datetime.now().strftime("%Y-%m-%d %H:%M:%S")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    successful_updates.append("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        (dl_time, 0, record["url"])"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    )  # (last_download, process=0, url)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if successful_updates:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                update_sql = f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                     UPDATE {self.CATALOG_JOURNAL_TABLE}"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                     SET last_download = ?,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                         process = ?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                     WHERE url = ? AND process = 1 AND active = 1;"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                 """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                cursor.executemany(update_sql, successful_updates)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                updated_count = cursor.rowcount"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    f"Updated download status for {updated_count} successfully processed files in catalog.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                db_ops.append("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    (update_sql + " (batch)", updated_count)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )  # Record operation (template)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.commit()  # Commit final status updates"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Clean up staging table"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return update_summary, processed_metadata, db_ops"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        except Exception as E:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            info = debug_info(E)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                self.CATALOG.rollback()  # Rollback any uncommitted changes on error"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ValueError("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"Failed to update CVM catalog at step {step}: {E} ({info})""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        finally:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Ensure staging table is dropped even if errors occurred mid-process"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                if FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    cursor = self.CATALOG.cursor()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            except sqlite3.Error as drop_err:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    f"Warning: Failed to drop staging table {self.REMOTE_FILES_TABLE}: {drop_err}""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Ensure main connection is still valid after potential errors"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if not FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("Warning: Catalog DB connection became invalid during update.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def get_cvm_files_to_process("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self, kind: Optional[str] = None, history: Optional[bool] = None"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    ) -> List[Tuple[str, str, bool, Tuple[str, ...]]]:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Retrieves a list of CVM file groups from the catalog that need data processing."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Files are selected if they are active and their last_updated timestamp is null"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        or older than their last_download timestamp. It then finds the corresponding"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        downloaded files in the history folder."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Args:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            kind (Optional[str], optional): Filter by data kind (e.g., 'IF_POSITION'). Defaults to None (all kinds)."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            history (Optional[bool], optional): Filter by history flag. Defaults to None (both)."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Returns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            List[Tuple[str, str, bool, Tuple[str, ...]]]: A list of tuples. Each tuple contains:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - kind (str): The kind of CVM file group."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - name (str): The base name of the CVM file group (e.g., 'inf_diario_fi_202312')."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - history (bool): Flag indicating if the file group is historical."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                - files (Tuple[str, ...]): A tuple of full paths to the actual downloaded file(s)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                           in the history folder corresponding to this group."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Raises:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ValueError: If fetching from the catalog fails."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ConnectionError: If the database connection is invalid."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        step = "QUERYING CATALOG FOR FILES TO PROCESS""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ConnectionError("Catalog database connection is not valid.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Compare ISO date strings directly"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            query = f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                SELECT kind, name, history -- Select distinct groups"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                FROM {self.CATALOG_JOURNAL_TABLE}"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                WHERE active = 1"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                AND (last_updated IS NULL OR last_download > last_updated)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            params: List[Any] = []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if kind is not None:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                query += " AND kind = ?""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                params.append(kind)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if history is not None:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                query += " AND history = ?""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                params.append(int(history))  # Convert bool to int for query"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Ensure we only get one entry per logical file group (kind, name, history)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            query += " GROUP BY kind, name, history ORDER BY kind, name""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            files_to_process_df = pd.read_sql(query, con=self.CATALOG, params=params)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if files_to_process_df.empty:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("No CVM files found in catalog needing data processing.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                return []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            step = "FINDING ACTUAL FILES IN HISTORY FOLDER""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            result = []"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            for record in files_to_process_df.to_dict(orient="records"):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                file_kind = record["kind"]"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                file_name = record["""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    "name""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                ]  # This is the base name (e.g., inf_diario_fi_YYYYMM)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                file_history = bool(record["history"])  # Convert back to bool"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Construct search pattern based on how files are saved by write_target_file"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Pattern: kind.name.* (or more specific if needed)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Ensure case-insensitivity if OS filesystem might be case-sensitive"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                search_pattern = f"{file_kind.lower()}.{file_name.lower()}.*""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    # Use fbpyutils find function"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    found_files = FU.find(self.HISTORY_FOLDER, search_pattern)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    if found_files:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        # Sort files for consistent order (e.g., if multiple parts from zip)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        result.append("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                            ("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                file_kind,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                file_name,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                file_history,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                tuple(sorted(found_files)),"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    else:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        # This indicates an inconsistency: catalog says process, but file missing"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                            f"CRITICAL WARNING: Catalog indicates file group '{file_name}' (Kind: {file_kind}, History: {file_history}) needs processing, but no files found in {self.HISTORY_FOLDER} matching pattern '{search_pattern}'. Check download integrity or catalog status.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        # Optionally: Mark this entry as errored in the catalog?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                except Exception as find_err:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                        f"Error searching for files for group {file_name} (Kind: {file_kind}): {find_err}""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print(f"Found {len(result)} CVM file groups needing data processing.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return result"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        except (sqlite3.Error, pd.io.sql.DatabaseError) as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            info = debug_info(e)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ValueError("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"Failed to get CVM files to process from catalog at step {step}: {e} ({info})""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def get_cvm_file_data("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self, cvm_file_path: str, check_header: bool = False"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    ) -> Tuple[str, str, pd.DataFrame, List[str]]:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Reads and processes data from a single downloaded CVM file using stored header mappings."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Args:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cvm_file_path (str): The full path to the downloaded CVM file in the history folder."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            check_header (bool, optional): Verify if the file header matches known mappings before processing."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                                           Defaults to False."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Returns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            Tuple[str, str, pd.DataFrame, List[str]]: Result from file_io.read_cvm_history_file:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                (kind, sub_kind, processed_data_df, partition_columns)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Raises:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            FileNotFoundError: If the cvm_file_path does not exist."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ValueError: If header check fails or processing errors occur (propagated from read_cvm_history_file)."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not os.path.exists(cvm_file_path):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise FileNotFoundError(f"CVM file not found: {cvm_file_path}")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        # Pass the pre-loaded headers DataFrame to the reading function"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        # This assumes self.HEADERS_DF was correctly initialized"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if self.HEADERS_DF is None or self.HEADERS_DF.empty:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise RuntimeError("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                "CVM client was not properly initialized with headers_df.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        return read_cvm_history_file("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            source_file=cvm_file_path,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            headers_df=self.HEADERS_DF,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            apply_conversions=True,  # Typically want converted data"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            check_header=check_header,"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    def mark_cvm_files_updated("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        self, processed_files_info: List[Tuple[str, str]]"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

    ) -> bool:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Updates the 'last_updated' timestamp in the catalog journal for successfully processed file groups."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Args:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            processed_files_info (List[Tuple[str, str]]): A list of tuples, where each tuple"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                contains (kind, name) of the file group that was successfully processed and loaded."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Returns:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            bool: True if the update operations were successful, False otherwise."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        Raises:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ValueError: If updating the catalog fails."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ConnectionError: If the database connection is invalid."""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        step = "MARKING FILES AS UPDATED IN CATALOG""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not FI.is_valid_db_connection(self.CATALOG):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ConnectionError("Catalog database connection is not valid.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        if not processed_files_info:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("No processed files provided to mark as updated.")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return True  # Nothing to do, considered successful"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        try:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            update_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Update based on kind and name, targeting active files"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            update_sql = f""""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                UPDATE {self.CATALOG_JOURNAL_TABLE}"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                SET last_updated = ?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                WHERE active = 1"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                  AND kind = ?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                  AND name = ?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                  -- Only update if it was actually downloaded"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                  AND last_download IS NOT NULL"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                  -- Optional: Only update if last_updated was older?"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                  -- AND (last_updated IS NULL OR last_updated < ?)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            """"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Prepare data for executemany: list of (update_time_str, kind, name) tuples"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            update_data = ["""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                (update_time_str, kind, name) for kind, name in processed_files_info"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            ]"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor = self.CATALOG.cursor()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            cursor.executemany(update_sql, update_data)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            updated_count = cursor.rowcount"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.commit()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"Marked {updated_count} file groups as updated (data processed) in the catalog.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            # Check if updated_count matches len(processed_files_info) for verification"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            if updated_count != len(processed_files_info):"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # This could happen if a file group had multiple entries (e.g. from zip) but only one needs update marker"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                # Or if the WHERE clause didn't match (e.g., active=0 or last_download is NULL)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                print("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                    f"Warning: Attempted to mark {len(processed_files_info)} groups, but updated {updated_count} rows in catalog. This might be expected or indicate an issue.""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            return True"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

        except sqlite3.Error as e:"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            info = debug_info(e)"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            self.CATALOG.rollback()"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            raise ValueError("""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

                f"Failed to mark CVM files as updated in catalog at step {step}: {e} ({info})""""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""

            )"""
CVM client module.

Provides a :class:`CVM` class that manages a local history of CVM files and a SQLite catalog
of available data.

Typical usage example
---------------------
>>> from fbpyutils_finance.cvm import CVM
>>> from fbpyutils_finance.cvm import HEADERS, HEADER_MAPPINGS
>>> client = CVM(HEADERS)
>>> df = client.get_cvm_catalog()
>>> df.head()

The class handles creating the history directory, initializing required database tables and
providing convenient accessors for the catalog.

All public methods contain VIBE‑CODE ready docstrings with examples.
"""


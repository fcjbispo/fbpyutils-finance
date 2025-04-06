'''
Data Providers: CVM Update Package
Provides updating data modules, functions and classes for CVM (Comissão de Valores Mobiliários) provider.

This package facilitates fetching, processing, and managing CVM public data,
such as fund registration (CAD_FI) and daily position information (DIARIO_FI).

Main entry point is the CVM class.
'''

import os
import pandas as pd
# Import base finance package for constants like APP_FOLDER, USER_APP_FOLDER
import fbpyutils_finance as FI

# --- Configuration / Constants ---

# URLs for CVM data portals
URL_IF_REGISTER = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS"
URL_IF_REGISTER_HIST = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS/HIST"
URL_IF_DAILY = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS"
URL_IF_DAILY_HIST = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST"

# Encodings
SOURCE_ENCODING = 'iso-8859-1' # Typical encoding for CVM files
TARGET_ENCODING = 'utf-8'     # Target encoding for processing and storage

# --- Header Mapping Files ---
# These files define how raw CVM file columns map to standardized target fields
# and specify necessary transformations and type conversions.
# It's crucial these files exist and are correctly maintained.

# Path to the Excel file containing the consolidated header definitions across different CVM file versions/layouts.
# Uses FI.APP_FOLDER which should be defined in fbpyutils_finance package
HEADERS_FILE = os.path.join(FI.APP_FOLDER, 'cvm', 'data', 'if_headers_v4.xlsx')
# Path to the Excel file containing the base mapping templates (used to generate HEADERS_FILE).
HEADER_MAPPINGS_FILE = os.path.join(FI.APP_FOLDER, 'cvm', 'data', 'if_header_mappings.xlsx')

# --- Load Header Data ---
# Load header definitions and mappings into pandas DataFrames upon package import.
# This makes them readily available to the CVM client and processing functions.

HEADERS = None
HEADER_MAPPINGS = None
_initialization_error = None

try:
    if not os.path.exists(HEADERS_FILE):
        _initialization_error = FileNotFoundError(f"CVM Headers File not found at: {HEADERS_FILE}")
    else:
        HEADERS = pd.read_excel(HEADERS_FILE, sheet_name='IF_HEADERS')

    if not os.path.exists(HEADER_MAPPINGS_FILE):
         # Allow HEADER_MAPPINGS to be missing if only running updates? No, needed for header checks.
        _initialization_error = FileNotFoundError(f"CVM Header Mappings File not found at: {HEADER_MAPPINGS_FILE}")
    else:
        HEADER_MAPPINGS = pd.read_excel(HEADER_MAPPINGS_FILE, sheet_name='IF_HEADERS')

except Exception as e:
    _initialization_error = RuntimeError(f"Failed to load CVM header files: {e}")

# Raise error after trying to load both, providing a clear message
if _initialization_error:
    print(f"FATAL: Failed to initialize fbpyutils_finance.cvm package: {_initialization_error}")
    raise _initialization_error


# --- Public Interface ---
# Import the main class and potentially other core functions/classes from submodules
# to make them accessible directly via `from fbpyutils_finance import cvm`

# Main client class
from .cvm_client import CVM

# Header management functions
from .headers import get_cvm_updated_headers, check_cvm_headers_changed, write_cvm_headers_mappings, get_cvm_file_metadata

# File I/O and processing (expose if needed externally)
from .file_io import read_cvm_history_file
from .processing import apply_expressions, apply_converters, get_expression_and_converters

# Expose the converters module itself
from . import converters
# Expose utility functions if they are intended for public use
from .utils import * # Or list specific utils: is_nan_or_empty, make_datetime, etc.

# Define __all__ to control `from fbpyutils_finance.cvm import *` behavior
# Include only the intended public API elements
__all__ = [
    # Core Class
    'CVM',

    # Loaded DataFrames (read-only access recommended)
    'HEADERS',
    'HEADER_MAPPINGS',

    # Header Management
    'get_cvm_updated_headers',
    'check_cvm_headers_changed',
    'write_cvm_headers_mappings',
    'get_cvm_file_metadata', # Useful for external analysis

    # Processing/IO (Expose cautiously)
    'read_cvm_history_file',
    # 'apply_expressions', # Maybe too internal?
    # 'apply_converters', # Maybe too internal?
    # 'get_expression_and_converters', # Maybe too internal?

    # Converters Module
    'converters',

    # Utility functions (if any are public)
    'is_nan_or_empty', # Example public utility
    # Add other public utils from .utils if needed

    # Constants
    'URL_IF_REGISTER',
    'URL_IF_REGISTER_HIST',
    'URL_IF_DAILY',
    'URL_IF_DAILY_HIST',
    'SOURCE_ENCODING',
    'TARGET_ENCODING',
    'HEADERS_FILE', # Expose paths
    'HEADER_MAPPINGS_FILE',
]

print("fbpyutils_finance.cvm package initialized successfully.")

# Cleanup temporary variable
del _initialization_error

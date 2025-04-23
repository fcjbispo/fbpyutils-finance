## Usage / Core Functions

This section details the core utility and calculation functions available directly under `fbpyutils_finance`.

### Interest Rate Conversions

These functions convert interest rates between daily, monthly, and annual periods, assuming compound interest and standard day counts (30 days/month, 360 days/year).

*   **`rate_daily_to_monthly(rate: float) -> float`**
    *   Converts a daily interest rate to its equivalent monthly rate.
    *   Formula: `(1 + daily_rate) ** 30 - 1`
*   **`rate_monthly_to_daily(rate: float) -> float`**
    *   Converts a monthly interest rate to its equivalent daily rate.
    *   Formula: `(1 + monthly_rate) ** (1 / 30) - 1`
*   **`rate_monthly_to_annual(rate: float) -> float`**
    *   Converts a monthly interest rate to its equivalent annual rate.
    *   Formula: `(1 + monthly_rate) ** 12 - 1`
*   **`rate_annual_to_monthly(rate: float) -> float`**
    *   Converts an annual interest rate to its equivalent monthly rate.
    *   Formula: `(1 + annual_rate) ** (1 / 12) - 1`
*   **`rate_annual_to_daily(rate: float) -> float`**
    *   Converts an annual interest rate to its equivalent daily rate.
    *   Formula: `(1 + annual_rate) ** (1 / 360) - 1`
*   **`rate_daily_to_annual(rate: float) -> float`**
    *   Converts a daily interest rate to its equivalent annual rate.
    *   Formula: `(1 + daily_rate) ** 360 - 1`

### Stock Calculations

Functions for calculating stock returns and handling price adjustments.

*   **`stock_return_rate(current: float, previous: float) -> float | None`**
    *   Calculates the simple return rate between two prices.
    *   Formula: `current / previous - 1`
    *   Returns `None` if `previous` is `None`.
*   **`stock_adjusted_return_rate(current: float, previous: float, factor: float = 1, dividend_yeld: float = 0, tax: float = 2) -> float | None`**
    *   Calculates return rate considering a price adjustment `factor` (e.g., for splits/inplits), `dividend_yeld` (paid during the period), and an optional `tax` on dividends (defaulting to 2, implying 0% tax if not specified differently, as `1 - tax` is used).
    *   Formula: `(current * factor) / (previous - (dividend_yeld * abs(1 - tax))) - 1`
    *   Returns `None` if `previous` is `None`.
*   **`stock_adjusted_price(adjusted: float, adjusted_return_rate: float) -> float`**
    *   Calculates the theoretical previous price given the current adjusted price and the adjusted return rate between the two points.
    *   Formula: `adjusted / (1 + adjusted_return_rate)`
*   **`stock_adjusted_return_rate_check(current: float, previous_adjusted: float) -> float`**
    *   Calculates the return rate between the current price and a previously adjusted price. Useful for verifying adjustments.
    *   Formula: `current / previous_adjusted - 1`
*   **`stock_event_factor(expression: str) -> tuple[str | None, float]`**
    *   Parses a stock event string (like "10:1" for split or "1:10" for inplit/reverse split) to determine the event type and the numerical factor to apply to historical prices.
    *   Arguments:
        *   `expression` (str): Event string, e.g., "10:1" (split 1-to-10) or "1:10" (inplit 10-to-1).
    *   Returns:
        *   `tuple`: ('SPLIT' or 'INPLIT', factor). Factor is > 1 for SPLIT, < 1 for INPLIT. Returns `(None, 1)` if expression is empty or `None`.
    *   Raises: `ValueError` if the expression format is invalid.

### Investment Analysis

*   **`get_investment_table(df: pd.DataFrame, investment_amount: float) -> pd.DataFrame`**
    *   Calculates investment allocation metrics based on minimizing negative profit/loss impact (anti-Warren Buffett strategy). It assigns higher weights to assets with smaller losses (or larger gains) relative to the worst performer.
    *   Arguments:
        *   `df` (pd.DataFrame): DataFrame with columns 'Ticker', 'Price', 'Quantity', 'Average Price'.
        *   `investment_amount` (float): The total amount to be invested/allocated across the assets in the DataFrame.
    *   Returns:
        *   `pd.DataFrame`: The input DataFrame with added columns:
            *   `Profit/Loss`: `(Price - Average Price) * Quantity`
            *   `Adjusted Profit/Loss`: `Profit/Loss` shifted so the minimum is 0.
            *   `Weight`: `1 / (Adjusted Profit/Loss + 0.01)` (Inverse weight, higher for better performers).
            *   `Proportion`: Normalized `Weight` (sums to 1).
            *   `Investment Value`: `Proportion * investment_amount`.
            *   `Quantity to Buy`: `Investment Value / Price`.
    *   Raises: `ValueError` if required columns are missing.

### Utility Functions

*   **`random_header() -> dict`**
    *   Returns a randomly chosen dictionary containing common browser headers (User-Agent, Accept, etc.). Useful for web scraping to mimic different browsers.
*   **`is_valid_db_connection(conn) -> bool`**
    *   Checks if the provided object `conn` appears to be a valid database connection (duck typing by checking for a callable `execute` method).
*   **`numberize = lambda x: float(x.replace(",", ""))`**
    *   A lambda function to convert a string containing a number (potentially with commas as thousands separators) into a float.
*   **`first_or_none = lambda x: None if len(x) == 0 else x[0]`**
    *   A lambda function to safely get the first element of a sequence `x`, returning `None` if the sequence is empty.

## Modules

- **fbpyutils_finance.bovespa:** Functionality for fetching and processing historical stock data from the Bovespa stock exchange (B3).
    *   **Classes:**
        *   **`FetchModes`**
            *   **Description:** Defines constants for different data retrieval modes.
            *   **Attributes:**
                *   `LOCAL` (int): Fetch only from local storage (value: 0).
                *   `DOWNLOAD` (int): Download data from the source (value: 1).
                *   `LOCAL_OR_DOWNLOAD` (int): Fetch from local if available, otherwise download (value: 2).
                *   `STREAM` (int): Stream data directly from the source URL (value: 3).
        *   **`StockHistory(download_folder: str = None)`**
            *   **Description:** Fetches and processes historical stock data from Bovespa. Handles downloading, storing, and parsing of official Bovespa historical data files (COTAHIST).
            *   **Arguments:**
                *   `download_folder` (str, optional): Path to the folder where downloaded Bovespa data files (ZIP) will be stored or read from. Defaults to the user's home directory if not provided.
            *   **Raises:**
                *   `OSError`: If the provided `download_folder` path is invalid (doesn't exist or is not a directory).
            *   **Methods:**
                *   **`get_stock_history(period: str = 'A', period_data: str = None, fetch_mode: FetchModes = FetchModes.LOCAL_OR_DOWNLOAD, compact: bool = True, original_names: bool = False) -> pd.DataFrame`**
                    *   **Description:** Fetches, parses, and returns Bovespa historical stock data for a specified period.
                    *   **Arguments:**
                        *   `period` (str, optional): The time period ('A' for annual, 'M' for monthly, 'D' for daily). Defaults to 'A'.
                        *   `period_data` (str, optional): The specific date for the period (e.g., '2023' for annual, '012023' for monthly, '15012023' for daily). Defaults to the most recent complete period (current year for 'A', current month for 'M', yesterday for 'D').
                        *   `fetch_mode` (FetchModes, optional): How to retrieve the data (`FetchModes.LOCAL`, `FetchModes.DOWNLOAD`, `FetchModes.LOCAL_OR_DOWNLOAD`, `FetchModes.STREAM`). Defaults to `FetchModes.LOCAL_OR_DOWNLOAD`.
                        *   `compact` (bool, optional): Whether to return only a subset of essential columns. Defaults to `True`.
                        *   `original_names` (bool, optional): Whether to use the original Portuguese column names from the Bovespa file. Defaults to `False` (uses translated English names).
                    *   **Returns:**
                        *   `pd.DataFrame`: A pandas DataFrame containing the historical stock data, processed and formatted.
                    *   **Raises:**
                        *   `ValueError`: If an invalid `fetch_mode` or `period` is provided.
                        *   `OSError`: If `fetch_mode` is `LOCAL` and the required local file is invalid or missing.
                        *   `requests.exceptions.RequestException`: If downloading fails (implicitly via `requests.get`).
                        *   `UnicodeDecodeError`: If the data file cannot be read with any of the attempted encodings (ISO-8859-1, cp1252, latin, utf-8).
                        *   `TypeError`: If the parsed data is not a pandas DataFrame.
                *   **`validate_period_date(period_date: str) -> bool`** (static method)
                    *   **Description:** Validates if a given date string matches supported Bovespa formats ('%Y%m' or '%Y%m%d').
                    *   **Arguments:**
                        *   `period_date` (str): The date string to validate.
                    *   **Returns:**
                        *   `bool`: `True` if the format is valid.
                    *   **Raises:**
                        *   `ValueError`: If the date string format is invalid.
                *   **`to_float(x: str | any) -> float`** (static method)
                    *   **Description:** Converts a Bovespa numeric string (with implied decimal places) to a float.
                    *   **Arguments:**
                        *   `x` (str | any): The value to convert.
                    *   **Returns:**
                        *   `float`: The converted float value.
                *   **`to_date(x: str | any, format: str = '%Y%m%d') -> datetime.date`** (static method)
                    *   **Description:** Converts a Bovespa date string to a Python date object.
                    *   **Arguments:**
                        *   `x` (str | any): The date string to convert.
                        *   `format` (str, optional): The expected format of the input string. Defaults to '%Y%m%d'.
                    *   **Returns:**
                        *   `datetime.date`: The converted date object.
                *   **`get_info_tables() -> Dict`** (static method)
                    *   **Description:** Reads supplementary information tables (like BDI codes, market types) stored in an accompanying Excel file (`tabelas_anexas_bovespa.xlsx`).
                    *   **Returns:**
                        *   `Dict`: A dictionary containing the status and, if successful, a nested dictionary named 'tables' where keys are sheet names and values are pandas DataFrames of the tables. Includes error message if reading fails.
- **fbpyutils_finance.cvm:** For accessing and processing data from the CVM (Brazilian Securities and Exchange Commission). Handles downloading, parsing, and managing CVM data files, including fund registers (CAD_FI) and daily fund information (DIARIO_FI).
    *   **Classes:**
        *   **`CVM(catalog: sqlite3.Connection = None, history_folder: str = None)`**
            *   **Description:** Main class for interacting with CVM data. Manages a local catalog (SQLite DB) of available CVM files, handles downloading updates, and provides methods to access processed data.
            *   **Arguments:**
                *   `catalog` (sqlite3.Connection, optional): An existing SQLite database connection to use for the catalog. If `None`, a new connection to `catalog.db` in the user's app folder is created.
                *   `history_folder` (str, optional): Path to the folder where downloaded and processed CVM files are stored. If `None`, defaults to a 'history' subfolder within the user's app folder.
            *   **Methods:**
                *   **`check_history_folder(history_folder: str = None) -> str`** (static method)
                    *   **Description:** Checks if the specified history folder exists, creates it if not, and returns the validated path.
                *   **`get_cvm_catalog() -> pd.DataFrame | None`**
                    *   **Description:** Retrieves the current catalog of CVM files tracked by the instance from the SQLite database.
                    *   **Returns:** A pandas DataFrame with catalog details (file name, kind, URLs, download/update timestamps, etc.), or `None` if the catalog table doesn't exist yet.
                *   **`update_cvm_catalog() -> Tuple[List[Dict], List[Dict], List[Tuple]]`**
                    *   **Description:** Checks the official CVM data portal for new or updated files (both current and historical for IF_REGISTER and IF_POSITION), downloads them if necessary, updates the local catalog database, and stores the files in the `history_folder`. Handles ZIP files and different text encodings.
                    *   **Returns:** A tuple containing:
                        1.  `update_results` (List[Dict]): Summary of updates per file (name, kind, errors, successes, skips).
                        2.  `metadata_to_process` (List[Dict]): Detailed metadata of files that were downloaded or updated.
                        3.  `ops` (List[Tuple]): SQL operations performed during the update (for debugging).
                    *   **Raises:** `ValueError` on failure during any step (e.g., network issues, file processing errors).
                *   **`get_cvm_files(kind: str = 'IF_POSITION', history: bool = False) -> Tuple[Tuple]`**
                    *   **Description:** Queries the local catalog for files of a specific `kind` that need processing (based on `last_updated` vs `last_download` timestamps) and returns their details along with the actual file paths found in the `history_folder`.
                    *   **Arguments:**
                        *   `kind` (str, optional): The type of CVM data ('IF_POSITION' or 'IF_REGISTER'). Defaults to 'IF_POSITION'.
                        *   `history` (bool, optional): Whether to retrieve historical files (`True`) or current files (`False`). Defaults to `False`.
                    *   **Returns:** A tuple of tuples, where each inner tuple contains `(kind, name, history_flag, file_paths_tuple)`.
                    *   **Raises:** `ValueError` if querying the catalog fails.
                *   **`get_cvm_file_data(cvm_file: str) -> Tuple[str, str, pd.DataFrame, List[str]]`**
                    *   **Description:** Reads a specific CVM data file (previously downloaded and stored in `history_folder`), parses it according to predefined mappings and transformations (handling different header versions), applies data type conversions, adds period information (year, month), and returns the processed data.
                    *   **Arguments:**
                        *   `cvm_file` (str): The full path to the CVM data file to process.
                    *   **Returns:** A tuple containing `(kind, sub_kind, processed_data_df, partition_columns_list)`.
                    *   **Raises:** `ValueError` if header mappings are missing, header hash doesn't match known versions, or processing/conversion fails.
                *   **`update_cvm_files(cvm_files: List[Tuple[str, str, str]]) -> bool`**
                    *   **Description:** Updates the `last_updated` timestamp in the local catalog for the specified files, marking them as processed.
                    *   **Arguments:**
                        *   `cvm_files` (List[Tuple[str, str, str]]): A list of tuples, each containing `(kind, name, last_update_timestamp_str)`.
                    *   **Returns:** `True` if the update was successful.
                    *   **Raises:** `ValueError` if updating the catalog fails.
    *   **Internal Helper Functions:** (Includes functions like `_get_url_paths`, `_update_cvm_history_file`, `_read_cvm_history_file`, `_apply_expressions`, `_apply_converters`, `_check_cvm_headers_changed`, etc., which handle the core logic of fetching, parsing, transforming, and managing CVM data and headers).
- **fbpyutils_finance.yahoo:** For retrieving stock, currency, and dividend data from Yahoo Finance using both the `yfinance` library and web scraping.
    *   **Classes:**
        *   **`YahooCurrencyDataProvider(params: Dict)`**
            *   **Description:** Fetches historical exchange rate data between two currencies using `yfinance`.
            *   **Arguments (`params` Dict):**
                *   `currency_from` (str): Base currency code (e.g., "USD").
                *   `currency_to` (str): Target currency code (e.g., "BRL").
                *   `start` (str | datetime.date): Start date for the data range.
                *   `end` (str | datetime.date): End date for the data range.
            *   **Methods:**
                *   **`get_data() -> pd.DataFrame`**
                    *   **Description:** Downloads the currency exchange rate data.
                    *   **Returns:** A pandas DataFrame with columns like 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', plus 'Ticker' (e.g., "USDBRL") and 'Date'.
                    *   **Raises:** `AssertionError` if required params are missing or `end` <= `start`. Implicitly raises exceptions from `yfinance.download`.
        *   **`YahooStockDataProvider(params: Dict)`**
            *   **Description:** Fetches historical stock price data or dividend payment data for a specific ticker using `yfinance`.
            *   **Arguments (`params` Dict):**
                *   `ticker` (str): The stock ticker symbol (e.g., "AAPL").
                *   `market` (str): The market ('BR' for Brazil, 'US' for USA). Determines if '.SA' suffix is added.
                *   `start` (str | datetime.date): Start date for the data range.
                *   `end` (str | datetime.date): End date for the data range.
                *   `payments` (bool, optional): If `True`, fetches dividend payments instead of price history. Defaults to `False`.
            *   **Methods:**
                *   **`get_data() -> pd.DataFrame`**
                    *   **Description:** Downloads the stock price history or dividend payments.
                    *   **Returns:**
                        *   If `payments` is `False`: A pandas DataFrame with OHLCV data plus 'Ticker' and 'Date'.
                        *   If `payments` is `True`: A pandas DataFrame with dividend 'Payment' amounts indexed by date, plus 'Ticker' and 'Date' columns. Returns `None` if no dividends found in the period.
                    *   **Raises:** `AssertionError` if required params are missing, `end` <= `start`, or market is invalid. Implicitly raises exceptions from `yfinance.download` or `yf.Ticker().dividends`.
    *   **Functions:**
        *   **`stock_price(x: str, market: str = None) -> Dict`**
            *   **Description:** Performs a Yahoo Finance web scrape to get the *current* stock price and basic info for a ticker. Note: This uses web scraping, not `yfinance`, and might be less reliable.
            *   **Arguments:**
                *   `x` (str): The stock ticker symbol (e.g., "AAPL", "PETR4.SA").
                *   `market` (str, optional): Market identifier (primarily used by the caller, not directly used in the scraping URL logic itself in this implementation).
            *   **Returns:**
                *   `Dict`: A dictionary containing the stock information if successful, or error details if failed. Structure:
                    ```python
                    {
                        'info': 'STOCK PRICE',
                        'source': 'YAHOO',
                        'status': 'SUCCESS' or 'ERROR',
                        'details': {
                            # On SUCCESS:
                            'market': str, # Extracted from page
                            'ticker': str, # Extracted from page
                            'name': str, # Extracted from page
                            'currency': str, # Extracted from page
                            'price': float, # Extracted from page
                            'variation': None, # Currently None
                            'variation_percent': None, # Currently None
                            'trend': None, # Currently None
                            'position_time': datetime.datetime,
                            # On ERROR:
                            'error_message': str
                        }
                    }
                    ```
            *   **Raises:**
                *   Internally catches exceptions (like `ValueError` if ticker is missing, scraping fails, or parsing fails) and sets the `'status'` to `'ERROR'` with an `'error_message'` in `'details'`. Direct exceptions are unlikely unless there's an issue outside the `try...except` block (e.g., network error in `_ysearch`).
- **fbpyutils_finance.bing:** For retrieving stock data from Bing Finance.
    *   **Functions:**
        *   **`stock_price(x: str, market: str = None) -> Dict`**
            *   **Description:** Performs a Bing search to fetch the current price and related information for a given stock ticker.
            *   **Arguments:**
                *   `x` (str): The stock ticker symbol to search for (e.g., "AAPL", "MSFT").
                *   `market` (str, optional): The market identifier to specify the exchange (e.g., "NASDAQ", "BVMF"). Defaults to `None`, which performs a general search.
            *   **Returns:**
                *   `Dict`: A dictionary containing the stock information if successful, or error details if failed. Structure:
                    ```python
                    {
                        'info': 'STOCK PRICE',
                        'source': 'BING',
                        'status': 'SUCCESS' or 'ERROR',
                        'details': {
                            # On SUCCESS:
                            'market': str,
                            'ticker': str,
                            'name': str,
                            'currency': str,
                            'price': float,
                            'variation': None, # Currently None
                            'variation_percent': None, # Currently None
                            'trend': None, # Currently None
                            'position_time': datetime.datetime,
                            # On ERROR:
                            'error_message': str
                        }
                    }
                    ```
            *   **Raises:**
                *   Internally catches exceptions (like `ValueError` if ticker is missing, search fails, or parsing fails) and sets the `'status'` to `'ERROR'` with an `'error_message'` in `'details'`. Direct exceptions are unlikely to be raised to the caller unless there's an issue outside the `try...except` block.
- **fbpyutils_finance.tesourodireto:** For accessing data from Tesouro Direto (Brazilian National Treasury direct sale program).
    *   **Functions:**
        *   **`treasury_bonds(x: str = None) -> Dict`**
            *   **Description:** Retrieves current information about available Brazilian Treasury Bonds directly from the Tesouro Direto API.
            *   **Arguments:**
                *   `x` (str, optional): The specific bond name to retrieve (e.g., "Tesouro Selic 2027"). If `None`, retrieves information for all available bonds.
            *   **Returns:**
                *   `Dict`: A dictionary containing bond information. Structure:
                    ```python
                    {
                        'info': 'TREASURY BOND',
                        'source': 'TESOURO DIRETO',
                        'status': 'SUCCESS', 'NOT FOUND', or 'ERROR',
                        'details': {
                            # On SUCCESS:
                            'market': {
                                'status': str ('OPEN' or 'CLOSED'),
                                'closing_time': datetime.datetime, # TZ Aware (America/Sao_Paulo)
                                'opening_time': datetime.datetime, # TZ Aware (America/Sao_Paulo)
                                'position_time': datetime.datetime # TZ Aware (America/Sao_Paulo)
                            },
                            'matches': int, # Number of bonds returned
                            'bonds': [
                                {
                                    'bond_name': str,
                                    'due_date': datetime.datetime,
                                    'financial_indexer': str,
                                    'annual_investment_rate': float | None, # Rate for buying
                                    'annual_redemption_rate': float | None, # Rate for selling
                                    'isin_code': str,
                                    'sell_price': float | None, # Price if you sell back to Treasury
                                    'sell_price_unit': float | None, # Minimum value to sell
                                    'buy_price': float | None, # Price if you buy from Treasury
                                    'buy_price_unit': float | None, # Minimum value to buy
                                    'extended_description': str
                                },
                                # ... more bonds
                            ],
                            # On NOT FOUND:
                            'bond_name': str, # The name searched for
                            # On ERROR:
                            'error_message': str
                        }
                    }
                    ```
            *   **Raises:**
                *   Internally catches exceptions (`TypeError` for SSL cipher issues, `SystemError` for API errors, general `Exception`) and sets the `'status'` to `'ERROR'` with an `'error_message'` in `'details'`. Direct exceptions are unlikely unless there's an issue outside the `try...except` block.
- **fbpyutils_finance.google:** For retrieving stock price and currency exchange rate data by scraping Google Search results. Note: Web scraping can be unreliable due to changes in Google's page structure.
    *   **Functions:**
        *   **`exchange_rate(x: str, y: str) -> Dict`**
            *   **Description:** Performs a Google search to find the exchange rate between two currencies.
            *   **Arguments:**
                *   `x` (str): The currency code to convert from (e.g., "USD").
                *   `y` (str): The currency code to convert to (e.g., "BRL").
            *   **Returns:**
                *   `Dict`: A dictionary containing the exchange rate information. Structure:
                    ```python
                    {
                        'info': 'EXCHANGE RATE',
                        'source': 'GOOGLE',
                        'status': 'SUCCESS', 'NOT FOUND', or 'ERROR',
                        'details': {
                            # On SUCCESS:
                            'from': str, # e.g., "USD (Dólar americano)"
                            'to': str, # e.g., "BRL (Real brasileiro)"
                            'unit': int, # The unit of the 'from' currency (usually 1)
                            'exchange_rate': float, # The calculated exchange rate
                            # On NOT FOUND:
                            'from': str, # Original 'from' currency code
                            'to': str, # Original 'to' currency code
                            # On ERROR:
                            'error_message': str
                        }
                    }
                    ```
            *   **Raises:**
                *   Internally catches exceptions (`ValueError` if currencies are missing or parsing fails, general `Exception`) and sets the `'status'` to `'ERROR'` or `'NOT FOUND'`. Direct exceptions are unlikely unless there's an issue outside the `try...except` block (e.g., network error in `_googlesearch`).
        *   **`stock_price(x: str, market: str = None) -> Dict`**
            *   **Description:** Performs a Google search to find the current stock price, variation, and other details for a given ticker.
            *   **Arguments:**
                *   `x` (str): The stock ticker symbol (e.g., "AAPL", "PETR4").
                *   `market` (str, optional): The market identifier (e.g., "BVMF", "NASDAQ"). If not provided, attempts to extract it from the search results.
            *   **Returns:**
                *   `Dict`: A dictionary containing the stock price information. Structure:
                    ```python
                    {
                        'info': 'STOCK PRICE',
                        'source': 'GOOGLE',
                        'status': 'SUCCESS' or 'ERROR',
                        'details': {
                            # On SUCCESS:
                            'market': str,
                            'ticker': str,
                            'name': str, # Extracted company name
                            'currency': str, # e.g., "BRL", "USD"
                            'price': float,
                            'variation': float, # Price change amount
                            'variation_percent': float, # Price change percentage (e.g., 0.01 for 1%)
                            'trend': str, # 'UP', 'DOWN', or 'NEUTRAL'
                            'position_time': datetime.datetime, # TZ Aware, based on market timezone
                            # On ERROR:
                            'error_message': str
                        }
                    }
                    ```
            *   **Raises:**
                *   Internally catches exceptions (`ValueError` if ticker is missing, search fails, parsing fails, market timezone not found, etc.) and sets the `'status'` to `'ERROR'`. Direct exceptions are unlikely unless there's an issue outside the `try...except` block.
- **fbpyutils_finance.cei:** For processing data exported from CEI (Canal Eletrônico do Investidor) in Excel format. It reads various report types (movements, provisioned events, negotiations, positions) and consolidates them into structured data.
    *   **Functions:**
        *   **`get_cei_data(input_folder: str, parallelize: bool = True) -> List[Tuple[str, int, pd.DataFrame | None]]`**
            *   **Description:** Finds and processes various CEI report Excel files (e.g., `movimentacao-*.xlsx`, `posicao-*.xlsx`) within the specified `input_folder`. It uses predefined schemas and processing functions for each report type.
            *   **Arguments:**
                *   `input_folder` (str): The path to the directory containing the CEI Excel report files.
                *   `parallelize` (bool, optional): If `True` (and multiple CPU cores are available), processing of different report types will run in parallel. Defaults to `True`.
            *   **Returns:**
                *   `List[Tuple[str, int, pd.DataFrame | None]]`: A list of tuples, one for each processed report type found. Each tuple contains:
                    *   `operation_name` (str): The internal name of the report type (e.g., 'movimentacao', 'posicao_acoes').
                    *   `row_count` (int): The number of rows in the processed DataFrame (0 if no data or processing failed).
                    *   `data` (pd.DataFrame | None): A pandas DataFrame containing the consolidated and processed data for that report type, or `None` if no files were found or processing failed for that type.
            *   **Note:** This function relies on specific file naming conventions (like `movimentacao-*.xlsx`) and internal schema processing functions located in `fbpyutils_finance.cei.schemas`. Errors during the processing of a specific file type are generally handled within the schema functions, potentially resulting in `None` or an empty DataFrame for that type in the output list.
- **fbpyutils_finance.investidor10:** For retrieving data related to Brazilian Real Estate Investment Trusts (FIIs) by scraping the Investidor10 website and fiis.com.br. Note: Web scraping can be unreliable due to website structure changes.
    *   **Functions:**
        *   **`get_fii_daily_position(parallelize: bool = True) -> pd.DataFrame`**
            *   **Description:** Scrapes multiple pages from Investidor10 and fiis.com.br to gather comprehensive daily data for FIIs. This includes payment schedules (past and future based on 'data com'), IFIX composition, dividend yield rankings, and individual FII indicators (price, P/VP, liquidity, net worth, vacancy, etc.). It consolidates this information into a single DataFrame.
            *   **Arguments:**
                *   `parallelize` (bool, optional): If `True` (and multiple CPU cores are available), scraping individual FII indicator pages will run in parallel. Defaults to `True`.
            *   **Returns:**
                *   `pd.DataFrame`: A pandas DataFrame containing the consolidated daily position data for FIIs. Columns include details like 'ticker', 'name', 'payment_date', 'com_date', 'payment', 'price', 'price_date', 'fund_type', 'segment', 'ifix_share', 'dy_current', 'p_vp', 'daily_liquidity', 'net_worth', 'vacancy', 'shareholders', 'shares', 'equity_by_share', 'equity', 'last_payment', 'reference_date', etc.
            *   **Raises:**
                *   `SystemError`: If HTTP requests to the source websites fail (e.g., non-200 status code).
                *   Other exceptions related to network issues, HTML parsing errors (if website structure changes), or data processing errors within pandas/sqlite.
            *   **Note:** This function performs extensive web scraping and relies heavily on the current structure of the Investidor10 and fiis.com.br websites. Changes to these sites may break the function. It uses an in-memory SQLite database to join the data scraped from different sources.

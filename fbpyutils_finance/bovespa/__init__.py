"""
fbpyutils_finance.bovespa - B3 (Bovespa) Historical Stock Data Provider

Purpose: This module provides classes and functions to fetch, download, parse, and process historical stock data (COTAHIST) from B3 (Brazilian stock exchange), including ZIP file handling, fixed-width parsing, column conversion, and data validation for periods (daily, monthly, annual).

Main contents:
- FetchModes (class): Constants for data fetching modes (LOCAL, DOWNLOAD, etc.)
- StockHistory (class): Main class for handling B3 historical data, with methods for path building, downloading, data treatment, local checks, and getting history
- Static methods: validate_period_date(), to_float(), to_date(), get_info_tables()

High-level usage pattern:
Import StockHistory and create instance with download_folder, then call get_stock_history(period='A', fetch_mode=FetchModes.LOCAL_OR_DOWNLOAD) to get DataFrame of stock data.

Examples:
>>> from fbpyutils_finance.bovespa import StockHistory
>>> history = StockHistory(download_folder='~/bovespa_data')
>>> df = history.get_stock_history(period='A', period_data='2023')
>>> print(df.head())
   datpre  codbdi  tpmerc  codneg  nomres  especi  ...  preult  totneg  quotot  voltot
0  20230103      2       1    A1AA11  A1AA11  A1AA11  ...    1234  1000   1234567
... (actual data varies)
"""

import os
import requests
import pandas as pd
from datetime import date, datetime, timedelta
from typing import Any, Dict, Optional, Tuple  # Added date, Optional, Tuple, Dict, Any

import fbpyutils_finance as FI
from fbpyutils import file as F, xlsx as XL


_bvmf_cert = FI.CERTIFICATES["bvmf-bmfbovespa-com-br"]


class FetchModes:
    """
    Defines constants for different data retrieval modes used in StockHistory.

    Attributes:
        LOCAL (int): Fetch data only from local storage.
        DOWNLOAD (int): Download data from the source.
        LOCAL_OR_DOWNLOAD (int): Try local storage first, then download if not found or invalid.
        STREAM (int): Fetch data as a stream (currently used similarly to DOWNLOAD).
    """

    LOCAL = 0
    DOWNLOAD = 1
    LOCAL_OR_DOWNLOAD = 2
    STREAM = 3


class StockHistory:
    """
    Fetches and processes historical stock data (COTAHIST) from the B3 website (formerly BOVESPA).

    This class handles downloading the historical data files (ZIP format),
    parsing the fixed-width text files within the ZIP, and returning the data
    as a pandas DataFrame. It supports different fetching modes (local, download)
    and time periods (daily, monthly, annual).

    Attributes:
        download_folder (str): The directory where downloaded COTAHIST ZIP files
                               are stored and read from.
    """

    _col_widths = [
        2,
        8,
        2,
        12,
        3,
        12,
        10,
        3,
        4,
        13,
        13,
        13,
        13,
        13,
        13,
        13,
        5,
        18,
        18,
        13,
        1,
        8,
        7,
        13,
        12,
        3,
    ]

    _col_names = [
        "record_type",
        "trade_date",
        "bdi_code",
        "ticker",
        "market_type",
        "ticker_issuer",
        "ticker_specs",
        "term_days",
        "currency",
        "open_value",
        "max_value",
        "min_value",
        "average_value",
        "close_value",
        "best_buy_offer",
        "best_sell_offer",
        "total_trades",
        "total_trades_papers",
        "total_trades_value",
        "option_market_current_price",
        "option_market_current_price_adjustment_indicator",
        "option_market_due_date",
        "ticker_trade_factor",
        "option_market_current_price_in_points",
        "ticker_isin_code",
        "ticker_distribution_number",
    ]

    _converters = {
        "record_type": lambda x: str(int(x)),
        "trade_date": lambda x: str(x),
        "bdi_code": lambda x: str(x),
        "ticker": lambda x: str(x),
        "market_type": lambda x: str(int(x)),
        "ticker_issuer": lambda x: str(x),
        "ticker_specs": lambda x: str(x),
        "term_days": lambda x: str(x),
        "currency": lambda x: str(x),
        "open_value": lambda x: str(int(x)),
        "max_value": lambda x: str(int(x)),
        "min_value": lambda x: str(int(x)),
        "average_value": lambda x: str(int(x)),
        "close_value": lambda x: str(int(x)),
        "best_buy_offer": lambda x: str(int(x)),
        "best_sell_offer": lambda x: str(int(x)),
        "total_trades": lambda x: str(int(x)),
        "total_trades_papers": lambda x: str(int(x)),
        "total_trades_value": lambda x: str(int(x)),
        "option_market_current_price": lambda x: str(int(x)),
        "option_market_current_price_adjustment_indicator": lambda x: str(int(x)),
        "option_market_due_date": lambda x: str(int(x)),
        "ticker_trade_factor": lambda x: str(int(x)),
        "option_market_current_price_in_points": lambda x: str(int(x)),
        "ticker_isin_code": lambda x: str(x),
        "ticker_distribution_number": lambda x: str(x),
    }

    _data_columns = [
        "trade_date",
        "bdi_code",
        "market_type",
        "ticker",
        "ticker_issuer",
        "ticker_specs",
        "ticker_isin_code",
        "term_days",
        "currency",
        "open_value",
        "min_value",
        "max_value",
        "average_value",
        "close_value",
        "total_trades",
        "total_trades_papers",
        "total_trades_value",
    ]

    _original_col_names = [
        "tipreg",
        "datpre",
        "codbdi",
        "codneg",
        "tpmerc",
        "nomres",
        "especi",
        "prazot",
        "modref",
        "preabe",
        "premax",
        "premin",
        "premed",
        "preult",
        "preofc",
        "preofv",
        "totneg",
        "quatot",
        "voltot",
        "preexe",
        "indopc",
        "datven",
        "fatcot",
        "ptoexe",
        "codisi",
        "dismes",
    ]

    _original_data_columns = [
        "datpre",
        "codbdi",
        "tpmerc",
        "codneg",
        "nomres",
        "especi",
        "codisi",
        "prazot",
        "modref",
        "preabe",
        "premin",
        "premax",
        "premed",
        "preult",
        "totneg",
        "quatot",
        "voltot",
    ]

    @staticmethod
    def validate_period_date(period_date: str) -> bool:
        """
        Validates if a given string matches supported date formats ('%Y%m' or '%Y%m%d').

        Args:
            period_date (str): The date string to validate.

        Returns:
            bool: True if the string matches one of the supported formats.

        Raises:
            ValueError: If the string does not match any supported format.
        """
        formats = ["%Y%m", "%Y%m%d"]  # Supported date formats

        for date_format in formats:
            try:
                datetime.strptime(period_date, date_format)
                # Check if the parsed date string matches the original format
                if (
                    datetime.strptime(period_date, date_format).strftime(date_format)
                    == period_date
                ):
                    return True  # Date is valid and matches format
            except ValueError:
                pass

        raise ValueError("Invalid date format or value: " + period_date)

    @staticmethod
    def to_float(x: Any) -> float:
        """
        Converts a B3-formatted price string (last 2 chars are decimals) or any value to float.

        Args:
            x (Any): The value to convert. If string, assumes B3 price format (e.g., '12345' -> 123.45).

        Returns:
            float: The converted float value.
        """
        return (
            0.0
            if type(x) == str and not x
            else float(".".join([x[0:-2], x[-2:]]))
            if type(x) == str
            else float(x)
        )

    @staticmethod
    def to_date(x: Any, format: str = "%Y%m%d") -> Optional[date]:
        """
        Converts a value to a date object using pandas.to_datetime.

        Args:
            x (Any): The value to convert (typically a string like 'YYYYMMDD').
            format (str, optional): The expected date format string. Defaults to '%Y%m%d'.

        Returns:
            Optional[date]: The converted date object, or None if conversion fails ('ignore' errors).
        """
        result = pd.to_datetime(x, format=format, errors="ignore")
        if isinstance(result, str):
            return None
        if pd.isna(result):  # Check for NaT
            return None
        return result.date()

    @staticmethod
    def get_info_tables() -> Dict[str, Any]:
        """
        Reads auxiliary information tables from the 'tabelas_anexas_bovespa.xlsx' file.

        This file contains mappings for codes used in the COTAHIST files (e.g., BDI codes, market types).

        Returns:
            Dict[str, Any]: A dictionary containing the status and, on success,
                            another dictionary 'tables' where keys are sheet names
                            and values are pandas DataFrames of the sheet content.
                            Example: {'status': 'OK', 'tables': {'bdi_codes': DataFrame, ...}, 'message': '...'}
                            On error: {'status': 'ERROR', 'message': '...'}
        """
        info_tables_path = os.path.join(
            FI._ROOT_DIR, "bovespa", "tabelas_anexas_bovespa.xlsx"
        )
        response: Dict[str, Any] = {"status": "OK", "tables": {}, "message": ""}
        try:
            # Assuming XL.ExcelWorkbook and read_sheet are defined elsewhere in fbpyutils
            info_tables = XL.ExcelWorkbook(info_tables_path)
            response["tables"] = {}
            sheet_names = XL.get_sheet_names(
                info_tables_path
            )  # Use get_sheet_names function
            for sheet in sheet_names:  # Iterate through sheet_names
                # Assuming read_sheet returns a tuple/list of lists/tuples
                info_data = tuple(info_tables.read_sheet(sheet))
                if info_data and len(info_data) > 0:
                    response["tables"][sheet] = pd.DataFrame(
                        info_data[1:],
                        columns=[
                            str(c).lower() for c in info_data[0]
                        ],  # Ensure columns are strings
                    )
                else:
                    response["tables"][sheet] = pd.DataFrame()  # Handle empty sheets
            response["message"] = (
                f"All {len(sheet_names)} sheets fetched."  # Use sheet_names variable
            )
            return response
        except Exception as e:
            response["status"] = "ERROR"
            response["message"] = f"Error fetching bovespa info tables: {str(e)}"
            response.pop("tables", None)  # Remove tables key on error
            return response

    def __init__(self, download_folder: Optional[str] = None) -> None:
        """
        Initializes the StockHistory instance.

        Args:
            download_folder (Optional[str], optional): The path to the folder for
                storing/retrieving downloaded COTAHIST files. If None, defaults
                to the user's home directory. Defaults to None.

        Raises:
            OSError: If the specified download_folder does not exist or is not a directory.
        """
        if download_folder is None or len(download_folder) == 0:
            download_folder = os.path.expanduser("~")

        if not os.path.exists(download_folder):
            raise OSError("Path doesn't exists.")

        if not os.path.isdir(download_folder):
            raise OSError("Path is not a folder.")

        self.download_folder = download_folder

    def _build_paths(
        self, period: str = "A", period_date: Optional[str] = None
    ) -> Tuple[str, str]:
        """
        Constructs the download URL and local file path for a COTAHIST file.

        Args:
            period (str, optional): The period type ('A' annual, 'M' monthly, 'D' daily). Defaults to 'A'.
            period_date (Optional[str], optional): The specific date string for the period.
                Format depends on the period:
                - 'A': 'YYYY' (e.g., '2023')
                - 'M': 'MMYYYY' (e.g., '012023')
                - 'D': 'DDMMYYYY' (e.g., '15012023')
                If None, defaults to the current year (A), current month/year (M),
                or yesterday (D). Defaults to None.

        Returns:
            Tuple[str, str]: A tuple containing (download_url, local_filepath).

        Raises:
            ValueError: If the period is invalid or period_date format is incorrect.
        """
        period = period or "A"

        if period is None or period not in ["A", "M", "D"]:
            raise ValueError("Invalid period. User A, M or D.")

        if period_date:
            self.validate_period_date(period_date=period_date)

        if period == "A":
            period_date = period_date or datetime.today().strftime("%Y")
        elif period == "M":
            period_date = period_date or datetime.today().strftime("%m%Y")
        else:
            yesterday = datetime.today() - timedelta(days=1)
            period_date = period_date or yesterday.strftime("%d%m%Y")

        cotfile = "COTAHIST_" + period + period_date + ".ZIP"

        url = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist/" + cotfile

        output_file = os.path.sep.join([self.download_folder, cotfile])

        return url, output_file

    def _download_stock_history(
        self, period: str = "A", period_data: Optional[str] = None
    ) -> str:
        """
        Downloads a COTAHIST ZIP file for the specified period.

        Args:
            period (str, optional): Period type ('A', 'M', 'D'). Defaults to 'A'.
            period_data (Optional[str], optional): Specific date string for the period. Defaults to None.

        Returns:
            str: The full path to the downloaded ZIP file.

        Raises:
            requests.exceptions.RequestException: If the download fails.
            ValueError: If period or period_data are invalid (via _build_paths).
            OSError: If file writing fails.
        """
        url, output_file = self._build_paths(period, period_data)

        block_size = 1024**3

        response = requests.get(url, stream=True, verify=_bvmf_cert)

        with open(output_file, "wb") as handle:
            for data in response.iter_content(block_size):
                handle.write(data)

        return output_file

    def _treat_data(
        self, data: pd.DataFrame, original_names: bool, compact: bool
    ) -> pd.DataFrame:
        """
        Processes the raw DataFrame read from the COTAHIST file.

        This includes filtering for actual stock records (record_type '1'),
        converting date and numeric columns to appropriate types, handling NaNs,
        and optionally selecting a compact set of columns or renaming columns
        to their original Portuguese names.

        Args:
            data (pd.DataFrame): The raw DataFrame read from the file.
            original_names (bool): If True, rename columns to original names (e.g., 'datpre').
            compact (bool): If True, select only a subset of essential columns.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        cot_data = data[data["record_type"] == "1"].copy(deep=True)

        for col in [
            "open_value",
            "min_value",
            "max_value",
            "average_value",
            "close_value",
            "total_trades_value",
        ]:
            cot_data[col] = cot_data[col].apply(StockHistory.to_float)

        cot_data["trade_date"] = cot_data["trade_date"].apply(StockHistory.to_date)

        cot_data = cot_data.fillna(0)

        if original_names:
            cot_data.columns = self._original_col_names
            if compact:
                return cot_data[self._original_data_columns]
            else:
                return cot_data
        else:
            if compact:
                return cot_data[self._data_columns]
            else:
                return cot_data

    def _check_local_history(
        self, period: str = "A", period_data: Optional[str] = None
    ) -> bool:
        """
        Checks if a valid COTAHIST ZIP file exists locally for the given period.

        Args:
            period (str, optional): Period type ('A', 'M', 'D'). Defaults to 'A'.
            period_data (Optional[str], optional): Specific date string for the period. Defaults to None.

        Returns:
            bool: True if a valid local ZIP file exists, False otherwise.
        """
        _, local_file = self._build_paths(period, period_data)

        return (
            os.path.exists(local_file)
            and os.path.isfile(local_file)
            and F.mime_type(local_file) == "application/zip"
        )

    def get_stock_history(
        self,
        period: str = "A",
        period_data: Optional[str] = None,
        fetch_mode: int = FetchModes.LOCAL_OR_DOWNLOAD,
        compact: bool = True,
        original_names: bool = False,
    ) -> pd.DataFrame:
        """
        Fetches, parses, and processes B3 historical stock data (COTAHIST).

        Args:
            period (str, optional): Period type ('A', 'M', 'D'). Defaults to 'A'.
            period_data (Optional[str], optional): Specific date string for the period. Defaults to None.
            fetch_mode (int, optional): Fetch mode constant from FetchModes class.
                                        Defaults to FetchModes.LOCAL_OR_DOWNLOAD.
            compact (bool, optional): If True, return only essential columns. Defaults to True.
            original_names (bool, optional): If True, use original Portuguese column names. Defaults to False.

        Returns:
            pd.DataFrame: A DataFrame containing the historical stock data.

        Raises:
            ValueError: If fetch_mode is invalid.
            OSError: If local file access fails when required.
            requests.exceptions.RequestException: If download fails.
            Exception: For errors during file reading or processing.
        """
        if fetch_mode not in [
            FetchModes.LOCAL,
            FetchModes.DOWNLOAD,
            FetchModes.LOCAL_OR_DOWNLOAD,
            FetchModes.STREAM,
        ]:
            raise ValueError("Invalid fetch mode.")

        if fetch_mode == FetchModes.LOCAL_OR_DOWNLOAD:
            if self._check_local_history(period, period_data):
                fetch_mode = FetchModes.LOCAL
            else:
                fetch_mode = FetchModes.DOWNLOAD

        if fetch_mode == FetchModes.DOWNLOAD:
            data_file = self._download_stock_history(period, period_data)

        if fetch_mode == FetchModes.LOCAL:
            if self._check_local_history(period, period_data):
                _, data_file = self._build_paths(period, period_data)
            else:
                raise OSError("Invalid or non existent local file.")

        if fetch_mode == FetchModes.STREAM:
            data_file, _ = self._build_paths(period, period_data)

        cot = None
        encoding_list = ["ISO-8859-1", "cp1252", "latin", "utf-8"]
        while cot is None and len(encoding_list) > 0:
            encoding = encoding_list.pop()
            try:
                cot = pd.read_fwf(
                    data_file,
                    header=None,
                    compression="zip",
                    widths=self._col_widths,
                    names=self._col_names,
                    converters=self._converters,
                    encoding=encoding,
                )
            except UnicodeDecodeError:
                cot = None

        if cot is None:
            # Raise a runtime error as we couldn't decode the file with any known encoding
            raise RuntimeError("Error reading stock history file. Unknown encoding.")

        if type(cot) != pd.core.frame.DataFrame:
            raise TypeError("Failed to get the stock history. Invalid output data.")

        return self._treat_data(cot, original_names, compact)

"""
fbpyutils_finance.investidor10 - Investidor10 FIIs (Fundos de Investimento Imobiliário) Data Provider

Purpose: This module provides functionality to retrieve and consolidate daily FII (Real Estate Investment Funds) data from Investidor10 website, including payment calendars, IFIX composition, dividend yield rankings, and detailed indicators.

Main contents:
- get_fii_daily_position() (function): Main function to retrieve consolidated daily FII position
- _create_db_indexes() (function): Create SQLite indexes for faster joins

High-level usage pattern:
Import get_fii_daily_position and call it to get a consolidated DataFrame with all FII information from multiple sources.

Examples:
>>> from fbpyutils_finance.investidor10 import get_fii_daily_position
>>> df = get_fii_daily_position()
>>> isinstance(df, pd.DataFrame)
True
>>> 'ticker' in df.columns
True
>>> 'payment' in df.columns
True
"""

# fbpyutils_finance/investidor10/__init__.py
import os
import sqlite3
import pandas as pd
from multiprocessing import Pool
from typing import List, Dict, Any, Optional

from fbpyutils_finance import logger

# Import functions from submodules
from .constants import (
    FIIS_PAYMENT_URL,
    IFIX_PAGE_URL,
    FIIS_DY_DETAILS_URL,
    CAPTURE_DATE,
    PARALLELIZE as DEFAULT_PARALLELIZE,
)
from .payments import get_fii_all_payment_data
from .ifix import get_ifix_data
from .ranking import get_fii_dy_ranking_data
from .indicators import get_fii_indicators

# Publicly expose the main function
__all__ = ["get_fii_daily_position"]


def _create_db_indexes(cursor: sqlite3.Cursor):
    """Creates indexes on the SQLite tables for faster joins."""
    logger.info("Creating database indexes")
    try:
        logger.debug("Creating index fii_payment_calendar_i01")
        cursor.execute(
            "create index fii_payment_calendar_i01 on fii_payment_calendar (substr(payment_date, 1, 4))"
        )
        logger.debug("Creating index fii_payment_calendar_i02")
        cursor.execute(
            "create index fii_payment_calendar_i02 on fii_payment_calendar (payment_date, ticker)"
        )
        logger.debug("Creating index fii_ifix_position_i01")
        cursor.execute(
            "create index fii_ifix_position_i01 on fii_ifix_position (ticker)"
        )
        logger.debug("Creating index fii_dividend_yeld_ranking_i01")
        cursor.execute(
            "create index fii_dividend_yeld_ranking_i01 on fii_dividend_yeld_ranking (ticker)"
        )
        logger.debug("Creating index fii_indicators_i01")
        cursor.execute(
            "create index fii_indicators_i01 on fii_indicators (ticker)"
        )  # Index added for indicators table
        logger.info(f"Successfully created {5} database indexes")
    except sqlite3.OperationalError as e:
        # Handle cases where index might already exist if run multiple times in same session (though unlikely with :memory:)
        logger.warning(f"Could not create index, it might already exist: {e}")
        print(f"Warning: Could not create index, it might already exist. Error: {e}")


def get_fii_daily_position(parallelize: Optional[bool] = None) -> pd.DataFrame:
    """
    Retrieves the daily consolidated position of FIIs (Fundos de Investimento Imobiliário).

    This function fetches data from multiple sources:
    1. FII payment calendar (Investidor10).
    2. IFIX composition (Fiis.com.br).
    3. FII Dividend Yield ranking (Investidor10).
    4. Detailed indicators for each FII (Investidor10).

    It stores the intermediate data in an in-memory SQLite database, performs joins,
    and returns a comprehensive DataFrame.

    Args:
        parallelize (Optional[bool], optional): Flag to enable/disable parallel processing
            for fetching FII indicators. If None, uses the default value from constants.
            Parallelization requires more than one CPU core. Defaults to None.

    Returns:
        pd.DataFrame: A DataFrame containing the consolidated daily position of FIIs.
            Columns include payment details, IFIX info, ranking data, and detailed indicators.
            Returns an empty DataFrame if a critical data fetching step fails.

    Raises:
        SystemError: If HTTP requests fail for critical data sources.
        AttributeError: If expected HTML elements are not found during scraping.
        sqlite3.Error: If database operations fail.
        Exception: Catches other potential errors during processing.
    """
    should_parallelize = parallelize if parallelize is not None else DEFAULT_PARALLELIZE
    use_multiprocessing = (
        should_parallelize and os.cpu_count() is not None and os.cpu_count() > 1
    )
    logger.info(
        f"get_fii_daily_position(parallelize={parallelize}) -> parallelize={should_parallelize}, use_multiprocessing={use_multiprocessing}"
    )

    # Use in-memory SQLite database
    db: Optional[sqlite3.Connection] = None
    try:
        db = sqlite3.connect(":memory:")
        cursor = db.cursor()

        # --- Fetch and Store Data ---
        print("Fetching FII payment calendar...")
        fii_payments_df = get_fii_all_payment_data(FIIS_PAYMENT_URL)
        if fii_payments_df.empty:
            print(
                "Warning: FII payment data is empty. Resulting DataFrame might be incomplete."
            )
        fii_payments_df.to_sql(
            "fii_payment_calendar", con=db, index=False, if_exists="replace"
        )
        print(f"Stored {len(fii_payments_df)} payment records.")

        print("Fetching IFIX composition...")
        ifix_df = get_ifix_data(IFIX_PAGE_URL)
        if ifix_df.empty:
            print("Warning: IFIX data is empty.")
        ifix_df.to_sql("fii_ifix_position", con=db, index=False, if_exists="replace")
        print(f"Stored {len(ifix_df)} IFIX records.")

        print("Fetching FII DY ranking...")
        ranking_df = get_fii_dy_ranking_data(FIIS_DY_DETAILS_URL)
        if ranking_df.empty:
            print("Warning: FII DY ranking data is empty.")
        ranking_df.to_sql(
            "fii_dividend_yeld_ranking", con=db, index=False, if_exists="replace"
        )
        print(f"Stored {len(ranking_df)} ranking records.")

        # --- Prepare for Indicator Fetching ---
        # Get unique ticker/details pairs from payment data
        fii_info_df = pd.read_sql(
            "SELECT DISTINCT ticker, details FROM fii_payment_calendar WHERE details IS NOT NULL",
            con=db,
        )
        fii_info_df["capture_date"] = CAPTURE_DATE
        # Add sleep parameter placeholder (None initially) for the tuple structure expected by get_fii_indicators
        fii_info_df["sleep"] = None
        fii_info_tuples = tuple(fii_info_df.to_records(index=False))

        print(f"Fetching detailed indicators for {len(fii_info_tuples)} unique FIIs...")
        indicator_results: List[Optional[Dict[str, Any]]] = []

        # --- Fetch Indicators (Parallel or Sequential) ---
        if use_multiprocessing and len(fii_info_tuples) > 0:
            print(f"Using parallel processing with {os.cpu_count()} workers.")
            with Pool(os.cpu_count()) as pool:
                # Pass default sleep time if needed, or let get_fii_indicators handle it
                indicator_results = pool.map(get_fii_indicators, fii_info_tuples)
        elif len(fii_info_tuples) > 0:
            print("Using sequential processing.")
            for info in fii_info_tuples:
                indicator_results.append(get_fii_indicators(info))  # type: ignore # Correct tuple structure
        else:
            print("No FIIs found to fetch indicators for.")

        # Filter out None results (errors during fetching/parsing)
        valid_indicators = [d for d in indicator_results if d is not None]
        print(f"Successfully fetched indicators for {len(valid_indicators)} FIIs.")

        if not valid_indicators:
            print(
                "Warning: No valid FII indicators were fetched. Resulting DataFrame will lack indicator data."
            )
            # Create an empty DataFrame with expected columns to avoid SQL errors
            fii_indicators_df = pd.DataFrame(
                columns=[
                    "ticker",
                    "url",
                    "ref_date",
                    "price",
                    "price_date",
                    "fund_name",
                    "fund_id",
                    "audience",
                    "mandate_type",
                    "segment",
                    "fund_type",
                    "term_type",
                    "management_type",
                    "admin_rate",
                    "vacancy",
                    "shareholders",
                    "shares",
                    "equity_by_share",
                    "equity",
                    "last_payment",
                    "equity_unit",
                ]
            )
        else:
            fii_indicators_df = pd.DataFrame.from_dict(valid_indicators)
            # Rename columns to match SQL query expectations
            fii_indicators_df = fii_indicators_df.rename(
                columns={
                    "PAPEL": "ticker",
                    "URL": "url",
                    "DATA_REFERÊNCIA": "ref_date",
                    "COTAÇÃO": "price",
                    "DATA_COTAÇÃO": "price_date",
                    # Map other keys directly if names match, otherwise add rename rules
                    "NUMERO DE COTISTAS": "shareholders",
                    "COTAS EMITIDAS": "shares",
                    "VAL. PATRIMONIAL P/ COTA": "equity_by_share",
                    "VALOR PATRIMONIAL": "equity",
                    "VALOR PATRIMONIAL UNIT": "equity_unit",
                    "ÚLTIMO RENDIMENTO": "last_payment",
                    "VACÂNCIA": "vacancy",
                    # Add renames for keys that might differ slightly if needed
                    # 'NOME DO FUNDO': 'fund_name', # Example if key was different
                    # 'CNPJ DO FUNDO': 'fund_id', # Example
                }
            )

            # Select and order columns expected by the database table
            expected_indicator_cols = [
                "ticker",
                "url",
                "ref_date",
                "price",
                "price_date",
                "fund_name",
                "fund_id",
                "audience",
                "mandate_type",
                "segment",
                "fund_type",
                "term_type",
                "management_type",
                "admin_rate",
                "vacancy",
                "shareholders",
                "shares",
                "equity_by_share",
                "equity",
                "equity_unit",
                "last_payment",
            ]
            # Ensure all expected columns exist, adding missing ones with None
            for col in expected_indicator_cols:
                if col not in fii_indicators_df.columns:
                    fii_indicators_df[col] = None
            fii_indicators_df = fii_indicators_df[expected_indicator_cols]

        fii_indicators_df.to_sql(
            "fii_indicators", con=db, index=False, if_exists="replace"
        )
        print(f"Stored {len(fii_indicators_df)} indicator records.")

        # --- Create Indexes ---
        print("Creating database indexes...")
        _create_db_indexes(cursor)

        # --- Final Query ---
        print("Executing final join query...")
        final_query = """
            SELECT
                substr(p.payment_date, 1, 4)       as payment_year,
                substr(p.payment_date, 1, 7)       as payment_year_month,
                substr(p.payment_date, 1, 10)      as payment_date,
                substr(p.com_date, 1, 10)          as com_date,
                p.ticker,
                coalesce(f.title, p.name)          as name, -- Use IFIX title if available, else payment name
                i.fund_name,
                i.fund_id,

                coalesce(r.fund_type, i.fund_type) as fund_type, -- Use ranking type if available
                coalesce(r.segment, i.segment)     as segment,   -- Use ranking segment if available
                i.audience,
                i.mandate_type,
                i.term_type,
                i.management_type,
                i.admin_rate,

                p.payment,
                i.price,
                i.price_date,
                CASE
                    WHEN i.price IS NOT NULL AND i.price != 0 -- Avoid division by zero
                    THEN p.payment / i.price
                    ELSE null
                END                                as payment_price_ratio,

                f.share                            as ifix_share,
                r.dy_current,
                r.p_vp,
                r.daily_liquidity,
                r.daily_liquidity_unit,
                r.net_worth,
                r.net_worth_unit,
                r.var_last_12_months,

                i.vacancy,
                i.shareholders,
                i.shares,
                i.equity_by_share,
                i.equity,
                i.equity_unit,
                i.last_payment,

                p.reference_date
            FROM fii_payment_calendar AS p
            LEFT JOIN fii_ifix_position AS f
                ON p.ticker = f.ticker AND date(p.reference_date) = date(f.reference_date) -- Join on date if available
            LEFT JOIN fii_dividend_yeld_ranking AS r
                ON p.ticker = r.ticker AND date(p.reference_date) = date(r.reference_date) -- Join on date
            LEFT JOIN fii_indicators AS i
                ON p.ticker = i.ticker AND date(p.reference_date) = date(i.ref_date) -- Join on date
            -- WHERE substr(p.payment_date, 1, 4) <> '9999' -- Filter out invalid dates if necessary
            ORDER BY p.payment_date, p.ticker
        """
        result_df = pd.read_sql(final_query, con=db)
        print(f"Generated final DataFrame with {len(result_df)} rows.")

        # --- Data Type Conversion for Final DataFrame ---
        date_cols = ["payment_date", "com_date", "price_date", "reference_date"]
        for col in date_cols:
            if col in result_df.columns:
                result_df[col] = pd.to_datetime(result_df[col], errors="coerce").dt.date

        numeric_cols = [
            "payment",
            "price",
            "payment_price_ratio",
            "ifix_share",
            "dy_current",
            "p_vp",
            "daily_liquidity",
            "net_worth",
            "var_last_12_months",
            "vacancy",
            "shareholders",
            "shares",
            "equity_by_share",
            "equity",
            "last_payment",
        ]
        for col in numeric_cols:
            if col in result_df.columns:
                result_df[col] = pd.to_numeric(result_df[col], errors="coerce")

        return result_df

    except (requests.exceptions.RequestException, SystemError, AttributeError) as e:
        print(f"Error during data fetching or parsing: {e}")
        # Return empty DataFrame with expected columns if critical error occurs
        # Define expected columns based on the final SELECT query
        expected_cols = [
            "payment_year",
            "payment_year_month",
            "payment_date",
            "com_date",
            "ticker",
            "name",
            "fund_name",
            "fund_id",
            "fund_type",
            "segment",
            "audience",
            "mandate_type",
            "term_type",
            "management_type",
            "admin_rate",
            "payment",
            "price",
            "price_date",
            "payment_price_ratio",
            "ifix_share",
            "dy_current",
            "p_vp",
            "daily_liquidity",
            "daily_liquidity_unit",
            "net_worth",
            "net_worth_unit",
            "var_last_12_months",
            "vacancy",
            "shareholders",
            "shares",
            "equity_by_share",
            "equity",
            "equity_unit",
            "last_payment",
            "reference_date",
        ]
        return pd.DataFrame(columns=expected_cols)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        # Consider returning empty DF here as well
        expected_cols = [  # Duplicated for clarity in error handling
            "payment_year",
            "payment_year_month",
            "payment_date",
            "com_date",
            "ticker",
            "name",
            "fund_name",
            "fund_id",
            "fund_type",
            "segment",
            "audience",
            "mandate_type",
            "term_type",
            "management_type",
            "admin_rate",
            "payment",
            "price",
            "price_date",
            "payment_price_ratio",
            "ifix_share",
            "dy_current",
            "p_vp",
            "daily_liquidity",
            "daily_liquidity_unit",
            "net_worth",
            "net_worth_unit",
            "var_last_12_months",
            "vacancy",
            "shareholders",
            "shares",
            "equity_by_share",
            "equity",
            "equity_unit",
            "last_payment",
            "reference_date",
        ]
        return pd.DataFrame(columns=expected_cols)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise  # Re-raise unexpected errors
    finally:
        if db:
            db.close()
            print("Database connection closed.")

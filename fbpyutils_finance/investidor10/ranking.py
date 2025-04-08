# fbpyutils_finance/investidor10/ranking.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
from typing import Optional

from .constants import HEADERS, BS4_PARSER, CAPTURE_DATE
from .utils import tag_to_str, any_to_number

def get_fii_dy_ranking_data(fii_dy_details_url: str) -> pd.DataFrame:
    """
    Retrieves and processes the FII (Fundos de Investimento Imobiliário)
    dividend yield (DY) ranking data from the specified Investidor10 URL.

    Args:
        fii_dy_details_url (str): The URL of the Investidor10 FII DY ranking page
                                  (e.g., FIIS_DY_DETAILS_URL from constants).

    Returns:
        pd.DataFrame: A DataFrame containing the DY ranking data with columns:
                      ['ticker', 'dy_current', 'p_vp', 'daily_liquidity',
                       'daily_liquidity_unit', 'net_worth', 'net_worth_unit',
                       'var_last_12_months', 'fund_type', 'segment', 'reference_date'].
                      Returns an empty DataFrame if the table or rows are not found.

    Raises:
        SystemError: If the HTTP request fails.
        AttributeError: If the ranking table ('table#rankigns') is not found.
        ValueError: If number parsing fails for critical fields.
    """
    try:
        dy_page = requests.get(fii_dy_details_url, headers=HEADERS)
        dy_page.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemError(f"HTTP request failed for {fii_dy_details_url}: {e}")

    soup = BeautifulSoup(dy_page.text, BS4_PARSER)

    # Note: The original code used id='rankigns'. Verify if this is correct or a typo for 'rankings'.
    # Using 'rankings' as it's more likely correct. Adjust if needed.
    dy_ranking_table = soup.find('table', id='rankings') # Corrected ID?
    if not dy_ranking_table:
         # Try the original ID if the corrected one fails
         dy_ranking_table = soup.find('table', id='rankigns')
         if not dy_ranking_table:
            raise AttributeError(f"Could not find ranking table with id 'rankings' or 'rankigns' on {fii_dy_details_url}")


    dy_rows = dy_ranking_table.findAll('tr')
    if len(dy_rows) <= 1: # Check if there's more than just the header row
        print(f"Warning: No data rows found in the ranking table on {fii_dy_details_url}. Returning empty DataFrame.")
        return pd.DataFrame(columns=[
            'ticker', 'dy_current', 'p_vp', 'daily_liquidity',
            'daily_liquidity_unit', 'net_worth', 'net_worth_unit',
            'var_last_12_months', 'fund_type', 'segment', 'reference_date'
        ])

    dy_data = []
    # Skip header row (dy_rows[0])
    for dy_row in dy_rows[1:]:
        cells = dy_row.findAll('td')
        # Ensure the row has the expected number of cells
        if len(cells) < 8:
            print(f"Warning: Skipping row due to insufficient cells ({len(cells)} found, expected 8): {dy_row}")
            continue

        try:
            # Unpack cells - adjust indices if table structure changes
            dy_ticker_cell, dy_current_cell, dy_p_vp_cell, dy_daily_liquidity_cell, \
            dy_net_worth_cell, dy_ytd_var_cell, dy_fund_type_cell, dy_segment_cell = cells[:8] # Take first 8

            # --- Data Extraction and Cleaning ---
            dy_ticker = tag_to_str(dy_ticker_cell)

            # Use any_to_number for robust float conversion
            dy_current = any_to_number(tag_to_str(dy_current_cell))
            dy_p_vp = any_to_number(tag_to_str(dy_p_vp_cell))
            dy_ytd_var = any_to_number(tag_to_str(dy_ytd_var_cell)) # Assumes YTD Var is numeric %

            # Handle liquidity and net worth (value + unit)
            liquidity_str = tag_to_str(dy_daily_liquidity_cell)
            liquidity_parts = liquidity_str.split(' ')
            dy_daily_liquidity = any_to_number(liquidity_parts[0]) if liquidity_parts else None
            dy_daily_liquidity_unit = liquidity_parts[1] if len(liquidity_parts) > 1 else None

            net_worth_str = tag_to_str(dy_net_worth_cell)
            net_worth_parts = net_worth_str.split(' ')
            dy_net_worth = any_to_number(net_worth_parts[0]) if net_worth_parts else None
            dy_net_worth_unit = net_worth_parts[1] if len(net_worth_parts) > 1 else None

            dy_fund_type = tag_to_str(dy_fund_type_cell)
            dy_segment = tag_to_str(dy_segment_cell)

            # Append data only if essential fields are present
            if dy_ticker:
                 dy_data.append((
                    dy_ticker, dy_current, dy_p_vp, dy_daily_liquidity, dy_daily_liquidity_unit,
                    dy_net_worth, dy_net_worth_unit, dy_ytd_var, dy_fund_type, dy_segment, CAPTURE_DATE
                ))
            else:
                print(f"Warning: Skipping row due to missing ticker: {dy_row}")


        except (AttributeError, ValueError, IndexError) as e:
            print(f"Warning: Could not parse row in ranking table. Error: {e}. Row: {dy_row}")
            continue # Skip problematic row

    dy_columns = [
        'ticker', 'dy_current', 'p_vp', 'daily_liquidity',
        'daily_liquidity_unit', 'net_worth', 'net_worth_unit',
        'var_last_12_months', 'fund_type', 'segment', 'reference_date'
    ]

    if not dy_data:
         print(f"Warning: No data could be successfully parsed from ranking table on {fii_dy_details_url}. Returning empty DataFrame.")
         return pd.DataFrame(columns=dy_columns)


    ranking_df = pd.DataFrame(dy_data, columns=dy_columns)

    # Ensure correct dtypes
    numeric_cols = ['dy_current', 'p_vp', 'daily_liquidity', 'net_worth', 'var_last_12_months']
    for col in numeric_cols:
        ranking_df[col] = pd.to_numeric(ranking_df[col], errors='coerce')
    ranking_df['reference_date'] = pd.to_datetime(ranking_df['reference_date'], errors='coerce').dt.date


    return ranking_df

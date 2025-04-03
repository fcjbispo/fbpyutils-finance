# fbpyutils_finance/investidor10/ifix.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import Optional

from .constants import HEADERS, BS4_PARSER, CAPTURE_DATE
from .utils import tag_to_str

def get_ifix_data(ifix_page_url: str) -> pd.DataFrame:
    """
    Retrieves IFIX (Índice de Fundos de Investimentos Imobiliários) composition data
    from the specified fiis.com.br URL.

    Args:
        ifix_page_url (str): The URL of the fiis.com.br page containing the IFIX data
                             (e.g., IFIX_PAGE_URL from constants).

    Returns:
        pd.DataFrame: A pandas DataFrame containing the IFIX composition data with columns:
                      ['ticker', 'title', 'share', 'details', 'reference_date'].
                      Returns an empty DataFrame if no data is found or parsing fails.

    Raises:
        SystemError: If the HTTP request fails.
        AttributeError: If expected HTML elements (like the table body) are not found.
    """
    try:
        ifix_page = requests.get(ifix_page_url, headers=HEADERS)
        ifix_page.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        raise SystemError(f"HTTP request failed for {ifix_page_url}: {e}")

    soup = BeautifulSoup(ifix_page.text, BS4_PARSER)
    ifix_table_body = soup.find('tbody')

    if not ifix_table_body:
        raise AttributeError(f"Could not find 'tbody' element on the page: {ifix_page_url}")

    ifix_data = []
    df_columns = ['ticker', 'title', 'share', 'details', 'reference_date']

    # Helper to parse float, handling potential errors
    def parse_share(value_str: str) -> Optional[float]:
        try:
            # Assumes format like 'X,XX%'
            return float(value_str.replace(',', '.').replace('%', '').strip())
        except (ValueError, AttributeError):
            return None # Return None if conversion fails

    for row in ifix_table_body.children:
        if isinstance(row, Tag) and row.name == 'tr': # Process only table row tags
            cells = row.find_all('td')
            if len(cells) < 2: # Expect at least ticker/link and share columns
                continue

            # Find ticker within an anchor tag <a>
            ticker_anchor = cells[0].find('a')
            # Find title within a paragraph tag <p> (often inside the first cell)
            title_tag = cells[0].find('p')
            # Share is usually in the second cell, potentially with class 'fixed-column'
            share_cell = cells[1] # Adjust index if structure differs

            if ticker_anchor and title_tag and share_cell:
                ticker = tag_to_str(ticker_anchor)
                title = tag_to_str(title_tag)
                share_str = tag_to_str(share_cell)
                share = parse_share(share_str)
                details_url = ticker_anchor.get('href') # Get URL from the anchor

                # Ensure details_url is a string
                if isinstance(details_url, Tag): # Should not happen with .get() but check anyway
                    details_url = tag_to_str(details_url)
                elif not isinstance(details_url, str):
                    details_url = None # Set to None if not a string

                if ticker and title and share is not None: # Only append if essential data is valid
                    ifix_data.append((
                        ticker,
                        title,
                        share,
                        details_url,
                        CAPTURE_DATE
                    ))
                else:
                     print(f"Warning: Skipping row due to missing data (Ticker: {ticker}, Title: {title}, Share: {share_str})")


    if not ifix_data:
        print(f"Warning: No valid IFIX data parsed from {ifix_page_url}. Returning empty DataFrame.")
        return pd.DataFrame(columns=df_columns)

    # Create DataFrame with potentially fewer columns if parsing failed for all rows in some aspect
    # However, the append logic ensures we only add rows with the core data.
    ifix_df = pd.DataFrame(ifix_data, columns=df_columns)

    # Ensure correct dtypes
    ifix_df['share'] = pd.to_numeric(ifix_df['share'], errors='coerce')
    ifix_df['reference_date'] = pd.to_datetime(ifix_df['reference_date'], errors='coerce').dt.date

    return ifix_df

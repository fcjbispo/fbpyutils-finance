# fbpyutils_finance/investidor10/payments.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime
from typing import Literal

from .constants import HEADERS, BS4_PARSER, CAPTURE_DATE, MONTHS_PT
from .utils import tag_to_str, any_to_number


def get_fii_all_payment_data(fiis_page_url: str) -> pd.DataFrame:
    """
    Retrieve and process payment data for all FIIs (Fundos de Investimento Imobiliário)
    listed on the payment date page.

    Scrapes the webpage, parses payment information grouped by month and year,
    and returns a structured DataFrame.

    Args:
        fiis_page_url (str): The URL of the FIIs payment date page to scrape
                             (e.g., FIIS_PAYMENT_URL from constants).

    Returns:
        pd.DataFrame: A DataFrame containing the payment data for FIIs with columns:
                      ['ticker', 'name', 'payment', 'com_date', 'payment_date',
                       'details', 'reference_date'].

    Raises:
        SystemError: If the HTTP request to the FIIs page returns a non-200 status code.
        ValueError: If date parsing fails.
        AttributeError: If expected HTML elements are not found.
    """
    fiis_page = requests.get(fiis_page_url, headers=HEADERS)

    if fiis_page.status_code != 200:
        raise SystemError(f'Http Error not 200: {fiis_page.status_code} for URL: {fiis_page_url}')

    soup = BeautifulSoup(fiis_page.text, BS4_PARSER)
    list_content = soup.find('div', attrs={'id': 'list-content'})
    if not list_content:
        raise AttributeError("Could not find 'div' with id 'list-content' on the page.")

    data = []
    current_year = datetime.now().year

    for month_group in list_content.findAll('div', attrs=({'class': 'month-group-payment'})):
        month_name_tag = month_group.find('h3', attrs={'class': 'month-name'})
        if month_name_tag:
            try:
                # Extract year from header like "Janeiro 2024"
                current_year = int(tag_to_str(month_name_tag).split(' ')[-1])
            except (IndexError, ValueError):
                # Fallback or log warning if year parsing fails
                pass # Keep using the previously determined year

        for payment_card in month_group.findAll('div', attrs={'class': 'payment-card'}):
            try:
                payment_day_str = tag_to_str(payment_card.find('div', attrs={'class': 'payment-day'}))
                payment_month_str = tag_to_str(payment_card.find('div', attrs={'class': 'text-center'}))

                payment_day = int(payment_day_str)
                # Find month index (1-based)
                payment_month = MONTHS_PT.index(payment_month_str) + 1

                payment_date = datetime(current_year, payment_month, payment_day).date()

            except (AttributeError, ValueError, IndexError) as e:
                # Log or handle cases where date components are missing/invalid
                print(f"Warning: Could not parse payment date in card. Error: {e}")
                continue # Skip this card

            for payment_row in payment_card.find_all('div', attrs={'class': 'row payment-row'}):
                try:
                    ticker_anchor = payment_row.find('a', attrs={'class': 'fii-ticker'}, href=True)
                    if not ticker_anchor: continue # Skip if no ticker link

                    fii_ticker = tag_to_str(ticker_anchor)
                    fii_details = ticker_anchor['href']
                    # Find the last h4 tag for the name
                    name_tags = payment_row.find_all('h4')
                    fii_name = tag_to_str(name_tags[-1]) if name_tags else 'N/A'

                    p_tags = payment_row.find_all('p')
                    if len(p_tags) < 2: continue # Skip if not enough info

                    # Payment amount (Provento)
                    payment_str = tag_to_str(p_tags[0]).split(' ')[-1] # Expects format "Provento R$ X.XX"
                    fii_pmt = any_to_number(payment_str) # Use robust conversion

                    # COM date (Data COM)
                    com_date_str = p_tags[1].text.split(' ')[-1] # Expects format "Data COM DD/MM/YYYY"
                    fii_com_date = datetime.strptime(com_date_str, '%d/%m/%Y').date()

                    data.append([
                        fii_ticker, fii_name, fii_pmt, fii_com_date, payment_date, fii_details, CAPTURE_DATE
                    ])
                except (AttributeError, ValueError, IndexError, KeyError) as e:
                     # Log or handle cases where row data is missing/invalid
                    print(f"Warning: Could not parse payment row for ticker {fii_ticker if 'fii_ticker' in locals() else 'Unknown'}. Error: {e}")
                    continue # Skip this row

    fii_payment_dates = pd.DataFrame(
        data, columns=['ticker', 'name', 'payment', 'com_date', 'payment_date', 'details', 'reference_date']
    )

    # Ensure correct dtypes
    fii_payment_dates['payment'] = pd.to_numeric(fii_payment_dates['payment'], errors='coerce')
    fii_payment_dates['com_date'] = pd.to_datetime(fii_payment_dates['com_date'], errors='coerce').dt.date
    fii_payment_dates['payment_date'] = pd.to_datetime(fii_payment_dates['payment_date'], errors='coerce').dt.date
    fii_payment_dates['reference_date'] = pd.to_datetime(fii_payment_dates['reference_date'], errors='coerce').dt.date


    return fii_payment_dates


def get_fii_payment_data(fiis_page_url: str, date_type: Literal['com', 'payment']) -> pd.DataFrame:
    """
    Retrieves FII payment data (either 'com' date or 'payment' date based)
    from a specific Investidor10 page (e.g., dividendos/ or dividendos/data_pgto/).

    Args:
        fiis_page_url (str): The URL of the page containing the FII payment data.
        date_type (Literal['com', 'payment']): The type of date the page focuses on.
                                              This determines the column name for the date.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the FII payment data with columns:
                      ['ticker', 'name', 'payment', f'{date_type}_date', 'details', 'reference_date'].

    Raises:
        TypeError: If the provided date_type is not 'com' or 'payment'.
        SystemError: If the HTTP request fails.
        AttributeError: If expected HTML elements are not found.
        ValueError: If date or number parsing fails.
    """
    if date_type not in ('com', 'payment'):
        raise TypeError(f"Invalid date_type: '{date_type}'. Must be 'com' or 'payment'.")

    fiis_page = requests.get(fiis_page_url, headers=HEADERS)

    if fiis_page.status_code != 200:
        raise SystemError(f'Http Error not 200: {fiis_page.status_code} for URL: {fiis_page_url}')

    soup = BeautifulSoup(fiis_page.text, BS4_PARSER)
    # Find the container, adjust if necessary based on actual page structure
    content_div = soup.find('div', attrs={'id': 'list-content'}) # Or a more specific container
    if not content_div:
         raise AttributeError("Could not find the main content container ('div' with id 'list-content').")

    fii_payment_rows = content_div.find_all('div', attrs={'class': 'row payment-row'})
    if not fii_payment_rows:
        print(f"Warning: No payment rows found on {fiis_page_url}. Returning empty DataFrame.")
        # Return empty DataFrame with correct columns if no rows found
        return pd.DataFrame(columns=['ticker', 'name', 'payment', f'{date_type}_date', 'details', 'reference_date'])


    fii_payments = []
    for payment_row in fii_payment_rows:
        try:
            ticker_anchor = payment_row.find('a', attrs={'class': 'fii-ticker'}, href=True)
            if not ticker_anchor: continue

            fii_ticker = tag_to_str(ticker_anchor)
            fii_details = ticker_anchor['href']
            name_tags = payment_row.find_all('h4')
            fii_name = tag_to_str(name_tags[-1]) if name_tags else 'N/A'

            p_tags = payment_row.find_all('p')
            if len(p_tags) < 2: continue

            # Payment amount
            payment_str = tag_to_str(p_tags[0]).split(' ')[-1]
            fii_payment_amount = any_to_number(payment_str)

            # Date (either COM or Payment depending on the page)
            date_str = p_tags[1].text.split(' ')[-1]
            fii_date = datetime.strptime(date_str, '%d/%m/%Y').date()

            fii_payments.append((fii_ticker, fii_name, fii_payment_amount, fii_date, fii_details, CAPTURE_DATE))

        except (AttributeError, ValueError, IndexError, KeyError) as e:
            print(f"Warning: Could not parse payment row for ticker {fii_ticker if 'fii_ticker' in locals() else 'Unknown'}. Error: {e}")
            continue

    fii_payment_dates_df = pd.DataFrame(
        fii_payments, columns=['ticker', 'name', 'payment', f'{date_type}_date', 'details', 'reference_date']
    )

    # Ensure correct dtypes
    fii_payment_dates_df['payment'] = pd.to_numeric(fii_payment_dates_df['payment'], errors='coerce')
    fii_payment_dates_df[f'{date_type}_date'] = pd.to_datetime(fii_payment_dates_df[f'{date_type}_date'], errors='coerce').dt.date
    fii_payment_dates_df['reference_date'] = pd.to_datetime(fii_payment_dates_df['reference_date'], errors='coerce').dt.date


    return fii_payment_dates_df

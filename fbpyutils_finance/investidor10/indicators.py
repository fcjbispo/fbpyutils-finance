# fbpyutils_finance/investidor10/indicators.py
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from typing import Optional, Dict, Tuple, Any, Union

from .constants import HEADERS, BS4_PARSER
from .utils import tag_to_str, any_to_number

def get_fii_indicators(info: Tuple[str, str, Union[datetime.date, str], Optional[float]], default_sleep: float = 0.3) -> Optional[Dict[str, Any]]:
    """
    Retrieves detailed indicators for a specific FII (Fundo de Investimento Imobiliário)
    from its details page on Investidor10.

    Args:
        info (Tuple[str, str, Union[datetime.date, str], Optional[float]]):
            A tuple containing FII information:
            - fii_ticker (str): The FII ticker symbol (e.g., 'MXRF11').
            - fii_details_url (str): The URL of the FII's details page.
            - capture_date (Union[datetime.date, str]): The date when the data is captured.
            - sleep (Optional[float]): Optional sleep time in seconds after the request.
                                       If None, `default_sleep` is used.
        default_sleep (float, optional): Default sleep time if not provided in `info`. Defaults to 0.3.

    Returns:
        Optional[Dict[str, Any]]: A dictionary containing the FII indicators.
            Keys include 'PAPEL', 'URL', 'DATA_REFERÊNCIA', 'COTAÇÃO', 'DATA_COTAÇÃO',
            and other indicators scraped from the page (e.g., 'NUMERO DE COTISTAS',
            'VAL. PATRIMONIAL P/ COTA', 'VACÂNCIA', etc.).
            Returns None if the request fails, parsing errors occur, or essential
            information is missing.

    Raises:
        SystemError: If the HTTP request returns a non-200 status code (and error handling doesn't catch it).
                     Note: The function currently catches general exceptions and returns None.
    """
    sleep_time: Optional[float] = None
    try:
        # Unpack info tuple, handling optional sleep
        if len(info) == 4:
            fii_ticker, fii_details_url, capture_date, sleep_override = info
            sleep_time = sleep_override if sleep_override is not None else default_sleep
        elif len(info) == 3:
            fii_ticker, fii_details_url, capture_date = info
            sleep_time = default_sleep
        else:
            print(f"Warning: Invalid info tuple length ({len(info)}). Expected 3 or 4. Skipping.")
            return None

        # Ensure capture_date is a date object if passed as string
        if isinstance(capture_date, str):
            try:
                capture_date = datetime.strptime(capture_date, '%Y-%m-%d').date()
            except ValueError:
                 print(f"Warning: Invalid capture_date string format for {fii_ticker}. Expected YYYY-MM-DD. Using None.")
                 capture_date = None # Or handle as error

        fii_indicator_data: Dict[str, Any] = {
            'PAPEL': fii_ticker,
            'URL': fii_details_url,
            'DATA_REFERÊNCIA': capture_date
        }

        # --- Make HTTP Request ---
        dt_page = requests.get(fii_details_url, headers=HEADERS)
        dt_page.raise_for_status() # Check for HTTP errors

        # --- Parse HTML ---
        soup = BeautifulSoup(dt_page.text, BS4_PARSER)

        # --- Extract Price and Price Date ---
        cotacao_card = soup.find('div', attrs={'class': '_card cotacao'})
        if not cotacao_card:
            print(f"Warning: Could not find price card for {fii_ticker}. Skipping.")
            return None # Essential info missing

        cotacao_body = cotacao_card.find('div', attrs={'class': '_card-body'})
        price_tag = cotacao_body.find('span') # Assuming price is in a span
        price_date_info = cotacao_body.find('i') # Assuming date info is in an <i> tag's attribute

        if price_tag:
            # Extract price text (e.g., "R$ 10,50") and convert
            fii_price_str = tag_to_str(price_tag).split(' ')[-1]
            fii_indicator_data['COTAÇÃO'] = any_to_number(fii_price_str)
        else:
             fii_indicator_data['COTAÇÃO'] = None
             print(f"Warning: Could not find price value for {fii_ticker}.")


        if price_date_info and 'data-content' in price_date_info.attrs:
            # Extract date string (e.g., "Última atualização em DD/MM/YYYY")
            date_str = price_date_info.attrs['data-content'].split(' ')[-1]
            try:
                fii_indicator_data['DATA_COTAÇÃO'] = datetime.strptime(date_str, '%d/%m/%Y').date()
            except ValueError:
                fii_indicator_data['DATA_COTAÇÃO'] = None
                print(f"Warning: Could not parse price date '{date_str}' for {fii_ticker}.")
        else:
            fii_indicator_data['DATA_COTAÇÃO'] = None
            print(f"Warning: Could not find price date information for {fii_ticker}.")


        # --- Extract Table Indicators ---
        indicators_table = soup.find('div', attrs={'id': 'table-indicators'})
        if indicators_table:
            for cell in indicators_table.findAll('div', attrs={'class': 'cell'}):
                key_tag = cell.find('div', attrs={'class': 'desc'})
                value_tag = cell.find('div', attrs={'class': 'value'})

                if key_tag and value_tag:
                    key = tag_to_str(key_tag.find('span')) # Get text from inner span
                    value_str = tag_to_str(value_tag.find('span')) # Get text from inner span
                    fii_indicator_data[key] = value_str # Store raw string first
                else:
                    # Log if cell structure is unexpected
                    print(f"Warning: Unexpected cell structure in indicators table for {fii_ticker}.")

        else:
            print(f"Warning: Could not find indicators table ('div#table-indicators') for {fii_ticker}.")


        # --- Post-process specific indicators ---
        # Use .get() with default None to avoid KeyErrors if indicators weren't found
        cotistas_str = fii_indicator_data.get('NUMERO DE COTISTAS')
        cotas_str = fii_indicator_data.get('COTAS EMITIDAS')
        val_pat_cota_str = fii_indicator_data.get('VAL. PATRIMONIAL P/ COTA')
        val_pat_str = fii_indicator_data.get('VALOR PATRIMONIAL')
        ult_rend_str = fii_indicator_data.get('ÚLTIMO RENDIMENTO')
        vacancia_str = fii_indicator_data.get('VACÂNCIA')

        # Convert to appropriate types, handling None and potential errors
        num_cotistas = any_to_number(cotistas_str)
        fii_indicator_data['NUMERO DE COTISTAS'] = int(num_cotistas) if num_cotistas is not None else None

        cotas_emitidas = any_to_number(cotas_str)
        fii_indicator_data['COTAS EMITIDAS'] = int(cotas_emitidas) if cotas_emitidas is not None else None

        # Assumes format "R$ XX.XX"
        fii_indicator_data['VAL. PATRIMONIAL P/ COTA'] = any_to_number(
            val_pat_cota_str.split(' ')[-1] if val_pat_cota_str else None
        )

        # Assumes format "R$ XXX.XXX.XXX,XX Bi/Mi"
        if val_pat_str:
            parts = val_pat_str.split(' ')
            if len(parts) >= 3:
                fii_indicator_data['VALOR PATRIMONIAL'] = any_to_number(parts[1]) # The numeric part
                fii_indicator_data['VALOR PATRIMONIAL UNIT'] = parts[2] # The unit (Bi/Mi)
            else:
                 fii_indicator_data['VALOR PATRIMONIAL'] = any_to_number(val_pat_str) # Fallback attempt
                 fii_indicator_data['VALOR PATRIMONIAL UNIT'] = None
        else:
            fii_indicator_data['VALOR PATRIMONIAL'] = None
            fii_indicator_data['VALOR PATRIMONIAL UNIT'] = None


        # Assumes format "R$ X.XX"
        fii_indicator_data['ÚLTIMO RENDIMENTO'] = any_to_number(
            ult_rend_str.split(' ')[-1] if ult_rend_str else None
        )

        fii_indicator_data['VACÂNCIA'] = any_to_number(vacancia_str) # Already handles %

        # --- Optional Sleep ---
        if sleep_time is not None and sleep_time > 0:
            time.sleep(sleep_time)

        return fii_indicator_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching indicators for {fii_ticker if 'fii_ticker' in locals() else 'Unknown'}: {e}")
        return None
    except AttributeError as e:
         print(f"Error parsing HTML for {fii_ticker if 'fii_ticker' in locals() else 'Unknown'}: {e}")
         return None
    except Exception as e:
        # Catch any other unexpected errors during processing
        print(f"Unexpected error processing indicators for {fii_ticker if 'fii_ticker' in locals() else 'Unknown'}: {e}")
        return None

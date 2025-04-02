from fbpyutils import debug

from typing import Dict, Optional
import requests
import datetime
from bs4 import BeautifulSoup

from fbpyutils_finance import numberize # Removed unused MARKET_INFO, first_or_none


# -

def _makeurl(x: str) -> str:
    """
    Build a Bing search URL from query string.

    Args:
        x (str): Search query to convert into URL

    Returns:
        str: Formatted Bing search URL

    Example:
        >>> _makeurl("test query")
        'https://www.bing.com/search?q=test+query&qs=n&form=QBRE&sp=-1'
    """
    q = '+'.join(x.split())
    url = f"https://www.bing.com/search?q={q}&qs=n&form=QBRE&sp=-1"
    return url

def _bingsearch(x: str) -> requests.models.Response:
    """
    Performs a default Bing search using custom headers.

    Args:
        x (str): The search query string

    Returns:
        requests.models.Response: An HTTP response with the HTML page resulting from the search query.
    """
    h = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
    }

    s = requests.Session()
    url = _makeurl(x)
    r = s.get(url, headers=h)

    return r


def stock_price(
    x: str, market: Optional[str] = None
) -> Dict:
    """
    Performs a Bing search for the current price of the supplied ticker.

    Args:
        x (str): The ticker symbol to search for.
        market (Optional[str], optional): The market exchange symbol (e.g., 'BVMF', 'NASDAQ').
                                          If provided, it's used to refine the search. Defaults to None.

    Returns:
        Dict: A dictionary containing the stock price information or an error message.
              On success: {'info': 'STOCK PRICE', 'source': 'BING', 'status': 'SUCCESS',
                           'details': {'market': str, 'ticker': str, 'name': str, 'currency': str,
                                       'price': float, 'variation': None, 'variation_percent': None,
                                       'trend': None, 'position_time': datetime}}
              On error: {'info': 'STOCK PRICE', 'source': 'BING', 'status': 'ERROR',
                         'details': {'error_message': str}}
    """
    result = {
        'info': 'STOCK PRICE',
        'source': 'BING',
        'status': 'SUCCESS',
        'details': {}
    }

    try:
        if not x:
            raise ValueError('Ticker is required')

        token, ticker = 'Cotação', x.upper()

        search = ' '.join([':'.join([market.upper(), ticker]) if market else ticker, token])

        response = _bingsearch(search)

        if response.status_code != 200:
            raise ValueError('Bing Search Fail!')

        soup = BeautifulSoup(response.text, "html.parser")

        step = 'Search: ticker_name, market'
        head = soup.find_all("div" , class_='b_tophbh bgtopwh' )

        element1, element2 = None, None
        for e in head:
            element1 = e.find("h2", class_="b_topTitle")
            if element1:
                break
        for e in head:
            element2 = e.find("div", class_="fin_metadata b_demoteText")
            if element2:
                break

        if all([element1, element2]):
            ticker_name, market, ticker = element1.text, *element2.text.replace(' ', '').split(':')
        else:
            raise ValueError(f'Bing Search Fail on step {step}!')


        step = 'Search: price, currency'
        head = soup.find_all('div', class_='b_tophbb bgtopgr')

        element2, element3 = None, None
        for e in head:
            element1 = e.find('div', class_='fin_quotePrice')
            if element1:
                element2 = element1.find_all('div', class_='b_hPanel')
                if element2:
                    for e1 in element2:
                        element3 = e1.find('span', class_='price_curr')
                        if element3:
                            break

        for e in head:
            element1 = e.find_all('div', id='Finance_Quote')
            if element1:
                for e1 in element1:
                    element2 = e1.find('div', class_="b_focusTextMedium")
                    if element2:
                        break

        if all([element2, element3]):
            price, currency= numberize(element2.text), element3.text
        else:
            raise ValueError(f'Bing Search Fail on step {step}!')


        # step = 'Search: position date'
        # element2 = None
        # for e in head:
        #     element1 = e.find_all('div', class_='fin_metadata b_demoteText')
        #     if element1:
        #         for e1 in element1:
        #             element2 = e1.find('span', class_="fin_lastUpdate")
        #             if element2:
        #                 break
        # if all([element2]):
        #     position_date = element2.text.replace('  ', ' ')
        # else:
        #     raise ValueError(f'Bing Search Fail on step {step}!')

        result['details'] = {
            'market': market,
            'ticker': ticker,
            'name': ticker_name,
            'currency': currency,
            'price': price,
            'variation': None,
            'variation_percent': None,
            'trend': None,
            'position_time':  datetime.datetime.now()
        }
    except Exception as e:
        m =  debug.debug_info(e)
        result['status'] = 'ERROR'
        result['details'] = {
            'error_message': m
        }
    
    return result

# Example usage removed: stock_price('XYLD')

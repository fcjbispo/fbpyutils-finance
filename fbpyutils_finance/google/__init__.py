'''
Google search info provider.
'''
from infobr import core

from fbpyutils.datetime import apply_timezone

from typing import Dict
import requests 
import datetime
from bs4 import BeautifulSoup

_market_info = [
        {
            'region': 'América', 
            'market': 'BVMF', 
            'name': 'B3 - Bolsa de Valores do Brasil e Mercado de balcão', 
            'delay': '15', 
            'timezone': 'America/Sao_Paulo' 
        },
        {'region': 'América', 'market': 'NASDAQ', 'name': 'NASDAQ Last Sale', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
        {'region': 'América', 'market': 'NYSE', 'name': 'NYSE', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
        {'region': 'América', 'market': 'NYSEARCA', 'name': 'NYSE ARCA', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
        {'region': 'América', 'market': 'NYSEAMERICAN', 'name': 'NYSE American', 'delay': 'Em tempo real*', 'timezone': 'America/New_York' },
]

_choose = lambda n, x, y: x[n] if len(x) > n else y

_numberize = lambda x: float(x.replace(".", "").replace(",", "."))

_first_or_none = lambda x: None if len(x) == 0 else x[0]

def _makeurl(x):
    '''
        Build default google search url output.

        x
            The search query string

        Return an string with a full google search url from que search query
    '''
    q = '+'.join(x.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8&num=1&lr=lang_ptBR&hl=pt-BR'
    return url

def _googlesearch(x: str) -> requests.models.Response:
    '''
    Performs a default google search using custom headers.

        x
            The search query string

        Return an http response with the html page resulting from que search query
    '''
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

def exchange_rate(
    x: str, y: str
) -> Dict:
    '''
    Performs a google search for the first currency returning its exchange rate to the second currency.

        x
            The currency from exchange

        y
            The currency to be exchanged

        Return the value for 1 unit of currency from exchanged to currency to
    '''
    
    result = {
        'info': 'EXCHANGE RATE',
        'source': 'GOOGLE',
        'status': 'SUCCESS',
        'details': {}
    }

    try:
        if not all([x, y]):
            raise ValueError('Two currencies are required')

        token, currency_from, currency_to = 'Cotação', x.upper(), y.upper()

        search = ' '.join([currency_from, currency_to, token])

        response = _googlesearch(search)

        soup = BeautifulSoup(response.text, "lxml") 

        head = soup.find_all("span", class_="r0bn4c rQMQod")
        body = soup.find_all("div" , class_='BNeawe iBp4i AP7Wnd' )        

        h, s = set(), set()

        for t in head:
            h.add(t.text)

        for t in body:
            s.add(t.text)

        if not any([h, s]):
            result['status'] = 'NOT FOUND'
            result['details'] = {
                'from': currency_from,
                'to': currency_to,
            }
            return result

        currency_parts = [] if not h else h.pop().split()

        currency = 0 if len(currency_parts) < 1 else int(_numberize(currency_parts[0]))

        currency_name = '' if len(currency_parts) < 2 else ' '.join(currency_parts[1:-1])

        exchange_parts = [] if not s else s.pop().split()

        exchange = 0 if len(exchange_parts) < 1 else _numberize(exchange_parts[0])

        exchange_name = '' if len(exchange_parts) < 2 else ' '.join(exchange_parts[1:])

        if not all([currency, currency_name, exchange, exchange_name]):
            raise ValueError('Unable to parse exchange rate.')

        result['details'] = {
            'from': '{} ({})'.format(currency_from, currency_name),
            'to': '{} ({})'.format(currency_to, exchange_name),
            'unit': currency,
            'exchange_rate': exchange,
        }

    except Exception as e:
        m =  core.debug_info(e)
        result['status'] = 'ERROR'
        result['details'] = {
            'error_message': m
        }

    return result


def stock_price(
    x: str, market: str='BVMF'
) -> Dict:
    '''
    Performs a google search for the supplied ticker in the default market.

        x
            The ticker to search for the current price

        market
            The name for the market on the ticker will be searched. Default=BVMF
            This version supports only Brazilian BVMF market

        Return an standart dict with stock price and info for the ticker supplied
    '''
    
    result = {
        'info': 'STOCK PRICE',
        'source': 'GOOGLE',
        'status': 'SUCCESS',
        'details': {}
    }

    try:
        if not x:
            raise ValueError('Ticker is required')

        market = market or 'BVMF'

        token, ticker, market = 'Preço das ações', x.upper(), market.upper()

        if market not in ['BVMF']:
            raise ValueError('Unsupported market: {}'.format(market))

        search = ' '.join([ticker, market])

        response = _googlesearch(search)

        if response.status_code != 200:
            raise ValueError('Google Search Fail!')

        soup = BeautifulSoup(response.text, "html.parser") 

        # ticker_name
        head = soup.find_all( "div" , class_='kCrYT' )

        ticker_head = set()

        for t in head:
            if token in t.text:
                ticker_head.add(t.text)

        if ticker_head:
            ticker_head_info = ticker_head.pop().split('/')
            ticker_name_out = None if len(ticker_head_info) == 0 else ticker_head_info[0].rstrip()
        else:
            ticker_name_out = None

        if not ticker_name_out:
            raise ValueError('Unable to parse info: {}'.format('Ticker Name'))

        # price, variation, variation_percent, trend_out
        price_info = soup.findAll(name='div', class_="BNeawe iBp4i AP7Wnd")

        try:
            price_out, variation_out, variation_percent_out = map(
                _numberize, 
                price_info[0].text.replace('%', '').replace('(', '').replace(')', '').split(' ')
            )

            variation_percent_out = round(variation_percent_out / 100, 2)
        except Exception as e:
            raise ValueError('Unable to parse info: {}: {}'.format('Price Info', e))

        trend_out = 'NEUTRAL' if variation_out == 0 else ('UP' if variation_out > 0 else 'DOWN')

        # ticker_out, market_out

        ticker_out, market_out = ticker, market
        
        if not all([ticker_out, market_out]):
            raise ValueError('Unable to parse info: {}'.format('Market Info'))

        # date_time_info, currency
        time_currency_info = soup.findAll(name='span', class_="r0bn4c rQMQod")

        date_time_info, currency = time_currency_info[1].text.split(' · ')[:-1]

        currency_out = currency.split()[-1]

        position_date_info = date_time_info.replace('.', '').replace(',', '').split()

        day = None if len(position_date_info) == 0 else str(position_date_info[0])

        month = None if len(position_date_info) < 3 else \
            str(
                [
                    'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
                    'jul', 'ago', 'set', 'out', 'nov', 'dez'
                ].index(position_date_info[2]) + 1).rjust(2, '0')

        year = str(datetime.datetime.today().year)

        time = None if len(position_date_info) < 4 else position_date_info[3]

        if not all([day, month, year, time]):
            raise ValueError('Unable to parse info: {}'.format('Convert position date'))

        date_time_str = '-'.join([year, month, day, time])

        tz = [m['timezone'] for m in _market_info if m['market'] == market]
        tz = _first_or_none(tz)

        if not tz:
            raise ValueError('Unable to parse info: {}'.format('Market Timezone'))

        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d-%H:%M')

        date_time_info = apply_timezone(date_time_obj, tz)

        result['details'] = {
            'market': market_out,
            'ticker': ticker_out,
            'name': ticker_name_out,
            'currency': currency_out,
            'price': price_out,
            'variation': variation_out,
            'variation_percent': variation_percent_out,
            'trend': trend_out,
            'position_time':  date_time_info
        }

    except Exception as e:
        m =  core.debug_info(e)
        result['status'] = 'ERROR'
        result['details'] = {
            'error_message': m
        }

    return result
'''
Tesouro Direto search info provider.
'''
from infobr import core

from fbpyutils.datetime import apply_timezone

import requests, urllib3

from typing import Dict

from datetime import datetime

urllib3.disable_warnings()

def treasury_bonds(x: str=None) -> Dict:
    '''
    List current information from Brazilian Treasury Bonds and the daily market.

        x
            The name of the treasury bond to get info for. Defaults to None.

        Return all the current information for one treasury bond in the current market or all available if no name is given
    '''
    h = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-control': 'no-cache'
    }

    u = "https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json"

    result = {
        'info': 'TREASURY BOND',
        'source': 'TESOURO DIRETO',
        'status': 'SUCCESS',
        'details': {}
    }

    cipher = 'HIGH:!DH:!aNULL'
    r = None

    try:
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += cipher
        try:
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += cipher
        except AttributeError:
            # no pyopenssl support used / needed / available
            pass         

        r = requests.get(u, verify=False, headers=h)

        if not r:
            raise TypeError('All ciphers tryied to negotiate secure connection. No success at all.')

        data = r.json()

        if data.get('responseStatus') != 200:
            raise SystemError('Error getting information from source')

        response_data = data.get('response')

        response_market_data = response_data['TrsrBondMkt']

        response_business_data = response_data['BizSts']

        tz = 'America/Sao_Paulo'

        market_info = {
            'status': 'OPEN' if response_market_data['sts'] == 'Aberto' else 'CLOSED',
            'closing_time': apply_timezone(datetime.fromisoformat(response_market_data['clsgDtTm']), tz),
            'opening_time': apply_timezone(datetime.fromisoformat(response_market_data['opngDtTm']), tz),
            'position_time': apply_timezone(datetime.fromisoformat(response_business_data['dtTm']), tz)
        }

        bonds = [
            {
                'bond_name': b['TrsrBd'].get('nm'),
                'due_date': datetime.fromisoformat(b['TrsrBd'].get('mtrtyDt')),
                'financial_indexer': b['TrsrBd'].get('FinIndxs', {}).get('nm'), 
                'annual_investment_rate': b['TrsrBd'].get('anulInvstmtRate'),
                'annual_redemption_rate': b['TrsrBd'].get('anulRedRate'),
                'isin_code': b['TrsrBd'].get('isinCd'),
                'sell_price': b['TrsrBd'].get('untrRedVal'),
                'sell_price_unit': b['TrsrBd'].get('minRedVal'),
                'buy_price': b['TrsrBd'].get('untrInvstmtVal'),
                'buy_price_unit': b['TrsrBd'].get('minInvstmtAmt'),
                'extended_description': ' '.join([b['TrsrBd'].get('featrs'), b['TrsrBd'].get('invstmtStbl')]).replace('\r\n', '')
            } 
            for b in response_data['TrsrBdTradgList'] if b['TrsrBd'].get('nm', 'NA') == x or x is None
        ]

        if len(bonds) == 0:
            result['status'] = 'NOT FOUND'
            result['details'] = {
                'bond_name': x or 'ALL',
            }
            return result

        result['details'] = {
            'market': market_info,
            'matches': len(bonds),
            'bonds': bonds
        }

    except Exception as e:
        m =  core.debug_info(e)
        result['status'] = 'ERROR'
        result['details'] = {
            'error_message': m
        }

    return result

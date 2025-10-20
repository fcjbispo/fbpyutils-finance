# tests/tesourodireto/test_tesourodireto_treasury_bonds.py
import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime
from fbpyutils_finance.tesourodireto import treasury_bonds
from fbpyutils.datetime import apply_timezone

# Mock data simulating the API response
MOCK_API_RESPONSE_SUCCESS = {
    "responseStatus": 200,
    "response": {
        "TrsrBondMkt": {
            "sts": "Aberto",
            "clsgDtTm": "2025-08-04T18:00:00",
            "opngDtTm": "2025-08-04T09:30:00"
        },
        "BizSts": {
            "dtTm": "2025-08-04T11:30:00"
        },
        "TrsrBdTradgList": [
            {
                "TrsrBd": {
                    "nm": "Tesouro Selic 2027",
                    "mtrtyDt": "2027-03-01T00:00:00",
                    "FinIndxs": {"nm": "SELIC"},
                    "anulInvstmtRate": 0.0015,
                    "anulRedRate": 0.0010,
                    "isinCd": "BRSTNCLF1R39",
                    "untrRedVal": 14000.50,
                    "minRedVal": 140.00,
                    "untrInvstmtVal": 14005.60,
                    "minInvstmtAmt": 140.05,
                    "featrs": "Liquidez diária",
                    "invstmtStbl": "Pós-fixado"
                }
            },
            {
                "TrsrBd": {
                    "nm": "Tesouro Prefixado 2029",
                    "mtrtyDt": "2029-01-01T00:00:00",
                    "FinIndxs": {"nm": "PRE"},
                    "anulInvstmtRate": 0.1150,
                    "anulRedRate": 0.1145,
                    "isinCd": "BRSTNCNTF1Q8",
                    "untrRedVal": 800.20,
                    "minRedVal": 32.00,
                    "untrInvstmtVal": 801.00,
                    "minInvstmtAmt": 32.04,
                    "featrs": "Rentabilidade definida",
                    "invstmtStbl": "Prefixado"
                }
            },
            {
                "TrsrBd": {
                    "nm": "Tesouro IPCA+ 2035",
                    "mtrtyDt": "2035-05-15T00:00:00",
                    "FinIndxs": {"nm": "IPCA"},
                    "anulInvstmtRate": 0.0550,
                    "anulRedRate": 0.0545,
                    "isinCd": "BRSTNCNTB1Z8",
                    "untrRedVal": 3500.75,
                    "minRedVal": 35.00,
                    "untrInvstmtVal": 3505.80,
                    "minInvstmtAmt": 35.05,
                    "featrs": "Proteção contra inflação",
                    "invstmtStbl": "Indexado à inflação"
                }
            }
        ]
    }
}

MOCK_API_RESPONSE_NOT_FOUND = {
    "responseStatus": 200,
    "response": {
        "TrsrBondMkt": {
            "sts": "Fechado",
            "clsgDtTm": "2025-08-04T18:00:00",
            "opngDtTm": "2025-08-05T09:30:00"
        },
        "BizSts": {
            "dtTm": "2025-08-04T19:00:00"
        },
        "TrsrBdTradgList": [] # Empty list simulates not found when filtering
    }
}


MOCK_API_RESPONSE_ERROR_STATUS = {
    "responseStatus": 500,
    "message": "Internal Server Error"
}

TZ = 'America/Sao_Paulo'

EXPECTED_MARKET_INFO_OPEN = {
    'status': 'OPEN',
    'closing_time': apply_timezone(datetime.fromisoformat("2025-08-04T18:00:00"), TZ),
    'opening_time': apply_timezone(datetime.fromisoformat("2025-08-04T09:30:00"), TZ),
    'position_time': apply_timezone(datetime.fromisoformat("2025-08-04T11:30:00"), TZ)
}

EXPECTED_BONDS_ALL = [
    {
        'bond_name': 'Tesouro Selic 2027',
        'due_date': datetime.fromisoformat("2027-03-01T00:00:00"),
        'financial_indexer': 'SELIC',
        'annual_investment_rate': 0.0015,
        'annual_redemption_rate': 0.0010,
        'isin_code': 'BRSTNCLF1R39',
        'sell_price': 14000.50,
        'sell_price_unit': 140.00,
        'buy_price': 14005.60,
        'buy_price_unit': 140.05,
        'extended_description': 'Liquidez diária Pós-fixado'
    },
    {
        'bond_name': 'Tesouro Prefixado 2029',
        'due_date': datetime.fromisoformat("2029-01-01T00:00:00"),
        'financial_indexer': 'PRE',
        'annual_investment_rate': 0.1150,
        'annual_redemption_rate': 0.1145,
        'isin_code': 'BRSTNCNTF1Q8',
        'sell_price': 800.20,
        'sell_price_unit': 32.00,
        'buy_price': 801.00,
        'buy_price_unit': 32.04,
        'extended_description': 'Rentabilidade definida Prefixado'
    },
    {
        'bond_name': 'Tesouro IPCA+ 2035',
        'due_date': datetime.fromisoformat("2035-05-15T00:00:00"),
        'financial_indexer': 'IPCA',
        'annual_investment_rate': 0.0550,
        'annual_redemption_rate': 0.0545,
        'isin_code': 'BRSTNCNTB1Z8',
        'sell_price': 3500.75,
        'sell_price_unit': 35.00,
        'buy_price': 3505.80,
        'buy_price_unit': 35.05,
        'extended_description': 'Proteção contra inflação Indexado à inflação'
    }
]

EXPECTED_BOND_SELIC = [EXPECTED_BONDS_ALL[0]]


@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_success_all(mock_get):
    """
    Test treasury_bonds function for successful retrieval of all bonds.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_API_RESPONSE_SUCCESS
    mock_response.status_code = 200
    # Simulate successful request
    mock_response.__bool__.return_value = True
    mock_get.return_value = mock_response

    result = treasury_bonds()

    assert result['status'] == 'SUCCESS'
    assert result['info'] == 'TREASURY BOND'
    assert result['source'] == 'TESOURO DIRETO'
    assert result['details']['market'] == EXPECTED_MARKET_INFO_OPEN
    assert result['details']['matches'] == 3
    assert result['details']['bonds'] == EXPECTED_BONDS_ALL
    mock_get.assert_called_once()


@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_success_specific(mock_get):
    """
    Test treasury_bonds function for successful retrieval of a specific bond.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_API_RESPONSE_SUCCESS
    mock_response.status_code = 200
    mock_response.__bool__.return_value = True
    mock_get.return_value = mock_response

    bond_name_to_find = "Tesouro Selic 2027"
    result = treasury_bonds(x=bond_name_to_find)

    assert result['status'] == 'SUCCESS'
    assert result['details']['market'] == EXPECTED_MARKET_INFO_OPEN
    assert result['details']['matches'] == 1
    assert result['details']['bonds'] == EXPECTED_BOND_SELIC
    mock_get.assert_called_once()


@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_not_found(mock_get):
    """
    Test treasury_bonds function when a specific bond name is not found.
    """
    mock_response = MagicMock()
    # Use success response but filter will result in empty list
    mock_response.json.return_value = MOCK_API_RESPONSE_SUCCESS
    mock_response.status_code = 200
    mock_response.__bool__.return_value = True
    mock_get.return_value = mock_response

    bond_name_to_find = "Tesouro Inexistente 2040"
    result = treasury_bonds(x=bond_name_to_find)

    assert result['status'] == 'NOT FOUND'
    assert result['details']['bond_name'] == bond_name_to_find
    assert 'market' not in result['details']
    assert 'matches' not in result['details']
    assert 'bonds' not in result['details']
    mock_get.assert_called_once()

@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_not_found_empty_list_from_api(mock_get):
    """
    Test treasury_bonds function when the API returns an empty list of bonds.
    """
    mock_response = MagicMock()
    # Use a response where TrsrBdTradgList is empty
    mock_response.json.return_value = MOCK_API_RESPONSE_NOT_FOUND
    mock_response.status_code = 200
    mock_response.__bool__.return_value = True
    mock_get.return_value = mock_response

    result = treasury_bonds(x=None) # Requesting all bonds

    assert result['status'] == 'NOT FOUND'
    assert result['details']['bond_name'] == 'ALL'
    assert 'market' not in result['details']
    assert 'matches' not in result['details']
    assert 'bonds' not in result['details']
    mock_get.assert_called_once()


@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_request_error_status(mock_get):
    """
    Test treasury_bonds function when the API returns an error status code.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_API_RESPONSE_ERROR_STATUS
    mock_response.status_code = 500 # Simulate server error
    mock_response.__bool__.return_value = True # Request itself succeeded
    mock_get.return_value = mock_response

    result = treasury_bonds()

    assert result['status'] == 'ERROR'
    assert 'error_message' in result['details']
    # Check if the error message contains the expected SystemError text
    assert 'Error getting information from source' in result['details']['error_message']
    mock_get.assert_called_once()


@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_request_failure(mock_get):
    """
    Test treasury_bonds function when the requests.get call fails (returns None/False).
    """
    # Simulate requests.get returning None or a False-like object
    mock_get.return_value = None

    result = treasury_bonds()

    assert result['status'] == 'ERROR'
    assert 'error_message' in result['details']
    # Check if the error message contains the expected TypeError text
    assert 'All ciphers tryied to negotiate secure connection' in result['details']['error_message']
    mock_get.assert_called_once()


@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_exception_during_processing(mock_get):
    """
    Test treasury_bonds function when an unexpected exception occurs during processing.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_API_RESPONSE_SUCCESS
    mock_response.status_code = 200
    mock_response.__bool__.return_value = True
    mock_get.return_value = mock_response

    # Patch datetime.fromisoformat to raise an exception
    # We need to patch it within the target module's namespace
    with patch('fbpyutils_finance.tesourodireto.datetime') as mock_datetime_in_module:
        # Configure the mock datetime object within the module
        mock_datetime_in_module.fromisoformat.side_effect = ValueError("Invalid date format")
        # Ensure other datetime attributes/methods used (like the class itself for isinstance checks, etc.) are retained
        mock_datetime_in_module.now.return_value = datetime.now() # Example if now() was used
        mock_datetime_in_module.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs) # Allow creating datetime objects


        result = treasury_bonds()

        assert result['status'] == 'ERROR'
        assert 'error_message' in result['details']
        # The error message comes from fbpyutils.debug.debug_info(e)
        # We expect the original exception type and message to be part of it.
        assert 'ValueError' in result['details']['error_message']
        assert 'Invalid date format' in result['details']['error_message']

    mock_get.assert_called_once()

@patch('fbpyutils_finance.tesourodireto.requests.get')
def test_treasury_bonds_market_closed(mock_get):
    """
    Test treasury_bonds function when the market status is 'CLOSED'.
    """
    # Create a deep copy to avoid modifying the original mock data
    import copy
    closed_response = copy.deepcopy(MOCK_API_RESPONSE_SUCCESS)
    closed_response['response']['TrsrBondMkt']['sts'] = 'Fechado' # Change status to Closed

    mock_response = MagicMock()
    mock_response.json.return_value = closed_response
    mock_response.status_code = 200
    mock_response.__bool__.return_value = True
    mock_get.return_value = mock_response

    result = treasury_bonds()

    assert result['status'] == 'SUCCESS'
    assert result['details']['market']['status'] == 'CLOSED'
    assert result['details']['matches'] == 3 # Should still find bonds even if market is closed
    mock_get.assert_called_once()

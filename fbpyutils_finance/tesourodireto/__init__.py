"""
fbpyutils_finance.tesourodireto - Tesouro Direto (Brazilian Treasury Bonds) Info Provider

Purpose: This module provides functionality to retrieve information about Brazilian Treasury Bonds (Tesouro Direto) including bond details, rates, market status, and pricing information.

Main contents:
- treasury_bonds() (function): Retrieve information about treasury bonds from Tesouro Direto API

High-level usage pattern:
Import treasury_bonds and call it with specific bond names or without parameters to get information about available Brazilian treasury bonds.

Examples:
>>> from fbpyutils_finance.tesourodireto import treasury_bonds
>>> bonds = treasury_bonds()
>>> bonds['status']
'SUCCESS'
>>> # Get specific bond
>>> bond = treasury_bonds('Tesouro IPCA+ 2035')
>>> isinstance(bond['details']['bonds'], list)
True
"""

import requests
import urllib3

from fbpyutils import debug
from fbpyutils.datetime import apply_timezone

from typing import Dict
from datetime import datetime

from fbpyutils_finance import logger

urllib3.disable_warnings()


def treasury_bonds(x: str = None) -> Dict:
    """
    Retrieve information about treasury bonds from a specific source.

    Args:
        x (str, optional): The name of the bond to retrieve information for. If not provided, information for all bonds is retrieved.

    Returns:
        Dict: A dictionary containing information about the treasury bonds.
            - 'info' (str): Information about the type of bonds ('TREASURY BOND').
            - 'source' (str): The source of the bond information ('TESOURO DIRETO').
            - 'status' (str): The status of the retrieval process ('SUCCESS', 'NOT FOUND', or 'ERROR').
            - 'details' (Dict): Additional details about the bonds.
                - 'market' (Dict): Information about the market status and timings.
                - 'matches' (int): The number of bonds that match the provided name (if any).
                - 'bonds' (List[Dict]): A list of dictionaries containing information about the matching bonds.

    Raises:
        TypeError: If all ciphers fail to negotiate a secure connection.
        SystemError: If there is an error getting information from the source.

    Examples:
        >>> bonds = treasury_bonds()
        >>> bonds['status'] in ['SUCCESS', 'NOT FOUND', 'ERROR']
        True
        >>> # Get specific bond
        >>> bond_info = treasury_bonds('Tesouro IPCA+ 2035')
        >>> 'bonds' in bond_info['details']
        True
        >>> isinstance(bond_info['details']['bonds'], list)
        True
    """
    logger.info(f"treasury_bonds(x='{x}')")
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-control": "no-cache",
    }

    u = "https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json"
    logger.debug(f"Treasury API URL: {u}")

    result = {
        "info": "TREASURY BOND",
        "source": "TESOURO DIRETO",
        "status": "SUCCESS",
        "details": {},
    }

    cipher = "HIGH:!DH:!aNULL"
    r = None

    try:
        logger.debug("Making request to Tesouro Direto API")
        r = requests.get(u, verify=False, headers=h)

        if not r:
            logger.error("All cipher negotiations failed")
            raise TypeError(
                "All ciphers tryied to negotiate secure connection. No success at all."
            )

        logger.debug(f"API response status: {r.status_code}")
        data = r.json()

        if data.get("responseStatus") != 200:
            logger.error(f"API returned non-200 status: {data.get('responseStatus')}")
            raise SystemError("Error getting information from source")

        response_data = data.get("response")
        logger.debug("Successfully parsed JSON response")

        response_market_data = response_data["TrsrBondMkt"]

        response_business_data = response_data["BizSts"]

        tz = "America/Sao_Paulo"

        market_info = {
            "status": "OPEN" if response_market_data["sts"] == "Aberto" else "CLOSED",
            "closing_time": apply_timezone(
                datetime.fromisoformat(response_market_data["clsgDtTm"]), tz
            ),
            "opening_time": apply_timezone(
                datetime.fromisoformat(response_market_data["opngDtTm"]), tz
            ),
            "position_time": apply_timezone(
                datetime.fromisoformat(response_business_data["dtTm"]), tz
            ),
        }
        logger.debug(f"Market info: {market_info}")

        bonds = [
            {
                "bond_name": b.get("TrsrBd", {}).get("nm"),
                "due_date": datetime.fromisoformat(b.get("TrsrBd", {}).get("mtrtyDt")),
                "financial_indexer": b.get("TrsrBd", {}).get("FinIndxs", {}).get("nm"),
                "annual_investment_rate": b.get("TrsrBd", {}).get("anulInvstmtRate"),
                "annual_redemption_rate": b.get("TrsrBd", {}).get("anulRedRate"),
                "isin_code": b.get("TrsrBd", {}).get("isinCd"),
                "sell_price": b.get("TrsrBd", {}).get("untrRedVal"),
                "sell_price_unit": b.get("TrsrBd", {}).get("minRedVal"),
                "buy_price": b.get("TrsrBd", {}).get("untrInvstmtVal"),
                "buy_price_unit": b.get("TrsrBd", {}).get("minInvstmtAmt"),
                "extended_description": " ".join(
                    [
                        str(b.get("TrsrBd", {}).get("featrs", "NA")),
                        str(b.get("TrsrBd", {}).get("invstmtStbl", "NA")),
                    ]
                )
                .replace("\r\n", "")
                .replace("NoneType", "NA"),
            }
            for b in response_data.get("TrsrBdTradgList", {})
            if b and (b.get("TrsrBd", {}).get("nm", "NA") == x or x is None)
        ]
        logger.debug(f"Found {len(bonds)} bonds matching criteria")

        if len(bonds) == 0:
            logger.warning(f"No bonds found matching: {x or 'ALL'}")
            result["status"] = "NOT FOUND"
            result["details"] = {
                "bond_name": x or "ALL",
            }
            logger.info("treasury_bonds() -> NOT FOUND")
            return result

        result["details"] = {
            "market": market_info,
            "matches": len(bonds),
            "bonds": bonds,
        }
        logger.info(f"treasury_bonds() -> SUCCESS: found {len(bonds)} bonds")

    except Exception as e:
        logger.error(f"Error retrieving treasury bonds: {e}", exc_info=True)
        m = debug.debug_info(e)
        result["status"] = "ERROR"
        result["details"] = {"error_message": m}

    return result

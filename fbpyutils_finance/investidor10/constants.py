# fbpyutils_finance/investidor10/constants.py
from datetime import datetime

# Configuration
PARALLELIZE: bool = True  # Flag to enable/disable parallel processing
BS4_PARSER: str = 'lxml'  # HTML parser for BeautifulSoup

# HTTP Headers
HEADERS: dict[str, str] = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'
}

# URLs for Investidor10 and Fiis.com.br
FIIS_COM_URL: str = 'https://investidor10.com.br/fiis/dividendos/'
FIIS_PAYMENT_URL: str = 'https://investidor10.com.br/fiis/dividendos/data_pgto/'
FIIS_DY_DETAILS_URL: str = 'https://investidor10.com.br/fiis/rankings/maior-dividend-yield/'
IFIX_PAGE_URL: str = "https://fiis.com.br/ifix/"

# Data Capture Date
CAPTURE_DATE: datetime.date = datetime.now().date()

# Month names in Portuguese for date parsing
MONTHS_PT: list[str] = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

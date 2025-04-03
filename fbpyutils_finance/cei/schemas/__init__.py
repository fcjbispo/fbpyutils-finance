# fbpyutils_finance/cei/schemas/__init__.py
"""
This package provides functions to process different types of CEI (Canal Eletrônico do Investidor)
Excel report files, converting them into standardized pandas DataFrames.
"""

# Import processing functions from submodules to expose them at the package level
from .movimentacao import process_schema_movimentacao
from .eventos_provisionados import process_schema_eventos_provisionados
from .negociacao import process_schema_negociacao
from .posicao_acoes import process_schema_posicao_acoes
from .posicao_emprestimo_ativos import process_schema_posicao_emprestimo_ativos
from .posicao_etf import process_schema_posicao_etf
from .posicao_fundos_investimento import process_schema_posicao_fundos_investimento
from .posicao_tesouro_direto import process_schema_posicao_tesouro_direto
from .posicao_renda_fixa import process_schema_posicao_renda_fixa

# Define __all__ to control what `from fbpyutils_finance.cei.schemas import *` imports
__all__ = [
    "process_schema_movimentacao",
    "process_schema_eventos_provisionados",
    "process_schema_negociacao",
    "process_schema_posicao_acoes",
    "process_schema_posicao_emprestimo_ativos",
    "process_schema_posicao_etf",
    "process_schema_posicao_fundos_investimento",
    "process_schema_posicao_tesouro_direto",
    "process_schema_posicao_renda_fixa",
]

# Note: The utility functions (_deal_double_spaces, _extract_file_info, etc.)
# are now internal to the submodules or within utils.py and are not exposed here.
# The warnings.simplefilter("ignore") has been removed as it might hide useful warnings.
# Individual functions handle errors and print warnings/errors as needed.

"""
fbpyutils_finance.cei.schemas - CEI Schema Processing Package

Purpose: This package provides functions to process different types of CEI (Canal Eletrônico do Investidor)
Excel report files, converting them into standardized pandas DataFrames using schema-specific processors.

Main contents:
- process_schema_movimentacao (function): Process stock movement records
- process_schema_eventos_provisionados (function): Process provisioned events
- process_schema_negociacao (function): Process negotiation records
- process_schema_posicao_acoes (function): Process stock position statements
- process_schema_posicao_emprestimo_ativos (function): Process active loan position statements
- process_schema_posicao_etf (function): Process ETF position statements
- process_schema_posicao_fundos_investimento (function): Process investment fund position statements
- process_schema_posicao_tesouro_direto (function): Process treasury direct position statements
- process_schema_posicao_renda_fixa (function): Process fixed income position statements

High-level usage pattern:
Import individual schema processors and call them with lists of Excel file paths to get processed DataFrames.

Examples:
>>> from fbpyutils_finance.cei.schemas import process_schema_movimentacao
>>> data = process_schema_movimentacao(['movimentacao-2023.xlsx'])
>>> isinstance(data, pd.DataFrame)
True
>>> from fbpyutils_finance.cei import schemas
>>> dir(schemas)
[..., 'process_schema_movimentacao', 'process_schema_negociacao', ...]
"""

# Import processing functions from submodules to expose them at the package level
from fbpyutils_finance import logger
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

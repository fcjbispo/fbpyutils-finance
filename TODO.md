# TODO List - fbpyutils-finance

This file tracks the development status and testing coverage of the `fbpyutils-finance` package based on `DOC.md` and `coverage.xml`.

**Overall Test Coverage:** 71.09% (Target: >= 90%) - **NEEDS IMPROVEMENT**

---

## Core Functions (`fbpyutils_finance/__init__.py`)

*   **Initialized:** Yes
*   **Implemented:** Yes (Interest Rate Conversions, Stock Calculations, Investment Analysis)
*   **Tested:** Yes (Coverage: 99%)
*   **Status:** OK

## Utilities (`fbpyutils_finance/utils.py`)

*   **Initialized:** Yes
*   **Implemented:** Yes (random_header, is_valid_db_connection, numberize, first_or_none)
*   **Tested:** Partial (Coverage: 72.73%)
*   **Status:** **NEEDS MORE TESTS**

## Module: `bing`

*   **Initialized:** Yes
*   **Implemented:** Yes (stock_price)
*   **Tested:** Yes (Coverage: 98.55%)
*   **Status:** OK

## Module: `bovespa`

*   **Initialized:** Yes
*   **Implemented:** Yes (FetchModes, StockHistory, get_stock_history, etc.)
*   **Tested:** Yes (Coverage: 100%)
*   **Status:** OK

## Module: `cei`

*   **Initialized:** Yes
*   **Implemented:** Yes (get_cei_data)
*   **Tested:** Yes (Coverage: 100%)
*   **Status:** OK

## Module: `cei.schemas`

*   **Initialized:** Yes
*   **Implemented:** Yes (Processing logic for various CEI report types)
*   **Tested:** Partial (Overall: 78.6%)
    *   `eventos_provisionados.py`: 80.36%
    *   `movimentacao.py`: 85.71%
    *   `negociacao.py`: 83.67%
    *   `posicao_acoes.py`: 77.46%
    *   `posicao_emprestimo_ativos.py`: 79.75%
    *   `posicao_etf.py`: 75.76%
    *   `posicao_fundos_investimento.py`: 76.12%
    *   `posicao_renda_fixa.py`: 77.78%
    *   `posicao_tesouro_direto.py`: 76.81%
    *   `utils.py`: 71.93%
*   **Status:** **NEEDS MORE TESTS** (All schema files require improved coverage)

## Module: `cvm`

*   **Initialized:** Yes
*   **Implemented:** Yes (CVM class, catalog management, file fetching/processing)
*   **Tested:** Partial (Overall: 51.78%) - **VERY LOW COVERAGE**
    *   `__init__.py`: 82.86%
    *   `converters.py`: 82.64%
    *   `cvm_client.py`: 36.69% (**Critical**)
    *   `file_io.py`: 59.2% (**Critical**)
    *   `headers.py`: 40.2% (**Critical**)
    *   `processing.py`: 78.82%
    *   `remote.py`: 36.78% (**Critical**)
    *   `utils.py`: 90.48% (OK)
*   **Status:** **NEEDS SIGNIFICANTLY MORE TESTS** (Focus on `cvm_client`, `headers`, `remote`, `file_io`)

## Module: `google`

*   **Initialized:** Yes
*   **Implemented:** Yes (exchange_rate, stock_price via scraping)
*   **Tested:** Partial (Coverage: 59.13%)
*   **Status:** **NEEDS MORE TESTS**

## Module: `investidor10`

*   **Initialized:** Yes
*   **Implemented:** Yes (get_fii_daily_position via scraping)
*   **Tested:** Partial (Overall: 80.57%)
    *   `__init__.py`: 78.64%
    *   `constants.py`: 100% (OK)
    *   `ifix.py`: 81.48%
    *   `indicators.py`: 74.74%
    *   `payments.py`: 82.47%
    *   `ranking.py`: 80.00%
    *   `utils.py`: 91.18% (OK)
*   **Status:** **NEEDS MORE TESTS** (Focus on `__init__`, `indicators`, `ifix`, `payments`, `ranking`)

## Module: `tesourodireto`

*   **Initialized:** Yes
*   **Implemented:** Yes (treasury_bonds via API)
*   **Tested:** Yes (Coverage: 100%)
*   **Status:** OK

## Module: `yahoo`

*   **Initialized:** Yes
*   **Implemented:** Yes (YahooCurrencyDataProvider, YahooStockDataProvider, stock_price via scraping)
*   **Tested:** Yes (Coverage: 94.26%)
*   **Status:** OK

---

**Summary of Actions Needed:**

1.  **Increase Test Coverage:** Prioritize adding tests for modules with coverage below 90%, especially `cvm`, `google`, `cei.schemas`, `investidor10`, and `fbpyutils_finance.utils`.
2.  **Refactor `cvm`:** Consider refactoring the `cvm` module to improve testability, given the very low coverage in critical components.
3.  **Review Scraping Modules:** Modules relying on web scraping (`google`, `investidor10`, parts of `yahoo` and `bing`) might need updates if website structures change. Ensure tests mock external calls effectively.

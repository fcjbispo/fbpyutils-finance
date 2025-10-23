import pytest
from datetime import date
from fbpyutils_finance.cei.schemas.utils import deal_double_spaces, extract_file_info, extract_product_id

def test_deal_double_spaces_removes_extra_spaces():
    assert deal_double_spaces("A  B   C") == "A B C"
    assert deal_double_spaces("NoDoubleSpaces") == "NoDoubleSpaces"
    assert deal_double_spaces("  Leading and  trailing  ") == " Leading and trailing "

def test_extract_file_info_valid_formats():
    # movimentacao-2024-01-01.xlsx
    ftype, fdate = extract_file_info("some/path/movimentacao-2024-01-01.xlsx")
    assert ftype.endswith("movimentacao")
    assert isinstance(fdate, date)
    assert fdate.year == 2024

    # posicao-2024-01-01-12-30-45.xlsx
    ftype, fdate = extract_file_info("posicao-2024-01-01-12-30-45.xlsx")
    assert ftype == "posicao"
    assert isinstance(fdate, date)
    assert fdate.year == 2024

    # prefix-2024-01-01-a-2024-01-31.xlsx
    ftype, fdate = extract_file_info("prefix-2024-01-01-a-2024-01-31.xlsx")
    assert isinstance(fdate, date)

def test_extract_file_info_invalid_format():
    with pytest.raises(ValueError):
        extract_file_info("invalidfile.xlsx")

def test_extract_product_id_tesouro():
    assert extract_product_id("Tesouro Selic 2025") == "Tesouro Selic 2025"

def test_extract_product_id_with_separator():
    assert extract_product_id("Empresa XYZ - XYZW4") == "XYZW4"
    assert extract_product_id("Futuro - ABCZ9") == "ABCZ9"

def test_extract_product_id_no_separator():
    assert extract_product_id("XYZW4") == "XYZW4"
    assert extract_product_id("Some Product") == "Some Product"

def test_extract_product_id_non_string():
    assert extract_product_id(12345) == ""

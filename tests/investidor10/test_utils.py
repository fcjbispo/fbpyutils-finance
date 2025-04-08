import pytest
from fbpyutils_finance.investidor10 import utils

def test_tag_to_str_with_tag():
    from bs4 import BeautifulSoup
    html = "<p> Test\nText </p>"
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find('p')
    assert utils.tag_to_str(tag) == "TestText"

def test_tag_to_str_with_string():
    assert utils.tag_to_str(" Some\nString ") == "SomeString"

@pytest.mark.parametrize("input_value,expected", [
    ("R$ 1.234,56", 1234.56),
    ("1.234,56 %", 1234.56),
    ("1234.56", 1234.56),
    ("-", None),
    ("", None),
    ("R$ -", None),
    ("R$ 0,00", 0.0),
    ("R$ 12.345", 12345.0),
    ("R$ 12,34", 12.34),
    ("12,34", 12.34),
    ("12.34", 12.34),
    ("R$ 1.234", 1234.0),
    (None, None),
])
def test_any_to_number(input_value, expected):
    assert utils.any_to_number(input_value) == expected

import pytest

from issue_soup.color import IllegalHexArgumentException
from issue_soup.color import parse_hex


@pytest.mark.parametrize("test_input,expected", [
    ("ffffff", "#FFFFFF"),
    ("aBaaCD", "#ABAACD"),
    ("ddd", "#DDDDDD"),
    ("bab", "#BBAABB"),
    ("123123", "#123123"),
    ("112233", "#112233"),
    ("910", "#991100"),
    ("123", "#112233"),
])
def test_parse_hex(test_input, expected):
    assert parse_hex(test_input) == expected


@pytest.mark.parametrize("test_input,expected_exception", [
    ("aa", IllegalHexArgumentException),
    ("aaaaaaa", IllegalHexArgumentException),
    ("a", IllegalHexArgumentException),
    ("aaaaaaaaa", IllegalHexArgumentException),
    ("foobar", IllegalHexArgumentException),
    ("\naaabb", IllegalHexArgumentException),
])
def test_parse_hex_raise_exceptions(test_input, expected_exception):
    with pytest.raises(expected_exception):
        parse_hex(test_input)

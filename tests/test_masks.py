from src.masks import get_mask_account
from src.masks import get_mask_card_number
import pytest


@pytest.mark.parametrize('value, expected', [("73654108430135874305", "**4305"),
                                             ("35383033474447895560", "**5560"),
                                             ("64686473678894779589", "**9589")])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize('value, expected', [("7000792289606361", "7000 79** **** 6361"),
                                             ("8990922113665229", "8990 92** **** 5229"),
                                             ("5999414228426353", "5999 41** **** 6353")])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

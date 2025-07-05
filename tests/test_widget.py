from src.widget import mask_account_card
from src.widget import get_date
import pytest


@pytest.mark.parametrize("input_list, expected_output", [
    (["Visa Classic 1234 5678 9012 3456"], "Visa Classic 1234 56** **** 3456"),
    (["Ваш счет №12345678901234567890"], "Счет **** **** **** **** 7890"),
])
def test_type_recognition_and_masking(input_list, expected_output: [str]) -> None:
    result = mask_account_card(input_list)
    assert result == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    (["MasterCard 1234 5678 9012 3456"], "MasterCard 1234 56** **** 3456"),
    (["Счет №11112222333344445555"], "Счет **** **** **** **** 5555"),
])
def test_various_formats(input_list, expected_output):
    result = mask_account_card(input_list)
    assert result == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    (["Visa   Gold   1234   5678   9012   3456"], "Visa   Gold   1234 56** **** 3456"),
])
def test_input_with_extra_spaces(input_list, expected_output):
    result = mask_account_card(input_list)
    assert result == expected_output


@pytest.mark.parametrize("invalid_input", [
    [],
    ["Только название без номера"],
    ["Некорректный счет №abcde"],
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(Exception):
        mask_account_card(invalid_input)

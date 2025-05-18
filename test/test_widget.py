import pytest

from scr.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_info, expected_card_info",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(card_info: str, expected_card_info: str) -> None:
    assert mask_account_card(card_info) == expected_card_info


def test_mask_account_card_incorrect_check(incorrect_check: str) -> None:
    assert mask_account_card("Счёт 12312312312131223sd3") == incorrect_check


def test_mask_account_card_empty_data(empty_data: str) -> None:
    assert mask_account_card("") == empty_data


@pytest.mark.parametrize(
    "full_date, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-12-12T02:26:18.6714077", "12.12.2022"),
    ],
)
def test_get_date(full_date: str, expected_date: str) -> None:
    assert get_date(full_date) == expected_date


@pytest.mark.parametrize(
    "full_date_2, incorrect_date",
    [
        ("2024-03-11B02:26:18.671407", "Неверный формат даты"),
        ("2024-1-11B02:26:18.671407", "Неверный формат даты"),
        (" ", "Неверный формат даты"),
    ],
)
def test_get_date_incorrect(full_date_2: str, incorrect_date: str) -> None:
    assert get_date(full_date_2) == incorrect_date

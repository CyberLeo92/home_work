import pytest
from scr.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected_card", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1231231231123123123", "Введен неверный номер карты"),
    ("1231231231123sd3", "Введен неверный номер карты"),
    (" ", "Введен неверный номер карты")
])
def test_get_mask_card_number(card_number, expected_card):
    assert get_mask_card_number(card_number) == expected_card


@pytest.mark.parametrize("account_number, expected_acc", [
    ("73654108430135874305", "**4305"),
    ("1231234784dsaa494000", "Введен неверный номер счёта"),
    ("2173u1892a123", "Введен неверный номер счёта"),
    (" ", "Введен неверный номер счёта")
])
def test_get_mask_account(account_number, expected_acc):
    assert get_mask_account(account_number) == expected_acc

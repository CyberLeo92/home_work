import pytest

from scr.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("4484871238190252", "4484 87** **** 0252"),
    ],
)
def test_get_mask_card_number(card_number: str, expected_card: str) -> None:
    assert get_mask_card_number(card_number) == expected_card


def test_get_mask_incorrect_card(incorrect_card: str) -> None:
    assert get_mask_card_number("1231231231123sd3") == incorrect_card
    assert get_mask_card_number("1231231231123123123") == incorrect_card
    assert get_mask_card_number("") == incorrect_card


@pytest.mark.parametrize(
    "account_number, expected_acc",
    [
        ("73654108430135874305", "**4305"),
        ("18238123718932913455", "**3455"),
    ],
)
def test_get_mask_account(account_number: str, expected_acc: str) -> None:
    assert get_mask_account(account_number) == expected_acc


def test_get_mask_incorrect_account(incorrect_check: str) -> None:
    assert get_mask_account("1231234784dsaa494000") == incorrect_check
    assert get_mask_account("2173u1892a123") == incorrect_check
    assert get_mask_account(" ") == incorrect_check

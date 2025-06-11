import json
from unittest import mock

import pytest

from scr.utils import financial_transaction_data


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="invalid json")
@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load: str, mock_open: str) -> None:
    result = financial_transaction_data("fake_path.json")
    assert result == []


def test_get_info_about_transactions(correct_path: str) -> None:
    with open(correct_path) as file:
        data = json.load(file)
    assert financial_transaction_data(correct_path) == data


def test_get_info_about_transactions_invalid(incorrect_path: str) -> None:
    assert financial_transaction_data(incorrect_path) == []

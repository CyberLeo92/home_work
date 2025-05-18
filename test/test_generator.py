import pytest

from scr.generator import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_incorrect_code_currency(transactions_for_test: list[dict]) -> None:
    filtered = filter_by_currency(transactions_for_test, "EUR")
    with pytest.raises(StopIteration):
        next(filtered)


@pytest.mark.parametrize(
    "expected_transaction",
    [
        (
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        )
    ],
)
def test_transaction_descriptions(transactions_for_test: list, expected_transaction: list) -> None:
    test_value_transaction = transaction_descriptions(transactions_for_test)
    assert list(test_value_transaction) == list(expected_transaction)


def test_incorrect_card_number_generator() -> None:
    gen = card_number_generator(1, 10000000000000000)
    with pytest.raises(ValueError) as exc_info:
        next(gen)
    assert str(exc_info.value) == "Номер карты не может содержать больше 16 цифр"

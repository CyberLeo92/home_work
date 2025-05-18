from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    И поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions(transaction_list: list) -> Iterator[dict]:
    """
    Функция-генератор принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди.
    """
    for transaction in [t["description"] for t in transaction_list]:
        yield transaction


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    start_card_number = "0000000000000000"
    nums = (num for num in range(start, stop + 1))
    for num in nums:
        card_number = start_card_number[: -len(str(num))] + str(num)
        if stop > 9999999999999999:
            raise ValueError("Номер карты не может содержать больше 16 цифр")
        else:
            yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


gen = card_number_generator(1, 8)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

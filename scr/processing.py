from datetime import datetime
from typing import Any


def filter_by_state(list_info: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция для сортировки по ключу 'state'.
    Она принимает список словарей и возвращает новый список словарей, согласно ключа 'state'.
    """
    new_list = []
    for status in list_info:
        if status["state"] == state:
            new_list.append(status)
    return new_list


def sort_by_date(list_of_values: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки даты"""
    try:
        return sorted(list_of_values, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=reverse)
    except ValueError:
        print("Данные введены неверно")
        raise  # Повторно выбрасываем исключение

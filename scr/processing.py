import re
from collections import Counter
from datetime import datetime
from typing import Any, List, Dict


def filter_by_state(list_info: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция для сортировки по ключу 'state'.
    Она принимает список словарей и возвращает новый список словарей, согласно ключа 'state'.
    """
    if not list_info:  # Проверка пустого списка
        return []
    state = state.upper()
    new_list = []
    for transaction in list_info:
        if "state" in transaction:
            if transaction["state"].upper() == state:
                new_list.append(transaction)
    return new_list


def sort_by_date(list_of_values: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция сортировки даты"""
    try:
        return sorted(list_of_values, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=reverse)
    except ValueError:
        print("Данные введены неверно")
        raise  # Повторно выбрасываем исключение


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
     Функция, которая фильтрует операции по заданной строке в описании
    (с использованием регулярных выражений)

    Параметры "data": список операция
    Параметры "search": строка для поиска
    Возвращает: отфильтрованный список операций
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = []
    for op in data:
        if 'description' in op and pattern.search((op['description'])):
            result.append(op)
    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Функция, которая подсчитывает количество операций по заданным категориям

    Параметры "data": список операция
    Параметры "categories": строка для поиска
    Возвращает: Словарь (ключ - категория: значение - количество)
    """
    category_counter = Counter()  # Счётчик
    for tx in data:
        if 'description' in tx and tx['description'] in categories:
            category_counter[tx['description']] += 1
    return dict(category_counter)

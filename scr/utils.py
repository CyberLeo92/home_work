import json
from typing import Any


def financial_transaction_data(filename: str) -> list[dict] | Any:
    """ Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(filename, encoding='utf-8') as file:
            utils_data = json.load(file)
            return utils_data
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []


if __name__ == '__main__':
    print(financial_transaction_data(r'..\data\operations.json'))

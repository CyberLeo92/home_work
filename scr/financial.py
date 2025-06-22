# Создание функционального модуля file_reader.py и теста test_file_reader.py
import csv
import logging
from typing import Any, Dict, List

import pandas as pd

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("C:/Users/Admin/PycharmProjects/home_work_leo/logs/financial.log",
                                   encoding="utf-8")
f_fo = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(f_fo)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_transactions_from_csv(file: str) -> List[Dict[str, Any]]:
    """
    Функция считывающая CSV-файл и возвращающая список словарей.

    Ожидаются столбы в файле:
        - id, state, date, amount, currency_name, currency_code, description, from, to
    Параметры файла: путь к SCV-файла
    Возвращает: список словарей с транзакциями
    Ошибки, которые обрабатываются: FileNotFoundError, KeyError, csv.Error
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            result = []
            for row in reader:
                try:
                    transaction = {
                        "id": row["id"],
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {
                            "amount": row["amount"],
                            "currency": {
                                "name": row["currency_name"],
                                "code": row["currency_code"],
                            },
                        },
                        "description": row["description"],
                        "from": row.get("from", ""),  # Если столбец может отсутствовать
                        "to": row["to"],
                    }
                    result.append(transaction)
                except KeyError as e:
                    logger.error(f"Неверная структура CSV: отсутствует столбец {e}")
                    raise
            logger.info(f"Успешно прочитан CSV-файл: {file}")
            return result
    except FileNotFoundError:
        logger.error(f"Файл {file} не найден")
        raise
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {e}")
        raise


def read_transactions_from_excel(file: str) -> List[Dict[str, Any]]:
    """
    Функция считывающая Excel-файл и возвращающая список словарей.

    Ожидаются столбы в файле:
        - id, state, date, amount, currency_name, currency_code, description, from, to
    Параметры файла: путь к Excel-файла
    Возвращает: список словарей с транзакциями
    Ошибки, которые обрабатываются: FileNotFoundError, ValueError, pd.errors.EmptyDataError
    """
    try:
        df = pd.read_excel(file)
        required_columns = [
            "id", "state", "date", "amount",
            "currency_name", "currency_code",
            "description", "from", "to"
        ]

        # Проверка наличия всех столбцов
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            logger.error(f"В файле Excel отсутствуют столбцы: {missing_columns}")
            raise ValueError(f"Отсутствуют столбцы: {missing_columns}")

        result = []
        for _, row in df.iterrows():
            transaction = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {
                        "name": row["currency_name"],
                        "code": row["currency_code"],
                    },
                },
                "description": row["description"],
                "from": row.get("from", ""),  # Если столбец может отсутствовать
                "to": row["to"],
            }
            result.append(transaction)
        logger.info(f"Успешно прочитан Excel-файл: {file}")
        return result
    except FileNotFoundError:
        logger.error(f"Файл {file} не найден")
        raise
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {e}")
        raise


if __name__ == "__main__":
    print(read_transactions_from_csv("../data/transactions.csv"))
    print(read_transactions_from_excel("../data/transactions_excel.xlsx"))
    pass

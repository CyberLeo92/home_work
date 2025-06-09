import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def currency_for_usd_or_euro(transaction: dict) -> str | None | Any:
    """Функция принимает транзакцию и возвращает ее сумму. Если в транзакции валюта не является рублями,
    то функция конвертирует ее в рубли"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        rub = "RUB"
        amounts = float(transaction["operationAmount"]["amount"])
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={currency}&amount={amounts}"

        payload = {}
        headers = {
            "apikey": API_KEY
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        try:
            if status_code != 200:
                return "Проблема с сервером"
            else:
                result = response.json()
                return result["result"]
        except requests.exceptions.RequestException as e:
            return f"Проблема с сервером: {e}"

    except Exception as e:
        print(f"Произошла ошибка с подключением {e}")
        return None


def convert_to_rub(transaction: dict) -> str | float | None | Any:
    """ Функция для обработки рублей"""
    if not isinstance(transaction, dict):
        return "Ошибка: transaction не является словарем."
    elif not transaction:
        return "Словарь пуст."
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        return currency_for_usd_or_euro(transaction)

from unittest.mock import patch

from scr.external_api import convert_to_rub, currency_for_usd_or_euro


@patch('requests.request')
def test_get_currency_usd_or_euro(mock_request):
    mock_response = mock_request.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 100.0}

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }
    result = currency_for_usd_or_euro(transaction)
    assert result == 100.0


@patch('requests.request')
def test_currency_for_usd_or_euro_error(mock_request):
    """Тест при отсутствии сети и валюта USD"""
    mock_response = mock_request.return_value
    mock_response.status_code = 500
    mock_response.json.return_value = 'Проблема с сервером'

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }
    result = currency_for_usd_or_euro(transaction)
    assert result == 'Проблема с сервером'


def test_convert_empty():
    """Тест если пустой словарь """
    transaction = {}
    result = convert_to_rub(transaction)
    assert result == "Словарь пуст."


def test_convert_to_rub_empty():
    """ Тест если transaction не словарь """
    transaction = ("amount" "10", "currency" "USD")
    result = convert_to_rub(transaction)
    assert result == "Ошибка: transaction не является словарем."

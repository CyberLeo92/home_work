import pandas as pd
import pytest


@pytest.fixture
def filter_state() -> list[dict]:
    """Данные для функций 'test_filter_by_executed' и 'test_filter_by_canceled'"""
    return [
        {"id": 816976472, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 765799246, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 123812831, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 809385983, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def incorrect_sort_date() -> list[dict]:
    """Данные для test_sort_by_date_incorrect"""
    return [{"date": "12-03-18"}]  # Некорректный формат даты


@pytest.fixture
def incorrect_check() -> str:
    """Данные для функций test_mask_account_card_incorrect_check и test_get_mask_incorrect_account"""
    return "Введен неверный номер счёта"


@pytest.fixture
def empty_data() -> str:
    """Пустые данные для функции test_mask_account_card_empty_data"""
    return "Введен неверный номер карты"


@pytest.fixture
def incorrect_date() -> str:
    """Данные для функции test_get_date_incorrect"""
    return "Неверный формат даты"


@pytest.fixture
def incorrect_card() -> str:
    """Данные для функции test_get_mask_incorrect_card"""
    return "Введен неверный номер карты"


@pytest.fixture
def transactions_for_test() -> list[dict]:
    """Данные для функций test_filter_by_currency_incorrect_code_currency и test_transaction_descriptions"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def correct_path():
    """Данные для функции test_get_info_about_transactions"""
    file = '..\\data\\operations.json'
    return file


@pytest.fixture
def incorrect_path():
    """Данные для функции test_get_info_about_transactions_invalid"""
    file = ''
    return file


@pytest.fixture
def csv_mock_data() -> str:
    """ Фикстура с mock-данными для функции test_read_csv_success """
    return """id;state;date;amount;currency_name;currency_code;description;from;to
1;EXECUTED;2023-10-01;100;USD;840;Payment;Card 1234;Account 5678
2;PENDING;2023-10-02;200;EUR;978;Transfer;;Account 9999
"""


@pytest.fixture
def excel_mock_data():
    """ Фикстура с mock-данными для функции test_read_excel_success"""
    return pd.DataFrame({
        "id": [1, 2],
        "state": ["EXECUTED", "PENDING"],
        "date": ["2023-10-01", "2023-10-02"],
        "amount": [100, 200],
        "currency_name": ["USD", "EUR"],
        "currency_code": ["840", "978"],
        "description": ["Payment", "Transfer"],
        "from": ["Card 1234", ""],
        "to": ["Account 5678", "Account 9999"],
    })

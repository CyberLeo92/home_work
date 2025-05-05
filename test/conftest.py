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
    return [{'date': '12-03-18'}]  # Некорректный формат даты


@pytest.fixture
def incorrect_check() -> str:
    """Данные для функций test_mask_account_card_incorrect_check и test_get_mask_incorrect_account
    """
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

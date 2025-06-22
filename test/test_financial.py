from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from scr.financial import read_transactions_from_csv, read_transactions_from_excel


# Тесты для CSV файла
def test_read_csv_success(csv_mock_data: str) -> None:
    """ Тест для успешного прочтения CVS файла"""
    with patch("builtins.open", mock_open(read_data=csv_mock_data)):
        result = read_transactions_from_csv("dummy_path.csv")
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["id"] == "1"
        assert result[0]["operationAmount"]["amount"] == "100"
        assert result[1]["state"] == "PENDING"


def test_read_csv_file_not_found() -> None:
    """ Тест если отсутствует CSV файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_transactions_from_csv("non_existent.csv")


def test_read_csv_missing_columns() -> None:
    """ Тест обработки отсутствия столбцов в CSV файле"""
    with patch("builtins.open", mock_open(read_data="id;state\ntest;123")):
        with pytest.raises(KeyError):
            read_transactions_from_csv("invalid.csv")


# Далее тесты для Excel файла
def test_read_excel_success(excel_mock_data) -> None:
    """ Тест для успешного прочтения Excel файла"""
    with patch("pandas.read_excel", return_value=excel_mock_data):
        result = read_transactions_from_excel("dummy_path.xlsx")
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[0]["operationAmount"]["amount"] == 100
        assert result[1]["state"] == "PENDING"


def test_read_excel_file_not_found() -> None:
    """ Тест если отсутствует Excel файла"""
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_transactions_from_excel("non_existent.xlsx")


def test_read_excel_missing_columns() -> None:
    """Тест обработки отсутствия столбцов в Excel файле"""
    with patch("pandas.read_excel", return_value=pd.DataFrame({"id": [1]})):
        with pytest.raises(ValueError):
            read_transactions_from_excel("invalid.xlsx")


# Тесты с реальными файлами:
def test_real_csv_file() -> None:
    """Опциональный тест с CSV файлом"""
    import os
    if os.path.exists("../data/transactions.csv"):
        result = read_transactions_from_csv("../data/transactions.csv")
        assert isinstance(result, list)


def test_real_excel_file() -> None:
    """Опциональный тест с CSV файлом"""
    import os
    if os.path.exists("../data/transactions_excel.xlsx"):
        result = read_transactions_from_excel("../data/transactions_excel.xlsx")
        assert isinstance(result, list)

import os
import tempfile

import pytest

from scr.decorators import log


@log()
def function_for_test(x, y):
    return x + y


def test_log():
    with pytest.raises(TypeError, match="Неверно переданы аргументы"):
        function_for_test()


def test_log_capsys(capsys):
    function_for_test(1, 3)
    captured = capsys.readouterr()
    assert captured.out == "function_for_test ok\n"


@log(filename="mylog.txt")
def test_file_func(x, y):  # для нижнего тестирования
    return x + y


def test_log_file_with_capsys(capsys):
    """
    тест с использованием capsys для декоратора ниже с проверкой записи в файл mylog.txt
    """
    with tempfile.NamedTemporaryFile(delete=False) as tmp:  # Нужно, чтоб создать временный файл
        tmp_name = tmp.name
    try:
        test_file_func(1, 2)
        with open("mylog.txt") as f:
            content = f.read()
        assert "test_file_func ok" in content
        captured = capsys.readouterr()
        assert captured.out == ""
    finally:
        if os.path.exists("mylog.txt"):
            os.unlink("mylog.txt")

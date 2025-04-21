"""
Для тестов функций
"""


def get_date(full_date: str) -> str:
    """
    Функция, которая показывает корректно дату
    """
    only_data = full_date.split("T")
    correct_data = only_data[0].split("-")
    return ".".join(correct_data[::-1])


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))

from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор способен выводить логи в консоль и в случае передачи
    необязательного аргумента filename, записывать логи в указанный файл
    """

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> Any:
    return x + y


print(my_function(4, 5))

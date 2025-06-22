import json
import logging
from typing import Any

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('C:/Users/Admin/PycharmProjects/home_work_leo/logs/utils.log',
                                   encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def financial_transaction_data(filename: str) -> list[dict] | Any:
    """ Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info('Производиться поиск файла для чтения')
        with open(filename, encoding='utf-8') as file:
            utils_data = json.load(file)
            if type(utils_data) is not list:
                logger.error('Ошибка TypeError')
            logger.info(f'Успешно загружено {len(utils_data)} записей из файла {filename}')
            return utils_data
    except FileNotFoundError as ex:
        logger.error(f'Ошибка {ex}]')
        print("Файл не найден")
        return []
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка {ex}]')
        print("Ошибка декодирования файла")
        return []
    finally:
        logger.info('Завершение работы')
        return None


if __name__ == '__main__':
    print(financial_transaction_data(r'..\data\operations.json'))

import logging

logger = logging.getLogger('masks')
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты
    в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    logger.info('Проверяем точно ли введенные данные карты ровны 16 символам')
    if len(card_number) == 16 and card_number.isdigit():
        logger.info(f'Успешно создана маска для карты: {card_number[:4]} **** **** {card_number[12:]}')
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.error('Введен неверный номер карты"')  # Введенные данные не корректны
        return ""


if __name__ == '__main__':
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_card_number("8990922113665229"))


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX
    """
    logger.info('Проверяем точно ли введенные номера счета ровны 20 символам')
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        logger.error('Введен неверный номер счёта')
        return "Введен неверный номер счёта"


if __name__ == '__main__':
    print(get_mask_account("73654108430135874305"))

def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты
    в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    if len(card_number) == 16:
        if card_number.isdigit():
            return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        else:
            return "Введен неверный номер карты"
    else:
        return "Введен неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX
    """
    if len(account_number) == 20:
        if account_number.isdigit():
            return f"**{account_number[-4:]}"
        else:
            return "Введен неверный номер счёта"
    else:
        return "Введен неверный номер счёта"

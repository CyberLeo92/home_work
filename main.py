from scr.masks import get_mask_account, get_mask_card_number


def main() -> None:
    """
    Функция:
    запрашивает у пользователя номер карты
    скрывает номер карту
    запрашивает у пользователя номер счёта
    скрывает номер счёта
    """
    # Запрашивает номер карты
    user_card_number = input("Введите номер карты: ")
    hide_number_card = get_mask_card_number(user_card_number)

    # Запрашивает номер счёта
    user_score_number = input("Введите номер счёта: ")
    hide_number_score = get_mask_account(user_score_number)

    print(hide_number_card, hide_number_score, sep="\n")


if __name__ == "__main__":
    main()

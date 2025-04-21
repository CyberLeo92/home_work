from scr.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """
    Функция обрабатывает информацию как о картах и о счетах.
    """
    card_info_split = card_info.split()
    if "Счет" in card_info_split:
        return f"Cчет {get_mask_account(card_info_split[1])}"
    else:
        card_num = []
        payment_system = []  # платёжная система Visa/Maestro и т.д.
        for info in card_info_split:
            if info.isdigit():
                card_num.append(info)
            if info.isalpha():
                payment_system.append(info)
        str_card_num = " ".join(card_num)
        str_payment_system = " ".join(payment_system)
        return f"{str_payment_system} {get_mask_card_number(str_card_num)}"


if __name__ == "__main__":
    print(mask_account_card(str("Maestro 7000792289606361")))
    print(mask_account_card(str("Счет 73654108430135874305")))


def get_date(full_date: str) -> str:
    """
    Функция, которая показывает корректно дату
    """
    only_data = full_date.split("T")
    correct_data = only_data[0].split("-")  # если понадобиться только время в будущих д/з only_data[1] + split(".")
    return ".".join(correct_data[::-1])


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))

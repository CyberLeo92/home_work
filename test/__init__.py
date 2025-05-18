"""
Для тестов функций
"""

# from scr.masks import get_mask_account
#
#
# def mask_account_card(card_info: str) -> str:
#     """
#     Функция обрабатывает информацию как о картах и о счетах.
#     """
#     card_info_split = card_info.split()
#     if "Счет" in card_info_split:
#         if len(card_info_split[1]) == 20 and card_info_split[1].isdigit():
#             return f"Счет {get_mask_account(card_info_split[1])}"
#         else:
#             return "Введен неверный номер счёта"
#
#
#
# if __name__ == "__main__":
#     print(mask_account_card(str("Счет 12312312312131223sd3")))

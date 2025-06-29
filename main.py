from scr import processing, utils, widget
from scr.masks import get_mask_account, get_mask_card_number


def main_old() -> None:
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


def main():
    print("""Привет! Добро пожаловать в программу работу с банковскими транзакциями.
Выберите необходимый пункт меню:
   1. Получить информацию о транзакциях из JSON-файла
   2. Получить информацию о транзакциях из CSV-файла
   3. Получить информацию о транзакциях из XLSX-файла""")

    # Загрузка данных
    while True:
        choice = input("Ваш выбор: ").strip()

        if choice in ("1", "2", "3"):
            break
        print("Введен некорректный пункт. Пожалуйста, выберите 1, 2 или 3.")

    transactions = []
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = utils.financial_transaction_data(
            "C:/Users/Admin/PycharmProjects/home_work_leo/data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = utils.financial_transaction_data(
            "C:/Users/Admin/PycharmProjects/home_work_leo/data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = utils.financial_transaction_data(
            "C:/Users/Admin/PycharmProjects/home_work_leo/data/transactions_excel.xlsx")

    valid_states = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Ваш выбор: "
        ).upper().strip()

        if state in valid_states:
            print(f"Операции отфильтрованы по статусу '{state}'")
            filtered_transactions = processing.filter_by_state(transactions, state)
            break
        else:
            print(f"Статус операции '{state}' недоступен.")

    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").lower().strip()
    if sort_choice in {"да", "yes"}:
        while True:
            direction = input("Сортировать по убыванию? (Да/Нет): ").lower().strip()

            if direction in {"да", "yes"}:
                reverse = True
                break
            elif direction in {"нет", "no"}:
                reverse = False
                break
            else:
                print("Пожалуйста, введите 'Да' или 'Нет'.")

        filtered_transactions = processing.sort_by_date(filtered_transactions, reverse)

    # Фильтрация рублевых транзакций
    rub_only = input("Выводить только рублевые транзакции? (Да/Нет): ").lower().strip()
    if rub_only in {"да", "yes", "y"}:
        filtered_transactions = [tx for tx in filtered_transactions
                                 if tx["operationAmount"]["currency"]["code"] == "RUB"]

    # Фильтрация по ключевому слову
    keyword_filter = input(
        "Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").lower().strip()
    if keyword_filter in {"да", "yes", "y"}:
        keyword = input("Введите слово для поиска в описании: ").strip()
        filtered_transactions = processing.process_bank_search(filtered_transactions, keyword)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}\n")
    for tx in filtered_transactions:
        date_str = widget.get_date(tx["date"])
        description = tx.get("description", "Без описания")

        from_info = widget.mask_account_card(tx.get("from", "")) if tx.get("from") else ""
        to_info = widget.mask_account_card(tx.get("to", ""))

        amount = tx["operationAmount"]["amount"]
        currency = tx["operationAmount"]["currency"]["code"]

        print(f"{date_str} {description}")
        if from_info:
            print(f"{from_info} -> {to_info}")
        else:
            print(f"{to_info}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()

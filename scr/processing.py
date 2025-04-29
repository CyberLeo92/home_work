def filter_by_state(list_info: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Функция сортировки по ключу 'state'
    """
    new_list = []
    for status in list_info:
        if status['state'] == state:
            new_list.append(status)
    return new_list


def sort_by_date(list_info: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция сортировки даты
    """
    return sorted(list_info, key=lambda item: item['date'], reverse=reverse)

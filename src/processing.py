from datetime import datetime


def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрации по статусу операции"""
    result = []

    for i in data:
        if i["state"] == state:
            result.append(i)
    return result


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки элементов списка по дате"""
    sorted_dict = sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_dict

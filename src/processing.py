from datetime import datetime

def filter_by_state(data, state='EXECUTED') -> list:
    """Функция, которая принимает список словарей и
    опционально значение для ключа state"""
    operation_executed = []
    operation_canceled = []

    for i in data:
        if i["state"] == "CANCELED":
            operation_canceled.append(i)
            return operation_canceled
        elif i["state"] == "EXECUTED":
            operation_executed.append(i)
            return operation_executed



def sort_by_date(data, reverse=True) -> list:
    """Функция, которая принимает список словарей и
    необязательный параметр, задающий порядок сортировки"""
    sorted_dict = sorted(data, key=lambda  x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_dict

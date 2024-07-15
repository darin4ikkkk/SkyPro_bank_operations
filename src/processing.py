from typing import Optional


def filter_by_state(data: list, state_key: Optional[str] = "EXECUTED") -> list:
    """Отсортировывает только успешные операции"""
    executed = []
    for item in data:
        key = item.get('state')
        if key == state_key:
            executed.append(item)
    return executed


def sort_key(data: dict) -> str:
    """Получает дату из словаря по ключу 'date'"""
    return data.get('date')


def sort_by_date(data: list, reverse_key: Optional[bool] = True) -> list:
    """Сортирует операции по дате"""
    sorted_operations = sorted(data, key=sort_key, reverse=reverse_key)
    return sorted_operations

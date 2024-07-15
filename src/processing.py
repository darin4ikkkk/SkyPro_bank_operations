from typing import Optional

def filter_by_state(data: list, state_key: Optional[str] = "EXECUTED") -> list:
    "Отсортировывает только успешные операции"
    executed = []
    for item in data:
        key = item.get('state')
        if key == state_key:
            executed.append(item)
    return executed



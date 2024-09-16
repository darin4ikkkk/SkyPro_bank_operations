from functools import wraps
from datetime import time


def log(filename=None):
    """Запись вызова функции и её результата в файл или консоль"""
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{func.__name__} OK / time_start = {time_1}, time_end = {time_2}")
                else:
                    print(f"{func.__name__} OK / time_start = {time_1}, time_end = {time_2}")
            except Exception as e:
                if filename:
                    time_2 = time()
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs} / time_start = {time_1}, time_end = {time_2}")
                else:
                    time_2 = time()
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs} / time_start = {time_1}, time_end = {time_2}")
            return result
        return wrapper
    return my_decorator








from functools import wraps


def log(filename=None):
    """Запись вызова функции и её результата в файл или консоль"""
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{func.__name__} OK")
                else:
                    print(f"{func.__name__} OK")
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            return result
        return wrapper
    return my_decorator








import pytest
import os
from src.decorators import log


@log()
def my_function_console(x: int, y: int):
    """Функция для проверки работы декоратора log (вывод в консоль)"""
    return x/y

filename = "/Users/darinasmirnova/PycharmProjects/SkyPro91/logs/my_log.txt"
@log(filename)
def my_function_file(x: int, y: int):
    """Функция для проверки работы декоратора log (запись в файл)"""
    return x/y


def test_dec_log_console_ok(capsys):
    my_function_console(2, 1)
    captured = capsys.readouterr()
    assert captured.out == 'my_function_console OK\n'

def test_dec_log_file_ok():
    my_function_file(2, 1)
    with open(filename, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert 'my_function_file OK' in logs

def test_dec_log_console_error(capsys):
    my_function_console(2, 0)
    captured = capsys.readouterr()
    assert captured.out == 'my_function_console error: division by zero. Inputs: (2, 0), {}\n'

    my_function_console(2, '1')
    captured = capsys.readouterr()
    assert captured.out == "my_function_console error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (2, '1'), {}\n"

def test_dec_log_file_error():
    my_function_file(2, 0)
    with open(filename, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert 'my_function_file error: division by zero. Inputs: (2, 0), {}' in logs


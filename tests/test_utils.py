import os

from unittest.mock import patch

import pytest

from src.utils import load_transactions, transaction_amount


@pytest.fixture
def path():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return path_to_file


@pytest.fixture
def path_empty_list():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return path_to_file


@pytest.fixture
def path_mistake_json():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_2.json")
    return path_to_file


@pytest.fixture
def transaction():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
         "amount": "31957.58",
         "currency": {
          "name": "руб.",
          "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


@pytest.fixture
def transaction_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_nofile():
    assert load_transactions('nofile') == []


def test_financial_transactions(path):
    assert load_transactions(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
             "name": "руб.",
             "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_empty_list(path_empty_list):
    assert load_transactions(path_empty_list) == []


def test_financial_transactions_mistake_json(path_mistake_json):
    assert load_transactions(path_mistake_json) == []


def test_transaction_amount(transaction):
    assert transaction_amount(transaction) == '31957.58'


@patch('src.utils.currency_conversion')
def test_transaction_amount_non_rub(mock_currency_conversion, transaction_1):
    mock_currency_conversion.return_value = 1000.0
    assert transaction_amount(transaction_1) == 1000.0
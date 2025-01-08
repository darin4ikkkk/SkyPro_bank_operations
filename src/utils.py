import json
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion


def load_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                transactions = json.load(file)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        return []


def transaction_amount(transaction: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
    else:
        amount = currency_conversion(transaction)
    return amount



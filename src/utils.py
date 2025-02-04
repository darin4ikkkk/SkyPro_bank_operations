import json, logging
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion


logger = logging.getLogger("utils")

file_handler = logging.FileHandler("../logs/utils_log.log")
file_formatter = logging.Formatter("%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info("Открываю файл с транзакциями")
        with open(path, encoding="utf-8") as file:
            try:
                transactions = json.load(file)
            except JSONDecodeError:
                logger.error("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            logger.error("Список транзакций пуст")
            return []
        logger.info("Создан список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        logger.error("Файл с транзакциями не найден")
        return []


def transaction_amount(transaction: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
        logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(transaction)
        logger.info("Код валюты транзакции не RUB, произведена конвертация")
    return amount



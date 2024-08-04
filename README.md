# SkyPro_bank_operations

## Описание:

**SkyPro_bank_operations - это виджет, который выводит 5 последних успешных банковских операций**

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/darin4ikkkk/SkyPro_bank_operations.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте проект в IDE, например, PyCharm.
2. Запустите модуль main.py.

### Модуль generators.py
модуль generators содержит функции\
для работы с массивами транзакций

функция filter_by_currency принимает на вход список словарей, представляющих транзакции\
и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).

генератор transaction_descriptions принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

генератор card_number_generator выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, 
где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.


## Тестирование
Наш проект покрыт unit-тестами Pytest. 

Для их запуска выполните команду:
```
pytest
```


## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

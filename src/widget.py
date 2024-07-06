from datetime import date

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_acc_num: str) -> str:
    """Маскирует и номер карты и номер счёта"""
    if "Счет" in card_or_acc_num:
        return get_mask_account(card_or_acc_num)
    else:
        return get_mask_card_number(card_or_acc_num)


def get_date(orig_date: str) -> str:
    """Форматирует дату"""
    thedate = date.fromisoformat(orig_date[:10])
    date_formatted = thedate.strftime("%d.%m.%Y")  # День Месяц Год
    return date_formatted




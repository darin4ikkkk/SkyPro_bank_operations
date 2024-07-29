from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert get_mask_card_number("Maestro 7010792289606861") == "Maestro 7010 79** **** 6861"
    assert get_mask_card_number("7010791281606161") == "7010 79** **** 6161"
    assert get_mask_card_number("") == "Отсутствует номер"


def test_get_mask_account():
    assert get_mask_account("Счет 73654108430135874305") == "Счет **4305"
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("") == "Отсутствует номер"

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 7010792289606861") == "Maestro 7010 79** **** 6861"
    assert mask_account_card("7010791281606161") == "7010 79** **** 6161"

    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

    assert mask_account_card("") == "Отсутствует номер"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-03-11") == "11.03.2024"
    assert get_date("") == "Дата отсутствует"

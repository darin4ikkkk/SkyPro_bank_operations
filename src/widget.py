from masks import get_mask_card_number, get_mask_account
def mask_account_card(card_or_acc_num: str) -> str:
    if "Счет" in card_or_acc_num:
        return get_mask_account(card_or_acc_num)
    else:
        return get_mask_card_number(card_or_acc_num)


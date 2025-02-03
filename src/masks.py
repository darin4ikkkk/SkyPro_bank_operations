def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты"""
    len_num = len(card_num)
    if len_num > 0:
        card_num_mask = card_num.replace(card_num[(len_num - 10) : (len_num - 4)], "** **** ")
        new_len = len(card_num_mask)
        num_list = list(card_num_mask)
        num_list[new_len - 15] = card_num_mask[new_len - 15] + " "
        card_num_masked = "".join(num_list)

        return card_num_masked
    return "Отсутствует номер"


def get_mask_account(acc_num: str) -> str:
    """Маскирует номер счёта"""
    len_num = len(acc_num)
    if len_num > 0:
        acc_num_masked = acc_num.replace(acc_num[(len_num - 20) : (len_num - 4)], "**")
    else:
        return "Отсутствует номер"

    return acc_num_masked


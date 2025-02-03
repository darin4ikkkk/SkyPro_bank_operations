import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename = "../logs/masks_log.log",
    filemode = "w",
    )
card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()

def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты"""
    card_number_logger.info("Создаю маску номера карты")
    len_num = len(card_num)
    if len_num > 0:
        card_num_mask = card_num.replace(card_num[(len_num - 10) : (len_num - 4)], "** **** ")
        new_len = len(card_num_mask)
        num_list = list(card_num_mask)
        num_list[new_len - 15] = card_num_mask[new_len - 15] + " "
        card_num_masked = "".join(num_list)
        card_number_logger.info("Маска номера карты создана")
        return card_num_masked
    card_number_logger.error("Неправильный номер карты")
    return "Отсутствует номер"


def get_mask_account(acc_num: str) -> str:
    """Маскирует номер счёта"""
    mask_account_logger.info("Создаю маску номера счета")
    len_num = len(acc_num)
    if len_num > 0:
        acc_num_masked = acc_num.replace(acc_num[(len_num - 20) : (len_num - 4)], "**")
        mask_account_logger.info("Маска номера счета создана")
    else:
        mask_account_logger.error("Неправильный номер счета")
        return "Отсутствует номер"
    return acc_num_masked


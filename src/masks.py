import logging


logger = logging.getLogger("mask")

file_handler = logging.FileHandler("../logs/masks_log.log")
file_formatter = logging.Formatter("%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты"""
    logger.info("Создаю маску номера карты")
    len_num = len(card_num)
    if len_num > 0:
        card_num_mask = card_num.replace(card_num[(len_num - 10) : (len_num - 4)], "** **** ")
        new_len = len(card_num_mask)
        num_list = list(card_num_mask)
        num_list[new_len - 15] = card_num_mask[new_len - 15] + " "
        card_num_masked = "".join(num_list)
        logger.info("Маска номера карты создана")
        return card_num_masked
    logger.error("Неправильный номер карты")
    return "Отсутствует номер"


def get_mask_account(acc_num: str) -> str:
    """Маскирует номер счёта"""
    logger.info("Создаю маску номера счета")
    len_num = len(acc_num)
    if len_num > 0:
        acc_num_masked = acc_num.replace(acc_num[(len_num - 20) : (len_num - 4)], "**")
        logger.info("Маска номера счета создана")
    else:
        logger.error("Неправильный номер счета")
        return "Отсутствует номер"
    return acc_num_masked


from enum import Enum


class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_CHOOSE_CITY = "1"
    S_CHOOSE_CATEGORY = "2"
    S_TEST = "3"
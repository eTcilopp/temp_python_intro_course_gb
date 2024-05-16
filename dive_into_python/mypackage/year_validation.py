"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from datetime import datetime

__all__ = ['date_is_valid']


def date_is_valid(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def _is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print(date_is_valid(sys.argv[1]))
    else:
        print("Invalid arguments")

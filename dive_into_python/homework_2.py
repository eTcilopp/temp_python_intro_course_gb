"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def get_hex(num: int, hex_num_res: str = '') -> str:
    hex_digits = '0123456789abcdef'
    if not num:
        return f'0x{hex_num_res if hex_num_res else 0}'
    hex_num_res = str(hex_digits[num % 16]) + hex_num_res
    return get_hex(num // 16, hex_num_res)


assert get_hex(100) == hex(100)
assert get_hex(1000) == hex(1000)
assert get_hex(5) == hex(5)
assert get_hex(321) == hex(321)
assert get_hex(0) == hex(0)
assert get_hex(12340) == hex(12340)

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""

import fractions


def my_fraction_sum_and_mul(a: str, b: str) -> str:
    def find_common_divisor(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    dividend_a, divisor_a = [int(el) for el in a.split('/')]
    dividend_b, divisor_b = [int(el) for el in b.split('/')]

    sum_dividend = divisor_b * dividend_a + divisor_a * dividend_b
    sum_divisor = divisor_a * divisor_b
    cd = find_common_divisor(sum_dividend, sum_divisor)
    frac_sum = f'{int(sum_dividend/cd)}/{int(sum_divisor/cd)}'

    mul_dividend = dividend_a * dividend_b
    mul_divisor = divisor_a * divisor_b
    cd = find_common_divisor(mul_dividend, mul_divisor)
    frac_mul = f'{int(mul_dividend/cd)}/{int(mul_divisor/cd)}'

    return frac_sum, frac_mul


assert my_fraction_sum_and_mul("1/2", "1/3") == (str(fractions.Fraction(1, 2) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 2) * fractions.Fraction(1, 3)))
assert my_fraction_sum_and_mul("1/4", "1/3") == (str(fractions.Fraction(1, 4) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 4) * fractions.Fraction(1, 3)))
assert my_fraction_sum_and_mul("1/5", "1/3") == (str(fractions.Fraction(1, 5) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 5) * fractions.Fraction(1, 3)))
assert my_fraction_sum_and_mul("1/6", "1/3") == (str(fractions.Fraction(1, 6) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 6) * fractions.Fraction(1, 3)))
assert my_fraction_sum_and_mul("1/7", "1/3") == (str(fractions.Fraction(1, 7) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 7) * fractions.Fraction(1, 3)))
assert my_fraction_sum_and_mul("1/8", "1/3") == (str(fractions.Fraction(1, 8) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 8) * fractions.Fraction(1, 3)))
assert my_fraction_sum_and_mul("1/9", "1/3") == (str(fractions.Fraction(1, 9) + fractions.Fraction(1, 3)), str(fractions.Fraction(1, 9) * fractions.Fraction(1, 3)))

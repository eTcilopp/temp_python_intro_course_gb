"""
Задача 2
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def analyze_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return "Треугольник не существует"
    elif a == b == c:
        return "Треугольник равносторонний"
    elif a == b or a == c or b == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"


assert analyze_triangle(3, 4, 8) == "Треугольник не существует"
assert analyze_triangle(3, 3, 3) == "Треугольник равносторонний"
assert analyze_triangle(3, 3, 4) == "Треугольник равнобедренный"
assert analyze_triangle(3, 4, 6) == "Треугольник разносторонний"
assert analyze_triangle(1, 4, 6) == "Треугольник не существует"

"""
Задача 3
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def is_prime(n):
    if n < 0 or n > 100000:
        raise ValueError("Число должно быть в диапазоне от 0 до 100000")
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


assert is_prime(0) is False
assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(5) is True
assert is_prime(123) is False

"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def guess_number(lower_limit=LOWER_LIMIT, upper_limit=UPPER_LIMIT):
    print(f"Угадайте число от {lower_limit} до {upper_limit}")
    num = randint(lower_limit, upper_limit)
    for i in range(10):
        guess = int(input("Введите число: "))
        if guess < num:
            print("Больше")
        elif guess > num:
            print("Меньше")
        else:
            return "Вы угадали!"
    return f"Вы проиграли! Загаданное число: {num}"


print(guess_number())

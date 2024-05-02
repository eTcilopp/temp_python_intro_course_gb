"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def get_file_info(
    file_path_wirth_file_name_and_extension: str
        ) -> tuple[str, str, str]:
    *file_path_elements, file_name_with_extension =\
        file_path_wirth_file_name_and_extension.split('\\')
    file_path = '\\'.join(file_path_elements)
    file_name, file_extension = file_name_with_extension.split('.')
    return file_path, file_name, file_extension


assert get_file_info(r"C:\Users\UserDocuments\Lightshot\file.exe") == ("C:\\Users\\UserDocuments\\Lightshot", "file", "exe")


"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""


def get_one_line_generator(*args):
    return {name: salary * float(premium[:-1]) / 100 for name, salary, premium in zip(*args)}


assert get_one_line_generator(
    ['Alice', 'Bob', 'Charlie'], [1000, 2000, 3000], ['10%', '20%', '30%']
    ) == {'Alice': 100.0, 'Bob': 400.0, 'Charlie': 900.0}


"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = iter(fibonacci())
for i in range(10):
    print(next(fibonacci))

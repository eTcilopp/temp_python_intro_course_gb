'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''

n = 5
x = 1

res = len([el for el in range(1, n+1) if el == x])

print(f'-> {res}') ## 1
# Признаться, не понял задачу: исходя из условия, число X всегда должно встречаться один или ноль раз 

'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5

'''
n = 5
x = 6

dict_arr = {abs(x-el): el for el in range(1, n+1)}
res = dict_arr[min(dict_arr.keys())]
print(f'-> {res}')

'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12

'''
WEIGHT_DICT = {
    'A, E, I, O, U, L, N, S, T, R': 1,
    'D, G': 2,
    'B, C, M, P': 3,
    'F, H, V, W, Y': 4,
    'K': 5,
    'J, X': 8,
    'Q, Z': 10,
    'А, В, Е, И, Н, О, Р, С, Т': 1,
    'Д, К, Л, М, П, У': 2,
    'Б, Г, Ё, Ь, Я': 3,
    'Й, Ы ': 4, 
    'Ж, З, Х, Ц, Ч': 5,
    'Ш, Э, Ю': 8,
    'Ф, Щ, Ъ': 10
}

def get_weight(word):
    return sum([[v for k, v in WEIGHT_DICT.items() if letter.lower() in k.lower()][0] for letter in word])

word = 'ноутбук'
print(get_weight(word))
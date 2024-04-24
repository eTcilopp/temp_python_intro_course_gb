"""
1. Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

def get_duplicates(inbound_list: list) -> list:
    return [el for el in set(inbound_list) if inbound_list.count(el) > 1]

assert get_duplicates([1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3]
assert get_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]) == []
assert get_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
assert get_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1]


"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""


def get_most_frequent_symbols(text: str, n: int = 10) -> list:
    if n == 0:
        return []
    frequency_dict = {}
    for symbol in text:
        if symbol.isalpha():
            symbol = symbol.lower()
            frequency_dict[symbol] = frequency_dict.get(symbol, 0) + 1
    return list(dict(sorted(frequency_dict.items(), key=lambda item: item[1])))[-n:]

assert sorted(get_most_frequent_symbols('abracadabra')) == sorted(['a', 'b', 'r', 'c', 'd'])
assert sorted(get_most_frequent_symbols('abracadabra', 3)) == sorted(['a', 'b', 'r'])
assert sorted(get_most_frequent_symbols('abracadabra', 2)) == sorted(['a', 'r'])
assert sorted(get_most_frequent_symbols('abracadabra', 1)) == sorted(['a'])
assert sorted(get_most_frequent_symbols('abracadabra', 0)) == sorted([])
larger_text = """
Wikipedia[note 3] is a free content online encyclopedia written and maintained by a community of volunteers,
known as Wikipedians, through open collaboration and the use of the wiki-based editing system MediaWiki.
Wikipedia is the largest and most-read reference work in history.[3][4] It is consistently ranked as one of the ten
most popular websites in the world, and as of 2024 is ranked the fifth most visited website on the Internet by
Semrush,[5] and second by Ahrefs.[6] Founded by Jimmy Wales and Larry Sanger on January 15, 2001,
Wikipedia is hosted by the Wikimedia Foundation, an American nonprofit organization that employs a staff of over 700 people.[7]
"""

print(get_most_frequent_symbols(larger_text, 10))

"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант
"""


def get_backpack_items(backpack_stuff: dict, max_load_capacity: int) -> dict:
    number_of_items = len(backpack_stuff.items())
    all_stuff = '0b' + '1' * number_of_items
    result = set()
    item_list = list(backpack_stuff.keys())
    for combination in range(int(all_stuff, 2), 1, -1):
        bool_list = [bool(int(el)) for el in list(format(combination, f'0{number_of_items}b'))]
        load_variant = [item for item, is_true in zip(item_list, bool_list) if is_true]
        total_item_weight = sum([backpack_stuff.get(item) for item in load_variant])
        if total_item_weight > max_load_capacity:
            continue
        try:
            smallest_value = min(v for k, v in backpack_stuff.items() if k not in load_variant)
        except ValueError:
            return load_variant
        if max_load_capacity - total_item_weight > smallest_value:
            continue
        result.add(tuple(sorted(load_variant)))
    return result
stuff_in_backpack = {
    "тент": 1.5,
    "спальник": 2.0,
    "палатка": 3.0,
    "термос": 0.5,
    "еда (консервы)": 1.2,
    "вода (литр)": 1.0,
    "печка для готовки": 0.8,
    "кастрюля": 0.7,
    "посуда (набор)": 1.0,
    "палочки для хождения": 1.2,
    "первая помощь (набор)": 0.5,
    "фонарик": 0.3,
    "карта местности": 0.2,
    "компас": 0.1,
    "запасные батарейки": 0.2,
    "нож": 0.4,
    "средство от комаров": 0.3,
    "зубная щетка и паста": 0.2,
    "запасной телефон (с зарядкой)": 0.5,
    "подушка для сна": 0.8
}



print(*get_backpack_items(stuff_in_backpack, 15.0))

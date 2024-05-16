import random


def queens_are_safe(queen_coords: list[int]) -> bool:
    for i in range(len(queen_coords)):
        for j in range(i + 1, len(queen_coords)):
            if (queen_coords[i][0] == queen_coords[j][0] or
                queen_coords[i][1] == queen_coords[j][1] or
                abs(queen_coords[i][0] - queen_coords[j][0]) == abs(queen_coords[i][1] - queen_coords[j][1])):
                return False
    return True


def generate_random_pairs(num_pairs=8):
    pairs = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(num_pairs)]
    return pairs


def find_safe_positions(num_pairs=8):
    while True:
        queens_positions = generate_random_pairs(num_pairs)
        if queens_are_safe(queens_positions):
            return queens_positions

""" Найденные решения:
[(2, 8), (3, 1), (4, 5), (1, 4), (8, 3), (5, 7), (6, 2), (7, 6)]
[(2, 5), (5, 3), (8, 4), (3, 7), (6, 8), (1, 2), (4, 1), (7, 6)]
[(3, 7), (1, 6), (5, 8), (4, 1), (2, 4), (7, 5), (8, 3), (6, 2)]
[(8, 5), (4, 7), (1, 2), (2, 6), (6, 8), (3, 1), (5, 4), (7, 3)]
"""

